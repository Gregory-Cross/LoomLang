"""Run the milestone B boundary regressions in a fresh private compiler build directory.

python -B boundary_checks.py --directory DIR [--row A-T1|...|N5]
The selection, observed values, native process records and slot journal are in RESULTS.json.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import driver_build
import driver_cases
import naturals_build as shared
import reader_build


PROJECT = Path(__file__).resolve().parent
FIXTURES = PROJECT / "fixtures/boundaries"
ROWS = ("A-T1", "A-T2", "A-T3", "A-T4", "A-T5", "A-T6", "A-T7", "A-D2", "A-D3", "N5")


def replace_once(data, site, replacement):
    if data.count(site) != 1:
        raise ValueError(f"observer site changed: {site!r}")
    return data.replace(site, replacement)


def observed_source(name, data):
    """Observe work and exception sites only in the private test build."""
    if name == "value.ml":
        site = b"let rec visit a b pending ="
        return replace_once(data, site, site + b"\n    incr Visit_counter.count;")
    if name == "natural.ml":
        site = b"let of_decimal text ="
        return replace_once(data, site, site + b"""
  Option.iter (fun path ->
    let stream = open_out_gen [Open_creat; Open_append; Open_binary] 0o600 path in
    Fun.protect ~finally:(fun () -> close_out stream)
      (fun () -> Printf.fprintf stream "%d\\n" (String.length text)))
    (Sys.getenv_opt "LOOM_TEST_DECIMAL_SIZES");""")
    if name == "run_record.ml":
        # Track where the original raise happened. The production counts and
        # limit conditions remain active, including the later emission check.
        data = replace_once(data, b"exception Value_limit", b"""exception Value_limit
let test_graph_limit_site : (string -> unit) ref = ref (fun _ -> ())
let hit site = (!test_graph_limit_site) site; raise Value_limit""")
        data = replace_once(data, b"let count () =", b'let site = ref "root" in\n    let count () =')
        data = replace_once(data, b"then raise Value_limit else incr minimum", b"then hit !site else incr minimum")
        data = replace_once(data, b"if Seen.mem seen v then resume stack\n      else begin",
                            b'if Seen.mem seen v then resume stack\n      else begin\n        site := (if !minimum = 0 then "root" else "child");')
        data = replace_once(data, b"| (v, i, width) :: rest ->", b'| (v, i, width) :: rest ->\n          site := "edge";')
        data = replace_once(data, b"then raise Value_limit;\n      Buffer.add_string",
                            b'then begin (!test_graph_limit_site) "emit"; raise Value_limit end;\n      Buffer.add_string')
    return data


def build_probes(core, directory, env, journal):
    names = (*driver_build.COMMON, *driver_build.DRIVER, "bootstrap.mli", "bootstrap.ml",
             "test_runner.ml", "reader_probe.ml")
    for name in names:
        (directory / name).write_bytes(observed_source(name, (PROJECT / "src" / name).read_bytes()))
    for name in ("protocol_probe.ml", "value_counts.ml"):
        (directory / name).write_bytes((FIXTURES / name).read_bytes())
    (directory / "visit_counter.ml").write_bytes(b"let count = ref 0\n")
    sources = {p.name: shared.sha(p) for p in sorted(directory.glob("*.ml*"))}
    snapshot = hashlib.sha256(driver_cases.compact(sources)).hexdigest()
    (directory / "driver_identity.ml").write_bytes(driver_build.identity_source(snapshot))
    core.save(directory / "OBSERVED-SOURCES.json", sources)
    modules = ["visit_counter.ml", *driver_build.COMMON, "driver_identity.ml", *driver_build.DRIVER,
               "bootstrap.mli", "bootstrap.ml", "test_runner.ml", "reader_probe.ml", "protocol_probe.ml", "value_counts.ml"]
    shared.command(core, [core.OCAMLOPT, *driver_build.FLAGS, "-c", *modules], directory, env, journal)
    common = ["visit_counter", *driver_build.CORE, "sha256", "driver_identity", "run_record"]
    for target, deps in (("driver", common), ("protocol_probe", common), ("reader_probe", common[:4]),
                         ("value_counts", common[:3]), ("test_runner", ["bootstrap"])):
        objects = [name + ".cmx" for name in (*deps, target)]
        shared.command(core, [core.OCAMLOPT, *objects, "-o", target + ".exe"], directory, env, journal)
    return snapshot


def compare_protocol(raw, expected):
    try:
        actual = json.loads(raw, object_pairs_hook=driver_cases.unique_object)
    except ValueError:
        return None, False
    # JSON encodings distinguish boolean and numeric scalars at every depth.
    matches = json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)
    return actual, matches


def run(directory, rows, result):
    core = shared.load_helper()
    env = core.private_environment(directory)
    journal, cases = result["journal"], result["cases"]
    driver_rows = [json.loads(line) for line in (PROJECT / driver_build.FIXTURES).read_bytes().splitlines()]
    expected_protocol = json.loads((FIXTURES / "protocol.json").read_bytes())

    def record(name, passed, **details):
        cases.append({"name": name, "passed": passed, **details})

    def launch(name, *args):
        return core.launch([directory / (name + ".exe"), *args], directory, env, journal)

    with shared.held_slots(core, ("build", "run"), journal, 600):
        snapshot = build_probes(core, directory, env, journal)
        for row in rows:
            start = len(cases)
            for fixture in driver_rows:
                if not fixture["id"].startswith("agy." + row + "."):
                    continue
                dest = directory / fixture["id"]
                case_env = env
                if row == "N5":
                    case_env = {**env, "LOOM_TEST_DECIMAL_SIZES": str(dest / "decimal-sizes.txt")}
                item = driver_cases.run(core, directory / "driver.exe", dest, fixture, "normal",
                                        case_env, journal, driver_build.PAPER_SHA256, snapshot)
                if row == "N5":
                    sizes = [int(s) for s in (dest / "decimal-sizes.txt").read_bytes().splitlines()]
                    # OCaml's host ceiling is at most 19 decimal digits on the supported 63-bit host.
                    item["conversion_sizes"] = sizes
                    item["passed"] = item["passed"] and bool(sizes) and max(sizes) <= 19
                cases.append(item)
            for name, expected in expected_protocol.items():
                if not name.startswith(row.lower().replace("-", "") + "-"):
                    continue
                observed = launch("protocol_probe", name)
                raw = observed["stdout"]
                if name == "at4-unavailable":
                    expected["report"].update(contract_manifest_sha256=driver_build.PAPER_SHA256,
                                              build_snapshot_sha256=snapshot)
                actual, matches = compare_protocol(raw, expected)
                passed = (observed["exit_code"] == 0 and not observed["stderr"] and matches
                          and raw.endswith("\n") and raw.count("\n") == 1)
                if name == "at3-quote":
                    passed = passed and bytes.fromhex(expected["quoted_hex"]) in raw.encode("utf-8")
                record(name, passed, expected=expected, actual=actual)
                if name in ("at4-unavailable", "at6-guards"):
                    wrong = json.loads(json.dumps(expected))
                    if name == "at4-unavailable":
                        wrong["report"]["execution"]["started"] = 1
                        field = "report.execution.started"
                    else:
                        wrong["entry"]["callbacks"] = True
                        field = "entry.callbacks"
                    decoded, accepted = compare_protocol(json.dumps(wrong) + "\n", expected)
                    record(name + ".wrong-type", decoded is not None and not accepted,
                           field=field, actual=decoded, accepted=accepted)
            if row == "A-T5":
                for fixture in reader_build.select("normal"):
                    if not fixture["id"].startswith("agy.A-T5."):
                        continue
                    name = fixture["id"]
                    source = directory / (name + ".loom")
                    reader_build.write_source(source, fixture)
                    request, actual = directory / (name + ".tsv"), directory / (name + ".out")
                    shared.natural_corpus.write_requests(request, [(name, fixture.get("view", "shape"), "file",
                                                                    source.name, fixture["limit"])])
                    proc = launch("reader_probe", request, actual, "normal")
                    want = name + "\t" + fixture["expect"] + "\n"
                    got = actual.read_bytes().decode("utf-8") if actual.exists() else None
                    record(name, proc["exit_code"] == 0 and proc["stdout"].strip() == "PROCESSED 1"
                           and not proc["stderr"] and got == want, expected=want, actual=got)
            if row == "A-D2":
                valid = b"sample\tgreeting.input\tgreeting.expected"
                malformed = "ERROR each test needs name, input and expected, tab-separated"
                for label, data, error in (
                        ("crlf-comments-blanks", b"\t \r\n  # ignored\t \r\n" + valid + b"\r\n", None),
                        ("leading-tab", b"\t" + valid + b"\r\n", malformed),
                        ("trailing-tab", valid + b"\t\r\n", malformed),
                        ("padded-name-filename", b"  " + valid + b"  \r\n", None),
                        ("padded-filename-validation", b"sample\tgreeting.input\t. \r\n",
                         "ERROR fixture must be a file name: ."),
                        ("padded-duplicate", valid + b"\n " + valid + b"\n", "ERROR duplicate test name: sample"),
                        ("blank-name", b"  \tgreeting.input\tgreeting.expected\n", malformed)):
                    suite = directory / (label + ".tests")
                    suite.write_bytes(data)
                    obs = launch("test_runner", "--fixtures", PROJECT / "fixtures", "--suite", suite)
                    if error is None:
                        ok = obs["exit_code"] == 0 and not obs["stderr"] and obs["stdout"].splitlines() == [
                            "PASS sample", "SUMMARY selected=1 passed=1 failed=0"]
                    else:
                        ok = obs["exit_code"] == 2 and not obs["stdout"] and obs["stderr"].splitlines() == [error]
                    record("manifest." + label, ok, stdout=obs["stdout"], stderr=obs["stderr"], exit=obs["exit_code"])
            if row == "A-D3":
                obs = launch("value_counts")
                lines = obs["stdout"].splitlines()
                ok = obs["exit_code"] == 0 and not obs["stderr"] and len(lines) == 17 and lines[-1] == "OBSERVATIONS 16\tFAILURES 0"
                record("equality.visit-counts", ok, observations=lines, stderr=obs["stderr"])
            expected_count = {"A-T1": 7, "A-T2": 1, "A-T3": 2, "A-T4": 4, "A-T5": 4,
                              "A-T6": 2, "A-T7": 2, "A-D2": 7, "A-D3": 1, "N5": 3}
            if len(cases) - start != expected_count[row]:
                raise ValueError("incomplete case selection for " + row)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", required=True)
    parser.add_argument("--row", choices=ROWS, action="append")
    args = parser.parse_args()
    rows = args.row or ROWS
    if len(set(rows)) != len(rows):
        parser.error("duplicate row")
    directory = shared.load_helper().checked_directory(args.directory)
    directory.mkdir(exist_ok=False)
    result = {"rows": rows, "cases": [], "journal": []}
    try:
        run(directory, rows, result)
        ids = [item["name"] for item in result["cases"]]
        if len(set(ids)) != len(ids) or not ids:
            raise ValueError("missing or duplicate selection")
        return int(any(not item["passed"] for item in result["cases"]))
    finally:
        shared.load_helper().save(directory / "RESULTS.json", result)


if __name__ == "__main__":
    sys.exit(main())
