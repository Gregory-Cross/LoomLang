# Milestone B arithmetic primitives

**SOURCE.** The owner approved implementing milestone B with the reviewed provisional prices in CHARGES.md. The owner has not adopted those prices. R20 line 1012 names the natural primitives. R20 lines 1018–1019 and 1060–1068 specify edge outcomes, including subtraction stopping at zero and builtin none for an operand of the wrong kind. FORMS.md B-F02 and B-F05 select add, sub and mul for B. The older paper's ordered value spelled `row` is now `tuple`. The current source spelling for a unary definition is `def f[x]=e`.

## Reaching an operation

**PROPOSED in FORMS.md B-F05/B-F06 and OUTCOMES.md B-O02/B-O07.** The checker resolves a binary primitive to its tag and two expressions before entry. A primitive application with the wrong number of arguments refuses with `resolve.primitive_arity`, the name, expected and actual counts, and its source location. Execution has not started, used fuel is zero and the budget is intact. A tuple or builtin none is a valid runtime operand. The caller supplies the already checked program, a natural input and a fresh meter to the piece 14 frames.

**PROPOSED in B-F06 and CHARGES.md B-C08.** Frames evaluate the left operand, then the right, once per written occurrence. They call the primitive only with two obtained immutable values, its tag, the original application site and the same meter. Any earlier stop remains at the actual unpaid child. A callee uses its fixed definition index and its own expression path. A stop on the primitive itself belongs to the application head.

## Quotation, payment and construction

**PROPOSED in CHARGES.md B-C02/B-C05/B-C06.** The meter inspects both values. For a natural, its part is its mathematical bit length, with zero assigned one. For a tuple or builtin none the part is one. Write `a` and `b` for the two natural widths and `m` for their maximum. The single provisional table in Meter gives these four unit-weight components.

| Reached case | A | R | T | W | Paid result |
| --- | --- | --- | --- | --- | --- |
| Add two naturals | a+b | m+1 | 0 | m | Exact sum |
| Subtract two naturals | a+b | a | 0 | m | Left minus right, floored at zero |
| Multiply two naturals | a+b | a+b | 0 | a*b | Exact product |
| Either operand a tuple or builtin none | part(left)+part(right) | 0 | 0 | 1 | The store's existing builtin none |

**SOURCE and reviewed proposal.** R20 lines 1025–1032 require an overflow-safe prospective bound, separate work charge and payment before building. B-C05/B-C06/B-C08 require the entire selected invoice even for a zero operand, a short result, truncation, an algebraic shortcut or an interner hit. The primitive asks `Meter.arithmetic` for its invoice and submits it once to `Meter.pay`. On success the paid callback performs the selected Natural operation and calls the value store once for its final natural, or returns the existing none for a wrong-kind edge. The builtin none result is an ordinary paid value and can become an operand of the next operation.

**PROPOSED in B-C08 and B-O02/B-O03.** When a known invoice is too large, the failing operation performs no arithmetic on its operand values, makes no result lookup or insertion, and spends zero. The stop retains the selected invoice, primitive tag (also on wrong kind), source location, and the balance after all earlier debits. Used plus remaining equals the starting budget. The meter also distinguishes an unavailable mathematical bound. Native resource exceptions follow the external tool-fault channel.

**PROPOSED implementation of B-C05.** Addition's result has at most m+1 bits, truncated subtraction's at most a bits, and multiplication's at most a+b bits. Existing Natural.add, Natural.sub and Natural.mul implement these operations on normalized project-owned limbs. The paid callback interns one final semantic natural. Its limb buffers, carries, borrows and normalization are host implementation work. The zero semantic-temporary column supplies no native scratch or capacity qualification. The positive-temporary and genuine unavailable-bound witnesses remain open.

## Entry point and verification

**PROPOSED.** Instantiate `Eval.With_primitives` with the same scoped store used by the reader. Its `run` installs the three operations at the committed frame dispatch. `Eval.Make` retains the injectable dispatch for frame clients. Piece 16 owns report serialization. The development tests submit decimal operands to the separate, project-pinned Python natural oracle and compare keyed results with the native evaluator. Native execution uses project-owned natural arithmetic throughout.
