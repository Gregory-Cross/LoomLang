(* Test-only prefix for the isolated report-faults executable. The remainder
   of its driver is copied byte for byte from the selected source tree. *)
module Driver_fault = struct
  let mode = Sys.getenv_opt "LOOM_DRIVER_TEST_FAULT"
  let source_probe = mode = Some "read-before-eof" || mode = Some "copy-after-eof"
  let reads = ref 0
  let eof_seen = ref false
  let trace event =
    Out_channel.with_open_gen [Open_wronly; Open_creat; Open_append; Open_binary] 0o600
      "fault-trace.txt" (fun channel -> output_string channel event; output_char channel '\n')
end

(* Both EOF-length controls read the actual channel in short positive chunks.
   Their first injected exception differs only in whether EOF was observed. *)
let input channel bytes offset length =
  if not Driver_fault.source_probe then Stdlib.input channel bytes offset length
  else begin
    if Driver_fault.mode = Some "read-before-eof" && !(Driver_fault.reads) = 1 then begin
      Driver_fault.trace "read:oom";
      raise Out_of_memory
    end;
    let count = Stdlib.input channel bytes offset (min length 5) in
    incr Driver_fault.reads;
    if count = 0 then begin
      Driver_fault.eof_seen := true;
      Driver_fault.trace "read:EOF"
    end else Driver_fault.trace ("read:" ^ string_of_int count);
    count
  end

module Buffer = struct
  include Buffer
  let contents data =
    if Driver_fault.source_probe then
      Driver_fault.trace ("copy:" ^ string_of_int (length data));
    if Driver_fault.mode = Some "copy-after-eof" && !(Driver_fault.eof_seen) then
      raise Out_of_memory;
    contents data
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
    | Some "encode-once-stdout" when !attempts = 1 -> raise Stack_overflow
    | Some "stderr-encode" when result.code = "tool.report_io" -> raise Out_of_memory
    | _ ->
        let report = encode state result in
        if Driver_fault.mode = Some "encode-once-stdout" then
          Driver_fault.trace ("encoded:" ^ result.code);
        report
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
