(* Development-only JSON formatting; the execution meter is observed, never charged. *)
let quote s =
  let buffer = Buffer.create (String.length s) in
  Buffer.add_char buffer '"';
  let rec copy i =
    if i < String.length s then begin
      let next = match s.[i] with
        | '"' -> Buffer.add_string buffer "\\\""; i + 1
        | '\\' -> Buffer.add_string buffer "\\\\"; i + 1
        | '\b' -> Buffer.add_string buffer "\\b"; i + 1
        | '\012' -> Buffer.add_string buffer "\\f"; i + 1
        | '\n' -> Buffer.add_string buffer "\\n"; i + 1
        | '\r' -> Buffer.add_string buffer "\\r"; i + 1
        | '\t' -> Buffer.add_string buffer "\\t"; i + 1
        | '\000' .. '\031' as c -> Printf.bprintf buffer "\\u%04x" (Char.code c); i + 1
        | '\032' .. '\127' as c -> Buffer.add_char buffer c; i + 1
        | _ ->
            let u = String.get_utf_8_uchar s i in
            let n = Uchar.utf_decode_length u in
            if Uchar.utf_decode_is_valid u then Buffer.add_substring buffer s i n
            else Buffer.add_string buffer "\\ufffd";
            i + n
      in copy next
    end
  in
  copy 0;
  Buffer.add_char buffer '"';
  Buffer.contents buffer

let obj fields =
  "{" ^ String.concat "," (List.map (fun (name, value) -> quote name ^ ":" ^ value) fields) ^ "}"
let strings fields = obj (List.map (fun (name, value) -> name, quote value) fields)
let optional render = function None -> "null" | Some x -> render x
let integer n = quote (string_of_int n)
let natural n = quote (Natural.to_decimal n)
let host_limit digits = Option.value (int_of_string_opt digits) ~default:max_int

type location = { definition : int option; path : int list option; offset : int option }
let nowhere = { definition = None; path = None; offset = None }

type context = {
  mutable name : string option;
  mutable entry_index : int option;
  mutable argument : string option;
  mutable budget : string option;
  mutable source_limit : string;
  mutable value_limit : string;
  mutable source_bytes : int option;
  mutable source_sha256 : string option;
  mutable entry_attempted : bool;
  mutable meter : Eval.location Meter.t option;
}

let context () =
  let default = Natural.to_decimal Reader.default_source_limit in
  { name = None; entry_index = None; argument = None; budget = None;
    source_limit = default; value_limit = default; source_bytes = None; source_sha256 = None; entry_attempted = false; meter = None }

let mark_entry_attempt state () = state.entry_attempted <- true

type status = Returned | Out_of_fuel | Refused | Tool_error
type outcome = {
  status : status; code : string; at : location; invoice : Meter.invoice option;
  value : string option; facts : (string * string) list;
}

let outcome ?(at = nowhere) ?invoice ?value ?(facts = []) status code =
  { status; code; at; invoice; value; facts }

let exit_code = function Returned -> 0 | Out_of_fuel -> 2 | Refused -> 3 | Tool_error -> 4
let status_name = function
  | Returned -> "returned" | Out_of_fuel -> "out_of_fuel"
  | Refused -> "refused" | Tool_error -> "tool_error"

let stopped (stop : Eval.location Meter.stop) =
  let site = stop.Meter.at in
  let at = { definition = Some (Eval.definition_index site); path = Eval.expression_path site;
             offset = Eval.source_offset site } in
  let primitive = function Checker.Add -> "add" | Checker.Sub -> "sub" | Checker.Mul -> "mul" in
  let event, extra = match stop.Meter.failed_event with
    | Meter.Structural Meter.Entry -> "entry", []
    | Meter.Structural Meter.Literal -> "literal", []
    | Meter.Structural Meter.Variable -> "variable", []
    | Meter.Structural Meter.Call -> "call", []
    | Meter.Structural Meter.Return -> "return", []
    | Meter.Tuple -> "tuple", []
    | Meter.Arithmetic op -> primitive op, []
    | Meter.Wrong_kind op -> "wrong-kind", ["operation", primitive op]
  in
  let invoice, reason = match stop.Meter.cause with
    | Meter.Insufficient invoice -> Some invoice, []
    | Meter.Bound_unavailable text -> None, ["reason", text]
  in
  let facts = ["event", event; "failed_operation_debit", Natural.to_decimal stop.Meter.failed_operation_debit] @ extra @ reason in
  outcome ~at ?invoice ~facts Out_of_fuel (Meter.stop_code stop.Meter.cause)

let encode state result =
  let inv (i : Meter.invoice) =
    obj ["A", natural i.Meter.a; "R", natural i.Meter.r; "T", natural i.Meter.t; "W", natural i.Meter.w; "total", natural i.Meter.total]
  in
  let path xs = "[" ^ String.concat "," (List.map integer xs) ^ "]" in
  let used, remaining = match state.meter with
    | None -> "0", state.budget
    | Some m ->
        let a = Meter.accounting m in
        Natural.to_decimal a.Meter.used, Some (Natural.to_decimal a.Meter.remaining)
  in
  obj ["schema", quote "loom-b-report/1-candidate"; "status", quote (status_name result.status);
       "code", quote result.code; "profile", quote "milestone-b-forms/1-candidate";
       "meter", quote "milestone-b-ARTW/1-candidate";
       "contract_manifest_sha256", quote Driver_identity.contract_manifest_sha256;
       "build_snapshot_sha256", quote Driver_identity.build_snapshot_sha256;
       "source_sha256", optional quote state.source_sha256;
       "source_bytes", optional integer state.source_bytes;
       "entry", obj ["name", optional quote state.name; "definition_index", optional integer state.entry_index];
       "input", optional quote state.argument;
       "checking", strings ["reading", "unmetered"; "resolving", "unmetered"; "checking", "unmetered"];
       "reporting", quote "unmetered";
       "limits", strings ["source_bytes", state.source_limit; "value_bytes", state.value_limit];
       "execution", obj ["started", string_of_bool state.entry_attempted; "budget", optional quote state.budget;
                         "used", quote used; "remaining", optional quote remaining];
       "at", obj ["definition_index", optional integer result.at.definition;
                  "expr_path", optional path result.at.path; "source_offset", optional integer result.at.offset];
       "invoice", optional inv result.invoice; "value", Option.value result.value ~default:"null";
       "facts", strings result.facts]

exception Value_limit

module Graph (Store : sig type scope end) = struct
  module Seen = Hashtbl.Make (struct
    type t = Store.scope Value.t
    let equal = Value.equal
    let hash = Value.hash
  end)

  let render ~limit root =
    let ceiling = host_limit limit in
    let seen = Seen.create 32 and ordered = Queue.create () in
    (* Each node and each field reference needs at least one payload byte. *)
    let minimum = ref 0 in
    let count () = if !minimum >= ceiling then raise Value_limit else incr minimum in
    let rec visit v stack =
      if Seen.mem seen v then resume stack
      else begin
        count ();
        Seen.add seen v (Seen.length seen);
        Queue.add v ordered;
        match Value.tuple_width v with
        | Some width when width > 0 -> resume ((v, 0, width) :: stack)
        | Some _ | None -> resume stack
      end
    and resume = function
      | [] -> ()
      | (v, i, width) :: rest ->
          count ();
          let next = if i + 1 < width then (v, i + 1, width) :: rest else rest in
          visit (Value.field v i) next
    in
    visit root [];
    let buffer = Buffer.create (min ceiling 256) in
    let emit text =
      if String.length text > ceiling - Buffer.length buffer then raise Value_limit;
      Buffer.add_string buffer text
    in
    emit "{\"root\":\"0\",\"nodes\":[";
    Queue.iter (fun v ->
      let id = Seen.find seen v in
      if id > 0 then emit ",";
      emit "{\"id\":"; emit (integer id);
      (match Value.kind v with
       | Value.Natural ->
           let n = Option.get (Value.as_natural v) in
           emit ",\"kind\":\"natural\",\"decimal\":\""; emit (Natural.to_decimal n); emit "\""
       | Value.Builtin_none -> emit ",\"kind\":\"none\""
       | Value.Tuple ->
           emit ",\"kind\":\"tuple\",\"fields\":[";
           for i = 0 to Option.get (Value.tuple_width v) - 1 do
             if i > 0 then emit ",";
             emit (integer (Seen.find seen (Value.field v i)))
           done;
           emit "]");
      emit "}") ordered;
    emit "]}";
    Buffer.contents buffer
end
