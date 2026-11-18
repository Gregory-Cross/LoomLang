(* Development fixture notation: postfix n<digits>, o, t<width>, and dup. *)
module Samples () = struct
  module Store = Value.Make ()

  let rec take_fields count stack fields =
    if count = 0 then Store.tuple (Array.of_list fields) :: stack
    else
      match stack with
      | top :: rest when count > 0 -> take_fields (count - 1) rest (top :: fields)
      | _ -> invalid_arg "invalid fixture tuple width"

  let value text =
    let step stack token =
      if token = "o" then Store.none :: stack
      else if token = "dup" then List.hd stack :: stack
      else if String.length token < 2 then invalid_arg "invalid fixture token"
      else
        let payload = String.sub token 1 (String.length token - 1) in
        match token.[0] with
        | 'n' ->
            (match Natural.of_decimal payload with
            | Ok n -> Store.natural n :: stack
            | Error error -> invalid_arg error)
        | 't' -> take_fields (int_of_string payload) stack []
        | _ -> invalid_arg "unknown fixture token"
    in
    match List.fold_left step [] (String.split_on_char ' ' text) with
    | [root] -> root
    | _ -> invalid_arg "fixture must describe one value"

  let shared_chain depth leaf =
    let root = ref (value leaf) in
    for _level = 1 to depth do
      root := Store.tuple [| !root; !root |]
    done;
    !root
end

let relation a b =
  let same = Value.equal a b in
  if same <> Value.equal b a then failwith "asymmetric content equality";
  if same && Value.hash a <> Value.hash b then failwith "equal values have different hashes";
  same

let kind_name v =
  match Value.kind v with
  | Value.Natural -> "natural"
  | Value.Tuple -> "tuple"
  | Value.Builtin_none -> "none"

let fields value =
  match Value.tuple_width value with
  | Some width -> Array.init width (Value.field value)
  | None -> invalid_arg "frame fixture must supply children in a tuple"

(* Only the small byte-vector fixtures request expansion. Hashing, equality
   and interning never materialize an unfolded shared tree. *)
let encoding_hex root =
  let buffer = Buffer.create 32 in
  let rec emit v =
    String.iter (fun c -> Printf.bprintf buffer "%02x" (Char.code c)) (Value.local_header v);
    match Value.tuple_width v with
    | None -> ()
    | Some width ->
        for i = 0 to width - 1 do emit (Value.field v i) done
  in
  emit root;
  Buffer.contents buffer

let bytes_of_hex token =
  if token = "" then invalid_arg "use EMPTY for a zero-byte frame header";
  let hex = if token = "EMPTY" then "" else token in
  if String.length hex mod 2 <> 0 then invalid_arg "odd-length hex fixture";
  String.init (String.length hex / 2)
    (fun i -> Char.chr (int_of_string ("0x" ^ String.sub hex (2 * i) 2)))

let answer inject name operation left right argument =
  let module L = Samples () in
  let module R = Samples () in
  (* Give the two stores different admission histories. *)
  ignore (R.value "n6789");
  match operation with
  | "equal" ->
      let same = relation (L.value left) (R.value right) in
      string_of_bool (if inject && name = "control.planted-wrong-equality" then not same else same)
  | "hash" -> string_of_int (Value.hash (L.value left))
  | "encoding" -> encoding_hex (L.value left)
  | "kind" -> kind_name (L.value left)
  | "natural" ->
      (match Value.as_natural (L.value left) with None -> "absent" | Some n -> Natural.to_decimal n)
  | "width" ->
      (match Value.tuple_width (L.value left) with None -> "absent" | Some n -> string_of_int n)
  | "field" ->
      string_of_bool (relation (Value.field (L.value left) (int_of_string argument)) (R.value right))
  | "intern" ->
      let a = L.value left in
      let before = L.Store.interned_count () in
      let b = L.value right in
      Printf.sprintf "%b %d %d" (relation a b) before (L.Store.interned_count ())
  | "snapshot" ->
      let source = [| L.value left |] in
      let saved = L.Store.tuple source in
      let hash_before = Value.hash saved in
      source.(0) <- L.value right;
      string_of_bool (relation saved (R.value (left ^ " t1")) && Value.hash saved = hash_before)
  | "frame" ->
      let children = fields (L.value left) in
      let before = L.Store.interned_count () in
      (match L.Store.of_local_frame (bytes_of_hex argument) children with
      | Ok v -> if relation v (R.value right) then "ok" else "wrong-value"
      | Error error ->
          if L.Store.interned_count () <> before then failwith "refused frame added a node";
          (match error with
          | Value.Reserved_sequence -> "reserved-sequence"
          | Value.Unknown_kind -> "unknown-kind"
          | Value.Malformed_frame -> "malformed"))
  | "shared-chain" ->
      let depth = int_of_string argument in
      if depth < 0 then invalid_arg "negative fixture depth";
      string_of_bool (relation (L.shared_chain depth left) (R.shared_chain depth right))
  | _ -> invalid_arg ("unknown fixture operation " ^ operation)

let main () =
  let input = ref "" and output = ref "" and inject = ref false in
  Arg.parse
    [ "--input", Arg.Set_string input, "Fixture requests";
      "--output", Arg.Set_string output, "Named results";
      "--inject-wrong-equality", Arg.Set inject, "Plant the named development mismatch" ]
    (fun arg -> raise (Arg.Bad ("unexpected argument " ^ arg))) "value_probe --input FILE --output FILE";
  let data = In_channel.with_open_bin !input In_channel.input_all in
  let count = ref 0 in
  Out_channel.with_open_bin !output (fun channel ->
    let process line =
      match String.split_on_char '\t' line with
      | [name; op; left; right; argument] when name <> "" ->
          Printf.fprintf channel "%s\t%s\n" name (answer !inject name op left right argument);
          incr count
      | _ -> invalid_arg "expected five tab-separated fixture fields"
    in
    let rec lines = function
      | [] | [""] -> ()
      | [last] -> process last
      | line :: rest ->
          let n = String.length line in
          process (if n > 0 && line.[n - 1] = '\r' then String.sub line 0 (n - 1) else line);
          lines rest
    in
    lines (String.split_on_char '\n' data));
  Printf.printf "PROCESSED %d\n%!" !count;
  if !count = 0 then 2 else 0

let () =
  let code =
    try main () with
    | Invalid_argument e | Sys_error e | Failure e -> Printf.eprintf "ERROR %s\n%!" e; 2
  in
  exit code
