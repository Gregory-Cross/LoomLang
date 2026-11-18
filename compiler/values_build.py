"""Build and check milestone B values with the existing private OCaml toolchain.

Run python -B values_build.py build --kind clean|rebuild --directory DIR, then
python -B values_build.py check --control normal|wrong-equality|zero --directory DIR.
DIR is a direct child of the compiler build root. A clean build needs a fresh DIR.
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
MODULES = ("natural.mli", "natural.ml", "value.mli", "value.ml", "value_probe.ml")
CASES = "fixtures/values/cases.tsv"
ANSWERS = "fixtures/values/expected.tsv"
FILES = ("build.py", "naturals_build.py", "natural_corpus.py", "values_build.py", "VALUES.md",
         CASES, ANSWERS, *("src/" + name for name in MODULES))


def inputs():
    return {name: shared.sha(PROJECT / name) for name in FILES}


def table(path, columns):
    records = [line.split("\t") for line in path.read_text(encoding="utf-8").splitlines()]
    # A zero-byte frame header is spelled EMPTY in the final TSV field.
    if any(len(row) != columns or not row[0] or not row[-1] for row in records):
        raise ValueError("invalid fixture record in " + str(path))
    if len({row[0] for row in records}) != len(records):
        raise ValueError("duplicate fixture name in " + str(path))
    return records


def check(core, args, directory, env, result, journal):
    rows = table(PROJECT / CASES, 5)
    answers = dict(table(PROJECT / ANSWERS, 2))
    if {row[0] for row in rows} != set(answers):
        raise ValueError("request and literal answer names differ")
    if args.control == "wrong-equality":
        rows = [row for row in rows if row[0] == "control.planted-wrong-equality"]
        if len(rows) != 1:
            raise ValueError("expected exactly one planted equality case")
    elif args.control == "zero":
        rows = []
    case = directory / ("check-" + args.control + "-" + uuid.uuid4().hex)
    case.mkdir()
    requests, expected, actual = (case / name for name in ("requests.tsv", "expected.tsv", "actual.tsv"))
    shared.natural_corpus.write_requests(requests, rows)
    with expected.open("x", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(row[0] + "\t" + answers[row[0]] + "\n")

    with shared.held_slots(core, ("run",), journal, args.wait_seconds):
        executable = directory / "value_probe.exe"
        ledger = json.loads((directory / "VALUE-BUILD.json").read_bytes())
        matched = shared.sha(executable)
        if ledger["inputs"] != result["source_bindings"] or ledger["executable_sha256"] != matched:
            raise RuntimeError("stale value build or changed executable")
        result["executable_sha256"] = matched
        argv = [executable, "--input", requests, "--output", actual]
        if args.control == "wrong-equality":
            argv.append("--inject-wrong-equality")
        probe = core.launch(argv, directory, env, journal)
        if probe["exit_code"] != (0 if rows else 2) or probe["stdout"].strip() != f"PROCESSED {len(rows)}":
            raise RuntimeError("value probe did not process the selection: " + probe["stderr"])
        code, comparison = shared.natural_corpus.compare(rows, expected, actual)
        core.save(case / "COMPARISON.json", comparison)
        result.update(control=args.control, processed=len(rows), comparison=comparison,
                      data_files={p.name: {"path": str(p), "sha256": shared.sha(p)}
                                  for p in (requests, expected, actual, case / "COMPARISON.json")})
    return code


def execute(core, args, directory, result, journal):
    if args.action == "build" and args.kind == "clean":
        directory.mkdir(parents=True, exist_ok=False)
    elif not (directory / "VALUE-BUILD.json").is_file():
        raise ValueError("rebuild/check requires a successful value build")
    env = core.private_environment(directory)
    before = inputs()
    result.update(source_bindings=before, environment=env, directory=str(directory), jobs=1,
                  jobs_reason="ordered Natural and Value interfaces/implementations, then probe and link",
                  python_version=sys.version, ocamlopt_sha256=shared.sha(core.OCAMLOPT))
    if args.action == "build":
        result["kind"] = args.kind
        with shared.held_slots(core, ("build", "run"), journal, args.wait_seconds):
            def command(argv):
                return shared.command(core, argv, directory, env, journal)

            result["ocaml_version"] = command([core.OCAMLOPT, "-version"])["stdout"].strip()
            for module in MODULES:
                target = directory / module
                target.write_bytes((PROJECT / "src" / module).read_bytes())
                if shared.sha(target) != before["src/" + module]:
                    raise RuntimeError("source changed while copying " + module)
                command([core.OCAMLOPT, "-w", "+a-70", "-warn-error", "+a-70", "-c", module])
            command([core.OCAMLOPT, "natural.cmx", "value.cmx", "value_probe.cmx", "-o", "value_probe.exe"])
            if inputs() != before:
                raise RuntimeError("source changed during value build")
            core.save(directory / "VALUE-BUILD.json",
                      {"inputs": before, "executable_sha256": shared.sha(directory / "value_probe.exe")})
        return 0
    code = check(core, args, directory, env, result, journal)
    if inputs() != before:
        raise RuntimeError("source changed during value check")
    return code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    build = sub.add_parser("build")
    build.add_argument("--kind", choices=("clean", "rebuild"), required=True)
    test = sub.add_parser("check")
    test.add_argument("--control", choices=("normal", "wrong-equality", "zero"), default="normal")
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
            log = logs / ("values-" + stamp + ".json")
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
