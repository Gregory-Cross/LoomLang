(* json.ml - JSON text for records.jsonl (bake-off OCaml producer, Claude Bake-ocaml). *)

type t =
  | Null
  | Str of string
  | Num of Nat.t
  | Num_ref of string (* Immutable natural identity, expanded only by the serializer. *)
  | Arr of t list
  | Dict of (string * t) list

exception Duplicate_name of string

let add_string b s =
  Buffer.add_char b '"';
  String.iter
    (fun c ->
      match c with
      | '"' -> Buffer.add_string b "\\\""
      | '\\' -> Buffer.add_string b "\\\\"
      | c when Char.code c < 0x20 -> Buffer.add_string b (Printf.sprintf "\\u%04x" (Char.code c))
      | c -> Buffer.add_char b c)
    s;
  Buffer.add_char b '"'

let rec check_names = function
  | [] -> ()
  | (k, _) :: rest -> if List.mem_assoc k rest then raise (Duplicate_name k) else check_names rest

let rec add_to_buffer b = function
  | Null -> Buffer.add_string b "null"
  | Str s -> add_string b s
  | Num n -> Buffer.add_string b (Nat.to_decimal n)
  | Num_ref id ->
    if not (String.starts_with ~prefix:"nat:" id) then invalid_arg "expected a natural reference";
    let digits = String.sub id 4 (String.length id - 4) in
    (match Nat.of_decimal digits with
     | Some value -> Buffer.add_string b (Nat.to_decimal value)
     | None -> invalid_arg "noncanonical natural reference")
  | Arr xs ->
    Buffer.add_char b '[';
    List.iteri (fun i x -> if i > 0 then Buffer.add_char b ','; add_to_buffer b x) xs;
    Buffer.add_char b ']'
  | Dict kvs ->
    check_names kvs;
    Buffer.add_char b '{';
    List.iteri
      (fun i (k, v) ->
        if i > 0 then Buffer.add_char b ',';
        add_string b k;
        Buffer.add_char b ':';
        add_to_buffer b v)
      kvs;
    Buffer.add_char b '}'
