type primitive = Add | Sub | Mul

type 'scope expression = { span : Reader.span; form : 'scope form }
and 'scope form =
  | Literal of 'scope Value.t
  | Local_slot of int
  | Tuple of 'scope expression list
  | Arithmetic of primitive * 'scope expression * 'scope expression
  | Call of int * 'scope expression

type 'scope definition = {
  name : Reader.word;
  parameter : Reader.word;
  body : 'scope expression;
  declaration_span : Reader.span;
}

type role = Local | Definition | Primitive | Constructor | Keyword
type required_role = Need_local | Need_callable
type arity = { call_name : string; expected : int; actual : int }

type cause =
  | Reserved_global of { name : string; declaration_index : int }
  | Duplicate_global of { name : string; first_index : int; second_index : int }
  | Unsupported_definition_arity of { name : string; actual : int }
  | Reserved_binder of { name : string; definition_index : int }
  | Binder_global_collision of { name : string; definition_index : int; global_index : int }
  | Unbound_variable of string
  | Unknown_call of string
  | Wrong_role of { name : string; actual_role : role; required_role : required_role }
  | Primitive_arity of arity
  | Named_arity of arity
  | Entry_missing of string
  | Entry_wrong_role of { name : string; actual_role : role }

type location =
  | Entry_argument
  | In_definition of {
      definition_index : int;
      expr_path : int list option;
      position : Reader.position;
    }

type refusal = { cause : cause; at : location }
type error = Refused of refusal | Tool_error of Reader.fault

type 'scope program = {
  source_bytes : string;
  selected_entry : int;
  definitions : 'scope definition array;
}

let source p = p.source_bytes
let entry_index p = p.selected_entry
let definition_count p = Array.length p.definitions

let definition_at p index =
  if index < 0 || index >= definition_count p then None else Some p.definitions.(index)

let role_name = function
  | Local -> "local" | Definition -> "definition" | Primitive -> "primitive"
  | Constructor -> "constructor" | Keyword -> "keyword"

let describe cause =
  let number key n = key, string_of_int n in
  let arity_facts a = ["name", a.call_name; number "expected" a.expected; number "actual" a.actual] in
  match cause with
  | Reserved_global { name; declaration_index } ->
      "check.reserved_global", ["name", name; number "declaration_index" declaration_index]
  | Duplicate_global { name; first_index; second_index } ->
      "check.duplicate_global", ["name", name; number "first_index" first_index; number "second_index" second_index]
  | Unsupported_definition_arity { name; actual } ->
      "check.unsupported_definition_arity", ["name", name; number "actual" actual]
  | Reserved_binder { name; definition_index } ->
      "check.reserved_binder", ["name", name; number "definition_index" definition_index]
  | Binder_global_collision { name; definition_index; global_index } ->
      "check.binder_global_collision", ["name", name; number "definition_index" definition_index;
                                       number "global_index" global_index]
  | Unbound_variable name -> "resolve.unbound_variable", ["name", name]
  | Unknown_call name -> "resolve.unknown_call", ["name", name]
  | Wrong_role { name; actual_role; required_role } ->
      let required = match required_role with Need_local -> "local" | Need_callable -> "callable" in
      "resolve.wrong_role", ["name", name; "actual_role", role_name actual_role; "required_role", required]
  | Primitive_arity a -> "resolve.primitive_arity", arity_facts a
  | Named_arity a -> "resolve.named_arity", arity_facts a
  | Entry_missing name -> "invoke.entry_missing", ["name", name]
  | Entry_wrong_role { name; actual_role } ->
      "invoke.entry_wrong_role", ["name", name; "actual_role", role_name actual_role]

exception Reject of refusal

let reject at cause = raise (Reject { cause; at })

let reject_word definition_index expr_path word cause =
  let position = word.Reader.word_span.Reader.start_pos in
  reject (In_definition { definition_index; expr_path; position }) cause

type target = Parameter | Function of int | Builtin of primitive | Tuple_head | Def_keyword

let reserved = function
  | "def" -> Some Def_keyword
  | "add" -> Some (Builtin Add)
  | "sub" -> Some (Builtin Sub)
  | "mul" -> Some (Builtin Mul)
  | "tuple" -> Some Tuple_head
  | _ -> None

let role_of = function
  | Parameter -> Local | Function _ -> Definition | Builtin _ -> Primitive
  | Tuple_head -> Constructor | Def_keyword -> Keyword

let globals_of declarations =
  let globals = Hashtbl.create (Array.length declarations) in
  Array.iteri (fun index decl ->
    let word = decl.Reader.name in
    let name = word.Reader.spelling in
    if Option.is_some (reserved name) then
      reject_word index None word (Reserved_global { name; declaration_index = index });
    match Hashtbl.find_opt globals name with
    | Some first_index -> reject_word index None word (Duplicate_global { name; first_index; second_index = index })
    | None -> Hashtbl.add globals name index) declarations;
  globals

let checked_parameters globals declarations =
  (* Finish every arity check before looking at the spelling of any binder. *)
  let parameters = Array.mapi (fun index decl ->
    match decl.Reader.parameters with
    | [word] -> word
    | other ->
        let word = decl.Reader.name in
        reject_word index None word
          (Unsupported_definition_arity { name = word.Reader.spelling; actual = List.length other })) declarations
  in
  Array.iteri (fun definition_index word ->
    let name = word.Reader.spelling in
    if Option.is_some (reserved name) then
      reject_word definition_index None word (Reserved_binder { name; definition_index });
    match Hashtbl.find_opt globals name with
    | Some global_index ->
        reject_word definition_index None word (Binder_global_collision { name; definition_index; global_index })
    | None -> ()) parameters;
  parameters

let lookup globals parameter name =
  if String.equal name parameter then Some Parameter
  else match reserved name with
    | Some target -> Some target
    | None -> Option.map (fun index -> Function index) (Hashtbl.find_opt globals name)

type operation = Make_tuple | Binary of primitive | Invoke of int

type 'scope frame = {
  operation : operation;
  whole_span : Reader.span;
  parent_path_rev : int list;
  remaining : 'scope Reader.expression list;
  next_index : int;
  completed_rev : 'scope expression list;
}

let assemble op span completed_rev =
  let form = match op, completed_rev with
    | Make_tuple, items -> Tuple (List.rev items)
    | Binary primitive, [right; left] -> Arithmetic (primitive, left, right)
    | Invoke index, [argument] -> Call (index, argument)
    | (Binary _ | Invoke _), _ -> failwith "checked application lost its arity"
  in
  { span; form }

let resolve_body globals definition_index parameter root =
  let find word = lookup globals parameter word.Reader.spelling in
  let fail path_rev word cause =
    reject_word definition_index (Some (List.rev path_rev)) word cause
  in
  let operation path_rev word args =
    let name = word.Reader.spelling in
    match find word with
    | None -> fail path_rev word (Unknown_call name)
    | Some (Parameter | Def_keyword as target) ->
        fail path_rev word (Wrong_role { name; actual_role = role_of target; required_role = Need_callable })
    | Some Tuple_head -> Make_tuple
    | Some (Builtin primitive) ->
        let actual = List.length args in
        if actual <> 2 then fail path_rev word (Primitive_arity { call_name = name; expected = 2; actual });
        Binary primitive
    | Some (Function index) ->
        let actual = List.length args in
        if actual <> 1 then fail path_rev word (Named_arity { call_name = name; expected = 1; actual });
        Invoke index
  in
  (* One frame per open application. Parent paths share tails, and only a
     reported failure materializes a root-to-leaf path. Calls keep indices. *)
  let rec visit path_rev node frames =
    let span = node.Reader.expr_span in
    match node.Reader.form with
    | Reader.Literal (_, value) -> finish { span; form = Literal value } frames
    | Reader.Reference word ->
        let name = word.Reader.spelling in
        (match find word with
        | Some Parameter -> finish { span; form = Local_slot 0 } frames
        | Some (Function _ | Builtin _ | Tuple_head | Def_keyword as target) ->
            fail path_rev word (Wrong_role { name; actual_role = role_of target; required_role = Need_local })
        | None -> fail path_rev word (Unbound_variable name))
    | Reader.Apply (word, arguments) ->
        let op = operation path_rev word arguments in
        (match arguments with
        | [] -> finish (assemble op span []) frames
        | first :: remaining ->
            let frame = { operation = op; whole_span = span; parent_path_rev = path_rev;
                          remaining; next_index = 1; completed_rev = [] } in
            visit (0 :: path_rev) first (frame :: frames))
  and finish node = function
    | [] -> node
    | frame :: outer ->
        let completed_rev = node :: frame.completed_rev in
        match frame.remaining with
        | [] -> finish (assemble frame.operation frame.whole_span completed_rev) outer
        | first :: remaining ->
            let next = { frame with remaining; completed_rev; next_index = frame.next_index + 1 } in
            visit (frame.next_index :: frame.parent_path_rev) first (next :: outer)
  in
  visit [] root []

let check ~entry program =
  let phase = ref "check" in
  try
    let declarations = Array.of_list program.Reader.definitions in
    let globals = globals_of declarations in
    let parameters = checked_parameters globals declarations in
    phase := "resolve";
    let definitions = Array.mapi (fun index decl ->
      let parameter = parameters.(index) in
      let body = resolve_body globals index parameter.Reader.spelling decl.Reader.body in
      { name = decl.Reader.name; parameter; body; declaration_span = decl.Reader.definition_span }) declarations
    in
    phase := "check";
    let selected_entry = match reserved entry with
      | Some target -> reject Entry_argument (Entry_wrong_role { name = entry; actual_role = role_of target })
      | None ->
          match Hashtbl.find_opt globals entry with
          | Some index -> index
          | None -> reject Entry_argument (Entry_missing entry)
    in
    Ok { source_bytes = program.Reader.source; selected_entry; definitions }
  with
  | Reject refusal -> Error (Refused refusal)
  | Out_of_memory -> Error (Tool_error (Reader.Host_memory !phase))
  | Stack_overflow -> Error (Tool_error (Reader.Host_stack !phase))
  | exn -> Error (Tool_error (Reader.Internal_error { phase = !phase; reason = Printexc.to_string exn }))
