(* Private boundary-test helper. Production compilation never includes this module. *)
let on_reversal : (int -> unit) ref = ref (fun _ -> ())

let rev values =
  let ordered = List.rev values in
  (!on_reversal) (List.length ordered);
  ordered

let test_eval_fault site target =
  match Sys.getenv_opt "LOOM_TEST_EVAL_FAULT" with
  | Some ("observe" | "input-memory" | "entry-memory" | "entry-stack" | "tuple-memory" as mode) ->
      Out_channel.with_open_gen [Open_wronly; Open_creat; Open_append; Open_binary] 0o600
        "eval-fault-trace.txt"
        (fun channel -> output_string channel site; output_char channel '\n');
      if mode = target ^ "-memory" then raise Out_of_memory;
      if mode = target ^ "-stack" then raise Stack_overflow
  | _ -> ()
