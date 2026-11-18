(* Each fixture explicitly schedules obtained events. The callback observes
   the debit and, for value events, performs a single construction/lookup. *)
open Meter

let nat text = match Natural.of_decimal text with Ok n -> n | Error why -> invalid_arg why
let decimal = Natural.to_decimal

let primitive = function
  | "add" -> Checker.Add | "sub" -> Checker.Sub | "mul" -> Checker.Mul
  | _ -> invalid_arg "unknown arithmetic fixture"

let primitive_name = function Checker.Add -> "add" | Checker.Sub -> "sub" | Checker.Mul -> "mul"

let event_name = function
  | Structural Entry -> "entry" | Structural Literal -> "literal"
  | Structural Variable -> "variable" | Structural Call -> "call" | Structural Return -> "return"
  | Tuple -> "tuple" | Arithmetic op -> primitive_name op | Wrong_kind op -> "wrong-kind/" ^ primitive_name op

let invoice_text event i =
  event_name event ^ "(" ^ String.concat "," (List.map decimal [i.a; i.r; i.t; i.w; i.total]) ^ ")"

let show_estimate = function
  | Known b -> invoice_text b.event b.invoice
  | Unavailable { event; reason } -> event_name event ^ "(?" ^ reason ^ ")"

let show_balance state = decimal state.used ^ "," ^ decimal state.remaining

let same_balance x y =
  Natural.compare x.budget y.budget = 0 && Natural.compare x.used y.used = 0
  && Natural.compare x.remaining y.remaining = 0

let power_of_two exponent =
  if exponent < 0 then invalid_arg "negative power fixture";
  let rec power n =
    if n = 0 then Natural.one
    else
      let half = power (n / 2) in
      let square = Natural.mul half half in
      if n mod 2 = 0 then square else Natural.add square square
  in
  power exponent

exception Callback_fault

let run_case budget_text fault_at steps =
  let module Store = Value.Make () in
  let budget = nat budget_text in
  let meter = create ~budget in
  let value = function
    | "none" -> Store.none
    | "empty" -> Store.tuple [||]
    | "nested" -> let empty = Store.tuple [||] in Store.tuple [|empty; empty|]
    | text when String.starts_with ~prefix:"2^" text ->
        let exponent = int_of_string (String.sub text 2 (String.length text - 2)) in
        Store.natural (power_of_two exponent)
    | text -> Store.natural (nat text)
  in
  let prepare parts =
    let noop _ = () in
    match parts with
    | ["entry"] -> (fun () -> structural Entry), noop
    | ["literal"] -> (fun () -> structural Literal), noop
    | ["variable"] -> (fun () -> structural Variable), noop
    | ["call"] -> (fun () -> structural Call), noop
    | ["return"] -> (fun () -> structural Return), noop
    | "tuple" :: fields ->
        let obtained = List.map value fields in
        (fun () -> tuple obtained), (fun _ -> ignore (Store.tuple (Array.of_list obtained)))
    | ["bits"; op; left; right] ->
        let op = primitive op and left = nat left and right = nat right in
        (fun () -> natural_bits op ~left ~right), noop
    | ["unavailable"; op; reason] ->
        let event = Arithmetic (primitive op) in
        (fun () -> Unavailable { event; reason }), (fun _ -> failwith "unavailable bound permitted work")
    | [name; left; right] ->
        let op = primitive name and x = value left and y = value right in
        let construct b =
          match b.event, Value.as_natural x, Value.as_natural y with
          | Arithmetic actual, Some a, Some c when actual = op ->
              let result = match op with
                | Checker.Add -> Natural.add a c | Checker.Sub -> Natural.sub a c | Checker.Mul -> Natural.mul a c
              in
              ignore (Store.natural result)
          | Wrong_kind actual, _, _ when actual = op -> ignore Store.none
          | (Structural _ | Tuple | Arithmetic _ | Wrong_kind _), _, _ -> failwith "wrong construction event"
        in
        (fun () -> arithmetic op x y), construct
    | _ -> invalid_arg "bad meter step"
  in
  let step index raw =
    let quote, construct = prepare (String.split_on_char ',' raw) in
    let inventory = Store.interned_count () and before = accounting meter in
    let estimate = quote () in
    if Store.interned_count () <> inventory || not (same_balance (accounting meter) before) then
      failwith "quotation changed state";
    let calls = ref 0 and during = ref "-" in
    let build b =
      incr calls;
      during := show_balance (accounting meter);
      if fault_at = Some index then raise Callback_fault;
      construct b
    in
    let status, effective, location, failed_debit =
      try
        match pay meter ~at:index estimate ~build with
        | Ok () -> "paid", show_estimate estimate, string_of_int index, "-"
        | Error stop ->
            let billed = match stop.cause with
              | Insufficient i -> invoice_text stop.failed_event i
              | Bound_unavailable reason -> event_name stop.failed_event ^ "(?" ^ reason ^ ")"
            in
            (match stopped meter with
            | Some saved when saved.at = stop.at && stop_code saved.cause = stop_code stop.cause
                              && same_balance (accounting meter) stop.accounting -> ()
            | Some _ | None -> failwith "stop not retained");
            if !calls <> 0 || Store.interned_count () <> inventory then failwith "unpaid construction";
            stop_code stop.cause, billed, string_of_int stop.at, decimal stop.failed_operation_debit
      with Callback_fault -> "callback-fault", show_estimate estimate, string_of_int index, "-"
    in
    let after = accounting meter in
    if Natural.compare after.budget budget <> 0 ||
       Natural.compare (Natural.add after.used after.remaining) budget <> 0 then failwith "fuel conservation";
    let new_nodes = Store.interned_count () - inventory in
    String.concat "|" [show_estimate estimate; status; effective; location; failed_debit;
                       show_balance after; string_of_int !calls; !during; string_of_int new_nodes]
  in
  String.concat ";" (("budget=" ^ budget_text) :: List.mapi step (String.split_on_char ';' steps))

let run requests actual =
  let count = ref 0 in
  In_channel.with_open_bin requests (fun input ->
    Out_channel.with_open_bin actual (fun output ->
      let rec records () =
        match In_channel.input_line input with
        | None -> ()
        | Some row ->
            let row = if String.ends_with ~suffix:"\r" row then String.sub row 0 (String.length row - 1) else row in
            (match String.split_on_char '\t' row with
            | [id; "trace"; budget; fault; steps] ->
                let fault_at = if fault = "-" then None else Some (int_of_string fault) in
                Printf.fprintf output "%s\t%s\n" id (run_case budget fault_at steps)
            | _ -> invalid_arg "bad meter request");
            incr count;
            records ()
      in
      records ()));
  Printf.printf "PROCESSED %d\n%!" !count;
  if !count = 0 then 2 else 0

let () =
  let code = try
    match Array.to_list Sys.argv with
    | [_; requests; actual] -> run requests actual
    | _ -> invalid_arg "expected requests and actual"
  with Invalid_argument msg | Sys_error msg | Failure msg -> Printf.eprintf "ERROR %s\n%!" msg; 2
  in
  exit code
