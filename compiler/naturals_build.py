"""Pieces 2 and 3 commands using piece 1's pinned build/process/slot helpers."""
import argparse
from contextlib import ExitStack, contextmanager
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time
import uuid

import natural_corpus

PROJECT = Path(__file__).resolve().parent
HELPER = PROJECT / "build.py"
HELPER_SHA256 = "f9d1980fe0ef65c284ad0d4b690e77be97d7de21a32c63b4fe0733bfd16ed7e9"
MODULES = ("natural.mli", "natural.ml", "natural_probe.ml")
FILES = ("build.py", "naturals_build.py", "natural_corpus.py", "natural_oracle.py",
         "NATURALS.md", "fixtures/naturals-smoke.tsv", "fixtures/naturals-smoke.expected.tsv",
         *("src/" + name for name in MODULES))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_helper():
    if sha(HELPER) != HELPER_SHA256:
        raise RuntimeError("piece 1 command changed; review/rebind required")
    spec = importlib.util.spec_from_file_location("loom_piece1_build", HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def inputs():
    return {name: sha(PROJECT / name) for name in FILES}


@contextmanager
def held_slots(core, kinds, journal, wait_seconds):
    deadline = time.monotonic() + wait_seconds
    with ExitStack() as stack:
        while True:
            try:
                stack.enter_context(core.slots(kinds, journal))
                break
            except RuntimeError as error:
                if '"state": "BUSY"' not in str(error) or time.monotonic() >= deadline:
                    raise
                print("WAIT shared slot busy; no native work started", file=sys.stderr, flush=True)
                time.sleep(min(10, max(0, deadline - time.monotonic())))
        yield


def command(core, argv, directory, env, journal):
    record = core.launch(argv, directory, env, journal)
    if record["exit_code"] != 0:
        raise RuntimeError("command failed: " + str(argv[0]) + ": " + record["stderr"])
    return record


def execute(core, args, directory, journal):
    if args.action == "build" and args.kind == "clean":
        directory.mkdir(parents=True, exist_ok=False)
    elif not (directory / "NATURAL-BUILD.json").is_file():
        raise ValueError("rebuild/check needs a successful natural build")
    env = core.private_environment(directory)
    before = inputs()
    result = {"action": args.action, "source_bindings": before, "environment": env,
              "directory": str(directory), "jobs": 1,
              "jobs_reason": "ordered interface, implementation, then probe and link",
              "python_version": sys.version, "ocamlopt_sha256": sha(core.OCAMLOPT)}
    if args.action == "build":
        result["kind"] = args.kind
        with held_slots(core, ("build", "run"), journal, args.wait_seconds):
            version = command(core, [core.OCAMLOPT, "-version"], directory, env, journal)
            result["ocaml_version"] = version["stdout"].strip()
            for name in MODULES:
                (directory / name).write_bytes((PROJECT / "src" / name).read_bytes())
                command(core, [core.OCAMLOPT, "-w", "+a-70", "-warn-error", "+a-70", "-c", name],
                        directory, env, journal)
            command(core, [core.OCAMLOPT, "natural.cmx", "natural_probe.cmx", "-o", "natural_probe.exe"],
                    directory, env, journal)
            if inputs() != before:
                raise RuntimeError("source changed during natural build")
            core.save(directory / "NATURAL-BUILD.json", {
                "inputs": before, "executable_sha256": sha(directory / "natural_probe.exe")})
        return 0, result

    case = directory / ("check-" + args.control + "-" + uuid.uuid4().hex)
    case.mkdir()
    rows, metadata = natural_corpus.generate(PROJECT / "fixtures/naturals-smoke.tsv")
    if args.control in ("wrong-sum", "wrong-product"):
        rows = [row for row in rows if row[0] == "control.planted-" + args.control]
        if len(rows) != 1:
            raise RuntimeError("missing planted control: " + args.control)
    elif args.control == "zero":
        rows = []
    requests, expected, actual = (case / name for name in ("requests.tsv", "expected.tsv", "actual.tsv"))
    natural_corpus.write_requests(requests, rows)
    with held_slots(core, ("run",), journal, args.wait_seconds):
        # A rebuild can replace these while we wait. Validate only after the
        # run slot excludes that writer, and keep it through comparison.
        binding = json.loads((directory / "NATURAL-BUILD.json").read_bytes())
        executable_sha256 = sha(directory / "natural_probe.exe")
        if binding["inputs"] != before or binding["executable_sha256"] != executable_sha256:
            raise RuntimeError("stale natural build or changed executable")
        result["executable_sha256"] = executable_sha256
        if args.control == "zero":
            expected.write_bytes(b"")
            actual.write_bytes(b"")
        else:
            oracle = command(core, [sys.executable, "-B", PROJECT / "natural_oracle.py",
                                   "--input", requests, "--output", expected], directory, env, journal)
            result["oracle"] = json.loads(oracle["stdout"])
            if result["oracle"]["processed"] != len(rows):
                raise RuntimeError("oracle count differs from selected")
            argv = [directory / "natural_probe.exe", "--input", requests, "--output", actual]
            if args.control in ("wrong-sum", "wrong-product"):
                argv.append("--inject-" + args.control)
            probe = command(core, argv, directory, env, journal)
            if probe["stdout"].strip() != "PROCESSED " + str(len(rows)):
                raise RuntimeError("probe count differs from selected")
        if args.control == "normal":
            # Independent literal answers guard the oracle's transport/basic operations.
            smoke = (PROJECT / "fixtures/naturals-smoke.tsv").read_text(encoding="utf-8").splitlines()
            literal = (PROJECT / "fixtures/naturals-smoke.expected.tsv").read_text(encoding="utf-8").splitlines()
            oracle_lines = expected.read_text(encoding="utf-8").splitlines()
            if len(smoke) != len(literal) or oracle_lines[:len(literal)] != literal:
                raise RuntimeError("oracle disagrees with the literal smoke answers")
        code, comparison = natural_corpus.compare(rows, expected, actual)
        core.save(case / "COMPARISON.json", comparison)
    if inputs() != before:
        raise RuntimeError("source changed during natural check")
    result.update(control=args.control, corpus=metadata, comparison=comparison,
                  data_files={p.name: {"path": str(p), "sha256": sha(p)}
                              for p in (requests, expected, actual, case / "COMPARISON.json")})
    return code, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    build = sub.add_parser("build")
    build.add_argument("--kind", choices=("clean", "rebuild"), required=True)
    check = sub.add_parser("check")
    check.add_argument("--control", choices=("normal", "wrong-sum", "wrong-product", "zero"), default="normal")
    for option in (build, check):
        option.add_argument("--directory", required=True)
        option.add_argument("--wait-seconds", type=int, default=600)
    args = parser.parse_args()
    if args.wait_seconds < 0:
        parser.error("wait-seconds must be nonnegative")
    core = load_helper()
    directory = core.checked_directory(args.directory)
    journal = []
    started = time.perf_counter()
    result = {"start_utc": core.utc(), "action": args.action}
    code = 2
    try:
        code, detail = execute(core, args, directory, journal)
        result.update(detail)
    except Exception as error:
        result["error"] = type(error).__name__ + ": " + str(error)
    finally:
        result.update(exit_code=code, end_utc=core.utc(), wall_seconds=time.perf_counter() - started,
                      journal=journal)
        if directory.is_dir():
            logs = directory / "logs"
            logs.mkdir(exist_ok=True)
            log = logs / ("natural-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f") + ".json")
            core.save(log, result)
            result["log"] = str(log)
        # Named case results are preserved in the bound report, not truncated stdout.
        public = {key: value for key, value in result.items() if key not in ("journal", "environment", "comparison")}
        if "comparison" in result:
            public["comparison"] = {k: v for k, v in result["comparison"].items() if k != "cases"}
            public["failed_cases"] = [case for case in result["comparison"]["cases"] if not case["passed"]]
        print(json.dumps(public, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
