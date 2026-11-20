# Milestone B evaluation frames and unary calls

**SOURCE.** Piece 14 takes a program admitted by the milestone B checker, its selected entry index, one supplied natural input and a fresh piece 13 fuel meter. The owner approved building against the reviewed provisional charge table. The prices have not been adopted by the owner. The earlier paper spelling `row` means the ordered evaluator value now called `tuple`. The provisional definition spelling is `def f[x]=e`.

**SOURCE.** R20 lines 609 and 611 give left-to-right arguments and a value bound in the current activation. Lines 1006–1008 give the first-order forms. Lines 1021–1026 cover fueled calls, self-calls, exhaustion and the call charge. R20 lines 894 and 1000 record the sketch decision and require linked immutable tuples for first-build frames and state. Claude Arch reviewed the original sketches and cost account. Codex B reviewed both revised sketches and their R2 cost account.

## Admitted program and machine state

**PROPOSED in FORMS.md B-F03–B-F07.** The reader and checker finish before execution. B-F03 and B-F04 give the grammar and words. B-F05 and B-F06 fix the definition indices and unary local slot, admit forward, self and mutual calls, and require evaluation once per written occurrence in source order. B-F07 assigns unsupported forms to admission. Execution receives literals, a local read, an ordered tuple, a tagged binary primitive or a unary call to a fixed index. The machine uses the checker's definition table and retains its source positions.

**PROPOSED implementation of R20 line 1000.** The current activation is an immutable pair of definition index and bound argument. Pending work is a linked list of immutable tagged tuples. A frame carries precisely the waiting call, tuple field, primitive operand or function return. The machine alternates between visiting a checked expression and delivering an obtained value to the next frame. It advances in tail position, including across definition calls and returns. On exhaustion the stack drops out of scope. The stop carries the failed location and accounting. The value store outlives a run at the caller's discretion.

**PROPOSED location under OUTCOMES.md B-O02/B-O03.** External entry uses its selected definition index with absent expression path and source offset. A body root has the empty path. A child appends its zero-based written position to its parent's path. A callee body starts a fresh root in its own definition. A call payment belongs to the caller's call expression. Literal, read, tuple and primitive sites use their expression's starting byte offset from the reader. Internally, child indices may be prepended to a shared reversed path. The accessor restores root-to-child order for reporting.

## Events and construction

**PROPOSED in CHARGES.md B-C03, B-C04, B-C07 and B-C08.** Input/literal preparation, reading and checking are outside execution fuel. Entry and each reached literal, read and named call use their piece 13 structural invoice. The meter computes and commits the full charge once before permitting the event. A known shortfall reports `fuel.insufficient`, its invoice, the prior balance and zero failed-operation debit. Previously paid work stands. OUTCOMES.md B-O02/B-O03 makes exhaustion inconclusive and distinguishes a genuine unavailable bound and host tool faults. This interface passes through the meter's stop.

| Reached event | Action after payment |
| --- | --- |
| External entry | Bind the already prepared input to slot zero in the selected definition and visit its body. Pay entry once. |
| Natural literal | Deliver the admitted piece 11 value. |
| Local slot zero | Deliver the argument of this activation. Each written read pays again. |
| Named unary call | First obtain the argument in the caller. Pay at the call site, bind the argument in the fixed callee and visit its body. |
| Ordered tuple | Obtain every field once, left to right, including equal or repeated fields. Quote the obtained fields to the meter. After payment restore their written order and call the piece 11 constructor once, including for an empty or previously interned tuple. |
| Function return | Return the obtained body value to the waiting frame. The piece 13 return invoice has zero cost. The entry body's return completes the run. |

**PROPOSED.** A tuple frame remembers the caller's activation and tuple location, the remaining fields, the next written position and the already obtained values in reverse order. Completed callees release their own binder. Pending siblings run with their original caller's binder. The array passed to the value store is created inside the paid callback. The first unpaid child prevents visits to later siblings and prevents the enclosing construction.

**PROPOSED boundary for piece 15.** A primitive visits its left operand at child zero, then its right operand at child one. The dispatch function receives the resolved add/sub/mul tag, those two obtained values, the primitive's location and the same meter. Piece 15 owns primitive classification, quoting, payment and value construction through piece 13. The frame resumes only with a legitimately obtained value. Piece 14 supplies the internal dispatch interface. Its structural runner defines no substitute arithmetic result, refusal or exhaustion code for pending integration. Piece 16 owns report formatting.
