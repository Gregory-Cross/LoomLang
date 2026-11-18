(* Test-only prefix for the isolated report-faults executable. The remainder
   of its driver is copied byte for byte from the selected source tree. *)
module Driver_fault = struct
  let mode = Sys.getenv_opt "LOOM_DRIVER_TEST_FAULT"
  let trace event =
    Out_channel.with_open_gen [Open_wronly; Open_creat; Open_append; Open_binary] 0o600
      "fault-trace.txt" (fun channel -> output_string channel event; output_char channel '\n')
end

module Sha256 = struct
  let hex bytes =
    Driver_fault.trace ("hash:" ^ string_of_int (String.length bytes));
    if Driver_fault.mode = Some "hash" then raise Out_of_memory;
    Sha256.hex bytes
end

module Run_record = struct
  include Run_record
  let attempts = ref 0
  let encode state (result : outcome) =
    incr attempts;
    Driver_fault.trace ("encode:" ^ result.code);
    match Driver_fault.mode with
    | Some "encode-always" -> raise Out_of_memory
    | Some "encode-once" when !attempts = 1 -> raise Out_of_memory
    | Some "stderr-encode" when result.code = "tool.report_io" -> raise Out_of_memory
    | _ -> encode state result
end

(* Only the recovery fixture waits between its completed stderr flush and exit. *)
let flush channel =
  let recover = Driver_fault.mode = Some "recover-stdout" in
  (try Stdlib.flush channel with
   | Sys_error message as exn when recover && channel == stdout ->
       Driver_fault.trace ("stdout-failed:" ^ message);
       raise exn);
  if recover && channel == stderr then begin
    Driver_fault.trace "stderr-flushed";
    if input_line stdin <> "stdout-restored" then failwith "missing stdout restoration";
    Driver_fault.trace "stdout-restored"
  end
