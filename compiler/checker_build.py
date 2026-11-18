"""Build and check the piece 12b checker with the private milestone B toolchain.

python -B checker_build.py build --kind clean|rebuild --directory DIR
python -B checker_build.py check --control normal|wrong-cause|zero --directory DIR
DIR is a direct child of the compiler build root. A clean build requires a fresh DIR.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import time
import uuid

import naturals_build as shared


PROJECT = Path(__file__).resolve().parent
MODULES = ("natural.mli", "natural.ml", "value.mli", "value.ml",
           "reader.mli", "reader.ml", "checker.mli", "checker.ml", "checker_probe.ml")
FIXTURES = "fixtures/checker/cases.jsonl"
FILES = ("build.py", "naturals_build.py", "natural_corpus.py", "checker_build.py",
         "READER.md", "CHECKER.md", FIXTURES, *("src/" + name for name in MODULES))
PLANTED = {"wrong-cause": "control.planted-wrong-cause"}


def inputs():
    return {name: shared.sha(PROJECT / name) for name in FILES}


def select(control):
    records = [json.loads(line) for line in (PROJECT / FIXTURES).read_text(encoding="utf-8").splitlines()]
    names = [row["id"] for row in records]
    if not records or len(set(names)) != len(names):
        raise ValueError("checker fixtures are empty or have duplicate case names")
    if control == "zero":
        return []
    if control in PLANTED:
        if PLANTED[control] not in names:
            raise ValueError("planted case missing for " + control)
        return [row for row in records if row["id"] == PLANTED[control]]
    return records


def write_source(path, row):
    if "source" in row and "call_depth" not in row:
        data = row["source"].encode("utf-8")
    elif "call_depth" in row and "source" not in row:
        depth = row["call_depth"]
        if type(depth) is not int or depth < 1 or row["leaf"] not in ("x", "missing"):
            raise ValueError("invalid deep checker fixture")
        data = b"def a[x]=" + b"a[" * depth + row["leaf"].encode("ascii") + b"]" * depth
    else:
        raise ValueError("expected one checker source for " + row["id"])
    path.write_bytes(data)


def check(core, args, directory, env, result, journal):
    records = select(args.control)
    case = directory / ("check-" + args.control + "-" + uuid.uuid4().hex)
    case.mkdir()
    requests, expected, actual = (case / name for name in ("requests.tsv", "expected.tsv", "actual.tsv"))
    rows = []
    with expected.open("x", encoding="utf-8", newline="\n") as answers:
        for index, item in enumerate(records):
            filename = f"{index:04d}.loom"
            write_source(case / filename, item)
            rows.append((item["id"], item.get("view", "shape"), filename, item["entry"]))
            answers.write(item["id"] + "\t" + item["expect"] + "\n")
    shared.natural_corpus.write_requests(requests, rows)
    with shared.held_slots(core, ("run",), journal, args.wait_seconds):
        executable = directory / "checker_probe.exe"
        ledger = json.loads((directory / "CHECKER-BUILD.json").read_bytes())
        matched = shared.sha(executable)
        if ledger["inputs"] != result["source_bindings"] or ledger["executable_sha256"] != matched:
            raise RuntimeError("stale checker build or changed executable")
        result["executable_sha256"] = matched
        probe = core.launch([executable, requests, actual, args.control], directory, env, journal)
        if probe["exit_code"] != (0 if rows else 2) or probe["stdout"].strip() != f"PROCESSED {len(rows)}":
            raise RuntimeError("checker probe did not process the selection: " + probe["stderr"])
        code, comparison = shared.natural_corpus.compare(rows, expected, actual)
        core.save(case / "COMPARISON.json", comparison)
        result.update(control=args.control, processed=len(rows), comparison=comparison,
                      data_files={p.name: {"path": str(p), "sha256": shared.sha(p)}
                                  for p in (requests, expected, actual, case / "COMPARISON.json")})
    return code


def execute(core, args, directory, result, journal):
    ledger = directory / "CHECKER-BUILD.json"
    if args.action == "build" and args.kind == "clean":
        directory.mkdir(parents=True, exist_ok=False)
    elif not ledger.is_file():
        raise ValueError("rebuild/check requires a successful checker build")
    env = core.private_environment(directory)
    before = inputs()
    result.update(source_bindings=before, environment=env, directory=str(directory), jobs=1,
                  jobs_reason="ordered Natural, Value, Reader and Checker interfaces and implementations, then probe and link",
                  python_version=sys.version, ocamlopt_sha256=shared.sha(core.OCAMLOPT))
    if args.action == "check":
        code = check(core, args, directory, env, result, journal)
        if inputs() != before:
            raise RuntimeError("source changed during checker check")
        return code

    result["kind"] = args.kind
    with shared.held_slots(core, ("build", "run"), journal, args.wait_seconds):
        def command(argv):
            return shared.command(core, argv, directory, env, journal)

        result["ocaml_version"] = command([core.OCAMLOPT, "-version"])["stdout"].strip()
        for name in MODULES:
            target = directory / name
            target.write_bytes((PROJECT / "src" / name).read_bytes())
            if shared.sha(target) != before["src/" + name]:
                raise RuntimeError("source changed while copying " + name)
            command([core.OCAMLOPT, "-w", "+a-70", "-warn-error", "+a-70", "-c", name])
        exe = "checker_probe.exe"
        command([core.OCAMLOPT, "natural.cmx", "value.cmx", "reader.cmx", "checker.cmx", "checker_probe.cmx", "-o", exe])
        if inputs() != before:
            raise RuntimeError("source changed during checker build")
        result["executable_sha256"] = shared.sha(directory / exe)
        temporary_ledger = directory / ("CHECKER-BUILD-" + uuid.uuid4().hex + ".tmp")
        core.save(temporary_ledger, {"inputs": before, "executable_sha256": result["executable_sha256"]})
        temporary_ledger.replace(ledger)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    build = sub.add_parser("build")
    build.add_argument("--kind", choices=("clean", "rebuild"), required=True)
    test = sub.add_parser("check")
    test.add_argument("--control", choices=("normal", *PLANTED, "zero"), default="normal")
    for option in (build, test):
        option.add_argument("--directory", required=True)
        option.add_argument("--wait-seconds", type=int, default=600)
    args = parser.parse_args()
    if args.wait_seconds < 0:
        parser.error("wait-seconds must be nonnegative")
    core = shared.load_helper()
    directory = core.checked_directory(args.directory)
    journal = []
    started = time.perf_counter()
    result = {"start_utc": core.utc(), "action": args.action}
    code = 2
    try:
        code = execute(core, args, directory, result, journal)
    except Exception as error:
        result["error"] = type(error).__name__ + ": " + str(error)
    finally:
        result.update(exit_code=code, end_utc=core.utc(), wall_seconds=time.perf_counter() - started,
                      journal=journal)
        if directory.is_dir():
            logs = directory / "logs"
            logs.mkdir(exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f")
            log = logs / ("checker-" + stamp + ".json")
            core.save(log, result)
            result["log"] = str(log)
        public = {k: v for k, v in result.items() if k not in ("journal", "environment", "comparison")}
        if "comparison" in result:
            public["comparison"] = {k: v for k, v in result["comparison"].items() if k != "cases"}
            public["failed_cases"] = [row for row in result["comparison"]["cases"] if not row["passed"]]
        print(json.dumps(public, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
