# Literal read of a natural in execution

**PROPOSED · paired reference row.** For this trial `b2-pair` names the candidate paired prices of DESIGN §15.12 with exact integer quotation. A *start* fixes the program and input handle offered for admission, the export and its limits, the initial balances, the prior state, the schedule and the linked observer. A *site* is a place in a program where an event can occur, and a *visit* numbers the arrivals at one site within a run, from 1. An *event* is one reached transition at a site and visit. Its *price* is an ordered pair (work, construction). A *hold* reserves credit privately. A *commit* publishes an event's selected value or binding, its paired debit and its mandatory record in one step. The *starting pool* is the set of value nodes identified before execution. A *literal read* is the event of reaching a written literal in execution. Let v be a natural literal written at site s of an admitted program, reached at visit n under the environment η with effective balances k = (W,C) of the sole serial root scope.

## Rule and phases

Under `b2-pair` the literal charge is c_lit = (1,0). The premise k ≥ c_lit is affordability c_lit ≤ k, which holds when both component inequalities hold, here 1 ≤ W and 0 ≤ C. Its failure ¬(c_lit ≤ k) gives the allowance cut at s, visit n.

    k ≥ c_lit
    ──────────────────────────────────   (P-Val)
    η ⊢ v ⇓^(k → k − c_lit) v

Admission placed node(v) in the starting pool before execution. That work, including any literal check under its own admission envelope, draws on neither component of the run's grant. Reaching the literal in execution is an event and is charged. Interning makes node(v) = node(u) for every value u of equal content.

1. **Quote.** The price row supplies (1,0) without reading the digits, header or width of v.
2. **W < 1**, that is W = 0. Stop for work at s, visit n. Record the requested pair (1,0), the balances before the attempt (0,C), the work deficit 1 and the construction deficit 0, which the price row fixes. Work is the reason. No selection, debit or prefix change occurs, both balances stay as they were, and earlier committed events stand.
3. **W ≥ 1.** The construction test 0 ≤ C holds for every admitted C. Hold (1,0), select node(v) from the starting pool, which constructs nothing, and commit the debit (1,0), the selected reference and the record together. Settle to (W−1,C).

**Literal source.** Record the literal occurrence, its site and visit, event kind and pooled node reference.

**Resource account (trial scope).** The quote is a constant, and the affordability test needs only whether the work balance is zero. A refusal record holds the site, visit, kind, requested pair, both deficits and references to the pre-attempt balances. A paid read stages one reference to a pooled node, and cumulative construction does not change. A copy of the literal that a build keeps belongs to the build's separately bounded storage, not to either price.

**SOURCE · standing.** D1852 displays P-Val with the charge c_lit; the display is a paragraph with no tag of its own (D13). D1848, which fixes the paired judgment and leaves c_lit to the applicable table ("An unspecified charge cannot be read as zero"), is proposed, and so is the first segment of D1858 ("These rules thread state and fuel left to right"). INFERENCE: P-Val stands no stronger than proposed. D1962 sets the literal read at (1,0) under the leading proposed tag of D1970. D1898 (built) puts the interning of literals before execution, outside fuel, and charges "a literal *in* execution". D1864 (proposed) gives the cut when the fuel left is below the charge of a reached literal. D1846 decides interning by content. D1946 and D1972 (proposed) make a literal read a selection at zero construction. D1948 (proposed) puts program literals in the starting pool. D999 (proposed) gives literal checks their own admission envelope: "Neither component comes from the enclosing execution." The partial first build implements natural literals (D39 and the second segment of D1858, built); other literal forms are outside this page. D1866, D1927 and D1956 apply as on the top entry's page.

## Common trial record

**PROPOSED.** A start fixes the program and input handle offered for admission, the entry definition, build, descriptors, export and its limits, scope, initial balances, prior state, schedule and linked observer. A *witness* is evidence captured where an event actually reaches a phase. Units in a pair are ordered (work, construction). Each event of the three kinds on these pages, top entry, literal read and local read, ends in one of two phases: WorkCheck, where its quote is refused for work, or Commit. None has a size pass, and its construction test holds by the price row.

Validate the start before the top entry: resolve the export's limits and admit the program and the input handle. Bind the input to its immutable reference and validated metadata, each literal occurrence to its pooled node and each local occurrence to its resolved parameter. Intern admitted natural values by content. Retain the source binding of each read in its private witness. After resolution a display name never identifies a parameter. A configuration or admission refusal prevents entry and is reported before the run. It supplies no reached-event witness, allowance cut, return or event projection.

Bind each private witness to the admitted start, descriptors, actual event (definition, site, visit and kind), the source binding of a read (the literal occurrence and its pooled node, or the resolved parameter and the input reference bound to it), the scope supplying the grant, the observer and the schedule. Retain the pre-attempt balances, reached phase, requested pair, deficits on refusal, limiting scope, live and released holds, debit, settled remainder, result or stop, committed pair, request/trail prefix and held account. The witnesses of one run are ordered as their events occurred. These three transitions emit no semantic request or trail item and add no holding. A successful transition retains its mandatory commit record as recoverable evidence. A checked reference may stand for a field if the checker can recover it at this start. A zero event debit means there was no commit.

The run account's committed pair is the componentwise sum of its committed debits, (0,0) for an empty account. With no outstanding hold, initial = committed + remaining for that account. The first unpaid event ends the evaluation, and earlier commits stand. A start that schedules no host interruption does not exercise the host-stop record.

**PROPOSED · observers.** Run the ordinary and the linked trial-exact observer separately at export `b`. Ordinary buys the returned value or the visible primary stop in its proper position, the public actions and the later-readable state. At this boundary the latter two are empty. Trial-exact adds **only** the debit of the selected event and the available pair after that event's commit or after the run's stop cleanup. The selected event is the event at the start's selected site and visit. If that event commits nothing, because it is refused or never reached, its debit in this projection is (0,0). The entry debit, phases, requested pairs, deficits, first unpaid site, source bindings, holds, latest debit and committed pair are not additional purchases. A pre-run refusal has no projection under either observer. Compare projected records only at the same start, grant, schedule and observer. The inclusion obligation applies to actual records; independently establish that each reached event emitted evidence.

**Evidence origin.** Capture each private record at its reached transition before projecting it. Bind every value, header or payload access, when present, to its reference and phase through the implementation's access boundary. PROPOSED: the quotes on these pages are constants, so a refused event needs no value, and a reference model reads none at the quote; D1954 moves any value-dependent quote work to a charged stage. Keep entry point and capture provenance separately. A self-reported no-read flag or agreement on a public result alone cannot establish private access behavior. Missing or inconsistent bindings fail validation.

**SOURCE · governing DESIGN SHA-256** `6439d9cfb70cfb02457ba06a90cfea999b7535bf9ae063cd131bd18c2fa8870a`. The following excerpts retain their local standing.

> D1846 · For $v, w$ not sequences, $\mathrm{node}(v) = \mathrm{node}(w) \iff v = w$ in content (interning)

> D1848 · These abstract rules leave $c_{\mathsf{var}}$, $c_{\mathsf{lit}}$, $c_{\mathsf{tup}}$ and $c_{\mathsf{con}}$ to the applicable table. An unspecified charge cannot be read as zero.

> D1852 · `\frac{k \ge c_{\mathsf{lit}}}{\eta \vdash v \Downarrow^{k \to k - c_{\mathsf{lit}}} v}\ \textsf{(P-Val)}`

> D1864 · Under the stated meter profile the result is $\mathsf{oof}$ when a premise gives $\mathsf{oof}$ or the fuel left is below the charge of the event reached: a variable, a literal, a tuple, a case, a call or a loop turn.

> D1866 · Insufficient allowance or the profile-defined inability to establish its safe advance bound produces the cut of §15.9 before construction, with both balances at the attempted event unchanged.

> D1898 · Reaching a literal *in* execution is charged.

> D1946 · A variable, admitted literal, returned reference, memo hit, selected tuple field or already admitted constant such as the bare wrong-kind answer selects a value at $c=0$.

> D1948 · The starting pool is identified before execution. It includes admitted input, program literals, built-ins, declaration descriptors and any named initial store.

> D1962 · | Top entry, local read, literal read, ordinary call after its argument, or completed eligible memo hit | $1$ per indicated event. Body entry is not charged a second time for the same call. | $0$ |

> D1972 · Reads and wrong-kind returns select admitted values at zero construction.
