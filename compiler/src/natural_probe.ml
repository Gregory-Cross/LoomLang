(* A development text interface. No Python or big-number library is linked. *)
let natural text =
  match Natural.of_decimal text with
  | Ok value -> value
  | Error error -> invalid_arg error

let answer row inject_wrong_sum =
  match String.split_on_char '\t' row with
  | [ name; operation; left; right ] when name <> "" ->
      let value =
        match operation with
        | "parse" ->
            (match Natural.of_decimal left with
            | Ok value -> Natural.to_decimal value
            | Error _ -> "INVALID")
        | "roundtrip" -> Natural.to_decimal (natural left)
        | "bits" -> Natural.to_decimal (Natural.bit_length (natural left))
        | "compare" -> string_of_int (Natural.compare (natural left) (natural right))
        | "add" ->
            let a = natural left and b = natural right in
            let before_a = Natural.to_decimal a and before_b = Natural.to_decimal b in
            let sum = Natural.add a b in
            if Natural.to_decimal a <> before_a || Natural.to_decimal b <> before_b then
              failwith "addition mutated an input";
            let sum =
              if inject_wrong_sum && name = "control.planted-wrong-sum" then
                Natural.add sum Natural.one
              else sum
            in
            Natural.to_decimal sum
        | _ -> invalid_arg ("unknown natural operation: " ^ operation)
      in
      name ^ "\t" ^ value ^ "\n"
  | _ -> invalid_arg "expected name, operation, left and right, tab-separated"

let input_row source =
  let buffer = Buffer.create 128 in
  let rec read () =
    match input_char source with
    | '\n' ->
        (* Only an observed LF makes the preceding CR part of line framing. *)
        let length = Buffer.length buffer in
        if length > 0 && Buffer.nth buffer (length - 1) = '\r' then
          Buffer.truncate buffer (length - 1);
        Buffer.contents buffer
    | character ->
        Buffer.add_char buffer character;
        read ()
    | exception End_of_file ->
        if Buffer.length buffer = 0 then raise End_of_file
        else Buffer.contents buffer
  in
  read ()

let main () =
  let input = ref "" and output = ref "" and inject = ref false in
  Arg.parse
    [ ("--input", Arg.Set_string input, "Decimal text requests");
      ("--output", Arg.Set_string output, "Decimal text results");
      ("--inject-wrong-sum", Arg.Set inject, "Development negative control") ]
    (fun value -> raise (Arg.Bad ("unexpected argument: " ^ value)))
    "natural_probe --input FILE --output FILE";
  if !input = "" || !output = "" then invalid_arg "input and output are required";
  let source = open_in_bin !input in
  Fun.protect ~finally:(fun () -> close_in_noerr source) (fun () ->
      let destination = open_out_bin !output in
      Fun.protect ~finally:(fun () -> close_out_noerr destination) (fun () ->
          let count = ref 0 and finished = ref false in
          while not !finished do
            match input_row source with
            | row ->
                output_string destination (answer row !inject);
                incr count
            | exception End_of_file -> finished := true
          done;
          Printf.printf "PROCESSED %d\n%!" !count;
          if !count = 0 then 2 else 0))

let () =
  let code =
    try main () with
    | Invalid_argument error | Sys_error error | Failure error ->
        Printf.eprintf "ERROR %s\n%!" error;
        2
  in
  exit code
