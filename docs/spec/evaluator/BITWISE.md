# AND, OR and XOR on two obtained naturals

**PROPOSED · paired reference rows for `b10-pair`.** For this trial `b10-pair` names the paired profile of the governing DESIGN applied to these three operations. Let x,y be the ordered obtained naturals. A *width* is the number of canonical binary digits, with β(0)=1. Read a=β(x) and b=β(y) from the validated headers, and put m=max(a,b). A *header* is that size metadata; a *payload* is a value's own digits. Before the attempt (W,C) are the effective balances at the sole serial root. Operand acquisition is already complete. Each operation constructs its natural result on every occurrence, even when the result is zero, equals an operand or is already interned.

**SOURCE · price choice.** The owner chose the four-field Add layout for AND, OR and XOR (B-1) and the admitted wrong-kind fee (K-1). The numerical rows below retain the proposed standing of Math2’s descriptor with Codex A’s review amendments. The family’s E and OC2 imports are listed in the [import register](IMPORTS.md).

**Words.** A *reference* is an immutable name of an admitted value; *interned* means stored once for each content. An *invoice* is the pair (w,c) an event requests: work w and construction c. A *quote* computes the work invoice before any credit is held. A *hold* removes credit privately from the available balance until commit or release. A *row* is one priced line of a descriptor for one kind of reached event; a *descriptor* is a named set of rows and observation rules. A *width check* derives a set S of possible result widths without reading a payload. A *size pass* is the funded, read-only measurement of the exact result width. A *step* is one unit of scheduled work. A *column* is a binary position across the operands. A *field* is a scratch register of a fixed number of binary digits. *Emission* writes the result's digits into private staging. A *certificate* is a recorded inequality w>W proved without forming w. The *basis* of a record item is the set of facts it was computed from; the *provenance* of c names the phase that established it.

## Meaning and construction

**PROPOSED · meaning.** DESIGN includes the three operations (D1844) but writes no equation. Write x=Σ x_i 2^i and y=Σ y_i 2^i with digits x_i, y_i ∈ {0,1}, every digit above an operand's width being 0. There is no fixed width. Then

    AND(x,y) = Σ (x_i·y_i) 2^i
    OR(x,y)  = Σ max(x_i, y_i) 2^i
    XOR(x,y) = Σ ((x_i + y_i) mod 2) 2^i

**SOURCE / INFERENCE · construction.** The construction invoice is the exact width of the result, c = β(f(x,y)), for f the selected operation. A zero result costs one cell (D1939, D1946). From the headers alone, the result width lies in the following set S. Every member of each set occurs for some operands with those headers.

| Operation | S from the headers |
|---|---|
| AND | {a} if a=b; the integer interval [1, min(a,b)] otherwise |
| OR | {m} |
| XOR | {m} if a≠b; the integer interval [1, max(1, a−1)] if a=b |

OR always has width m, so its header gives its exact size. D1952 `[proposed]` lets a row read such a size directly. For an exact header result, the B-1 rows make the size pass on every funded event, also where the header fixes c. Add's row makes one even when its set is a singleton (D1972 `[proposed]`).

## Work invoice

**SOURCE.** The paired work invoice has the form w = α+β_R+β_T+γ: argument parts, a safe result reservation, a safe temporary reservation and the scheduled work (D1890–1894). A missing row rejects the profile for its operation before execution (D1927).

**PROPOSED · the three bitwise rows.** Each natural row has the form w=α+R+T+γ of D1890–1894, with α=a+b. R and T are the result and temporary reservations in work, and γ counts scheduled steps. R is β_R and T is β_T, and p=β(2(a+b+2)) (D1958).

| Row | w | c |
|---|---|---|
| AND | a+b+R+T+2(m+1), with R=min(a,b), T=4p | β(AND(x,y)) |
| OR | a+b+R+T+2(m+1), with R=m, T=4p | β(OR(x,y)), which equals m |
| XOR | a+b+R+T+2(m+1), with R=m, T=4p | β(XOR(x,y)) |

The three bitwise rows are D1967's truncated-subtract row with its result bound R=a replaced by the operation's own bound (below).

**PROPOSED · the reference step.** One unit of α prices one argument digit counted by its header. One unit of R or T reserves one logical cell (D1980). One unit of c is one constructed digit (D1935–1946). One unit of γ is one scheduled step, of one of these kinds:

- a *bitwise size step* processes one aligned column: at most one digit from each operand and the Boolean test;
- a *bitwise emission step* processes one column and writes its output digit;

A step also includes a fixed number of operations on the fields below: an increment, an assignment or one comparison. Setting a pass's fields belongs to its first step. These are reference rates, not measured host costs (D1970). At column i, a slot whose width is at most i supplies zero from its header and performs no payload read.

**SOURCE · what any complete row must satisfy.** w ≥ 1 (D1888 `[proposed]`). The result reservation is a safe bound on the result width, worked out before anything is built and in a way that cannot itself overflow (D1886 `[decided]`); each reservation is at least the cells it reserves (D1980 `[proposed]`, stated for the partial fragment; these rows meet it only on the premise that it extends to them). The quote uses validated metadata and grant widths, and moves any value-dependent calculation to a charged stage (D1952 `[proposed]`, D1954 `[proposed]`).

**INFERENCE · safe bounds from the proposed equations.** For AND, x_i·y_i = 0 at every position i ≥ min(a,b), since the shorter operand's digit there is 0, so min(a,b) is a safe bound from the headers. For OR and XOR both digits are 0 at every i ≥ m, so m is one. For XOR at a=b ≥ 2 both digits at position a−1 are 1 and cancel, so a−1 is one too; at a=b=1 every result has width 1, so max(1, a−1) covers both cases. The rows use R=min(a,b) for AND and m for OR and XOR; the tighter XOR bound max(1,a−1) at a=b is not used.

**PROPOSED · quote, sizing and kind rules.**

- **Width check on a work refusal.** Use the sets S above.
- **Size pass.** Every funded B-1 natural event makes the read-only size pass.
- **Operand of another kind.** The [batch-1 wrong-kind row](WRONG-KIND.md) applies, its scope widened to AND, OR and XOR (K-1): request (h(x)+h(y)+1, 0) and return the admitted none, where h is a natural's width and is one for a tuple or the built-in none (D1958, D1965). Both ordered contributions count, also when the slots alias; write h₁=h(x) and h₂=h(y). K-1 has its own quote/work-check/selection path and omits natural sizing and emission. If W<w, stop for work: request (w,0), work deficit w−W, construction deficit known to be zero. No width set, size pass, payload read or bound natural-result expression belongs to this row. Debit (0,0). Otherwise reserve (w,0), select the admitted none, and commit its reference, the record and the work debit together; settle to (W−w,C). No natural operation, size pass or emission runs, and c=0 is affordable at every C.
- **Unavailability.** The predicate is empty: each safe bound follows from the headers.

## Phases, under a complete row

1. **Quote and work check.** Compute w from the validated headers and the grant, with exact arithmetic; no bitwise quote needs a certificate. If W<w, stop for work. Record the exact invoice and deficit. The work cut still has zero debit, unchanged balances and no funded size pass. Record the width check S, its image D={max(0,s−C) for s in S}, min D and its status: sufficient if max D=0, short if min D>0, undetermined otherwise. A singleton D gives the exact construction deficit; a singleton S certifies the width itself, while the size pass stays unreached. Retain the unevaluated expression max(0, β(f(x,y))−C), bound to the descriptor, the selected operation's row, the reached event, the two ordered immutable references and effective C. Keep both slots even when they alias, and in their order even though the operations are symmetric. Work is primary on a joint shortfall. No hold, size pass, payload read, debit, new natural or prefix change occurs. For any future build claiming this header-only behavior, apply the [backing-read control](BACKING-READ-CONTROL.md).
2. **Size pass and construction check.** If W≥w, hold (w,0), make the T workspace available before reading a digit, and make the read-only size pass, including at C=0. It scans the columns from the top: from column min(a,b)−1 for AND and m−1 for OR and XOR, one column per step, down to 0. Each size step reads digit i of each operand whose width exceeds i, by index, and tests the operation's Boolean value. The pass stops at the first column i whose value is 1, with c=i+1; if no column gives 1, c=1. It creates no result node and publishes nothing. The provenance of c is *size pass*, also where the headers already fix c (OR; AND with a=b; XOR with a≠b). If C<c, stop for construction. Record the requested (w,c) and the deficits (0, c−C), release the work hold, and commit nothing.
3. **Commit.** If C≥c, reserve the incremental construction balance c, which completes the full pair (w,c), and the record capacity; emission reuses the T workspace. Back the staged result with exactly c digits. Emission processes columns i=0,…,c−1 in increasing order. At each column, read digit i by index from each ordered operand slot whose width exceeds i. Use a header zero for any other slot. Write the resulting digit into private staging. Commit the result, its debit and its record together, then settle to (W−w, C−c).

**PROPOSED, with INFERENCE bounds · resource account (trial scope).** T=4p reserves D1970's four p-digit fields: the column index (below m), the carry or borrow field and the comparison field (unused, held at 0) and the highest nonzero output position (at most m). This is the reviewed Add layout, over-reserved by two fields. A step's two digits and its Boolean value live only within the step. At any moment the live scratch is these four fields, besides the hold and the staged result. Every field value is at most m, below 2^p. Steps: at most min(a,b) (AND) or m (OR, XOR) size steps and c ≤ R emission steps: at most 2m < 2(m+1).

Define t=max(1,β(a),β(b),β(W),β(C)) on natural rows and use β(h₁),β(h₂) for the two contributions on K-1. A natural row's quote forms its integers by addition, doubling, subtraction, comparison and β (the position of the top digit). There is no multiplication. Each formed integer has at most t+4 binary digits. The wrong-kind quote adds two contributions and 1, and the sum has at most t+1 digits. Keep a constant number of interval/point tags, exponent references and numeric fields. A fixed number of bounded integer additions, comparisons, bit-length reads and bounded writes gives O(t) numeric workspace and bit work. The stated t+4 bound on numerical quote intermediates is sufficient. Instrumentation counts refer only to the stated algorithm.

A refusal record holds a fixed number of fields of O(t) digits: the pre-attempt pair, w, the deficit, at most two pieces of S and of D, min D, the status, the basis and the provenance. It also holds a fixed number of references: descriptor, row, event, the two operands and the scope. A commit record holds w, c, the debit and the remaining pair. The first refusal of a run needs no hold: its quote and record come from the profile's separate bookkeeping bound (D1954 "including the very first refusal"; D1980's Q).

The quote frame, the quote's own fields, lives from the quote to the work check. On a work refusal its fields pass to the record and the frame is released. On a funded event the frame keeps w and the field width through the hold; the size pass and emission then use only the four fields of T. A construction refusal releases the hold and the fields. A commit releases the fields after publication. No row keeps a further copy of an operand, because size and emission steps read the operands in place (D1980 "Count any further simultaneously retained copies explicitly": there are none). Physical backing is the staged result's c digits, the four fields, the quote frame and the record, accounted apart from W (D1956, D1980).

At the work hold, make the funded pass's T workspace available before reading a digit. Reuse it for emission and reserve only the incremental construction balance after the work hold. Account separately for the staged c digits, four fields, constant per-column transient bits and live quote/record state. Encode a pass's reads by ordered slot, phase and a bounded index range with direction, or a checked reference to equivalent origin evidence. Bind both slots even if they alias. Use actual access-boundary evidence to validate those ranges. For r total encoded identifier and binding bits, add O(r) space and output work or cite the admitted store's bounded reference-access rule. The O(t) claim covers numeric bookkeeping; copying an arbitrary payload or listing all accesses individually has a different cost. Preserve live/released holds, pre- and post-balances, cumulative debit, prefix, observer and actual phase from the field map at refusal, commit or controlled host stop.

## Common trial record

**PROPOSED.** A start fixes the admitted inputs, selected operation, program, definition, occurrence, visit, build, descriptors, scope, initial balances, prior state, schedule and linked observer. A *witness* is evidence captured where that operation actually reaches a phase. A *hold* reserves credit privately. A *commit* publishes the result, paired debit and mandatory record atomically. Units in a pair are ordered (work, construction).

Validate the start before attempting a primitive. Bind each ordered operand slot to its immutable reference and its admitted kind and size metadata. Reference identity and interned content identity serve different purposes; one reference may occupy both argument positions. Keep the selected operation as well as the site in the binding. An unadmitted operand prevents entry and gives a pre-run refusal in the admission report. It supplies no reached-event witness, allowance cut, primitive return or event projection.

**Semantic fragment sequence.** One reached event on a natural row passes through these fragments, in order, and stops at the first that ends it: quote; work check (a work cut ends here); work hold; size pass; construction check (a construction cut ends here, with release of the hold); full reservation; private staging; commit; release of temporaries. The admission check precedes them all and is not a fragment of the event. A K-1 event passes through these fragments, in order, and stops at the first that ends it: quote; work check (a work cut ends here); full reservation of (w,0) and record capacity; selection of the admitted none; commit of the reference, record and work debit together; release of temporaries, here the quote fields, which every commit releases after publication. It records c=0 from the selected kind row. The natural sizing, width-check and emission fields are inapplicable.

**Mandatory record location.** The mandatory record of a returning event is published in the commit fragment, with the result and the debit (D1956). The record of a cut is the run record's report at the first unpaid event (D1925–1927). Neither enters the request or trail prefix: these rows make no request or trail entry.

**Field map.** Encode each record with these fields, so that independent encodings align field by field.

| Part | Fields |
|---|---|
| Start binding | program, definition, occurrence, visit, build, admission state, canonical, hash and paired descriptors, scope, export, observer, schedule, selected operation |
| Operands | slot 1: reference, kind, width; slot 2: reference, kind, width; whether the slots alias |
| Prefix | committed request/trail prefix before and after (empty here); private ordered debits (one entry on commit, none on a cut) |
| Event record | pre-attempt pair; reached fragment; requested work (number or certified inequality); requested construction (number, width set or bound expression); deficits; width set S, image D, min D, status; basis of S and D; holds (live, released); size-pass measurement; provenance of c; payload reads by fragment; debit; remaining after commit or cleanup; outcome; cumulative committed pair |
| Ordinary observation | result, or visible stop with its axis (work or construction) or the cause of a scheduled controlled physical stop; public actions (empty); later-readable state (empty) |
| Trial-exact observation | the ordinary observation, the selected event's debit, and the available pair after commit or cleanup |

**Basis per field.** Basis(S)=H, the ordered kind/width projection restricted to natural widths. Basis(D, min D, status)=(H,C). Map each interval or isolated point by max(0,s−C), coalescing overlapping pieces and preserving gaps. An exact natural fee uses H; its work deficit uses H and W. Bind the unevaluated construction expression to both ordered immutable operands, the reached event, effective C and descriptor. K-1 records contributions from the ordered kind/width headers and the work deficit from those contributions and W. A cut debits (0,0) and retains the pre-attempt available pair after cleanup. An exact c on a funded natural row records size-pass evidence. K-1 records c=0 from its selected kind row.

The run account's committed pair is the componentwise sum of its committed debits, (0,0) for an empty account. With no hold outstanding, initial = committed + remaining for that account. A zero event debit on a refusal means there was no commit.

**Observers.** Run the ordinary and the linked trial-exact observer separately at export `b`. Ordinary buys the returned value or the visible primary stop in its proper position (including the cause for a scheduled controlled physical stop), the public actions and the later-readable state. At this boundary the latter two are empty. Trial-exact adds **only** the selected event debit and the available pair after commit or stop cleanup. The private invoice, the certificate, the phase, the ordered bindings, the width set, the deficit image, the bound expression, the transient hold, the latest debit and the cumulative pair are not further purchases. The visible primary stop names its axis: it is a stop for work or a stop for construction, and on a joint shortfall it is a stop for work (D1952). The reason for a work cut, its exact deficit, is private. Compare projected records only at the same start, grant, schedule and observer.

**Evidence origin.** Capture the private record at the reached transition before projecting it. Bind actual payload reads, when present, to the ordered references and phase through the implementation's access boundary. A self-reported no-read flag or agreement on a public result alone cannot establish private access behaviour. Missing or inconsistent bindings fail validation.

**SOURCE · governing DESIGN SHA-256** `6439d9cfb70cfb02457ba06a90cfea999b7535bf9ae063cd131bd18c2fa8870a`. Each excerpt below is exact. If it does not end with its own tag, the tag of its segment follows in parentheses. D13: "A tag covers every sentence after the previous tag or the start of its paragraph."

> D1844 · The evaluator includes left and right shift, AND, OR and XOR. `[decided]` Their rules and charges await review. (segment `[proposed]`)

> D1886 · Before it builds anything a primitive works out $\beta$, an upper bound on the size of its result and of whatever it needs meanwhile, in a way that cannot itself overflow, and pays it. (segment `[decided]`)

> D1888 · Every reached event has a positive work price $w$ and a nonnegative construction price $c$. (segment `[proposed]`)

> D1946 · A construction pays on every occurrence, even if its content is already interned, happens to equal an operand, or dies at once. (segment `[decided]`)

> D1946 · Computing an arithmetic result constructs a natural even if zero is in the pool. (segment `[proposed]`)

> D1952 · Check work first, then measure the exact size of the result, then commit everything together. If both limits fall short, report work as the primary reason and retain the construction shortfall in the record. (segment `[decided]`)

> D1952 · Where the header supplies the exact size, the row can read it directly. (segment `[proposed]`)

> D1927 · The refusal performs no operand scan and commits neither debit. (segment `[proposed]`)

> D1927 · A missing row rejects the profile for that operation before execution. (segment `[proposed]`)

> D1958 · For naturals use their digit counts. For the argument contribution of an obtained tuple or the built-in none use one. (segment `[proposed]`)

> D1958 · The following abstract price includes the read-only size pass even when a build can obtain the same answer faster. `[proposed]`

> D1965 · | Binary arithmetic on a wrong kind | sum of argument contributions plus $1$ | $0$, returning the admitted none | (segment `[proposed]`)

> D1966 · | Add | $a+b+R+T+2(m+1)$, with $R=m+1,\ T=4p$ | $\mathrm{bits}(x+y)$ | (segment `[proposed]`)

> D1967 · | Truncated subtract | $a+b+R+T+2(m+1)$, with $R=a,\ T=4p$ | $\mathrm{bits}(\max(x-y,0))$ | (segment `[proposed]`)

> D1970 · The proposed addition/subtraction scratch layout has a column index, carry/borrow, comparison or sign state, and highest nonzero output position. (segment `[proposed]`)

> D1970 · Each field fits $p$ bits. Reuse that workspace between passes. A zero result occupies one logical digit. (segment `[proposed]`)

> D1970 · These are reference layout and price choices open to review against a different exact layout. They are not measured implementation costs. (segment `[proposed]`)

> D1972 · Represent an interval by its endpoints and a two-point set by its members. (segment `[proposed]`)

> D1972 · When work is affordable, hold it and perform the prescribed exact-size pass even at zero construction credit. (segment `[proposed]`)

> D1972 · The full schedule must similarly say what any primitive does on its edges, how it quotes exact size, prepays peak scratch, and treats shortfalls. (segment `[proposed]`)

> D1980 · $Q$ bounds transient price calculation, including on a refused first event. Each reservation component of a work invoice is at least the number of logical cells of the storage it reserves. (segment `[proposed]`)

> D1980 · Count any further simultaneously retained copies explicitly. (segment `[proposed]`)
