"""Run the finite milestone B rule comparisons through the native file driver.

Build the ordinary subject with driver_build.py. Run this command with check
and --directory DIR. Select a negative case family with --control NAME.
For a staged native mutation, build it in a fresh directory first with
conformance.py build --control NAME --directory NEW-DIR, then check that DIR.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import time
import uuid

import conformance_compare as comparison
import conformance_data as data
import conformance_subject as subjects
import driver_build
import driver_cases
import naturals_build as shared


PROJECT = data.PROJECT
HARNESS = ("CONFORMANCE.md", "conformance.py", "conformance_compare.py", "conformance_data.py",
           "conformance_subject.py", "fixtures/conformance/claims.json", "fixtures/conformance/cases.jsonl",
           "natural_oracle.py", "eval_build.py", "driver_cases.py", "driver_build.py")
STAGES = ("generated", "passed_program_check", "reached", "compared", "matched", "mismatched",
          "incomplete_value_agreement", "excluded")


def harness_inputs():
    return {name: shared.sha(PROJECT / name) for name in HARNESS}


def save_lines(path, records):
    path.write_bytes(b"".join(driver_cases.compact(r) for r in records))


def reference(path):
    return {"path": str(path), "sha256": shared.sha(path)}


def count_rows(rows):
    return {stage: sum(row[stage] for row in rows) for stage in STAGES}


def population(headers, captures, submitted):
    by_name = {r["name"]: r for r in captures}
    counts = Counter(submitted)
    rows = []
    for h in headers:
        name = h["id"]
        result = by_name.get(name, {})
        compared = bool(result) and counts[name] == 1
        rows.append({"id": name, "claim": h["claim"], "expected_outcome": h["expected_outcome"],
                     "observed_outcome": result.get("observed_outcome"), "generated": True,
                     "passed_program_check": result.get("passed_program_check", False),
                     "reached": result.get("reached", False), "compared": compared,
                     "matched": compared and result["passed"], "mismatched": compared and not result["passed"],
                     "incomplete_value_agreement": result.get("incomplete_value_agreement", False),
                     "excluded": bool(h["exclusion"]), "reason": h["exclusion"] or result.get("observed_code")})
    claim_counts = {}
    for claim in sorted({r["claim"] for r in rows}):
        cohort = [r for r in rows if r["claim"] == claim]
        claim_counts[claim] = {"total": count_rows(cohort), "by_expected_outcome": {
            status: count_rows([r for r in cohort if r["expected_outcome"] == status])
            for status in sorted({r["expected_outcome"] for r in cohort})}}
    totals = count_rows(rows)
    transitions = [("generated", "passed_program_check"), ("passed_program_check", "reached"), ("reached", "compared")]
    drops = []
    for start, end in transitions:
        dropped = [{"id": r["id"], "reason": r["reason"]} for r in rows if r[start] and not r[end]]
        drops.append({"from": start, "to": end, "net_drop": totals[start] - totals[end], "lost": dropped})
    observed = Counter(r["observed_outcome"] for r in rows if r["observed_outcome"] is not None)
    return {"total": totals, "by_claim": claim_counts, "by_expected_outcome": {
                s: count_rows([r for r in rows if r["expected_outcome"] == s])
                for s in sorted({r["expected_outcome"] for r in rows})},
            "observed_outcomes": dict(observed), "largest_drop": max(drops, key=lambda d: d["net_drop"]),
            "stages": rows}


def header(name, claim, case, paper, catalog, common):
    authored = paper.get(name, {})
    group = catalog["claims"][claim]
    clauses = catalog["case_clauses"][name]
    rules = {rule: {**catalog["rules"][rule], "observable_clause": clause} for rule, clause in clauses["rules"].items()}
    h = {"id": name, "claim": claim, "rules": rules, "forms": clauses["forms"],
         "nearest_wrong": group["nearest_wrong"],
         "paper": {k: v for k, v in authored.items() if k != "authored"}, "exclusion": authored.get("exclusion"),
         "expected_outcome": authored["expected_outcome"] if authored else case["expected"]["status"],
         "bindings": common}
    if case is not None:
        raw = driver_cases.source_bytes(case)
        h.update(adapted_fixture_sha256=driver_cases.checksum(driver_cases.compact(case)),
                 invocation=case["argv"], supplied_source_sha256=None if raw is None else driver_cases.checksum(raw),
                 supplied_source_bytes=None if raw is None else len(raw), expected=case["expected"],
                 source_prerequisite="missing file" if raw is None else "exact finite source bytes",
                 stdout_unwritable=bool(case.get("stdout_unwritable")),
                 decimal_request=catalog["decimal_requests"].get(name), finite_trace=catalog["finite_traces"].get(name),
                 diagnostic_token=catalog["diagnostic_tokens"].get(name))
        if "historical_source" in case:
            historic = case["historical_source"].encode("utf-8")
            h.update(historical_source_sha256=driver_cases.checksum(historic), historical_source_bytes=len(historic))
    return h


def rule_coverage(catalog, headers, captures, received):
    """Index the matched normal observations by the exact rule references in their case headers."""
    counts = Counter(received)
    results = {case["name"]: case for case in captures}
    rules = {rid: {**meta, "scope_only": rid in catalog["documentary"],
                   "documentary_reason": catalog["documentary"].get(rid), "case_ids": [],
                   "witnesses": [], "associated_controls": [], "tested_outcomes": {},
                   "reached": 0, "compared_named_cases": 0, "passed_program_check": 0}
             for rid, meta in catalog["rules"].items()}
    for header_row in headers:
        name = header_row["id"]
        result = results.get(name)
        if counts[name] != 1 or not result or not result["passed"] or not result["reached"]:
            continue
        for rid, edge in header_row["rules"].items():
            rule = rules[rid]
            rule["case_ids"].append(name)
            rule["witnesses"].append({"case": name, "primary_claim": header_row["claim"],
                                      "observable_clause": edge["observable_clause"],
                                      "native_report_sha256": result["native_report_sha256"]})
            rule["reached"] += 1
            rule["compared_named_cases"] += 1
            rule["passed_program_check"] += int(result["passed_program_check"])
            outcome = result["observed_outcome"]
            rule["tested_outcomes"][outcome] = rule["tested_outcomes"].get(outcome, 0) + 1
    for control, target in catalog["control_targets"].items():
        rid = target.get("clause")
        if rid in rules and target["case"] in rules[rid]["case_ids"]:
            rules[rid]["associated_controls"].append(control)
    return {"rule_file_sha256": catalog["rules_file_sha256"], "catalog_sha256": data.CATALOG_SHA256,
            "contract_sha256": data.CONTRACT_SHA256, "base_head": catalog["base_head"],
            "note": "Positive witnesses are matched normal observations. Control targets have separate run receipts.",
            "control_targets": catalog["control_targets"], "rules": rules}


def control_observation(target, captures, roster):
    if target.get("boundary") == "roster":
        field = target["field"]
        evidence = roster["errors"] if field == "zero compared count" else roster[field]
        detected = field in evidence if field == "zero compared count" else bool(evidence)
    else:
        observed = next(c for c in captures if c["name"] == target["case"])
        evidence = [e for e in observed["errors"] if e["field"] == target["field"]]
        detected = bool(evidence)
    return {"target": target, "detected": detected, "evidence": evidence}


def check(core, args, directory, env, journal, result, module, suite):
    catalog, cases, paper, claims, original = suite
    control = args.control
    variant = control if control in ("wrong-cause", "wrong-offset") else "normal"
    exe, rec = module.verify(directory, variant, result)
    if control not in subjects.MUTATIONS and variant == "normal":
        data.require(rec["snapshot_sha256"] == data.BASE_SNAPSHOT, "normal subject differs from the committed snapshot")
    selected_names = list(cases) if control == "normal" else catalog["controls"][control]
    generated = list(claims) if control == "normal" else selected_names
    folder = directory / ("conformance-" + control + "-" + uuid.uuid4().hex)
    folder.mkdir()
    (folder / "paper-original.jsonl").write_bytes(original)
    save_lines(folder / "selected.jsonl", [cases[n] for n in selected_names])
    common = {"rule_file_sha256": catalog["rules_file_sha256"], "design_sha256": catalog["design_file_sha256"],
              "claims_sha256": data.CATALOG_SHA256, "conformance_contract_sha256": data.CONTRACT_SHA256,
              "paper_fixture_sha256": catalog["paper_sha256"], "new_fixtures_sha256": catalog["new_fixtures_sha256"],
              "committed_driver_fixtures_sha256": catalog["driver_fixtures_sha256"],
              "oracle_sha256": catalog["oracle_sha256"], "base_head": catalog["base_head"],
              "contract_manifest_sha256": driver_build.PAPER_SHA256, "snapshot_sha256": rec["snapshot_sha256"],
              "executable_sha256": rec["executable_sha256"], "profile": catalog["profile"], "meter": catalog["meter"],
              "schema": "loom-b-report/1-candidate"}
    headers = [header(n, claims[n], cases.get(n), paper, catalog, common) for n in generated]
    save_lines(folder / "case-headers.jsonl", headers)
    selected = [cases[n] for n in selected_names]
    answers, oracle = comparison.decimal_answers(core, folder, selected, catalog, env, journal)
    other_source = driver_cases.source_bytes(cases["source.refusal-b"])
    captures = []
    for pos, case in enumerate(selected):
        captures.append(comparison.compare_case(core, exe, folder / str(pos), case, control, env, journal,
                                               rec["snapshot_sha256"], catalog, paper, answers, other_source))
    submitted = [r["name"] for r in captures]
    if control == "missing-id":
        submitted = submitted[:-1]
    elif control == "duplicate-id":
        submitted = [*submitted, submitted[0]]
    by_id = {r["name"]: r for r in captures}
    save_lines(folder / "submitted.jsonl", [{"id": n, "native_pid": by_id[n]["native_pid"],
                                             "candidate_sha256": by_id[n]["candidate_sha256"]} for n in submitted])
    transport = data.json_lines((folder / "submitted.jsonl").read_bytes())
    for row in transport:
        original = by_id.get(row["id"])
        data.require(original is not None and row["native_pid"] == original["native_pid"]
                     and row["candidate_sha256"] == original["candidate_sha256"], "unbound submitted observation")
    received = [r["id"] for r in transport]
    counts = Counter(received)
    roster_errors = []
    if not selected_names:
        roster_errors.append("zero compared count")
    missing = [n for n in selected_names if n not in counts]
    duplicate = [n for n, count in counts.items() if count > 1]
    unexpected = sorted(counts.keys() - set(selected_names))
    if missing or duplicate or unexpected or received != selected_names:
        roster_errors.append("missing, duplicate, unexpected or out-of-order compared IDs")
    populations = population(headers, captures, received)
    empty_claims = [n for n, c in populations["by_claim"].items()
                    if not c["total"]["reached"] or not c["total"]["compared"]]
    if control == "normal" and empty_claims:
        roster_errors.append("claim with zero reached or compared cases")
    roster = {"expected": selected_names, "received": received, "missing": missing, "duplicate": duplicate,
              "unexpected": unexpected, "checks": 1, "passed": not roster_errors, "errors": roster_errors}
    core.save(folder / "ROSTER.json", roster)
    core.save(folder / "POPULATIONS.json", populations)
    if control == "normal":
        core.save(folder / "RULE-COVERAGE.json", rule_coverage(catalog, headers, captures, received))
    else:
        observation = control_observation(catalog["control_targets"][control], captures, roster)
        core.save(folder / "CONTROL-OBSERVATION.json", observation)
    totals = populations["total"]
    summary = {"selected": len(selected_names), "compared": totals["compared"], "passed": totals["matched"],
               "failed": totals["mismatched"], "captured": len(captures), "roster_passed": roster["passed"],
               "roster_errors": roster_errors, "zero_population_claims": empty_claims, "cases": captures}
    core.save(folder / "COMPARISON.json", summary)
    result.update(variant=variant, control=control, executable_sha256=rec["executable_sha256"],
                  build_snapshot_sha256=rec["snapshot_sha256"], contract_manifest_sha256=driver_build.PAPER_SHA256,
                  oracle=oracle, comparison=summary, populations=populations["total"],
                  data_files={p.name: reference(p) for p in sorted(folder.iterdir()) if p.is_file()})
    module.verify(directory, variant, result)
    # Keep every genuine mismatch even when a later case stops on fuel or a transport control drops a row.
    if not selected_names:
        return 2
    return int(bool(roster_errors) or any(not case["passed"] for case in captures))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("build", "check"))
    parser.add_argument("--control", default="normal")
    parser.add_argument("--directory", required=True)
    parser.add_argument("--contract-manifest", type=Path, default=driver_build.PAPER)
    parser.add_argument("--wait-seconds", type=int, default=600)
    args = parser.parse_args()
    if args.wait_seconds < 0:
        parser.error("wait seconds must be nonnegative")
    core = shared.load_helper()
    directory = core.checked_directory(args.directory)
    journal = []
    result = {"action": args.action, "start_utc": core.utc(), "directory": str(directory), "jobs": 1,
              "jobs_reason": "ordered native module dependencies and serial CLI observations under the shared slot"}
    start = time.perf_counter()
    exit_code = 2
    try:
        building = args.action == "build"
        if building:
            data.require(args.control in subjects.MUTATIONS, "use driver_build.py for the committed build")
            directory.mkdir(parents=True, exist_ok=False)
        else:
            data.require((directory / "DRIVER-BUILD.json").is_file(), "an existing driver build is required")
        env = core.private_environment(directory)
        with shared.held_slots(core, ("build", "run") if building else ("run",), journal, args.wait_seconds):
            suite = data.load_suite(args.contract_manifest)
            data.require(args.control == "normal" or args.control in suite[0]["controls"], "unknown control")
            module = subjects.subject(directory, args.control, create=building)
            result.update(control=args.control, harness_bindings=harness_inputs(), source_bindings=module.inputs(),
                          paper_members=driver_build.verified_paper(args.contract_manifest), environment=env,
                          ocamlopt_sha256=shared.sha(core.OCAMLOPT), python_version=sys.version)
            if building:
                result["kind"] = "clean"
                exit_code = module.build(core, directory, env, result, journal)
            else:
                exit_code = check(core, args, directory, env, journal, result, module, suite)
            data.require(result["harness_bindings"] == harness_inputs() and result["source_bindings"] == module.inputs(),
                         "inputs changed during conformance command")
            data.load_suite(args.contract_manifest)
    except Exception as error:
        exit_code = 2
        result["error"] = type(error).__name__ + ": " + str(error)
    finally:
        result.update(exit_code=exit_code, end_utc=core.utc(), wall_seconds=time.perf_counter() - start, journal=journal)
        if directory.is_dir():
            logs = directory / "logs"
            logs.mkdir(exist_ok=True)
            log = logs / ("conformance-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f") + ".json")
            core.save(log, result)
            result["log"] = str(log)
        public = {k: v for k, v in result.items() if k not in ("journal", "environment", "comparison")}
        if "comparison" in result:
            public["comparison"] = {k: v for k, v in result["comparison"].items() if k != "cases"}
            public["failed_cases"] = [{"name": c["name"], "errors": c["errors"]}
                                      for c in result["comparison"]["cases"] if not c["passed"]]
        print(json.dumps(public, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
