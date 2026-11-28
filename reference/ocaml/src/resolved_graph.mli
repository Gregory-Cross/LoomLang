(** Admission of canonical resolved graph bytes. Before entry, the caller
    verifies scheduled_bytes against the independent digest from the start.
    Identical bytes still need valid canonical syntax, resolved edges and a
    known descriptor with a row for entry and each occurrence. *)
type node = Local_parameter | Literal of string | Add of int * int | Sub of int * int
type t = private { nodes : node list; body : int }
type refusal = Off_schedule | Malformed | Unknown_profile | Missing_row

(** The operation names are Entry, Local, Literal, Add and Sub. *)
val operation_allowed : descriptor:string -> string -> bool
val admit : descriptor:string -> scheduled_bytes:string -> string -> (t, refusal) result
