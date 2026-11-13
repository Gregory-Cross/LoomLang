# PROPOSED store gaps, revision 2

INFERENCE - Nine proposed gap entries, SG-001 to SG-009, against the pinned R1 inventory. SG-001 to SG-006 retain their source-qualified scope; SG-007 and SG-008 record newly identified interface boundaries; SG-009 remains OPEN with only the marked provisional TM-A answer, held for owner confirmation; no final outcome is selected. [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A] This count describes the inspected scope, not completeness of the language.

SOURCE — R13 is `DESIGN-TEXT-R13.md`, SHA-256 `20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce`. Lines are physical lines of that file.

SOURCE — Two of these are questions already sent to Claude Arch: QA-26 and QA-16 of `QUESTIONS-ARCH.md` in the package `2026-11-12-CLAUDE-ENG-SPEC-CATCH-UP-PLAN`. Claude Arch's replies go in a file named `QA-REPLIES.md`. The reviewed entry for a question there is what closes its gap. Until then no rule may depend on either outcome.

## SG-001 — The bytes that content identity hashes

- anchor: R13 D-STO-1 (line 500); R13 D-REC-4 (line 1071).
- what R13 has: "GAP 4: the bytes that content identity hashes are not given." D-REC-4 ends with the same mark, "GAP 4".
- what is not stated: Which bytes are hashed for a node, a symbol, a signature and a group of symbols, and with which function.
- touches: STO-001, STO-011, STO-012, STO-016, STO-019.
- recorded as: gap B03 of the record rules (`GAPS-RECORDS.md`) and gap E-16 of the evaluator rules (`GAPS-EVALUATOR.md`). The hash function's name is gap E-1; EV-013 holds only that both builds use the same one.
- closes when: the hash proposal is reviewed and the evaluator and record rules take it (plan card SC-04b). This file answers nothing about it.

## SG-002 — Whether slice 1's store has the cache of checks (QA-26)

- anchor: R13 D-STO-2 (line 502); R13 D-SL-0 (line 835); R13 D-SL-1 (line 837).
- what R13 has: D-STO-2 says how a check is cached and when it is reused. Its tag is `agreed, not run`. D-SL-1 names "The evaluator and the store" for slice 1 and does not name the cache. D-SL-0: "In slices 1 to 3 every claim is settled by a run."
- what is not stated: Whether the store that slice 1 builds has this cache.
- touches: STO-005, STO-006, STO-007.
- case: A slice 1 build checks the same membership claim twice, once for each of two programs that hold the same application.
  - outcome A: Slice 1 has the cache. The second check finds the first entry, sees that every question still has its answer, and reuses it.
  - outcome B: Slice 1 has no cache. The check runs again, and the cache arrives in a later slice.
  - cost of A: Slice 1 must record every question a check puts to the store, with the hash of each answer. That needs the hashed bytes (SG-001) before slice 1 can be built.
  - cost of B: Slice 1 repeats work. STO-005 to STO-007 then bind no slice 1 build, and the record of questions is first tested later.
- closes when: `QA-REPLIES.md` has a reviewed entry for QA-26.

## SG-003 — What the row query takes, and what it gives in slice 1 (QA-16)

- anchor: R13 D-STO-3 (lines 504 and 508); R13 D-ROW-1 (line 213); R13 D-SL-1 (line 837).
- what R13 has: The table's first row: "Row of a node", returning "The polynomial; its symbols; its reading under a bound". D-SL-1 speaks of "the root row".
- what is not stated: The concrete input and output records of the query, including how the context and admission facts are bound. The table already requires the polynomial, its symbols and its reading under a bound; those components are not open here. No absence of alternative routes in slice 1 is established.
- touches: STO-008.
- case: The same node holding a variable occurs with two supplied checking contexts and different admission facts. Ask for its row and an answer record that binds the applicable context. The following are two proposed interface arrangements, not selected record bytes.
  - outcome A: The API accepts a node only when its applicable context and admission facts are uniquely supplied through recorded dependencies. It returns the polynomial, symbols and bound reading with their dependency reference. In this case the bare node shared across two contexts is not a complete input: no row answer is licensed until its applicable dependency is bound. No context facts may be omitted.
  - outcome B: The query takes the node with explicit context and admission facts. It returns the same required components with their context and admission reference explicit in the answer record. Different contexts may produce different rows.
  - cost of A: The context and admission facts required by D-ROW-6 must be uniquely bound through another specified dependency. This option gives no permission to omit them from row computation or cache validity.
  - cost of B: The call, answer and any cached row must bind the explicit context. Its concrete record fields and encoding still need specification; this gap chooses none.
- closes when: `QA-REPLIES.md` has a reviewed entry for QA-16. The row rules, not this file, will then say what a row is.

## SG-004 — What a declaration's identity is made from, and identity across versions

- anchor: R13 D-TM-1 (line 172); R13 D-REC-3 (line 1069).
- what R13 has: "a declared symbol by its declaration". And: "The id of a declared symbol is, as a default, its theory's id with its position in the theory, and names are metadata. Open: identity across versions of a theory."
- what is not stated: What else an id may be, since the rule is "a default". And whether a symbol keeps its id when its theory gains a declaration before it, or is edited.
- touches: STO-013, STO-018.
- recorded as: for the versions part, gap L02 of the record rules (`GAPS-RECORDS.md`), "Declaration identity across theory versions". What a theory's id is itself is gap TG-002 of the terms rules. Neither is restated here.
- case: A theory has three declarations. A new one is put in before the third, which is otherwise untouched.
  - outcome A: Under a position-based identity policy, shifting the declaration changes its theory-id/position identity. Evidence about the old id does not by itself establish a claim about the new id. This does not delete the old symbol or its evidence from the store.
  - outcome B: A declaration may carry an id that does not move with its position. The default applies only where none is given.
  - cost of A: Evidence needed for the new identity must be transported or established under an applicable rule; no cross-version transport rule is chosen here. Old evidence remains about its old identity.
  - cost of B: Specify how a stable semantic id is allocated and retained, while keeping display names as metadata. This candidate chooses no such mechanism.
- closes when: the design text settles the open sentence, or the record rules' gap L02 is closed.

## SG-005 — What may add the other kinds of thing to the store

- anchor: R13 D-STO-1 (line 500), second and third sentences.
- what R13 has: The store holds eight kinds of thing. "Anything may add a term, a proposal or a note."
- what is not stated: What may add a theory, an interpretation, a representation, a claim, a piece of evidence or a built artefact. The third sentence names three kinds and is silent on the rest.
- touches: STO-003.
- case: A tool that is not trusted writes a run record into the store that says a program returned 4.
  - outcome A: The store accepts the object. If it is a valid run record, its evidence is relative to the build that actually ran it under EV-031 and EV-032. Acceptance alone neither authenticates the record nor licenses a claim.
  - outcome B: The store refuses it. Only a build of the evaluator, or a kernel program, may add evidence.
  - cost of A: Every reader of evidence must be safe against records that anything wrote. The safety rests on the reading rules alone.
  - cost of B: The store needs a rule for who may write which kind, and a way to know the writer.
- closes when: the design text says which. This gap is new here. It is not among the questions already sent to Claude Arch.

## SG-006 — Whether a check's context is part of the claim in the cache's key

- anchor: R13 D-STO-2 (line 502); R13 D-UO-10 (line 144).
- what R13 has: D-STO-2 keeps a check "under the checking program, the claim, and a record of every question it put to the store". D-UO-10: "A check of a node that holds variables is a check in a context, the sorts of those variables. A cache of such a check is keyed by the node and the context." Its tag is `fold`.
- what is not stated: How D-UO-10's already-required node-and-context distinction is represented within D-STO-2's program, claim and question record: whether the claim already contains the context or it is separately keyed. Context sensitivity is not open; this gap chooses no record shape.
- touches: STO-005.
- case: The same node, with one free variable, is checked for membership in two contexts that give the variable two different sorts.
  - outcome A: The claim holds its context (D-ADM-4 emits each membership claim "in the context of that application"). The two checks have two claims and so two entries, and D-STO-2's key is complete as written.
  - outcome B: The claim is about the node alone. The context is a fourth part of the key, as D-UO-10's words suggest.
  - cost of A: Nothing is added to the key. It rests on the claim record carrying its context, which the claim rules have not yet stated.
  - cost of B: The key has a part that D-STO-2 does not name, and D-STO-2's sentence is incomplete as written.
- closes when: the claim record is ruled (plan card SC-10) or the design text says which. This gap is new here.

## SG-007 - Store insertion, admission and update boundary (PROPOSED)

- anchor: R13 D-STO-1; STO-003. This entry records an undecided interface, not a new permission.
- not stated: Which object checks precede insertion of a term as data, and whether any logical replacement/removal API is provided. Permission for anything to add a term does not mean arbitrary bytes are a term.
- case A: A valid store-value encoding describes an object term that would fail its separate runnable-object admission, such as a wrong-arity application.
  - candidate A1: Store it as candidate data, with no claim that it is admitted to run; every consumer still owes its own admission/evidence prerequisites.
  - candidate A2: This insertion interface accepts only already-admitted object terms; any raw-candidate channel needs a separately stated contract.
  - costs: A1 needs a clear separation between presence as data and object admission. A2 needs that gate and a specified route for candidate data, without withdrawing STO-003's existing permission for valid terms/proposals/notes.
- case B: A writer asks to replace or remove a note reached by an existing cached query.
  - candidate B1: The logical interface provides addition, not logical deletion/replacement; physical reclamation cannot silently break promised references or answers.
  - candidate B2: A specified versioned update/removal operation exists, with its identity, history, cache-dependency and evidence effects explicitly defined.
  - costs: B1 needs retention/reclamation rules. B2 needs the update/version protocol and dependent-check behavior. Neither candidate is selected; no append-only implementation or garbage-collection algorithm is imposed here.
- closes when: Claude Arch states the insertion/update boundary, with owner authority for any change to admission, observable identity, evidence or shared formats.

## SG-008 - Execution context of a cached checking run (PROPOSED)

- anchor: R13 D-STO-1's build-relative run evidence; D-STO-2; STO-005. SG-006 separately preserves variable context; SG-001 preserves answer bytes.
- not stated: How a cached checking run's evaluator-build/evidence context is bound when another build considers reuse. The checking-program node alone does not record that the second build ran or replayed it.
- case: P checks the same claim and store answers in builds A and B. A's result is present; B considers it before local replay.
  - candidate A: Cache eligibility is partitioned by the applicable build/execution context, with that distinction recorded in the key or namespace.
  - candidate B: Entries can be shared, retaining A as the actual producing build and preserving the existing build-relative evidence status; a reader must check the context and any applicable evidence/trust requirements instead of treating import as B's replay.
  - costs: A may repeat checks and needs explicit key/context binding. B needs checked provenance and evidence-reading integration. Neither adds an automatic replay requirement or authorizes an unchecked cross-build yes.
- boundary: Answer ordering/absence bytes remain SG-001. D-STO-2's ambiguity-triggered rerun remains required; this gap chooses neither eager/lazy scheduling nor a mandatory positive cache hit.
- closes when: Claude Arch specifies the eligible reuse context and its representation; any new semantic reading or shared format follows the applicable owner route.

## SG-009 - Direct cycles in admitted term-constructor edges (PROPOSED; OPEN; TM-A provisional; owner confirmation pending) [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A]

- anchor: D-TM-1 shared terms; D-REC-1's shape under GAP 5; D-REC-4's separate named-recursion proposal.
- provisional answer (PROPOSED; standing: DRAFT): no term is among its own parts directly, with no name in between. Reference by a name stays, as a definition names itself or a group of definitions name each other (D-REC-4). [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A] The marked requirement is STO-010. Codex G's limit stands (card 0227): it is a revisable draft and no baseline. Nothing may fix record bytes, or admit or refuse a looping record in a run, on this answer.
- case: A builder offers n = app(n, zero), a direct constructor cycle rather than recursion through a named symbol. PROPOSED — Its TM-A expected refusal is only the marked paper case in STO-010. [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A]
  - candidate A: Admitted term-constructor edges must be well founded; specify the existing/intended admission invariant and its check/resource obligation.
  - candidate B: Such direct cycles are admitted; specify their identity, quotation, traversal, encoding and resource behavior.
  - costs: A requires the well-foundedness boundary and its validation. B requires cycle-aware semantics and a faithful codec; a group-hash proposal for named symbols does not by itself supply these.
- closes when: the owner confirms TM-A or changes the answer, and the intended admitted grammar and its required review are settled. Until then SG-009 is OPEN and the marked STO-010 requirement stays DRAFT. [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A] No rejection algorithm, graph order or byte profile is chosen, and no looping record is admitted or refused in a run on this answer.
- legacy unmarked dependencies (INFERENCE): The committed files written before tonight also need reading under TM-B: RULES-TERMS.md TERM-012 (147–159, continuation-site counting at154–155); RULES-STORE.md STO-014 (192–204, structural identity with nameless binders at200–201); RULES-RECORDS.md REC-002 (43–64, constructor-child depth-first numbering at55) and REC-004 (87–107, exact-once pattern depth-first walk and lexical checks at99); RULES-EVALUATOR.md EV-047 (859–870, whole-body inspection at866) and EV-121 (1756–1767, closure-wide forbidden-role scan at1763). A reversal needs accounts and deciding cases for constructor-cycle site counts, structural identity and binders, numbering, and syntactic scanning respectively; the old texts supply no direct-constructor-cycle account. These older unmarked accounts are not undone by searching the new mark: the named rules must be read under the owner's answer. Named-symbol recursion remains separate. This bounded inventory of supplied files fixes no record bytes, algorithm or runtime admission/refusal. [P0117:TM-A]

END OF GAPS-STORE
