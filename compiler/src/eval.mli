(** Piece 14 runs structural milestone B forms in an admitted program. *)
type location

val definition_index : location -> int
val expression_path : location -> int list option
val source_offset : location -> int option

(** Piece 15 supplies this internal dispatch. Both operands have already
    completed in written order. The handler owns the primitive payment. *)
type 'scope primitive_dispatch =
  meter:location Meter.t -> at:location -> Checker.primitive ->
  left:'scope Value.t -> right:'scope Value.t ->
  ('scope Value.t, location Meter.stop) result

module Make (Store : sig
  type scope
  val natural : Natural.t -> scope Value.t
  val tuple : scope Value.t array -> scope Value.t
end) : sig
  (** Use the same store as the reader and a fresh meter for this invocation.
      The entry callback runs after input interning, just before the Entry invoice.
      The caller can inspect accounting after a return or fuel stop. *)
  val run :
    ?on_entry_attempt:(unit -> unit) -> meter:location Meter.t -> primitive:Store.scope primitive_dispatch ->
    input:Natural.t -> Store.scope Checker.program ->
    (Store.scope Value.t, location Meter.stop) result
end

(** Normal milestone B execution, with metered add, sub and mul installed. *)
module With_primitives (Store : sig
  type scope
  val none : scope Value.t
  val natural : Natural.t -> scope Value.t
  val tuple : scope Value.t array -> scope Value.t
end) : sig
  val run :
    ?on_entry_attempt:(unit -> unit) -> meter:location Meter.t -> input:Natural.t -> Store.scope Checker.program ->
    (Store.scope Value.t, location Meter.stop) result
end
