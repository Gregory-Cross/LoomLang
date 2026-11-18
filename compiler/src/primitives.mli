(** Arithmetic on the two values obtained by the evaluator. *)
module Make (Store : sig
  type scope
  val none : scope Value.t
  val natural : Natural.t -> scope Value.t
end) : sig
  val dispatch :
    meter:'location Meter.t -> at:'location -> Checker.primitive ->
    left:Store.scope Value.t -> right:Store.scope Value.t ->
    (Store.scope Value.t, 'location Meter.stop) result
end
