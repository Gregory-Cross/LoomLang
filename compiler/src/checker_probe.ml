(* Compare public checker results to independently written fixture answers. *)
open Checker

let definition p index =
  match definition_at p index with
  | Some d -> d
  | None -> failwith "missing indexed definition"

let natural value =
  match Value.as_natural value with
  | Some n -> Natural.to_decimal n
  | None -> failwith "resolved literal is not natural"

let primitive_name = function Add -> "add" | Sub -> "sub" | Mul -> "mul"

let rec shape expr =
  match expr.form with
  | Literal value -> "n" ^ natural value
  | Local_slot slot -> "$" ^ string_of_int slot
  | Tuple items -> "tuple[" ^ String.concat "," (List.map shape items) ^ "]"
  | Arithmetic (op, left, right) -> primitive_name op ^ "(" ^ shape left ^ "," ^ shape right ^ ")"
  | Call (index, arg) -> Printf.sprintf "call#%d(%s)" index (shape arg)

let verify_program original p =
  let count = definition_count p in
  if source p <> original.Reader.source || count <> List.length original.Reader.definitions
     || Option.is_some (definition_at p (-1)) || Option.is_some (definition_at p count)
  then failwith "source or definition table bounds changed";
  let rec verify_nodes = function
    | [] -> ()
    | (raw, resolved) :: rest ->
        if raw.Reader.expr_span <> resolved.span then failwith "expression span changed";
        let children = match raw.Reader.form with
          | Reader.Apply (_, args) -> args
          | Reader.Reference _ -> []
          | Reader.Literal (digits, stored) ->
              (match resolved.form with
              | Literal v when Value.equal stored v && natural v = digits -> ()
              | Literal _ | Local_slot _ | Tuple _ | Arithmetic _ | Call _ -> failwith "literal changed");
              []
        in
        let checked_children = match resolved.form with
          | Tuple items -> items
          | Arithmetic (_, left, right) -> [left; right]
          | Call (_, arg) -> [arg]
          | Literal _ | Local_slot _ -> []
        in
        verify_nodes (List.fold_left2 (fun todo a b -> (a, b) :: todo) rest children checked_children)
  in
  List.iteri (fun i raw ->
    let d = definition p i in
    if d.name <> raw.Reader.name || [d.parameter] <> raw.Reader.parameters
       || d.declaration_span <> raw.Reader.definition_span then failwith "definition metadata changed";
    verify_nodes [raw.Reader.body, d.body]) original.Reader.definitions

let show_program view p =
  let first = "ok|entry=" ^ string_of_int (entry_index p) in
  match view with
  | "shape" ->
      let row index =
        let d = definition p index in
        Printf.sprintf "%d:%s[%s]=%s" index d.name.Reader.spelling d.parameter.Reader.spelling (shape d.body)
      in
      String.concat "|" (first :: List.init (definition_count p) row)
  | "chain" ->
      let rec depth n node = match node.form with
        | Call (0, child) -> depth (n + 1) child
        | Local_slot 0 -> n
        | Call _ | Local_slot _ | Literal _ | Tuple _ | Arithmetic _ -> failwith "wrong deep call graph"
      in
      if definition_count p <> 1 then failwith "wrong deep definition count";
      Printf.sprintf "%s|call_depth=%d|leaf=$0" first (depth 0 (definition p 0).body)
  | _ -> invalid_arg "unexpected admitted view"

let show_location view = function
  | Entry_argument -> "entry"
  | In_definition { definition_index; expr_path; position } ->
      let path = match expr_path with
        | None -> "-"
        | Some indices when view = "deep-error" ->
            if not (List.for_all ((=) 0) indices) then failwith "wrong deep diagnostic path";
            "zeros(" ^ string_of_int (List.length indices) ^ ")"
        | Some indices -> "[" ^ String.concat "," (List.map string_of_int indices) ^ "]"
      in
      Printf.sprintf "%d:%s@%d/%d/%d" definition_index path position.Reader.source_offset
        position.Reader.line position.Reader.column

let show_refusal view control refusal =
  let cause =
    if control = "wrong-cause" then
      match refusal.cause with
      | Unknown_call name -> Unbound_variable name
      | Reserved_global _ | Duplicate_global _ | Unsupported_definition_arity _
      | Reserved_binder _ | Binder_global_collision _ | Unbound_variable _
      | Wrong_role _ | Primitive_arity _ | Named_arity _ | Entry_missing _ | Entry_wrong_role _ ->
          failwith "planted wrong cause needs an unknown call"
    else refusal.cause
  in
  let code, facts = describe cause in
  let fields = List.map (fun (key, value) -> key ^ "=" ^ value) facts in
  String.concat "|" (code :: ("at=" ^ show_location view refusal.at) :: fields)

let answer path entry view control =
  let module Store = Value.Make () in
  let module Input = Reader.Make (Store) in
  match Input.read_file path with
  | Error e -> failwith ("checker fixture failed in reader: " ^ Reader.error_code e)
  | Ok original ->
      match check ~entry original with
      | Ok p -> verify_program original p; show_program view p
      | Error (Refused diagnostic) -> show_refusal view control diagnostic
      | Error (Tool_error fault) -> failwith (Reader.error_code (Reader.Tool_error fault))

let run requests actual control =
  let count = ref 0 in
  In_channel.with_open_bin requests (fun input ->
    Out_channel.with_open_bin actual (fun output ->
      let rec records () =
        match In_channel.input_line input with
        | None -> ()
        | Some row ->
            let row = if String.ends_with ~suffix:"\r" row then String.sub row 0 (String.length row - 1) else row in
            (match String.split_on_char '\t' row with
            | [id; view; filename; entry] ->
                let path = Filename.concat (Filename.dirname requests) filename in
                Printf.fprintf output "%s\t%s\n" id (answer path entry view control)
            | _ -> invalid_arg "bad checker request");
            incr count;
            records ()
      in
      records ()));
  Printf.printf "PROCESSED %d\n%!" !count;
  if !count = 0 then 2 else 0

let () =
  let code = try
    match Array.to_list Sys.argv with
    | [_; requests; actual; control] -> run requests actual control
    | _ -> invalid_arg "expected requests, actual, control"
  with Invalid_argument msg | Sys_error msg | Failure msg -> Printf.eprintf "ERROR %s\n%!" msg; 2
  in
  exit code
