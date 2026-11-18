(* Counted file-oriented probe. Literal answers live in fixtures/reader. *)
open Reader

let position at = Printf.sprintf "%d/%d/%d" at.source_offset at.line at.column
let span range = position range.start_pos ^ "-" ^ position range.end_pos

let literal digits value =
  match Value.as_natural value with
  | Some n when Natural.to_decimal n = digits -> digits
  | Some _ | None -> failwith "literal disagrees with piece 11 value"

let rec shape expression =
  match expression.form with
  | Literal (digits, value) -> literal digits value
  | Reference head -> head.spelling
  | Apply (head, children) -> head.spelling ^ "[" ^ String.concat "," (List.map shape children) ^ "]"

let declaration item =
  let params = List.map (fun p -> p.spelling) item.parameters in
  item.name.spelling ^ "[" ^ String.concat "," params ^ "]=" ^ shape item.body

let positions program =
  let fields = Buffer.create 256 in
  let emit label range =
    Buffer.add_string fields ("|" ^ label ^ "@" ^ span range)
  in
  let rec expression node =
    match node.form with
    | Literal (digits, value) -> emit ("literal=" ^ literal digits value) node.expr_span
    | Reference name ->
        emit "reference" node.expr_span;
        emit ("word=" ^ name.spelling) name.word_span
    | Apply (head, children) ->
        emit "apply" node.expr_span;
        emit ("head=" ^ head.spelling) head.word_span;
        List.iter expression children
  in
  List.iter (fun item ->
    emit "def" item.definition_span;
    emit ("name=" ^ item.name.spelling) item.name.word_span;
    List.iter (fun p -> emit ("param=" ^ p.spelling) p.word_span) item.parameters;
    expression item.body) program.definitions;
  "eof@" ^ position program.eof ^ Buffer.contents fields

let chain program =
  let length = String.length program.source in
  let at offset = { source_offset = offset; line = 1; column = offset + 1 } in
  let check range first last =
    if range.start_pos <> at first || range.end_pos <> at last then failwith "wrong generated chain span"
  in
  let rec visit depth node =
    let first = 8 + 2 * depth in
    check node.expr_span first (length - depth);
    match node.form with
    | Apply (head, children) ->
        if head.spelling <> "a" then failwith "wrong generated chain head";
        check head.word_span first (first + 1);
        (match children with
        | [] -> depth + 1
        | [child] -> visit (depth + 1) child
        | _ :: _ :: _ -> failwith "wrong generated chain width")
    | Literal _ | Reference _ -> failwith "wrong generated chain leaf"
  in
  match program.definitions with
  | [item] when item.name.spelling = "f" && item.parameters = [] && program.eof = at length ->
      check item.definition_span 0 length;
      check item.name.word_span 4 5;
      Printf.sprintf "depth=%d|bytes=%d" (visit 0 item.body) length
  | [] | [_] | _ :: _ :: _ -> failwith "wrong generated chain declaration"

let describe_error wrong_position error =
  let code = error_code error in
  match error with
  | Refused (at, cause) ->
      let reported = if wrong_position then { at with column = at.column + 1 } else at in
      let detail = match cause with
        | Encoding -> ""
        | Character cp -> "|code_point=" ^ string_of_int cp
        | Noncanonical_natural raw -> "|token=" ^ raw
        | Syntax { expected; actual } ->
            let seen = match actual with Token raw -> raw | End_of_source -> "<EOF>" in
            "|expected=" ^ expected ^ "|actual=" ^ seen
      in
      code ^ "@" ^ position reported ^ detail
  | Tool_error fault ->
      let detail = match fault with
        | Source_limit { limit; observed_at_least } ->
            "|limit=" ^ Natural.to_decimal limit ^ "|observed_at_least=" ^ Natural.to_decimal observed_at_least
        | Source_io { operation; system_error } ->
            "|operation=" ^ operation ^ "|system_error=" ^ (if system_error = "" then "empty" else "present")
        | Host_stack phase | Host_memory phase -> "|phase=" ^ phase
        | Internal_error { phase; reason } -> "|phase=" ^ phase ^ "|reason=" ^ reason
      in
      code ^ detail

let answer path method_name view limit control =
  let module Store = Value.Make () in
  let module R = Reader.Make (struct
    type scope = Store.scope
    let natural n =
      match view with
      | "host-memory" -> raise Out_of_memory
      | "host-stack" -> raise Stack_overflow
      | "internal" -> failwith "planted store failure"
      | _ -> Store.natural n
  end) in
  let max_source_bytes =
    if limit = "default" then None
    else match Natural.of_decimal limit with
      | Ok n -> Some n
      | Error msg -> invalid_arg msg
  in
  let bytes () = In_channel.with_open_bin path In_channel.input_all in
  let result = match method_name with
    | "file" -> R.read_file ?max_source_bytes path
    | "bytes" -> R.read_bytes ?max_source_bytes (bytes ())
    | _ -> invalid_arg "unknown reader entry point"
  in
  match result with
  | Error error -> describe_error (control = "wrong-position") error
  | Ok program ->
      if program.source <> bytes () then failwith "successful reader changed source bytes";
      let program =
        if control = "dropped-declaration" then
          match program.definitions with
          | first :: _dropped :: rest -> { program with definitions = first :: rest }
          | [] | [_] -> failwith "dropped-declaration control needs two definitions"
        else program
      in
      match view with
      | "positions" -> positions program
      | "chain" -> chain program
      | "shape" | "intern" ->
          let forms = List.map declaration program.definitions in
          let result = String.concat "|" ("ok" :: forms) in
          if view = "intern" then result ^ "|store_nodes=" ^ string_of_int (Store.interned_count ())
          else result
      | _ -> invalid_arg "unexpected successful probe view"

let run requests actual control =
  let count = ref 0 in
  let handle output line =
    let line =
      if String.ends_with ~suffix:"\r" line then String.sub line 0 (String.length line - 1) else line
    in
    match String.split_on_char '\t' line with
    | [id; view; method_name; filename; limit] ->
        let path = Filename.concat (Filename.dirname requests) filename in
        let response = answer path method_name view limit control in
        Printf.fprintf output "%s\t%s\n" id response;
        incr count
    | _ -> invalid_arg "bad reader request"
  in
  In_channel.with_open_bin requests (fun input ->
    Out_channel.with_open_bin actual (fun output ->
      let rec lines () =
        match In_channel.input_line input with
        | Some line -> handle output line; lines ()
        | None -> ()
      in
      lines ()));
  Printf.printf "PROCESSED %d\n%!" !count;
  if !count = 0 then 2 else 0

let () =
  let code =
    try
      match Array.to_list Sys.argv with
      | [_; requests; actual; control] -> run requests actual control
      | _ -> invalid_arg "expected requests, actual, control"
    with Invalid_argument msg | Sys_error msg | Failure msg -> Printf.eprintf "ERROR %s\n%!" msg; 2
  in
  exit code
