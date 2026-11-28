(* nat.ml - exact naturals for the bake-off OCaml producer (Claude Bake-ocaml, card 0001).

   Representation invariant: a natural is an int array of limbs in base 2^30, least significant limb first, with no
   high zero limb; zero is the empty array. Every intermediate below stays under 2^62, inside OCaml's 63-bit native
   int, so no operation wraps; each bound is stated where it is used. Arrays are filled while being built and never
   written afterwards. *)

type t = int array

let base_bits = 30
let base = 1 lsl base_bits
let mask = base - 1

let zero : t = [||]

let normalize (a : int array) : t =
  let n = ref (Array.length a) in
  while !n > 0 && a.(!n - 1) = 0 do decr n done;
  if !n = Array.length a then a else Array.sub a 0 !n

let of_int n : t =
  if n < 0 then invalid_arg "Nat.of_int: negative";
  let rec go n acc = if n = 0 then Array.of_list (List.rev acc) else go (n lsr base_bits) ((n land mask) :: acc) in
  go n []

let one = of_int 1

let limb (a : t) i = if i < Array.length a then a.(i) else 0

let compare (x : t) (y : t) =
  let lx = Array.length x and ly = Array.length y in
  if lx <> ly then Stdlib.compare lx ly
  else begin
    let i = ref (lx - 1) in
    while !i >= 0 && x.(!i) = y.(!i) do decr i done;
    if !i < 0 then 0 else Stdlib.compare x.(!i) y.(!i)
  end

let equal x y = compare x y = 0
let max x y = if compare x y >= 0 then x else y
let min x y = if compare x y <= 0 then x else y

(* Limb sums are below 2^31. *)
let add (x : t) (y : t) : t =
  let l = Stdlib.max (Array.length x) (Array.length y) in
  let r = Array.make (l + 1) 0 in
  let carry = ref 0 in
  for i = 0 to l - 1 do
    let s = limb x i + limb y i + !carry in
    r.(i) <- s land mask;
    carry := s lsr base_bits
  done;
  r.(l) <- !carry;
  normalize r

let sub_trunc (x : t) (y : t) : t =
  if compare x y <= 0 then zero
  else begin
    let l = Array.length x in
    let r = Array.make l 0 in
    let borrow = ref 0 in
    for i = 0 to l - 1 do
      let d = x.(i) - limb y i - !borrow in
      if d < 0 then begin r.(i) <- d + base; borrow := 1 end
      else begin r.(i) <- d; borrow := 0 end
    done;
    normalize r
  end

(* The binary digits of a machine int n > 0. *)
let int_width n =
  let rec go n k = if n = 0 then k else go (n lsr 1) (k + 1) in
  go n 0

let width_count (x : t) =
  let l = Array.length x in
  if l = 0 then 1 else (base_bits * (l - 1)) + int_width x.(l - 1)

let bits x = of_int (width_count x)

(* bits(x+y) by one pass over the limbs: when the last carry is 0, the sum has l limbs and its top limb is the last
   limb sum, which is nonzero because x or y has l limbs and a nonzero top limb; when it is 1, the sum has l+1 limbs
   and its top limb is 1. *)
let sum_bits (x : t) (y : t) : t =
  let l = Stdlib.max (Array.length x) (Array.length y) in
  if l = 0 then of_int 1
  else begin
    let carry = ref 0 and top = ref 0 in
    for i = 0 to l - 1 do
      let s = limb x i + limb y i + !carry in
      top := s land mask;
      carry := s lsr base_bits
    done;
    if !carry <> 0 then of_int ((base_bits * l) + 1)
    else if !top = 0 then invalid_arg "Nat.sum_bits: operand breaks the representation invariant"
    else of_int ((base_bits * (l - 1)) + int_width !top)
  end

(* bits(max(x-y,0)): 1 when x <= y; otherwise one pass from the low limb keeps the borrow and the index and value of
   the highest nonzero difference limb (x > y, so the final borrow is 0 and some limb is nonzero). *)
let diff_bits (x : t) (y : t) : t =
  if compare x y <= 0 then of_int 1
  else begin
    let l = Array.length x in
    let borrow = ref 0 and top_i = ref (-1) and top_v = ref 0 in
    for i = 0 to l - 1 do
      let d = x.(i) - limb y i - !borrow in
      let d = if d < 0 then begin borrow := 1; d + base end else begin borrow := 0; d end in
      if d <> 0 then begin top_i := i; top_v := d end
    done;
    if !top_i < 0 then invalid_arg "Nat.diff_bits: no nonzero difference limb"
    else of_int ((base_bits * !top_i) + int_width !top_v)
  end

let pow10 = [| 1; 10; 100; 1_000; 10_000; 100_000; 1_000_000; 10_000_000; 100_000_000; 1_000_000_000 |]

(* x*m + a for 0 <= m <= 10^9 and 0 <= a < 10^9: each limb product is below 2^60 and each carry below 2^31, and the
   result has at most l+1 limbs because 10^9 + 1 < 2^30. *)
let mul_add_small (x : t) m a : t =
  let l = Array.length x in
  let r = Array.make (l + 1) 0 in
  let carry = ref a in
  for i = 0 to l - 1 do
    let v = (x.(i) * m) + !carry in
    r.(i) <- v land mask;
    carry := v lsr base_bits
  done;
  r.(l) <- !carry;
  normalize r

let is_digit c = c >= '0' && c <= '9'

let of_decimal s =
  let n = String.length s in
  if n = 0 || (not (String.for_all is_digit s)) || (n > 1 && s.[0] = '0') then None
  else begin
    let acc = ref zero and i = ref 0 in
    while !i < n do
      let k = Stdlib.min 9 (n - !i) in
      let chunk = ref 0 in
      for j = !i to !i + k - 1 do chunk := (!chunk * 10) + (Char.code s.[j] - 48) done;
      acc := mul_add_small !acc pow10.(k) !chunk;
      i := !i + k
    done;
    Some !acc
  end

(* (q, r) with x = q*d + r and 0 <= r < d, for 1 <= d <= 10^9: each partial dividend is below d * 2^30 < 2^60. *)
let divmod_small (x : t) d =
  let l = Array.length x in
  let q = Array.make l 0 in
  let rem = ref 0 in
  for i = l - 1 downto 0 do
    let v = (!rem lsl base_bits) lor x.(i) in
    q.(i) <- v / d;
    rem := v mod d
  done;
  (normalize q, !rem)

let to_decimal (x : t) =
  if Array.length x = 0 then "0"
  else begin
    let chunks = ref [] and cur = ref x in
    while Array.length !cur > 0 do
      let q, r = divmod_small !cur 1_000_000_000 in
      chunks := r :: !chunks;
      cur := q
    done;
    let b = Buffer.create (9 * List.length !chunks) in
    List.iteri
      (fun i c -> if i = 0 then Buffer.add_string b (string_of_int c) else Buffer.add_string b (Printf.sprintf "%09d" c))
      !chunks;
    Buffer.contents b
  end
