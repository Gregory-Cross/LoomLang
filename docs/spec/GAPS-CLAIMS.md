# Claims gaps, revision 2

INFERENCE - Eight recorded questions, CG-001 to CG-008. Each states a missing account or an unresolved reading of the cited R13 passages, with a discriminating case, candidate outcomes and their costs. None is chosen. This inventory is not a claim that no other question remains.

SOURCE — R13 is `DESIGN-TEXT-R13.md`, SHA-256 `20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce`. Lines are physical lines of that file.

SOURCE — Three of these are questions already sent to Claude Arch: QA-10, QA-12 and QA-15 of `QUESTIONS-ARCH.md` in the package `2026-11-12-CLAUDE-ENG-SPEC-CATCH-UP-PLAN`. Claude Arch has replied in `QA-REPLIES.md` of the package `2026-11-12-CLAUDE-ARCH-OPEN-SLICE-1`, with words proposed for the next design revision. **Those replies are unreviewed and are not R13.** Each is named below as the proposed answer under review. No rule is written from one. A gap closes when its reply is reviewed and the design text takes it.

## CG-001 — What the first part of the obligation generator writes, and what settles it (QA-10)

- anchor: R13 D-CL-1 (line 417); R13 D-ADM-4 (line 553); R13 D-SL-1 (line 837).
- what R13 has: "Every fact in the store is a claim". D-ADM-4: "The obligation generator emits one membership claim for each application". D-SL-1 names "the first part of the obligation generator, which emits a membership claim for each application".
- what is not stated: Which fields of a claim the generator fills, and whether the generator also settles the claim it emits.
- touches: CLM-001, CLM-007, CLM-009, CLM-010.
- case: A slice 1 program holds one application whose argument sort and parameter sort are the same node.
  - outcome A: The generator writes a claim that carries its statement and nothing else. Something else runs `same` and adds the run record as evidence.
  - outcome B: The generator runs `same` itself and writes the claim with its evidence, its row and its settled field filled.
  - cost of A: Two things must each be specified: what emits, and what runs and records. A claim can stand in the store with no evidence, and reads as unknown until a run is added.
  - cost of B: The generator is a trusted text, and it then does two jobs. A fault in how it runs `same` is inside the trusted base.
- proposed answer under review: `QA-REPLIES.md` line 47 (QA-10), with new passage D-ADM-9 in its `REPLACEMENTS.json` (item AD-1). It proposes outcome A.
- closes when: that reply is reviewed and the design text takes it.

## CG-002 — What reads a status in slice 1, and what form a statement has (QA-12)

- anchor: R13 D-CL-1 (lines 421 and 422); R13 D-CL-2 (line 431); R13 D-ST-1 (line 109); R13 D-SL-2 (line 839).
- what R13 has: Status "is a reading and is not stored (D-CL-2)". D-CL-2: the status "is a reading of its evidence at a site, under a bound, at one state of the store, by rule 4". D-SL-2 puts "the reader of evidence at a site" in slice 2. D-ST-1: "A statement is a term of the statement sort of a logic, and a logic is a theory."
- what is not stated: What reads the status of a membership claim in slice 1, before the reader of evidence exists. And whether a slice 1 statement is a term of a logic's statement sort, which needs some logic theory in slice 1, or a fixed record form.
- touches: CLM-004, CLM-005.
- case: A slice 1 build must decide whether a membership is yes before it admits a program.
  - outcome A: No reader is needed in slice 1. The membership is yes when a run of `same` gave yes and this build made or replayed that run. The statement is a term of the statement sort of one small theory that slice 1 ships, with no laws.
  - outcome B: Slice 1 has a small reader of its own, and a statement is a fixed record form until slice 2 brings logic theories.
  - cost of A: Slice 1 ships a theory whose only use is to give statements a sort. Its symbols must be named. A record that another build wrote counts for nothing until replayed.
  - cost of B: A second form for statements exists for one slice and must be replaced. It is an exception to D-ST-1, which is agreed.
- proposed answer under review: `QA-REPLIES.md` line 51 (QA-12), with new passage D-ADM-10 (item AD-1). It proposes outcome A.
- closes when: that reply is reviewed and the design text takes it.

## CG-003 — Close in slice 1 (QA-15)

- anchor: R13 D-RUNEV-1 (lines 764 and 769); R13 D-CL-4 (line 436).
- what R13 has: "Slices 1 to 3 use Eval and Close." And the table's Close row: "A statement for every word over some generators, from one checked finite description that is closed under them".
- what is not stated: Whether any slice 1 claim is settled by Close, and whether the closure checker is a trusted text of slice 1.
- touches: CLM-012, CLM-014, CLM-018.
- case: A slice 1 build is offered a run that claims to cover every word over some generators.
  - outcome A: Slice 1 uses Eval alone. The run counts only as Eval gives it: this program on this input returned this output. The closure checker is not a slice 1 text.
  - outcome B: Slice 1 uses Close as well. The closure checker is one of slice 1's trusted texts, and the run can settle the statement for every word.
  - cost of A: R13's sentence is read as naming the slices by which Close has arrived, not each of them. Nothing in slice 1 can be settled for a whole sort by one run.
  - cost of B: One more trusted text in slice 1, with its soundness claim, and rules for Close are owed before slice 1 can be built.
- proposed answer under review: `QA-REPLIES.md` line 83 (QA-15), with an addition to D-RUNEV-1 (item RE-1). It proposes outcome A.
- closes when: that reply is reviewed and the design text takes it. This file has no rule on Close.

## CG-004 — "Every claim is settled by a run" beside "settled never"

- anchor: R13 D-CL-4 (line 436); R13 D-CL-1 (line 426); R13 D-ROW-5 (line 221).
- what R13 has: "In slices 1 to 3 every claim is settled by a run." The settled field allows "never". D-ROW-5: "In slice 1 the default representation's tracking claim is settled never".
- what is not stated: How the two fit. A claim that is settled never is not settled by a run.
- touches: CLM-010, CLM-013.
- case: Slice 1's default tracking claim, which has no evidence.
  - outcome A: The sentence of D-CL-4 is about the kind of evidence: before slice 4 nothing is settled by a derivation. A claim may still be settled never, by name, and stand in the row.
  - outcome B: The sentence means what it says of every claim, and "settled never" is not a state a slice 1 claim may have. The tracking claim must then be settled by some run.
  - cost of A: None beyond a clearer sentence. It agrees with D-ROW-5 and with D-SL-1's root row.
  - cost of B: It contradicts D-ROW-5 as written, and slice 1 would owe a run that settles the lowering.
- closes when: the design text says which. This gap is new here. It is not among the questions already sent to Claude Arch.

## CG-005 — Whether slice 1's bound admits a checker's soundness as an assumption by name

- anchor: R13 D-RUNEV-2 (line 772); R13 D-ROW-9 (line 230); R13 D-CL-4 (line 436).
- what R13 has: For a checker that is not a trusted text, the soundness claim "is proved, or it stays unknown and stands in the row as an assumption by name". Before slice 4 there are no derivations. D-ROW-9 says of slice 1's bound: "this gives no blanket ban on every other axiom or trust entry", and leaves the bound's scope to GAP 6.
- what is not stated: Whether a slice 1 program whose row names a checker's soundness as an assumption fits slice 1's one fixed bound.
- touches: CLM-018.
- case: A slice 1 program brings a checker of its own and leans on its yes.
  - outcome A: The bound admits the entry. If the other admission obligations are met, the program is admitted and its root row names the checker's soundness.
  - outcome B: The bound refuses this unknown soundness assumption. The program cannot use this checker's yes to establish P on that assumption.
  - cost of A: Slice 1 admits programs whose claims rest on something nobody has checked, by name.
  - cost of B: This program cannot use its checker's yes to establish P while the soundness claim remains unknown and the bound refuses its named assumption. Running the checker and recording its particular return under Eval is a separate matter.
- closes when: R13's GAP 6, the complete scope of the bound, is filled. This gap is new here. A sort's literal check is not such a checker where it is the sort's only account of its literals: D-ADM-3 says it then "owes no claim that it is right".

## CG-006 — Which sense of "rule" is meant in "Evidence with assumptions is a rule"

- anchor: R13 D-CL-1 (line 424); R13 D-TH-5 (line 99).
- what R13 has: "Evidence with assumptions is a rule". D-TH-5: "A rule is a step of the reference run."
- what is not stated: Whether "rule" in the claim's table is the rule of D-TH-5 or an ordinary word for something that holds under conditions.
- touches: CLM-008.
- case: Evidence for Q that used an undischarged claim P.
  - outcome A: "Rule" is the ordinary word. The evidence shows Q where P holds, and it is recorded as evidence with one assumption.
  - outcome B: "Rule" is D-TH-5's. The evidence is recorded as a rule of some theory, and the reference run could step by it.
  - cost of A: One word in R13 has two senses, and a reader must be told.
  - cost of B: Evidence would enter the reference run, which nothing else in R13 suggests.
- closes when: the design text says which, or uses another word. This gap is new here. CLM-008's case is written for outcome A's reading of the sentence and marks nothing as decided.

## CG-007 - What identifies the route in the settled account

- anchor: SOURCE R13 D-CL-1 (line 426); D-ROW-10 (line 232).
- what R13 has: The settled account says when and by which route. The five alternatives name timings. D-ROW-10 names alternative evidence routes that the reader chooses among and records.
- what is not stated: INFERENCE - Whether that account must name a chosen route separately or may recover it unambiguously from linked evidence and context; what the route component says for never is also unstated. This question specifies no record encoding or new evidence category.
- touches: CLM-010.
- case: Two supplied evidence routes for one claim have the same settlement timing. A reader must identify which route the account reports, or identify that no settlement occurred.
  - outcome A: PROPOSED - The account names the chosen route through an explicit route relation, with a specified account for never.
  - outcome B: PROPOSED - The account identifies the route through unambiguous linked evidence and context, with a specified account for never.
  - cost of A: An additional route relation and validation duties must be stated.
  - cost of B: The recovery rule and ambiguity checks must be stated.
- question as Codex X states it (ruling H5, PROPOSED by X): Claude Arch should propose, and applicable owner authority decide if semantics change: must the settled account name a chosen route separately, or may an unambiguous route be recovered from linked evidence/context? Separate naming costs a route relation and validation; recovery costs a specified recovery and ambiguity rule; either answer must define the account for never.
- whose decision, in Codex X's words: Claude Arch drafts; applicable owner authority is required for new semantic adoption. SOURCE - Card 0039: open, routed by Claude A; no outcome is chosen here.
- closes when: Claude Arch's route account is independently reviewed and installed in the design text under the applicable owner authority. No answer is adopted here.

## CG-008 - A named trusted checker outside its one trusted claim

- anchor: SOURCE R13 D-RUNEV-2 (line 772).
- what R13 has: Soundness is for statements of this form, in this theory and scope. A trusted text has one such claim and its name supplies no other. Any other checker's soundness is proved or remains unknown and named in the row.
- what is not stated: INFERENCE - Whether other checker is classified by the text's identity or by its invocation relative to its one trusted soundness claim.
- touches: CLM-017, CLM-018.
- case: Trusted text T has one soundness claim for form F in theory L and scope K. It returns yes on P outside that claim's theory or scope.
  - outcome A: PROPOSED - This invocation follows the ordinary other-checker route with a separate soundness claim for P's form, theory and scope, retaining the bound and all other admission duties.
  - outcome B: PROPOSED - This invocation gets no automatic other-checker fallback; a separate scoped contract must first authorize that route.
  - cost of A: Invocation-relative classification and the additional soundness, dependency and admission duties must be specified.
  - cost of B: Separate scoped proof or trust-contract work is owed before that fallback can be used.
- question as Codex X states it (ruling H7, PROPOSED by X): Claude Arch should propose, and applicable owner authority decide: does an out-of-scope invocation of a named trusted checker use the ordinary other-checker route with additional scoped soundness, or require a separate scoped contract first? The first costs explicit invocation-relative classification plus the new soundness/bound duties; the second costs a separate proof/trust contract before that fallback can be used. Neither answer forbids the particular Eval run.
- whose decision, in Codex X's words: Claude Arch drafts; applicable owner authority is required for new semantic adoption. SOURCE - Card 0039: open, routed by Claude A; no outcome is chosen here.
- closes when: The fallback classification is independently reviewed and installed in the design text under the applicable owner authority. Neither answer broadens T's existing trusted claim or forbids its particular Eval run.

END OF GAPS-CLAIMS
