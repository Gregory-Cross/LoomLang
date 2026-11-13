# Terms and theories coverage, revision 2, part 1

SOURCE — One row for each sentence of five passages of R13 (`DESIGN-TEXT-R13.md`, SHA-256 `20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce`): D-TH-1, D-TH-2, D-TH-3, D-TH-4 and D-TH-6. Each sentence is quoted exactly. A program matched every quotation against R13.

INFERENCE — "Holds it" means a rule states the sentence, or a gap records what the sentence leaves open. A row may name both. No sentence of the five passages is left with "no rule and no gap".

| # | Anchor, line | Sentence | R13 tag | Rule | Gap |
|---|---|---|---|---|---|
| 1 | D-TH-1, 91 | "A theory is a vocabulary: sorts, operations, laws and rules." | kept | TERM-001 | TG-002, TG-005, TG-008, TG-012 |
| 2 | D-TH-1, 91 | "The integers, a mutable store, a logic, an instruction set and a file format are all theories." | kept | TERM-002 | none |
| 3 | D-TH-2, 93 | "A sort may be indexed by terms, as in a vector of length n." | kept | TERM-003 | TG-001, TG-011 |
| 4 | D-TH-3, 95 | "An operation may bind variables." | fold | TERM-004 | none |
| 5 | D-TH-3, 95 | "A bound argument carries a multiplicity, declared in the operation's signature: how many times the operation calls it." | fold | TERM-005 (it is declared in the signature), TERM-006 (what it says) | TG-004, TG-010 |
| 6 | D-TH-3, 95 | "It is one or any." | fold | TERM-007 | TG-003 |
| 7 | D-TH-3, 95 | "Whether a third value, none, for a parameter that is never called, is added goes to test." | approved, to test | no rule | TG-003 |
| 8 | D-TH-4, 97 | "A law is a statement the theory asserts." | kept | TERM-008 | none |
| 9 | D-TH-6, 102 | "An effect is an operation whose last argument is a bound continuation, so order is written into the term." | fold | TERM-009 (what an effect is), TERM-010 (order) | TG-006, TG-007 |
| 10 | D-TH-6, 102 | "Its multiplicity is owed by every interpretation of the effect: a handler is a rule, and clause (b) of D-UO-3 counts the continuation in it." | fold | TERM-011 (owed by every interpretation), TERM-012 (a handler is a rule) | TG-009 |

## Rule sentences that come from beside the anchor

INFERENCE — Two rules carry words from a second R13 passage, named in the rule's "from". TERM-005 and TERM-007 also cite supporting lines without adding words. They are set out here so a reviewer can check each.

| Rule | Words | From |
|---|---|---|
| TERM-008 | "A law is declared in its theory, as a sort and an operation are." | D-REC-1, line 1046: `law` is a kind of declared symbol |
| TERM-010 | "What runs after an effect is inside that effect's continuation." | D-UO-14, line 166: "everything after an effect is inside its continuation" |
| TERM-005, TERM-007 | no added words; a supporting line only | D-REC-3, line 1069; D-REC-1, line 1053 |

## What is outside this part

SOURCE — D-TH-5 (rules) and D-TH-7 (the three declarations of a sort, and the refusal) are part 2. D-CON-1 is a summary sentence and gets no rule. The record shapes of D-REC-1 to D-REC-4 belong to the record rules.

SOURCE — Slice 1 has no quotation form. [register: `2026-11-12-CODEX-F-REGISTER-EDIT-7-HOST-LANGUAGE\DECISIONS.postimage.md` (SHA-256 `6ed970ec3dfcefe083c2c99521595e887ff1fb9473a9cff932f1b47e12128383`), row 48; recorded there as Claude Arch's own call with S-A.]

END OF COVERAGE-TERMS
