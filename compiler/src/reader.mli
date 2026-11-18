type position = { source_offset : int; line : int; column : int }
type span = { start_pos : position; end_pos : position }
type word = { spelling : string; word_span : span }

type 'scope expression = { form : 'scope form; expr_span : span }
and 'scope form =
  | Literal of string * 'scope Value.t
  | Reference of word
  | Apply of word * 'scope expression list

type 'scope definition = {
  name : word;
  parameters : word list;
  body : 'scope expression;
  definition_span : span;
}

type 'scope program = {
  source : string;
  definitions : 'scope definition list;
  eof : position;
}

type actual = Token of string | End_of_source

type refusal =
  | Encoding
  | Character of int
  | Noncanonical_natural of string
  | Syntax of { expected : string; actual : actual }

type fault =
  | Source_io of { operation : string; system_error : string }
  | Source_limit of { limit : Natural.t; observed_at_least : Natural.t }
  | Host_memory of string
  | Host_stack of string
  | Internal_error of { phase : string; reason : string }

type error = Refused of position * refusal | Tool_error of fault

val error_code : error -> string
val default_source_limit : Natural.t

module Make (Store : sig
  type scope
  val natural : Natural.t -> scope Value.t
end) : sig
  (** Read a literal file path in binary mode. Successful output covers
      all declarations through EOF and retains the original source bytes. *)
  val read_file :
    ?max_source_bytes:Natural.t -> string -> (Store.scope program, error) result

  (** Same byte limit, grammar, positions and ordering for an in-memory source. *)
  val read_bytes :
    ?max_source_bytes:Natural.t -> string -> (Store.scope program, error) result
end
