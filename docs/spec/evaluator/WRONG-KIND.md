# Binary arithmetic on an admitted wrong kind

**PROPOSED · common edge of add, truncated subtract and multiply.** A *kind* is the admitted value form used to select the operation’s row. This paired descriptor prices only obtained naturals, obtained tuples and the built-in `option.none` for this dispatch. An applicable wrong-kind arithmetic event has at least one non-natural among those forms. Preserve both argument positions and bind the particular arithmetic operation. Two admitted naturals take that operation’s natural row. An unsupported descriptor/input combination is refused before execution; it cannot masquerade as an admitted wrong kind.

## Price and phases

For each of the two obtained operands read its validated kind header. Its argument contribution h is its canonical binary width if natural (zero has width one), or one for a tuple or built-in none. This quote does not traverse tuple fields or read natural digits. In profile `b1-pair` the row requests

    w = h(left)+h(right)+1,    c = 0.

The bare none is the already admitted option.none holding the empty tuple. Selecting it constructs neither a tuple, a case nor a natural. The zero here is a construction invoice; the returned value is a case.

1. If W<w at the root, stop for work with request (w,0), work deficit w−W and known construction deficit zero. The same pre-attempt balances remain after the refusal. No hold, size scan, payload access, new result, debit or prefix entry. Construction demand is known from selection of the row. No natural-product width check or bound natural-result expression belongs to this edge.
2. If W≥w, c=0 is affordable for any admitted C. Reserve (w,0) before publication, select the existing none, and commit its reference, record and the work debit together. Settle to (W−w,C). This path never runs the natural arithmetic operation or its digit-sizing/emission passes. It requires no construction credit for obtaining the answer. On both paths keep a bounded evidence record with the selected operation, ordered kind/contribution references and actual access/phase evidence.

**Resource account.** The quote needs at most two validated contributions and a fixed number of bounded additions/comparisons. For L≥1 the maximum bit length of the contributions and grants, L+2 bits suffice per quote integer. The row uses one selected reference and bounded terminal metadata. Header and witness validation is part of the profile’s separate bookkeeping bound. An implementation measuring physical storage must include its actual representations and capacities.

**SOURCE · standing.** D1958 and D1965 give the proposed priced forms and invoice; D1946 and D2054–56 distinguish selecting the existing result from constructing a value. D2052 decides the wrong-kind none, and the scalar driver implements it for these three operations. D1925–29, D1952–56 and D643–58 govern the account, check order, atomic publication and linked observation. The scalar driver’s work charge and this paired experiment are separate profiles.

**PROPOSED · common trial record.** A start fixes the admitted inputs, selected operation, program, definition, occurrence, visit, build, descriptors, scope, initial balances, prior state, schedule and linked observer. A *witness* is evidence captured where that operation actually reaches a phase. A *hold* reserves credit privately. A *commit* publishes the result, paired debit and mandatory record atomically. Units in a pair are ordered (work, construction).

Validate the start before attempting a primitive. Bind each ordered operand slot to its immutable reference and its admitted kind and size metadata. Reference identity and interned content identity serve different purposes. Two admitted references may resolve to one natural node; one reference may also occupy both argument positions. The printed value alone cannot decide which relation the start specifies. Keep the selected operation as well as the site in the binding. An unadmitted operand prevents entry and gives a pre-run refusal in the admission report. It supplies no reached-event witness, allowance cut, primitive return or event projection.

Bind each private witness to the admitted start, descriptors, actual event, ordered reference/header pairs, scope supplying the grant, observer and schedule. Retain the pre-attempt balances, reached phase, quoted requests or certified evidence, deficits on refusal, limiting scope, live and released holds, debit, settled remainder, outcome, cumulative committed pair, request/trail prefix and held account. Keep enough origin evidence to check which headers and payloads were accessed at which phase. A checked reference may stand for a field if the checker can recover it at this start. The work quote may use validated headers and opaque identities without dereferencing payloads. A zero event debit on refusal means there was no commit.

The run account’s committed pair is the componentwise sum of its committed debits, zero for an empty account. With no outstanding hold, initial = committed + remaining for that account. A controlled physical stop is a distinct kind with actual cause, phase, committed pair, any outstanding reservation, prefix and holdings; if there was a committed event its latest debit is recoverable. Discard unpublished staging and release a precommit hold. A later interruption after commit preserves the paid event. A request/trail prefix need not enumerate every debit.

**Observers.** Run the ordinary and linked trial-exact observer separately at export `b`. Ordinary buys the returned value or visible primary stop in its proper position (including the cause for a scheduled controlled physical stop), public actions and later-readable state. At this boundary the latter two are empty. Trial-exact adds **only** the selected event debit and the available pair after commit or stop cleanup. The private invoice, phase, ordered bindings, deficit image, symbolic expression, transient hold, latest debit and cumulative pair are not additional purchases. Compare projected records only at the same start, grant, schedule and observer. The inclusion obligation applies to actual records; independently establish that the selected occurrence emitted evidence.

**Evidence origin.** Capture the private record at the reached transition before projecting it. Bind actual payload reads, when present, to the ordered references and phase through the implementation’s access boundary. Keep entry point and capture provenance separately. A self-reported no-read flag or agreement on a public result alone cannot establish private access behavior. Missing or inconsistent bindings fail validation.

**SOURCE · governing DESIGN SHA-256** `6439d9cfb70cfb02457ba06a90cfea999b7535bf9ae063cd131bd18c2fa8870a`. The following excerpts retain their local standing.

> D1958 · For the argument contribution of an obtained tuple or the built-in none use one.

> D1965 · | Binary arithmetic on a wrong kind | sum of argument contributions plus $1$ | $0$, returning the admitted none |

> D2052 · | A primitive given a value of the wrong kind | `none` | `[decided]` The driver implements this case for `add`, `sub` and `mul`. `[built: milestone B, partial]` |

> D2056 · For the paired schedule an edge that selects the already admitted none pays the specified argument and work charge and has zero construction.
