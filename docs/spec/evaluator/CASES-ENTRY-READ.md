# Top entry, literal read and local read under a paired grant

**SOURCE · finite outside-model conformance.** A start fixes the program, the input handle offered for admission and the admission state's entry for it, the export and its limits (W,C), the prior state, the schedule and the observer. A witness is the ordered sequence of private phase records emitted for a reached event. The ordinary observer sees the returned value or the visible primary stop, with empty actions and later-readable state. The linked trial-exact observer also sees the debit of the selected event at `top.body`, visit 1, and the available pair. Entry debit, phases, requested pairs, deficits, first unpaid site, source bindings and holds are private in this batch. See the [top entry](ENTRY.md), [literal read](LITERAL.md) and [local read](LOCAL.md) rules.

**SOURCE · starts.** Each row starts afresh at export `b` with build B0, admission state A0, canonical descriptor K0, hash descriptor H0 and meter `b2-pair`. Export `b` requires the caller to supply both W and C and publishes no default for either. The serial root scope supplies both balances. Prior debit is (0,0); the committed prefix, request/trail prefix, holdings, hold and memo cache are empty, and no host interruption is scheduled. Each program has a single unmarked unary definition `top`, whose body is a single node at `top.body`. A0 places each program literal in the starting pool and binds the local occurrence to its resolved parameter. For the input handle `i1` it holds either an entry giving the value, its validated kind and width, or no entry. Handles are local to their start, and the case ID is an external selection label. T01–T04 ran first, each under ordinary and then trial-exact observation on fresh starts, and the remaining rows followed. The display column uses the abstract syntax of DESIGN §15.1 for orientation only.

| Program | Node at `top.body` | Display |
|---|---|---|
| P1 | a local read whose resolved target is the parameter of `top` (position 1) | `top(x) = x` |
| P2 | a literal holding `nat:5` | `top(x) = 5` |
| P3 | a literal holding `nat:0` | `top(x) = 0` |
| P4 | a literal holding `nat:18446744073709551616` | `top(x) = 18446744073709551616` |

## Starts and results

**SOURCE.** Every event requests (1,0). The reached events are listed in order with their terminal phases: Commit is a paid event and WorkCheck a refusal at work preflight. The body source is the parameter in P1 and the literal's pooled node in the other programs. *Shared* means that the literal and the input have equal content and share a pooled node; *own* means that the literal's node is distinct. Committed is the run account's cumulative debit and remaining the settled pair after the run. The last column gives the trial-exact additions, the selected body debit and then the available pair. **PROPOSED trial convention.** In an admitted execution where the selected body is refused or never reached, its debit in the trial-exact projection is (0,0). A pre-entry refusal has no event projection.

| ID | Program | A0 entry for `i1` | W,C | Reached events | Body source | Committed | Remaining | Ordinary | Trial-exact additions |
|---|---|---|---|---|---|---|---|---|---|
| T01 | P1 | `nat:5`, natural, width 3 | (1,0) | entry Commit · local WorkCheck | parameter | (1,0) | (0,0) | work stop | (0,0) · (0,0) |
| T02 | P2 | `nat:5`, natural, width 3 | (1,0) | entry Commit · literal WorkCheck | literal, shared | (1,0) | (0,0) | work stop | (0,0) · (0,0) |
| T03 | P1 | `nat:5`, natural, width 3 | (2,0) | entry Commit · local Commit | parameter | (2,0) | (0,0) | return 5 | (1,0) · (0,0) |
| T04 | P2 | `nat:5`, natural, width 3 | (2,0) | entry Commit · literal Commit | literal, shared | (2,0) | (0,0) | return 5 | (1,0) · (0,0) |
| T05 | P1 | `nat:5`, natural, width 3 | (0,0) | entry WorkCheck | parameter | (0,0) | (0,0) | work stop | (0,0) · (0,0) |
| T06 | P2 | `nat:5`, natural, width 3 | (0,0) | entry WorkCheck | literal, shared | (0,0) | (0,0) | work stop | (0,0) · (0,0) |
| T07 | P1 | `nat:5`, natural, width 3 | (3,0) | entry Commit · local Commit | parameter | (2,0) | (1,0) | return 5 | (1,0) · (1,0) |
| T08 | P2 | `nat:5`, natural, width 3 | (3,0) | entry Commit · literal Commit | literal, shared | (2,0) | (1,0) | return 5 | (1,0) · (1,0) |
| T09 | P1 | `nat:5`, natural, width 3 | (1,4) | entry Commit · local WorkCheck | parameter | (1,0) | (0,4) | work stop | (0,0) · (0,4) |
| T10 | P2 | `nat:5`, natural, width 3 | (0,4) | entry WorkCheck | literal, shared | (0,0) | (0,4) | work stop | (0,0) · (0,4) |
| T11 | P2 | `nat:0`, natural, width 1 | (2,0) | entry Commit · literal Commit | literal, own | (2,0) | (0,0) | return 5 | (1,0) · (0,0) |
| T12 | P1 | `nat:0`, natural, width 1 | (2,0) | entry Commit · local Commit | parameter | (2,0) | (0,0) | return 0 | (1,0) · (0,0) |
| T13 | P3 | `nat:5`, natural, width 3 | (2,0) | entry Commit · literal Commit | literal, own | (2,0) | (0,0) | return 0 | (1,0) · (0,0) |
| T14 | P3 | `nat:5`, natural, width 3 | (1,0) | entry Commit · literal WorkCheck | literal, own | (1,0) | (0,0) | work stop | (0,0) · (0,0) |
| T15 | P1 | `nat:18446744073709551616`, natural, width 65 | (2,0) | entry Commit · local Commit | parameter | (2,0) | (0,0) | return 18446744073709551616 | (1,0) · (0,0) |
| T16 | P4 | `nat:5`, natural, width 3 | (2,0) | entry Commit · literal Commit | literal, own | (2,0) | (0,0) | return 18446744073709551616 | (1,0) · (0,0) |
| T17 | P1 | no entry | (2,0) | none; admission refusal before entry | — | — | — | none | none |
| T18 | P1 | `nat:5`, natural, width 3 | (not supplied, 0) | none; configuration refusal before entry | — | — | — | none | none |

## Pre-entry reports

**SOURCE.** T17 offers P1 at (2,0) with the handle `i1`, for which A0 holds no entry. T18 offers P1 with A0's entry `nat:5` and C = 0, and supplies no W. Under each observer the model reported a pre-run admission refusal for T17 and a pre-run configuration refusal for T18. In the independent diagnostic, all four offers stopped before admission installation or run construction. None produced a top entry, witness, allowance cut, debit, return or event projection. T18 · T05 separates an absent required limit from W = 0, a valid grant that reaches the entry and is cut there.

**INFERENCE.** Each of the two starts has one fault, so either order of the configuration and admission checks gives the same reports. Neither DESIGN nor these rules fix that order, and it stays open on the [coverage list](COVERAGE-GAPS.md). A start with both faults is **NOT RUN**.

## Comparisons

**SOURCE / INFERENCE.** Each pair differs on the named axes of its starts and on no other of program, A0 entry, W and C. The private difference is derived from the rules, and the independent trace comparison matched it. The view columns agree with the views recomputed from the capture. The last column compares only the trial-exact additions. The full trial-exact view also carries the ordinary value, so for T12 · T03, T13 · T04, T15 · T03 and T16 · T04 the additions agree while the full views differ.

| Pair | Axes that differ | Private difference | Ordinary | Trial-exact additions |
|---|---|---|---|---|
| T01 · T02 | program | kind and source of the refused read at top.body/1 | equal | equal |
| T03 · T04 | program | kind and source of the paid read; both selections resolve to natural 5 | equal | equal |
| T05 · T06 | program | program identity only; the body is unreached | equal | equal |
| T07 · T08 | program | kind and source of the paid read; both selections resolve to natural 5 | equal | equal |
| T01 · T03 | W | cut at top.body/1 against a return; committed (1,0) against (2,0) | differ | differ |
| T05 · T01 | W | cut at top.entry/1 with nothing committed against a cut at top.body/1 after the entry's commit | equal | equal |
| T03 · T07 | W | remaining (0,0) against (1,0) | equal | differ |
| T09 · T01 | C | remaining construction 4 against 0; the same cut site | equal | differ |
| T10 · T06 | C | remaining construction 4 against 0; the same cut site | equal | differ |
| T11 · T04 | A0 entry | the literal's node is not, against is, node(`i1`) | equal | equal |
| T12 · T03 | A0 entry | the selected node holds nat:0 against nat:5 | differ | equal |
| T13 · T04 | program | literal nat:0 against nat:5 | differ | equal |
| T14 · T13 | W | cut at top.body/1 against a return | differ | differ |
| T15 · T03 | A0 entry | the selected node has width 65 against 3; the same prices | differ | equal |
| T16 · T04 | program | the literal has width 65 against 3; the same prices | differ | equal |
| T02 · T14 | program | the refused literal holds nat:5 against nat:0 | equal | equal |
| T17 · T03 | A0 entry | pre-run admission refusal against a run | differ | differ |
| T18 · T03 | W | pre-run configuration refusal against a run | differ | differ |
| T18 · T05 | W | an absent W is refused before entry; an explicit W = 0 reaches the entry and is cut there | differ | differ |

## Where a read's value comes from

**INFERENCE · first separating case.** T03 · T04 is the batch’s designated paid separating case. After the paid entry, a local read and a literal read return the same natural with equal public views under both observers. Only their private records separate them: the read's kind, its source binding and its selected reference. T01 · T02 distinguishes the private sources earlier, when the first unpaid read is refused.

**SOURCE.** A literal read and a local read can return the same pooled natural with different source evidence. In T04 the input and the literal have equal content and share the node `pool:1`. The literal read's witness binds the literal occurrence and selects `pool:1`. In T03 the local read's witness binds the resolved parameter, recovers the input reference `input:i1` from the entry committed at ordinal 1 and selects it; that reference resolves to `pool:1`. The independent decoder rejected a T04 record whose literal selected the equal input alias and a T03 record whose local selected the equal pooled node. In T11 the input `nat:0` and the literal `nat:5` have distinct nodes. T12 and T13 return zero through the local and literal paths, and T15 and T16 return the 65-bit natural 2⁶⁴ through them. Node and reference names are the outside model's and are local to their start.

## Event coverage

**SOURCE.** The model processed 18 starts under both observers, giving 36 offers. Of these, 32 entered execution and four produced pre-entry reports. The capture holds 58 reached-event witnesses with 248 private phase records, 32 public projections and four pre-entry reports, which are counted separately. Per observer the witnesses comprise 13 top-entry commits and three top-entry work refusals, five literal-read commits and two literal-read work refusals, and four local-read commits and two local-read work refusals. The selected body was reached in 13 runs per observer, with nine commits and four work refusals. In three runs per observer the entry was refused and the body was unreached.

**SOURCE · independent checks.** The trace comparison independently derived the private records and both observer views for each admitted start and matched them to the capture, including the source bindings where the public views coincide. For T17 and T18 it matched the pre-entry reports and the absence of event projections under both observers. Its five in-memory controls rejected changed presence, source identity, refusal class or emission bytes while the public view stayed unchanged. The witness decoder accepted every genuine record and rejected 12 altered samples, each once. With the T03 trial-exact witness at `top.body`, visit 1, withheld and its projection retained, it reported one missing witness. With all 58 reached-event witnesses withheld, it reported 58 missing and still validated the four pre-entry reports.

**SOURCE · what the prefix records.** No phase record carries a semantic request, a trail item or a holding, including at a paid return. Each successful event's commit record carries its debit with its published binding or selected reference.

**SOURCE · access.** The independent access diagnostic found no payload lookup on the 14 work cuts across both observers. Each of the 18 funded returns made one payload lookup, at the model's export boundary after the body commit. A trap on the backing store caught that lookup for a funded local return (T03) and a funded literal return (T11). Validation and interning of the input and literals happen before execution, outside the grant and outside the probe. This supports the access claim for this outside model and capture.

**NOT RUN.** Project evaluator execution, physical-resource qualification, controlled host interruption and a start with both a configuration fault and an admission fault. [Coverage and gaps](COVERAGE-GAPS.md)

**SOURCE · standing and edition.** P-Top remains PROPOSED, since DESIGN writes no top-entry judgment. The (1,0) prices of `b2-pair` remain candidate prices, which D1962 sets under the leading proposed tag of D1970. P-Val and P-Var are displays with no tag of their own (D1852); INFERENCE: they stand no stronger than proposed. The observer purchases, A0's input-handle entries and export `b`'s requirement of both limits are PROPOSED trial conventions. This page records evidence for those trial rules and adopts nothing new. The rules govern under DESIGN SHA-256 `6439d9cfb70cfb02457ba06a90cfea999b7535bf9ae063cd131bd18c2fa8870a`. The model's producer has SHA-256 `c540325c3eb608fad37faed4dd5f960d7dc5c2efd989cd0bdaf7b9978b8f33f3` and its capture SHA-256 `be2f364ecf6539ee0c7ef4610229dde19a6998ae239cb811a7afe86f28c3d8d8`. The rule pages it consumed are byte-identical to the three linked above.
