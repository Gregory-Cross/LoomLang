(** Project-owned, immutable mathematical naturals, limited by host resources,
    with no chosen maximum value. This module is not a metered evaluator. *)
type t

val zero : t
val one : t

(** Accept one or more ASCII decimal digits. Leading zeroes are accepted;
    signs, whitespace and separators are rejected. *)
val of_decimal : string -> (t, string) result

(** Canonical decimal digits, with zero printed as ["0"]. *)
val to_decimal : t -> string

(** Exactly [-1], [0] or [1]. *)
val compare : t -> t -> int

val add : t -> t -> t

(** Exact mathematical bit length, itself a natural: zero has length zero.
    Exposes the argument-size component needed by D-EV-1 without imposing a
    machine-integer bound on later meter arithmetic or choosing its tariff. *)
val bit_length : t -> t
