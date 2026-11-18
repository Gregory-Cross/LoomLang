"""Independent integer and transaction model for the provisional B price table."""
import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re


STRUCTURAL = {"entry", "literal", "variable", "call", "return"}
PRIMITIVES = {"add", "sub", "mul"}
COVERED = object()


def price_table(path):
    text = path.read_text(encoding="utf-8")
    marker = "let provisional_prices = [\n"
    if text.count(marker) != 1:
        raise ValueError("expected one provisional price table")
    body = text.split(marker, 1)[1].split("\n]", 1)[0]
    table = {}
    for line in body.splitlines():
        match = re.fullmatch(r"\s*(\w+)_row,\s*\((\w+),\s*(\w+),\s*(\w+),\s*(\w+)\);", line)
        if not match or match[1].lower() in table:
            raise ValueError("invalid price row: " + line)
        table[match[1].lower()] = match.groups()[1:]
    if set(table) != STRUCTURAL | PRIMITIVES | {"wrong_kind", "tuple"}:
        raise ValueError("incomplete provisional table")
    return table


def value(token):
    if token == "none":
        return None
    if token == "empty":
        return ()
    if token == "nested":
        return ((), ())
    if token.startswith("2^"):
        return 1 << int(token[2:])
    if not re.fullmatch(r"0|[1-9][0-9]*", token):
        raise ValueError("bad operand: " + token)
    return int(token)


def part(v):
    return max(1, v.bit_length()) if isinstance(v, int) else 1


@dataclass(frozen=True)
class Quote:
    event: str
    components: tuple | None
    reason: str = ""

    @property
    def total(self):
        return None if self.components is None else sum(self.components)

    def render(self):
        if self.components is None:
            detail = "?" + self.reason
        else:
            detail = ",".join(map(str, (*self.components, self.total)))
        return f"{self.event}({detail})"


def priced(table, row, event, left=0, right=0, width=0, fields=0):
    measures = {"Zero": 0, "One": 1, "Left_part": left, "Sum_parts": left + right,
                "Max_part": max(left, right), "Max_plus_one": max(left, right) + 1,
                "Product_parts": left * right, "Field_sum": fields, "Width_plus_one": width + 1}
    return Quote(event, tuple(measures[c] for c in table[row]))


def prepare(table, step):
    kind, *args = step
    if kind in STRUCTURAL and not args:
        return priced(table, kind, kind), (), None
    if kind == "bits":
        op, left, right = args
        if op not in PRIMITIVES or min(int(left), int(right)) < 1:
            raise ValueError("bad measured widths")
        return priced(table, op, op, int(left), int(right)), (), None
    if kind == "unavailable":
        op, reason = args
        return Quote(op, None, reason), (), None
    operands = tuple(map(value, args))
    if kind == "tuple":
        return priced(table, kind, kind, width=len(operands), fields=sum(map(part, operands))), operands, lambda: operands
    if kind not in PRIMITIVES or len(operands) != 2:
        raise ValueError("bad operation: " + kind)
    x, y = operands
    if not all(isinstance(v, int) for v in operands):
        return priced(table, "wrong_kind", "wrong-kind/" + kind, part(x), part(y)), operands, lambda: None
    def construct():
        if kind == "add":
            return x + y
        if kind == "sub":
            return max(0, x - y)
        return x * y
    return priced(table, kind, kind, part(x), part(y)), operands, construct


def admit(store, v):
    if isinstance(v, tuple):
        for child in v:
            admit(store, child)
    store.add(v)


def budget_for(funding, quotes):
    threshold = sum(q.total for q in quotes if q.total is not None)
    if funding == "exact":
        return threshold
    if funding == "one-less" and threshold > 0:
        return threshold - 1
    if funding == "zero":
        return 0
    if funding.startswith("spare:"):
        return threshold + int(funding[6:])
    raise ValueError("invalid funding selection: " + funding)


def model(table, case):
    steps = [prepare(table, step) for step in case["steps"]]
    through = case.get("through", len(steps))
    if not 1 <= through <= len(steps):
        raise ValueError("bad funding prefix")
    budget = budget_for(case["funding"], [q for q, _, _ in steps[:through]])
    parts = ["budget=" + str(budget)]
    used, remaining, stopped = 0, budget, None
    store = {None}
    derivation = []
    for index, (q, operands, construct) in enumerate(steps):
        for v in operands:
            admit(store, v)
        nodes_before = len(store)
        before = (used, remaining)
        if stopped is None:
            if q.components is None:
                stopped = ("fuel.bound_unavailable", q, index)
            elif q.total > remaining:
                stopped = ("fuel.insufficient", q, index)
        if stopped is not None:
            status, effective, where = stopped
            calls, during, failed_debit = 0, "-", "0"
        else:
            used += q.total
            remaining -= q.total
            effective, where, calls, failed_debit = q, index, 1, "-"
            during = f"{used},{remaining}"
            if case.get("fault_at") == index:
                status = "callback-fault"
            else:
                status = "paid"
                result = COVERED if construct is None else construct()
                if result is not COVERED:
                    admit(store, result)
        assert used + remaining == budget
        parts.append("|".join([q.render(), status, effective.render(), str(where), failed_debit,
                               f"{used},{remaining}", str(calls), during, str(len(store) - nodes_before)]))
        derivation.append({"step": index, "event": q.event, "components": q.components, "cost": q.total,
                           "before": before, "after": (used, remaining), "status": status,
                           "calls": calls, "new_nodes": len(store) - nodes_before, "effective_location": where})
    encoded = ";".join(",".join(step) for step in case["steps"])
    request = (case["id"], "trace", str(budget), str(case.get("fault_at", "-")), encoded)
    return request, ";".join(parts), {"budget": budget, "through": through, "steps": derivation}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("prices", "cases", "requests", "expected", "derivations"):
        parser.add_argument("--" + name, required=True, type=Path)
    args = parser.parse_args()
    table = price_table(args.prices)
    traces = {}
    with args.requests.open("x", encoding="utf-8", newline="\n") as requests, \
            args.expected.open("x", encoding="utf-8", newline="\n") as expected:
        for line in args.cases.read_text(encoding="utf-8").splitlines():
            case = json.loads(line)
            if case["id"] in traces:
                raise ValueError("duplicate case")
            row, result, trace = model(table, case)
            requests.write("\t".join(row) + "\n")
            expected.write(case["id"] + "\t" + result + "\n")
            traces[case["id"]] = trace
    args.derivations.write_text(json.dumps({"provisional_prices": table, "cases": traces}, indent=2) + "\n",
                                encoding="utf-8", newline="\n")
    print("EXPECTED", len(traces))
    return 0 if traces else 2


if __name__ == "__main__":
    raise SystemExit(main())
