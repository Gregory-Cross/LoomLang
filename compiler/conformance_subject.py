"""Stage a single named test mutation outside the repository for the committed driver builder."""
import importlib.util

import driver_build
import eval_build


ARGUMENT_ORDER = [
    ("visit_child activation at 0 left (Primitive_left (activation, at, op, right) :: stack)",
     "visit_child activation at 1 right (Primitive_left (activation, at, op, left) :: stack)"),
    ("visit_child activation at 1 right (Primitive_right (at, op, value) :: rest)",
     "visit_child activation at 0 right (Primitive_right (at, op, value) :: rest)"),
    ("primitive ~meter ~at op ~left ~right:value", "primitive ~meter ~at op ~left:value ~right:left"),
]
MUTATIONS = {
    "wrong-sum": ("src/primitives.ml", eval_build.PRIMITIVE_MUTATIONS["wrong-sum"]),
    "wrong-product": ("src/primitives.ml", eval_build.PRIMITIVE_MUTATIONS["wrong-product"]),
    "wrong-debit": ("src/primitives.ml", eval_build.PRIMITIVE_MUTATIONS["free-edge"]),
    "tuple-order": ("src/eval.ml", eval_build.MUTATIONS["order"]),
    "argument-order": ("src/eval.ml", ARGUMENT_ORDER),
    "wrong-call-debit": ("src/eval.ml", eval_build.MUTATIONS["call"]),
    "wrong-read-debit": ("src/eval.ml", eval_build.MUTATIONS["read"]),
}


def subject(directory, control, create=False):
    """Validate every staged input before loading its byte-identical build command."""
    if control not in MUTATIONS:
        return driver_build
    target = directory.with_name(directory.name + "-sources")
    if create:
        target.mkdir(exist_ok=False)
    changed, edits = MUTATIONS[control]
    names = (*driver_build.INPUTS, "natural_corpus.py")
    for name in names:
        data = (driver_build.PROJECT / name).read_bytes()
        if name == changed:
            for old, new in edits:
                if data.count(old.encode()) != 1:
                    raise ValueError("test mutation site changed in " + name)
                data = data.replace(old.encode(), new.encode())
        dest = target / name
        if create:
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open("xb") as stream:
                stream.write(data)
        if dest.read_bytes() != data:
            raise ValueError("test subject changed in " + name)
    spec = importlib.util.spec_from_file_location("conformance_driver_build", target / "driver_build.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
