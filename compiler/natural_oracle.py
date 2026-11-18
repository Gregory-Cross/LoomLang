"""Development-only decimal oracle; Python integers, with no subject import."""
import argparse
import json
from pathlib import Path
import platform
import sys


def natural(text):
    if not text or any(c < "0" or c > "9" for c in text):
        raise ValueError("expected only ASCII decimal digits")
    return int(text, 10)


def answer(operation, left, right):
    if operation == "parse":
        try:
            return str(natural(left))
        except ValueError:
            return "INVALID"
    value = natural(left)
    if operation == "roundtrip":
        return str(value)
    if operation == "bits":
        return str(value.bit_length())
    other = natural(right)
    if operation == "add":
        return str(value + other)
    if operation == "compare":
        return str((value > other) - (value < other))
    raise ValueError("unknown operation: " + operation)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    # Python's decimal-conversion guard is not a mathematical bound. This
    # interpreter-local setting affects this development oracle process only.
    sys.set_int_max_str_digits(0)
    count = 0
    names = set()
    # Iterate on LF only: a lone CR, including at EOF, is operand data.
    with args.input.open(encoding="utf-8", newline="\n") as source:
        with args.output.open("x", encoding="utf-8", newline="\n") as target:
            for row in source:
                if row.endswith("\n"):
                    row = row[:-1]
                    if row.endswith("\r"):
                        row = row[:-1]
                fields = row.split("\t")
                if len(fields) != 4 or not fields[0] or fields[0] in names:
                    raise ValueError("invalid or duplicate decimal request")
                name, operation, left, right = fields
                names.add(name)
                target.write(name + "\t" + answer(operation, left, right) + "\n")
                count += 1
    print(json.dumps({"oracle": "Python built-in int", "python_version": sys.version,
                      "implementation": platform.python_implementation(),
                      "int_max_str_digits": sys.get_int_max_str_digits(),
                      "processed": count}))
    return 0 if count else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print("ERROR " + str(error), file=sys.stderr)
        sys.exit(2)
