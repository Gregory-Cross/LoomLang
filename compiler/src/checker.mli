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

(** Only a successful whole-program check constructs an admitted program. *)
type 'scope program

val check : entry:string -> 'scope Reader.program -> ('scope program, error) result

(** The B-O05 code and named facts. The node location is supplied by [at]. *)
val describe : cause -> string * (string * string) list

val source : 'scope program -> string
val entry_index : 'scope program -> int
val definition_count : 'scope program -> int
val definition_at : 'scope program -> int -> 'scope definition option
