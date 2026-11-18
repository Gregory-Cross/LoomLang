(** Immutable milestone B values. A store's scope prevents a tuple from
    acquiring children from a different interner. *)
type 'scope t

type kind = Natural | Tuple | Builtin_none
type frame_error = Reserved_sequence | Unknown_kind | Malformed_frame

val kind : 'scope t -> kind
val as_natural : 'scope t -> Natural.t option
val tuple_width : 'scope t -> int option

(** Zero-based host position. A wrong kind or out-of-range position gives
    builtin none. The width distinguishes absence from a stored none. *)
val field : 'scope t -> int -> 'scope t

(** Content equality also works across independently constructed stores. *)
val equal : 'left t -> 'right t -> bool

(** The local B-value-v1 fingerprint. Collisions require a content check. *)
val hash : 'scope t -> int

(** One local encoding frame, including its LF. Tuple children follow in
    position order. The format and hash inputs are specified in VALUES.md. *)
val local_header : 'scope t -> string

module Make () : sig
  type scope

  val none : scope t
  val natural : Natural.t -> scope t

  (** Takes a snapshot of the supplied ordered fields. *)
  val tuple : scope t array -> scope t

  (** Read one local frame with its already obtained children. An S tag is
      reserved. Errors add no value to the store. *)
  val of_local_frame : string -> scope t array -> (scope t, frame_error) result

  (** Host-side verification inventory, including builtin none. *)
  val interned_count : unit -> int
end
