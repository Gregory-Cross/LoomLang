(* Observe graph, quotation, meter and reporting boundaries in the private test build. *)
let nat text =
  match Natural.of_decimal text with Ok n -> n | Error why -> invalid_arg why

let hex text =
  let out = Buffer.create (2 * String.length text) in
  String.iter (fun c -> Printf.bprintf out "%02x" (Char.code c)) text;
  Buffer.contents out

let json_strings values =
  "[" ^ String.concat "," (List.map Run_record.quote values) ^ "]"

let balance_fields meter =
  let a = Meter.accounting meter in
  ["used", Run_record.natural a.Meter.used;
   "remaining", Run_record.natural a.Meter.remaining;
   "stopped", string_of_bool (Option.is_some (Meter.stopped meter))]

let graph_case id limit =
  let module Store = Value.Make () in
  let module Graph = Run_record.Graph (Store) in
  let root = Store.tuple [|Store.natural (nat "4")|] in
  let failures = ref [] in
  let previous = !Run_record.test_graph_limit_site in
  let result =
    Fun.protect
      ~finally:(fun () -> Run_record.test_graph_limit_site := previous)
      (fun () ->
        Run_record.test_graph_limit_site := (fun site -> failures := site :: !failures);
        try `Rendered (Graph.render ~limit root)
        with Run_record.Value_limit -> `Limited)
  in
  let result_name, rendered = match result with
    | `Rendered text -> "returned", text
    | `Limited -> "value_limit", "null"
  in
  Run_record.obj
    ["case", Run_record.quote id; "limit", Run_record.quote limit;
     "result", Run_record.quote result_name;
     "failure_sites", json_strings (List.rev !failures); "rendered", rendered]

let quote_case () =
  (* NUL; malformed singleton FF; ASCII A; valid UTF-8 U+2603. *)
  let input = "\000\255A\226\152\131" in
  let rendered = Run_record.quote input in
  Run_record.obj
    ["case", Run_record.quote "at3-quote";
     "input_hex", Run_record.quote (hex input);
     "quoted_hex", Run_record.quote (hex rendered);
     "rendered", rendered]

let unavailable_case () =
  let module Store = Value.Make () in
  let module Source = Reader.Make (Store) in
  let module Frames = Eval.Make (Store) in
  let source = "def main[x]=mul[x,1]" in
  let parsed = match Source.read_bytes source with
    | Ok tree -> tree
    | Error e -> failwith ("reader: " ^ Reader.error_code e)
  in
  let program = match Checker.check ~entry:"main" parsed with
    | Ok admitted -> admitted
    | Error (Checker.Refused r) -> failwith (fst (Checker.describe r.Checker.cause))
    | Error (Checker.Tool_error e) -> failwith (Reader.error_code (Reader.Tool_error e))
  in
  let meter = Meter.create ~budget:(nat "9") in
  let callbacks = ref 0 and dispatches = ref 0 in
  let primitive ~meter:passed ~at op ~left ~right:_ =
    if passed != meter then failwith "evaluator substituted meter";
    if op <> Checker.Mul then failwith "expected mul dispatch";
    incr dispatches;
    (* Synthetic estimate at the genuine evaluator-supplied location. Current
       production B arithmetic has finite estimates; this is a boundary test. *)
    Meter.pay passed ~at
      (Meter.Unavailable { event = Meter.Arithmetic op; reason = "synthetic unavailable mul bound" })
      ~build:(fun _ -> incr callbacks; left)
  in
  let stop = match Frames.run ~meter ~primitive ~input:(nat "4") program with
    | Ok _ -> failwith "synthetic unavailable bound returned"
    | Error stop -> stop
  in
  let latched_identity = match Meter.stopped meter with
    | Some latched -> latched == stop
    | None -> false
  in
  let context = Run_record.context () in
  context.Run_record.name <- Some "main";
  context.Run_record.entry_index <- Some (Checker.entry_index program);
  context.Run_record.argument <- Some "4";
  context.Run_record.budget <- Some "9";
  context.Run_record.source_bytes <- Some (String.length source);
  context.Run_record.source_sha256 <- Some (Sha256.hex source);
  context.Run_record.meter <- Some meter;
  Run_record.obj
    ["case", Run_record.quote "at4-unavailable";
     "synthetic", "true";
     "dispatches", string_of_int !dispatches;
     "callbacks", string_of_int !callbacks;
     "latched_identity", string_of_bool latched_identity;
     "report", Run_record.encode context (Run_record.stopped stop)]

let guards_case () =
  (* Keep all three invalid cases on the same running meter, in this order. *)
  let meter = Meter.create ~budget:Natural.one in
  let callbacks = ref 0 in
  let pay estimate =
    Meter.pay meter ~at:() estimate ~build:(fun _ -> incr callbacks)
  in
  let invalid id action =
    let exception_name =
      try ignore (action ()); "none" with Invalid_argument _ -> "Invalid_argument"
    in
    Run_record.obj
      (["guard", Run_record.quote id;
        "exception", Run_record.quote exception_name;
        "callbacks", string_of_int !callbacks] @ balance_fields meter)
  in
  let left = invalid "zero-left" (fun () ->
    pay (Meter.natural_bits Checker.Mul ~left:Natural.zero ~right:Natural.one)) in
  let right = invalid "zero-right" (fun () ->
    pay (Meter.natural_bits Checker.Mul ~left:Natural.one ~right:Natural.zero)) in
  let blank = invalid "blank-reason" (fun () ->
    pay (Meter.Unavailable { event = Meter.Arithmetic Checker.Mul; reason = " \t\r\n" })) in
  let entry = match pay (Meter.structural Meter.Entry) with
    | Ok () -> "paid"
    | Error _ -> "stopped"
  in
  let after_entry = Run_record.obj
    (["result", Run_record.quote entry; "callbacks", string_of_int !callbacks] @ balance_fields meter)
  in
  Run_record.obj
    ["case", Run_record.quote "at6-guards";
     "guards", "[" ^ String.concat "," [left; right; blank] ^ "]";
     "entry", after_entry]

let run = function
  | "at1-root" -> graph_case "at1-root" "0"
  | "at1-edge" -> graph_case "at1-edge" "1"
  | "at1-child" -> graph_case "at1-child" "2"
  | "at1-emit" -> graph_case "at1-emit" "3"
  | "at1-render" -> graph_case "at1-render" "4096"
  | "at3-quote" -> quote_case ()
  | "at4-unavailable" -> unavailable_case ()
  | "at6-guards" -> guards_case ()
  | _ -> invalid_arg "unknown protocol case"

let () =
  let code =
    try
      if Array.length Sys.argv <> 2 then invalid_arg "expected one protocol case id";
      print_endline (run Sys.argv.(1));
      0
    with Invalid_argument why | Failure why | Sys_error why ->
      Printf.eprintf "PROTOCOL ERROR %s\n%!" why;
      2
  in
  exit code
