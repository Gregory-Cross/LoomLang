"""Build and check the provisional milestone B meter with the private OCaml toolchain.

python -B meter_build.py build --kind clean|rebuild --directory DIR
python -B meter_build.py check --control normal|wrong-price|zero --directory DIR
A clean build requires a fresh direct child of the compiler build root.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import time
import uuid

import naturals_build as shared


PROJECT = Path(__file__).resolve().parent
MODULES = ("natural.mli", "natural.ml", "value.mli", "value.ml", "reader.mli", "reader.ml",
           "checker.mli", "checker.ml", "meter.mli", "meter.ml", "meter_probe.ml")
FIXTURES = "fixtures/meter/cases.jsonl"
FILES = ("build.py", "naturals_build.py", "natural_corpus.py", "meter_build.py", "meter_oracle.py",
         "METER.md", "VALUES.md", "CHECKER.md", FIXTURES, *("src/" + n for n in MODULES))
PLANTED = "control.planted-wrong-price"


def inputs():
    return {n: shared.sha(PROJECT / n) for n in FILES}


def wrong_price(source):
    # Omit only addition's work in the negative binary.
    pattern = rb"^([ \t]*Add_row,[ \t]*\(Sum_parts,[ \t]*Max_plus_one,[ \t]*Zero,[ \t]*)Max_part\);"
    planted, count = re.subn(pattern, rb"\g<1>Zero);", source, flags=re.MULTILINE)
    if count != 1:
        raise ValueError("expected one addition work charge to plant")
    return planted


def compile_variant(core, directory, variant, env, journal, before):
    target = directory if variant == "normal" else directory / "wrong-price"
    target.mkdir(exist_ok=True)
    for name in MODULES:
        original = PROJECT / "src" / name
        data = original.read_bytes()
        if hashlib.sha256(data).hexdigest() != before["src/" + name]:
            raise RuntimeError("source changed before copying " + name)
        if variant == "wrong-price" and name == "meter.ml":
            data = wrong_price(data)
        copy = target / name
        copy.write_bytes(data)
        if copy.read_bytes() != data:
            raise RuntimeError("source copy mismatch")
        shared.command(core, [core.OCAMLOPT, "-w", "+a-70", "-warn-error", "+a-70", "-c", name],
                       target, env, journal)
    objects = [Path(n).with_suffix(".cmx").name for n in MODULES if n.endswith(".ml")]
    exe = target / "meter_probe.exe"
    shared.command(core, [core.OCAMLOPT, *objects, "-o", exe.name], target, env, journal)
    return {"executable": exe.relative_to(directory).as_posix(), "executable_sha256": shared.sha(exe),
            "meter_source_sha256": shared.sha(target / "meter.ml")}


def select(control):
    cases = [json.loads(line) for line in (PROJECT / FIXTURES).read_text(encoding="utf-8").splitlines()]
    ids = [c["id"] for c in cases]
    if not cases or len(set(ids)) != len(ids) or PLANTED not in ids:
        raise ValueError("missing or duplicate meter fixtures")
    if control == "zero":
        return []
    if control == "wrong-price":
        return [c for c in cases if c["id"] == PLANTED]
    return cases


def check(core, args, directory, env, result, journal):
    records = select(args.control)
    case = directory / ("check-" + args.control + "-" + uuid.uuid4().hex)
    case.mkdir()
    selected, requests, expected, actual, derivations = (case / n for n in
        ("selected.jsonl", "requests.tsv", "expected.tsv", "actual.tsv", "derivations.json"))
    selected.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8", newline="\n")
    with shared.held_slots(core, ("run",), journal, args.wait_seconds):
        ledger = json.loads((directory / "METER-BUILD.json").read_bytes())
        variant = "wrong-price" if args.control == "wrong-price" else "normal"
        bound = ledger["variants"][variant]
        binary = directory / bound["executable"]
        digest = shared.sha(binary)
        if (ledger["inputs"] != result["source_bindings"] or digest != bound["executable_sha256"]
                or shared.sha(binary.parent / "meter.ml") != bound["meter_source_sha256"]):
            raise RuntimeError("stale meter build, changed executable or changed variant source")
        result.update(variant=variant, executable_sha256=digest, meter_source_sha256=bound["meter_source_sha256"])
        oracle = core.launch([sys.executable, "-B", PROJECT / "meter_oracle.py", "--prices", PROJECT / "src/meter.ml",
                              "--cases", selected, "--requests", requests, "--expected", expected,
                              "--derivations", derivations], directory, env, journal)
        expected_status = 0 if records else 2
        if oracle["exit_code"] != expected_status or oracle["stdout"].strip() != f"EXPECTED {len(records)}":
            raise RuntimeError("meter oracle did not derive the selection: " + oracle["stderr"])
        probe = core.launch([binary, requests, actual], directory, env, journal)
        if probe["exit_code"] != expected_status or probe["stdout"].strip() != f"PROCESSED {len(records)}":
            raise RuntimeError("meter probe did not process the selection: " + probe["stderr"])
        rows = [line.split("\t") for line in requests.read_text(encoding="utf-8").splitlines()]
        if [row[0] for row in rows] != [record["id"] for record in records]:
            raise ValueError("oracle selection differs from requested cases")
        code, comparison = shared.natural_corpus.compare(rows, expected, actual)
        compared = case / "COMPARISON.json"
        core.save(compared, comparison)
        result.update(control=args.control, processed=len(records), comparison=comparison,
                      data_files={p.name: {"path": str(p), "sha256": shared.sha(p)}
                                  for p in (selected, requests, expected, actual, derivations, compared)})
    return code


def execute(core, args, directory, result, journal):
    ledger = directory / "METER-BUILD.json"
    if args.action == "build" and args.kind == "clean":
        directory.mkdir(parents=True, exist_ok=False)
    elif not ledger.is_file():
        raise ValueError("rebuild/check requires a successful meter build")
    env = core.private_environment(directory)
    before = inputs()
    result.update(source_bindings=before, environment=env, directory=str(directory), jobs=1,
                  jobs_reason="ordered interfaces and implementations, isolated serial normal and planted builds",
                  python_version=sys.version, ocamlopt_sha256=shared.sha(core.OCAMLOPT))
    if args.action == "check":
        status = check(core, args, directory, env, result, journal)
        if inputs() != before:
            raise RuntimeError("source changed during meter check")
        return status

    result["kind"] = args.kind
    with shared.held_slots(core, ("build", "run"), journal, args.wait_seconds):
        version = shared.command(core, [core.OCAMLOPT, "-version"], directory, env, journal)
        result["ocaml_version"] = version["stdout"].strip()
        variants = {}
        for variant in ("normal", "wrong-price"):
            variants[variant] = compile_variant(core, directory, variant, env, journal, before)
        if inputs() != before:
            raise RuntimeError("source changed during meter build")
        result.update(variants=variants, executable_sha256=variants["normal"]["executable_sha256"])
        temporary = directory / ("METER-BUILD-" + uuid.uuid4().hex + ".tmp")
        core.save(temporary, {"inputs": before, "variants": variants})
        temporary.replace(ledger)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    build = sub.add_parser("build")
    build.add_argument("--kind", required=True, choices=("clean", "rebuild"))
    test = sub.add_parser("check")
    test.add_argument("--control", default="normal", choices=("normal", "wrong-price", "zero"))
    for option in (build, test):
        option.add_argument("--directory", required=True)
        option.add_argument("--wait-seconds", type=int, default=600)
    args = parser.parse_args()
    if args.wait_seconds < 0:
        parser.error("wait-seconds must be nonnegative")
    core = shared.load_helper()
    directory = core.checked_directory(args.directory)
    journal = []
    tick = time.perf_counter()
    result = {"start_utc": core.utc(), "action": args.action}
    code = 2
    try:
        code = execute(core, args, directory, result, journal)
    except Exception as error:
        result["error"] = type(error).__name__ + ": " + str(error)
    finally:
        result.update(exit_code=code, end_utc=core.utc(), wall_seconds=time.perf_counter() - tick, journal=journal)
        if directory.is_dir():
            logs = directory / "logs"
            logs.mkdir(exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f")
            log = logs / ("meter-" + stamp + ".json")
            core.save(log, result)
            result["log"] = str(log)
        public = {k: v for k, v in result.items() if k not in ("journal", "environment", "comparison")}
        if "comparison" in result:
            public["comparison"] = {k: v for k, v in result["comparison"].items() if k != "cases"}
            public["failed_cases"] = [r for r in result["comparison"]["cases"] if not r["passed"]]
        print(json.dumps(public, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
