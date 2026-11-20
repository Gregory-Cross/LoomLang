type location = { definition : int; reversed_path : int list option; offset : int option }

let definition_index at = at.definition
let expression_path at = Option.map List.rev at.reversed_path
let source_offset at = at.offset

type 'scope primitive_dispatch =
  meter:location Meter.t -> at:location -> Checker.primitive ->
  left:'scope Value.t -> right:'scope Value.t ->
  ('scope Value.t, location Meter.stop) result

type 's activation = { owner : int; argument : 's Value.t }

type 's frame =
  | Return_body of location
  | Call_argument of location * int
  | Tuple_field of 's activation * location * int * 's Checker.expression list * 's Value.t list
  | Primitive_left of 's activation * location * Checker.primitive * 's Checker.expression
  | Primitive_right of location * Checker.primitive * 's Value.t

exception Exhausted of location Meter.stop

let obtained = function Ok value -> value | Error stop -> raise (Exhausted stop)

let expression_site activation path expression =
  { definition = activation.owner; reversed_path = Some path;
    offset = Some expression.Checker.span.Reader.start_pos.Reader.source_offset }

let child_path parent index =
  match parent.reversed_path with
  | Some path -> index :: path
  | None -> invalid_arg "Eval: an entry site has no expression children"

module Make (Store : sig
  type scope
  val natural : Natural.t -> scope Value.t
  val tuple : scope Value.t array -> scope Value.t
end) = struct
  let run ?(on_entry_attempt = fun () -> ()) ~meter ~(primitive : Store.scope primitive_dispatch) ~input program =
    let pay at estimate build = obtained (Meter.pay meter ~at estimate ~build) in
    let structural at event = pay at (Meter.structural event) (fun _ -> ()) in
    let rec enter index argument stack =
      match Checker.definition_at program index with
      | None -> invalid_arg "Eval: invalid admitted definition index"
      | Some definition ->
          let activation = { owner = index; argument } in
          let body = definition.Checker.body in
          let at = expression_site activation [] body in
          visit activation at body (Return_body at :: stack)
    and visit activation at expression stack =
      match expression.Checker.form with
      | Checker.Literal value ->
          structural at Meter.Literal;
          deliver value stack
      | Checker.Local_slot 0 ->
          structural at Meter.Variable;
          deliver activation.argument stack
      | Checker.Local_slot _ -> invalid_arg "Eval: invalid admitted unary slot"
      | Checker.Call (index, argument) ->
          visit_child activation at 0 argument (Call_argument (at, index) :: stack)
      | Checker.Tuple fields ->
          next_field activation at 0 [] fields stack
      | Checker.Arithmetic (op, left, right) ->
          visit_child activation at 0 left (Primitive_left (activation, at, op, right) :: stack)
    and visit_child activation parent index expression stack =
      let at = expression_site activation (child_path parent index) expression in
      visit activation at expression stack
    and next_field activation at index reversed_values fields stack =
      match fields with
      | [] ->
          let value = pay at (Meter.tuple reversed_values) (fun _ ->
            Store.tuple (Array.of_list (List.rev reversed_values))) in
          deliver value stack
      | field :: rest ->
          let frame = Tuple_field (activation, at, index + 1, rest, reversed_values) in
          visit_child activation at index field (frame :: stack)
    and deliver value stack =
      match stack with
      | [] -> value
      | Return_body at :: rest ->
          structural at Meter.Return;
          deliver value rest
      | Call_argument (at, target) :: rest ->
          structural at Meter.Call;
          enter target value rest
      | Tuple_field (activation, at, index, fields, reversed) :: rest ->
          next_field activation at index (value :: reversed) fields rest
      | Primitive_left (activation, at, op, right) :: rest ->
          visit_child activation at 1 right (Primitive_right (at, op, value) :: rest)
      | Primitive_right (at, op, left) :: rest ->
          let result = obtained (primitive ~meter ~at op ~left ~right:value) in
          deliver result rest
    in
    let argument = Store.natural input and index = Checker.entry_index program in
    let entry = { definition = index; reversed_path = None; offset = None } in
    try
      on_entry_attempt ();
      structural entry Meter.Entry;
      Ok (enter index argument [])
    with Exhausted stop -> Error stop
end

module With_primitives (Store : sig
  type scope
  val none : scope Value.t
  val natural : Natural.t -> scope Value.t
  val tuple : scope Value.t array -> scope Value.t
end) = struct
  module Frames = Make (Store)
  module Arithmetic = Primitives.Make (Store)

  let run ?on_entry_attempt ~meter ~input program =
    Frames.run ?on_entry_attempt ~meter ~primitive:Arithmetic.dispatch ~input program
end
