# Claims coverage, revision 2

SOURCE - These 25 coverage rows quote the sentences and table cells of D-CL-1, D-CL-4, D-RUNEV-1 and D-RUNEV-2 identified below, against the pinned DESIGN-TEXT-R13.md (SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce). INFERENCE - SC-10 is slice-1 and Eval-only for D-RUNEV-1. Close is retained as CG-003; the Close and Reflect "Its row" cells are deferred with those contracts. Reflect's arrival and claim cell are explicitly outside scope, and "What a run shows" is a heading, not an obligation.

INFERENCE - "Rule here" names an active rule of RULES-CLAIMS.md. "Cited" names an obligation held elsewhere, with its stated scope retained. "Gap" names a CG entry here or an explicitly identified dependency gap in a pinned input. CLM-016 is retired, so its historical example is held by the cited EV rules.

| # | Anchor, line | Sentence or table cell | R13 tag | Rule here | Cited | Gap |
|---|---|---|---|---|---|---|
| 1 | D-CL-1, 417 | "Every fact in the store is a claim, and a claim never says more than its statement." | agreed | CLM-001, CLM-002 | none | CG-001 |
| 2 | D-CL-1, 417 | "A sort membership, a law at an interpretation, a tracking clause, a covering fact and a width are all claims." | agreed | CLM-003 | ADM-001 beside it, for memberships | none |
| 3 | D-CL-1, 421 | Statement: "A proposition whose quantifiers name their domains. Its scope is part of what it says" | agreed | CLM-004 | none | CG-002 |
| 4 | D-CL-1, 422 | Status: "Yes, no, unknown or conflict. It is a reading and is not stored (D-CL-2)" | approved, as forced move 16 | CLM-005 | EV-015 and REC-013 beside it | CG-002 |
| 5 | D-CL-1, 423 | Evidence: "One of three kinds. A derivation. A run record: program, input, output, step bound and the build that ran it. A counterexample, which may be a set of values" | agreed | CLM-006, for the last sentence | STO-004 for the three kinds; EV-027 to EV-031 for the run record | none |
| 6 | D-CL-1, 424 | Assumptions: "The claims the evidence used and did not discharge. Evidence with assumptions is a rule" | agreed | CLM-007, CLM-008 | none | CG-001; CG-006 |
| 7 | D-CL-1, 425 | Row: "The polynomial of D-ROW-10" | agreed | CLM-009 | none | CG-001, for which fields emission supplies |
| 8 | D-CL-1, 426 | Settled: "When, and by which route: at build, at load, once in a run, at each evaluation of its site, or never" | agreed | CLM-010 | none | CG-001; CG-004; CG-007 |
| 9 | D-CL-1, 427 | Notes: "The notes about this claim. A note is not evidence, and no licence can cite one" | agreed | CLM-011 | none | none |
| 10 | D-CL-4, 436 | "A run becomes evidence by one of three rules, Eval, Close and Reflect (D-RUNEV-1)." | agreed | CLM-012 | none | CG-003 |
| 11 | D-CL-4, 436 | "In slices 1 to 3 every claim is settled by a run." | agreed | no rule here | none | CG-004; universal settlement versus settled never remains unresolved |
| 12 | D-CL-4, 436 | "Derivations arrive in slice 4." | agreed | CLM-013 | none | none |
| 13 | D-RUNEV-1, 764 | "Three rules." | agreed | CLM-012 | none | none |
| 14 | D-RUNEV-1, 764 | "Slices 1 to 3 use Eval and Close." | agreed | CLM-014, for Eval | none | CG-003, for Close |
| 15 | D-RUNEV-1, 764 | "Reflect arrives with the derivation checker in slice 4." | agreed | no rule and no gap | none | none: slice 4 |
| 16 | D-RUNEV-1, 768 | The Eval row: "f(v) = w, for this input"; "The build that ran" | agreed | CLM-015, for the row | EV-033 for the claim's form; EV-031 for the build | E-26 in GAPS-EVALUATOR.md for state-qualified Eval; no extension selected |
| 17 | D-RUNEV-1, 769 | The Close row: "A statement for every word over some generators, from one checked finite description that is closed under them" | agreed | no rule | none | CG-003 |
| 18 | D-RUNEV-1, 770 | The Reflect row: "A checker for a theory's statements accepted a derivation" | agreed | no rule and no gap | none | none: slice 4 |
| 19 | D-RUNEV-2, 772 | "What a run shows." | approved, as forced move 14 | no rule and no gap | none | none: it names the passage |
| 20 | D-RUNEV-2, 772 | "Eval settles a statement of the form f(v) = w and no other." | approved, as forced move 14 | no rule here | EV-033 for state-free Eval | E-26 in GAPS-EVALUATOR.md for the state-qualified Eval contract; no extension selected |
| 21 | D-RUNEV-2, 772 | "A run of a checking program on a statement P settles that the program returned yes on P." | approved, as forced move 14 | no rule here | EV-033 for a completed affirmative state-free checking run; EV-034 for the separate scoped soundness obligation | E-26 retains state-qualified Eval; no extension selected |
| 22 | D-RUNEV-2, 772 | "P follows only with a second claim, the program's soundness: what it accepts is true, for statements of this form, in this theory and scope." | approved, as forced move 14 | no rule here | EV-034 | none |
| 23 | D-RUNEV-2, 772 | "Each of the trusted texts has one such claim, which is what D-TB-2 trusts that text for, and its name gives it no other." | approved, as forced move 14 | CLM-017 | none | CG-008, for out-of-scope invocation fallback |
| 24 | D-RUNEV-2, 772 | "For any other checker the claim is proved, or it stays unknown and stands in the row as an assumption by name." | approved, as forced move 14 | CLM-018 | none | CG-003; CG-005; CG-008 |
| 25 | D-RUNEV-2, 773 | "Case: a checker that accepts everything, run on 0 = 1, gives a true run record and a false statement." | R13's own case | no rule here | EV-034's explicit affirmative-checker case, under EV-033's state-free Eval premise | none |

## Counts

SOURCE - 25 rows. 16 name an active rule here. 4 have cited holders without an active rule here (rows 20, 21, 22 and 25), retaining the external E-26 qualification where applicable. 2 are held by a gap only (rows 11 and 17). 3 have no rule and no gap: rows 15 and 18 concern slice 4, and row 19 is a heading with no obligation.

## What is outside this file

SOURCE — D-CL-2 (how a status is read, and conflict) and D-CL-3 (a note's record) are slice 2 rules. D-RUNEV-3 to D-RUNEV-5 are Close. D-RL-1 to D-RL-13 are the reading rules.

END OF COVERAGE-CLAIMS
