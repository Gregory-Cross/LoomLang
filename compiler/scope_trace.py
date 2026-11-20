"""Validate and render the documentary milestone B S-case scope and trace view."""

import argparse
from collections import defaultdict
from hashlib import sha256
from itertools import zip_longest
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
SCOPE = "compiler/fixtures/scope/b-scope.json"
VIEW = "compiler/S-CASE-SCOPE.md"
CATALOG = "compiler/fixtures/conformance/claims.json"
S_JSON = "docs/spec/S-CASES.json"
S_MARKDOWN = "docs/spec/S-CASES.md"
RULES = "docs/spec/RULES-EVALUATOR.md"
FIXTURES = {
    "compiler/fixtures/driver/cases.jsonl": "driver_fixtures_sha256",
    "compiler/fixtures/conformance/cases.jsonl": "new_fixtures_sha256",
}
SOURCES = (
    S_JSON, S_MARKDOWN, CATALOG,
    "compiler/DRIVER.md", "compiler/src/driver.ml", "compiler/src/checker.mli",
    "docs/spec/RULES-RUN1.md", "docs/spec/GAPS-RUN1.md",
)
CASE_IDS = (
    "S-SEQ-01", "S-SEQ-02", "S-REUSE-01", "S-MATCH-01", "S-MATCH-02",
    "S-HOST-01", "S-HOST-02", "S-SCOPE-01", "S-FAILURE-01-AFTER-DECISION",
    "C4-S01.related_unequal_hidden_payload", "C4-S02.related_unequal_with_use_and_held",
    "C4-S03.unchecked_relation_checked_inequality",
)
DOC_CASE = "S-SCOPE-01"
DOC_RULES = {"EV-018", "EV-021", "EV-033", "EV-034", "EV-088"}
SLICE_1_CHOICES = ("ROW1-A O2(a)", "ROW1-A O2(b)", "ROW1-A O1(e)")
DISPOSITION_R2 = {
    "subject": "a2e195c5548fc6dccf6371edfced073aa61f4567",
    "seal_sha256": "cabedf24b41d40ac931329a9916a22bd80d1b29af57b7f3fd406ec0058f6bd67",
    "document_sha256": "3ea95b5c1746cdce67695fd6f91e89fbeca807b2e690d990576ee8ab40dcd87a",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    value = dict(pairs)
    require(len(value) == len(pairs), "duplicate JSON property")
    return value


def decode(raw):
    return json.loads(raw, object_pairs_hook=unique_object)


def read(relative):
    return (ROOT / relative).read_bytes()


def checked(relative, expected):
    raw = read(relative)
    require(sha256(raw).hexdigest() == expected, f"stale SHA-256 for {relative}")
    return raw


def matches_hex(value, digits):
    return isinstance(value, str) and re.fullmatch(f"[0-9a-f]{{{digits}}}", value) is not None


def plain_line(value):
    return isinstance(value, str) and bool(value.strip()) and "\n" not in value and "\r" not in value


def exact_keys(value, keys, context):
    require(isinstance(value, dict) and value.keys() == set(keys), f"unexpected fields for {context}")


def scope_cases(rows):
    require(isinstance(rows, list), "expected a list of S cases")
    cases = {}
    for row in rows:
        exact_keys(row, ("id", "runtime", "premise", "b_disposition"), "S case")
        name = row["id"]
        require(name in CASE_IDS, f"unexpected S case ID: {name}")
        require(name not in cases, f"duplicate S case ID: {name}")
        require(row["runtime"] == "NOT RUN", f"{name}: expected runtime NOT RUN")
        require(plain_line(row["premise"]) and plain_line(row["b_disposition"]),
                f"{name}: missing premise or B disposition")
        cases[name] = row
    for name in CASE_IDS:
        require(name in cases, f"missing S case ID: {name}")
    return cases


def documentary_result(rows):
    require(isinstance(rows, list) and len(rows) == 1, "expected one documentary result")
    result = rows[0]
    exact_keys(result, ("id", "classification", "result", "slice_1", "slice_2", "b_profile"),
               "documentary result")
    require(result["id"] == DOC_CASE, f"documentary result must belong to {DOC_CASE}")
    require(result["classification"] == "documentary",
            f"{DOC_CASE}: evidence must stay documentary")
    require(result["result"] == "CONSISTENT WITH THE B PROFILE", f"{DOC_CASE}: unexpected result")
    require(result["slice_2"] == {"selected_policies": [], "execution": "NOT DONE"},
            f"{DOC_CASE}: slice 2 policies must stay unselected and execution NOT DONE")
    choices = result["slice_1"]
    require(isinstance(choices, list), "expected slice 1 decisions")
    for choice in choices:
        exact_keys(choice, ("decision", "policy"), "slice 1 choice")
        require(plain_line(choice["policy"]), "expected slice 1 policy text")
    require(tuple(choice["decision"] for choice in choices) == SLICE_1_CHOICES,
            "slice 1 decision roster differs")
    require(plain_line(result["b_profile"]), "missing B profile account")
    return result


def check_original_cases(json_bytes, markdown_bytes):
    originals = decode(json_bytes)
    require(isinstance(originals, list) and tuple(row["id"] for row in originals) == CASE_IDS,
            "original S-case JSON roster differs")
    for row in originals:
        require("NOT RUN" in row["status"], f'{row["id"]}: original execution status differs')
    rows = re.findall(r"^\| ((?:S-|C4-S)[^| ]+) \|", markdown_bytes.decode("utf-8"), re.M)
    require(tuple(rows) == CASE_IDS, "original S-case Markdown roster differs")


def load_scope():
    scope = decode(read(SCOPE))
    exact_keys(scope, ("schema", "subject", "profile", "disposition", "source_sha256",
                      "cases", "documentary_results"), "B scope")
    require(scope["schema"] == "loom-b-s-scope/1-candidate", "unexpected scope schema")
    require(matches_hex(scope["subject"], 40), "invalid scope commit")
    cases = scope_cases(scope["cases"])
    document = documentary_result(scope["documentary_results"])
    require(scope["disposition"] == DISPOSITION_R2, "disposition binding differs from sealed R2")
    exact_keys(scope["source_sha256"], SOURCES, "scope sources")
    sources = {name: checked(name, scope["source_sha256"][name]) for name in SOURCES}
    check_original_cases(sources[S_JSON], sources[S_MARKDOWN])
    catalog = decode(sources[CATALOG])
    profile = scope["profile"]
    exact_keys(profile, ("name", "meter", "contract_manifest_sha256"), "B profile")
    require(matches_hex(profile["contract_manifest_sha256"], 64)
            and profile["contract_manifest_sha256"] == catalog["contract_manifest_sha256"],
            "profile digest differs from the catalog's forms seal")
    require((profile["name"], profile["meter"]) == (catalog["profile"], catalog["meter"]),
            "profile or meter name differs from the catalog")
    require(sha256(sources["compiler/DRIVER.md"]).hexdigest() == catalog["driver_contract_sha256"],
            "driver contract differs from the catalog")
    return scope, cases, document, catalog


def fixture_locations(catalog):
    locations = {}
    for path, pin in FIXTURES.items():
        for line, raw in enumerate(checked(path, catalog[pin]).splitlines(), 1):
            name = decode(raw)["id"]
            require(name not in locations, f"duplicate fixture ID: {name}")
            locations[name] = path.removeprefix("compiler/"), line
    chosen = [name for group in catalog["claims"].values() for name in group["cases"]]
    require(len(catalog["claims"]) == 8 and len(chosen) == len(set(chosen)) == 90,
            "ordinary claim roster differs")
    require(set(chosen) == catalog["case_clauses"].keys() and set(chosen) <= locations.keys(),
            "ordinary case links or fixture inventory differ")
    require(not set(chosen).intersection(CASE_IDS), "S case credited as an ordinary fixture")
    return {name: locations[name] for name in chosen}


def validate_rules(rules, lines):
    require(len(rules) == 41, "evaluator rule roster differs")
    for rid, rule in rules.items():
        head, standing = rule["line"], rule["standing_line"]
        require(type(head) is int and type(standing) is int and 1 <= head < standing <= len(lines),
                f"{rid}: invalid source locator")
        require(lines[head - 1] == f'## {rid} — {rule["title"]}', f"{rid}: rule heading differs")
        revisions = [line for line in lines[head:standing - 1] if line.startswith("- revision: ")]
        require(revisions == [f'- revision: {rule["revision"]}'], f"{rid}: rule revision differs")
        text = lines[standing - 1]
        require(text == rule["standing_text"]
                and text.split(" — ", 1)[0].casefold() == "- standing: " + rule["standing"],
                f"{rid}: rule standing differs")


def trace_index(catalog, locations):
    rules = catalog["rules"]
    lines = checked(RULES, catalog["rules_file_sha256"]).decode("utf-8").splitlines()
    validate_rules(rules, lines)
    documentary = catalog["documentary"]
    require(documentary.keys() == DOC_RULES and DOC_RULES <= rules.keys(),
            "documentary evaluator roster differs")
    normal = defaultdict(list)
    forms = defaultdict(list)
    for name, relation in catalog["case_clauses"].items():
        form_clauses, rule_clauses = relation["forms"], relation["rules"]
        require(bool(form_clauses) and all(form_clauses.values()) and all(rule_clauses.values()),
                f"{name}: missing observable clause")
        for rid in rule_clauses:
            require(rid in rules and rid not in documentary,
                    f"{name}: unknown or documentary evaluator clause {rid}")
            normal[rid].append(name)
        for clause in form_clauses:
            forms[clause].append(name)
    require(normal.keys() == rules.keys() - DOC_RULES, "normal evaluator link roster differs")

    targets, controls = catalog["control_targets"], catalog["controls"]
    require(targets.keys() == controls.keys() and len(targets) == 19, "control target roster differs")
    by_rule = defaultdict(list)
    for control, target in targets.items():
        selected = controls[control]
        if isinstance(selected, str):
            selected = [selected]
        require(len(selected) == len(set(selected)) and set(selected) <= locations.keys(),
                f"{control}: invalid control selections")
        if target.get("boundary") == "roster":
            exact_keys(target, ("boundary", "field"), control)
        else:
            exact_keys(target, ("case", "clause", "field"), control)
            name, clause = target["case"], target["clause"]
            require(name in selected, f"{control}: target is outside its selected cases")
            relation = catalog["case_clauses"][name]
            require(clause in relation["rules"] or clause in relation["forms"],
                    f"{control}: target clause is outside {name}")
            if clause in rules:
                by_rule[clause].append(control)
    return normal, by_rule, forms


def cell(value):
    return str(value).replace("|", r"\|")


def fixture_ref(name, locations):
    path, line = locations[name]
    return f"[\x60{name}\x60]({path}#L{line})"


def render(scope, cases, document, catalog, locations, normal, controls, forms):
    profile = scope["profile"]
    disposition = scope["disposition"]
    gov = scope["source_sha256"]
    planned = "PLANNED ([subject](#trace-subject))"
    entries = [
        "# Milestone B S-case scope and trace links", "",
        "<!-- Generated by compiler/scope_trace.py. -->", "",
        "## Trace subject", "",
        f"SOURCE. Candidate snapshot \x60{scope['subject']}\x60. "
        f"The catalog labels its base \x60{catalog['base_head']}\x60.",
        f"SOURCE. Forms \x60{profile['name']}\x60, meter \x60{profile['meter']}\x60, "
        f"forms package seal \x60{profile['contract_manifest_sha256']}\x60.",
        f"SOURCE. [Claims catalog](fixtures/conformance/claims.json) SHA-256 \x60{gov[CATALOG]}\x60. "
        f"[Evaluator rules](../{RULES}) SHA-256 \x60{catalog['rules_file_sha256']}\x60.", "",
        f"PROPOSED. The S-case dispositions encode Codex D's R2 at \x60{disposition['subject']}\x60. "
        f"Disposition SHA-256 \x60{disposition['document_sha256']}\x60. "
        f"Package seal \x60{disposition['seal_sha256']}\x60.", "",
        "## S-case disposition", "",
        f"SOURCE. The [original JSON](../{S_JSON}) and [original table](../{S_MARKDOWN}) "
        "retain the complete premises, including the C4 source conditions and current qualifications.",
        f"Their SHA-256 pins are \x60{gov[S_JSON]}\x60 and \x60{gov[S_MARKDOWN]}\x60.", "",
        "PROPOSED. Preserve eligibility, applicability of the payload obligation and sequence reachability "
        "as separate checks on the C4 comparisons. To discharge the sequence premise by absence, establish "
        "that neither initial state reaches a sequence and neither run introduces one. Otherwise check "
        "the matched contents, corresponding identities and changes under RUN1-001 S2.", "",
        "| Original ID | Runtime | Documentary result | Premise and applicable policy | B disposition |",
        "| --- | --- | --- | --- | --- |",
    ]
    for name in CASE_IDS:
        row = cases[name]
        result = "[One comparison](#documentary-comparison)" if name == DOC_CASE else "—"
        entries.append(f"| \x60{name}\x60 | {row['runtime']} | {result} | "
                       f"{cell(row['premise'])} | {cell(row['b_disposition'])} |")
    entries.extend((
        "", "## Documentary comparison", "",
        f"INFERENCE. \x60{document['id']}\x60 is consistent with the B profile. "
        f"Slice 2 execution is **{document['slice_2']['execution']}**. "
        "Slice 2 leaves open what happens after a reply is refused, whether a never-answered "
        "request remains asked, and whether literal admission uses the fixed slice-1 allowance.", "",
        "SOURCE. The slice 1 decisions recorded in the bound disposition are:", "",
    ))
    for choice in document["slice_1"]:
        entries.append(f"- \x60{choice['decision']}\x60. {choice['policy']}")
    entries.extend((
        "", f"SOURCE. {document['b_profile']}",
        f"[Driver source](src/driver.ml) · [Driver contract](DRIVER.md) · "
        f"[Checked forms](src/checker.mli) · [Run rules](../docs/spec/RULES-RUN1.md) · "
        f"[Run gaps](../docs/spec/GAPS-RUN1.md)", "",
        f"SOURCE. {len(cases)} runtime NOT RUN, zero runtime passes, one documentary result, "
        "zero ordinary fixtures and zero positive rule witnesses from these S cases.", "",
        "## Evaluator rule reverse index", "",
        f"SOURCE. The catalog has {len(catalog['rules'])} rules and {len(catalog['claims'])} claim groups "
        f"and links {len(locations)} selected normal fixtures through "
        f"{sum(map(len, normal.values()))} evaluator edges and {sum(map(len, forms.values()))} form edges.",
        f"The {len(DOC_RULES)} documentary evaluator rows have zero positive witnesses. "
        "All normal fixture links below are planned. No observed witness is credited by this view.",
        "An observed witness needs a unique reached and matched native report for the measured subject "
        "from [conformance.py's rule coverage](conformance.py). Control targets have separate receipts.", "",
        "| Evaluator rule and source line | Revision | Standing | Normal fixtures | Control targets | Evidence |",
        "| --- | ---: | --- | --- | --- | --- |",
    ))
    for rid, rule in sorted(catalog["rules"].items()):
        rule_link = f'[\x60{rid}\x60](../{RULES}#L{rule["line"]}) (line {rule["line"]})'
        linked = ", ".join(fixture_ref(name, locations) for name in sorted(normal.get(rid, ()))) or "—"
        targets = ", ".join(f"[\x60{key}\x60](#control-targets)" for key in sorted(controls.get(rid, ()))) or "—"
        evidence = (f"Documentary only. {catalog['documentary'][rid]}"
                    if rid in catalog["documentary"] else planned)
        entries.append(f"| {rule_link} | {rule['revision']} | {cell(rule['standing_text'].removeprefix('- standing: '))} "
                       f"| {linked} | {targets} | {cell(evidence)} |")
    entries.extend((
        "", "## Form clause links", "",
        "SOURCE. The catalog also links ordinary fixtures to clauses of the bound forms package.", "",
        "| Form clause | Normal fixtures | Evidence |",
        "| --- | --- | --- |",
    ))
    for clause, names in sorted(forms.items()):
        links = ", ".join(fixture_ref(name, locations) for name in sorted(names))
        entries.append(f"| \x60{clause}\x60 | {links} | {planned} |")
    entries.extend((
        "", "## Control targets", "",
        f"SOURCE. {len(catalog['control_targets'])} targets from the catalog's \x60control_targets\x60. "
        "These links describe controls and carry no positive witness credit.", "",
        "| Control | Fixture or boundary | Clause | Field | Evidence |",
        "| --- | --- | --- | --- | --- |",
    ))
    for key, target in sorted(catalog["control_targets"].items()):
        ref = fixture_ref(target["case"], locations) if "case" in target else target["boundary"]
        entries.append(f"| \x60{key}\x60 | {ref} | {target.get('clause', '—')} | {cell(target['field'])} | {planned} |")
    return ("\n".join(entries) + "\n").encode("utf-8")


def row_identifier(line):
    match = re.match(rb"\| (?:\[)?\x60([^\x60]+)\x60", line or b"")
    return match[1].decode("utf-8", errors="replace") if match else None


def compare_view(expected, actual):
    for number, (new, old) in enumerate(zip_longest(expected.splitlines(keepends=True),
                                                   actual.splitlines(keepends=True)), 1):
        if new != old:
            expected_id, actual_id = row_identifier(new), row_identifier(old)
            if expected_id and actual_id and expected_id != actual_id:
                detail = f" (expected {expected_id}, found {actual_id})"
            else:
                identifier = expected_id or actual_id
                detail = f" ({identifier})" if identifier else ""
            raise ValueError(f"generated view differs at line {number}{detail}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="compare the generated bytes without writing files")
    args = parser.parse_args()
    try:
        scope, cases, document, catalog = load_scope()
        locations = fixture_locations(catalog)
        normal, controls, forms = trace_index(catalog, locations)
        rendered = render(scope, cases, document, catalog, locations, normal, controls, forms)
        if args.check:
            compare_view(rendered, read(VIEW))
            print(f"{VIEW} matches. {len(cases)} runtime NOT RUN, one documentary result.")
        else:
            sys.stdout.buffer.write(rendered)
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f"Scope trace check failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
