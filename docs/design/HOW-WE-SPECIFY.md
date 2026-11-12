# How we specify: Claude Arch

## 1. Status

- Card 0031, all four parts done. The card and its eight inputs matched their hashes (section 6).
- My main findings:
  1. **The design already contains most of a specification method.** Its claim record, its row, its rule that evidence is kept and status is read, and its cache keyed by what a check asked are the links the outside research was asked to find. I propose we use those shapes for our own spec work now, in plain files, and not invent a second scheme.
  2. **A spec here has three kinds of binding item:** texts that define by being run, numbered rules that something else must satisfy, and declarations taken as true. Each rule names where it came from, and carries one deciding case.
  3. **E's proposals:** I accept 1, 3, 4, 5, 6 and 7 with changes, and accept the aim of 2 while rejecting its mechanism (hashes of marked spans of code).
  4. **Specification can't start on the design as it stands,** because the 48 corrections are all proposals and there is no single design text to cite. Section 5 lists that and eight more items, two of which are gaps I found that the design does not list.
- Nothing from the outside answer that failed Codex O (Citations)'s check is used. Where I use the answer at all, it is for mechanisms that can be read and tried without its sources.
- Labels: SOURCE gives a file and line. D is `DESIGN.md`, C is `CORRECTIONS.md` (C22 is its item 22), N is `ADR_NOTES.md`, E is Claude E's report, O is Codex O (Citations)'s report, G is the outside answer. INFERENCE is my reading. PROPOSED is my suggestion. What each lane does is INFERENCE from the name the card gives it; I have not read the lanes' briefs.

One author's view. Not reviewed or accepted; no owner decision.

## 2. What the specification is, for this design

### What the design already fixes

- SOURCE D L346: the reference run is a program for the evaluator; "This fixes what the reference does. The compiled program must agree with it".
- SOURCE D L375: seven program texts are trusted because "They define what a row, a use, a run, a clause, a reading of evidence and a derivation are, whatever runs them."
- SOURCE D L368, L548-L565: the evaluator is the only trusted machine code, built twice by independent means, and is given by a grammar, a list of primitives and a meter.
- SOURCE D L377-L378: the statements of section 2 are "trusted to say what is meant", and a build takes its declarations as true.
- SOURCE D L382: the elaborator, the planner, every proposer, the passes, the engine and the lab are not trusted.
- SOURCE C29 (L431-L437): each of the seven texts has one soundness claim, "which is what section 6 trusts that text for".

INFERENCE: so the usual picture, prose rules on one side and code that must conform on the other, fits only part of this design. For seven programs the text is the definition. For the evaluator nothing lies beneath it to define it. And for everything not trusted, the design says only what it submits and who checks it.

### Three kinds of binding item, and prose

PROPOSED. An item binds in one of three ways, told apart by what it means to conform.

| Kind | What conforms | Parts of the design |
|---|---|---|
| **Defining text.** A program in the evaluator's language | Only that text, by its hash | The seven kernel programs (D L375). Evaluated definitions of the standard theories (C7). Literal checks (C25). The machine theory's decoder (D L329) |
| **Numbered rule.** A statement that some named kind of subject must satisfy | Any subject with evidence for the statement | See the next table |
| **Declaration.** A theory a build takes as true | Nothing. It is trusted, and identified by content | The standard theories with their covering, use-once and multiplicity declarations, the machine model with the conditions it marks, the system-call model (D L378) |

| Part of the design | Becomes | Why |
|---|---|---|
| The evaluator: grammar, each primitive at its edges, the meter line by line, the hash, interning, fuel (D L548-L565; C8, C41) | Numbered rules, each with input and output vectors | No lower program defines it, and two builds must agree. D L833 sets the test: someone who wrote none of it builds the second from the text alone |
| Records, content identity, the lock, the cache key (D L591-L612, L359-L364, L295; C6, C25, C32, C37) | Numbered rules on formats | Replay and comparison between builds need agreement to the byte |
| What a compiled program owes: agreement with the reference run (C37), what each stage writes (D L323-L329), what the plain path promises (C27), the three claims binding text, graph and bytes (C38) | Numbered rules on every build and lowering | No text defines these. They are what a compiler must do |
| The clauses of the tracking claim (D section 2), the rules on claims (D section 3), Eval, Close and Reflect (D L580-L584) | Numbered rules whose text is a statement | D L377. They are already statements, and one day they are terms in the store |
| The reference run and the six other texts | Defining texts. Each also gets numbered rules saying what it is trusted for | D L375; C29. A text with no stated intent can be read and can't be reviewed |
| The planner, proposers, engine, lab and elaborator | Prose. Rules only on what they submit and who decides (D L505-L512) | D L382 |
| Reasons, alternatives, the seven places it may be wrong, the tests of open questions, measurements | Decision records and prose | SOURCE `docs/adr/README.md` L7-L13 keeps rule, rationale and evidence apart |
| Surface syntax | Nothing yet | Open: D L152 |

**Rule and text can disagree, and neither wins silently.** PROPOSED: for what a program's run observes, a build is compared with the reference run's text at its recorded hash, as D L346 has it. A rule that the text is found to break is a defect report against the trusted base. If mending it can alter any of the six things named under "a change needs rules and evidence" (what some program's run observes; what is admitted or refused; a row; a reading of evidence, and so a licence; a format or hash on which two builds or a replay must agree; the trusted base), the owner decides. The deciding cases are evidence for that question and never the whole of it: a mend that leaves every case where it was can still change the contract. Only where none of the six can change does the reviewer confirm, and the confirmation says why. INFERENCE: this keeps D L375 (the text defines) and still gives a reviewer something to hold the text against.

**Writing the defining texts is specification, not implementation.** INFERENCE from D L346 and L375: if the reference run is the definition, then until it is written the definition does not exist, and it can't be checked by reading alone. The specification phase therefore needs one evaluator able to run it. I state this as a dependency only.

### What a rule is

PROPOSED. One rule, one obligation. Shown on a real item:

```
rule      RUN-004        revision 1        standing: working, falls with C22
kind      requirement    subject: the reference run; through agreement, every lowering
from      DESIGN L346 as replaced by CORRECTIONS item 22, second bullet
text      An argument runs each time the operation that holds it runs. A variable stands
          for the value already bound to it, and using it runs nothing again.
case      pair(work(), work()), where work() makes one request: the run makes two requests.
excludes  one request (L346 as written: one node, one run for each activation)
```

- **ID.** An area and a number. It is never reused and carries no section number or position. SOURCE `docs/adr/001-specification-traceability.md` L14-L17: paths and section numbers are not durable identities. The new rules need a namespace apart from the pilot's 240 (N L11).
- **Revision and hash.** The ID names the rule through its changes. Each revision has a hash of its binding fields (kind, subject, text, case, excludes). Evidence cites the ID and that hash. A retired rule keeps its ID with what replaced it.
- **Kind.** Definition, requirement, or permission (what a planner or lowering may do, as in C4). A definition says what a word or a form denotes, and by itself nothing conforms to it or breaks it. A sentence that says what a build must do with the thing defined is a requirement, with the build as its subject; it is written as its own rule, or as a marked clause of one. A caution addressed to a reviewer or an author is neither: it goes in a note beside the rule and is no part of what is checked.
- **Subject.** The kind of thing that can conform: an evaluator build, a named text, a lowering, a writer of records, a build.
- **Case and excludes.** One concrete input with the outcome the rule requires, and the nearest wrong outcome it rules out. SOURCE: the corrections already work this way; C13, C18, C22 to C25, C31, C32, C34, C36, C37 and C42 each carry a labelled case. INFERENCE: a rule with no case that a plausible wrong subject would fail can't be tested and can't be put to the owner. The excluded outcome is also the fault to seed (section 4) and option B on the owner's card.
- **From.** Exactly one of four:
  - a design item, by the design text's hash and a stable anchor;
  - an owner decision, by its hash-bound record;
  - derived, naming the rules it follows from;
  - **gap**: the design does not say, and the specifier had to choose.
  
  A gap rule can't be approved until a design amendment or an owner decision gives it one of the other three. INFERENCE: the count of gap rules is the count of gaps someone has recorded, and no more. It depends on how finely gaps are cut and on what has been looked at, and it cannot count an omission nobody has found. A report gives it beside what was covered, what was out of scope and what is unknown. A smaller count alone is not evidence of readiness. D L832 reports that the trusted base "has grown each time a builder read it".
- **Standing.** Draft, working, approved, retired. Working is for a rule made from an item marked Open or TO BE TESTED. It names the test that settles it and what falls with it. SOURCE C L188-L190, L277: C22 is "the working rule", "not adopted", and "If a wrong term is accepted there, this item falls". The format has to hold a rule like that without pretending it is settled.

A rule never names code, a test or evidence. Those name the rule (section 3). A rule's own case is part of the rule and is written in it. A longer fixture that exercises the rule names the rule. If a rule cannot be read without a fixture, the fixture's deciding content belongs in the rule.

## 3. The links

### The design already has them

SOURCE for each row; that they line up is INFERENCE.

| What the research asks for | What the design has | Where |
|---|---|---|
| An evidence record | The claim record: statement, status, evidence, assumptions, row, settled, notes | D L253-L261 |
| The oracle a verdict rested on | The row of the evidence: the build, a decider or checker with what it assumes | D L84 |
| Stale evidence | A check is reused "only while every question still has the same answer", including the answer that nothing was there | D L295 |
| No status written by hand | "Evidence is never changed or removed. The status of a claim is a reading of its evidence" | C32 (L478-L480) |
| Two results that disagree | The reading is a conflict, which licenses nothing and shows both | C32 (L480-L483) |
| What a change affects | The query "what rests on a claim" | D L304 |
| A reviewer's opinion | A note. "A note is not evidence, and no licence can cite one" | D L261 |
| How strong the evidence is | Kinds are not ranks. Running cases gives "a yes for the enumerated set, by name" | D L276, L270 |
| What a checker's yes shows | That the checker returned yes. The statement needs the checker's soundness claim as well | C29 (L433-L437) |
| A waiver | A claim assumed by name, settled never, shown in the row and in the semantic part of the lock | D L275; C26, C28 |
| Code conforms to its meaning | Code is a name for its term, under a tracking claim | D L124; C38 (L602-L603) |

### E's proposal 1, where each fact lives: accept, with four changes

SOURCE E L137. PROPOSED changes:

1. **Authored links run one way, from the later thing to the earlier.** A rule names its origin. A test names the rules it exercises, in its own header. A marker in code names a rule. An evidence record names the rule, the subject and the check. Nothing names forward: a rule lists no code, test or evidence, and a decision record lists no rules. The pilot's decisions carry an authored `affected_rules` field (SOURCE `docs/architecture-decisions.toml` L148); that becomes a generated view, and a rule that waits on an open decision says so in its own `from`.
2. **Whether a subject satisfies a rule is never written by hand.** The outside answer's manifest has `"status": "verified"` as an authored field (SOURCE G L266). I reject that. A rule's standing is authored in the rule. Conformance is a reading, computed from the evidence records whose hashes match the current rule and the current subject.
3. **Evidence is not kept in one editable manifest.** Each evidence record is a file in a sealed package and is never edited, which is already our rule for delivered folders (SOURCE AGENTS.md, "Never edit a delivered folder") and the design's for evidence (C32). The manifest becomes a generated ledger. In the pilot the manifest holds the ID and points at the text by anchor (SOURCE `docs/requirements.toml` L5-L9), so an ID and its text live apart; the ID moves to sit with the text.
4. **A marker in code is for finding, and binds nothing.** SOURCE N L13, L23: a marker resolves by its token and "can resolve while attaching to the wrong item".

**The smallest trial that would show it wrong.** On paper, with no build: write ten of the evaluator's edge rules in the format of section 2 with their vectors. Then retitle one, split one, retire one, and reverse the decision behind one. List every edit made by hand and mark each as a judgment or a copy. Any copy fails the proposal. E's own bar, more than one edit each, is too strict for a split: each test that named the old rule has to be pointed at one half, and that is a judgment each time. The trial also fails if the reverse views can't be generated by a script written in a day, because one-way links are unusable without them, and the pilot's were intended and never built (SOURCE N L5; E L70).

### E's proposal 2, binding evidence to content: accept the aim, reject the mechanism

SOURCE E L138. The aim is already our rule for packages (SOURCE AGENTS.md, "changed bytes reopen evidence") and the design's for claims (D L293, L295). On the rule's side I accept it as E wrote it: a hash of the rule's binding fields in every evidence record.

On the code's side I reject hashes of marked spans, for now.

- SOURCE E L126: a span hash changes on every reformat and rename, and nobody has counted the noise. SOURCE O L195, L199, L201: the answer's figure for stale specs does not support this cure, its cost estimate is unvalidated, and its checker was never shown.
- INFERENCE: the right grain depends on what it costs to get the evidence again.

| Evidence | Binds to | Why |
|---|---|---|
| A run: vectors, or comparison with the reference run on generated inputs | The build that ran (D L257) | Cheap to repeat, so it is repeated on every build. Being stale is cured by running, and no span is needed |
| Anything about a defining text | The hash of the whole text | The texts are few and small, and a change to a trusted text should reopen everything about it |
| A review by reading | The exact files read, as packages bind them now | Costly to repeat. Recorded as a note, which is what the design calls it |
| A derivation | The statement as the prover elaborated it, and all it depends on | Section 4, proposal 7 |

- INFERENCE: for code that is Loom terms the design already has the exact answer. A defined symbol is identified by its content with binders nameless and names as metadata (D L66, L608), so a reformat or a rename changes no node, and C38 binds text, reader and graph by hash. Span hashes over host code would be a rough copy of that.

**The smallest trial that would show me wrong.** Read-only, on the existing repository's history. Take the pilot's 325 markers (SOURCE N L12) and the last 50 commits that touch `src/`. For each commit count the markers whose own item changed and the markers whose file changed. If binding by file flags several times more than binding by item, and a sample of the extra flags are edits that could not bear on the marked item, then reviews bound by file cost too much re-reading and spans earn their place. This is the old compiler's code, so the result is a guide and no more. E's half of the trial stands beside it: on ten rules, change one rule's text and see that only its evidence is flagged.

### E's proposal 4, what an evidence record names: accept, in the design's shape

SOURCE E L140. PROPOSED: the record is the design's claim record, filled for our own work.

```
statement    what was settled, with its scope:
             "RUN-004 rev 1 holds of the text step@<hash> on every term of this grammar to nine occurrences"
rule         ID and hash                  subject    its kind and hash
kind         run | derivation | counterexample      (a review is a note, filed with its method)
row          what the result leans on, each by hash: the check, the oracle and what the oracle
             was built from, the generator, the tools
controls     the wrong subjects this check was shown to refuse (section 4)
counts       for a run over generated or enumerated inputs: generated, admitted, reached, compared
transfer     where a model or a fixture was examined and not the rule's subject: the account that
             carries the result to that subject; or "none"
assumptions  what was used and not discharged
who          producer, reviewer
             (no status field: status is read)
```

Four fields go beyond E's list.

- **The statement, with its scope.** SOURCE D L251: "a claim never says more than its statement." Without this field, "evidence for rule R" always claims the whole rule. The record of C22's test is the model: it says what ran and then "Not covered: the whole language, handlers beyond small fixed cases, sort indices, and lowering" (C L267-L277).
- **What the oracle was built from:** the rule's text, a design item, another implementation, or the subject itself. INFERENCE: two programs written apart are not two readings written apart. Every lane reads the same rule, and no record can show a rule that all of them misread alike. What this field does catch is a test derived from the code it tests.
- **The four counts,** for a run over generated or enumerated inputs. Generated: the distinct inputs made. Admitted: those that passed every check standing before the thing under test. Reached: those whose run got as far as the thing under test. Compared: those whose outcome was set against the oracle's and given a verdict. Each count is at most the one before it. The statement's scope is the compared set and no larger one. For a comparison of agreement with the reference run, fuel exhaustion alone gives no verdict and does not count the input as compared. A mismatch already established by the completed prefix counts as a comparison for disagreement and is never erased by a later fuel cut; only the uncompleted remainder is inconclusive. A compared count of 0 has checked nothing, whatever the command returned. The record gives the main reason for the largest drop. A control is a run and gives its own four. A record of such a run without them reads in the ledger as ran, population not shown. This applies to records written from now on; an earlier record is not edited.
- **The transfer account.** Where what was examined is a model on paper, a model in another language or a finite fixture, and not the subject the rule names, the record's subject is that model, by hash, and its statement says so. The record then gives the account that carries the result to the named subject, or says `none`. An account names the subject by its kind, and by its hash once it exists; says which part of the model answers to which part of the subject; and puts every step it does not show among the record's assumptions. The account is not evidence of its own steps: a step counts only where a record of its own shows it. With `none`, the record is a result about the model: it can show a rule's text wrong or its case consistent, and it is no evidence that any subject conforms. With an account, the ledger shows the record under the named subject as a model result with its open assumptions, and never as a plain yes while one is open. A model that serves as the oracle for a real subject needs no account: the subject is what ran, and the model is in the row. This applies to records written from now on; an earlier record is not edited.

E's "two verdicts resting on one oracle count once" becomes: a reading counts distinct rows, not records.

**The smallest trial that would show it wrong.** Write these records for the three lanes' tests of C22 (C L264-L273: one lane's census, and another's recount "with its own program"). It fails if a field can't be filled from the packages as delivered, if the record loses something the HANDOFF says that a reader needs, or if two records with different rows turn out to share a source the row did not show. For this trial on packages delivered before the counts and transfer fields were required, record missing counts or transfer information as absent; their absence alone does not fail the trial or enlarge what the earlier evidence shows.

### How the links run

```
   design item or owner decision
              ^  from
            rule  <---- named by ---- test, marker in code
              ^                           ^
              +------ evidence record ----+----> subject, by hash (a text, a build, the files read)
```

- **Decision to rule.** The rule's `from` cites the decision record by hash. When a decision is replaced, a generated view lists the rules whose origin no longer stands, and they return to working.
- **Rule to code and tests.** Nothing is authored on the rule. Generated views list rules with no test, rules with no case, and tests that name a retired rule.
- **Evidence to all three.** The record names the rule and its hash, the subject and its hash, and the check in its row.
- **Generated, never edited:** reverse views, the stale list (records whose rule hash or subject hash is not the current one), and what rests on a rule.

PROPOSED, where they live: rules in the repository, since they are semantic (SOURCE AGENTS.md: Claude D "records semantic decisions ... in the repository"); evidence records inside sealed packages outside it (SOURCE AGENTS.md: evidence stays outside the repository); the ledger generated from both. Whether the new rules sit beside the pilot's manifest or apart from it is not decided here.

From the pilot I would keep stable IDs, the separation of decision, rule and evidence, and waivers with an owner and an end date. I would not keep three things. A marker that resolves is not coverage. `spec-check resolved` is a placeholder that returns success (SOURCE N L17), which is a check that can't fail. And all 240 requirements are `critical` (SOURCE N L11), so severity tells nothing apart.

### Could the design's own claims carry these links one day?

INFERENCE: yes. That a compiled program does what its term says is already a tracking claim (D L124; C38). The stale check is D L295 and the impact query is D L304. Once the compiler is written in Loom (D L487), a rule is a statement in the store, an evidence record is a claim, and the ledger is three store queries.

INFERENCE, what the design lacks for it: identity across versions of a theory is open (D L473, L608), and that is exactly a rule's revision; an owner's decision has no record in the store; and a review has no place but a note.

PROPOSED: allow for it now, with four things and no more.
1. Both ends of every link are content hashes, with the kind of hash stated.
2. An evidence record takes the claim record's fields and their meanings.
3. Evidence is never edited and status is never stored.
4. A rule may carry an optional formal statement beside its prose.

Rules are not written as Loom terms now: there is no syntax (D L152) and no store. The trial is the one for proposal 4. If the claim's shape can't hold a real review package, drop the alignment.

## 4. The workflow

All PROPOSED. Lanes are named as the card names them.

### Who writes and who reviews

| Step | Who | What leaves the step |
|---|---|---|
| 1. Turn an area of the design into a list of rules, each with its origin, case and excluded outcome. Mark every gap | Claude Arch, as lead specifier | The rule list and the gap list |
| 2. Write the rule text | The lead specifier for rules about meaning: the run, agreement, use-once, the tracking statements. Codex D (Specs) for formats and tables, from the list | Draft rules |
| 3. Hold each rule against its origin: does it say what the item says and no more, and does the case's outcome follow from the item? | Codex G (Spec Reviewer) | A review, or a finding |
| 4. From the rule's text alone, and without seeing any defining text: write the cases, a small model, and the excluded alternatives as runnable wrong subjects | Codex S (Rule Tester) | Vectors and controls |
| 5. Run every small case of a rule that speaks of all terms, as the design's reviewers did on 657,283 terms (D L52) | Codex Q (Model Checker) | A yes for a named finite set, or a counterexample |
| 6. Write each defining text from the approved rules alone. Every question the writer has to ask is logged as a gap | An author who did not write the rules. By AGENTS.md's roles that is Claude C | The text, and more gaps |
| 7. Review the text against the rules | Codex C (Core Reviewer) | A review, or a finding |
| 8. For each checker: its definition, its soundness statement, its damaged corpus (D L396; C29) | Codex R (Certificates) | What a named checker owes |
| 9. For the few rules worth a proof: the formal statement and the derivation | Codex N (Lean), reviewed with proposal 7's list by a lane that did not write it | A derivation with its row |
| 10. Keep the ledger: index the evidence records, compute the readings, the stale list and the coverage views | Codex V (Test Ledger) | Generated views |
| 11. Apply reviewed rule files to the repository | Claude D, as AGENTS.md has it | A commit |

INFERENCE: step 6 is the strongest check on the rules, and it is the design's own test for the trusted base (D L833): have someone who wrote none of it build from the text alone. Steps 4 and 6 are kept apart on purpose. The tester's oracle comes from the rule and the author's text comes from the rule, and neither sees the other's work, as with C22's test, run "each against a run written apart from the check" (C L264-L265).

### Where the owner decides

One question sorts it: **can a change alter any of the six things named under "a change needs rules and evidence", or does a new case need an outcome the design does not fix?** If yes, the owner decides. That gives:

- a gap rule whose choice some program could observe;
- two design items that give different outcomes on one case;
- a working rule becoming approved, or falling, once its test is in;
- every assumed rule (a waiver): for which subject, and until when;
- a change to an approved rule that moves a case;
- the line of proposal 6 itself.

Only where none of the six can change does Codex G (Spec Reviewer) confirm, saying why, and the owner is not asked. A gap whose resolution cannot change any of the six is the lead specifier's choice, reviewed, with a line of record.

### E's proposal 3, a reviewer's check shown able to fail: accept, changed

SOURCE E L139. The design has this twice already. A named checker owes a corpus of damaged certificates, because "Agreement on valid certificates shows nothing about a checker that accepts everything" (D L396). And the harness must refuse two wrong lowerings "by controls that drop a value and that use one twice" (C37, L589-L590). AGENTS.md asks for "meaningful negative and resource controls".

Changes:
- **The fault to seed is the rule's own excluded outcome,** made into a wrong subject. It is not a random edit to the code. The design's history supplies real ones: the old count (D L616), one run per node against one run per occurrence (C L264-L266), the start clause applied only after removal (C18, L170-L171).
- **No pass mark.** SOURCE O L197: the answer's 90% has no support as a bar for us.
- **The record says so.** Each run record lists its controls. A record with none reads in the ledger as ran, and not shown able to fail.

**The smallest trial that would show it wrong.** On the first area reviewed, take ten rules and build each one's excluded alternative. If the checks already written refuse all ten, that shows those ten rules' checks can fail. It does not show the step is redundant for other rules. The step may drop to a sample only under a stated policy: which rules are sampled, how often, and what finding restores the full step. A rule whose kind, area or check differs from the ten keeps the full step until its own alternative has been refused. If most alternatives can't be made to run, report that limit; it does not license dropping the step for other rules.

### E's proposal 5, the owner's one-page card: accept

SOURCE E L141. The card is the rule's deciding case: the input, what each option gives on it, which other rules and cases move with each option, what each costs, one recommendation, and what stays open either way. INFERENCE: this costs nothing extra once rules carry a case and an excluded outcome.

One limit. Some choices have no single input, such as the foundation (D L141-L148) and where the engine enters (D L497). Their card shows the test and what each result of the test would mean. I set no target for the owner's minutes: the answer's figures are unvalidated (SOURCE O L199).

**Trial:** E's. Recast two open choices in this form and ask the owner which form was quicker to decide from. I would use C22 against D L346, and where the engine enters.

### E's proposal 6, the threshold below which a change needs no spec: accept, with a derived line

SOURCE E L142. The outside answer draws the line at one or two files (G L477), on a benchmark whose figures do not carry over (O L196). The design has a line of its own. SOURCE D L361-L362: changing the semantic part of the lock "changes the program", and changing the operational part "changes nothing a client can see, apart from time, memory, and where the program runs out of a resource".

PROPOSED: a change needs rules and evidence when it can alter any of six things:
1. what some program's run observes;
2. what is admitted or refused;
3. a row;
4. a reading of evidence, and so a licence;
5. a format or hash on which two builds or a replay must agree;
6. the trusted base.

Anything else goes by test alone: how the planner and proposers search, costs inside the operational part, the wording of a message beyond what a rule requires of it, tooling. A placing that two lanes dispute goes above the line.

**The smallest trial that would show it wrong.** Two lanes each place the 48 corrections and a dozen imagined changes to the untrusted parts (D L382). If they disagree on more than a few, the line is not sharp enough to use.

### E's proposal 7, known ways to get a proof accepted without proving the claim: accept, and widen

SOURCE E L143. The answer's figures for how often this happens are unverified (O L74), and I use none of them. Its mechanisms can each be read and tried (E L129):
1. the definition proved is not the one that runs (G L170);
2. a local notation changes what an unedited statement means (G L172);
3. an axiom is added, or a hole is left;
4. a helper definition under the statement is changed (G L171);
5. the statement proved is not the rule's formal statement.

INFERENCE: the design's answer is the row. A derivation's row lists the laws it used and names the guest kernel (D L84, L141, L146). So a derivation's evidence record binds the statement as elaborated, everything it depends on, and the axioms used. The list is for whichever lane reviews Codex N (Lean)'s work.

PROPOSED, the widening: one short list for each kind of evidence, of how a yes says less than it seems. Ours so far, each from a source in front of me:
- a command that returns success having checked nothing (N L17);
- no test selected (AGENTS.md: "missing or zero selections fail");
- a run cut short by fuel read as agreement, or as erasing a mismatch already established by its completed prefix; only the part not yet compared is inconclusive;
- a checker that accepts everything (D L396; C29);
- a table fitted to answers, checked in place of the operation that gave them (C30);
- a damaged certificate that is still valid, counted as one that must be refused (C29, L442-L444);
- a generator whose inputs are mostly refused before the comparison runs; the record's four counts show it (section 3);
- a result on a model read as a result on the subject it models; the record's transfer account is the answer (section 3);
- INFERENCE: two builds made from one source.

**Trial:** E's. Seed each Lean trick once in a small file and see whether the review catches it.

## 5. Lead specifier

### What the role needs that the architect's did not

All PROPOSED.

1. **One design text to cite.** The architect wrote against line numbers of a text that kept moving. A rule's `from` needs anchors that do not move.
2. **A rule against designing inside the spec.** The architect fills a gap. The specifier records it and sends it back. Because I am also the amendment author, a gap I answered myself would be my own work approved by me, which AGENTS.md tells us to avoid. So the answer to a gap is reviewed by a lane that is not mine, or decided by the owner.
3. **State that outlives a session.** I have no memory between sessions (card, L5). The rule files, the gap list and the ledger have to be the whole state, so that a fresh session can go on from them alone.
4. **A way to run.** A specification made partly of running texts can't be led by reading. The role needs one evaluator and the texts on isolated scratch, which AGENTS.md already allows an assigned Claude for measurement.
5. **A short route to the owner:** the card of proposal 5.
6. **Say over standing.** The right to hold a rule at working, and to refuse approval to a gap rule.
7. **One written form for terms** in rules and cases.

### What I would hand off

- Adversarial review of the design: to Codex C (Core Reviewer) and the reviewing lanes. I should not specify an item and also be the reviewer of its design.
- Amendments to areas under specification: to another author, or mine with an independent review.
- Format rules, tables, and the tooling for views: to Codex D (Specs) and Codex V (Test Ledger).
- The defining texts and the second evaluator: to authors who work from the rules alone.
- Reading outside research: to Claude E and Codex D (Specs).

### Open design items that must be closed before specification can start

Items only. Items 1 and 2 stand under every rule. Items 3 to 9 stand under the rules for the evaluator, the store and the run, which every other rule cites.

1. **The corrections have no disposition, and there is no single design text.** SOURCE C L2: "Nothing here is adopted. The document's author has not seen this list." C L185: "Every item is PROPOSED and none is adopted." Needed: items A and 1 to 48 each adopted, changed or refused, and one text with stable anchors. This includes the passages that can't both stand: relation and symbol (C1), a predicate as a question (C2), a rule as an equation (C20), an assumed membership (C26, L381-L385), the exchange law of Open (C36), and the candidates query that returns nothing at the start (C28, L418-L420).
2. **Whether one node means one run: C22 against D L346.** A working rule by the owner's decision and "not adopted" (C L188-L190), with one lane's review of most of its test "not in" (C L273). The reference run, the use-once count, the state record and agreement each take their form from it (C37, L575-L576).
3. **The evaluator's unstated parts.** The hash is "one named function" with no name (D L558). The edges are "Proposed" (D L556). The meter's table, one line for each primitive, "is part of the evaluator's specification" and is not written (C41, L626). What compare, divmod and same return, and how a value is built from computed parts (D L574-L576; C8).
4. **The bytes that content identity hashes.** INFERENCE, a gap I found and not one the design lists: D L591-L612 identifies nodes, symbols and theories by content and gives no encoding. Only the hash of rules that name themselves is proposed (D L612).
5. **The records still owed.** The signature (C6; C25). The evaluated symbol (C7). The state and outcome of the reference run, "to be given with slice 1" (D L609) and with shapes still to be tested (C37, L566-L567). How a value of a data sort crosses the evaluator's edge (C25, L341).
6. **Outcomes the design names and does not state.** The payload of the failure where no rule matches, "a failure with a stated payload" (C27, L405). The default bound (D L355; C35, L544).
7. **The host boundary.** What a request is, what a host's theory reports, and how a reply is admitted (D L229, L610; C37, L573-L574). The system-call model is trusted (D L378) and has no content yet.
8. **Quotation.** Whether a term handed to an operation is seen as written or as its value. The mark is owed and its written form is untested (C21, L202-L203).
9. **A written form for terms in rules and cases, with its reading as nodes.** INFERENCE, a gap I found: the surface syntax is open (D L152), and every case in every rule needs one.

**Open, and able to wait.** INFERENCE: the design marks each of these Open with a test, and a working rule can carry it. The use-once check on the whole language (D L459). The two theorems (D L460-L462). The clauses for effects (D L228-L232; C15, C16). The backward form's open points (C12, C24, C47). Where a tracker must be defined (C17). Whether an interpretation and a record are one thing (D L70). Whether tracking evidence is affordable (D L466). The foundation (D L141-L148; C48). The core for rule 9, which "cannot be judged before then" (C46, L673-L674). Identity across versions, which has a default (D L608). The roles of row entries (C35). The surface syntax for everything but the reader of text. Where the engine enters (D L497). Search at size, the payoff, and guarantees in probability (D L470-L474).

## 6. What I checked

SOURCE: every hash and time below is copied from tool output.

**The card.** `0031-how-we-specify.md`: `9d5c8675e7f98f8bc7c0493943463c0793f1547ce6a95142647c981b2d17e86f`, matching the message, before acting and again at the end.

| Input | SHA-256, as computed | Card | Read |
|---|---|---|---|
| `ADR_NOTES.md` | `8cb23e466ad2c5d6f056e82a83461b0feef38021779a034abf7b5250a5396fa0` | match | All |
| `PROMPT.md` | `1d2e801dbfe87201eadb2f72cfdc16af750988fc376a425a08e6359eeaaa858c` | match | All |
| `CONTEXT.md` | `4eb9cf2b7ac6467686b0d8035bbc079a80dcf2fe66547e89b837c6504ffb46e0` | match | All |
| `sdd-gem-dr.txt` | `873de82e8a07452cfdb1af70920e9a107c60c905f53271f4c865217d9075a951` | match | In part: L1-L6, L160-L319, L424-L494. For the rest I relied on E's and O's readings |
| Claude E's `REPORT.md` | `eb4e5313ef9046778a5e4d4ba98a2f747d263ec725f506a228d524402344cf04` | match | All |
| Codex O (Citations)'s `REPORT.md` | `9e0be2a8adcf03e98c34609a252303a0c5dd5295256fe675bcad9b5da8450c2b` | match | All |
| `DESIGN.md` | `4fba31c09ed80f0cdf1b2823bf96d834aeeadafd08fb2ffe5a9c6768c1b14f24` | match | All, L1-L857 |
| `CORRECTIONS.md` | `f6997713573a51695edafd2a0fad6511a7d38773751dadc39e5843bf345b672d` | match | All, items A and 1 to 48 |

**AGENTS.md.** At the start: `baa162d13866b2f454d6499ee2c25d15a7a7ea7b92fb0e833829aaff2d3e6777` at 2026-11-10 15:50:26, the card's value. At the end: the same value at 2026-11-10 15:59:15. Sections 1 to 5 were written before the second reading. After it I wrote this section and made four small wording fixes: the list of corrections that carry a labelled case in section 2, the count of items in section 1, and "written by hand" for "typed" twice in section 3.

**Repository, read-only.** The pilot's files as they stand in the working tree at `C:\Users\grego\Loom-release-repair`, not checked against Codex D (Specs)'s bindings: `docs/adr/001-specification-traceability.md` (all), `docs/adr/README.md` (all), `docs/requirements.toml` L1-L40, `docs/architecture-decisions.toml` L134-L183. I did not open `tools/xtask/src/main.rs`; what I say of the checker rests on N.

**Line references.** I checked each quoted passage against the line I cite while writing. A reference to a whole correction (C7, C25) is to the item and not to a line.

**Not checked.** No web, so no published source. The owner's decision of 2026-11-10 on C22 is cited from C L188-L190 only; I did not verify its hash-bound record and act on nothing because of it. What each Codex lane does is read from its name on the card. No trial proposed here has been run.

**Not done.** No subagent: the reading did not split in a way that would have saved judgment. No Git, build, slot, test or message. I ran `Get-FileHash`, `Get-Date`, line counts, and `bb.py show --open` once (one open entry, unrelated to this card). The only file written is this one. ExitPlanMode was not called, as the card says.

END OF HOW-WE-SPECIFY-CLAUDE-ARCH
