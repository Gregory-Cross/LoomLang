(* SHA-256 of immutable file bytes, for development report provenance. *)
let constants = [|
  0x428a2f98l; 0x71374491l; 0xb5c0fbcfl; 0xe9b5dba5l; 0x3956c25bl; 0x59f111f1l; 0x923f82a4l; 0xab1c5ed5l;
  0xd807aa98l; 0x12835b01l; 0x243185bel; 0x550c7dc3l; 0x72be5d74l; 0x80deb1fel; 0x9bdc06a7l; 0xc19bf174l;
  0xe49b69c1l; 0xefbe4786l; 0x0fc19dc6l; 0x240ca1ccl; 0x2de92c6fl; 0x4a7484aal; 0x5cb0a9dcl; 0x76f988dal;
  0x983e5152l; 0xa831c66dl; 0xb00327c8l; 0xbf597fc7l; 0xc6e00bf3l; 0xd5a79147l; 0x06ca6351l; 0x14292967l;
  0x27b70a85l; 0x2e1b2138l; 0x4d2c6dfcl; 0x53380d13l; 0x650a7354l; 0x766a0abbl; 0x81c2c92el; 0x92722c85l;
  0xa2bfe8a1l; 0xa81a664bl; 0xc24b8b70l; 0xc76c51a3l; 0xd192e819l; 0xd6990624l; 0xf40e3585l; 0x106aa070l;
  0x19a4c116l; 0x1e376c08l; 0x2748774cl; 0x34b0bcb5l; 0x391c0cb3l; 0x4ed8aa4al; 0x5b9cca4fl; 0x682e6ff3l;
  0x748f82eel; 0x78a5636fl; 0x84c87814l; 0x8cc70208l; 0x90befffal; 0xa4506cebl; 0xbef9a3f7l; 0xc67178f2l
|]

let ( +! ) = Int32.add
let ( ^! ) = Int32.logxor
let rotate x n = Int32.logor (Int32.shift_right_logical x n) (Int32.shift_left x (32 - n))
let small0 x = rotate x 7 ^! rotate x 18 ^! Int32.shift_right_logical x 3
let small1 x = rotate x 17 ^! rotate x 19 ^! Int32.shift_right_logical x 10
let large0 x = rotate x 2 ^! rotate x 13 ^! rotate x 22
let large1 x = rotate x 6 ^! rotate x 11 ^! rotate x 25

let compress h words =
  for i = 16 to 63 do
    words.(i) <- small1 words.(i - 2) +! words.(i - 7) +! small0 words.(i - 15) +! words.(i - 16)
  done;
  let a = ref h.(0) and b = ref h.(1) and c = ref h.(2) and d = ref h.(3) in
  let e = ref h.(4) and f = ref h.(5) and g = ref h.(6) and last = ref h.(7) in
  for i = 0 to 63 do
    let choose = Int32.logand !e !f ^! Int32.logand (Int32.lognot !e) !g in
    let majority = Int32.logand !a !b ^! Int32.logand !a !c ^! Int32.logand !b !c in
    let first = !last +! large1 !e +! choose +! constants.(i) +! words.(i) in
    let second = large0 !a +! majority in
    last := !g; g := !f; f := !e; e := !d +! first;
    d := !c; c := !b; b := !a; a := first +! second
  done;
  Array.iteri (fun i v -> h.(i) <- h.(i) +! v) [| !a; !b; !c; !d; !e; !f; !g; !last |]

let hex source =
  let h = [| 0x6a09e667l; 0xbb67ae85l; 0x3c6ef372l; 0xa54ff53al;
             0x510e527fl; 0x9b05688cl; 0x1f83d9abl; 0x5be0cd19l |] in
  let words = Array.make 64 0l in
  let length = String.length source in
  let full = length / 64 and tail = length mod 64 in
  for i = 0 to full - 1 do
    for j = 0 to 15 do words.(j) <- String.get_int32_be source (i * 64 + j * 4) done;
    compress h words
  done;
  let ending = Bytes.make (if tail < 56 then 64 else 128) '\000' in
  Bytes.blit_string source (full * 64) ending 0 tail;
  Bytes.set ending tail '\x80';
  Bytes.set_int64_be ending (Bytes.length ending - 8) (Int64.shift_left (Int64.of_int length) 3);
  for i = 0 to Bytes.length ending / 64 - 1 do
    for j = 0 to 15 do words.(j) <- Bytes.get_int32_be ending (i * 64 + j * 4) done;
    compress h words
  done;
  String.concat "" (Array.to_list (Array.map (Printf.sprintf "%08lx") h))
