# Claims rules, revision 2: claims and run evidence in slice 1

INFERENCE - Seventeen active draft rules are retained among CLM-001 to CLM-018; CLM-016 is a retired historical entry, replaced by EV-033 and EV-034. The active rules transcribe D-CL-1, D-CL-4, the Eval part of D-RUNEV-1, and D-RUNEV-2. Nothing here is adopted or approved. Unresolved reconciliations remain gaps; Claude Arch's unreviewed replies are not rule authority.

SOURCE — R13 is `DESIGN-TEXT-R13.md`, SHA-256 `20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce`. Each rule's "from" names an R13 anchor. A line number beside an anchor is a physical line of that file and is a locator only. R13's own tag for the words is kept beside each rule. R13 itself waits on an independent review.

SOURCE - The rule form follows HOW-WE-SPECIFY.md:54-80. The seventeen active rules have draft standing; CLM-016 is retired. No active rule's source point is tagged working or waiting. The revision binding hashes below cover the five binding fields required by the method; the hash convention is package metadata, not a Loom record format.

SOURCE - The following bound rules supply existing obligations. CLM-016 is retained only as a retired historical entry; its archived binding fields are not an additional requirement:
- EV-015: running out of fuel means unknown and never no.
- EV-027 to EV-031: a run record holds its program, input and supplied step bound and names the executing build. A successful record holds its returned value; a stopped run records its resource outcome and committed prefix rather than a fabricated output. These are necessary retained obligations, not a complete record or replay contract.
- EV-033: for a state-free run, Eval settles only the statement that this program on this input returned this output; a complete state-qualified Eval inference remains open at E-26.
- EV-034: passing from a checker's yes to its input statement needs the separate soundness claim.
- REC-013: what an evidence reader records of its grounds.
- STO-004 (store rules R1, in review): evidence is a derivation, a run record or a counterexample.
- ADM-001 (admission rules R2, written against design text R5; R3 on R13 is being written): the membership obligations of an application.

SOURCE — Close is outside this file. Whether slice 1 uses it is gap CG-003. Reflect arrives in slice 4.

PROPOSED — Cases use small invented symbols such as `double`, `zero` and `accept_all`. They are examples for a reader. They are not Loom syntax and add no vocabulary.

## CLM-001 — Every fact in the store is a claim

- revision: 1
- standing: draft
- kind: definition
- subject: a fact in the store
- from: SOURCE R13 D-CL-1 (line 417), first sentence, first part. R13 tag: `D L251 | agreed`.
- text: Every fact in the store is a claim.
- case: A slice 1 build finds that an argument is a member of its parameter's sort. What it writes to the store is a claim with that statement. It writes no bare mark on the term.
- excludes: Recording that a term passed admission as a mark on the term, with no claim that says what was found.
- gaps: CG-001 (what the first part of the obligation generator writes, and what settles it).

## CLM-002 — A claim never says more than its statement

- revision: 1
- standing: draft
- kind: requirement
- subject: a reader of a claim
- from: SOURCE R13 D-CL-1 (line 417), first sentence, second part. R13 tag: `D L251 | agreed`.
- text: A claim never says more than its statement.
- case: A run shows that `double(zero)` returned `zero`. The claim says that, for this input. A reader does not take it to say that `double` returns its argument for every input.
- excludes: Reading a claim about one input as a claim about all inputs.
- gaps: none.

## CLM-003 — Five things that are claims

- revision: 2
- standing: draft
- kind: definition
- subject: a fact in the store
- from: SOURCE R13 D-CL-1 (line 417), second sentence. R13 tag: `D L251 | agreed`.
- text: A sort membership, a law at an interpretation, a tracking clause, a covering fact and a width are all claims.
- case: In slice 1 an application gives rise to a sort membership. It is a claim, with the fields of CLM-004 to CLM-011.
- excludes: Treating a sort membership as a check result with no statement, status or evidence of its own.
- gaps: none for this classification. D-SL-2 brings laws at interpretations and scope and covering. D-SL-3 brings the generator for tracking clauses. D-ROW-5 already names slice 1's default representation's tracking claim. These cited slice passages do not assign the first use of widths.

## CLM-004 — The statement of a claim

- revision: 1
- standing: draft
- kind: definition
- subject: the statement of a claim
- from: SOURCE R13 D-CL-1 (line 421), the Statement row of the table. R13 tag: `D L253-L261 | agreed`.
- text: The statement of a claim is a proposition whose quantifiers name their domains. Its scope is part of what it says.
- case: A statement says that a law holds for every member of a named sort. The sort is written in the statement. A second statement that names a smaller sort is a different statement.
- excludes: A statement that says "for every x" and leaves the domain of x to be understood.
- gaps: CG-002 (what form a statement has in slice 1).

## CLM-005 — The status of a claim is a reading and is not stored

- revision: 1
- standing: draft
- kind: requirement
- subject: a build that reads or writes claims
- from: SOURCE R13 D-CL-1 (line 422), the Status row of the table. R13 tag: `the status row from C32 | approved, as forced move 16`.
- text: The status of a claim is yes, no, unknown or conflict. It is a reading. It is not stored.
- case: A claim's evidence is one run record. A build reads the claim and finds yes. It writes no "yes" into the claim's record. A later reader reads the evidence again.
- excludes: A stored status field that a reader trusts without reading the evidence.
- gaps: CG-002 (what reads a status in slice 1). How the reading is made, at a site and under a bound, is D-CL-2 and rule 4, which are later rules. That running out of fuel reads as unknown is EV-015.

## CLM-006 — A counterexample may be a set of values

- revision: 1
- standing: draft
- kind: permission
- subject: a counterexample as evidence
- from: SOURCE R13 D-CL-1 (line 423), the Evidence row of the table, last sentence. R13 tag: `D L253-L261 | agreed`.
- text: A counterexample may be a set of values.
- case: A statement says no two values share a name. Its counterexample is a set of two values with one name. One value alone would not refute it.
- excludes: Requiring every counterexample to be a single value.
- gaps: none. That evidence has three kinds is STO-004. What a run record holds is EV-027 to EV-031. Neither is restated.

## CLM-007 — The assumptions of a claim

- revision: 1
- standing: draft
- kind: definition
- subject: the assumptions field of a claim
- from: SOURCE R13 D-CL-1 (line 424), the Assumptions row of the table, first sentence. R13 tag: `D L253-L261 | agreed`.
- text: The assumptions of a claim are the claims that its evidence used and did not discharge.
- case: A slice 1 membership is settled by one run of `same`. The run used no other claim. Its assumptions are none.
- excludes: Leaving out of the field a claim that the evidence relied on.
- gaps: CG-001 (which claim fields the obligation generator supplies at emission; this definition does not choose an emission policy).

## CLM-008 — Evidence with assumptions is a rule

- revision: 1
- standing: draft
- kind: definition
- subject: a piece of evidence that has assumptions
- from: SOURCE R13 D-CL-1 (line 424), the Assumptions row of the table, second sentence. R13 tag: `D L253-L261 | agreed`.
- text: Evidence with assumptions is a rule.
- case: INFERENCE, on the ordinary reading of the word (gap CG-006 holds the other reading): a piece of evidence shows a statement Q and used a claim P that it did not discharge. It does not show Q outright. It shows Q where P holds.
- excludes: Reading evidence that used an undischarged claim as settling its statement with nothing owed.
- gaps: CG-006 (which sense of "rule" is meant).

## CLM-009 — The row of a claim

- revision: 2
- standing: draft
- kind: definition
- subject: the row field of a claim
- from: SOURCE R13 D-CL-1 (line 425), the Row row of the table. R13 tag: `D L253-L261 | agreed`.
- text: The row of a claim is the polynomial of D-ROW-10.
- case: Supply a completed state-free run of `double(zero)` that returned `zero` in build B. Eval settles the particular equation `double(zero) = zero`, and that Eval claim's row names B (CLM-015). This does not by itself settle a membership statement.
- excludes: Claiming that the row account is complete while its required row is absent. This does not decide when the generator must supply it; CG-001 retains that question.
- gaps: CG-001 (which fields the generator supplies at emission). The polynomial is defined by D-ROW-10; the separate row rules remain a draft dependency. This definition fixes neither a claim-record encoding nor a slice for the first use of alternatives.

## CLM-010 — When and how a claim is settled

- revision: 2
- standing: draft
- kind: definition
- subject: the settled field of a claim
- from: SOURCE R13 D-CL-1 (line 426), the Settled row of the table. R13 tag: `D L253-L261 | agreed`.
- text: The settled field of a claim says when the claim is settled and by which route: at build, at load, once in a run, at each evaluation of its site, or never.
- note: INFERENCE The five named alternatives close the timing component only. They do not enumerate or encode the route component; its missing account remains CG-007.
- case: Slice 1's default tracking claim is settled never (D-ROW-5). A membership that became a guard is settled at each evaluation of its site (D-ADM-4).
- excludes: A sixth settlement timing, or claiming the settlement account complete while its timing or required route account is absent. This does not decide which fields the generator supplies at emission (CG-001), or what identifies a route (CG-007).
- gaps: CG-001 (fields supplied at emission); CG-004 (universal settlement beside settled never); CG-007 (what identifies the route and what never records). No outcome is selected.

## CLM-011 — A note is not evidence

- revision: 1
- standing: draft
- kind: requirement
- subject: a reader of evidence, and anything that grants a licence
- from: SOURCE R13 D-CL-1 (line 427), the Notes row of the table. R13 tag: `D L253-L261 | agreed`.
- text: The notes field holds the notes about this claim. A note is not evidence, and no licence can cite one.
- case: A note says a membership probably holds. A build is asked to admit a program on it. The build does not. The claim's status is read from its evidence, which the note is not part of.
- excludes: Admitting a program, or granting any licence, on the strength of a note.
- gaps: none. What a note's own record holds is D-CL-3, a later rule.

## CLM-012 — A run becomes evidence by one of three rules

- revision: 1
- standing: draft
- kind: definition
- subject: a run offered as evidence
- from: SOURCE R13 D-CL-4 (line 436), first sentence; R13 D-RUNEV-1 (line 764), first sentence. R13 tags: `D L263 | agreed`; `D L580-L586 | agreed`.
- text: A run becomes evidence by one of three rules: Eval, Close and Reflect.
- case: A run record is offered for a claim. A reader asks which of the three rules makes it evidence for that claim. If none does, the record is not evidence for that claim.
- excludes: A fourth way for a run to count as evidence.
- gaps: CG-003 (Close in slice 1).

## CLM-013 - Derivations do not settle claims before slice 4

- revision: 2
- standing: draft
- kind: requirement
- subject: a build of slices 1 to 3
- from: SOURCE R13 D-CL-4 (line 436), third sentence. R13 tag: `D L263 | agreed`. The preceding universal settlement sentence and its repetition at D-SL-0 (line 835) remain the unresolved reconciliation in CG-004.
- text: Derivations arrive in slice 4. In slices 1 to 3 a derivation does not settle a claim.
- case: A slice 1 build is handed a derivation as evidence for a membership. It does not take the derivation as settling the claim.
- excludes: A slice 1 claim read as yes on a derivation.
- gaps: CG-004 (whether "every claim is settled by a run" requires settlement of every claim, and how that fits "settled never"; no outcome is selected here).

## CLM-014 — Slice 1 uses Eval

- revision: 1
- standing: draft
- kind: requirement
- subject: a build of slice 1
- from: SOURCE R13 D-RUNEV-1 (line 764), second sentence, its Eval part. R13 tag: `D L580-L586 | agreed`.
- text: Slice 1 uses Eval.
- case: A slice 1 membership is settled by a run of `same` that returned yes. Eval makes that run evidence for the statement that this program on this input returned that output.
- excludes: A slice 1 build with no rule that makes a run evidence.
- gaps: CG-003. R13's sentence is "Slices 1 to 3 use Eval and Close." Only its Eval part is ruled here.

## CLM-015 — The row of a claim made by Eval is the build that ran

- revision: 1
- standing: draft
- kind: requirement
- subject: a claim that Eval makes
- from: SOURCE R13 D-RUNEV-1 (line 768), the Eval row of the table, third cell. R13 tag: `D L580-L586 | agreed`.
- text: The row of a claim that Eval makes is the build that ran.
- case: Build B runs `double(zero)` and records that it returned `zero`. The claim's row names B. A reader who does not trust B has been told what the claim leans on.
- excludes: An Eval claim with an empty row.
- gaps: E-26 in the pinned GAPS-EVALUATOR.md retains the complete state-qualified Eval inference. The state-free claim form is held by EV-033 and the executing-build record field by EV-031; neither is restated by this claim-row requirement.

## CLM-016 - Retired: checker-run conclusions are held by EV-033 and EV-034

- revision: 2
- standing: retired - replaced by EV-033 and EV-034 in the pinned RULES-EVALUATOR.md; the five binding fields below are retained as archival revision-1 wording, with no active CLM obligation.
- kind: requirement
- subject: a build that reads a run of a checking program
- from: SOURCE R13 D-RUNEV-2 (line 772), third sentence, and its case (line 773). R13 tag: `C29 | approved, as forced move 14`.
- text: A run of a checking program on a statement P settles that the program returned yes on P.
- case: R13's own: a checker that accepts everything, run on 0 = 1, gives a true run record and a false statement. Call the checker `accept_all`. The run settles that `accept_all` returned yes on 0 = 1. It does not settle 0 = 1.
- excludes: Reading 0 = 1 as yes because a checking run returned yes on it.
- gaps: E-26 remains the external state-qualified Eval dependency; retirement does not close it.

SOURCE - R13 D-RUNEV-2:772-773 supplies this historical checker illustration. INFERENCE - Use EV-033 for the state-free Eval conclusion and EV-034 for separate soundness in the statement form, theory and scope. The archived universal wording above is not a new rule that an unfinished, negative or exhausted checking run returned yes.

## CLM-017 — Each trusted text has one soundness claim

- revision: 2
- standing: draft
- kind: requirement
- subject: a trusted text
- from: SOURCE R13 D-RUNEV-2 (line 772), fifth sentence. R13 tag: `C29 | approved, as forced move 14`.
- text: Each of the trusted texts has one soundness claim. That claim is what D-TB-2 trusts the text for. The text's name gives it no other.
- case: Supply a trusted text T with its one soundness claim restricted to statement form F in theory L and scope K. In a sufficiently fueled state-free run, T returns yes on a statement outside that claim's form, theory or scope. The run supplies its particular Eval conclusion under EV-033; the supplied trust does not establish that statement under EV-034.
- excludes: Taking a trusted text's yes as settling a statement of a form it is not trusted for.
- gaps: CG-008 (out-of-scope invocation of a named trusted checker). Which texts are trusted, and for what, is D-TB-2, which has no rule file yet. No additional trust or fallback permission is supplied by this rule.

## CLM-018 — A checker that is not a trusted text

- revision: 2
- standing: draft
- kind: requirement
- subject: a checker that is not one of the trusted texts
- from: SOURCE R13 D-RUNEV-2 (line 772), sixth sentence. R13 tag: `C29 | approved, as forced move 14`.
- text: For any other checker the soundness claim is proved, or it stays unknown and stands in the row as an assumption by name.
- case: A program brings its own checker for a statement form. No proof of the checker's soundness is in the store. A claim that leans on the checker's yes has the checker's soundness in its row, as an assumption, by name.
- excludes: A claim that leans on such a checker and whose row does not name the checker's soundness.
- gaps: CG-005 (whether slice 1's bound admits this unknown soundness entry); CG-008 (fallback for an out-of-scope invocation of a named trusted checker). CLM-013 rules out derivation evidence before slice 4; this does not decide whether an admitted run-evidence route can settle a particular soundness statement. Close in slice 1 remains CG-003. This row obligation does not waive D-ADM-4 or D-RL-12.

## Revision binding hashes

PROPOSED - Package-metadata convention for HOW-WE-SPECIFY.md:69: SHA-256 of the five complete UTF-8 field lines, including each original LF, in this order: kind, subject, text, case, excludes. Include the literal '- field: ' prefixes; concatenate those lines without any extra separator. Hash no heading, revision, standing, from, note, gaps or hash-table bytes. This convention binds prose revisions and selects no Loom record encoding or evaluator hash.

INFERENCE - CLM-016 is retired. Its row binds the archived five field lines retained for identity history, not an active requirement. Its retirement revision is 2; those binding bytes are unchanged from revision 1. Evidence for active rules must name the ID, applicable revision and binding hash; an archival digest supplies no active authority.

| ID | Revision | Standing | SHA-256 of five field lines |
|---|---:|---|---|
| CLM-001 | 1 | draft | bc4f30896fb7deb73a2e8335a4e479d8704c87aab823d1d64ff147353afd1cd3 |
| CLM-002 | 1 | draft | cee9ccd57a17c2b5db07fc11a7763653a131a7de12891474c66e620602979f44 |
| CLM-003 | 2 | draft | afd15252421b61fb0cebadc13af401d1931ed8dddaea6a52e81d2e9674f9eac4 |
| CLM-004 | 1 | draft | ebc04c30e582594b09cb609cc489fbc2e59942d93092775c080905ffcafc70bf |
| CLM-005 | 1 | draft | 1b4b9072b519cfb0e91caf8f6b48a344cb180c841f6349b05e1b1c879d38448d |
| CLM-006 | 1 | draft | b6a629d9829ee68f4bbd6211d844d40fa99563f8565ef725945447cdbdbcbbf9 |
| CLM-007 | 1 | draft | 7aa0f3e587ed7baa6ae4604e224402e9aea7e977759ca80a8c3c3dc37b9c42a6 |
| CLM-008 | 1 | draft | 44e0df547667ca73d090d4040e73f659297e858b647492399ee29eb5fd42e019 |
| CLM-009 | 2 | draft | 9e2ae0f2283ede49ac75b0e057be38e93721c52a739575b7534269051fc6b8af |
| CLM-010 | 2 | draft | 111d8a4561cf4dbec27f8cac9ec6370821f7621a26b3270e270f3342d7d90481 |
| CLM-011 | 1 | draft | 5af177aaeb44ae186a31811ae52a6e3af32c610c85fa84f69f42bbb0f6e9070f |
| CLM-012 | 1 | draft | 5e33f0bda55ca482872830afcfdac2484ec954ce268fd570cda663afaffdeb5f |
| CLM-013 | 2 | draft | 46a10f54f12ea997b013642d72f5311aa0eb1ada0635c3517f4a7aad4dc190b5 |
| CLM-014 | 1 | draft | 7901afbce37ef004881e8c5367ba21015bf1e8df7ac7cdd8dc3ff2291d9ab8df |
| CLM-015 | 1 | draft | a47964686d9cdd872112d3e59d876f7508081782ec527e68b7336b698700df1d |
| CLM-016 | 2 | retired | e7b7aaae0c45b1db569ad444256fa5d9ea7e99c748109e4329945817e5c7bfab |
| CLM-017 | 2 | draft | 108656af2906f7ba7b14d0ae3144990df5f62a082f8790d8ee353859c36b7b32 |
| CLM-018 | 2 | draft | 4e3a27e8fe6f1b3f87e46939730da75d0430ba5fed531196acfd59f1c2ba0a46 |

END OF RULES-CLAIMS
