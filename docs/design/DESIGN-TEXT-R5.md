# One design text, revision 5: Claude Arch

## 1. Status

- **This is revision 5:** revision 4 with the edits of my card 0058 report applied. It folds Codex C's review of revision 4 (card 0524): its two repairs and its optional label; Codex G's review of the evaluator's rules R6 (card 0173): its sentence on the memo, and two details on which it found this text silent, what a completed write gives and what `length` does to the last place; and three unreviewed outside reads by agy, whose findings that report takes, declines or leaves open one by one. Codex G's review of meter revision 5 (card 0172) is back, and two tags now say so. No owner decision is new since revision 4. A correction to my card 0055 report: its "no new design" and "nothing else new" were too broad, since slice 2 for the fixed build during a run, and that build's finish line (D-JIT-4), were my proposals, as their tags say. Left open by name: whether `slice` takes a start and an end or a start and a length (D-EV-1); D-ADM-5's name for the indexed values of the standard theories; and the word for an ordered field of the records, such as D-REC-1's parameters, now that a sequence is the kind that changes. An annex of the card 0058 report matches each description of an owner record in section 3's tags to its record file.
- **Revision 4** was revision 3 with the edits of my card 0055 report applied. It folds Codex C's review of revision 3's part 1 (card 0523) and Codex Q's review of its part 2 (card 0092), both words only; the owner's six answers on my card 0052; and the owner's hold on web topic 5. For K-13 it points to meter revision 5. Revision 3 was in two parts. Part 1 was revision 2 with the edits of my card 0051 report applied, folding revision 2's two reviews, the owner's decisions of 2026-11-10 on values, sequences and edge cases, the breadcrumbs, and three open items from the second attack. Part 2, the edits of my card 0052 report, folded the web round 3 answers: five corrections; the proposals and open items of D-WEB-1 to D-WEB-8; the answers' positions on three items that waited on the owner (recovery's second half, item 23, five or six facets); and three directions held back for the owner (abduction ranking induction, look-back declared by the callee, one early build during a run). The owner has now answered all six (D-UO-17, D-TH-7, D-FAC-1, D-STO-7, D-LB-3, D-JIT-4). The answers are outside input, written against revision 1; topic 8 was not answered. Revision 2 was revision 1 with the edits of my card 0040 report applied. Section 3 is the design text. The rest of this section, and sections 2 and 4 to 7, are revision 1's account of itself and are kept as history; what revision 2 changed, and why, is in the card 0040 report.
- Card 0037 with its two addenda, all five parts done. The card, both addenda, the twelve inputs, the ledger and the five new owner records matched their hashes (section 7).
- **Codex G (Spec Reviewer)'s findings.** I accept all eighteen, each with G's own fix, and reject none.
- **Revision 1.** Section 3 is the whole text again: 217 numbered passages and the register of run results. Against the first text 39 are added, 57 changed, 2 retired and 122 as they were, by a program's comparison.
- **What is folded:** the concurrency core with Codex C (Core Reviewer)'s five fixes; recovery, with both of its decisions left open for the web round as addendum 2 asks; lens 09's twelve items; the optimizer's five doors; the names; Codex S (Rule Tester)'s results; and a first text for building ahead of time and during a run, as addendum 1 asks.
- **My two calls on concurrency,** by the owner's leave. Counting repeated looks: confident. The core in this round: confident for the parts the tests cover, as working rules; three parts left open.
- **Three limits.**
  - I read Codex Q (Model Checker)'s review of the core tests only to its line 60, my recovery report to line 345, and my optimizer report to line 235.
  - Codex S's four store tests are not yet reviewed, and everything resting on them is marked so. Codex Q's review of the rewritten store rule was not an input; I have it only as Codex G reports it.
  - No lane other than me has read the new passages. They need the same review the first text had.
- **For the owner:** ten new points and one question for the web round, in section 5.
- **The first spec cards:** the evaluator, with a gap list of seventeen and four draft cards, in section 6.
- Labels: SOURCE is a file and line, or an anchor. INFERENCE is my reading. PROPOSED is my suggestion. The short names of sources are at the head of section 3.

One author's view. Not reviewed or accepted; no owner decision.

## 2. Codex G's findings

SOURCE: Codex G (Spec Reviewer)'s report, cited as G with its line. Its verdict is SOUND WITH FIXES (G L1). PROPOSED: I accept all eighteen findings, each with G's own fix, and reject none. Where I did more or less than G wrote, the last column says so.

| Finding | Verdict | What I did in revision 1 |
| --- | --- | --- |
| F01, D-TR-5 contradicts D-TR-6 (G L9) | Accept | The last sentence of D-TR-5 now defers to the cover rule of D-TR-6. The owner has since decided the point: section 3's tag on D-TR-6 |
| F02, D-RUN-1 keeps an old licence to exchange (G L11) | Accept | The last bullet is G's sentence |
| F03, the meter lost the charge by argument size (G L13) | Accept | Restored beside C41's lines in D-EV-1 |
| F04, D-REC-1 still shows Next, Done and Ask (G L15) | Accept | `step` now points to D-RUN-7 for its state and outcomes. D-RUN-8 says "asked" |
| F05, literal and data values in D-ADM-5 (G L17) | Accept | G's sentence. The data edge stays marked to test in D-ADM-3 |
| F06, D-STO-7 lost four clauses, and its standing was too strong (G L19-L26) | Accept | All four clauses restored. The tag now reads: direction approved, application conditional on a test that is not run. D-ENG-7 is qualified the same way |
| F07, D-PR-6 dropped its source's cautions (G L28) | Accept | Both cells restored |
| F08, the held-out protocol's mechanism was cut short (G L30) | Accept | Sentence restored |
| F09, the history of item 24 is stale (G L32, L88-L99) | Accept, and taken further | G reports a review by Codex Q (Model Checker) of the rewritten rule that was not an input of mine. Codex S (Rule Tester)'s later store tests are an input now, so the tags on D-TR-10 to D-TR-13 and the rows of D-EVD carry both, each marked with who reviewed it |
| F10, approval labels too wide (G L34) | Accept | D-UO-11 and D-UO-12 are split as G gives them |
| F11, replaced words still quoted in five tags (G L36) | Accept, plus one | The five tags now name the line and not the words. I did the same to a sixth, on D-ST-2, which G did not list |
| F12, the limit of the hash trial (G L38) | Accept | Restored in D-FND-3 |
| F13, the scope of the owner's figures (G L40) | Accept | Restored in D-TB-5 |
| F14, three cases lost their scope (G L42) | Accept | All three restored |
| F15, the line between operations that return and those that may not (G L44) | Accept | Restored at the head of D-TR-15 |
| F16, the register dropped results and scope (G L46-L61) | Accept | Every row of G's table is restored in D-EVD, which now says it groups some cited history. D L50's commentary is added to what is cited and not copied |
| F17, three attributions (G L63) | Accept | D-STO-6, D-SL-4 and the case in D-RUN-5 |
| F18, slice 1's minimal scope (G L65) | Accept | Appended to D-SL-1 |

**G's standing rulings (G L71-L86).** I follow every one. Three changed a tag: D-UO-11, D-UO-12 and D-STO-7. The rest were KEEP.

**G's rulings on my 22 doubts (G L105-L128).** Thirteen KEEP, eight CHANGE, one for the owner. The eight changes are the findings above. The one for the owner, whether a function may be held in data (G L123), is now answered inside the concurrency core: D-CONC-2 lets a constructor hold a function, and D-ADM-2 is changed to match. It is still a proposal, and it goes to the owner as part of "the core in this round".

**One thing G could not check** (G L140): items 49 to 51 against their first texts, which were in neither G's inputs nor mine. That is still not done.

**The count.** G corrects my "181 passages" to 180 numbered passages plus D-EVD (G L128). Revision 1's count is in section 7.

## 3. The design text, revision 5

**How to read it.** Each passage has an anchor, `D-` then an area and a number. An anchor is never reused and says nothing of position. After each passage a tag in square brackets gives where the words come from and how they stand:

- `D L42` is a line of the sealed `DESIGN.md`; `C22` is item 22 of the sealed `CORRECTIONS.md`. `R24`, `R29`, `R30`, `R32`, `R34`, `R35` and `R36` are my reports on cards 0024 (item 24 and late reviews), 0029 (stops), 0030 (chance), 0032 (recovery), 0034 (Gemini's lens 09), 0035 (the concurrency core) and 0036 (the optimizer). `G` is Codex G (Spec Reviewer)'s review of the first text. `CR2` is Codex C (Core Reviewer)'s review of R35. `ST` is Codex S (Rule Tester)'s tests of the core. `G2` is Codex G's review of revision 1. `Q89` and `Q90` are Codex Q (Model Checker)'s reviews of Codex S's store tests and of its tests of substitution, licence, Close and the invariant. `R38` is my report on card 0038 (look-back), and `LBR` is Codex C's review of it. In the evaluator's passages, `revision 4` with a K-number or a section is my sequences and value kinds report, revision 4, and `meter revision 5` is my card 0053 report on the meter; neither is this text's own revision, though this text is now revision 5 too. `rules R6` is Codex D (Specs)'s evaluator rules, revision 6, whose rules are numbered EV-1 upward; `G 0172` and `G 0173` are Codex G's reviews of those rules' revision 5 with the meter, and of rules R6; `EV-A2` is my card 0057 report on the bytes operations.
- `agreed`, `kept`, `open`: the design's own mark, on words no item touches. `author's` is a passage the design's author marked "mine, unreviewed", which item A accepts.
- `fold`: the words of an item put in place of the design's, as I recommend. PROPOSED by me, decided by nobody, and waiting on the owner like every proposal here. For a fold that only repairs a case the design's own words let through, the other answer is the design as it was, at the line the tag cites; those words are in the sealed design and are not repeated.
- `waiting on the owner`: a real choice. The other answer is given in the line after the passage.
- `owner (recorded)`: the owner chose between two answers, and a record binds it.
- `owner, unrecorded`: a card reports the owner's words, and there is no record yet. No passage has this tag now.
- `open: web round`: the owner has sent the choice to the next round of outside review. Neither answer is recommended in the text.
- `Arch's call, by the owner's leave (recorded)`: one of the two concurrency choices, which the owner's record leaves to me where I am confident.
- `approved`: named in one of the owner's records of 2026-11-10, read strictly. "As forced move n" means the owner's record on the 33 forced moves of the first text: each is approved for its own fix and no more, and a test that the passage still owes is still owed.
- `working`: a working rule. D-WRK-1 names its test and what falls with it.
- `GAP n`: gap n of my 0031 report, marked and not filled. `PLACEHOLDER`: not folded, because its source is not in or not an input.

**What is not copied.** The design's run results are not left inside passages, because many were run under rules this text replaces (C22: "The old comparisons of section 1 are evidence for L346 with the old count, and for nothing else"). They are in the register D-EVD at the end. Codex G found that sound, on condition that scope and superseded-rule limits are kept (G L61). The toy's printouts (D L637-L781), the seven places the design may be wrong (D L783-L834) and the list of the author's unreviewed additions (D L836-L856) are cited there by line and not copied.

**Names.** SRE stands for Structural Representation Explorer. It is what the design's section 9 called by an older word, and what that section called the lab is LoomLab. The compiler's optional optimization paths are the optimizer (D-OPT-1). The backend is not named: where the design named one, this text says "the backend". What replaced the one word for a value's kind are the facets (D-FAC-1).

---

### The constructs

**D-CON-1.** Loom is a language in which a program, a theorem and a compiled artefact are terms in one store, and every fact about them is a claim with a scope, a status, evidence and an account of what it rests on. There are seven constructs. The first four describe what is said, and the last three describe what is known about it. `[D L5, L11 | kept]`

#### Theory

**D-TH-1.** A theory is a vocabulary: sorts, operations, laws and rules. The integers, a mutable store, a logic, an instruction set and a file format are all theories. `[D L15, L23 | kept]`

**D-TH-2.** A sort may be indexed by terms, as in a vector of length n. `[D L17 | kept]`

**D-TH-3.** An operation may bind variables. A bound argument carries a multiplicity, declared in the operation's signature: how many times the operation calls it. It is one or any. `[D L18; C6 | fold]` Whether a third value, none, for a parameter that is never called, is added goes to test. `[R29 section 4 | approved, to test]`

**D-TH-4.** A law is a statement the theory asserts. `[D L19 | kept]`

**D-TH-5.** A rule is a step of the reference run. It applies to arguments that are values, and only when no earlier rule of its symbol matches them. Read as a statement, a rule says that for all values of its variables that no earlier rule matches, its two sides have the same run. A rule is used at a term that is not yet a value only where D-RUN-6 lets the planner move, share or drop that term. Putting a definition's body in place of a call keeps each argument bound: the arguments run in the reference order and the body sees their values. A binding is taken away only as D-RUN-6 allows for the term it binds. Derivations, and yes by computation (D-LAW-2), use rules in this reading and no other. `[C20; R29 section 4, in place of the rule sentence of D L19 | approved]`
Case: f(0) = 0 and f(x) = 1, read with no condition, give 0 = 1; and discard(x) = unit makes discard(loop()) return where its run never does.

**D-TH-6.** An effect is an operation whose last argument is a bound continuation, so order is written into the term. Its multiplicity is owed by every interpretation of the effect: a handler is a rule, and clause (b) of D-UO-3 counts the continuation in it. `[D L20; C6 | fold]`

**D-TH-7.** A sort may carry any of three declarations: it is finite with these values, it is data with these constructors, it is use-once, meaning the theory has no law to copy or to drop its values. A data sort with a constructor that takes a use-once argument must be declared use-once, and its declaration is refused otherwise. The refusal names the field. `[D L21; C23 second point | fold; the refusal, naming the field, by the owner's record of the six answers, item 2 | decided]` This replaces "the refusal is open: web round". The answer not taken: such a data sort is made use-once without being declared so. That would also keep a use-once value contained; the web round's answer was for the refusal because, made use-once silently, a change to one field changes which client programs are legal without changing the line clients read. `[web round 3, topic 2 | outside input]` D-UO-17 keeps the one mark now and records two as the direction.
Case: a sort of boxes that is not use-once, the rule finish(Box(h), tag) = read(h), and the term that binds b to Box(x) and takes pair(finish(b, 0), finish(b, 1)). Without the added declaration rule every clause passes, and the run reads x twice.

#### Statements, relations and predicates

**D-ST-1.** A statement is a term of the statement sort of a logic, and a logic is a theory. `[D L27 | agreed]`

**D-ST-2.** A relation is a set of pairs, as in mathematics, and it may relate more than two sorts. A symbol R whose application R(x, y) is a statement gives the relation {(x, y) | R(x, y)}. R is declared as any operation is, or defined by a formula. Two symbols may give the same relation. They are then two nodes, and that the two relations are equal is a claim: the statement that R1 and R2 hold of the same pairs. A predicate is a relation in one argument. It gives a set in the same way, and two predicates may give one set. `[C1, in place of the sentences of D L27 and L36 on a symbol and its set | fold]`

**D-ST-3.** Converse, composition, union and the fibres of a representation's relation are read on the set, and a tracking claim or a law is read on the statements. R(x, y) is a statement and not a computed truth value, and whether it can be decided is a claim. `[D L27 | agreed]`

**D-ST-4.** Nothing in the design is called a property. What mathematics calls a property is one of four things here. `[D L29-L34 | agreed; last bullet C2 | fold]`
- Of an element, it is a predicate.
- Of a structure, it is a law at an interpretation, which is a claim, or a predicate on interpretations.
- Data that is unique when it exists, such as a unit element, may be written either way: as an operation with laws, or as a statement that one exists. The choice decides what an interpretation must preserve and what a client can reach.
- What the SRE asks of an object is a question: an operation from the object's sort to a sort the client can read. A predicate whose statement is decided at each object gives a question with the answers yes and no. An undecided predicate is not a question, and what is known of it at an object is a claim.

#### The use-once check

**D-UO-1.** Use-once is checked on every use-once value, scope by scope. A scope is the body of a binder, the right-hand side of a rule, or a whole term. A use-once value is a bound variable or a pattern variable of a use-once sort, or any node whose sort is use-once: the result of an operation that returns such a value, or a function made by clause (c). `[D L40 | agreed]`

**D-UO-2.** Clause (a). Each use-once value has exactly one consuming site in the scope that makes it. A site is an occurrence: an argument position reached along one path from the root of the scope. A node reached along two paths gives each of its sites twice. Sites are never gathered across two binders. Three answers suffice: no site, one site, more than one. `[D L42; C22 third bullet | working: C22]`
Case: g(d, d) with d = read(x). The node read(x) holds x at one position and runs twice, so x has two sites.

**D-UO-3.** Clause (b). Each rule is a scope: a pattern variable of a use-once sort has exactly one site on the right-hand side. A case analysis on a use-once value is therefore written as rules that take it as an argument. `[D L43 | agreed]` A pattern variable that stands for a bound argument of multiplicity one is a use-once function in its rule. It has exactly one site, and clause (d) says where that site may be. This holds in slice 1 too, beside the narrower rule. `[C23 first point | approved, as forced move 9]`
Case: relay(h) = twice(h), with h declared to be called once. Without the added sentences it passes, and its run calls h twice.

**D-UO-4.** Clause (c). A binder makes a use-once function when its body consumes a use-once variable that is bound outside it. Making it is that value's one site outside, and inside the body the value has exactly one site. `[D L44; C22 fifth bullet | working: C22]`

**D-UO-5.** Clause (d). A use-once function may stand only where its taker calls it exactly once: as the function of an application, or as a bound argument whose declared multiplicity is one. `[D L45 | agreed]`

**D-UO-6.** Clause (e). Every rule step and every lowering keeps the observations of the run, in order, and what the run consumes of each use-once value. A change to either needs a claim that licenses that change at that place (D-TH-5, D-OP-2). A value is copied only where its sort has a law to copy it. `[C22 fourth bullet, in place of D L46 | working: C22]`

**D-UO-7.** Handing on the result of a scope is one site. `[D L58 | author's]` Performing a failure hands on what its scope still holds: a use-once value with no other site in a scope whose last operation is a failure has that failure as its site. `[R29 3.3 | approved, as forced move 30]`

**D-UO-8.** An operation with no arguments runs at each occurrence like any other, and each run of an operation that returns a use-once value returns a new value, whatever its content. So a constant of a use-once sort written at two places is two values. One fixed value, such as a handle that the host holds, enters a term only as a variable. `[C22 fifth bullet, in place of the reading at D L59 | working: C22]`
Case: f(b) = read_in(K, b) and pair(f(false), f(true)). Each call makes its own K. And pair(read(x), (y -> read(k))(read(k))), which D L59 gives as a wrong term, is a right one.

**D-UO-9.** A term that consumes a use-once value adds no entry to the row by that fact, and it may still not be dropped or run twice. The check is a fact about the term as stated under the reference run. `[D L60; C4 | approved, as forced move 1]`

**D-UO-10.** A check of a node that holds variables is a check in a context, the sorts of those variables. A cache of such a check is keyed by the node and the context. This holds for sort membership as for use-once. `[C23 third point | fold]` For one use-once value, counted on the shared graph with the count capped at two, the count visits each node once. The whole check is not shown to be one visit for each node. `[C22 | working: C22]`

**D-UO-11.** What the check says. No run consumes a use-once value twice, and a run that returns has consumed each one or handed it on. A run that does not end may hold a value for ever: the rule spin(h) = spin(h) passes every clause and never consumes h. That every value is consumed in the end is a further claim, that the run ends. `[C23 fourth point | fold; "a run that returns", R29 3.3 | approved]`

**D-UO-12.** A run stops without returning in three ways: a failure that nothing answers, a stop for a resource, and running out of fuel. A stop is not a drop. The stopped run holds every use-once value it had not consumed, as a run that does not end holds them, and its outcome names them. What the check promises of a run that returns it does not promise of one that stops. `[R29 3.3 | approved]` The possible failure is in the row (D-ADM-4, D-PATH-1), and a bound may refuse it. `[R29 L92-L93; C26; C27 | fold]`
Case: pair(fail(e), read(x)) passes every clause, and its run ends in a failure with x never consumed.

**D-UO-16.** Going on after a failure is where a value could be lost, and there the check decides. A failing operation that takes an answer is answered like any operation. Its rule may run the continuation once, with a value in place of the one that failed, and nothing is lost. A failure that takes no answer has a continuation that can never be run. The rule that answers it receives that continuation. It holds a value that may not be dropped when an environment in it, a frame in it that waits with an argument already obtained, or handler state it captured holds one that is live. The rule may not leave such a continuation unused and return. `[R32 section 5 | fold]`
Whether the rule can get at what the continuation holds is open, and the owner has sent it to the web round. The first answer: the rule may take from it. take(k, S) gives the live values of sort S that k holds, each once, the innermost first, and what is left of k. It is defined only for a continuation that can never be run. A value inside a datum is taken with its datum. The rule owes each value it takes what any holder owes: it finishes it by an operation of its theory, uses it, or hands it on. When nothing that may not be dropped is left in k, the rule may leave k and return. A value of a sort the rule cannot name cannot be taken, and neither can a function. Over those the rule can only fail in its turn, and whatever answers that failure receives a continuation that holds them. The entry in the row for a possible failure lists the sorts of the values that may be held when it happens and may not be dropped. A rule that returns after a failure is admitted over a body only if it takes every sort the body's row lists for the failures it answers. `[R32 section 5, decision 1 | open: web round]`
The second answer: no take. A program recovers from a failure only where the failed part held nothing, and anything that must survive a failure is kept by an owner outside the part that may fail (R29 3.3). The owner reopened this answer, so it is not the working rule either.
A third answer, from the web round: no take, and no reaching into a continuation. A part that can fail declares in its result what it hands back: it returns either its result or a failure with a payload and a residue, and the residue is ordinary owned data holding what survives. Every caller the failure passes must finish, hand on, or add to its own residue whatever it still owes; turning the failure into a value is not enough. Its case to refuse: a `bind` that passes a failure on and gives the success callback no site. What comes back is what survives now, not an earlier state; returning to an earlier state is going back to a kept point (D-BC-2, D-BC-3), which the answer had not seen. A failure with no declared exit propagates, or stops, with its surviving values held. For the cases shown this needs no new operation in the reference run; its general translation is not checked. `[web round 3, topic 2; its nearest precedent could not be checked by Codex P; its program not rerun | proposed, to be tested before take]`
Meanwhile, PROPOSED: the text fixes only what both answers share. A stop holds what it held (D-UO-12). A failing operation that takes an answer is answered like any operation. A rule that answers a failure may always fail in its turn. A rule that returns after a failure is admitted where the failed part held nothing that may not be dropped. Whether, and how, a rule may return where the failed part did hold such a value is not specified, and no rule of the specification is written for it until the round answers. Slice 1 has no handlers, so nothing there waits on it.
What depends on the answer: D-CONC-12, the failure in a task; D-CONC-14, since take would be a new operation of the reference run; the entry in the row for a possible failure, which would list sorts (D-PATH-1, D-ROW-2); and D-RUN-7, whose held values take would have to find.
Cases, proposed and not run. Under the first answer, the proposed test should show that a parser that holds its input and retries gets the input back as it stood. And a rule that takes from the continuation of an operation that does take an answer, and then runs that continuation, must be refused: the value would be in two places.
The first answer would cost this: one operation more in the reference run, which is trusted text; the check's pass at failing points reports sorts; and a compiled program must know at each call that may fail which slots hold live values. D-UO-13, the placeholder of the first text, is retired.

**D-UO-17.** Whether each sort may say for itself that its values can simply be left behind is decided for now: the text keeps one mark, exactly once, and records two marks as the proposed direction. `[the owner's record of the six answers, item 1 | decided]` This replaces "open, and the owner has sent it to the web round". The direction, which was the first answer: copying and dropping are two questions, and the theory answers each. A sort is marked no-copy, no-drop, or both. No-copy: the theory has no law to copy its values. No-drop: it has no law to drop them. Use-once is both. In clause (a): a value of a sort marked no-copy has at most one consuming site in the scope that makes it, and a value of a sort marked no-drop has at least one. A function carries each mark that the values it holds require, and each mark that its contract for being called requires: a contract to run at most once makes it no-copy, a contract to be run makes it no-drop, and a contract to run exactly once imposes both, even when it holds nothing, as for a Task (D-UO-3, D-CONC-2). `[the contract clause: web round 3, topic 2, made precise by Codex Q's review of revision 3, part 2 | proposed]` A data sort carries every mark its fields carry, and its declaration is refused otherwise. In place of a law a theory may give an operation: one that copies, or one that finishes, which consumes a value and returns nothing of its sort. An operation runs where the program calls it, and what it does is in the row there. Dropping a value that has a law to drop is no act in the meaning: nothing is observed, and nothing enters the row. How it runs and what it costs belongs to the representation. In D-TR-12: resuming twice is refused over a value marked no-copy, and never resuming over a value marked no-drop. `[R32 section 5, decision 2, which would change D-TH-7, D-UO-2 and D-TR-12 | the direction, by the owner's record; not built now; not run]`
What is kept now, which was the second answer: one mark, exactly once, as D-TH-7 has it. Catching a failure gives no permission to drop a held value. Recovery may return only after every obligation has been used, finished or handed on through a permitted operation; otherwise the failure propagates with the value retained. Whether the catcher can get at the value is D-UO-16's decision, not this one. A library handler may perform a cleanup that is available. `[R32 L251-L258; G2 F06]`
Every other passage is written with the one mark and stays so. Before the direction is built: reading each existing use-once declaration as both marks keeps every contract that does not change as it was, and that is all the comparison so far shows; capture, functions passed as values, declarations and a new census are still owed. `[Codex Q's review of revision 3, part 2 | fold]` What the direction would change: D-TH-7, D-UO-2 and D-TR-12 as the tag says; D-CONC-2 and D-CONC-3, where "use-once" would read "no-copy and no-drop"; D-CONC-12; and the census behind D-TR-11 to D-TR-13.
Case that must be refused: a datum of a sort that may be dropped, holding a value that may not. Leaving the datum drops what is inside.
What it changes elsewhere if taken: Codex S's census for D-TR-12 counted a rule that never resumes as wrong under the single mark, and over a name marked only no-copy it becomes right; and a Task must stay no-drop, or a deadlock can vanish (D-CONC-11). A sort with a declared finish is not a third kind of sort: the finish is an operation, with effects, and usage stays two yes-or-no answers.

**D-UO-14.** Until the test of D-UO-15 passes, slice 1 may build the narrower rule: clauses (a) and (b), and a refusal of any binder that consumes a use-once value from outside. `[D L48 | agreed]` The narrower rule ends with slice 1. Under it a use-once value cannot be used after an effect, because everything after an effect is inside its continuation, and slice 2 brings effects. `[D L62; C5 | fold]`

**D-UO-15.** Open. The test: the comparison of the check with what a run consumes, on the whole language, with data that holds a use-once field, effects, and a value consumed once in each of two branches. `[D L62 | open]` Known to be refused though right: a value consumed once in each of two branches that are passed as functions, and a value used once and also handed to a function that is never called. `[D L52 | agreed]` The same census, with none added as a multiplicity and then with a pair of call profiles for the two branches, is the test of whether those are recovered: no wrong term accepted, and a count of the refused right terms each recovers. `[R29 section 4 | approved, to test]`

#### Term

**D-TM-1.** A term is an expression over theories, stored as a shared graph. Equal terms are one node. A defined symbol is identified by its content, a declared symbol by its declaration, and a term by its structure with binders made nameless. Programs, proofs, data and machine code are terms. `[D L66 | kept]` This is about the store and about identity. That two pieces of code are one node is never by that a reason to reuse a run (D-RUN-3). `[C22 first bullet | working: C22]`

**D-TM-2.** Any node can be read as data. A term, a theory, an interpretation, a representation and a derivation are each values of a sort of their own, so a question or a predicate may take one as its argument. `[D L68 | agreed]` A term is handed over as data only by quote(e). The reader of text makes it a literal of the sort of terms, holding the node of e as written with the context of its variables. The run does not evaluate inside a quotation, and no rule, interpretation or move of the planner enters one. A value does not carry the term that produced it. Running a quoted term is an operation of its own, and what the term reaches enters the row where it is run. What a quotation holds is fixed when the text is read. `[C21; the sentence before this tag from R38 5.2 | working; not decided by the owner, who asked for look-back, which D-LB-1 to D-LB-4 begin]` The other answer: any term may be read as data wherever it stands, as D L68 has it, and what an operation sees then depends on whether its argument ran first. GAP 8: the written form of the mark is not settled.
Case: root_is_add(add(1, 2)). Without a quotation it sees 3.

**D-TM-3.** A structure is given as an interpretation of its theory. A predicate on structures that the theory's own language cannot state, such as being finite, complete or simple, is a predicate on interpretations, stated in whatever foundation is hosted. A predicate on theories, such as being consistent, is a predicate on theories as data. Read as data a term is its node, so such a predicate may tell apart two terms that a law makes equal. `[D L68 | agreed; last sentence the author's inference]`

**D-TM-4.** Open: whether an interpretation and a record that holds the same carrier, operations and laws are one thing, or two connected by a claim. The test: in slice 2 write one monoid both ways and look for a client that can tell them apart. `[D L70 | open]`

#### Look-back

**D-LB-1.** A look-back sees the term written at one argument place of one call, as the reader of text made it: its outer symbol and its parts, with variables as variables. It does not follow a variable back to what was bound to it, or a parameter back to the caller. It does not see how a value was produced, the plan, a name chosen for a value, or anything else in the store: those are outside this mode on present evidence. A history that is recorded explicitly and handed over beside a value would be a wider interface with its own meaning and tracking, and is not designed. There are two kinds. In look-back that cannot be seen, the result is the same whatever was seen, and the look only chooses how to compute it. In look-back that can be seen, the result depends on what was seen. `[R38 2.1, 2.3 and 5.2; the limits on "never" from LBR finding 1 | fold; the first set, taken into this revision by the owner's record]`
An observation that gives one answer on all terms the whole evaluation makes equal, in a domain where every admitted term reaches a value, is an observation of the value. Giving one answer on terms that some named laws make equal is weaker: a view of a sum by its leaves respects regrouping and still tells 1 + 2 from 3. `[R38 2.3; LBR finding 1 | fold]`

**D-LB-2.** Look-back that cannot be seen. A theory may mark a law as a look-back law: a law with a direction, whose left side is an operation applied to an argument written in a stated shape. The optimizer may use it at a site only where the law is yes there (D-RL-4) and every condition of D-RUN-6 holds for the runs it moves, repeats or leaves out, the calls of a function handed to the operation among them: the bindings of arguments, the activation, the way each claim was admitted, evidence read again where the term now stands, no effect, no open choice, no possible non-termination, no use-once consumption, and no result of a use-once sort shared, run again or left unmade. A look-back law over parts that may have those is used only under a claim about the two runs (D-RUN-1). The two runs then agree as D-RUN-9 and D-RUN-10 ask: the requests, the outcome with a failure's payload, what is consumed, value by value and activation by activation, who holds each fresh result, and the values held at a failure. A stop for a resource is not agreement. Using a look-back law changes nothing the reference run observes; time, memory and where a resource runs out may differ. The plain path uses none. That an operation is called a functor or a natural transformation licenses nothing: its own law, with its scope, does. `[R38 5.2; the full conditions from LBR finding 2 | fold; the first set]`
Its test, for each marked law, proposed: exhaustion over every small term that the two sides have the same run in that full sense, with controls that must each be refused: a wrong law; a right law over a function that has an effect; two maps made one where the functions fail with different payloads; the same under a resolver that answers by position; an element left out whose function fails or does not end; a rewrite that leaves a use-once value unconsumed; two fresh use-once results made one; a value held at a failure on one side only; and evidence that does not hold where the term now stands. `[R38 5.4, step 0; LBR finding 2 | to test; D-EVD row 28 is what has run]` These refusal controls exercise the current simple first-set licence without a separate full-run claim. Each case records its law, scope, sites, selected interpretation and expected refusal. The use-once control detects changed consumption or ownership, including a value neither consumed nor handed on at successful return; failure and endless runs may retain values as D-UO-11 and D-UO-12 allow. An effectful callback is refused by this route even where a separately established full-run claim could justify that instance. `[Codex C's review of the look-back passages, repair 4 | fold]`
Case: map(f, map(g, xs)) made one pass. With g(1) failing with one payload and f(0) with another, on an input holding 0 and then 1 the two sides fail with different payloads.

**D-LB-3.** Look-back that can be seen has two forms. One is the quotation of D-TM-2, written at the call. The other is a declaration by the callee in place of the mark at the call, which the reader of text translates into an ordinary call on a quotation. `[the owner's record of the six answers, item 5: the declared form comes forward | decided; its test is still owed]` This replaces "a declaration by the callee in place of the mark at the call is later, and waits on its test". A declared look-back is applied by name only, is never handed on as a function, and follows no variable. A quotation mentions no use-once variable, in either form. The web round's answer shows three things this passage owes, for both forms. First, executable substitution in the elaborated core never enters a quotation: it leaves each quotation and the context of its variables fixed. Changing the source is another matter: `(x → is_variable(x))(3)` gives true, and its ordinary beta contraction, `is_variable(3)`, gives false, so contracting the source is not a valid equation across an interface that observes syntax. Second, under the answer's convention that a looked-at argument is syntax only and does not run, capture comes before an effect inside the argument is turned into a continuation (D-STG-1); taking the effect out first would make `ignore_syntax(print("x"))` print. An interface that takes a value and its syntax runs the value part as any argument runs. Third, the passage must say whether the looked-at argument also runs; the answer's choice is that it does not. `[web round 3, topic 7; its sources checked by Codex O; its program not rerun; the first two points made precise by Codex Q's review of revision 3, part 2 | proposed]` Whatever builds it must keep one boundary: declarations are resolved and each quotation fixed once, before any rule puts a body in place of a call; a quotation's content and the context of its variables are kept through that and through storing; ordinary arguments still run first; a part built during a run is given the same fixed graph (D-JIT-2); and a changed declaration is a new recorded reading (D-TB-2). `[R38 5.2; the boundary from LBR finding 5 | fold; the first set]`
Open, for the web round, as a request for sources: I recall a published claim that letting every function inspect its operands leaves few or no equations between different terms. Which result is it, under which assumptions about evaluation and observation, and does it bear on a quotation fixed when the text is read? This text rests on no such result. `[R38 section 3; LBR finding 6]`

**D-LB-4.** The order of widening, each step with its test. The first set, D-LB-2 over parts with no effect, is in this revision; the owner's record of the six answers also brings step 4 below forward into D-LB-3, whose test is still owed. `[R38 5.4; the condition on step 1 from LBR finding 4 | working; remaining widening steps are proposals]`
1. Laws read off the rules: an operation commutes with every total map of elements that has no effect, where the operation is one family across element sorts whose behaviour on structure does not depend on the sort, on anything chosen by the sort or on a representation, and where its rules, with every helper they call, never test an element, compare two elements, make a constant of the element sort, or apply an operation to an element. Until this is a theorem for this language's rules, whatever reads it off the rules is a decider named in the row.
2. Look-back laws over parts that have effects: each is a claim about the two runs at the selected interpretations.
3. A representation that remembers how a value was made, such as a value of a data sort held as a map not yet done. It is a representation like any other and owes its tracking claim, failures, runs without end and use included.
4. Brought forward into D-LB-3 by the owner's record of the six answers. It was: look-back that can be seen by declaration, under D-LB-3's boundary: applied by name only, never handed on as a function, no use-once variable inside, no following of variables.
Case for step 1's condition on sorts: a family that returns its argument where the element sort has one member, and the empty value of the argument's sort otherwise, tests no element and makes none, and does not commute with a map from a sort of one member to a sort of two. A check with maps inside one sort cannot find it.

#### Interpretation

**D-IN-1.** An interpretation replaces each sort, constructor, operation and effect of one theory by a term of another. It is applied by substitution, through the rules of defined symbols. It must preserve sorts. `[D L74; C44 | approved, as forced move 24]`

**D-IN-2.** Each law of the source becomes a claim at the interpretation. The claim is the law's statement, with the definitions it uses, carried through the map, and it is never given by the map. Where the map gives a defined symbol an image of its own, that the image agrees with the definition carried through is a further claim. `[D L74; C44 | approved, as forced move 24]` A derivation of a statement from the laws of the source, carried through the map, is evidence for the carried statement, with the carried laws as its assumptions. `[R36 door 3 | approved]`
Case: a law is a symbol, so a map over every symbol can send a law to true.

**D-IN-3.** An instance of an algebraic structure, a fold over data, a handler of an effect and a compiler stage are interpretations. `[D L74 | kept]`

**D-IN-4.** An interpretation is selected at a use by naming it, or by a default declared for a theory in a scope. Two defaults that both apply are a refusal that lists them. `[D L76 | agreed]`

#### Row

**D-ROW-1.** The row of a term is what it leans on. It has three sources. `[D L80 | agreed]`

**D-ROW-2.** Source (i). The declared operations, effects and laws reachable from the term, through its arguments and through the rules of defined symbols, less those a selected interpretation replaces. Declared sorts, and the constructors of a data sort, are not entries: they lean on nothing. `[D L82 | agreed]` A defined or evaluated symbol whose recursion has no evidence that it ends is an entry, as possible non-termination. `[C34 first point; C25 | owner (recorded): the first text's choice 6]` The answer not taken: a recursion with no evidence that it ends is an assumption, settled never, as D L83 had it.

**D-ROW-3.** Source (ii). Every claim the term rests on that is settled never, by name: an assumed membership, a tracking claim with no evidence, a clause assumed within the bound (D-TR-5), and the claim that a run ends, where a use relies on it and it is assumed. A program may run without assuming that it ends. `[D L83 | agreed; C34 first point | owner (recorded): choice 6; C28 | approved, as forced move 13]`

**D-ROW-4.** Source (iii). The row of the evidence of every other claim it rests on: the build that ran, a decider or checker with what it assumes, the laws a derivation used. `[D L84 | agreed]`

**D-ROW-5.** The meaning row is (i) to (iii) for the term as stated. `[D L86, L88 | author's]` The artefact row adds, for each representation chosen, (i) to (iii) for its trackers and its tracking claims. In slice 1 the default representation's tracking claim is settled never, and that is why the root row names the lowering and the backend. `[D L86 | agreed; "the backend" by the owner's record that keeps the backend neutral]`

**D-ROW-6.** Each membership claim of the term as stated is settled in one of three ways, and the term's admission says which: by evidence that passes through no representation; by a test at each evaluation (rule 7), and then the failure of the test is an outcome of the meaning; or never, by name. The meaning row is computed from these and from nothing chosen later. Evidence that a plan finds through a chosen representation, and that lets it drop the test, is entered in the artefact row with that representation's trackers and tracking claims. It does not change how the meaning settles the claim. A term whose statement names a representation as the ground of a membership has that representation as part of the term: it is then not a choice, and its row is in the meaning row. `[C50 as in R24 | approved, as forced move 28]`
Case: an operation asks that its argument be a pure braid. One representation's tracking claim would settle the membership by two laws; a second leaves a test in place. Without this passage the meaning row changes with the representation.

**D-ROW-7.** A row records effects, possible non-termination, open choices, axioms, unverified tools and the target machine in one account. A permission is a bound on the row. The row does not say in what order anything runs, which D-RUN-1 settles. `[D L90 | agreed]`

**D-ROW-8.** Each entry keeps its source, (i), (ii) or (iii), its role, and when it acts. The role is one of three: what the term does when it runs, what is assumed, and what is trusted. An entry of source (i) acts when the term runs, or only when a bound argument is called. An entry of source (iii) acts when its claim was settled: at build, at load, once in a run, or at each evaluation. Only the last two act in a run. A bound says which of these it limits. The test of a guard is part of the run it guards, and what the test reaches is in the row before the bound is read. A check that only the artefact makes, and the meaning does not, is in the artefact row. `[C35 | working; owner (recorded): the item is taken, and its test is still owed]` The answer not taken, which is also what stands if the test fails: every entry counts as acting in the run, which is safe and less exact.

**D-ROW-9.** A bound parameter names a row variable, and the operation's declared row bound may hold it. The row of an application is the declared bound with the argument's row put for the variable, and it keeps what evaluating the argument itself reaches. A definition is checked against the row bound it declares. Slice 1 has one fixed bound and exports no operation that takes a function, so it may count every entry as acting in the run. `[C35 | working]` GAP 6: the default bound is named and not stated.

**D-ROW-10.** With alternatives the row is a polynomial. Over the row's symbols, alternative routes add and joint requirements multiply. It is kept as a shared term and never expanded. Its free symbols are the set a reader sees. Read in true and false it answers a bound. `[D L92 | agreed]` The sum is over routes that the planner or the reader of evidence chooses among and records: two pieces of evidence for one claim, two representations for one sort, two trackers for one operation `[R36 door 5 | fold]`. Two branches of a run are not routes, and what either reaches is required. The row of a chosen plan holds the routes chosen. `[C34 second point | fold]`

**D-ROW-11.** Read in costs the polynomial gives an upper bound on the cost of settling, because it charges an entry once for each place it stands, and one settlement may serve several places. The bound holds where each job has one fixed cost that is not negative and all the work is counted. A settlement is a job: one checking program on one input, in one context, settled at one time (at build, at load, once in a run, or at each evaluation). The context holds the evidence the job rests on and the route that settled it. Two places share a job only when all four are the same. A guard settled at each evaluation is paid at each evaluation, and a checker run on two inputs is two jobs. The cost of a route is the summed cost of its distinct jobs, each for as many times as it must run. Finding the cheapest route is a search, because it contains the problem of the cheapest cover. The cost of running is not read from the row. It is counted on the chosen plan, by how many times each step runs. `[C34 third point, in place of the cost-reading clause of D L92 | fold]`
Case: (x + y)(x + z) with x at 5 and y and z at 3. The reading in costs picks y and z, at 6. Settling x once costs 5.

**D-ROW-12.** A symbol leaves the row in two ways. By answer: an interpretation supplies it, and its claims are yes. By indifference: every lawful answer gives the client the same observations. `[D L93 | agreed]`

#### Open choice and resolver

**D-OP-1.** An open choice is the effect pick of the theory Open. It takes a set and a continuation, and the continuation receives a member. `[D L97, L101 | author's]` Open has one law, and every resolver owes it: the answer is in the set. That the set is not empty is a claim at each pick. `[C36 | approved, as forced move 18]`

**D-OP-2.** The exchange is not a law of Open. It holds in one reading only: a term stands for its set of outcomes, and the pick is unresolved on both sides. There a pick may be exchanged with a step when neither uses the other's result, the step runs its continuation exactly once, and the move takes the pick neither into nor out of the scope of a handler or a resolver. Any other exchange is a claim about that pair. It names the two selected interpretations, the scope and what is observed, and it is settled as any claim is. `[C36, in place of the second law at D L97 | approved, as forced move 18; the condition to be tested]`
Cases: a step runs its continuation twice and joins the results; a pick from {0, 1} before it gives [0, 0] or [1, 1], and after it four outcomes. And a step runs its continuation once inside a resolver that answers 0; a pick before the step gives 0 or 1, and moved inside it gives 0.

**D-OP-3.** A resolver is an interpretation of Open: a term that answers each pick. What a resolver may read is its argument list and nothing else, and it is written down: the set alone; the set and a seed; or the set and the position of the pick in the run. The guarantee depends on it. A resolver that reads only the set gives one answer wherever the pick stands. One that reads the position does not. `[D L99 | agreed]` Where a program names no resolver, the default answers by the position of the pick in the source. The reader of text passes that position as an argument of the pick. The semantic part of the lock records the resolver and what it reads. `[D L99; C10 | fold]`

**D-OP-4.** Open, with its first test: whether a draw is a pick whose resolver reads a seed from a declared finite sort, with the promised law settled by counting seeds. The test is a fair coin against a constant, which must be refused, and against its own negation, which must be accepted with a matching of seeds. `[R30 3.2 | open]`

#### Representation

**D-REP-1.** A representation of a sort S, in a target theory U, consists of: `[D L105-L112 | agreed]`
- a sort N of U, whose values are the names;
- a relation names(n, v) between names and values of S, stated as a term;
- a signature: the operations on S that a client reaches. At a module boundary it is the exported operations, each with a declared row bound, and a client relies on the bound only;
- a tracker on names for each operation in the signature;
- one form for its hidden sorts, forward or backward, and the tracking claim of D-TR-1;
- where a name stands for many values, optional resolution and width claims.

**D-REP-2.** If a client can read a name's identity, its hash, its bytes, or the name itself as data, that reading is an operation on the hidden sort and needs a tracker like any other. Reading the term as stated is a different operation from reading the name chosen for it. `[C19 | approved, as forced move 7]`

**D-REP-3.** The naming relation is a relation and not a map: a name may stand for several values, and a value may have several names. `[D L108, L116-L125; said outright as R29 section 4 asks, wording new here | fold]`

**D-REP-4.** The target may be any theory. The cases below are one construct. `[D L114-L125 | agreed]`

| Kind | Target | The relation is given by |
| --- | --- | --- |
| Holding: a layout | A machine theory | A map from names to values, possibly from a sum of name sorts |
| Analysis | A lattice, or enclosures | A set of values for each name |
| Invariant or quotient | Any theory | A map from values to names |
| Embedding, or structure-preserving map | Any theory, or another model | A map from values to names |
| Approximate fit | A geometry | A bound on a distance between name and value |
| Late choice | Any theory | A set of values still to be chosen among |
| Code for one term | A machine theory | Running the code. A check for one program is the relation for one pair |
| A set given by a predicate | A test, a list, a generator, a constraint | Each answers some of member, enumerate, count and pick |
| Another algorithm for an operation `[R36 door 2, approved]` | The same theory | Equality: the names are the values themselves |

**D-REP-5.** A partial holding with an escape is a total holding into a sum of name sorts, and a guard is the case analysis inside a tracker. A listed set is a subset of the set it lists until its covering fact is settled. Turning a predicate into a list is solving, done by a proposer under a budget. `[D L127 | agreed]`

#### Claim and note, positions, usage

**D-CN-1.** A claim is a statement with a status and evidence. A note is an estimate, a sample, a candidate or a proposal. D-CL-1 and D-CL-3 give both records. `[D L131 | agreed]`

**D-CN-2.** A theory stands in one of three positions to a term. The term is stated in it, which is its meaning. The term leans on it, which is its row. The term is represented in it. The compiler may change one without disturbing the others. `[D L135 | kept]`

**D-CN-3.** Whether a value may be copied or dropped belongs to its theory. What a permitted copy costs belongs to its representation. `[D L137 | agreed]`

#### Facets

**D-FAC-1.** What other languages put into one word for a value's kind, this design keeps apart as facets. The word is the owner's: facets are the dimensions of what that one word used to cover. `[the owner's record on facets | approved, for the word]` The facets in use are five. Meaning: the sort, its theory, and what a model makes of it. Effects: what running does, shown in the row. Usage: whether a value may be copied or dropped. Representation: how a value is laid out and computed. Evidence: what is known about it and on what that rests. `[R32, "By concern", which cites a note that is not an input of this revision | fold]`
The count stays at five. `[the owner's record of the six answers, item 3 | decided]` This replaces "whether there are five or six is open, and is in the web round". What I found on checking the five against this text, kept as INFERENCE:
- The text's own division is three positions of a theory to a term, meaning, row and representation (D-CN-2), with usage placed in the theory and its cost in the representation (D-CN-3), and with claims as the record of what is known (D-CL-1). Those are the same five. But the row is not one facet: by D-ROW-8 an entry is what the term does, what is assumed, or what is trusted, so one row carries effects and part of evidence together.
- The three declarations on a sort (D-TH-7) do not fall under one facet either. Finite and data say what values there are, which is meaning, and they are covering facts, which is evidence (D-RL-2). Use-once is usage.
- The strongest candidate for a sixth is time: when a thing is known or acts. It appears inside four of the five: a quotation fixed at reading (D-TM-2), when a row entry acts (D-ROW-8), when a claim is settled (D-CL-1), and building ahead of time or during a run (D-JIT-1). With five facets, time is treated across the existing concerns; D-ROW-8 already lets a bound select when entries act. `[Codex C's review, repair 5 | fold; five facets by the owner's record]`
- A second candidate is identity: what makes two things one, by content for a node and by declaration for a declared symbol (D-TM-1). This comparison concerns identity of stored terms and declared symbols. A node is also an evaluator value whose identity is observable by same and memo (D-EV-2, D-REC-3). Fresh use-once values and activations remain distinct for run accounting, and identity observations on represented names still require tracking (D-UO-8, D-RUN-9, D-REP-2). A sequence is a third case: it is one thing by its own name and not by what it holds (D-SEQ-2), and D-ATT-1 asks what that does to "yes by identity". Identity is not a facet of its own; it is treated across the five, as time is. `[Codex C's review, repair 2 | fold; five facets by the owner's record]`
- What the web round said. Neither answer says six. One says seven views, adding cost and stage, and adds that kept as checked attributes inside the five "nothing substantive is lost". The other, which is cut off, says four, by merging usage with effects and interpretation with representation; it gives arguments before it stops, and the worked sections it promises are missing. Both say identity is not a facet, and both say the five cannot be changed independently of each other. `[web round 3, topic 9, both answers; sources checked by Codex O, none contradicted | outside input; the owner kept five]`
- Proposed: a facet is a separately usable view of what is said of a term, each with its own check. It is not a part that can be changed alone: the row's evidence entries follow from the route chosen for the meaning's claims (D-ROW-4), and a representation's row joins the artefact row (D-ROW-5). So "changed without disturbing the others" in D-CN-2 means that the meaning and its row are kept (D-ROW-6), and not that nothing else moves. `[web round 3, topic 9; Claude Arch | proposed]`

#### The foundation

**D-FND-1.** Mathematics is stated in theories hosted on a small core. Classical principles are declared laws, so they show in rows. A set given by a predicate on an existing sort is a subset of that sort. A predicate is always on a sort, so there is no set of everything. Foundations are connected to each other by interpretations. `[D L141; C3 | fold]`

**D-FND-2.** What the core is has three positions, and all are open. Slices 1 to 3 need none. `[D L141-L148; C48 | open]`

| Position | What it says |
| --- | --- |
| Home first | The default theory, Home, is an extensional dependent theory with universes, quotients, subsets whose membership is a claim, and proof sorts whose inhabitants are all equal. Lean's theory is included in Home if the first test below passes |
| Finite checks first | First a logic of finite checks only, in which statements are about the evaluator's own terms and induction has no quantifiers. Lean is a guest from the first day, and its results are attested with Lean's kernel named in the row. Home is grown from what programs and the SRE need |
| A framework that takes a theory as data | A small framework for derivations that takes a theory as data, its symbols and its rule forms with their side checks, and hosts both Home and the logic of finite checks |

**D-FND-3.** The tests. The first translates 1,000 library declarations, chosen to cover each feature of Lean's theory, and counts failures by feature. The second writes one chapter of mathematics that is not about matrices in both shapes. `[D L148 | open]` For the third position: before the trial, record the hash of the checker's whole trusted text, with the part that applies rules and the part that runs side checks. Add Home and then Lean's theory as data alone, and compare the hash. An unchanged hash shows the same bytes and no more. That each encoding is faithful, that its side checks are in fact run, and that no axiom came in with the data are checked apart, and every added axiom, side check and trusted program is entered in its theory and its row. A changed hash fails this trial and is explained; it does not show what every such framework must be. `[C48 | fold, to be tested in slice 4]`

**D-FND-4.** The third position's costs stand beside it. Where the framework rewrites, it owes whatever its checking procedure relies on, that the rewriting ends and comes to one result; a procedure with a bound may answer unknown. Where every conversion is written out, the size of the certificates is measured, with sharing, and not assumed. And where Home is said to include Lean's theory, including means: every statement carries over, every derivation carries over, and conversion behaves alike. A translation that leaves the guest's kernel in the row is attestation, not inclusion. `[C48 | fold]`

**D-FND-5.** PLACEHOLDER: Gemini's answer on lens 13, which bears on the foundation, is not in.

#### A sample

**D-SYN-1.** Loom syntax, invented and not run. Open: the surface syntax is not settled by anything in this text. `[D L152 | open]` GAP 9: rules and cases need one written form for terms, with its reading as nodes, and there is none.

```
theory Monoid
  sort M
  op   (·) : M, M → M
  law  assoc : (a·b)·c = a·(b·c)

interpret Monoid in ℤ with M = ℤ, (·) = (+)          -- assoc: a claim at this instance

def total (xs : Seq ℤ) : ℤ = sum xs                     -- no entry from source (i): a function

represent ℤ in Machine.Word64 + Big as I64              -- a holding; a sum of two name sorts
  names   Small w, z where z = signed w
  names   Big b, z   where z = b
  reaches (+) = add_checked, (·) = mul_checked

represent Graph in Poly ℤ as Spectral                   -- not a holding
  names   p, g where p = charpoly (adjacency g)
  reaches edges = − coeff p 2

claim spectral_edges : ∀ g : Graph. edges g = − coeff (charpoly (adjacency g)) 2
```
`[D L154-L174; the comment on total from C4 | approved, as forced move 1]`

### The tracking claim

**D-TR-1.** A tracking claim says that a representation's trackers do on names what the operations do on values: every outcome on names is an outcome of the meaning. It does not say the two have the same outcomes. `[D L178; C14 | approved, as forced move 5]` A statement about how often an outcome occurs is not carried by inclusion, and on an infinite carrier an equal law doesn't give inclusion either, so a program that draws owes both. `[R30 4.4, edit 2 | fold]`
Case: a meaning that may give 0 or 1 is tracked by a tracker that always gives 0, and by one that always gives 1. Changing between the two changes what a client sees (D-LOCK-2).

**D-TR-2.** A guarantee about two runs at once is carried by inclusion only in part. A statement that holds of every pair of the meaning's runs holds of every pair of the tracker's, which are among them. A comparison between the sets of outcomes at two inputs is not carried in general: that the two sets are equal is lost, and that they share no outcome is kept. A guarantee that is not carried is a claim of its own, with its own scope, and nothing is carried beyond what the stated comparison proves. `[C14 | approved, as forced move 5]`
Case: a meaning that may give either bit at either secret is tracked by one that gives the secret.

**D-TR-3.** A tracking claim has one form for all operations on a hidden sort, and one form for all hidden sorts of a representation. Mixing forms is unsound. Values that are chosen together are represented together, under one relation on the tuple. `[D L178; C11, which strikes the clause proposed at D L244 | approved, as forced move 2]` Open, run by nobody: a licence for mixed forms where the graph of which witness depends on which has no cycle. `[C11 | open]`
Case: hidden sorts F, forward, and B, backward, each with the values 0 and 1 and one name for both. make gives (0, 0) or (1, 1), and its tracker gives the two names. test(f, b) gives whether f = b, and its tracker gives false. Both pass the struck clause, and test(make()) is true in the meaning and false on names.

**D-TR-4.** The setting: a hidden sort S, names N, the relation names(n, v), a signature, and a tracker f\~ for each operation f in it. An observed sort is one the client can read. `[D L180 | agreed]`

#### Clauses common to both forms

**D-TR-5.** C1, sorts. Each tracker has the sort of its operation with S replaced by N.
C2, observed results. At an observed sort, related means equal. In a lax representation it may mean instead that the tracker's answer is a set containing the true answer, with a stated width. `[D L184-L185 | agreed]`
C3, signature. The claim covers a term only if every operation the term applies at S is in the signature, with each of its clauses, at the site of use, yes; or unknown and tested by a guard whose other branch is covered; or unknown and assumed by name within the bound. A clause that is no licenses nothing. An assumed clause stays unknown. It is an entry of source (ii) and a selection in the semantic part of the lock. No clause that discharges a machine-model condition is assumed (rule 10). `[D L186; C28 | approved, as forced move 13; "assumed by name" goes with D-ADM-4]` A representation is a candidate at a site only if each tracker's own conditions are yes there, or are tested there with a branch as D-TR-6 allows. `[D L188; R36 door 4, which is also G F01's repair | approved]`

**D-TR-6.** A tracker owes its clauses on the scope where its own conditions hold, and no more. The plan owes cover: at each site, for every call that the operation's own conditions admit, the chosen tracker's conditions are yes, or are tested with a branch to another representation. Each branch chosen has its clauses yes, guarded or assumed as C3 allows. The default representation covers every admitted call of an operation that has a way to run (D-PATH-1). It supplies no way to run, no assumption removes a test on a machine-model condition, and cover does not say that a call returns. `[C17, closing the question left open at D L188 | owner (recorded): the first text's choice 8. The narrower repair, that a condition may be tested at the site with a branch, was approved earlier by the record on R36's door 4]` The answer not taken: the representation owes that its trackers are defined wherever their operations are, and one that is not comes with its own escape or is refused.

#### The forward form: the world chooses the value

**D-TR-7.** A name may stand for several values, and whatever is said must hold for each. Layouts, analyses, invariants and quotients take this form. `[D L192 | agreed]`
- F1, start. For each operation c that makes a value of S from observed arguments a: names(c\~(a), c(a)).
- F2, step. If names(n, v), and f\~ is defined at n, then f is defined at v, the observed results are equal in the sense of C2, and the hidden results are related.
- F3, open choices. Where f leaves a choice open, F2 asks for some outcome of f. Where f\~ leaves one open, F2 holds for every outcome of f\~.

No reachable name is empty. That follows from F1 and F2. `[D L194-L198 | agreed]`

#### The backward form: the realiser chooses the value

**D-TR-8.** A name stands for values still to be chosen among. An implementation that settles a choice later than its specification takes this form. `[D L202 | agreed]`
- B0, non-empty. Every name reachable through the signature stands for at least one value. `[D L204 | agreed]` Where the claim is to cover a run without end, every reachable name also stands for finitely many values. Without that, a tracking claim in the backward form speaks of each finite stretch of a run, and whether the whole run ends is a separate claim about the client. `[C12 | approved, as forced move 3]`
- B1, start. Every value named by c\~(a) is an outcome of c(a). `[D L205 | agreed]`
- B2, step. If f\~ takes n to n′ with observed results o, then for every w with names(n′, w) there is a v with names(n, v) such that f takes v to w with the same o. `[D L206 | agreed]`
- B3, use once. S is use-once for the client. Copying, if wanted, is an operation of the signature with clauses of its own. `[D L207 | agreed]`

The "there is" in B2 is discharged by a witness term that a proposer supplies and the kernel checks. `[D L209 | agreed]`
Case for B0: the meaning picks a natural k, and tick counts it down, printing a until it prints stop. One name stands for every k, and its tracker prints a for ever. Without the added finiteness condition B0 to B3 all pass, every run of the meaning ends, and the run on names does not.

**D-TR-9.** A step relates whole configurations: all the hidden values that are live, with what holds between them. What a step consumes leaves the configuration, what survives stays, and what it makes joins. An operation with no hidden result keeps the old name only where the value survives. Where nothing survives, the configuration is empty, and the empty configuration is related to itself. This lets no live use-once value be dropped and no state be copied. How the obligation generator learns what each operation consumes and keeps is owed with slice 4. `[C47, in place of the last sentence of B2 at D L206 | approved as a design edit, as forced move 26; working, since its tests are still owed]`
Case: finish consumes a use-once bit and prints it, and one name stands for both bits. With the old sentence the name is still there after finish and no relation passes B2, yet the tracker is right.

**D-TR-10.** B3 behind a store. B3 does not mean that every object which chooses late must be passed linearly. Where the hidden state sits behind an effect such as a store, the effect's order threads the name, and the client copies a reference and not the name. `[D L211 | agreed as a reading]` B3 then holds where the state of the store's handler, which holds the name, is a use-once value, and the check accounts for every place that state is held: environments, the handler frames a continuation has captured, other names for the state, and the activations it belongs to. The name is a use-once pattern variable in each rule of the store's handler, so by clause (b) the rule uses it once and hands on the name its tracker returns. `[C24 as rewritten in R24, in place of the final sentence of D L211 | working; checked on two finite models, each reviewed by Codex Q: D-EVD rows 13 and 14]`

**D-TR-11.** What a continuation holds. The continuation that a handler receives for an operation is the part of the run between the operation and that handler. It holds the store's state exactly when the store's handler is live in that part: the store's handler encloses the operation, and the handler that answers encloses the store's. A handler inside the store's scope receives a continuation that does not hold the store. So does a handler whose continuation only goes on to make a store later: it holds code that makes one, and no state. `[C24 as rewritten in R24 | working; checked on two finite models, each reviewed by Codex Q: D-EVD rows 13 and 14]`

**D-TR-12.** A continuation that holds use-once state is a use-once value in the rule that receives it, whether or not its text names the state, and whatever multiplicity the operation declares. By clause (b) that rule runs it exactly once. A rule that never resumes, or that resumes twice, is refused. To hand such a continuation on is to pass a use-once value: to a parameter declared to be run once, or to a rule in the term that passes the check with that parameter read as use-once. An interpretation that is selected, and a lowering, keep the same count (D-RUN-9). `[C24 as rewritten in R24 | working; checked on two finite models, each reviewed by Codex Q: D-EVD rows 13 and 14]` The known-rule alternative is a check at one call; its caching and its relation to D-UO-5's declared-one boundary remain open. `[R24 section 6; G L92]` What happens where a rule answers a failure is D-UO-16. The other answer to D-TR-11 to D-TR-13, on record and not recommended: D-TR-13's ban by scope alone, which refused 87,196 of 92,176 right terms on the same model.
Case: one name stands for 0 and 1, and reading it gives 0 with a name for 0, or 1 with a name for 1. With the returned name handed on, two reads give (0, 0) or (1, 1). With the old name used twice, they give all four pairs. The order of the two reads is the same in both.
Case: an operation declared any, used inside one store and answered by an enclosing handler that resumes once. It is a right term, and the earlier form of this passage refused it for the declaration alone.

**D-TR-13.** Where the handler is not in the term: the operation is performed by a bound argument, or is answered by an interpretation selected later, or by a handler outside the term that is checked. Then nothing can be counted and the declaration decides. Inside the scope of a store's handler, such an operation may be used only if the multiplicity of its continuation is declared one, and by D-UO-3 whatever answers it then resumes exactly once. This is a ban by scope. It is sufficient and not exact: it does not say that the continuation holds the store, only that the check cannot tell. An operation that narrows a choice returns a new name. A failure or a stop for a resource inside the scope is owed as D-TR-15 says. A new name alone is no evidence of B3. `[C24 as rewritten in R24 | working; checked on two finite models, each reviewed by Codex Q: D-EVD rows 13 and 14. The fallback where the recipient is not known, and the limits on capture and its cache, stand]`

#### Lax representations

**D-TR-14.** A lax representation is in the forward form and may add two claims. Resolution: for each value and each width asked for, some name stands only for values within that width. Width: a bound on how much a tracker widens its answer. A request for a result to a given precision is a claim about the result's name, checked on the result. A representation whose resolution claim is no is refused such a request before it runs. `[D L215-L220 | kept]`

**D-TR-19.** A width claim, like every clause, is stated for a name and a value it stands for. It says nothing of a name that stands for no value. A representation may offer a decided predicate on names that every constructor's tracker establishes and every tracker keeps, as evidence for a claim that would otherwise range over all names. That it is kept is a clause to be checked. `[R34 L9-6, adding to D-TR-14 | fold]`

#### Clauses for effects

**D-TR-15.** The clauses above are for operations that return. Five more cover those that may not. `[D L224 | agreed]` An operation with a continuation. If the arguments are related, and the continuations are related as whole computations at every related result, under related captured values and related handler state, then the two runs of the operation are related: for each run on names there is a run of the meaning, as the form of the claim requires, with the same observations in the same order, then related results or the same failure, and the same consumption of each use-once value. Two runs are compared as wholes. That the continuation's results are related says nothing of how often it ran, or of what it captured. A run without end, and steps that one side takes alone, are owed as D-TR-18 says, and a stop for a resource as D-TR-17 says. `[C15, in place of the clause at D L228 | approved as a design edit, as forced move 6. One finite reading of it, with stateful callbacks, has been run and reviewed: D-EVD row 16. The general clause is open]`
Case: a handler that resumes twice, or never, is handed the same continuation as one that resumes once, and the three runs print different things.

**D-TR-16.** A failure. A failure is an observed result. Where the operation fails, the tracker fails, and the payloads are related as results are: equal in the sense of C2 at an observed sort. A failure that no client catches is reported by the host, so its payload is observed unless the host's theory reports none. A tracker does not return where its operation fails, and it adds no failure of its own except by the resource clause. `[D L229 | agreed]` GAP 7: what a host's theory reports is part of the host boundary, which has no content yet.

**D-TR-17.** Running out of a resource. The same outcome, or the realiser stops where the meaning does not. The resource is named in the row. `[D L230 | open. Finite checks of agreement at a stop are run and reviewed, D-EVD row 15; this whole clause has no test and no proof]`

**D-TR-18.** Steps that only one side takes. Where the realiser takes steps the meaning does not, or the reverse, the relation holds across them, and a measure in a well-founded order falls at each such step, so that neither side stalls the other for ever. Code for a term with a loop is a name for it only under this clause. `[D L231 | open]` Not ending. The tracker's run fails to end exactly where its operation's does, apart from the resource clause. `[D L232 | open]` Both are owed for the client's run and not for each operation, since every operation can return while the client's run on names never ends. In the backward form the measure for one-sided steps falls as the matching value is sought backward from a given step, and not along the run. `[C16 | fold; read, not run]`

### Claims

**D-CL-1.** Every fact in the store is a claim, and a claim never says more than its statement. A sort membership, a law at an interpretation, a tracking clause, a covering fact and a width are all claims. `[D L251 | agreed]`

| Field | What it holds |
| --- | --- |
| Statement | A proposition whose quantifiers name their domains. Its scope is part of what it says |
| Status | Yes, no, unknown or conflict. It is a reading and is not stored (D-CL-2) |
| Evidence | One of three kinds. A derivation. A run record: program, input, output, step bound and the build that ran it. A counterexample, which may be a set of values |
| Assumptions | The claims the evidence used and did not discharge. Evidence with assumptions is a rule |
| Row | The polynomial of D-ROW-10 |
| Settled | When, and by which route: at build, at load, once in a run, at each evaluation of its site, or never |
| Notes | The notes about this claim. A note is not evidence, and no licence can cite one |

`[D L253-L261 | agreed; the status row from C32 | approved, as forced move 16]`

**D-CL-2.** Evidence is never changed or removed. The status of a claim is a reading of its evidence at a site, under a bound, at one state of the store, by rule 4. It is yes, no, unknown or conflict, and it is not stored apart from those three. Where admitted evidence gives yes and admitted evidence gives no for one statement at one site, the reading is a conflict. A conflict licenses nothing. Its message gives both pieces of evidence with their rows and does not say which is at fault: something that one of them rests on, in its row or in the trusted base, is false. `[C32 | approved, as forced move 16; the records to be tested]`
Case: evidence for P licenses a plan. Evidence against P arrives later. The hash of the first is unchanged, the old build still replays, and a new build reports the conflict.

**D-CL-3.** A note has a record of its own: the nodes it is about, its kind, its method and its content. The kinds are estimate, sample, candidate and proposal. A note may stand alone, as a candidate theory does. `[D L265 | agreed]`

**D-CL-4.** A run becomes evidence by one of three rules, Eval, Close and Reflect (D-RUNEV-1). In slices 1 to 3 every claim is settled by a run. Derivations arrive in slice 4. `[D L263 | agreed]`

#### Rules on claims

**D-RL-1.** Rule 1, scope. For a statement about every member of a set, a yes passes to subsets and a no to supersets. For a statement that some member exists, the directions reverse. `[D L269 | agreed]`

**D-RL-2.** Rule 2, exhaustion. Running every case counts for a sort only with a covering fact. A covering fact has three kinds: the sort is declared finite with these values, the sort is declared data with these constructors, or a proved claim says that an enumeration misses nothing. Without one, the result is a yes for the enumerated set, by name. `[D L270 | agreed]` The covering fact that a sort is data with these constructors covers a case split by constructor. It does not make an enumeration up to a size exhaustive. `[C30 | fold]`

**D-RL-3.** Rule 3, membership. Using a scoped yes at an object needs evidence that the object is in the scope. `[D L271 | agreed]`

**D-RL-4.** Rule 4, reading at the site. Evidence is read where it is used, with each assumption replaced by the site's own evidence. All yes gives yes. One unknown gives unknown, naming what is missing. One no gives nothing from this evidence. `[D L272 | agreed]`

**D-RL-5.** Rule 5, backward from a no. A conclusion that is no, with every other assumption yes, makes the remaining assumption no. `[D L273 | agreed]`

**D-RL-6.** Rule 6, unanswerable. That a name cannot answer a question is shown by a set of values with that name, one refuting each candidate answer. `[D L274 | agreed]` A refutation is a record. It names one representation with its naming relation, one scope of values, the question with its interpretation, and the whole set of answers the question admits, with any width. It holds the values, and for each value evidence that the value has the name under that relation and evidence of its answer to that question. Every piece is for those same four: that two names are one node does not by itself show that two values have one name under the relation. The reader of evidence checks each piece, checks that the names are one node, and checks that no single admitted answer is right for all the values. It then reads no for that name, that question and those admitted answers, and for nothing wider. What it read is recorded as D-RUNEV-2 and D-LOCK-3 ask. One right answer, and intervals of a stated width, are two kinds of admitted answer and not the only ones. For the others, and for a refutation by infinitely many values, D-RL-7 says what evidence is owed. The values need not be all that have the name: it is enough that no admitted answer is right for all of those given. A pair suffices only where D-RL-7 says so. `[C49 as fixed in R24 | approved, as forced move 27; the record to be tested]`
Case: two braids with one name and traces 0 and 2. The no rests on two runs that give the name, two that give the traces, and the comparison 0 is not 2.

**D-RL-7.** When a pair suffices. A pair suffices when the question has one right answer, and when answers are intervals on a line. The second half is about the sets of right answers, one set for each value that has the name, all in one ordered space of answers. A pair suffices where the name stands for finitely many values and each set is an interval. Where it stands for infinitely many, a pair suffices where the answers are real numbers, each set is a closed interval, and at least one of them is bounded. An interval that is itself returned as an answer is not this case: where any bounded interval that holds the value is a right answer, every finite set of values has a common answer and the set of all natural numbers has none. Another kind of answer may bring its own checked theorem that a pair suffices. Otherwise any finite set of values with that name and no common right answer refutes, and it is checked by computing where the answer sort decides, for a finite set of values, whether a common right answer exists. Where no finite set will do, the refutation is the whole set of values, given by a derivation that names the covering fact for that set. What a refutation shows is in D-RL-6; this passage says when two values are enough. `[D L274; C45 | approved, as forced move 25; the two sentences from "Otherwise" are R34 L9-3, in place of C45's one | fold; last sentence R29 section 4]`
Case: the right answers for the value v are the numbers from v up. Any two values share an answer and no number is right for all.

**D-RL-13.** The program that checks a refutation is an entry of the obligation generator for tracking clauses. It reads a record of the name, the question, the witnesses, a claim for each that the name stands for it, a claim for each of its right answers, and the check that no answer is right for all. What it settles is that this name cannot answer this question. It settles nothing about a family, and it sets no status (D-CL-2). Each answer sort that wants refutations supplies the decided check, with a soundness claim as D-RUNEV-2 asks. `[R34 L9-3, adding to rule 6 | fold]`
Case: three disks of radius 1.1 at the corners of a triangle of side 2 meet in pairs and not all three. No pair refutes, and three values do.

**D-RL-8.** Rule 7, guards and assumptions. An unknown claim that has a test is settled at each evaluation of its site: that is a guard, and for a representation the other summand of the name sort is where the value goes when the test fails. A guard on a membership has no slower branch (D-ADM-4). An unknown claim with no test is settled never, and shows in the row. `[D L275; C26 | approved, as forced move 11]`

**D-RL-9.** Rule 8, kinds are not ranks. Proved for every input, computed exactly for one object, held on an enumerated set, and estimated differ in statement and in evidence. They are not points on one scale. `[D L276 | kept]` "Estimated" is read as a note until the third part of D-PR-6 is taken up. `[R30 4.4, edit 3 | fold]`

**D-RL-10.** Rule 9, what a use must assume. A row lists what the evidence leaned on. A use of the claim may need less, as the table below sets out, and a bound may be stated against what a use needs. What a use must assume is read from the statement, the evidence that settled it and the site, after rule 4. The statement is read after its definitions are unfolded to a fixed core. A statement that leaves the core, by a quantifier over sets or functions, by a definition that is not unfolded, or by a check not shown to end, takes the last row. Where the evidence gives a witness for every input in the statement's scope and each witness is checked, the assumption of the third row is not needed. A finite result sort serves the same way only with its covering fact, a search that ends, and the evidence of what the search found. Neither removes what D-RUNEV-2 asks: the soundness claim of the checker that accepted a witness, and what that claim rests on, stay in what the use assumes. `[D L277; C46 | working]`

| Form of the statement | What a use must assume |
| --- | --- |
| A statement of the form f(v) = w, settled by Eval. That a checker returned yes on P is such a statement | The build, and nothing else |
| A finite check that holds for every input, proved in some theory | Only that the theory is consistent: were an instance false, the theory would also prove that it fails |
| For every input some output exists, used as a fact | That the theory proves no false statement of that form |
| Any other statement. P itself, where a checker returned yes on P, is here: a use assumes the checker's soundness claim and what that claim rests on | The laws listed |

`[D L280-L285; first and last rows C29 | approved, as forced move 14]`

**D-RL-11.** Two conditions on rule 9. Where the finite check answers no at an input, the theory proves that it does. And rule 9 is read after rule 4: a law that is no at the site makes the theory inconsistent there, and the evidence still gives nothing. `[D L287 | author's; first condition as C46 reads it | fold]` Until the foundation of slice 4 names a core, only the first and the last rows of the table are used. Owed with it: the grammar of the core; which definitions are unfolded, by a procedure that ends, with a bound past which a statement takes the last row; which evidence each row requires; and, for the second row, the program or derivation that turns each run that answers no into a proof in the theory. Cases the reader of evidence must then pass: a statement and its unfolding take the same row; a definition that hides a quantifier is found; a definition that names itself does not keep the reader unfolding for ever; and two kinds of evidence for one statement take different rows. `[C46 | working; owner (recorded): the item is taken, and its test is still owed]` The answer not taken: the middle rows of the table are used now, as D L280-L285 give them.

**D-RL-12.** Rule 10, a guard on the machine model is never removed by an assumption. A machine theory marks the conditions its own model depends on, such as an index inside its array. A claim that discharges one must be yes, or be tested at each evaluation. It may not be settled never, whatever the bound admits: one false assumption there could corrupt the memory that every run record rests on. The same holds for every claim its evidence rests on: its row has no entry of source (ii). And its row holds a declared law only if the machine theory itself declares it. Any other guard may be removed by an assumed claim when the bound admits it, and the assumption goes in the semantic part of the lock. `[D L278; C33 | approved, as forced move 17; its wording is still to be tested]`

#### Chance

**D-PR-1.** A claim is settled yes, no or unknown by a derivation, a run record or a counterexample, and no claim carries a confidence; chance may be what a statement is about, and since tracking keeps which outcomes may occur and not how often, a program that promises a law owes that law as a claim of its own. `[R30 4.1, sentence 1 | approved]`

**D-PR-2.** A proposer, resolver, test generator or sampler may draw at random if its program and its seed are recorded; what it returns counts only by the check then run on it, a search that finds nothing reports unknown, and a seed fixes one run and is evidence of no law. `[R30 4.1, sentence 2 | approved]`

**D-PR-3.** A result on a census, a sample or a test corpus is a yes for those members by name; induction from it reports the whole set of hypotheses, in a declared language, that agree with every settled entry, and reaches an unlisted input only by a covering fact, a derivation, or a statement in the form of D-PR-4. `[R30 4.1, sentence 3 | approved]`

**D-PR-4.** A guarantee in probability is an ordinary statement that names what is drawn, by what law, the event and the bound, settled by a derivation that covers every step from the draw to the statement; a use of the sampled conclusion itself rests on one named assumption, settled never, that the recorded draw was not a bad one, which a bound on the row may refuse and rule 10 always refuses; and two bounds combine only by a derivation. `[R30 4.1, sentence 4 | approved as the only allowed form; deferred, nothing built]`

**D-PR-5.** A score, whether a code length under a named decoder with every part counted, a cost, a worth or an estimate, is a note recorded with its method; it orders proposals inside a set that exact checks have already fixed, it gives the one claim that this program returned this number on these bytes, and entropy is said only of a distribution that is itself a term. `[R30 4.1, sentence 5 | approved]`

**D-PR-6.** What was one open item, guarantees in probability and a theory of distortion, is three. `[R30 4.2, in place of D L474 and L539; G F07 | fold]`

| Part | Standing | What it is |
| --- | --- | --- |
| Distortion | Open. Exact work, with no chance in it | That an answer holds the true value, and that it is narrow, are two claims. An operation carries error by a law of its own. Lens 10 has a first design, unreviewed. R30 reports gaps in it: a name that no value fits passes vacuously, and one-sided answers get a field and no law |
| Laws of programs that draw | Open. Exact work | On a finite seed sort: by counting, as D-OP-4 proposes. On infinite carriers, lens 10's kernels are the candidate, and wait for the real numbers |
| Guarantees from a sample, or from a check that draws | Deferred, not dropped | The form is D-PR-4. Nothing is built until the first job where an exact check has been measured as unaffordable and a derivation of the bound exists. Until then such a result is a note |

### The store and its queries

**D-STO-1.** The store is one graph, addressed by content. It holds terms, theories, interpretations, representations, claims, evidence, notes and built artefacts. Anything may add a term, a proposal or a note. Evidence is a derivation, a run record or a counterexample. A run record is evidence relative to the build it names until the evaluator replays it. `[D L293 | agreed]` GAP 4: the bytes that content identity hashes are not given.

**D-STO-2.** A check is cached under the checking program, the claim, and a record of every question it put to the store with the hash of each answer, including the answer that nothing was there. It is reused only while every question still has the same answer. A new declaration that makes a once-unique default ambiguous therefore reruns the checks that asked. `[D L295 | agreed, not run]`

**D-STO-3.** The queries. `[D L297-L309 | agreed; the candidates row from C28, the reach row from C39 | approved, as forced moves 13 and 21]`

| Query | What it returns | Answered by | Can it license |
| --- | --- | --- | --- |
| Row of a node | The polynomial; its symbols; its reading under a bound | A kernel program | Yes |
| Status of a claim at a site | Evidence read at the site, by rules 4, 9 and 10 | A kernel program | Yes |
| What a term reaches at a sort | The uses, taken against a candidate's signature (D-STO-4) | A kernel program | Yes |
| Candidates for a term at a sort | Representations for which each clause, for that signature at that site, is yes, or has a test that the plan places as a guard, or is assumed within the bound. The answer says which, clause by clause | A kernel program over the above | Yes |
| Is this object in a recorded scope | Membership evidence, or unknown | A kernel program, or a guard | Yes |
| What rests on a claim | Every claim and artefact that would change if it were settled either way | A graph walk | It informs |
| The cheapest route to a goal | A plan: the polynomial read in costs (D-ROW-11) | The planner, a proposer. Each step is checked | No. The checks do |
| The worth of an open claim | The difference of two such readings | A proposer | No |
| Which unknown claims would give this goal | Sets of claims, each with a way to be settled and a cost, that derive the goal and derive nothing that is no | A proposer under a budget | No. An answer is a proposal |
| Candidate theories | Implications over the table of laws at instances, each with the instances it was found on and the cheapest question that would refute it | A proposer | No. A candidate is a note |
| Find a value that satisfies a predicate | A value and its membership evidence, or unknown at the budget | A proposer under a budget | The evidence does |

**D-STO-4.** The walk that gives the first source of the row gives two results. The row follows the rules of every defined symbol and leaves out constructors. The uses are taken against a candidate's signature: the walk does not enter the rules of an operation that the signature lists, and reports that operation as a use. It enters the rules of every other defined symbol, whatever sorts its own signature mentions, and reports what it finds. A constructor of the sort is a use, and so is a pattern that matches one, as an operation that inspects a name (D-REP-2). It is one text with two results, and the second is counted in the trusted base. `[C39 as in R24, in place of the idea at D L856 | approved, as forced move 21]`
Case: a client calls its own step function on a braid, and the step function calls the operation that adds a crossing. Following every rule, the walk reports the stored matrix and no operation. Stopping at every symbol whose signature mentions the sort, it reports the step function, which no representation lists.

**D-STO-5.** The answer to "which unknown claims would give this goal" is the row polynomial of the goal with yes and no substituted, plus one check for each refuted claim. Where a goal needs some r that meets several requirements, the polynomial is the sum over r of the product of r's requirements, and never the product of the sums. A set of claims is offered only when the set as a whole derives nothing that is no. The table behind candidate theories is three-valued, and an unknown entry neither supports nor refutes. Each candidate is spent as a question for the query before it. `[D L311; C40 | approved, as forced move 22]`

**D-STO-6.** A refusal says what would lift it. When a goal is refused, the message lists the answers to "which unknown claims would give this goal". Guard placement is the same query, limited to claims that have a test. `[D L315-L317 | agreed]`

**D-STO-7.** Abduction ranks induction and does not bound it. The candidate-theories query orders its conclusions by the unknown-claims query: a law that some open goal's explanation contains, at an instance where it is unknown, is taken before one that no such explanation contains, and the second is not refused for that. Worth has an exact source: the goals that the law would give. The order is exact; a random schedule over it, which the web round's answer also offers, stays under the owner's rule that exact methods come first. `[the owner's record of the six answers, item 4: rank, not bound | decided provisionally, with a note to reconsider]` This replaces the approved direction, "abduction bounds induction", under which a law was worth inducing a theory for only if some open goal's explanation contained it. **Open, by the same record:** to reconsider ranking against bounding before the design closes; the owner had no view either way. The language of hypotheses is declared and recorded with the result: which laws may stand in a body, and how long a body may be. For each instance where the conclusion is yes there is a bottom: the laws that are yes there, kept to those the store's rules connect to the conclusion or to the goal, and a body is a part of every such bottom. With three values there are two sets, the hypotheses that surely agree with every settled entry and those that would agree if some unknown entries came out one way; the unknown entries on which they differ are abducibles again, and the guaranteed split of my card 0027 report, section 4.1, orders them. The kept set is one note, with one exact claim. The note holds the conclusion, the instances for and against, the language, and the set, by its most specific member and its most general members, or "not listed, at this budget". The claim is: in language L, the hypotheses that agree with every settled entry of table T are exactly these. For a finite L that is settled by exhaustion with L's covering fact. A kept set predicts an unknown entry only where every member that applies agrees, and the prediction is still a candidate. A score orders members inside the set and never decides membership.
Three corrections from the web round, proposed. First, "a body is a part of every such bottom" is the positive-coverage condition for a classifier, whose negative examples must also be excluded, and as a rule for implications it throws away valid ones: with rows (A, B, Q) of (1, 0, 1), (0, 1, 1) and (0, 0, 0), "A gives Q" and "B gives Q" both hold and the rule keeps neither. An implication fits a table exactly when no row has its body true and its conclusion false; the job must say which of the two it wants. Second, the set may have no single most specific member in the declared language, and its most general members can be far more than the table: in the answer's constructed table, 21 rows over 40 attributes in 20 pairs leave 3^20 survivors with 2^20 most general among them, described by one formula of 20 clauses. That is one witness, not a property of every table of that size. So the note may hold the set as a formula, and says "represented but not listed" apart from "not determined". Third, laws that are each possible need not be possible together: with P = 1, Q unknown and R = 0, "P gives Q" fits if Q is 1 and "Q gives R" fits if Q is 0, and the two fit under no one value. A candidate theory is judged whole, under one completion of the unknown entries. `[web round 3, topic 4; its sources checked by Codex P, one supported and one partly; the three cases checked by hand; the first two made precise by Codex Q's review of revision 3, part 2 | proposed]` The same answer's proposal that abduction should rank and not bound induction is now this passage's direction, by the owner's record above. `[R30 5.2; G F06 | the direction is now the owner's provisional record; application conditional on the 56-candidate test, which is not run]`

### The stages

**D-STG-1.** Five stages, each ending in claims written to the store. The row is checked before representations are chosen and again after. `[D L323-L331 | agreed for the last sentence, kept for the rest]`
1. Read. Text to tree to graph. The tree is kept for messages and formatting only. Text that has an effect inside an argument is turned into continuations, left to right.
2. Mean. Sort membership, laws at interpretations, and the use-once check. A claim that cannot be settled is recorded as unknown, with when it could be settled.
3. Row. The meaning row is computed and checked against the bound. A failure here is final.
4. Represent. The planner chooses representations under the bound and reads each licence at its site. A claim to be settled at evaluation becomes a guard. The artefact row is the meaning row joined with the row of each representation chosen, and it is checked again.
5. Emit. The last representation is into bytes. The bytes are decoded by the machine theory's own decoder and compared.

**D-STG-2.** Decoding shows that the bytes are the chosen machine program. That the machine program does what the term says is the tracking claim. That the bytes loaded are those bytes, with the bindings the plan names, is checked at load. `[C38 | approved]`

**D-STG-3.** What a term needs in order to be admitted is settled for the term as stated, and its evidence or its assumption is in the meaning row, whatever produced it, an analysis included. Where a term is admitted with a guard and a representation chosen at stage 4 removes the guard by its tracking claim, that claim's row is in the artefact row alone, and the meaning row keeps the entry for the possible failure. `[R34 L9-4, adding to stage 4; it agrees with D-ROW-6 | fold]` So a program whose bound refuses a possible failure is refused even where a later analysis would have removed every guard, unless that analysis is brought forward as evidence for the term as stated. The writer chooses.

### Admission

**D-ADM-1.** Every symbol has a signature, and every definition and literal is checked against it. `[C25 | approved, as forced move 10]`

**D-ADM-2.** A term is admitted in a context, the sorts of its variables. A variable has the sort its context gives it. An application of a symbol is checked against the symbol's signature, argument by argument, by the membership claims of D-ADM-4, and has the result sort of the signature after substitution of indices. A bound argument is checked with its variables added to the context at the sorts its parameter declares, and its body must be a member of the result sort its parameter declares. A binder carries no sort of its own. A binder that is applied takes the sort of its variable from the checked argument. A binder that stands anywhere else is refused. Each rule of a defined symbol is admitted once, as a scope: its patterns are constructor terms of the parameter sorts, each variable takes its sort from the place it stands at in a pattern, and the right-hand side must be a member of the declared result sort. Each image in an interpretation is checked against the source signature carried through the map. `[C25; C6 | approved, as forced move 10, for the checking of signatures; where a binder may stand goes with the concurrency core]` D-CONC-2 adds one more place a binder may stand, a bound parameter of a constructor, if the core is taken. That answers the choice the first text put to the owner here.
Case: a symbol declared to give a truth value, with the one rule f() = zero, has a signature and is wrong.

**D-ADM-3.** A literal is a member of its sort by a claim, settled by a run of the sort's literal check on the sort's indices and the value. The check is a definition in the evaluator's language that the sort's signature names. Where it is the sort's only account of its literals, it says which values they are, and it owes no claim that it is right. A sort declared finite has no check of its own: its literals are the values listed. A sort that names no check and lists no values admits no literal. A check that is meant to agree with some other account of the sort owes the claim that it does. A check that runs out of fuel leaves the membership unknown, and the literal is refused. A value of a data sort is a constructor term and never a literal. `[C25 | approved, as forced move 10]` GAP 5: how a value of a data sort crosses the evaluator's edge is to be tested.
Case: a literal that says it is a vector of length 4 and holds three numbers. And a sort declared finite with the values 0 and 1, with a check that also passes 2.

**D-ADM-4.** Sort membership. The obligation generator emits one membership claim for each application, in the context of that application: the argument, already checked at a sort T, is a member of the parameter's sort S after substitution of indices. Where T and S are the same node the claim is yes, by a run of same. Where they are not, nothing follows: the claim is unknown, and never no by that. An unknown membership with a test becomes a guard. A guard on a membership has no slower branch: where its test fails the run fails, and that failure is an effect in the meaning row. An unknown membership with no test is a refusal, unless the program assumes it by name. It is then an entry of source (ii) and stands in the semantic part of the lock, and rule 10 still holds. `[C26, in place of D L335 | approved, as forced move 11; the assumption by name: owner (recorded)]` The owner's answer, by the record on the two slice 1 choices: membership by name is allowed as a named opt-in assumption, switched on in slice 2 with the permission controls, refused in slice 1, and never under rule 10. The answer not taken: always a refusal, until evidence exists.

**D-ADM-5.** An evaluated symbol is defined in the evaluator's language. The reference run applies the definition to checked argument values and checks the result as below. The numbers, bytes and arrays of the standard theories are given this way, so no native tool stands in the meaning row of arithmetic. `[C7 | fold]` An evaluated symbol takes and returns no value of a use-once sort: the evaluator copies its values freely. It receives checked values, and its result is checked before it is used: a literal by the literal check of the result sort, a constructor term by admission, field by field. The label on a result is not evidence. A build that runs a definition by other code than the evaluator owes that the two agree (D-TB-6). It adds nothing to a row beyond the build, except that an evaluated definition that is not total by its syntax adds possible non-termination. `[C25, which amends the last sentence of C7 | approved, as forced move 10]`
Case: an evaluated definition that puts one incoming value into both fields of a pair. Each field has the right sort and one value has become two.

**D-ADM-6.** A signature may list conditions: statements over its indices and parameters, with the arguments put in at each call. At each call a condition is a claim the term rests on, beside its membership claims, settled as D-ROW-6 says. A statement is not a test. Where a condition has a test, the signature names the test and the claim that ties the test's outcomes to the condition, with what D-RUNEV-2 asks of that claim. A test that does not finish, or that fails for want of fuel, settles nothing. `[C51 as fixed in R24 | owner (recorded): the first text's choice 7; working, since its test is still owed]`

**D-ADM-7.** A test runs before the operation, in the order the conditions are listed, on the argument values the run has already obtained. It does not run the arguments again. The guard and its failure are admitted with the call, under the ordinary checks of sort, context and use-once. A test may not consume an argument that the operation then uses, unless it hands the value back; without that the guard is refused. A test, its condition and its failure stand in the row, with their roles and times (D-ROW-8), and in the cost of the call. A test left at a call is a use that C3 sees (D-STO-4); a tracker that takes the test inside owes the behaviour of the whole guarded call. That a condition is yes does not by itself let a plan remove what its test does: an effect, a choice or a possible run without end stays unless D-RUN-6 and D-TR-15 let it go. A machine theory marks which conditions of its operations fall under rule 10, with what D-RL-12 asks. No sort is made by a condition: the argument keeps its sort, and the claim is about the call. `[C51 as fixed in R24 | owner (recorded): the first text's choice 7; working, since its test is still owed]`

**D-ADM-8.** The owner has since taken D-ADM-6 and D-ADM-7, so the comparison below no longer decides between the two; it is kept as a check on that choice. The answer not taken: the demand is a sort of its own, made by a predicate, with a conversion at each call. Whether a condition on an argument is better carried as D-ADM-6 has it, or as a parameter sort cut out by a predicate, with membership as a claim under D-ADM-4, goes to test. `[R34 L9-9 | working]` The test: write a pure braid and an index below a bound both ways, count the records touched, and see whether either form fails to state a condition on two parameters at once. It checks the owner's choice; a failure is reported to the owner and does not select the other answer. `[Codex G's review of revision 2, F01 | fold]` A second mark for rule 10 on a source signature is not taken: the machine theory marks those conditions (D-RL-12).

### Order of evaluation, and the reference run

**D-RUN-1.** Order. `[D L339-L342 | agreed; the first and last bullets as C36 reads them, G F02 | approved, as forced move 18]`
- An operation with a continuation runs where the term puts it. Two such operations may be exchanged, shared or dropped only by a claim about the two at their selected interpretations. That two operations have different row symbols gives no exchange.
- Row entries that are laws, tools or models impose no order.
- A term that may not terminate is never dropped or run early without evidence that it terminates.
- Moves of an open choice use D-OP-2. Its set-of-outcomes reading applies only while the pick is unresolved on both sides, under the conditions there; every other exchange needs the claim about the selected interpretations, scope and observations named there.

**D-RUN-2.** The reference run is a program for the evaluator, called step. It is call by value: the arguments of an operation run before it, left to right. The rules of one symbol are tried in the order written, and the first whose patterns match is applied. A pattern is built from constructors and variables, each variable once. At an operation with a continuation the run stops and asks. This fixes what the reference does. The compiled program must agree with it (D-RUN-9), and each slice checks that agreement on generated inputs. `[D L346 | agreed, not run]`

**D-RUN-3.** An argument runs each time the operation that holds it runs, in that operation's activation. A variable stands for the value already bound to it in the activation of its binder, and using it runs nothing again. So a run must be shared only where the term binds it. The run may also reuse a result it has already obtained, where reuse cannot be seen: for a term with no effect, no open choice and no use-once consumption, whose result may be copied, at the same values of its variables. Whether a term consumes is read from what its run does and not from its free variables: read(K()) has none, and consumes. This is beside what D-RUN-6 allows, and it needs no evidence that the term ends. It never lets a run that has not finished be skipped, dropped or made early. That two pieces of code are one node is never by that a reason to reuse. `[C22 second bullet, in place of the shared-node sentence of D L346; the words on copying and on consuming from R29 section 4 | working: C22; the R29 words approved]`
Cases: pair(work(), work()) with work costly is two runs by the definition, and one where the run reuses. pair(K(), K()) with K a producer of a use-once value is never reused: one result would stand at two places. Codex S ran both on a fixture of 44 cases, and Codex Q confirmed it (D-EVD row 17): under the old local test for reuse, without the words on copying, one use-once result does stand at two places.

**D-RUN-4.** A writer who wants one run of a costly term names it. A rule step may copy a value where its sort allows, and must bind a term that has not run before it puts it in two places. Nothing changes for identity: sort membership by same, laws that are yes by identity, caches and claims are about code and stay on nodes. `[C22 | working: C22]`

**D-RUN-5.** First match is for a run, where the arguments are values. On a term with variables, a rule is applied only when no earlier rule could match an instance of the term. `[D L350 | author's]`
Case, observed in the old toy (D L350; D-EVD row 11): with the rules f(zero) = one and f(n) = two tried in order, a normaliser that takes f(x) to two makes (x -> f(x))(zero) run to two where f(zero) runs to one.

**D-RUN-6.** A planner may share, move or drop a term whose row holds no effect, no open choice and no possible non-termination, and that consumes no use-once value. Running a term again at a second place is a move of the same kind, and is read the same way. A term whose result is of a use-once sort is neither shared nor run again. Wherever the term is moved or shared it keeps the bindings of its arguments, its activation, and the way each of its claims was admitted: by evidence, by a guard, or by an assumption by name. Evidence that justifies the move, or that lets a guard be left out, is read again at the new site (rule 4, D-CL-2) and must be yes there. An assumption by name that is not on the machine model stays an assumption by name, with its place in the lock: moving the term does not make it yes. A claim that is yes because a test passed is yes only for the same values, in a state the test still describes, at places the test comes before on every path. Outside those places the term needs other evidence that is yes there, or a guard of its own. Rule 10 holds throughout. Reuse of a result already obtained (D-RUN-3) is a separate matter. `[C4 as fixed in R24, with the second and third sentences from R29 section 4, in place of the last sentence of D L346 and the second limit at D L351 | approved]`
Case: an exact division under a test that its divisor is not zero. Inside the branch the claim on the divisor is yes, and the division's row holds no effect. By the first sentence alone the planner may hoist it above the test, where the divisor may be zero.

**D-RUN-7.** The state of the reference run, and its outcomes. `[C37; the outcomes as R29 3.3 gives them | approved, as forced move 19, for the state and for agreement value by value; shapes to be tested by building slice 1; that an outcome names what is held was approved earlier]`

```
state   = { control: a node with its environment, or a value; frames: what remains to be done;
            handlers: the handler frames in force; next activation: a count; fuel: what is left;
            consumed: a count for each use-once value }
outcome = returned(value) | failed(payload, held) | asked(request, continuation) | out of fuel(held)
          and for the compiled run also stopped(resource, held)
          -- held names the use-once values the run had and did not consume
```

**D-RUN-8.** A function value holds its body and its environment. A reply from the host is admitted as D-ADM-2 and D-ADM-3 admit any value, before the run resumes, and one request takes one reply. The reference run counts what it consumes of each use-once value. Under D-RUN-3 the state needs no table of results. At an operation with a continuation, the outcome of step is asked. The caller answers it with a selected interpretation of the effect's theory, or passes it to the host when the symbol is left in the row. `[C37; D L610 | approved, as forced move 19]` GAP 7: what a request is and the system-call model have no content yet.

**D-RUN-9.** Agreement. The compiled program agrees with the reference run on an input when three things hold. Its requests are the reference's, in order and with equal observed arguments. Its outcome is the reference's: the same failure with an equal payload, or a result related to the reference's as the tracking claim says, which at an observed sort is equal. And it consumes each use-once value as the reference does, value for value and activation for activation, except where a claim licenses a change (D-UO-6). The reference's own count does not show the third of the compiled side. It is shown by checked evidence that the lowering keeps use, or by a way of watching the compiled run that is itself checked. A match of requests and outcome without it is recorded as that and no more, with use not checked. Where the meaning leaves a choice open, the compiled run must be one of the reference's runs (D-TR-1). The compiled run may stop for a resource that the row names where the reference goes on, and not the reverse. A run cut short by fuel shows neither agreement nor disagreement. `[C37 | approved, as forced move 19; it gives no step-by-step interface and no proof for a lowering. Finite checks of agreement at a stop are run and reviewed: D-EVD row 15]`
Case: a value is finished once by the meaning. One lowering finishes it twice and one never, and neither tells the host. All three runs make the same requests and return the same result. The harness of slice 1 must refuse the two wrong ones, by controls that drop a value and that use one twice.

**D-RUN-10.** At a failure the compiled run holds the values the reference holds. Where the compiled run stops for a resource and the reference goes on, its requests are the first of the reference's, in order, and each value it consumed the reference consumes, and no more often. Such a run is recorded as stopped for a resource and never as agreement. `[R29 3.3 | approved, as forced move 31. The finite check behind it, D-EVD row 15, compares an ordered prefix of requests and final counts value by value; it is not a step-by-step trace of ownership]`

### The concurrency core

Whether the core is in this round was put to the owner (R35 section 5, choice 2). The owner's record leaves it to me where I am confident. I am confident of this much, and it is *Arch's call, by the owner's leave (recorded)*: D-CONC-2 to D-CONC-6, D-CONC-8 to D-CONC-11 and D-CONC-14 are in this round, as working rules. My reason is one of timing and not of proof: they change the use-once check, the signature and admission, which are trusted texts, and it is cheaper to specify those once than to change them after they are specified; Codex S's three tests that lean on them passed, and Codex Q recounted them. I am not confident that they are right in every context: the census of D-CONC-3 is not run. If it accepts a wrong term they fall, and D-TH-3, D-UO-5, D-ADM-2 and D-TR-12 stand as they are. I am not confident of D-CONC-7, D-CONC-13 or the protocols of D-CONC-10, and they stay open; R35's tests 1 and 3 would supply bounded checks of the first two, once the translation, the owner's completion and the guard are specified; they do not by themselves define or prove those contracts. Test 1 has since been run and reviewed on one encoding (D-EVD row 24). D-CONC-12 waits on the web round. The answer not taken: the core is left out, and the first version has no scheduler written in Loom with tasks held as functions. R35 is my report on card 0035; CR2 is Codex C (Core Reviewer)'s review of it, with fixes G1 to G5; ST is Codex S (Rule Tester)'s tests of the core, which Codex Q (Model Checker) recounted and confirmed for tests 1 to 3 at the same bounds. D-CONC-1, the placeholder of the first text, is retired.

**D-CONC-2.** Functions held in data. A constructor may take a bound parameter. A constructor calls nothing: it holds the function. The multiplicity declared there is what the holder owes. At one, the function held is a use-once function in whatever rule takes the datum apart. At any, it is an ordinary function there. A data sort with a constructor that holds a function at multiplicity one is declared use-once, and so is every data sort that holds a value of it. A declaration is refused otherwise. A use-once function may stand in five places and no others: where it is applied; at a bound parameter declared one; at a bound parameter of an operation whose rule is in the term and passes the check with that parameter read as use-once (D-TR-12); at a constructor's bound parameter of multiplicity one; and as the result of its scope. It is never held at a constructor's parameter of multiplicity any. A binder may also stand at a bound parameter of a constructor. `[R35 4.1, adding to D-TH-3, D-TH-7, D-UO-5 and D-ADM-2 | fold, to be tested; ST tests 1 to 3 ran with it assumed]`

**D-CONC-3.** A function is use-once when clause (c) makes it so, when it stands for a bound parameter of multiplicity one (D-UO-3), or when it is a continuation that holds use-once state (D-TR-12): in an environment, in a frame that waits with an argument already obtained, or in handler state. By clause (c), a function that holds a use-once function is use-once. Putting a function in a datum, taking it out and handing it on each move the one obligation. Only running the function discharges it, and then what it returns is owed in its own right. In D-TR-10, fields of data are among the places a store's state is held, and in D-TR-12 "runs it exactly once" reads: runs it exactly once, or hands it on once. `[R35 4.1 | fold, to be tested]` Still owed: the census of the whole language with functions in data, by context. `[CR2 L23]`

**D-CONC-4.** Tasks. The continuation of pick is declared one in Open: every resolver answers a pick once, as the host does. Exploring every answer is done by running again with other replies. `[R35 4.2; CR2 L25, L34 | fold]`

```
theory Tasks                                -- a library theory: declarations and definitions
  sort   Task       use-once   data  Task(Unit → Unit, held at one)
  sort   Wait_A     use-once   data  Wait_A(A → Unit, held at one)     -- one such sort for each sort A
  sort   Ready      use-once   data  None | More(Task, Ready)             waited on, written out
  effect spawn     : Task → Unit
  effect suspend_A : (Wait_A → Unit, called once) → A
  effect wake_A    : Wait_A, A → Unit       -- the continuation of each effect is declared one
  def    yield     = suspend_Unit(w -> wake_Unit(w, unit))
```

**D-CONC-5.** The scheduler is a handler of Tasks into Open, with a Ready as its state. Each rule hands the queue to exactly one successor: the computation it runs, or *next*. `[R35 4.2 | fold]`
- spawn(t), with continuation k: t and Task(k) join the queue; then *next*.
- suspend(f), with continuation k: f(Wait(k)) runs under the scheduler with the queue.
- wake(Wait(g), a), with continuation k: Task(u -> g(a)) joins the queue; k(unit) runs on.
- Whatever runs under the scheduler and returns, returns to *next* with the queue as it then stands. That is one rule for the first body, for a task's body, and for the function given to suspend.
- *next*: if the queue is None, the scheduler returns. Otherwise it asks pick for a place in the queue, takes that Task out, and runs its body under itself with the rest.
- A failure in a task: D-CONC-12.

**D-CONC-6.** What the scheduler's rules say. `[R35 4.2 | fold]`
- A task is its continuation up to the scheduler, and each is held at one. With yield declared one, all 68 schedulers that dropped or doubled an ordinary task are refused, and no right one is (ST; Q recounted the same 68).
- With pick unresolved, the term means its set of outcomes over every answer to the picks (D-OP-2). Each assignment of answers to the picks is one sequential run, replayed from its record. A resolver is a scheduling policy and answers each pick once. A machine's scheduler, later, is a tracker for pick (D-TR-1).
- Between two picks no other task takes a step. So what a task does between two picks is undivided as far as this scheduler's orders go. It says nothing of a machine, of a host's request, or of handlers outside. A task that suspends between a read and a write has made its update in two parts, and the lost update is among its outcomes. Without the lock the outcomes are 1 and 2; with it, 2 (ST; Q).
- Where every answer to the picks gives the same observations, pick leaves the row by indifference (D-ROW-12): the tasks do not race as far as anything observed can tell.
- Only tasks in the queue are offered to pick, and a task that waits is held by what it waits for. "Can run" means enabled in this library. It is no promise that a task finishes, that a host answers, or that a resolver is fair, and a wait outside the library is not registered.
- This higher-order core needs D-CONC-2. A scheduler over first-order command tags and explicit task state is a separate design with its own proof, and nothing here rules it out. `[CR2 G5, in place of R35's claim that without the rule there is no scheduler]`

**D-CONC-7.** Handlers by substitution: a candidate, not yet a rule. R35 proposes that a handler with state is applied by substitution, as D-IN-1 says, so that a continuation that crosses a handler is a function value like any other, the frames it has captured are environments of function values, and the handlers field of D-RUN-7 can go. It is worked by hand on one case and not run. `[R35 section 3 | open]` Codex C finds it an unclosed translation obligation: D-IN-1 alone neither forbids handler frames at run time nor fixes when handlers disappear. Owed before the field is removed or the cases of step are counted: what "at n" means and how a continuation is applied; the return case, with where the successor state goes; the completion wrapper for a task that performs no operation; an operation performed by a bound argument whose body is not in the term; a store outside the scheduler, which stays ambient and must supply its current state when a task resumes; rules that call themselves; nested handlers of one operation. `[CR2 G2, L40-L52]` Until then D-RUN-7 keeps its handlers field. The web round gives a candidate for the translation, for continuations declared to run once: a use-once datum that is either a return or a request holding its payload and the rest of the computation; a handler as an ordinary definition over that datum, with a rule for a return, a rule for its own request, and a rule that passes any other request outward. Two things it shows are owed and not chosen. A callback compiled apart must return that datum, so its calling convention changes. And a request made inside a handler's own clause goes to an enclosing handler in the candidate, which substitution alone does not decide. `[web round 3, topic 3; its source partly supported; its program not shown and not rerun | candidate; the two owed points are open]` S's test 4 judged its 600 configurations right, 120 right and 480 wrong, and did not establish that step is unchanged; Q agrees that the test establishes neither a new primitive nor an unchanged step. Since then Codex S has run the 600 configurations again with each handler read as a function that passes its state, on the generic evaluator with no case added, and Codex Q confirmed it for that evaluator and that encoding (D-EVD row 24). New source rules were supplied for it. General substitution, writes, stores that interact, a bound argument whose body is not in the term, recursion, failure, fairness and schedules without end are not tested. `[S card 0012, test 1; Q90]`

**D-CONC-8.** Shared state. An owner: a store's handler round the scheduler owns the state, D-TR-10 to D-TR-13 apply as they stand, and tasks hold references. A cell moves a value between holders. It does not lend. `[R35 4.3 | fold; the counter case ran in ST]`

```
sort Cell_S   use-once   data  Free(S) | Out(waiting : a queue of Wait_S)
take : Ref(Cell_S) → S               give : Ref(Cell_S), S → Unit
  take on Free(s)              the cell becomes Out(none), and the caller has s
  take on Out(ws)              the caller is suspended, and its Wait_S joins ws
  give(s') on Out(none)        the cell becomes Free(s')
  give(s') on Out(w, then ws)  the cell becomes Out(ws), and wake(w, s')
  give(s') on Free(s)          a failure, "cell full". Both values are held at it (D-UO-12)
def hold(c, f : S → S, called once) = give(c, f(take(c)))
```

**D-CONC-9.** What the cell gives. The value is with one holder at a time, and nobody gives what they do not hold. It does not give return: a task may take a value and finish it, or send it elsewhere, and the cell then stays Out. Whoever waits on it goes on waiting, and D-CONC-11 says where that shows. After f returns, hold attempts one give of its result, and that give may fail when the cell has been filled meanwhile, by f itself or by another task. hold does not promise that the value taken is the value given back: f may finish its input and return another value of S. A promise of return to this cell needs a condition or an authority that excludes intervening gives, which is further interface and evidence and is not given here. The invariant that makes take and give undivided: from reading the cell to writing it there is no pick; in a contended take the function given to suspend writes the cell before it returns to *next*. `[R35 4.3; the two sentences on hold from CR2 G1, in place of R35's "it holds on every run in which f returns" | fold]`
Case, from Codex C: the cell is Free(s) and the callback separately owns r. f(x) = give(c, x); r. take moves s to f; f gives s back and returns r; the final give(c, r) meets Free(s) and fails "cell full", with both values held. The callback returned normally.

**D-CONC-10.** Channels and protocols. An empty channel is Msgs of the empty queue. Two tasks may each call recv on one channel: one gets the message and the other waits; what the check refuses is the same use-once value at two places. A value sent is moved, by clause (b). `[R35 4.4 | fold; channels that carry ordinary messages ran in ST; a use-once payload is not run]`

```
sort Chan_A   use-once   data  Msgs(a queue of A) | Recvs(a queue of Wait_A)
send : Ref(Chan_A), A → Unit         recv : Ref(Chan_A) → A
```

For protocols there is a sketch only, in a report that is not an input of this card. Still owed before it can be checked: the sort of message kinds and the family of bodies; how a link binds its protocol; the equations for the dual; and the membership checks on the index. What the check and membership give is order: each end follows its protocol, and is closed at most once. It is closed exactly once only on a run that returns without handing it on. They do not give progress. `[R35 4.4 | open]`

**D-CONC-11.** Claims about a term that uses tasks. Three things are claimed apart, and none gives another. `[R35 4.5 | fold, to be tested]`
- Use. No run consumes a use-once value twice, and a run that returns has consumed each or handed it on (D-UO-11). The use-once check settles it, and settles nothing else.
- Outcomes. Every outcome of the term, over every answer to its picks, is in a stated set; and, where it is wanted, every member of the set is an outcome. An outcome is the whole of what the outermost scope returns or stops with, each owner's final state included. Running every answer settles the claim only where the picks form a finite tree, every pick is from a set with a covering fact, and no branch is left out, a failing one or one that stops included. Otherwise it is settled by Close where Close applies, or by a derivation. One run with its replies settles that run.
- Progress. Three claims, each read on the whole outcome: no outcome holds a waiting task; every run returns; and, under a named resolver, a task in the queue runs within a stated number of picks.

The scheduler's own return shows nothing: it returns when its queue is empty. A Task and a Wait cannot be dropped, so a wait that is left is in the final state of whatever owns it, and that state is part of what the owner's scope returns. In ST's test 3, two tasks that each receive first end, on every answer, with both waits in the store handed on and never as an ordinary result, and discard(Task(b)) = unit is refused (Q recounted all 14 tapes: the 2 of this program, and 12 of two controls that complete). The certificate for freedom from deadlock is a library theory, later.

**D-CONC-13.** Where a wait shows: a sketch that is not yet a rule. R35 has the scope of an owner that can hold a wait return a use-once Ended_A, which is Clear(A) or Waiting(A, the owner's final state), and has the plain value got by settle : Ended_A → A, with the condition that its argument is Clear (D-ADM-6). The possibility of a wait is then carried by the result's sort and by an ordinary guard's failure in the row, with no new kind of row entry. `[R35 4.5 | open; new and not run]` Codex C finds three things owed before it stands. Owner completion must be defined for every state: Clear must certify that every remaining obligation was finished or transferred into A or another continuing carrier, since an owner can end with Free(s) and no wait, and Clear(Unit) would then leave s out. The bridge from "no outcome holds a waiting task" to Clear at this call has to be shown; the first does not give the second. And the test must be named as D-ADM-6 asks: a pure, total probe that returns its whole Ended argument with the answer, with its claim, and with the whole carrier kept on failure. `[CR2 G3, L72-L78]`

**D-CONC-12.** A failure in a task. The scheduler answers it. Under D-UO-16: it takes from the failed task's continuation what the task held and may not be dropped. Where the theory names someone who looks after the task, the rule hands them the payload with what it took, ends the task and goes to *next*, and the others run on. Where there is nobody to hand to, or something held cannot be taken, the rule fails in its turn, and the queue and the task are held at the stop. Tasks as written names nobody, so until it does the last sentence is the whole rule: a yes to D-UO-16 does not by itself let the others go on. `[R35 4.2; the last clause from CR2 G4 | open: web round, with D-UO-16]` Under D-UO-16's second answer: the rule goes on only where the failed task held nothing, and otherwise fails in its turn. If the usage mark is split (D-UO-17), Task and Wait carry both marks.

**D-CONC-14.** What the core costs. `[R35 4.6; CR2 L82-L89 | fold]`

| Kind | What |
| --- | --- |
| Trusted programs that change | The use-once check: the five places, fields in the account, the rule on moving. The signature record and admission: a constructor may hold a function. The run record: requests and replies. With D-UO-16, the reference run gains take. With D-UO-17, the check reads two marks. Also the costs D-UO-12 already brings: liveness in order of evaluation, what a possible failure holds in the row, held values in outcomes, and a watch on the compiled run |
| Trusted programs that do not, on a condition | The evaluator. step, if D-CONC-7's translation is specified and holds. That is not shown |
| Declarations a build takes as true | Pick's continuation declared one. The sorts and multiplicities of Tasks, Cell and Chan. Ended and the condition on settle, if D-CONC-13 is taken |
| Library definitions, checked like any | The scheduler's rules, yield, take, give, hold, send, recv. That a given scheduler does what a client wants is the outcomes claim, and it is owed for each |
| Statements and evidence owed | The three kinds of claim of D-CONC-11, each with its scope and the whole configuration it reads. A soundness claim for any checker of them (D-RUNEV-2). The census of D-CONC-3. The translation of D-CONC-7 and its preservation of scope and activation. Agreement of use between source and compiled runs. An identity for each fresh run |

**D-CONC-15.** Looking twice at a held-out set: count it. Each run that looks leaves a record, a second run of the same job is another run, and a result carries the number of looks behind it. Giving each test set to one job is a promise about jobs only and does not stop that job looking twice. `[R35 section 2, F7, and section 5, choice 1 | Arch's call, by the owner's leave (recorded)]` I am confident of the direction: counting closes nothing, since a rule that forbids can be added over the same records later, and Codex C accepted the repair to the record. The answer not taken: forbid the second look by a gatekeeper that hands out one permission. Still owed: an identity for each fresh run, and checked links from a result to its looks (CR2 L29). PLACEHOLDER: the record of a look, the private evaluator and the scope statements K1, K2 and K5 are in my reports on cards 0026 and 0028, which are not inputs of this card. On K2, Codex S's test of a nested update (D-EVD row 16) found that the full clause of D-TR-15 already refuses the tracker R28 aimed at, under S's finite reading of that clause, so that case asks for no new sentence. Codex Q has since confirmed that result for S's chosen finite reading (D-EVD row 16). No general relation follows from it, and it does not by itself remove K2.

### The path that always runs

**D-PATH-1.** Every sort has a default representation: uniform, boxed, with every guard in place. `[D L355 | kept]` A program is admitted when each membership is yes, guarded or assumed by name; when every application it can reach has a way to run; and when its meaning row fits the bound. A way to run is a rule that matches, an evaluated definition, an implementation in the host, or a selected interpretation whose image has a way to run in its turn. For a symbol that has rules, the failure of a call that no rule matches is a way to run as well: it is a failure with a stated payload, observed as any failure is. A declared symbol with no rules, no evaluated definition, no implementation in the host and no selected interpretation is refused, and gains no way to run from that failure. Where the rules of a symbol are not shown to match every admitted call, the possible failure is an effect in the meaning row. The entry says that a call may fail, not that one does, and the bound says whether it is admitted. `[C27, in place of the second and third sentences of D L355 | approved, as forced move 12, for refusing an operation with no way to run; the failing call: owner (recorded)]` The owner's answer, by the record on the two slice 1 choices: a call that no rule covers is accepted and fails cleanly when run. The answer not taken: the program is refused at admission unless its rules are shown to cover every case.
Case: over a sort of two values, the one rule f(0) = 0 leaves f(1) with nothing to run.

**D-PATH-2.** In slice 1 the rules are shown to match every call only by a last rule whose patterns are all variables. From slice 2 the case split shows it. `[C27 | approved, as forced move 12]` Slice 1 also accepts rules that list each constructor of a data sort once at one argument, with variables below. `[R29 section 2, entry 3 | owner (recorded)]` The answer not taken: in slice 1 only a last rule of variables counts as covering.

**D-PATH-3.** The payload of the failure of a call that no rule matches is the symbol and its arguments at observed sorts. An argument of a use-once sort is not in the payload. It is held. `[R29 3.3 | owner (recorded)]` GAP 6 is narrower now: this payload is decided, and the wider boundary with the host that it belongs to is still open. The answer not taken: the payload is left to the specification of each symbol.

**D-PATH-4.** For an admitted program the plain path gives a plan under the default bound, and the machine-model conditions of that plan are settled as rule 10 requires. A missing proof about a representation makes code slower and never stuck. A missing membership or a missing way to run is a refusal, or a failure that the row names. No assumption supplies a way to run. `[C27 | approved, as forced move 12]`

### Selection and the lock

**D-LOCK-1.** A build writes a lock in two parts. A rebuild replays the lock and never searches. `[D L359, L364 | agreed]`

**D-LOCK-2.** The semantic part records resolvers with what they read, orders, every selection a client could observe, and every assumption that removes a guard. Changing it changes the program. A representation that rests on a claim settled never is such a selection. `[D L361 | agreed]` So is a representation whose tracker settles a choice that the meaning leaves open, unless that choice leaves the row by indifference. `[C14 | approved, as forced move 5]` So are a membership assumed by name (D-ADM-4) and a clause assumed within the bound (D-TR-5). `[C26; C28 | approved, as forced moves 11 and 13]`

**D-LOCK-3.** The operational part records the plan with its representations. Changing it changes nothing a client can see, apart from time, memory, and where the program runs out of a resource. `[D L362 | agreed]` It records for each licence the evidence its reading used, by hash, and each question that reading put to the store with the hash of the answer, including the answer that nothing was there. It records as well the site, the bound, and every input of the reading that did not come from the store: the definitions and defaults it used, and which text of the reader of evidence read it. A rebuild replays that reading. A reading at a later state of the store is a new reading, and it may be a conflict where the old one was yes. `[C32 | approved, as forced move 16]`

### Ahead of time and just in time

**D-JIT-1.** Both ways of building are in the design from the start. Ahead of time is the default: a build writes its bytes and its lock before any run (D-STG-1, D-LOCK-1). Just in time is optional and is chosen for a part of a program: stages 4 and 5 run for that part during a run. No record that slice 1 fixes, the lock, the run record or agreement, may assume that all of a program's code exists before the run. `[the owner's record on building ahead of time and during a run: both from the start, ahead of time preferred | approved; the rest of this passage, and D-JIT-2 to D-JIT-5, are mine | fold]`

**D-JIT-2.** What a part built just in time owes that a part built ahead of time does not. `[addendum 1 | fold]`
- A choice it makes in a run is settled once in a run or at load (D-CL-1), by the same reading of evidence at the site (D-RL-4). The reader of evidence and the store are then needed by the run, and their builds are in the artefact row.
- It chooses only within the operational part of the lock. Every selection in the semantic part is fixed by the build's lock before the run (D-LOCK-2), so the program is the same program however its parts are built.
- Each time it makes code, the bytes are decoded by the machine theory's own decoder and compared, the tracking claim is owed as for any code, and the check of D-STG-2 is made before the code is entered. Whatever makes memory runnable inside a run is a loader, trusted by name or checked (D-TB-2).
- Code made in a run has a life: it is kept while any entry into it can still be used. Who owns it and when it ends are not designed.
- Agreement is with the reference run, as D-RUN-9 says, for every run, whatever mix of code ran. That a run built one way and a run built the other agree with each other follows only from each agreeing with the reference. Where the meaning leaves a choice open, it is the semantic part of the lock that makes them the same.

**D-JIT-3.** The lock. The operational part may record, for a part of the program, that its plan is chosen in the run, by which planner and under which bound. The run record then holds what was chosen, and a replay takes its choices from the lock and that record and does not search. `[addendum 1 | fold]` Read strictly, D-LOCK-1's "never searches" was the one sentence of the first text that shut building just in time out; this passage is what keeps it open. The rest of that text was silent, and read as ahead of time only: D-STG-1's five stages in one pass, D-STG-2's check "at load", and D-SL-1's plain path.

**D-JIT-4.** Where it first appears. First, one fixed build during a run, in a slice before slice 5. `[the owner's record of the six answers, item 6 | decided; the record does not name the slice]` It is the web round's case: `f(x) = x + 1`, built at its first call with the one default representation. It chooses nothing, so it needs no planner, and it tests that no record assumes all of a program's code exists before the run. Its finish line: that part is emitted at its first call; its bytes are decoded and checked before they are entered; the run record names that build; that run agrees with the reference run; and the same program built wholly ahead of time agrees with the reference run too. My proposed slice is slice 2, so that slice 1 stays the smallest slice. The other answer is slice 1, which would test D-JIT-1's last sentence in the slice that fixes those records, at the cost of a loader in the run and a life for code made in a run (D-JIT-2) inside slice 1. `[web round 3, topic 6; Claude Arch | proposed; the slice is the owner's]` This replaces my reason for slice 5 alone: "I see nothing for a part built in a run to choose before there is a planner". Then a plan chosen in a run, in slice 5, which has the planner and code as a name for its term. Its finish line: one part of one program is planned and emitted during a run; its bytes are decoded and checked before they are entered; that run agrees with the reference run; the same program built wholly ahead of time agrees with the reference run too; and a replay makes the same choices without searching. Every other part builds ahead of time, under D-JIT-1's last sentence; D-WEB-6 (g) proposes how slice 1 tests that. `[addendum 1 | fold]`

**D-JIT-5.** Choosing a way of building for each part. Where a program falls into parts that are handled independently and each part takes at most one way of building, the allowed choices form a partition matroid, with the parts as its blocks. That is all the matroid of the old note amounts to: compilation itself is not one. Picking the cheapest way for each part separately is best only where exactly one way is taken for each part, the costs add, and no part's choice bears on another's. A cost paid once for having any part built just in time, or a cost at the boundary between two parts built differently, does not change which choices are allowed. It ties the costs together, so the cheapest way for each part taken alone need no longer be the cheapest whole: with three parts, the best independent choice costs 6; a fee of 8 for building anything in the run makes "all ahead of time" best at 13; a charge of 4 at each boundary makes "all in the run" best at 8. Some tied costs still have an exact method, a single shared fee among them; in general the choice is a search (D-ROW-11). `[web round 3, topic 6, clarifying and qualifying the sentence on picking the cheapest way for each part, which already asked that the costs add and be independent; its two sources supported by Codex O; the three figures checked by hand | proposed]` `[addendum 1; the recovery ledger, draft 15, L141, as history; Codex O's row O9 | fold]`

### The trusted base

**D-TB-1.** The only trusted machine code is one evaluator, built twice by independent means. It is the total first-order fragment of Loom itself. Everything else a kernel does is a program for it, so a checker is an ordinary program and the ordinary compiler compiles it. `[D L368 | agreed]`

**D-TB-2.** What is trusted, and why it cannot be removed. `[D L370-L380 | agreed; changed rows tagged]`

| Trusted | Why it cannot be removed |
| --- | --- |
| The evaluator, in two builds | Something has to run. Every run record names the build, and the two are compared |
| Interning inside the evaluator: equal values are one node, seen by same and by memo. A sequence is one node by its name and not by what it holds (D-SEQ-2) | It is how a program sees identity, so no separate loader is needed |
| Content hash as identity `[R30 4.3, approved]` | Where two hashes agree and both contents are in hand, the contents are compared, so a collision is a refusal and never a merge. Where only a hash is in hand, in a lock, a cache record or another store, it is trusted, by name, that the named hash function gave no collision among the items cited. No number is attached |
| Fuel on every run | Fuel is the step bound. The evaluator is total, and the programs it checks need not be. Running out is unknown and never no |
| The texts of seven programs, each from the slice where it enters. Slice 1: the row computer, the use-once check, the reference run, and the first part of the obligation generator, for sort membership. Slice 2: the case split, the reader of evidence at a site, and the obligation generator for laws. Slice 3: the obligation generator for tracking clauses. Slice 4: the derivation checker | They define what a row, a use, a run, a clause, a reading of evidence and a derivation are, whatever runs them. The reader of evidence applies rules 1 to 6, 9 and 10 `[C49, approved]`. The row computer's walk has a second result, the uses, which is counted here `[C39, approved]`. The closure checker is counted with the case split, in slice 2, or as an eighth text `[C30; the "or" is not settled. By the owner's record it is decided when the trusted texts are written; D-RUNEV-5 bears on it]` |
| The three rules by which a run becomes a claim: Eval, Close and Reflect | They say what a run is evidence of |
| The statements of the tracking claim | A clause is trusted to say what is meant, as any statement is |
| The declarations a build takes as true | Its theories, with their covering, use-once and multiplicity declarations, the machine model with the conditions it marks, and the system-call model |
| The reading of the text `[C38; R29 section 4, approved]` | Every claim is about a graph. A build records the bytes of its source, the reader and the elaborator each by hash, the version of the syntax, the graph by hash, and each question the elaborator put to the store with its answer. That the graph says what the text says is a claim. It is settled by a checked correspondence between the two. Or it is not owed, because the build declares that the graph itself is the program: the declaration binds that exact graph to the rendering of it that was inspected, and the rendering must be faithful. Showing the graph is neither of these. Otherwise the reader stands in the artefact row by name. In slice 1 the reader stands in the row, beside the lowering |
| The hardware, and the loader of binaries | Nothing runs without them |
| Each decider, checker or oracle still named in a row | With the assumptions it declares |

**D-TB-3.** A rendering shows a run that is bound once apart from code that stands at two places. Under D-RUN-3 those are two programs: the second consumes twice where the first consumes once. `[R29 section 4 | approved]` Which form the checked correspondence takes after slice 1 is open. `[C38 | open]`

**D-TB-4.** Not trusted: the elaborator, the planner, every proposer and solver, the passes, the assembler, the SRE, LoomLab, the optimizer, and agents. The two theorems of D-THM-1 and D-THM-3 are results with rows. Until they are proved, evidence for the one program serves: a derivation from slice 4 on, and before that the lowering is named in the row. `[D L382 | agreed]`

**D-TB-5.** Three routes for a fact established by a run. Replay defines evidence. The second route is the default for flat work, and the row names the route taken. The figures are the owner's, quoted as given. They were measured on generated proofs of two shapes, long lists of clauses and trees. `[D L386-L392 | agreed]`

| Route | Cost against a direct check | What the row gains |
| --- | --- | --- |
| Replay by the evaluator | The owner measured 14 to 33 times on long flat proofs and 2.5 to 4.3 times on tree-shaped ones, for a well-built checker | Nothing |
| A checker proved correct once, then compiled | About one | The compile chain and machine model, less what has tracking evidence |
| An unverified checker | About one | That checker, by name and hash |

**D-TB-6.** To be named in a row, an unverified checker comes with five things. Its definition as a program for the evaluator, which is what replay runs. The statement of its soundness claim. The claim that it accepts only what that definition accepts, unknown until proved. A recipe that rebuilds it to the same hash. And a corpus of damaged certificates, made by mutating valid ones, each labelled by replay under the definition as accepted, refused or unknown at the budget, and it must refuse every one labelled refused. A mutation can leave a certificate valid. Agreement on valid certificates shows nothing about a checker that accepts everything. The corpus result is a note. `[D L396; C29 | approved, as forced move 14]`

#### How a run becomes a claim

**D-RUNEV-1.** Three rules. Slices 1 to 3 use Eval and Close. Reflect arrives with the derivation checker in slice 4. `[D L580-L586 | agreed]`

| Rule | The claim | Its row |
| --- | --- | --- |
| Eval | f(v) = w, for this input | The build that ran |
| Close | A statement for every word over some generators, from one checked finite description that is closed under them | The build |
| Reflect | A checker for a theory's statements accepted a derivation | The build, and the laws the derivation used |

**D-RUNEV-2.** What a run shows. Eval settles a statement of the form f(v) = w and no other. A run of a checking program on a statement P settles that the program returned yes on P. P follows only with a second claim, the program's soundness: what it accepts is true, for statements of this form, in this theory and scope. Each of the trusted texts has one such claim, which is what D-TB-2 trusts that text for, and its name gives it no other. For any other checker the claim is proved, or it stays unknown and stands in the row as an assumption by name. `[C29 | approved, as forced move 14]`
Case: a checker that accepts everything, run on 0 = 1, gives a true run record and a false statement.

**D-RUNEV-3.** What Close covers. The description, the start cases and each step are checked against the generators that the conclusion names, as terms. A table fitted to answers is not the operation that gave them, and Close on a table concludes about the table. Each step is shown for every argument the generator admits, for every outcome it may have, failures among them, and for every value that a name stands for. Where a name stands for infinitely many values that is a statement about all of them, and trying one is not enough. The conclusion is for every finite word over generators of one hidden argument, and for every finite term over generators of several, with every tuple of arguments checked. It does not cover a run without end (D-TR-8) or a generator that takes a bound argument, and it does not say that an outcome exists where a generator is partial. `[C30 as fixed in R24 | fold]`
Case: the table 0 -> 0 is closed, the real operation takes 0 to 1, and Close on the table gives x = 0 after every word.

**D-RUNEV-4.** A run is evidence by Close only when the program that ran is the closure checker, which is one of the trusted texts and has its soundness claim. A run of any other program, by itself, settles only what that program returned. Anything further needs that program's soundness claim, with its scope and what it rests on. The description has finitely many states. Where the meaning has infinitely many, Close on a finite description concludes about the meaning only with evidence that each question asked gives the same answer through the description: laws of a declared theory, which then stand in the row, or a derivation, from slice 4. The claim names the scope of values it is for and the naming relation, and its start, its steps and its answers are each checked for that scope. What ties the infinitely many values to the finite description, the scope with it, stands in the row. `[C30 as fixed in R24 | fold]`
Cases: a program that returns true on every input, offered as the closure check. And braids with integer matrices, named by the matrix mod 2: the six names are closed under the generators, and that they answer parity rests on two laws, for the braids built from the empty braid by the two generators and not for every stored value. The split over all 16 matrices mod 2 fails six cases for each generator, so the relation is cut down to what is reached, with that cut checked, or the wider claim is refused.

**D-RUNEV-5.** Close has a program. A run counts as Close only if it is a run of one fixed program on a description. The description names a data sort with its covering fact, a finite relation between names and values, and for each constructor, operation and question the real symbol and its tracker. The program checks five things. The symbols are the sort's own constructors and the operations as stated, as nodes (D-RUNEV-3). The start clause holds. Every step holds for every tuple of related pairs, every admitted argument and every outcome, in the direction of the form (D-THM-4). Each question's tracker agrees with the real question at every related pair, as C2 has it. And every name the trackers can reach from the start has a value, with the use-once condition of D-THM-3 in the backward form. It concludes what D-RUNEV-3 allows and no more: the tracking clauses for every finite term over those generators, on the relation given. That the representation's own naming relation is the relation given is part of the description and is checked. `[R34 L9-2 | fold]` It is one more trusted text, or one more entry of the obligation generator for tracking clauses; the count in D-TB-2 goes up either way. Its test, T-B, has six cases it must refuse: a table fitted to answers where the real operation differs; a start clause applied only after removal; a tracker with an outcome the meaning lacks; one name for every natural number; a tracker that agrees with a made-up question and not the real one; and a table that is not the representation's own relation. Codex S wrote one fixed first-order program over a registry and ran it on eighteen descriptions: five accepted and thirteen refused, the six among them, each at its own stage. Codex Q recounted it with its own interpreter and agrees (D-EVD row 26). The registry, with its covering facts and where they come from, is a trusted input of that test, and its fuel is not the meter of D-EV-1. Arbitrary descriptions, covers without end, failures as outcomes and a second build are not done. `[R34 section 5, T-B; G2 F07; S card 0012, test 3; Q90]`

### What is proved, and the two theorems

**D-THM-0.** Nothing is proved in Loom, because Loom does not exist yet. What exists is a toy kernel of 480 lines with its scripts and their runs, the reviewers' scripts and their runs, and two theorems that are owed. What is trusted is D-TB-2, and nothing else. `[D L400, L438 | kept]`

**D-THM-1.** Representations compose. Let one representation name the values of S by names N1 over a signature, and a second name the values of N1 by names N2, in the same form, its signature holding every tracker the first uses, as the same nodes. Then "n2 names v when n2 names some n1 that names v" is a representation of S in that form over the first signature. Its assumptions and rows are joined, and its scope is where both hold. `[D L442 | agreed]` The theorem is stated for signatures whose operations take no bound argument. Beyond that a chain is kept as a chain, as it is for a forward link followed by a backward link, or the composite's own clauses are checked directly. `[C13; D L245 | approved, as forced move 4]`
Case: three models of two hidden sorts, with one, two and four functions from the first sort to the second, and an operation that asks whether a function is constant. Both links pass. The rebuilt composite relates the meaning's one function to one that is not constant.

**D-THM-2.** Four hypotheses are to be kept beyond the pure first-order case. The middle theory is shared exactly. Where an operation takes several steps, the relation holds at every point the other side can observe, and not only at completed calls. The inner representation adds no failure where the outer statement says there is none. Each link's measure for one-sided steps is well-founded, and the measures compose inner first. `[D L444-L449 | agreed, run by nobody]`

**D-THM-3.** A representation carries through a term that reaches its hidden sorts only through the signature. Forward: for related inputs, the term on names and the term on values are related at hidden results and equal at observed ones. Backward: every outcome of the term on names is an outcome of the term on values for some choice the meaning leaves open, provided each use-once value passes the check of D-UO-1. `[D L451 | agreed]` For first-order terms the theorem is an instance of Close in both forms: the relation is the finite description, and each pair of an operation and its tracker is a generator. The backward case is for finite stretches of a run (D-TR-8), with B0, B1 and use-once in what is checked. It is owed from bound arguments on. `[D L453; C18 | fold; C12's limit to finite stretches is approved, as forced move 3]`

**D-THM-4.** For finite systems both forms are inequalities between tables of true and false. With R the relation, C an operation on names and A the same operation on values, forward is transpose(R)·C ≤ A·transpose(R) and backward is C·R ≤ R·A. Each is kept when two operations are put in sequence, so each holds for every finite sequence. The greatest relation that passes is computed by removal, and the start clause takes part from the first step. For the backward form, begin with the pairs in which the name is not a start name or the value is a start value. Remove a pair of a name n' and a value w whenever some step on names from n to n' has no step on values to w, with the same observation, from a value still paired with n. Repeat until nothing is removed, and begin again after any further restriction. Then each name that must be reached needs at least one value. For the forward form, begin with every pair the scope allows. Remove a pair of a name n and a value v whenever some step on names from n to n' has no step on values from v, with the same observation, to a value still paired with n'. Repeat until nothing is removed, begin again after any further restriction, and then check the forward start clause on what remains. In both forms the steps are those of the real generators, at every argument and outcome (D-RUNEV-3), and a pair is of whole configurations (D-TR-9). The result is for the steps and the scope named. `[C18 | fold]`
Case for the direction of the forward form: one name, one value, a meaning that gives only 0 and a tracker that gives 0 or 1. A removal that matches the steps on values keeps the pair, and the tracker gives 1 where the meaning cannot.

**D-THM-5.** A third way for bound arguments, to be tested. Where every operation is total, gives one result and has no effect, every value may be copied and dropped, results and the values a function holds among them, and no sort has an index, a representation may supply its relation at every function sort it needs. Its certificate shows that application keeps the relations, that the combinators I, K and S, in which every binder can be written, are related to themselves at each sort used, and that each exported operation is related to its tracker. The combinators are the standard ones: their usual equations hold, the admitted binders are in fact translated by them, and the certificate covers every sort at which that translation uses them. Any other primitive the code may use has its own entry. K drops an argument and S uses one twice, which is why every value must allow both. Functions are equal when they agree at every argument. Two such certificates compose, relation by relation, through the same middle operations. Without the combinators the certificate can be empty: an empty relation at a function sort passes a check of application alone. This way gives nothing for a function that has an effect, holds state, or takes, returns or holds a use-once value. `[C13 | working]`

#### How a law is yes before slice 4

**D-LAW-1.** A law at an interpretation is yes by one of three runs. Its statement is the same node as a declared law of the target theory, which then stands in the row like any law used. Or exhaustion with a covering fact. Or a decider named in the row with the laws it assumes. It is no by a counterexample, and otherwise unknown. `[D L491 | agreed, not run in this form]`

**D-LAW-2.** Yes by computation, when both sides of a law rewrite to one node with their variables left in, is the third run. The decider named in the row is the normaliser, assuming nothing but the rules, under the limit on rule order of D-RUN-5 and the reading of rules in D-TH-5. No fourth run is needed. `[C9, closing the question left open at D L493 | owner (recorded)]` The answer not taken: it stays open until slice 2 counts how many of its laws are yes by the three runs of D-LAW-1 without it.

**D-LAW-3.** A claim settled on an enumerated set reaches every case before slice 4 in two ways only. By Close on the real generators, where the description is finite. Or by a decider named in the row with the laws it assumes, where the claim is that a projection onto a finite sort commutes with each generator and the decider settles it. That a declared law is used by a rewriting program is a use of that program, with its soundness claim, and not a yes by identity of nodes. A claim whose proof needs an invariant with a quantifier of its own waits for slice 4. `[R34 L9-7 | fold]` So the SRE's reports on infinite objects in slice 3 are mostly candidates. Codex S ran the loop of abducing and then generalising on one family of polynomials, and Codex Q confirmed its counts (D-EVD row 27): the invariant with a parameter is among the schemas kept, with many others, in a language of hypotheses that already contained it. The general lift is NOT DONE: there is no covering fact, no admitted hypothesis with a quantifier, and no checked derivation. `[S card 0012, test 4; Q90]`

#### Open, each with the test that settles it

**D-OPEN-1.** `[D L457-L475 | open; rows changed by an item are tagged]`

| Open question | The test |
| --- | --- |
| The use-once check on the whole language | D-UO-15 |
| Representations compose | Prove it first for finite systems with one hidden sort and one form. Search: a random realiser of a random realiser, the composite checked against the first meaning |
| A representation carries through a term | The first-order case is Close. Search for the rest: random terms over small representations, aimed at a name used twice, two hidden arguments, a branch then a hidden step, and a shared node |
| Higher-order terms, local state, non-termination and effects in that theorem | The same search with those term shapes. The clauses of D-TR-15, D-TR-17 and D-TR-18 are tried there for the first time: a handler that resumes twice, one that never resumes, a realiser that runs out, a loop, and a run that does not end |
| A licence for mixed forms `[C11, in place of the row on an operation between sorts of two forms]` | Not designed. The clause once proposed is refuted (D-TR-3) |
| Whether an interpretation and a record are one thing | D-TM-4 |
| Whether tracking evidence is affordable for real data structures | Write one mutable hash map as a holding of a finite map, in a fixed two weeks. Count lines of evidence for each line of tracker. Above about ten to one, with no route to automation, holdings ship as named row entries |
| The foundation: three positions | D-FND-3 |
| The evaluator: which form of bounded recursion, and its cost; its edge results are recorded in D-VAL-6 | Write the trusted texts for it in both forms and measure them against direct builds. The owner's figures in D-TB-5 are the reference |
| Rule 9 | In slice 4, remove one guard by a theorem that uses a classical law, and state what that use assumes as a derivation. The cases of D-RL-11 |
| Search by proposers, at the size of a planner or of the SRE | Ten small numeric kernels: planning time, guards left, and run time against the plain path. For the SRE, a search for a coarsest representation on the five-vertex graphs |
| Where the SRE enters | The owner's choice (D-SL-8) |
| The payoff of keeping the three positions apart | Three measurements. For a term as stated, no choice of representation, of plan or of guard to drop alters the meaning row `[C50]`. The best plan the planner finds within a stated budget, with three representations to choose from, beats the best it finds with one by a geometric mean of at least 1.2, and the record says where a plan was found by exhaustion `[C42]`. Checking costs under ten times, and annotations under twice, those of a conventional typed language |
| Identity across versions of a theory | Change one declaration of a theory in slice 2 and count the claims that must be settled again |
| Distortion; laws of programs that draw; guarantees from a sample | D-PR-6 |
| Surface syntax | Port 2,000 lines of ordinary higher-order code and count annotations |
| The form of the checked correspondence between text and graph | D-TB-3 |

The question "where a tracker must be defined" (D L464) is closed by D-TR-6, by the owner's record on the first text's choice 8.

### The first slices

**D-SL-0.** Five slices, each from source text to machine code. Each ends with three checks: the compiled program and the reference run agree on generated inputs, the artefact's row is printed, and the two builds of the evaluator agree. In slices 1 to 3 every claim is settled by a run. `[D L479 | agreed]`

**D-SL-1.** The evaluator and the store. The evaluator of D-EV-1, twice. The records of D-REC-1: terms, theories and rules with content identity. Four kernel programs: the row computer, the use-once check, the reference run with the record of its state, and the first part of the obligation generator, which emits a membership claim for each application. The use-once check may be the narrower rule of D-UO-14. A plain path to machine code through a checked low-level form, ahead of time by default, with the uniform boxed representation and counted references. `[D L481 | agreed; the wording of the path by the owner's record that keeps the backend neutral]` A small machine theory for its target, with its decoder, enough for the plain path; data declarations; and the host's operations reached through Ask under one fixed bound. `[C43 | fold]` Done when both builds agree on generated runs, the compiled programs agree with the reference run, the use-once check agrees with the reference run's count of what each generated term consumes `[C5]`, and the root row lists the backend, the lowering and the reader of text `[C38]` by name because nothing has evidence yet. Slice 1 needs no foundation, no derivation, no representation but the default, and no planner. `[D L543 | agreed; G F18]`

**D-SL-2.** Claims and interpretations. The case split, the reader of evidence at a site, and the obligation generator for laws at an interpretation. The use-once check in full, clauses (a) to (d) `[C5]`. A status for each law at each interpretation, a search for counterexamples, scope and covering, assumptions and reading at the site, data and folds, effects with handlers, bounds on rows, selection, and the semantic part of the lock. A first proposer of one rewrite, splitting a fold, each step licensed by a law read at its site. Done when a fold over the integers is split, the same fold over floating point is left alone, and the refusal names the law that failed and lists what would lift it. In this slice that list is the unknown laws on the refused licence. The full query arrives in slice 5. `[D L482 | agreed]` And, proposed: the fixed build during a run of D-JIT-4, with its finish line, if the owner names this slice for it. `[the owner's record of the six answers, item 6: a slice before slice 5 | decided; this slice proposed by Claude Arch]`

**D-SL-3.** Representations in the forward form. The first machine theory that holdings are made into `[C43]`, for words and memory, with the first holding. The obligation generator for the clauses of the tracking claim. Relation, signature, trackers and clauses F1 to F3. Total holdings into sums, such as a machine word or a big integer. Guards settled at evaluation. Ranges as a lax representation with resolution. The artefact row as a polynomial, and the operational part of the lock. The harness for the three measurements. Done when a sum over words runs with one guard per element, and with none where ranges are known, and when a representation exact only for what one client reaches is accepted for that client and refused for another. `[D L483 | agreed]`

**D-SL-4.** Evidence. The foundation tests come first, and the logic that derivations are then built in is the position that survives. The derivation checker, which enters the trusted base here. Derivation objects, solver certificates with checkers that owe the five things of D-TB-6, the three routes recorded, and the backward form with B0 to B3 on a late choice. Done when one guard is removed by a theorem, one run record is replayed by both builds, and the cost of replay is measured. `[D L484 | agreed; the five things from C29 | approved, as forced move 14; the wording on the foundation tests from C48 | fold]`

**D-SL-5.** The planner and a second target. The polynomial read in costs. The four proposer queries in full. A second machine theory. Code as a name for its term. A first library of representations that are not layouts, such as graphs under two spectral names. Done when no trusted program changed between slices 4 and 5, and when a proof arrives and a plan changes with no edit to the source. `[D L485 | agreed]` And when one algorithm is substituted under a theorem of a theory at one interpretation, and refused at a second where a law of the theory is no. `[R36 door 1 | approved]` Codex S ran this in small, and Codex Q confirmed it (D-EVD row 25): on every simple graph of up to five vertices the three laws hold of forests and the algorithm is licensed, and for matchings it is licensed at the 173 graphs where the laws do hold and refused at the other 927. That is finite evidence for those graphs. It is not this finish line, which is in the language and needs the theorem. And when the finish line of D-JIT-4 for a plan chosen in a run is met, if that passage is taken. `[addendum 1 | fold]`

**D-SL-6.** After these come the real numbers with enclosures, parallel schedules licensed by exchange laws, hosted foundations, file formats and their migration, the compiler written in Loom, and a rehearsal of changing the foundation. `[D L487 | kept]`

**D-SL-8.** Open, for the owner: where the SRE enters. An earlier version put the SRE and LoomLab after slice 5. On finite objects the SRE needs only runs, covering facts and forward representations, which slice 3 has, and the reviewers' earlier order made it the next slice after that. `[D L497 | open; names by the owner's record]` Substitution by a law is in slice 2 and the planner in slice 5 whichever is chosen, so nothing is blocked. `[R36 section 4, door 1]`

### The SRE, LoomLab and the optimizer

The anchors of this part keep the letters ENG from the first text. They name the SRE.

**D-OPT-1.** Names. SRE stands for Structural Representation Explorer. The SRE is shared infrastructure for two clients: LoomLab, a metaprogram that is not part of the compiler, and the compiler's optional optimization paths, here called the optimizer until the owner names them. The optimizer is never called an engine. The part that builds and checks representations, which the design's section 9 called by an older word, is the SRE, and what that section called the lab is LoomLab. The plain path always runs without the optimizer. `[the owner's records on names, and on the SRE's long name | approved]`

**D-ENG-1.** The SRE builds, checks and combines representations of objects. LoomLab uses the SRE to find questions, laws and theories. Both are libraries and proposers over the store. Neither is trusted, and whatever either establishes is a claim that a kernel program checked. Nothing in the rest of the design is specific to them, and the compiler is the first client of every construct they use. `[D L501 | agreed; names by the owner's record]`

**D-ENG-2.** What the SRE submits, and who decides. `[D L505-L512 | kept; "keep it as a proposal" from C28 | approved, as forced move 13]`

| The SRE submits | Who decides | Against what | What the planner may then do |
| --- | --- | --- | --- |
| A representation: target, relation, signature, trackers | The kernel, by sort preservation | The declarations of both theories | Keep it as a proposal |
| That this name names this object | The kernel by computation, or a verified checker run compiled | The relation's definition at this object | Use the name for the questions in the signature |
| That the name answers this question, which is a tracking law | The kernel, on a derivation for the sort or on an enumeration with a covering fact | The question's definition in the object's theory | Replace the question by its tracker inside the scope |
| That the name does not answer it: values with one name and no common answer | The kernel, by computing (D-RL-6) | The same definition | Never use that name for that question |
| A width or a distortion for this object | The kernel, or a checker in exact arithmetic | The definition of the measure | Use the answer at that width |
| An estimate | Nobody | Nothing | Nothing. It guides search only |

**D-ENG-3.** What goes in. Any object: a closed term, an interpretation of any theory, or a black box with a set of questions. An open registry of families; each family is a target theory with a proposer of representations into it. A census for each theory, with a record of how it was drawn. A budget. `[D L516-L519 | agreed]`

**D-ENG-4.** A black box is a theory of declared questions with no rules, asked through an effect. Each answer is a run record whose row names the endpoint. From answers alone the SRE has claims about the inputs asked. Unless the census is every input of a sort that has a covering fact, it has no yes about every input: a second box agrees on the census and differs elsewhere. A yes about every input is a claim about a definition. One recorded answer can still refute a statement about every answer, as D-ENG-10 says. A commitment made before the census fixes which definition is meant, and no more. The claim reaches the box only through a further claim: that this endpoint, at this version and in this state, answers as the definition does. That claim is checked, or trusted by name, or assumed by name. A claim in probability about inputs that were not asked states how the inputs are drawn. `[C31 | working; its limit on a yes for every input is approved, as forced move 15; that a refutation is not so limited is G2 F01]`
Case: an endpoint commits to the program that always answers 0. It answers 0 to the first question and 1 to the second. The commitment still opens correctly.

**D-ENG-10.** With no claim that ties the endpoint to a definition, the SRE has four things and no more. A yes for each input asked, as a run record. A no, for the whole sort, to any statement about every answer that one recorded answer refutes (rule 1). That a given name cannot answer a given question, from two recorded inputs under that name with no common right answer. And a lower bound on names: k recorded inputs whose answers to the same experiments disagree in pairs need k names. The last two, and any answer given from the record in place of asking again, lean on the endpoint answering the same input the same way. That is a claim about the endpoint, and where it is assumed it is an assumption by name in the row and in the semantic part of the lock. Everything else is a candidate. `[R34 L9-5, adding to D-ENG-4 | fold]`

**D-ENG-5.** What comes out. For each representation, a sheet with one line for each question. A line says whether the answer is exact, within a width, one-sided or not given. It carries the claim and its cost, and it says so when the line tells the reader nothing. Refutations: a refutation is a set of values with one name and no common answer, kept with the class of realisers that it rules out. The coarsest representation that still answers a given set of questions, found by refinement and checked clause by clause. `[D L523-L525 | agreed]`

**D-ENG-6.** Where each question has one right answer and each operation gives one result, the coarsest representation for a set of questions and operations has as its names the classes of values that no run of the operations followed by a question tells apart. Where a question has several right answers there may be several coarsest representations, none coarser than another, and those classes are finer than any of them. There, say which answers are right and what the tracking clauses require before calling a representation coarsest. A coarsest representation says what suffices and nothing of cost: building a name can cost more than asking the object as it was given. A choice among representations needs a workload: how the object arrives, and how many questions and updates follow. `[C42 | fold]`
Cases: values a, b and c whose right answers are {0}, {0, 1} and {1}; a and b may share a name that answers 0, b and c one that answers 1, and all three may not share one. And 3 by 3 tables of bits, named by their six parities: one question costs 3 reads on the table and 10 by way of the name, and six cost 18 and 15.

**D-ENG-9.** Names need not be classes. Where a question has several right answers, one value may stand under two names, and a family of overlapping sets, each with a common right answer and each carried by every operation into some set of the family, is a representation. It can have fewer names than any such partition. Among those families there is a greatest, for operations of one hidden argument: the sets that keep a common right answer under every question after every sequence of operations. The greatest is not the one with fewest names, and finding the fewest is a search. With an operation of two hidden arguments a greatest family is not shown to exist. Under such a representation the answer for one value can depend on the path that reached it. That is sound only where the meaning leaves the choice of right answer open at each asking, and it is a tracker settling an open choice, so it stands in the semantic part of the lock (D-LOCK-2). `[R34 L9-1, adding to D-ENG-6; the last two sentences are R34's own condition | fold]`
Case: values a, b, c; g sends a to b, b to c, c to c; r sends a to a, b to a, c to b. The sets {a, b} and {b, c} are closed and each has a common answer. No partition into two parts is closed with a common answer in each part. So two names against three.

**D-ENG-11.** What a line of a sheet says, exact, within a width, one-sided, refuted or nothing, is a reading of its claims at one state of the store, and it is not stored apart from them. `[R34 L9-8, adding to D-ENG-5 | fold]`

**D-ENG-7.** LoomLab's loop. Exploration proposes laws and theories, through the candidate-theories query, as D-STO-7 ranks it when that passage's test condition is met. Until the owner's record of the six answers, D-STO-7 bounded it. The query for which unknown claims would give a goal proposes what to settle. Worth ranks both. LoomLab's first duty is finding questions: what the representations distinguish on a census. `[D L531-L535 | agreed]` A held-out set is reached only through the operations of a named protocol, and a claim about inputs outside it cites that protocol's theorem. Where no theorem covers the path taken, LoomLab reports what was observed and no more. `[R30 4.4, edit 1, in place of D L535's sentence on a test set | owner (recorded): the rule is taken; its mechanism is still to test. This is apart from my call on counting looks, D-CONC-15]` To be tested as its mechanism: the set is a use-once value of a hidden sort whose signature is the protocol's operations. The use-once check then holds every client to the protocol, and a protocol that allows a second look hands back a new value to look with. `[R30 4.4; G F08 | to test]`

**D-ENG-8.** One record crosses to the compiler or to a person. It holds a subject, a change, assumptions, what is preserved, evidence, and an estimated benefit, which is a note. `[D L535 | agreed]`

**D-ENG-12.** Finding a representation by a table of experiments. A name is the tuple of answers to experiments, each a question after a sequence of operations; a failed closure check adds an experiment; the naming relation is the conjunction of the experiments. It is a proposer, so its faults waste budget and cannot make a false yes. On an object that can only be asked it ends in candidates, since nothing plays the part of the lift. `[R34 L9-10 | working]` Its test, T-A, for Codex Q (Model Checker), proposed and not run: every system of at most four values, with one or two operations of one hidden argument and one question whose right answers are a set for each value. For each, the fewest names over closed partitions, the fewest over closed covers, and the greatest closed family of D-ENG-9. Then the same with one operation of two hidden arguments. And for each cover found, its runs on names compared with the meaning's sets of outcomes. Representations found by hand are the controls. `[R34 section 5, T-A; G2 F07]` Nothing else falls with it.

**D-ENG-13.** Candidate theories by exploring a three-valued table. A smallest generating set of the implications that hold is a compact form of the kept set of D-STO-7, and a candidate algorithm for it, not a rival. With unknown entries there are two tables, so "the" generating set needs care. `[R34 L9-11 | working]` Its test is a third count in the 56-candidate test of D-STO-7: the 56 as found, a smallest generating set, and the kept sets with conclusions taken from the unknown-claims query. A sixth addition to D-STO-7 is proposed in the same report and not folded: that the examples given to induction include the residual goals of failed lifts, with hypotheses indexed by a count. Its test is T-C of that report, which Codex S has run and Codex Q confirmed on one family (D-EVD row 27): the schema with a parameter is kept, among 25 of 45 in the smaller language and 125 of 882 in the wider, and the language already contained it. That is a schema kept in a declared language. It is not the finding of that language, nor of one answer.

**D-ENG-14.** Three routes from a definition to an endpoint: checked, trusted and assumed. The first step replays the definition against every recorded answer, and that step alone refuses the case of D-ENG-4. The checked route settles a transcript; a box with state needs a further claim; a verified container image is trust. `[R34 L9-12 | working]` Its test: the three records on D-ENG-4's case and on one box with state, to see what each route can and cannot refuse.

#### The optimizer

**D-OPT-2.** The optimizer may change the algorithm. Another algorithm for an operation is a representation in which nothing is renamed (D-REP-4, last row): its tracker is another program for the operation, and its tracking claim says the two agree on the scope. It is also a rewrite by a law with a condition; the design draws no line between an algorithm and a representation. A structure is a theory. That a problem has the structure is an interpretation, each of whose laws is a claim there (D-IN-2). That the structure has a fast algorithm is a theorem of the theory, and it reaches the problem as D-IN-2's last sentence says. The licence is that evidence read at the site (D-RL-4). The SRE proposes the interpretation; the kernel checks each claim; nothing the SRE says is evidence. A claim about every member of a family, such as every graph, states its domain and how it is settled: by a derivation that is checked, or by a covering fact. A finite census is neither, and an argument on paper is neither (D-EVD row 25). `[R36 sections 3.1 and 3.2; the owner's record that the design says this now | approved for the row, the sentence, the finish line and the repair; this paragraph is my joining of them]`

**D-OPT-3.** Where the condition of a substituted algorithm is settled. Proved for a family, by a derivation. Checked for one object at build or at load, by exhaustion with a covering fact or by a decider named in the row. By a guard before the call, each time, with the cover D-TR-6 asks. Or by a check of the answer after the tracker and before any use of its result, each time. Two limits. The condition must be the tracker's own, which the plan covers with a branch; written as a membership of the argument in a narrower sort, a failed test would be a failure (D-RL-8). And the check after the fact is sound only for a tracker whose row holds no effect. That is needed and is not enough. The attempt and the check must each end, or run under a checked mechanism that gives control back when its bound is spent, or the fallback is never reached. The fallback must still have its arguments, and every obligation the attempt or the check created must be accounted for. A rejected answer and a spent bound both go to a fallback that covers them. For now an attempt that consumes a use-once value is excluded; that is a restriction chosen to be safe, not a finding that no wider safe form exists. The rule is about the whole of attempt, check and fallback, not about the attempt alone. `[web round 3, topic 1, its two cases checked by hand; the check's own ending and the obligations from Codex Q's review of revision 3, part 2 | proposed]` An algorithm whose answer is within a factor of the best is a lax tracker (D-TR-14), and may replace the exact operation only where the meaning asked for an answer to that width. A problem with several best answers leaves a choice open, and an algorithm settles it: that is a selection in the semantic part of the lock, unless the choice leaves the row by indifference (D-LOCK-2). `[R36 sections 3.3 to 3.5 | fold]`

**D-OPT-4.** What licenses a greedy method. A theorem for the structure and the objective in hand, with its conditions checked, and never a label, a fingerprint, a confidence, or the fact that local swaps usually work. For a finite, nonempty family of allowed sets in which every part of an allowed set is allowed, the greedy method that takes items in order of falling weight gives an allowed set of greatest total weight, for every nonnegative additive weight, exactly when the family has the exchange property. Such a family is a matroid. Over its bases, taking items in order of rising weight gives a base of least total weight, and in order of falling weight one of greatest, for arbitrary real additive weights. The general axioms of a greedoid do not give such a result, though some greedoids that are not matroids have a theorem of their own for every linear objective. Choosing from an e-graph is a different problem: with every occurrence of a shared part paid for and costs additive, the cheapest choice is found exactly in one pass from the leaves up where the dependencies have no cycle; where they have one, it needs repeated relaxation to a fixed point, a finite term to extract, and costs that give a well-founded optimum. With a shared part paid for once it is NP-hard in general, which rules out a polynomial-time exact algorithm for all general, finitely encoded instances unless P is NP, and does not rule out exact methods on special families. An e-graph is a proposer's working memory and is not where correctness lives. `[R36 section 2.3, with the wordings of Codex O (Citations)'s check, rows O1, O3, O4, O6, O7 and O8; the objective and direction, and the two cases of extraction, from G2 F02 and F03 | fold]`

**D-OPT-5.** Three things stay as they are. A problem stated with nothing to run is refused, on purpose (D-PATH-1, D-PATH-4): every problem comes with a definition that runs, however slowly, and that definition is the reference the fast version is tested against. A problem with several best answers should be stated with pick over the best answers, and not by an order of search, or an algorithm that returns another best answer is wrong. And recognising a search that a user wrote by hand is open: someone must propose that the term equals a library operation, and that is settled by a derivation or by exhaustion on a small sort. `[R36 section 4, doors 7, 8 and 10 | kept; no decision asked]`

### The evaluator

**D-EV-1.** `[D L548-L565 | agreed; lines changed by C8 and C41 marked | fold; C41's charge before building is approved, as forced move 23; the kinds of value, the choices and the sets are a proposal the owner asked for (D-VAL-1); sequences that change and stay the same sequence, the strict starting read, charges that count from the last access, and the recorded edge results are the owner's by the records named in D-VAL-6 and D-SEQ-1 to D-SEQ-4; the exact construction of a sequence's name, the test for a state-free definition and the numbers of the meter remain Claude Arch's proposals under review; fixed length and sets that hold sequences are Codex A's decisions under the owner's delegation]` The charge for a loop turn is left to the evaluator's specification. GAP 3: the hash function has no name; the meter's entries for the natural and byte primitives and the size of its unit are not written; the entries for the other primitives are a proposal under review (D-SEQ-4). Also open: whether `slice` takes a start and an end, or a start and a length. No owner record and no rule decides it; EV-A2 proposes a start and a length, and the choice is the owner's. `[EV-A2, gap 1 | open]`

```
value    v ::= n | bytes | row(v, .., v) | name.j(v) | set{v, ..} | sequence
               -- all but a sequence are interned: equal values are one node. A sequence is one node by its name
choice   name has k cases                               -- order, truth and option are declared in every program
def      f(x1, .., xk) = e                              -- first-order
e      ::= x | v | prim(e, ..) | f(e, ..) | let x = e; e
         | row(e, .., e) | name.j(e)                                                      -- C8; D-VAL-1
         | case e of name.j(x) => e; .. else => e       -- else may be left out when every case has a branch (D-VAL-3)
         | for x < e1 from y = e2 do e3                 -- e1 and e2 run once, before the loop; e3 may use x
                                                           and y and gives the next y; the value is the last y
prim     naturals: add, sub, mul, divmod, compare, shift, bit operations
         bytes: get, slice, concat, hash       rows: get, length
         sets: empty, insert, remove, member, size, members
         sequences: make(n, e), length, contents, a write at a position       same(e, e)
         compare gives a case of order; same and member give a case of truth; divmod gives the row
         (quotient, remainder)                                                            -- C8; D-VAL-2
edges    no primitive fails. sub stops at zero; divmod by zero gives (0, a); a read, a slice or a write
         outside the range gives none; a primitive given a value of the wrong kind gives none -- D-VAL-6
hash     one named function, the same in both builds
total    a definition is total by its syntax when it has at most one loop and calls only total
         definitions that come before it. A definition may call itself. It is then not total, and
         runs only with fuel                                                              -- C8
checker  any definition, run as eval(fuel, f, v); running out of fuel is unknown, never no
meter    a primitive charges by the bit length of its arguments, a call charges one, and a loop
         turn charges one                                                                 -- D; C8
         before it builds anything, a primitive works out an upper bound on the size of its result
         and of whatever it needs meanwhile, in a way that cannot itself overflow, and charges for
         that. A run that cannot pay, or whose bound cannot be worked out, stops as out of fuel with
         nothing built. The work a primitive does is charged apart, by its line in the meter's
         table. That table, one line for each primitive, is part of the evaluator's specification,
         and both builds charge by it                                                     -- C41
memo     a mark on a state-free f (D-SEQ-3): calls are cached by the identity of the argument; a hit charges one. The cache
         has run lifetime, so both builds spend fuel alike; returning to a kept point restores its saved entries (D-BC-2)   -- G 0173
```
The evaluator holds finite sequences and not arrays: a sequence is mathematics, and an array is a representation of one, which belongs to representation. `[the owner's record on sequences | approved]` Bytes stay as they are; the record does not decide them. A write changes the sequence it is given, for every holder, and gives no new sequence (D-SEQ-1). `[the owner's record that sequences change and stay | decided]` Equal values are one node, as the first line of the block says, so two byte values of equal content are one node; how a value written outside the evaluator is mapped to one is a separate question. `[Codex G's review of the evaluator's rules, F01 and F07]`
Case for the meter: a shift of 1 by 2^64 has small arguments and a result of 2^64 + 1 bits.

**D-EV-2.** Fuel is the step bound of D-CL-1. Every run record holds the program, the input, the output, the fuel and the build. All values except sequences are interned by content, and a sequence is one node by its name (D-SEQ-2); same and memo are how a program sees identity. The counted loop is the default. The alternative: a definition may call itself on what one case or row argument holds, or on a smaller natural. Open, with its test in D-OPEN-1. No primitive gives the size of everything a case or a row holds below its top, so with the counted loop a total definition can walk a term only when it is handed a bound, or is handed the term as a row of its nodes in order, since a row has a length. Otherwise the kernel's graph walks are checkers run with fuel. A record of a run that uses sequences holds more than this sentence says: D-SEQ-3. `[D L567-L570 | agreed; the alternative and the last sentence the author's]`

### Values, choices and sets

**D-VAL-1.** The evaluator has six kinds of value: a natural, bytes, a row, a case, a set and a sequence. A row is several values in fixed positions; it never changes, and it is read by position. A case is one value marked as case j of a declared choice; it is the coproduct, as a row is the product. A set is a finite collection of values without repeats. A sequence is D-SEQ-1. There are no tagged values: what `tag(v, .., v)` did is done by a case that holds a row. `[the owner's record of the conversation on sets and a coproduct: a lean and a request for this proposal, not an adoption | proposed; Codex D is drafting rules from it]`

**D-VAL-2.** Choices. A program declares its choices, `name has k cases`, with k from zero up. A choice's identity is its name and k together. Every program has three it did not write: `order` with 3 cases (less 0, equal 1, greater 2), `truth` with 2 (no 0, yes 1) and `option` with 2 (none 0, some 1). A program's own declarations have different names from each other and from these three, so `name.j(e)` means one choice. `[the owner left how choices are referred to with Claude Arch | decided by Claude Arch: one name, one choice in a program]` A case holds exactly one value, and a case with nothing to hold holds the empty row. A declaration does not limit what a case holds, since the evaluator has no sorts. Refused before the run: a constructor, a `case` or a branch that names a choice not declared; a case number not below its count; two branches for one number. Every case in a literal, the input or the starting state is checked against its own name, count and number, to every depth. The byte form of a name, a count and a number is not fixed here. `[revision 4, K-2 | proposed; reviewed by Codex G as ready to draft]`

**D-VAL-3.** Case analysis. One `case` names one choice. If its subject is a case of that choice with a branch, that branch runs. If it is a case of that choice without one, the `else` branch runs. If it is anything else, a value of another kind or a case of another choice, the `case` gives `none` and no branch runs. The `else` may be left out when every case of the choice has a branch. `[the owner's record on case 16, the second of two: option B | decided]` **Open, by the same record:** to reconsider, before the design and the implementation close, the other answer, in which `else` also takes subjects outside the choice. Option B removes using a case's `else` branch as a fallback for subjects outside the choice. What that does to mixed inputs still needs checking; the wrong-kind results and `same` already let a program tell some kinds apart: `same(compare(x, 0), none)` gives `truth.no` for a natural x and `truth.yes` for any other value; unlike `add`, `compare` does not build a copy of x. `[Codex C's review of revision 3, part 1 | fold; compare in place of add, from an outside read, by Claude Arch | proposed]`

**D-VAL-4.** One order over all values. Kinds first: natural, bytes, row, case, set, sequence. Naturals by size. Bytes by length, then byte by byte. Rows by length, then position by position. Cases by choice (name, shorter first and then byte by byte; then count), then case number, then what they hold. Sets by size, then members in order. Sequences by name (D-SEQ-2). A set is held with its members in this order and without repeats, and equal sets are one node. The order is total given the orders of choices and of sequence names. A program sees it only in the order of `members`; `compare` takes naturals only. `[revision 4, K-3 and K-8 | proposed; reviewed by Codex G as a conditional order ready to draft]`

**D-VAL-5.** Sets. `empty` is the set with no members. `insert(s, v)` has the members of s and v; if v is already a member it is s itself. `remove(s, v)` has the members of s other than v; if v is not a member it is s itself. `member(s, v)` is `truth.yes` exactly when v is a member. `size(s)` is the number of members. `members(s)` is a row holding each member once in the order of D-VAL-4. A set never changes. `[revision 4, K-14 | proposed; reviewed by Codex G as ready to draft]` A member may be any value. One that is or holds a sequence is compared and ordered by that sequence's name, never by what it holds or by its last place; changing a sequence leaves every set that holds it the same set; no set operation reads a sequence. `[Codex A, card 0475, under the owner's delegation | decided; stands unless the owner objects]`

**D-VAL-6.** Edges. No primitive fails. `[D L556 | agreed]`

| Case | Result | Whose |
|---|---|---|
| `sub(2, 5)` | 0 | owner, record edge-defaults-approved |
| `divmod(7, 0)` | the row (0, 7) | the same |
| Reading a row or bytes outside its range | a bare `none` | the same; and record out-of-range-bare-none |
| `slice` outside the range | `none` | record edge-defaults-approved |
| A write to a sequence outside it | `none`; nothing changes, no trail entry | the same |
| A shift right by more than the length | 0 | owner, record drop-head-strict-edges |
| A shift left by a huge amount | no special default: the safe bound on the result is reserved before anything is built; if that bound cannot be worked out safely or cannot be paid, the run stops as out of fuel; otherwise the ordinary shift result | the same |
| `make(0, v)` | an empty sequence; v is still evaluated | the same |
| `contents` of an empty sequence | the empty row; its last place stays 0 | the same |
| An arriving sequence whose last place breaks the rule: 0 for an empty one; a position from 0 to its length less one for any other | refused at the start | the same |
| `for x < 0 from y = 7 do ..` | no turns; the value is 7 | the same |
| A loop bound that is not a natural | the loop does not run; its value is `none` | the same |
| A primitive given a value of the wrong kind | `none` | the same |

`none` is the built-in `option.none` holding the empty row. A row that stores `none` cannot be told from a read outside its range, so a program that stores `none` checks the length first. `[the owner's record on option A, record out-of-range-bare-none]` What an edge result is charged, its arguments and one, is not the owner's: `[meter revision 5, K-13, rule E | proposed; G 0172 found it ready for Codex D to draft]` A loop whose bound is not a natural has still run e1 and then e2, once each, and what they did stands; only its turns are left out. `[meter revision 5, rule L; rules R6, EV-093 | proposed]`

### Sequences

**D-SEQ-1.** A sequence is an order of positions holding realized values. Changing what a position holds changes the sequence, for every holder, and it stays the same sequence. A change that happened is a fact whether or not anything later reads it. `[the owner's record that sequences change and stay | decided]` A sequence keeps its length; a different length is a distinct sequence. `[Codex A, card 0475, under the owner's delegation | decided; stands unless the owner objects]` A finite sequence is never called a list. `[the owner's record on wording | decided]` What a sequence holds at one moment is a row.

**D-SEQ-2.** A sequence's name shows which run made it. `[the owner: a sequence's name shows which run made it | decided]` The run part comes from the run's start itself, so two runs from one start name their sequences alike; it does not tell one occasion of running from another. `[the owner's record on the start as scope | decided]` Proposed construction: a sequence's name is a pair of a scope and a count, and two sequences are the same exactly when their pairs are equal. The scope is the named hash of a fixed label followed by the bytes of the program, the entry, the input and the starting state. Under this construction equal starts are the same logical run. A new run counts from zero; a replay is a new run from a recorded start; going back to a kept point stays in the same run and the count is never reused. A sequence that comes in keeps its pair; one that already carries the scope just computed is refused. Pairs are ordered by scope, shorter first and then byte by byte, then by count. `[revision 4, K-1 | proposed; reviewed by Codex C as ready to draft; the bytes and the hash are not fixed]`

**D-SEQ-3.** State, the record and the memo. A run's starting state gives, for each sequence the input can reach, what its positions hold and its last place; a literal in a program holds no sequence; a reachable sequence with no contents given is refused. The count is not part of a starting state. A record of a new run adds to the record of D-EV-2, which keeps naming the build: the choice declarations, the starting state, the scope, that the count began at zero with an empty memo, the fuel, the result or the stop, the trail of makes and writes in order, and each sequence's last place at the end. It supports: from this state, this build's run gave this result or stopped, having made these changes. `[revision 4, K-4 and K-12 | proposed; reviewed by Codex C as ready to draft]` Proposed test: a definition is state-free when neither it nor anything it can call uses `make`, `contents` or the write; a call that cannot be resolved fails the test. Only a definition that passes it may carry the memo mark. `[revision 4, K-10 | proposed; reviewed by Codex C as ready to draft]` A memo mark on any other definition is refused before the run. `[the owner's record confirming the refusal | decided; the exact test above stays proposed]` Every definition that admission and the checking of results run must be state-free (D-ADM-5); work that uses sequences goes to a checker with a record of its own. `[revision 4, K-10 and K-11 | proposed; reviewed by Codex C as ready to draft]`

**D-SEQ-4.** Reading, writing and charges. The primitives on a sequence are `make(n, e)`, `length`, `contents`, a write at a position, and `same`. `make` evaluates e once and gives a new sequence whose n positions all hold that value. Its arguments run first, n and then e, as for every primitive; if n is not a natural, `make` gives `none`, makes no sequence and takes no count (D-SEQ-2). `[meter revision 5, its stages and rule E; rules R6, EV-107 | proposed]` A program reads a sequence by `contents(s)`, which gives a row of what its positions hold now, and then reads the row; a position that holds a sequence gives that sequence, not what it holds. There is no read of a sequence at a position and no whole-sequence write. `[the owner's records: start on the strict variant; the head variant dropped; the whole-sequence write left out | decided]` Positions count from 0. `[the owner | decided]` A write that is made gives `truth.yes`, whatever value it wrote, so it is never mistaken for a write outside the range, which gives `none`. `length` of a sequence changes nothing, its last place included. `[rules R6, EV-045, EV-066 and EV-068, where the write's result is still a candidate; G 0173 found this text silent on both | proposed]` Charges count from where the last access was. `[the owner's record: charges count from where the last access was | decided]` Proposed, as K-13's mechanics: each sequence has a last place, which starts at position 0. The work part of a write that is made is its distance from the last place, plus one, and the write leaves the last place where it wrote; the write's whole charge also has the other parts named below. `contents` is charged its walk. For a sequence that is not empty it leaves the last place at the last position; for an empty one it gives the empty row and keeps the last place at 0, as D-VAL-6's edge rule says. The last place affects only what is charged, never what a program reads; it is part of the state, the record and every kept point. `[revision 4, K-13, with the record and kept-point contracts | proposed; the numbers under review; the empty case decided by the owner's edge record]`
A read at a position, charged the same way, is a recorded later option and not part of the design. Every rule, vector and program of the strict form stays valid if it is added. What would add it, found in a real checker: a sequence read while another holder may write it; or the checker's own memory of its writes costing more than twice what direct reads would; or a stale-copy mistake made and caught in review. Authors log each time they wanted to read in place, and the log is read before the builds are frozen. `[the owner's record keeping the strict variant, with Claude Arch's card 0048 for the evidence | working]`
The whole entry of each primitive, in four parts (arguments, what is built, what is held meanwhile, work), the four stages in which it is charged, the schedule for comparison and search, and three rules the table rests on (an edge result; a loop bound that is not a natural; which starting last places are admitted) are in meter revision 5, which replaces revision 4's K-13. `[meter revision 5, K-13 | proposed; G 0172 found it ready for Codex D to draft, with named gaps; pointed to and not copied]` The write to a sequence should have another word than `set`. `[revision 4, section 3.1 | proposed]` Reading a row should have another name than any read of a sequence. `[the owner: yes if Claude Arch and Codex D both agree; Claude Arch agrees; Codex D's view is due | waiting]`

### Breadcrumbs

`[the owner's records on breadcrumbs and on tracking jumps compositionally; Claude Arch's cards 0042 to 0049; reviewed by Codex C four times | all four passages proposed, none adopted]`

**D-BC-1.** The trail of a run is, in the order things happened, the fragments it executed: each request, answered or still open, with its reply when there is one; each failure and each catch; each place where a suspended continuation was resumed; and each restoration made in going back. A suspended continuation adds its fragment when it is resumed and not before. The trail of a whole is the fragments of its parts in the order the reference run executes them. The trail, or the record it is part of, also holds the final result or the failure and what it held, which answer met which pick, which values used only once were consumed, value for value and activation for activation, and for each reply from outside its endpoint, version, state and row. Defining the projections from these to D-RUN-9, D-CONC-6 and D-ENG-4 is owed.

**D-BC-2.** A kept point of a run is the rest of the run from there, as a value. Restored at a kept point: bindings, frames, loop state, handlers, activation and use-once information, the memo's entries, the result so far, and the contents and last place of every sequence reachable at the point. Never restored: the count that names new sequences. After going back has finished and been paid for, compare the continuation with a fresh run given the same answers, under a correspondence of names that fixes every sequence made before the point and keeps the order of those made after. If every charged input agrees and the fuel left is equal, they agree in their result or their stop, in what the sequences hold and their last places, and in the requests, replies and changes compared. Where corresponding names change a charge, two continuations that both finish agree in result, state and observations; their fuel use, and the point at which either runs out, may differ. So equal finite budgets do not by themselves guarantee the same result or stop, the same final state, or the same complete trail. A kept point that holds a value that may not be copied is run once or handed on once (D-TR-12).

**D-BC-3.** Going back to a kept point has two phases, each over the sequences reachable at the point, sequence by sequence in the order of names. A sequence made after the point is left out: nothing restored holds it. First each position written since the point is given back its value at the point, from the first position up, by a write charged as a write; a position that already holds that value is left alone. Then each sequence whose last place, as the first phase left it, differs from its place at the point is moved back, a sequence that was only read included, charged one for its marker and one for each position moved. `[two questions from an outside read, answered by Claude Arch | proposed]` Each step is charged before it is made, from the run's own remaining fuel, and no fuel is returned. If the next step cannot be paid for in advance, the run stops as out of fuel; the steps and markers already made stay made, and the trail holds them. This simple rule needs control of both what is restored and the last places: it applies only where nothing else can change those positions or move those last places between the kept point and the end of going back. Otherwise a protocol specified apart must account for the accesses in between and keep what they must observe. Keeping other writers out is not enough, since `contents` moves a last place without changing a position. D-TR-10 to D-TR-13 and D-CONC-8, on ownership and shared state, do not by themselves give that protocol. `[Codex C's review of revision 3, part 1 | fold; no protocol is proposed here]` Whether the writes of a failed part are kept or undone is the catching handler's choice. What the host was told stays recorded.

**D-BC-4.** An entry for a write may hold one of four amounts: that position i changed; that it changed to x; that it changed from y; or from y to x. `[the owner's sketch | the four amounts are the owner's]` For a stretch of the trail and one position, "from" of the first write and "to" of the last summarize the change between the two ends, for a consumer that looks only at the ends. What happened between stays in the ordered trail. Entries name the sequence by its name and the position. Between two kept points at most one "from" is needed for each position of a sequence.

### Open, from the second attack

`[Claude Arch's triage of the second attack, card 0050; its sources are being checked by Codex O | each is open, with a proposal; none is decided]`

**D-ATT-1.** Open. "Yes because the two sides are one node" is false for a term whose run makes something new. `make(1, 0)` written twice is one node and two sequences, which `same` tells apart; a constant of a use-once sort is the same case (D-UO-8), and the reference run's count of consumption (D-RUN-7) must not be keyed by a value that the evaluator makes one by content. Proposed: a use-once value in the reference run carries a name as a sequence does (D-SEQ-2), and "yes by identity of node" (D-RUN-4, D-LAW-2) is allowed only for state-free terms (D-SEQ-3). Its test: every small term, comparing "one node" with "two runs give the same value".

**D-ATT-2.** Open. Two of the meaning's values kept in one place of the machine pass every tracking clause, and a later read returns the wrong one: two cells made with 10 and 20, both named by one slot, read back 20 for the first. Proposed: a clause that the names of live values rest on parts of the machine's state that do not overlap, and that a tracker changes only the parts its own arguments rest on. Its test: the obligation generator on that two-cell tracker, which must be refused.

**D-ATT-3.** Open. The node record (D-REC-1) has no binder except a function, though D-RUN-4 requires a step to bind a term that has not run before it puts it in two places. Proposed: a `let` in the node record, read as part of the enclosing scope by the use-once check, as the evaluator's own language already has. Its test: `square(work(x))` run by a rule step, counting runs of `work`, and the use-once check on a `let` whose body uses an outer use-once value. A fourth point from the same attack is already answered here: a use-once value consumed once in each of two branches is two sites in one scope (D-UO-2), is written as rules that take it as an argument (D-UO-3), and its remaining case is recorded as refused though right (D-UO-15).

### From web round 3

`[web round 3: eight answers by one model and one cut-off answer by another, all written against revision 1; extracts by Codex U and Codex P; sources checked by Codex P and Codex O, none found to contradict its answer, some not checkable; read for this text through four helpers' inventories | web-answer material here is outside input folded as a proposal or an open item by Claude Arch; those proposals are not adopted; D-WEB-5 separately records the owner's decided hold and conditional permission]`

**D-WEB-1.** The explorer and the optimizer. Proposed: (a) Recognizing a search a user wrote by hand takes three separate claims: that this program computes this operation, that the interpretation satisfies the theory's laws, and that the replacement tracks it. Equal final values are not the first. (b) A call to a named library operation is searched in a stated order: identity, evidence already held, recipes for that operation, cheap refutations, then proofs. (c) A failed attempt reports which of these it was: a checked counterexample, a name too coarse, an obligation left, a form not supported, a budget spent, or a cost observed. A failed induction step is not a refuted law. (d) A search has one budget for proposing, checking and refining together, and exhausting a grammar shows absence only inside it, only with its covering fact, and only where every candidate was excluded conclusively; a proof left unfinished leaves absence unknown. (e) A cost is recorded as a bound, a measurement or an estimate, and each claims something different: a recorded computation establishes the number it returned on the bytes it names (D-PR-5); a bound covers its stated domain and needs evidence for that domain; an estimate carries its method and does not become a bound. (f) A result of extraction from an equality graph names how shared parts are charged: the least cost of an extraction from the same graph is 8 when every occurrence is paid and 5 when a shared part is paid once, and the two least extractions differ, since the one least under sharing costs 10 when every occurrence is paid. `[(d), (e) and (f) made precise by Codex Q's review of revision 3, part 2 | proposed]` Open: that the four routes of D-OPT-3 mix scope, time and kind of evidence; and the answer's seven records for the shared interface.

**D-WEB-2.** Recovery. Open, for the backend: what a compiled program must know at each call that may fail (which roots are live, which are moved or consumed, where they are), and that building the record of what survives cannot itself lose a value when memory runs out.

**D-WEB-3.** The concurrency core. Proposed: (a) For D-CONC-13: the carrier of a finished owner is clear or residual, where clear means this owner kept nothing and not that nothing waits; a probe that is pure, total and returns its whole argument; and the missing premise, that wherever an owner returns residual the whole outcome holds a wait. Without that premise a free cell holding a value is residual with no wait. (b) Looking at the queue hands the queue back, or the queue is used twice. (c) On two processors each real run must match some sequence of picks at whole segments, and a scope ends only when nothing is running, in flight or able to add work: two tasks that each read a counter and write one more give 2 in the core and can give 1 on two processors. Open, each filling a place this text marks as later: a use-once permit that makes "give it back to this cell" enforceable; protocols as a grammar with duals and hidden endpoints; a certificate of progress that names its claim and its assumptions; and the price of a scheduler over first-order command tags.

**D-WEB-4.** Finding laws. Proposed: (a) A smallest generating set of the implications that hold is a basis of one theory, and is a different result from a set of alternative theories (D-ENG-13). (b) A declared language of hypotheses names more than which laws and how long a body: its symbols, its constants, the sizes of terms and clauses, its quantifiers and how fitting is decided. A length limit alone does not make it finite, and a finite one need not be affordable. (c) A failed proof is kept as a residual with its assumptions, and three outcomes are kept apart: a false law, an induction hypothesis too weak, and an attempt not finished. Kept as an optional note, with its objective declared: ordering experiments by a prior. The recorded default stays the guaranteed split of D-STO-7, and the answer itself keeps policies for different objectives apart. Not taken, by the owner's rule that exact methods come first: the answer's trigger for building guarantees from samples. It drops the condition that an exact check has been measured as unaffordable, though it still asks for the exact route's recorded cost, the different conclusion a sample gives, and a derivation; a timeout alone would not meet it. D-PR-6 stands. `[Codex Q's review of revision 3, part 2 | fold]`

**D-WEB-5.** How rules are written. These bear on the method of specifying, which is not part of this text. Proposed for it: a case must separate the right reading from a named wrong one before any build; a rule's identity covers the meaning it rests on, notation and imports included; a rule's subject is whatever can satisfy it. Open: two computed gates, ready and accepted; and independence by who sees what, since two reviewers who miss the same faults miss them together. The owner holds topic 5: the specification trial goes on as Claude Arch runs it, and these points, with my card 0054 report on them, are kept and not acted on. Separately, once the meter table of K-13 is in Codex D's rules, Codex D may drop the sixteen fuel lines there that are true by definition. `[the owner's record holding topic 5 | decided]`

**D-WEB-6.** Building during a run. Proposed, filling what D-JIT-2 says is not designed: (a) a version of a part is fixed once made; a new one takes new calls and running ones finish where they are; moving a running computation is a separate checked step. (b) A version is kept while a frame, a pending return, a closure, a suspended continuation or live code can still enter it. (c) Making, checking and publishing a version are separate, and no caller sees one half published. (d) A fact learned in a run has a scope; a part built for it is entered only inside that scope or after a test, and falls back otherwise: a sum built for length two gives 11 on (4, 7) and must give 20 on (4, 7, 9). (e) Each attempt to build has a budget and then goes on by the version it has or a fallback; a build that runs out is not a failure of the program. (f) The record names each build and each version entered, and replaying what a program did, replaying what was planned and reproducing the bytes are three claims. (g) "Runs ahead of time" is tested with the ability to publish code taken away. Open: taking unit build jobs in fixed slots by the loss each avoids, whose two sources could not be checked.

**D-WEB-7.** Look-back. Proposed: step 3 of D-LB-4 is split into terms that are pure and total and the rest, because a kept construction's own run is then part of the claim. A view that respects named laws names them, exports only what respects them, and gives the same answer whatever the optimizer's budget. Open: what an inspector may see of a variable's number, which is D-ATT's question of how variables are numbered from another side.

**D-WEB-8.** Facets and the row. Proposed: (a) admission uses one selection of routes for all demands: if one route avoids a write and trusts a forbidden checker and another does the reverse, each demand has a route and the plan is still refused. (b) A bound says which of three things it promises about finishing: a bound on runs that return, which holds only if they return; that the run finishes within the bound; or a cap that is enforced, with the stops it permits named. `[made precise by Codex Q's review of revision 3, part 2 | proposed]` Open: a view for what an observer may learn, since a row holding "reads a secret" and "writes in public" cannot tell writing 0 from writing the secret; a view for what a computation needs from its context; and whether a reference to a store's cell can leave its store, which one answer asserts with no term shown.

### The records

**D-REC-1.** `[D L591-L603 | agreed, not run; lines changed by C6, C7, C23, C25 and C44 marked | fold; the lines from C25 and C44, and the line for step from C37, are approved, as forced moves 10, 24 and 19]` GAP 5: the shapes are to be tested by building slice 1.

```
Node            = sym(symbol, nodes) | lit(sort, value) | var(index) | lam(node) | app(node, node)
Symbol          = declared(id, theory, kind: sort | op | constructor | effect | law, signature)
                | defined(content hash, signature, rules)                                 -- C25
                | evaluated(content hash, signature, definition)                          -- C7, C25
Signature       = for an operation: { indices: a count, parameters: list of Parameter, result: sort }
                  for a sort: { indices: sorts,
                                declarations: any of finite(values), data(constructors), use-once }
                                                                                          -- C6, C23
Parameter       = value(sort) | bound(sorts of its variables, sort of its result, multiplicity: one | any)
                                                                                          -- C6
Rule            = { variables: a count, patterns: nodes, result: node }   -- variables stand as var indices;
                                                                             a rule is a scope for the use-once check
Theory          = { id, symbols }
Interpretation  = { from: theory, into: theory,
                    map: each sort, constructor, operation and effect of the source -> node }   -- C44
Claim           = the record of D-CL-1
Note            = { about: nodes, kind: estimate | sample | candidate | proposal, method, content }
row(n)          = the three sources of D-ROW-1
step            = the reference run, a program for the evaluator; its state and outcomes are recorded
                  in D-RUN-7                                                              -- C37; G F04
```

**D-REC-2.** Three passages add to a signature without yet giving it a field here: a sort's literal check (D-ADM-3), an operation's conditions (D-ADM-6), and a bound parameter's row variable (D-ROW-9). `[C25; C51; C35]`

**D-REC-3.** A node is a value of the evaluator, so the store's graph is the evaluator's interned values and the identity of a node is same. A sort's declarations are in its signature. A bound argument's multiplicity is in the signature of its operation. The id of a declared symbol is, as a default, its theory's id with its position in the theory, and names are metadata. Open: identity across versions of a theory. `[D L606-L608 | agreed]`

**D-REC-4.** The content hash of a defined symbol whose rules name the symbol itself, or of several that name each other: hash the group together, with each member written as its position in the group. `[D L612 | author's, proposed, not run]` GAP 4.

### Run results so far

**D-WRK-1.** The working rules, their tests, and what falls with each. `[the first text's section 2, kept here; rows changed by a later input are marked]`

| Working rule | Its test | If it falls |
| --- | --- | --- |
| Amendment 22: D-UO-2, 4, 6, 8, 10; D-RUN-3, 4. By the owner's record | The rerun comparisons on what is not covered: the whole language, handlers beyond small fixed cases, sort indices, lowering. D-EVD rows 4 and 17 are what has run, and both are reviewed | D L346 stands again, with the state of D-RUN-7 gaining a table of results |
| Quotation: D-TM-2 | None named beyond the written form of the mark | D L68 stands unqualified |
| The store's continuation: D-TR-11, D-TR-12 | Checked on two finite models, each reviewed (D-EVD rows 13 and 14). Open: deriving capture in general, the specialising check and its cache, and lowering | D-TR-13 alone stands |
| A last use: D-TR-9 | Its case, run by a second reviewer; the footprint record, to test | B2's old last sentence returns |
| A row entry's source and time: D-ROW-8, D-ROW-9 | A bound that tells a check's write at build from a guard's write in a run | Every entry counts as acting in the run |
| Rule 9 on a fixed core: D-RL-10, D-RL-11 | The four cases at the end of D-RL-11, in slice 4 | Only the first and last rows of the table are used |
| A condition in a signature: D-ADM-6, D-ADM-7. Taken by the owner; the test is still owed | An index bound and a purity condition: one test a call, each argument run once, evidence at the site removes the test, rule 10 refuses to assume the bound. And D-ADM-8's comparison | Return the failed test to the owner for a decision; a sort made by a predicate remains the alternative |
| A black box: D-ENG-4 | None named; its case is the control | Nothing else |
| The third way for bound arguments: D-THM-5 | Not named | Nothing else |
| Abduction ranks induction: D-STO-7. By the owner's record of the six answers, provisionally and to reconsider; it replaced bounding, whose direction was approved | The 56-candidate test, with D-ENG-13's third count. Not run | The candidate-theories query stays as D-STO-3 has it |
| Lens 09's four: D-ADM-8, D-ENG-12, D-ENG-13, D-ENG-14 | Named in each passage | Nothing else |
| The concurrency core: D-CONC-2 to 6, 8 to 11, 14. My call | The census of the whole language with functions held in data, by context. Not run. The three core tests that ran are D-EVD row 18 | D-TH-3, D-UO-5, D-ADM-2 and D-TR-12 stand as they are, and a binder that is neither applied nor a bound argument is refused |
| Look-back that cannot be seen: D-LB-2, and step 1 of D-LB-4 | D-LB-2's test with its nine controls. For step 1, a census of operations defined by rules, across element sorts and following helpers, and then the theorem. D-EVD row 28 is what has run | The marked laws are used only as any law is, by a proposer, with no mark; step 1 stays a decider named in the row |

**D-EVD.** Not design. The results the design, an item or a later input reports, each with the rule it was run under and who has reviewed it. Some rows group cited history. None is a proof. A result run under a rule this text replaces is evidence for that rule and for nothing here.

| # | Result | Run under | Where |
| --- | --- | --- | --- |
| 1 | Use-once, the reviewers' model: of 657,283 terms the old count accepted 37,564 wrong; clauses (a) to (d) accepted none and kept 160,022 of 161,498 right; the narrower rule kept 126,014 | One run for each node (D L346), sites by identity | D L52 |
| 2 | Use-once, the author's model: of 5,357 terms the old count accepted 924 wrong; (a) to (d) none, keeping 1,379 of 1,423; rule steps change 3,725 terms, 181 lose acceptance and 282 gain it | The same | D L54, L60, L708-L728 |
| 3 | A constant read as an outer value only: 4 wrong of 5,357; in a second model 48 wrong of 80,585 | The same | D L59; C item A |
| 4 | Run by occurrence, count by path, a new value at each run: no wrong term in 110,285 and 486,623 terms, keeping 30,330 of 31,079 and 90,652 of 91,983 right. With a constant as one fixed value, 20,754 wrong. With the rule steps D-TH-5 allows, no accepted term changes and 222 refused become accepted. A third lane recounted both tests, the first to seven occurrences and the wider to six, and agrees on every count | D-RUN-3, D-UO-2, D-UO-8 | C22; R24 section 4 |
| 5 | Without the rule on data with a use-once field, the wider census accepts 8,094 wrong terms | D-RUN-3 | C23 |
| 6 | A store's continuation, the earlier rule: on 276,528 programs the earlier form of D-TR-13 used alone accepted no wrong term and refused 87,196 of 92,176 right; a rule on the continuation's text alone accepted 2,148 wrong | The earlier form | R24 section 2 |
| 7 | Forms: of 60,000 random systems 164 pass forward and 33 backward, none wrong. Without B0, 1,017 of 1,256 wrong; the reviewers found 794 of 811 with an empty name wrong and none of 13 without. Mixed forms print 1 where the meaning prints 0. A late-choice name read twice gives (0, 1). A holding with one name for every integer passes F1 to F3 | D-TR-7, D-TR-8, D-TR-14 | D L178, L240-L243 |
| 8 | Composites: 427 in one form all pass, none wrong; of 97 forward-then-backward, 17 pass neither form, none wrong. 758 forward first-order systems closed under Close reach no wrong pair; 593 of them had a name that stands for several values, with a two-argument hidden operation and a branch on an observation. Start clause applied only after removal: 6 of 48 leave a bad pair | D-THM-1, D-THM-3, D-THM-4 | D L245, L415, L434; C18 |
| 9 | Rules on claims: a list of three was refused a count because a fourth was missing, and the list of four was given the count 4; with arbitrary sets as answers 6,257 of 16,838 unanswerable cases had no refuting pair, with intervals none of 36,986; one guard settled five times in a run, yes four times and then no | D-RL-2, D-RL-7, D-RL-8 | D L270, L274, L275 |
| 10 | Queries: the polynomial 96 + 93·comm + 40·assoc + 31·assoc·comm, with totals 189, 71, 62 and worths 118, 3, 9. INFERENCE of C34, to be confirmed against the script: each route's cost is taken where its claims are yes, the least is kept, and the totals are over two sites, one of which already has comm. Three instances gave 56 candidate theories, among them that every ring commutes, and a fourth removed 7. A power algorithm was refused over floating point, naming four laws that are no there; over the Gaussian integers its answer was seven claims to settle; a second algorithm had nothing to settle over the integers and was licensed | D-STO-3, D-ROW-11 | D L313, L319; C34 |
| 11 | Rows: a decider entered a row only through the evidence of a membership claim; a pick with no continuation is one node; rules tried in order gave two answers on a term with a variable. The failure clause ran on one case with two hosts, and nowhere else, with a client that has no handler: a tracker with another payload is told apart under the host that reports payloads and not under the other, and a tracker that returns where its operation fails is told apart under both | D-ROW-5, D-OP-1, D-RUN-5, D-TR-16 | D L88, L101, L229, L234, L350 |
| 12 | Grouped history: the eleven earlier toy results, the SRE's two small sheets found by hand, the toy's printouts, and the cases against the old count | Various | D L406-L416, L527, L614-L781 |
| 13 | The store's continuation as rewritten: 276,528 annotated terms, 92,176 right and all admitted, 184,352 wrong and all refused. Run by Codex S and independently reviewed by Codex Q. Capture placement and ownership were supplied facts of the finite grammar; forgetting inherited capture admits 864 wrong cases; deriving capture in general, the specialising check and its cache, stops for a resource and native lowering are not established | D-TR-11 to D-TR-13 | As G reports it, G L90-L92. Q's review itself is not an input of this card |
| 14 | An inner handler that reads the store: the main term returns only (0, 0) or (1, 1) with sound ownership, and D-TR-11 to D-TR-13 admit it, four of six terms in all; an outer handler that resumes twice gives all four pairs. Codex Q confirmed it within its bounds: six terms, 12 runs on names paired with 12 concrete runs. That four of six terms are admitted says nothing of handlers in general | D-TR-11 to D-TR-13 | Codex S, store tests, test 1 |
| 15 | Agreement at a stop: of four lowerings, the one that consumes the first value and runs out of memory is recorded as stopped for a resource and not as agreement; the three that consume twice, consume an unrelated value, or consume a held value before failing are refused. 28 comparisons, none counting a stop as agreement. S's first run used an invalid reference and is kept and not relied on. Codex Q confirmed the corrected run: 56 replays and 246 instructions, giving five agreements, four stops for a resource, 17 refusals and two inconclusive. For a permitted resource stop, the model compares an ordered prefix of requests and final counts value by value; that rule requires neither a step-by-step ownership trace nor equal held sets. Its failure comparisons separately require matching held identities | D-RUN-9, D-RUN-10 | Codex S, store tests, test 3, as corrected |
| 16 | A nested update without a scheduler: the lost update happens, 11 in the meaning against 10 on names, and every first-order check passes; the full clause for a bound argument and its continuation, under S's finite reading, already refuses the tracker, 8 of 40 cases failing. Codex Q confirmed it for that reading: 100 pairs of callbacks, 400 starts and 102,800 observations; the tracker that writes a stale value fails 8 of 40 related cases and the one that reads again passes 40 of 40. No general relation follows | D-TR-15, read finitely | Codex S, store tests, test 2 |
| 17 | Reuse: with D-RUN-3 as worded before R29, one use-once result stands at two places, and one value is consumed twice in two events, not once as R29 predicted; with the words "whose result may be copied", only the ordinary term is reused. Codex Q confirmed it on the fixture of 44 cases. "As worded before R29" means the old local test for reuse, and not the whole of item 22 under its other limits | D-RUN-3 | Codex S, store tests, test 4 |
| 18 | The core: 504 and 24 configurations, with all 68 schedulers that dropped or doubled a task refused and no right one refused; with a lock the counter ends at 2, without it at 1 or 2; two tasks that each receive first end with both waits in the store, on the two tapes of that program; the twelve tapes of the two controls complete. Codex Q recounted tests 1 to 3 with its own model and agrees. Test 4, a parked continuation, judged 120 right and 480 wrong correctly and did not establish that step is unchanged | D-CONC-2 to D-CONC-11 | ST, as R35 cites it; Q's review L1-L45 |
| 19 | Codex C's own finite checks on R35: three ownership ledgers for hold, one of which fails "cell full" after the callback returns; four owner states for settle; 24 cases comparing frames with environments. A reviewer's checks, by nobody else | D-CONC-7, D-CONC-9, D-CONC-13 | CR2 L50, L68, L78 |
| 20 | By hand, not run: the cases of D-ENG-9 and D-RL-13, the induction that needs a stronger invariant, and R36's worked case of a cheapest connector | D-ENG-9, D-RL-13, D-LAW-3, D-OPT-2 | R34 section 2; R36 section 5 |
| 21 | In the toy's own form, one term was yes at one sort by a decider, and unknown at another with the guard k = n + m left over | The toy's form of D-ADM-4 | D L335 |
| 22 | A count over a term as a tree gave 2 where the graph has 1 | D-TB-2, interning | D L373 |
| 23 | A cached sum gives 2 on one shared consumer and 1,073,741,824 on thirty levels, where the set has one member. Three answers agree with the set capped at two on 20,000 random shared terms | The old count; D-UO-10 | D L432 |
| 24 | Handlers read as functions that pass their state: the 600 configurations again, on the generic evaluator with no case added. 120 admitted and right, 480 refused and wrong, over 6,324 completed answer tapes. Codex Q recounted all of it with its own interpreter and agrees, and found the evaluator byte for byte the earlier one. Counters as corrected: 41,616 reads and 15,216 calls of the choosing rule. New source rules were supplied. General substitution, writes, stores that interact, a callback whose body is not in the term, recursion, failure, fairness and schedules without end are untested | D-CONC-7 | Codex S, card 0012, test 1; Q90 |
| 25 | One algorithm licensed and refused. On all 1,100 simple labelled graphs of up to five vertices, the three laws hold of forests at every graph, and of matchings at 173, with 927 refused. With weights, on the 76 graphs of up to four vertices and every weak order of weights with ties, using the test's tier offset two, 9,396 cases, the greedy choice over forests never differs from a least-cost maximal base, and over matchings it gives 3,687 that are not best and 779 that are another best. Codex Q recounted these. The larger weighted count on five vertices had its arithmetic reviewed and was not replayed. The objective is least weight among maximal bases, and orders with ties do not cover every positive weight. That exchange holds for the forests of every finite graph is an argument on paper: the licence for the family, its covering evidence and the derivations are NOT DONE | D-OPT-2, D-OPT-4, D-SL-5 | Codex S, card 0012, test 2; Q90 |
| 26 | Close as one fixed program: eighteen descriptions, five accepted, thirteen refused, none unknown; the six required refusals each at its own stage; 45 definitions and 352 obligations. Codex Q's own interpreter agrees on every verdict. The registry and its covering facts are trusted inputs, and the fuel is not D-EV-1's meter | D-RUNEV-5 | Codex S, card 0012, test 3; Q90 |
| 27 | Abduce, then generalise, on polynomials built by zero, inc, shift and mul_x, with parity at 2: induction on the first residual fails at shift; the statement for every k passes; the smaller language keeps 25 of 45 schemas and the wider 125 of 882, the target among them. Codex Q recounted all 927 candidates. The general lift is NOT DONE | D-LAW-3, D-ENG-13 | Codex S, card 0012, test 4; Q90 |
| 28 | Look-back, my own check on card 0038: 23,983 list terms of up to nine nodes, where every observation of the written term that was tried gives two answers inside all 15 classes of equal terms, and the value's outer constructor gives one; ten rewrites, of which two right ones change the number or order of visits; 243 operations that use an element only as itself, all commuting with the 27 maps of one sort of three members. Codex C recounted the first two parts exactly, and the 243 under its own reading of the grammar; my two larger inventories were not recounted. Codex C's own controls: a family that depends on the element sort fails 68 comparisons across sorts and none inside one sort; seven laws agree in all 763 pure cases; two maps made one, unguarded, disagree in 4,944 of 28,672 mixed cases | D-LB-1 to D-LB-4 | R38 section 6; LBR findings 2 to 4 |

A warning kept from the design: its author reports that earlier reviewers used the clause for one-sided steps on a worked chain the author had not seen, and reported the backward form as where it is known to misbehave (D L231). That is history about an earlier form, not a shown failure of D-TR-18.

**Cited and not copied.** The seven places where the design is most likely to be wrong (D L783-L834). The author's list of unreviewed additions (D L836-L856), which item A answers. The design's remark that the check replaced a count of consumers, with its appendix of cases (D L50). The published sources behind rule 9 (D L289) and behind the use-once check (D L790). The costs of the five sentences on chance (R30 4.1). The rest of R34, R35, R36 and R38: their readings of other reports, their tests, and what they put to the owner.

## 4. What changed

From the first text, my 0033 report as sealed, to revision 1. SOURCE for the lists of added and retired anchors: a program's comparison of the two files (section 7). The list of changed anchors is from my own edits, and INFERENCE to that extent. An anchor that is not listed is as it was.

**Retired, 2.** Neither number is used again.

| Anchor | Reason |
| --- | --- |
| D-UO-13 | It was the placeholder for recovery. D-UO-16 and D-UO-17 take its place |
| D-CONC-1 | It was the placeholder for the concurrency core. D-CONC-2 to D-CONC-15 take its place |

**Added, 39.**

| Anchors | What | From |
| --- | --- | --- |
| D-UO-16 | Going on after a failure: both answers, and what the text does meanwhile | R32, decision 1. Open: web round, by addendum 2 |
| D-UO-17 | One usage mark or two: both answers, and what the text does meanwhile | R32, decision 2. Open: web round, by addendum 2 |
| D-CONC-2, D-CONC-3 | Functions held in data, and where a use-once function may stand | R35 4.1 |
| D-CONC-4, D-CONC-5, D-CONC-6 | Tasks, the scheduler's rules, and what they say | R35 4.2; Codex C's G5 |
| D-CONC-7 | Handlers by substitution, as a candidate with what it still owes | R35 section 3; Codex C's G2 |
| D-CONC-8, D-CONC-9 | The owner, the cell, and what hold does and does not promise | R35 4.3; Codex C's G1 |
| D-CONC-10 | Channels, and protocols as a sketch | R35 4.4 |
| D-CONC-11, D-CONC-13 | The three kinds of claim; where a wait shows, as a sketch with what it owes | R35 4.5; Codex C's G3 |
| D-CONC-12 | A failure in a task | R35 4.2; Codex C's G4 |
| D-CONC-14 | What the core costs | R35 4.6; Codex C's account |
| D-CONC-15 | Counting looks at a held-out set; a placeholder for what is in reports that were not inputs | R35 sections 2 and 5 |
| D-JIT-1 to D-JIT-5 | Ahead of time as the default, just in time kept open: what it owes, the lock, where it first appears, and the partition matroid | Addendum 1 to card 0037 |
| D-OPT-1 | The names | The owner's two records on names |
| D-OPT-2 | The optimizer may change the algorithm | R36; the owner's record |
| D-OPT-3, D-OPT-4, D-OPT-5 | Where a condition is settled; what licenses a greedy method, as Codex O (Citations) narrowed it; three doors left as they are | R36; Codex O's check |
| D-ENG-9, D-ENG-10, D-ENG-11 | Overlapping names; what is known of an object that can only be asked; a sheet's line is read | R34, L9-1, L9-5, L9-8 |
| D-ENG-12, D-ENG-13, D-ENG-14 | Three working items with their tests | R34, L9-10 to L9-12 |
| D-RUNEV-5 | Close has a program | R34, L9-2 |
| D-RL-13 | The program that checks a refutation | R34, L9-3 |
| D-STG-3 | Where the evidence that admits a term is paid, and where a removed guard is | R34, L9-4 |
| D-TR-19 | A claim about names is stated under the naming relation | R34, L9-6 |
| D-LAW-3 | What a lift may cite before slice 4 | R34, L9-7 |
| D-ADM-8 | A condition as a sort cut by a predicate, to test against D-ADM-6 | R34, L9-9 |
| D-WRK-1 | The working rules with their tests | The first text's section 2, which this report no longer carries |

**Changed, 57.** A program's comparison of the two files finds these 57 and no others, once a paragraph with no anchor at the head of the concurrency core is set aside. The other 122 passages of the first text are as they were, up to white space.

| Anchors | What changed | Reason |
| --- | --- | --- |
| D-TR-5 | Its last sentence | Codex G's F01, in the wording the owner approved as R36's door 4 |
| D-RUN-1 | Its last bullet | G F02 |
| D-EV-1 | The meter's first line restored; C8's defaults tagged as waiting | G F03; card 0037 |
| D-REC-1, D-RUN-8 | step points to D-RUN-7; "asked" | G F04 |
| D-ADM-5 | One sentence | G F05 |
| D-STO-7 | Four clauses restored; standing narrowed | G F06 |
| D-PR-6 | Two cells restored | G F07 |
| D-ENG-7 | The mechanism's sentence restored; the bound by D-STO-7 made conditional; names; tag | G F06, F08, F11; the owner's records |
| D-TR-10, D-TR-11, D-TR-12, D-TR-13 | Tags now say the rule has been run and reviewed on one finite model. D-TR-12 gains R24's caveat on the known-rule check, a pointer to D-UO-16, and the other answer | G F09; Codex S's store tests |
| D-UO-11, D-UO-12 | The approved part of each tag narrowed | G F10 |
| D-TH-5, D-ROW-11, D-RUN-3, D-ST-2 | Tags no longer quote replaced words. D-RUN-3 also points to Codex S's reuse test | G F11; S's test 4 |
| D-FND-3 | The limit of the hash trial | G F12 |
| D-TB-5 | The scope of the owner's figures | G F13 |
| D-TH-7, D-TR-8 | Cases given their old-rule scope. D-TH-7's refusal tagged as waiting | G F14; card 0037 |
| D-TR-15 | The opening line on operations that may not return | G F15 |
| D-EVD | Ten restorations; eleven new rows; its heading says some rows group history | G F16; the new inputs |
| D-STO-6, D-SL-4, D-RUN-5 | Attribution | G F17 |
| D-SL-1 | Slice 1's minimal scope; "the WebAssembly engine" | G F18; names |
| D-ST-4, D-FND-2, D-TB-4, D-OPEN-1, D-SL-8, D-ENG-1, D-ENG-2, D-ENG-4 | "The engine" is the SRE and "the lab" is LoomLab. D-TB-4 adds the optimizer to what is not trusted. D-SL-8 gains one sentence from R36's door 1 | The owner's records on names |
| D-ROW-5 | "The engine" there is written "the WebAssembly engine" | My reading, tagged as such |
| D-SL-5 | Two finish lines added: an algorithm substituted and refused; D-JIT-4's | R36 door 1, approved; addendum 1 |
| D-REP-4 | One row: another algorithm for an operation | R36 door 2, approved |
| D-IN-2 | One sentence: a derivation travels with an interpretation | R36 door 3, approved |
| D-ROW-10 | "Two trackers for one operation" among the routes | R36 door 5. Not in the owner's record |
| D-RL-7 | A finite set of witnesses between a pair and the whole set | R34, L9-3 |
| D-TM-2, D-TR-6, D-ROW-2, D-ADM-6, D-ADM-7 | Tagged waiting on the owner, with the other answer in the next line | Card 0037: choices 3, 8, 6 and 7 of the first text |
| D-ADM-4, D-PATH-1 | Tagged owner (recorded), with the answer and the answer not taken. D-ADM-4 now says slice 1 refuses | The owner's record on the two slice 1 choices; addendum 2 |
| D-ADM-2 | No longer a choice put to the owner by itself: D-CONC-2 answers it if the core is taken | Codex G's ruling on my doubt (G L123); R35 4.1 |
| D-LAW-2, D-ROW-8, D-RL-11, D-PATH-2, D-PATH-3, D-TB-2 | Tagged waiting on the owner, with the other answer. D-TB-2's cell on the closure checker now points to D-RUNEV-5 | Card 0037: the smaller choices |
| The legend at the head of section 3 | New sources, new tags, the names | All of the above |

**Not changed, though an input touches it.** D-RUN-7 keeps its handlers field: R35 proposes removing it and Codex C's G2 says not yet. D-TH-3, D-UO-5 and the other passages the core amends are left as they were, with the amendments stated in D-CONC-2 and D-CONC-3, so that the core can be taken or left whole. D-TH-7, D-UO-2 and D-TR-12 are likewise untouched by D-UO-17. D-FND-5, lens 13, is still a placeholder.

## 5. For the owner

Only what is new since my reports on cards 0033 and 0035. The choices already put to you are not repeated. All recommendations are PROPOSED.

**1. Building ahead of time and building during a run.** You asked for both from the start, with ahead of time preferred. The text read as ahead of time only, and never named the other. It now says both are in the design, ahead of time is the default, and building during a run is an option for a part of a program (D-JIT-1 to D-JIT-5). Four things for you to confirm or change:
- A part built during a run may choose only things a user cannot see, apart from time and memory. Everything that changes what the program does is fixed before the run. So a program is the same program however it is built.
- I have put its first appearance late, where the planner arrives, because before then a part built during a run has nothing to choose. Its finish line is one part built during a run, checked before it is entered, and agreeing with the reference.
- How long code made during a run is kept, and who owns it, is not designed.
- On the old note that said "the compiler is a matroid": what is sound in it is small. Choosing one way of building for each independent part is a simple structure in which picking the cheapest for each part is right, so long as the parts do not affect each other. A cost paid once for having the run-time builder at all already breaks that. The compiler as a whole is not that structure.

**2. Two concurrency choices you left to me.** I took both, and say how sure I am.
- *Counting repeated looks at a test set.* Confident. Counting forbids nothing and shuts nothing off: a rule that forbids can be added later over the same records.
- *The concurrency core in this round.* Confident that most of it belongs in now, as working rules, because it changes three of the trusted texts and it is cheaper to write those once. Not confident that it is right in every corner: one large test is not yet run, and if it fails those rules fall. Three parts I left open because the core's reviewer found real holes: how a paused task is resumed without changing the reference run, how a task left waiting shows in a result, and protocols.

**3. What the core's reviewer changed in what I told you on card 0035.** Three corrections.
- I said that without the new rule there is no scheduler at all. That was too strong. A simpler scheduler is possible without it; this one needs it.
- I said a yes to taking back what failed code held would let the other tasks go on when one fails. Not by itself: someone has to be named to hand the held things to, and nobody is yet.
- I said one helper gives a lock's value back on every run. It does not: it tries once, and the try can fail.

**4. The store rule has now been run.** The first text asked you which rule for a store should stand while the better one was untested. It has since been run on 276,528 small programs and checked by a second lane: no wrong program let through, no right one refused. It is still a working rule, because that model was handed some facts a real checker would have to work out.

**5. A function kept as a value.** The first text asked you whether a function may be stored like any other value. The concurrency core answers it in one narrow way: a function may be stored where the data's own declaration says it holds one, and how often it may be run. That goes with the core, as my call above.

**6. Lens 09.** Eight proposals are folded as proposals. Three have a cost you may care about:
- One more trusted program, the one whose run counts as "checked on every case by closing under the operations". Today that rule is trusted and no program is named for it.
- A program whose limits forbid any possible failure is refused even when a later analysis would have shown the failure can't happen, unless the writer brings that analysis forward as evidence.
- Before proofs arrive, what the SRE reports about infinite objects will mostly be candidates, not facts.

**7. The optimizer.** What you decided is folded: the row, the sentence, the finish line and the repair. One further line I added is not in your record: that two algorithms for one operation are two routes the planner may choose between. A citation check found three of my statements about greedy methods too absolute, and the text now carries the narrower forms.

**8. A reading of mine to confirm.** In two places the design says a build's row "names the lowering and the engine". I read that engine as the WebAssembly engine that runs the program, and not the SRE, and wrote it so.

**9. Where I was wrong.** One prediction of mine failed in a detail. I said the older wording on reuse would consume one value once where it should be twice. The test found it consumed one value twice, which is worse. The repair I proposed still held. That test is not yet reviewed.

**10. Specification starts with the evaluator.** Its first gap list is in section 6. Seventeen things the design names and does not state will come to you as short cards, each as a case with two outcomes. The first three are the name of the hash function, what a primitive gives at its edges, and the table of fuel charges.

### A question for the web round, on recovery

*Self-contained, for outside reviewers.*

**Background.** In this language some values must be used exactly once: a file that must be closed, a lock's state that must be given back, a ticket that must not be used twice. The checker refuses a program that could use such a value twice or silently drop it. When a piece of code fails, it may be holding such values. If nothing catches the failure, the run stops, the values are still held, and the outcome names them: nothing is silently lost. The open question is what may happen when something does catch the failure and wants to carry on. The failed code can never be resumed, and the values are inside it.

**Decision 1. May whoever catches a failure take back what the failed code was holding?**
- *Yes.* The catcher is handed the held values and must finish, use or pass on each one. A parser can retry from where it failed; a failed task's lock can be given back; a file can be closed and the program goes on. Cost: one new operation in the small reference interpreter that everything else is checked against, which must find the live values inside code that has stopped; and compiled programs must know, at every call that might fail, what is being held. Values the catcher cannot name, and functions that hold something, still cannot be taken.
- *No.* Catching a failure and carrying on is allowed only where the failed code held nothing of this kind. Anything that must survive a failure is kept by an owner outside the code that may fail, and the code works through a reference. Cost: no change to the reference interpreter; a rule of style that writers will meet often, and that makes the plain way of writing a parser or a lock unavailable.

**Decision 2. May each kind of value say for itself whether it can simply be left behind?**
- *Yes.* "Never used twice" and "never left unused" become two separate marks. A ticket or a not-yet-read choice is marked only "never twice", and catching a failure over it needs no cleanup. A file keeps both marks. Cost: the checker learns two marks where it had one, and its tests are run again.
- *No.* One mark, "exactly once". Catching a failure gives no permission to drop a held value: a program may carry on only after each held value has been used, finished or handed on by an operation it is allowed to call, and otherwise the failure goes on up with the value still held. Whether the catcher can reach the value at all is decision 1. A library may supply the cleanup where one exists.

**Cases that would settle them.** For each, say what the program should be allowed to do, and what the language must then guarantee.
1. A program opens a file, hands it to code that fails halfway, catches the failure, and continues.
2. A task fails while holding what it took from a lock; other tasks are waiting for that lock.
3. A parser holds its input, fails partway, and wants to retry from where it stopped.
4. A ticket is made, then a failure happens before the ticket is used; the failure is caught.
5. A catcher takes a value out of code that could in fact still be resumed, and then resumes it. This one must be refused: the value would be in two places.
6. A container that may be left behind holds a value that may not. Leaving the container would drop what is inside.
7. The failed code holds a value of a kind the catcher has no name for.

**What we would like back.** Whether there is a third design we have missed. Whether "yes" to decision 1 can be had without adding an operation to the trusted interpreter. Which published languages have faced this with values that may not be dropped, and what they chose. And any case where either "yes" lets a value be lost or used twice.

## 6. The first spec cards

All PROPOSED. Claude A relays; I contact no lane.

### The first area: the evaluator

INFERENCE, my reasons. Every run record names the evaluator's build (D-TB-2), every trusted text is a program for it (D-TB-1), and nothing lies beneath it to define it, so it is the one part that numbered rules alone must fix (my 0031 report, section 2). It is also small, has no open decision of meaning inside it, and waits on neither the web round nor the concurrency core. Its passages: D-EV-1, D-EV-2, D-TB-1, the rows of D-TB-2 on the evaluator, interning, the content hash and fuel, D-RUNEV-1's Eval, D-RUNEV-2's first sentence, the run record in D-CL-1, and D-ADM-5 where it says what an evaluated definition is.

### Its gap list against revision 1

SOURCE for "what the text has": the anchor named. INFERENCE for each gap: I looked for the answer in the passages above and did not find it. E-1 to E-3 are gap 3 of my 0031 report; the rest are new here. None is filled.

| # | Anchor | What the text has | What is not stated |
| --- | --- | --- | --- |
| E-1 | D-EV-1, hash; D-TB-2 | "one named function, the same in both builds" | Its name, and the form of its result |
| E-2 | D-EV-1, edges | Three edge results, marked "Proposed" | Whether they are adopted. A case each: sub(2, 5); divmod(7, 0); get past the end |
| E-3 | D-EV-1, meter | A charge by bit length of arguments; one for a call and for a loop turn; a table, "one line for each primitive", that is part of the specification | The table. How bit lengths combine for two arguments. The bound each primitive works out for its result. What let, case and a variable cost |
| E-4 | D-EV-1, value | n, bytes, tag(v, .., v), array | Whether a natural has a largest size. How a literal array or bytes value is written. What names a tag, and whether its count of fields is fixed |
| E-5 | D-EV-1, prim | "no primitive fails" | What a primitive gives on an argument of the wrong shape, such as add of a tag and a natural |
| E-6 | D-EV-1, prim | "bit operations"; shift | Which bit operations. The direction of shift and what a shift by more than the length gives |
| E-7 | D-EV-1, prim; C8's line | compare gives one of three tags, divmod one tag holding two, same one of two tags | The names of those tags. C8's defaults also wait on the owner (D-EV-1's tag) |
| E-8 | D-EV-1, arrays | get, set, length, make(n, e) | Whether set gives a new array and leaves the old one as it was. Whether e in make runs once |
| E-9 | D-EV-1, case | A case on tag(x, ..), ending with an else branch | What a case does with a natural, bytes or an array as its subject. Whether two branches may name one tag |
| E-10 | D-EV-1, for | e1 and e2 run once; the value is the last y | What the loop does when e1 is not a natural. The value when e1 is 0 |
| E-11 | D-EV-1, total | At most one loop; calls only total definitions that come before it | Whether a loop inside a called definition counts. What a program is: a list of definitions in an order, and how it is written |
| E-12 | D-EV-1, checker; D-CL-1 | eval(fuel, f, v); out of fuel is unknown, never no | How a definition of several parameters is given one v. The form of the out-of-fuel outcome. What unit fuel is in |
| E-13 | D-EV-1, memo | Calls cached by the identity of the argument; a hit charges one; the cache lives for the run | How a definition is marked. The key for several arguments. Whether a call cut short by fuel leaves an entry |
| E-14 | D-EV-1, value; D-TB-2 | Values are interned; same sees identity | Whether same on two arrays or two bytes values of equal content is always yes. What interning charges |
| E-15 | D-TB-1, D-TB-2 | "built twice by independent means"; "the two are compared" | What makes two builds independent. What is compared, on which inputs, and what the record of a comparison holds |
| E-16 | D-STO-1; D-REC-4 | Content identity; gap 4 | The bytes that a value's identity hashes. It belongs to the records, and the hash primitive here must agree with it |
| E-17 | D-EV-2; D-OPEN-1 | The counted loop is the default; recursion on a proper part is the alternative, open | Which stands. Rules are written for the default and marked working |

### Order of relay

Codex D (Specs) first. Codex G (Spec Reviewer) on D's sealed draft. Codex S (Rule Tester) on the rule file after G's review, and without the design. Codex V (Test Ledger) last. In each card `<R1>` stands for the sealed copy of this report and `<...>` for a sealed folder that does not exist yet: Claude A puts in the path and SHA-256 at relay.

Codex Q (Model Checker) gets no card yet. INFERENCE: nothing in this area is a statement about every program until the meter's table exists (E-3). When it does, "a definition that is total by its syntax ends within a fuel bound read from its text" is Q's to run on every small definition.

### Draft card for Codex D (Specs)

```
To: Codex D (Specs).   Card: the evaluator's rules, draft 1.

Why. Specification starts here. The evaluator is the first area: every run record names its build, and
nothing lies beneath it to define it, so numbered rules have to fix it. Nothing you write adopts
anything; the owner decides.

Inputs. Check each hash before reading. Stop and report on a mismatch.
  <R1>  path and SHA-256 from Claude A. Read section 3, these passages only: D-EV-1, D-EV-2, D-TB-1,
        D-TB-2, D-RUNEV-1, D-RUNEV-2, D-CL-1, D-ADM-5, D-STO-1, D-REC-4. Read section 6: the gap list
        E-1 to E-17.
  C:\Users\grego\.codex\reviews\2026-11-10-CLAUDE-ARCH-HOW-WE-SPECIFY\REPORT.md
        SHA-256 1cac49df25a7085203b63098a7d5ae8afc11e16e3f81c1b67a175b5977bb923f
        Read section 2, "What a rule is": the form every rule takes.
  No other file. Not the repository.

Do.
  1. Write the rules, EV-001 onward, in the form of that section 2: one obligation in each; revision 1;
     kind (definition, requirement or permission); subject (an evaluator build); from (an anchor of
     <R1>, with <R1>'s SHA-256); text; case; excludes.
     A case is a program, an input and a fuel, with the output and the fuel left, or "out of fuel".
     Excludes is the nearest wrong outcome on that case.
  2. Standing. "working" where the anchor's tag says working or waiting on the owner, naming what it
     waits on. "draft" for everything else. Nothing is "approved".
  3. Gaps. For each of E-1 to E-17, and any you find, write a gap entry: the anchor, what is not
     stated, one case, two candidate outcomes on it, and what each would cost. Choose neither. A rule
     that needs a gap's answer is written with standing "draft" and names the gap.
  4. Coverage. A table from each line of the block in D-EV-1 to the rules and gaps that cover it.
  5. Propose, in HANDOFF.md, how a rule's hash is computed from its binding fields (kind, subject,
     text, case, excludes). One paragraph. It is a proposal for the reviewer.

Output. A fresh folder C:\Users\grego\.codex\reviews\YYYY-MM-DD-CODEX-D-EVALUATOR-RULES with
RULES-EVALUATOR.md, GAPS-EVALUATOR.md, COVERAGE.md, HANDOFF.md and the two bindings files.

Your own checks, each reported with its count.
  a. Every "from" names an anchor that exists in <R1>. None names a line number.
  b. Every requirement has a case and an excludes.
  c. Every line of D-EV-1's block is in COVERAGE.md.
  d. Every sentence of a rule that its anchor does not say is listed, and is either removed or turned
     into a gap entry.
  e. The word "type" is not used of Loom: say sort, value space, theory, model.

Stops. Stop and report, without choosing, if:
  - a hash does not match;
  - two passages of <R1> give different outcomes on one case (give the case);
  - you need a file that is not listed;
  - a rule cannot be written without filling a gap.
No code, no build, no Git, no repository write, no web. Label claims SOURCE, INFERENCE or PROPOSED.
```

### Draft card for Codex G (Spec Reviewer)

```
To: Codex G (Spec Reviewer).   Card: review of the evaluator's rules, draft 1.

Why. Codex D (Specs) has drafted the first rule file. Before any test is written from it, each rule is
held against the passage it comes from. This review adopts nothing.

Inputs. Check each hash before reading. Stop and report on a mismatch.
  <D's sealed folder>  path and SHA-256 of its OUTPUT_BINDINGS.json from Claude A. Read
        RULES-EVALUATOR.md, GAPS-EVALUATOR.md, COVERAGE.md and HANDOFF.md.
  <R1>  path and SHA-256 from Claude A. Section 3, the passages D's card lists, and section 6's gap list.
  C:\Users\grego\.codex\reviews\2026-11-10-CLAUDE-ARCH-HOW-WE-SPECIFY\REPORT.md
        SHA-256 1cac49df25a7085203b63098a7d5ae8afc11e16e3f81c1b67a175b5977bb923f   Section 2 only.

Do. Start from the passage, not from the rule.
  1. For each rule: does its text say what its anchor says, and no more? Does the outcome of its case
     follow from the anchor alone? If it needs something the anchor does not say, that is a finding,
     and the rule should name a gap. Is its excludes a wrong outcome that a plausible build could give?
     Is its standing right?
  2. For each gap entry: is it truly not stated? If <R1> does state it, say where.
  3. Is any line of D-EV-1's block covered by nothing? Is any rule hiding a choice that should be a gap?
  4. Review D's proposal for a rule's hash: is it fixed by the binding fields and nothing else?
  5. Give each rule one verdict: holds; holds with a fix (give the words); does not hold (say why).

Output. A fresh folder C:\Users\grego\.codex\reviews\YYYY-MM-DD-CODEX-G-EVALUATOR-RULES-REVIEW with
REPORT.md, HANDOFF.md and the two bindings files. The first line of REPORT.md is the overall verdict.

Your own checks. Use finite checks of your own, not D's scripts. Report how many rules and gaps you
compared, and by what method.

Stops. Stop and report if a hash does not match, if you need a file that is not listed, or if D's folder
has changed since it was sealed. Do not rewrite the rule file: give fixes as words. No code beyond
your own checks, no build, no Git, no repository write, no web.
```

### Draft card for Codex S (Rule Tester)

```
To: Codex S (Rule Tester).   Card: vectors and controls for the evaluator's rules.

Why. A rule is only as good as a test that can fail. You work from the rule file alone, and not from
the design: every question you have to ask shows where the rules do not say enough. Author evidence
only; it adopts nothing.

Inputs. Check each hash before reading. Stop and report on a mismatch.
  <D's rule file, as revised after review>  path and SHA-256 from Claude A: RULES-EVALUATOR.md and
        GAPS-EVALUATOR.md.
  Do not open <R1>, the design, the corrections or the repository. If you cannot go on without them,
  that is a result: stop and report the question.

Do. State your bounds before the first run.
  1. Build a small model of the evaluator from the rules alone.
  2. For each requirement rule, write its case as a vector, and at least two more vectors that the
     rule decides.
  3. For each requirement rule, make its excluded outcome into a switchable wrong variant of the
     model. Show that the rule's vectors pass on the model and that at least one fails on the wrong
     variant. A rule whose wrong variant passes every vector is reported as "not shown able to fail".
  4. Keep a list of every place where the rules did not say enough to build the model: the rule, the
     smallest case, and the outcomes you could not choose between.
  5. For each gap entry, write vectors for both candidate outcomes, labelled. Choose neither.

Output. A fresh folder C:\Users\grego\.codex\reviews\YYYY-MM-DD-CODEX-S-EVALUATOR-VECTORS with the
model, VECTORS.json, CONTROLS.json, QUESTIONS.md, REPORT.md, HANDOFF.md and the two bindings files.

Your own checks. Recompute every vector's expected outcome at the primary, apart from the model that
produced it. Report counts: rules, vectors, controls that failed as they should, rules not shown able
to fail, questions.

Stops. Stop and report if a hash does not match, or if a rule gives two outcomes on one case. Python
with -B only. No native build, no Git, no repository write, no web, no slots. A run cut short by its
bound is reported as neither a pass nor a failure.
```

### Draft card for Codex V (Test Ledger)

```
To: Codex V (Test Ledger).   Card: the first evidence records and three views, for the evaluator.

Why. The team's method says that whether a rule is satisfied is read from evidence records and never
written by hand. This card tries that on the first real evidence. It is also the trial of the record's
shape: if a field cannot be filled from the packages as delivered, the shape is wrong, and that is
what to report.

Inputs. Check each hash before reading. Stop and report on a mismatch.
  <D's sealed folder, revised>, <G's sealed folder>, <S's sealed folder>   paths and SHA-256 from
        Claude A.
  C:\Users\grego\.codex\reviews\2026-11-10-CLAUDE-ARCH-HOW-WE-SPECIFY\REPORT.md
        SHA-256 1cac49df25a7085203b63098a7d5ae8afc11e16e3f81c1b67a175b5977bb923f
        Section 3 only: "E's proposal 4" (the record's fields) and "How the links run".

Do.
  1. For each of S's results, write one record with these fields: the statement settled, with its
     scope; the rule's ID and hash; the subject's kind and hash; the kind of evidence (a run); the row
     (the check, the oracle and what the oracle was built from, the generator, the tools, each by
     hash); the controls; the assumptions; who produced it and who reviewed it. No status field.
  2. G's review is filed as a note with its method, not as evidence.
  3. Generate three views from the records, by a program: rules with no vector; records whose rule
     hash is not the current one; rules that ran and were not shown able to fail.
  4. List every field you could not fill from the packages as delivered, and what was missing.

Output. A fresh folder C:\Users\grego\.codex\reviews\YYYY-MM-DD-CODEX-V-EVALUATOR-LEDGER with
RECORDS.json, the three views, the program that made them, REPORT.md, HANDOFF.md and the two
bindings files.

Your own checks. Each record's hashes match the sealed files. Each view is made again from the
records and compared. Report counts.

Stops. Stop and report if a hash does not match or a sealed folder has changed. Do not edit a
delivered folder. Do not decide whether a rule is satisfied: the views say what the records say.
Python with -B only. No Git, no repository write, no web.
```

## 7. What I checked

SOURCE: every hash and time below is copied from tool output.

**The card.** `0037-design-text-r1.md`: `414d5c4d85f3d968b640553971ff9f5cd2344ba1cb06b88b071ce087a852b80e` at 2026-11-10 17:01:54, before reading it, and again at 17:21:29. It matches the message both times.

**The two addenda.** Both came as messages from Claude A's session while I was working, and I received both.
- Addendum 1, `0037-addendum-1-aot-and-jit.md`: `37b3613e340893a2215671abe20d6681223e4a78c4ff3cda5fbe9cabaaedff75` at 17:03:14 and at 17:21:29, matching the message. Its one input, the recovery ledger, draft 15: `9ad3c990e273f58a378a3831ad1ec9815e9b499bb45546d639e87db32021eb33` at 17:10:02 and at 17:21:29, matching the addendum. I read its lines 141, 183 and 412 and no others.
- Addendum 2, `0037-addendum-2-owner-answers.md`: `74e74ffe98526b795aba5a663403be964d9edf33fc0dda035263f384278dceee` at 17:17:10 and at 17:21:29, matching the message. Its two records are in the table of records below.

**AGENTS.md.** `baa162d13866b2f454d6499ee2c25d15a7a7ea7b92fb0e833829aaff2d3e6777` at the start, 17:01:54, and at the end, 17:21:29. It matches the card both times. Sections 2 to 6 were written before the second reading. After it I wrote section 1 and this section, and put a count and one sentence at the head of one table in section 4.

**The inputs.** Hashed at 17:02:09, before reading, and again at 17:21:29. All twelve match the card both times.

| Input | SHA-256 | Read |
| --- | --- | --- |
| Codex G's review, cited as G | `e9a44aa3a6508356873f1cb170a7e8693c1fc406a5aa105b5fad6b80d8aff5b6` | All |
| R35, the core revised | `477057b8097aba2b75f67dd6371e68eacbda0bd375f3019847269e227319de13` | All |
| Codex C's review of R35, cited as CR2 | `50c8da7f768790ed202a45f4fa4193509c3a2307ecc8947507dc0faf3c03e3cf` | All |
| Codex Q's review of the core tests | `d0dbc3ebe3b71d79e1f6ce3b5f962400aa2c5e6686881cb3c411bd36567353b5` | L1-L60 of 154: its verdict and its recount of tests 1 to 3. Not its sections on test 4 and the lock |
| R32, recovery | `786641cd245dc4021bee869ec950c6f680c1c831244ad102331d049e316cd012` | L1-L345 of 440: all but the end of its section for the owner and its checks |
| R34, lens 09 | `997b5b3462c524b296d745baf398eba6d0e2464aa7899e4ef83939c63b44d518` | All |
| R36, the optimizer | `1692f6459b89c20a3bbc3de8eef351f44740342a767db98e19d7b1b23590d6b0` | L1-L235 of 260: all but its checks |
| Codex O (Citations)'s check | `39e96248c4a40cdc7011872fb1e79b7559bc9b5a214d1ad9c202ed2d102e458b` | All |
| Codex S's store, reuse and stop tests | `d489a51077847c24a7fc911fb919c1a1a2ef9c6011f7e79058fe831ee38546c7` | All. None of its models or result files |
| Owner record: the optimizer may change the algorithm | `8270cf6ed1a7c1c5fb089d97769993db7364a8ecd5726a33e0def143bb23a183` | All |
| Owner record: names | `493f889986234f752ccf4d15470b95fdbe403b8c74856b1c8552a103326cb8f0` | All |
| Owner record: the SRE as shared infrastructure | `6c928eaae1654538a1807f319a1ca548d8e3a988aefc8f81fc6d8de90444607d` | All |

**Records from addendum 2,** hashed at 17:17:17 and at 17:21:29, matching the addendum both times.

| Record | SHA-256 |
| --- | --- |
| The two slice 1 choices | `d24eb6ad9e8177a727a5e0cf89aaef9fdfa4c914a269a2e3fe9ff74d9c5c5ec0` |
| Recovery to the web round; choices 1 and 4; concurrency | `cc900e601926ab2880016922a07edfb5d36f9010d4bba005f0cf7b70ff6c9e59` |

**The owner records, against the transcript.** For the five new records I hashed the raw bytes of the ten transcript lines they name, at 17:03:06 and 17:17:28. All ten match, and each holds the words its record quotes. I read no more of the transcript. What each record authorises I took from its `authorizes_only` field, read strictly. The two records from card 0033 I checked the same way then. One thing to know: the owner's line behind the record on the two slice 1 choices says "I will take your recommendations"; that those recommendations are the two answers is Claude A's reading in the record, which I did not check against the brief it names.

**Earlier inputs I rely on again.** The design and the corrections, read whole on card 0031 in this session. The first text as sealed, `d7ca342daeaeaff41b772444fad1a2bd230cc5d4d19bf5db40d1bc987a59fcc9`, hashed at 17:02:09 and 17:21:29: this file began as an exact copy of it.

**Checks on this file, by program.**
- At 17:21:06: 218 anchors are defined, none twice: 217 numbered passages and D-EVD. Against the first text, 39 are added and 2 retired. The only anchors named and not defined are the two retired ones. The four draft cards for Codex lanes hold none of the ten words the card rules out.
- At 17:21:42: comparing each passage with the same anchor in the sealed first text, 58 differ. One of the 58, D-RUN-10, differs only because a paragraph with no anchor now follows it. The other 57 are the 57 of section 4's table.
- The word "typed" occurs once, in the design's own phrase about other languages, and "type" once, inside the draft card that tells Codex D (Specs) not to use it.

**Checks by hand.** Each of G's eighteen fixes against G's words as I applied it. Each of Codex C's G1 to G5 against the passage that carries it. Each of L9-1 to L9-12 and doors 1 to 5 against its source. I did not go back through all 39 new passages a second time against their sources.

**Not checked.** Codex Q's review of the rewritten store rule: not an input, and D-EVD row 13 says so. My reports on cards 0026 and 0028, which hold the record of a look and the sentence K2: not inputs, and D-CONC-15 says so. Items 49 to 51 against their first texts, as before. The lines of Codex Q's, R32's and R36's reports that the table above says I did not read. No count, census or case in the text was run again by me.

**Not done.** No subagent. The card suggests one for checking that each fix landed and for the change table. I did both by program instead: the comparison above gives the change table's lists exactly, which a reader's summary would not. Whether each new passage says what its source says is a judgment, and it should be made by a reviewer who is not me. No web, Git, build, slot, test or message to any lane. I ran `Get-FileHash`, `Get-Date`, two loops that hash named transcript lines, one command that printed three lines of the ledger, and four read-only checks of this file. The only file written is this one, which replaced my 0033 text after that was sealed. ExitPlanMode was not called, as the card says.

END OF DESIGN-TEXT-R1-CLAUDE-ARCH
