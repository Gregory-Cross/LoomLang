# Record and binding rules, revision 2

PROPOSED — The four inherited substantial DRAFT contracts remain proposed encodings, bounded by G0180:13-16 and qualified below. REC-005 and REC-006 record only the selected OC-01 A and OQ1 A policies; they supply no chosen encoding or implementation. No adoption beyond the owner records; full REC-D remains gated.

SOURCE — Aliases, raw pins and physical-line convention are in SOURCE_NAMESPACES.json and INPUT_BINDINGS.json. R8 evaluator contracts are cited by number only; their text is not incorporated or edited. G0178:1,18,99 supplies a bounded SOUND disposition with this exact qualification: “Exact paired rules/gaps closure passes; CHANGES matches a separately stated old hash; coverage preservation passes against the reverse-delta candidate; independent old coverage identity and the three unchanged-file comparisons are NOT DONE.” This is source-attributed review evidence, not full record readiness. PLAN:147-148,154 and the current bounded card delimit this authoring task.

SOURCE — Current-round aliases: OC01_RECORD = owner-record-2026-11-11-oc-01-core-let.json; WEB_RECORD = owner-record-2026-11-11-web-oq1-oq3-a.json; ARCH_WEB = the pinned Claude Arch web-round REPORT.md; WEB_DIGEST = the pinned DIGEST.md/DIGEST.json. INPUT_BINDINGS.json binds their exact paths and raw hashes. The earlier aliases and exact G boundaries in REC-001–004 are inherited R1 source locators and historical drafting boundaries, not renewed owner waits or a prohibition on the selected core let. They are not new R2 source verification or acceptance.

SOURCE / INFERENCE — The raw OC-01 owner line (SHA-256 1f991efbcb8fc133b6cd32fd85a499a88fbd65feb9071b4eccd8b705989e78d4) and web owner line (50069223960d1d4728f93e85dae978e195f17b3f1db7f15967540c4162570b43) match the records' session, timestamp and text. The first OC-01 raw line is a peer attachment, despite the record's intervening_human_lines label; it is not owner intent. Raw question lines were not supplied or read, and are not authenticated here. The recorded authorizes_only fields bound this disposition. OQ2/OQ3 concern evaluator rules; these record files select no further policy. Changed bytes reopen review.

## REC-001 — Counted binder and application shapes

- revision: 2

- standing: DRAFT — PROPOSED; no adoption or phase authority.

- kind: proposed requirement

- subject: the proposed abstract Node shape in checked positive parameter-count cases

- from: SOURCE G0180:13,32; NA1_R1:62-78; DESIGN_R5:539,1028-1041 (D-ADM-2, D-REC-1),164,166 (D-TM-1/2)

- text: PROPOSED Use the proposed abstract alternatives `sym(symbol, nodes)`, `lit(sort, value)`, `var(index)`, `lam(count, body)` and `app(function, arguments)`. The node collections are finite and ordered; this leaves their concrete scalar/sequence codec open. Keep the existing symbol and literal fields abstract. Represent one written k-variable binder by one `lam(k, body)` node. In the checked positive-count cases covered here, the count of a binder in a bound-argument position agrees with that checked parameter's declared variables; an application supplies as many arguments as its checked function binds. Obtain counts from checked function/parameter/signature information, including for arbitrary function expressions. This is a proposed completion of R5's unary sketch, not an encoding uniquely required or already adopted by R5.

- case: PROPOSED C01-C05: the representation `lam(2, b)` retains one written binder and differs structurally from `lam(1, lam(1, b))`; the comparison grants no admission to the latter placement. With checked count two, two supplied arguments agree and one does not. A missing checked count leaves a prerequisite missing. The zero-count case remains outside this bounded draft.

- excludes: PROPOSED No selected let-node encoding in this shape contract; REC-005 records the selected core-let scope policy; no normalization that merges written grouped and nested binders; no inferred arity from an arbitrary function node's shape; no lam0 admission or blanket lam0 refusal. Full syntax, sort, literal, placement and use-once checks still apply.

- exact G boundary: SOURCE Checked positive parameter-count cases only. Keep existing symbol/literal fields abstract; no new `let` constructor, zero-variable-parameter admission, complete scalar/sequence codec, quotation policy or content-byte identity is supplied. Count consistency uses checked signature/parameter information.

- gaps: B01-B05; G2-G4/G7-G9/G11/G13; O1; I01/I03/I05.

## REC-002 — Local and canonical rule-variable numbering

- revision: 1

- standing: DRAFT — PROPOSED; no adoption or phase authority.

- kind: proposed requirement

- subject: indices within already checked ordered binding contexts and rule patterns

- from: SOURCE G0180:14,33-34,45; NA1_R1:85-113,149-156; DESIGN_R5:136 (D-UO-10),164,166 (D-TM-1/2),539 (D-ADM-2),564 (D-RUN-2),1031,1041 (D-REC-1)

- text: PROPOSED Number local variables from zero, visiting the innermost binder block first and variables in their written order within each block. Entering a k-variable block shifts every prior index by k. For a rule, visit its first pattern and then subsequent patterns; within each, visit constructor children left to right, depth first. Number each pattern variable at its single encounter from zero through k-1 and set Rule.variables to k. Repetition and a permutation away from this traversal are not canonical. For closed overall terms and their closed subterms, this direct representation supports the same written nameless subnode at different surrounding placements. Open fragments retain their checked context as a separate premise. N3 is conditional on an already supplied ordered external context: this contract selects no canonical order for that context. Recursive-group self-reference is a symbol/member position, not a lexical variable index. Contextual checking and store-sensitive cache evidence remain required even where nodes are equal.

- case: PROPOSED C06-C11: in inner block [a,b] over outer [x], the indices of a,b,x are 0,1,2. Patterns `C(a,D(b)), c` produce `C(var(0),D(var(1))), var(2)` and Rule.variables=3. Repeated variables and traversal permutation fail the small numbering control. C12 compares the body index of a closed identity binder at outer depths zero and one: both local indices are zero, whereas unadjusted root-based levels are zero and one. This is a representation control, not an admission or universal levels theorem.

- excludes: PROPOSED No detached open-fragment equality, context erasure, observable quotation choice, external-context order, universal rejection of normalized/contextual levels, or inference from node equality to execution reuse or cache validity.

- exact G boundary: SOURCE Innermost block first, written order within each block; first pattern then left-to-right depth-first traversal. Closed overall terms and their closed subterms support the direct-node identity rationale. Open fragments retain their checked context as a separate premise; final external-context order, detached identity and quote observability remain G8/G13/G7. This does not reject every normalized level representation.

- gaps: B02/B03/U05/L02; G2/G7-G10/G13; I02/I03.

## REC-003 — Matching value environments and closure capture

- revision: 2

- standing: DRAFT — PROPOSED; no adoption or phase authority.

- kind: proposed requirement

- subject: the proposed environment representation under a preserved matching-environment invariant

- from: SOURCE G0180:15,18,35,37-39; NA1_R1:120-125,132-133,136-138,160-191,196-211; DESIGN_R5:564,566,569 (D-RUN-2/3/4),580-590 (D-RUN-7/8/9),1055 (D-REC-3); EV_R8 EV-043:556-559, EV-074:928-931, EV-064:808,810-811 (citations only)

- text: PROPOSED Represent the empty environment by row() and one value followed by its tail environment by row(value, environment). Enter an obtained block v0 through v(k-1) over E as row(v0,row(v1,...row(v(k-1),E)...)). Lookup follows i second fields and then returns the first field, without rerunning work. Rule entry places its matched values in canonical walk order over an empty environment; defined-symbol rules are top level and bind nothing from outside. Construct a closure when its lam runs, retaining count, body and the current environment. Application evaluates the function, then its arguments left to right, and runs the body with those obtained values entered over the closure's captured environment. Rule entry, binder entry and capture must preserve a well-formed environment matching the checked lexical context, variable order and values. A legitimate stored none remains a value; lexical bounds alone do not establish this matching invariant. An incomplete argument/initializer creates no pending binding. Completed prefix effects/debits need not roll back. Held means unconsumed use-once obligations, not all environment fields; admission refusal, returned none, failed, asked and out-of-fuel remain distinct. These last constraints do not supply their complete schemas or activation-sensitive evidence.

- case: PROPOSED C13-C19: entering [a,b] over [x] yields [a,b,x]. A closure capturing outer value 1, then receiving 2, reads outer index 1 and argument index 0 to return pair(1,2), even if the caller holds 9. A rule block [3,4] swapped by indices returns pair(4,3). Entering [7,8] over [1] gives pair(7,1) at indices 0 and 2. The abstract obtained-value fixture calls work once, stores its ordinary result v and reads pair(v,v) without a second work event; it introduces no core-let translation. Stored none is returned at a valid address. C20-C23 distinguish a missing environment from that value and retain a completed prefix when a later argument stops, with no entered argument block.

- excludes: PROPOSED No storing unevaluated work, extending the caller environment in place of the captured environment, treating all stored fields as held, or runtime-environment validity from S1 alone. The tagged valid-address observation in the checker is a test aid, not a proposed evaluator result wrapper. No activation identity, full evaluator-value/Node/Symbol/function codec, continuation/Ask layout or fuel tariff is provided. This environment draft supplies no core-let execution encoding; REC-005 records the selected scope policy.

- exact G boundary: SOURCE Rule entry, binder entry and capture must preserve a well-formed matching environment. An already supplied external context is ordered consistently with that environment; this does not choose its canonical external order. Only already obtained values are stored. No full evaluator-value codec, dynamic activation identity, complete control/continuation layout or fuel charge follows.

- gaps: B01/B02/B05-B09/U03/U04; G1/G4-G6/G11; O1; I01/I04/I05/I07.

## REC-004 — Supplementary S1-S3 binding checks

- revision: 1

- standing: DRAFT — PROPOSED; no adoption or phase authority.

- kind: proposed requirement

- subject: proposed binding checks before an admitted object's run, in addition to all other admission obligations

- from: SOURCE G0180:16,36,38,59-61,117; NA1_R1:145-156,196-211; DESIGN_R5:136,158,160 (D-UO-10/14/15),539-547 (D-ADM-2..5); EV_R8 EV-043, EV-074, EV-064 by number; EV_GAPS_R8:34,38

- text: PROPOSED Assume valid natural index/count fields and already checked signature/parameter information for the cases covered. S1: each var(i) is below the number of lexically available variables, including the supplied checked context; entering a binder adds its count for its body. S2: each application has the checked function's bound-argument count, and a binder in a bound-argument position has that checked parameter's count. For arbitrary function expressions, obtain this information from checking rather than the node alone. S3: rule patterns contain var(0) through var(k-1) exactly once in the first-pattern, left-to-right depth-first walk, agreeing with Rule.variables. Propose these checks at admission before the object run. They supplement the full syntax, signature, sort, literal, placement, membership and use-once admission requirements, retaining result and host-reply checks where applicable. Refusal starts no refused object run and is not an ordinary returned none. S1 is a lexical check and does not validate an arbitrary runtime environment. This placement supplies no admission/checker price or resource interface.

- case: PROPOSED C24-C31: with lexical width two, index one meets S1 and index two does not. Invalid natural-field fixtures fail the stated metadata premise. S1 can accept index zero at width one while an empty runtime environment fails the separate matching premise. A checked two-argument arbitrary function expression accepts two arguments under S2, but missing checked information is unresolved, not an arity guess. Canonical pattern indices [0,1,2] with Rule.variables=3 meet S3; [1,0,2] and a count mismatch do not. These are finite supplement controls, not a complete admission checker or matcher.

- excludes: PROPOSED No replacement of broader admission, no new narrow-scope use-once exception, no interpretation of missing prerequisites as a normal none, no complete admission/fuel proof, and no free checker or complete whole-program tariff.

- exact G boundary: SOURCE These supplement the full syntax/signature/sort/literal/placement/use-once admission obligations. S2 needs checked function/signature information for arbitrary function expressions. Natural/count field validity is a premise. S1 alone does not validate runtime environments. Admission-before-object-run does not price admission or its checker runs.

- gaps: B02/B04-B09/U01-U05/L01; G6/G8-G12; O1; I01/I04/I05/I07.

## REC-005 — Selected core-let scope; encoding remains open

- revision: 1

- standing: SOURCE — OC-01 A selected by OC01_RECORD; record encoding and checks remain PROPOSED or open. No broader adoption or phase authority.

- kind: requirement

- subject: the selected core let's relationship to its enclosing use-once scope

- from: SOURCE OC01_RECORD authorizes_only and authenticated owner line; WEB_DIGEST F065/F087; inherited O1/B01/I06

- text: SOURCE OC-01 A adds a core let whose body belongs to the enclosing use-once scope, so an ordinary computed value may be used beside an outside use-once value. The no-core-let/narrow-applied-binder refusal branch B and the no-core-let/change-every-applied-binder branch C are not selected. INFERENCE This settles O1's owner outcome only; it does not choose a Node alternative, field order, reader syntax, admission algorithm, evaluation encoding, charge or planner translation.

- case: SOURCE / INFERENCE In O1's schematic f(h) = let y = work(); use(y,h), h is an outer use-once value and work yields an ordinary value: selected A allows the core-let enclosing-scope reading. This schematic is not a chosen concrete reader form or an executed implementation check. PROPOSED Keep a companion control distinguishing this selected core let from a general change to every applied binder.

- excludes: SOURCE / INFERENCE No repeat owner ballot for the answered A/B/C outcome; no automatic applied-binder exception, lam0 admission, detached-quotation policy, planner inlining permission, equal-budget result or full observation proof.

- authority boundary: SOURCE Only the outcome named by OC01_RECORD is selected. PROPOSED Complete faithful let representation, use-once checking, environment/activation preservation and planner obligations through author/reviewer work; any additional observable policy keeps its existing authority route.

- gaps: B01/B02/B05/B07; G1/G6/G7/G9/G11/G13; O1; I01/I04/I05/I06/I07.

## REC-006 — Selected fresh-production identity and reuse condition

- revision: 1

- standing: SOURCE — OQ1 A with Arch's condition selected by WEB_RECORD; representation remains open. No broader adoption or phase authority.

- kind: requirement

- subject: fresh use-once production, consumption identity, and result reuse justified from the same term node

- from: SOURCE WEB_RECORD authorizes_only and authenticated owner line; ARCH_WEB OQ1; WEB_DIGEST OQ1/F002/purityfresh

- text: SOURCE OQ1 A selects a fresh production name for each fresh result; one shared term node does not identify two executions' fresh results. A term may be computed once and its result reused only if all five conditions hold: it makes nothing new; it has no effect; it has no open choice; it consumes nothing use-once; and its result may be copied. State-freedom alone is insufficient. Consumption is counted by the fresh production's semantic identity, not by interned content. INFERENCE These names do not select a counter, concrete namespace, address, wire format or allocation algorithm; node equality does not itself establish the five conditions, execution reuse or cache validity.

- case: SOURCE / INFERENCE ARCH_WEB section 2.2 contrasts make(1, 0) written twice (one node and two sequences, which same tells apart) and a constant of a use-once sort (the same case). PROPOSED Pair a copyable ordinary-result reuse control satisfying all five conditions with separate controls failing each condition. Track two fresh results with equal content as two identities, and retain the required fresh use-once result's obligation when it appears unused or execution later fails. These are proposed controls, not newly run programs or a complete small-term test.

- excludes: SOURCE / INFERENCE No fresh-result sharing or deletion justified by identical code/content, no purity-only reuse test, no merging of consumption counts by interned content, no reuse of an unfinished or invalidated cache result, and no selected activation/capture/held codec. The five conditions are necessary here, not a complete optimizer licence.

- authority boundary: SOURCE Only WEB_RECORD's OQ1 outcome and all five Arch conditions are selected. INFERENCE The fresh-production duty cannot be discharged by leaving the corresponding fresh result unmade (WEB_DIGEST F002); faithful matched-run, failure and held-account evidence remains owed.

- gaps: B07/B09; G1/G4/G5; I02/I04/I07/I11.

SOURCE / INFERENCE — R1's finite-check account is historical author evidence only: its CASES.json and verify_records.py belong to the R1 folder and were not reopened or rerun here. R2's author check covers preservation, structure and selected-policy/gap text only; all newly proposed semantic controls are NOT RUN. No source-author/reviewer program or full core evaluator was run. Every inherited technical gap remains; only the authenticated OC-01/OQ1 owner waits are answered. Changed source needs independent review.
