(* Little-endian radix B=2^30 limbs. Invariant: 0 <= limb < B, and the last
   limb is nonzero. The empty array is the only zero. Arrays never escape this
   module and no operation mutates an input; normalization takes owned arrays.

   This implementation requires OCaml's 63-bit native int (62 magnitude bits):
   max_int = 2^62 - 1. No operation relies on integer wraparound.
   - Addition: (B-1)+(B-1)+1 = 2B-1 < 2^31.
   - A future schoolbook multiply step, product plus stored result plus carry:
     (B-1)^2+(B-1)+(B-1) = B^2-1 = 2^60-1 < max_int.
     Multiplication is not implemented by this piece.
   - Decimal input: 10*(B-1)+9 = 10B-1 < 2^34.
   - Small multiply here uses factors <=30 and carry < factor, hence <30B.
   - Decimal output divides by D=10^9. Its combined numerator is at most
     (D-1)*B+(B-1) = D*B-1 < 2^60; its quotient limb is <B.

   Array/string allocation and indexing have the host's finite capacity. A
   capacity exception is a host resource failure, not a largest Loom natural.
   The exact bit count is computed as a natural, not native length*30. *)
let () =
  if Sys.int_size <> 63 then
    failwith "Natural requires an OCaml host with 63-bit native integers"

type t = int array

let limb_bits = 30
let base = 1 lsl limb_bits
let mask = base - 1
let zero = [||]
let one = [| 1 |]

let normalize owned =
  let length = ref (Array.length owned) in
  while !length > 0 && owned.(!length - 1) = 0 do
    decr length
  done;
  if !length = 0 then zero
  else if !length = Array.length owned then owned
  else Array.sub owned 0 !length

let with_extra_limb length =
  if length >= Sys.max_array_length then raise Out_of_memory;
  Array.make (length + 1) 0

let of_nonnegative_int value =
  if value < 0 then invalid_arg "Natural.of_nonnegative_int";
  let rec gather remaining reversed =
    if remaining = 0 then Array.of_list (List.rev reversed)
    else gather (remaining lsr limb_bits) ((remaining land mask) :: reversed)
  in
  gather value []

let multiply_small value factor initial_carry =
  (* Only callers below supply factors 10 or 30, and 0<=carry<factor. *)
  let length = Array.length value in
  let result = with_extra_limb length in
  let carry = ref initial_carry in
  for index = 0 to length - 1 do
    let part = (value.(index) * factor) + !carry in
    result.(index) <- part land mask;
    carry := part lsr limb_bits
  done;
  result.(length) <- !carry;
  normalize result

let of_decimal text =
  let length = String.length text in
  if length = 0 then Error "empty decimal natural"
  else
    let valid = ref true in
    for index = 0 to length - 1 do
      let digit = text.[index] in
      if digit < '0' || digit > '9' then valid := false
    done;
    if not !valid then Error "expected only ASCII decimal digits"
    else
      let value = ref zero in
      for index = 0 to length - 1 do
        value := multiply_small !value 10 (Char.code text.[index] - Char.code '0')
      done;
      Ok !value

let compare left right =
  let left_length = Array.length left and right_length = Array.length right in
  if left_length < right_length then -1
  else if left_length > right_length then 1
  else
    let index = ref (left_length - 1) in
    while !index >= 0 && left.(!index) = right.(!index) do
      decr index
    done;
    if !index < 0 then 0
    else if left.(!index) < right.(!index) then -1
    else 1

let add left right =
  let left_length = Array.length left and right_length = Array.length right in
  let length = max left_length right_length in
  if length = 0 then zero
  else
    let result = with_extra_limb length in
    let carry = ref 0 in
    for index = 0 to length - 1 do
      let a = if index < left_length then left.(index) else 0 in
      let b = if index < right_length then right.(index) else 0 in
      let part = a + b + !carry in
      result.(index) <- part land mask;
      carry := part lsr limb_bits
    done;
    result.(length) <- !carry;
    normalize result

let bit_length value =
  let length = Array.length value in
  if length = 0 then zero
  else
    let top = ref value.(length - 1) and count = ref 0 in
    while !top > 0 do
      incr count;
      top := !top lsr 1
    done;
    let lower = multiply_small (of_nonnegative_int (length - 1)) limb_bits 0 in
    add lower (of_nonnegative_int !count)

let divide_decimal_group value =
  let divisor = 1_000_000_000 in
  let length = Array.length value in
  let quotient = Array.make length 0 in
  let remainder = ref 0 in
  for index = length - 1 downto 0 do
    let combined = (!remainder * base) + value.(index) in
    quotient.(index) <- combined / divisor;
    remainder := combined mod divisor
  done;
  (normalize quotient, !remainder)

let to_decimal value =
  if Array.length value = 0 then "0"
  else
    let remaining = ref value and groups = ref [] in
    while Array.length !remaining > 0 do
      let quotient, remainder = divide_decimal_group !remaining in
      groups := remainder :: !groups;
      remaining := quotient
    done;
    match !groups with
    | [] -> assert false
    | first :: rest ->
        let buffer = Buffer.create 32 in
        Buffer.add_string buffer (string_of_int first);
        List.iter (fun group -> Printf.bprintf buffer "%09d" group) rest;
        Buffer.contents buffer
