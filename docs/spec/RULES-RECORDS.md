# Record and binding rules, revision 3

SOURCE — R3 is card0488's bounded record transcription. OWN_IMP3 and OWN_OVERNIGHT supply the stop, whole-held failed-attempt, reporting and grounding decisions carried in R12; OWN_METHOD releases improvements 8/9 for method work but does not approve the exact proposed wording; OWN_WRITE removes the sequence last-place marker. Four supplied raw external-human answers match their records; the write decision is a queued human attachment. Raw questions are not supplied/authenticated; no full transcript was opened. OWNER-LINE-VERIFICATION.json records the scope.

SOURCE / PROPOSED — REC-007–013 state required semantic information from R12 with its standing; their field labels/grouping are author proposals, not selected wire keys or layouts. REC-014/015 transcribe the conditional method proposal, not a claim that it is reviewed/applied or already a conformance gate. REC-016 applies only the selected no-last-place constraint. Existing REC-001–006 binding fields and IDs stay unchanged. No charge, outcome constructor, nonresource stop permission, decoder, ledger implementation or phase authority is supplied.

INFERENCE — The base record files contain zero last-place/head/kept-point fields to remove. REC-016 prevents importing R12:992/994/1004/1006's superseded marker fields into current state/record/kept-point representations; it does not edit R12 or set replacement charges. R12's failed-build G10 means RUN_GAPS:RG-010, not the inherited record gap G10 about name resolution. Reported action outcome, comparison conclusion, and evidence reading (yes/no/unknown/conflict) are separate dimensions.

SOURCE — Current aliases are the 18 exact inputs in INPUT_BINDINGS.json: RECORD_RULES/GAPS/COVERAGE are the R2 base; R12 is DESIGN-TEXT-R12.md; ARCH_IMPROVEMENTS and METHOD_IMPROVEMENTS are the two bound Arch reports; RUN_RULES/RUN_GAPS are RUN1 R2; OWN_*/RAW_* pair each supplied owner record with its raw answer. Physical-line citations refer to these pinned bytes. Earlier aliases and review receipts in the retained R2 text are historical locators only, not newly opened inputs or evidence for changed bytes. Independent R3 review remains pending.

R2 historical preface (retained):

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

- text: PROPOSED Represent the empty environment by row() and one value followed by its tail environment by row(value, environment). Enter an obtained block v0 through v(k-1) over E as row(v0,row(v1,...row(v(k-1),E)...)). Lookup follows i second fields and then returns the first field, without rerunning work. Rule entry places its matched values in canonical walk order over an empty environment; defined-symbol rules are top level and bind nothing from outside. Construct a closure when its lam runs, retaining count, body and the current environment. Application evaluates the function, then its arguments left to right, and runs the body with those obtained values entered over the closure's captured environment. Rule entry, binder entry and capture must preserve a well-formed environment matching the checked lexical context, variable order and values. A legitimate stored none remains a value; lexical bounds alone do not establish this matching invariant. An incomplete argument/initializer creates no pending binding. Completed paid debits are not refunded and already emitted requests remain recorded. An incomplete argument or initializer does not by itself roll back completed prefix effects; any permitted state restoration follows the separately specified handler or kept-point contract. Held means unconsumed use-once obligations, not all environment fields; admission refusal, returned none, failed, asked and out-of-fuel remain distinct. These last constraints do not supply their complete schemas or activation-sensitive evidence.

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

- text: PROPOSED Assume valid natural index/count fields and already checked signature/parameter information for the cases covered. S1: each variable use var(i) is below the number of lexically available variables, including the supplied checked context; entering a binder adds its count for its body. Pattern-variable introductions in a checked defined-symbol rule are binding declarations checked by S3, not uses checked against the pre-match environment. Check that rule's result with its Rule.variables pattern variables available in canonical walk order and no outside bindings; nested binders extend that lexical context. Full pattern syntax, signature, sort and placement checks still apply. S2: each application has the checked function's bound-argument count, and a binder in a bound-argument position has that checked parameter's count. For arbitrary function expressions, obtain this information from checking rather than the node alone. S3: rule patterns contain var(0) through var(k-1) exactly once in the first-pattern, left-to-right depth-first walk, agreeing with Rule.variables. Propose these checks at admission before the object run. They supplement the full syntax, signature, sort, literal, placement, membership and use-once admission requirements, retaining result and host-reply checks where applicable. Refusal starts no refused object run and is not an ordinary returned none. S1 is a lexical check and does not validate an arbitrary runtime environment. This placement supplies no admission/checker price or resource interface.

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

## REC-007 — Resource-stop information and its checking comparison

- revision: 1

- standing: SOURCE — required record content selected by OWN_IMP3 Q1 and OWN_OVERNIGHT Q1; concrete fields/bytes remain PROPOSED/open.

- kind: requirement

- subject: a writer of a record of a resource stop, and a reader of its permission/comparison evidence

- from: SOURCE R12:602 (D-RUN-10),599; ARCH_IMPROVEMENTS:45,47–53; OWN_IMP3 Q1; OWN_OVERNIGHT Q1; RUN_RULES:110

- text: SOURCE A resource-stop record names the resource, cause, program activity, applicable artefact row entry and bound, and binds the stop to the run and tracking claim under which the ordered-prefix and consumption duties are checked. The bindings may name separately kept records. Naming an entry does not establish permission or perform the comparison. If established row/bound evidence forbids the stop, that is a checked violation; missing or unchecked evidence is reported as a deficit and by itself is neither permission nor mismatch. Preserve stopped-for-resource as the run outcome; report checking of prefix/consumption separately. This rule does not classify a failed first-call build.

PROPOSED — Field labels and grouping below describe information, not a wire schema. Requiredness follows the stated source and applicability; references may point to separately kept records where the source permits it.

| Field label | Meaning | Requiredness and standing | Source and owner boundary |
|---|---|---|---|
| resource | The resource for which this run stopped. | SOURCE required for a resource stop. | R12:602; OWN_IMP3 Q1 |
| cause | The actual cause of this resource stop, distinct from merely naming a resource. | SOURCE required for a resource stop. | R12:602; OWN_IMP3 Q1 |
| activity | What the program was doing when the stop occurred. | SOURCE required for a resource stop. | R12:602; OWN_IMP3 Q1 |
| permission_entry_and_bound | The applicable artefact row entry and bound offered as permitting this stop. | SOURCE required information; missing/unchecked evidence is explicitly a deficit, not fabricated permission. | R12:602; OWN_IMP3 Q1 |
| run_and_tracking_binding | The stopped run and tracking claim under which the ordered-prefix and value-consumption comparison is checked. | SOURCE required; may reference records elsewhere; actual comparison completion is separate. | R12:602; OWN_OVERNIGHT Q1 |
| permission_evidence_and_comparison_extent | Which permission, ordered-prefix and consumption obligations are checked, missing or unchecked. | SOURCE required distinctions whenever reporting those claims; names alone prove none of them. | R12:599,602; OWN_OVERNIGHT Q1; OWN_OVERNIGHT Q2 |

- case: PROPOSED NOT RUN. R3-C01: a record names an entry but lacks a checked applicable bound, and no independent violation is established: report the deficit and incomplete comparison, without inferred permission or mismatch. R3-C02: established row/bound evidence forbids the stop: preserve that violation even if comparison work remains unfinished. A permitted resource stop remains stopped, not agreement.

- excludes: SOURCE / INFERENCE No automatic permission from a row label, no mismatch from missing evidence alone, no agreement from a permitted stopped prefix, no compulsory step-by-step ownership trace, and no general permission for depth or another resource.

- gaps: B06/B09/I04/I11/I12; R12:D-JIT-4/G10 and RUN_GAPS:RG-010 stay I13.

## REC-008 — Failed first-call build tied to the whole held account

- revision: 1

- standing: SOURCE — decided fixed-build stop and owner-recorded failed-attempt/whole-held information; fields and links remain PROPOSED/open.

- kind: requirement

- subject: a writer of the fixed first-call failed-build-attempt record and its stopped-run report

- from: SOURCE R12:723 (D-JIT-4),147,595,602; ARCH_IMPROVEMENTS:65,73,169,176; OWN_OVERNIGHT Q1; RUN_RULES:112–114; RUN_GAPS:79–85

- text: SOURCE For the fixed first-call build, record the stopped attempt and reason and bind it to the stopped run's entire unconsumed use-once account: obtained arguments and values in callers, environments, waiting frames, continuations, handler state and owned data. This is required whether or not the build stop is a resource stop. The function has not been entered; there is no spare copy, consumption, drop or host transfer caused merely by stopping. Preserve already-made requests in order and no further requests by the stopped program. Name the part, attempted-build call and reached step. Report the attempt separately from the enclosing stopped run. Classification remains OPEN at RUN_GAPS:RG-010: if resource, REC-007 also applies; otherwise the separate stop rule is still owed. Concrete links, lock/loader contracts and bytes are not supplied.

PROPOSED — Field labels and grouping below describe information, not a wire schema. Requiredness follows the stated source and applicability; references may point to separately kept records where the source permits it.

| Field label | Meaning | Requiredness and standing | Source and owner boundary |
|---|---|---|---|
| attempt_subject_and_part | The failed build attempt and the part it attempted to build. | SOURCE required in the fixed failed-build case. | R12:723; OWN_OVERNIGHT Q1 |
| attempted_call | The call at which that part's first build was attempted. | SOURCE required. | R12:723; OWN_OVERNIGHT Q1 |
| reached_step_and_reason | How far the build attempt got and the actual reason for failure. | SOURCE required; no selected failure taxonomy follows. | R12:723; OWN_OVERNIGHT Q1 |
| stopped_run_binding | The enclosing stopped run, distinct from the failed build action. | SOURCE required; do not report agreement. | R12:595,723; OWN_OVERNIGHT Q1; OWN_OVERNIGHT Q2 |
| whole_held_binding | Every use-once value unconsumed at this call, including handler/continuation/caller obligations as well as arguments. | SOURCE required whether resource or nonresource; not a field containing only arguments. | R12:147,723; OWN_OVERNIGHT Q1 |
| request_boundary | The preserved ordered requests already made and the fact that this stopped program makes no further request. | SOURCE required behavior/evidence boundary; concrete encoding remains open. | R12:723; OWN_OVERNIGHT Q1 |
| classification_dependent_comparison | Resource-stop duties apply only if that classification is established; otherwise a separate stop rule is owed. | SOURCE classification remains OPEN; no constructor, row treatment or permission selected. | R12:602,723; OWN_OVERNIGHT Q1 leaves G10 open; RUN_GAPS:83–85 |

- case: PROPOSED NOT RUN. R3-C03: at a failed first-call build, argument a and a separate handler-held value h are both unconsumed; a record naming only a is incomplete. R3-C04: retain that same complete account, attempt and request boundary with classification unresolved; do not invent stopped(resource,held), a nonresource constructor or a fallback execution.

- excludes: SOURCE / INFERENCE No argument-only held account, no loss/drop/host transfer on stop, no entry into unchecked part code, no implied resource classification or dedicated nonresource row entry, and no assumption that every part was already built.

- gaps: B07/B09/I04/I11/I12/I13; full attempt links, lock/loader and complete held/activation codec remain open.

## REC-009 — Action-qualified report and enclosing-run link

- revision: 1

- standing: SOURCE — report subject/phase/enclosing-run content required by OWN_OVERNIGHT Q2; exact forms and placement remain PROPOSED/open.

- kind: requirement

- subject: a producer of an admission, build-attempt or run report

- from: SOURCE R12:595 (D-RUN-7 reporting),597,700,723; ARCH_IMPROVEMENTS:117,180–184; OWN_OVERNIGHT Q2

- text: SOURCE A report identifies the subject and phase of its admission, build attempt or run. Actions can nest: a build, reply check or produced-value check can occur inside a run. Link the action to its enclosing run when there is one, and report that run's outcome separately when available. Distinguish initial admission refusal (subject execution not begun), refused reply (the existing run remains asked), stopped build attempt, ordinary returned none, failure and fuel exhaustion. Name the actual cause where an action is refused or stopped as REC-007/008/011 require. This is neither a universal outcome constructor nor a selected result/literal-check row. Record versus diagnostic placement remains open.

PROPOSED — Field labels and grouping below describe information, not a wire schema. Requiredness follows the stated source and applicability; references may point to separately kept records where the source permits it.

| Field label | Meaning | Requiredness and standing | Source and owner boundary |
|---|---|---|---|
| action_subject | The particular object or action reported: admission subject, build-attempt subject, or run. | SOURCE required for every report in this scope. | R12:595; OWN_OVERNIGHT Q2 |
| phase | The action's phase; nested checking/building is not collapsed into one linear admission-build-run lifetime. | SOURCE required. | R12:595; OWN_OVERNIGHT Q2 |
| reported_fact_and_actual_cause | What happened, preserving refusal, stopped attempt, ordinary result, failure and exhaustion; actual cause for refusal/stop. | SOURCE distinctions required where applicable; do not invent a cause for an ordinary result or an unselected check outcome. | R12:595,700,723; OWN_OVERNIGHT Q2 |
| enclosing_run | The run within which the action occurred. | SOURCE required when there is an enclosing run; absence is not a fabricated run identity. | R12:595; OWN_OVERNIGHT Q2 |
| enclosing_run_outcome | That enclosing run's outcome, separately from the inner action's report. | SOURCE reported separately when available; unavailable is not success. | R12:595; OWN_OVERNIGHT Q2 |

- case: PROPOSED NOT RUN. R3-C05: distinguish admission refusal before object start from an admitted object returning none. R3-C06: pair a failed first-call build action with its enclosing stopped run; a reply refusal is instead tied to the same asked request/continuation. A completed build of every part is not a report prerequisite.

- excludes: SOURCE / INFERENCE No conflation of a checker/action result with the enclosing run outcome, no ordinary none encoding for refusal, no automatic complete-action success from a successful body, and no chosen diagnostic/record storage or result/literal-check outcome.

- gaps: U04/I04/I09/I12; result-check and literal-check outcomes remain R12:D-ADM-5/E-21.

## REC-010 — Three comparison conclusions with their checked scope

- revision: 1

- standing: SOURCE — agreement, established mismatch or incomplete is required by OWN_OVERNIGHT Q2; concrete evidence/record forms remain open.

- kind: requirement

- subject: a writer or reader of a comparison under matched choices and a D-RUN-9 tracking claim

- from: SOURCE R12:599–602; ARCH_IMPROVEMENTS:27,180–184; OWN_OVERNIGHT Q2; RUN_RULES RUN1-003

- text: SOURCE Use one of agreement, established mismatch or incomplete as the full comparison's conclusion. Agreement needs both runs returned or in corresponding failures and every required request/order, related outcome, failure-held account and value/activation consumption obligation checked, including licensed changes. One checked violation that no continuation can remove establishes mismatch even with other work unfinished. Otherwise identify the unchecked remainder and why it is incomplete, including fuel cut, wait, permitted resource stop, unfinished build-stop comparison or matching requests/outcome with use unchecked. A later cut never erases an established mismatch. Record a permitted resource stop as stopped and state prefix/consumption checking separately; permitted unequal outcomes/held accounts are not themselves mismatches. Open choice retains inclusion in permitted reference runs, not equality of every possible run.

PROPOSED — Field labels and grouping below describe information, not a wire schema. Requiredness follows the stated source and applicability; references may point to separately kept records where the source permits it.

| Field label | Meaning | Requiredness and standing | Source and owner boundary |
|---|---|---|---|
| matched_runs_and_tracking | Which reference and compiled runs, matching choices and tracking claim are compared. | SOURCE required context for this comparison. | R12:599,602; OWN_OVERNIGHT Q2 |
| conclusion | Exactly the applicable conclusion: agreement, established mismatch, or incomplete. | SOURCE required; these are comparison conclusions, not run outcome constructors or evidence yes/no statuses. | R12:599; OWN_OVERNIGHT Q2 |
| checked_obligations_and_evidence | The request/order, outcome/held and compiled consumption evidence and any licensed change checked. | SOURCE required to justify the claimed conclusion; the reference's own count alone does not prove compiled use. | R12:599–602; OWN_OVERNIGHT Q2 |
| irreversible_violation | The checked violation that no continuation can remove. | SOURCE required basis for established mismatch; a mere missing check is not such a basis. | R12:599; OWN_OVERNIGHT Q2 |
| unchecked_remainder_and_reason | What remains unexamined or unchecked, and why. | SOURCE required when incomplete. PROPOSED any separately reported unfinished work does not weaken an established mismatch. | R12:599; OWN_OVERNIGHT Q2 |
| stop_comparison_extent | Whether a permitted stopped prefix and its consumption limits were checked, separately from the stopped run outcome. | SOURCE required when reporting such a resource-stop comparison; never agreement merely from permission. | R12:599,602; OWN_OVERNIGHT Q2; OWN_OVERNIGHT Q1 |

- case: PROPOSED NOT RUN. R3-C07: finished requests/outcomes match but compiled use was not checked: incomplete. R3-C08: a checked duplicate consumption in a completed prefix remains established mismatch after a later fuel cut. R3-C09: a permitted resource stop with checked prefix/count limits remains stopped/incomplete for full agreement, and a permitted held difference is not itself mismatch.

- excludes: SOURCE / INFERENCE No pass from matched values alone, no agreement for a permitted resource stop, no mismatch from allowed differences, no resetting an established violation to unknown, and no equality-of-all-choices requirement.

- gaps: B09/I04/I08/I12; full tracking evidence and rich projections remain open.

## REC-011 — Refusal cause and connected reasons

- revision: 1

- standing: SOURCE — subject and actual cause required by OWN_OVERNIGHT Q2; exact taxonomy, forms and placement remain open.

- kind: requirement

- subject: a producer of a refusal report, including a refused rewrite, representation or build check

- from: SOURCE R12:700 (D-PATH-4); ARCH_IMPROVEMENTS:153,180–184; OWN_OVERNIGHT Q2

- text: SOURCE Identify what was refused and its actual cause. Where applicable distinguish a source-rule violation (rule and place), an unsupported slice form (which form, without declaring the program wrong), an unknown obligation (claim and missing evidence), and exhausted bounded search/check (bound). These reasons are neither exhaustive nor exclusive. Exhaustion itself is unknown, never no, and does not erase an established result. A no is reported as no; conflict carries both pieces without assigning fault. A refused rewrite/representation/build check does not by itself condemn the source program. Preserve connections between overlapping reasons rather than inventing one replacement cause.

PROPOSED — Field labels and grouping below describe information, not a wire schema. Requiredness follows the stated source and applicability; references may point to separately kept records where the source permits it.

| Field label | Meaning | Requiredness and standing | Source and owner boundary |
|---|---|---|---|
| refused_subject_and_cause | The actual refused object/action and why it was refused. | SOURCE required for a refusal report. | R12:700; OWN_OVERNIGHT Q2 |
| violated_rule_and_place | The particular source rule and place of violation. | SOURCE required when a source-rule violation is the reason. | R12:700; OWN_OVERNIGHT Q2 |
| unsupported_form | The form unsupported in this slice. | SOURCE required when applicable; unsupported is not synonymous with wrong. | R12:700; OWN_OVERNIGHT Q2 |
| unknown_claim_and_missing | The unresolved obligation and the evidence missing. | SOURCE required when the reason is an unknown obligation. | R12:700; OWN_OVERNIGHT Q2 |
| exhausted_bound | The bound exhausted by a search or check. | SOURCE required when applicable; exhaustion alone has unknown standing. | R12:700; OWN_OVERNIGHT Q2 |
| no_conflict_and_reason_connections | An established no, both conflicting evidence pieces, and connections among overlapping reasons, as applicable. | SOURCE preserve the actual result and connected reasons; no closed one-of-four cause tag. | R12:700; OWN_OVERNIGHT Q2 |

- case: PROPOSED NOT RUN. R3-C10: an unsupported representation is named without calling the source program invalid. R3-C11: an exhausted search plus a separately established no keeps the no and names the exhausted bound; a conflict reports both evidence pieces without invented blame.

- excludes: SOURCE / INFERENCE No exhaustive or exclusive four-reason enum, no exhaustion-as-no, no erasure of an existing finding, and no mandatory durable-record placement selected over diagnostics.

- gaps: U04/I04/I09/I12; exact reason links, identifiers and record/diagnostic placement remain open.

## REC-012 — Host-reply ownership in attempt and run records

- revision: 1

- standing: SOURCE — host ownership until acceptance selected by OWN_IMP3 Q2; paid-preparation/commit order stays PROPOSED.

- kind: requirement

- subject: a writer of host-reply checking/acceptance records and the run's held account

- from: SOURCE R12:597 (D-RUN-8),595; ARCH_IMPROVEMENTS:93–103; OWN_IMP3 Q2; RUN_RULES RUN1-002

- text: SOURCE Until acceptance, reply-carried use-once values remain the host's and are not added to the run's held account; checking or refusal does not consume, drop or transfer them. A failed preacceptance charge likewise leaves ownership with the host and the run's held account unchanged, without selecting the run's outcome. A refused reply remains tied to the same asked request and continuation. PROPOSED The candidate sequence is successful check, all successful paid preparation, then one ownership commit with values accounted for before continuation use. After commitment, a later stop accounts for the admitted values under the existing held rule. No identity encoding, unpaid-charge outcome or other preparation-failure mapping is selected.

PROPOSED — Field labels and grouping below describe information, not a wire schema. Requiredness follows the stated source and applicability; references may point to separately kept records where the source permits it.

| Field label | Meaning | Requiredness and standing | Source and owner boundary |
|---|---|---|---|
| request_reply_and_check_subject | The reply attempt and its existing request/continuation, distinguished from the enclosing run. | SOURCE record/report distinctions required; exact linkage fields remain PROPOSED/open. | R12:595,597; OWN_IMP3 Q2; OWN_OVERNIGHT Q2 |
| ownership_before_acceptance | Reply values remain host-owned; they are not part of the run's held account before acceptance. | SOURCE required ownership boundary, also for refusal or unpaid preacceptance charge. | R12:597; OWN_IMP3 Q2 |
| check_preparation_and_commit_evidence | Which checking/preparation succeeded and was paid, and the one commit where ownership passes. | PROPOSED conditional protocol fields; no charge or selected implementation. | R12:597; ARCH_IMPROVEMENTS:95,103 (order PROPOSED); OWN_IMP3 Q2 covers ownership only |
| held_after_acceptance_or_stop | Accepted values accounted to the run before continuation use and in later stop accounting; preacceptance values stay host-owned. | SOURCE ownership consequence; ordering/encoding follows the separately PROPOSED protocol. | R12:147,597; OWN_IMP3 Q2 |

- case: PROPOSED NOT RUN. R3-C12: refusing a reply carrying h preserves host ownership and the same asked request; h is not newly run-held. R3-C13: a precommit payment failure preserves that boundary without naming a run outcome. A proposed successful commit transfers once; a subsequent stop retains the newly admitted unconsumed h.

- excludes: SOURCE / PROPOSED No transfer merely on validation, no double commit or precommit continuation use, no assumption that every output/reply signature is fixed, no host-identity codec and no guessed fuel/preparation outcome.

- gaps: B08/U04/I04/I09/I12; protocol/charges, attempt links and outcome mapping remain open.

## REC-013 — Grounded support, route context and unfinished dependencies

- revision: 1

- standing: SOURCE — self-only and mutually-only support give no support under OWN_IMP3 Q3; record grouping remains PROPOSED.

- kind: requirement

- subject: an evidence reader and a writer recording the grounds, context and unresolved support of its reading

- from: SOURCE R12:445 (D-RL-4),501 (D-STO-2); ARCH_IMPROVEMENTS:135–141; OWN_IMP3 Q3

- text: SOURCE A positive reading needs finite grounded support. Revisit of the same claim at the same site, bound and store state supplies no support from that route, not a no for the claim. Read independent evidence separately; independent yes and admitted no can still conflict, and no yes/no leaves unknown with unresolved support identified. An assumption allowed by name remains an assumption, not evidence that makes it yes. Distinguish unfinished chains from completed context-bound readings; a result depending on an unfinished chain is not reused as unconditional. PROPOSED Records supporting a claimed reading expose the information below; R12 requires the reader behavior but does not mandate a durable support graph or prescribe these fields. These labels make the existing distinctions inspectable without creating a cache implementation or conformance gate. SOURCE R12:445's current mixed-premise/alternative-reading text is a source boundary; this rule transcribes the grounded-support record consequence, not a new status election.

PROPOSED — Field labels and grouping below describe information, not a wire schema. Requiredness follows the stated source and applicability; references may point to separately kept records where the source permits it.

| Field label | Meaning | Requiredness and standing | Source and owner boundary |
|---|---|---|---|
| claim_site_bound_store | The claim, use site, bound and store state under which this support route is read. | SOURCE required context for deciding whether a revisit is the same contextual claim. | R12:445; OWN_IMP3 Q3 |
| support_route_and_grounded_pieces | The particular route and its finite grounded supporting evidence; alternatives remain separately readable. | SOURCE positive reading needs grounded support; field labels/route encoding PROPOSED. | R12:445; OWN_IMP3 Q3 |
| unresolved_support_and_assumptions | The unresolved chain/assumptions and why a route yields no support or remains unknown, without treating a named assumption as yes. | SOURCE distinctions required when applicable. | R12:445; OWN_IMP3 Q3 |
| completion_and_cache_dependencies | Whether the reading is completed in its context or relies on an unfinished chain; cached checking premises include store answers and absence. | SOURCE retain dependencies; no unconditional reuse from an unfinished chain; concrete cache binding remains open. | R12:445,501; OWN_IMP3 Q3 covers grounded support; D-STO-2 remains source-qualified agreed/not-run |

- case: PROPOSED NOT RUN. R3-C14: a supports b and b supports a at one site/bound/store, with no independent grounds: the cycle supplies no support, not a no. R3-C15: add an independent grounded positive piece; keep that route readable. A bounded unfinished traversal is neither a completed yes nor an unconditional cached result.

- excludes: SOURCE / INFERENCE No cycle-as-proof, no blanket negative verdict from a circular route, no erasure of independent grounds/conflicts, no permission-as-evidence, and no content-hash-only context or cache proof.

- gaps: I02/I08/I12; concrete support graph, current reader integration and context/cache encodings remain open.

## REC-014 — Four population counts in applicable test reports

- revision: 1

- standing: PROPOSED — transcription of METHOD_IMPROVEMENTS R1 under OWN_METHOD's released hold; exact words/review/application are not owner-adopted here.

- kind: proposed requirement

- subject: a producer and record writer for a new test run over generated or enumerated inputs, including each control

- from: SOURCE METHOD_IMPROVEMENTS:5–6,42,58,95,200,225,235–239; OWN_METHOD (items8/9 hold release); no R12 field source

- text: PROPOSED For each applicable run, carry generated, admitted, reached and compared counts: distinct inputs made; inputs passing every check before the thing under test; inputs whose execution reached it; inputs given an oracle comparison verdict. They are nested populations, so generated>=admitted>=reached>=compared, and the statement covers the compared set only. The harness counts them; a writer does not estimate or repair them later. Each check and each control has its own four. Report a measured zero explicitly alongside the other measured counts, and state the main reason for the largest neighbouring drop when there is a drop. Compared=0 means nothing was checked, whatever exit code the command returned. INFERENCE A measured zero at any earlier stage requires zero at later stages by nesting; this does not permit manufacturing zeros for absent measurements. The source does not prescribe a tie or no-drop encoding. PROPOSED For a comparison of agreement with the reference run, fuel exhaustion alone supplies no verdict and is not compared; an irreversible prefix mismatch counts for disagreement and survives a later fuel cut. Missing counts are absent, not zeros: read that record as ran, population not shown. Applicability is not every derivation, note or proof. Earlier records are not rewritten; this proposal neither invalidates an old trial merely for absent new fields nor enlarges its evidence.

PROPOSED — Field labels and grouping below describe information, not a wire schema. Requiredness follows the stated source and applicability; references may point to separately kept records where the source permits it.

| Field label | Meaning | Requiredness and standing | Source and owner boundary |
|---|---|---|---|
| counts.generated | Distinct inputs generated or enumerated for this run. | PROPOSED required for an applicable new run; no count for unrelated non-run records is invented. | METHOD_IMPROVEMENTS:42,58,237; OWN_METHOD releases item8, not exact words; R12 not applicable |
| counts.admitted | Those generated inputs passing every prerequisite before the tested thing. | PROPOSED required; at most generated. | METHOD_IMPROVEMENTS:58,237; OWN_METHOD item8 release |
| counts.reached | Those admitted inputs whose run reaches the tested thing. | PROPOSED required; at most admitted. | METHOD_IMPROVEMENTS:58,237; OWN_METHOD item8 release |
| counts.compared | Those reached inputs compared with the oracle to a verdict; includes established prefix disagreement, excludes fuel-cut-only non-verdicts. | PROPOSED required; at most reached; zero explicitly means checked nothing. | METHOD_IMPROVEMENTS:58,95,237; OWN_METHOD item8 release |
| population_drop_reason_and_compared_scope | Main reason for the largest adjacent drop when one exists, and the actual compared set bounding the claim; tie/no-drop representation is unspecified. | PROPOSED required in applicable reports; neither monotonicity nor scope errors are silently repaired. | METHOD_IMPROVEMENTS:58,237–239; OWN_METHOD item8 release |
| count_presence_and_per_control_counts | Whether the producer supplied counts, and the separate four for each check and each control run. | PROPOSED missing means absent/population not shown, not fabricated zero; each check and control carries its own counts. | METHOD_IMPROVEMENTS:58,237,239; OWN_METHOD item8 release |

- case: PROPOSED NOT RUN. R3-C16: 10 generated, 8 admitted, 3 reached, 0 compared reports checked nothing and identifies the largest drop 8 to 3. R3-C17: missing counts are absent, not 0/0/0/0. R3-C18: one prefix mismatch followed by fuel exhaustion counts as a compared disagreement; a pure fuel cut with no established violation does not. Each corresponding control keeps its own four.

- excludes: PROPOSED No exit-code-as-coverage, generated-as-compared substitution, invented zero, unmeasured retrospective estimate, count repair, universal four-count requirement on non-run evidence, or rewriting of earlier records.

- gaps: I14; method exact-word review/application, harness population accounting and ledger integration remain open.

## REC-015 — Transfer account from an examined model to the named subject

- revision: 1

- standing: PROPOSED — transcription of METHOD_IMPROVEMENTS R1 under OWN_METHOD's released hold; an account does not prove its own steps.

- kind: proposed requirement

- subject: a producer or reader of a new result examining a model/fixture instead of the rule's named subject

- from: SOURCE METHOD_IMPROVEMENTS:5–6,127–144,200,205–210,226–239; OWN_METHOD item9 release; no R12 field source

- text: PROPOSED When the examined thing is a paper model, another-language model or finite fixture rather than the rule's subject, the record names that model by hash as its subject and says so in its statement. Give a transfer account or explicit none. An account names the intended subject by kind and by hash once it exists, maps the relevant model parts to subject parts, and marks every unshown step as an assumption. A step counts only when a separate evidence record shows it; the account itself is not that evidence. None leaves a model result only, able to challenge rule text or a case but not establish subject conformance. With an account, show it under the intended subject as a model result with open assumptions, never plain yes while any is open. A model used only as oracle for the real subject that ran needs no transfer account and is named in the evidence row. No prior record is edited or reopened; a transfer assumption is no automatic waiver of a rule.

PROPOSED — Field labels and grouping below describe information, not a wire schema. Requiredness follows the stated source and applicability; references may point to separately kept records where the source permits it.

| Field label | Meaning | Requiredness and standing | Source and owner boundary |
|---|---|---|---|
| examined_subject_and_statement | The actual examined model/fixture by hash, and a statement scoped to that model. | PROPOSED required when model/fixture replaces the rule's subject. | METHOD_IMPROVEMENTS:144,237; OWN_METHOD item9 release; R12 not applicable |
| transfer | The account carrying the result to the intended subject, or explicit none. | PROPOSED required for this applicability; none means model-only evidence, not a conformance result. | METHOD_IMPROVEMENTS:127–144,239; OWN_METHOD item9 release |
| intended_subject | The intended subject's kind and hash once it exists. | PROPOSED required within an account; no invented hash for a nonexistent subject. | METHOD_IMPROVEMENTS:144,237; OWN_METHOD item9 release |
| correspondence_and_steps | Which model part answers to which subject part, and the steps carrying the result. | PROPOSED required within an account; prose mapping alone is not proof. | METHOD_IMPROVEMENTS:144; OWN_METHOD item9 release |
| open_assumptions_and_step_evidence | Every unshown step as an assumption; separate evidence records for steps claimed shown. | PROPOSED required within an account; open assumptions prohibit a plain subject yes. | METHOD_IMPROVEMENTS:144,210,237–239; OWN_METHOD item9 release |
| oracle_only_model_reference | A model used solely as oracle when the real subject was examined. | PROPOSED name it in the evidence row; no transfer account is required merely for this oracle role. | METHOD_IMPROVEMENTS:144,237–239; OWN_METHOD item9 release |

- case: PROPOSED NOT RUN. R3-C19: a Python fixture checks an abstract rule but no named subject ran: subject=model hash and transfer=none, model-only result. R3-C20: an account leaves the codec correspondence unshown: record that assumption and do not display plain subject yes. R3-C21: the actual subject ran against a model oracle: name the model in the row, without demanding a transfer account for its oracle role.

- excludes: PROPOSED No relabelling a model hash as the subject hash, no account-as-self-proof, no subject qualification from transfer=none, no hidden open step, no owner waiver from an account, and no retroactive rewriting of historical evidence.

- gaps: I08/I14; each transfer step's evidence, exact-word review/application and ledger integration remain owed.

## REC-016 — Current sequence records carry no last-place marker

- revision: 1

- standing: SOURCE — OWN_WRITE selects no sequence last-place marker; this record consequence changes no charge.

- kind: requirement

- subject: a writer or reader of current sequence state, run-record and kept-point representations

- from: SOURCE OWN_WRITE authorizes_only and authenticated RAW_WRITE; CARD item3; R12:992,994,1004,1006 are legacy marker-bearing text, not current marker authority

- text: SOURCE A sequence carries no last-place marker. Current state, run-record and kept-point representations do not carry that marker. INFERENCE The three R2 record files contain no such field, so there is no existing removal span. Do not import the older starting/final/saved/restored marker fields from R12 into these current records. Preserve all independently required sequence contents, identity, held obligations and other state information; binder/member positions and next-activation or fresh-sequence counters are different matters. This does not specify a replacement write/restoration charge, restoration phase, concurrency protocol or codec migration. Historical source/evidence is not rewritten.

PROPOSED — Field labels and grouping below describe information, not a wire schema. Requiredness follows the stated source and applicability; references may point to separately kept records where the source permits it.

| Field label | Meaning | Requiredness and standing | Source and owner boundary |
|---|---|---|---|
| sequence_last_place | The removed per-sequence last-access/last-place marker, including initial/final and kept-point saved/restored copies. | SOURCE excluded from current semantic state/record/kept-point fields; zero such fields occur in the base files. | OWN_WRITE; CARD item3; supersedes marker portions of R12:992/994/1004/1006 for this scope |
| independent_sequence_and_state_information | Contents, sequence identity, held obligations and separately required bindings/frames/handlers/counters. | SOURCE existing duties remain; no unrelated field is removed because it contains a position or count. | R12:587–592,992,1004 (non-marker portions); OWN_WRITE removes only the marker here |

- case: PROPOSED NOT RUN. R3-C22: proposing a last-place field for each reachable sequence in a new starting/final/kept-point record contradicts the selected marker removal. Removing that field alone does not establish codec, replay or restoration validity; retain the same contents/identity/held obligations.

- excludes: SOURCE / INFERENCE No substituted distance charge or guessed new tariff, no deletion of binder positions or sequence contents, no restored fresh-name supply, no retrospective archive edits, and no full restoration/replay claim from field absence.

- gaps: I15; evaluator charges and restoration changes belong to their own review, while codec/dependent-state evidence remains open.
