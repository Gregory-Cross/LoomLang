let () =
  if Sys.int_size <> 63 then failwith "Core requires 63-bit OCaml ints"

type pair = Nat.t * Nat.t
type value = { reference : string; header_width : int; payload : bool array }

let id v = v.reference
let width v = v.header_width

(* Admission and construction work on private, unprotected input. Once installed
   the payload has no write route and its header and identity stand separately. *)
let empty_bits = [||]

let make_value digits bits =
  { reference = "nat:" ^ digits;
    header_width = max 1 (Array.length bits);
    payload = bits }

let value digits =
  let n = String.length digits in
  if n = 0 || (n > 1 && digits.[0] = '0')
     || not (String.for_all (fun d -> d >= '0' && d <= '9') digits)
  then invalid_arg "Core.value: expected canonical decimal";
  if digits = "0" then make_value digits empty_bits
  else
    let quotient = Bytes.of_string digits in
    let first = ref 0 and bits_reversed = ref [] in
    while !first < n do
      let remainder = ref 0 in
      for i = !first to n - 1 do
        let d = 10 * !remainder + Char.code (Bytes.get quotient i) - 48 in
        Bytes.set quotient i (Char.chr (48 + d / 2));
        remainder := d mod 2
      done;
      bits_reversed := (!remainder = 1) :: !bits_reversed;
      if Bytes.get quotient !first = '0' then incr first
    done;
    make_value digits (Array.of_list (List.rev !bits_reversed))

let of_bits input =
  let count = ref (Array.length input) in
  while !count > 0 && not input.(!count - 1) do decr count done;
  if !count = 0 then make_value "0" empty_bits
  else
    let bits = Array.sub input 0 !count in
    let n = ref Nat.zero in
    for i = !count - 1 downto 0 do
      let doubled = Nat.add !n !n in
      n := if bits.(i) then Nat.add doubled Nat.one else doubled
    done;
    make_value (Nat.to_decimal !n) bits

type settled = {
  remaining : pair;
  total : pair;
  latest : pair;
  reversed_entries : (string * (value * Json.t)) list;
}

type account = { grant : pair; mutable current : state }
and state = { ledger : settled; mutable status : status }
and status = Idle | Open of view | Held of hold | Preparing of hold | Terminal
and view = { run : account; event : string; operands : value list }
and hold = { owner : view; work : Nat.t; mutable construction : Nat.t option }

let zero_pair = Nat.zero, Nat.zero
let account grant =
  { grant; current = { ledger = { remaining = grant; total = zero_pair;
                                  latest = zero_pair; reversed_entries = [] };
                       status = Idle } }

let settled a = a.current.ledger.remaining
let committed a = a.current.ledger.total
let last a = a.current.ledger.latest
let prefix a = List.rev_map fst a.current.ledger.reversed_entries
let records a = List.rev_map snd a.current.ledger.reversed_entries
let latest_record a =
  match a.current.ledger.reversed_entries with
  | [] -> None
  | (_, record) :: _ -> Some record

let outstanding a =
  match a.current.status with
  | Idle | Open _ | Terminal -> zero_pair
  | Held h | Preparing h -> h.work, Option.value h.construction ~default:Nat.zero

let available a =
  let w, c = settled a in
  let held_w, held_c = outstanding a in
  Nat.sub_trunc w held_w, Nat.sub_trunc c held_c

let view run event operands =
  (match run.current.status with
   | Held h | Preparing h -> invalid_arg ("Core.view: outstanding credit for " ^ h.owner.event)
   | Terminal -> invalid_arg "Core.view: terminal account"
   | Idle | Open _ -> ());
  let v = { run; event; operands } in
  run.current.status <- Open v;
  v

(* The arithmetic invoice, reservations and accessor must refer to the same
   dispatch, even when another account has an identical balance and site. *)
let require_event account view site left right =
  match account.current.status, view.operands with
  | Open active, [first; second] when active == view && view.run == account
      && view.event = site && first == left && second == right -> ()
  | _ -> invalid_arg "Core: mismatched event operands or account"

let hold_work v work =
  (match v.run.current.status with
   | Open active when active == v -> ()
   | _ -> invalid_arg "Core.hold_work: inactive view");
  if Nat.compare work (fst (available v.run)) > 0 then
    invalid_arg "Core.hold_work: insufficient credit";
  let h = { owner = v; work; construction = None } in
  v.run.current.status <- Held h;
  h

let require_live v h =
  match v.run.current.status with
  | Held active when active == h && h.owner == v -> ()
  | _ -> invalid_arg "Core: inactive or foreign capability"

let reserve v h construction =
  require_live v h;
  (match h.construction with
   | Some _ -> invalid_arg "Core.reserve: already reserved"
   | None -> ());
  if Nat.compare construction (snd (available v.run)) > 0 then
    invalid_arg "Core.reserve: insufficient credit";
  h.construction <- Some construction

let release v h =
  require_live v h;
  v.run.current.status <- Idle

let stop v =
  let state = v.run.current in
  match state.status with
  | Open active when active == v -> state.status <- Terminal
  | Held h when h.owner == v -> state.status <- Terminal
  | Terminal -> ()
  | _ -> invalid_arg "Core.stop: inactive view"

let commit v h site value prepare =
  require_live v h;
  if site <> v.event then invalid_arg "Core.commit: site differs from event";
  let c = match h.construction with
    | Some c -> c
    | None -> invalid_arg "Core.commit: incomplete reservation"
  in
  let a = v.run and w = h.work in
  let before = a.current in
  let next =
    try
      (* The witness may inspect the live reservation and previous prefix.
         It cannot mutate the reservation or open another event. *)
      before.status <- Preparing h;
      let record = value, prepare () in
      let grant_w, grant_c = a.grant and total_w, total_c = before.ledger.total in
      let next_w = Nat.add total_w w and next_c = Nat.add total_c c in
      let ledger = {
        remaining = (Nat.sub_trunc grant_w next_w, Nat.sub_trunc grant_c next_c);
        total = (next_w, next_c);
        latest = (w, c);
        reversed_entries = (site, record) :: before.ledger.reversed_entries
      } in
      { ledger; status = Idle }
    with exn ->
      before.status <- Terminal;
      raise exn
  in
  a.current <- next

let probe = ref (fun (_ : string) (_ : int) (_ : string) (_ : string) (_ : int) -> ())
let current_phase = ref "admission"
let on_probe f = probe := f
let phase p =
  if Probe_switch.enabled then begin
    current_phase := p;
    !probe p 0 "" "phase" (-1)
  end

let observe slot v operation index =
  if Probe_switch.enabled then !probe !current_phase slot v.reference operation index

let operand v slot =
  match slot, v.operands with
  | 1, first :: _ -> first
  | 2, _ :: second :: _ -> second
  | _ -> invalid_arg "Core: absent operand slot"

(* Every event-time elimination of protected data passes these three observation
   points. The physical array may be shared. Attribution follows the use. *)
let extract slot v =
  let a = Sys.opaque_identity v.payload in
  observe slot v "extract" (-1);
  a

let length slot v a =
  let n = Array.length a in
  observe slot v "length" (-1);
  n

let load slot v a index =
  let b = Array.unsafe_get a index in
  observe slot v "load" index;
  b

let bit v h slot index =
  require_live v h;
  let x = operand v slot in
  if index < 0 then invalid_arg "Core.bit: negative index";
  if index >= x.header_width then false
  else
    let a = extract slot x in
    let n = length slot x a in
    if index < n then load slot x a index else false

let calibration_read v slot =
  if not Probe_switch.enabled then invalid_arg "Core: calibration requires probe build";
  let x = operand v slot in
  let a = extract slot x in
  let n = length slot x a in
  if n > 0 then ignore (Sys.opaque_identity (load slot x a 0))

let stale_control () =
  let grant = Nat.of_int 8, Nat.of_int 8 in
  let a = account grant and b = account grant in
  let one = value "1" in
  let open_event a = view a "same-event" [one; one] in
  let u = open_event a and v = open_event b in
  let hu = hold_work u Nat.one and hv = hold_work v Nat.one in
  let rejected f =
    try ignore (f ()); false with
    | Invalid_argument reason -> reason = "Core: inactive or foreign capability"
  in
  let read v h () = bit v h 1 0 in
  let positives = bit u hu 1 0 && bit v hv 1 0 in
  let foreign = rejected (read u hv) && rejected (read v hu) in
  release u hu;
  let released = rejected (read u hu) in
  let next = open_event a in
  let fresh = hold_work next Nat.one in
  let stale = rejected (read next hu) && rejected (read u fresh) in
  reserve next fresh Nat.one;
  let live = bit next fresh 1 0 in
  commit next fresh "same-event" one (fun () -> Json.Null);
  let closed = rejected (read next fresh) in
  release v hv;
  positives && foreign && released && stale && live && closed
