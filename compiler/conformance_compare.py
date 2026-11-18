"""Independent projections of the paper, bounded traces, and decimal-oracle answers."""
import json
import re
import sys

import conformance_data as data
import driver_cases


EVIDENCE_CONTROLS = {"wrong-sharing", "wrong-resource", "stale-source", "stale-build",
                     "stale-profile", "stale-meter", "stale-input"}


def decimal_answers(core, folder, selected, catalog, env, journal):
    requests = []
    for case in selected:
        name = case["id"]
        if name not in catalog["decimal_requests"]:
            continue
        operation, left, right = catalog["decimal_requests"][name]
        match = re.fullmatch(r"def main\[x\]=(add|sub|mul)\[(x|[0-9]+),(x|[0-9]+)\]", case["source"])
        data.require(match is not None, "decimal witness no longer has its named operands")
        arg = case["argv"][case["argv"].index("--input") + 1]
        operands = [arg if text == "x" else text for text in match.groups()[1:]]
        data.require([operation, left, right] == [match.group(1), *operands], "stale decimal-oracle request")
        requests.append((name, operation, left, right))
    if not requests:
        return {}, None
    args_path = folder / "decimal-input.tsv"
    answer_path = folder / "decimal-expected.tsv"
    args_path.write_bytes("".join("\t".join(row) + "\n" for row in requests).encode("ascii"))
    script = data.PROJECT / "natural_oracle.py"
    data.checked(script, catalog["oracle_sha256"])
    proc = core.launch([sys.executable, "-B", script, "--input", args_path, "--output", answer_path],
                       folder, env, journal)
    data.require(proc["exit_code"] == 0 and not proc["stderr"], "decimal oracle process failed")
    receipt = json.loads(proc["stdout"])
    expected_ids = [r[0] for r in requests]
    answers = [line.split("\t") for line in answer_path.read_bytes().decode("ascii").splitlines()]
    data.require(receipt["processed"] == len(requests) and [r[0] for r in answers] == expected_ids
                 and len(set(expected_ids)) == len(expected_ids)
                 and all(len(r) == 2 and re.fullmatch(r"0|[1-9][0-9]*", r[1]) for r in answers),
                 "incomplete, duplicate or invalid decimal answer")
    return dict(answers), {**receipt, "script_sha256": catalog["oracle_sha256"], "keys": expected_ids}


def observe(raw):
    try:
        record = json.loads(raw.decode("utf-8"), object_pairs_hook=driver_cases.unique_object)
    except (ValueError, UnicodeError):
        return {}
    return record if isinstance(record, dict) else {}


def altered(raw, control, other_source):
    report = json.loads(raw, object_pairs_hook=driver_cases.unique_object)
    if control == "wrong-sharing":
        value = report["value"]
        root, child = value["nodes"]
        data.require(root["fields"] == [child["id"], child["id"]], "sharing mutation premise")
        value["nodes"].append({**child, "id": "2"})
        root["fields"][1] = "2"
    elif control == "wrong-resource":
        report["execution"].update(used="0", remaining=report["execution"]["budget"])
    elif control == "stale-source":
        report["source_sha256"] = driver_cases.checksum(other_source)
    elif control == "stale-build":
        report["build_snapshot_sha256"] = "0" * 64
    elif control == "stale-profile":
        report["profile"] = "milestone-b-forms/0-stale"
    elif control == "stale-meter":
        report["meter"] = "milestone-b-ARTW/0-stale"
    elif control == "stale-input":
        report["input"] = "5"
    else:
        raise ValueError("unknown observation mutation")
    changed = driver_cases.compact(report)
    data.require(changed != raw, "control did not change the observation")
    return changed


def projection(case, info, report, native_exit, answer, trace, diagnostic):
    errors = []

    def compare(field, expected, actual):
        if expected != actual:
            errors.append({"field": field, "expected": expected, "actual": actual})

    def fields(key):
        obj = report.get(key)
        return obj if isinstance(obj, dict) else {}

    execution, facts, at = fields("execution"), fields("facts"), fields("at")
    if info is not None:
        paper = info["authored"]["expected"]
        for key in ("status", "code"):
            compare("paper." + key, paper[key], report.get(key))
        compare("paper.exit", paper["exit_code"], native_exit)
        for paper_key, report_key in (("started", "started"), ("fuel_used", "used"), ("fuel_remaining", "remaining")):
            if paper_key in paper:
                compare("paper." + paper_key, paper[paper_key], execution.get(report_key))
        if "value" in paper:
            compare("paper.value", data.graph_projection(paper["value"]), report.get("value"))
        if "invoice" in paper:
            compare("paper.invoice", paper["invoice"], report.get("invoice"))
        if "failed_operation_debit" in paper:
            compare("paper.failed_operation_debit", paper["failed_operation_debit"], facts.get("failed_operation_debit"))
        for key, value in paper.get("facts", {}).items():
            actual = at.get(key) if key == "source_offset" else facts.get(key)
            compare("paper.facts." + key, value, actual)
        for key, value in paper.get("stop", {}).items():
            if key == "event" and value == "row":
                value = "tuple"
            compare("paper.stop." + key, value, facts.get(key) if key == "event" else at.get(key))
    if answer is not None:
        expected = {"root": "0", "nodes": [{"id": "0", "kind": "natural", "decimal": answer}]}
        compare("decimal.value", expected, report.get("value"))
    if trace is not None:
        spent = sum(cost for _, cost in trace["paid"])
        budget = int(case["expected"]["balance"][0])
        compare("trace.execution", {"started": True, "budget": str(budget), "used": str(spent),
                                    "remaining": str(budget - spent)}, execution)
        if "unpaid" in trace:
            stop = trace["unpaid"]
            compare("trace.status", "out_of_fuel", report.get("status"))
            compare("trace.event", stop["event"], facts.get("event"))
            compare("trace.path", stop["path"], at.get("expr_path"))
            compare("trace.definition", stop["definition"], at.get("definition_index"))
            compare("trace.invoice", stop["invoice"], report.get("invoice"))
            compare("trace.failed_operation_debit", "0", facts.get("failed_operation_debit"))
        else:
            compare("trace.status", "returned", report.get("status"))
    if diagnostic is not None:
        source = driver_cases.source_bytes(case)
        needle = diagnostic.encode("utf-8")
        data.require(source.count(needle) == 1, "diagnostic token is ambiguous")
        compare("diagnostic.byte_offset", str(source.index(needle)), at.get("source_offset"))
    return errors


def boundary(status, code):
    if status in ("returned", "out_of_fuel"):
        return "execution"
    if not isinstance(code, str):
        return None
    if status == "tool_error":
        return code
    if status == "refused":
        if code.startswith("invoke.entry"):
            return "checked entry selection"
        return code.split(".")[0]
    return None


def compare_case(core, exe, folder, case, control, env, journal, snapshot, catalog, paper, answers, other_source):
    name = case["id"]
    native = driver_cases.run(core, exe, folder, case, "normal", env, journal,
                              catalog["contract_manifest_sha256"], snapshot)
    stream = "stderr.bin" if case.get("stdout_unwritable") else "stdout.bin"
    stdout = (folder / stream).read_bytes()
    observed = observe(stdout)
    candidate = stdout
    errors = list(native["errors"])
    if control in EVIDENCE_CONTROLS:
        candidate = altered(stdout, control, other_source)
        (folder / "candidate.bin").write_bytes(candidate)
        additional, _gold = driver_cases.compare(case, driver_cases.source_bytes(case), candidate,
                                                native["native_exit"], catalog["contract_manifest_sha256"], snapshot,
                                                folder / case.get("filename", "program.loom"))
        errors.extend(additional)
    record = observe(candidate)
    errors.extend(projection(case, paper.get(name), record, native["native_exit"], answers.get(name),
                             catalog["finite_traces"].get(name), catalog["diagnostic_tokens"].get(name)))
    receipt_path = folder / "process.json"
    proc = json.loads(receipt_path.read_bytes())
    native_status, native_code = observed.get("status"), observed.get("code")
    expected = case["expected"]
    reached = boundary(native_status, native_code) == boundary(expected["status"], expected["code"])
    if not reached:
        errors.append({"field": "boundary", "expected": boundary(expected["status"], expected["code"]),
                       "actual": boundary(native_status, native_code)})
    execution = observed.get("execution")
    checked_program = isinstance(execution, dict) and execution.get("started") is True
    artifacts = native["artifacts"]
    if control in EVIDENCE_CONTROLS:
        artifacts["candidate.bin"] = {"path": str(folder / "candidate.bin"), "sha256": driver_cases.checksum(candidate)}
    return {"name": name, "passed": not errors, "errors": errors, "expected_exit": expected["exit"],
            "native_exit": proc["exit"], "native_pid": proc["pid"], "native_argv": proc["argv"],
            "expected_outcome": expected["status"], "observed_outcome": native_status, "observed_code": native_code,
            "passed_program_check": checked_program, "reached": reached,
            "incomplete_value_agreement": native_status == "out_of_fuel", "source_sha256": native["subject_sha256"],
            "observed_source_sha256": observed.get("source_sha256"), "observed_source_bytes": observed.get("source_bytes"),
            "native_report_sha256": driver_cases.checksum(stdout), "candidate_sha256": driver_cases.checksum(candidate),
            "oracle_answer": answers.get(name), "artifacts": artifacts}
