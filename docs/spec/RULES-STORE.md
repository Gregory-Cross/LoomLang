# PROPOSED store rules, revision 2: the store in slice 1

INFERENCE — DRAFT. Nineteen rules, STO-001 to STO-019. They transcribe six passages of design text R13: D-STO-1, D-STO-2, the first row of D-STO-3's table (the row of a node), D-TM-1, D-REC-3 and D-REC-4. Nothing here is reviewed, adopted or approved. PROPOSED — Only the marked DRAFT TM-A requirement in STO-010 supplies a provisional restriction for SG-009; it is held for owner confirmation. [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A]

SOURCE — R13 is `DESIGN-TEXT-R13.md`, SHA-256 `20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce`. Each rule's "from" names an R13 anchor. A line number beside an anchor is a physical line of that file and is a locator only. R13's own tag for the words is kept beside each rule. R13 itself waits on an independent review.

SOURCE - The form follows HOW-WE-SPECIFY.md lines 54 to 80. Each rule has revision, standing, kind, subject, from, text, case and excludes, and a per-rule binding hash. Standing is draft for every rule here. The obligation-bearing final sentence of D-TM-1 is working: C22; it is cited through EV-003 rather than repeated.

PROPOSED - Documentary binding profile STO-FIELDS-1: binding-sha256 is SHA-256 of the literal complete field lines for kind, subject, text, case and excludes, in that order, including their original line terminators. This profile applies to these one-line fields; any future multiline form needs an explicit extension. Evidence cites the rule ID, revision and this digest. This is a proposed document-binding convention, not the evaluator hash or any Loom node, symbol, record or recursive-group encoding; E-1, E-16 and B03 remain open.

SOURCE — Rules already written are cited and not repeated:
- EV-003: equal admitted immutable evaluator values are one observable node under its canonical-representation premises; equal code alone grants no reuse of a run.
- EV-013: both evaluator builds use the same named hash.
- EV-031 and EV-032: a run record names its build; before replay it is evidence relative to that build.
- REC-002: how variables are numbered when binders are made nameless.
- REC-013: what an evidence reader records, cached premises among it.
- TERM-005 (terms rules R1, in review): a bound argument's multiplicity is declared in the operation's signature.

SOURCE — The bytes that content identity hashes are not given in R13 (its GAP 4). They are recorded as gap B03 of the record rules and gap E-16 of the evaluator rules. No rule here says what is hashed. Rules that speak of content identity say only that it exists and what it must tell apart.

PROPOSED — Cases use small invented symbols such as `double`, `zero` and `even`. They are examples for a reader. They are not Loom syntax and add no vocabulary.

## STO-001 — The store is one graph, addressed by content

- revision: 2
- binding-sha256: ad38a8b195ac6eec0816cdef35842d12d883b704b513e6e1c0c8dfd8d643b18e
- standing: draft
- kind: definition
- subject: the store
- from: SOURCE R13 D-STO-1 (line 500), first sentence. R13 tag: `D L293 | agreed`.
- text: The store is one graph. It is addressed by content.
- case: In one logical store, insert the same admitted term double(zero) twice under the term-identity premises of STO-011 to STO-014. Both references reach the same logical node by content identity.
- excludes: A logical store whose records cannot be reached through its content-addressed graph, or whose only identity for a thing is its placement address.
- gaps: SG-001 (the bytes that content identity hashes). This rule concerns one logical store; it does not require independent evaluator builds to share physical storage or choose a cross-session persistence policy.

## STO-002 — What the store holds

- revision: 2
- binding-sha256: 2b81fe95ac851779eeb545dabdcbbf5f83a8bbd1db1b06b5706ea590904e4522
- standing: draft
- kind: definition
- subject: the store
- from: SOURCE R13 D-STO-1 (line 500), second sentence. R13 tag: `D L293 | agreed`.
- text: The store holds terms, theories, interpretations, representations, claims, evidence, notes and built artefacts.
- case: In a fixture producing a term, its theory, a membership claim, a valid corresponding run record and a built artefact, all five are represented in the logical store. This example does not fix a slice's complete production inventory or the record codecs.
- excludes: Keeping claims or evidence outside the logical store's content-addressed graph so that its node-addressing mechanism cannot reach them.
- gaps: none for the whole-language inventory. Slice 1 keeps the default representation of D-SL-1; this rule chooses no further representation or interpretation. Write authority for other stored kinds remains SG-005.

## STO-003 — Anything may add a term, a proposal or a note

- revision: 2
- binding-sha256: b188cb839a14c4ad6d3b389e687c1cd649ffc16a2a4d275698bc7340e6280fcf
- standing: draft
- kind: permission
- subject: a writer to the store
- from: SOURCE R13 D-STO-1 (line 500), third sentence. R13 tag: `D L293 | agreed`.
- text: Anything may add a term, a proposal or a note.
- case: An untrusted tool adds a note saying that a term looks slow, and the store accepts the note under this permission. Acceptance alone does not make a claim yes or license a step. If the addition changes a recorded store answer, the applicable dependencies and reuse conditions of STO-005 to STO-007 still apply.
- excludes: A store that takes a term or a note only from a trusted program.
- gaps: SG-005 (R13 names three kinds here and does not say what may add the others).

## STO-004 — The three kinds of evidence

- revision: 1
- binding-sha256: f9ffa061f0b097006127fc7ba22594423f1d0b4248eed75bb5450eeaf4ce1efc
- standing: draft
- kind: definition
- subject: a piece of evidence in the store
- from: SOURCE R13 D-STO-1 (line 500), fourth sentence. R13 tag: `D L293 | agreed`.
- text: Evidence is a derivation, a run record or a counterexample.
- case: A membership claim in slice 1 is settled by a run of `same`. Its evidence is a run record. A note that says the claim probably holds is not evidence.
- excludes: Counting a note, an estimate or a sample as evidence.
- gaps: none for the evidence categories. D-SL-0 requires claims in slices 1 to 3 to be settled by runs, and D-SL-1 needs no derivation. This is no new prohibition on storing a derivation as data. Build-relative run-record evidence remains EV-031 and EV-032.

## STO-005 — What a cached check is kept under

- revision: 2
- binding-sha256: 40285b39255d34a171a4870e48ed9a06aab660b839860943575845ba55541fcc
- standing: draft
- kind: requirement
- subject: the cache of checks
- from: SOURCE R13 D-STO-2 (line 502), first sentence. R13 tag: `D L295 | agreed, not run`. Beside it: D-UO-10 (line 144), for the mandatory context distinction.
- text: A check is cached under three things: the checking program, the claim, and a record of every question the check put to the store with the hash of each answer. The record includes each answer that nothing was there.
- case: A check asks the store two questions. The first has an answer and the second finds nothing. Its cache entry binds the checking program, the claim, both questions and the hash of each answer, including the answer of absence. This case fixes no encoding of either answer.
- excludes: An entry kept under the claim alone, or one that leaves out a question because its answer was that nothing was there.
- gaps: SG-002 (whether slice 1 has the cache); SG-006 (where the mandatory node/context distinction is represented); SG-008 (the checking run's execution/evidence context). D-UO-10 already requires node and context for a cached check of a node with variables. REC-013 retains the separate evidence-reader support obligations; no cross-build cache-key policy is selected here.

## STO-006 — A cached check is reused only while every answer is the same

- revision: 2
- binding-sha256: 60aa07a30b4fd1bd628092b17bdd7ec455c7a3e82fa86efe2bf1cf6ac66e1b20
- standing: draft
- kind: requirement
- subject: the cache of checks
- from: SOURCE R13 D-STO-2 (line 502), second sentence. R13 tag: `D L295 | agreed, not run`.
- text: A cached check is reused only while every question in its record still has the same answer.
- case: The entry of STO-005 is considered later, and the first question now has a different answer. That stale entry is not reused. STO-007 separately states the specified default-ambiguity rerun obligation.
- excludes: Reusing the entry because the claim and the checking program are unchanged.
- gaps: SG-002.

## STO-007 - A new declaration that makes a default ambiguous reruns the checks that asked

- revision: 1
- binding-sha256: f5963ec77e7e01b7d4635bfe023eec582e6278cf878816da54021634f947fee8
- standing: draft
- kind: requirement
- subject: the cache of checks
- from: SOURCE R13 D-STO-2 (line 502), third sentence. R13 tag: `D L295 | agreed, not run`.
- text: A new declaration that makes a once-unique default ambiguous reruns the checks that asked.
- case: A check asked which default applies in a scope, and one did. A new declaration adds a second default for the same scope. The question now has a different answer. Every cached check that asked it runs again.
- excludes: Keeping those entries because nothing they named was edited.
- gaps: SG-002. Defaults for a theory in a scope are D-IN-4; interpretation selection is named in D-SL-2. This rule does not decide whether slice 1 has the check cache.

## STO-008 — The row of a node is a query of the store, and what it returns

- revision: 1
- binding-sha256: 31bd9b2db655b3378e31127fc63f12e22031be39f01a8d52cd959d1c91fd9c0e
- standing: draft
- kind: definition
- subject: the query "row of a node"
- from: SOURCE R13 D-STO-3 (line 504), the table's first row (line 508), columns one and two. R13 tag: `D L297-L309 | agreed`.
- text: The store answers the query "row of a node". The query returns the polynomial, its symbols, and its reading under a bound.
- case: A slice 1 program is admitted and its root node is given to the query. The answer names what the node leans on, and says whether that fits slice 1's one fixed bound.
- excludes: An answer that says only "fits" or "does not fit" and does not give the row.
- gaps: SG-003 (what the query takes, and what the polynomial is in slice 1). What a row is and how it is computed belong to the row rules, which are a draft outside the repository.

## STO-009 — A kernel program answers the row query, and its answer can license

- revision: 2
- binding-sha256: 7d07fa3c1fead42a73eadc0e51544c2adbf764db9e25317e0a9cd9bd3669c1ad
- standing: draft
- kind: requirement
- subject: the query "row of a node"
- from: SOURCE R13 D-STO-3 (line 504), the table's first row (line 508), columns three and four. R13 tag: `D L297-L309 | agreed`.
- text: The row of a node is answered by a kernel program. Its answer can license.
- case: A build needs to know whether a program fits the bound. It takes the answer of the row computer, a kernel program of slice 1 (D-SL-1). A proposer's guess at the row is not that answer.
- excludes: Admitting a program solely on an unverified row supplied by a proposer or an untrusted tool, without the kernel program's answer.
- gaps: none.

## STO-010 — A term is an expression over theories, stored as a shared graph

- revision: 3
- binding-sha256: c9ef04d77ff2c15cfb60a6f8bfea294964d43290b3c5cc8ab35acd9c864c9276
- standing: draft
- kind: definition; PROPOSED marked requirement for TM-A (standing: DRAFT) [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A]
- subject: a term in the store; for the marked TM-A requirement, a term constructor or a reader of a described term [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A]
- from: SOURCE R13 D-TM-1 (line 172), first sentence. R13 tag: `D L66 | kept`. PROPOSED — gap SG-009 for the marked TM-A requirement; [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A].
- text: A term is an expression over theories. It is stored as a shared graph. PROPOSED — Marked requirement (standing: DRAFT): no term is among its own parts directly, with no name in between. Reference by a name stays, as a definition names itself or a group of definitions name each other (D-REC-4). [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A]
- case: The term `pair(double(zero), double(zero))` has two arguments that are the same expression. In the store they are one node, reached from the pair at two places. PROPOSED — Marked TM-A case (DRAFT; paper description only): in n = app(n, zero), n labels a described node rather than a declared or defined symbol; a constructor edge returns to that node directly, with no name in between. Under the marked requirement this description is refused. [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A] No record bytes are supplied, and no looping record is admitted or refused in a run on this answer.
- excludes: Storing a term as a tree in which each occurrence of an equal part is a separate copy. PROPOSED — The marked TM-A case excludes treating the direct self-part description as an admitted term under this DRAFT requirement. Reference by a name is outside this exclusion: a definition may name itself or a group of definitions may name each other (D-REC-4; STO-019). [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A] This is no result from a run.
- gaps: SG-009 remains OPEN; TM-A is provisional and awaits owner confirmation. [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A] No record bytes, rejection algorithm or runtime admission/refusal is fixed on this answer. Counting sites along paths of the shared graph remains the use-once rules' D-UO-2 obligation.

## STO-011 — Equal terms are one node

- revision: 1
- binding-sha256: 82e33eea7a94a1fb69b58641f55379d583670cf48b4955ff893655de6f669148
- standing: draft
- kind: requirement
- subject: the store
- from: SOURCE R13 D-TM-1 (line 172), second sentence. R13 tag: `D L66 | kept`. Beside it: EV-003, which states the same of evaluator values.
- text: Equal terms are one node.
- case: Two theories are read from two files, and each holds the term `double(zero)` over the same symbols. The store has one node for it.
- excludes: Two nodes for equal terms because they came from two files.
- gaps: SG-001. When two terms are equal rests on STO-012 to STO-014.

## STO-012 — A defined symbol is identified by its content

- revision: 1
- binding-sha256: d95608e0c27ddf247b2685a8d5989bc718c2821a8709955b13a56fe8e660522d
- standing: draft
- kind: requirement
- subject: a defined symbol
- from: SOURCE R13 D-TM-1 (line 172), third sentence, first part. R13 tag: `D L66 | kept`. Beside it: R13 D-REC-1 (line 1047), `defined(content hash, signature, rules)`.
- text: A defined symbol is identified by its content.
- case: Two writers each define a symbol with the same signature and the same rules, and give it different names. It is one symbol.
- excludes: Telling the two apart by the names their writers gave them.
- gaps: SG-001. A symbol whose rules name itself is STO-019.

## STO-013 — A declared symbol is identified by its declaration

- revision: 2
- binding-sha256: 2e30f34e0834b88683c9dbbf14e08ec5b00787e8309992fbc680852cc8fb84e7
- standing: draft
- kind: requirement
- subject: a declared symbol
- from: SOURCE R13 D-TM-1 (line 172), third sentence, second part. R13 tag: `D L66 | kept`.
- text: A declared symbol is identified by its declaration.
- case: A theory has two distinct declarations of operations with equal signatures. They remain two symbols under declaration identity; equal signatures alone do not merge them.
- excludes: Merging two declared symbols because their signatures are equal.
- gaps: SG-004 (what a declaration's identity is made from). STO-018 gives the default.

## STO-014 — A term is identified by its structure, with binders made nameless

- revision: 1
- binding-sha256: c576f7581468719895090df8fe6f2a21600d9f25ed073179af2914c6d33306bb
- standing: draft
- kind: requirement
- subject: a term in the store
- from: SOURCE R13 D-TM-1 (line 172), third sentence, third part. R13 tag: `D L66 | kept`.
- text: A term is identified by its structure, with its binders made nameless.
- case: One writer writes a binder with the variable x and another writes the same binder with the variable y. Nothing else differs. The two terms are one node.
- excludes: Two nodes for terms that differ only in the names of their bound variables.
- gaps: none. How the variables are numbered once the names are gone is REC-002 and is not restated.

## STO-015 — Programs, proofs, data and machine code are terms

- revision: 1
- binding-sha256: 50da3f1c72c20c360f228510f982adce422b8b54e1cef7a71d83c94f459d50eb
- standing: draft
- kind: definition
- subject: a term in the store
- from: SOURCE R13 D-TM-1 (line 172), fourth sentence. R13 tag: `D L66 | kept`.
- text: Programs, proofs, data and machine code are terms.
- case: The machine code that a slice 1 build emits is in the store as a term. It has a node and an identity as a program has.
- excludes: Holding emitted machine code only as a file beside the store, with no node.
- gaps: none.

## STO-016 — A node is a value of the evaluator, and its identity is `same`

- revision: 1
- binding-sha256: f571d4957cd1ad222e0e51f0564e45a73b054986b996e09ec3a71ae856d5a8a1
- standing: draft
- kind: requirement
- subject: the store, and an evaluator build that holds it
- from: SOURCE R13 D-REC-3 (line 1069), first sentence. R13 tag: `D L606-L608 | agreed`. Beside it: EV-003 for canonical-value premises and EV-004/EV-069 for the existing same result law. This rule supplies the store-node/evaluator-value bridge and selects no result carrier or physical interning scheme.
- text: A node is a value of the evaluator. The store's graph is the evaluator's interned values. The identity of a node is `same`.
- case: A checking program is given two nodes and asks `same` of them. The answer is yes exactly when they are one node of the store.
- excludes: A store with an identity of its own that can differ from what `same` says of two nodes.
- gaps: SG-001. What interning costs and how values are made canonical is the evaluator rules' gap E-14.

## STO-017 — A sort's declarations are in its signature

- revision: 1
- binding-sha256: 7461ee6eeb45b507058cb9835b73695b09e3f8579c015308974f1079576b1648
- standing: draft
- kind: requirement
- subject: the signature of a sort
- from: SOURCE R13 D-REC-3 (line 1069), second sentence. R13 tag: `D L606-L608 | agreed`. Beside it: R13 D-REC-1 (lines 1050 to 1051).
- text: A sort's declarations are in its signature.
- case: A sort is declared use-once. A reader that holds only the sort's signature can say so.
- excludes: Keeping the use-once mark of a sort somewhere that its signature does not show.
- gaps: none. That a bound argument's multiplicity is in the signature of its operation, the next sentence of D-REC-3, is TERM-005 and is not restated. Which declarations a sort may carry is D-TH-7, part 2 of the terms rules.

## STO-018 — The default id of a declared symbol, and names

- revision: 2
- binding-sha256: 07fa06edba85e8de764e05d774eb5d6ce701e5e80aeb1cef994aa859033315ee
- standing: draft
- kind: requirement
- subject: a declared symbol
- from: SOURCE R13 D-REC-3 (line 1069), fourth sentence. R13 tag: `D L606-L608 | agreed`.
- text: The id of a declared symbol is, as a default, its theory's id with its position in the theory. Names are metadata.
- case: Under the default, hold the theory id T and declaration position three fixed and change only the display name. The declared-symbol id remains T with position three. This fixture makes no cross-version identity claim.
- excludes: An id that changes when only a name changes.
- gaps: SG-004 (identity across versions of a theory, which R13 marks open; what "as a default" leaves room for). What a theory's id is itself is gap TG-002 of the terms rules.

## STO-019 — Symbols that name each other are hashed as a group

- revision: 2
- binding-sha256: ea413555b519b68cc1fa33650954690ead7c331dece689a1c07418b526e63a6c
- standing: draft
- kind: requirement
- subject: the content hash of a defined symbol
- from: SOURCE R13 D-REC-4 (line 1071). R13 tag: `D L612 | author's, proposed, not run`.
- text: Where a defined symbol's rules name the symbol itself, or several defined symbols name each other, the group is hashed together. Each member is written as its position in the group.
- case: Given an already supplied group containing even and odd in that supplied order, even has a rule that calls odd and odd has a rule that calls even. Hash the supplied group together, with these internal references represented by member positions one and two. The boundary, order and byte profile are prerequisites of this fixture.
- excludes: Hashing `even` alone, which would need the hash of `odd`, which would need the hash of `even`.
- gaps: SG-001. The group's boundary, the order of its members, and the bytes hashed are gap B03 of the record rules. R13's tag says this passage is its author's proposal and has not been run.

END OF RULES-STORE
