# Obtained natural subtraction under a paired grant

**PROPOSED · paper rule.** At one reached subtraction on two already obtained naturals, work buys the read-only measurement of the result width. A work refusal uses only the two admitted widths. A funded return constructs one natural, including when its value is zero.

A *start* fixes the state and grants before the selected event. A *descriptor* names the chosen price and observation rules. A *hold* removes credit temporarily from the available balance. A *commit* publishes the result and records both debits in one transition. A *projection* selects the parts of a record visible to one caller. A *witness* is evidence tied to the reached event. Here ℕ includes zero. In source locators D means the bound DESIGN.md and F means FORMAL-R7.1.md. [IMPORTS.md](IMPORTS.md) identifies the editions and the two FORMAL uses.

## Domain and price

**SOURCE.** D1958, D1967 and D1970 give a **proposed** paired tariff. D1935–46 counts one logical cell per natural digit, including a digit for zero. D1952 orders work, exact measurement and joint commit; D1956 marks atomic publication of the funded event decided. Read the individual standing tags under D13.

**PROPOSED.** Fix descriptor `sub-pair` to this candidate row, exact quote arithmetic and the single serial scope of the case table below. Let x,y ∈ ℕ be the ordered operands. Write β(0)=1 and β(n)=⌊log₂ n⌋+1 for n>0 (an integer digit count). Start with validated widths a=β(x), b=β(y), m=max(a,b), p=β(2(a+b+2)). For effective balances (W,C), the row specifies

    z = max(x−y,0)
    R = a,  T = 4p
    w = a+b+R+T+2(m+1)
    c = β(z).

The equations name the result and price. Their order on the page does not authorize reading operand digits to form z or c before work is funded. R and T are work allowances for result and temporary reservations. The two scans cover size and emission. The size pass may count from the ordered digits with the prescribed bounded work area; it forms no result node. The price includes that pass even when values are equal, the result is already interned or the host has a shortcut. Inputs, entry, operand reads and surrounding expressions have already been dealt with at this start. The quoted work belongs to this occurrence only.

## First unpaid event or return

**SOURCE / PROPOSED trial transcription.** Apply D1925–27 and D1952–56, D1972 in this order.

1. **W<w.** Quote w using admitted size metadata. Run the mandatory width check below. Work is the primary stop, with exact deficit w−W under this descriptor. Preserve (W,C) before the attempt, the row and ordered operand identities, the width check and its result, the construction deficit information and the unreached size phase. The request for construction remains β(max(x−y,0)) as a bound term unless established numerically by the width evidence. Never scan or compare the operand payloads in this branch, even if the reader can see them in the case table. The debit is (0,0). The event makes no commit and leaves no result, outstanding hold or change to the prefix.
2. **W≥w.** Hold (w,0) and perform the exact read-only size pass, including at C=0. Determine c before testing construction. If C<c, report a construction stop with requested (w,c), work deficit zero and construction deficit c−C. Release the work hold and keep the prefix, both debits and the published state as they were. The pass was reached under a hold; the event did not commit.
3. **W≥w and C≥c.** Hold the full (w,c) and the required workspace and record capacity, stage the natural privately, and atomically commit the exact pair, result and mandatory record. The remaining pair is (W−w,C−c). There is one committed event, including when z=0. This trial injects no host interruption.

**SOURCE.** On branch 1 D1972 prescribes the following S, from validated widths alone. Intervals are inclusive integer intervals. Singletons and two-point sets have no duplicate members.

| Operand widths | S, possible construction widths |
|---|---|
| a<b | {1} |
| a=b | [1,max(1,a−1)] |
| a=b+1 | [1,a] |
| a≥b+2 | {a−1,a} |

Let g(s)=max(0,s−C). Record the image g(S). Map interval endpoints to the interval [g(low),g(high)]; map a two-point set memberwise and remove duplicates. A singleton image certifies the exact **deficit**, even if c itself is unresolved. A singleton S independently establishes c by width alone. Mark construction **sufficient** when max g(S)=0, **short** when min g(S)>0, and **undetermined** otherwise. Retain the certified lower bound min g(S) and always keep the symbolic deficit max(0,β(max(x−y,0))−C), bound to the descriptor, subtraction row, reached definition/occurrence/visit and the immutable left and right references **in order**. Width-only knowledge leaves the size pass unreached even when it determines the number. On branch 2 use measured c. [D1927, D1972]

**INFERENCE · why the four rows differ.** The values of width k form the integer interval [2^(k−1),2^k−1] for k≥2, and [0,1] for k=1. The differences of two such intervals fill every integer between their extreme differences. If a<b, all differences truncate to zero. At equal widths ≥2 the truncated difference ranges from zero to 2^(a−1)−1; at width one both possible result values have one digit. At adjacent widths the smallest difference is one and the largest reaches width a (including b=1). At a gap of at least two, even the smallest difference exceeds 2^(a−2), and none exceeds x. Taking x=2^(a−1) with a positive right operand realizes width a−1; taking x=2^a−1 with the smallest right operand realizes width a. Thus the work-cut check cannot generally substitute a single guessed width for either of the last two rows.

## Record and two trial observers

**SOURCE.** D643–51 and D654–58 fix ordinary public behaviour and permit a per-boundary linked opt-in that identifies the meter, fields and scope. D1923–31 describes the paired evaluator record. D1954–56 distinguishes a hold, measurement and publication.

**PROPOSED.** Bind each internal record to the build, program, admitted start, hash/canonical and paired descriptor, ordered operand references, root scope, boundary, definition, occurrence and visit. Record the phase reached, initial and pre-attempt pair, debit and remaining pair, result or stop with the applicable evidence above, and the committed prefix and account. Begin with an empty prefix and holdings; there are no requests, memo events or other purchases. A returned value enters the result only on commit. Remaining always samples **after** commit or release. On either refusal the latest event debits are (0,0) and the remaining pair equals the pre-attempt pair. A work reservation used for measurement is private.

* **Ordinary at export b.** Return the natural or the visible primary allowance stop (work or construction), with the public actions and later-readable state empty. No numeric meter readings are purchased here. A reader comparing projections keeps a resource stop distinct from a returned zero.
* **Linked exact at the same export.** Start with the same ordinary projection. For this paper trial select the existing paired readings of the sole root event: pre-attempt pair, event debit and remaining pair; on refusal also the requested work, known or symbolic construction demand, primary reason, deficits and the reached pricing phase. On a work refusal include the width check and its certified deficit image/status and recoverable bound expression described above. On a construction refusal give the measured demand and deficits. At a return the debit gives the exact pair. The descriptor/start and ordered references may bind evidence by identity; a reader must be able to recover the expression for this occurrence. This projection creates no extra public field in the general export contract and does not expose the entire private record. No byte encoding is prescribed.

**SOURCE / INFERENCE.** D1967 preserves EV-115’s natural result and the underflow zero. Historical RULES-EVALUATOR L1677–87 used one scalar N8 total with A=a+b, R=a, T=0 and W=m. Its S01–04 prices are controls for that descriptor. Neither the whole-program cost nor either new allowance is inferred from them. COVERAGE-EVALUATOR’s EV-115 row records its draft standing; GAPS-EVALUATOR E-3/E-18/E-27 retain wider meter, interface and numeric-oracle work. The D1970 reservations and D1972 preflight are proposed reference costs; the trial supplies no measurement, adoption, memory qualification or production conformance result.

## Fixed starts and expected paper records

**SOURCE · paper comparison only.** Two independently derived sets of records agree on all 28 starts and 56 selected projections. They give 12 work refusals, six construction refusals and ten returns. The trial has no emitted subtraction witnesses. Subtraction execution, decoding and conformance are **NOT RUN**. The E and OC2 passages apply to these paper records under their own scope in [IMPORTS.md](IMPORTS.md).

**SOURCE ·** Each row starts afresh for each observer. The header is (program `paper-sub`, build `B0`, admission `A0`, canonical descriptor `K0`, hash descriptor `H0`, paired descriptor `sub-pair`). The operation is the natural subtraction row, at definition `trial`, occurrence `sub.site`, visit 1. The sole scope `root` supplies both balances at export `b`. The operands have already been obtained. A0 binds each displayed immutable reference to its natural and validated width in that position. The grant is both the initial and pre-attempt pair. The prior debit and hold are (0,0). The initial prefix, public actions, and later-readable state are empty. There are no requests, memo events, additional purchases, later events or scheduled interruptions. The start ID labels the worksheet only.

**INFERENCE · Reading a row.** Take the common header, the ledger row and its phase evidence below. Together they specify the private record. The **ordinary** column is the complete varying part of the ordinary projection. A return occupies the result position and has no stop. A refusal occupies the stop position and has no result. Both have public actions [] and later-readable state ∅. In particular a returned 0 is observable.

For the **linked exact** projection take that same ordinary record and the ledger’s **Pre, Debit and Remaining**. At a refusal also take the reached pricing phase, primary reason and the applicable refusal row below. At a return the debit itself gives the price pair and there are no refusal fields. This defines both projections at every start without publishing the shared private header as extra meter fields. For a work stop, the refusal row supplies both the conditional demand q and its retained deficit expression, or a known demand plus that expression. For a construction stop it supplies the measured pair and both numerical deficits. Holds and workspace are private. Evidence may resolve its specified bindings by identity.

In the tables b′ denotes the right width (b in the rule); q is β(max(x−y,0)). An entry “1 by width” names certified demand with the size pass unreached. The nonempty private sequence on return contains the single paid event. The request/trail prefix stays empty for all 28 starts.

| Start | Left | Right | (a,b′) | Pre | w | Reached phase | Size pass | Construction demand | Ordinary | Debit | Remaining |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | nat:2 | nat:5 | (2,3) | (30,0) | 31 | WorkCheck | no | 1 by width | work stop | (0,0) | (30,0) |
| S02 | nat:2 | nat:5 | (2,3) | (30,1) | 31 | WorkCheck | no | 1 by width | work stop | (0,0) | (30,1) |
| S03 | nat:2 | nat:5 | (2,3) | (31,0) | 31 | ConstructionCheck | yes | 1 measured | construction stop | (0,0) | (31,0) |
| S04 | nat:2 | nat:5 | (2,3) | (31,1) | 31 | Commit | yes | 1 measured | return 0 | (31,1) | (0,0) |
| S05 | nat:0 | nat:0 | (1,1) | (22,0) | 23 | WorkCheck | no | 1 by width | work stop | (0,0) | (22,0) |
| S06 | nat:0 | nat:0 | (1,1) | (23,1) | 23 | Commit | yes | 1 measured | return 0 | (23,1) | (0,0) |
| S07 | nat:5 | nat:5 | (3,3) | (36,1) | 37 | WorkCheck | no | q | work stop | (0,0) | (36,1) |
| S08 | nat:5 | nat:5 | (3,3) | (37,0) | 37 | ConstructionCheck | yes | 1 measured | construction stop | (0,0) | (37,0) |
| S09 | nat:5 | nat:5 | (3,3) | (37,1) | 37 | Commit | yes | 1 measured | return 0 | (37,1) | (0,0) |
| S10 | nat:7 | nat:4 | (3,3) | (36,2) | 37 | WorkCheck | no | q | work stop | (0,0) | (36,2) |
| S11 | nat:7 | nat:4 | (3,3) | (37,1) | 37 | ConstructionCheck | yes | 2 measured | construction stop | (0,0) | (37,1) |
| S12 | nat:7 | nat:4 | (3,3) | (37,2) | 37 | Commit | yes | 2 measured | return 3 | (37,2) | (0,0) |
| S13 | nat:4 | nat:7 | (3,3) | (37,1) | 37 | Commit | yes | 1 measured | return 0 | (37,1) | (0,0) |
| S14 | nat:8 | nat:7 | (4,3) | (40,0) | 41 | WorkCheck | no | q | work stop | (0,0) | (40,0) |
| S15 | nat:15 | nat:4 | (4,3) | (40,2) | 41 | WorkCheck | no | q | work stop | (0,0) | (40,2) |
| S16 | nat:15 | nat:4 | (4,3) | (40,4) | 41 | WorkCheck | no | q | work stop | (0,0) | (40,4) |
| S17 | nat:8 | nat:7 | (4,3) | (41,1) | 41 | Commit | yes | 1 measured | return 1 | (41,1) | (0,0) |
| S18 | nat:15 | nat:4 | (4,3) | (41,3) | 41 | ConstructionCheck | yes | 4 measured | construction stop | (0,0) | (41,3) |
| S19 | nat:15 | nat:4 | (4,3) | (41,4) | 41 | Commit | yes | 4 measured | return 11 | (41,4) | (0,0) |
| S20 | nat:16 | nat:3 | (5,2) | (43,3) | 44 | WorkCheck | no | q | work stop | (0,0) | (43,3) |
| S21 | nat:31 | nat:2 | (5,2) | (43,4) | 44 | WorkCheck | no | q | work stop | (0,0) | (43,4) |
| S22 | nat:31 | nat:2 | (5,2) | (43,5) | 44 | WorkCheck | no | q | work stop | (0,0) | (43,5) |
| S23 | nat:16 | nat:3 | (5,2) | (44,3) | 44 | ConstructionCheck | yes | 4 measured | construction stop | (0,0) | (44,3) |
| S24 | nat:16 | nat:3 | (5,2) | (44,4) | 44 | Commit | yes | 4 measured | return 13 | (44,4) | (0,0) |
| S25 | nat:31 | nat:2 | (5,2) | (44,4) | 44 | ConstructionCheck | yes | 5 measured | construction stop | (0,0) | (44,4) |
| S26 | nat:31 | nat:2 | (5,2) | (44,5) | 44 | Commit | yes | 5 measured | return 29 | (44,5) | (0,0) |
| S27 | nat:2 | nat:0 | (2,1) | (26,1) | 27 | WorkCheck | no | q | work stop | (0,0) | (26,1) |
| S28 | nat:2 | nat:0 | (2,1) | (27,2) | 27 | Commit | yes | 2 measured | return 2 | (27,2) | (0,0) |

### Work refusal · width evidence and linked exact fields

**INFERENCE ·** For each WorkCheck row the scope root limits work. The invoice w exceeds W. The ordered headers select the candidate width set S. Map every s in S to max(0,s−C) to get the deficit image D. Brackets denote inclusive integer intervals. A singleton D establishes the exact deficit. A singleton S independently establishes the construction demand. For any other S the demand field `q` means the bound term β(max(x−y,0)) for the operands in this row. The size pass is unreached in all twelve rows.

In the table, `E(u,v,C)` denotes the retained expression max(0,β(max(x−y,0))−C) with u in the x position and v in the y position. Its binding identifies `sub-pair`, the subtraction row, the reached definition/occurrence/visit `trial/sub.site/1`, the admitted start at b/root, its phase, its ordered immutable operand references and its effective C. Preserve E even when D is a singleton. The reader can recover the width check, demand or bound, primary work reason, work deficit, construction image, lower bound and status from the indicated evidence. The cases used here are S={1} for a<b′, S=[1,max(1,a−1)] for a=b′, S=[1,a] for a=b′+1, and S={a−1,a} for a≥b′+2. The lower bound is recoverable from D even if the representation stores it separately. No operand payload is compared or scanned. This attempt has no hold, release, staged result or commit. The free balance is Pre throughout, final hold is (0,0), and both the committed prefix and cumulative debit stay empty and (0,0), respectively.

| Start | Requested work | Work deficit | Width check S | Requested construction | Construction deficit D | min D | Status | Bound expression |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | 31 | 1 | {1} | 1 by width | {1} | 1 | short | E(nat:2,nat:5,0) |
| S02 | 31 | 1 | {1} | 1 by width | {0} | 0 | sufficient | E(nat:2,nat:5,1) |
| S05 | 23 | 1 | {1} | 1 by width | {1} | 1 | short | E(nat:0,nat:0,0) |
| S07 | 37 | 1 | [1,2] | q | [0,1] | 0 | undetermined | E(nat:5,nat:5,1) |
| S10 | 37 | 1 | [1,2] | q | {0} | 0 | sufficient | E(nat:7,nat:4,2) |
| S14 | 41 | 1 | [1,4] | q | [1,4] | 1 | short | E(nat:8,nat:7,0) |
| S15 | 41 | 1 | [1,4] | q | [0,2] | 0 | undetermined | E(nat:15,nat:4,2) |
| S16 | 41 | 1 | [1,4] | q | {0} | 0 | sufficient | E(nat:15,nat:4,4) |
| S20 | 44 | 1 | {4,5} | q | {1,2} | 1 | short | E(nat:16,nat:3,3) |
| S21 | 44 | 1 | {4,5} | q | {0,1} | 0 | undetermined | E(nat:31,nat:2,4) |
| S22 | 44 | 1 | {4,5} | q | {0} | 0 | sufficient | E(nat:31,nat:2,5) |
| S27 | 27 | 1 | [1,2] | q | [0,1] | 0 | undetermined | E(nat:2,nat:0,1) |

### Construction refusal · measured evidence and linked exact fields

**INFERENCE ·** Root limits construction in these six rows. The work hold funds the read-only exact-size pass, including in S03 and S08 where C=0. The primary reason is construction, the reached phase is ConstructionCheck, and both deficits are now numeric. Only the work hold is acquired and released. There is no full reservation, staged result, or commit. Remaining equals Pre, the final hold and cumulative debit are (0,0), and the committed prefix stays empty. The released hold and free balance during measurement are private.

| Start | Requested (w,c) | Deficits (work,construction) | Work hold released | Free during size pass |
| --- | --- | --- | --- | --- |
| S03 | (31,1) | (0,1) | (31,0) | (0,0) |
| S08 | (37,1) | (0,1) | (37,0) | (0,0) |
| S11 | (37,2) | (0,1) | (37,0) | (0,1) |
| S18 | (41,4) | (0,1) | (41,0) | (0,3) |
| S23 | (44,4) | (0,1) | (44,0) | (0,3) |
| S25 | (44,5) | (0,1) | (44,0) | (0,4) |

On each return the funded size pass precedes the full hold, staging and atomic publication. The final hold is zero, and the debit supplies the exact returned event’s price. On S07 even coincident operand references leave the width-only status undetermined. On S10, S16 and S22 the deficit is exactly zero with several possible demand widths. Reversing the operands in S11/S13 changes the measured result. The equal headers and grants in S24/S25 admit different measured widths.
