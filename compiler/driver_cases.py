"""Run unchanged CLI invocations and compare exit status, raw report bytes and provenance."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


def checksum(data):
    return hashlib.sha256(data).hexdigest()


def compact(value):
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")


def capture_recovering_stdout(directory, command, out, err):
    """Let the fault fixture finish its stderr report before restoring its private stdout file."""
    import msvcrt

    trace = directory / "fault-trace.txt"
    with (directory / "stdout.bin").open("r+b", buffering=0) as guard:
        msvcrt.locking(guard.fileno(), msvcrt.LK_NBLCK, 1)
        with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=out, stderr=err) as child:
            try:
                deadline = time.monotonic() + 10
                while child.poll() is None:
                    if trace.exists() and b"stderr-flushed" in trace.read_bytes().splitlines():
                        msvcrt.locking(guard.fileno(), msvcrt.LK_UNLCK, 1)
                        child.communicate(input=b"stdout-restored\n", timeout=10)
                        break
                    if time.monotonic() >= deadline:
                        raise TimeoutError("report-fault fixture did not flush stderr")
                    time.sleep(0.01)
                return child.pid, child.returncode
            finally:
                if child.poll() is None:
                    child.kill()


def capture(directory, mode, exe, argv):
    """Run inside the supervisor's Windows job. Preserve the two actual byte streams."""
    def sink(name, unwritable):
        path = directory / name
        if unwritable:
            path.touch(exist_ok=False)
            return path.open("rb")
        return path.open("xb")

    command = [exe, *argv]
    with sink("stdout.bin", mode in ("report-io", "both-unwritable")) as out, sink("stderr.bin", mode == "both-unwritable") as err:
        if mode == "recover-stdout":
            pid, code = capture_recovering_stdout(directory, command, out, err)
        else:
            with subprocess.Popen(command, stdout=out, stderr=err) as child:
                pid, code = child.pid, child.wait()
    (directory / "process.json").write_bytes(compact({"argv": command, "pid": pid, "exit": code}))
    return code


def source_bytes(case):
    if "source" in case:
        return case["source"].encode("utf-8")
    if "source_hex" in case:
        return bytes.fromhex(case["source_hex"])
    return None


def expected(case, raw_source, contract, snapshot, system_error):
    want = case["expected"]
    entry, definition = want["entry"]
    budget, used, remaining = want["balance"]
    di, path, offset = want["at"]
    facts = dict(want["facts"])
    if "system_error" in facts:
        facts["system_error"] = system_error
    return {
        "schema": "loom-b-report/1-candidate", "status": want["status"], "code": want["code"],
        "profile": "milestone-b-forms/1-candidate", "meter": "milestone-b-ARTW/1-candidate",
        "contract_manifest_sha256": contract, "build_snapshot_sha256": snapshot,
        "source_sha256": checksum(raw_source) if want["bound"] else None,
        "source_bytes": str(len(raw_source)) if want.get("length_known", want["bound"]) else None,
        "entry": {"name": entry, "definition_index": definition}, "input": want["input"],
        "checking": {"reading": "unmetered", "resolving": "unmetered", "checking": "unmetered"},
        "reporting": "unmetered", "limits": dict(zip(("source_bytes", "value_bytes"), want["limits"], strict=True)),
        "execution": {"started": want["started"], "budget": budget, "used": used, "remaining": remaining},
        "at": {"definition_index": di, "expr_path": path, "source_offset": offset},
        "invoice": want["invoice"], "value": want["value"], "facts": facts,
    }


def unique_object(pairs):
    obj = dict(pairs)
    if len(obj) != len(pairs):
        raise ValueError("duplicate JSON member")
    return obj


def compare(case, raw_source, raw_report, actual_exit, contract, snapshot, path):
    want = case["expected"]
    errors = []
    if actual_exit != want["exit"]:
        errors.append({"field": "exit", "expected": want["exit"], "actual": actual_exit})
    try:
        report = json.loads(raw_report.decode("utf-8", "strict"), object_pairs_hook=unique_object)
        if not isinstance(report, dict):
            raise ValueError("object required")
    except (UnicodeError, ValueError) as error:
        return errors + [{"field": "report", "error": str(error)}], None
    message = None
    if "system_error" in want["facts"]:
        facts = report.get("facts")
        message = facts.get("system_error") if isinstance(facts, dict) else None
        if not isinstance(message, str) or not message.strip() or (want["code"] == "tool.source_io" and str(path) not in message):
            errors.append({"field": "facts.system_error", "error": "missing observed OS error or failed source path"})
    gold = expected(case, raw_source, contract, snapshot, message)
    for key, value in gold.items():
        if key not in report or report[key] != value:
            errors.append({"field": key, "expected": value, "actual": report.get(key)})
    gold_bytes = compact(gold)
    if raw_report != gold_bytes:
        errors.append({"field": "report_bytes", "expected": checksum(gold_bytes), "actual": checksum(raw_report)})
    return errors, gold_bytes


def run(core, exe, directory, case, control, env, journal, contract, snapshot):
    directory.mkdir()
    source = source_bytes(case)
    path = directory / case.get("filename", "program.loom")
    if source is not None:
        path.write_bytes(source)
        if path.read_bytes() != source:
            raise ValueError("source fixture changed before invocation")
    args = [str(path) if token == "@PROGRAM@" else token for token in case["argv"]]
    mode = "report-io" if case.get("stdout_unwritable") else "normal"
    if case.get("both_unwritable"):
        mode = "both-unwritable"
    if control == "report-faults":
        if case["fault_mode"] == "recover-stdout":
            mode = "recover-stdout"
        env = {**env, "LOOM_DRIVER_TEST_FAULT": case["fault_mode"]}
    record = core.launch([sys.executable, "-B", Path(__file__).resolve(), directory, mode, exe, *args],
                         directory, env, journal)
    process = json.loads((directory / "process.json").read_bytes())
    if process["exit"] != record["exit_code"] or process["argv"] != [str(exe), *args] or record["stdout"] or record["stderr"]:
        raise RuntimeError("CLI child capture failed")
    stdout = (directory / "stdout.bin").read_bytes()
    stderr = (directory / "stderr.bin").read_bytes()
    process_only = "fallback_stderr" in case
    from_stderr = mode != "normal" or process_only
    native = stderr if from_stderr else stdout
    compared = native
    if control == "wrong-digest":
        original = checksum(source).encode("ascii")
        needle = b'"source_sha256":"' + original + b'"'
        if native.count(needle) != 1:
            raise RuntimeError("native source binding missing before evidence control")
        replacement = (b"1" if original.startswith(b"0") else b"0") + original[1:]
        compared = native.replace(needle, b'"source_sha256":"' + replacement + b'"', 1)
    (directory / "compared.bin").write_bytes(compared)
    if process_only:
        gold = case["fallback_stderr"].encode("utf-8")
        errors = []
        if process["exit"] != case["expected"]["exit"]:
            errors.append({"field": "exit", "expected": case["expected"]["exit"], "actual": process["exit"]})
        if compared != gold:
            errors.append({"field": "fallback_stderr", "expected": checksum(gold), "actual": checksum(compared)})
    else:
        errors, gold = compare(case, source, compared, process["exit"], contract, snapshot, path)
    if (stdout if from_stderr else stderr):
        errors.append({"field": "streams", "error": "unexpected bytes on the other stream"})
    if control == "report-faults":
        trace = (directory / "fault-trace.txt").read_bytes().splitlines()
        expected_trace = [event.encode("ascii") for event in case["trace"]]
        if mode == "recover-stdout" and gold is not None:
            system_error = json.loads(gold)["facts"]["system_error"]
            if isinstance(system_error, str):
                expected_trace = [line.replace(b"@OS_ERROR@", system_error.encode("utf-8")) for line in expected_trace]
        if trace != expected_trace:
            errors.append({"field": "fault_trace", "error": "observed calls differ from the selected control"})
    if gold is not None:
        (directory / "expected.bin").write_bytes(gold)
    bindings = {p.name: {"path": str(p), "sha256": checksum(p.read_bytes())}
                for p in sorted(directory.iterdir()) if p.is_file()}
    return {"name": case["id"], "operation": "file driver", "passed": not errors, "errors": errors,
            "expected_exit": case["expected"]["exit"], "native_exit": process["exit"],
            "status": case["expected"].get("status"), "code": case["expected"].get("code"),
            "subject_sha256": None if source is None else checksum(source), "artifacts": bindings}


if __name__ == "__main__":
    raise SystemExit(capture(Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4:]))
