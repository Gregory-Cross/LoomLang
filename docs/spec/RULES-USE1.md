# Use-once check rules, package revision 3

PROPOSED — DRAFT ONLY. Nine active check rules and one retired R2 rule; peer review and the census are pending. Source-stated working qualifications remain; no rule is fixed or adopted. Binding hashes name the five fields specified by HOW-WE-SPECIFY; RULE-DATA.json records the canonical convention.

SOURCE — The base is the supplied USE1 R2 package; the current design text is R13 SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce. Stable R2 IDs are revised or retired, never reused. USE1-005–010 split duties out of the mixed R2 contracts. The old rule revision field was 1 although the package was called R2; changed inherited rule bindings are revision 2, and new IDs start at revision 1.

PROPOSED — This file covers the check before a run: D-UO-1–5,7,10,14–17, use-once data declarations, the proposed let check and first-build working D-CONC-2/3. D-UO-13 is retired. Run-side and lowering duties are boundary entries below; they are not run or agreement rules in this file. Checked sorts, context, signatures, admitted forms and relevant live-duty facts are explicit premises. A local pass never supplies whole admission.

SOURCE / PROPOSED - R13 D-ATT-3:1018 records core-let outcome A. The old let ballot and exclusion are retired. LT-1 and LT-4-R1 remain proposals, not adopted sections of R13, and every receiving rule stays DRAFT. N-A is a conditional drafting premise subject to UG-013 and prior F2b. OWNER-QUEUE-R3.md:19 defines D-A as refusing constructor bound parameters. That restriction is a marked drafting premise, not an owner answer. The wider R13 D-CONC-2/3 working account stays separately conditional and grants no D-A permission. C has no selected account; UG-003 and BND-LET record only its common part. [P0117:D-A] [P0117:N-A]

PROPOSED — No case or census has run here. The register gate and CENSUS design keep the check, signature record and admission unfixed until the census runs and is reviewed. In particular the let with a use-once initializer and functions in data need those controls. R13:607 and D-WRK-1:1090 retain the working core fallback if a wrong term is accepted.

## USE1-001 — The narrower check refuses outside-consuming binders

- revision: 3
- standing: DRAFT — peer and reviewed census required; no adoption.
- binding SHA-256: 643401a22b70bb3e7a36f7df4c2923ce92da066ff37d1468c1ea3ebb4a3b7b00
- kind: requirement
- subject: the slice 1 use-once checker, with checked scopes, sorts and signatures
- from: SOURCE R13 D-UO-4:131; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-14:166; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-ATT-3:1018; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- rests on: PROPOSED LT-2-R1 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-LET-AND-WATCH-R1\REPLACEMENTS.json /replacements/1; SHA-256 05621d0663bd9e38d2de0b1132007008b8393b0bbd3d8275dbe9ec87b76d8f5c; PROPOSED LT-1 - C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-LET-AND-WATCH\REPLACEMENTS.json /replacements/0; SHA-256 d2215518c3430f44058078cf48667f2d81e9bff9fe676e98f6ad3199e3430c47; PROPOSED LT-4-R1 - C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-LET-AND-WATCH-R1\REPLACEMENTS.json /replacements/2; SHA-256 05621d0663bd9e38d2de0b1132007008b8393b0bbd3d8275dbe9ec87b76d8f5c
- text: PROPOSED Until the full check passes D-UO-15, apply clauses (a) and (b) and refuse every binder whose body consumes a use-once value bound outside it. This includes an immediately applied binder and an output continuation; a binder using only its own use-once parameter does not fail this test alone. Do not install clause (c) as a way around this refusal. Under proposed LT-2-R1, distinguish source scope from elapsed run: an already obtained argument or rule environment may wait while a called defined symbol asks for output. Waiting across that call is not an extra refusal. Output written inside a let initializer is read as output inside an argument and lifted over the rest of that initializer, the let body and whatever follows the let in the scope it stands in; its continuation is refused if it uses an outside use-once value. The narrower rule ends with slice 1. The let itself is checked by USE1-009.
- case: PROPOSED With admitted schematic signatures, h use-once, ordinary work() and use(y,h) using h once, the core let f(h)=let y=work();use(y,h) does not fail this refusal, while its applied-binder form whose body uses outside h does. Under LT-2-R1, let y=say(b);finish(h,y) is not additionally refused when say asks for output with a continuation capturing no outside use-once value; the directly written output whose continuation uses h is refused. These are conditional clause outcomes, not whole admission.
- excludes: PROPOSED An exemption for immediate application, a blanket ban on a value waiting across a call, ending an effect continuation at the initializer, or admitting the direct-output form by choosing the pending output question.
- gaps: UG-002, UG-004, UG-009, UG-010, UG-012

## USE1-002 — Count one site per root path in the making scope

- revision: 2
- standing: DRAFT — peer and reviewed census required; no adoption.
- binding SHA-256: a30abd9840e16a2fd00e812f3847824ca4d86b130c2b21a9ebe30935b0e5fa09
- kind: requirement
- subject: the use-once site counter on a checked finite scope graph
- from: SOURCE R13 D-UO-2:125; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-3:128; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-7:137; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-10:144; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- rests on: PROPOSED CR-2 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-OWNER-PAGES-R1\REPLACEMENTS.json /replacements/1; SHA-256 256489928043460a4ad9dc343ee995a0466b76b31d8d1fd95a83f8d00b3936d0; PROPOSED CR-5 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-OWNER-PAGES-R1\REPLACEMENTS.json /replacements/4; SHA-256 256489928043460a4ad9dc343ee995a0466b76b31d8d1fd95a83f8d00b3936d0; PROPOSED CR-7 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-OWNER-PAGES-R1\REPLACEMENTS.json /replacements/6; SHA-256 256489928043460a4ad9dc343ee995a0466b76b31d8d1fd95a83f8d00b3936d0
- text: PROPOSED For each applicable use-once value require exactly one site in the scope that makes it; each use-once pattern variable owes exactly one site on its rule right side. A site is an argument occurrence reached along a root path. Count both paths to a shared node, and never combine sites from distinct binders. Handing on a scope result is one site, including its result position. A scope whose last operation is failure gives that failure as the site of a still-held use-once value with no other site; do not add this site where another site is written. Counts may saturate at two: zero, one, more than one. Under proposed CR-2, an operation-result occurrence is a value at that occurrence, while two paths to a variable are two sites of one value. Under proposed CR-7, count sites without deciding whether the runtime event consumes or moves. This chooses no answer to question C. D-UO-10 states a one-value capped graph-count bound; it does not establish a bound for the whole check, which stays in UG-006.
- case: PROPOSED For g(d,d) with d=read(x), the shared read(x) node is reached twice and x has two sites, so the check refuses. A single hand-on of h as the scope result has one site. In pair(fail(e),read(h)), the written read(h) remains h’s site; the failure does not add a second static site, and run retention belongs to BND-RUN-12.
- excludes: PROPOSED Counting shared nodes only once, treating static sites as chosen consuming events, combining two binders, omitting result sites, adding an unconditional failure site, or claiming whole-check linearity.
- gaps: UG-001, UG-002, UG-003, UG-005, UG-006, UG-007, UG-012

## USE1-003 — A variable-bearing check is keyed by node and context

- revision: 3
- standing: DRAFT — peer and reviewed census required; no adoption.
- binding SHA-256: 12497bb010e951a9320f475c27dbf2cb5ed96e8510ebd97d86c2fe4d7fb2d23e
- kind: requirement
- subject: a cache used by the use-once checker or its membership prerequisite
- from: SOURCE R13 D-UO-10:144; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- rests on: SOURCE R13 only; no named amendment dependency.
- text: PROPOSED A check of a node containing variables is a check in the context giving their sorts. Retain both node and that context in its check-cache key. The context holds each variable's use-once standing beside its sort: the declared multiplicity of a bound parameter's variable, and a parameter read as use-once under USE1-007; a pass under one standing never discharges a check under another. This applies to use-once and sort membership. Node identity alone cannot reuse the verdict under a different context. The key does not supply the store’s other evidence, answer-validity or reread conditions, nor a runtime activation identity.
- case: PROPOSED The same variable-bearing code node checked with x at an ordinary sort and with x at a use-once sort has distinct check keys; the ordinary-context result cannot discharge the use-once-context obligation.
- excludes: PROPOSED A node-only key, equating lexical context with obtained-value environment, or using the key as a complete cache-validity proof.
- gaps: UG-001, UG-004, UG-005, UG-006, UG-012

## USE1-004 — R2 run and agreement contract retired to boundaries

- revision: 2
- standing: RETIRED — historical ID retained; see replacement boundaries.
- binding SHA-256: 9ca35bba0b586f01e44315f28e27f898c455d2197b0b318aa408a9cb6ffa1221
- kind: requirement
- subject: historical R2 mixed run/agreement contract
- from: SOURCE R13 D-UO-6:135; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-9:142; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-11:146; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-12:148; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-RUN-9:600; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- rests on: SOURCE R13 only; no named amendment dependency.
- text: PROPOSED RETIRED in this file. R2 mixed run outcomes, consumption and optimizer/lowering agreement. Card 0499 assigns those obligations to the run and agreement files. BND-RUN-09, BND-RUN-11, BND-RUN-12 and BND-AGREEMENT name the promises and their source; they introduce no run or lowering rule here.
- case: PROPOSED Historical O/P examples remain evidence only for their old bindings and are NOT RUN or transferred to this revision.
- excludes: PROPOSED Treating this retired ID as an active use-once-check rule or as a run/agreement implementation.
- gaps: UG-007, UG-008, UG-011, UG-012
- replaced by: BND-RUN-09, BND-RUN-11, BND-RUN-12, BND-AGREEMENT

## USE1-005 — Scope and use-once value in the retained one-mark check

- revision: 2
- standing: DRAFT — peer and reviewed census required; no adoption.
- binding SHA-256: ee6260869716fbee38858adce3b28e296264427bef10b3a46fda99636804bc50
- kind: definition
- subject: the values and scopes to which the pre-run check applies
- from: SOURCE R13 D-UO-1:123; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-3:128; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-17:160; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-17:161; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-17:162; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- rests on: PROPOSED LT-1 - C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-LET-AND-WATCH\REPLACEMENTS.json /replacements/0; SHA-256 d2215518c3430f44058078cf48667f2d81e9bff9fe676e98f6ad3199e3430c47; PROPOSED LT-4-R1 - C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-LET-AND-WATCH-R1\REPLACEMENTS.json /replacements/2; SHA-256 05621d0663bd9e38d2de0b1132007008b8393b0bbd3d8275dbe9ec87b76d8f5c
- text: PROPOSED A scope is a binder body, a rule right side or a whole term. A use-once value is a bound or pattern variable at a use-once sort, or a node of such a sort, including an operation result, or a pattern variable for a bound parameter declared one, which is a use-once function in its rule (R13 D-UO-3:128, USE1-006); the full clause (c) can also make a function use-once, but the narrower rule refuses that outside-consuming binder. Each rule is its own scope. Case analysis on a use-once value is written as rules that take it as an argument. The current check has one exactly-once mark. Separate no-copy and no-drop marks are a recorded direction, not a second implemented setting here; their capture, declaration, function and census consequences stay in UG-002. That a core let body is no separate binder scope is decided (R13 D-ATT-3:1018, outcome A); its proposed record and check are specified only by USE1-009.
- case: PROPOSED A use-once pattern variable in one rule owes its own right-side site; a site in another rule or another binder does not belong to that obligation. A zero-site or two-site value fails USE1-002 under the current single mark.
- excludes: PROPOSED Treating every graph node as one dynamic value, gathering obligations across rules, applying two marks now, or making the let into an applied binder.
- gaps: UG-001, UG-002, UG-005, UG-009, UG-012

## USE1-006 — A declared-one pattern function retains its call duty

- revision: 2
- standing: DRAFT — peer and reviewed census required; no adoption.
- binding SHA-256: 2683a854519d5f5e4c8fa6c06dcc1f6e828864121c7a651371485139ac356889
- kind: requirement
- subject: the use-once checker for a rule taking a bound parameter declared one
- from: SOURCE R13 D-UO-3:128; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-5:133; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-CONC-3:611; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- rests on: PROPOSED TH-1-R2 — C:\Users\grego\.codex\reviews\2026-11-13-CLAUDE-ARCH-SLICE-1-WORDS-R2\REPLACEMENTS.json /replacements/0; SHA-256 ac9020d106544ea1d0467147f4d83d51a7a9e805891cef1ed26fc7ec177b3a11; PROPOSED UO-1 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-OPEN-SLICE-1\REPLACEMENTS.json /replacements/1; SHA-256 d2552ab511c8eeda7a08f258cd86c1006afd6225d3dd5ff48ddad982ff61112b
- text: PROPOSED Treat the pattern variable for a bound parameter declared one as a use-once function even if it captures nothing. Require one site and the placement permitted by USE1-007; one passing occurrence to a taker that calls twice does not discharge the duty. Under proposed TH-1-R2, one and any describe numbers of calls in a run, not textual occurrences: one carries the duty to call once, with no second call; a returning scope calls it once or passes the duty on once, at a permitted parameter declared one or at another position USE1-007 permits. Passing does not erase the duty. Holding it in data, taking it out and handing it on retain that call duty; only running it discharges the duty, with returned values owed in their own right. R13 D-UO-3:128 (approved, as forced move 9) keeps this pattern-function duty and clause (d) in slice 1 beside the narrower rule; proposed UO-1 restates it. Runtime event identity at its first binding or handoff is not defined here: it waits on C. Return, divergence and stopped-run qualifications are BND-RUN-11 and BND-RUN-12.
- case: PROPOSED relay(h)=twice(h) with h declared one is refused even if h is written once: the any/twice taker is not a permitted one-duty site. outer(g)=inner(g) with both parameters declared one may pass this local duty if inner has one permitted site; other checks remain.
- excludes: PROPOSED Counting one textual pass as proof of one call, requiring termination, losing an outstanding duty during handoff, or drafting a first-binding/consuming event under C.
- gaps: UG-002, UG-003, UG-004, UG-012, UG-014

## USE1-007 — Use-once functions stand only at permitted positions

- revision: 3
- standing: DRAFT — peer and reviewed census required; no adoption.
- binding SHA-256: 95c77b8a5a20194024495218ab74b948d8fea52e85ad1cffc97432eb4f1e4e22
- kind: requirement
- subject: the pre-run use-once checker at function-taking positions
- from: SOURCE R13 D-UO-5:133; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-CONC-2:609; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-CONC-3:611; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- rests on: PROPOSED UO-1 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-OPEN-SLICE-1\REPLACEMENTS.json /replacements/1; SHA-256 d2552ab511c8eeda7a08f258cd86c1006afd6225d3dd5ff48ddad982ff61112b
- text: PROPOSED Check function positions against the R13 working account, subject to the marked D-A scope restriction below. R13 D-CONC-2:609 names five working positions: application; a bound parameter declared one; a bound parameter of an operation whose rule is in the term and passes the check with that parameter read as use-once; a constructor bound parameter of multiplicity one; and the result of its scope. Under the marked D-A premise, refuse constructor bound parameters, including those declared one; declaring the data sort use-once supplies no exception. The wider account is conditional working text, and its constructor permission is not available under D-A. The remaining permissions stay conditional on the selected reviewed scope and grant no new owner answer. Where the operation has several rules, the third position needs every rule that can take the call to be in the term and to pass that check; one passing rule is not enough. The working account never permits a use-once function at a constructor parameter of multiplicity any. Under a separately reviewed scope admitting functions in data, holding calls nothing and the later call duty remains owed. The narrower outside-capture refusal still applies. A core-let initializer is no sixth position. No rule is fixed before the required census and review; a wrong accepted term invokes D-WRK-1. No scheduler or handler protocol is supplied. [P0117:D-A]
- case: PROPOSED Under the marked D-A premise, constructor bound parameters are refused at either one or any, even if the data sort is declared use-once. A use-once function as a core-let initializer is refused too. Only in a separately reviewed scope admitting the wider R13 working account could a constructor parameter declared one clear this position check, with USE1-008 and USE1-006 still owed; that is no D-A pass or whole admission. [P0117:D-A]
- excludes: PROPOSED A sixth let-initializer position, holding a use-once function at multiplicity any, or unconditional acceptance of all functions in data before D and the census.
- gaps: UG-002, UG-003, UG-004, UG-009, UG-012, UG-014

## USE1-008 — A data declaration exposes every use-once field duty

- revision: 3
- standing: DRAFT — peer and reviewed census required; no adoption.
- binding SHA-256: 914addb77093a1484faff3fd9e9e49f6436020e365e2d1ff09bccc6dde5921c8
- kind: requirement
- subject: the declaration check for data sorts with use-once content
- from: SOURCE R13 D-TH-7:104; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-TH-7:105; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-CONC-2:609; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-CONC-3:611; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- rests on: SOURCE R13 only; no named amendment dependency.
- text: PROPOSED Refuse a data sort declaration whose constructor takes a use-once argument unless the sort is declared use-once; name an offending field and never change the declaration silently. Under the marked D-A premise, constructor bound parameters are refused; a use-once data declaration supplies no exception. Separately, the wider working D-CONC-2 account requires a data sort holding a function at multiplicity one to be declared use-once, and propagates that duty to every data sort holding a value of it. Its declared-any function is ordinary in the rule taking the datum apart and cannot conceal a use-once function forbidden by USE1-007. Those wider obligations supply no D-A permission. The retained single mark supplies no copying or dropping law. This refusal floor chooses no first-field versus all-fields report policy and no representation. [P0117:D-A]
- case: PROPOSED An ordinary Box declaration with a use-once field h is refused and an offending field is named; otherwise using a bound box twice could duplicate its field. Under D-A a Task constructor holding a bound function is refused even if Task is declared use-once. In a separately reviewed scope admitting the wider R13 working account, a multiplicity-one function field would require a use-once data sort and retain its later call duty; that is no D-A exception. [P0117:D-A]
- excludes: PROPOSED Making a data sort use-once silently, omitting transitive containment, reporting no offending field, or dropping a datum that holds a non-droppable value.
- gaps: UG-002, UG-004, UG-005, UG-012, UG-014

## USE1-009 — The proposed core let belongs to its enclosing check scope

- revision: 2
- standing: DRAFT — peer and reviewed census required; no adoption.
- binding SHA-256: 868cddaf59b1dc7892fc90165c765cc23d3b8b6c405845ec0e006132c90ad602
- kind: requirement
- subject: the use-once checker on the proposed core-let record
- from: SOURCE R13 D-ATT-3:1018; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-1:123; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-2:125; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-14:166; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- rests on: PROPOSED LT-1 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-LET-AND-WATCH\REPLACEMENTS.json /replacements/0; SHA-256 d2215518c3430f44058078cf48667f2d81e9bff9fe676e98f6ad3199e3430c47; PROPOSED LT-4-R1 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-LET-AND-WATCH-R1\REPLACEMENTS.json /replacements/2; SHA-256 05621d0663bd9e38d2de0b1132007008b8393b0bbd3d8275dbe9ec87b76d8f5c
- text: PROPOSED Under proposed LT-1 and LT-4-R1 D-ATT-4/D-ATT-5, the core let is its own node, distinct from an applied binder. Its body begins no check scope; count initializer and body sites in the enclosing scope. A value standing as the whole let body has that body position as its one site, and the let's own result has its site where the let stands. An outside use-once value used in that body has an enclosing-scope site, so the let itself causes no outside-capture refusal. If the initializer is checked at a use-once sort, its variable is a value of that scope with exactly one site in the body. Standing as initializer is the initializer node’s one site; binding to the variable consumes nothing under every answer to C. This adds no permission for a binder or use-once function as initializer. An applied binder and an output continuation remain binders with their own bodies and outside-capture refusal. Under LT-4-R1, an effect in an initializer is read as one inside an argument and lifted over the rest of the initializer, the let body and whatever follows the let in the scope it stands in; no continuation ends at the initializer or at the let. The initializer’s run order, absence of a new reference activation and inlining conditions are cited in BND-LET and not implemented by this check clause.
- case: PROPOSED With admitted ordinary work(), f(h)=let y=work();use(y,h) keeps h’s sole site in f’s scope and passes this local check. The applied-binder counterpart captures outside h and is refused. For a use-once ordinary value initializer, one body use of the bound variable clears its local count, zero or two do not; a use-once function initializer is refused by USE1-007.
- excludes: PROPOSED Reopening the decided let ballot, treating the let as an applied binder, making its body a scope, treating binding as consumption, or inventing an initializer position for a use-once function.
- gaps: UG-001, UG-002, UG-003, UG-004, UG-005, UG-009, UG-012

## USE1-010 — A returning failure rule may leave no live duty unused

- revision: 1
- standing: DRAFT — peer and reviewed census required; no adoption.
- binding SHA-256: 6467777c6d41650f3fd769de59a625b8dddf03f4aba98c3b5457a64f4ef8b9f5
- kind: requirement
- subject: the pre-run use-once checker on a failure-answering rule, beyond slice 1
- from: SOURCE R13 D-UO-16:151; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-16:153; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-16:155; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-17:161; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- rests on: SOURCE R13 only; no named amendment dependency.
- text: PROPOSED When checking a failure-answering rule, distinguish an operation taking an answer from a failure whose continuation can never run. An answer-taking operation may have its continuation used once. A never-runnable continuation holding a live use-once value in its environment, an obtained-argument frame or captured handler state may not be left unused by a rule that returns. Under R13’s retained B-for-now boundary, no take is introduced: a catcher goes on only when the failed part held no value that may not be dropped, or handed what survives back openly in its result, with every caller’s obligations still owed. Otherwise failure propagates with the held duties. A rule may fail in its turn. These are checking conditions on supplied live-duty facts, not a consuming-event account or a recovery implementation. Slice 1 has no handlers.
- case: PROPOSED A proposed returning catcher that discards a never-runnable continuation holding h is refused. A return over an empty held account clears only this obligation. Failing again retains the obligation under the run boundary; it is not an ordinary successful return.
- excludes: PROPOSED Adding take, treating a failure value alone as completed cleanup, rolling back to an earlier state, or treating a stopped run as having already discharged returning-run duties.
- gaps: UG-001, UG-003, UG-007, UG-011, UG-012

## Boundaries with other rule files

PROPOSED — These entries name the promises the check relies on or is intended to establish. They route the destination’s operational rule; none is a new run, lowering, host or store implementation. Source sentence coverage records a gap as well as the boundary.

### BND-RUN-08 — Producer occurrences and fixed input values

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-UO-8:139; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-8:140; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-ATT-1:1014; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED The run file owns per-occurrence nullary execution, new values and fixed-host values entering as variables. The check uses CR-2’s proposed occurrence distinction in USE1-002. Defined-rule returns, data packing/unpacking and first-binding events wait on C; this boundary installs no account for them.
- related: USE1-002, UG-001, UG-003
- proposed dependency: PROPOSED CR-2 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-OWNER-PAGES-R1\REPLACEMENTS.json /replacements/1; SHA-256 256489928043460a4ad9dc343ee995a0466b76b31d8d1fd95a83f8d00b3936d0; PROPOSED LT-4-R1 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-LET-AND-WATCH-R1\REPLACEMENTS.json /replacements/2; SHA-256 05621d0663bd9e38d2de0b1132007008b8393b0bbd3d8275dbe9ec87b76d8f5c

### BND-RUN-09 — Consumption is not a row entry by itself

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-UO-9:142; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED The check is on the term as stated under the reference run. Consuming a use-once value adds no row entry by that fact; operations still owe their effects/costs and the value may not be dropped or run twice. Run/row files own that behavior; these checks do not compute a new row policy.
- related: UG-010
- proposed dependency: SOURCE R13 only; no named amendment dependency.

### BND-RUN-11 — The check’s returning-run promise

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-UO-11:146; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED The intended soundness promise is no double consumption; a returning run has consumed each value or handed it on. A nonending run may hold it forever, so eventual consumption requires a separate ending claim. The run file owns these promises and their events; this package proves none of them.
- related: USE1-002, USE1-006, UG-011
- proposed dependency: SOURCE R13 only; no named amendment dependency.

### BND-RUN-12 — Stopped and waiting duties

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-UO-12:148; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-12:149; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-RUN-7:585; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-RUN-8:598; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED Failure with no answer, resource stop and fuel exhaustion are nonreturning. A stop is not a drop; the run retains and names every unconsumed duty. Returning-run promises do not assert that a stop already consumed them. A failure may precede a written site. Asked host waits remain run-side. No run-state or held encoding is drafted here.
- related: USE1-002, USE1-010, UG-007, UG-011
- proposed dependency: SOURCE R13 only; no named amendment dependency.

### BND-RUN-COUNT — Reference consumption account

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-RUN-7:585; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED D-RUN-7:590 carries a count for each use-once value and :593 explains held. That count is dynamic, separate from USE1-002 static sites. LT-4-R1 ATT-7’s common part records consumings with their activation; all disputed events wait on C. Reference counts do not establish compiled consumption.
- related: UG-001, UG-003, UG-007, UG-008
- proposed dependency: PROPOSED LT-4-R1 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-LET-AND-WATCH-R1\REPLACEMENTS.json /replacements/2; SHA-256 05621d0663bd9e38d2de0b1132007008b8393b0bbd3d8275dbe9ec87b76d8f5c

### BND-AGREEMENT — Optimizer and lowering preservation

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-UO-6:135; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-RUN-9:600; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED D-UO-6 binds each rule step and lowering to ordered observations and each value’s consumption except where a claim licenses change; copying needs its sort’s law. The agreement file owns this requirement, compiled use evidence, matching choices and the distinction among agreement, established mismatch and incomplete. Request/outcome equality alone checks no compiled consumption; no lowering rule or witness is supplied here.
- related: USE1-004, UG-008
- proposed dependency: SOURCE R13 only; no named amendment dependency.

### BND-RUN-SHARING — Obtained values and binding unrun work

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-RUN-3:574; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-RUN-3:575; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-RUN-4:577; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-ATT-1:1014; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED Run rules own argument activations, variables denoting obtained values, result reuse and bind-before-duplication. Use current D-ATT-1’s full restriction, including makes-nothing-new, rather than R2’s earlier reuse premise set. The check’s context and path counts do not grant execution reuse, early work or duplication.
- related: USE1-002, USE1-003, UG-001, UG-009
- proposed dependency: SOURCE R13 only; no named amendment dependency.

### BND-LET — Proposed let run and names

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-ATT-3:1018; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED Only USE1-009’s check clause is drafted. LT-4-R1 proposes ATT-4 initialization/run order, enclosing reference activation, contextual-bound-argument limit and inlining conditions, and ATT-6/ATT-7/ATT-8 names and correspondence. These sections are absent from R13 and remain PROPOSED run/record/agreement work. Under every C answer, only the common part stated in UG-003 is recorded. C-A is not chosen; equality of compiled/reference names is not assumed.
- related: USE1-009, UG-001, UG-003, UG-008, UG-009
- proposed dependency: PROPOSED LT-4-R1 — C:\Users\grego\.codex\reviews\2026-11-12-CLAUDE-ARCH-LET-AND-WATCH-R1\REPLACEMENTS.json /replacements/2; SHA-256 05621d0663bd9e38d2de0b1132007008b8393b0bbd3d8275dbe9ec87b76d8f5c

### BND-ADM — The admission checker’s three contacts

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-ADM-2:547; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-ADM-7:560; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-ADM-4:553; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED Admission owns checked signature/context/sort facts and binder positions at D-ADM-2, proposed LT-4-R1 D-ATT-4's let admission among them, and checks guards under ordinary sort/context/use-once duties at D-ADM-7. Local handback is not a whole use-once pass. Question N’s N-A refusal is a conditional obligation-generator drafting premise in open UG-013, not an adopted refusal. Before fixing admission or use-once rules, obtain the owner answer or establish that the selected slice-1 scope cannot reach the case; M-A is not established as the sole trigger. No wider admission contract or new membership mechanism is added. PT-1 remains a proposed case clarification, not a literal-pattern permission. [P0117:N-A]
- related: UG-004, UG-013
- proposed dependency: PROPOSED PT-1 — C:\Users\grego\.codex\reviews\2026-11-13-CLAUDE-ARCH-SLICE-1-WORDS-R2\REPLACEMENTS.json /replacements/7; SHA-256 ac9020d106544ea1d0467147f4d83d51a7a9e805891cef1ed26fc7ec177b3a11

### BND-TERMS — Declared multiplicity versus keeping it

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-UO-3:128; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-5:133; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED Committed RULES-TERMS TERM-006:84 points to the use-once rules for checking declared multiplicity; TERM-012:157 points to clause (b) for a handler, first needed in slice2. USE1-006 and USE1-007 hold the pre-run duties of declared multiplicity. No rule in this file holds the handler-continuation duties of R13 D-TR-11:390, D-TR-12:392 and D-TR-13:396 (working), first reachable with handlers after slice 1; UG-011 records them open. TERM-005/006/007 still own signature declaration and meaning; TH-1-R2 stays a proposal and the terms file is untouched.
- related: USE1-006, USE1-007
- proposed dependency: PROPOSED TH-1-R2 — C:\Users\grego\.codex\reviews\2026-11-13-CLAUDE-ARCH-SLICE-1-WORDS-R2\REPLACEMENTS.json /replacements/0; SHA-256 ac9020d106544ea1d0467147f4d83d51a7a9e805891cef1ed26fc7ec177b3a11

### BND-STORE — Shared storage is not unique occurrence counting

- standing: BOUNDARY ONLY
- from: SOURCE R13 D-UO-2:125; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce; R13 D-UO-10:144; SHA-256 20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce
- boundary: SOURCE / INFERENCE / PROPOSED Committed RULES-STORE STO-010:151 assigns path counting to D-UO-2. USE1-002 counts paths, not interned nodes. STO-005/006 own the remaining store-cache evidence and answer-validity conditions; USE1-003 adds no waiver. No store or canonical identity contract changes.
- related: USE1-002, USE1-003
- proposed dependency: SOURCE R13 only; no named amendment dependency.

SOURCE — Committed interface pins: RULES-TERMS.md SHA-256 ef5733c131b35d0b41917ef40f3643a60374dd0edb242064774ff6c99eb00324, TERM-006:84 and TERM-012:157; RULES-STORE.md SHA-256 aab44cc62ca1bc49e2e4caf792cdb13685bcb9be621579156fb91ee7c5ce65e9, STO-010:151. Those files are unchanged. Eng RA is the supplied REPORT’s admission/check boundary; it grants no rule adoption.
