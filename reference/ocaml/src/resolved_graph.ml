(* Resolved unary graphs. The caller binds scheduled_bytes to the digest in
   the selected start before calling admit. offered_bytes is the exact
   immutable string to be decoded and later evaluated. *)
type node =
  | Local_parameter
  | Literal of string
  | Add of int * int | Sub of int * int

type t = { nodes : node list; body : int }

type refusal = Off_schedule | Malformed | Unknown_profile | Missing_row

(* These keys bind the exact add-descriptor.json and sub-descriptor.json
   bytes. The lists name their row keys in witness vocabulary. *)
let rows = function
  | "c329f863a3612d9bc09869ec47726c4fbe20101f70f190af75eb635b209a5608" ->
      Some ["Entry"; "Local"; "Literal"; "Add"]
  | "ca2932e7f3c4b6ad6a17e9455b6a72bc7522de1cd964f7cc5b8ac04dd94ce7e6" ->
      Some ["Entry"; "Local"; "Literal"; "Add"; "Sub"]
  | _ -> None

let operation_allowed ~descriptor operation =
  match rows descriptor with
  | None -> false
  | Some allowed -> List.mem operation allowed

let node_row = function
  | Local_parameter -> "Local"
  | Literal _ -> "Literal"
  | Add _ -> "Add"
  | Sub _ -> "Sub"

exception Invalid_graph

let decode bytes =
  let pos = ref 0 in
  let length = String.length bytes in
  let consume token =
    let n = String.length token in
    if n > length - !pos || String.sub bytes !pos n <> token then raise Invalid_graph;
    pos := !pos + n
  in
  let peek () =
    if !pos >= length then raise Invalid_graph;
    bytes.[!pos]
  in
  let natural () =
    let first = !pos in
    while !pos < length && bytes.[!pos] >= '0' && bytes.[!pos] <= '9' do
      incr pos
    done;
    let count = !pos - first in
    if count = 0 || (count > 1 && bytes.[first] = '0') then raise Invalid_graph;
    String.sub bytes first count
  in
  let index () =
    match int_of_string_opt (natural ()) with
    | Some n when n >= 0 -> n
    | _ -> raise Invalid_graph
  in
  let node () =
    consume "[\"";
    match peek () with
    | 'l' ->
        consume "l";
        (match peek () with
         | 'o' -> consume "ocal\",1]"; Local_parameter
         | 'i' ->
             consume "iteral\",\"";
             let digits = natural () in
             consume "\"]";
             Literal digits
         | _ -> raise Invalid_graph)
    | ('a' | 's') as tag ->
        consume (if tag='a' then "add\"," else "sub\",");
        let left = index () in
        consume ",";
        let right = index () in
        consume "]";
        if tag = 'a' then Add (left, right) else Sub (left, right)
    | _ -> raise Invalid_graph
  in
  consume "[\"unary-natural\",[";
  let rec nodes i stack rev =
    let item = node () in
    (* The stack holds exactly the completed subtrees in left-to-right order,
       latest first. Consuming the last two validates both operand bindings.
       A repeated, orphaned or forward reference cannot become a body. *)
    let pending = match item, stack with
      | (Add (l, r) | Sub (l, r)), right :: left :: rest when left = l && right = r -> i :: rest
      | (Add _ | Sub _), _ -> raise Invalid_graph
      | (Literal _ | Local_parameter), _ -> i :: stack
    in
    let acc = item :: rev in
    match peek () with
    | ',' -> consume ","; nodes (i + 1) pending acc
    | ']' ->
        consume "],";
        let body = index () in
        consume "]\n";
        if !pos <> length || body <> i || pending <> [i] then raise Invalid_graph;
        {nodes = List.rev acc; body}
    | _ -> raise Invalid_graph
  in
  nodes 0 [] []

let admit ~descriptor ~scheduled_bytes offered_bytes =
  if not (String.equal scheduled_bytes offered_bytes) then Error Off_schedule
  else match rows descriptor with
    | None -> Error Unknown_profile
    | Some allowed ->
        try
          let graph = decode offered_bytes in
          if List.mem "Entry" allowed &&
             List.for_all (fun node -> List.mem (node_row node) allowed) graph.nodes
          then Ok graph else Error Missing_row
        with Invalid_graph -> Error Malformed
