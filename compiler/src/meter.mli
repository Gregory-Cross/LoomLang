(** Milestone B meter. The reviewed prices are provisional and not owner-adopted. *)
type structural = Entry | Literal | Variable | Call | Return

type event =
  | Structural of structural
  | Tuple
  | Arithmetic of Checker.primitive
  | Wrong_kind of Checker.primitive

type invoice = private { a : Natural.t; r : Natural.t; t : Natural.t; w : Natural.t; total : Natural.t }
type bill = private { event : event; invoice : invoice }
type estimate = Known of bill | Unavailable of { event : event; reason : string }

type accounting = { budget : Natural.t; used : Natural.t; remaining : Natural.t }
type stop_cause = Insufficient of invoice | Bound_unavailable of string

type 'location stop = {
  cause : stop_cause;
  failed_event : event;
  at : 'location;
  failed_operation_debit : Natural.t;
  accounting : accounting;
}

type 'location t

val create : budget:Natural.t -> 'location t
val accounting : 'location t -> accounting
val stopped : 'location t -> 'location stop option
val stop_code : stop_cause -> string

(** Quote obtained operands or a single structural event. No Loom result is
    built during quotation. Every current B row has a known exact invoice. *)
val structural : structural -> estimate
val tuple : 'scope Value.t list -> estimate
val arithmetic : Checker.primitive -> 'scope Value.t -> 'scope Value.t -> estimate

(** The same B-C05 row for known mathematical operand widths. Both widths
    use the paper's minimum of one. Zero is an invalid measurement. *)
val natural_bits : Checker.primitive -> left:Natural.t -> right:Natural.t -> estimate

(** Latch a stop, or commit the entire debit before calling [build] once.
    An exception from [build] propagates with the debit retained. *)
val pay : 'location t -> at:'location -> estimate -> build:(bill -> 'a) -> ('a, 'location stop) result
