let nat s = match Nat.of_decimal s with Some v -> v | None -> invalid_arg "natural"
let s x = Json.Str x
let n x = Json.Num x
let i x = n (Nat.of_int x)
let pair (a,b) = Json.Arr [n a; n b]
let obj x = Json.Dict x
let names xs = Json.Arr (List.map s xs)
let zero = Nat.zero, Nat.zero
let one = Nat.one, Nat.zero
let emit_json chan record =
  let buf = Buffer.create 512 in
  Json.add_to_buffer buf record; Buffer.add_char buf '\n';
  output_string chan (Buffer.contents buf)
let emit chan fields = emit_json chan (obj fields)
let bytes h =
  if String.length h mod 2 <> 0 then invalid_arg "hex";
  String.init (String.length h / 2)
    (fun j -> Char.chr (int_of_string ("0x" ^ String.sub h (2*j) 2)))
let outcome = function
  | Ok v -> "return",Json.Num_ref (Core.id v)
  | Error why -> "stop",s why
let check_call_bindings fn =
  let grant = Nat.of_int 50, Nat.of_int 5 in
  let a = Core.account grant and b = Core.account grant in
  let x = Core.value "2" and y = Core.value "3" in
  let site = "same-site" in
  let old = Core.view a site [x;y] in
  let v = Core.view a site [x;y] and foreign = Core.view b site [x;y] in
  let call view name l r =
    fn ~definition:"control" ~descriptor:"control" ~site:name
       ~interrupt:false ~prepare:(fun _ detail -> detail) a view l r in
  let refused view name l r =
    match call view name l r with
    | exception Invalid_argument reason -> reason = "Core: mismatched event operands or account"
    | _ -> false in
  refused foreign site x y && refused old site x y &&
  refused v "other-site" x y && refused v site y x &&
  Core.available a = grant && Core.available b = grant &&
  (match call v site x y with Ok _,_,_ -> true | _ -> false)

let () =
  set_binary_mode_out stdout true; set_binary_mode_out stderr true;
  if Array.length Sys.argv = 2 && Sys.argv.(1) = "stale-control" then begin
    if not (Core.stale_control () && check_call_bindings Arithmetic.add && check_call_bindings Arithmetic.sub) then failwith "stale view accepted";
    emit stdout ["control",s "stale-equally-funded";"outcome",s "rejected";"int_size",i Sys.int_size]
  end else begin
    let arg k = Sys.argv.(k) in
    let case = arg 1 and observer = arg 2 and descriptor = arg 3 in
    let scheduled = arg 4 and offered = arg 5 and mode = arg 6 in
    let grant = nat (arg 8),nat (arg 9) in
    let plant = arg 10 = "calibrate" in
    if plant && not Probe_switch.enabled then invalid_arg "calibration needs probe";
    if observer <> "ordinary" && observer <> "trial-exact" then invalid_arg "observer";
    let run = case ^ "/" ^ observer in
    let output typ fields = emit stdout (["kind",s typ;"run",s run] @ fields) in
    let site = ref "before-entry" and seq = ref 0 in
    let diag fields =
      if Probe_switch.enabled then begin
        incr seq;
        emit stderr (["run",s run;"seq",i !seq;"site",s !site] @ fields)
      end in
    Core.on_probe (fun phase slot refid operation index ->
      diag ["phase",s phase;"slot",i slot;"ref",s refid;"operation",s operation;
            "index",(if index < 0 then Json.Null else i index)]);
    let a = Core.account grant in
    let pool = Hashtbl.create 8 in
    let intern text = match Hashtbl.find_opt pool text with
      | Some v -> v | None -> let v=Core.value text in Hashtbl.add pool text v; v in
    let def = if mode = "graph" then "top" else if Array.length Sys.argv > 13 && arg 13="Sub" then "trial" else "pilot" in
    let scope = if def="trial" then "root" else if mode="graph" then arg 13 else "serial-root" in
    let selected = if mode = "graph" then "top.body" else arg 11 in
    let selected_meter = ref None in
    let event event_site kind operands execute =
      site := event_site;
      let prefix_before = Core.prefix a and initial = Core.settled a in
      let prior = Core.committed a and latest = Core.last a in
      let v = Core.view a event_site operands in
      let record result detail debit settled total hold prefix =
        let tag,visible = outcome result in
        obj ["kind",s "witness";"run",s run;"definition",s def;"site",s event_site;"visit",i 1;
          "operation",s kind;"pre",pair initial;"prior_committed",pair prior;"latest_before",pair latest;
          "prefix_before",names prefix_before;"evidence",detail;"debit",pair debit;"settled",pair settled;
          "committed",pair total;"hold_after",pair hold;"prefix_after",names prefix;
          "limit_scope",(match result with Error ("work"|"construction")->s scope|_->Json.Null);
          "requests",names [];"trail",names [];"holdings",names [];tag,visible] in
      let prepare value detail =
        let ((w,c) as debit) = Core.outstanding a in
        let old_w,old_c = prior in
        record (Ok value) detail debit (Core.available a)
          (Nat.add old_w w,Nat.add old_c c) zero (prefix_before @ [event_site]) in
      let result,detail,supplement =
        try
          Core.phase "begin"; Core.phase "quote";
          if plant && List.length operands = 2 then Core.calibration_read v 1;
          execute v prepare
        with exn -> Core.stop v; raise exn in
      let debit,witness = match result with
        | Ok value -> (match Core.latest_record a with
            | Some (retained,full) when value == retained -> Core.last a,full
            | _ -> failwith "incomplete committed record")
        | Error _ -> zero,record result detail zero (Core.settled a)
                           (Core.committed a) (Core.outstanding a) (Core.prefix a) in
      if event_site = selected then
        selected_meter := Some (debit, Core.settled a, supplement);
      Core.phase "witness-render";
      emit_json stdout witness;
      Core.phase "end"; site := "between-events"; Core.phase "between-events"; result in
    let reference event_site kind binding select =
      event event_site kind [] (fun v prepare ->
        let before = Core.available a in
        let common = ["origin",binding;"requested",pair one] in
        if Nat.compare (fst before) Nat.one < 0 then begin
          Core.phase "work-refusal"; Core.stop v;
          Error "work",obj (common @ ["phase",s "WorkCheck";"deficits",pair one;
            "holds",Json.Arr [];"released",pair zero]),[]
        end else begin
          let hold=Core.hold_work v Nat.one in Core.phase "reference";
          let value=select () in Core.reserve v hold Nat.zero;
          let detail = obj (common @ ["phase",s "Commit";"selected_ref",s (Core.id value);
            "holds",Json.Arr [pair one];"released",pair zero]) in
          let answer = Ok value,detail,[] in
          Core.phase "commit";
          Core.commit v hold event_site value (fun () -> prepare value detail);
          answer
        end) in
    let binary kind event_site interrupt left right =
      let fn = match kind with "Add" -> Arithmetic.add | "Sub" -> Arithmetic.sub | _ -> invalid_arg "operation" in
      event event_site kind [left;right] (fun v prepare ->
        fn ~definition:def ~descriptor ~site:event_site ~interrupt ~prepare a v left right) in
    let project result =
      site := "boundary"; Core.phase "projection";
      let tag,v = outcome result in
      let fields=[tag,v;"actions",names [];"later_state",names []] in
      let purchased = if observer="ordinary" then [] else
        let debit,remaining,supplement = match !selected_meter with
          | Some sample -> sample
          | None -> zero,Core.settled a,[] in
        ["event_debit",pair debit;"remaining",pair remaining] @ supplement in
      output "projection" ["selected",s selected;"fields",obj (fields @ purchased)] in
    let header fields =
      output "start" (["definition",s def;"observer",s observer;"descriptor",s descriptor;
        "scheduled",s scheduled;"offered",s offered;"export",s "b";"scope",s scope;
        "grant",pair grant;"prior_debit",pair zero;"selected",s selected;"visit",i 1;
        "prior_prefix",names [];"memo",names []] @ fields) in
    if mode="graph" then begin
      let scheduled_bytes=bytes (arg 11) and offered_bytes=bytes (arg 12) in
      let handle=arg 14 and admitted_handle=arg 15 in
      let bound = handle <> "" && handle = admitted_handle in
      header ["input_handle",s handle;"input_ref",(if bound then s ("nat:"^arg 7) else Json.Null);"schedule",s "uninterrupted"];
      match Resolved_graph.admit ~descriptor ~scheduled_bytes offered_bytes with
      | Error err -> output "pre-entry-refusal" ["reason",s (match err with
        Off_schedule -> "off-schedule graph" | Malformed -> "malformed resolved graph"
        | Unknown_profile -> "unknown descriptor" | Missing_row -> "missing descriptor row")]
      | Ok _ when not bound -> output "pre-entry-refusal" ["reason",s "unknown input handle"]
      | Ok graph when scope <> "root" && List.exists (function Resolved_graph.Sub _ -> true | _ -> false) graph.nodes ->
        output "pre-entry-refusal" ["reason",s "unsupported Sub scope"]
      | Ok graph ->
        let input = intern (arg 7) in
        let nodes=Array.of_list graph.nodes in
        let literals=Array.map (function Resolved_graph.Literal x -> Some (intern x) | _ -> None) nodes in
        let values=Array.make (Array.length nodes) None in
        Core.phase "post-admission";
        let get k = Option.get values.(k) in
        let rec body bound k =
          let site = if k=graph.body then "top.body" else "top.body." ^ string_of_int k in
          let result = match nodes.(k) with
            | Resolved_graph.Local_parameter ->
              reference site "Local" (obj ["parameter_position",i 1;"input_handle",s handle;"bound_ref",s (Core.id bound)]) (fun ()->bound)
            | Resolved_graph.Literal _ ->
              let value = Option.get literals.(k) in
              reference site "Literal" (obj ["literal_occurrence",s site;"pooled_ref",s (Core.id value)]) (fun ()->value)
            | Resolved_graph.Add (l,r) -> binary "Add" site false (get l) (get r)
            | Resolved_graph.Sub (l,r) -> binary "Sub" site false (get l) (get r) in
          match result with
          | Ok v when k<graph.body -> values.(k)<-Some v; body bound (k+1)
          | _ -> result in
        let entry = reference "top.entry" "Entry" (obj ["parameter_position",i 1;"input_handle",s handle]) (fun ()->input) in
        project (match entry with Error _ as e -> e | Ok bound -> body bound 0)
    end else if mode="obtained" then begin
      (* Ordered private preparation occurrences are supplied as start data,
         independently of the arithmetic evaluator. Admission interns them all. *)
      let rec prepare j acc =
        if j=Array.length Sys.argv then List.rev acc else
        let item=arg j,arg (j+1),intern (arg (j+2)),intern (arg (j+3)),arg (j+4) in
        prepare (j+5) (item::acc) in
      let events=prepare 12 [] in
      header ((if def="trial" then ["program",s "paper-sub";"meter",s "sub-pair";"admission",s "A0";"canonical_descriptor",s "K0";"hash_descriptor",s "H0"] else []) @ ["schedule",Json.Arr (List.map (fun (site,op,l,r,intervention) -> obj
        ["site",s site;"operation",s op;"operands",names [Core.id l;Core.id r];
         "intervention",s (if intervention = "interrupt" then "StagedBeforeCommit" else intervention)]) events)]);
      let seen=Hashtbl.create (List.length events) in
      let unique (label,_,_,_,_) =
        if Hashtbl.mem seen label then false else (Hashtbl.add seen label (); true) in
      if not (List.for_all unique events) then
        output "pre-entry-refusal" ["reason",s "repeated occurrence site"]
      else if not (List.for_all (fun (_,op,_,_,_) -> (op="Add" || op="Sub") && Resolved_graph.operation_allowed ~descriptor op) events) then
        output "pre-entry-refusal" ["reason",s "missing descriptor row"]
      else if scope <> "root" && List.exists (fun (_,op,_,_,_) -> op="Sub") events then
        output "pre-entry-refusal" ["reason",s "unsupported Sub scope"]
      else if not (Hashtbl.mem seen selected) then
        output "pre-entry-refusal" ["reason",s "unknown selected occurrence"]
      else if not (List.for_all (fun (_,op,_,_,intervention) ->
          intervention = "none" || (op = "Add" && intervention = "interrupt")) events) then
        output "pre-entry-refusal" ["reason",s "unsupported intervention"]
      else begin
      Core.phase "post-admission";
      let rec run_events = function
        | [] -> invalid_arg "empty schedule"
        | (site,op,l,r,intervention)::rest ->
          match binary op site (intervention = "interrupt") l r,rest with
          | Ok _,(_::_) -> run_events rest | result,_ -> result in
      project (run_events events)
      end
    end else invalid_arg "mode";
    (* The match/if above is complete before writing the loss check below. *)
    if Probe_switch.enabled then
      emit stderr ["run",s run;"operation",s "end-stream";"count",i !seq]
  end
