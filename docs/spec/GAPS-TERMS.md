# Terms and theories gaps, revision 2, part 1

INFERENCE — Twelve gaps, TG-001 to TG-012. Each is a place where R13 does not say what a rule of `RULES-TERMS.md` would need. Each gives a case and two candidate outcomes with what each would cost. **None is owner-confirmed.** PROPOSED — TG-011 carries the provisional I-A restriction only, remains OPEN, and changes none of the other gaps. [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A] TG-001 to TG-006 are the gaps found in five short passages. TG-007 to TG-012 register six design choices that Codex G's ruling on an outside critique found to need a decision (its H2 and H4 to H8); each gives Codex G's statement of the choice word for word. Twelve is a count of what has been found. It is not a claim that there are no others.

SOURCE — R13 is `DESIGN-TEXT-R13.md`, SHA-256 `20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce`. Lines are physical lines of that file.

SOURCE — Two of these are questions already sent to Claude Arch: QA-13 and QA-25 of `QUESTIONS-ARCH.md` in the package `2026-11-12-CLAUDE-ENG-SPEC-CATCH-UP-PLAN`. Claude Arch's replies go in a file named `QA-REPLIES.md`. The entry for each question there, once reviewed, is what closes its gap. Until then no rule may depend on either outcome.

## TG-001 — Indexed sorts in slice 1, and how two index terms are compared (QA-13)

- anchor: R13 D-TH-2 (line 93); R13 D-ADM-4 (line 553); R13 D-SL-1 (line 837).
- what R13 has: "A sort may be indexed by terms, as in a vector of length n." And at D-ADM-4: an argument checked at a sort T is a member of the parameter's sort S "after substitution of indices"; "Where T and S are the same node the claim is yes".
- what is not stated: Whether slice 1 admits a sort with an index at all. And, where it does, whether an index term is run before two sorts are compared, or compared as written.
- touches: TERM-003.
- case 1: A slice 1 program declares the sort `vector` with a length.
  - outcome A: The declaration is admitted in slice 1.
  - outcome B: The declaration is refused in slice 1 as a form not supported in this slice (D-PATH-4 names that kind of refusal).
  - cost of A: Slice 1's admission must compare index terms, so case 2 must be answered before slice 1 is built.
  - cost of B: Slice 1 programs cannot state a length in a sort. The literal case of D-ADM-3, "a vector of length 4", cannot be written in slice 1.
- case 2: An operation takes a `vector` of length `4`. Its argument was checked at `vector` of length `2 + 2`.
  - outcome A: Index terms are compared as written. `2 + 2` and `4` are different nodes. The membership is unknown. With no test it is a refusal.
  - outcome B: Index terms are run first. Both give 4, the sorts are the same node, and the membership is yes.
  - cost of A: Right programs are refused until the writer puts the index in one written form.
  - cost of B: Admission runs terms. Each run needs fuel and an allowance, and an index term that does not end must have an outcome.
- closes when: `QA-REPLIES.md` has a reviewed entry for QA-13.

## TG-002 — What a theory's id is (QA-25)

- anchor: R13 D-REC-3 (line 1069); R13 D-REC-1 (line 1057), `Theory = { id, symbols }`; R13 D-TH-1 (line 91).
- what R13 has: "The id of a declared symbol is, as a default, its theory's id with its position in the theory, and names are metadata. Open: identity across versions of a theory."
- what is not stated: What the theory's own id is made from.
- touches: TERM-001, and every rule that names a declared symbol.
- case: Two files each declare a theory with the same sorts, operations, laws and rules, in the same order. One file calls it `counters` and the other `tallies`.
  - outcome A: A theory's id is a hash of its declarations. The two files give one theory, and their symbols are the same symbols.
  - outcome B: A theory's id is assigned when the theory is declared and is not made from its content. The two files give two theories, and no symbol of one is a symbol of the other.
  - cost of A: A symbol's id holds its theory's id, and the theory's id would hash its symbols. The hash needs a rule that breaks that circle, as D-REC-4 does for a group of defined symbols by writing each member as its position. Two writers who mean different things by equal declarations get one theory.
  - cost of B: Identity rests on something outside content. It must be said what that is, so that it does not become a display name, which R13 says is metadata. Equal theories written twice stay apart, and every claim about one must be made again for the other.
- closes when: `QA-REPLIES.md` has a reviewed entry for QA-25.

## TG-003 — A third multiplicity, none

- anchor: R13 D-TH-3 (line 95), fourth sentence; R13 D-UO-15 (line 168).
- what R13 has: "Whether a third value, none, for a parameter that is never called, is added goes to test." Tag: `R29 section 4 | approved, to test`. The test is named at D-UO-15: the census of the use-once check against what a run consumes, "with none added as a multiplicity", passing when no wrong term is accepted and with a count of the refused right terms it recovers.
- what is not stated: Whether none is to be added. R13 sends the question to the D-UO-15 census and supplies no settling result for it here.
- touches: TERM-007.
- case: An operation takes a bound argument and never calls it. A use-once value is used once elsewhere and is also handed to that argument. D-UO-15 names this term as "refused though right" today.
  - outcome A: Multiplicity stays one or any. The term stays refused.
  - outcome B: none is added. The signature may declare the argument as never called, and the term is accepted.
  - cost of A: Some right terms stay refused. Nothing changes in the record or the check.
  - cost of B: The record line `one | any` gains a value, the use-once check gains a case, and every signature reader must handle it. It is safe only if the census shows no wrong term accepted.
- closes when: the census of D-UO-15 is run and reviewed, and the design text takes its result.

## TG-004 — Omitted source spelling of a bound argument's multiplicity

- anchor: R13 D-TH-3 (line 95); D-REC-1 (line 1053); D-REC-3 (line 1069); D-SYN-1 (line 319); D-UO-3 (line 128); D-UO-5 (line 133).
- what R13 has: A bound argument carries one or any, declared in its operation's signature. The Parameter record carries that multiplicity. D-SYN-1 leaves the surface syntax unsettled.
- what is not stated: Whether source may omit a bound parameter's multiplicity spelling and elaborate to an explicit value in the operation's signature. R13 does not leave a missing semantic multiplicity as an alternative.
- touches: TERM-005.
- case: A source declaration of each has one bound argument and writes no multiplicity. Its elaborated bound parameter must still carry one or any.
  - outcome A: The source declaration is refused for omitting the spelling.
  - outcome B: The source declaration is admitted by inserting an explicit default before checking. Which default is used remains unchosen here.
  - cost of A: Every such source signature must spell the multiplicity. The semantic signature still has the field R13 already requires.
  - cost of B: A default and its elaboration must be stated. At the declared-multiplicity boundary of D-UO-5, one permits passing a function that captures a use-once value and any does not; conversely, a rule may call an ordinary bound function repeatedly under any but not under the one contract. Neither default simply admits every call the other admits.
- closes when: the source spelling and its elaboration are stated in reviewed design text or a reviewed reply. This is a source-form question, not permission to omit the semantic field. It is new here and not among the 27 questions already sent.

## TG-005 — Whether constructors count among a theory's operation members

- anchor: R13 D-TH-1 (line 91); D-TH-6 (line 102); D-TH-7 (line 104); D-REC-1 (lines 1046 to 1057); D-IN-1 (line 202); the Tasks theory (lines 616 to 623).
- what R13 has: A theory's vocabulary has sorts, operations, laws and rules. An effect is an operation. Symbol has declared, defined and evaluated alternatives, and Theory has symbols. The Tasks theory expressly contains declarations and definitions. A defined symbol need not have a reverse theory field for a theory to contain it.
- what is not stated: Whether a constructor counts among the operation members of a theory or is a distinct component of its data-sort declaration. D-IN-1 names constructors, operations and effects separately; D-TH-6 expressly makes effects operations, but no corresponding constructor classification is stated.
- touches: TERM-001.
- case: A theory declares the data sort Box with the sole constructor pack and no other operations. Someone asks how many operation members that theory has.
  - outcome A: pack counts as an operation member, so the answer is one.
  - outcome B: pack is a constructor component of the data-sort declaration, with its own declared constructor symbol but no extra operation member, so the answer is zero.
  - cost of A: Questions ranging over a theory's operation members must include constructors.
  - cost of B: The distinction between operation members and constructor components must be stated so the theory's vocabulary and its symbols can be read together.
- closes when: reviewed design text states the classification. Neither candidate is selected here; this gap prescribes no new record field and does not deny that a theory can contain definitions and rules.

## TG-006 — The symbol and signature of slice 1's one output operation

- anchor: R13 D-TH-6 (line 102); R13 D-ROW-9 (line 230); R13 D-SL-1 (line 837).
- what R13 has: An effect is an operation whose last argument is a bound continuation. Slice 1's bound "permits one output operation reached through Ask". And: "GAP 6 remains for the output operation's exact symbol and signature".
- what is not stated: Which effect slice 1's output operation is: its symbol, its parameters, and the multiplicity of its continuation.
- touches: TERM-009.
- case: A slice 1 program puts out one value and goes on.
  - outcome A: The output operation is declared like any effect, with a value parameter and a continuation of multiplicity one.
  - outcome B: Its signature differs: for example it returns the host's reply to the continuation as a value of a declared sort.
  - cost of A: Nothing new is needed in the terms rules. The host's reply carries no value.
  - cost of B: The reply's sort and its admission (D-RUN-8) become part of the signature, and the run rules and row rules must agree with it.
- closes when: R13's GAP 6 is filled. The draft run rules record related Ask matters as their gaps RG-006 and RG-007. It is recorded here only because TERM-009's case names an output effect.

## TG-007 — Where an effect may stand once the reader has made continuations (Codex G's H2)

- anchor: R13 D-TH-6 (line 102); R13 D-STG-1 (line 533); R13 D-ROW-9 (line 230).
- what R13 has: "Text that has an effect inside an argument is turned into continuations, left to right." That is the reader's work, at stage 1.
- what is not stated: What must hold of a term after the reader: whether an effect may stand inside a helper definition that is called from an argument place, or only where nothing else follows it.
- touches: TERM-010.
- case: A helper definition performs `out`. Another operation takes a call of that helper as an argument.
  - outcome A: The helper may perform effects. Their order is fixed by stated rules of normal form, and the row and order duties follow the helper.
  - outcome B: A stricter boundary holds: an effect stands only at the tail, and a helper called from an argument place is free of effects.
  - cost of A: Explicit rules for the normal form and for tracking the helper's effects.
  - cost of B: A design amendment, and limits or changed interfaces for helpers.
- choice as Codex G states it: Claude Arch should specify the post-reader placement invariant: effectful helper definitions under row/order obligations cost explicit normalization and tracking rules; a stricter tail/purity boundary costs a design amendment and restrictions or interface changes for helpers. Neither new policy is selected.
- closes when: Claude Arch's answer is reviewed and the design text takes it. Open; routed by Claude A. Neither outcome is selected here.

## TG-008 — How a theory uses what another theory declares (Codex G's H4)

- anchor: R13 D-TH-1 (line 91); R13 D-REC-3 (line 1069).
- what R13 has: A theory is a vocabulary of sorts, operations, laws and rules. A declared symbol's id is its theory's id with its position.
- what is not stated: How a theory refers to a symbol it does not declare, and whether such a reference makes that symbol a member, visible, or neither.
- touches: TERM-001.
- case: A theory of counters has the rule `next(n) = n + 1`. The symbols `+` and `1` are declared in a theory of numbers.
  - outcome A: A theory carries explicit records of what it imports and what it shows.
  - outcome B: A theory refers directly to identified symbols of the store, with no import record.
  - cost of A: Rules for dependency and for identity across the import.
  - cost of B: Rules for whether a referred symbol is available, where it came from, and how a reference is resolved.
- choice as Codex G states it: Claude Arch should choose explicit imports/visibility records, costing dependency and identity rules, or direct references to identified store symbols, costing availability/provenance and resolution rules; neither answer automatically makes every reference a member.
- closes when: Claude Arch's answer is reviewed and the design text takes it. Open; routed by Claude A. Neither outcome is selected here.

## TG-009 — How an interpretation that is not a rule keeps a continuation's multiplicity (Codex G's H5)

- anchor: R13 D-TH-6 (line 102); R13 D-REC-1 (line 1059); R13 D-RUN-8 (line 598).
- what R13 has: The multiplicity of an effect's continuation is owed by every interpretation of the effect. A handler is a rule, and the use-once check counts the continuation in it. An effect may also be answered by an image under an interpretation, or passed to the host.
- what is not stated: How an image that is not a rule, or the host, is shown to keep the multiplicity, and how its handler and state are written down so that this can be checked.
- touches: TERM-011, TERM-012.
- case: Slice 1's host answers the output effect. Its answer is not a rule of any theory in the term.
  - outcome A: Images and hosts carry obligations stated as terms or rules that a checker can check.
  - outcome B: The host stands behind a contract of its own, with separate evidence that it keeps the multiplicity.
  - cost of A: Explicit encodings and checks for images and hosts.
  - cost of B: A stated trusted obligation, and an account of it in the row.
- choice as Codex G states it: Claude Arch and record/specification work should choose checkable term/rule obligations for images and hosts, costing explicit encodings and checks, or a separately evidenced primitive contract boundary, costing a stated trusted obligation and account; preserve universal multiplicity under either answer.
- closes when: Claude Arch's answer is reviewed and the design text and record rules take it. Open; routed by Claude A. Neither outcome is selected here. The obligation of TERM-011 holds under either.

## TG-010 — What multiplicity one requires where a run does not end, and through higher-order binding (Codex G's H6)

- anchor: R13 D-TH-3 (line 95); R13 D-UO-3 (line 128); R13 D-UO-15 (line 168); R13 D-PATH-4 (line 701).
- what R13 has: A multiplicity says how many times the operation calls its bound argument. The use-once check counts sites and positions, which is a safe test and not the meaning. The census of D-UO-15 is the named test.
- what is not stated: What "one" requires of a run that stops, fails or does not end before the call, and how it is kept when a bound argument is handed on to another operation.
- touches: TERM-006.
- case: An operation declares its bound argument with multiplicity one. A run of the operation does not end, and the argument is never called.
  - outcome A: One is a duty of safety and ownership: the argument is called at most once, and is owed until the run ends or hands it on.
  - outcome B: One is a stronger condition: the call must come to pass.
  - cost of A: An account of what is still owed when a run stops.
  - cost of B: Limits on programs, and proof duties wherever a run may not end.
- choice as Codex G states it: Claude Arch should state how one is retained across divergence and higher-order binding: a safety/ownership obligation until termination or handoff costs a residual-obligation account; a stronger completion condition costs restrictions and proof obligations for divergence. The existing site/position check and open none experiment remain intact.
- closes when: Claude Arch's answer is reviewed and the design text takes it. Open; routed by Claude A. Neither outcome is selected here. The site and position check, and gap TG-003, stand as they are.

## TG-011 — What an index term may be (Codex G's H7)

- anchor: R13 D-TH-2 (line 93); R13 D-REC-1 (line 1050); R13 D-ADM-4 (line 553).
- what R13 has: A sort may be indexed by terms. A sort's signature gives the sorts of its indices.
- what is not stated: Whether an index term may perform an effect, consume a use-once value, or depend on another argument.
- touches: TERM-003.
- provisional answer (PROPOSED; not owner-confirmed): A plain index only: it may depend on earlier arguments, has no effect or open choice, makes and consumes no use-once value or sequence, and gives a result that may be copied. [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A]
- case: A sort is indexed by a term that reads a use-once value, or by a term that performs an effect. PROPOSED — This compares the historical alternatives; the marked I-A requirement and its deciding effectful-index case are TERM-003, pending owner confirmation. [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A]
  - outcome A: Such index terms are permitted.
  - outcome B: Such index terms are refused.
  - cost of A: Rules for the fuel that admission spends on them, for their scope, and for who owns what they consume.
  - cost of B: Stated limits, and programs that are refused.
- choice as Codex G states it: Claude Arch should permit effectful/use-once or dependent index terms, costing admission fuel, scope and ownership rules, or restrict them, costing explicit restrictions and rejected programs; TG-001 stays open and neither policy is selected. PROPOSED — The unselected wording here records Codex G's historical alternatives; the I-A answer above is provisional only and this gap remains OPEN. [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A]
- closes when: Claude Arch's answer is reviewed, the owner confirms it and the design text takes it. OPEN; routed by Claude A. PROPOSED — I-A is provisional only; timing, fuel and repeated reads of an index still need rules under either answer. TG-001 stays open. [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A]

## TG-012 — The order of a theory's declarations, and two declarations with one name (Codex G's H8)

- anchor: R13 D-REC-3 (line 1069).
- what R13 has: "The id of a declared symbol is, as a default, its theory's id with its position in the theory, and names are metadata."
- what is not stated: Which order fixes a declaration's position, what happens when two declarations carry one name, and whether a position is stable from one version of a theory to the next.
- touches: TERM-001.
- case: Two writers set down the same declarations of one theory in different orders. Or one theory holds two declarations with the same name.
  - outcome A: A canonical order is fixed, with a rule for two declarations of one name.
  - outcome B: The order supplied is kept, and names stay metadata.
  - cost of A: Rules for the order, for the codec, and for the ambiguous case.
  - cost of B: Every reference must be bound explicitly, and no promise is made that a name or a position is stable across versions.
- choice as Codex G states it: Claude Arch should fix canonical ordering and duplicate-name resolution, costing ordering/codec and ambiguity rules, or retain supplied order and metadata names, costing explicit reference bindings and no name/version-stability promise; do not change the existing position-based default silently.
- closes when: Claude Arch's answer is reviewed and the design text takes it. Open; routed by Claude A. Neither outcome is selected here. It stands beside TG-002. The position-based default is not changed.

END OF GAPS-TERMS
