(* Author probe for the injectable frames and the normal arithmetic evaluator.
   Store observations record the balance at the real lookup or construction. *)
let nat s = match Natural.of_decimal s with Ok n -> n | Error why -> invalid_arg why
let dec = Natural.to_decimal

let balance (state : Meter.accounting) = dec state.Meter.used ^ "," ^ dec state.Meter.remaining

let show_location definition expr_path source_offset =
  let path = match expr_path with
    | None -> "-"
    | Some xs when List.length xs > 128 && List.for_all ((=) 0) xs ->
        "zeros(" ^ string_of_int (List.length xs) ^ ")"
    | Some xs -> "[" ^ String.concat "," (List.map string_of_int xs) ^ "]"
  in
  let offset = match source_offset with None -> "-" | Some n -> string_of_int n in
  Printf.sprintf "%d:%s@%s" definition path offset

let location at =
  show_location (Eval.definition_index at) (Eval.expression_path at) (Eval.source_offset at)

let primitive_name = function Checker.Add -> "add" | Checker.Sub -> "sub" | Checker.Mul -> "mul"

let event_name = function
  | Meter.Structural Meter.Entry -> "entry"
  | Meter.Structural Meter.Literal -> "literal"
  | Meter.Structural Meter.Variable -> "variable"
  | Meter.Structural Meter.Call -> "call"
  | Meter.Structural Meter.Return -> "return"
  | Meter.Tuple -> "tuple"
  | Meter.Arithmetic p -> primitive_name p
  | Meter.Wrong_kind p -> "wrong-kind/" ^ primitive_name p

let value_text root =
  let buf = Buffer.create 32 in
  let rec visit = function
    | [] -> Buffer.contents buf
    | v :: pending ->
        if Buffer.length buf > 0 then Buffer.add_char buf ',';
        let header = Value.local_header v in
        Buffer.add_substring buf header 0 (String.length header - 1);
        match Value.tuple_width v with
        | None -> visit pending
        | Some width ->
            let rest = ref pending in
            for i = width - 1 downto 0 do rest := Value.field v i :: !rest done;
            visit !rest
  in
  visit [root]

exception Primitive_boundary of string * Eval.location

let stop_receipt meter stop =
  (match Meter.stopped meter with
  | Some original when original == stop -> ()
  | Some _ | None -> failwith "stop identity lost");
  let bill = match stop.Meter.cause with
    | Meter.Insufficient i -> String.concat "," (List.map dec [i.Meter.a; i.Meter.r; i.Meter.t; i.Meter.w; i.Meter.total])
    | Meter.Bound_unavailable reason -> "?" ^ reason
  in
  Meter.stop_code stop.Meter.cause, event_name stop.Meter.failed_event,
  location stop.Meter.at, bill, dec stop.Meter.failed_operation_debit

let run_case filename entry input_text budget_text preload mode =
  let module Raw = Value.Make () in
  let input = nat input_text and budget = nat budget_text in
  let meter = Meter.create ~budget in
  let calls = ref [] in
  let module Store = struct
    type scope = Raw.scope
    let natural = Raw.natural
    let tuple fields =
      let paid = balance (Meter.accounting meter) and before = Raw.interned_count () in
      let value = Raw.tuple fields in
      let added = Raw.interned_count () - before in
      calls := Printf.sprintf "%s:%d:%s" paid added (value_text value) :: !calls;
      value
  end in
  let module Reader_for_store = Reader.Make (Store) in
  let module Frames = Eval.Make (Store) in
  let argument = Raw.natural input in
  (match preload with
  | "none" -> ()
  | "empty" -> ignore (Raw.tuple [||])
  | "pair" -> ignore (Raw.tuple [|argument; argument|])
  | _ -> invalid_arg "unknown tuple preload");
  let pending = Weak.create 1 in
  let primitive ~meter:passed ~at op ~left ~right =
    if passed != meter then failwith "dispatch received a different meter";
    let operands = primitive_name op ^ "(" ^ value_text left ^ "/" ^ value_text right ^ ")" in
    raise (Primitive_boundary (operands, at))
  in
  let[@inline never] execute () =
    let bytes = In_channel.with_open_bin filename In_channel.input_all in
    let parsed = match Reader_for_store.read_bytes bytes with
      | Ok p -> p | Error e -> failwith ("fixture reader: " ^ Reader.error_code e)
    in
    let program = match Checker.check ~entry parsed with
      | Ok p -> p
      | Error (Checker.Refused r) -> failwith ("fixture checker: " ^ fst (Checker.describe r.Checker.cause))
      | Error (Checker.Tool_error e) -> failwith (Reader.error_code (Reader.Tool_error e))
    in
    if mode = "cleanup" then begin
      let def = Option.get (Checker.definition_at program (Checker.entry_index program)) in
      match def.Checker.body.Checker.form with
      | Checker.Tuple [_; sibling] -> Weak.set pending 0 (Some sibling)
      | Checker.Tuple _ | Checker.Literal _ | Checker.Local_slot _ | Checker.Arithmetic _ | Checker.Call _ ->
          failwith "cleanup expects an unvisited second tuple field"
    end;
    try
      match Frames.run ~meter ~primitive ~input program with
      | Ok value -> `Returned value
      | Error stop -> `Stopped stop
    with Primitive_boundary (operands, at) -> `Dispatch (operands, at)
  in
  let result = execute () in
  let released =
    match mode with
    | "normal" -> "-"
    | "cleanup" ->
        Gc.full_major ();
        if Weak.check pending 0 then failwith "pending expression retained after fuel stop";
        "clear"
    | _ -> invalid_arg "unknown probe mode"
  in
  let status, detail, site, invoice, failed =
    match Sys.opaque_identity result with
    | `Returned value -> "returned", value_text value, "-", "-", "-"
    | `Dispatch (operands, at) -> "internal-dispatch", operands, location at, "-", "-"
    | `Stopped stop -> stop_receipt meter stop
  in
  let state = Meter.accounting meter in
  if Natural.compare state.Meter.budget budget <> 0 ||
     Natural.compare (Natural.add state.Meter.used state.Meter.remaining) budget <> 0 then
    failwith "fuel conservation";
  let log = match List.rev !calls with [] -> "-" | data -> String.concat ";" data in
  String.concat "|" [status; detail; site; invoice; failed; balance state; log; released]

let run_primitives filename entry input_text budget_text =
  let module Raw = Value.Make () in
  let budget = nat budget_text in
  let meter = Meter.create ~budget and writes = ref [] in
  let observe kind construct =
    let paid = balance (Meter.accounting meter) and before = Raw.interned_count () in
    let result = construct () in
    let added = Raw.interned_count () - before in
    writes := Printf.sprintf "%s:%s:%d:%s" kind paid added (value_text result) :: !writes;
    result
  in
  let module Store = struct
    type scope = Raw.scope
    let none = Raw.none
    let natural n =
      if Natural.compare (Meter.accounting meter).Meter.used Natural.zero = 0 then Raw.natural n
      else observe "n" (fun () -> Raw.natural n)
    let tuple fields = observe "t" (fun () -> Raw.tuple fields)
  end in
  let module Source = Reader.Make (Raw) in
  let module Evaluator = Eval.With_primitives (Store) in
  let bytes = In_channel.with_open_bin filename In_channel.input_all in
  let tree = match Source.read_bytes bytes with
    | Ok tree -> tree | Error e -> failwith (Reader.error_code e)
  in
  let started, (status, detail, at, invoice, failed) =
    match Checker.check ~entry tree with
    | Error (Checker.Tool_error e) -> failwith (Reader.error_code (Reader.Tool_error e))
    | Error (Checker.Refused r) ->
        let code, facts = Checker.describe r.Checker.cause in
        let fields = String.concat "," (List.map (fun (key, v) -> key ^ "=" ^ v) facts) in
        let at = match r.Checker.at with
          | Checker.Entry_argument -> "entry"
          | Checker.In_definition { definition_index; expr_path; position } ->
              show_location definition_index expr_path (Some position.Reader.source_offset)
        in
        "0", ("refused", code ^ ":" ^ fields, at, "-", "-")
    | Ok program ->
        let result = match Evaluator.run ~meter ~input:(nat input_text) program with
          | Error stop -> stop_receipt meter stop
          | Ok value ->
              if Value.kind value = Value.Builtin_none && value != Raw.none then
                failwith "wrong-kind result is not the store's builtin none";
              "returned", value_text value, "-", "-", "-"
        in
        "1", result
  in
  let state = Meter.accounting meter in
  if Natural.compare (Natural.add state.Meter.used state.Meter.remaining) budget <> 0 then
    failwith "primitive fuel conservation";
  let log = match List.rev !writes with [] -> "-" | xs -> String.concat ";" xs in
  String.concat "|" [status; detail; at; invoice; failed; balance state; started; log]

let run requests actual =
  let count = ref 0 in
  In_channel.with_open_bin requests (fun input ->
    Out_channel.with_open_bin actual (fun output ->
      let rec rows () = match In_channel.input_line input with
        | None -> ()
        | Some line ->
            let line = if String.ends_with ~suffix:"\r" line then String.sub line 0 (String.length line - 1) else line in
            (match String.split_on_char '\t' line with
            | [id; "primitives"; source; entry; argument; fuel; "-"] ->
                let filename = Filename.concat (Filename.dirname requests) source in
                Printf.fprintf output "%s\t%s\n" id (run_primitives filename entry argument fuel)
            | [id; mode; source; entry; argument; fuel; preload] ->
                let filename = Filename.concat (Filename.dirname requests) source in
                Printf.fprintf output "%s\t%s\n" id (run_case filename entry argument fuel preload mode)
            | _ -> invalid_arg "bad frame request");
            incr count;
            rows ()
      in rows ()));
  Printf.printf "PROCESSED %d\n%!" !count;
  if !count = 0 then 2 else 0

let () =
  let code = try
    match Array.to_list Sys.argv with
    | [_; requests; actual] -> run requests actual
    | _ -> invalid_arg "expected requests and actual"
  with Invalid_argument msg | Sys_error msg | Failure msg -> Printf.eprintf "ERROR %s\n%!" msg; 2
  in exit code
