# Milestone B fuel meter

**SOURCE** — The owner approved piece 13 in the overnight plan, item 3, using Codex D's independently reviewed charge table. **The prices are provisional and have not been adopted by the owner.** CHARGES.md lines 3, 7 and 58 distinguish the design constraints from the proposed tariff. R20 D-EV-1, lines 1025–1032, requires safe prospective bounds, separate work accounting and payment before building.

## Measuring and pricing one event

**PROPOSED in CHARGES.md** — Lines 13–14 define `ell(0) = 1` and `ell(n) = bit_length(n)` for positive naturals. An obtained natural's part is `ell(n)`. A tuple or builtin none contributes one part. A tuple used as an operand contributes one regardless of nesting, width or sharing. The charge sheet uses the former spelling `row` for the fixed-position value now called `tuple`.

**PROPOSED in CHARGES.md** — Line 22 defines an invoice with four exact natural components. They are argument parts `A`, prospective result reservation `R`, temporary semantic parts `T` and work `W`. The full charge is `A + R + T + W` with unit weights. For natural operands let `a = ell(x)`, `b = ell(y)` and `m = max(a,b)`. For a tuple let `k` be its field count and `s` the sum of their parts, including repeated occurrences.

| CHARGES.md line | Reached event | A | R | T | W | Payment boundary |
| ---: | --- | --- | --- | --- | --- | --- |
| 33 | External entry | 0 | 0 | 0 | 1 | Before input binding and the entry body |
| 34 | Program natural literal | 0 | 0 | 0 | 1 | Before yielding the admitted value |
| 35 | Local variable read | 0 | 0 | 0 | 1 | Before yielding the bound value |
| 36 | Ordinary unary call | 0 | 0 | 0 | 1 | After obtaining its argument, before binding and the body |
| 37 | Return of an obtained result | 0 | 0 | 0 | 0 | Covered return, with no extra debit |
| 51 | Natural add | a+b | m+1 | 0 | m | Before result construction or lookup |
| 52 | Natural truncated subtraction | a+b | a | 0 | m | Before result construction or lookup |
| 53 | Natural multiplication | a+b | a+b | 0 | a*b | Before result construction or lookup |
| 64 | Add, sub or mul with either operand a tuple or builtin none | part(x)+part(y) | 0 | 0 | 1 | Before returning the existing builtin none |
| 72 | Tuple of obtained fields | s | k+1 | 0 | 0 | Before canonical lookup or construction, including the empty tuple |

**PROPOSED in CHARGES.md** — Lines 23, 39 and 80 put operand evaluation in left-to-right order before pricing the enclosing event. Reading, resolution, checking, literal/input interning and reporting are outside execution fuel. Entry incurs its own charge once. The structural charges cover parameter binding, return, frame administration and dispatch. Arithmetic and tuple construction each incur their own table row.

**PROPOSED in CHARGES.md** — Lines 55–56 give the natural result bounds. Addition needs at most `m+1` bits, subtraction at most `a` bits, and multiplication at most `a+b` bits under the stated size measure. Lines 55, 64, 72 and 117–121 retain the full selected charge for zero operands, subtraction below zero, a short result, sharing and canonical reuse. A wrong-kind arithmetic operation uses the one wrong-kind invoice. The selected rows have zero billable semantic temporaries. A future construction needing a billable temporary requires a reviewed reservation and revised tests before it can use that construction. Native memory and scratch requirements remain separate.

## Payment and failure

**SOURCE and reviewed proposal** — R20 D-EV-1 lines 1027–1032 and CHARGES.md lines 80–81 require the full bill before the fuel check. If the balance covers it, debit once and then permit work. If the balance is short, the operation spends zero and performs no construction or lookup. All earlier debits stand. At every boundary `used + remaining = budget`. Lines 98–108 distinguish a single invoice on obtained operands from a whole run containing earlier paid events.

**SOURCE of report causes** — OUTCOMES.md lines 24–25 and 52–60 give `fuel.insufficient` for a known unpaid invoice and `fuel.bound_unavailable` for a genuinely unavailable safe bound. The first supplies the invoice and remaining fuel. The second supplies a concrete reason and an absent invoice. Both retain the failed event, its location, prior accounting and a failed-operation debit of zero. A wrong-kind event retains its primitive. The caller records that execution started when entry was attempted, including a failed entry payment.

**PROPOSED in CHARGES.md** — Lines 13, 22, 80 and 89–90 require exact natural arithmetic. A budget, component, work product, total or accumulated debit may exceed host integer width. Use piece 2–3 Natural operations through the comparison and balance update. The B rows have finite mathematical bounds. Host allocation, stack or I/O failures belong to the OUTCOMES.md B-O06 tool channel. EV-018's positive-temporary witness and EV-021's concrete unavailable-bound witness remain open under lines 89–90 and 119–122.

## Interface for frames, primitives and reports

**PROPOSED** — A run owns a meter with immutable accounting snapshots. Piece 14 quotes structural events and tuples. Piece 15 quotes arithmetic from the two obtained piece 11 values. The meter classifies wrong-kind operands before choosing a row. The single production table `provisional_prices` selects all four components. The size-level natural arithmetic quote accepts positive, exact operand bit lengths and uses the same row as the value-level quote.

**PROPOSED** — Pieces 14 and 15 pass a quote and a source location to `pay` with a construction callback. The meter commits the new accounting before invoking the callback once. A free return invokes its continuation with the current balance. A stop is terminal for that meter and later requests return the first stop. A callback exception leaves the committed debit in place and propagates to the invoking tool. The meter neither traverses a checked program nor executes arithmetic on its behalf.

**PROPOSED** — Piece 16 reads the budget, used fuel and remaining fuel, and the known invoice or unavailable-bound reason from the stop. It supplies report formatting and uses the caller's location. A producer reporting genuine bound unavailability supplies the event and reason before construction. All current B quotation functions yield known invoices.
