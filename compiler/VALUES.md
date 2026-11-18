# Milestone B immutable values (piece 11)

**SOURCE.** B admits uncapped naturals, finite immutable tuples and the ordinary
builtin result `option.none`. The owner renamed the fixed-position value
called “row” in the original passages to **tuple**. B supplies no general case
constructor, bytes, set or sequence. A tuple can hold any admitted value,
including another tuple or builtin none. [Forms B-F01, B-F02, B-F05 and B-F07](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-D-MILESTONE-B-FORMS-R1/FORMS.md:8)
[Design D-VAL-1 and D-VAL-2](../docs/design/DESIGN-TEXT-R17.md#values-choices-and-sets)
[Owner terminology decision](C:/Users/grego/.codex/reviews/_relay/inputs/owner-record-2026-11-17-row-renamed-manifest-tuple.json)

| B value | Content and invariants | Basis |
|---|---|---|
| Natural | The mathematical nonnegative integer. Zero has one content. Sharing, leading zeroes in development input, and limb allocation do not distinguish equal numbers. | B-F02 and the [committed natural interface](src/natural.mli) |
| Tuple | A fixed width `k >= 0` and exactly `k` values in written order. Positions start at 0. Repeated positions count separately. Width, order and each field's content participate in equality. The empty tuple is valid. | D-VAL-1, D-VAL-4, B-F02, B-F05, [B-O04](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-D-MILESTONE-B-FORMS-R1/OUTCOMES.md:67) |
| Builtin none | The one ordinary case `option.none` (choice `option`, case 0, fixed empty-tuple payload). It differs from natural zero and from the empty tuple. It may be returned or stored in a tuple. B has no source literal for it. | D-VAL-2, D-VAL-6, B-F02, B-F03, [B-C06](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-D-MILESTONE-B-FORMS-R1/CHARGES.md:62) and B-O02/B-O04 |

**SOURCE.** Reading a position outside a tuple gives the bare builtin none.
Reading an in-range field containing none gives that same ordinary value. The
width distinguishes those situations. An obtained wrong-kind operand of
`add`, `sub` or `mul` produces the existing none after the edge invoice is
paid. Wrong arity is refused before evaluation. Running out of fuel yields a
separate outcome. [D-VAL-6, including the option payload](C:/LoomLang/docs/design/DESIGN-TEXT-R17.md:1062)
[B-F05](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-D-MILESTONE-B-FORMS-R1/FORMS.md:45)
[B-O02](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-D-MILESTONE-B-FORMS-R1/OUTCOMES.md:23)

**SOURCE.** Equal admitted immutable values share a node. Each written
occurrence is still evaluated and charged. The B forms provide no observation
of allocation, address, interner membership or construction history. A later
development report assigns its own first-encounter IDs and preserves sharing
and field order. [D-EV-1/D-EV-2](C:/LoomLang/docs/design/DESIGN-TEXT-R17.md:1001)
[B-F02 and B-F06](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-D-MILESTONE-B-FORMS-R1/FORMS.md:54)
[B-O04](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-D-MILESTONE-B-FORMS-R1/OUTCOMES.md:69)

**PROPOSED implementation.** Each invocation creates a `Value.Make ()` store.
Its abstract scope makes tuple children belong to that store. A store retains
one node per distinct content during its lifetime. An interned tuple owns its
field array. Mutating the caller's array after construction cannot change a
value, and positional access exports only immutable children. A node needs no
pointer back to the store. A host-only inventory count lets a test measure
reuse. B code cannot read it. Host array, memory and string capacity are
implementation resources. [Milestone plan, value boundary and piece 11](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-A-FIRST-MILESTONE-PLAN-OCAML/PLAN.md:106)

**PROPOSED equality.** `Value.equal` is the one content-equality function.
Both direct comparisons and interner candidate comparisons use it. It works
on values constructed in different stores. Naturals compare through
`Natural.compare`, none equals none, and tuples compare corresponding fields
after width. Distinct kinds differ. A cached content hash may reject a
mismatch. A hash match always requires a content check. An explicit worklist
and a set of visited pairs of store-local node numbers avoid recursive host
stack growth and repeated expansion of shared subgraphs. A pair is meaningful
only within that traversal, with one store per side. Equal numbers in separate
stores prove nothing about the values. [D-VAL-1/D-VAL-4](C:/LoomLang/docs/design/DESIGN-TEXT-R17.md:1046)
[Owner decision on a single equality route](C:/Users/grego/.codex/reviews/_relay/inputs/owner-record-2026-11-17-sequences-room-on-paper-new-reopen-test.json)

**PROPOSED local encoding and hash (B-value-v1).** These are private
development conventions. The canonical wire format, evaluator hash primitive
and run-record format remain with their designated work. One local frame is
an ASCII header including its LF and its ordered child values. Headers and
child encodings in preorder determine the complete logical bytes. The API
emits and reads one frame at a time so interning a shared child never flattens
its subtree. Header numerals use canonical unsigned decimal with one zero for
zero. The decoder checks the complete header and the supplied child count.
This development input is distinct from the B source grammar. [Plan, deferred codecs](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-A-FIRST-MILESTONE-PLAN-OCAML/PLAN.md:90)
[B-O04, development display](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-D-MILESTONE-B-FORMS-R1/OUTCOMES.md:75)

| First byte | Local frame | Children |
|---|---|---|
| `N` | `N`, canonical natural digits, LF | Zero |
| `T` | `T`, canonical width digits, LF | Exactly that many, in position order |
| `O` | `O`, LF | Zero supplied. The fixed empty payload is implicit. |
| `S` | **Reserved_sequence** | Its encoding, hash branch and equality rule are reserved. Any frame beginning with this byte is refused before lookup or construction. |

For example, the logical bytes of `tuple[0,none]` are `T2\nN0\nO\n`.
Hash each node over its header bytes followed, for a tuple, by each child's
cached hash as four unsigned little-endian bytes. Start at 0, updating
`h = (257*h + byte + 1) mod 1_000_000_007`. The intermediate is below
`2^38` on the required 63-bit OCaml host. Store-local numbers never enter the
encoding or the hash. Different values can collide. For example the natural
headers for `5737421554731` and `4399495151043` both hash to `457519830`.
New use of `S` would leave all existing tags, bytes and hash inputs intact.
The owner left the sequence design on paper, including its future starting
state and make/write record. B has no sequence value constructor, allocation,
mutation, or alternate frame layout. [Owner reservation](C:/Users/grego/.codex/reviews/_relay/inputs/owner-record-2026-11-17-sequences-room-on-paper-new-reopen-test.json)
[Sketch cost account](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-A-TWO-SKETCHES-R2/COST-ACCOUNT.md:74)

**SOURCE of the proposed piece 13 tariffs.** The reviewed charge sheet uses
`part(n) = max(1, bit_length(n))` and `part(tuple) = part(none) = 1`.
Its exact proposed invoice is `A + R + T + W`. The evaluator must pay the
whole invoice before canonical lookup and construction, including a reuse
hit. A failed debit leaves that operation's result unbuilt. [D-EV-1](C:/LoomLang/docs/design/DESIGN-TEXT-R17.md:1023)
[Charge sheet B-C01–B-C08](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-D-MILESTONE-B-FORMS-R1/CHARGES.md:11)

| Event | Piece 13's proposed charge |
|---|---|
| Admit a source literal or input | Intern before execution, outside execution fuel (B-C03). |
| Yield a natural literal or read a local value | One before yield. Entry and a named call each cost one at their specified points. Return adds zero (B-C04). |
| Make a tuple from obtained fields | `A=sum(part(field_i)), R=k+1, T=W=0`. Field evaluation is paid left to right beforehand. Empty costs 1. With obtained 4 and 7 the invoice is 9 (B-C07). |
| Make a natural arithmetic result | For operand sizes `a,b` and `m=max(a,b)`, pay `(A,R,T,W)` equal to `(a+b,m+1,0,m)` for add, `(a+b,a,0,m)` for sub, or `(a+b,a+b,0,a*b)` for mul (B-C05). |
| Give the existing none on wrong-kind arithmetic | `A=part(x)+part(y), R=T=0, W=1` (B-C06). |
| Compare content during lookup or inspect a tuple field from host code | Canonical lookup is covered by the enclosing paid reservation, or by unmetered admission/report work. B has no source-level equality or positional-get operation and the sheet assigns neither a standalone invoice. Host access and equality here add no new meter event (B-F05/B-F07, B-C03/B-C11). |

**PROPOSED integration.** The reader can intern literals and inputs in one
store. The meter can inspect the kind, the exact natural and the tuple width
before constructing a result. Frames can hold immutable children and pass one
explicit machine state through their transition function. Piece 15 can return
the store's builtin none on a paid wrong-kind edge. These are consumers of
piece 11. [Plan, pieces 11–15](C:/Users/grego/.codex/reviews/2026-11-17-CODEX-A-FIRST-MILESTONE-PLAN-OCAML/PLAN.md:197)
[Arch, section 4](C:/Users/grego/.codex/reviews/2026-11-17-CLAUDE-ARCH-TWO-SKETCHES-REVIEW/REVIEW.md:63)
