"""Test-only structural reference. Ordinary cases use direct recursive interpretation.
The deep generators use their written call patterns without Python recursion.
"""
import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re

from meter_oracle import part, price_table, priced


TOKEN = re.compile(r"[A-Za-z_][A-Za-z_0-9]*|[0-9]+|[\[\],=]|\s+")


@dataclass(frozen=True)
class Node:
    name: str
    offset: int
    children: tuple | None


def definitions(source):
    # These fixtures use the admitted ASCII subset. The native reader and
    # checker independently admit the same source bytes in the probe.
    tokens = [(m[0], m.start()) for m in TOKEN.finditer(source) if not m[0].isspace()]
    if "".join(m[0] for m in TOKEN.finditer(source)) != source or not source.isascii():
        raise ValueError("unexpected fixture text")
    cursor = 0

    def take(wanted=None):
        nonlocal cursor
        name, offset = tokens[cursor]
        cursor += 1
        if wanted is not None and name != wanted:
            raise ValueError(f"expected {wanted} at {offset}")
        return name, offset

    def expr():
        name, offset = take()
        children = None
        if cursor < len(tokens) and tokens[cursor][0] == "[":
            take("[")
            fields = []
            if tokens[cursor][0] != "]":
                fields.append(expr())
                while tokens[cursor][0] == ",":
                    take(",")
                    fields.append(expr())
            take("]")
            children = tuple(fields)
        return Node(name, offset, children)

    result = {}
    while cursor < len(tokens):
        take("def")
        name, _ = take()
        take("[")
        binder, _ = take()
        take("]")
        take("=")
        if name in result:
            raise ValueError("fixture has duplicate definition")
        result[name] = (len(result), binder, expr())
    return result


def value_text(value):
    pending, parts = [value], []
    while pending:
        item = pending.pop()
        if isinstance(item, tuple):
            parts.append("T" + str(len(item)))
            pending.extend(reversed(item))
        else:
            parts.append("N" + str(item))
    return ",".join(parts)


def site(owner, path, offset):
    if path is None:
        shown = "-"
    elif isinstance(path, int):
        shown = f"zeros({path})" if path > 128 else "[" + ",".join(["0"] * path) + "]"
    else:
        shown = "[" + ",".join(map(str, path)) + "]"
    return f"{owner}:{shown}@{offset if offset is not None else '-'}"


class Boundary(Exception):
    def __init__(self, fields):
        super().__init__(*fields)
        self.fields = fields


class Run:
    def __init__(self, prices, fuel, preload, argument):
        self.prices = prices
        self.fixed = {k: priced(prices, k, k) for k in ("entry", "call", "variable", "literal", "return")}
        self.budget = fuel
        self.used = 0
        self.store = set()
        self.tuple_calls = []
        if preload == "empty":
            self.store.add(())
        elif preload == "pair":
            self.store.add((argument, argument))
        elif preload != "none":
            raise ValueError("bad preload")

    def balance(self):
        return f"{self.used},{self.budget - self.used}"

    def charge(self, bill, owner, path, offset):
        if self.budget is not None and bill.total > self.budget - self.used:
            invoice = ",".join(map(str, (*bill.components, bill.total)))
            raise Boundary(["fuel.insufficient", bill.event, site(owner, path, offset), invoice, "0"])
        self.used += bill.total

    def ordinary(self, table, entry, argument):
        def body(name, value):
            owner, binder, expression = table[name]

            def evaluate(node, path):
                tag, children, offset = node.name, node.children, node.offset
                if children is None:
                    if tag == binder:
                        self.charge(self.fixed["variable"], owner, path, offset)
                        return value
                    self.charge(self.fixed["literal"], owner, path, offset)
                    return int(tag)
                values = tuple(evaluate(child, path + (i,)) for i, child in enumerate(children))
                if tag == "tuple":
                    bill = priced(self.prices, "tuple", "tuple", width=len(values), fields=sum(map(part, values)))
                    self.charge(bill, owner, path, offset)
                    new = values not in self.store
                    self.store.add(values)
                    if self.budget is not None:
                        self.tuple_calls.append(f"{self.balance()}:{int(new)}:{value_text(values)}")
                    return values
                if tag in ("add", "sub", "mul"):
                    left, right = values
                    boundary = f"{tag}({value_text(left)}/{value_text(right)})"
                    raise Boundary(["internal-dispatch", boundary, site(owner, path, offset), "-", "-"])
                self.charge(self.fixed["call"], owner, path, offset)
                arg, = values
                return body(tag, arg)

            obtained = evaluate(expression, ())
            self.charge(self.fixed["return"], owner, (), expression.offset)
            return obtained

        self.charge(self.fixed["entry"], table[entry][0], None, None)
        return body(entry, argument)


def generate(case):
    family = case.get("generator")
    if family is None or family == "deep-stop":
        return case["source"]
    depth = case["depth"]
    if depth < 1:
        raise ValueError("invalid generator depth")
    if family == "chain":
        return "".join(f"def f{i}[x]=f{i+1}[x]\n" for i in range(depth - 1)) + f"def f{depth-1}[x]=x\n"
    if family == "nested":
        return "def main[x]=" + "id[" * depth + "x" + "]" * depth + "\ndef id[y]=y\n"
    raise ValueError("unknown generator")


def deep(run, case, source, argument):
    family = case["generator"]
    fixed = run.fixed
    if fixed["return"].total:
        raise ValueError("deep reference requires a covered return")
    run.charge(fixed["entry"], 0, None, None)
    if family == "chain":
        start = 0
        for i, line in enumerate(source.splitlines(keepends=True)):
            body = start + line.index("=") + 1
            if i + 1 == case["depth"]:
                run.charge(fixed["variable"], i, (), body)
            else:
                read_offset = start + line.rindex("[x]") + 1
                run.charge(fixed["variable"], i, (0,), read_offset)
                run.charge(fixed["call"], i, (), body)
            start += len(line)
        return argument
    if family == "nested":
        depth = case["depth"]
        root = source.index("=") + 1
        run.charge(fixed["variable"], 0, depth, root + 3 * depth)
        inner = source.rindex("=") + 1
        for i in reversed(range(depth)):
            run.charge(fixed["call"], 0, i, root + 3 * i)
            run.charge(fixed["variable"], 1, (), inner)
        return argument
    if family != "deep-stop" or run.budget is None:
        raise ValueError("deep recursion requires explicit fuel")
    # main[x]=tuple[spin[x],77] then spin[y]=spin[y]. The second
    # main field remains pending across all repeated spin activations.
    if source != "def main[x]=tuple[spin[x],77] def spin[y]=spin[y]":
        raise ValueError("deep stop control changed shape")
    run.charge(fixed["variable"], 0, (0, 0), source.index("spin[x]") + 5)
    run.charge(fixed["call"], 0, (0,), source.index("spin[x]"))
    period = fixed["variable"].total + fixed["call"].total
    complete = (run.budget - run.used) // period
    run.used += complete * period
    run.charge(fixed["variable"], 1, (0,), source.rindex("spin[y]") + 5)
    run.charge(fixed["call"], 1, (), source.rindex("spin[y]"))
    raise AssertionError("a partial cycle must stop")


def reference(case, prices, source):
    entry, argument = case.get("entry", "main"), int(case.get("input", "4"))
    preload, mode = case.get("preload", "none"), case.get("mode", "normal")
    table = None if "generator" in case else definitions(source)

    def execute(run):
        return run.ordinary(table, entry, argument) if table is not None else deep(run, case, source, argument)

    fuel = case["fuel"]
    if fuel in ("exact", "one-less"):
        dry = Run(prices, None, preload, argument)
        try:
            execute(dry)
        except Boundary as b:
            if b.fields[0] != "internal-dispatch":
                raise
        budget = dry.used - int(fuel == "one-less")
    else:
        budget = int(fuel)
    if budget < 0:
        raise ValueError("negative fixture budget")
    meter = Run(prices, budget, preload, argument)
    try:
        result = execute(meter)
        fields = ["returned", value_text(result), "-", "-", "-"]
    except Boundary as b:
        fields = b.fields
    if mode == "cleanup" and fields[0] != "fuel.insufficient":
        raise ValueError("cleanup fixture must exhaust")
    fields.extend([meter.balance(), ";".join(meter.tuple_calls) or "-", "clear" if mode == "cleanup" else "-"])
    return (entry, str(argument), str(budget), preload, mode), "|".join(fields)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("prices", "cases", "directory"):
        parser.add_argument("--" + name, required=True, type=Path)
    args = parser.parse_args()
    prices = price_table(args.prices)
    subjects = args.directory / "subjects"
    subjects.mkdir()
    count = 0
    with (args.directory / "requests.tsv").open("x", encoding="utf-8", newline="\n") as requests, \
            (args.directory / "expected.tsv").open("x", encoding="utf-8", newline="\n") as expected:
        for line in args.cases.read_bytes().splitlines():
            c = json.loads(line)
            source = generate(c)
            filename = f"subjects/{count}.loom"
            (args.directory / filename).write_bytes(source.encode("utf-8"))
            (entry, argument, fuel, preload, mode), answer = reference(c, prices, source)
            requests.write("\t".join([c["id"], mode, filename, entry, argument, fuel, preload]) + "\n")
            expected.write(c["id"] + "\t" + answer + "\n")
            count += 1
    print("EXPECTED", count)
    return 0 if count else 2


if __name__ == "__main__":
    raise SystemExit(main())
