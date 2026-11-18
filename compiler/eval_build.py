"""Build and compare milestone B frames with the private toolchain and shared slots.

python -B eval_build.py build --kind clean|rebuild --directory DIR
python -B eval_build.py check --control normal|order|repeat|call|read|zero --directory DIR
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import time
import uuid

import naturals_build as shared


PROJECT = Path(__file__).resolve().parent
DEPENDENCIES = ("natural", "value", "reader", "checker", "meter")
EVALUATOR = ("eval.mli", "eval.ml", "eval_probe.ml")
FIXTURES = "fixtures/frames/cases.jsonl"
MODULES = tuple(f"{name}.{ext}" for name in DEPENDENCIES for ext in ("mli", "ml")) + EVALUATOR
INPUTS = ("build.py", "naturals_build.py", "natural_corpus.py", "meter_oracle.py", "frames_oracle.py",
          "eval_build.py", "EVALUATOR.md", "CHECKER.md", "METER.md", FIXTURES, *("src/" + n for n in MODULES))
TUPLE_STEP = "next_field activation at 0 [] fields stack"
MUTATIONS = {
    "order": [(TUPLE_STEP, "next_field activation at (List.length fields - 1) [] (List.rev fields) stack"),
              ("at, index + 1, rest, reversed_values", "at, index - 1, rest, reversed_values")],
    "repeat": [(TUPLE_STEP, "let fields = match fields with\n"
                "            | a :: b :: rest when a.Checker.form = b.Checker.form -> a :: rest\n"
                "            | others -> others in\n          " + TUPLE_STEP)],
    "call": [("structural at Meter.Call;", "structural at Meter.Return;")],
    "read": [("structural at Meter.Variable;", "structural at Meter.Return;")],
}


def inputs():
    return {name: shared.sha(PROJECT / name) for name in INPUTS}


def source_file(target, name, bound, control):
    key = "src/" + name
    data = (PROJECT / key).read_bytes()
    if hashlib.sha256(data).hexdigest() != bound[key]:
        raise RuntimeError("source changed while copying " + key)
    if name == "eval.ml" and control != "normal":
        for old, new in MUTATIONS[control]:
            old, new = old.encode(), new.encode()
            if data.count(old) != 1:
                raise ValueError("plant site changed for " + control)
            data = data.replace(old, new)
    dest = target / name
    dest.write_bytes(data)
    if dest.read_bytes() != data:
        raise RuntimeError("source copy mismatch for " + name)


def build(core, directory, env, result, journal):
    bound = result["source_bindings"]
    version = shared.command(core, [core.OCAMLOPT, "-version"], directory, env, journal)
    result["ocaml_version"] = version["stdout"].strip()
    flags = ["-w", "+a-70", "-warn-error", "+a-70"]
    for name in MODULES[:-len(EVALUATOR)]:
        source_file(directory, name, bound, "normal")
        shared.command(core, [core.OCAMLOPT, *flags, "-c", name], directory, env, journal)
    dependencies = [directory / (stem + ".cmx") for stem in DEPENDENCIES]
    variants = {}
    for control in ("normal", *MUTATIONS):
        target = directory if control == "normal" else directory / control
        target.mkdir(exist_ok=True)
        for name in EVALUATOR:
            source_file(target, name, bound, control)
            shared.command(core, [core.OCAMLOPT, "-I", directory, *flags, "-c", name], target, env, journal)
        exe = target / "eval_probe.exe"
        shared.command(core, [core.OCAMLOPT, "-I", directory, *dependencies, "eval.cmx", "eval_probe.cmx",
                              "-o", exe.name], target, env, journal)
        variants[control] = {"executable": exe.relative_to(directory).as_posix(),
                             "executable_sha256": shared.sha(exe), "eval_source_sha256": shared.sha(target / "eval.ml")}
    if inputs() != bound:
        raise RuntimeError("frame inputs changed during build")
    if len({v["eval_source_sha256"] for v in variants.values()}) != len(variants):
        raise RuntimeError("compiled controls have duplicate source")
    result.update(variants=variants, executable_sha256=variants["normal"]["executable_sha256"])
    tmp = directory / ("EVAL-BUILD-" + uuid.uuid4().hex + ".tmp")
    core.save(tmp, {"inputs": bound, "variants": variants})
    tmp.replace(directory / "EVAL-BUILD.json")
    return 0


def check(core, directory, control, env, result, journal):
    ledger = json.loads((directory / "EVAL-BUILD.json").read_bytes())
    variant = control if control in MUTATIONS else "normal"
    binding = ledger["variants"][variant]
    exe = directory / binding["executable"]
    if (ledger["inputs"] != result["source_bindings"] or shared.sha(exe) != binding["executable_sha256"]
            or shared.sha(exe.parent / "eval.ml") != binding["eval_source_sha256"]):
        raise RuntimeError("stale or mismatched frame executable or source")
    result.update(variant=variant, executable_sha256=binding["executable_sha256"], eval_source_sha256=binding["eval_source_sha256"])
    cases = [json.loads(line) for line in (PROJECT / FIXTURES).read_bytes().splitlines()]
    ids = {c["id"] for c in cases}
    if len(ids) != len(cases) or not {"control." + m for m in MUTATIONS}.issubset(ids):
        raise ValueError("missing or duplicate frame fixtures")
    selected = cases if control == "normal" else [c for c in cases if control != "zero" and c["id"] == "control." + control]
    case = directory / ("check-" + control + "-" + uuid.uuid4().hex)
    case.mkdir()
    subset, requests, expected, actual, compared = [case / n for n in
        ("selected.jsonl", "requests.tsv", "expected.tsv", "actual.tsv", "COMPARISON.json")]
    subset.write_text("".join(json.dumps(c) + "\n" for c in selected), encoding="utf-8", newline="\n")
    required_exit = 0 if selected else 2
    oracle = core.launch([sys.executable, "-B", PROJECT / "frames_oracle.py", "--prices", PROJECT / "src/meter.ml",
                          "--cases", subset, "--directory", case], directory, env, journal)
    if oracle["exit_code"] != required_exit or oracle["stdout"].strip() != f"EXPECTED {len(selected)}":
        raise RuntimeError("frame oracle failed: " + oracle["stderr"])
    native = core.launch([exe, requests, actual], directory, env, journal)
    if native["exit_code"] != required_exit or native["stdout"].strip() != f"PROCESSED {len(selected)}":
        raise RuntimeError("native frame probe failed: " + native["stderr"])
    rows = [line.split("\t") for line in requests.read_text(encoding="utf-8").splitlines()]
    if [r[0] for r in rows] != [c["id"] for c in selected]:
        raise ValueError("wrong subjects in the frame oracle")
    code, comparison = shared.natural_corpus.compare(rows, expected, actual)
    core.save(compared, comparison)
    result.update(control=control, processed=len(selected), comparison=comparison,
                  data_files={p.name: {"path": str(p), "sha256": shared.sha(p)}
                              for p in (subset, requests, expected, actual, compared)},
                  subjects={r[0]: {"path": str(case / r[2]), "sha256": shared.sha(case / r[2])} for r in rows})
    if inputs() != result["source_bindings"]:
        raise RuntimeError("frame inputs changed during comparison")
    return code


def execute(core, args, directory, result, journal):
    building = args.action == "build"
    if building and args.kind == "clean":
        directory.mkdir(parents=True, exist_ok=False)
    elif not (directory / "EVAL-BUILD.json").is_file():
        raise ValueError("rebuild/check requires an existing frame build")
    env = core.private_environment(directory)
    result.update(source_bindings=inputs(), environment=env, directory=str(directory), jobs=1,
                  jobs_reason="ordered module dependencies, then each isolated evaluator variant or serial test process",
                  python_version=sys.version, ocamlopt_sha256=shared.sha(core.OCAMLOPT))
    slots = ("build", "run") if building else ("run",)
    with shared.held_slots(core, slots, journal, args.wait_seconds):
        if building:
            result["kind"] = args.kind
            return build(core, directory, env, result, journal)
        return check(core, directory, args.control, env, result, journal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    compile_cmd = sub.add_parser("build")
    compile_cmd.add_argument("--kind", required=True, choices=("clean", "rebuild"))
    compare_cmd = sub.add_parser("check")
    compare_cmd.add_argument("--control", default="normal", choices=("normal", *MUTATIONS, "zero"))
    for cmd in (compile_cmd, compare_cmd):
        cmd.add_argument("--directory", required=True)
        cmd.add_argument("--wait-seconds", type=int, default=600)
    args = parser.parse_args()
    if args.wait_seconds < 0:
        parser.error("wait-seconds must be nonnegative")
    core = shared.load_helper()
    directory = core.checked_directory(args.directory)
    result = {"action": args.action, "start_utc": core.utc()}
    journal = []
    start = time.perf_counter()
    code = 2
    try:
        code = execute(core, args, directory, result, journal)
    except Exception as error:
        result["error"] = type(error).__name__ + ": " + str(error)
    finally:
        result.update(exit_code=code, end_utc=core.utc(), wall_seconds=time.perf_counter() - start, journal=journal)
        if directory.is_dir():
            logs = directory / "logs"
            logs.mkdir(exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f")
            path = logs / ("frames-" + stamp + ".json")
            core.save(path, result)
            result["log"] = str(path)
        message = {k: v for k, v in result.items() if k not in ("journal", "environment", "subjects", "comparison")}
        if "comparison" in result:
            message["comparison"] = {k: v for k, v in result["comparison"].items() if k != "cases"}
            message["failed_cases"] = [c for c in result["comparison"]["cases"] if not c["passed"]]
        print(json.dumps(message, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
