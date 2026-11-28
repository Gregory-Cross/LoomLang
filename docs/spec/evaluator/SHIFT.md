# Left and right shift on two obtained naturals

**PROPOSED · paired reference rows for `b9-pair`.** For this trial `b9-pair` names the paired profile of the governing DESIGN applied to these two operations. Let x be the obtained natural to be shifted and n the obtained shift amount, in that order. A *width* is the number of canonical binary digits, with β(0)=1. Read a=β(x) and b=β(n) from the validated headers; a *header* is that size metadata, and a *payload* is a value's own digits. Before the attempt (W,C) are the effective balances at the sole serial root. Operand acquisition is already complete. A shift constructs its natural result on every occurrence, even when the result is zero, equals an operand or is already interned.

**SOURCE · price choice.** The owner chose a header-only shift quote (S-1) and the admitted wrong-kind fee (K-1). The numerical rows below retain the proposed standing of Math2’s descriptor with Codex A’s review amendments. The family’s E and OC2 imports are listed in the [import register](IMPORTS.md).

**Words.** A *reference* is an immutable name of an admitted value; *interned* means stored once for each content. An *invoice* is the pair (w,c) an event requests: work w and construction c. A *quote* computes the work invoice before any credit is held. A *hold* removes credit privately from the available balance until commit or release. A *row* is one priced line of a descriptor for one kind of reached event; a *descriptor* is a named set of rows and observation rules. A *width check* derives a set S of possible result widths without a funded pass, using the two width headers alone. A *size pass* is the funded, read-only measurement of the exact result width. A *build* is one executing implementation, and a *machine word* is its fixed-width integer. A *build fault* is a failure of a build, which is never an allowance cut. A *step* is one unit of scheduled work. A *field* is a scratch register of a fixed number of binary digits; a *cursor* is a field that holds a digit position. *Emission* writes the result's digits into private staging. A *certificate* is a recorded inequality w>W proved without forming w. The *basis* of a record item is the set of facts it was computed from; the *provenance* of c names the phase that established it. SHL and SHR name the left- and right-shift rows. The naturals of width b form the *amount class* [L_b,U_b]: L_1=0 and U_1=1; L_b=2^(b−1) and U_b=2^b−1 for b≥2. [P] is 1 when P holds and 0 otherwise.

## Meaning and construction

**PROPOSED · meaning.** DESIGN includes both shifts (D1844) but writes no equation. This page takes the meaning their names and edges give:

    left shift:   L(x,n) = x·2^n
    right shift:  R(x,n) = ⌊x / 2^n⌋

**SOURCE / INFERENCE · construction.** The construction invoice is the exact width of the result:

    c_L = a+n  if x>0,   c_L = 1  if x=0
    c_R = max(1, a−n)

The left-shift values are D2047's. The right-shift value follows from the equation: for n ≥ a the result is 0, which still occupies one digit. These equations define c; they do not license reading a payload before work is held.

## Work invoice

**SOURCE.** The paired work invoice has the form w = α+β_R+β_T+γ: argument parts, a safe result reservation, a safe temporary reservation and the scheduled work (D1890–1894). A missing row rejects the profile for its operation before execution (D1927).

**PROPOSED · the two shift rows.** Each natural row has the form w=α+R+T+γ of D1890–1894, with α=a+b. R and T are the result and temporary reservations in work, and γ counts scheduled steps. R is β_R and T is β_T.

| Row | w | c |
|---|---|---|
| Left shift | a+b+R+T+γ, with R=a+U_b, T=4·β(2(R+2)), γ=(b+1)+R | 1 if x=0; a+n otherwise |
| Right shift | a+b+R+T+γ, with R=max(1,a−L_b), T=4·β(2(a+2)), γ=[b≤β(a)]·b+R | max(1,a−n) |

For the right shift R=1 whenever b>β(a), because then L_b>a; the quote takes that case from the two widths and never forms L_b.

**PROPOSED · the reference step.** One unit of α prices one argument digit counted by its header. One unit of R or T reserves one logical cell (D1980). One unit of c is one constructed digit (D1935–1946). One unit of γ is one scheduled step, of one of these kinds:

- a *shift amount step* reads one digit of n into the amount field; the left shift's *zero test* reads x's one digit;
- a *shift copy step* reads one source digit by its index and writes one output digit; a *fill step* writes one zero digit.

A step also includes a fixed number of operations on the fields below: an increment, an assignment or one comparison. Setting a pass's fields belongs to its first step. These are reference rates, not measured host costs (D1970).

**PROPOSED, with INFERENCE bounds · scratch and steps.** Left shift: T reserves four fields of p_L=β(2(R+2)) digits: the amount and fill counter (at most U_b), the source cursor (at most a), the destination cursor (at most R) and the result width (at most R). Every value is at most R+1, which is below 2^(p_L−1). The size pass and emission reuse the fields (D1970). The size pass takes b+[a=1] ≤ b+1 steps and emission takes c ≤ R, so γ=(b+1)+R covers both.

Right shift: T reserves four fields of p_R=β(2(a+2)) digits: the amount and source offset (at most U_b ≤ 2a−1 whenever it is read), the source cursor (below a), the destination cursor (below a) and the result width (at most a). Every value is below 2(a+2), which is below 2^p_R. The size pass takes [b≤β(a)]·b steps and emission takes c ≤ R.

**SOURCE · what any complete row must satisfy.** w ≥ 1 (D1888 `[proposed]`). The result reservation β_R is a safe bound on the result width, worked out before anything is built and in a way that cannot itself overflow (D1886 `[decided]`, D2046 `[decided]`, D2047 `[proposed]`). Each reservation is at least the cells it reserves (D1980 `[proposed]`, stated for the partial fragment; these rows meet it only on the premise that it extends to them). The quote uses validated metadata and grant widths, and moves any value-dependent calculation to a charged stage (D1952 `[proposed]`, D1954 `[proposed]`). The descriptor states a total, reproducible predicate for "preflight bound unavailable" (D1927 `[proposed]`).

**INFERENCE · the rows meet these conditions.** w ≥ α = a+b ≥ 2. R ≥ c. Left shift: c=1 ≤ R when x=0, and c=a+n ≤ a+U_b=R otherwise. Right shift: if b>β(a), c=1=R; otherwise n ≥ L_b, so c=max(1,a−n) ≤ max(1,a−L_b)=R. So R is a safe result bound worked out from the two widths alone, and each reservation is at least the cells it reserves, on the premise above (D1980). Every value-dependent calculation is in the funded size pass, which γ charges. Left-shift certificate: b ≥ β(W)+2 gives 2^(b−1) ≥ 2^(β(W)+1) > W, since W < 2^β(W). Also b ≥ 3, so w > R = a+2^b−1 ≥ 2^b > 2^(b−1). Hence w > 2^(b−1) > W. Right-shift header bypass: b>β(a) gives n ≥ 2^(b−1) ≥ 2^β(a) > a. The quote reads only the two width headers and W, every integer it forms is bounded as the resource account below states, and the predicate for "preflight bound unavailable" is empty.

**PROPOSED · quote, sizing and kind rules.**

- **Quote.** Only the validated headers supply operand information. A left shift reserves β_R ≥ a+2^b−1, the widest result for any amount of width b. A right shift reserves at least the widest result for any amount of width b, which is at most a. The quote never reads x's digit; a header a=1 does not tell 0 from 1, so the left-shift bound covers x=1.
- **Width check on a work refusal.** S is the set of result widths possible for all operands with the given headers.
- **Operand of another kind.** The [batch-1 wrong-kind row](WRONG-KIND.md) applies, its scope widened to the two shifts (K-1): request (h(x)+h(n)+1, 0) and return the admitted none, where h is a natural's width and is one for a tuple or the built-in none (D1958, D1965). Both ordered contributions count, also when the slots alias; write h₁=h(x) and h₂=h(n). K-1 has its own quote/work-check/selection path and omits natural sizing and emission. If W<w, stop for work: request (w,0), work deficit w−W, construction deficit known to be zero. No width set, size pass, payload read or bound natural-result expression belongs to this row. Debit (0,0). Otherwise reserve (w,0), select the admitted none, and commit its reference, the record and the work debit together; settle to (W−w,C). No natural operation, size pass or emission runs, and c=0 is affordable at every C.
- **Unavailability.** The predicate for "preflight bound unavailable" (D1927) is empty: every quote reaches an exact invoice or a certificate from the headers and W, and every integer it forms has at most t+4 binary digits (resource account below). A build that cannot hold a quantity this profile establishes has a build fault.

## Phases, under a complete row

1. **Quote and work check.** Compute w, or a certified inequality w>W, from the two widths and W. A capped calculation may prove the excess without forming the large number; record the certified inequality, the row and the operands (D1927). The left-shift quote does this exactly when b ≥ β(W)+2: stop for work with the certificate w > 2^(b−1) > W, recorded as the row, b and W. The quote forms neither 2^b nor w, and the exact deficit stays the unevaluated row expression. Otherwise form w exactly. The right-shift quote takes R=1 and size term 0 if b>β(a); otherwise R=max(1,a−L_b), with L_b ≤ a, and size term b. It forms w exactly and needs no capped exit. If W<w, stop for work. Record the requested work or the certificate, and the exact deficit w−W when w is formed. Record the width check S (the table below, basis H), its image D={max(0,s−C) for s in S}, min D and its status: sufficient if max D=0, short if min D>0, undetermined otherwise. Retain the unevaluated expression max(0, β(f(x,n))−C), bound to the descriptor, row, reached event, the two ordered immutable references and effective C, even when the two slots alias. Work is primary on a joint shortfall. No hold, size pass, debit, new natural or prefix change occurs. No payload is read. For any future build claiming this header-only behavior, apply the [backing-read control](BACKING-READ-CONTROL.md).
2. **Size pass and construction check.** If W≥w, hold (w,0), make the T workspace available before reading a digit, and, except where the right shift skips it (below), make the read-only size pass, including at C=0. Left shift: The size pass reads the b digits of n into the amount field, one amount step each. When a=1 it also reads x's one digit (the zero test). It sets c=1 when a=1 and that digit is 0, and c=a+n otherwise. The size term b+1 is charged whether or not a=1, because the published schedule fixes γ from the headers alone. Right shift: The same SHR tariff applies to every amount. When n≥a the funded result is zero with c=1. Skip the size pass exactly when b>β(a); in that case R=c=1. Otherwise read all b amount digits under the work hold, including when n≥a. In general 0≤R−c≤U_b−L_b. Zero slack is guaranteed on the header bypass and can also occur elsewhere. The size pass reads the amount digits into the amount field, one amount step each, and sets c=max(1,a−n); it reads no digit of x, also at a=1. Neither pass forms the shifted integer. A completed funded amount pass reads each index 0,…,b−1 of ordered amount slot 2 once. The row leaves their visit order open. Bind the accesses that occur to slot 2 and the size phase with a directed bounded range or a checked reference to equivalent origin evidence. A controlled stop records the reached access prefix. The provenance of c is *size pass*; on the header bypass it is *headers*, and the record says that the size pass never ran and gives it no credit. If C<c, stop for construction. Record the requested (w,c), the deficits (0, c−C) and the exact c with its provenance, release the work hold, and commit nothing. Both balances and the prefix stay as before.
3. **Commit.** If C≥c, reserve the incremental construction balance c, which completes the full pair (w,c), and the record capacity; emission reuses the T workspace. Emit the result into private staging. Back the staged result with exactly c digits, never R. Left shift: If x=0, one fill step writes the digit 0. Otherwise n fill steps write zeros at positions 0,…,n−1, then a copy steps read x's digit j and write it at position n+j, for j=0,…,a−1. Right shift: If n ≥ a, one fill step writes the digit 0. Otherwise the source cursor is set to n once, by bounded position access, and a−n copy steps read x's digit n+j and write it at position j, for j=0,…,a−n−1. No step advances over a skipped digit. Commit the result, its debit and its record together, then settle to (W−w, C−c).

**PROPOSED · width sets from H.** The width check of phase 1 takes S from this table. Every member of each set occurs for some operands with those headers (INFERENCE). The set ignores operand identity even when the slots alias.

| Row | S from H | Form |
|---|---|---|
| Left shift, a≥2 | [a+L_b, a+U_b] | interval |
| Left shift, a=1 | {1} ∪ [1+L_b, 1+U_b]; this is [1,2] when b=1 | point and interval (new; D1972 has only intervals and two-point sets) |
| Right shift | [max(1,a−U_b), max(1,a−L_b)]; {1} when b>β(a) | interval |

A left-shift endpoint a+2^(b−1) or a+2^b−1, and its image member, is kept as a tagged expression in (a,b,C): a+2^e+δ with e=b−1 and δ=0, or e=b and δ=−1. The resource account below says how it is compared and written.

**PROPOSED · edges and large amounts.** A right shift by n ≥ a returns 0 at c=1 (D2045 decides the 0 for n>a). The right-shift row prices every n; for n ≥ a it constructs 0 at c=1, and for b>β(a) the headers prove n>a and no size pass runs. The full SHR work invoice applies on this edge. Computing zero constructs a one-digit natural (D1946). A left shift of zero returns 0 at c=1; its work is the left-shift row's, since the header a=1 does not tell 0 from 1. No row forms a shifted integer before both checks pass (D2046, D2047). The reason "preflight bound unavailable" arises only by the descriptor's predicate, never as a substitute for a certified excess. A machine-word overflow in a build, on a price the profile can establish, is a build fault: never an allowance cut and never "unavailable". Truncating the amount to a machine word, or wrapping a sum, is a defect of the build.

**PROPOSED, with INFERENCE bounds · resource account (trial scope).** Define t=max(1,β(a),β(b),β(W),β(C)) on natural rows and use β(h₁),β(h₂) for the two contributions on K-1. A natural row's quote forms its integers by addition, doubling, subtraction, comparison and β (the position of the top digit). There is no multiplication. Each formed integer has at most t+4 binary digits. The left-shift certificate exit forms only β(W)+2 and b−1. The wrong-kind quote adds two contributions and 1, and the sum has at most t+1 digits. Keep a constant number of interval/point tags, exponent references and numeric fields. For e≥β(C)+1, a+2^e+δ>C for δ∈{−1,0} and a≥1. Decide the comparison symbolically. Otherwise write a one followed by e zeros, then add a and δ by bounded integer arithmetic. The constructed endpoint fits t+2 bits. Treat the b=1 class directly. Apply the same cap before writing any deficit endpoint or min D. On SHR take the b>β(a) exit before forming either class endpoint. In an exact SHL quote b≤β(W)+1, so constructing U_b by writing b one-bits takes O(t) bit work. A fixed number of bounded integer additions, comparisons, bit-length reads and these bounded writes gives O(t) numeric workspace and bit work. The stated t+4 bound on numerical quote intermediates is sufficient. Instrumentation counts refer only to the stated algorithm.

A refusal record holds a fixed number of fields of O(t) digits: the pre-attempt pair, w or the certificate (b,W), the deficit or its unevaluated expression, at most two pieces of S and of D with tagged endpoints, min D, the status, the basis and the provenance. It also holds a fixed number of references: descriptor, row, event, the two operands and the scope. A commit record holds w, c, the debit and the remaining pair. The first refusal of a run needs no hold: its quote and record come from the profile's separate bookkeeping bound (D1954 "including the very first refusal"; D1980's Q).

The quote frame, the quote's own fields, lives from the quote to the work check. On a work refusal its fields pass to the record and the frame is released. On a funded event the frame keeps w and the field width through the hold; the size pass and emission then use only the four fields of T. A construction refusal releases the hold and the fields. A commit releases the fields after publication. No row keeps a further copy of an operand, because copy steps read the operand in place (D1980 "Count any further simultaneously retained copies explicitly": there are none). Physical backing is the staged result's c digits, the four fields, the quote frame and the record, accounted apart from W (D1956, D1980). R is credit, not memory: a left shift of x=0 reserves R=1+U_b work units for a one-digit result.

At the work hold, make the funded pass's T workspace available before reading a digit. Reuse it for emission and reserve only the incremental construction balance after the work hold. Account separately for the staged c digits, four fields, constant per-column transient bits and live quote/record state. Encode a pass's reads by ordered slot, phase and a bounded index range with direction, or a checked reference to equivalent origin evidence. Bind both slots even if they alias. Use actual access-boundary evidence to validate those ranges. For r total encoded identifier and binding bits, add O(r) space and output work or cite the admitted store's bounded reference-access rule. The O(t) claim covers numeric bookkeeping; copying an arbitrary payload or listing all accesses individually has a different cost. Preserve live/released holds, pre- and post-balances, cumulative debit, prefix, observer and actual phase from the field map at refusal, commit or controlled host stop.

## Common trial record

**PROPOSED.** A start fixes the admitted inputs, selected operation, program, definition, occurrence, visit, build, descriptors, scope, initial balances, prior state, schedule and linked observer. A *witness* is evidence captured where that operation actually reaches a phase. A *hold* reserves credit privately. A *commit* publishes the result, paired debit and mandatory record atomically. Units in a pair are ordered (work, construction).

Validate the start before attempting a primitive. Bind each ordered operand slot to its immutable reference and its admitted kind and size metadata. Reference identity and interned content identity serve different purposes; one reference may occupy both argument positions. Keep the selected operation as well as the site in the binding. An unadmitted operand prevents entry and gives a pre-run refusal in the admission report. It supplies no reached-event witness, allowance cut, primitive return or event projection.

**Semantic fragment sequence.** One reached event on a natural row passes through these fragments, in order, and stops at the first that ends it: quote; work check (a work cut ends here); work hold; size pass (none on a right shift with b>β(a), where the headers give c); construction check (a construction cut ends here, with release of the hold); full reservation; private staging; commit; release of temporaries. The admission check precedes them all and is not a fragment of the event. A K-1 event passes through these fragments, in order, and stops at the first that ends it: quote; work check (a work cut ends here); full reservation of (w,0) and record capacity; selection of the admitted none; commit of the reference, record and work debit together; release of temporaries, here the quote fields, which every commit releases after publication. It records c=0 from the selected kind row. The natural sizing, width-check and emission fields are inapplicable.

**Mandatory record location.** The mandatory record of a returning event is published in the commit fragment, with the result and the debit (D1956). The record of a cut is the run record's report at the first unpaid event (D1925–1927). Neither enters the request or trail prefix: these rows make no request or trail entry.

**Field map.** Encode each record with these fields, so that independent encodings align field by field.

| Part | Fields |
|---|---|
| Start binding | program, definition, occurrence, visit, build, admission state, canonical, hash and paired descriptors, scope, export, observer, schedule |
| Operands | slot 1: reference, kind, width; slot 2: reference, kind, width; whether the slots alias |
| Prefix | committed request/trail prefix before and after (empty here); private ordered debits (one entry on commit, none on a cut) |
| Event record | pre-attempt pair; reached fragment; requested work (number or certified inequality); requested construction (number, width set or bound expression); deficits; width set S, image D, min D, status; basis of S and D; holds (live, released); size-pass measurement; provenance of c; payload reads by fragment; debit; remaining after commit or cleanup; outcome; cumulative committed pair |
| Ordinary observation | result, or visible stop with its axis (work or construction) or the cause of a scheduled controlled physical stop; public actions (empty); later-readable state (empty) |
| Trial-exact observation | the ordinary observation, the selected event's debit, and the available pair after commit or cleanup |

**Basis per field.** Basis(S)=H, the ordered kind/width projection restricted to natural widths. Basis(D, min D, status)=(H,C). Map each interval or isolated point by max(0,s−C), coalescing overlapping pieces and preserving gaps. An exact natural fee uses H; its work deficit uses H and W. A capped SHL exit binds H,W, the row and the unevaluated work deficit. Bind the unevaluated construction expression to both ordered immutable operands, the reached event, effective C and descriptor. K-1 records contributions from the ordered kind/width headers and the work deficit from those contributions and W. A cut debits (0,0) and retains the pre-attempt available pair after cleanup. An exact c records headers on the SHR bypass and funded size-pass evidence on the other natural paths.

The run account's committed pair is the componentwise sum of its committed debits, (0,0) for an empty account. With no hold outstanding, initial = committed + remaining for that account. A zero event debit on a refusal means there was no commit.

**Observers.** Run the ordinary and the linked trial-exact observer separately at export `b`. Ordinary buys the returned value or the visible primary stop in its proper position (including the cause for a scheduled controlled physical stop), the public actions and the later-readable state. At this boundary the latter two are empty. Trial-exact adds **only** the selected event debit and the available pair after commit or stop cleanup. The private invoice, the certificate, the phase, the ordered bindings, the width set, the deficit image, the bound expression, the transient hold, the latest debit and the cumulative pair are not further purchases. The visible primary stop names its axis: it is a stop for work or a stop for construction, and on a joint shortfall it is a stop for work (D1952). The reason for a work cut, its exact deficit or its certificate, is private. Compare projected records only at the same start, grant, schedule and observer.

**Evidence origin.** Capture the private record at the reached transition before projecting it. Bind actual payload reads, when present, to the ordered references and phase through the implementation's access boundary. A self-reported no-read flag or agreement on a public result alone cannot establish private access behaviour. Missing or inconsistent bindings fail validation.

**SOURCE · governing DESIGN SHA-256** `6439d9cfb70cfb02457ba06a90cfea999b7535bf9ae063cd131bd18c2fa8870a`. Each excerpt below is exact. If it does not end with its own tag, the tag of its segment follows in parentheses. D13: "A tag covers every sentence after the previous tag or the start of its paragraph."

> D1844 · The evaluator includes left and right shift, AND, OR and XOR. `[decided]` Their rules and charges await review. (segment `[proposed]`)

> D1886 · Before it builds anything a primitive works out $\beta$, an upper bound on the size of its result and of whatever it needs meanwhile, in a way that cannot itself overflow, and pays it. (segment `[decided]`)

> D1888 · Every reached event has a positive work price $w$ and a nonnegative construction price $c$. (segment `[proposed]`)

> D1952 · Check work first, then measure the exact size of the result, then commit everything together. If both limits fall short, report work as the primary reason and retain the construction shortfall in the record. (segment `[decided]`)

> D1954 · A row cannot run the primitive for free to learn its price. For a nonzero left shift the required digit count is the input width plus the shift amount. Compare the amount with the residual capacity by checked arithmetic before forming a shifted integer. (segment `[proposed]`)

> D1927 · The refusal performs no operand scan and commits neither debit. (segment `[proposed]`)

> D1927 · A machine word overflow on a price the profile can establish is a build fault. A missing row rejects the profile for that operation before execution. (segment `[proposed]`)

> D2045 · | A shift right by more than the length | 0 | `[decided]` |

> D2047 · | Paired profile, same shift | The primitive row prepays the safe result and temporary bounds from work and requires the exact logical result width in construction. For nonzero $x$ shifted left by $n$ the result width is $\mathrm{bits}(x)+n$. For zero it is one. A failed check builds no shifted value. | `[proposed]` |

> D1958 · For naturals use their digit counts. For the argument contribution of an obtained tuple or the built-in none use one. (segment `[proposed]`)

> D1958 · The following abstract price includes the read-only size pass even when a build can obtain the same answer faster. `[proposed]`

> D1965 · | Binary arithmetic on a wrong kind | sum of argument contributions plus $1$ | $0$, returning the admitted none | (segment `[proposed]`)

> D1970 · The proposed addition/subtraction scratch layout has a column index, carry/borrow, comparison or sign state, and highest nonzero output position. (segment `[proposed]`)

> D1970 · Each field fits $p$ bits. Reuse that workspace between passes. A zero result occupies one logical digit. (segment `[proposed]`)

> D1970 · These are reference layout and price choices open to review against a different exact layout. They are not measured implementation costs. (segment `[proposed]`)

> D1972 · Represent an interval by its endpoints and a two-point set by its members. (segment `[proposed]`)

> D1972 · When work is affordable, hold it and perform the prescribed exact-size pass even at zero construction credit. (segment `[proposed]`)

> D1972 · The full schedule must similarly say what any primitive does on its edges, how it quotes exact size, prepays peak scratch, and treats shortfalls. (segment `[proposed]`)

> D1980 · $Q$ bounds transient price calculation, including on a refused first event. Each reservation component of a work invoice is at least the number of logical cells of the storage it reserves. (segment `[proposed]`)

> D1980 · Count any further simultaneously retained copies explicitly. (segment `[proposed]`)

> D2046 · | A shift left by a huge amount | no special default: the safe bound on the result is reserved before anything is built; if that bound cannot be worked out safely or cannot be paid, the run stops as out of fuel; otherwise the ordinary shift result | `[decided]` |

> D2054 · An edge result is charged its arguments and one. `[proposed]`
