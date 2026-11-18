(* Standard-library runner. Test inputs and expected bytes live in fixtures. *)
type test = { name : string; input : string; expected : string }

let read_file path =
  let channel = open_in_bin path in
  Fun.protect
    ~finally:(fun () -> close_in_noerr channel)
    (fun () -> really_input_string channel (in_channel_length channel))

let fixture_leaf name =
  if name = "" || name = "." || name = ".."
     || String.exists (fun c -> c = '/' || c = '\\' || c = ':') name
  then invalid_arg ("fixture must be a file name: " ^ name);
  name

let load_tests path =
  let names = Hashtbl.create 8 in
  read_file path |> String.split_on_char '\n'
  |> List.filter_map (fun raw ->
         let line = String.trim raw in
         if line = "" || line.[0] = '#' then None
         else
           match String.split_on_char '\t' line with
           | [ name; input; expected ] when name <> "" ->
               if Hashtbl.mem names name then
                 invalid_arg ("duplicate test name: " ^ name);
               Hashtbl.add names name ();
               Some
                 { name; input = fixture_leaf input;
                   expected = fixture_leaf expected }
           | _ -> invalid_arg "each test needs name, input and expected, tab-separated")

let run fixtures tests =
  let selected = List.length tests in
  if selected = 0 then (
    Printf.printf "SUMMARY selected=0 passed=0 failed=0\n%!";
    prerr_endline "ERROR zero tests selected";
    2)
  else
    let failed =
      List.fold_left
        (fun count test ->
          try
            let input = read_file (Filename.concat fixtures test.input) in
            let expected = read_file (Filename.concat fixtures test.expected) in
            let actual = Bootstrap.greeting (String.trim input) in
            if actual = expected then (
              Printf.printf "PASS %s\n%!" test.name;
              count)
            else (
              Printf.printf "FAIL %s expected=%S actual=%S\n%!"
                test.name expected actual;
              count + 1)
          with Sys_error message ->
            Printf.printf "FAIL %s error=%S\n%!" test.name message;
            count + 1)
        0 tests
    in
    Printf.printf "SUMMARY selected=%d passed=%d failed=%d\n%!"
      selected (selected - failed) failed;
    if failed = 0 then 0 else 1

let main () =
  let fixtures = ref "" and suite = ref "" in
  let options =
    [ ("--fixtures", Arg.Set_string fixtures, "Fixture directory");
      ("--suite", Arg.Set_string suite, "Plain-text test manifest") ]
  in
  Arg.parse options
    (fun value -> raise (Arg.Bad ("unexpected argument: " ^ value)))
    "test_runner --fixtures DIRECTORY --suite MANIFEST";
  if !fixtures = "" || !suite = "" then
    invalid_arg "both --fixtures and --suite are required";
  run !fixtures (load_tests !suite)

let () =
  let code =
    try main () with
    | Invalid_argument message | Sys_error message ->
        Printf.eprintf "ERROR %s\n%!" message;
        2
  in
  exit code
