type pair = Nat.t * Nat.t
type value

val value : string -> value
val of_bits : bool array -> value
val id : value -> string
val width : value -> int

type account
type view
type hold

val account : pair -> account
val available : account -> pair
val settled : account -> pair
val outstanding : account -> pair
val committed : account -> pair
val last : account -> pair
val prefix : account -> string list
val latest_record : account -> (value * Json.t) option
val records : account -> (value * Json.t) list
val view : account -> string -> value list -> view
val require_event : account -> view -> string -> value -> value -> unit
val hold_work : view -> Nat.t -> hold
val reserve : view -> hold -> Nat.t -> unit
val release : view -> hold -> unit
val stop : view -> unit
val commit : view -> hold -> string -> value -> (unit -> Json.t) -> unit
val bit : view -> hold -> int -> int -> bool

val calibration_read : view -> int -> unit
val phase : string -> unit
val on_probe : (string -> int -> string -> string -> int -> unit) -> unit
val stale_control : unit -> bool
