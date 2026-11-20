open Run_record

let digit = function '0' .. '9' -> true | _ -> false
let letter = function 'a' .. 'z' | 'A' .. 'Z' | '_' -> true | _ -> false
let word s =
  String.length s > 0 && letter s.[0] && String.for_all (fun c -> letter c || digit c) s
let numeral s =
  String.length s > 0 && (String.length s = 1 || s.[0] <> '0') && String.for_all digit s
let as_nat s = match Natural.of_decimal s with Ok n -> n | Error why -> invalid_arg why

let flags = ["--program"; "--entry"; "--input"; "--fuel"; "--max-source-bytes"; "--max-value-bytes"]
let parse_argv state argv =
  let fields = Hashtbl.create 6 in
  let get = Hashtbl.find_opt fields in
  let rec scan i =
    if i = Array.length argv then None
    else
      let flag = argv.(i) in
      let error code key = Some (outcome ~facts:[key, flag; "argv_index", string_of_int (i - 1)]
                                  Refused ("invoke.arguments." ^ code)) in
      if not (List.mem flag flags) then error "unknown_flag" "token"
      else if Hashtbl.mem fields flag then error "duplicate_flag" "flag"
      else if i + 1 = Array.length argv || String.starts_with ~prefix:"--" argv.(i + 1) then error "missing_value" "flag"
      else begin Hashtbl.add fields flag argv.(i + 1); scan (i + 2) end
  in
  let syntax = scan 1 in
  let valid flag test = match get flag with Some raw when test raw -> Some raw | Some _ | None -> None in
  state.name <- valid "--entry" word;
  state.argument <- valid "--input" numeral;
  state.budget <- valid "--fuel" numeral;
  Option.iter (fun text -> state.source_limit <- text) (valid "--max-source-bytes" numeral);
  Option.iter (fun text -> state.value_limit <- text) (valid "--max-value-bytes" numeral);
  match syntax with
  | Some result -> Error result
  | None ->
      match List.find_opt (fun f -> not (Hashtbl.mem fields f)) ["--program"; "--entry"; "--input"; "--fuel"] with
      | Some flag -> Error (outcome ~facts:["flag", flag] Refused "invoke.arguments.missing_flag")
      | None ->
          let token f = Hashtbl.find fields f in
          let invalid f code = Error (outcome ~facts:["token", token f] Refused code) in
          if state.name = None then invalid "--entry" "invoke.arguments.malformed_entry"
          else if state.argument = None then invalid "--input" "invoke.bad_input"
          else if state.budget = None then invalid "--fuel" "invoke.bad_fuel"
          else match List.find_opt (fun f -> Hashtbl.mem fields f && not (numeral (token f)))
                       ["--max-source-bytes"; "--max-value-bytes"] with
            | Some flag -> Error (outcome ~facts:["flag", flag; "token", token flag] Refused "invoke.arguments.bad_tool_limit")
            | None -> Ok (token "--program", token "--entry", token "--input", token "--fuel")

exception Source_fault of Reader.fault

let read_source path limit =
  let io operation work =
    try work () with Sys_error system_error -> raise (Source_fault (Reader.Source_io { operation; system_error }))
  in
  let ceiling = host_limit limit in
  let channel = io "open" (fun () -> open_in_bin path) in
  Fun.protect ~finally:(fun () -> close_in_noerr channel) (fun () ->
    let chunk = Bytes.create 8192 and data = Buffer.create (min 8192 ceiling) in
    let rec read () =
      let size = Buffer.length data in
      let left = ceiling - size in
      let wanted = if left < Bytes.length chunk then left + 1 else Bytes.length chunk in
      let n = io "read" (fun () -> input channel chunk 0 wanted) in
      if n = 0 then Buffer.contents data
      else if n > left then begin
        let limit = as_nat limit in
        raise (Source_fault (Reader.Source_limit { limit; observed_at_least = Natural.add limit Natural.one }))
      end
      else if n > Sys.max_string_length - size then raise Out_of_memory
      else begin Buffer.add_subbytes data chunk 0 n; read () end
    in read ())

let fault f =
  let facts = match f with
    | Reader.Source_io { operation; system_error } -> ["operation", operation; "system_error", system_error]
    | Reader.Source_limit { limit; observed_at_least } ->
        ["limit", Natural.to_decimal limit; "observed_at_least", Natural.to_decimal observed_at_least]
    | Reader.Host_memory phase | Reader.Host_stack phase -> ["phase", phase]
    | Reader.Internal_error { phase; reason } -> ["phase", phase; "reason", reason]
  in outcome ~facts Tool_error (Reader.error_code (Reader.Tool_error f))

let reader_error = function
  | Reader.Tool_error f -> fault f
  | Reader.Refused (pos, cause) as error ->
      let facts = match cause with
        | Reader.Encoding -> []
        | Reader.Character cp -> ["code_point", string_of_int cp]
        | Reader.Noncanonical_natural token -> ["token", token]
        | Reader.Syntax { expected; actual } ->
            let found = match actual with Reader.Token raw -> raw | Reader.End_of_source -> "<EOF>" in
            ["expected", expected; "actual", found]
      in
      let at = { nowhere with offset = Some pos.Reader.source_offset } in
      outcome ~at ~facts Refused (Reader.error_code error)

let checker_error = function
  | Checker.Tool_error f -> fault f
  | Checker.Refused refusal ->
      let at = match refusal.Checker.at with
        | Checker.Entry_argument -> nowhere
        | Checker.In_definition { definition_index; expr_path; position } ->
            { definition = Some definition_index; path = expr_path; offset = Some position.Reader.source_offset }
      in
      let code, facts = Checker.describe refusal.Checker.cause in
      outcome ~at ~facts Refused code

let external_error phase = function
  | Source_fault f -> fault f
  | Out_of_memory -> fault (Reader.Host_memory phase)
  | Stack_overflow -> fault (Reader.Host_stack phase)
  | exn -> fault (Reader.Internal_error { phase; reason = Printexc.to_string exn })

let invoke state phase argv =
  match parse_argv state argv with
  | Error refused -> refused
  | Ok (file, entry, argument, fuel) ->
      phase := "read";
      let bytes = read_source file state.source_limit in
      state.source_bytes <- Some (String.length bytes);
      state.source_sha256 <- Some (Sha256.hex bytes);
      let module Store = Value.Make () in
      let module Source = Reader.Make (Store) in
      let module Execute = Eval.With_primitives (Store) in
      let module Display = Graph (Store) in
      match Source.read_bytes ~max_source_bytes:(as_nat (string_of_int (host_limit state.source_limit))) bytes with
      | Error e -> reader_error e
      | Ok program ->
          phase := "check";
          match Checker.check ~entry program with
          | Error e -> checker_error e
          | Ok admitted ->
              state.entry_index <- Some (Checker.entry_index admitted);
              phase := "evaluate";
              let input = as_nat argument and meter = Meter.create ~budget:(as_nat fuel) in
              state.meter <- Some meter;
              match Execute.run ~on_entry_attempt:(mark_entry_attempt state) ~meter ~input admitted with
              | Error stop -> stopped stop
              | Ok value ->
                  phase := "report";
                  try outcome ~value:(Display.render ~limit:state.value_limit value) Returned "value.returned"
                  with Value_limit -> outcome ~facts:["evaluation_status", "returned"] Tool_error "tool.value_limit"

let write_report channel report =
  set_binary_mode_out channel true;
  output_string channel report; output_char channel '\n'; flush channel

let main argv =
  let state = context () and phase = ref "invocation" in
  let result = try invoke state phase argv with exn -> external_error !phase exn in
  let report, status =
    try encode state result, result.status with exn ->
      let failure = external_error "report" exn in encode state failure, failure.status
  in
  try
    write_report stdout report;
    exit_code status
  with exn ->
    let failure = match exn with
      | Sys_error system_error -> outcome ~facts:["operation", "write"; "system_error", system_error] Tool_error "tool.report_io"
      | other -> external_error "report" other
    in
    write_report stderr (encode state failure);
    exit_code Tool_error

(* The primitive used by Stdlib.exit after its hooks. Terminal recovery must
   not invoke another formatter, flush hook or allocating exit handler. *)
external exit_without_hooks : int -> 'a = "caml_sys_exit"

let () =
  try
    if not Sys.win32 then Sys.set_signal Sys.sigpipe Sys.Signal_ignore;
    exit_without_hooks (main Sys.argv)
  with _ ->
    (try write_report stderr "loom-b: report unavailable" with _ -> ());
    exit_without_hooks 4
