(* json.mli - JSON values and their text (RFC 8259) for records.jsonl. With Emit and Nat.to_decimal it forms the
   trusted bridge from the producer's values to the bytes of the output file. Part of the bake-off OCaml producer
   (Claude Bake-ocaml, card 0001). *)

type t =
  | Null
  | Str of string
  | Num of Nat.t
  | Num_ref of string (* Immutable natural identity, expanded only by the serializer. *)
  | Arr of t list
  | Dict of (string * t) list (* a JSON object: members in this order *)

exception Duplicate_name of string

val add_to_buffer : Buffer.t -> t -> unit
(** Appends the text of a value with no whitespace: a string with '"', '\\' and the control characters below 0x20
    escaped, a natural as its exact decimal digits, members in the given order. Raises [Duplicate_name] if an object
    would carry one name twice. *)
