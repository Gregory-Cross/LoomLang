# PROPOSED store coverage, revision 2

SOURCE — One row for each sentence of six passages of R13 (`DESIGN-TEXT-R13.md`, SHA-256 `20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce`): D-STO-1, D-STO-2, D-STO-3 as far as this card goes, D-TM-1, D-REC-3 and D-REC-4. Each sentence is quoted exactly. A program matched every quotation against R13, and checked that the rows for five of the passages use up every word of the passage. For D-STO-3 only the heading sentence and the table's first row are in scope; row 12 below stands for the other ten.

INFERENCE — "Rule here" is a rule of `RULES-STORE.md`. "Cited" is a rule written elsewhere that already holds the sentence, so no rule here repeats it. "Gap" is an entry of `GAPS-STORE.md` unless it carries another file's prefix.

| # | Anchor, line | Sentence | R13 tag | Rule here | Cited | Gap |
|---|---|---|---|---|---|---|
| 1 | D-STO-1, 500 | "The store is one graph, addressed by content." | agreed | STO-001 | none | SG-001 |
| 2 | D-STO-1, 500 | "It holds terms, theories, interpretations, representations, claims, evidence, notes and built artefacts." | agreed | STO-002 | none | none |
| 3 | D-STO-1, 500 | "Anything may add a term, a proposal or a note." | agreed | STO-003 | none | SG-005 |
| 4 | D-STO-1, 500 | "Evidence is a derivation, a run record or a counterexample." | agreed | STO-004 | none | none |
| 5 | D-STO-1, 500 | "A run record is evidence relative to the build it names until the evaluator replays it." | agreed | no rule here | EV-031, EV-032 | none |
| 6 | D-STO-1, 500 | "GAP 4: the bytes that content identity hashes are not given." | R13's own mark | no rule | none | SG-001 (B03, E-16) |
| 7 | D-STO-2, 502 | "A check is cached under the checking program, the claim, and a record of every question it put to the store with the hash of each answer, including the answer that nothing was there." | agreed, not run | STO-005 | REC-013 beside it | SG-002, SG-006, SG-008 |
| 8 | D-STO-2, 502 | "It is reused only while every question still has the same answer." | agreed, not run | STO-006 | none | SG-002 |
| 9 | D-STO-2, 502 | "A new declaration that makes a once-unique default ambiguous therefore reruns the checks that asked." | agreed, not run | STO-007 | none | SG-002 |
| 10 | D-STO-3, 504 | "The queries." | agreed | STO-008 | none | none |
| 11 | D-STO-3, 508 | The table's first row, four cells: "Row of a node"; "The polynomial; its symbols; its reading under a bound"; "A kernel program"; "Yes" | agreed | STO-008 (what it returns), STO-009 (who answers; it can license) | none | SG-003 |
| 12 | D-STO-3, 509 to 518 | The table's ten other rows, from "Status of a claim at a site" to "Find a value that satisfies a predicate" | agreed; two rows approved | no rule and no gap here | none | none here: outside SC-09's named scope; no first-needed slice is established here; QA-20 remains open for the uses result |
| 13 | D-TM-1, 172 | "A term is an expression over theories, stored as a shared graph." | kept | STO-010; PROPOSED marked requirement, standing: DRAFT [provisional: Claude Arch under the owner's overnight record, card 0117, question TM: TM-A] [P0117:TM-A] | none | SG-009 OPEN, owner confirmation pending; no record bytes or runtime admission/refusal fixed |
| 14 | D-TM-1, 172 | "Equal terms are one node." | kept | STO-011 | EV-003 beside it | SG-001 |
| 15 | D-TM-1, 172 | "A defined symbol is identified by its content, a declared symbol by its declaration, and a term by its structure with binders made nameless." | kept | STO-012, STO-013, STO-014 | REC-002 for the numbering | SG-001, SG-004 |
| 16 | D-TM-1, 172 | "Programs, proofs, data and machine code are terms." | kept | STO-015 | none | none |
| 17 | D-TM-1, 172 | "This is about the store and about identity." | working: C22 | no rule and no gap | none | none: a remark on what the passage is about |
| 18 | D-TM-1, 172 | "That two pieces of code are one node is never by that a reason to reuse a run (D-RUN-3)." | working: C22 | no rule here | EV-003 | none |
| 19 | D-REC-3, 1069 | "A node is a value of the evaluator, so the store's graph is the evaluator's interned values and the identity of a node is same." | agreed | STO-016 | EV-003 beside it | SG-001 (B03, E-16); evaluator E-14 for canonicalization and interning |
| 20 | D-REC-3, 1069 | "A sort's declarations are in its signature." | agreed | STO-017 | none | none |
| 21 | D-REC-3, 1069 | "A bound argument's multiplicity is in the signature of its operation." | agreed | no rule here | TERM-005 | none |
| 22 | D-REC-3, 1069 | "The id of a declared symbol is, as a default, its theory's id with its position in the theory, and names are metadata." | agreed | STO-018 | none | SG-004 (TG-002) |
| 23 | D-REC-3, 1069 | "Open: identity across versions of a theory." | agreed | no rule | none | SG-004 (L02) |
| 24 | D-REC-4, 1071 | "The content hash of a defined symbol whose rules name the symbol itself, or of several that name each other: hash the group together, with each member written as its position in the group." | author's, proposed, not run | STO-019 | none | SG-001 (B03) |
| 25 | D-REC-4, 1071 | "GAP 4." | R13's own mark | no rule | none | SG-001 |

## Counts

SOURCE — 25 rows. 17 have a rule here. 3 are held by a rule written elsewhere (rows 5, 18, 21). 3 are held by a gap only (rows 6, 23, 25). 2 have no rule and no gap: row 12, which is outside this card, and row 17, which states no obligation.

## What is outside this card

SOURCE — D-STO-3's ten other queries, D-STO-4 (the walk and the uses, which the row rules cover in draft), D-STO-5 to D-STO-7, D-TM-2 to D-TM-4, and the record shapes of D-REC-1 and D-REC-2.

END OF COVERAGE-STORE
