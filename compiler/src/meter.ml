type structural = Entry | Literal | Variable | Call | Return

type event =
  | Structural of structural
  | Tuple
  | Arithmetic of Checker.primitive
  | Wrong_kind of Checker.primitive

type invoice = { a : Natural.t; r : Natural.t; t : Natural.t; w : Natural.t; total : Natural.t }
type bill = { event : event; invoice : invoice }
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

type row =
  | Entry_row | Literal_row | Variable_row | Call_row | Return_row
  | Add_row | Sub_row | Mul_row | Wrong_kind_row | Tuple_row

type component =
  | Zero | One | Left_part | Sum_parts | Max_part | Max_plus_one
  | Product_parts | Field_sum | Width_plus_one

(* The sole production price table. Columns are A, R, T and W in that order.
   CHARGES.md B-C04 through B-C07. Prices are provisional and not adopted. *)
let provisional_prices = [
  Entry_row,      (Zero,      Zero,           Zero, One);
  Literal_row,    (Zero,      Zero,           Zero, One);
  Variable_row,   (Zero,      Zero,           Zero, One);
  Call_row,       (Zero,      Zero,           Zero, One);
  Return_row,     (Zero,      Zero,           Zero, Zero);
  Add_row,        (Sum_parts, Max_plus_one,   Zero, Max_part);
  Sub_row,        (Sum_parts, Left_part,      Zero, Max_part);
  Mul_row,        (Sum_parts, Sum_parts,      Zero, Product_parts);
  Wrong_kind_row, (Sum_parts, Zero,           Zero, One);
  Tuple_row,      (Field_sum, Width_plus_one, Zero, Zero);
]

let row_of = function
  | Structural Entry -> Entry_row
  | Structural Literal -> Literal_row
  | Structural Variable -> Variable_row
  | Structural Call -> Call_row
  | Structural Return -> Return_row
  | Arithmetic Checker.Add -> Add_row
  | Arithmetic Checker.Sub -> Sub_row
  | Arithmetic Checker.Mul -> Mul_row
  | Wrong_kind _ -> Wrong_kind_row
  | Tuple -> Tuple_row

type measures = { left : Natural.t; right : Natural.t; width : Natural.t; field_sum : Natural.t }

let empty = { left = Natural.zero; right = Natural.zero; width = Natural.zero; field_sum = Natural.zero }
let maximum x y = if Natural.compare x y >= 0 then x else y

let price event measures =
  let component = function
    | Zero -> Natural.zero
    | One -> Natural.one
    | Left_part -> measures.left
    | Sum_parts -> Natural.add measures.left measures.right
    | Max_part -> maximum measures.left measures.right
    | Max_plus_one -> Natural.add (maximum measures.left measures.right) Natural.one
    | Product_parts -> Natural.mul measures.left measures.right
    | Field_sum -> measures.field_sum
    | Width_plus_one -> Natural.add measures.width Natural.one
  in
  let arg, result, temp, work = List.assoc (row_of event) provisional_prices in
  let a = component arg and r = component result and t = component temp and w = component work in
  let total = Natural.add (Natural.add a r) (Natural.add t w) in
  Known { event; invoice = { a; r; t; w; total } }

let structural event = price (Structural event) empty

let natural_bits op ~left ~right =
  if Natural.compare left Natural.zero = 0 || Natural.compare right Natural.zero = 0 then
    invalid_arg "Meter.natural_bits requires positive measured widths";
  price (Arithmetic op) { empty with left; right }

let part = function
  | Some n -> maximum Natural.one (Natural.bit_length n)
  | None -> Natural.one

let arithmetic op x y =
  let x_nat = Value.as_natural x and y_nat = Value.as_natural y in
  let left = part x_nat and right = part y_nat in
  match x_nat, y_nat with
  | Some _, Some _ -> natural_bits op ~left ~right
  | None, _ | Some _, None -> price (Wrong_kind op) { empty with left; right }

let tuple fields =
  let add_field (width, total) v =
    Natural.add width Natural.one, Natural.add total (part (Value.as_natural v))
  in
  let width, field_sum = List.fold_left add_field (Natural.zero, Natural.zero) fields in
  price Tuple { empty with width; field_sum }

type 'location state = Running of accounting | Stopped of 'location stop
type 'location t = 'location state Atomic.t

let create ~budget = Atomic.make (Running { budget; used = Natural.zero; remaining = budget })

let accounting meter =
  match Atomic.get meter with Running state -> state | Stopped stop -> stop.accounting

let stopped meter =
  match Atomic.get meter with Running _ -> None | Stopped stop -> Some stop

let stop_code = function
  | Insufficient _ -> "fuel.insufficient"
  | Bound_unavailable _ -> "fuel.bound_unavailable"

let pay meter ~at estimate ~build =
  (* The complete replacement state is ready before the single commit.
     Retrying a contended commit never retries the construction callback. *)
  let rec reserve () =
    let previous = Atomic.get meter in
    match previous with
    | Stopped stop -> Error stop
    | Running balance ->
        let stop failed_event cause =
          let reason = { cause; failed_event; at; failed_operation_debit = Natural.zero; accounting = balance } in
          if Atomic.compare_and_set meter previous (Stopped reason) then Error reason else reserve ()
        in
        match estimate with
        | Unavailable { event; reason } ->
            if String.trim reason = "" then invalid_arg "missing unavailable-bound reason";
            stop event (Bound_unavailable reason)
        | Known bill ->
            let cost = bill.invoice.total in
            if Natural.compare balance.remaining cost < 0 then stop bill.event (Insufficient bill.invoice)
            else if Natural.compare cost Natural.zero = 0 then Ok bill
            else
              let updated = { balance with used = Natural.add balance.used cost;
                                           remaining = Natural.sub balance.remaining cost } in
              if Atomic.compare_and_set meter previous (Running updated) then Ok bill else reserve ()
  in
  match reserve () with
  | Error stop -> Error stop
  | Ok bill -> Ok (build bill)
