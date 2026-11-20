type kind = Natural | Tuple | Builtin_none
type frame_error = Reserved_sequence | Unknown_kind | Malformed_frame

type node = { number : int; fingerprint : int; content : content }
and content = Number of Natural.t | Fields of node array | None_case

type 'scope t = node

let kind value =
  match value.content with
  | Number _ -> Natural
  | Fields _ -> Tuple
  | None_case -> Builtin_none

let as_natural value =
  match value.content with Number n -> Some n | Fields _ | None_case -> None

let tuple_width value =
  match value.content with
  | Fields fields -> Some (Array.length fields)
  | Number _ | None_case -> None

let tuple_header width = "T" ^ string_of_int width ^ "\n"

let header = function
  | Number n -> "N" ^ Natural.to_decimal n ^ "\n"
  | Fields fields -> tuple_header (Array.length fields)
  | None_case -> "O\n"

let local_header value = header value.content

let fold_byte state byte =
  (* (p-1)*257 + 256 < 2^38 on Natural's required 63-bit host. *)
  ((257 * state) + byte + 1) mod 1_000_000_007

let fingerprint content =
  let initial = String.fold_left (fun h c -> fold_byte h (Char.code c)) 0 (header content) in
  match content with
  | Number _ | None_case -> initial
  | Fields fields ->
      Array.fold_left
        (fun state child ->
          let h = ref state in
          for i = 0 to 3 do
            h := fold_byte !h ((child.fingerprint lsr (8 * i)) land 255)
          done;
          !h)
        initial fields

let hash value = value.fingerprint
let none_node = { number = 0; fingerprint = fingerprint None_case; content = None_case }

let field value index =
  match value.content with
  | Fields fields when index >= 0 && index < Array.length fields -> fields.(index)
  | Fields _ | Number _ | None_case -> none_node

let equal left right =
  (* Numbers only name visited pairs, with one store on each side throughout
     this traversal. Neither a matching hash nor matching node numbers prove
     equality. The worklist also handles deeply linked immutable tuples. *)
  let visited = Hashtbl.create 16 in
  let rec visit a b pending =
    if a == b then advance pending
    else if a.fingerprint <> b.fingerprint then false
    else
      match a.content, b.content with
      | None_case, None_case -> advance pending
      | Number x, Number y -> Natural.compare x y = 0 && advance pending
      | Fields xs, Fields ys ->
          let pair = a.number, b.number in
          if Array.length xs <> Array.length ys then false
          else if Hashtbl.mem visited pair then advance pending
          else (
            Hashtbl.add visited pair ();
            advance ((xs, ys, 0) :: pending))
      | None_case, (Number _ | Fields _)
      | Number _, (None_case | Fields _)
      | Fields _, (None_case | Number _) -> false
  and advance = function
    | [] -> true
    | (xs, ys, i) :: rest ->
        if i = Array.length xs then advance rest
        else visit xs.(i) ys.(i) ((xs, ys, i + 1) :: rest)
  in
  visit left right []

module Content_table = Hashtbl.Make (struct
  type t = node
  let equal = equal
  let hash = hash
end)

module Make () = struct
  type scope = unit

  let nodes = Content_table.create 32
  let none = none_node
  let () = Content_table.add nodes none none
  let interned_count () = Content_table.length nodes

  let intern content =
    (* The candidate's number is fresh for this lookup. Only stored nodes
       consume a number, and nodes never leave this table during its lifetime. *)
    let candidate = { number = interned_count (); fingerprint = fingerprint content; content } in
    match Content_table.find_opt nodes candidate with
    | Some existing -> existing
    | None ->
        if candidate.number = max_int then raise Out_of_memory;
        Content_table.add nodes candidate candidate;
        candidate

  let natural n = intern (Number n)
  let tuple fields = intern (Fields (Array.copy fields))

  let of_local_frame bytes children =
    let length = String.length bytes and width = Array.length children in
    if length = 0 then Error Malformed_frame
    else
      match bytes.[0] with
      | 'S' -> Error Reserved_sequence
      | 'O' ->
          if width = 0 && bytes = "O\n" then Ok none else Error Malformed_frame
      | 'T' ->
          if bytes = tuple_header width then Ok (tuple children) else Error Malformed_frame
      | 'N' ->
          if width <> 0 || length < 3 || bytes.[length - 1] <> '\n'
             || (length > 3 && bytes.[1] = '0') then Error Malformed_frame
          else
            (match Natural.of_decimal (String.sub bytes 1 (length - 2)) with
            | Ok n -> Ok (natural n)
            | Error _ -> Error Malformed_frame)
      | _ -> Error Unknown_kind
end
