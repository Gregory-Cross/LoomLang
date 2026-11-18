type position = { source_offset : int; line : int; column : int }
type span = { start_pos : position; end_pos : position }
type word = { spelling : string; word_span : span }

type 'scope expression = { form : 'scope form; expr_span : span }
and 'scope form =
  | Literal of string * 'scope Value.t
  | Reference of word
  | Apply of word * 'scope expression list

type 'scope definition = {
  name : word;
  parameters : word list;
  body : 'scope expression;
  definition_span : span;
}

type 'scope program = {
  source : string;
  definitions : 'scope definition list;
  eof : position;
}

type actual = Token of string | End_of_source

type refusal =
  | Encoding
  | Character of int
  | Noncanonical_natural of string
  | Syntax of { expected : string; actual : actual }

type fault =
  | Source_io of { operation : string; system_error : string }
  | Source_limit of { limit : Natural.t; observed_at_least : Natural.t }
  | Host_memory of string
  | Host_stack of string
  | Internal_error of { phase : string; reason : string }

type error = Refused of position * refusal | Tool_error of fault

let error_code = function
  | Refused (_, Encoding) -> "read.encoding"
  | Refused (_, Character _) -> "read.character"
  | Refused (_, Noncanonical_natural _) -> "read.noncanonical_natural"
  | Refused (_, Syntax _) -> "read.syntax"
  | Tool_error (Source_io _) -> "tool.source_io"
  | Tool_error (Source_limit _) -> "tool.source_limit"
  | Tool_error (Host_memory _) -> "tool.host_memory"
  | Tool_error (Host_stack _) -> "tool.host_stack"
  | Tool_error (Internal_error _) -> "tool.internal_error"

exception Abort of error

let tool fault = raise (Abort (Tool_error fault))
let refuse at cause = raise (Abort (Refused (at, cause)))

let phase name work =
  try work () with
  | Abort _ as e -> raise e
  | Out_of_memory -> tool (Host_memory name)
  | Stack_overflow -> tool (Host_stack name)
  | exn -> tool (Internal_error { phase = name; reason = Printexc.to_string exn })

let result work = try Ok (work ()) with Abort error -> Error error

let exact_decimal digits =
  match Natural.of_decimal digits with
  | Ok n -> n
  | Error reason -> failwith reason

let default_source_limit = exact_decimal "1048576"
let largest_host_int = exact_decimal (string_of_int max_int)

(* A source that fits an OCaml string fits a host int. Keep larger requested
   limits exact and only narrow them after comparing against that bound. *)
let host_limit n =
  if Natural.compare n largest_host_int > 0 then max_int
  else int_of_string (Natural.to_decimal n)

let over_limit limit =
  tool (Source_limit { limit; observed_at_least = Natural.add limit Natural.one })

let with_io operation work =
  try work () with Sys_error system_error -> tool (Source_io { operation; system_error })

let load_file limit path =
  let ceiling = host_limit limit in
  let channel = with_io "open" (fun () -> open_in_bin path) in
  Fun.protect ~finally:(fun () -> close_in_noerr channel) (fun () ->
    let chunk = Bytes.create 8192 in
    let buffer = Buffer.create (min ceiling (Bytes.length chunk)) in
    let rec consume () =
      let size = Buffer.length buffer in
      let remaining = ceiling - size in
      let wanted =
        if remaining < Bytes.length chunk then remaining + 1 else Bytes.length chunk
      in
      let count = with_io "read" (fun () -> input channel chunk 0 wanted) in
      if count = 0 then Buffer.contents buffer
      else if count > remaining then over_limit limit
      else if count > Sys.max_string_length - size then raise Out_of_memory
      else begin
        Buffer.add_subbytes buffer chunk 0 count;
        consume ()
      end
    in
    consume ())

let origin = { source_offset = 0; line = 1; column = 1 }

let forward at bytes =
  { at with source_offset = at.source_offset + bytes; column = at.column + bytes }

let newline text at =
  let offset = at.source_offset in
  let width =
    if text.[offset] = '\r' && offset + 1 < String.length text
       && text.[offset + 1] = '\n' then 2 else 1
  in
  { source_offset = offset + width; line = at.line + 1; column = 1 }

let validate_encoding text =
  let rec scan at =
    if at.source_offset < String.length text then
      match text.[at.source_offset] with
      | '\r' | '\n' -> scan (newline text at)
      | '\000' .. '\127' -> scan (forward at 1)
      | _ ->
          let decoded = String.get_utf_8_uchar text at.source_offset in
          if not (Uchar.utf_decode_is_valid decoded) then refuse at Encoding;
          scan { at with source_offset = at.source_offset + Uchar.utf_decode_length decoded;
                         column = at.column + 1 }
  in
  scan origin

type kind = Word of string | Digits of string | Left | Right | Comma | Equals | Eof
type token = { kind : kind; token_span : span }
type cursor = { text : string; mutable next_pos : position }

let is_digit = function '0' .. '9' -> true | _ -> false
let is_word_part = function
  | 'A' .. 'Z' | 'a' .. 'z' | '_' | '0' .. '9' -> true
  | _ -> false

let next_token cursor =
  let text = cursor.text in
  let length = String.length text in
  let rec skip at =
    if at.source_offset = length then at
    else match text.[at.source_offset] with
      | ' ' | '\t' -> skip (forward at 1)
      | '\r' | '\n' -> skip (newline text at)
      | _ -> at
  in
  let start_pos = skip cursor.next_pos in
  let first = start_pos.source_offset in
  let emit width kind =
    let end_pos = forward start_pos width in
    cursor.next_pos <- end_pos;
    { kind; token_span = { start_pos; end_pos } }
  in
  let run accepts =
    let stop = ref (first + 1) in
    while !stop < length && accepts text.[!stop] do incr stop done;
    String.sub text first (!stop - first)
  in
  if first = length then emit 0 Eof
  else match text.[first] with
    | 'A' .. 'Z' | 'a' .. 'z' | '_' ->
        let raw = run is_word_part in emit (String.length raw) (Word raw)
    | '0' .. '9' ->
        let raw = run is_digit in
        if raw.[0] = '0' && String.length raw > 1 then refuse start_pos (Noncanonical_natural raw);
        emit (String.length raw) (Digits raw)
    | '[' -> emit 1 Left
    | ']' -> emit 1 Right
    | ',' -> emit 1 Comma
    | '=' -> emit 1 Equals
    | _ ->
        let decoded = String.get_utf_8_uchar text first in
        refuse start_pos (Character (Uchar.to_int (Uchar.utf_decode_uchar decoded)))

(* Complete the lexical pass before the parser can diagnose a token. Replay
   the immutable bytes to avoid retaining a second, file-sized token array. *)
let validate_tokens text =
  let cursor = { text; next_pos = origin } in
  while (next_token cursor).kind <> Eof do () done

let actual_token = function
  | Word raw | Digits raw -> Token raw
  | Left -> Token "[" | Right -> Token "]" | Comma -> Token "," | Equals -> Token "="
  | Eof -> End_of_source

let parse natural source =
  let cursor = { text = source; next_pos = origin } in
  let look = ref (next_token cursor) in
  let take () =
    let head = !look in
    look := next_token cursor;
    head
  in
  let syntax expected =
    let token = !look in
    refuse token.token_span.start_pos (Syntax { expected; actual = actual_token token.kind })
  in
  let expect kind expected =
    if !look.kind <> kind then syntax expected;
    ignore (take ())
  in
  let word expected =
    match !look.kind with
    | Word spelling -> { spelling; word_span = (take ()).token_span }
    | Digits _ | Left | Right | Comma | Equals | Eof -> syntax expected
  in
  let close_apply head arguments =
    let end_pos = (take ()).token_span.end_pos in
    { form = Apply (head, List.rev arguments); expr_span = { start_pos = head.word_span.start_pos; end_pos } }
  in
  (* Each frame holds an unclosed application and its completed arguments
     in reverse order. Both transitions are tail calls at every depth. *)
  let rec expression expected frames =
    match !look.kind with
    | Digits raw ->
        let expr_span = (take ()).token_span in
        finish { form = Literal (raw, natural (exact_decimal raw)); expr_span } frames
    | Word _ ->
        let head = word "word" in
        if !look.kind <> Left then finish { form = Reference head; expr_span = head.word_span } frames
        else begin
          ignore (take ());
          if !look.kind = Right then finish (close_apply head []) frames
          else expression "expression or ]" ((head, []) :: frames)
        end
    | Left | Right | Comma | Equals | Eof -> syntax expected
  and finish node = function
    | [] -> node
    | (head, previous) :: outer ->
        let arguments = node :: previous in
        if !look.kind = Right then finish (close_apply head arguments) outer
        else if !look.kind = Comma then begin
          ignore (take ());
          expression "expression" ((head, arguments) :: outer)
        end else syntax ", or ]"
  in
  let rec parameters expected previous =
    let param = word expected in
    let current = param :: previous in
    if !look.kind = Right then List.rev current
    else if !look.kind = Comma then begin
      ignore (take ());
      parameters "word" current
    end else syntax ", or ]"
  in
  let rec definitions previous =
    if !look.kind = Eof then
      { source; definitions = List.rev previous; eof = !look.token_span.start_pos }
    else begin
      if !look.kind <> Word "def" then syntax "def";
      let start_pos = (take ()).token_span.start_pos in
      let name = word "word" in
      expect Left "[";
      let parameters = if !look.kind = Right then [] else parameters "word or ]" [] in
      expect Right "]";
      expect Equals "=";
      let body = expression "expression" [] in
      let definition_span = { start_pos; end_pos = body.expr_span.end_pos } in
      definitions ({ name; parameters; body; definition_span } :: previous)
    end
  in
  definitions []

module Make (Store : sig
  type scope
  val natural : Natural.t -> scope Value.t
end) = struct
  let read_source text =
    phase "decode" (fun () -> validate_encoding text);
    phase "tokenize" (fun () -> validate_tokens text);
    phase "parse" (fun () -> parse Store.natural text)

  let read_file ?(max_source_bytes = default_source_limit) path =
    result (fun () -> read_source (phase "read" (fun () -> load_file max_source_bytes path)))

  let read_bytes ?(max_source_bytes = default_source_limit) text =
    result (fun () ->
      phase "read" (fun () ->
        if String.length text > host_limit max_source_bytes then over_limit max_source_bytes);
      read_source text)
end
