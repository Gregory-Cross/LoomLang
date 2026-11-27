# Add cases under the paired trial descriptor

**SOURCE · outside-model conformance.** Case 21 ran first, followed by controls 01–20. A witness is evidence emitted at one reached event. A projection is the part of a run that one observer can read. The comparison checked 21 ordinary and 21 exact projections. An independent decoder validated 46 witnesses, including four private preparation events across the two runs of case 21. The project evaluator is **NOT RUN**.

All pairs are ordered (work, construction). The header binds build B0, program P0, admission A0, canonical descriptor K0, hash descriptor H0 and paired meter `pilot-pair`. A0 binds the ordered natural references and their validated widths. Fix definition `pilot`, visit 1, root scope and export b. The caller sees the selected `add.site` event under each observer specified in [ADD.md](ADD.md). Public actions and later-readable state are empty.

## 21 · Interruption after two committed Adds

**SOURCE.** Begin at (90,8) with empty prefix, zero debit and zero hold. Run the three occurrences in order. Only the third supplies a public observation. Each preparation result belongs to the private prefix.

| Occurrence | Left reference | Right reference | Schedule |
|---|---|---|---|
| prep.one | nat:1 | nat:0 | uninterrupted |
| prep.two | nat:4 | nat:2 | uninterrupted |
| add.site | nat:5 | nat:3 | fixture-interrupt after staging, immediately before commit |

| Occurrence | Ordinary result or stop | Event debit | Cumulative prior | Remaining after commit or cleanup |
|---|---|---|---|---|
| prep.one | 1 | (24,1) | (0,0) | (66,7) |
| prep.two | 6 | (33,3) | (24,1) | (33,4) |
| add.site | host(fixture-interrupt) | (0,0) | (57,4) | (33,4) |

The two internal results in the table describe the prefix. On the selected event the last debit alone is (33,3). The funded size pass measured 4 and the staged candidate is 8. At StagedBeforeCommit the live hold is (33,4), so free credit is (0,0). Cleanup discards staging, releases the full hold and preserves the ordered two-event prefix. The cumulative debit stays (57,4) and the final hold is (0,0).

- **Ordinary:** ControlledHost(fixture-interrupt) in the stop position, with empty result, actions and later-readable state.
- **Exact:** the ordinary record, event debit (0,0), remaining (33,4), and supplement (StagedBeforeCommit, outstanding (33,4), prior committed (57,4)). The last debit and free credit at interruption are useful diagnostic values in this comparison. They are outside the purchased supplement.

## 01–20 · Single-event controls

**SOURCE.** Each row starts fresh with the displayed grant, no prior debit, hold or prefix. ID 12 alone requests the same precommit interruption as 21. W denotes refusal before sizing, C refusal after exact sizing, K a successful commit and H the staged host interruption. Remaining is measured after commit or cleanup. The columns for the work invoice and size evidence describe what happened privately; the ordinary and exact projections are specified below.

**Notation for the exact projection.** Take the ordinary column, the debit and remaining columns, and exactly the branch supplement shown. On W, write `U, Sht, OK` for undetermined, short, sufficient, respectively. The four fields are work deficit, deficit image, status and expression. `e(x,y,C)` denotes the unevaluated expression max(0,bits(x+y)−C) with descriptor pilot-pair, row Add, event (pilot,add.site,1), ordered immutable references (nat:x,nat:y), and effective C substituted. Compare slot 1 and slot 2 as opaque references, preserving aliases. A bare formula or a payload-based reconstruction loses this binding. Thus equality of the image and status can coexist with different expression bindings. On C the sole supplement is construction deficit. On K there is no supplement. On H it is (phase, outstanding reservation, prior committed pair). The evaluator alone keeps the private evidence identified below.

| ID | (x,y) | Grant | Branch | Work; size evidence | Ordinary | Debit | Remaining | Exact supplement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | (5,3) | (32,3) | W | 33; widths {3,4} | work | (0,0) | (32,3) | 1, {0,1}, U, e(5,3,3) |
| 02 | (4,2) | (32,3) | W | 33; widths {3,4} | work | (0,0) | (32,3) | 1, {0,1}, U, e(4,2,3) |
| 03 | (5,3) | (33,3) | C | 33; c=4 | construction | (0,0) | (33,3) | 1 |
| 04 | (4,2) | (33,3) | K | 33; c=3 | 6 | (33,3) | (0,0) | — |
| 05 | (5,3) | (33,4) | K | 33; c=4 | 8 | (33,4) | (0,0) | — |
| 06 | (4,2) | (33,4) | K | 33; c=3 | 6 | (33,3) | (0,1) | — |
| 07 | (5,3) | (32,2) | W | 33; widths {3,4} | work | (0,0) | (32,2) | 1, {1,2}, Sht, e(5,3,2) |
| 08 | (4,2) | (32,2) | W | 33; widths {3,4} | work | (0,0) | (32,2) | 1, {1,2}, Sht, e(4,2,2) |
| 09 | (5,3) | (32,4) | W | 33; widths {3,4} | work | (0,0) | (32,4) | 1, {0}, OK, e(5,3,4) |
| 10 | (4,2) | (32,4) | W | 33; widths {3,4} | work | (0,0) | (32,4) | 1, {0}, OK, e(4,2,4) |
| 11 | (3,3) | (28,2) | W | 29; widths {3} | work | (0,0) | (28,2) | 1, {1}, Sht, e(3,3,2) |
| 12 | (5,3) | (33,4) | H | 33; c=4 | host(fixture-interrupt) | (0,0) | (33,4) | precommit staged, (33,4), (0,0) |
| 13 | (5,3) | (34,3) | C | 33; c=4 | construction | (0,0) | (34,3) | 1 |
| 14 | (4,2) | (34,3) | K | 33; c=3 | 6 | (33,3) | (1,0) | — |
| 15 | (1,0) | (23,1) | W | 24; widths {1,2} | work | (0,0) | (23,1) | 1, {0,1}, U, e(1,0,1) |
| 16 | (1,1) | (23,1) | W | 24; widths {1,2} | work | (0,0) | (23,1) | 1, {0,1}, U, e(1,1,1) |
| 17 | (1,0) | (24,1) | K | 24; c=1 | 1 | (24,1) | (0,0) | — |
| 18 | (1,1) | (24,1) | C | 24; c=2 | construction | (0,0) | (24,1) | 1 |
| 19 | (5,3) | (30,1) | W | 33; widths {3,4} | work | (0,0) | (30,1) | 3, {2,3}, Sht, e(5,3,1) |
| 20 | (5,3) | (33,1) | C | 33; c=4 | construction | (0,0) | (33,1) | 3 |

**SOURCE · distinguishing cases.** In 01 and 02 the ordinary stop and the deficit set agree, but the expressions bind different operands. In 11 the size pass is unreached even though the width evidence determines a singleton deficit. In 19 and 20 changing work from 30 to 33 changes which axis refuses; both deficits are 3 on the primary axis. In 21 reordering the private prefix preserves its total while changing the run.

**SOURCE · negative controls.** The independent decoder rejected all 18 invalid private variants across the two observers. They exercised receipt substitution, wrong schedule or phase, loss of the recoverable singleton, swapped operands, dropped or reordered prefix entries and constant-one deficits. A checked indirect reference could recover the genuine singleton. Withholding the selected 21 witness left its two internal receipts intact and produced missing coverage under each observer. [Evidence scope](COVERAGE-GAPS.md)
