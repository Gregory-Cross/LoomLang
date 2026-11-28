# Shift and bitwise operations under a paired grant

A *start* fixes the operands, grant and schedule. An *offer* presents a start for one observer with fresh balances. A *witness* records the private phases of a reached operation. An *observer* selects which facts a caller sees. A *header* supplies validated kind and binary width. An operand's *payload* supplies its digits. A *hold* reserves credit privately. A *commit* publishes the result, debit and mandatory record together. Pairs below give work first and construction second.

**PROPOSED trial.** At export `b` a serial root supplies both balances (W, C). Each admitted start selects one operation in definition `trial` at visit 1. The two operand slots are already obtained. The earlier debit is (0, 0), with empty prefixes, holdings, hold and memo cache. The ordinary observer sees the return or primary stop axis, with empty actions and later-readable state. Trial-exact adds the selected event debit and the available pair after commit or cleanup. The quote, exact deficit, ordered reads and temporary hold stay private. The owner selected S-1, B-1 and K-1 as the price direction. The reference rules, funding and observer conventions retain their proposed standing. [Shift](SHIFT.md) · [Bitwise](BITWISE.md)

## Two left shifts with the same quote

**SOURCE.** B9-01 and B9-02 ran first, each under ordinary and then trial-exact observation. They offer zero and one, respectively, as the left operand. Both amounts equal 18446744073709551616 (2⁶⁴). The width headers are (1, 65) and the grant is (1180591620717411303424, 5). In both quotes the result bound is R = 36893488147419103232, the scratch reservation is T = 268 and the scheduled work is γ = 36893488147419103298. Including the two argument widths gives w = **73786976294838206864**.

- **Zero.** Under the work hold, B9-01 measures c = 1. It stages a single zero digit and commits natural 0. Trial-exact sees debit (73786976294838206864, 1) and available (1106804644422573096560, 4).
- **One.** B9-02 measures c = **18446744073709551617**, one digit beyond the shift amount. The construction deficit is **18446744073709551612**. ConstructionCheck releases (73786976294838206864, 0) before any result staging. Both observers see a construction stop. Trial-exact also sees debit (0, 0) and available (1180591620717411303424, 5).

**SOURCE / INFERENCE · a certified work cut.** B9-03 and B9-04 repeat those operands with grant (1000000, 5). The quote certifies w > 2^(65−1) > 1000000. It retains the work deficit symbolically as w_SHL(H)−W for the two ordered headers H. The width set S is {1} ∪ [18446744073709551617, 36893488147419103232]. Its construction-deficit image D at C = 5 is {0} ∪ [18446744073709551612, 36893488147419103227]. These decimal endpoints expand the symbolic record for the reader. The minimum deficit is 0 and construction sufficiency is undetermined. The event binds the unevaluated construction deficit to the operation, reached WorkCheck, both ordered references, descriptor and C. Neither start measures c. Both publicly stop for work, with debit (0, 0) and available (1000000, 5) under trial-exact. The funded pair above shows why the two headers cannot determine the actual construction shortfall.

## Right shift at and beyond the input width

**SOURCE.** B9-19 shifts 5 right by 3, its width. The funded pass reads 2 amount digits before establishing c = 1 and staging a zero without a further operand read. B9-20 shifts 5 right by 4. Here the amount width exceeds the binary width of the left operand's width. The headers certify an overshift, the recorded amount stays absent and sizing uses 0 operand digits. Both ordinary views return zero. Trial-exact distinguishes debit (25, 1), available (999975, 0) from debit (24, 1), available (999976, 0). B9-23 is a funded copy control. Shifting 40 right by 3 copies 3 left-operand digits and returns 5. Read observations here concern the outside model. [Backing-read control](BACKING-READ-CONTROL.md)

## Three operations on the same two naturals

**SOURCE.** B10-01, B10-02 and B10-03 opened the bitwise schedule in that order, each under both observers. On (6, 3) with grant (1000000, 2), AND requests (31, 2), returns 2 and leaves (999969, 0). OR and XOR each request (32, 3). Each measures width 3 under its work hold, stops for construction with deficit (0, 1), releases the hold and leaves (1000000, 2). A size pass still ran where the two widths fixed the result width.

**SOURCE / INFERENCE.** B10-16 offers OR on the same operands with (0, 2). Its width set is {3} and its construction-deficit image is {1}. Work is short by 32, so both observers see a work stop at this joint shortfall. This differs publicly from B10-02 even though the construction shortage is identical.

**SOURCE.** B10-12 and B10-13 both XOR seven with seven. In the former, distinct handles refer to the same interned value. In the latter, both slots name the same handle. The funded size pass reads 3 digits from each ordered slot, and staging reads 1 from each. Their ordinary return is 0 and their exact additions agree at debit (37, 1), available (999963, 0). Their private handle bindings distinguish them.

## An admitted wrong kind and a missing handle

**SOURCE.** B9-26 (SHL) and B10-21 (AND) have an admitted empty tuple and natural 5. The K-1 request is (5, 0) and the grant covers it exactly. Commit publishes the admitted none and debit (5, 0). ReleaseTemporaries subsequently releases the quote fields with additional debit (0, 0), leaving (0, 0). K-1 skips natural sizing and staging. B9-27 (SHR) and B10-22 (XOR) instead offer natural 5 and admitted none at (4, 0). WorkCheck stops with deficits (1, 0) and debit (0, 0).

**SOURCE.** B9-28 (SHL) and B10-23 (OR) each offer (5, 0) and two handles. A0 binds `h1` to natural 5 and lacks `h2`. Under each observer the model issues a pre-entry admission report identifying `h2`. The grant belongs to the offer. There is no event, allowance cut, event debit, settled balance or purchased event projection.

## Finite scope

**SOURCE.** Counts cover the exact outside-model schedule. Each reached event has a public projection. Each pre-entry report is counted separately.

| Family | Starts | Offers | Pre-entry reports | Reached events | Returns | Work cuts | Construction cuts | Private phase records | Operand-digit reads |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Shift | 28 | 56 | 2 | 54 | 22 | 22 | 10 | 278 | 372 |
| Bitwise | 23 | 46 | 2 | 44 | 18 | 14 | 12 | 244 | 130 |
| Together | 51 | 102 | 4 | 98 | 40 | 36 | 22 | 522 | 502 |

**SOURCE.** Each observer accounts for 51 offers, 49 reached events and 2 pre-entry reports. Of the private phase records, ordinary has 261 and trial-exact has 261. G independently compared the R7 starts, private records and public outcomes. Q decoded the reached-event witnesses and admission reports and reconciled the funded-phase digit reads with an instrumented backing store. Across 98 quotes and 36 work-refused events, the access counts were 0 and 0 operand digits respectively. The observation begins after admission. A future evaluator build claiming the same discipline needs the access control on its own bound representation, configuration and starts. [Backing-read control](BACKING-READ-CONTROL.md)

**SOURCE · edition.** The examples use Spec3's R7 shift and bitwise starts and F's R1 outside-model capture. The capture binds producer SHA-256 `e0c4efe153c8cc45bc7e4c97085792e0525fdd7ad66d5e53e06d740116216674`. The capture itself has SHA-256 `57bd1af103259f3590ae080c40f1946281854ca335d102a6371d4f7402e5c742`. G's row 07 trace comparison and Q's row 08 witness check cover these identities.

**NOT RUN in this trial.** Project evaluator execution, controlled host interruption and physical-resource qualification. [Coverage and gaps](COVERAGE-GAPS.md)
