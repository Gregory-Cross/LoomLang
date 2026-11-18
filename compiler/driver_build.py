"""Build and check the milestone B development CLI in the private OCaml environment.

python -B driver_build.py build --kind clean|rebuild --directory DIR
python -B driver_build.py check --control normal|report-faults|wrong-exit|wrong-cause|wrong-offset|wrong-digest|zero --directory DIR
The normal executable is DIR/loom-b.exe.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import time
import uuid

import driver_cases
import naturals_build as shared


PROJECT = Path(__file__).resolve().parent
PAPER = Path.home() / ".codex/reviews/2026-11-17-CODEX-D-MILESTONE-B-FORMS-R1/OUTPUT_BINDINGS.json"
PAPER_SHA256 = "480d8212ab38bef6dacceaedf713a20331160feacd97a110582adaf6373ae33d"
FIXTURES = "fixtures/driver/cases.jsonl"
FAULT_CASES = "fixtures/driver/report-faults.jsonl"
FAULT_PREFIX = "fixtures/driver/report_faults.ml"
CORE = ("natural", "value", "reader", "checker", "meter", "primitives", "eval")
COMMON = tuple(name + ext for name in CORE for ext in (".mli", ".ml")) + ("sha256.ml",)
DRIVER = ("run_record.ml", "driver.ml")
INPUTS = ("build.py", "naturals_build.py", "driver_build.py", "driver_cases.py", "DRIVER.md", FIXTURES, FAULT_CASES, FAULT_PREFIX,
          *("src/" + name for name in (*COMMON, *DRIVER)))
FLAGS = ["-w", "+a-70", "-warn-error", "+a-70"]
PLANTS = {
    "wrong-exit": ("run_record.ml", "Refused -> 3", "Refused -> 0"),
    "wrong-cause": ("driver.ml", 'error "unknown_flag" "token"', 'error "duplicate_flag" "token"'),
    "wrong-offset": ("driver.ml", "Some pos.Reader.source_offset", "Some (pos.Reader.source_offset + 1)"),
}


def inputs():
    return {name: shared.sha(PROJECT / name) for name in INPUTS}


def verified_paper(path):
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != PAPER_SHA256:
        raise ValueError("reviewed contract manifest changed")
    index = json.loads(data)
    items = index if isinstance(index, list) else index["members"]
    members = items if isinstance(items, dict) else {e["path"]: e["sha256"] for e in items}
    for name in ("FORMS.md", "CHARGES.md", "OUTCOMES.md", "FIXTURES.txt"):
        if shared.sha(path.parent / name) != members[name]:
            raise ValueError("reviewed contract member changed: " + name)
    return {name: members[name] for name in ("FORMS.md", "CHARGES.md", "OUTCOMES.md", "FIXTURES.txt")}


def source(name, variant, bound):
    data = (PROJECT / "src" / name).read_bytes()
    if hashlib.sha256(data).hexdigest() != bound["src/" + name]:
        raise RuntimeError("source changed before copy: " + name)
    if variant == "report-faults" and name == "driver.ml":
        prefix = (PROJECT / FAULT_PREFIX).read_bytes()
        if hashlib.sha256(prefix).hexdigest() != bound[FAULT_PREFIX]:
            raise RuntimeError("driver fault fixture changed before copy")
        return prefix + b"\n" + data
    if variant in PLANTS and PLANTS[variant][0] == name:
        _, before, after = PLANTS[variant]
        if data.count(before.encode()) != 1:
            raise ValueError("plant site changed: " + variant)
        data = data.replace(before.encode(), after.encode())
    return data


def snapshot(bound, paper_members, version, compiler_sha, variant):
    native = {name: hashlib.sha256(source(name, variant, bound)).hexdigest() for name in (*COMMON, *DRIVER)}
    return {"schema": "loom-b-build-inputs/1", "variant": variant, "sources": native,
            "build_commands": {key: bound[key] for key in ("build.py", "naturals_build.py", "driver_build.py")},
            "driver_contract_sha256": bound["DRIVER.md"], "contract_manifest_sha256": PAPER_SHA256,
            "contract_members": paper_members, "ocaml_version": version, "ocamlopt_sha256": compiler_sha,
            "warning_flags": FLAGS, "link_modules": [*CORE, "sha256", "driver_identity", "run_record", "driver"]}


def snapshot_bytes(record):
    return (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def identity_source(snapshot_hash):
    return (f'let contract_manifest_sha256 = "{PAPER_SHA256}"\n'
            f'let build_snapshot_sha256 = "{snapshot_hash}"\n').encode("ascii")


def variant_directory(directory, variant):
    return directory if variant == "normal" else directory / variant


def build(core, directory, env, result, journal):
    bound = result["source_bindings"]
    def compile_in(folder, args):
        return shared.command(core, [core.OCAMLOPT, *args], folder, env, journal)
    version = compile_in(directory, ["-version"])["stdout"].strip()
    result["ocaml_version"] = version
    for name in COMMON:
        (directory / name).write_bytes(source(name, "normal", bound))
        compile_in(directory, [*FLAGS, "-c", name])
    common_objects = [directory / (name + ".cmx") for name in (*CORE, "sha256")]
    variants = {}
    for variant in ("normal", *PLANTS, "report-faults"):
        target = variant_directory(directory, variant)
        target.mkdir(exist_ok=True)
        record = snapshot(bound, result["paper_members"], version, result["ocamlopt_sha256"], variant)
        snapshot_path = target / "BUILD-SNAPSHOT.json"
        snapshot_path.write_bytes(snapshot_bytes(record))
        snapshot_hash = shared.sha(snapshot_path)
        identity = target / "driver_identity.ml"
        identity.write_bytes(identity_source(snapshot_hash))
        compile_in(target, ["-I", directory, *FLAGS, "-c", identity.name])
        for name in DRIVER:
            path = target / name
            path.write_bytes(source(name, variant, bound))
            if shared.sha(path) != record["sources"][name]:
                raise RuntimeError("compiled source copy differs: " + name)
            compile_in(target, ["-I", directory, *FLAGS, "-c", name])
        exe = target / "loom-b.exe"
        compile_in(target, ["-I", directory, *common_objects, "driver_identity.cmx", "run_record.cmx", "driver.cmx",
                            "-o", exe])
        variants[variant] = {"executable": exe.relative_to(directory).as_posix(), "executable_sha256": shared.sha(exe),
                             "snapshot_sha256": snapshot_hash, "identity_source_sha256": shared.sha(identity)}
    if inputs() != bound:
        raise RuntimeError("build inputs changed during compilation")
    core.save(directory / "DRIVER-BUILD.json", {"inputs": bound, "ocaml_version": version, "variants": variants})
    result.update(variants=variants, executable_sha256=variants["normal"]["executable_sha256"])
    return 0


def verify(directory, variant, result):
    ledger = json.loads((directory / "DRIVER-BUILD.json").read_bytes())
    target = variant_directory(directory, variant)
    bound = result["source_bindings"]
    if ledger["inputs"] != bound:
        raise ValueError("driver build is stale")
    rec = ledger["variants"][variant]
    snap = snapshot(bound, result["paper_members"], ledger["ocaml_version"], result["ocamlopt_sha256"], variant)
    snap_file = target / "BUILD-SNAPSHOT.json"
    if snap_file.read_bytes() != snapshot_bytes(snap) or shared.sha(snap_file) != rec["snapshot_sha256"]:
        raise ValueError("build snapshot mismatch")
    identity = target / "driver_identity.ml"
    if identity.read_bytes() != identity_source(rec["snapshot_sha256"]) or shared.sha(identity) != rec["identity_source_sha256"]:
        raise ValueError("embedded identity source mismatch")
    for name, digest in snap["sources"].items():
        if shared.sha((directory if name in COMMON else target) / name) != digest:
            raise ValueError("compiled source copy mismatch: " + name)
    exe = target / "loom-b.exe"
    if exe.relative_to(directory).as_posix() != rec["executable"] or shared.sha(exe) != rec["executable_sha256"]:
        raise ValueError("driver executable mismatch")
    return exe, rec


def check(core, directory, control, env, result, journal):
    variant = control if control in (*PLANTS, "report-faults") else "normal"
    exe, rec = verify(directory, variant, result)
    fixtures = FAULT_CASES if control == "report-faults" else FIXTURES
    cases = [json.loads(line) for line in (PROJECT / fixtures).read_bytes().splitlines()]
    ids = [case["id"] for case in cases]
    if not ids or len(ids) != len(set(ids)):
        raise ValueError("empty or duplicate driver inventory")
    if control in ("normal", "report-faults"):
        selected = cases
    elif control == "zero":
        selected = []
    else:
        selected = [case for case in cases if case["id"] == "control." + control]
        if len(selected) != 1:
            raise ValueError("missing planted-control fixture")
    folder = directory / ("check-" + control + "-" + uuid.uuid4().hex)
    folder.mkdir()
    suite = folder / "selected.jsonl"
    suite.write_bytes(b"".join(driver_cases.compact(c) for c in selected))
    records = []
    for index, case in enumerate(selected):
        records.append(driver_cases.run(core, exe, folder / str(index), case, control, env, journal,
                                        PAPER_SHA256, rec["snapshot_sha256"]))
    if [r["name"] for r in records] != [c["id"] for c in selected]:
        raise ValueError("missing, duplicate or reordered CLI record")
    passed = sum(r["passed"] for r in records)
    summary = {"selected": len(selected), "compared": len(records), "passed": passed, "failed": len(records) - passed,
               "cases": records}
    if not records:
        summary["error"] = "zero compared count"
    cmp_path = folder / "COMPARISON.json"
    core.save(cmp_path, summary)
    result.update(variant=variant, control=control, processed=len(records), executable_sha256=rec["executable_sha256"],
                  build_snapshot_sha256=rec["snapshot_sha256"], contract_manifest_sha256=PAPER_SHA256,
                  comparison=summary, data_files={p.name: {"path": str(p), "sha256": shared.sha(p)} for p in (suite, cmp_path)})
    verify(directory, variant, result)
    if inputs() != result["source_bindings"]:
        raise RuntimeError("driver inputs changed during comparison")
    return 2 if not records else int(summary["failed"] > 0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    compiling = sub.add_parser("build")
    compiling.add_argument("--kind", choices=("clean", "rebuild"), required=True)
    checking = sub.add_parser("check")
    checking.add_argument("--control", choices=("normal", "report-faults", *PLANTS, "wrong-digest", "zero"), default="normal")
    for cmd in (compiling, checking):
        cmd.add_argument("--directory", required=True)
        cmd.add_argument("--wait-seconds", type=int, default=600)
        cmd.add_argument("--contract-manifest", type=Path, default=PAPER)
    args = parser.parse_args()
    if args.wait_seconds < 0:
        parser.error("wait seconds must be nonnegative")
    core = shared.load_helper()
    directory = core.checked_directory(args.directory)
    result = {"action": args.action, "start_utc": core.utc(), "directory": str(directory), "jobs": 1,
              "jobs_reason": "ordered native module compilation, then serial file-driver cases"}
    journal = []
    started = time.perf_counter()
    code = 2
    try:
        building = args.action == "build"
        if building and args.kind == "clean":
            directory.mkdir(parents=True, exist_ok=False)
        elif not (directory / "DRIVER-BUILD.json").is_file():
            raise ValueError("rebuild/check requires an existing driver build")
        env = core.private_environment(directory)
        with shared.held_slots(core, ("build", "run") if building else ("run",), journal, args.wait_seconds):
            result.update(source_bindings=inputs(), paper_members=verified_paper(args.contract_manifest),
                          environment=env, ocamlopt_sha256=shared.sha(core.OCAMLOPT), python_version=sys.version)
            if building:
                result["kind"] = args.kind
                code = build(core, directory, env, result, journal)
            else:
                code = check(core, directory, args.control, env, result, journal)
    except Exception as error:
        result["error"] = type(error).__name__ + ": " + str(error)
    finally:
        result.update(exit_code=code, end_utc=core.utc(), wall_seconds=time.perf_counter() - started, journal=journal)
        if directory.is_dir():
            logs = directory / "logs"
            logs.mkdir(exist_ok=True)
            path = logs / ("driver-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f") + ".json")
            core.save(path, result)
            result["log"] = str(path)
        public = {k: v for k, v in result.items() if k not in ("journal", "environment", "comparison")}
        if "comparison" in result:
            public["comparison"] = {k: v for k, v in result["comparison"].items() if k != "cases"}
            public["failed_cases"] = [{k: c[k] for k in ("name", "errors")} for c in result["comparison"]["cases"] if not c["passed"]]
        print(json.dumps(public, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
