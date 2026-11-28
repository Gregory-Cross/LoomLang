(* nat.mli - the producer's carrier for the naturals N = {0,1,2,...}: exact at every size, never wrapping.
   Part of the bake-off OCaml producer (Claude Bake-ocaml, card 0001).

   The carrier [t] is abstract: other modules reach a natural only through the operations below, so every value
   keeps the representation invariant of nat.ml (normalized limbs) and no operation can wrap. *)

type t

val zero : t
val one : t

val of_int : int -> t
(** [of_int n] is n, for a machine int n >= 0 (used for small constants and bit counts only).
    Raises [Invalid_argument] on a negative n. *)

val of_decimal : string -> t option
(** [of_decimal s] is the natural that [s] spells when [s] is a nonempty string of ASCII decimal digits with no
    leading zero (except "0" itself), and [None] for any other string. *)

val to_decimal : t -> string
(** The exact decimal digits: no sign, no leading zero. *)

val compare : t -> t -> int
val equal : t -> t -> bool
val max : t -> t -> t
val min : t -> t -> t

val add : t -> t -> t
(** x + y. *)

val sub_trunc : t -> t -> t
(** [sub_trunc x y] = max(x - y, 0). *)

val bits : t -> t
(** The binary width: bits 0 = 1, and bits n counts the binary digits of n > 0. *)

val sum_bits : t -> t -> t
(** [sum_bits x y] = bits (add x y), measured without forming x + y: one read-only pass over the limbs of x and y
    whose only state is two machine words (a carry and the latest limb sum); no natural is allocated for x + y. *)

val diff_bits : t -> t -> t
(** [diff_bits x y] = bits (sub_trunc x y), measured without forming max(x - y, 0): a read-only comparison, then
    one read-only pass whose only state is three machine words (a borrow, and the index and value of the highest
    nonzero difference limb seen so far); no natural is allocated for the difference. *)
