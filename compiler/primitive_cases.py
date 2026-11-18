"""Development-only primitive fixtures, decimal-oracle protocol and native receipt checks."""
from collections import defaultdict
from dataclasses import dataclass
import json
from frames_oracle import Boundary, Run, definitions, site, value_text
from meter_oracle import part, price_table, priced


PRIMITIVES = {"add", "sub", "mul"}


def indexed_nodes(root):
    pending = [(root, ())]
    while pending:
        node, path = pending.pop()
        yield node, path
        if node.children:
            pending.extend((node.children[i], path + (i,)) for i in reversed(range(len(node.children))))


def arity_refusal(table):
    for owner, _, root in table.values():
        for node, path in indexed_nodes(root):
            if node.name in PRIMITIVES and node.children is not None and len(node.children) != 2:
                facts = f"resolve.primitive_arity:name={node.name},expected=2,actual={len(node.children)}"
                return ["refused", facts, site(owner, path, node.offset), "-", "-"]
    return None


def plan_number(op, x, y):
    # Used to plan nested requests and derive exact test funding. Final
    # receipt generation takes each paid numeric result from natural_oracle.py.
    if op == "add":
        return x + y
    if op == "sub":
        return max(0, x - y)
    return x * y


@dataclass
class Subject:
    spec: dict
    table: dict
    fuel: int | None
    refusal: list | None


def simulate(subject, prices, answers=None):
    c, table, budget = subject.spec, subject.table, subject.fuel
    argument = int(c.get("input", "4"))
    entry = c.get("entry", "main")
    state = Run(prices, budget, "none", argument)
    store = {argument, None}
    for _, _, body in table.values():
        store.update(int(n.name) for n, _ in indexed_nodes(body) if n.name.isdecimal())
    writes, requests, attempts = [], [], []

    def intern(kind, value):
        fresh = value not in store
        if budget is not None:
            writes.append(f"{kind}:{state.balance()}:{int(fresh)}:{value_text(value)}")
        store.add(value)
        return value

    def body(name, arg):
        owner, parameter, root = table[name]

        def visit(node, path):
            op, children, offset = node.name, node.children, node.offset
            if children is None:
                event = "variable" if op == parameter else "literal"
                state.charge(state.fixed[event], owner, path, offset)
                return arg if op == parameter else int(op)
            values = tuple(visit(child, path + (i,)) for i, child in enumerate(children))
            if op == "tuple":
                bill = priced(prices, "tuple", "tuple", width=len(values), fields=sum(map(part, values)))
                state.charge(bill, owner, path, offset)
                return intern("t", values)
            if op not in PRIMITIVES:
                state.charge(state.fixed["call"], owner, path, offset)
                item, = values
                return body(op, item)
            left, right = values
            numeric = type(left) is int and type(right) is int
            row, event = (op, op) if numeric else ("wrong_kind", "wrong-kind/" + op)
            bill = priced(prices, row, event, part(left), part(right))
            if budget is not None:
                attempts.append({"operation": op, "event": event, "at": site(owner, path, offset),
                                 "left": value_text(left), "right": value_text(right),
                                 "components": bill.components, "required": bill.total, "used_before": state.used,
                                 "remaining_before": budget - state.used, "paid": bill.total <= budget - state.used})
            state.charge(bill, owner, path, offset)
            if not numeric:
                return None
            key = f"{c['id']}.op{len(requests) + 1}"
            requests.append((key, op, str(left), str(right)))
            result = plan_number(op, left, right) if answers is None else int(answers[key])
            return intern("n", result)

        result = visit(root, ())
        state.charge(state.fixed["return"], owner, (), root.offset)
        return result

    if subject.refusal is not None:
        fields = subject.refusal.copy()
        started = "0"
    else:
        started = "1"
        try:
            state.charge(state.fixed["entry"], table[entry][0], None, None)
            result = body(entry, argument)
            fields = ["returned", value_text(result), "-", "-", "-"]
        except Boundary as stop:
            fields = stop.fields
    receipt = None if budget is None else "|".join([*fields, state.balance(), started, ";".join(writes) or "-"])
    return state.used, requests, receipt, attempts


def write_rows(path, rows):
    with path.open("x", encoding="utf-8", newline="\n") as out:
        for row in rows:
            out.write("\t".join(row) + "\n")


def prepare(cases, directory, prices_path):
    prices = price_table(prices_path)
    folder = directory / "subjects"
    folder.mkdir()
    subjects, commands, numbers = [], [], []
    for i, c in enumerate(cases):
        source = c["source"]
        table = definitions(source)
        subject = Subject(c, table, None, arity_refusal(table))
        fuel = c["fuel"]
        if fuel in ("exact", "one-less"):
            cost, _, _, _ = simulate(subject, prices)
            subject.fuel = cost - int(fuel == "one-less")
        else:
            subject.fuel = int(fuel)
        if subject.fuel < 0:
            raise ValueError("negative fixture funding")
        filename = f"subjects/{i}.loom"
        (directory / filename).write_bytes(source.encode("utf-8"))
        commands.append((c["id"], "primitives", filename, c.get("entry", "main"), c.get("input", "4"),
                         str(subject.fuel), "-"))
        _, numeric, _, _ = simulate(subject, prices)
        numbers.extend(numeric)
        subjects.append(subject)
    if len({row[0] for row in numbers}) != len(numbers):
        raise ValueError("duplicate planned decimal request")
    write_rows(directory / "requests.tsv", commands)
    write_rows(directory / "decimal-input.tsv", numbers)
    return subjects, commands, numbers, prices


def records(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        fields = line.split("\t")
        if len(fields) != 2 or not fields[0]:
            raise ValueError("malformed keyed output in " + str(path))
        yield fields[0], fields[1]


def expected(subjects, requests, prices, directory):
    answers = {}
    for name, value in records(directory / "decimal-expected.tsv"):
        if name in answers:
            raise ValueError("duplicate decimal oracle result " + name)
        if not value.isascii() or not value.isdecimal() or (len(value) > 1 and value[0] == "0"):
            raise ValueError("noncanonical decimal oracle result " + name)
        answers[name] = value
    if set(answers) != {r[0] for r in requests}:
        raise ValueError("missing or unexpected decimal oracle result")
    replay, receipts, derivations = [], [], {}
    for subject in subjects:
        used, numeric, receipt, attempts = simulate(subject, prices, answers)
        name = subject.spec["id"]
        receipts.append((name, receipt))
        replay.extend(numeric)
        derivations[name] = {"budget": str(subject.fuel), "used": str(used), "attempts": attempts,
                             "decimal_ids": [r[0] for r in numeric]}
    if replay != requests:
        raise ValueError("oracle-backed operands or invocation order differ from the planned decimal requests")
    write_rows(directory / "expected.tsv", receipts)
    (directory / "derivations.json").write_text(json.dumps(derivations, indent=2) + "\n", encoding="utf-8", newline="\n")


def compare(names, expected_path, actual_path, operation):
    if len(set(names)) != len(names):
        raise ValueError("duplicate selected ID")
    expected_by_id, actual_by_id = defaultdict(list), defaultdict(list)
    for target, path in ((expected_by_id, expected_path), (actual_by_id, actual_path)):
        for name, value in records(path):
            target[name].append(value)
    extra = sorted((expected_by_id.keys() | actual_by_id.keys()) - set(names))
    cases, paired = [], 0
    for name in [*names, *extra]:
        want, got = expected_by_id[name], actual_by_id[name]
        row = {"name": name, "operation": operation}
        if name in extra or len(want) != 1 or len(got) != 1:
            row.update(passed=False, expected_count=len(want), actual_count=len(got),
                       reason="unexpected ID" if name in extra else "output count differs from one")
        else:
            paired += 1
            row["passed"] = want[0] == got[0]
            if not row["passed"]:
                row.update(expected=want[0], actual=got[0])
        cases.append(row)
    passed = sum(r["passed"] for r in cases)
    result = {"selected": len(names), "compared": len(names), "value_pairs_compared": paired, "passed": passed,
              "failed": len(cases) - passed, "cases": cases}
    if not names:
        result["error"] = "zero compared count"
    return result


def observed_numbers(native, path):
    rows = []
    for name, receipt in records(native):
        fields = receipt.split("|")
        if len(fields) != 8:
            raise ValueError("malformed native primitive receipt")
        index = 0
        for write in fields[-1].split(";"):
            if write == "-":
                continue
            kind, _, _, value = write.split(":", 3)
            if kind == "n":
                if not value.startswith("N"):
                    raise ValueError("numeric lookup supplied a nonnatural value")
                index += 1
                rows.append((f"{name}.op{index}", value[1:]))
    write_rows(path, rows)
