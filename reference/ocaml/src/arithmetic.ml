(* Add under the paired tariff. An argument reference names its admitted
   immutable value. Only Core.bit reads an operand digit. *)

let number x = Json.Num x
let integer x = number (Nat.of_int x)
let pair (w, c) = Json.Arr [number w; number c]
let double n = Nat.add n n

let work_price a b m =
  let inputs = Nat.add (Nat.of_int a) (Nat.of_int b) in
  let p = Nat.bits (double (Nat.add inputs (Nat.of_int 2))) in
  let r = Nat.add (Nat.of_int m) Nat.one in
  Nat.add (Nat.add inputs r) (Nat.add (double (double p)) (double r))

(* Width evidence on an unfunded work quote. Both slots remain bound when
   they designate the same admitted value. *)
let work_refusal ~definition ~descriptor ~site operands a b m (w, c) price =
  let lower, upper =
    let high = Nat.add (Nat.of_int m) Nat.one in
    (if a = b && a >= 2 then high else Nat.of_int m), high
  in
  let endpoints x y =
    Json.Arr (if Nat.equal x y then [number x] else [number x; number y])
  in
  let low = Nat.sub_trunc lower c and high = Nat.sub_trunc upper c in
  let status =
    if Nat.equal high Nat.zero then "sufficient"
    else if Nat.compare low Nat.zero > 0 then "short"
    else "undetermined"
  in
  let event =
    Json.Dict ["definition", Json.Str definition; "occurrence", Json.Str site;
               "visit", integer 1]
  in
  let expression =
    Json.Dict ["formula", Json.Str "max(0,bits(x+y)-C)";
               "descriptor", Json.Str descriptor; "row", Json.Str "Add";
               "event", event; "operands", operands; "effective_c", number c]
  in
  let supplement =
    ["work_deficit", number (Nat.sub_trunc price w);
     "deficit_image", endpoints low high; "status", Json.Str status;
     "expression", expression]
  in
  (["possible_widths", endpoints lower upper; "minimum_deficit", number low]
   @ supplement), supplement

(* The sizing pass retains a carry only. The width is at least m, including
   the all-zero case (bits(0) = 1), and exceeds m precisely on a carry. *)
let sum_width view hold m =
  let carry = ref false in
  for i = 0 to m - 1 do
    let x = Core.bit view hold 1 i in
    let y = Core.bit view hold 2 i in
    carry := (x && y) || ((x || y) && !carry)
  done;
  if !carry then m + 1 else m

let stage_sum view hold m c =
  let result = Array.make c false in
  let carry = ref false in
  for i = 0 to m - 1 do
    let x = Core.bit view hold 1 i in
    let y = Core.bit view hold 2 i in
    let different = x <> y in
    result.(i) <- different <> !carry;
    carry := (x && y) || (different && !carry)
  done;
  if !carry then result.(m) <- true;
  Core.of_bits result

let add_event ~definition ~descriptor ~site ~interrupt ~prepare account view left right =
  Core.phase "quote";
  let a = Core.width left and b = Core.width right in
  let operands = Json.Arr [Json.Str (Core.id left); Json.Str (Core.id right)] in
  let m = max a b in
  let price = work_price a b m in
  let (w, c) as grant = Core.settled account in
  let witness final_hold phase extra =
    Json.Dict (["row", Json.Str "Add"; "operands", operands;
                "widths", Json.Arr [integer a; integer b];
                "work_invoice", number price; "reached", Json.Str phase;
                "final_hold", pair final_hold] @ extra)
  in
  if Nat.compare w price < 0 then begin
    Core.phase "work-refusal";
    let evidence, supplement =
      work_refusal ~definition ~descriptor ~site operands a b m grant price
    in
    Core.stop view;
    Error "work", witness (Core.outstanding account) "WorkRefusalBeforeSize" evidence, supplement
  end else begin
    let hold = Core.hold_work view price in
    let work_hold = Core.outstanding account in
    Core.phase "size";
    let width = sum_width view hold m in
    let measured = Nat.of_int width in
    let evidence = ["work_hold", pair work_hold; "measured_c", number measured;
                    "requested", pair (price, measured)] in
    if Nat.compare c measured < 0 then begin
      Core.phase "construction-refusal";
      let supplement = ["construction_deficit", number (Nat.sub_trunc measured c)] in
      let released = Core.outstanding account in
      Core.phase "cleanup";
      Core.stop view;
      Error "construction",
      witness (Core.outstanding account) "ConstructionRefusalAfterSize"
        (evidence @ ["released", pair released] @ supplement), supplement
    end else begin
      Core.reserve view hold measured;
      Core.phase "stage";
      let staged = stage_sum view hold m width in
      let live = Core.outstanding account in
      let staged_evidence =
        evidence @ ["staged", Json.Str (Core.id staged); "full_hold", pair live]
      in
      if interrupt then begin
        let prior = Core.committed account in
        let free = Core.available account in
        let supplement = ["phase", Json.Str "StagedBeforeCommit";
                          "outstanding", pair live; "prior_committed", pair prior] in
        Core.phase "cleanup";
        Core.stop view;
        Error "fixture-interrupt",
        witness (Core.outstanding account) "StagedBeforeCommit"
          (staged_evidence @ ["free_at_interrupt", pair free; "released", pair live;
                              "staging", Json.Str "discarded"] @ supplement), supplement
      end else begin
        Core.phase "commit";
        let detail = witness (Nat.zero, Nat.zero) "Committed" staged_evidence in
        let result = Ok staged, detail, [] in
        Core.commit view hold site staged (fun () -> prepare staged detail);
        result
      end
    end
  end

let sub_work_price a b m =
  let left = Nat.of_int a in
  let inputs = Nat.add left (Nat.of_int b) in
  let p = Nat.bits (double (Nat.add inputs (Nat.of_int 2))) in
  let scans = double (Nat.add (Nat.of_int m) Nat.one) in
  Nat.add (Nat.add inputs left) (Nat.add (double (double p)) scans)

(* Represent the width evidence compactly even for a large inclusive interval.
   Clipping an interval to zero preserves contiguity. Clipping a two-point
   set can identify its members, in which case retain the single image. *)
let sub_work_refusal ~definition ~descriptor ~site operands a b (w, c) price =
  let lower, upper, interval =
    if a < b then 1, 1, false
    else if a = b then 1, max 1 (a - 1), true
    else if a - b = 1 then 1, a, true
    else a - 1, a, false
  in
  let encode lo hi =
    if Nat.equal lo hi then Json.Dict ["set", Json.Arr [number lo]]
    else Json.Dict [(if interval then "interval" else "set"),
                    Json.Arr [number lo; number hi]]
  in
  let lower = Nat.of_int lower and upper = Nat.of_int upper in
  let low = Nat.sub_trunc lower c and high = Nat.sub_trunc upper c in
  let status =
    if Nat.equal high Nat.zero then "sufficient"
    else if Nat.compare low Nat.zero > 0 then "short"
    else "undetermined"
  in
  let event = Json.Dict ["definition", Json.Str definition; "occurrence", Json.Str site;
                         "visit", integer 1] in
  let term formula =
    Json.Dict ["formula", Json.Str formula; "descriptor", Json.Str descriptor;
               "row", Json.Str "Sub"; "event", event; "operands", operands;
               "effective_c", number c; "boundary", Json.Str "b";
               "scope", Json.Str "root"; "phase", Json.Str "WorkCheck"]
  in
  let demand =
    if Nat.equal lower upper then number lower else term "bits(max(x-y,0))"
  in
  ["phase", Json.Str "WorkCheck"; "primary", Json.Str "work";
   "requested_work", number price; "requested_construction", demand;
   "work_deficit", number (Nat.sub_trunc price w);
   "possible_widths", encode lower upper; "deficit_image", encode low high;
   "minimum_deficit", number low; "status", Json.Str status;
   "expression", term "max(0,bits(max(x-y,0))-C)"]

(* Each pass reads all and only the in-range digits of both ordered slots.
   The outgoing borrow at the top marks underflow for truncated subtraction. *)
let scan_difference view hold a b digit =
  let borrow = ref false in
  for i = 0 to max a b - 1 do
    let x = i < a && Core.bit view hold 1 i in
    let y = i < b && Core.bit view hold 2 i in
    let different = x <> y in
    digit i (different <> !borrow);
    borrow := (not x && y) || (not different && !borrow)
  done;
  !borrow

let difference_width view hold a b =
  let width = ref 1 in
  let underflow = scan_difference view hold a b
      (fun i set -> if set then width := i + 1) in
  if underflow then 1 else !width

let stage_difference view hold a b width =
  let result = Array.make width false in
  let underflow = scan_difference view hold a b
      (fun i set -> if i < width then result.(i) <- set) in
  (* The funded measurement gives exactly one cell on underflow. *)
  if underflow then result.(0) <- false;
  Core.of_bits result

let sub_event ~definition ~descriptor ~site ~interrupt ~prepare account view left right =
  if interrupt then invalid_arg "Sub has no scheduled interruption";
  Core.phase "quote";
  let a = Core.width left and b = Core.width right in
  let operands = Json.Arr [Json.Str (Core.id left); Json.Str (Core.id right)] in
  let price = sub_work_price a b (max a b) in
  let (w, c) as grant = Core.settled account in
  let pre = ["pre", pair grant] in
  let witness final_hold phase extra =
    Json.Dict (["row", Json.Str "Sub"; "operands", operands;
                "widths", Json.Arr [integer a; integer b];
                "work_invoice", number price; "reached", Json.Str phase;
                "final_hold", pair final_hold] @ extra)
  in
  if Nat.compare w price < 0 then begin
    Core.phase "work-refusal";
    let supplement = pre @
      sub_work_refusal ~definition ~descriptor ~site operands a b grant price in
    Core.stop view;
    Error "work", witness (Core.outstanding account) "WorkCheck" supplement, supplement
  end else begin
    let hold = Core.hold_work view price in
    let work_hold = Core.outstanding account in
    Core.phase "size";
    let width = difference_width view hold a b in
    let measured = Nat.of_int width in
    let evidence =
      ["work_hold", pair work_hold; "measured_c", number measured;
       "requested", pair (price, measured);
       "free_during_size", pair (Core.available account)]
    in
    if Nat.compare c measured < 0 then begin
      Core.phase "construction-refusal";
      let supplement =
        pre @ ["phase", Json.Str "ConstructionCheck"; "primary", Json.Str "construction";
               "requested_work", number price; "requested_construction", number measured;
               "work_deficit", number Nat.zero;
               "construction_deficit", number (Nat.sub_trunc measured c)]
      in
      let released = Core.outstanding account in
      Core.phase "cleanup";
      Core.stop view;
      Error "construction",
      witness (Core.outstanding account) "ConstructionCheck"
        (evidence @ ["released", pair released] @ supplement),
      supplement
    end else begin
      Core.reserve view hold measured;
      Core.phase "stage";
      let staged = stage_difference view hold a b width in
      let live = Core.outstanding account in
      Core.phase "commit";
      let detail = witness (Nat.zero, Nat.zero) "Commit" (pre @ evidence @
        ["staged", Json.Str (Core.id staged); "full_hold", pair live]) in
      let result = Ok staged, detail, pre in
      Core.commit view hold site staged (fun () -> prepare staged detail);
      result
    end
  end

let dispatch event ~definition ~descriptor ~site ~interrupt ~prepare account view left right =
  Core.require_event account view site left right;
  try event ~definition ~descriptor ~site ~interrupt ~prepare account view left right
  with exn -> Core.stop view; raise exn

let add = dispatch add_event
let sub = dispatch sub_event
