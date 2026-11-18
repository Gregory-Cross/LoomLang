"""Finite, reproducible decimal corpus, independent of the OCaml sources."""
from collections import Counter
from pathlib import Path
import random

LIMB_BITS = 30
LAST_BOUNDARY = 113
RANDOM_SEED = 0x4C4F4F4D0201
RANDOM_PAIRS = 128
MAX_RANDOM_DIGITS = 1024
EXTENDED_LIMBS = (115, 128, 256)


def generate(smoke: Path):
    rows = [tuple(line.split("\t")) for line in smoke.read_text(encoding="utf-8").splitlines()]

    def put(name, operation, left, right="-"):
        rows.append((name, operation, str(left), str(right)))

    # Every radix transition B^k in this finite range, including each neighbour.
    for k in range(1, LAST_BOUNDARY + 1):
        boundary = 1 << (LIMB_BITS * k)
        for offset, suffix in [(-1, "below"), (0, "at"), (1, "above")]:
            value = boundary + offset
            label = f"limb.{k:03d}.{suffix}"
            put(label + ".roundtrip", "roundtrip", value)
            put(label + ".bits", "bits", value)
            put(label + ".compare", "compare", value, boundary)
            put(label + ".reverse-compare", "compare", boundary, value)
            put(label + ".plus-one", "add", value, 1)
            put(label + ".one-plus", "add", 1, value)
            put(label + ".double", "add", value, value)
            put(label + ".plus-zero", "add", value, 0)
        # Same limb count, with the decisive low digit under an equal prefix.
        put(f"limb.{k:03d}.low-compare", "compare", boundary + 7, boundary + 8)
        put(f"limb.{k:03d}.equal", "compare", boundary + 9, boundary + 9)

    for exponent in (31, 32, 61, 62, 63, 64, 127, 128):
        pivot = 1 << exponent
        for offset, suffix in [(-1, "below"), (0, "at"), (1, "above")]:
            value = pivot + offset
            label = f"machine.{exponent}.{suffix}"
            put(label + ".roundtrip", "roundtrip", value)
            put(label + ".bits", "bits", value)
            put(label + ".add", "add", value, pivot)
            put(label + ".compare", "compare", value, pivot)

    # Decimal groups and interior zero padding, not just powers of the radix.
    for digits in (1, 8, 9, 10, 18, 19, 27, 28, 100, 511, 1023):
        pivot = 10 ** digits
        for offset, suffix in [(-1, "below"), (0, "at"), (1, "above")]:
            put(f"decimal.{digits}.{suffix}.roundtrip", "roundtrip", pivot + offset)
            put(f"decimal.{digits}.{suffix}.bits", "bits", pivot + offset)
        put(f"decimal.{digits}.leading-zeroes", "roundtrip", "00000" + str(pivot + 17))

    rng = random.Random(RANDOM_SEED)
    lengths = (1, 2, 9, 10, 19, 30, 127, 256, 511, 1024)

    def number(length):
        return str(rng.randrange(1, 10)) + "".join(str(rng.randrange(10)) for _ in range(length - 1))

    for index in range(RANDOM_PAIRS):
        left = number(lengths[index % len(lengths)])
        right = number(rng.choice(lengths))
        label = f"random.{index:03d}"
        put(label + ".left-roundtrip", "roundtrip", left)
        put(label + ".right-roundtrip", "roundtrip", right)
        put(label + ".left-bits", "bits", left)
        put(label + ".right-bits", "bits", right)
        put(label + ".compare", "compare", left, right)
        put(label + ".reverse-compare", "compare", right, left)
        put(label + ".add", "add", left, right)
        put(label + ".reverse-add", "add", right, left)

    # Explicit classes supplement the smoke rows and random pairs. These are
    # finite witnesses; no OCaml source or implementation helper is imported.
    base = 1 << LIMB_BITS
    put("edge.zero.roundtrip", "roundtrip", 0)
    put("edge.zero.bits", "bits", 0)
    put("edge.zero.parse", "parse", 0)
    for index, (left, right) in enumerate(((0, 0), (0, 1), (1, 0),
                                          (0, base**3 + 7), (base**3 + 7, 0))):
        for operation in ("add", "compare"):
            put(f"edge.zero.{index}.{operation}", operation, left, right)

    for width in (3, 6, 16):
        middle = base ** (width // 2)
        high = 7 * base ** (width - 1)
        left, right = high + 2 * middle, high + 2 * middle - 1
        # Equal high prefix; decisive middle limb opposes the low limbs.
        put(f"edge.middle.{width}.forward", "compare", left, right)
        put(f"edge.middle.{width}.reverse", "compare", right, left)
        put(f"edge.middle.{width}.equal", "compare", left, left)

    for width in (2, 3, 8, 32):
        target = base**width
        left = ((target - 1) // (base - 1)) * (base // 2)
        right = target - left
        # Both operands span width limbs. Every result limb below the new
        # top is zero: after the first sum, a_i + b_i + carry equals B.
        put(f"edge.carry.{width}.equal-width", "add", left, right)
        put(f"edge.carry.{width}.equal-width-reverse", "add", right, left)
        if width > 2:
            short = base + 1
            put(f"edge.carry.{width}.uneven", "add", target - short, short)
            put(f"edge.carry.{width}.uneven-reverse", "add", short, target - short)

    for limbs in EXTENDED_LIMBS:
        value = base ** (limbs - 1) + base + 7
        put(f"edge.large.{limbs}.roundtrip", "roundtrip", value)
        put(f"edge.large.{limbs}.bits", "bits", value)
        put(f"edge.large.{limbs}.add", "add", value, 1)
        put(f"edge.large.{limbs}.compare", "compare", value, value - 1)

    for index, value in enumerate((0, 1, base**3 + 7)):
        padded = "00000" + str(value)
        for operation in ("parse", "roundtrip", "bits"):
            put(f"edge.leading.{index}.{operation}", operation, padded)
        for operation in ("add", "compare"):
            put(f"edge.leading.{index}.{operation}-left", operation, padded, value)
            put(f"edge.leading.{index}.{operation}-right", operation, value, padded)

    invalid = ("", "+", "-", "+0", "-0", " 0", "0 ", "1 2", "1_000",
               "1,000", "1.0", "0x10", "1e3", "x1", "\u0661", "\uff11",
               "\u00a01", "\U0001d7d9")
    for index, text in enumerate(invalid):
        put(f"edge.invalid.{index:02d}", "parse", text)

    # During decimal division, high limb D-1 leaves remainder D-1 before
    # combining with low limb B-1: the maximum numerator D*B-1.
    division_bound = 1_000_000_000 * base - 1
    put("edge.division.max-numerator.roundtrip", "roundtrip", division_bound)
    put("edge.division.max-numerator.bits", "bits", division_bound)
    put("edge.division.max-numerator.add-zero", "add", division_bound, 0)

    assert rows and len({row[0] for row in rows}) == len(rows)
    assert all(len(row) == 4 for row in rows)
    assert all(not any(c in field for c in "\t\r\n") for row in rows for field in row)
    assert max(len(row[2]) for row in rows if row[0].startswith("random.")) == MAX_RANDOM_DIGITS
    metadata = {"selected": len(rows), "operations": dict(Counter(row[1] for row in rows)),
                "limb_bits": LIMB_BITS, "last_boundary": LAST_BOUNDARY,
                "last_boundary_decimal_digits": len(str(1 << (LIMB_BITS * LAST_BOUNDARY))),
                "last_boundary_significant_limbs": LAST_BOUNDARY + 1,
                "random_seed": RANDOM_SEED, "random_pairs": RANDOM_PAIRS,
                "max_random_digits": MAX_RANDOM_DIGITS,
                "extended_limbs": EXTENDED_LIMBS,
                "extra_classes": dict(Counter(row[0].split(".")[1] for row in rows
                                              if row[0].startswith("edge."))),
                "finite_scope": "B^k neighbours k=1..113 plus explicit classes through 256 limbs; not every natural"}
    return rows, metadata


def write_requests(path, rows):
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write("\t".join(row) + "\n")


def compare(rows, expected_path, actual_path):
    def read(path):
        values = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            parts = line.split("\t")
            if len(parts) != 2 or not parts[0] or parts[0] in values:
                raise ValueError("invalid or duplicate result in " + str(path))
            values[parts[0]] = parts[1]
        return values

    names = [row[0] for row in rows]
    if len(set(names)) != len(names):
        raise ValueError("duplicate selected case")
    expected = read(expected_path)
    actual = read(actual_path)
    if set(expected) != set(names) or set(actual) != set(names):
        raise ValueError("selected, expected and actual names differ")
    cases = [{"name": name, "operation": row[1], "passed": actual[name] == expected[name],
              **({} if actual[name] == expected[name] else
                 {"expected": expected[name], "actual": actual[name]})}
             for name, row in zip(names, rows)]
    failed = sum(not case["passed"] for case in cases)
    result = {"selected": len(rows), "compared": len(cases),
              "passed": len(cases) - failed, "failed": failed, "cases": cases}
    if not cases:
        return 2, {**result, "error": "zero compared count"}
    return (1 if failed else 0), result
