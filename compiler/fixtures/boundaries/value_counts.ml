(* Count each visit in the private test build, including comparisons during interning.
   The colliding leaves also appear in the value fixtures. *)

let failures = ref []
let observations = ref 0

let require name condition =
  if not condition then failures := name :: !failures

let observe name expected_result expected_count operation =
  Visit_counter.count := 0;
  let result = operation () in
  let count = !(Visit_counter.count) in
  incr observations;
  Printf.printf "%s\tresult=%b\tvisits=%d\texpected_result=%b\texpected_visits=%d\n%!"
    name result count expected_result expected_count;
  require (name ^ ": result") (result = expected_result);
  require (name ^ ": visit count") (count = expected_count)

let natural digits =
  match Natural.of_decimal digits with
  | Ok value -> value
  | Error message -> invalid_arg message

let collision_left = "5737421554731"
let collision_right = "4399495151043"

module Samples () = struct
  module Store = Value.Make ()

  let leaf digits = Store.natural (natural digits)

  let chain depth digits =
    let root = ref (leaf digits) in
    for _level = 1 to depth do
      root := Store.tuple [| !root; !root |]
    done;
    !root
end

let self depth =
  let module S = Samples () in
  let root = S.chain depth "7" in
  observe (Printf.sprintf "self.depth-%d" depth) true 1
    (fun () -> Value.equal root root)

let reintern depth =
  let module S = Samples () in
  let child = S.chain depth "7" in
  let parent = S.Store.tuple [| child; child |] in
  let before = S.Store.interned_count () in
  for round = 1 to 3 do
    observe (Printf.sprintf "reintern.depth-%d.round-%d" depth round) true 3
      (fun () ->
        let repeated = S.Store.tuple [| child; child |] in
        repeated == parent && S.Store.interned_count () = before)
  done

let cross_store_equal () =
  let module L = Samples () in
  let module R = Samples () in
  (* Different admission histories also prevent treating local node numbers
     as semantic equality. Store.none alone is globally shared by Value. *)
  ignore (R.leaf "6789");
  let left = L.chain 32 "7" in
  let right = R.chain 32 "0007" in
  observe "cross-store.equal.depth-32" true 65
    (fun () -> Value.equal left right);
  observe "cross-store.equal.depth-32.reverse" true 65
    (fun () -> Value.equal right left)

let cross_store_unequal () =
  let module L = Samples () in
  let module R = Samples () in
  (* Matching admission histories deliberately give unlike leaves matching
     store-local numbers; the fixture collision defeats a hash-only answer. *)
  let left = L.chain 32 collision_left in
  let right = R.chain 32 collision_right in
  require "cross-store.unequal: colliding roots"
    (Value.hash left = Value.hash right);
  observe "cross-store.unequal-colliding.depth-32" false 33
    (fun () -> Value.equal left right);
  observe "cross-store.unequal-colliding.depth-32.reverse" false 33
    (fun () -> Value.equal right left)

let distinct_colliding_leaves () =
  let module S = Samples () in
  let left = S.leaf collision_left in
  let before = S.Store.interned_count () in
  let right = S.leaf collision_right in
  require "colliding leaves: distinct objects" (not (left == right));
  require "colliding leaves: separate admissions"
    (S.Store.interned_count () = before + 1);
  require "colliding leaves: fixture fingerprint"
    (Value.hash left = 457519830 && Value.hash right = 457519830);
  observe "same-store.distinct-colliding-leaves" false 1
    (fun () -> Value.equal left right);
  observe "same-store.distinct-colliding-leaves.reverse" false 1
    (fun () -> Value.equal right left)

let sibling_continuation () =
  let module S = Samples () in
  let shared_child = S.chain 32 "7" in
  let left_leaf = S.leaf collision_left in
  let right_leaf = S.leaf collision_right in
  let left = S.Store.tuple [| shared_child; left_leaf |] in
  let right = S.Store.tuple [| shared_child; right_leaf |] in
  require "sibling continuation: distinct parents" (not (left == right));
  require "sibling continuation: identical first child"
    (Value.field left 0 == Value.field right 0);
  require "sibling continuation: colliding parents"
    (Value.hash left = Value.hash right);
  (* The shortcut must advance pending work, reaching the unequal second
     leaf. Returning true immediately for shared_child is incorrect. *)
  observe "sibling-continuation.after-identical-depth-32-child" false 3
    (fun () -> Value.equal left right);
  observe "sibling-continuation.after-identical-depth-32-child.reverse" false 3
    (fun () -> Value.equal right left)

let () =
  self 1;
  self 32;
  reintern 1;
  reintern 32;
  cross_store_equal ();
  cross_store_unequal ();
  distinct_colliding_leaves ();
  sibling_continuation ();
  require "exactly 16 selected observations" (!observations = 16);
  Printf.printf "OBSERVATIONS %d\tFAILURES %d\n%!"
    !observations (List.length !failures);
  match List.rev !failures with
  | [] -> ()
  | names ->
      List.iter (fun name -> Printf.eprintf "FAIL %s\n%!" name) names;
      exit 1
