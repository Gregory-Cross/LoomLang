"""Read the pinned paper corpus and validate each role-specific runnable projection."""
from collections import Counter
import json
from pathlib import Path
import re

import driver_build
import driver_cases


PROJECT = Path(__file__).resolve().parent
CATALOG = PROJECT / "fixtures/conformance/claims.json"
EXTRA = PROJECT / "fixtures/conformance/cases.jsonl"
CATALOG_SHA256 = "43b9cc54c017bf13dfb0b3130cec2fbdf2b0b187c8cc9098b35409a8952df988"
CONTRACT_SHA256 = "423e262c4d742e85eeb5f2846e0a843a1e064d59b335e308c5e82532b063538e"
BASE_SNAPSHOT = "92e3c5b01918f2cce7d3269b1bf3fa459589ec1146e03dd4c2e4f9451b7e1658"
CONSTRUCTOR_ROWS = {
    "R-demo", "R-demo-spare", "F-demo-one-less",
    "R-empty-row", "R-row", "R-order-a", "R-order-b", "R-reuse-full-row",
    "R-wrong-kind-none", "R-nested-row-part-one", "R-none-in-row", "F-none-one-less", "F-row-one-less",
}
RENAMED = re.compile(r"(?<![A-Za-z0-9_])row(?=\[)")


def checked(path, expected):
    data = path.read_bytes()
    if driver_cases.checksum(data) != expected:
        raise ValueError("stale binding for " + str(path))
    return data


def require(condition, message):
    if not condition:
        raise ValueError(message)


def json_lines(data):
    return [json.loads(line, object_pairs_hook=driver_cases.unique_object) for line in data.splitlines()]


def by_id(rows):
    result = {r["id"]: r for r in rows}
    require(len(rows) == len(result) and all(result), "empty or duplicate fixture ID")
    return result


def paper_argv(fields):
    pairs = [("--program", "@PROGRAM@"), ("--entry", fields["entry"]),
             ("--input", fields["input"]), ("--fuel", fields["fuel"])]
    for key in ("max_source_bytes", "max_value_bytes"):
        if key in fields:
            pairs.append(("--" + key.replace("_", "-"), fields[key]))
    argv = [token for flag, value in pairs if flag not in fields.get("argv_omit", []) for token in (flag, value)]
    return argv + fields.get("argv_extra", [])


def validate_inputs(paper, case):
    fields = paper["input"]
    raw = driver_cases.source_bytes(fields)
    expected = raw
    if paper["id"] in CONSTRUCTOR_ROWS:
        text, count = RENAMED.subn("tuple", fields["source"])
        require(count > 0, "historical constructor role missing")
        expected = text.encode("utf-8")
    require(expected == driver_cases.source_bytes(case), "adapted source differs for " + paper["id"])
    require(paper_argv(fields) == case["argv"], "adapted invocation differs for " + paper["id"])
    require((expected is None) == (fields.get("source_error") == "not_found"), "invalid missing-file premise")
    return raw != expected


def graph_projection(value):
    """Number value-projection nodes on first preorder visit and intern by full paper content."""
    seen = {}
    nodes = []

    def visit(item):
        key = json.dumps(item, sort_keys=True, separators=(",", ":"))
        if key in seen:
            return seen[key]
        ident = str(len(nodes))
        seen[key] = ident
        node = {"id": ident}
        nodes.append(node)
        if set(item) == {"natural"}:
            node.update(kind="natural", decimal=item["natural"])
        elif item == {"none": True}:
            node.update(kind="none")
        elif set(item) == {"row"}:
            node.update(kind="tuple", fields=[visit(child) for child in item["row"]])
        else:
            raise ValueError("unknown paper value")
        return ident

    return {"root": visit(value), "nodes": nodes}


def load_suite(manifest_path):
    checked(PROJECT / "CONFORMANCE.md", CONTRACT_SHA256)
    cat = json.loads(checked(CATALOG, CATALOG_SHA256), object_pairs_hook=driver_cases.unique_object)
    checked(PROJECT / "natural_oracle.py", cat["oracle_sha256"])
    checked(PROJECT / "DRIVER.md", cat["driver_contract_sha256"])
    checked(PROJECT / "driver_build.py", cat["driver_build_sha256"])
    design = PROJECT.parent / "docs/design/DESIGN-TEXT-R20.md"
    if not design.exists():
        design = (manifest_path.parent.parent / "2026-11-18-CODEX-F-R20-Q-FIXES"
                  / "REPLAY-COPY.NOT-THE-REPOSITORY-FILE.DESIGN-TEXT-R20.md")
    checked(design, cat["design_file_sha256"])
    ev = checked(PROJECT.parent / "docs/spec/RULES-EVALUATOR.md", cat["rules_file_sha256"]).decode().splitlines()
    plan = manifest_path.parent.parent / "2026-11-17-CODEX-A-FIRST-MILESTONE-PLAN-OCAML"
    checked(plan / "PLAN.md", cat["plan_sha256"])
    ready = json.loads(checked(plan / "SPEC-READINESS.json", cat["readiness_sha256"]))
    spec = by_id(ready["rules"])
    for rid, rule in cat["rules"].items():
        entry = spec[rid]
        require(entry["file_sha256"] == cat["rules_file_sha256"] and entry["line"] == rule["line"]
                and entry["state"] == rule["standing"] and rule["standing_line"] == entry["standing_line"]
                and ev[rule["line"] - 1].startswith("## " + rid + " ")
                and ev[entry["revision_line"] - 1] == "- revision: " + str(rule["revision"])
                and ev[rule["standing_line"] - 1] == rule["standing_text"] == entry["standing_text"],
                "rule revision or standing differs for " + rid)
    paper_members = driver_build.verified_paper(manifest_path)
    require(driver_build.PAPER_SHA256 == cat["contract_manifest_sha256"]
            and paper_members["FIXTURES.txt"] == cat["paper_sha256"], "paper contract mismatch")
    original = checked(manifest_path.parent / "FIXTURES.txt", cat["paper_sha256"])
    paper_rows = json_lines(original)
    by_id(paper_rows)
    expected_counts = {"returned": 24, "out_of_fuel": 15, "refused": 32, "tool_error": 3}
    require(Counter(r["expected"]["status"] for r in paper_rows) == expected_counts, "original populations changed")
    committed = by_id(json_lines(checked(PROJECT / driver_build.FIXTURES, cat["driver_fixtures_sha256"])))
    extra_rows = by_id(json_lines(checked(EXTRA, cat["new_fixtures_sha256"])))
    require(committed.keys().isdisjoint(extra_rows), "fixture ID in both committed and piece 17 data")
    paper_cases = {name: case for name, case in (committed | extra_rows).items() if "paper_line" in case}
    require(set(paper_cases) == {"paper." + row["id"] for row in paper_rows}, "paper projection roster differs")
    chosen = {}
    claims = {}
    for claim, spec_row in cat["claims"].items():
        require(spec_row["cases"], "empty primary claim")
        for name in spec_row["cases"]:
            require(name not in claims, "duplicate case across primary claims")
            claims[name] = claim
    paper_info = {}
    for index, (line, authored) in enumerate(zip(original.splitlines(keepends=True), paper_rows, strict=True), 1):
        name = "paper." + authored["id"]
        require(authored["execution"] == "NOT RUN", "paper execution standing changed")
        info = {"id": name, "authored_id": authored["id"], "line": index,
                "original_line_sha256": driver_cases.checksum(line), "original_execution": authored["execution"],
                "authored": authored, "expected_outcome": authored["expected"]["status"]}
        paper_info[name] = info
        case = paper_cases[name]
        require(case["paper_line"] == index, "paper line mismatch")
        info["historical_spelling_adapted"] = validate_inputs(authored, case)
        chosen[name] = case
    require(len(chosen) == len(paper_info) == 74, "paper selection incomplete")
    for name in cat["existing_cases"]:
        require(name not in chosen, "duplicate supplemental case")
        chosen[name] = committed[name]
    for name, case in extra_rows.items():
        if name in paper_cases:
            continue
        require(name not in chosen, "duplicate supplemental case")
        if "historical_source" in case:
            raw = case["historical_source"]
            adapted, count = RENAMED.subn("tuple", raw)
            require(count == 1 and adapted == case["source"], "supplemental role translation changed")
            size = len(adapted.encode("utf-8"))
            if name == "trace.renamed-offset":
                require(case["expected"]["at"][2] == str(adapted.encode().index(b"#")), "adapted offset changed")
            else:
                cap = size if name == "trace.renamed-cap-exact" else size - 1
                require(case["argv"][-2:] == ["--max-source-bytes", str(cap)], "adapted source cap changed")
        chosen[name] = case
    require(len(chosen) == 90 and claims.keys() == chosen.keys() == cat["case_clauses"].keys(),
            "missing or unexpected member of the case inventory")
    documentary = cat["documentary"].keys()
    credited = set()
    for name, relation in cat["case_clauses"].items():
        rules, forms = relation["rules"], relation["forms"]
        require(forms and all(forms.values()) and all(rules.values()), "missing observable clause for " + name)
        require(rules.keys() <= cat["rules"].keys() and rules.keys().isdisjoint(documentary),
                "unknown or documentary rule credited to " + name)
        credited.update(rules)
    require(credited | documentary == cat["rules"].keys(), "rule missing from the coverage inventory")
    require(cat["controls"].keys() == cat["control_targets"].keys(), "control target missing")
    for control, target in cat["control_targets"].items():
        if target.get("boundary") == "roster":
            continue
        name = target["case"]
        require(name in cat["controls"][control], "target outside the selected control")
        relation = cat["case_clauses"][name]
        require(target["clause"] in relation["rules"] or target["clause"] in relation["forms"],
                "control targets a clause outside its case")
    require(all(len(ids) == len(set(ids)) and set(ids) <= chosen.keys() for ids in cat["controls"].values()),
            "invalid control roster")
    return cat, chosen, paper_info, claims, original
