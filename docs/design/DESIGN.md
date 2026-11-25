# Loom language and compiler design

<a id="ch-0"></a>

## 0. Reading guide

### 0.1 What this document is

A program, a theorem and a compiled artefact are terms in one store. A claim about any of them has a scope, a status, evidence and dependencies (§1.1). A program can admit several right answers. A compiler that selects one must account for the run that produced it, including outside requests, any value held on failure, and any resource stop. Every admitted runnable definition has a plain execution path. A faster path needs evidence that its replacement is valid at the use site (§§8–11).

### 0.2 Standing tags

Read each tag with the statement, rule or table immediately before it. A qualification can restrict the scope, timing or strength of a decision.

| Tag | Meaning |
|---|---|
| `[decided]` | Settled for the design as it stands. A decision may be provisional, concern only a direction, or still await a test. |
| `[proposed]` | A candidate rule, condition or formulation awaiting adoption in the scope stated. Where an alternative is on record it is given beside the proposal. |
| `[proposed: working rule]` | A provisional rule at its stated scope. Its test may be owed, unnamed, already run within a bound, or a prerequisite to reliance. §23.1 gives the test and fallback. |
| `[open]` | Not settled. An outstanding choice and an outstanding test have different consequences. §24 indexes design questions separately from checks still owed on rules with their own standing. |
| `[built: milestone B, partial]` | Implemented in the partial first build (§0.4). It follows the item's standing tag and does not change it. |

Evidence is stated beside a tag in plain words, for example "checked on two finite models" or "read, not run". A finite check establishes the cases it covers and no more (§23.2).

A worked example that begins "Case:" belongs to the design and has the standing its tag gives. One that begins "Illustration:" is added here to make a rule or a figure checkable; so is a line that restates a rule in symbols after its tag. Neither adds to the design nor carries a standing.

“The project owner” identifies who settles a question where the design assigns it to that person. An item can instead name a delegated decision or require concurrence. The word "owner" alone is used of values: the owner of a cell, of a queue, of a scope.

### 0.3 Names

- **SRE** stands for Structural Representation Explorer (§20).
- **SkeinLab** is the lab, a client of the SRE. It seeks mathematical signals and connections for hard problems. A fit can have value in its own right. `[decided]`
- **The optimizer** is the compiler's optional optimization paths (§20.1). The SRE serves both clients. One way the optimizer may optimize is to compute an already defined answer more cheaply. Any claim of a cost advantage needs a workload and a comparison. `[decided]`
- **Facets.** The design retains five views used to describe a term (§1.59). `[decided]` The proposed account distinguishes meaning, effects, usage, representation and evidence. Their checks can depend on one another. `[proposed]`
- **The backend.** For now, generated C is the route to qualify for the first compiled demonstration. `[decided]` For the long-term native Windows x64 checked path, prefer a simple emitter from the checked low-level form (§10.5). Require independent per-build validation of the final executable bytes against that form, under explicit machine, loader, ABI, runtime and resource contracts. An alternative producer may satisfy the same check. Claim only the covered form-to-machine step. The targets come in this order: x86-64 first, Arm next on the same scheme, and GPUs later, for bounded kernels only. `[decided]` Return the choice to the project owner if qualification of the C route fails at a stage, if a build during a run in slice 2 proves too costly under C, or when the second target of slice 5 is planned. Revisit the producer choice if a restricted existing backend meets the same contract at lower total cost, or if the checker or runtime boundary cannot be kept reviewable. `[decided]`

### 0.4 What is built

The partial first build (milestone B) is a reader, a checker, an evaluator with a fuel meter and a file driver. It reads and checks first-order definitions whose expressions are natural literals, a reference to the definition's parameter, tuple construction, calls of named definitions and the three natural primitives `add`, `sub` and `mul`. It has exact naturals, interned immutable values, a meter that works out and pays each charge before the event, and left-to-right evaluation once per written occurrence. It distinguishes a returned value, execution-fuel exhaustion, a refusal before execution and a host or tool fault. Its development prices are provisional. See §15 for the abstract accounting and the concrete implementation profile. `[built: milestone B, partial]` The full comparison with compiled programs in slice 1 remains due (§19).

### 0.5 Notation

Mathematics is written in LaTeX notation. Program text, grammars and concrete syntax are in code font; the concrete syntax shown is illustrative unless an item says it is fixed. Inference rules are written with premises over a conclusion and a name in parentheses. Substitution is $t[x := u]$.

| Symbol | Meaning |
|---|---|
| $\mathbb{N}$ | the natural numbers from 0 |
| $\mathsf{yes}, \mathsf{no}, \mathsf{unknown}, \mathsf{conflict}$ | the four possible readings of a claim at a site (§4.2). Each individual checker has the result set specified for that checker |
| $T, T'$ | theories; $T = (\mathcal{S}, \mathcal{O}, \mathcal{L}, \mathcal{R})$: sorts, operation symbols, laws, rules |
| $A, B, C$ | sorts; $S$ a hidden sort, $N$ its sort of names, $O$ an observed sort |
| $f, g, h$ | operation symbols; $c$ a constructor; $f : A_1 \times \dots \times A_k \to B$ |
| $m \in \{\mathbf{1}, \boldsymbol{\omega}\}$ | the multiplicity of a bound argument: one, any |
| $t, u, s$ | terms; $p$ a pattern; $x, y, z$ variables |
| $v, w$ | values |
| $\varphi, \psi$ | statements; $\mathsf{St}_{\ell}$ the statement sort of a logic $\ell$ |
| $\iota : T \to T'$ | an interpretation |
| $\kappa$ | a claim |
| $\mathcal{M}(t)$ | the manifest of a term |
| $\rho$ | a representation; $\mathrm{names}(n, v)$: the name $n$ stands for the value $v$; $\tilde f$ the tracker of $f$ |
| $\mathrm{Runs}(t)$, $\mathrm{Out}(t)$ | the runs and the outcomes that the meaning of $t$ allows; $\mathrm{obs}(r)$ the ordered observations of a run $r$ |
| $e$ | an expression of the evaluator's language; $\eta$ an environment |
| $k$ | the allowance passed to $\mathrm{eval}(k,f,v)$. In the paired profile $k=(W,C)$, remaining reference work and cumulative construction credit. The historical milestone B profile takes one natural. |
| $\sigma$ | the state of the changing sequences; $\tau$ a trail |
| $\pi$ | a plan: what the planner selected |
| $\mathrm{bits}(n)$ | the bit length of a natural |
| $\langle v_1, \dots, v_k \rangle$ | a tuple; in program text `tuple(v1, .., vk)` |

These conventions apply across sections. Variables bound by a formula and abbreviations local to one example have their scope and meaning there.

### 0.6 Layout

**Part I. What is said and what is known**

- [§1 The constructs](#ch-1)
- [§2 The records](#ch-2)
- [§3 The tracking claim](#ch-3)
- [§4 Claims](#ch-4)
- [§5 The store and its queries](#ch-5)

**Part II. From text to runs**

- [§6 The stages](#ch-6)
- [§7 Admission](#ch-7)
- [§8 Order of evaluation and the reference run](#ch-8)
- [§9 The concurrency core](#ch-9)
- [§10 The path that always runs](#ch-10)
- [§11 Selection and the lock](#ch-11)
- [§12 Building ahead of time and during a run](#ch-12)

**Part III. Trust and proof**

- [§13 The trusted base](#ch-13)
- [§14 What is proved: the two theorems](#ch-14)

**Part IV. The evaluator**

- [§15 The evaluator](#ch-15)
- [§16 Values, choices and sets](#ch-16)
- [§17 Changing sequences](#ch-17)
- [§18 The trail a run leaves](#ch-18)

**Part V. The plan, the explorer and the optimizer**

- [§19 The first five slices](#ch-19)
- [§20 The SRE, SkeinLab and the optimizer](#ch-20)

**Part VI. Open matters and evidence**

- [§21 Open questions on identity, binding and ownership](#ch-21)
- [§22 Further proposals and open questions](#ch-22)
- [§23 Working rules and what the finite checks establish](#ch-23)
- §24 Index · [Open questions](#open-questions) · [Tests owed](#tests-owed)

# Part I. What is said and what is known

<a id="ch-1"></a>

## 1. The constructs

**§1.1 Store.** A program, a theorem and a compiled artefact are terms in one store; every fact about them is a claim $\kappa = (\varphi, \mathit{scope}, \mathit{status}, \mathit{evidence}, \mathit{deps})$, $\mathit{deps}$ being what it rests on. Here status is a reading at a site (§4.2), not an independently stored field. The seven constructs in order are theory, term, interpretation, manifest, open choice with its resolver, representation and claim. The first four describe what is said and the last three describe what is known about it. `[decided]`

### Theory

**§1.2 Theory.** A theory $T = (\mathcal{S}, \mathcal{O}, \mathcal{L}, \mathcal{R})$ is a vocabulary of sorts, operations, laws (statements $T$ asserts) and ordered rules. Relations sit in $\mathcal{O}$: a symbol giving one has a statement result and is declared as an operation or defined by a formula (§1.9). The integers, a mutable store, a logic, an instruction set and a file format are all theories. `[decided]`

**§1.3 Sort parameters.** A sort may be indexed by terms, as in a vector of length $n$. `[decided]` For the paper design and one review, the project owner chose that a reusable declaration names, in order, the sorts it takes. Milestone B keeps its existing scope. `[decided]` A reusable sort or operation signature may bind sort parameters. An application supplies one sort per sort place, separately from its term-index places. In `Vec<A;n>`, `A` is a sort and `n` a term. A field or result may use an enclosing sort parameter. Refuse a missing, extra or wrong-category argument. Two sorts given to `Vec` have the right count but put a sort in a term place. `[proposed]` For now the first build accepts plain indices only. An index may depend on earlier arguments, has no effect or open choice, makes or uses up no sequence or use-once value, and gives a result that may be copied. `[decided]` When, how often and at what cost an index runs remain open (§7.14). `[open]`

**§1.4 Multiplicity.** An operation may bind variables:

$$f : P_1 \times \dots \times P_k \to B, \quad P ::= A \mid (A_1, \dots, A_j \Rightarrow B')^{m}, \quad m \in \{\mathbf{1}, \boldsymbol{\omega}\}.$$

The multiplicity $m$ ("one", "any") of a bound argument $b$ is how many times the operation calls it. `[proposed]` The signature must state it; one that states none is refused, with no default: a default would change which programs pass the use-once check without changing the line a reader sees (the reason of §1.7). `[proposed]` $m$ counts calls in a run, not places in the text. $\boldsymbol{\omega}$ permits any number of calls, including zero. $\mathbf{1}$: a duty to call $b$ once. No run calls $b$ twice. A returning scope has called it once, or passed the duty on at a permitted parameter declared $\mathbf{1}$ (§1.16, §1.22), which neither erases the duty nor permits a second call. A run that does not end may keep $b$ uncalled for ever. A failed or stopped run keeps every outstanding duty and names the held values in its outcome (§1.23). None of this needs a proof that the run ends. The check on sites that keeps it (§1.14, §1.16) is sufficient and refuses some right terms (§1.32). `[proposed]` Open: may a bound argument bind no variable ($j = 0$)? It is an open point of the record rules. `[open]` Open: is a third value, none, for a parameter never called, added? It goes to test (§1.32). `[open]`

**§1.5 Rule.** A rule is a step of the reference run. Rule $i$ of $f$, $f(\vec p_i) \to u_i$ with variables $\vec x_i$, applies only to arguments that are values and that no earlier rule of $f$ matches. Write $f_{\rm ready}(\vec v)$ for the call state after all attached membership guards pass in parameter order and then all attached condition tests pass in listed order on those values (§7.6, §7.9). The enclosing run retains their work and observations. A guard that fails, stops or never finishes does not enter this state. The rule describes the remaining run ($\simeq$):

$$\frac{\vec v\text{ values}\quad \mathrm{match}(\vec p_i,\vec v) = \theta\quad\forall j<i.\ \mathrm{match}(\vec p_j,\vec v)\text{ fails}}{f_{\rm ready}(\vec v)\simeq u_i[\theta]}$$

At a term not yet a value a rule is used only where §8.6 lets the planner move, share or drop that term. Putting a body in place of a call keeps each argument bound: arguments run in the reference order and the body sees their values; a binding is removed only as §8.6 allows for its term. Derivations, and $\mathsf{yes}$ by computation (§14.8), use rules in this reading only. Case: `f(0) = 0`, `f(x) = 1` read with no condition give `0 = 1`; `discard(x) = unit` makes `discard(loop())` return where its run never does. `[decided]` Read rightly, the second rule of `f` has no instance at 0, and `discard(loop())` runs its argument, which never returns.

**§1.6 Effect.** An effect is an operation whose last argument is a bound continuation, so order is written into the term. Its multiplicity is owed by every interpretation of the effect: a handler is a rule, and clause (b) (§1.14) counts the continuation in it. `[proposed]` After the reader of text an effect stands with its continuation last, and no argument place of a call holds an effect directly: the reader has turned such text into continuations, left to right (§6.1). A pattern holds none, being built of constructors and variables (§8.2). A defined symbol whose rules perform an effect may stand wherever a term may, argument places included: the effect is in its manifest (§1.43), the definition is checked against its declared manifest bound (§1.46), and the effect happens when that argument runs, left to right (§8.2). So two such calls side by side make their requests in the order written, and no build chooses. Keeping effects to the tail of a rule, or helpers free of effects, would be an amendment and is not proposed. `[proposed]`

Where an effect stays in the manifest and the host answers it, nothing in the term can be counted and the declared multiplicity decides (§3.13). That the host keeps it is part of the system-call model, which with the multiplicity declarations is among the declarations a build takes as true (§13.2). Slice 1 has only this host case. `[proposed]` Its output sends bytes and the host replies “done” carrying nothing. `[decided]` One request takes one admitted reply (§8.9). That fixes the first output direction; it neither qualifies the host model nor gives the concrete interface and encoding. From slice 2 an image that is a term keeps the multiplicity by the rules it is applied through (§1.40), checked as here. No interpretation and no host is exempt. `[proposed]`

**§1.7 Sort declarations.** A sort may carry any of `finite(values)`, `data(constructors)`, `use-once`; use-once, $\mathrm{uo}(A)$, means $T$ has no law to copy or to drop values of $A$. A data sort with a constructor taking a use-once argument must be declared use-once: `[proposed]`

$$\frac{A \text{ data} \quad c : \dots \times A_i \times \dots \to A \quad \mathrm{uo}(A_i) \quad \neg\,\mathrm{uo}(A)}{\text{declaration of } A \text{ refused, naming field } i}\ \textsf{(A-Data)}$$

If the declaration omits the mark, refuse it and name the field. Not taken: making such a sort use-once silently; that too keeps a use-once value contained, but a change to one field would change which client programs are legal without changing the line clients read. `[decided]` §1.28 keeps one mark now, two as the direction. Case: boxes not use-once, rule `finish(Box(h), tag) = read(h)`, `b` bound to `Box(x)`, term `pair(finish(b, 0), finish(b, 1))`: without $\textsf{(A-Data)}$ every clause passes and the run reads `x` twice. `[proposed]`

### Statements, relations and predicates

**§1.8 Statement.** A statement $\varphi$ is a term of the statement sort $\mathsf{St}_{\ell}$ of a logic $\ell$; a logic is a theory. `[decided]`

**§1.9 Relation.** A relation is a set of pairs, as in mathematics, and may relate more than two sorts. $R$, with $R(x, y)$ a statement, gives $\{(x, y) \mid R(x, y)\}$ (over sorts $S_1, \dots, S_k$: $\{(x_1, \dots, x_k) \in S_1 \times \dots \times S_k \mid R(x_1, \dots, x_k)\}$), and is declared as any operation or defined by a formula. $R_1, R_2$ giving one relation are two nodes; that the relations are equal is a claim, $\forall x, y.\ R_1(x, y) \leftrightarrow R_2(x, y)$. A predicate is a relation in one argument and gives a set likewise; two predicates may give one set. `[proposed]`

**§1.10 Set, statement.** Converse, composition, union and the fibres of a representation's relation are read on the set; a tracking claim or a law on the statements. $R(x, y)$ is a statement, not a computed truth value; whether it can be decided is a claim. `[decided]`

**§1.11 No "property".** Nothing in the design has that name. What mathematics calls so is: of an element, a predicate; of a structure, a law at an interpretation (a claim) or a predicate on interpretations; for data unique when it exists, such as a unit element, either an operation with laws or a statement that one exists, the choice deciding what an interpretation must preserve and what a client can reach. `[decided]` What the Structural Representation Explorer asks of an object is a question: an operation from the object's sort to a sort the client can read. A predicate decided at each object gives a question with answers $\mathsf{yes}$, $\mathsf{no}$; an undecided one is no question, and what is known of it at an object is a claim. `[proposed]`

### The use-once check

**§1.12 Scopes, values.** The check runs on every use-once value, scope by scope. A scope $D$: the body of a binder, the right-hand side of a rule, or a whole term. A use-once value $a$: a bound or pattern variable of a use-once sort, or a node of a use-once sort (the result of an operation returning one, or a function made by clause (c)). `[decided]` The body of a core let is no scope: it belongs to the scope the let stands in (§21.3, §21.5). `[decided]` A use-once function is a use-once value however it arises (the three ways of §9.3): made by clause (c); a pattern variable standing for a bound argument of multiplicity $\mathbf{1}$ (§1.14); a continuation holding use-once state (§3.12). So a binder whose body has a site of a use-once function bound outside it is a binder of clause (c), refused by the narrower rule (§1.30). `[proposed]`

**§1.13 Clause (a).** A site of $a$ in $D$ is an occurrence: an argument position reached along one path from the root of $D$; a node reached along two paths gives each of its sites twice. Sites are never gathered across two binders. With $\#_D(a) \in \{0, 1, {\ge}2\}$ the number of sites (three answers suffice), the scope $D$ that makes $a$ must have $\#_D(a) = 1$: exactly one consuming site. `[proposed: working rule]` A consuming site here is any site: occurrences are counted, not whether the run consumes the value there or only moves it (§21.7). `[proposed]` Case: `g(d, d)`, `d = read(x)`: the node `read(x)` holds `x` at one position and runs twice, so `x` has two sites. `[proposed: working rule]`

**§1.14 Clause (b).** Each rule $f(\vec p) \to u$ is a scope: a pattern variable $x$ of a use-once sort has $\#_u(x) = 1$. So a case analysis on a use-once value is written as rules taking it as an argument. `[decided]` A pattern variable standing for a bound argument of multiplicity $\mathbf{1}$ is a use-once function in its rule, with exactly one site, placed as clause (d) allows; so too in slice 1, beside the narrower rule. Case: `relay(h) = twice(h)`, `h` declared called once: without this it passes and its run calls `h` twice. `[decided]` One step removed: `relay(g) = twice(y -> g(y))`, `g` declared called once. The binder's body has a site of `g`, bound outside, so by §1.12 it is a binder of clause (c): the narrower rule refuses it (§1.30), and under the full check it is a use-once function that may not stand at a parameter its taker calls twice (clause (d)). Ignoring this capture would admit the rule and let its run call `g` twice. `[proposed]`

**§1.15 Clause (c).** A binder makes a use-once function when its body $t$ consumes a use-once variable $x$ bound outside it. Making it is the one site of $x$ outside; inside, $\#_t(x) = 1$. `[proposed: working rule]` Here and in §1.30 "consumes" means has a site ($\#_t(x) \ne 0$), as in §1.13: occurrences, not what the run does. `[proposed]`

**§1.16 Clause (d).** A use-once function may stand only where its taker calls it exactly once: as the function of an application, or as a bound argument declared $\mathbf{1}$. `[decided]`

**§1.17 Clause (e).** Every rule step and lowering keeps $\mathrm{obs}(r)$, the run's observations in order, and what the run consumes of each use-once value; changing either needs a claim licensing that change at that place (§1.5, §1.53). A value is copied only where its sort has a law to copy it. `[proposed: working rule]`

**§1.18 Result, failure.** Handing on a scope's result is one site. `[decided]` Performing a failure hands on what its scope still holds: in a scope whose last operation is a failure, a use-once value with no other site has that failure as its site. `[decided]` This and §1.19 say what a site and a value are for clause (a), under the narrower rule (§1.30) as under the full one; the place of a scope's result is a site though no argument position. `[proposed]`

**§1.19 New values.** An operation with no arguments runs at each occurrence like any other. Each run of a constructor of a data sort declared use-once makes a new value, whatever its content, as does each run of a closed operation with no rules that returns one (the later shape of that case is open, §21.7). An operation defined by rules hands on the value its right-hand side gave, for the cases decided at §21.7 (returning, passing along, or putting a use-once value inside data moves the same value; taking data apart uses up the data and hands on its fields). So a use-once constant written at two places is two values, and one fixed value, such as a handle the host holds, enters a term only as a variable. Case: with `f(b) = read_in(K, b)`, each call in `pair(f(false), f(true))` makes its own `K`; and `pair(read(x), (y -> read(k))(read(k)))` is a right term, not a wrong one. `[proposed: working rule]` In the check a use-once value that is an operation's result is an occurrence of its node: one node reached along two paths is two values, each with the one site it stands at; a variable reached along two paths is one value with two sites (§1.13; counted by path in §23.2 row 4). `[proposed]`

**§1.20 Manifest.** A term that consumes a use-once value adds no entry to its manifest $\mathcal{M}(t)$ by that fact, and may still not be dropped or run twice. The check is a fact about the term as stated under the reference run. `[decided]`

**§1.21 Context, cost.** A node $t$ holding variables is checked in a context $\Gamma$: each variable's sort and its use-once standing there, the standing being the multiplicity a bound parameter declares for its variable, or the use-once reading under which a parameter is checked again (§3.12). A pass under one standing never discharges a check under another. `[proposed]` A cache of the check is keyed by $(t, \Gamma)$, for sort membership as for use-once. `[proposed]` For one use-once value, counting on the shared graph with the count capped at two visits each node once; the whole check is not shown to be one visit per node. `[proposed: working rule]`

**§1.22 Guarantee.** No run consumes a use-once value twice. `[proposed]` A run that returns has consumed each such value or handed it on. `[decided]` An endless run may hold one for ever: `spin(h) = spin(h)` passes every clause without consuming `h`. Eventual consumption requires a separate termination claim. `[proposed]`

**§1.23 Stops.** A run stops without returning in three ways: a failure nothing answers, a stop for a resource, running out of fuel. A stop is no drop: the stopped run holds every use-once value it had not consumed, as an endless run does, and its outcome names them. What the check promises of a run that returns it does not promise of one that stops. `[decided]` The possible failure is in the manifest (§7.6, §10.1), and a bound may refuse it. `[proposed]` Case, full check: `pair(fail(e), read(x))` passes every clause and its run ends in a failure with `x` never consumed. Slice 1 has no explicit failing operation to write; §10.1 and §7.6 specify its unmatched-call and membership-guard failures, and the evaluated result-check and literal-check outcomes left open in §7.7 stay open. `[proposed]`

**§1.24 After a failure.** Going on after a failure is where a value could be lost; there the check decides. A failing operation that takes an answer is answered like any operation: its rule may run the continuation once, with a value in place of the one that failed, and nothing is lost. A failure that takes no answer has a continuation $K$ that can never be run, which the answering rule receives. $K$ holds a value that may not be dropped when an environment in it, a frame in it waiting with an argument already obtained, or handler state it captured holds a live one. The rule may not leave such a $K$ unused and return. `[proposed]`

**§1.25 Outcome B, chosen for now: no take.** A catcher may not reach into a failed part and take back what it held. It may go on (its rule return) only where the failed part held nothing that may not be dropped, or handed back what it held openly in its result, every caller's obligations still owed; otherwise the failure carries on, the values retained and named in the outcome. What must survive a failure may be kept by an owner outside the part that may fail. A rule answering a failure may always fail in its turn; a stop holds what it held (§1.23). Slice 1 has no handlers, so nothing there waits on this. Bring outcome A to the project owner at any of these triggers: (1) the declared-residue test on its frozen fixtures refuses an eligible positive encoding under the present check, accepts a control with an independently supported wrong account, or needs a new operation in the reference run (report unresolved and unrun tests to the project coordinator; neither alone triggers A); (2) real programs show unplanned failures while holding live values to be common; (3) before any rule letting a catcher return after a failed part held a live value is drafted (handlers arrive in slice 2); (4) at the latest, at slice 2's review. Evidence: the test has run and its partial, finite author evidence was independently reviewed as sound; for those frozen encodings and declared premises no new operation in the reference run was needed and (1) has not fired. Two callback probes remain unresolved; how often real programs meet the unrecovered failure is unmeasured; the general translation is not checked (for now). `[decided]`

**§1.26 Declared residue.** A way to write recovery under B, with no take and no reaching into a continuation. A part that can fail declares in its result what it hands back: it returns its result, or a failure with a payload and a residue, which is ordinary owned data holding what survives. Every caller the failure passes must finish, hand on, or add to its own residue whatever it still owes; turning the failure into a value is not enough. To refuse: a `bind` that passes a failure on and gives the success callback no site. What comes back is what survives now, not an earlier state; returning to an earlier state is going back to a kept point (§18.2, §18.3). A failure with no declared exit propagates, or stops, with its surviving values held. The cases shown need no new operation in the reference run; the general translation is not checked. Test declared residue before adopting `take`. §1.25 gives the frozen-fixture result and its limits. The nearest precedent could not be checked and its program was not rerun. `[proposed]`

**§1.27 Outcome A, set aside for now: take.** A is set aside for now. `[decided]` Under the proposal, $\mathrm{take}(K, A)$, defined only for the never-runnable $K$ of a caught failure that takes no answer, gives the live values of sort $A$ that $K$ holds, each once, innermost first, and what is left of $K$. A value inside a datum is taken with its datum. The rule owes each taken value what any holder owes: to finish it by an operation of its theory, use it, or hand it on. It may leave $K$ and return only when every taken obligation is used, finished or handed on through a permitted operation and nothing that may not be dropped is left in $K$. A function, or a value of a sort the rule cannot name, cannot be taken: over those the rule can only fail in its turn, and whatever answers that failure receives a continuation holding them. No general recovery rule for resource stops or running out of fuel is given. A possible failure's manifest entry (§10.1, §1.43) would give the sorts of the values that may be held when it happens and may not be dropped; a rule returning after a failure would be admitted over a body only if it takes every sort the body's manifest gives for the failures it answers. Cost: one more operation in the reference run, which is trusted text (§9.14); the check's pass at failing points reports sorts; a compiled program must know at each call that may fail which slots hold live values. Also depending on A: the failure in a task (§9.13), and §8.8, whose held values take would have to find. `[proposed]`

Cases under A: a test would catch a failure that takes no answer and take the permitted held values; the parser would retry with the input as it stands after the failed reads, not an earlier state, the return condition and the exclusions of take being as above. To refuse: a rule that takes from the continuation of an operation that does take an answer and then runs it: the value would be in two places. This is no general recovery test for resource or fuel stops (not run). `[proposed]` Open: the task-failure rule, and the backend's account of surviving values (§22.2); B supplies no take operation and no new manifest or outcome schema. `[open]`

**§1.28 One mark now.** The single exactly-once mark (§1.7) stays through slice 1. The project owner decides whether to split it before slice 2’s interfaces are drafted. `[decided]` With one mark, catching a failure gives no permission to drop a held value: recovery returns only after every obligation is used, finished or handed on through a permitted operation, else the failure propagates with the value retained, and the catcher may not reach in (outcome B, §1.25); a library handler may perform a cleanup that is available. (for now, under the one mark and outcome B) `[decided]` The other rules assume the one mark. Before the direction is built: reading each existing use-once declaration as both marks keeps every unchanged contract as it was, which is all the comparison so far shows. Owed: for the two marks, before the direction is built, capture, functions passed as values, declarations and a new census. `[proposed]` Before slice 2’s interfaces are drafted, revisit the split together with closed operations (§21.7) and the host ownership interface. For now the first build refuses a closed operation with no rules (implemented in the host or as an evaluated definition) that takes a use-once value, bare or inside data, naming the parameter and the inside sort. A selected interpretation whose image has rules goes through that image. `[decided]` The project owner left six questions open for that review. Which theory is entitled to consume the value? What event counts as “given out”? Which kinds may be discarded? What must an operation declare? What happens when a closed operation returns a use-once value? Who may name a constructor, given that a rule naming it can end a token? `[open]`

**§1.29 Direction: two marks.** Separating the marks is the proposed direction. `[proposed]` Copying and dropping are two questions, and the theory answers each: a sort is marked no-copy (no law to copy its values), no-drop (no law to drop them), or both, which is use-once.

- Clause (a): in the scope $D$ that makes $a$, no-copy requires $\#_D(a) \le 1$, no-drop $\#_D(a) \ge 1$.
- A function carries each mark the values it holds require.
- A data sort carries every mark its fields carry, else its declaration is refused. To refuse: a datum of a sort that may be dropped, holding a value that may not; leaving the datum drops what is inside.
- In place of a law a theory may give an operation: one that copies, or one that finishes (consumes a value and returns nothing of its sort). It runs where the program calls it, and what it does is in the manifest there. A sort with a declared finish is no third kind of sort: the finish is an operation, with effects, and usage stays two yes-or-no answers.
- Dropping a value that has a law to drop is no act in the meaning: nothing is observed, nothing enters the manifest; how it runs and what it costs belongs to the representation.
- In §3.12: resuming twice is refused over a no-copy value, never resuming over a no-drop one.

It would change §1.7, §1.13, §3.12; §9.2 and §9.3 ("use-once" reading "no-copy and no-drop"); §9.13; and the census behind §3.11 to §3.13, which counted a rule that never resumes as wrong under the single mark: over a name marked only no-copy it becomes right. A Task must stay no-drop, or a deadlock can vanish (§9.11) (unbuilt; tests unrun). `[proposed]` A function also carries each mark its contract for being called requires: to run at most once, no-copy; to be run, no-drop; to run exactly once, both, even when it holds nothing, as for a Task (§1.14, §9.2). `[proposed]`

**§1.30 Narrower rule.** Until the test of §1.32 passes, slice 1 may build the narrower rule: clauses (a) and (b), and refusal of any binder that consumes a use-once value from outside ($\#_t(x) \ne 0$ for its body $t$ and a use-once $x$ bound outside). `[decided]` Clause (d) is in slice 1's check too, for the one kind of use-once function the narrower rule leaves: a pattern variable standing for a bound argument of multiplicity $\mathbf{1}$, with exactly one site, where clause (d) allows (§1.14). No other arises, the binder clause (c) would make into one being refused. Slice 1 source may declare an operation taking a bound argument, and call it; it has no exported operation that takes a function (§1.46). `[proposed]` The narrower rule ends with slice 1: under it a use-once value cannot be used after an effect, everything after an effect being inside its continuation, and slice 2 brings effects. `[proposed]`

**§1.31 Narrower rule and output.** Slice 1 has one effect, its output (§1.46), so that last claim is true of the text of one scope, not of a run. Refused: the output's own continuation whose body consumes a use-once value bound outside it (a continuation is a binder as any other). Not refused: a value that waits while an output is asked from inside a call: in an argument already obtained, in a rule's environment, or in a let whose initializer calls a defined symbol whose run reaches the output. For a term otherwise meeting admission and clauses (a) and (b), such waiting is no additional refusal. An output written in the initializer itself is no such case: the reader lifts it over the whole let (§21.4), and its continuation then holds the let's body. Case (schematic terms, admitted signatures): `h` of a use-once sort, an ordinary output result, rule `say(b) = out(b, r -> unit)`, caller `let y = say(b); finish(h, y)` finishing `h` once. The continuation in `say` captures no outside use-once value. One request takes one admitted reply (§8.9), so the caller resumes at most once; if no reply is committed, `h` stays held. The rightness claim is for this fixture; it does not follow merely from a waiting value or from the host's one-reply rule. So one program is refused with its output written straight and accepted with the output behind a defined symbol: one more case refused though right (§1.32), ending with the narrower rule. Slice 1's generated terms include both shapes, and the reference run's count is compared on the accepted one (§19.2). `[proposed]` Open: should the straight form be admitted in slice 1? Nothing here chooses it. `[open]`

**§1.32 Owed test.** Owed: the comparison of the use-once check with what a run consumes, on the whole language, with data holding a use-once field, effects, and a value consumed once in each of two branches. `[open]` Known refused though right: a value consumed once in each of two branches passed as functions; a value used once and also handed to a function never called. `[decided]` The same census, with none added as a multiplicity and then with a pair of call profiles for the two branches, tests whether those are recovered: no wrong term accepted, and a count of the refused right terms each recovers (to test). `[decided]`

### Term

**§1.33 Term and identity.**
A term $t$ is an expression over theories, stored in a shared graph with one node per identity: $\mathrm{node}(t) = \mathrm{node}(u) \iff \mathrm{id}(t) = \mathrm{id}(u)$. A declared symbol is identified by its declaration, a defined symbol by its content, a term by its structure with binders made nameless. Programs, proofs, data and machine code are terms. `[decided]` This is about store and identity only: two pieces of code being one node is never by that a reason to reuse a run (§8.3). `[proposed: working rule]` Hash-bearing identities and references are qualified by their exact canonical/hash profile; replacing it needs explicit new evidence or reviewed migration, and claims no agreement of old and new observable bytes, runs or resource outcomes. `[proposed]`
At the full slice 1 reference/compiled comparison after milestone B, review this distinction: name each program occurrence within its scope; distinguish its visits in a run and their activations. `[proposed]`

**§1.34 Terms as data; quotation.**
Any node can be read as data: a term, theory, interpretation, representation and derivation are each values of a sort of their own, so a question or predicate may take one as argument. `[decided]`
A term is handed over as data only by `quote(e)`. The reader of text makes it a literal of the sort of terms holding $(\mathrm{node}(e), \Gamma)$: the node of $e$ as written with the context $\Gamma$ of its variables, fixed when the text is read. The run does not evaluate inside a quotation; no rule, interpretation or planner move enters one. A value does not carry the term that produced it. Running a quoted term is an operation of its own; what the term reaches enters the manifest where it is run. `[proposed: working rule]` In the general look-back design, only the quotation written at the call can be relied on (§1.38). The provisional first-build reader refuses a quotation (§19.4). The designer chose that refusal under the project owner’s provisional first-reader decision; the project owner gave no separate ruling on quotation. `[decided]`
Alternative: any term may be read as data wherever it stands; what an operation sees then depends on whether its argument ran first. Case: `root_is_add(add(1, 2))` without a quotation sees 3.
Open: the written form of the quotation mark. `[open]`

**§1.35 Predicates on structures, theories, terms.**
A structure is given as an interpretation of its theory. A predicate on structures that the theory's language cannot state (finite, complete, simple) is a predicate on interpretations, stated in whatever foundation is hosted; one on theories (consistent) is a predicate on theories as data. `[decided]` Reading a term as data exposes its node, so such a predicate may distinguish two terms a law equates. `[proposed]`
Open: are an interpretation and a record with the same carrier, operations and laws one thing, or two connected by a claim? Test: in slice 2 write one monoid both ways and look for a client that tells them apart. `[open]`

### Look-back

**§1.36 What is seen.**
A look-back sees the term written at one argument place of one call, as the reader of text made it: outer symbol and parts, variables as variables. It follows no variable to what was bound to it and no parameter to the caller. It does not see how a value was produced, the plan, a name chosen for a value, or anything else in the store: outside this mode on present evidence. A history recorded explicitly and handed over beside a value would be a wider interface with its own meaning and tracking; not designed. Unseen look-back: the result is the same whatever was seen; the look only chooses how to compute it. Seen look-back: the result depends on what was seen. (first set) `[proposed]`
An observation $q$ with $q(t) = q(u)$ for all terms the whole evaluation makes equal, in a domain where every admitted term reaches a value, observes the value. Agreeing only on terms that some named laws make equal is weaker: a view of a sum by its leaves respects regrouping and still tells `1 + 2` from `3`. `[proposed]`

**§1.37 Unseen: look-back laws.**
A theory may mark a law $\ell$ as a look-back law: directed, $f(p) \Rightarrow u$, the left side an operation applied to an argument written in a stated shape $p$. The optimizer may use $\ell$ at a site only where (L1) $\ell$ is $\mathsf{yes}$ there (§4.5) and (L2) every condition of §8.6 holds for the runs it moves, repeats or leaves out, calls of a function handed to the operation included: bindings of arguments, the activation, how each claim was admitted, evidence read again where the term now stands, no effect, no open choice, no possible non-termination, no use-once consumption, no use-once result shared, run again or left unmade. The sequence restrictions of §8.6 apply to the term and its callees, including the restriction for now on moving or omitting a sequence-making term. Over parts that may have those, $\ell$ is used only under a claim about the two runs (§8.1). The two runs then agree as §8.10 and §8.12 ask: the requests; the outcome with a failure's payload; what is consumed, value by value and activation by activation; who holds each fresh result; the values held at a failure. A stop for a resource is not agreement. Use changes nothing the reference run observes; time, memory and where a resource runs out may differ. The plain path uses none. Calling an operation a functor or natural transformation licenses nothing: its own law, with its scope, does (first set). `[proposed: working rule]`
Test per marked law: exhaustion over every small term that both sides have the same run in that full sense, with controls each to be refused: (1) a wrong law; (2) a right law over a function with an effect; (3) two maps made one where the functions fail with different payloads; (4) the same under a resolver answering by position; (5) an element left out whose function fails or does not end; (6) a rewrite leaving a use-once value unconsumed; (7) two fresh use-once results made one; (8) a value held at a failure on one side only; (9) evidence not holding where the term now stands. (to test; §23.2 row 28 is what has run) `[proposed]`
The controls exercise the simple first-set licence, with no separate full-run claim. Each case records law, scope, sites, selected interpretation and expected refusal. The use-once control detects changed consumption or ownership, including a value neither consumed nor handed on at successful return; failed and endless runs may retain values as §1.22 and §1.23 allow. An effectful callback is refused by this route even where a separately established full-run claim could justify it. `[proposed]`
Case (3): `map(f, map(g, xs))` made one pass; `xs` holds 0 then 1, $g(0) = 0$, $g(1)$ fails with payload $a$, $f(0)$ fails with payload $b \neq a$. Two passes: $g(1)$ fails first, payload $a$. One pass: $f(g(0)) = f(0)$ fails first, payload $b$.

**§1.38 Seen: two forms.**
(F1) The quotation of §1.34, written at the call. This is the only form that clients of the general design may rely on for now. `[decided]`

(F2) A declaration by the callee in place of the mark at the call, translated by the reader of text into an ordinary call on a quotation. `[proposed: working rule]`
The project owner made F2 provisional. It returns to decided only when its execution rule is written and accepted and four tests pass against it. Test a variable operand, an effectful operand, refusal when the function is handed on, and the same answer from a part built during a run. Queue all four tests now. They have not run against an accepted rule. `[decided]`
A declared look-back is applied by name only, never handed on as a function, and follows no variable. A quotation mentions no use-once variable, in either form. `[proposed]`

1. Executable substitution in the elaborated core leaves each quotation and its variable context fixed. Changing the source differs. `(x → is_variable(x))(3)` gives true, while its source-level beta contraction `is_variable(3)` gives false. The contraction changes an observation of syntax. `[proposed]`
2. Under the syntax-only alternative (b) below, the operand does not run. Capture precedes turning an effect inside the operand into a continuation (§6.1), or `ignore_syntax(print("x"))` would print. The supporting sources were checked and the example program was not rerun. A syntax-and-value interface runs the value part as an ordinary argument. `[proposed]`
3. Whether a declared operand also runs is open for the project owner. The three answers are (a) run it once and give both its written form and its value, (b) give only its written form without running it, and (c) let the declaration choose, with both sets of obligations and tests. The designer recommends (a) as the first step. None is selected. `[open]`

For the paper comparison, work those three candidates and a fourth, requiring explicit quotation at the call, through the four tests above. Add a control whose operand makes a fresh use-once value, recording whether it runs and who holds the result. These are paper predictions. The fourth candidate supplies a comparison with F1. `[proposed]`
For every execution choice, a build resolves declarations and fixes each quotation once, before any rule puts a body in place of a call; a quotation's content and variable context are kept through that and through storing; ordinary arguments still run first; a part built during a run gets the same fixed graph (§12.2); a changed declaration is a new recorded reading (§13.2) (first set). `[proposed]`

**§1.39 Order of widening.**
Each step has its test. The first set applies §1.37 to parts with no effect. `[proposed: working rule]` Steps 1–3 are proposed. Step 4 is the working rule of §1.38:

1. Laws read off the rules: an operation commutes with every total, effect-free map of elements, where (a) it is one family across element sorts whose behaviour on structure does not depend on the sort, on anything chosen by the sort, or on a representation, and (b) its rules, with every helper they call, never test an element, compare two elements, make a constant of the element sort, or apply an operation to an element. Until this is a theorem for this language's rules, whatever reads it off the rules is a decider named in the manifest.
2. Look-back laws over parts with effects: each a claim about the two runs at the selected interpretations.
3. A representation that remembers how a value was made, such as a data-sort value held as a map not yet done: a representation like any other, owing its tracking claim, failures, runs without end and use included.
4. Seen look-back by declaration under §1.38's boundary (by name only, never handed on, no use-once variable inside, no following of variables): a working rule until its execution rule is accepted and its four tests pass. If it falls, keep it as a later widening step.

Case for (a): a family returning its argument where the element sort has one member, and the empty value of the argument's sort otherwise, tests no element and makes none, and does not commute with a map from a one-member sort to a two-member sort. A check with maps inside one sort cannot find it. `[proposed]` Illustration: on the one-item sequence of the single member, mapping into the two-member sort and then applying the family gives the empty sequence, while applying the family and then mapping keeps the item.

### Interpretation

**§1.40 Definition.**
An interpretation $\iota : T \to T'$ replaces each sort, constructor, operation and effect of $T$ by a term of $T'$, preserving sorts: $f : A_1 \times \dots \times A_k \to B$ gives $\iota(f) : \iota(A_1) \times \dots \times \iota(A_k) \to \iota(B)$. It is applied by substitution, through the rules of defined symbols; the induced map on terms is $\hat\iota(x) = x$; $\hat\iota(f(t_1, \dots, t_k)) = \iota(f)(\hat\iota(t_1), \dots, \hat\iota(t_k))$ for $f$ a constructor, declared operation or effect of the source, or a defined symbol given an image of its own (§1.41); and for any other defined symbol $g$, $\hat\iota(g(t_1, \dots, t_k)) = g^{\iota}(\hat\iota(t_1), \dots, \hat\iota(t_k))$, where $g^{\iota}$ is $g$ with each of its rules carried through $\hat\iota$. `[decided]`

**§1.41 Claims at an interpretation.**
Each law $\varphi$ of $T$ becomes a claim with statement $\hat\iota(\varphi)$: the law's statement, with the definitions it uses, carried through the map; never given by the map. Where $\iota$ gives a defined symbol $g$ its own image, that $\iota(g)$ agrees with $g$'s definition carried through is a further claim. `[decided]` If $d$ derives $\psi$ from laws $\varphi_1, \dots, \varphi_n$ of $T$, $\hat\iota(d)$ is evidence for $\hat\iota(\psi)$ with assumptions $\hat\iota(\varphi_1), \dots, \hat\iota(\varphi_n)$. `[decided]`
Case: a map allowed to replace a law symbol directly could map it to true and thereby appear to settle its own obligation. Carrying the statement and its definitions through the interpretation prevents that.

**§1.42 Instances; selection.**
An instance of an algebraic structure, a fold over data, a handler of an effect and a compiler stage are interpretations. `[decided]` One is selected at a use by naming it, or by a default declared for a theory in a scope; two defaults that both apply are a refusal naming them. `[decided]`

### Manifest

**§1.43 Three sources.**
The manifest $\mathcal{M}(t)$ is what $t$ leans on. `[decided]`
(i) Declared operations, effects and laws reachable from $t$ through its arguments and the rules of defined symbols, less those a selected interpretation replaces. Declared sorts and constructors of a data sort are no entries: they lean on nothing. `[decided]` A defined or evaluated symbol whose recursion has no evidence that it ends is an entry, as possible non-termination. `[decided]` Not taken: it is an assumption, settled never.
(ii) By name, every claim $t$ rests on that is settled never: an assumed membership, a tracking claim with no evidence `[decided]`, a clause assumed within the bound (§3.5) `[decided]`, and the claim that a run ends, where a use relies on it and it is assumed; a program may run without assuming it ends. `[decided]`
(iii) The manifest of the evidence of every other claim it rests on: the build that ran, a decider or checker with what it assumes, the laws a derivation used. `[decided]`

**§1.44 Meaning and artefact manifests.**
The meaning manifest $\mathcal{M}_m$ is (i) to (iii) for the term as stated. `[decided]` The artefact manifest $\mathcal{M}_a$ adds, for each representation chosen, (i) to (iii) for its trackers and tracking claims. In slice 1 the default representation's tracking claim is settled never; hence the root manifest names the lowering and the backend. ("backend", a neutral word, is decided) `[decided]` On the generated C route the outside C compiler's recorded output is the comparison program of §6.2; tracking what that program does stays separate, and the unsettled lowering and backend stay named in the root manifest. `[decided]`
Each membership claim of the term as stated is settled, as its admission says, in one of three ways: by evidence passing through no representation; by a test at each evaluation (a guard, §4.10), whose failure is then an outcome of the meaning; or never, by name. $\mathcal{M}_m$ is computed from these and nothing chosen later. Evidence a plan finds through a chosen representation, letting it drop the test, enters $\mathcal{M}_a$ with that representation's trackers and tracking claims and does not change how the meaning settles the claim. A term whose statement names a representation as the ground of a membership has it as part of the term: no choice, and its manifest is in $\mathcal{M}_m$. `[decided]`
Case: an operation asks for a pure braid. One representation's tracking claim would settle the membership by two laws; a second leaves a test. Without this rule $\mathcal{M}_m$ changes with the representation.

**§1.45 One account; role and acting time.**
A manifest records effects, possible non-termination, open choices, axioms, unverified tools and the target machine in one account. A permission is a bound on the manifest. Order of running is not in it; §8.1 settles that. `[decided]`
Each entry keeps source, role and acting time. Role: what the term does when it runs, what is assumed, or what is trusted. A source (i) entry acts when the term runs, or only when a bound argument is called. A source (iii) entry acts when its claim was settled: at build, at load, once in a run, or at each evaluation; only the last two act in a run. A bound says which it limits. A guard's test is part of the run it guards; what it reaches is in the manifest before the bound is read. A check only the artefact makes is in $\mathcal{M}_a$. The source, role and acting-time rule is in use. `[decided]` It remains provisional pending its test. `[proposed: working rule]` Not taken, and the fallback if the test fails: every entry counts as acting in the run; safe, less exact.

**§1.46 Manifest variables; the slice 1 bound.**
A bound parameter names a manifest variable $\alpha$, which the operation's declared bound $\mathrm{bound}(f)$ may hold. An application has manifest $\mathrm{bound}(f)[\alpha := \mathcal{M}(u)]$ for argument $u$, keeping what evaluating $u$ itself reaches. A definition is checked against its declared bound. Slice 1 has one fixed bound and exports no operation taking a function, so it may count every entry as acting in the run. `[proposed: working rule]`
That bound permits: one output operation reached through Ask; possible non-termination; compiled stops for memory and for the stack (a separately named resource, on memory's terms), under §8.10 and §8.12, recorded as stopped for a resource, never as agreement. It permits no open choice (`pick`). It admits the unmatched-call failure of §1.51; the guard-failure question there stays open. The C route's guard for a clean stack stop is unqualified (§10.11). The allowance for literal checks at admission is fixed with the bound, apart from execution fuel (§7.5). Membership by name stays refused (§7.6); no blanket ban on other axiom or trust entries follows. `[decided]`
Open: the output operation's exact symbol and signature; the manifest/bound scope, role and acting time of resource, target and tool entries; amount and charging protocol of the literal-check allowance. `[open]`
Open: the interface for use-once ownership at the host boundary, needed for any use-once entry, result or failure state and for the reference/compiled consumption account; the output operation does not settle it. `[open]`

**§1.47 Polynomial.**
With alternatives $\mathcal{M}(t)$ is a polynomial over the manifest's symbols: alternative routes add, joint requirements multiply. It is kept as a shared term, never expanded. Its free symbols are the set a reader sees. Read in true and false, a product as "and" and a sum as "or", it answers a bound. `[decided]` Sums range over routes the planner or the reader of evidence chooses among and records: two pieces of evidence for one claim, two representations for one sort, two trackers for one operation. `[proposed]` Two branches of a run are not routes: what either reaches is required. A chosen plan's manifest holds the routes chosen. `[proposed]`

**§1.48 Cost reading; naming the route.**
A settlement is a job: one checking program, one input, one context, one time (at build, at load, once in a run, at each evaluation). The context holds the evidence the job rests on and the route that settled it. Two places share a job only when all four agree. A guard settled at each evaluation is paid at each; a checker run on two inputs is two jobs.

$$\mathrm{cost}(\text{route}) = \sum_{j \text{ distinct job}} n_j \cdot \mathrm{cost}(j), \quad n_j = \text{times } j \text{ must run}.$$

Read in costs, the polynomial is an upper bound on the cost of settling: it charges an entry once per place it stands, while one settlement may serve several. The bound holds where each job has one fixed non-negative cost and all work is counted. The cheapest route is a search (it contains cheapest cover). Running cost is not read from the manifest; it is counted on the chosen plan by how often each step runs. `[proposed]`
Case: $(x + y)(x + z)$, $x$ at 5, $y$, $z$ at 3. The cost reading picks $y$ and $z$: 6. Settling $x$ once: 5. (The reading adds across a product and takes the least across a sum, $\min(5, 3) + \min(5, 3) = 6$; it charges each occurrence, so it is an upper bound where one settlement serves two places.)
The settled account of a claim (§4.1) is a time, one of the five, and a route. The route is no value of a second enumeration: it is what the settling job's context holds, identified by the selected evidence and the context in which it is read. It may take several jobs, costs summed; for a fact established by a run it is one of the three routes of §13.5. The account refers to the settling job or jobs; to one root job only when its record and context identify the selected evidence and recover the whole route unambiguously, with every distinct job required and the rule under which each run is evidence (§13.7). The reference must determine the route in the context where the evidence is read (§4.5); one compatible with two routes does not complete the account. A claim settled at each evaluation of its site is settled by a guard: each evaluation is a job, and before the run the account names the guard. A planner-chosen route is recorded with the plan before any job runs. Two pieces of evidence give two accounts, each in its context: alternatives that add; a reader choosing one records which. A claim settled never has no job and no route, and stands in the manifest by name. In slice 1 nothing chooses among routes (§19.2). (no record bytes, no new admission restriction chosen) `[proposed]`

**§1.49 Leaving the manifest.**
By answer: an interpretation supplies the symbol and its claims are $\mathsf{yes}$. By indifference: every lawful answer gives the client the same observations. `[decided]`

**§1.50 Manifest computer, slice 1.**
Input: a node, in the context its admission used where it holds variables. Read from the store: the rules of each defined symbol reached, how admission settled each membership claim of the term as stated, the manifest of the evidence of each claim rested on. Output: the manifest of §1.47, with no sum, since slice 1 chooses among no routes (planner or reader of evidence): $\mathcal{M}(t) = a_1 \cdots a_n$, all entries required, each with source, role and acting time, all countable as acting in the run. No interpretation is selected, so (i) removes nothing.
$\mathcal{M}_a$ starts from $\mathcal{M}_m$ and adds actual artefact dependencies, operations and checks, each with source, role and acting time: default trackers and tracking claim; named reader and elaborator; boxing memory stops; the stack as its own named resource on memory's terms; the machine-model conditions no test can show, as trusted under the build part each rests on; artefact-only guards and build and load checks. The completed manifest is checked again (§6.4). The root manifest of §19.2 is $\mathcal{M}_a$ of the whole program, at the root of its graph. What identifies an entry, and the record's form, are the record rules' to give (not yet fixed).
The walk also reads reached signatures and declarations and the whole checked action of each evaluated symbol; it retains the declared operations, effects, laws and possible non-termination of (i), and what each retained guard test reaches before the bound is read. These are inputs of the one manifest text, not extra trusted texts. `[proposed]`

**§1.51 Fixed bound: possible failure, non-termination.**
The slice 1 bound admits the possible failure of a call no rule matches: slice 1 accepts such a program (§10.1); under one fixed bound it would else be refused, the answer not taken there. The run ends $\mathsf{failed}(\mathit{payload}, \mathit{held})$ (§8.8), payload as §10.3, reported as §3.16. `[proposed]`
Open: does the bound also admit the failure of a guard a build put in (§7.6)? `[open]` The designer proposes yes: the existing possible-failure entry would cover both an unmatched call and failure of an inserted check. The bound's permissions are the project owner's to grant, one by one, so this is put to the project owner. `[proposed]`
The only evidence slice 1 can hold that a run ends is the evaluator's test by syntax, for evaluated definitions (§15.1, §7.7): an evaluated symbol is an entry of possible non-termination when its definition is not total by its syntax. For rule-defined symbols slice 1 has no test and no evidence (Eval settles one input; derivations arrive in slice 4), so every defined symbol whose rules reach it again, directly, through other symbols or through the body of a bound argument, is an entry. The bound permits the entry, so this changes what a manifest prints, not which programs are admitted. A syntactic test for rules, such as descent on a constructor's argument, would be a new decider named in the manifest; none is proposed for slice 1. `[proposed]`

**§1.52 Names in the root manifest.**
A name is a name with the hash of the bytes that ran and a recipe rebuilding them to that hash, as §13.5 and §13.6 name an unverified checker. Named: the reader of text, with the hash the build records; the elaborator, by its own hash (§13.2); the evaluator build that ran, by source (iii), as each run record names it (§13.7); the lowering and the backend, since the default representation's tracking claim is settled never. Under the lowering: its two steps, the checker of the low-level form, the runtime (§10.8). Under the backend: outside C compiler, assembler, linker. The machine theory, with its decoder, is a declaration the build takes as true (§10.6). Which compiler is named waits on its choice (§19.2); the bytes a hash covers are not yet given. Also named: the assembly-text parser, operand resolver and binary/data comparator of §10.7, or the bound component whose bytes contain each. Actual unverified checking roles retain §13.6. Declaring the machine theory does not prove an implementation of these checks agrees with its account. `[proposed]`
How a build accepts a named assumption, and what a strict build refuses: §13.13.

### Open choice and resolver

**§1.53 Open choice.**
An open choice is the effect $\mathsf{pick}$ of theory $\mathsf{Open}$: it takes a set $X$ and a continuation, which receives a member. `[decided]` $\mathsf{Open}$ has one law, owed by every resolver: the answer is in $X$. $X \neq \emptyset$ is a claim at each pick. `[decided]`
Exchange is no law of $\mathsf{Open}$. It holds in one reading only: a term stands for its set of outcomes $\mathrm{Out}(t)$ and the pick is unresolved on both sides. There a pick may be exchanged with a step when (a) neither uses the other's result, (b) the step runs its continuation exactly once, (c) the move takes the pick neither into nor out of the scope of a handler or resolver. Any other exchange is a claim about that pair, naming the two selected interpretations, the scope and what is observed, settled as any claim. The exchange condition still needs its test. `[decided]`
Case (b): a step runs its continuation twice and joins the results; a pick from $\{0, 1\}$ before it gives $\langle 0, 0 \rangle$ or $\langle 1, 1 \rangle$, after it four outcomes. Case (c): a step runs its continuation once inside a resolver answering 0; a pick before the step gives 0 or 1, moved inside it gives 0.

**§1.54 Resolver; draws.**
A resolver is an interpretation of $\mathsf{Open}$: a term answering each pick. It may read its ordered parameters and nothing else, written down as: the set alone; the set and a seed; or the set and the pick's position in the run. The guarantee depends on it: reading only the set gives one answer wherever the pick stands; reading the position does not. `[decided]` With no resolver named, the default answers by the pick's position in the source, passed by the reader of text as an argument of the pick. The semantic part of the lock records the resolver and what it reads. `[proposed]`
Open: is a draw a pick whose resolver reads a seed from a declared finite sort, the promised law settled by counting seeds? First test: a fair coin against a constant must be refused; against its own negation, accepted with a matching of seeds. `[open]` Illustration: with seeds 0 and 1 counted equally and the coin returning its seed, the coin agrees with a given constant on one seed of two, so that comparison fails; the coin at seed $s$ equals the negated coin at seed $1 - s$, which is the matching.

### Representation

**§1.55 Definition.**
A representation of a sort $S$ in a target theory $U$ is $\rho = (N, \mathrm{names}, \Sigma, \{\tilde f\}_{f \in \Sigma}, \mathit{form}, \mathit{opt})$:

- $N$: a sort of $U$; its values are the names;
- $\mathrm{names}(n, v)$: a relation between names and values of $S$, stated as a term;
- $\Sigma$: the signature, the operations on $S$ a client reaches; at a module boundary the exported operations, each with a declared manifest bound, and a client relies on the bound only;
- $\tilde f$: a tracker on names for each $f \in \Sigma$;
- $\mathit{form}$: one form for its hidden sorts, forward or backward, with the tracking claim of §3.2;
- $\mathit{opt}$: where a name stands for many values, optional resolution and width claims. `[decided]`

$\mathrm{names}$ is a relation, not a map: a name may stand for several values, a value may have several names. `[proposed]`

**§1.56 Reading a name.**
A client's reading of a name's identity, hash, bytes, or the name itself as data is an operation on the hidden sort and needs a tracker like any other. Reading the term as stated differs from reading the name chosen for it. `[decided]` An observed hash retains its exact canonical/hash profile (§1.33). `[proposed]`

**§1.57 One construct, any target.**
The target may be any theory; the cases are one construct. `[decided]`

| Kind | Target | $\mathrm{names}$ given by |
| --- | --- | --- |
| Holding: a layout | A machine theory | A map from names to values, possibly from a sum of name sorts |
| Analysis | A lattice, or enclosures | A set of values for each name |
| Invariant or quotient | Any theory | A map from values to names |
| Embedding, or structure-preserving map | Any theory, or another model | A map from values to names |
| Approximate fit | A geometry | A bound on a distance between name and value |
| Late choice | Any theory | A set of values still to be chosen among |
| Code for one term | A machine theory | Running the code. A check for one program is the relation for one pair |
| A set given by a predicate | A test, an enumeration, a generator, a constraint | Each answers some of member, enumerate, count and pick |
| Another algorithm for an operation | The same theory | Equality: the names are the values themselves. `[decided]` |
| Linear state (first finite stage of the Structural Representation Explorer) | Vectors over a declared field | A map to vector names, with checked trackers for the operations; a dimension bound is a separate claim (§20.8). `[proposed]` |

A partial holding with a fallback is a total holding into a sum of name sorts; a guard is the case analysis inside a tracker. An enumerated set is a subset of the set it enumerates until its covering fact is settled. Turning a predicate into an enumeration is solving, done by a proposer under a budget. `[decided]`

### Claims, positions and usage

**§1.58 Claims, positions, usage.**
A claim $\kappa$ is a statement with a status and evidence; §4.1 gives its record. `[decided]` A theory stands in one of three positions to a term: the term is stated in it (its meaning), leans on it (its manifest), or is represented in it. The compiler may change one without disturbing the others. `[decided]` Whether a value may be copied or dropped belongs to its theory; what a permitted copy costs, to its representation. `[decided]`

### Facets

**§1.59 The five facets.**
What other languages put into one word for a value's kind, this design keeps apart as facets: the dimensions of what that word used to cover. (for the word) `[decided]` Five are in use. Meaning: the sort, its theory, what a model makes of it. Effects: what running does, shown in the manifest. Usage: whether a value may be copied or dropped. Representation: how a value is laid out and computed. Evidence: what is known about it and on what that rests. `[proposed]` The count stays five. `[decided]`
The following are inferences from the five-facet account.

- The three positions in §1.58 account for meaning, manifest and representation. The theory determines permissible use, the representation its cost, and claims record what is known. A manifest entry describes an effect, assumption or trust (§1.45), so the manifest carries both effects and part of evidence.
- The three declarations on a sort (§1.7) fall under no single facet: finite and data say what values there are (meaning) and are covering facts (evidence, §4.4); use-once is usage.
- Time, when a thing is known or acts, is the strongest candidate for a sixth. It appears inside four of the five: a quotation fixed at reading (§1.34), when a manifest entry acts (§1.45), when a claim is settled (§4.1), building ahead of time or during a run (§12.1). With five, time is treated across the existing concerns; a bound can already select when entries act.
- Identity, what makes two things one, is a second: by content for a node, by declaration for a declared symbol (§1.33); this concerns stored terms and declared symbols. A node is also an evaluator value whose identity `same` and `memo` observe (§15.9, §2.5). Fresh use-once values and activations stay distinct for run accounting, and identity observations on represented names still need tracking (§1.19, §8.10, §1.56). A sequence is a third case: one thing by its own name, not by what it holds (§17.2); §21.1 asks what that does to "yes by identity". Identity is no facet of its own; like time it is treated across the five. `[proposed]`

Proposed: a facet is a separately usable view of what is said of a term, each with its own check, not a part that can be changed alone: the manifest's evidence entries follow from the route chosen for the meaning's claims (§1.43), and a representation's manifest joins the artefact manifest (§1.44). So "changed without disturbing the others" in §1.58 means the meaning and its manifest are kept (§1.44), not that nothing else moves. `[proposed]`

Distinction, what a caller may learn across a boundary, is a third candidate. It is not a facet of its own, for this reason. A Distinction verdict is a law about every pair of the meaning's runs from starts the observer cannot tell apart. Inclusion carries it to every realization (§3.3), and its check is the check of a law of the meaning. Representation's judgment is a different one, each realization run matched by some meaning run, and the two agree only where each run has one outcome; so Distinction needs a declared home in the boundary's contract and the every-pair reading in Meaning's laws, but no check of its own. The home is the public law of §3.20, and the reading is §3.21's. The case rests on the open item of §22.8, a view for what an observer may learn. (five, with this rationale) `[decided]` It would reopen if carrying a two-run law through effectful or higher-order client terms needed rules of introduction, composition and refusal that Meaning's law logic and Effects' manifests do not give; the theorem that §3.21 defers tests that. `[proposed]` In the rationale, one outcome gives a setting in which the two checks can coincide. Equal verdicts in a particular example do not establish that its runs each have just one internal outcome. Two distinct internal outcomes can both report the same public result. (a clarification) `[proposed]`
Illustration: where each start $s$ has exactly one run, $|\mathrm{Runs}(t(s))| = 1$, the two readings of §3.21 say the same of two starts, since a statement about every member of a one-element set and one about some member agree. With two runs from one start they can part: in the case of §3.3, $\mathrm{Out}(t(0)) = \mathrm{Out}(t(1)) = \{0, 1\}$ matches each run from one secret by some run from the other, while two runs, one from each secret, can return 0 and 1.

### The foundation

**§1.60 Hosting.**
Mathematics is stated in theories hosted on a small core. Classical principles are declared laws, so they show in manifests. A set given by a predicate on an existing sort is a subset of that sort. A predicate is always on a sort, so there is no set of everything. Foundations are connected to each other by interpretations. `[proposed]`

**§1.61 Two questions, three positions.**
An LF-style framework for binding and derivations is the fixed-framework candidate. A dependent calculus in the kernel makes a change of foundation a kernel change. Pure LF leaves conversion to reified traces. With λΠ-modulo, each hosted foundation’s confluence becomes a trust root. The candidate aims to let each hosted foundation pay once for a normaliser, with fixed kernel text and no trusted confluence assumption. Whether to use a predicative dependent theory by default is open.
Open: (a) how the proof checker is built: one small fixed checker handed each theory's rules as data, or a checker written for one theory. `[open]`
Open: (b) which mathematics Loom speaks by default and when it arrives: a full theory at once, or only finite checks at first, grown as needed. Slices 1 to 3 need neither answer. `[open]`
Three positions combine answers to (a) and (b). The third is that earlier decision, now to be tested; it can host either initial mathematics. A predicative default stays among the open options, apart from checker architecture; whether Home is predicative is still to be stated. `[proposed]`

| Position | What it says |
| --- | --- |
| Home first | The default theory, Home, is an extensional dependent theory with universes, quotients, subsets whose membership is a claim, and proof sorts whose inhabitants are all equal. Whether Lean's theory is included in Home is a separate claim (§1.63); test 1 of §1.62 is evidence that it is feasible and cannot settle it |
| Finite checks first | First a logic of finite checks only: statements are about the evaluator's own terms and induction has no quantifiers. Lean is a guest from the first day, its results attested with Lean's kernel named in the manifest. Home is grown from what programs and the Structural Representation Explorer need |
| A framework taking a theory as data | A small framework for derivations that takes a theory as data, its symbols and its rule forms with their side checks, and hosts both Home and the logic of finite checks |

For (b): before slice 4's foundation trials are designed, say for each position whether its default theory is predicative, and add to test 1 a count of the declarations that fail for that reason alone. What settles it: that count, and for each candidate whether its checker's soundness is proved or entered as an assumption. The project owner took this timing and test. It has not run, and question (b) stays open. `[decided]`
For (a): before slice 4's interfaces are drafted, and in any case before the derivation checker enters the trusted base, run test 3 and measure the costs of §1.63; if the framework passes, it is taken. The project owner took this timing, test and conditional outcome. It has not run, and question (a) stays open. `[decided]`

**§1.62 Tests.**
Owed: the foundation's first two tests. Test 1 translates 1,000 library declarations, chosen to cover each feature of Lean's theory, and counts failures by feature. It is evidence of feasibility only: a failure records an obstacle in this trial and must be explained; a thousand successes do not establish theory inclusion, which is a claim over the whole guest theory, owed apart, with its own domain and proof. Test 2 writes one chapter of mathematics that is not about matrices in both shapes. `[open]`
Owed: the foundation's test 3 (unchanged hash), for the third position: before the trial, record the hash of the checker's whole trusted text, with the part that applies rules and the part that runs side checks. Add Home, then Lean's theory, as data alone; compare the hash. An unchanged hash shows the same bytes and no more. That each encoding is faithful, that its side checks are in fact run, and that no axiom came in with the data are checked apart; every added axiom, side check and trusted program is entered in its theory and its manifest. A changed hash fails this trial and is explained; it does not show what every such framework must be. This procedure is proposed, to be tested in slice 4. `[proposed]`

**§1.63 Costs of the third position.**
Where the framework rewrites, it owes whatever its checking procedure relies on: that the rewriting ends and comes to one result; a procedure with a bound may answer $\mathsf{unknown}$. Where every conversion is written out, certificate size is measured, with sharing, not assumed. Where Home is said to include Lean's theory, including means: every statement carries over, every derivation carries over, and conversion behaves alike. A translation that leaves the guest's kernel in the manifest is attestation, not inclusion. `[proposed]`

### A sample

**§1.64 Sample.**
The example below uses invented Loom syntax and has not run. The surface syntax remains open. `[open]`
Open: rules and cases need one written form for terms, with its reading as nodes; there is none. `[open]`

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

The comment on `total` has a narrow standing. Merely being a function contributes no entry from source (i). `[decided]` Illustration: at the integer interpretation the displayed associativity claim reads $(a+b)+c=a+(b+c)$. With $a=2$, $b=3$, $c=4$, both sides give 9. This calculation covers one input. The final line about graphs states a claim whose proof is still owed.

<a id="ch-2"></a>

## 2. The records

**§2.1 Schemas.**

```
Node ::= sym(symbol, nodes) | lit(sort, value) | var(index) | lam(node) | app(node, node)
       | let(node, node)
Symbol ::= declared(id, theory, kind: sort | op | constructor | effect | law, signature)
         | defined(content hash, signature, rules)
         | evaluated(content hash, signature, definition)
Signature ::= { indices: a count, parameters: ordered Parameters, result: sort }    -- operation
            | { indices: sorts,
                declarations: any of finite(values), data(constructors), use-once } -- sort
Parameter ::= value(sort)
            | bound(sorts of its variables, sort of its result, multiplicity: one | any)
Rule ::= { variables: a count, patterns: nodes, result: node }
Theory ::= { id, symbols }
Interpretation ::= { from: theory, into: theory,
                     map: each sort, constructor, operation and effect of the source -> node }
Note ::= { about: nodes, kind: estimate | sample | candidate | proposal, method, content }
```

`Claim` is the §4.1 record, `row(n)` the three §1.43 sources and `step` the evaluator program for the reference run (§8.8 gives its state and outcomes). Rule variables use `var` indices. A rule scopes the use-once check. Agreed, unrun shapes: `Node` without `let`, `declared`, the operation signature, `Rule`, `Theory`, `Interpretation`’s `from` and `into` fields, `Claim`, `Note` and `row(n)`. The signature fields of `defined` and `evaluated`, source-symbol mapping to nodes and account of `step` are also settled and unrun. `[decided]` The evaluator-definition field of `evaluated` and the sort-signature and parameter lines are proposed and unrun. `[proposed]` The core let is settled (§21.3). `[decided]` Its proposed record is the `let` alternative (§21.4). `[proposed]` Building slice 1 will test these shapes. `[open]`

**§2.2 Reusable declarations.** At the first client needing a reusable declaration, compare storing the family application in the kernel with expanding a closed use during elaboration and presenting a concrete declaration to the kernel. Both must preserve the application identity, the complete substituted declaration and all its admission obligations: cases, fields, parameter and result profiles, conditions, declared marks. Before choosing the verifier and the storage form, bring that client's need to inspect the family, the cost of checking and sharing expansions across modules, and a retained concrete signature with its profile-qualified identity. `[proposed]` Which storage form and verifier to use at that first client remain open. `[open]` Bring back a proposal for claims quantified over sorts only when slice 4 can carry and check their derivations. `[proposed]`

**§2.3 Profile change.** Hash-bearing identities and references are qualified by their exact canonical/hash profile. Replacing it requires explicit new evidence or a reviewed migration, and claims no agreement of old and new observable bytes, runs or resource outcomes. This governs §2.5 and §2.7 too. `[proposed]`

**§2.4 Fields not yet given.** Open: the fields for three additions to a signature, which have none above yet: a sort's literal check (§7.5), an operation's conditions (§7.8), a bound parameter's manifest variable (§1.46). Each addition keeps the standing of its own passage. `[open]`

**§2.5 Identity.** A node is a value of the evaluator: the store's graph is the evaluator's interned values, and node identity is `same`. A sort's declarations are in its signature; a bound argument's multiplicity is in its operation's signature. By default the id of a declared symbol is its theory's id with its position in the theory; names are metadata. `[decided]` Open: identity across versions of a theory. `[open]`

The five readings below are proposed. The record shapes await the slice 1 test (§2.1).

1. A theory's id is made from its content, not assigned: the store is addressed by content (§5.1).
2. A theory's symbols are of all three forms: those it declares, and the defined and evaluated symbols it supplies. Its operations in the sense of §1.2 are its symbols of kind op, constructor and effect (§1.6), with its defined and evaluated symbols, each carrying an operation's signature; its rules are those of its defined symbols.
3. A defined or evaluated symbol names no theory and is identified by its content (§1.33): the theory names it, and one definition may be among the symbols of two theories.
4. A theory may use a symbol it does not declare: a node holds the symbol itself, by its identity, so a declaration or rule refers directly to a symbol of another theory in the store. Referring makes it no member. The record keeps no table of imports and none of what a theory shows; how the written form names another theory's symbols goes with the notation. The identities of the symbols a theory's declarations mention are part of those declarations' content.
5. Positions are assigned by one supplied order across all kinds of declarations. This is a record proposal, not a decision that presentation order changes theory identity; neither canonical nor supplied order follows uniquely from the default above. Two declarations may share a display name at record level and stay distinct by position; explicit references identify which is meant. Whether the written form permits that spelling, and how an ambiguous name resolves, belongs to the notation. No position is promised stable across versions. `[proposed]`

Open, for the project owner: what makes a theory the same theory, that is, which of its content its id is made from, and with it whether reordering the same declarations changes the id. `[open]` Open: the bytes hashed, canonicalization, and the device keeping a theory's id and its declared symbols' ids from resting on each other. `[open]`

**§2.6 Applied sorts.** The identity of an applied sort is the tuple of: the exact family declaration's identity; the identities of the resolved sort arguments, in order; the ordered term-index nodes after substitution. For a family declaration $F_d$, resolved sort arguments $S_1, \dots, S_j$ and term-index nodes $i_1, \dots, i_m$ after substitution,

$$\mathrm{AppId} = \bigl(\mathrm{id}(F_d),\ \langle \mathrm{id}(S_1), \dots, \mathrm{id}(S_j) \rangle,\ \langle i_1, \dots, i_m \rangle\bigr),$$

so sort arguments enter by identity and index terms as the nodes themselves. Index terms are compared as written; references are used under their exact canonical/hash profile. A concrete declaration generated for a closed application takes that application's identity once a check establishes that it is the complete declaration got by substituting the exact sort arguments and term indices into that family: an exception to the default identity by declaring theory and position. Two modules expanding the same application of the same family must produce the same identity. `[proposed]`

**§2.7 Recursion.** The content hash of a defined symbol whose rules name itself, or of several that name each other: hash the group together, each member written as its position in the group (not run). `[proposed]` Open: the bytes hashed. `[open]`

<a id="ch-3"></a>

## 3. The tracking claim

**§3.1 Setting.**
Notation: $\gamma(n) = \{v \mid \mathrm{names}(n, v)\}$; $\tilde t$ is the term $t$ on names; $\mathrm{Out}(t)$, $\mathrm{Runs}(t)$ are the outcomes and runs the meaning of $t$ allows; $\mathrm{obs}(r)$ the ordered observations of run $r$; $\sim$ is "related" ($\mathrm{names}$ at $S$, C2 at $O$); $K$ is a continuation.
A hidden sort $S$, names $N$, the relation $\mathrm{names}(n, v)$ ("name $n$ stands for value $v$") of a representation $\rho$, a signature $\Sigma$, and a tracker $\tilde f$ for each operation $f$ in it. An observed sort $O$ is one the client can read. `[decided]`

**§3.2 Inclusion.**
Trackers do on names what operations do on values: every outcome on names matches a permitted meaning outcome under the stated relation,

$$\forall \tilde o \in \mathrm{Out}(\tilde t).\ \exists o \in \mathrm{Out}(t).\ \tilde o \sim o$$

The claim does not say the two have the same outcomes. `[decided]` Here the observed inputs and the tracking relation are fixed. Forward tracking must match for each compatible hidden input fixed in advance (§3.7). In backward tracking, fix a finite run on names and any compatible final meaning configuration. A witness chooses a compatible predecessor at each step, preserving the observations. B1 checks that the resulting start was allowed (§3.8). `[decided]`
How often an outcome occurs is not carried by inclusion, and on an infinite carrier an equal law does not give inclusion either, so a program that draws owes both. `[proposed]`
Illustration: the meaning draws $x$ uniformly from $[0, 1]$ and returns it; a tracker that returns 2 when $x = 0$ and $x$ otherwise has the same law, and 2 is no outcome of the meaning.
Case: $\mathrm{Out}(t) = \{0, 1\}$ is tracked by a tracker that always gives 0, and by one that always gives 1. Changing between them changes what a client sees (§11.2).
When a proposed replacement claim is first used, name the comparator (the public contract or the earlier body) and the observations the comparison preserves. In the case above a contract permitting 0 or 1 admits both constant bodies, while replacing the always-0 body by the always-1 body changes the old body's answer. Body reads: §5.2. `[proposed]`

**§3.3 Two runs at once.**
Compare both sides through the observations required by the tracking claim. If every tracker run has a matching meaning run and the comparison preserves a pair predicate $\Phi$, a guarantee of $\Phi$ for every pair of meaning runs transfers to every matched pair. At two inputs, disjoint sets of outcomes under that comparison stay disjoint; equality of the sets need not survive selection. A stronger property needs its own scoped claim. `[decided]`
Case: a meaning that may give either bit at either secret, $\mathrm{Out}(t(z)) = \{0, 1\}$ for $z \in \{0, 1\}$, is tracked by one that gives the secret, $\mathrm{Out}(\tilde t(z)) = \{z\}$. `[decided]`
What a caller observes at a boundary, the public law and the two-run description, with a worked boundary: §3.19 to §3.22.

**§3.4 One form.**
One form, forward or backward, for all operations on a hidden sort and for all hidden sorts of $\rho$. Mixing forms is unsound. Values chosen together are represented together, under one relation on the tuple. `[decided]`
Open: a licence for mixed forms where the graph of which witness depends on which has no cycle (not run). `[open]`
Case: hidden sorts $F$ (forward) and $B$ (backward), each with values 0, 1 and one name for both. `make` gives $\langle 0, 0 \rangle$ or $\langle 1, 1 \rangle$, its tracker the two names. `test(x, y)` gives whether $x = y$, its tracker false. Checking the two components under separate quantifiers admits that answer, yet `test(make())` is true in the meaning and false on names. `[decided]` A representation that fits neither form alone may instead be given as a chain of links, each in one form, and is then kept as a chain (§14.2). `[decided]` Illustration: one hidden sort that both forgets detail and settles a choice late. In the meaning, `init()` picks a bit $b$ and holds $(b, c)$ with $c = 0$, `inc` adds 1 to $c$, `par` returns $c \bmod 2$ and `reveal` returns $b$; the implementation holds $c \bmod 2$, and draws $b$ at the first `reveal` and keeps it. The forward form alone fails at `reveal`: by F1 the name `init` gives stands for some value, whose bit is settled, and the tracker of `reveal` may draw the other bit (F3). The backward form alone fails at the second `inc`, which comes back to the name `init` gave: by B1 and B0 that name stands for some $(b, 0)$, and `inc` never gives $c = 0$ (B2). Two links pass, each in its own form: a backward link naming the values by the drawn bit, if any, and the exact $c$, and a forward link naming those names by the implementation's names, the drawn bit, if any, and $c \bmod 2$.

**§3.5 Common clauses C1 to C3.**

- C1, sorts. $\tilde f$ has the sort of $f$ with $S := N$. `[decided]`
- C2, observed results. At $O$, $\tilde o \sim o$ means $\tilde o = o$. In a lax representation it may instead mean $o \in \tilde o$, the tracker's answer being a set of stated width. `[decided]`
- C3, signature. A term is covered only if every operation it applies at $S$ is in $\Sigma$, with each of its clauses, at the site of use: yes; or unknown and tested by a guard whose other branch is covered; or unknown and assumed by name within the bound. A no licenses nothing. An assumed clause stays unknown: it is an entry of the manifest's second source (claims settled never, by name, §1.43) and a selection in the semantic part of the lock. No clause that discharges a machine-model condition is assumed (§4.13). (assumption by name goes with §7.6) `[decided]`
- $\rho$ is a candidate at a site only if each tracker's own conditions are yes there, or tested there with a branch as §3.6 allows. `[decided]`

**§3.6 Cover.**
A tracker owes its clauses where its own conditions hold, and no more. The plan owes cover: at each site, for every call the operation's own conditions admit, the chosen tracker's conditions are yes, or tested with a branch to another representation, and each branch chosen has its clauses yes, guarded or assumed as C3 allows. The default representation covers every admitted call of an operation that has a way to run (§10.1); it supplies no way to run. No assumption removes a test on a machine-model condition. Cover does not say that a call returns. The answer not taken: $\rho$ owes that its trackers are defined wherever their operations are, and one that is not brings its own fallback or is refused. `[decided]`

**§3.7 Forward form (the world chooses the value): F1 to F3.**
A name may stand for several values, and what is said must hold for each. Layouts, analyses, invariants and quotients take this form.

- F1, start. For each $c$ making a value of $S$ from observed arguments $a$: $\mathrm{names}(\tilde c(a), c(a))$. Where a start can give several results, F1 reads as F3 reads a step: every result of the start's tracker names some result of the start, $\forall \tilde n \in \mathrm{Out}(\tilde c(a)).\ \exists v \in \mathrm{Out}(c(a)).\ \mathrm{names}(\tilde n, v)$, with any observed results related as in C2. As with any tracker, one that settles the start's choice is a selection under §11.2.
- F2, step. If $\mathrm{names}(n, v)$ and $\tilde f$ is defined at $n$, then $f$ is defined at $v$, observed results are related as in C2 and hidden results related.
- F3, open choices. F2 holds for every outcome of $\tilde f$ and asks for some outcome of $f$: $\forall \tilde o \in \mathrm{Out}(\tilde f(n)).\ \exists o \in \mathrm{Out}(f(v)).\ \tilde o \sim o$.

F2 and F3 in one line, writing $n \xrightarrow{\tilde f,\, \tilde o} n'$ for a step of the tracker with observed result $\tilde o$ and hidden result $n'$, and likewise for $f$:

$$\mathrm{names}(n, v) \wedge n \xrightarrow{\tilde f,\, \tilde o} n' \ \Rightarrow\ \exists o, w.\ v \xrightarrow{f,\, o} w \ \wedge\ \tilde o \sim o \ \wedge\ \mathrm{names}(n', w)$$

By F1 and F2 no reachable name is empty. `[decided]` F3 qualifies the step clause F2.

**§3.8 Backward form (the realiser chooses the value): B0 to B3.**
A name stands for values still to be chosen among. An implementation that settles a choice later than its specification takes this form. `[decided]`

- B0, non-empty. $\gamma(n) \neq \emptyset$ for every $n$ reachable through $\Sigma$. `[decided]` To cover a run without end, also $|\gamma(n)| < \infty$. Without it the claim speaks of each finite stretch of a run, and whether the whole run ends is a separate claim about the client. `[decided]`
- B1, start. $\mathrm{names}(\tilde c(a), v) \Rightarrow v \in \mathrm{Out}(c(a))$. `[decided]`
- B2, step. If $\tilde f$ takes $n$ to $n'$ with observed results $o$, then $\forall w \in \gamma(n').\ \exists v \in \gamma(n)$ such that $f$ takes $v$ to $w$ with the same $o$. The $\exists$ is discharged by a witness term that a proposer supplies and the kernel checks. `[decided]`
- B3, use once. $S$ is use-once for the client. Copying, if wanted, is an operation of $\Sigma$ with clauses of its own. `[decided]`

B2 in the notation of §3.7, with the same observed result $o$ on both sides:

$$n \xrightarrow{\tilde f,\, o} n' \wedge \mathrm{names}(n', w) \ \Rightarrow\ \exists v.\ \mathrm{names}(n, v) \wedge v \xrightarrow{f,\, o} w$$

Case for B0: the meaning picks a natural number, and `tick` counts it down, printing `a` until it prints `stop`. One name $n$ stands for every natural, $\gamma(n) = \mathbb{N}$, and its tracker prints `a` for ever. Without finiteness B0 to B3 all pass, every run of the meaning ends, and the run on names does not. `[decided]` The reason: each finite stretch of the run on names is matched by any natural large enough, and no one natural matches the run without end.

**§3.9 Configurations.**
A step compares whole configurations, including the relations among live hidden values. `[decided]` Write $I(\mathcal C)$ for their identities. Then $I(\mathcal C^{\prime})=(I(\mathcal C)\setminus\mathit{consumed})\cup\mathit{made}$. The step must also preserve what holds between surviving values as its relation requires. An operation with no hidden result keeps an old name only where its value survives. If the resulting configuration has no live values it is empty and related to itself. No live use-once value is dropped and no state is copied. Slice 4 owes the test of how the obligation generator learns what each operation consumes and keeps. `[proposed: working rule]`
Case: `finish` consumes a use-once bit and prints it, and one name stands for both bits. With the name still there after `finish` no relation passes B2, yet the tracker is right. `[decided]` Illustration: let `finish` print 1 on the name for both bits and leave the empty configuration. For that final configuration, B2 chooses the predecessor bit 1, which accounts for both the consumption and the observation. Requiring the very same run to start from a previously fixed bit 0 would impose a forward obligation.

### Stores and continuations

Every `[proposed: working rule]` item here was checked on two finite models (§23.2 rows 13 and 14).

**§3.10 B3 behind a store.**
B3 does not mean every object that chooses late must be passed linearly. Where the hidden state sits behind an effect such as a store, the effect's order threads the name, and the client copies a reference, not the name. (as a reading) `[decided]`
B3 then holds where the state of the store's handler, which holds the name, is a use-once value, and the check accounts for every place that state is held: environments, handler frames a continuation has captured, other names for the state, and the activations it belongs to. The name is a use-once pattern variable in each rule of the store's handler, so by clause (b) of the use-once check (§1.14) the rule uses it once and hands on the name its tracker returns. `[proposed: working rule]`

**§3.11 What a continuation holds.**
The continuation $K$ that handler $H$ receives for an operation performed at $q$ is the part of the run between $q$ and $H$. With $H_s$ the store's handler and $\sqsupset$ for "encloses":

$$K \text{ holds the store's state} \iff H_s \text{ is live in that part} \iff H \sqsupset H_s \sqsupset q$$

A handler inside the store's scope gets a $K$ that does not hold the store. So does one whose $K$ only goes on to make a store later: it holds code that makes one, and no state. `[proposed: working rule]`

**§3.12 Use-once continuations.**
A $K$ that holds use-once state is a use-once value in the rule that receives it, whether or not its text names the state, whatever multiplicity the operation declares. By clause (b) the rule runs it exactly once: never resuming, or resuming twice, is refused. Handing $K$ on is passing a use-once value: to a parameter declared to be run once, or to an operation whose rules are in the term, where every rule that can take the call passes the check with that parameter read as use-once. One passing rule is not enough; where the check cannot tell which rules can take the call, it is every rule. `[proposed]`
A selected interpretation, and a lowering, keep the same count (§8.10). `[proposed: working rule]`
The known-rule alternative is a check at one call. Open: its caching, and its relation to the declared-one boundary of §1.16. `[open]`
§1.24 covers a rule that answers a failure. The alternative scope ban is discouraged. In the fixture, the restricted version corresponding to §3.13 used alone refused 87,196 of 92,176 right terms (§23.2 row 6).
Case: one name stands for 0 and 1; reading it gives 0 with a name for 0, or 1 with a name for 1. Returned name handed on: two reads give $\langle 0, 0 \rangle$ or $\langle 1, 1 \rangle$. Old name used twice: all four pairs. The order of the reads is the same in both.
Case: an operation declared any, used inside one store and answered by an enclosing handler that resumes once, is a right term. The declaration alone does not refuse it.
Whether $K$ holds use-once state depends on every place the operation is performed, not on the text of the receiving rule. Where the check of a rule of a handler in the term cannot show that its $K$ holds none, it reads $K$ as use-once (handler not in the term: §3.13). Short of refusing the rule, only this reading keeps the promise of §1.22. (how many right rules it refuses is not counted) `[proposed]`

**§3.13 Handler not in the term.**
That is: the operation is performed by a bound argument, or answered by an interpretation selected later, or by a handler outside the term being checked. Nothing can be counted, and the declaration decides: inside the scope of a store's handler such an operation may be used only if its continuation's multiplicity is declared one, and by §1.14 whatever answers it resumes exactly once. This ban by scope is sufficient and not exact: it says only that the check cannot tell, not that $K$ holds the store. An operation that narrows a choice returns a new name; a new name alone is no evidence of B3. A failure or resource stop inside the scope is owed as §3.15 says. (the fallback where the recipient is not known, and the limits on capture and its cache, stand) `[proposed: working rule]`
The same ban, again sufficient and not exact, holds wherever else a use-once value is held between such an operation and the edge of the term: in an environment, in a frame that waits with an argument already obtained, or in handler state (§9.3). It adds no refusal to slice 1, where §1.30 says what may wait across the output under the narrower rule. (how many right terms it refuses is not counted; the case joins the census owed under §9.3) `[proposed]`
Case: `consume_pair(make_handle(), helper())`; `make_handle` gives a use-once value, `helper` performs an operation declared any. Handler in the term: $K$ holds the frame that waits with the handle, so it is use-once in the handler's rule, and resuming twice is refused (§3.12, §9.3). No handler in the term and no store: under the working rule alone the declaration decides, and an interpretation selected later could resume twice and consume the handle twice. Under the proposed one the term is refused unless the continuation is declared one. `[proposed]`

### Lax representations

**§3.14 Resolution and width.**
A lax representation is in the forward form and may add two claims, with $\mathrm{w}$ a width. Resolution, for each value $v$ in scope and each requested width $\varepsilon$: $\forall v, \varepsilon.\ \exists n.\ \mathrm{names}(n, v) \wedge \mathrm{w}(\gamma(n)) \le \varepsilon$. Width: a stated bound on how much a tracker widens its answer. A request for a result to a given precision is a claim about the result's name, checked on the result. A representation whose resolution claim is no is refused such a request before it runs. `[decided]` Illustration: the positive intervals $[1,2]$ and $[1/2,3/2]$ both have width 1. Their reciprocal images are $[1/2,1]$ and $[2/3,2]$, of widths $1/2$ and $4/3$. More generally, the image of $[a,a+1]$ has width $1/(a(a+1))$, unbounded as $a$ tends to zero from above. A finite bound depending on input width alone can hold on domains bounded away from zero.
A width claim, like every clause, is stated for $n, v$ with $\mathrm{names}(n, v)$, and says nothing where $\gamma(n) = \emptyset$. $\rho$ may offer a decided predicate on names that every constructor's tracker establishes and every tracker keeps, as evidence for a claim that would otherwise range over all names. That it is kept is a clause to be checked. `[proposed]` The general form of a width claim is open. `[open]` Before slice 3 fixes it, check that it can express dependence on input widths, values and domains, and the direction of a one-sided bound. `[proposed]`

### Clauses for effects

**§3.15 Operation with a continuation.**
The clauses above are for operations that return. Five more cover those that may not. `[decided]`

$$\frac{\tilde a\sim a \quad \tilde c\sim c \quad \tilde h\sim h \quad \forall(\tilde x,x).\ \tilde x\sim x\Rightarrow\;\tilde K_{\tilde c,\tilde h}(\tilde x)\sim_{\rm run} K_{c,h}(x)}{\tilde f(\tilde a,\tilde K)\sim_{\rm run} f(a,K)}\ \textsf{(B-Cont)}$$

Here $c,h$ and their tilded counterparts are the captures and handler state. Whole-run relatedness $\sim_{\rm run}$ requires that for each run $\tilde r$ on names there is a run $r$ of the meaning, as the form requires, with $\mathrm{obs}(\tilde r) = \mathrm{obs}(r)$ in order, then related results or the same failure, and the same consumption of each use-once value. Runs are compared as wholes: related results of $K$ say nothing of how often it ran, or of what it captured. Runs without end and one-sided steps: §3.18. Resource stops: §3.17. The design adopts this comparison. One finite reading with stateful callbacks was run and reviewed (§23.2 row 16). `[decided]`
Case: a handler that resumes twice, or never, is handed the same continuation as one that resumes once, and the three runs print different things.
Open: the general clause. `[open]`

**§3.16 Failure.**
A failure is an observed result. Where $f$ fails, $\tilde f$ fails, with payloads related as results are (by C2 at $O$, with equality in its exact case). A failure no client catches is reported by the host, so its payload is observed unless the host's theory reports none. $\tilde f$ does not return where $f$ fails, and adds no failure of its own except by the resource clause. `[decided]`
Slice 1: the host reports an uncaught failure with its payload and what it held. The payload is observed, so trackers failing with different observed payloads are told apart. `[decided]`
Open: the rest of the host theory and system-call model, the host completion interface, and the identity and ownership interface for held or returned use-once values. `[open]`

**§3.17 Running out of a resource.**
Open: the same outcome, or the realiser stops where the meaning does not; the resource is named in the manifest. (finite checks of agreement at a stop were run and reviewed, §23.2 row 15; the whole clause has no test and no proof) `[open]`
Slice 1: memory is a permitted resource for a compiled stop, under §8.10 and §8.12: the compiled run's requests are an ordered prefix of the reference's with equal observed arguments, and each value the compiled run consumes is consumed by the reference, and no more often. A prefix alone does not suffice. The stop is recorded as stopped for a resource, never as agreement. Equal held sets are not required. `[decided]`
The stack is a resource of its own, named in the manifest on the same terms as memory in the first build. The guard that makes a stack stop clean on the C route is unqualified; an uncontrolled overflow gives no permitted-stop evidence (§10.11). `[decided]`
The applicable scope of manifests and bounds, host ownership of use-once inputs, results and values held at failure (§1.46), and the general reference/compiled consumption account remain open. `[open]` A proposed policy would specify which resource stops count and their order when two runs are compared. `[proposed]`
First compiled demo: put the reservation design first, or state that no clean stack stop is claimed. `[proposed]`

**§3.18 One-sided steps; not ending.**
Open: where one side takes steps the other does not, the relation holds across them, and a measure $\mu$ in a well-founded order falls at each, so neither side stalls the other for ever. Code for a term with a loop is a name for it only under this clause. `[open]`
Open: the tracker's run fails to end exactly where its operation's does, apart from the resource clause. `[open]`
Both are owed for the client's run and not per operation: every operation can return while the client's run on names never ends. In the backward form $\mu$ falls as the matching value is sought backward from a given step, not along the run (read, not run). `[proposed]`

### Guarantees at a boundary

**§3.19 What a caller observes at a boundary.**
A boundary's contract says what a caller may observe. By default it is public behaviour: the returned values, the visible stops, the public actions, and the state a later call can read. Exact metering, the meter's readings, is observed only where a boundary opts in, one boundary at a time. A build preset that opts in counts only if it is recorded in the exported interface and checked at link. (the four parts summarize the proposals the project owner chose) `[decided]`
Where a run ends in a failure, the failure is part of that public behaviour, as the run's result, with its payload where §3.16 observes it. (derived from §3.16 and the default above) `[decided]`
Write $\mathrm{obs}_b(r)$ for what a caller at boundary $b$ observes of a run $r$. For runs that return, fail or stop, let $p_b(r)$ be the tuple below, with each component restricted to what is public at boundary $b$.

$$p_b(r) = \langle \mathrm{ret}(r),\ \mathrm{stop}(r),\ \mathrm{act}(r),\ \mathrm{later}(r) \rangle$$

for the result (the returned values, or a failure with its payload), the visible stop if the caller sees one, the public actions, and the state a later call can read. By default, $\mathrm{obs}_b(r)=p_b(r)$. Where the boundary opts in to the named meter $\mu$, $\mathrm{obs}_b(r)=\langle p_b(r),\mu(r)\rangle$, with $\mu(r)$ the meter's readings. For runs reporting a failure, §3.16 governs the observed result and payload.
§8.10 compares requests, outcome and consumption. A fuel cut or a permitted resource stop leaves unexamined work incomplete, and any established mismatch stands. Counting a stop that only the realiser makes among the outcomes supplies no matching meaning outcome at a boundary that observes it. That comparison verdict does not establish equality for a caller's law or select an exact-meter preset for an export. (a clarification) `[proposed]`
Each exported boundary names the fuel and physical-resource stops its callers can observe, the resources involved, and which limits are fixed or selectable for the related runs; these are settled at the first boundary that names them. (the project owner's choice) `[decided]`
Reminder (operational note with no design standing). The project owner's answer of 2026-11-22 settles how published functions state the work and construction limits: one rule for every export, the two allowances at an export below. Each boundary still identifies the stops its callers can observe, including any visible stop from a nested call. Reconsider those outstanding visibility questions, physical memory and stack stops, and slice 2's bounds at the first of these landmarks. (1) Design work begins on slice 2's manifest bounds (§19.8), or an earlier exported boundary names an observable fuel or physical-resource stop. Slice 1's working rule uses one fixed manifest bound (§1.46). (2) A replacement is first checked at a stated fuel limit under this section's rules, possibly at slice 2's first rewrite (§19.8). The boundary's contract identifies what its callers can observe at that limit. (3) An exported boundary first allows its callers to observe a stop raised inside another exported boundary it calls. Compare what each promises its own callers and ask whether a common rule would help. If no landmark has prompted a review, the end of February 2027 is a suggested date to check back.

**The two allowances at an export.** Every published function uses the same format to state its work and construction limits. For each limit it publishes its own finite value or default, or requires the caller to supply the value. It names which limits are fixed or selectable. `[decided]` The proposed interface also identifies the reference meter profile and publishes the permitted range for a selectable limit. `[proposed]` It names visible work, construction and permitted physical stops, as well as whether each meter reading is exported. Exact readings are private unless this boundary opts in to the named meter (this section's opening paragraph). The public consequences of exhaustion and of spending a shared remainder still count. A preset is part of the linked interface. `[proposed]` $0$ is a valid grant on either axis. On a fresh invocation an omitted axis takes its fixed value or its published default. `[decided]` An absent required value, an out-of-range selection, or an unresolvable profile is a configuration refusal before entry. `[proposed]` There is no implicit unlimited grant, conversion from one axis to the other, or machine-derived default. `[decided]` For example, an interface can fix work at 40 and accept construction from 0 through 8 with default 4. An omitted construction offer gives (40,4), while an explicit zero gives (40,0). These illustrate a contract, with no numerical preset imposed on other exports. A scalar historical record keeps its own profile. `[proposed]`

An inner call can only tighten the work and construction allowances its caller has left. `[decided]` An ordinary nested call shares the enclosing remainder. At a nested export, resolve each fixed or selected limit as a local maximum. On each axis use the lesser of the enclosing remainder and that maximum less spending since entry. `[proposed]` An internal call with no separate cap just inherits the remaining pair. Charge a successful event once to the run and count the same spending against each enclosing local maximum. On return only actual spending has reduced the caller's remainder. Identify the limiting scope in a cut, using the outermost of tied scopes for the primary axis. This is a cap on the call. Independent reserves for siblings require their own contract. `[proposed]`

A return and a visible stop can distinguish two providers even at a boundary that hides both balances. A cut confined to a checker can leave its claim unknown. Equal reference charges can accompany different physical peaks. An exact-meter opt-in names its profile, fields and scope. An operational change under §1.37, §11.3 or §12.2 owes the observations promised by affected boundaries, including an enclosing boundary. `[proposed]`

Fix a deterministic returning reference path, a common admitted start, a fixed profile and any identical replies. Suppose the path and its prices do not inspect its grants, no other stop intervenes, and allowances are shared by this one run without a tighter internal cap. If its successive prices are $(w_i,c_i)$, the pairs at which it completes are precisely

$$\{(W,C)\in\mathbb N^2 : W\ge\sum_i w_i\ \land\ C\ge\sum_i c_i\}.$$

Under those hypotheses the two minima are the path's two charges. A probe at one pair only establishes whether that pair suffices. Hold construction ample in the hidden-bit case below: identical results at work charges three and five separate when work is three or four. Hold work ample to test a construction threshold in the same way. `[proposed]`

Case: a provider whose cost depends on a hidden bit, three steps at one value and five at the other, with the same result at both. Under a limit of three or four steps one run returns and the other stops. `[proposed]`
By default a replacement must give equal public observations to every permitted caller at the same fuel limit, including what callers can do with leftover fuel; existing equal-observation promises keep equality. A boundary whose callers explicitly opt in to directional progress on a named fuel allowance may let a cheaper version finish where the old one stopped, never the reverse: the cheaper version must give the answer the old version gives with more fuel, preserve every request already made, and send nothing to the host that the contract does not already permit at that limit. Laws relating pairs of runs (hidden inputs; §3.20, §3.21) are always checked separately on the actual deployed versions, including mixed old and new. The reference checker keeps any promised fixed-fuel verdict while callers may accept extra completions. At the first proposed use of directional progress, one uniform-saving positive case and the hidden-selective and host-publication negative cases are required at the same stated limit; if unresolved, the plain path is kept. (the project owner's choice) `[decided]`

In the paired profile “the same fuel limit” means the same pair under the same profile and fixed or selectable limits. Check public actions, subsequent uses of both remainders, and relational laws even when neither reading is public. A directional-progress opt-in must identify the axis or axes and its guarantee at each permitted pair. A reduction of work cannot excuse a newly refused construction or an earlier visible action. Use the existing controls with the other axis held fixed and with both axes tight. `[proposed]`

**§3.20 One public law, and two ways to earn it.**
The caller's guarantee about what may be learned across a boundary is stated as one public law in the boundary's contract. A provider earns it in one of two ways: by a direct proof of the law, or by a checked access restriction. `[decided]`
The law says that two runs from starts the contract relates give the same observations under the observer of §3.19, in the reading §3.21 states. A checked access restriction is a checked limit on what the provider may ask of its arguments, so that it reaches what the law hides only through the operations its contract allows (§14.4). One sufficient argument checks this provider's access, including the primitives it can reach, and shows that the allowed operations and their composition preserve the required relation under the declared observer and shared choices. §14.4 supplies a first-order tracking result under its own premises. Using it for the caller's every-pair law requires the corresponding two-run argument. §14.6 remains to be tested. A theorem for the language that gives that argument once, for every provider that keeps the restriction, is owed. An exhibited violating pair refutes the law. A missing proof or an inapplicable restriction leaves the guarantee unchecked. A wider conditional guarantee must carry its named assumption under §13.13. (an application) `[proposed]`
Under the claim's stated assumptions, let $\chi$ range over the shared choices permitted by the contract. The run sets cover the declared outcome scope, including every stop visible to this observer.
With $R$ the start relation of the contract, $\chi$ what the two runs share (§3.21), and $\mathrm{Runs}(t(s) \mid \chi)$ the runs of $t$ from start $s$ with shared part $\chi$, the law reads

$$\forall (s_1, s_2) \in R.\ \forall \chi.\ \forall r_1 \in \mathrm{Runs}(t(s_1) \mid \chi).\ \forall r_2 \in \mathrm{Runs}(t(s_2) \mid \chi).\ \ \mathrm{obs}_b(r_1) = \mathrm{obs}_b(r_2)$$

A violating pair is two such runs with $\mathrm{obs}_b(r_1) \neq \mathrm{obs}_b(r_2)$.

**§3.21 The two-run description.**
A claim about two runs states its two-run description: the two sides; the start relation; the observer (§3.19); the outcomes compared, with the stops the observer sees among them; the assumptions; what the two runs share, such as availability and timing that come from the environment and not from the input; and, for each claim, which runs must match which: every pair of runs, which inclusion carries (§3.3), or each run of one side by some run of the other, which it does not carry. Both are fields of any exported certificate. A caller's guarantee across separately compiled boundaries is of the every-pair kind. Representation correctness is of the each-by-some kind. §3.3 links the two. It covers stops only if stops are outcomes, or if the representation adds none (§14.3). The two are not written as permanently separate: whether one theorem covers both is deferred, theorem later. The fields are needed no earlier than the first exported interface or certificate format. `[decided]`
As a record, $\delta = \langle \mathit{sides}, R, \mathrm{obs}_b, \mathit{Out}_b, \mathit{asm}, \mathit{Sh}, m \rangle$, where $\mathit{Sh}$ is the set of values the shared part can take (one value where nothing is shared) and $m$ is $\forall\forall$, every pair, or $\forall\exists$, each by some. Under $\mathit{asm}$, fix a permitted shared choice $\chi$ and use the runs for the declared outcome scope $\mathit{Out}_b$, including visible stops. With $X_i(s)$ the runs of side $i$ from start $s$ at the shared part $\chi$, the claim says of every $(s_1, s_2) \in R$ and every $\chi \in \mathit{Sh}$ what $m$ requires. For a claim whose comparison is equality of the declared observations, the two matching patterns are

$$\forall\forall:\ \forall r_1 \in X_1(s_1).\ \forall r_2 \in X_2(s_2).\ \mathrm{obs}_b(r_1) = \mathrm{obs}_b(r_2) \qquad \forall\exists:\ \forall r_1 \in X_1(s_1).\ \exists r_2 \in X_2(s_2).\ \mathrm{obs}_b(r_1) = \mathrm{obs}_b(r_2)$$

For another comparison, use the relation stated by that claim in place of equality.
Illustration: inclusion carries $\forall\forall$. If every run of a realization is matched by a meaning run from the same start, at the same shared part, with the same observations, two realization runs $\tilde r_1, \tilde r_2$ have matches $r_1, r_2$, and $\mathrm{obs}_b(\tilde r_1) = \mathrm{obs}_b(r_1) = \mathrm{obs}_b(r_2) = \mathrm{obs}_b(\tilde r_2)$. It does not carry $\forall\exists$: with $\mathrm{Out}(t(0)) = \mathrm{Out}(t(1)) = \{0, 1\}$ each run from one secret is matched by some run from the other, while the tracker of §3.3, with $\mathrm{Out}(\tilde t(0)) = \{0\}$ and $\mathrm{Out}(\tilde t(1)) = \{1\}$, returns 0 from secret 0 and only 1 from secret 1.
Case: the case of §3.3, a meaning that may give either bit at either secret, with the promise that the result shows nothing of the secret. At each secret the meaning permits both bits, so its sets of outcomes are equal across secrets. The secret-returning tracker passes the ordinary per-run test when each matching meaning run may choose its own bit. Two independent meaning runs can return different bits and fail the caller's every-pair guarantee. When the two meaning runs must return one shared environmental bit, their results agree. To refute the tracker as a refinement at that shared choice, the tracker and its matching meaning run must also preserve it. At shared bit 0 and secret 1 the meaning returns 0 and the tracker returns 1. `[proposed]` Illustration: with the shared bit $\chi$ the meaning is $t(z \mid \chi) = \chi$ and the tracker $\tilde t(z) = z$. A match that keeps $\chi$ fails exactly where $z \neq \chi$, at $(\chi, z) = (0, 1)$ and $(1, 0)$; a match free to choose its own bit finds the tracker's $z$ in $\{0, 1\}$ at every secret.

**§3.22 A worked boundary for §3.19 to §3.21.**
Case: a provider exports a counter: a hidden sort with the start zero, the updates tick and double, and the question div3. Its meaning keeps a number modulo six; tick adds one, double doubles, and div3 says whether the number is divisible by three. Its contract states one public law: two counters whose numbers agree modulo three give the same answers to div3 after any sequence of updates. That law is what lets the provider keep three states in place of six.

- What a caller may observe: the answers to div3 after any updates, under the default of §3.19. This finite example compares completed operations under the same public update sequence with sufficient resources. Each operation gives one result, emits no public action, and exposes later state only through the stated queries. The meter is not observed, since the boundary has not opted in.
- What the provider checked: a direct proof that agreement modulo three is kept by tick and double and decides div3, which a finite check over the six numbers settles (§14.5, the forward form, with agreement modulo three as the relation). The three-state implementation starts at zero. Reduction modulo three preserves the start, commutes with both updates, and preserves the answer to div3. Those checks establish the every-pair law for related counters under any common sequence of updates and give the corresponding meaning run for each tracker run in this example (§3.21). The other way of §3.20, a checked access restriction, is not used here.
- What breaks when the observer changes: add the question even. The numbers 1 and 4 agree modulo three, and even answers false at 1 and true at 4. That pair refutes equal observations for the expanded interface, so no provider of this meaning earns that law (§3.20). The div3-only law still holds. The three-state representation cannot answer both queries for every reachable state. From zero all six numbers can be reached, and with div3 and even every two of them are told apart by some sequence of updates, so no fewer than six states serve. Opting the boundary in to exact metering changes the observer too: a body that keeps three states and one that keeps six may then differ to the caller where they cost differently, so replacing one with the other needs a claim about cost as well (the comparator of §3.2).

(the numbers checked by a finite program) `[proposed]`

Illustration: on $\mathbb{Z}_6$, $\mathsf{tick}(x) = x + 1$, $\mathsf{double}(x) = 2x$ and $\mathsf{div3}(x) \iff 3 \mid x$. The relation is $x \mathrel{R} y \iff x \equiv y \pmod 3$, and the reduction $q(x) = x \bmod 3$ into $\mathbb{Z}_3$ satisfies

$$q(0) = 0, \qquad q(x + 1) = q(x) + 1, \qquad q(2x) = 2\,q(x), \qquad \mathsf{div3}(x) \iff q(x) = 0$$

because 3 divides 6, so $q$ respects sums and products. For every sequence $w$ of updates, $q(w(x)) = \tilde w(q(x))$, with $\tilde w$ the same updates on $\mathbb{Z}_3$; hence $x \mathrel{R} y$ gives $\mathsf{div3}(w(x)) = \mathsf{div3}(w(y))$. With even added, the answers $(\mathsf{div3}, \mathsf{even})$ at $0, 1, \ldots, 5$ are $(1,1), (0,0), (0,1), (1,0), (0,1), (0,0)$. Only the pairs $\{1, 5\}$ and $\{2, 4\}$ agree at once, and one tick separates both, so the six states are pairwise distinguishable.

<a id="ch-4"></a>

## 4. Claims

**§4.1 The claim record.**
Every fact in the store is a claim, and a claim never says more than its statement. A sort membership, a law at an interpretation, a tracking clause, a covering fact and a width are all claims. A claim $\kappa$ has these fields. `[decided]`

| Field | What it holds |
| --- | --- |
| Statement $\varphi$ | A proposition whose quantifiers name their domains. Its scope is part of what it says |
| Status | $\mathsf{yes}$, $\mathsf{no}$, $\mathsf{unknown}$ or conflict. A reading, not stored (§4.2). `[decided]` |
| Evidence | One of three kinds: a derivation; a run record (program, input, output, step bound, the build that ran it); a counterexample, which may be a set of values. In the paired profile the step bound is the pair of grants, and the record also names the meter and gives the stop, if any, and both remainders (§15.9). `[proposed]` |
| Assumptions | The claims the evidence used and did not discharge. Evidence with assumptions is a rule |
| Manifest | The polynomial of §1.47 |
| Settled | When, and by which route: at build, at load, once in a run, at each evaluation of its site, or never |
| Notes | The notes about this claim. A note is not evidence, and no licence can cite one |

In the assumptions row "rule" is the ordinary word, not the rule of a theory (§1.5). Evidence with assumptions shows its statement where its assumptions hold, and §4.5 reads it so, each assumption replaced by the site's own evidence. It is no step of the reference run and no rule of a theory. `[proposed]`

**§4.2 Status is a reading.**
Evidence is never changed or removed. The status of a claim is a reading of its evidence, by §4.5:

$$\mathrm{status}(\varphi, \text{site}, \text{bound}, \text{store state}) \in \{\mathsf{yes}, \mathsf{no}, \mathsf{unknown}, \text{conflict}\}$$

For a fixed statement its status depends on the site, bound and store state. No separate status is stored. Where admitted evidence gives yes and admitted evidence gives no for one statement at one site, the reading is a conflict. A conflict licenses nothing. Its message gives both pieces of evidence with their manifests and does not say which is at fault: something one of them rests on, in its manifest or in the trusted base, is false. Owed: the test of the records that this reading of status and of a conflict needs. `[decided]`
Case: evidence for $P$ licenses a plan, and evidence against $P$ arrives later. The hash of the first is unchanged, the old build still replays, and a new build reports the conflict. `[decided]`

**§4.3 Runs as evidence.**
A run becomes evidence by one of three rules, Eval, Close and Reflect (§13.7). In slices 1 to 3 every claim is settled by a run; derivations arrive in slice 4. `[decided]`
This is about the kind of evidence: before slice 4 no claim is settled by a derivation. A claim may still be settled never, and then it stands in the manifest by name (§1.43). Slice 1's default tracking claim is one (§1.44). `[proposed]`

### Rules on claims

**§4.4 Scope, exhaustion, membership.**
Scope. For $\forall x \in X.\ P(x)$, a yes passes to every $X' \subseteq X$ and a no to every $X' \supseteq X$. For $\exists x \in X.\ P(x)$ the directions reverse. `[decided]`
Exhaustion. Running every case counts for a sort only with a covering fact, of three kinds: the sort is declared finite with these values; the sort is declared data with these constructors; a proved claim says that an enumeration misses nothing. Without one the result is a yes for the enumerated set, by name. `[decided]` The data covering fact covers a case split by constructor. It does not make an enumeration up to a size exhaustive. `[proposed]`
Membership. Using a scoped yes at an object needs evidence that the object is in the scope. `[decided]`

**§4.5 Reading at the site.**
Evidence is read where it is used, each assumption replaced by the site's own evidence. For one piece of evidence whose assumptions read $r_1, \dots, r_j$, in this order:

1. some $r_i$ is no: the evidence gives nothing, whatever the others read. Nothing is named as missing, since settling it would not help;
2. otherwise some $r_i$ is conflict: nothing, and the conflict is reported (§4.2);
3. otherwise some $r_i$ is unknown: unknown, naming each missing one;
4. Otherwise it gives what it is evidence of: yes where it supports the statement, and no where it is evidence against it, for example a refutation (§4.7) or a counterexample (§14.7).

For one statement with several pieces: a yes from one and a no from another is a conflict; a yes with no no is yes; a no with no yes is no; where no piece gives yes or no the reading is unknown, with what each piece that gave unknown is missing. `[decided]`
Grounded support. A positive reading needs finite, grounded support. When following one chain of support would revisit the same claim at the same site, under the same bound and store state, that chain supplies no support from itself. This gives nothing from that route, not a no for the claim. Other pieces are still read: independent grounded support can give yes, and admitted yes and no still give conflict. If no piece gives yes or no the reading remains unknown, with the unresolved support identified. An assumption allowed by name remains an assumption (§1.43, §3.5, §4.13): permission to assume it is not evidence that makes it yes. The reader distinguishes an unfinished support chain from completed readings in their context, and a result that depends on the unfinished chain is not reused as an unconditional reading of the claim under §5.2. `[decided]` Illustration: with only "$P$ if $Q$" and "$Q$ if $P$" as evidence, each chain comes back to its own claim, so both read unknown; a separate proof of $Q$ then grounds $P$.

**§4.6 Backward from a no.**
A conclusion that is no, with every other assumption yes, makes the remaining assumption no. `[decided]`

**§4.7 Unanswerable.**
That a name cannot answer a question is shown by a set of values with that name, one refuting each candidate answer. `[decided]`
A refutation is a record. It names four things: one representation $\rho$ with its naming relation, one scope of values, the question with its interpretation, and the whole set $\mathcal{A}$ of answers the question admits, with any width. It holds values $v_1, \dots, v_j$, and for each $v_i$ evidence that it has the name under that relation and evidence of its answer to that question. Every piece is for those same four: that two names are one node does not by itself show that two values have one name under the relation. The reader of evidence checks each piece, checks that the names are one node, and checks

$$\neg \exists a \in \mathcal{A}.\ \forall i.\ a \text{ is right for } v_i$$

It then reads no for that name, that question and those admitted answers, and for nothing wider. What it read is recorded as §13.8 and §11.3 ask. One right answer, and intervals of a stated width, are two kinds of admitted answer and not the only ones; for the others, and for a refutation by infinitely many values, §4.8 says what evidence is owed. The $v_i$ need not be all the values that have the name. A particular pair with no common right answer is already a finite refutation. Whether every refutation of this kind has a refuting pair depends on the hypotheses in §4.8. Owed: the test of the record of a refutation. `[decided]`
Case: two braids with one name and traces 0 and 2. The no rests on two runs that give the name, two that give the traces, and the comparison $0 \neq 2$. `[decided]` Illustration: if the allowed answers instead enclose the trace in an interval of width 2, both traces fit $[0,2]$. The refutation for exact answers cannot be reused for that question.

**§4.8 When a pair suffices.**
Let $R_v$ be the set of right answers for a value $v$ that has the name. A pair suffices:

- when the question has one right answer;
- when the name stands for finitely many values and their right-answer sets $R_v$ are intervals in one ordered answer space, or for infinitely many values when all $R_v$ are closed real intervals and at least one is bounded;
- where another kind of answer brings its own checked theorem that a pair suffices.

An interval that is itself returned as an answer is not the second case: where any bounded interval that holds the value is a right answer, every finite set of values has a common answer and $\mathbb{N}$ has none. What a refutation shows is in §4.7. `[decided]` Illustration: the values $0, \dots, m$ have the common answer $[0, m]$ for every $m$, and no bounded interval holds every natural number.
Case: $R_v = \{a \mid a \ge v\}$, the numbers from $v$ up. Any two values share an answer and no number is right for all.
Otherwise any finite set of values with that name and no common right answer refutes, and it is checked by computing where the answer sort decides, for a finite set of values, whether a common right answer exists. Where no finite set will do, the refutation is the whole set of values, given by a derivation that names the covering fact for that set. `[proposed]`

**§4.9 The program that checks a refutation.**
It is an entry of the obligation generator for tracking clauses. It reads a record of the name, the question, the witnesses, a claim for each that the name stands for it, a claim for each of its right answers, and the check that no answer is right for all. It settles that this name cannot answer this question. It settles nothing about a family, and sets no status (§4.2). Each answer sort that wants refutations supplies the decided check, with a soundness claim as §13.8 asks. `[proposed]`
Case: three disks of radius 1.1 at the corners of a triangle of side 2 meet in pairs and not all three. No pair refutes, and three values do. `[proposed]` Illustration: two disks meet because $2<2.2$. Let $G$ be the centroid of the equilateral triangle with corners $p_1,p_2,p_3$. For any point $x$ the mean of the three squared distances is $\|x-G\|^2+4/3$. At least one squared distance therefore exceeds $1.1^2=1.21$, so the three disks have no common point.

**§4.10 Guards and assumptions; kinds are not ranks.**
Guards and assumptions. An unknown claim that has a test is settled at each evaluation of its site: that is a guard, and for a representation the other summand of the name sort is where the value goes when the test fails. A guard on a membership has no slower branch (§7.6). An unknown claim with no test is settled never, and shows in the manifest. `[decided]`
Kinds are not ranks. Proved for every input, computed exactly for one object, held on an enumerated set, and estimated differ in statement and in evidence. They are not points on one scale. `[decided]` "Estimated" is read as a note until the third part of §4.19 is taken up. `[proposed]`

**§4.11 What a use must assume.**
A manifest holds what the evidence leaned on. A use of the claim may need less, as the table sets out, and a bound may be stated against what a use needs. What a use must assume is read from the statement, the evidence that settled it and the site, after the reading of §4.5. The statement is read after its definitions are unfolded to a fixed core. A statement that leaves the core (by a quantifier over sets or functions, by a definition that is not unfolded, or by a check not shown to end) takes row 4. Where the evidence gives a witness for every input in the statement's scope and each witness is checked, the assumption of row 3 is not needed. A finite result sort serves the same way only with its covering fact, a search that ends, and the evidence of what the search found. Neither removes what §13.8 asks: the soundness claim of the checker that accepted a witness, and what that claim rests on, stay in what the use assumes. `[proposed: working rule]`

| Row | Form of the statement | What a use must assume |
| --- | --- | --- |
| 1 | $f(v) = w$, settled by Eval. That a checker returned yes on $P$ is such a statement | The build, and nothing else |
| 2 | A finite check that holds for every input, proved in some theory | Consistency suffices if each failing check has a refutation provable in that theory (§4.12) |
| 3 | For every input some output exists, used as a fact | That the theory proves no false statement of that form |
| 4 | Any other statement. $P$ itself, where a checker returned yes on $P$, is here: a use assumes the checker's soundness claim and what that claim rests on | The laws the manifest names |

Rows 1 and 4 are approved for the distinction between the checker’s answer and the statement checked. `[decided]` Illustration of rows 1 and 4: a checker that always returns yes establishes, even on a false $P$, the row 1 fact that it returned yes; $P$ itself needs the checker's soundness.

**§4.12 Two conditions on what a use must assume.**
First: where the finite check answers no at an input, the theory proves that it does. `[proposed]` Second: §4.11 is read after §4.5, so a law that is no at the site makes the theory inconsistent there, and the evidence still gives nothing. `[proposed]`
Until the foundation of slice 4 names a core, only rows 1 and 4 are used. `[decided]` Owed with it: the grammar of the core; which definitions are unfolded, by a procedure that ends, with a bound past which a statement takes row 4; which evidence each row requires; and for row 2 the program or derivation that turns each run that answers no into a proof in the theory. Cases the reader of evidence must then pass: a statement and its unfolding take the same row; a definition that hides a quantifier is found; a definition that names itself does not keep the reader unfolding for ever; two kinds of evidence for one statement take different rows. The answer not taken: rows 2 and 3 are used now. `[proposed: working rule]`

**§4.13 A guard on the machine model is never removed by an assumption.**
A machine theory marks the conditions its own model depends on, such as an index inside its array. A claim that discharges one must be yes, or be tested at each evaluation. It may not be settled never, whatever the bound admits: one false assumption there could corrupt the memory that every run record rests on. The same holds for every claim its evidence rests on: its manifest has no claim settled never (the manifest's second source, §1.43), and holds a declared law only if the machine theory itself declares it. The rule governs a guard and the evidence that may remove it. Wherever a test at the point of use can establish a condition, the test remains until evidence resting on no assumption replaces it. Any other guard may be removed by an assumed claim when the bound admits it, and the assumption goes in the semantic part of the lock. `[decided]` Test this formulation on a guard of the machine model.

**§4.14 The nine trusted obligations of the first build.**
For the first build, by the project owner's choice among the alternatives named below, nine named obligations remain as trust where the available checks do not establish them.

| | Obligation | Rests on |
| --- | --- | --- |
| 1 | Handle liveness | The ownership checker |
| 2 | The balance of owned references | The ownership checker |
| 3 | Issuance of a handle by this run's runtime | The printer and grammar checker |
| 4 | Valid output storage that is not an input's storage | The grammar and ownership checkers |
| 5 | Absence of undefined behaviour in printed C | The printer and grammar checker |
| 6 | Agreement of declarations with definitions | The interface checker |
| 7 | Sufficient stack reservation: the root, the next prologue, guards, enabled helpers and emergency cleanup, not merely a generated frame | The backend's frame report and the runtime's reservation and cleanup contracts |
| 8 | Correctness of the runtime's own unchecked code | That implementation, its review and tests |
| 9 | Correct translation of printed code to the machine program | The backend's tools |

A testable part of any of these still requires its check, including the interface checks before entry and the available output-address checks. Passing such a check establishes only what it checks. No blanket claim is made that the nine descriptions contain no testable facts. Each residual obligation stands in the artefact manifest as trusted (§1.45), naming its condition and the bound part of the build it rests on (§1.44). This does not make an unproved checker a proved or generally trusted text. It is not a yes, and is not an assumption of the second source that a program, a bound or a lock choice may select. It removes no available guard. It leaves the manifest only when evidence resting on no assumption replaces it. The set is closed: no program or build adds an obligation to it without a further decision of the project owner. Alternatives not selected: checked handle tickets, and freeing nothing during a run. This classification does not qualify the build or prove memory safety. `[decided]`

**§4.15 The same rule at a build's own runtime.**
The entries of a build's own runtime are also subject to §4.13 for conditions marked by the machine theory. At a call, such a condition must have a yes admissible under the rule, including its requirements on the evidence's manifest and declared laws, or be tested at that evaluation. The nine residual obligations of §4.14 are the one closed exception: each stands in the artefact manifest as trusted, is neither a yes nor a test, and removes no available guard. A checker returning yes supplies no further claim by itself: §13.8 governs its soundness claim and the scope in which a trusted text is trusted. This gives no extra checker trusted status and creates no further exception for an untestable condition (under review). `[proposed]`

### Chance

**§4.16 No confidence; draws; finite results.**
A derivation, run record or counterexample can settle a claim. The site reading can be yes, no, unknown or conflict (§4.2). No claim carries a confidence. Chance may be what a statement is about. Tracking keeps which outcomes may occur ($\mathrm{Out}$) and not how often ($\mathrm{Pr}$), so a program that promises a law owes that law as a claim of its own. `[decided]`
A proposer, resolver, test generator or sampler may draw at random if its program and its seed are recorded. What it returns counts only by the check then run on it. A search that finds nothing reports unknown. A seed fixes one run and is evidence of no law. `[decided]`
A result on a census, a sample or a test corpus $X_0$ is a yes for those members by name. Induction from it reports the whole set $\{\chi \in L \mid \chi \text{ agrees with every settled entry}\}$ of hypotheses in a declared language $L$, and reaches an input outside $X_0$ only by a covering fact, a derivation, or a statement in the form of §4.17. `[decided]`

**§4.17 A guarantee in probability.**
It is an ordinary statement that names what is drawn ($x$), by what law ($\mathcal{D}$), the event ($E$) and the bound ($\delta$), for example $\mathrm{Pr}_{x \sim \mathcal{D}}[E(x)] \le \delta$. It is settled by a derivation that covers every step from the draw to the statement. A use of the sampled conclusion itself rests on one named assumption, settled never, that the recorded draw was not a bad one. A bound on the manifest may refuse that assumption, and §4.13 always refuses it. Two bounds combine only by a derivation. This is the only approved form. Its construction is deferred and nothing has been built (§4.19). `[decided]`

**§4.18 Scores.**
A score, whether a code length under a named decoder with every part counted, a cost, a worth or an estimate, is a note recorded with its method (§20.2). It orders proposals inside a set that exact checks have already fixed. It gives the one claim that this program returned this number on these bytes. Entropy is said only of a distribution that is itself a term. `[decided]`
SkeinLab can keep the score with its method as an observation and investigate what it predicts. Any claim about that prediction states its scope and evidence. `[proposed]`

**§4.19 Distortion, laws of draws and sample guarantees.**
These three questions have different standings. `[proposed]`

| Part | Standing | What it is |
| --- | --- | --- |
| Distortion | Open. Exact work, with no chance in it | That an answer holds the true value, and that it is narrow, are two claims. An operation carries error by a law of its own. A first design exists, unreviewed, with gaps reported in it: a name that no value fits passes vacuously, and one-sided answers get a field and no law |
| Laws of programs that draw | Open. Exact work | On a finite seed sort: by counting, as §1.54 proposes. On infinite carriers the kernels of that first design are the candidate, and wait for the real numbers |
| Guarantees from a sample, or from a check that draws | Deferred, not dropped | Only the form in §4.17 is approved. Nothing is built until the first job where an exact check has been measured as unaffordable and a derivation of the bound exists. Until then such a result is a note. `[decided]` |

Open: a theory of distortion. `[open]`
Open: laws of programs that draw. `[open]`

<a id="ch-5"></a>

## 5. The store and its queries

**§5.1 The store.**
The store is one graph, addressed by content. It holds terms, theories, interpretations, representations, claims, evidence, notes and built artefacts. Anything may add a term, a proposal or a note; a proposal is a kind of note (§20.2). Evidence is a derivation, a run record or a counterexample. A run record is evidence relative to the build it names until the evaluator replays it. `[decided]`
Open, for the project owner: what may add each of the other kinds of thing. `[open]` The designer proposes that any writer may add every kind, each reading being protected by admission, evidence checking and replay. The other: writers of some kinds are restricted, which requires a rule that identifies them. Interning and content identity do not choose between the two, and neither is adopted. A record's claim to name a build is not authentication: the record rules still owe its binding to that build. Until that is specified, a build relies only on runs it made or replayed itself. `[proposed]` The proposed admission procedure in §7.11 says anyone may add a check’s run record, which is evidence. `[proposed]`
Open: the bytes that content identity hashes are not given. `[open]`
Every hashed content or dependency reference retains its canonical and hash profile context. Rehashing under a new profile requires the original content and separately reviewed migration/revalidation. An old digest is never relabelled. `[proposed]`

**§5.2 Cached checks.**
A check is cached under the triple $(\text{checking program}, \kappa, Q)$, where $\kappa$ is the claim and $Q$ records every question the check put to the store with the hash of each answer, including the answer that nothing was there. It is reused only while every question in $Q$ still has the same answer. So a new declaration that makes a once-unique default ambiguous reruns the checks that asked (not run). `[decided]`
The claim holds its context: a statement's scope is part of what it says (§4.1), and a membership is emitted in the context of its application (§7.6). So two checks of one node in two contexts have two claims and two entries. Node and context identify the claim, not every execution input. Reuse also binds the checking text and every input that can change the recorded answer, including applicable allowance, evaluator state and meter when relevant. An exhausted check's unknown is not a completed negative answer, and is not reused under a changed allowance as if completed. Store-answer validation alone does not prove those inputs unchanged. The hash-profile rule of §5.1 applies to these references too. `[proposed]`
At the first proposed reuse across a body edit, a check that unfolds, specializes or inlines a body records the identity of the body it read, using run identity and the recorded store answers. `[proposed]`

**§5.3 The queries.**

| Query | What it returns | Answered by | Can it license |
| --- | --- | --- | --- |
| Manifest of a node | The polynomial; its symbols; its reading under a bound | A kernel program | Yes |
| Status of a claim at a site | Evidence read at the site, by §4.5, §4.11 and §4.13 | A kernel program | Yes |
| What a term reaches at a sort | The uses, taken against a candidate's signature (§5.4) | A kernel program | Yes |
| Candidates for a term at a sort | Representations for which each clause, for that signature at that site, is yes, or has a test that the plan places as a guard, or is assumed within the bound. The answer says which, clause by clause | A kernel program over the above | Yes |
| Is this object in a recorded scope | Membership evidence, or unknown | A kernel program, or a guard | Yes |
| What rests on a claim | Every claim and artefact that would change if it were settled either way | A graph walk | It informs |
| The cheapest route to a goal | A plan $\pi$: the polynomial read in costs (§1.48) | The planner, a proposer. Each step is checked | No. The checks do |
| Effect of settling an open claim on the route's settlement cost | The difference of two such readings | A proposer | No |
| Which unknown claims would give this goal | Sets of claims, each with a way to be settled and a cost, that derive the goal and derive nothing that is no | A proposer under a budget | No. An answer is a proposal |
| Candidate theories | Implications over the table of laws at instances, each with the instances it was found on and the cheapest question that would refute it | A proposer | No. A candidate is a note |
| Find a value that satisfies a predicate | A value and its membership evidence, or unknown at the budget | A proposer under a budget | The evidence does |

Rows 3 (what a term reaches) and 4 (candidates): `[decided]`. The other rows: `[decided]`

**§5.4 The walk and its two results.**
The walk that gives the first source of the manifest gives two results. The manifest $\mathcal{M}(t)$ follows the rules of every defined symbol and leaves out constructors. The uses are taken against a candidate's signature $\Sigma$: the walk does not enter the rules of an operation in $\Sigma$, and reports that operation as a use. It enters the rules of every other defined symbol, whatever sorts its own signature mentions, and reports what it finds. A constructor of the sort is a use, and so is a pattern that matches one, as an operation that inspects a name (§1.56). It is one text with two results, and the second is counted in the trusted base. `[decided]`
Case: a client calls its own step function on a braid, and the step function calls the operation that adds a crossing. Following every rule, the walk reports the stored matrix and no operation. Stopping at every symbol whose signature mentions the sort, it reports the step function, which is in no representation's signature. `[decided]` Illustration: where the candidate's signature holds the operation that adds a crossing, the walk under the rule as stated enters the step function, does not enter that operation, and reports it as the use.

**§5.5 Which unknown claims would give a goal.**
The answer is the manifest polynomial of the goal with yes and no substituted, plus one check for each refuted claim. Where a goal needs some $r$ that meets several requirements $y_{r,1}, \dots, y_{r,j}$, the polynomial is the sum over $r$ of the product of $r$'s requirements, never the product of the sums:

$$\sum_r \prod_i y_{r,i}, \quad \text{never} \quad \prod_i \sum_r y_{r,i}$$

Illustration: with requirements $(a, b)$ for one candidate and $(c, d)$ for another the polynomial is $ab + cd$; $(a + c)(b + d)$ would add $ad$ and $cb$, each mixing the requirements of two candidates.
A set of claims is offered only when the set as a whole derives nothing that is no. The table behind candidate theories is three-valued, and an unknown entry neither supports nor refutes. Each candidate is spent as a question for this query. `[decided]`
A refusal says what would lift it: when a goal is refused, the message gives the answers to this query. Guard placement is the same query, limited to claims that have a test. `[decided]`
Review the proposed build explanation when the store-writer question goes to the project owner or when slice 4 names its first outside checker. An earlier need for an outside checker or a worked case showing that the required calculator checker is out of reach also triggers review. To explain a build, name the reading that licensed its choice. To examine it without a dependency, keep the original reading and make a new one under that restriction. `[proposed]`

**§5.6 Abduction ranks induction.**
Abduction ranks induction and does not bound it. The candidate-theories query orders its conclusions by the unknown-claims query: a law that some open goal's explanation contains, at an instance where it is unknown, is taken before one that no such explanation contains, and the second is not refused for that. Worth has an exact source: the goals that the law would give. The order is exact; a random schedule over it stays under the project owner's rule that exact methods come first. (direction only, provisional; application waits on a test of 56 candidates, not run) `[decided]`
The alternative is for abduction to bound induction, a law being worth inducing a theory for only if some open goal's explanation contained it. Open: to reconsider ranking against bounding before the design closes. `[open]`

**§5.7 The kept set of hypotheses.**
The language $L$ of hypotheses is declared and recorded with the result: which laws may stand in a body, and how long a body may be. For each instance $i$ where the conclusion is yes there is a bottom $\bot_i$: the laws that are yes there, kept to those the store's rules connect to the conclusion or to the goal. A body is a part of every such bottom. With three values there are two sets: the hypotheses that surely agree with every settled entry, and those that would agree if some unknown entries came out one way. The unknown entries on which they differ are abducibles again, ordered by guaranteed split: for each question take the fewest surviving candidates removed over its possible answers, per unit cost. Prefer the larger guarantee. The kept set is one note, with one exact claim. The note holds the conclusion, the instances for and against, the language, and the set, by its most specific member and its most general members, or "not listed, at this budget". The claim is: in language $L$, the hypotheses that agree with every settled entry of the table are exactly these. For a finite $L$ that is settled by exhaustion with $L$'s covering fact. A kept set predicts an unknown entry only where every member that applies agrees, and the prediction is still a candidate. A score orders members inside the set and never decides membership. `[proposed]`
To agree has two parts, and the bottoms give the first: the body is a part of $\bot_i$ for every settled instance $i$ where the conclusion is yes, and no settled instance has the body yes and the conclusion no. A hypothesis that only never fails, whose conclusion is also yes somewhere its body is not, is outside this set. `[proposed]`
Open: whether the job should keep that wider set. `[open]`

**§5.8 Three corrections to the kept set.**

1. "A body is a part of every such bottom" is the positive-coverage condition for a classifier, whose negative examples must also be excluded. As a rule for implications it throws away valid ones: with rows (A, B, Q) of (1, 0, 1), (0, 1, 1) and (0, 0, 0), "A gives Q" and "B gives Q" both hold and the rule keeps neither (the bottoms are $\{A\}$ and $\{B\}$, and neither body is a part of both). An implication fits a table exactly when no row has its body true and its conclusion false. The job must say which of the two it wants.
2. The set may have no single most specific member in $L$, and its most general members can be far more than the table: in one constructed table, 21 rows over 40 attributes in 20 pairs leave $3^{20}$ survivors with $2^{20}$ most general among them, described by one formula of 20 clauses. That is one witness, not a fact about every table of that size. So the note may hold the set as a formula, and says "represented but not listed" apart from "not determined".
3. Laws that are each possible need not be possible together: with P = 1, Q unknown and R = 0, "P gives Q" fits if Q is 1 and "Q gives R" fits if Q is 0, and the two fit under no one value. A candidate theory is judged whole, under one completion of the unknown entries.

The three cases were checked by hand. One source supported the account and another supported it in part. `[proposed]`

# Part II. From text to runs

<a id="ch-6"></a>

## 6. The stages

**§6.1 Pipeline.**
The manifest is checked before representations are chosen and again after. `[decided]` The retained pipeline has five stages, each ending in claims written to the store. $b$: the bound; $\mathcal{M}_m$, $\mathcal{M}_a$: the meaning and artefact manifests; $\pi$: the plan.

1. Read: text $\to$ tree $\to$ graph. The tree is kept for messages and formatting only. Text with an effect inside an argument becomes continuations, left to right.
2. Mean: sort membership, laws at interpretations, the use-once check. A claim that cannot be settled is recorded unknown, with when it could be.
3. Manifest: computes $\mathcal{M}_m$ and checks it against $b$. A failure here is final.
4. Represent: the planner chooses representations under $b$, reading each licence at its site. A claim to be settled at evaluation becomes a guard. $\mathcal{M}_a=\mathcal{M}_m\sqcup\bigsqcup_{\rho\in\pi}\mathcal{M}(\rho)$ is checked against $b$ again.
5. Emit: the last representation, into bytes, which the machine theory's own decoder decodes and compares.

**§6.2 Decoding and loading.**
Decoding shows that the bytes are the chosen machine program. On the generated-C route the independently decoded executable bytes are compared, under named bindings, with the outside C compiler's recorded output. `[decided]` That the machine program does what the term says is the tracking claim. That the bytes loaded are those bytes, with the bindings $\pi$ names, is checked at load. `[decided]`

**§6.3 Admission is for the term as stated.**
Admission assesses the term as stated. Its evidence or assumption goes in $\mathcal{M}_m$, including evidence from analysis. If a term is admitted with a guard and a stage-4 representation removes that guard by its tracking claim, that claim’s manifest goes in $\mathcal{M}_a$ alone. $\mathcal{M}_m$ retains the possible failure. A bound excluding it refuses the program unless the writer brings the analysis forward as admission evidence (§1.44). `[proposed]`

**§6.4 Slice 1.**
All five stages run and produce records, whose fields the record rules give. A run establishes what the program returned under §13.8, not every claim in that record. Text-to-graph correspondence stays as in §13.2; default tracking stays settled never, its named manifest dependencies retained.

- Read writes the graph, with the build's record of §13.2 for the reading of the text.
- Mean writes the membership claims of §7.11 and, scope by scope, the use-once result (§1.12). Laws at interpretations arrive in slice 2.
- Manifest writes $\mathcal{M}_m$ and its check against the fixed bound (§1.46).
- Represent has no planner: it is the plain path's fixed step (§10.4), each sort at its default representation, every guard in place (§10.1). Nothing is chosen, so no licence is read; the default's tracking claim is settled never, hence the lowering and the backend stand in the root manifest by name (§1.44). The second check still runs. $\mathcal{M}_a$ is $\mathcal{M}_m$ joined with what only the artefact does: those named entries, the reader of text, the compiled stops for memory and for the separately named stack resource (the C route's clean stack-stop guard is still unqualified), and each check the artefact makes and the meaning does not (§1.45). Represent ends with $\mathcal{M}_a$ made and checked.
- Emit writes the bytes and the comparison of §6.2; the lowering's two steps (§10.8), the form's check, compiling, decoding and comparing are all in it. It can refuse the build and cannot add to $\mathcal{M}_a$. `[proposed]`

<a id="ch-7"></a>

## 7. Admission

Notation: $\Gamma$ is a context, the sorts of the variables in scope; a signature is $f : (x_1{:}A_1, \dots, x_k{:}A_k) \to B$; $A[\vec x := \vec t]$ is a sort after substitution of indices; $\Gamma \vdash t \Rightarrow A$ says $t$ is checked in $\Gamma$ at $A$; $\Gamma \vdash t \in A$ says the membership of $t$ in $A$ is met at its site (§7.6). Admission accepts or refuses a subject. At a site a claim reads yes, no, unknown or conflict (§4.2). An individual test can have a narrower range of results.

**§7.1 Signatures.**
Every symbol has a signature, and every definition and literal is checked against it. `[decided]`

**§7.2 Terms, rules, images.**
A term is admitted in a context.

$$\frac{\Gamma(x) = A}{\Gamma \vdash x \Rightarrow A}\ \textsf{(F-Var)} \qquad \frac{f : (\vec x{:}\vec A) \to B \quad \Gamma \vdash t_i \Rightarrow A'_i \quad \Gamma \vdash t_i \in A_i[x_{<i} := t_{<i}]\ \ (i \le k)}{\Gamma \vdash f(\vec t) \Rightarrow B[\vec x := \vec t]}\ \textsf{(F-App)}$$

In (F-App), check memberships in parameter order with earlier arguments substituted (§7.6). In (F-Bound), $P$ is the declared profile of this bound parameter after index substitution. In (F-Rule), $\Gamma_{\vec p}$ gives each pattern variable the sort at its position. $A_i^*$ and $B^*$ are the signature’s parameter and result sorts instantiated in that pattern context, using earlier arguments for dependent indices. Admit each rule once, as a scope.

$$\frac{P=(\vec y{:}\vec C;D)\quad\Gamma,\vec y{:}\vec C\vdash u\in D}{\Gamma\vdash(\vec y\mapsto u)\text{ admitted at }P}\ \textsf{(F-Bound)}\quad\frac{p_i\text{ a constructor pattern of }A_i^*\ (i\le k)\quad\Gamma_{\vec p}\vdash u\in B^*}{f(\vec p)=u\text{ admitted}}\ \textsf{(F-Rule)}$$

Each image in an interpretation $\iota$ is checked against the source signature carried through $\iota$. `[decided]`

Case: a symbol declared to give a truth value, with the one rule `f() = zero`, has a signature and is wrong. `[decided]`

**§7.3 Where a binder may stand.**
A binder carries no sort of its own. When applied, it takes its variable’s sort from the checked argument. This is approved for checking signatures. `[decided]` For an indexed body result, the following proposed rule substitutes the argument into the result sort, avoiding capture where the index is admitted.

$$\frac{\Gamma \vdash t \Rightarrow A \quad \Gamma, x{:}A \vdash u \Rightarrow B}{\Gamma \vdash (x \mapsto u)(t) \Rightarrow B[x := t]}\ \textsf{(F-Beta)}$$

Illustration: if $g(n)$ has sort $\mathrm{Vec}(n)$, then $(n\mapsto g(n))(4)$ has sort $\mathrm{Vec}(4)$. The bound variable $n$ does not escape into the outer context. This completion of the result rule is proposed. `[proposed]`

A binder at any place but the function place of an application or a bound parameter is refused. §9.2 adds one place, a bound parameter of a constructor, under the working concurrency core. Binder placement goes with that core. `[proposed]` For now the first build refuses constructors with a bound parameter (§9.1, §19.5). `[decided]`

Slice 1 (the full core keeps the further places of §9.2). A pattern variable $z$ at a bound parameter carries that parameter's profile in the rule's context, $z : (\vec y{:}\vec C) \to D$: its variables' sorts and its result sort, the surrounding signature's indices instantiated. It may stand

- as the function of an application $z(\vec u)$: the arguments are checked in order by the claims of §7.6, each checked argument substituted for its bound variable in the remaining sorts and the result sort, preserving the context and avoiding capture, so $\Gamma \vdash u_j \in C_j[y_1 := u_1, \dots, y_{j-1} := u_{j-1}]$ and $\Gamma \vdash z(\vec u) \Rightarrow D[\vec y := \vec u]$;
- as a bound argument at a parameter whose variable sorts and result sort, brought into the same context with bound variables aligned, agree node for node with its profile; in slice 1 a difference is a refusal.

Elsewhere it is refused. The use-once side is §1.14 and §1.16. `[proposed]`

In slice 1 these checks (contexts, rules as scopes, where a binder stands) are the elaborator's. It is not trusted (§13.4) and stands in the root manifest with the reader (§13.2, §1.52). The memberships they rest on are the obligation generator's claims (§7.11). `[proposed]`

**§7.4 Sort parameters.**
Resolve a formal sort reference by its signature scope and position. Substitute the actual sorts without capture into fields, parameter profiles, results and conditions. Check each use with its actual sorts, including use-once obligations in data declarations and rule bodies. A pass at one use supplies evidence only for the statement and context checked there. `[proposed]`

**§7.5 Literals.**
A literal $v$ is a member of its sort $A$ by a claim, settled by a run of the sort's literal check $\mathrm{chk}_A$ on the sort's indices and $v$. $\mathrm{chk}_A$ is a definition in the evaluator's language that the sort's signature names.

- Where $\mathrm{chk}_A$ is the sort's only account of its literals, it says which values they are and owes no claim that it is right. Meant to agree with some other account of the sort, it owes the claim that it does.
- A sort declared finite has no check of its own: its literals are the values given, $V_A$.
- A sort that names no check and gives no values admits no literal.
- A check that runs out of fuel leaves the membership unknown, and the literal is refused.
- A value of a data sort is a constructor term and never a literal. `[decided]`

Slice 1: a literal check run for admission has one allowance $k_{\mathrm{lit}}$, fixed with the bound, the same for every host and run, stated apart from execution fuel. `[decided]` So, for the same literal and checker, indices, value, admission context, evaluator state and common meter, the host's chosen execution budget is not this check's fuel limit. That alone does not guarantee identical whole-program or reply admission across hosts: the other admission conditions must also match. Finite enumerated literals and constructor terms keep their own rules above. `[proposed]`

For literal checks using the paired profile, the single admission envelope written $k_{\mathrm{lit}}$ supplies a fixed $(W_{\mathrm{lit}},C_{\mathrm{lit}})$ in that profile, identical across hosts. Neither component comes from the enclosing execution. A cut on either leaves membership unknown and the literal is refused. An ordinary condition test reached in execution draws on that run after argument evaluation (§7.9). These rules supply no numeric admission preset. `[proposed]`

Open: the amount of $k_{\mathrm{lit}}$ and its charging protocol are unstated. `[open]`

Open: how a value of a data sort crosses the evaluator's edge is to be tested. `[open]`

For a sort declared finite the values given decide, whatever a check named beside them passes: in the second case below, 2 is no literal of the sort. The claim that such a check agrees with the values is owed, and until it is yes the check admits nothing. `[proposed]`

Cases: a literal that says it is a vector of length 4 and holds three numbers. A sort declared finite with $V_A = \{0, 1\}$ and a check that also passes 2. `[decided]`

**§7.6 Sort membership.**
The obligation generator emits a membership claim for each argument of an application, in that application’s context: the argument $t$, already checked at $A'$, is a member of the parameter's sort $A$ after substitution of indices. With $\equiv$ identity of nodes, by a run of `same`:

$$\frac{A'\equiv A}{\mathsf{member}(t,A,\Gamma)=\mathsf{yes}}\ \textsf{(F-Same)}\qquad\frac{A'\not\equiv A}{\text{node identity alone leaves membership unknown}}\ \textsf{(F-Other)}$$

From $A' \not\equiv A$ nothing follows: never no by that. An unknown membership

- with a test becomes a guard. A membership guard has no slower branch: where its test fails the run fails, and that failure is an effect in the meaning manifest;
- with no test is a refusal, unless the program assumes it by name. It is then an entry of the manifest's second source, the claims settled never, by name (§1.43), it stands in the semantic part of the lock, and §4.13 still holds. `[decided]`

Assumption by name is a named opt-in: switched on in slice 2 with the permission controls, refused in slice 1, never under §4.13. Not taken: always a refusal, until evidence exists. `[decided]`
If a guarantee still depends on this assumed membership, each build using the guarantee must accept that assumption by name (§13.13). (derived from the rule above and §13.13) `[decided]`

Report. Each build prints the guards it put in under this item: for each, the call it stands at, the test it runs, and the rule for what that test is charged when it runs. `[decided]` A build that put in none says so. Admission records the obligations and guards of its subject. The report for a chosen plan binds that inventory to the plan and identifies each test kept or removed, with the evidence for removal (§6.3); the meaning manifest keeps the possible failure. The plan's report is fixed with that build, not before the choice of representation. A run names the report through the build of the part it uses. A guard's rejection is linked to the same call identity in the run's diagnostic record and the build's report. `[proposed]` The report form and encoding remain open. `[open]` Each report of admission, a build attempt or a run identifies its subject and phase and links to any enclosing run (§8.8). `[decided]`

Order. Argument evaluation keeps its ordinary order and outcomes (§8.2). Once all argument values $\vec v$ of a call are obtained, its guards run before its operation, on $\vec v$, without evaluating the arguments again: membership guards in parameter order, then condition tests in the order written (§7.9), then $f(\vec v)$. The first guard to reject is the rejection reported, and no later test or the guarded operation then runs. An earlier argument failure or stop still prevents later argument evaluation; a host wait keeps its ordinary continuation. Not taken: testing each argument as soon as it is obtained. `[decided]`

**§7.7 Evaluated symbols.**
An evaluated symbol is defined in the evaluator's language. The reference run applies the definition to checked argument values and checks the result as below. The numbers, bytes and arrays of the standard theories are given this way, so no native tool stands in the meaning manifest of arithmetic. `[proposed]`

It takes and returns no value of a use-once sort: the evaluator copies its values freely. It receives checked values, and its result is checked before use: a literal by the result sort's literal check, a constructor term by admission, field by field. The label on a result is not evidence. A build that runs a definition by other code than the evaluator owes that the two agree (§13.6).

What it adds to a manifest is read from its whole checked action, not from its body alone. The action has five parts, each with its own outcome: (1) the admission of the arguments; (2) the build that runs the definition; (3) the run of the body; (4) the check of the result; (5) the bounded run of any literal check the result check makes. A body total by its syntax settles only (3). A result its check refuses, and a check that runs out of its allowance, are outcomes of the action.

- A definition total by its syntax, whose result check is total by its syntax and cannot refuse a result the definition can give, adds nothing beyond the build. This is the narrow promise.
- A definition not total by its syntax adds possible non-termination.
- For every other case the entries are owed, with those outcomes. `[decided]`

Open: what a refused result and an exhausted check each are in the reference run, and which manifest entry each has, is not specified and is owed. `[open]`

The build named is the evaluator build that ran, an entry of the manifest's third source, the manifests of evidence (§1.43). Code that runs a definition in the evaluator's place stands in the artefact manifest (§10.10). So no tool outside the evaluator stands in the meaning manifest of arithmetic. `[proposed]`

Case: an evaluated definition that puts one incoming value into both fields of a pair. Each field has the right sort and one value has become two. `[decided]`

**§7.8 Conditions in a signature.**
A signature may carry conditions $\varphi_1, \dots, \varphi_n$: statements over its indices and parameters. At a call $f(\vec t)$ each $\varphi_j[\vec x := \vec t]$ is a claim the term rests on, beside its membership claims, settled as §1.44 says. A statement is not a test. Where $\varphi_j$ has a test $q_j$, the signature names $q_j$ and the claim that ties the outcomes of $q_j$ to $\varphi_j$, with what §13.8 asks of that claim. A test that does not finish, or fails for want of fuel, settles nothing. (working rule: its test is still owed) `[decided]`

Conditions and their tests are part of slice 1. The tested conditions of §4.13 use this form (§10.11), and nothing in §19.2 leaves out a source signature's own. `[proposed]`

**§7.9 A condition's test.**
A test runs before the operation, in the order the conditions are written, on the argument values already obtained; it does not run the arguments again. The guard and its failure are admitted with the call, under the ordinary checks of sort, context and use-once. Each build prints these tests in the report of §7.6, marked as a condition's test. `[proposed]`

A test may not consume an argument the operation then uses, unless it hands the value back; without that the guard is refused. A test, its condition and its failure stand in the manifest, with their roles and times (§1.45), and in the cost of the call. `[proposed]`

Charging. The guarded call accounts for the test work that actually runs, on the existing meter for its invocation and work; being a guard has no extra price. In the reference evaluator this work uses execution fuel, after the call's arguments and before its operation, for membership guards and condition tests alike.

- An ordinary non-memoized evaluator definition call contributes the meter's one call event; the executed body and the other specified parts of the checked action keep their existing charges.
- A completed memo hit keeps the one work debit of §15.7 and constructs no result. Its arguments have already run. Under the paired profile the hit itself costs $(1,0)$. `[proposed]`
- Other invocation forms keep their own rules; a form whose charge is unspecified is named as a charging gap.

$k_{\mathrm{lit}}$ limits literal checking separately from execution fuel. A fuel cut or unpaid test leaves the condition unsettled. Compiled code gains neither semantic fuel nor resource-stop permission. Report a price only if constant across admitted arguments and relevant evaluator states, including memo state. A checked upper bound names its parameters, units and covered states. Otherwise report the metering rule and “no bound established”, or identify a missing metering rule. Syntactic totality establishes neither a charge bound nor the whole action’s outcomes and manifest (§7.7). This procedure uses existing charges and requires no static bound extractor. `[proposed]`

A test left at a call is a use that clause C3 of the tracking claim sees (§5.4); a tracker that takes the test inside owes the behaviour of the whole guarded call. That a condition is yes does not by itself let a plan remove what its test does: an effect, a choice or a possible run without end stays unless §8.6 and §3.15 let it go. A machine theory marks which conditions of its operations fall under §4.13, with what that item asks. No sort is made by a condition: the argument keeps its sort, and the claim is about the call. (working rule: its test is still owed) `[decided]`

A test may reject values at which its condition holds. Then a yes for the condition does not show that the test accepts, and a plan that removed it could turn the reference run's failure at such a value into another outcome, such as a return. It is removed only with a claim that the test accepts at that call. Put this refinement to the project owner because it qualifies the existing guard decision. `[proposed]` Illustration: the test $x > 0$ for the condition $x \ge 0$; at $x = 0$ the condition holds and the test rejects.

**§7.10 The alternative: a sort cut out by a predicate.**
Not taken: the demand is a parameter sort of its own, cut out by a predicate, with a conversion at each call and membership as a claim under §7.6. The comparison with §7.8 no longer decides between the two; it is kept as a check on the choice taken. `[proposed: working rule]`

Owed: the test of the two ways to carry a condition on an argument: write a pure braid and an index below a bound both ways, count the records touched, and see whether either form fails to state a condition on two parameters at once. A failure is reported to the project owner and does not select the other answer. `[proposed]`

Also not taken: a second mark for §4.13 on a source signature. The machine theory marks those conditions. `[proposed]`

**§7.11 The obligation generator, first part (slice 1).**
It emits every membership that admission asks for: one for each argument of each application (§7.6 applies separately at each argument); one for the right-hand side of each rule and one for the body of each bound argument, against the declared result sort; one for each literal.

A claim as emitted carries its statement, with its context as part of what it says (§4.1), and nothing else. The generator does not settle what it emits. For these two checks, anyone may run `same` or the literal check and submit its record under this proposal. A build relies only on runs it made or replayed (§7.12). That record is the claim's evidence, relative to the build it names until the evaluator replays it. The Eval claim of the checking run has the build that ran in its manifest. Reading its result as membership retains the checker's required soundness or agreement claim and all dependencies, including the debt of §7.5 to another account of the sort; it is assumption-free only when those requirements establish that. The claim is settled at build. A membership that becomes a guard is settled at each evaluation of its site. `[proposed]` Whether anyone may add evidence records is still open for the project owner under §5.1. `[open]`

**§7.12 Reading a status in slice 1.**
Slice 1 does not yet run slice 2's reader of evidence at a site. Its direct reading still records each statement, the admitted evidence and the evidence manifest.

- Identical sort nodes: a run of `same` gives the membership answer of §7.6. Different nodes alone: unknown, never no by that.
- A literal check completed with acceptance or rejection gives the corresponding answer, subject to its specified account and its agreement and soundness obligations. Exhaustion: unknown, and refusal.
- A finite literal is checked against the declared values: a match gives yes; completed rejection of every value gives no; an unfinished comparison gives unknown.
- Admitted yes and admitted no for the same statement at the same site give conflict and license nothing.

A build relies on runs it made or replayed; naming a build alone authenticates nothing. Eval establishes $f(v) = w$ for the build and input, with the named starting state for sequence use (§13.7). A checking answer establishes its checked statement only with the scoped soundness or account that §13.8 and §7.5 require, retaining its dependencies. These requirements also apply to claims that are not memberships. An unresolved tracking claim remains settled never and named in the manifest. Statements are terms under §1.8; their proposed vocabulary is §7.15. `[proposed]`

Open: general runtime membership-test availability, indices, use-once handling and whether the fixed bound permits guard failure remain separate questions. `[open]`

**§7.13 Which tests a membership has.**
Use only a test already specified for this membership. Refuse an unknown membership with none. `[decided]` Review this choice with the project owner alongside the ordinary-parameter use-once rule when the slice 1 admission and use-once contract review ends, or earlier if a first-build sketch or program is refused solely for lack of a test. Bring the count of those refusals and written contracts for literal checking and comparison with a finite collection. `[proposed]`

§7.5 gives a sort's literal check and a finite sort's given values; §7.7 gives the field-by-field admission of a constructor term returned by an evaluated symbol. These do not by themselves specify a total runtime membership test for every argument value, its treatment of use-once fields, or how an index is read at the call. Two future alternatives remain. One uses literal checks and finite-value comparison. The other adds a constructor-field walk that needs its own design. The proposal calls for a reviewed contract per new test for acceptance, indices, use-once fields, charges and failure. `[proposed]`

Open: which additional tests are available, on which sorts, with which index and use-once rules. It is put to the project owner before admission rules rely on them, and is separate from whether the fixed bound admits their failure. It is a question, not a new admission rule. `[open]`

**§7.14 Indexed sorts in slice 1.**
Slice 1 admits the plain term indices of §1.3, chosen for now. `[decided]` Two sorts are compared as written after substitution; an index term is not run. So a sort at `2 + 2` and the same sort at `4` are two nodes, and the membership is unknown, never no by that (§7.6, §8.4). With a specified applicable test it becomes a guard; without one it is a refusal, and the writer puts the index in one written form. Whether additional tests read an index by its value at the call is the open question of §7.13. Not taken: running index terms at admission. Each run would need fuel and an allowance, and an index term that does not end would need an outcome. This comparison and the exclusion of admission-time evaluation are proposed for slice 1. `[proposed]` The future alternative would allow unrestricted index terms. Under either choice the time, frequency and charge of index runs remain open, as does the reach of added call-site tests. `[open]` Bring the plain-index choice back to the project owner when those rules for time, frequency and cost have been written and reviewed, or sooner if a sketch or program needs an index it refuses. Bring the case and the extra rules an unrestricted index would need. `[proposed]`

**§7.15 The statements of slice 1.**
The statement sort of slice 1's small theory has five constructors, under working names that choose no spelling:

```
statement ::= member(n, s, c)   -- node n, in context c, is a member of sort s
            | literal(v, s)     -- value v is a literal of sort s
            | fits(n, c, b)     -- the meaning manifest of node n in context c fits bound b
            | once(n, c)        -- scope n in context c passes the use-once check
            | gives(f, v, w)    -- Eval: f on v gives w, scoped to its starting state for sequence use (§13.7)
```

A statement refers to the graph by holding nodes as values: a node is a value of the evaluator and its identity is `same` (§2.5); a term, a theory and a sort are each values of a sort of their own that a predicate may take (§1.34). So `n`, `s`, `f` are nodes, `c` a context, `b` the bound's node, `v` and `w` evaluator values.

A context is a tuple with one entry for each variable the node holds. A value variable's entry is its sort node and its use-once standing there (§1.21). The entry of a variable standing for a bound argument is its profile, the sort nodes of its variables and of its result (§7.2), with the multiplicity $m$ its parameter declares, or the use-once reading under which the parameter is checked again (§1.14, §1.21, §3.12). Two contexts that differ in any entry are different values, so the statements holding them are different statements, and a claim for one is no claim for the other: a pass under one standing never discharges a check under another.

The theory has no laws and no rules. An admitted claim's statement is checked as any constructor term is, field by field. Adding a constructor is a change to the theory a build ships and to its hash. `[proposed]`

<a id="ch-8"></a>

## 8. Order of evaluation and the reference run

**§8.1 Order.**

- An operation with a continuation runs where the term puts it. Two such operations may be exchanged, shared or dropped only by a claim about the two at their selected interpretations. Different manifest symbols give no exchange. `[decided]`
- Manifest entries that are laws, tools or models impose no order. `[decided]`
- A term that may not terminate is never dropped or run early without evidence that it terminates. `[decided]`
- Moves of an open choice use §1.53. Its set-of-outcomes reading applies only while the pick is unresolved on both sides, under the conditions there; every other exchange needs the claim about the selected interpretations, scope and observations named there. `[decided]`

**§8.2 The reference run.**
The reference run is a program for the evaluator, called `step`. It is call by value: the arguments of an operation run before it, left to right.

```
p ::= x | c(p, .., p)                  -- pattern; each variable once
E ::= [] | f(v, .., v, E, t, .., t)    -- evaluation context
```

Let $P_f$ mean that the obtained arguments passed membership guards in parameter order, then condition tests in listed order (§7.6). The first rejection prevents the rule or request from running. A request $f(\vec v)$ excludes the last, bound continuation $k$, saved with its pending frames as $E[k(-)]$. Compare the request at its observed arguments (§8.10).

$$\frac{t\to t'}{E[t]\to E[t']}\ \textsf{(G-Ctx)} \quad \frac{P_f(\vec v)\quad j=\min\{i:\vec p_i\text{ matches }\vec v\}}{f(\vec v)\to u_j\text{ under the match}}\ \textsf{(G-Rule)} \quad \frac{P_f(\vec v,k)\quad f\text{ requests}}{E[f(\vec v,k)]\text{ gives }\mathsf{asked}(f(\vec v),E[k(-)])}\ \textsf{(G-Ask)}$$

This fixes what the reference does. The compiled program must agree with it (§8.10), and each slice checks that agreement on generated inputs (not run). `[decided]`

**§8.3 Activations, sharing, reuse.**
An argument runs each time the operation that holds it runs, in that operation's activation. A variable stands for the value already bound to it in the activation of its binder ($x$ gives $\eta(x)$, $\eta$ that activation's environment); using it runs nothing again. So a run is shared only where the term binds it. `[proposed: working rule]`

The run may also reuse a result already obtained for a term $t$, at the same values of its variables, where reuse cannot be seen, that is when all hold:

1. $t$ makes nothing new: its run makes no sequence and no value of a use-once sort (§21.1). `[decided]`
2. $t$ has no effect and no open choice. `[decided]`
3. $t$ consumes nothing that is use-once. This is read from what its run does, not from its free variables: `read(K())` has none, and consumes. `[decided]`
4. Its result may be copied. `[decided]`
5. Neither $t$ nor anything it can call reads or writes a sequence. The project owner chose this restriction. `[decided]` Its exact wording is proposed for review. `[proposed]`

Reuse is beside what §8.6 allows and needs no evidence that the term ends. It never lets a run that has not finished be skipped, dropped or made early. That two pieces of code are one node is never by that a reason to reuse. `[proposed: working rule]`

Cases: `pair(work(), work())` with `work` costly is two runs by the definition, and one where the run reuses. `pair(K(), K())` with `K` a producer of a use-once value is never reused: one result would stand at two places. Both were run on a fixture of 44 cases and confirmed (§23.2 row 17): under a local reuse test that omits the copying condition, one use-once result does stand at two places. `[proposed: working rule]`

**§8.4 Naming a costly term; identity.**
A writer who wants one run of a costly term names it. A rule step may copy a value where its sort allows, and must bind a term that has not run before it puts it in two places. Nothing changes for identity: sort membership by `same`, laws that are yes by identity, caches and claims are about code and stay on nodes. `[proposed: working rule]` The fresh-production restriction on "yes by identity" is recorded in §21.1. `[decided]` Applying the full result-reuse condition to laws is a separate proposal there. `[proposed]`

**§8.5 First match on open terms.**
In execution the first rule matching the obtained values runs. `[decided]` For a term with variables the proposed restriction applies a rule only if no earlier rule could match an instance. `[proposed]` The named normaliser for equality by computation uses that restriction (§14.8). `[decided]`

Case, observed in a finite normaliser model (§23.2 row 11): with the rules `f(zero) = one` and `f(n) = two` tried in order, a normaliser that takes `f(x)` to `two` makes `(x -> f(x))(zero)` run to `two` where `f(zero)` runs to `one`. `[decided]`

**§8.6 When the planner may share, move or drop.**
Write $\mathrm{quiet}(t)$ when $\mathcal{M}(t)$ holds no effect, no open choice and no possible non-termination, $t$ consumes no use-once value, and neither $t$ nor anything it can call reads or writes a sequence. The following rule also requires the fresh-result exclusions and site conditions below.

$$\frac{\mathrm{quiet}(t)\quad \text{the proposed change meets the fresh-result and site conditions below}}{\text{the planner may share, move or drop } t}\ \textsf{(G-Plan)}$$

Without $\mathrm{quiet}(t)$ this licence does not apply; §8.1 and §1.53 give the exchanges that rest on a claim of their own. The project owner chose the cautious restriction. `[decided]` These exact words are proposed for review. `[proposed]` Running a term again at a second place is a move of the same kind, read the same way. Further:

- a term whose run makes something new (§21.1) is neither shared nor run again;
- a term whose result is of a use-once sort is also never left unmade: each run of it that the reference makes has its own corresponding run, which makes its own fresh result, also where that result looks unused;
- a term whose run makes a sequence is, for now, also neither moved nor left out: either can change the count that names later sequences (§17.2).

The project owner chose these limits. `[decided]` The third limit holds for now, with these exact words proposed for review. `[proposed]`

Open: whether a wider form is safe waits on the matching relation of names (§21.1). `[open]`

Side conditions. Wherever $t$ is moved or shared it keeps the bindings of its arguments, its activation, and the way each of its claims was admitted: by evidence, by a guard, or by an assumption by name.

- Evidence that justifies the move, or that lets a guard be left out, is read again at the new site (§4.5, §4.2) and must be yes there.
- An assumption by name that is not on the machine model stays an assumption by name, with its place in the lock: moving the term does not make it yes.
- A claim that is yes because a test passed is yes only for the same values, in a state the test still describes, at places the test comes before on every path. Outside those places the term needs other evidence that is yes there, or a guard of its own.
- §4.13 holds throughout.

Reuse of a result already obtained (§8.3) is a separate matter. `[decided]`

Case: an exact division under a test that its divisor is not zero. Inside the branch the claim on the divisor is yes, and the division's manifest holds no effect. Looking only at the manifest would allow the division to be hoisted above the test, where the divisor may be zero. The full rule requires evidence for the new site or a guard there. `[decided]`

**§8.7 Evidence after a write.**
Consider this wording at slice 2’s call conditions or when the stateful examples return before any widening of the sequence restrictions (§8.6). After a write, a use relying on an earlier test identifies what shows its claim still holds of these values here. `[proposed]`

**§8.8 State, outcomes, reports.**

```
state   ::= { control: a node with its environment, or a value; frames: what remains to be done;
              handlers: the handler frames in force; next activation: a count; next name: a count;
              allowance: meter profile and its remaining grant (W,C for the paired profile); consumed: a count for each use-once value }
outcome ::= returned(value) | failed(payload, held) | asked(request, continuation)
          | out of fuel(primary axis, held) | stopped(resource, held)   -- the latter is a permitted compiled stop
```

The paired allowance field and the primary-axis field above are proposed record fields for the paired profile. `[proposed]` `held` names the use-once values the run had and did not consume. Owed: the test of the shapes of the state and its outcomes, by building slice 1. `[decided]`

Every admission, build attempt or run report identifies its subject and phase and links to its enclosing run when there is one. `[decided]` Report the enclosing run’s outcome separately when available. A run may build a deferred part at its first call or check a reply or produced value before use. Reports distinguish refusal, a stopped build attempt, an ordinary result such as `none`, failure and fuel exhaustion.

- Refusing initial admission prevents that subject's execution; it is not an ordinary returned value.
- Refusing a host reply leaves the already asked run as §8.9 says.
- A failed first-call build is reported as a failed build attempt together with the stopped run that §12.4 requires. It presupposes neither a completed build of every part nor an answer to whether such a failure is a resource stop. A completed build is needed before that part's code is entered.

The reason in an allowance stop is work or construction (§15.9). A controlled physical interruption of the evaluator is recorded by its runner as host-stop(memory) or host-stop(stack), with the last committed prefix and any outstanding holdings. This is outside the ideal evaluation judgment. A compiled stop for a manifest-permitted resource must in addition meet §8.12. An uncontrolled allocator failure, stack overflow, killed process or missing record gives a host/tool fault or incomplete evidence. A clean host stop requires an already prepared way to preserve the prefix and held account. A host wait, ordinary failure, pre-run refusal and either allowance cut keep their existing phase distinctions. `[proposed]`

Open: the result-check and literal-check outcomes and manifest entries of §7.7 are not chosen here; whether each admission refusal is carried in a record or only in a diagnostic, and the forms of these reports, remain open. `[open]`

**§8.9 Function values, requests, replies.**
A function value holds its body and its environment. The reference run counts what it consumes of each use-once value. Under §8.3 the state needs no table of results. At an operation with a continuation the outcome of `step` is $\mathsf{asked}(\mathit{rq}, E)$, $\mathit{rq}$ the request and $E$ the whole saved continuation, including its pending frames (§8.2). The caller answers it with a selected interpretation of the effect's theory, or passes it to the host when the symbol is left in the manifest. A host reply is admitted as §7.2 and §7.5 admit any value, before the run resumes, and one request takes one admitted reply. `[decided]` "Reached through Ask", in §1.46 and §19.2, names this: the run stops at the operation with the outcome asked, and the host answers its request. `[proposed]`

Slice 1, a reply $w$ to $\mathsf{asked}(\mathit{rq}, E)$, with $H$ the run's held account:

1. Check. Checking $w$ transfers no ownership of what it carries. Until $w$ is committed its use-once values remain the host's and are not added to $H$. `[decided]`
2. Refusal. A $w$ that fails admission cannot resume the run. The run remains $\mathsf{asked}(\mathit{rq}, E)$, same request and continuation; the refused attempt is recorded; the host may answer again or end the run. Refusal neither consumes nor drops the values. It adds no outcome to §8.8 and no Loom-observed failure. `[decided]`
3. Preparation. After the check has passed, all preparation needed to accept $w$ and account for its values must succeed, and the charges required for that transition must be paid, before ownership changes. If a required charge cannot be paid before commitment, ownership has not passed: the values are still the host's and $H$ is as it was before the reply. What outcome the run then has is not chosen here; it waits on the charge protocol. `[proposed]`
4. Commitment. $w$ is then admitted and ownership transferred exactly once, the values accounted for by the run before $E$ can use them. A later stop accounts for the admitted values under §1.23. The returned values follow §1.19 and §21.1; no host identity encoding is chosen. `[proposed]`

Open: the exact request and reply records; the encoding of the instantiated result sort and index context; activation and identity; the continuation and host completion interfaces; reply provenance and their projections; the system-call model; the handling of other preparation failures; the remaining host interfaces. `[open]`

Open: request, reply-admission and resumption charges, their amounts and protocols, are unstated. `[open]` Under the common export rule in §3.19 each published function states its finite limits or requires the caller to supply them. A fresh invocation uses a published finite default when the caller omits that grant. `[decided]` Its first numerical presets, the host's admission interface, and any elapsed-time policy remain open. The fixed literal-check allowance of §7.5 is supplied separately. `[open]`

**§8.10 Agreement; the three conclusions of a comparison.**
Let $r_c$ be the compiled run and $r_r$ the reference run on one input. $r_c$ agrees with $r_r$ when:

1. Requests: those of $r_c$ are those of $r_r$, in order and with equal observed arguments.
2. Outcome: the same failure with an equal payload, or a result related to the reference's as the tracking claim says, which at an observed sort is equal.
3. Use: $r_c$ consumes each use-once value as $r_r$ does, value for value and activation for activation, except where a claim licenses a change (§1.17): with $u(x, \alpha)$ the number of consumptions of value $x$ in activation $\alpha$, $u_c(x, \alpha) = u_r(x, \alpha)$ for corresponding values and activations.

On 2: a failure's payload is compared as a result is. §3.16 has the payloads related as results are, so "an equal payload" is said of an observed sort, the only case slice 1 has (§10.3); at a sort not observed the payloads are related as the tracking claim says, and no equality of their representations is asked. (a reading; no case of slice 1 changes) `[proposed]`

On 3: the reference's own count does not show the compiled side. That is shown by checked evidence that the lowering keeps use, or by a way of watching the compiled run that is itself checked. A match of requests and outcome without it is recorded as that and no more, with use not checked.

Where the meaning leaves a choice open, $r_c$ must be one of the reference's runs, $r_c \in \mathrm{Runs}(t)$ (§3.2). The compiled run may stop for a resource that the manifest names where the reference goes on, and not the reverse. A run cut short by fuel shows no agreement, and no disagreement beyond what its completed prefix has already established: only the part not yet compared is inconclusive. A mismatch is established when no continuation of the cut run could remove it: a request in the compared prefix that differs in order, in operation or in an observed argument, or a use-once value consumed twice. (it gives no step-by-step interface and no proof for a lowering; finite checks of agreement at a stop are run and reviewed, §23.2 row 15) `[decided]`

A comparison, under the matching choices and tracking claim above, has one of three conclusions:

- Agreement: established only when both runs have returned or ended in corresponding failures and all requirements have been checked: every request in order, the related outcome and held account at failure, and consumption value for value and activation for activation, with any licensed change.
- Established mismatch: one checked violation of those requirements, or of the applicable stop requirements (§8.12), that no continuation of the unfinished runs could remove. One suffices, even when other parts remain unexamined.
- Incomplete: otherwise, with what remains unexamined or unchecked and why. This includes a fuel cut, a host wait, a permitted resource stop, a first-call build stop whose comparison is unfinished, and a match of requests and outcome with use not checked.

A permitted resource stop is still recorded as such; whether its prefix and consumption requirements were checked is stated separately. Different outcomes or held accounts allowed by §3.17 and §8.12 are not by themselves mismatches. An incomplete comparison never establishes agreement or withdraws an established mismatch. The comparison keeps the requirement $r_c \in \mathrm{Runs}(t)$. `[decided]`

Slice 1: a request the host never answers remains recorded as $\mathsf{asked}(\mathit{rq}, E)$, waiting; for comparison it shows neither agreement nor disagreement, and never erases a mismatch already seen. This waiting policy is not derived from the fuel-cut rule. `[decided]`

Open: the remaining host completion interface. `[open]`

Case: a value is finished once by the meaning. One lowering finishes it twice and one never, and neither tells the host. All three runs make the same requests and return the same result. The harness of slice 1 must refuse the two wrong ones, by controls that drop a value and that use one twice. `[decided]`

**§8.11 Comparison records after milestone B.**
At the full slice 1 comparison of reference and compiled runs, after milestone B: compare two production sites, one site visited twice, and replay from equal starts. Distinguish program identity, build evidence, occurrence and event. Compare an execution that emits 7 and returns 1 with one that just returns 1: equal results leave different requests. A wrong request witnessed before exhaustion remains a mismatch, while the unchecked remainder is incomplete. `[proposed]`

**§8.12 Failures, resource stops, faults of the build.**
At a failure the compiled run holds the values the reference holds. Where $r_c$ stops for a resource and $r_r$ goes on, the requests of $r_c$ are the first of the reference's, in order, and each value $r_c$ consumed $r_r$ consumes, and no more often. With $Q_c, Q_r$ the two sequences of requests and $u_c(x), u_r(x)$ the number of times each run consumes the use-once value $x$, summed over its activations: $Q_c$ is a prefix of $Q_r$ and $u_c(x) \le u_r(x)$ for every $x$. Such a run is recorded as stopped for a resource and never as agreement. (the finite check behind it, §23.2 row 15, compares an ordered prefix of requests and final counts value by value; it is not a step-by-step trace of ownership) `[decided]`

The record of a resource stop names (a) the resource and its cause, (b) what the program was doing, (c) the artefact manifest entry and applicable bound that permit the stop; and (d) it binds the stop to the run and tracking claim under which the ordered-prefix and consumption requirements above are checked. These bindings may name records kept elsewhere. Naming an entry alone does not establish permission or discharge the comparison. Where the applicable manifest and bound are established and do not permit the stop, it violates §8.10. Missing or unchecked evidence of that permission is reported as such, not treated as permission or by itself as proof of a mismatch. `[decided]`

Open: the record's fields and bytes. `[open]`

Open: whether a failed first-call build is a resource stop; this item does not classify it as one (§12.4). `[open]`

A build that detects a violation of an internal machine-model condition during a run reports a fault of the build, not a program failure or a permitted resource stop. The fault is not an outcome of §8.8 and certifies no held account. Its report gives subject, phase and cause to the extent established, preserves the already recorded requests and earlier failure or stop records, and marks any unverified state as such. For a comparison it is never agreement and never a stop. §8.10 still determines the conclusion: a checked violation of its requirements, or of the applicable stop requirements, that no continuation could remove remains an established mismatch; otherwise the comparison is incomplete, naming what is unchecked and why. A fault diagnostic alone supplies no such checked violation (under review). `[proposed]`

**§8.13 The watch on a compiled run.**
The watch is how a compiled run shows its use (§8.10): a log the runtime keeps of three events, each with the name of the value and the activation it happens in.

```
event ::= made(name, activation, what made it) | consumed(name, activation)
        | held(name, activation)   -- at a failure, a stop or running out of fuel,
                                   -- for each value made or given and not consumed
```

Each event is raised by the runtime entry that does the act, and by nothing else. `[proposed]` Taking apart a use-once datum consumes it (§21.7). `[decided]` The proposed entries report consumption on destructuring and making on construction. The event for a promised-once function remains open. Entry placement is a proposed implementation constraint. The correspondence between an entry's actual acts and its reports must itself be checked: placement alone does not establish that each act is reported exactly once or that each report has an act. With it checked, two calls produce two reports and an omitted call produces none. A count of references is none of these events (§10.9). A comparison sets the log beside the reference run's makings and consumings, name for name and activation for activation, with the values held at an outcome, as §8.10 and §8.12 require. Every compiled program whose agreement is claimed carries the watch; one built without it has its use not checked. `[proposed]`

Open: the events for a function at a parameter of multiplicity $\mathbf{1}$ are not drafted. `[open]`

Trying a rule's patterns is non-consuming. Inspecting constructor tags or fields to reject a candidate, a nested one included, neither consumes the inspected datums nor changes their names or held obligations. Only the selected rule's committed destructuring performs the consuming events; the lowering must bind them to that rule's logical activation. An inspection/commit interface is to be supplied and checked through runtime entries, with controls for first-rule failure followed by a later match, a catchall and no match. Until it is specified and qualified, no nested-pattern watch qualification is claimed. The making event's "what made it" is the maker-provenance projection that §21.8 requires; until that is defined and checked, the making-order comparison is recorded as unchecked. `[proposed]`

**§8.14 The check on the watch, slice 1.**
Required controls, none a proof of all programs:

1. The check of the printed C checks that a box is reached only through runtime entries.
2. The check of the low-level form checks its proposed correspondence to the admitted graph (§10.5).
3. A run of a checker establishes that it returned yes; using that yes still owes its soundness claim (§13.8).
4. Each run of the harness also tests wrong lowerings that drop a value, consume one twice, make two values in the other order, or change a failed run's held account. Each must be refused.

These alone do not check the correspondence between a runtime entry's actual acts and its reports. Independent validation of it must bind the exact watch, runtime entries and compared subject, name its premises and finite subjects, and include controls that perform an act twice inside an entry while reporting it once, omit an act's report, or report an act without performing it. Until it is checked for the compared run, the record is "use not checked". Once it is checked, the comparison records the route, code bindings and named inputs it covers; no conclusion extends beyond them (§4.16). The watch and each unverified checker keep their soundness dependencies in the root manifest under the lowering, by name; passing controls does not turn those assumptions into proved claims (§13.8, §13.4). This item does not choose the consuming and fresh-production account: §21.7 records one for the decided cases and leaves the case of a function promised to be used once unwritten and open. (a local repair; not a qualification result) `[proposed]`

<a id="ch-9"></a>

## 9. The concurrency core

**§9.1 Standing of the core.**
Under the project owner’s delegation, the design architect retained §§9.2–9.6, 9.8–9.11 and 9.14 as working rules. `[decided]` Their adoption for provisional use rests on timing: they change trusted texts (the use-once check, the signature, admission), cheaper to specify once than to change later; three bounded tests that lean on them passed and were recounted. They are not held right in every context: the census of §9.3 is not run, and if it accepts a wrong term they fall and §1.4, §1.16, §7.2 and §3.12 stand as they are. §9.7, §9.12 and the protocols of §9.10 stay open; two bounded tests would check the first two once the translation, owner completion and the guard are specified, without defining or proving those contracts; one has run, on one encoding (§23.2 row 24). The alternative would omit the core and its Loom scheduler with tasks held as functions. For now the first build refuses a constructor with a bound parameter as unsupported. `[decided]` The future first-build alternative would admit these constructors under the working rule (§19.5). Under either first-build policy, run and review the whole-language census before fixing the use-once rules, signature record and admission. On one frozen grammar neither setting accepted a wrong term through size eight, and every registered control passed. A blind recount agrees term by term through size seven. Size eight had no independent recount. The result note for this frozen grammar awaits review. This finite result leaves the whole-language census owed. `[proposed: working rule]`

### Functions held in data

**§9.2 Constructors that hold functions.**
A constructor may take a bound parameter, of multiplicity $m \in \{\mathbf{1}, \boldsymbol{\omega}\}$ (one, any); a binder may stand there. A constructor calls nothing: it holds the function, and $m$ is what the holder owes. In any rule that takes the datum apart, the function held is use-once if $m = \mathbf{1}$ and ordinary if $m = \boldsymbol{\omega}$. A data sort with a constructor holding a function at $\mathbf{1}$ must be declared use-once, and so must every data sort that holds a value of it. Applying the same requirement to each holder propagates it through nested data sorts; a declaration is refused otherwise. A use-once function may stand in exactly five places: (i) where it is applied; (ii) at a bound parameter declared $\mathbf{1}$; (iii) at a bound parameter of an operation whose rules are in the term, where every rule that can take the call (and, where the check cannot tell which can, every rule) passes the check with that parameter read as use-once (§3.12); (iv) at a constructor's bound parameter of multiplicity $\mathbf{1}$; (v) as the result of its scope. It is never held at a constructor's parameter of multiplicity $\boldsymbol{\omega}$. This adds to §1.4, §1.7, §1.16 and §7.2. (to be tested; three bounded tests ran with it assumed) `[proposed: working rule]`
Place (iii) comes from §1.14. `[proposed]`

**§9.3 Use-once functions and the one obligation.**
A function is use-once when clause (c) of the use-once rules makes it so (by it, a function that holds a use-once function is use-once), when it stands for a bound parameter of multiplicity $\mathbf{1}$ (§1.14), or when it is a continuation that holds use-once state (§3.12): in an environment, in a frame that waits with an argument already obtained, or in handler state. Invariant (one obligation): putting a function in a datum, taking it out and handing it on each move the one obligation; only running the function discharges it, and what it returns is then owed in its own right. In §3.10, fields of data are among the places a store's state is held, and in §3.12 "runs it exactly once" reads: runs it exactly once, or hands it on once. (to be tested; owed and not run: the census of the whole language with functions in data, by context) `[proposed: working rule]`

### Tasks and the scheduler

**§9.4 The theory Tasks.**
```
theory Tasks    -- a library theory: declarations and definitions
  sort Task   use-once  data Task(Unit → Unit, held at one)
  sort Wait_A use-once  data Wait_A(A → Unit, held at one)   -- one such sort for each sort A
  sort Ready  use-once  data None | More(Task, Ready)        -- waited on, written out
  effect spawn     : Task → Unit
  effect suspend_A : (Wait_A → Unit, called once) → A
  effect wake_A    : Wait_A, A → Unit    -- the continuation of each effect is declared one
  def yield = suspend_Unit(w -> wake_Unit(w, unit))
```
The continuation of `pick` is declared one in the theory Open; every resolver answers a pick once, as the host does. Exploring every answer is done by running again with other replies. `[proposed: working rule]`

**§9.5 The scheduler: configurations and transitions.**
The scheduler is a handler of Tasks into Open with state $Q$, a `Ready` queue ($\epsilon$ is `None`; $Q \oplus \theta$ is $Q$ with task $\theta$ joined). Configurations: $\langle Q \mid e \rangle$, the computation $e$ running under the scheduler with queue $Q$; $\mathsf{next}(Q)$; $\mathsf{done}$, the scheduler has returned. $K$ is an effect's continuation up to the scheduler; $F, G, F_0$ are function values; $v, w$ are values.

$$\begin{array}{ll}
\langle Q \mid K[\mathsf{spawn}(\theta)] \rangle \to \mathsf{next}(Q \oplus \theta \oplus \mathsf{Task}(K)) & \textsf{(H-Spawn)}\\
\langle Q \mid K[\mathsf{suspend}(F)] \rangle \to \langle Q \mid F(\mathsf{Wait}(K)) \rangle & \textsf{(H-Suspend)}\\
\langle Q \mid K[\mathsf{wake}(\mathsf{Wait}(G), v)] \rangle \to \langle Q \oplus \mathsf{Task}(u \mapsto G(v)) \mid K(\mathsf{unit}) \rangle & \textsf{(H-Wake)}\\
\langle Q \mid w \rangle \to \mathsf{next}(Q) \quad (w \text{ a returned value}) & \textsf{(H-Ret)}\\
\mathsf{next}(\epsilon) \to \mathsf{done} & \textsf{(H-Empty)}
\end{array}$$

$$\frac{Q \neq \epsilon \qquad \mathsf{pick} \text{ answers a place of } Q, \text{ holding } \mathsf{Task}(F_0) \qquad Q' = Q \text{ without it}}{\mathsf{next}(Q) \to \langle Q' \mid F_0(\mathsf{unit}) \rangle}\ \textsf{(H-Pick)}$$

(H-Ret) is one rule for the first body, a task's body and the function given to `suspend`: each returns to $\mathsf{next}$ with the queue as it then stands. Invariant (queue): each rule hands the queue to exactly one successor, the computation it runs or $\mathsf{next}$. A failure in a task: §9.13. `[proposed: working rule]`

**§9.6 What the scheduler's rules say.**

1. Invariant (tasks): a task is its continuation up to the scheduler, and each is held at one. Evidence: with `yield` declared one, all 68 schedulers that dropped or doubled an ordinary task are refused and no right one is (bounded test; the recount gave the same 68).
2. With `pick` unresolved the term means its set of outcomes over every answer to the picks (§1.53): $\mathrm{Out}(t) = \bigcup_{\alpha} \mathrm{Out}(t, \alpha)$, $\alpha$ an assignment of answers to the picks. Each $\alpha$ is one sequential run, replayed from its record. A resolver is a scheduling policy and answers each pick once; a machine's scheduler, later, is a tracker for `pick` (§3.2).
3. Between two picks no other task takes a step, so what a task does between two picks is undivided as far as this scheduler's orders go. That says nothing of a machine, of a host's request or of handlers outside. A task that suspends between a read and a write has made its update in two parts, and the lost update is among its outcomes. Case (the counter; bounded test, recounted): outcomes $\{1, 2\}$ without the lock, $\{2\}$ with it. Illustration: two increments from 0 that both suspend between read and write read 0 and 0 and write 1 and 1; run one after the other they reach 2.
4. Where every answer to the picks gives the same observations ($\mathrm{obs}(r_\alpha)$ equal for all $\alpha$), `pick` leaves the manifest by indifference (§1.49): the tasks do not race as far as anything observed can tell.
5. Scheduler's freedom: only tasks in the queue are offered to `pick`; a task that waits is held by what it waits for. "Can run" means enabled in this library. It is no promise that a task finishes, that a host answers or that a resolver is fair, and a wait outside the library is not registered.
6. This higher-order core needs §9.2. A scheduler over first-order command tags and explicit task state is a separate design with its own proof; nothing here rules it out. `[proposed: working rule]`

**§9.7 Handlers by substitution: a candidate, not a rule.**
Open: whether a handler with state is applied by substitution (§1.40), so that a continuation that crosses a handler is a function value like any other, the frames it captured are environments of function values, and the handlers field of §8.8 can go. Worked by hand on one case, not run. It is an unclosed translation obligation: §1.40 alone neither forbids handler frames at run time nor fixes when handlers disappear; until it closes §8.8 keeps the field. Owed before the field goes or the cases of step are counted: what "at $n$" means and how a continuation is applied; the return case, with where the successor state goes; the completion wrapper for a task that performs no operation; an operation performed by a bound argument whose body is not in the term; a store outside the scheduler, which stays ambient and must supply its current state when a task resumes; rules that call themselves; nested handlers of one operation. Evidence: a bounded test classified its 600 configurations correctly (120 admitted and right, 480 refused and wrong) and established neither a new primitive nor an unchanged step. Run again with each handler read as a function that passes its state, on the generic evaluator with no case added and new source rules supplied, the 600 were confirmed for that evaluator and that encoding (§23.2 row 24). An independent interpreter recounted 6,324 completed answer tapes, 41,616 reads and 15,216 calls of the choosing rule. The evaluator text was byte-for-byte unchanged for this encoding. Not tested: general substitution, writes, stores that interact, a bound argument whose body is not in the term, recursion, failure, fairness, schedules without end. `[open]`
Candidate translation, for continuations declared to run once (partial supporting evidence, with the program neither shown nor rerun): a use-once datum that is either a return or a request holding its payload and the rest of the computation; a handler is an ordinary definition over that datum, with a rule for a return, a rule for its own request and a rule that passes any other request outward. Open: two points the candidate shows owed and not chosen. A callback compiled apart must return that datum, so its calling convention changes. A request made inside a handler's own clause goes to an enclosing handler in the candidate, which substitution alone does not decide. `[open]`

### Shared state

**§9.8 Cells.**
An owner: a store's handler round the scheduler owns the state, §3.10 to §3.13 apply as they stand, and tasks hold references. A cell moves a value between holders. It does not lend.
```
sort Cell_S  use-once  data Free(S) | Out(waiting : a queue of Wait_S)
take : Ref(Cell_S) → S        give : Ref(Cell_S), S → Unit
def hold(c, f : S → S, called once) = give(c, f(take(c)))
```
Transitions of the cell's state ($v, v'$ values, $W$ a wait, $\mathit{ws}$ a queue of waits):

$$\begin{array}{lll}
\mathsf{take} & \mathsf{Free}(v) \to \mathsf{Out}(\epsilon);\ \text{the caller has } v & \textsf{(H-Take)}\\
\mathsf{take} & \mathsf{Out}(\mathit{ws}) \to \mathsf{Out}(\mathit{ws} \oplus W);\ \text{the caller is suspended, } W \text{ its wait} & \textsf{(H-Take-Wait)}\\
\mathsf{give}(v') & \mathsf{Out}(\epsilon) \to \mathsf{Free}(v') & \textsf{(H-Give)}\\
\mathsf{give}(v') & \mathsf{Out}(W, \mathit{ws}) \to \mathsf{Out}(\mathit{ws});\ \mathsf{wake}(W, v') & \textsf{(H-Give-Wake)}\\
\mathsf{give}(v') & \mathsf{Free}(v):\ \text{failure "cell full", both values held at it (§1.23)} & \textsf{(H-Give-Full)}
\end{array}$$

These cell rules are provisional. The counter case ran in the bounded tests. `[proposed: working rule]`

**§9.9 What the cell gives.**
Invariant (one holder): the value is with one holder at a time, and nobody gives what they do not hold. Invariant (undivided take and give): from reading the cell to writing it there is no pick; in a contended take the function given to `suspend` writes the cell before it returns to $\mathsf{next}$. The cell does not give return: a task may take a value and finish it, or send it elsewhere; the cell then stays `Out`, whoever waits on it goes on waiting, and §9.11 says where that shows. After `f` returns, `hold` attempts one `give` of its result, and that `give` may fail when the cell has been filled meanwhile, by `f` itself or by another task. `hold` does not promise that the value taken is the value given back: `f` may finish its input and return another value of `S`. A promise of return to this cell needs a condition or an authority that excludes intervening gives; that is further interface and evidence, not given here. `[proposed: working rule]`
Case: the cell is `Free(s)` and the callback separately owns `r`; `f(x) = give(c, x); r`. `take` moves `s` to `f`; `f` gives `s` back and returns `r`; the final `give(c, r)` meets `Free(s)` and fails "cell full", with both values held. The callback returned normally. `[proposed: working rule]`

**§9.10 Channels and protocols.**
```
sort Chan_A  use-once  data Msgs(a queue of A) | Recvs(a queue of Wait_A)
send : Ref(Chan_A), A → Unit        recv : Ref(Chan_A) → A
```
An empty channel is `Msgs` of the empty queue. Two tasks may each call `recv` on one channel: one gets the message and the other waits; what the check refuses is the same use-once value at two places. A value sent is moved, by clause (b) of the use-once rules. (channels that carry ordinary messages ran in the bounded tests; a use-once payload is not run) `[proposed: working rule]`
Open: protocols, for which there is a sketch only. Owed before it can be checked: the sort of message kinds and the family of bodies; how a link binds its protocol; the equations for the dual; the membership checks on the index. What the check and membership give is order: each end follows its protocol and is closed at most once, and exactly once only on a run that returns without handing it on. They do not give progress. `[open]`

### Claims, waits and failure

**§9.11 Three claims about a term that uses tasks.**
Three things are claimed apart, and none gives another.

- Use. No run in $\mathrm{Runs}(t)$, the runs the meaning of $t$ allows, consumes a use-once value twice, and a run that returns has consumed each or handed it on (§1.22). The use-once check settles it, and settles nothing else.
- Outcomes. $\mathrm{Out}(t) \subseteq X$ for a stated set $X$, over every answer to the picks; and, where wanted, $X \subseteq \mathrm{Out}(t)$. An outcome is the whole of what the outermost scope returns or stops with, each owner's final state included. Running every answer settles the claim only where the picks form a finite tree, every pick is from a set with a covering fact, and no branch is left out, a failing one or one that stops included. Otherwise it is settled by Close where Close applies, or by a derivation. One run with its replies settles that run.
- Progress. Three claims, each read on the whole outcome: no outcome holds a waiting task; every run returns; under a named resolver, a task in the queue runs within a stated number of picks.

The scheduler's own return shows nothing: it returns when its queue is empty. A `Task` and a `Wait` cannot be dropped, so a wait that is left is in the final state of whatever owns it, and that state is part of what the owner's scope returns. Case (bounded test; all 14 tapes recounted, the 2 of this program and 12 of two controls that complete): two tasks that each receive first end, on every answer, with both waits in the store handed on and never as an ordinary result, and `discard(Task(b)) = unit` is refused. The certificate for freedom from deadlock is a library theory, later (to be tested). `[proposed: working rule]`

**§9.12 Where a wait shows: a sketch, not a rule.**
Open: whether the scope of an owner that can hold a wait returns a use-once `Ended_A`, which is `Clear(A)` or `Waiting(A, the owner's final state)`, the plain value being got by `settle : Ended_A → A` on the condition that its argument is `Clear` (§7.8). The possibility of a wait is then carried by the result's sort and by an ordinary guard's failure in the manifest, with no new kind of manifest entry. New and not run. Owed before it stands: (1) owner completion defined for every state: `Clear` must certify that every remaining obligation was finished or transferred into `A` or another continuing carrier, since an owner can end with `Free(s)` and no wait, and `Clear(Unit)` would then leave `s` out; (2) the bridge from "no outcome holds a waiting task" to `Clear` at this call, which the first does not give; (3) the test named as §7.8 asks: a pure, total probe that returns its whole `Ended` argument with the answer, with its claim, and with the whole carrier kept on failure. `[open]`

**§9.13 A failure in a task.**
Open: the task-failure rule. Under outcome B of §1.24 the proposed rule goes on only where the failed task held nothing, and otherwise fails in its turn, with the queue and the task held at the stop. `[open]`
Outcome B is the one chosen. (for now; outcome A may be reconsidered) `[decided]`
Alternative set aside for now (outcome A): the scheduler would take what the task held and may not be dropped, from the never-runnable continuation of a caught failure that takes no answer. Where the theory names someone who looks after the task, the rule would hand them the payload with what it took, end the task and go to $\mathsf{next}$, and the others would run on. Where there is nobody to hand to, or something held cannot be taken, it would fail in its turn, with the queue and the task held at the stop. Going on would still require every taken obligation to be used, finished or permissibly handed on, with nothing owed left in the residual continuation; functions and unnameable sorts remain outside take. It supplies no general recovery rule for resource or fuel stops. Tasks as written names nobody, so a later choice of A would not by itself let the others go on. (set aside for now) `[decided]`
If the usage mark is split (§1.28), `Task` and `Wait` carry both marks. `[proposed]`

### Cost, and counted looks

**§9.14 What the core costs.**

| Kind | What |
| --- | --- |
| Trusted programs that change | The use-once check: the five places, fields in the account, the rule on moving. The signature record and admission: a constructor may hold a function. The run record: requests and replies. Outcome B of §1.24 adds no take; outcome A would add it if chosen later. Slice 1’s use-once check reads one mark. If the later split is adopted, the check reads both marks (§§1.28–1.29). Also the costs §1.23 already brings: liveness in order of evaluation, what a possible failure holds in the manifest, held values in outcomes, a watch on the compiled run |
| Trusted programs that do not, on a condition | The evaluator. Step, if the translation of §9.7 is specified and holds; that is not shown |
| Declarations a build takes as true | The continuation of `pick` declared one. The sorts and multiplicities of Tasks, Cell and Chan. `Ended` and the condition on `settle`, if §9.12 is taken |
| Library definitions, checked like any | The scheduler's rules, `yield`, `take`, `give`, `hold`, `send`, `recv`. That a given scheduler does what a client wants is the outcomes claim, owed for each |
| Statements and evidence owed | The three kinds of claim of §9.11, each with its scope and the whole configuration it reads. A soundness claim for any checker of them (§13.8). The census of §9.3. The translation of §9.7 and its preservation of scope and activation. Agreement of use between source and compiled runs. An identity for each fresh run |

The stated division of responsibilities belongs to the working concurrency core. `[proposed: working rule]`

**§9.15 Looking twice at a held-out set: count it.**
Each run that looks leaves a record, a second run of the same job is another run, and a result carries the number of looks behind it. Giving each test set to one job is a promise about jobs only and does not stop that job looking twice. Counting closes nothing: a rule that forbids can be added over the same records later. Alternative not taken: forbid the second look by a gatekeeper that hands out one permission. Still owed: an identity for each fresh run, and checked links from a result to its looks. The design architect chose counting under the project owner’s delegation. Only that direction is settled. `[decided]`
The look record, private evaluator and three accompanying scope statements are specified separately. Their exact terms are unavailable here. For the second scope statement, a confirmed nested-update test (§23.2 row 16) rejected the target tracker under the tested finite reading of §3.15. The result requires no change for that case and settles no general relation or scope statement.

<a id="ch-10"></a>

## 10. The path that always runs

**§10.1 Default representation; admission.**
Every sort has a default representation: uniform, boxed, every guard in place. `[decided]`

A program $P$ is admitted when (i) each membership is $\mathsf{yes}$, guarded or assumed by name where allowed (§7.6: permission controls from slice 2, never under rule 10); (ii) every application it can reach has a way to run; (iii) its meaning manifest $\mathcal{M}$ fits the bound. A way to run is (1) a rule that matches, (2) an evaluated definition, (3) an implementation in the host, (4) a selected interpretation whose image in turn has a way to run, or (5) for a symbol with rules, the failure of a call no rule matches: a failure with a stated payload (§10.3), observed as any failure. A declared symbol with no rules and none of (2) to (4) is refused; (5) gives it nothing. Where rules are not shown to match every admitted call, the possible failure is an effect in $\mathcal{M}$ (a call may fail; not: one does) and the bound decides admission. `[decided]` An otherwise admitted call can therefore fail cleanly for no match when it runs. Not taken: refusal at admission unless the rules are shown to cover every case. `[decided]`

Case: over a sort of two values, the one rule `f(0) = 0` leaves `f(1)` unmatched. If the bound admits the possible failure, this call fails cleanly. `[decided]` The sort is a data sort with `0`, `1` its two argument-free constructors: a pattern is built from constructors and variables (§7.2, §8.2); a literal is no pattern. `[proposed]`

**§10.2 Shown to cover.**
In slice 1 a last rule whose patterns are all variables covers every call, whatever rules precede it. Slice 1 also accepts rules giving each constructor of a data sort once at one argument, with variables below. Counting only the last all-variable rule was considered and not taken. From slice 2 the case split shows coverage. `[decided]`

Under the proposed narrow reading of constructor coverage, the symbol has exactly one rule per constructor $c$ of one data sort, all at the same argument place. Each has $c(x_1, \dots, x_r)$ there, every $x_i$ a variable, and a variable at every other place. No two match one call, so order does not matter. Outside this shape and the last all-variable rule, coverage is unestablished in slice 1. The possible failure enters $\mathcal{M}$ and the bound decides (§10.1). `[proposed]`

**§10.3 Failure payloads.**
For a call $f(v_1, \dots, v_k)$ let $I$ be the positions at observed sorts, less use-once sorts. No rule matches: $\mathrm{payload} = (f, \langle v_i \rangle_{i \in I})$; a use-once argument is held, not in the payload. Not taken: the payload left to each symbol's specification. `[decided]` Illustration: for $f(a, h, b)$ with $a, b$ observed and $h$ use-once, $I = \{1, 3\}$ and the payload is $(f, \langle a, b \rangle)$, with $h$ held.

Retained values keep parameter order; an omitted argument contributes no value. The record's decoding rule maps each retained value to its parameter position from the instantiated signature and the call's admission context; the signature alone serves only where those checks determine the omitted positions, else the record keeps the position information in its decoding account. What is omitted and what is held under §1.23 are unchanged. `[proposed]` Open: the byte encoding, to be specified and tested. `[open]` Open: the wider boundary with the host that this payload belongs to. `[open]`

A membership guard (§7.6) or a condition's test (§7.9) rejects: $\mathrm{payload} = (f, j, \langle v_i \rangle_{i \in I})$, $j$ naming the rejecting check; use-once arguments omitted and held as above. `[decided]` Use $j=\mathsf{membership}(i)$ for parameter position $i$, or $j=\mathsf{condition}(h)$ for list position $h$. Its bytes are open. `[proposed]` Further:

- this path meets the guard's ordinary use-once admission checks; no value is copied or made live again after consumption;
- the call's source place is not in the semantic payload but in the run's diagnostic record, linked to the call identity in the build's report (§7.6); a host may read it, yet the diagnostic site joins neither the program's semantic observations nor those compared under §8.10;
- this describes the guard's rejection and replaces no earlier failure of a test, fuel cut or internal runtime fault with a new failure;
- the existing held account, failure recovery rules and open result-check outcomes stand;
- three other recorded options for this payload remain unselected. `[decided]`

**§10.4 Invariant: an admitted program runs.**
For every admitted $P$ the plain path gives a plan $\pi_0$ under the default bound, with its machine-model conditions settled as §4.13 requires (§10.11). A missing proof about a representation makes code slower, never stuck; a missing membership or way to run is a refusal, or a failure the manifest names; no assumption supplies a way to run. `[decided]`

A report identifies the refused subject and its causes. For a source violation give the rule and place. For an unsupported form give the form and slice. For an unknown obligation give the claim and missing evidence. For an exhausted search or check give the bound. Exhaustion leaves $\mathsf{unknown}$ and preserves established results. Report $\mathsf{no}$ as such. For a conflict, give both pieces of evidence without assigning fault (§4.2). A stage may refuse a plan, rewrite, representation or build check while the source remains valid. Causes can overlap or extend beyond this list. `[decided]` Exact fields, bytes and diagnostic or record placement remain open. `[open]`

**§10.5 The checked low-level form.**
A form of Loom's own, of no backend, between the admitted program and the backend. Abstract syntax, using illustrative keywords:

```
program ::= entry-id def+
def     ::= def-id block+
block   ::= label args step* end
step    ::= local ":=" rhs | "guard" test
rhs     ::= constant | "entry" name args | "call" def-id args
          | "apply" local args | "make" def-id args | "request" args
end     ::= exit | "goto" label args | "case" local ("->" label args)+
exit    ::= "returned" local | "failed" payload | "stopped" resource
args    ::= "(" local* ")"
```

- The program’s `entry-id` names one declared `def-id`. Each call or make names one definition. The entry evaluates the admitted root term, with any input locals its entry block states; it exists even if the root reaches no defined or evaluated symbol; the program names it and the build enters it. One `def` more for each defined or evaluated symbol reached.
- A step binds one local, once, on locals already bound: a constant, a runtime entry's call (`entry`), a definition's call, a call of a function held in a local (`apply`, how a bound argument is called), the making of such a function from a definition and locals (`make`), or a request to the host.
- `guard` is a step: it runs its test and on failure leaves by the failed exit with the payload of §10.3. It is for a test whose failure fails the call: a membership, which has no slower branch (§4.10), or a condition's test (§7.9).
- Where a failed test sends the run elsewhere there is a `case` branch to a block of the same definition and no guard: a representation's test sending the value to its other summand (§4.10); an attempt's rejected answer or spent bound, which go to the fallback (§20.35). A spent bound never leaves by the failed exit.
- A block states its entry locals and uses only those and its own. It ends in an exit or a branch (on a case number or not) to a block of the same definition, handing over exactly that block's stated locals. A loop is a block branching back; an evaluated definition's counted loop is lowered so, without a call.
- Slice 1 has these three exits; a suspended-run exit arrives with handlers in slice 2. The slice 1 host wait of §8.10 stays: an unanswered request remains `asked(request, continuation)`, waiting.
- Each making and each consuming site of a use-once value is marked. A consuming mark identifies the runtime entry that performs and reports the act; the mark alone does not validate that entry's act/report correspondence (§8.13, §8.14). The marks follow §21.7’s account of making and consuming, including the project owner’s decision for the settled cases. The function promised to be called once remains open (§8.14).

The check establishes: (W) the form is well made: each local bound once and before use, each call matching what it calls, every block ending in a well-formed branch or stated exit; termination not required; (G) it corresponds to the admitted graph: requests in the source's order, each use-once value's consuming sites the source term's. (G) is structural, for the step from graph to form: its $\mathsf{yes}$ alone does not give §8.10 agreement, which needs all three conditions there (outcome and value-by-value use account included), nor any agreement for later steps. The checker is defined as a program for the evaluator, run on it by the slice 1 build, and is no trusted text (§13.1, §13.2); its $\mathsf{yes}$ settles only that it returned $\mathsf{yes}$ (§13.8); it stands in the root manifest under the lowering (§1.52). `[proposed]`

**§10.6 Machine theory, slice 1.**
A theory of the target processor's instructions, not of C: its decoder reads executable bytes (§6.2) and it stays when the backend changes. The build takes it as true (§13.2). In slice 1 it says which bytes are which instruction, with operands, for the instruction forms the named C compiler emits for the printed subset under the recorded options, and for the rewrites a linker may make. It need not yet say what an instruction does: slice 1's tracking claim is settled never (§1.44); the first holding made into a machine theory is slice 3's (§19.9). Its decoder is a definition $\mathrm{dec}$ from a range of bytes to a finite sequence of instructions or $\mathsf{refuse}$; bytes outside its cover are refused, never passed. In slice 1 the build runs $\mathrm{dec}$ and the parsing and comparing of §10.7 on the evaluator; a compiled copy of any would owe agreement with its definition (§7.7). The runtime's entries are operations of a second declared part of the machine model, the theory of boxes the default representation is into (§10.9); their conditions are marked there, and §4.13 holds of them as of an instruction's (§7.9). `[proposed]` The project owner chose the order of targets for the long-term route of §0.3: x86-64 first, then Arm on the same scheme. `[decided]` On that route this theory is the machine contract under which each build's final executable bytes are checked against the checked low-level form, and it must also say what each covered instruction does. `[proposed]`

**§10.7 Decoder and comparison, generated C route.**
For the generated C route the selected comparison target is the outside C compiler's recorded output (§1.44). The project owner chose generated C for the first compiled demonstration, for now. `[decided]` For the long-term route of §0.3 the project owner chose a different check: each build's final executable bytes are validated independently against the checked low-level form (§10.5). `[decided]`

The proposed check records the assembly text $a_i$ the named compiler writes for each printed part $i$, by hash. The table $\mathit{bnd}$ records the linker's map for each section and generated function, the mapping from a map address to an image position, and the expected identity of each runtime, import and helper target. For function $g$ in part $i$, let $Q_g$ be the instructions for $g$ parsed from $a_i$ with symbolic operands resolved through $\mathit{bnd}$. Let $\mathcal{T}_g$ be the exact transformation the recorded account specifies for that range, the identity when the linker leaves its instructions unchanged. For image $E$, the comparison requires

$$\mathrm{dec}(E|_{\mathit{bnd}(g)})\ne\mathsf{refuse},\qquad
\mathrm{dec}(E|_{\mathit{bnd}(g)})=\mathcal{T}_g(Q_g).$$

Compare the expected and decoded sequences instruction by instruction and data byte by byte. Resolving a symbolic operand does not license an instruction-changing linker rewrite. For each such rewrite independently check the executable instructions **and bindings** against the expected transformed sequence under the specified transformation. Until that account exists for the selected route, the rewrite is unsupported and comparison refuses. Name everything outside the comparison as trusted or refuse it. The map's own symbol identities and ranges are trusted under the named linker unless checked apart. `[proposed]`

The comparison is a claim settled at build by a run (§19.1). The first difference refuses the build and the report names the failed check and its cause without condemning the source program (§10.4). A mismatch of bytes or bindings at load prevents entry and is recorded (§6.2). Matching the recorded machine program does not prove that the lowering preserves the source meaning. The lowering and backend remain named in the root manifest. The comparison procedure has yet to be qualified. `[proposed]` Open: the compiler and version (§19.3). `[open]`

Illustration: two calls with the same opcode but different resolved targets differ at the operand. An opcode match does not establish the required target binding.

**§10.8 The lowering, slice 1.**
One fixed program in two steps, choosing nothing: $\mathrm{lower} = \mathrm{print}_{\mathrm{C}} \circ \mathrm{toform}$. $\mathrm{toform}$ takes the admitted program (the root term's graph, the rules of each defined symbol reached, the definition of each evaluated symbol, the guards admission left in place) to the low-level form (§10.5). $\mathrm{print}_{\mathrm{C}}$ prints it as C, one function per definition, named from the symbol's identity, never its display name. Arguments run left to right before a call; rules are tried in the order written (§8.2). Both steps, the form's checker and the runtime they call stand under the lowering in the root manifest; the C compiler, assembler and linker under the backend (§1.52). The lowering is an interpretation in the sense of §1.42, but slice 1 keeps no Interpretation record of it: its records are terms, theories and rules (§19.2), and the lowering stands in the manifest by name (§13.4). Both steps, the form's check, the compiling, the decoding and the comparison belong to stage 5, Emit; a failure of any refuses the build and leaves the manifest stage 4 checked unchanged (§6.4). `[proposed]`

**§10.9 Boxes and counted references.**
In the default representation every value of every sort is a box reached by a handle: $\mathrm{box} = (\mathit{kind}, \mathit{count}, \mathit{size}, \mathit{contents})$. Copying a handle raises $\mathit{count}$, giving one up lowers it, the box is freed at 0 (a handle copied and both then given up: $1 \to 2 \to 1 \to 0$), and each owned handle is given up exactly once on every exit. The count is memory management only: no observation, and not the consumption of §1.17 and §8.10. A use-once value is a box like any other; its consumption is a separate event raised by the consuming runtime entry (§8.13), and a failed or stopped run holds the use-once values made and not yet consumed. At an agreement conclusion, consumption meets §8.10 for the same values and activations. At a permitted resource stop, requests are an ordered prefix of the reference's and each value the compiled run consumed the reference consumes, no more often; the compiled run need not reach every consuming site the continuing reference reaches. These are the per-value comparison requirements of §8.12, not a step-by-step ownership trace. Held values and ownership handoff are reported apart from releasing local handles.

Where a box cannot be made the compiled run stops for memory (§1.46, §8.12), so every slice 1 program's artefact manifest has the memory entry: from boxing, since any allocation may be refused, not from counting. §21.6 and §21.8 propose a compiled run's names and their matching relation, §8.13 and §8.14 the watch and its qualification; they settle neither the promised-once function case open at §21.7 nor that the watch is checked. `[proposed]` Open: whether a parameter is borrowed or owned. `[open]`

**§10.10 Evaluated symbols in compiled code.**
A compiled program runs an evaluated symbol by lowering its definition like any other. The evaluator's own primitives, in which such a definition ends, are run by runtime entries: code written apart from the evaluator, sharing none with the build used as the reference. Both are other code than the evaluator and each owes that it agrees with it (§7.7). In slice 1 that claim has no proof: runs on generated inputs give a $\mathsf{yes}$ for those inputs by name (§4.16), and the runtime stands in the artefact manifest by name, under the lowering. Nothing native enters the meaning manifest. §7.7 points to §13.6 for the claim of agreement. Of its five things the runtime's code brings the three fitting code that runs a definition: the definition as a program for the evaluator; the claim that the code agrees with it, $\mathsf{unknown}$ until proved; a recipe rebuilding it to the same hash. A statement of soundness and a corpus of damaged certificates belong to a checker. The distinction is the code's role, not its packaging: a runtime component acting as an unverified checker brings all five before it is named for that role; the three give no exception for checking. `[proposed]`

**§10.11 Machine-model conditions on the plain path.**
For each condition the machine theory marks, §4.13 requires admissible evidence making it $\mathsf{yes}$, with its stated restrictions on the evidence manifest and declared laws, or a test at each evaluation. Each trusted text keeps its specific soundness scope (§13.8). Where there is no such evidence and a test can stand, the test stays at each evaluation. `[proposed]` Of the nine residual obligations in §4.14, carry only what available checks leave unestablished as trust in the artefact manifest. Name the condition and the bound part of the build. Keep every available guard. No assumption discharges it. `[decided]`

No test added here turns an ordinary result an entry permits into a runtime fault. Examples, only where the entry's specified preconditions require them: at a runtime entry, that a handle it reads is not empty, a value has the kind the entry requires, an ordinal or index is below its count; at an allocation, that the size fits and it was granted; at a call, that the stack reserved is enough; at activation, that the run is on one thread. The whole set of tests per entry is the runtime interface's to give. A failed test is never a failure of the meaning and is in no payload. A refused allocation is a stop for memory; a failed test at a runtime entry is a fault of the build (§8.12). In a comparison the fault is never agreement and never a permitted stop; earlier requests and semantic records remain. A checked violation no continuation could remove establishes mismatch; without one the comparison is incomplete, and incompleteness never withdraws an established mismatch (§8.10). `[proposed]`

The stack is a resource of its own, named in the manifest on the same terms as memory in the first build. `[decided]` So a refused reservation is a stack resource stop, with the resource-stop prefix and held-value requirements, not a newly permitted semantic failure. The guard making this a clean stop on the C route is unqualified; an uncontrolled overflow or a broken reservation contract gives no permitted-stop evidence. `[proposed]` Open: the runtime reservation, root/prologue/helper/cleanup coverage and the matching manifest and bound entries, to be specified and reviewed. `[open]`

Illustration: a generated frame occupies 48 stack units while an enabled helper needs another 32. A capacity of 64 cannot meet the simultaneous demand of 80. A refused reservation is compared under the resource-stop rules. Simply observing an overflow cannot qualify that stop.

<a id="ch-11"></a>

## 11. Selection and the lock

**§11.1 The lock.**
A build writes a lock $L = (L_s, L_o)$: a semantic and an operational part. A rebuild replays the lock without searching. `[decided]` Where a plan is chosen during execution, the proposed replay also uses the run record (§12.3). `[proposed]`

**§11.2 Semantic part $L_s$.**
It records resolvers with what they read, orders, every selection a client could observe, and every assumption that removes a guard. Changing it changes the program. A representation resting on a claim settled never is such a selection. `[decided]` So is one whose tracker settles a choice the meaning leaves open, unless that choice leaves the manifest by indifference. `[decided]` So are a membership assumed by name (§7.6) and a clause assumed within the bound (§3.5). `[decided]`

**§11.3 Operational part $L_o$.**
It records the plan $\pi$ with its representations. Changing it changes nothing a client can see except time, memory, and where the program runs out of a resource. `[decided]` Per licence it records: the evidence its reading used, by hash; each question the reading put to the store with the hash of the answer, "nothing there" included; the site; the bound; every input not from the store (definitions and defaults used, and which text of the reader of evidence read it). A rebuild replays that reading; a reading at a later state of the store is a new one and may be a conflict where the old was $\mathsf{yes}$. `[decided]` Every hashed content or dependency reference keeps its canonical/hash profile context; rehashing under a new profile needs the original content and separately reviewed migration/revalidation; an old digest is never relabelled. `[proposed]` A change of profile provides no evidence by itself that observable bytes, runs or resource outcomes agree. `[proposed]`

Illustration: if a licence depended on the recorded absence of an answer, replay reads that absence. Reading an answer added since the lock was made is a new reading.

**§11.4 The lock in slice 1.**
Both parts are written before any run (§12.1), in the form later slices fill: slice 1 fixes the form, slice 2 brings $L_s$'s first resolvers, selections among interpretations and assumptions, slice 3 $L_o$'s first choices (§19.8, §19.9). $L_s$ has one entry: the default representation rests on a tracking claim settled never (§1.44), a selection by §11.2; the entry names what the root manifest names, the lowering and the backend. $L_s$ has no resolver, order, selection among interpretations or assumption, and says so. $L_o$ holds the plain path's one plan: every sort at its default representation, every part built ahead of time, the bindings the plan names (§6.2, §10.7), the root manifest's tools with their hashes (§1.52), and an empty place for a part whose plan is chosen in a run (§12.3). A rebuild replays it. `[proposed]`

<a id="ch-12"></a>

## 12. Building ahead of time and during a run

**§12.1 Two build modes.**
Each part $i$ of a program has a mode $b_i \in \{\mathsf{aot}, \mathsf{jit}\}$: built ahead of time, or during a run. Both are in the design from the start; $\mathsf{aot}$ is the default. `[decided]` Under $\mathsf{aot}$ a build writes its bytes and its lock before any run (§6.1, §11.1). $\mathsf{jit}$ is optional and chosen for a part: stages 4 and 5 run for that part during a run. No record that slice 1 fixes (the lock, the run record, agreement) may assume that all of a program's code exists before the run. `[proposed]`

**§12.2 What a $\mathsf{jit}$ part owes that an $\mathsf{aot}$ part does not.**

1. A choice it makes in a run is settled once in a run or at load (§4.1), by the same reading of evidence at the site (§4.5). The run then needs the reader of evidence and the store; their builds are in the artefact manifest. `[proposed]`
2. It chooses only within the lock's operational part. Every selection in the semantic part is fixed by the build's lock before the run (§11.2), so the program is the same program however its parts are built. `[proposed]`
3. Each time it makes code, the bytes are decoded by the machine theory's own decoder and compared, the tracking claim is owed as for any code, and the check of §6.2 is made before the code is entered. Whatever makes memory runnable inside a run is a loader, trusted by name or checked (§13.2). `[proposed]`
4. Code made in a run is kept while any entry into it can still be used. `[proposed]` Open: who owns it and when its life ends. `[open]`
5. Agreement is with the reference run (§8.10), for every run, whatever mix of code ran. That a run built one way and a run built the other agree with each other follows only from each agreeing with the reference. Where the meaning leaves a choice open, the lock's semantic part makes them the same. `[proposed]`

**§12.3 The lock and replay.**
The operational part may record, for a part, that its plan is chosen in the run, by which planner and under which bound. The run record $\mathit{rec}$ then holds what was chosen, and a replay takes its choices from the lock $L$ and $\mathit{rec}$, $\mathrm{choices}(\mathrm{replay}) = \mathrm{choices}(L, \mathit{rec})$, and does not search. A first-call build may construct code during a run. The five-stage pass (§6.1), load check (§6.2) and slice 1 plain path (§19.2) describe ahead-of-time building. `[proposed]`

**§12.4 First: one fixed first-call build, slice 2.**
Slice 2 includes one fixed first-call build with its finish line (§19.8). Slice 1 stays wholly ahead of time. `[decided]`

Case: `f(x) = x + 1`, built at its first call with the one default representation. It chooses nothing, so needs no planner, and it tests that no record assumes all of a program's code exists before the run. The part's states:

$$\mathsf{unbuilt} \xrightarrow{\text{first call}} \mathsf{building} \xrightarrow{\text{emitted; bytes decoded and checked}} \mathsf{entered}, \qquad \mathsf{building} \xrightarrow{\text{build fails}} \mathsf{stopped}.$$

The proposal gives five checks for this example. Emit the part at its first call. Decode and check its bytes before entering them. Name that build in the run record. Establish that this run agrees with the reference. Establish that the same program built wholly ahead of time also agrees with the reference. `[proposed]`

$\mathsf{stopped}$: a failed build stops the run cleanly, with no spare copy of the function. The run is recorded as stopped, with the reason and what it held, never as agreement. `[decided]` What it held is every use-once value not consumed at this call, including the arguments already obtained and what is held in callers, environments, waiting frames, continuations, handler state and owned data (§1.23, §1.24, §9.3). The failed-attempt record binds that whole held account and the comparison that checks the stop, whatever its resource classification. Stopping neither consumes nor drops those values nor transfers them to the host; the deferred function has not been entered. The program's requests already made remain in order, and the stopped program makes no further request. The record names the part, the call at which its build was attempted, the reached step and the reason for failure. This account is required whether or not the stop is classed as a resource stop. `[decided]`

Open: whether this is a resource stop in the sense of §3.17. If it is, the resource-stop record and comparison requirements of §8.12 apply as well; if not, its separate stop rule is still owed. `[open]` Open: the concrete link from the failed attempt to the stopped run's held account, the record's fields and bytes, the lock fields and the loader contracts. `[open]`

**§12.5 Then: a plan chosen in a run, slice 5.**
Slice 5 has the planner and code as a name for its term. In the proposed slice 5 test, one part of one program is planned and emitted during a run; its bytes are decoded and checked before they are entered; that run agrees with the reference run; the same program built wholly ahead of time agrees with it too; a replay makes the same choices without searching. Every other part builds ahead of time, under the default in §12.1; §22.6 (g) proposes how slice 1 tests that. `[proposed]`

**§12.6 Choosing a mode for each part.**
Where a program falls into parts handled independently and each part takes at most one mode, the allowed choices form a partition matroid with the parts as its blocks. That is the only matroid here: compilation itself is not one. With a cost $\mathrm{cost}_i(b_i)$ per part, a fee paid once for having any part $\mathsf{jit}$, and a charge per differently built neighbouring pair in the set $E$ of boundaries,

$$\mathrm{cost}(b) = \sum_i \mathrm{cost}_i(b_i) + \mathit{fee} \cdot [\exists i.\ b_i = \mathsf{jit}] + \mathit{edge} \cdot \sum_{\{i,j\}\in E}[b_i\ne b_j].$$

Taking $\min_{b_i} \mathrm{cost}_i(b_i)$ part by part is best only where exactly one mode is taken for each part, the costs add, and no part's choice bears on another's. The fee and the boundary charge do not change which choices are allowed; they tie the costs together, so the cheapest mode for each part alone need not give the cheapest whole. Case, three parts, checked by hand: the best independent choice costs 6; $\mathit{fee} = 8$ makes "all ahead of time" best at 13; $\mathit{edge} = 4$ makes "all in the run" best at 8. Some tied costs still have an exact method, a single shared fee among them; in general the choice is a search (§1.48). `[proposed]`
Illustration, one table of costs for three parts in a row that gives all three figures: ahead of time 1, 6, 6 and in the run 3, 2, 3. Part by part the least is $1 + 2 + 3 = 6$, a mixed plan. With $\mathit{fee} = 8$ and no boundary charge, every plan with a part built in the run costs at least $6 + 8 = 14$, against $1 + 6 + 6 = 13$ for all ahead of time. With $\mathit{edge} = 4$ and no fee, every mixed plan costs at least $6 + 4 = 10$, all ahead of time 13, and all in the run $3 + 2 + 3 = 8$.

# Part III. Trust and proof

<a id="ch-13"></a>

## 13. The trusted base

**§13.1 The one trusted machine code.**
The only trusted machine code is one evaluator, built twice by independent means. It is the total first-order fragment of Loom itself. Everything else a kernel does is a program for it, so a checker is an ordinary program and the ordinary compiler compiles it. `[decided]` Total is said of the evaluator: every run $\mathrm{eval}(k, f, v)$ ends, because the fuel $k$ bounds its steps. It is not said of the programs it runs, which need not end; such a run stops as out of fuel, which is $\mathsf{unknown}$ and never $\mathsf{no}$ (§13.2, fuel). `[proposed]`

For a paired invocation, each reached reference event spends at least one unit of work when committed. A finite administrative transition such as forwarding an obtained value may be folded into that event. Between paid events, including before the first one, the admitted syntax and the profile give a finite bound on control and price calculation. No recursive entry, loop turn, unbounded preparation or publication can occur on a cycle of free transitions. Thus there are at most $W_0$ committed events and at most one terminal unpaid attempt. Waiting for an external answer leaves a recorded request; no wall-clock deadline follows. Construction can end the reference run earlier. Either allowance cut in a checker gives unknown. `[proposed]`

The project owner chose Maude as an independent second evaluator for development only. Maude stays a separate development tool and is never shipped. Downloading it requires separate owner approval. `[decided]` We propose using it for the second build in §13.1, running the Maude definition in a separate process and comparing it with the first build. `[proposed]`

**§13.2 The trusted base.**
Only the rows below belong to the trusted base (§14.1). `[decided]` The hash-profile clause, wherever cited, is: hash-bearing identities and references are qualified by their exact canonical/hash profile; replacing it requires explicit new evidence or reviewed migration, without claiming that old and new observable bytes, runs or resource outcomes agree. `[proposed]`

| Trusted | Why it cannot be removed |
|---|---|
| The evaluator, in two builds | Something has to run. Every run record names the build, and the two are compared `[decided]`. The hash-profile clause applies `[proposed]` |
| Interning inside the evaluator: equal values are one node, seen by `same` and by memo. A sequence is one node by its name, not by what it holds (§17.2) | It is how a program sees identity, so no separate loader is needed `[decided]` |
| Content hash as identity | Where two hashes agree and both contents are in hand, the contents are compared: a collision is a refusal, never a merge. Where only a hash is in hand (a lock, a cache record, another store) it is trusted, by name, that the named hash function gave no collision among the items cited. No number is attached `[decided]`. The hash's exact named profile accompanies its references; the proposed function is SHA3-256, subject to review and adoption; exact content comparison and collision refusal stay required when both contents are available `[proposed]` |
| Fuel on every run | Fuel is the step bound. The evaluator is total; the programs it checks need not be. Running out is $\mathsf{unknown}$, never $\mathsf{no}$ `[decided]`. A build of the evaluator that ends for want of its own stack or of the machine's memory before its fuel is spent has given no answer: that end settles nothing, $\mathsf{unknown}$ and never $\mathsf{no}$ `[proposed]` In the paired profile work bounds the number of committed reference events, and either an unpaid work price or an unpaid construction price ends that checker invocation with unknown. A qualified host stop records its own cause. `[proposed]` |
| The texts of seven programs, each from the slice where it enters. Slice 1: the manifest computer, the use-once check, the reference run, the first part of the obligation generator (sort membership). Slice 2: the case split, the reader of evidence at a site, the obligation generator for laws. Slice 3: the obligation generator for tracking clauses. Slice 4: the derivation checker | They define what a manifest, a use, a run, a clause, a reading of evidence and a derivation are, whatever runs them. The reader of evidence applies the rules of §4.4 to §4.7, §4.11 and §4.13 `[decided]`. The manifest computer's walk has a second result, the uses, counted here `[decided]`. Open: whether the closure checker is counted with the case split, in slice 2, or as an eighth text; settled when the trusted texts are written; §13.12 bears on it `[open]` |
| The three rules by which a run becomes a claim: Eval, Close, Reflect (§13.7) | They say what a run is evidence of `[decided]` |
| The statements of the tracking claim | A clause is trusted to say what is meant, as any statement is `[decided]` |
| The declarations a build takes as true | Its theories, with their covering, use-once and multiplicity declarations; the machine model with the conditions it marks; the system-call model `[decided]` |
| The reading of the text | Every claim is about a graph. A build records the bytes of its source, the reader and the elaborator each by hash, the version of the syntax, the graph by hash, and each question the elaborator put to the store with its answer. That the graph says what the text says is a claim. Either it is settled by a checked correspondence between the two; or it is not owed, because the build declares that the graph itself is the program: the declaration binds that exact graph to the rendering of it that was inspected, and the rendering must be faithful. Showing the graph is neither. Otherwise the reader stands in the artefact manifest by name. In slice 1 the reader stands in the manifest, beside the lowering `[decided]`. The hash-profile clause applies `[proposed]` |
| The hardware, and the loader of binaries | Nothing runs without them `[decided]` |
| Each decider, checker or oracle still named in a manifest | With the assumptions it declares `[decided]` |

**§13.3 A faithful rendering.**
A rendering shows a run that is bound once apart from code that stands at two places. Under §8.3 those are two programs: the second consumes twice where the first consumes once. `[decided]` Open: which form the checked correspondence takes after slice 1. `[open]`

**§13.4 Not trusted.**
The elaborator, the planner, every proposer and solver, the passes, the assembler, the SRE, SkeinLab, the optimizer, and agents. The two theorems of §14.2 and §14.4 are results with manifests. Until they are proved, evidence for the one program serves: a derivation from slice 4 on, and before that the lowering is named in the manifest. `[decided]`

**§13.5 Three routes for a fact established by a run.**
Replay defines evidence. The second route is the default for flat work, and the manifest names the route taken. `[decided]` The project owner reported the measurements below for generated proofs of two shapes, long lists of clauses and trees.

| Route | Cost against a direct check | What the manifest gains |
|---|---|---|
| Replay by the evaluator | Measured: 14 to 33 times on long flat proofs, 2.5 to 4.3 times on tree-shaped ones, for a well-built checker | Nothing |
| A checker proved correct once, then compiled | About one | The compile chain and machine model, less what has tracking evidence |
| An unverified checker | About one | That checker, by name and hash |

**§13.6 What an unverified checker brings.**
To be named in a manifest it comes with five things: (1) its definition as a program for the evaluator, which is what replay runs; (2) the statement of its soundness claim; (3) the claim that it accepts only what that definition accepts, $\mathsf{unknown}$ until proved; (4) a recipe that rebuilds it to the same hash; (5) a corpus of damaged certificates, made by mutating valid ones, each labelled by replay under the definition as accepted, refused or unknown at the budget; it must refuse every one labelled refused. A mutation can leave a certificate valid. Agreement on valid certificates shows nothing about a checker that accepts everything. The corpus result is a note. `[decided]` The hash-profile clause of §13.2 applies. `[proposed]`

### How a run becomes a claim

**§13.7 Three rules.**
Write $\mathrm{eval}_\beta$ for a run by build $\beta$ of the evaluator, $\mathit{close}$ for the closure checker, and $\varphi \triangleright M$ for a claim $\varphi$ with manifest $M$.

$$\frac{\mathrm{eval}_\beta(k,f,v)=w}{f(v)=w\ \triangleright\ \{\beta\}}\ \textsf{(L-Eval)}\qquad\frac{\mathrm{eval}_\beta(k,\mathit{close},D)=\mathsf{yes}\quad C(D)}{\Phi_D\ \triangleright\ M_D}\ \textsf{(L-Close)}\qquad\frac{\mathrm{eval}_\beta(k,\mathit{chk}_T,d)=\mathsf{yes}}{\mathit{chk}_T\text{ accepted }d\ \triangleright\ \{\beta\}\cup\mathrm{laws}(d)}\ \textsf{(L-Reflect)}$$

Eval covers its input and, for sequence use, its starting state (§17.3). Close concludes a property for words over the generators of a checked finite description closed under them. Eval and Close precede Reflect in slice 4. `[decided]` In the proposed Close account, $C(D)$ requires the trusted checker, scoped soundness and checks of the named start, generators, steps, relation and questions. $\Phi_D$ covers every finite word in those generators for one hidden argument or finite term for several, with all argument tuples checked. $M_D$ names the build and, for an infinite meaning, carries the checked bridge, scope and dependencies (§§13.10–13.11). `[proposed]` Reflect establishes acceptance of $d$. Its statement needs the checker’s soundness for that form, theory and scope, with its dependencies (§13.8). `[decided]`

For direct or transitive sequence access, the record and Eval claim name the starting state $\sigma_0$. The equality covers only that starting state and the build that ran. `[decided]` Write $f(v\mid\sigma_0)=w\ \triangleright\ \{\beta\}$ for (L-Eval), the form in §13.8 and `gives(f,v,w)` in §7.15. `[proposed]` State-identifying bytes remain open. `[open]`

Slice 1 uses Eval alone. Any evaluator program can supply $f(v)=w$ for the input, including the four trusted texts, `same`, admission comparisons, literal checks and other checks in this slice. Further conclusions need scoped soundness and its manifest (§13.8). Slice 1 has neither a trusted closure checker (§§13.2, 13.11) nor a claim for Close: its single tracking claim is settled never (§1.44). Close first applies when its checker enters, a slice to be chosen when the trusted texts are written. `[proposed]`

**§13.8 What a run shows.**
Eval settles only $f(v) = w$ for the input and build that ran, with the named starting state for sequence use (§13.7). A run of a checking program on a statement $\varphi$ settles that the program returned $\mathsf{yes}$ on $\varphi$. $\varphi$ follows only with a second claim, the program's soundness:

$$\frac{\mathit{chk}(\varphi) = \mathsf{yes} \qquad \text{sound}(\mathit{chk}):\ \forall \psi \text{ of this form, in this theory and scope}.\ \ \mathit{chk}(\psi) = \mathsf{yes} \Rightarrow \psi}{\varphi}\ \textsf{(L-Sound)}$$

In words, the second premise says that what the program accepts is true, for statements of this form, in this theory and scope.
Each trusted text has one such claim, which is what §13.2 trusts that text for, and its name gives it no other. For any other checker the claim is proved, or it stays $\mathsf{unknown}$ and stands in the manifest as an assumption by name. `[decided]`
Case: a checker that accepts everything, run on $0 = 1$, gives a true run record and a false statement. `[decided]`

**§13.9 Replacing a justification.**
When the planner first replaces a justification, review this proposed requirement. The replacement identifies the same claim, scope and use, and names its checker, what establishes the checker’s soundness for that scope and every dependency still used. `[proposed]`

**§13.10 What Close covers.**

- The description, the start cases and each step are checked against the generators the conclusion names, as terms. A table fitted to answers is not the operation that gave them: Close on a table concludes about the table.
- Each step is shown for every argument the generator admits, every outcome it may have (failures among them), and every value a name stands for. Where a name stands for infinitely many values that is a statement about all of them; trying one is not enough.
- The conclusion is for every finite word over generators of one hidden argument, and for every finite term over generators of several, with every tuple of arguments checked.
- Not covered: a run without end (§3.8); a generator that takes a bound argument. It does not say that an outcome exists where a generator is partial. `[proposed]`

Case: the table $0 \mapsto 0$ is closed, the real operation takes 0 to 1, and Close on the table gives $x = 0$ after every word. `[proposed]`

**§13.11 When a run is evidence by Close.**
Only when the program that ran is the closure checker, one of the trusted texts, with its soundness claim. A run of any other program, by itself, settles only what that program returned; anything further needs that program's soundness claim, with its scope and what it rests on. The description has finitely many states. Where the meaning has infinitely many, Close on a finite description concludes about the meaning only with evidence that each question asked gives the same answer through the description (the bridge): laws of a declared theory, which then stand in the manifest, or a derivation, from slice 4. The claim names the scope of values it is for and the naming relation, and its start, steps and answers are each checked for that scope. What ties the infinitely many values to the finite description, the scope with it, stands in the manifest. `[proposed]`

Cases. (1) A program that returns true on every input, offered as the closure check. (2) Braids with integer matrices, named by the matrix mod 2: the six names are closed under the generators, and that they answer parity rests on two laws, for the braids built from the empty braid by the two generators and not for every stored value. The split over all 16 matrices mod 2 fails six cases for each generator, so the relation is cut down to what is reached, with that cut checked, or the wider claim is refused. `[proposed]`

Illustration: a two-state table toggles even and odd. To use it for successor on the naturals, name $n$ by its parity $p(n)$ and establish the start $p(0)=\mathsf{even}$, the step $p(n+1)=\mathrm{toggle}(p(n))$, and the readout of every question in scope. Asking whether $n=0$ defeats this naming: 0 and 2 have one name and different answers. The closed table alone establishes no bridge for either question.

**§13.12 The Close program.**
A run counts as Close only if it is a run of one fixed program on a description $D$. $D$ names a data sort with its covering fact, a finite relation between names and values, and for each constructor, operation and question the real symbol and its tracker. The program checks five things:

1. the symbols are the sort's own constructors and the operations as stated, as nodes (§13.10);
2. the start clause holds;
3. every step holds for every tuple of related pairs, every admitted argument and every outcome, in the direction of the form (§14.5);
4. each question's tracker agrees with the real question at every related pair, as clause C2 has it;
5. every name the trackers can reach from the start has a value, with the use-once condition of §14.4 in the backward form.

It concludes what §13.10 allows and no more: the tracking clauses for every finite term over those generators, on the relation given. That the representation's own naming relation is the relation given is part of $D$ and is checked. It is one more trusted text, or one more entry of the obligation generator for tracking clauses; the count in §13.2 goes up either way. `[proposed]`

Its test has six cases it must refuse: a table fitted to answers where the real operation differs; a relation that passes only because a start clause changed it after removal, by removing or adding pairs, and removal did not run again; a tracker with an outcome the meaning lacks; one name for every natural number; a tracker that agrees with a made-up question and not the real one; a table that is not the representation's own relation. Run: one fixed first-order program over a registry, on eighteen descriptions: five accepted and thirteen refused, the six among them, each at its own stage. The finite trial checked 45 definitions and 352 obligations, with no unknown verdict. An independent recount with a separate interpreter agrees (§23.2 row 26). The registry, with its covering facts and where they come from, is a trusted input of that test, and its fuel is not the meter of §15.1. Not done: arbitrary descriptions, covers without end, failures as outcomes, a second build. `[proposed]`



### Checked guarantees and strict builds

**§13.13 Checked guarantees by default, named assumptions, and strict builds.**
A build gives checked guarantees by default. A guarantee wider than its checks stands only on a named assumption, and a build uses it only where it explicitly accepts that assumption by name. The assumption propagates: it stands in the manifest of every term and export that depends on it, whoever accepted it. A strict build accepts no such assumption and refuses any dependency on one, whatever any other build accepted. A provider's acceptance does not pass to its client. `[decided]`
Write $\mathrm{Asm}(\kappa)$ for the named assumptions on which a guarantee $\kappa$ still depends, and $\mathrm{Acc}(\mathcal{B})$ for those that a build $\mathcal{B}$ accepts by name. Then $\mathcal{B}$ uses $\kappa$ only where $\mathrm{Asm}(\kappa) \subseteq \mathrm{Acc}(\mathcal{B})$; every term or export $u$ that depends on $\kappa$ has $\mathrm{Asm}(\kappa) \subseteq \mathcal{M}(u)$, whichever build accepted them; a strict build has $\mathrm{Acc}(\mathcal{B}) = \emptyset$ and refuses any dependency on a $\kappa$ with $\mathrm{Asm}(\kappa) \neq \emptyset$; and each build's $\mathrm{Acc}$ is its own: an assumption in a provider's $\mathrm{Acc}$ is in its client's only where the client's build accepts it by name itself.
Admission by an assumed sort membership follows §7.6, including its slice restriction and the rule for machine-model guards (§4.13). (derived from §7.6 and the rule above) `[decided]`
For example, an effectful callback outside §14.6 needs a named assumption if its guarantee has no other sufficient proof. Read the premises on which this use still depends after §4.5 and §4.11. An assumed-role entry under §1.45 is one way a wider premise appears. The acceptance is a permission, which is a bound on the manifest (§1.45), and not evidence: the assumption stays an assumption (§4.5). (a reading) `[proposed]`
Strict builds share one strict profile, which holds the premises a strict build may take as trusted, and each strict build that receives a claim checks the premises that claim's particular proof uses. Choosing the profile's full set of trusted readers, checkers and services waits for the first real import, which brings one case the profile must accept and one it must reject. (the project owner's choice) `[decided]`
The choice deferred to the first real import covers all the premises a strict build may take as trusted, declarations included, such as a provider's asserted target law (§14.7). (the project owner's choice) `[decided]`
Three test entries, for which no acceptance may reach a strict build:

- A wider promise re-exported by a wrapper. Provider P exports f, whose guarantee reaches a callback with an effect only on the named assumption A, and P's build accepts A. Wrapper W calls f and exports g. A stands in the manifest of g. A build of W uses g's guarantee only if it accepts A by name itself, and a strict client of W refuses g, whatever P's build accepted. (derived from the rule above, for a guarantee that still depends on A) `[decided]`
- The named reader. §13.2 puts the reading of the text among what is trusted. The reader and elaborator are named in slice 1. A checked correspondence discharges the reading obligation. Choosing the graph itself as the program requires a faithful inspected rendering bound to that exact graph. §1.46 leaves the applicable tool-entry bound open. A named checker's yes establishes its return. Using the proposition also needs soundness for its statement form, theory and scope, and any required executable-to-definition correspondence. Unknown soundness is an assumption by name (§13.8, §13.6). A strict client refuses a claim that still depends on it. A named checker whose relevant obligations have been discharged can supply evidence. The reading of the text is in §13.2's table of what is trusted, and the reader is not among the claims settled never of §1.43, so the rule above alone does not make a strict build refuse the named reader; whether the strict profile includes it waits, with the other trusted readers, for the first real import. The declarations row can carry a provider's asserted target law (§14.7), and an endpoint bridge can be trusted by name (§20.7, §20.30). A row label alone does not settle either case. The nine residual obligations of §4.14 keep their named scope and remove no available guard. `[proposed]`
- The unsettled tracking of the lowering and the backend. In slice 1 the default representation's tracking claim is settled never, which is why the root manifest names the lowering and the backend (§1.44, §1.52). §1.43 counts a tracking claim with no evidence among the claims settled never by name. (restated from §1.43 and §1.44) `[decided]` A compiled-behaviour guarantee still relying on it carries a named assumption. A strict client refuses that reliance. An ordinary build must explicitly accept the named assumption if it uses that guarantee. Each compiled-behaviour guarantee states exactly which source, executable and behaviour it covers. A check tied to actual operands may certify or refute a particular run. Which bound governs this entry (§1.45, §1.46) is identified before admitting the first build that depends on such a wider promise. (the project owner's choice) `[decided]` Emitting, inspecting or storing the bytes makes a different claim. Running an otherwise admissible meaning on the evaluator remains available. The ninth residual obligation of §4.14, translation of printed code to the machine program, retains its own scope and does not establish general tracking. `[proposed]` The fixed slice 1 bound is amended only if it governs this entry and needs changing, and then only by the project owner's decision. (the project owner's choice) `[decided]`

<a id="ch-14"></a>

## 14. What is proved: the two theorems

**§14.1 What is proved.**
Nothing is proved in Loom. The proof evidence consists of a toy kernel of 480 lines, its scripts and their runs, and the reviewing scripts and their runs. Both theorems remain owed (§14.2, §14.4). What is trusted is §13.2, and nothing else. `[decided]`

The partial evaluator implementation (§0.4, §15.6) has a separate scope. Its results supply no proof of either theorem.

**§14.2 Theorem 1 (owed): representations compose.**
*Hypotheses.* $\rho_1$ names the values of $S$ by names $N_1$ over a signature $\Sigma$. $\rho_2$ names the values of $N_1$ by names $N_2$, in the same form, its signature holding every tracker $\rho_1$ uses, as the same nodes. *Conclusion.*

$$\mathrm{names}_{21}(n_2, v) \iff \exists n_1.\ \mathrm{names}_2(n_2, n_1) \wedge \mathrm{names}_1(n_1, v)$$

is a representation of $S$ in that form over $\Sigma$. Its assumptions and manifests are joined, and its scope is where both hold. `[decided]`

The theorem is stated for signatures whose operations take no bound argument. Beyond that a chain is kept as a chain, as it is for a forward link followed by a backward link, or the composite's own clauses are checked directly. `[decided]`

Case: three models of two hidden sorts, with one, two and four functions from the first sort to the second, and an operation that asks whether a function is constant. Both links pass. The rebuilt composite relates the meaning's one function to one that is not constant. `[decided]`

Illustration: for one observation and generator, let $F_0,F_1,F_2$ be its Boolean step tables at the value, middle and outer levels, and $R_1,R_2$ the two naming tables (§14.5). With $R_{21}=R_2R_1$ the forward step composes by

$$R_{21}^{\top} F_2=R_1^{\top}R_2^{\top}F_2\le R_1^{\top}F_1R_2^{\top}\le F_0R_{21}^{\top}.$$

For two backward links,

$$F_2R_{21}=F_2R_2R_1\le R_2F_1R_1\le R_{21}F_0.$$

The two inequalities in each line use the **same** middle generator $F_1$. This calculation establishes the finite step component. The asserted starts, scopes, observations, use and progress conditions of the theorem are still owed.

Finite evidence (§23.2 row 8): 427 same-form pairs passed with no wrong outcome observed; of 97 forward-then-backward pairs, 17 composites passed neither single form, although none gave a wrong observed outcome. These checks leave the general theorem owed.

**§14.3 Four hypotheses beyond the pure first-order case.**
To be kept: (H1) the middle theory is shared exactly; (H2) where an operation takes several steps, the relation holds at every point the other side can observe, not only at completed calls; (H3) the inner representation adds no failure where the outer statement says there is none; (H4) each link's measure for one-sided steps is well-founded, and the measures compose inner first. (run by nobody) `[decided]`

**§14.4 Theorem 2 (owed): a representation carries through a term.**
*Hypothesis.* The term $t$ reaches the hidden sorts of $\rho$ only through the signature. Write $\tilde t$ for $t$ on names: each $f$ replaced by its tracker $\tilde f$.

*Forward.* For each pair of jointly related inputs, whenever the term is defined on names it is defined on values. Every possible result on names has a matching result on values. Compare hidden results by the naming relation and observed results by C2 (§3.5).

$$\mathrm{names}(n,v)\ \Longrightarrow\ \forall z\in\mathrm{Out}(\tilde t(n)).\ \exists w\in\mathrm{Out}(t(v)).\ z\sim w.$$

*Backward.* For each outcome of the term on names, the term on values has that outcome for some choice the meaning leaves open, provided every use-once value passes the check of §1.12. This argument applies to each finite stretch of the run on names. For a run without end, each reachable name must also stand for finitely many values (§3.8). `[decided]`

More explicitly, take the whole name configurations $n_0,\ldots,n_j$ of a finite run and its observations $o_1,\ldots,o_j$. **For every** final joint valuation $w_j$ named by $n_j$, **there exist** predecessors $w_{j-1},\ldots,w_0$ such that $\mathrm{names}(n_i,w_i)$ throughout, and each meaning step $w_{i-1}\to w_i$ has the corresponding $o_i$ (B2). The initial valuation must be permitted by its start on the admitted arguments (B1), and every required reachable name has a value (B0). Where nothing survives, the final empty configuration is related to itself. The last step still owes a predecessor with the right values for everything it consumed (§3.9). Witnesses may differ between name runs or terminal valuations. (the backward clauses written out for this theorem) `[proposed]`

The first-order instance and its limits:

- For first-order terms over a representation that has a finite description with its covering fact, and whose trackers and questions pass the five checks of §13.12, the theorem is an instance of Close in both forms: the relation is the finite description, and each pair of an operation and its tracker is a generator.
- Where the meaning has infinitely many values, the instance concludes about the meaning only with the bridge of §13.11, which stands in the manifest.
- First-order terms over a representation with no finite description, or with no such bridge, are not covered by this instance; the theorem stays owed for them.
- It is owed from bound arguments on. `[proposed]`

The backward case is for finite stretches of a run (§3.8) `[decided]`, with B0, B1 and use-once in what is checked. `[proposed]`

Finite evidence (§23.2 row 8): 758 forward first-order systems closed under Close reached no wrong pair. Of them, 593 included a name for several values, a two-hidden-argument operation and a branch on an observation.

**§14.5 Finite systems: both forms as inequalities.**
For finite systems both forms are inequalities between tables of true and false. Let $R$ be the table of the relation (rows names, columns values), $\tilde F$ that of an operation on names and $F$ that of the same operation on values, one pair of tables for each operation and each observation, so that a step on names is compared with a step on values that has the same observation; products are Boolean and $\le$ is entry by entry.

$$\text{forward:}\ \ R^{\top} \tilde F \le F R^{\top} \qquad\qquad \text{backward:}\ \ \tilde F R \le R F$$

Each is kept when two operations are put in sequence, so each holds for every finite sequence. The calculation, which uses only that the Boolean product is monotone: $R^{\top} \tilde F_1 \tilde F_2 \le F_1 R^{\top} \tilde F_2 \le F_1 F_2 R^{\top}$ forward, and $\tilde F_1 \tilde F_2 R \le \tilde F_1 R F_2 \le R F_1 F_2$ backward; induction on the length gives every finite sequence. The greatest relation that passes is computed by removal. A start clause that removes pairs (B1) takes part from the first step, or removal runs again after it; a start clause that asks for pairs (F1) is checked on what removal leaves, and a check made only before removal is not enough.

*Backward.* Begin with the pairs $(n, w)$ such that, for every start case $c$ and every argument $a$ whose start name $\tilde c(a)$ is $n$, $w$ is an outcome of $c(a)$, as B1 of §3.8 has it. A name that is no start name begins paired with every value. Remove $(n', w)$ whenever some step on names from $n$ to $n'$ has no step on values to $w$, with the same observation, from a value still paired with $n$. Repeat until nothing is removed, and begin again after any further restriction. Then each name that must be reached needs at least one value.

*Forward.* Begin with every pair the scope allows. Remove $(n, v)$ whenever some step on names from $n$ to $n'$ has no step on values from $v$, with the same observation, to a value still paired with $n'$. Repeat until nothing is removed, begin again after any further restriction, then check the forward start clause on what remains.

In both forms the steps are those of the real generators, at every argument and outcome (§13.10), and a pair is of whole configurations (§3.9). The result is for the steps and the scope named. `[proposed]`

The finite trials found six bad relations in 48 cases when the start clause was applied only after removal. The count gives no direction for those cases (§23.2 row 8).

Case, direction of the forward form: one name, one value, a meaning that gives only 0 and a tracker that gives 0 or 1. A removal that matches the steps on values keeps the pair, and the tracker gives 1 where the meaning cannot. `[proposed]`

Case, first pairs of the backward form: a hidden sort with two start cases, `mk(0) = v0` and `mk(1) = v1`, whose start names are `n0` and `n1`; a question `read` that changes nothing, with `read(v0) = 0` and `read(v1) = 1`; a tracker whose `read` gives 1 on `n0` and 0 on `n1`.

- Beginning with every pair whose value is a start value keeps all four pairs. The `read` step then removes `(n0, v0)` and `(n1, v1)` and leaves `(n0, v1)` and `(n1, v0)`; each name has a value, and a tracker that is wrong at its first read passes.
- Beginning as B1 has it keeps only `(n0, v0)` and `(n1, v1)`. The `read` step removes both, no name has a value, and the tracker is refused. `[proposed]`

**§14.6 A third way for bound arguments, to be tested.**
*Conditions.* Every operation is total, gives one result and has no effect; every value may be copied and dropped, results and the values a function holds among them; no sort has an index. Then a representation may supply its relation at every function sort it needs. Its certificate shows that (a) application keeps the relations; (b) the combinators $\mathsf{I}$, $\mathsf{K}$ and $\mathsf{S}$, in which every binder can be written, are related to themselves at each sort used; (c) each exported operation is related to its tracker. The combinators are the standard ones: their equations are $\mathsf{I}\,x=x$, $\mathsf{K}\,x\,y=x$ and $\mathsf{S}\,f\,g\,x=f\,x\,(g\,x)$, the admitted binders are in fact translated by them, and the certificate covers every sort at which that translation uses them. Any other primitive the code may use has its own entry. $\mathsf{K}$ drops an argument and $\mathsf{S}$ uses one twice, which is why every value must allow both. Functions are equal when they agree at every argument. Two such certificates compose, relation by relation, through the same middle operations. Without (b) the certificate can be empty: an empty relation at a function sort passes a check of application alone. This way gives nothing for a function that has an effect, holds state, or takes, returns or holds a use-once value. `[proposed: working rule]`

### How a law is yes before slice 4

**§14.7 Status of a law at an interpretation.**
A law $\varphi$ at an interpretation $\iota$ is $\mathsf{yes}$ by one of three runs: (1) its statement is the same node as a declared law of the target theory, which then stands in the manifest like any law used; (2) exhaustion with a covering fact; (3) a decider named in the manifest with the laws it assumes. It is $\mathsf{no}$ by a counterexample, and otherwise $\mathsf{unknown}$. (not run in this form) `[decided]`

**§14.8 Yes by computation.**
When both sides of a law rewrite to one node with their variables left in, that is run (3): the decider named in the manifest is the normaliser, assuming nothing but the rules, under the limit on rule order of §8.5 and the reading of rules in §1.5. No fourth run is needed. Not taken: the question stays open until slice 2 counts how many of its laws are $\mathsf{yes}$ by the three runs of §14.7 without it. `[decided]`

**§14.9 Reaching every case before slice 4.**
A claim settled on an enumerated set reaches every case before slice 4 in two ways only: by Close on the real generators, where the description is finite; or by a decider named in the manifest with the laws it assumes, where the claim is that a projection onto a finite sort commutes with each generator and the decider settles it. That a declared law is used by a rewriting program is a use of that program, with its soundness claim, and not a $\mathsf{yes}$ by identity of nodes. A claim whose proof needs an invariant with a quantifier of its own waits for slice 4. `[proposed]`

Under the evidence rules available in slice 3, reports on infinite objects would mostly be candidates. Run: the loop of abducing and then generalising, on one family of polynomials, its counts confirmed independently (§23.2 row 27): the invariant with a parameter is among the schemas kept, with many others, in a language of hypotheses that already contained it. The general lift is not done: there is no covering fact, no admitted hypothesis with a quantifier, and no checked derivation. `[proposed]`

### Open, each with the test that settles it

**§14.10 Open questions and their tests.**

| Open question | The test that settles it |
|---|---|
| Owed: the use-once check on the whole language. | §1.32 `[open]` |
| Owed: a proof that representations compose (§14.2). | Prove it first for finite systems with one hidden sort and one form. Search: a random realiser of a random realiser, the composite checked against the first meaning `[open]` |
| Owed: a proof that a representation carries through a term (§14.4). | Close covers the first-order cases meeting §14.4’s finite-description, coverage and checker conditions, with a bridge for infinite meanings. Search for the rest: random terms over small representations, aimed at a name used twice, two hidden arguments, a branch then a hidden step, and a shared node `[open]` |
| Owed: higher-order terms, local state, non-termination and effects in the theorem that a representation carries through a term. | The same search with those term shapes. The clauses of §3.15, §3.17 and §3.18 are tried there for the first time: a handler that resumes twice, one that never resumes, a realiser that runs out, a loop, and a run that does not end `[open]` |
| Open: a licence for mixed forms. | Not designed. The clause once proposed is refuted (§3.4) `[open]` |
| Open: whether an interpretation and a record are one thing. | §1.35 `[open]` |
| Open: whether tracking evidence is affordable for real data structures. | Write one mutable hash map as a holding of a finite map, in a fixed two weeks. Count lines of evidence for each line of tracker. Above about ten to one, with no route to automation, holdings ship as named manifest entries `[open]` |
| Open: the foundation, three positions. | §1.62 `[open]` |
| Open: the evaluator: which form of bounded recursion, and its cost; its edge results are recorded in §16.6. | Write the trusted texts for it in both forms and measure them against direct builds. The project owner’s measurements in §13.5 are the reference `[open]` |
| Owed: the test of what a use of a claim must assume (the rule of §4.11). | In slice 4, remove one guard by a theorem that uses a classical law, and state what that use assumes as a derivation. The cases of §4.12 `[open]` |
| Open: search by proposers, at the size of a planner or of the SRE. | Ten small numeric kernels: planning time, guards left, and run time against the plain path. For the SRE, a search for a coarsest representation on the five-vertex graphs `[open]` |
| Open: where the SRE enters. | The project owner decides its later placement (§19.13) `[open]` |
| Open: the payoff of keeping the three positions apart. | Three measurements. (1) For a term as stated, no choice of representation, of plan or of guard to drop alters the meaning manifest. (2) The best plan the planner finds within a stated budget, with three representations to choose from, beats the best it finds with one by a geometric mean of at least 1.2, and the record says where a plan was found by exhaustion. (3) Checking costs under ten times, and annotations under twice, those of a conventional typed language `[open]` |
| Open: identity across versions of a theory. | Change one declaration of a theory in slice 2 and count the claims that must be settled again `[open]` |
| Open: distortion; laws of programs that draw; guarantees from a sample. | §4.19 `[open]` |
| Open: surface syntax. | Port 2,000 lines of ordinary higher-order code and count annotations `[open]` |
| Open: the form of the checked correspondence between text and graph. | §13.3 `[open]` |

The question "where a tracker must be defined" is closed by §3.6. `[decided]`

# Part IV. The evaluator

<a id="ch-15"></a>

## 15. The evaluator

**§15.1 Syntax.**

```
v    ::= n | bytes | tuple(v, .., v) | name.j(v) | set{v, ..} | sequence
decl ::= name has k cases
def  ::= f(x1, .., xk) = e
e    ::= x | v | prim(e, ..) | f(e, ..) | let x = e; e
       | tuple(e, .., e) | name.j(e)
       | case e of name.j(x) => e; .. [else => e]  -- omission requires a branch for every case of name
       | for x < e1 from y = e2 do e3
prim ::= add | sub | mul | divmod | compare | shift | bit operations -- naturals
       | get | slice | concat | hash | length -- bytes
       | get | length -- tuples
       | empty | insert | remove | member | size | members -- sets
       | make | length | contents | read, write at a position | same -- sequences
```

Definitions are first-order. Core expressions are variables, values, primitive applications, calls, let and the counted loop. `[decided]` The evaluator includes left and right shift, AND, OR and XOR. `[decided]` Their rules and charges await review. The rule text for the six kinds of value (§16.1, where four of the kinds are adopted), `tuple(e, ..)`, `name.j(e)` and the primitive table are proposed; `compare` gives a case of `order`, `same` and `member` a case of `truth`, `divmod` the tuple (quotient, remainder). `[proposed]` The evaluator holds finite sequences, not arrays: a sequence is mathematics, an array a representation of one, which belongs to representation; bytes stay as they are, not decided by this. `[decided]` For the first build the sequence rules are out under §19.2, with the starting-state part of the run record: no `make`, `contents`, read at a position, write or `same`; linked immutable tuples carry the frames, the state and the trail. `[decided]`

**§15.2 Nodes.** Let $\mathrm{node}(v)$ be the node holding $v$. For $v, w$ not sequences, $\mathrm{node}(v) = \mathrm{node}(w) \iff v = w$ in content (interning); two sequences are one node exactly when their names are equal (§17.2). `same` and memo are how a program sees identity. Equal byte contents therefore share one node. `[decided]` The partial build interns immutable naturals, tuples and the built-in `none`. `[built: milestone B, partial]` Open: how a value written outside the evaluator is mapped to a node. `[open]`

**§15.3 Judgment.** Write $\eta,\sigma\vdash e\Downarrow^{k\to k'}r\dashv\sigma'$. The environment, sequence state and run-local memo pass through the judgments in written order. In the paired profile $k=(W,C)$, $k'=(W',C')$, and $r$ is a value or an allowance cut with its reason and held account. The charges $q,c_{\mathsf{var}},c_{\mathsf{lit}},c_{\mathsf{call}},c_{\mathsf{turn}},c_{\mathsf{tup}},c_{\mathsf{con}}$ in these rules are pairs. A scalar work-only event fee $n$ abbreviates $(n,0)$. The fee for a loop turn may depend on the index of that turn (§15.4). Affordability $q\le k$ means both component inequalities. Subtraction is componentwise and is defined for payment only when both hold. Failure of affordability is $\neg(q\le k)$, including incomparable pairs. The judgment is parameterized by the meter profile. In the scalar milestone B profile $k,k'\in\mathbb N$ are the fuel before and after and $r ::= v \mid \mathsf{oof}$ (out of fuel). Its charges are naturals of the meter. These abstract rules leave $c_{\mathsf{var}}$, $c_{\mathsf{lit}}$, $c_{\mathsf{tup}}$ and $c_{\mathsf{con}}$ to the applicable table. An unspecified charge cannot be read as zero. The provisional §15.6 table gives prices for the local read, literal and tuple in the partial first build. General case construction is outside that build. In the paired profile, $\mathsf{oof}$ in these rules and elsewhere in the design names either allowance cut. `[proposed]`

Each written occurrence runs once, left to right, including repeated arguments. In P-Call $f(\vec x)=e_f$, $\mu_1$ is the memo after the arguments, and $D(f,\vec v,\mu_1)$ holds for an unmarked call or one without a completed matching entry. P-Hit in §15.7 precedes ordinary body entry. A primitive price is for the event on obtained arguments. Earlier argument events keep their charges, state and observable prefix when a later event cuts. Forwarding a result or binding an obtained value constructs nothing. A missing tariff entry is never a zero price. `[proposed]`

$$\frac{k \ge c_{\mathsf{var}}}{\eta \vdash x \Downarrow^{k \to k - c_{\mathsf{var}}} \eta(x)}\ \textsf{(P-Var)} \quad \frac{k \ge c_{\mathsf{lit}}}{\eta \vdash v \Downarrow^{k \to k - c_{\mathsf{lit}}} v}\ \textsf{(P-Val)}$$

$$\frac{\eta \vdash \vec e \Downarrow^{k \to k_1} \vec v \quad D(f,\vec v,\mu_1) \quad k_1 \ge c_{\mathsf{call}} \quad [\vec x := \vec v] \vdash e_f \Downarrow^{k_1 - c_{\mathsf{call}} \to k'} r}{\eta \vdash f(\vec e) \Downarrow^{k \to k'} r}\ \textsf{(P-Call)}$$

$$\frac{\eta \vdash \vec e \Downarrow^{k \to k_1} \vec v \quad \mathrm{chg}(\mathit{prim}, \vec v) = q \le k_1 \quad \delta_{\mathit{prim}}(s_1,\vec v)=(s_2,w)}{\eta \vdash \mathit{prim}(\vec e) \Downarrow^{k \to k_1 - q} w}\ \textsf{(P-Prim)}$$

These rules thread state and fuel left to right. A call entering the body pays after obtaining its arguments. A completed hit takes P-Hit (§15.7) and skips the body. The abstract event charges express that discipline without selecting a permanent tariff. `[proposed]` The partial first build implements natural literals, its definition's parameter, forward, self and mutual unary calls, and `add`, `sub` and `mul` at the prices of §15.6. `[built: milestone B, partial]`

(P-Let) If $e_1 \Downarrow^{k \to k_1} v_1$ and $\eta[x := v_1] \vdash e_2 \Downarrow^{k_1 \to k'} r$, then `let x = e1; e2` $\Downarrow^{k \to k'} r$. `[decided]`

(P-Tuple) If $\vec e \Downarrow^{k \to k_1} \vec v$ and $k_1 \ge c_{\mathsf{tup}}(\vec v)$, then `tuple(e, ..)` $\Downarrow^{k \to k_1 - c_{\mathsf{tup}}(\vec v)} \langle \vec v \rangle$. `[proposed]` `[built: milestone B, partial]`

(P-Con) If $e \Downarrow^{k \to k_1} v$ and $k_1 \ge c_{\mathsf{con}}(v)$, then `name.j(e)` $\Downarrow^{k \to k_1 - c_{\mathsf{con}}(v)}$ `name.j(v)`. `[proposed]` In P-Prim $s_1$ is the state after the arguments, including sequence contents, the fresh-name count and the trail where applicable. On payment, $\delta$ yields $w$ and the conclusion returns state $s_2$ (§§16.5–16.6, 17.4). A pure primitive preserves that state. `[proposed]` No primitive fails. `[decided]` Under the stated meter profile the result is $\mathsf{oof}$ when a premise gives $\mathsf{oof}$ or the fuel left is below the charge of the event reached: a variable, a literal, a tuple, a case, a call or a loop turn. `[proposed]` It is $\mathsf{oof}$, with nothing built, when a primitive's charge exceeds $k_1$ or cannot be worked out. `[decided]`

In the paired profile P-Con evaluates the payload once. If the remaining pair covers the case row, it pays that pair and returns the case with its obtained payload. P-Tuple works likewise on obtained fields. A logical constructor has the same price on a fresh allocation and an intern hit (§15.11). A paid successful transition produces its value, sequence changes, fresh-name changes and any trail entry together. A specified edge may return its ordinary value. Insufficient allowance or the profile-defined inability to establish its safe advance bound produces the cut of §15.9 before construction, with both balances at the attempted event unchanged. A cut from a premise propagates at its original occurrence. `[proposed]`

**§15.4 The counted loop.** $e_1$, then $e_2$, run once before the loop.

$$\frac{\eta \vdash e_1 \Downarrow^{k \to k_a} n \quad \eta \vdash e_2 \Downarrow^{k_a \to k_0} w_0 \quad n \in \mathbb{N} \quad \forall i < n:\ k_i \ge c_{\mathsf{turn}},\ \eta[x := i, y := w_i] \vdash e_3 \Downarrow^{k_i - c_{\mathsf{turn}} \to k_{i+1}} w_{i+1}}{\eta \vdash \mathtt{for}\ x < e_1\ \mathtt{from}\ y = e_2\ \mathtt{do}\ e_3 \Downarrow^{k \to k_n} w_n}\ \textsf{(P-For)}$$

`[decided]` Case: a loop with bound 2 records its counter as 0, then 1 (other bounds: §16.6). `[decided]`

In the paired profile P-For reads $c_{\mathsf{turn}}$ as the pair $c_{\mathsf{turn}}(i)$ for turn $i$, determined for the actual turn before the body starts. Its work is positive, with the work schedule still to be chosen. Its construction includes the logical digits of the natural index supplied to the body. A zero bound has no turn or index construction. The case above and the rule for a bound outside the naturals keep their original scope. `[proposed]`

**§15.5 Totality and the checker.** For definitions $f_1, \dots, f_m$ in program order, $e_i$ the body of $f_i$:

$$\mathrm{total}(f_i) \iff \#\mathtt{for}(e_i) \le 1 \ \wedge\ \forall f_j \text{ called in } e_i:\ j < i \wedge \mathrm{total}(f_j)$$

One pass in program order decides it. A definition may call itself; it is then not total and runs only with fuel. Here totality is the syntactic certificate above. A self-call can terminate on a particular input. `[proposed]` A checker is any definition run as $\mathrm{eval}(k, f, v)$; the result $\mathsf{oof}$ is $\mathsf{unknown}$, never $\mathsf{no}$. `[decided]` The file driver executes its supported definitions with fuel and reports exhaustion. `[built: milestone B, partial]`

**§15.6 The meter.** A call and a loop turn each charge 1, that is $c_{\mathsf{call}} = c_{\mathsf{turn}} = 1$; a primitive charges by the bit length of its arguments (numbers under review). `[proposed]` The charge for a loop turn is left to the evaluator's specification. `[decided]` For the full per-primitive tariff, let $a_p(v)$ denote the argument contribution for that value and operand in profile $p$. For a natural this can be its bit length. The active primitive, profile and state are implicit:

$$\mathrm{chg}(\mathit{prim}, \vec v) = \alpha(a_p(v_1),\dots,a_p(v_n)) + \beta(\vec v) + \gamma(\vec v)$$

Before it builds anything a primitive works out $\beta$, an upper bound on the size of its result and of whatever it needs meanwhile, in a way that cannot itself overflow, and pays it. The work $\gamma$ is charged apart, by the primitive's line in the meter's table; the table, one line for each primitive, is part of the evaluator's specification and both builds charge by it. `[decided]`  Case: `shift(1, 2^64)` has small arguments (1 and 65 bits) and a result of $2^{64} + 1$ bits. Open: the table's entries for the natural and byte primitives and the size of its unit are not written; complete meter integration remains. `[open]` The entries for the other primitives are a proposal (§17.4). `[proposed]`

The charges above are scalar. `[proposed]` A run in the paired profile starts with two separate finite natural allowances, one for reference work and one for cumulative construction. `[decided]` $W$ counts units of reference work fixed by the named table, including mandated advance prices. $C$ counts units of logical value construction fixed by §15.11. Every reached event has a positive work price $w$ and a nonnegative construction price $c$. A lookup can have $c=0$. `[proposed]` Spend neither if the pair cannot pay. Neither allowance can pay the other's price. `[decided]` Returning an already obtained value adds no event. `[proposed]`

In the paired profile $\mathrm{chg}(\mathit{prim},\vec v)$ is the pair $(w,c)$ below. The safe bound $\beta$ above splits into a result bound $\beta_R$ and a temporary bound $\beta_T$, and a primitive's line in the table may hold one row for each specified edge. For a primitive on obtained arguments, use that preflight. The paired row has

$$w=\alpha+\beta_R+\beta_T+\gamma,\qquad c=\sum_{u\ \mathrm{constructed\ by\ this\ event}} S(u).$$

Here $\alpha$ prices the arguments, $\beta_R$ is a safe result bound, $\beta_T$ a safe bound on the primitive's temporary workspace, and $\gamma$ pays the scheduled work, including any additional pass required to determine exact construction. Before construction, those four contributions are set aside in full in the event’s private work reservation. They can overlap in what they measure with $C$. A reservation and an exact construction answer different questions. Slack in a primitive's result bound and reusable private scratch do not consume cumulative construction credit. A logical intermediate explicitly built by the reference event does consume it, even if discarded before return. The row enumerates such constructions. At the final event commit its exact $c$ and its $w$ are final together (§15.12). `[proposed]`

The full table belongs to the reference evaluator. Two conforming builds use the same rows, event order, size unit, treatment of edges and schedule of the price check. They may use different layouts. §15.12 gives a concrete proposed fragment. The following historically measured table describes the existing single-balance driver only. `[proposed]`

**The partial milestone B profile.** The provisional OCaml file driver reads and checks a first-order program before starting a named unary definition on a natural input. It implements exact naturals, interned immutable tuples, the built-in wrong-kind result `none`, and the three binary natural primitives below. Each written argument is evaluated in order, including repetitions; calls to resolved definition indices may be forward, self or mutual. Reports distinguish a returned value, execution-fuel exhaustion, a pre-run refusal and a host/tool fault. Reading, resolution, checking, interning the input and literals before execution, and reporting are outside execution fuel. Reaching a literal *in* execution is charged. The file-size cap is a tool limit. A development record can identify the source, executing build, profile, initial and remaining fuel, and first unpaid event. `[built: milestone B, partial]`

For this profile take $\mathrm{bits}(0)=1$ and $\mathrm{bits}(x)=\lfloor\log_2 x\rfloor+1$ for $x>0$. A natural's argument part is its bit length; a tuple or the built-in `none` contributes one. Write $a=\mathrm{bits}(x), b=\mathrm{bits}(y), m=\max(a,b)$ for two obtained naturals. The charge adds four components in this order: argument parts, reserved result, reserved temporary space and logical work. The result and temporary reservations together are the $\beta$ of the abstract rule. For a tuple of $j$ obtained fields, $s$ sums their argument parts, counting each position even if its node is shared.

| Reached event | Argument parts | Result | Temporary | Work |
|---|---:|---:|---:|---:|
| Entry, literal, local read, or ordinary unary call | 0 | 0 | 0 | 1 |
| Natural addition | $a+b$ | $m+1$ | 0 | $m$ |
| Truncated natural subtraction | $a+b$ | $a$ | 0 | $m$ |
| Natural multiplication | $a+b$ | $a+b$ | 0 | $ab$ |
| Arithmetic on a wrong kind | $\mathrm{part}(x)+\mathrm{part}(y)$ | 0 | 0 | 1 |
| Form a tuple, including an interning hit | $s$ | $j+1$ | 0 | 0 |

Returning an obtained value has no further debit. If the next event costs $q$ and the balance is less than $q$, the event debits zero and constructs nothing. Prior debits stand. A safe bound that cannot be computed gives an out-of-fuel stop without inventing a numeric charge. These figures describe this one development profile. `[built: milestone B, partial]` The permanent tariff and complete general meter are still under review. `[proposed]`

Illustration: let `f(x) = add(x,3)` with input 2. Entry, the local read and the literal cost 3 together. Both naturals have bit length 2, so the addition costs $4+3+0+2=9$. With fuel 12 the driver returns 5 at balance zero. With 11 it reaches the addition with 8 left, stops there and spends none of that 8. For `f(x) = tuple(x,x)` on 2, entry and two reads again cost 3. The tuple costs $4+3+0+0=7$, counting both positions. Fuel 10 returns $\langle2,2\rangle$ at zero; fuel 9 stops before construction with 6 left. These are calculations for the partial driver. They do not establish a second evaluator, native/reference agreement or the full slice 1 finish check.

**§15.7 Memo.** For now only a one-argument state-free definition may carry a memo mark. To memoize several values pass a tuple as the one argument. A mark on a definition of zero or several arguments is refused before the run. Unmarked calls keep their usual arities. An unfinished entry for the current key is not a hit. The recursive call continues with the ordinary fuel rule. (§17.3 gives the proposed state-free test.) `[decided]`

For a marked $f$, a completed entry in $\mathit{memo}$ is keyed by the identity of its obtained argument. A hit charges 1: if $e\Downarrow^{k\to k_1}v$, $\mu_1(f,\mathrm{node}(v))=w$ in the table after argument evaluation and $k_1\ge1$, then $f(e)\Downarrow^{k\to k_1-1}w$ (P-Hit). $\mathit{memo}$ has run lifetime, so both builds spend fuel alike. The deferred kept-point design would restore its saved entries (§18.2). The exact cache and fee rules still need review. `[proposed]` The planned widening is to direct ordered multiargument keys, with reuse cost growing with arity, when a sketch or program shows a need. Zero-argument memo waits for a later complete profile. `[decided]` Owed: specify and review key identity, all arities, fees, entry installation, and behavior for interrupted, warmed, resumed and restored caches. `[open]`

In the paired profile, a completed eligible hit costs $(1,0)$ after argument evaluation and returns its previously obtained result. A miss enters the body normally. The cache is empty at a fresh start and installation is tied once to successful completion of the marked call. A cut in the body creates no completed entry. A pending key cannot suppress recursion. Keep the key and result rooted for the stated lifetime. For a unary miss, reserve bounded metadata capacity at paid call entry. Keep the tentative key private. Install the completed key and result only on successful return, once, as bounded administrative work covered by the named call row. A cut while the body is active retains its earlier charges and releases the unfilled entry. A construction named by the reference row pays its exact logical size before publication. The memo's keys, root slots, index and any private detached copy belong to the memo bound in §15.13, whatever representation a build chooses. The private layout changes neither invoice. A process-wide warm hash table may change actual storage but cannot change the reference hit/miss history, prices or stops. `[proposed]`

**§15.8 Hash, `slice`, `length`.** `hash` is SHA3-256 under the profile `sha3-256-fips202-2015-bytes-v1`, returns 32 bytes and is the same in both builds. (byte profile awaits review and adoption) `[proposed]` The proposed qualification includes a speed comparison against BLAKE3 and SHA-512/256 on a stated Loom workload. Specify the exact inputs, result form, charges, controls and thresholds that would prompt reconsideration. `[proposed]` Open: adoption of the byte profile and the thresholds for reconsidering it. Independent review of the profile, qualification of the implementation and the measured comparison are still owed. No speed result has been established. `[open]` Byte positions start at zero, and reading one byte gives its number in the range 0 to 255. For `B[61 62 63]` in hexadecimal, `get(B[61 62 63],1)` gives 98. `[decided]` `slice` takes a start and a length: `slice(B[61 62 63],1,2)`, start 1 and length 2, gives `B[62 63]`. `[decided]` Open: the rest of its out-of-range contract (§16.6's edge result stands), its paid arguments, its complete meter entry and its final spelling. `[open]` `length` extends to bytes: for a completed evaluation `length(B[61 62 63])` is 3; `length` on tuples and sequences is unchanged. `[decided]` Open: its byte-length entry and charge. `[open]`

**§15.9 Fuel and the run record.** Fuel is the step bound of §4.1. Every run record holds the program, the input, the output, the fuel and the build; a run that uses sequences records more (§17.3). Interning, and how a program sees identity, are in §15.2. `[decided]` Run records also bind the complete hash, canonical-byte and meter descriptor, separately from the executing build; no complete wire form of a record is supplied. `[proposed]` The value encoding and hash reserve room for a later sequence kind. The run record reserves room for its starting state, makes and writes. Adding them changes no existing bytes. Content equality of values is kept behind one function. `[decided]`

Record the program and entry, admitted input and starting state, the executing build, and the complete canonical, hash and meter descriptors. The paired record gives initial, committed and remaining $W,C$ and the result or stop. Name a reached event by definition, occurrence and visit, phase, and the effective boundary and limiting scope. Retain the committed request and trail prefix, state and held use-once account. Repeated source occurrences and repeated visits can have different first unpaid events. The record can refer to already bound evidence by identity. It does not require a permanent log of every debit. `[proposed]`

At the first unpaid event, report requested work and construction, balances before the attempt, and the deficit in each known component, $\max(0,w-W)$ or $\max(0,c-C)$. `[proposed]` If both fall short, work is the primary reason and the construction shortfall is retained. `[decided]` If only construction falls short, report construction. No event prefix is paid on just one axis. Earlier committed events stand. A capped price calculation may prove that a component exceeds its remaining grant without forming the enormous number. Record the certified inequality, the row and its operands. When a size pass is not reached, record that phase, the mandatory cheap check used, its result and the exact symbolic construction deficit from the row and operand identities. Record any certified lower bound on the shortfall. A check that establishes only a lower bound leaves the full demand unknown until the prescribed size pass. `[proposed]` For the three natural arithmetic rows of this paired descriptor, use the width check in §15.12 whenever the work invoice is refused. Let $S$ be the widths permitted by that check and let $C$ be the effective construction balance at the reached event. Record the image $D=\{\max(0,s-C)\mid s\in S\}$ in compact form. A singleton gives the exact deficit. Mark construction sufficient when $\max D=0$, short when $\min D>0$, and undetermined otherwise. Whenever the size pass is unreached on that work refusal, retain the expression $\max(0,\mathrm{bits}(f(x,y))-C)$, where $f$ is the row's operation and $x,y$ are the obtained operands. Bind it to the descriptor, row, reached event and ordered immutable operand identities recoverable from the event evidence. `[proposed]` When the sign is undetermined, that binding and the explicit undetermined status fulfill retention of the construction component (owner decision `_relay\inputs\owner-record-2026-11-25-design-r6-shortfall.json`). `[decided]` A later replay may establish the number. The refusal performs no operand scan and commits neither debit. Report work as primary, with its exact deficit or the descriptor's certified evidence of excess. The boundary determines which record fields a caller can observe. `[proposed]` For a tuple or case the header gives the exact demand, including on a work cut. The descriptor fixes the checks and their order so two builds report the same evidence. No invented zero, deficit or host-dependent arithmetic maximum belongs in this record. §15.12 fixes this order. If the reference profile itself cannot establish a required safe bound, report a work cut with reason “preflight bound unavailable”, before construction and without a numeric invoice for the unavailable part. The descriptor must give a total, reproducible predicate for this reason and its evidence on admitted operands. It cannot depend on the build's integer widths or on a discretionary timeout. A machine word overflow on a price the profile can establish is a build fault. A missing row rejects the profile for that operation before execution. `[proposed]`

A controlled physical memory or stack guard has a separate stop kind (§8.8, §8.12). It cannot be reported as either allowance cut. A host-stop record identifies the guarded resource, actual event and phase, the last committed pair, any private reservation, the prefix and holdings. A post-commit interruption preserves the paid event. Missing evidence or uncontrolled termination cannot be turned into a clean resource stop. The optional starting sequence state, makes and writes still use the reserved record space of §17.3. The precise wire bytes and authentication of the record remain open. `[proposed]`

Use a distinct, named descriptor for paired records and qualify replay by that descriptor. Existing scalar records keep their original meaning. `[proposed]`

**§15.10 Walking a term.** The counted loop is the default. No primitive gives the size of everything a case or a tuple holds below its top, so a total definition walks a term only when handed a bound, or the term as a tuple of its nodes in order, since a tuple has a length. Otherwise the kernel's graph walks are checkers run with fuel. `[decided]` Open: the alternative, a definition that may call itself on what one case or tuple argument holds, or on a smaller natural; test in §14.10. `[open]`

**§15.11 Logical construction.** Count one construction cell per binary digit of a number, per byte, per header and per slot. `[decided]` In the proposed layout a byte is a payload octet, a header belongs to a node, and an outgoing slot holds a reference. The first digit includes the natural's tag. A case header refers to the admitted declaration and alternative as one identified tag. References and tags stand for already accounted identities. A descriptor materialized by a reference row pays its prescribed logical size. Any variable-width identity or copy kept only by a build belongs to its independently bounded storage, including all the digits it keeps. An inline payload cannot be hidden in a slot. This defines the abstract graph. The number of bytes a host uses for a tag, digit or address is a separate matter. The shallow size $S$ is as follows. `[proposed]`

| Constructed value | Logical cells paid on this occurrence |
|---|---:|
| Natural $n$ | $\mathrm{bits}(n)$ with $\mathrm{bits}(0)=1$ |
| Byte string of length $j$ | $1+j$, including the header for empty bytes |
| Tuple of $j$ obtained fields | $1+j$, including one slot at every position |
| Case of an admitted choice | $2$, the case header naming its choice and alternative, and one payload slot |
| Set, if admitted in a later profile | $1+j$ for a constructed set of $j$ distinct obtained members. Selecting the unchanged input set under §16.5 builds nothing. |
| Sequence, if admitted in a later profile | An identity header, a reference to its already admitted run scope, the digits of its fresh ordinal, and a store header plus one slot per position on make. The total is $3+\mathrm{bits}(\nu)+j$ for a fresh $j$-position sequence. Charge any additional constructed values individually. |

`[proposed]` The row determines whether it constructs or selects an existing value. `[proposed]` A construction pays on every occurrence, even if its content is already interned, happens to equal an operand, or dies at once. `[decided]` A variable, admitted literal, returned reference, memo hit, selected tuple field or already admitted constant such as the bare wrong-kind answer selects a value at $c=0$. Computing an arithmetic result constructs a natural even if zero is in the pool. The tuple in an expression pays for every slot, including two references to the same child. Its children paid at their own construction events. A copy of a byte slice pays for its whole logical payload even when a host can use a view. A primitive with several new nodes lists each one, e.g. two newly produced naturals and the result tuple for ordinary divmod. On the specified zero-divisor branch which forms a tuple from the admitted zero and the obtained dividend, only the tuple is new. No traversal of the unfolding of an already held DAG is needed to price a parent. `[proposed]`

The starting pool is identified before execution. It includes admitted input, program literals, built-ins, declaration descriptors and any named initial store. A later external input cannot enlarge that pool for free. For a supported committed import, count the incoming logical graph once per distinct node of the explicitly supplied DAG and every stored slot, even if a host cache already has the same content. A reference to an identified node of this run is a transfer of a handle. A detached value required by the import row is a construction. A private decoding or staging copy belongs to the build's bounded workspace. Each supported import row states the representation, admission, bounds and ownership ordering. Validate the size and shape of the incoming graph within a named, bounded admission scope before materializing it inside the run. Bytes held by a host pending admission belong to the host. The currently open reply and resumption protocol in §8.9 still needs its own row before it can use this rule. `[proposed]`

A sequence position overwrite changes an existing slot. Any new payload constructed beforehand pays at its own event. The write's history record must fit §15.13 before publication. The snapshot returned by contents is a logical tuple copy, including every position. Scope and fresh-name identity still follow §§17.2–17.4. A control counter that stays private belongs to the frame account. A turn that presents its new natural index to the body counts that natural once for that turn. Sets, sequences, general memo and host interaction keep their existing build scope. `[proposed]`

**§15.12 Pricing and committing one event.** First obtain the operands and the applicable row from the reference state, including any completed semantic memo entry. Obtain digit counts, byte lengths and arities from validated size metadata prepared at admission or at the paid construction of the operand. Accumulate the argument contribution of a variable-arity row as each paid operand is obtained, using bounded frame fields. The completed tuple quote then reads the arity and that sum. Account for this bookkeeping in admission, the event tariff and §15.13. Compute the work invoice with exact or capped arithmetic on those admitted sizes. A capped calculation compares with the offered grant and retains a witness of excess. `[proposed]` Check work first, then measure the exact size of the result, then commit everything together. If both limits fall short, report work as the primary reason and retain the construction shortfall in the record. `[decided]` Where the header supplies the exact size, the row can read it directly. Where an affordable work invoice covers a size pass, use the exact size to decide construction affordability. A row may first compare a cheap lower bound. On a work refusal, record which construction checks ran and what they establish. `[proposed]` Both builds use the same prescribed stages and stopping rule. Each accepted event is paid and at most one terminal price attempt can follow the committed prefix of one uninterrupted evaluation. Once a cut ends that evaluation its caller cannot resume the unpaid event repeatedly against the same grant. A new run starts a new account. `[proposed]`

Preflight may privately hold an affordable work invoice while it computes the exact construction shape. Its bounded counting pass uses the obtained operands and bounded scratch, creates no result node and publishes nothing. Its work is covered by the held work invoice. Even a terminal width pass is reached only with that much work still available. The record distinguishes a pass reached under a hold from an operation committed. Administrative inspection of admitted size metadata and finite, capped price arithmetic take real machine work even at zero grant. The grant bounds the specified reference events, with those auxiliary costs bounded separately. The elementary check of the invoice itself has a separate, proved, terminating space and effort bound on the admitted metadata and grant widths, including the very first refusal. It may inspect a fixed number of sized descriptors or the aggregate already maintained by the paid operand events. A quote that requires an unbounded traversal or a value-dependent calculation must move that work to a charged stage. A row cannot run the primitive for free to learn its price. For a nonzero left shift the required digit count is the input width plus the shift amount. Compare the amount with the residual capacity by checked arithmetic before forming a shifted integer. For arithmetic whose normalized width depends on a carry, borrow, or leading product column, a read-only width pass is permitted and its cost is part of the tariff. An unqualified counting routine supplies no conforming row. `[proposed]`

An established allowance cut is reported before requesting physical backing for the refused event. If the host interrupts during the bounded price calculation, record the physical cause and the last stage actually reached. After both prices are known and affordable, hold the full pair and all required private workspace, record capacity and ownership metadata before starting the operation. Held credit is unavailable to any other operation. Stage the result, state change, memo or trail change privately. `[proposed]` A successful event commits the exact pair, value or mutation and mandatory record together. `[decided]` Its construction debit includes even a reference intermediate that was consumed inside the event. In an interrupted event, partially materialized private buffers remain covered by the outstanding reservation until discarded. An effect that cannot be recalled is issued only once its record and ownership transition can be published at that same boundary. An inability to fund either axis releases any provisional hold and commits neither debit. A controlled host stop before commit records the outstanding reservation and the prior committed pair. It discards unpublished staging, including tentative interner entries, and releases the private reservation. It records the phase reached even when price calculation ends before both reservations exist. After commit a later host stop retains the paired debit and visible prefix. A crash with an ambiguous external action is an incomplete execution record. This rule requires a qualified publication mechanism at effectful boundaries. `[proposed]`

**Candidate paired prices for the partial driver's expressions.** These prices are for a new reference profile. For naturals use their digit counts. For the argument contribution of an obtained tuple or the built-in none use one. These are the partial driver's admitted argument forms. Extending the example case row to additional payload forms requires argument contributions for each one. Let $a,b$ be natural operand widths, $m=\max(a,b)$, $j$ tuple arity and $s$ the sum of all field argument contributions with repetitions. Let $p=\mathrm{bits}(2(a+b+2))$. The following abstract price includes the read-only size pass even when a build can obtain the same answer faster. `[proposed]`

| Reached event | Work invoice $w$ | Exact logical construction $c$ |
|---|---:|---:|
| Top entry, local read, literal read, ordinary call after its argument, or completed eligible memo hit | $1$ per indicated event. Body entry is not charged a second time for the same call. | $0$ |
| Form a tuple of obtained fields | $s+j+1$ | $j+1$ |
| Form a case from an obtained payload, when the row is enabled | argument contribution plus $2$ | $2$ |
| Binary arithmetic on a wrong kind | sum of argument contributions plus $1$ | $0$, returning the admitted none |
| Add | $a+b+R+T+2(m+1)$, with $R=m+1,\ T=4p$ | $\mathrm{bits}(x+y)$ |
| Truncated subtract | $a+b+R+T+2(m+1)$, with $R=a,\ T=4p$ | $\mathrm{bits}(\max(x-y,0))$ |
| Multiply | $a+b+R+T+2(ab+R)$, with $R=a+b,\ T=8p$ | $\mathrm{bits}(xy)$ |

`[proposed]` Here $R,T$ are result and temporary reservations in work. One size pass and one emission pass account for the two scans. The proposed addition/subtraction scratch layout has a column index, carry/borrow, comparison or sign state, and highest nonzero output position. For multiplication also allow two operand positions, the column sum and a cursor. Scanning binary products by column requires at most $\min(a,b)$ one-bit contributions plus the carry from the preceding column. Each field fits $p$ bits. Reuse that workspace between passes. A zero result occupies one logical digit. Quote arithmetic, including forming or capping $ab$, is separately bounded in the meter's own frame. These are reference layout and price choices open to review against a different exact layout. They are not measured implementation costs. `[proposed]`

For a work refusal on two obtained naturals, let $a$ and $b$ be their validated widths and $m=\max(a,b)$. Compute $S$ from these widths alone. For addition, $S=\{a+1\}$ when $a=b\ge2$ and $S=\{m,m+1\}$ otherwise. For truncated subtraction, in order of the cases $a<b$, $a=b$, $a=b+1$ and $a\ge b+2$, use $\{1\}$, the integer interval $[1,\max(1,a-1)]$, the integer interval $[1,a]$, and $\{a-1,a\}$. For multiplication, use $\{1,m\}$ when $\min(a,b)=1$ and $\{a+b-1,a+b\}$ otherwise. Remove duplicate endpoints. Represent an interval by its endpoints and a two-point set by its members. Apply §15.9 to the effective pre-attempt balances. When work is affordable, hold it and perform the prescribed exact-size pass even at zero construction credit. Decide construction affordability on that exact size. Qualify the width check, its temporary storage, and terminal evidence capacity under §§15.12–15.13. A tuple or case can use its exact size from the header. Reads and wrong-kind returns select admitted values at zero construction. Both builds report the same reference phase. The full schedule must similarly say what any primitive does on its edges, how it quotes exact size, prepays peak scratch, and treats shortfalls. `[proposed]`

**§15.13 The memory ceiling. Claim 1.** Fix an admitted serial run with a finite start of $I$ logical cells and grants $(W_0,C_0)$. Let $B$ bound all other storage in the same logical units, computed before the run from the admitted program, its starting sizes, the profile and both grants. The bookkeeping bound depends on the work allowance even when the run builds nothing. Then live logical storage, including a funded event in flight, is at most $I+C_0+B$. In particular, the total logical size of completed constructions is exactly the sum of their construction debits and never exceeds $C_0$. On an interning hit the debit can exceed the increase in resident cells. `[proposed]`

To use the claim, partition all storage. Values and position arrays are initial or charged. Include active and suspended frames, operands and environments, held-value roots, memo keys and results, interner metadata, the entire retained trail including old payloads, the meter and its bounded price calculation, primitive temporary storage, pending publications and the largest terminal record in $B$ unless already paid elsewhere. Reserve before an effect. Count each retained copy and any overlap during growth, serialization or table resizing. A reference to a paid payload requires only its slot. Any unbounded string, integer, reply, copied value or saved frame hidden in a slot invalidates the bound. Only the constructions a reference row names pay $C$. Storage a build uses for frames, memo, trail, interner or meter state never changes either price, whatever its form, and belongs in $B$. Starting metadata already included in $I$ is counted there once. A value merely retained by memo or trail remains live even after its last local use. The bookkeeping envelope below must have independently checked terms for the claimed profile. A process memory limit is enforced separately by the host. `[proposed]`

For example, take $B=A+(W_0+1)F+W_0 M+(W_0+1)T+iC_0+Q+W_0$. Here $A$ is fixed start and emergency control, $F$ bounds one activation including pending operands and descent through an admitted body, $M$ and $T$ bound the memo and trail metadata attributable to a single paid event, and $i$ bounds additional interner index and size-metadata cells per newly stored node, each new node costing at least one construction cell. `[proposed]`

For the partial fragment let $D=2+|P|+I+W_0+C_0$, with $|P|$ the admitted syntax and operand slots. A stored digit count, byte length or arity of at most $D$ takes at most $\mathrm{bits}(D)$ digits. The coefficient $i$ covers their number and widths on each new node. Initial metadata belongs in the starting account. $Q$ bounds transient price calculation, including on a refused first event. Each reservation component of a work invoice is at least the number of logical cells of the storage it reserves. The last $W_0$ bounds one active primitive's simultaneous raw result reservation and temporary workspace because $\beta_R+\beta_T\le w\le W_0$ whenever its work is held. This also covers any unused tail in a preallocated result buffer, when the final value is narrower. Count any further simultaneously retained copies explicitly. `[proposed]`

All coefficients are in cells including any integer digits and auxiliary records they hold. Only a funded call creates another activation. Each growable bookkeeping record has a finite per-event or separate storage bound. A semantic payload constructed by a reference row pays its ordinary construction price even when a record retains it. Reserve the final report once. Application of these bounds to saved continuations, concurrent activity, repeated host attempts or asynchronous output requires bounds on all outstanding instances and buffers. Unlimited uncharged retry records do not meet the hypotheses. `[proposed]`

So the ceiling grows with both grants: with this $B$, live logical storage is at most $I+(1+i)C_0+(F+M+T+1)W_0+A+F+T+Q$. The independently determined coefficients, including $F$, $i$ and $Q$, can grow with the digit widths of the grants. For fixed coefficients the expression is affine in the displayed grants. The construction allowance does not bound the call stack: a definition that calls itself and builds nothing holds about $W_0/2$ live activations at $C_0=0$. `[proposed]`

**§15.14 Reading the limits.** The two reference allowances give identical logical outcomes on equal admitted starts with the same grants, profile, choices and admitted replies, given sufficient host resources. The host's elapsed time, physical peak and ability to finish can differ. `[proposed]` Illustration: with input 2, the expression tuple(x,x) costs three work units before tuple formation. The tuple row then asks for $(7,3)$. From $(10,3)$ it returns with $(0,0)$. From $(9,2)$ the row sees $(6,2)$, records both deficits of one, reports work first, and leaves both balances in place. A sequence of two distinct three-cell builds needs six construction units whether the first value has been dropped, retained locally, or held only by a memo or trail entry.

The cumulative profile never refunds a committed construction. `[proposed]` Open for later consideration: refunding construction credit when a value dies. `[open]`

<a id="ch-16"></a>

## 16. Values, choices and sets

**§16.1 Six kinds of value.** The full proposed grammar has six kinds: a natural, bytes, a tuple, a case, a set or a sequence. A tuple $\langle v_1, \dots, v_n \rangle$ is several values in fixed positions; it never changes and is read by position. A case `name.j(v)` is one value marked as case $j$ of a declared choice: the coproduct, as a tuple is the product. A set is a finite collection of values without repeats. A sequence is §17.1. A case holding a tuple represents a tagged product. There is no separate tagged-value kind. `[proposed]` The project owner adopted four basic kinds now: an exact natural number, bytes, a tuple and a case. The set waits for the first sketch. The sequence stays out of the first build, with its design on paper (§17.1, §19.2). This adopts the kinds only; each rule text still needs its review. `[decided]` Before adopting sets, bring the first slice 1 definition needing one to the project owner, or ask whether to wait if none does. `[proposed]`

**§16.2 Choices.** A program declares its choices, `name has k cases`, the count from zero up; a choice's identity is its name and its count together. Every program has three it did not write:

```
order  has 3 cases   -- less 0, equal 1, greater 2
truth  has 2 cases   -- no 0, yes 1
option has 2 cases   -- none 0, some 1
```

`[proposed]` A program's own declarations differ in name from each other and from these three, so `name.j(e)` means one choice: one name, one choice in a program. `[decided]` A case holds exactly one value; a case with nothing to hold holds the empty tuple $\langle\rangle$. A declaration does not limit what a case holds, since the evaluator has no sorts. Refused before the run: a constructor, a `case` or a branch that names a choice not declared; a case number not below its count; two branches for one number. Every case in a literal, the input or the starting state is checked against its own name, count and number, to every depth. The byte form of a name, a count and a number is not fixed here. `[proposed]`

**§16.3 Case analysis.** One `case` names one choice $a$; let $J$ be the case numbers that have a branch `a.j(x_j) => e_j`, and $w$ the subject's value. The judgment is that of §15.3.

$$\frac{\eta \vdash e \Downarrow^{k \to k_1} w \quad \eta' \vdash e' \Downarrow^{k_1 \to k'} r}{\eta \vdash \mathtt{case}\ e\ \mathtt{of} \dots \Downarrow^{k \to k'} r}\ \textsf{(Q-Case)} \qquad (\eta', e') = \begin{cases} (\eta[x_j := v],\ e_j) & w = a.j(v),\ j \in J \\ (\eta,\ e_{\mathtt{else}}) & w = a.j(v),\ j \notin J \end{cases}$$

$$\frac{\eta \vdash e \Downarrow^{k \to k'} w \quad w \text{ is not a case of } a}{\eta \vdash \mathtt{case}\ e\ \mathtt{of} \dots \Downarrow^{k \to k'} \mathtt{none}}\ \textsf{(Q-CaseNone)}$$

In Q-CaseNone $w$ is a value of another kind or a case of another choice, and no branch runs. `else` may be left out when every case of $a$ has a branch. `[decided]` Whether `else` should also take subjects outside the choice returns to the project owner before either design or implementation closes. `[open]` Bring a checker or parser with mixed inputs to compare the two rules. `[proposed]` The wrong-kind results and `same` already let a program tell some kinds apart: when evaluation completes with sufficient fuel, `same(compare(x, 0), none)` gives `truth.no` for a natural `x` and `truth.yes` for any other value; unlike `add`, `compare` builds no copy of `x`, but its applicable argument and operation charges still have to be paid. `[proposed]`

Illustration: in a `case` over `truth`, the result on `option.none` is `none`. No branch runs, even with an `else` supplied for a missing `truth` alternative.

**§16.4 One order over all values.** Kinds rank natural $<$ bytes $<$ tuple $<$ case $<$ set $<$ sequence. $v < w$ holds when the kind of $v$ ranks below that of $w$, or the kinds agree and:

| Both are | $v < w$ when |
|---|---|
| naturals | $v$ is the smaller |
| bytes | $v$ is shorter; at equal length, smaller at the first byte that differs |
| tuples | $v$ is shorter; at equal length, $v_i < w_i$ at the first position that differs |
| cases | first by choice (name: shorter first, then byte by byte; then count), then by case number, then by what they hold |
| sets | $v$ has fewer members; at equal size, by the members in order |
| sequences | by name (§17.2) |

A set is held with its members in this order and without repeats, and equal sets are one node. The order is total given the orders of choices and of sequence names. A program sees it only in the order of `members`; `compare` takes naturals only. `[proposed]`

**§16.5 Sets.** Let $M(X)$ be the members of a set $X$. A set never changes.

$$\begin{aligned} M(\mathtt{empty}) &= \emptyset \\ M(\mathtt{insert}(X, v)) &= M(X) \cup \{v\}; & v \in M(X) &\Rightarrow \mathtt{insert}(X, v) \text{ is } X \text{ itself} \\ M(\mathtt{remove}(X, v)) &= M(X) \setminus \{v\}; & v \notin M(X) &\Rightarrow \mathtt{remove}(X, v) \text{ is } X \text{ itself} \\ \mathtt{member}(X, v) &= \mathtt{truth.yes} \iff v \in M(X) \\ \mathtt{size}(X) &= |M(X)| \\ \mathtt{members}(X) &= \langle v_1, \dots, v_n \rangle, & M(X) &= \{v_1,\dots,v_n\},\quad v_i<v_{i+1}\ (1\le i<n) \text{ in the order of §16.4} \end{aligned}$$

`[proposed]` A member may be any value. One that is or holds a sequence is compared and ordered by that sequence's name, never by what it holds; changing a sequence leaves every set that holds it the same set; no set operation reads a sequence. (under the project owner’s delegation and subject to the project owner’s objection) `[decided]`

**§16.6 Edges.** No primitive fails. `[decided]` In general $\mathtt{sub}(a, b) = \max(a - b, 0)$ and $\mathtt{divmod}(a, 0) = \langle 0, a \rangle$.

| Case | Result | Standing |
|---|---|---|
| `sub(2, 5)` | 0 | `[decided]` `[built: milestone B, partial]` |
| `divmod(7, 0)` | the tuple $\langle 0, 7 \rangle$ | `[decided]` |
| Reading a tuple or bytes outside its range | a bare `none` | `[decided]` |
| `slice` outside the range | `none` | `[decided]` |
| A write to a sequence outside it | `none`; nothing changes, no trail entry | `[decided]` |
| A read of a sequence at a position outside it | `none`, as for a tuple | `[proposed]` |
| A shift right by more than the length | 0 | `[decided]` |
| A shift left by a huge amount | no special default: the safe bound on the result is reserved before anything is built; if that bound cannot be worked out safely or cannot be paid, the run stops as out of fuel; otherwise the ordinary shift result | `[decided]` |
| Paired profile, same shift | The primitive row prepays the safe result and temporary bounds from work and requires the exact logical result width in construction. For nonzero $x$ shifted left by $n$ the result width is $\mathrm{bits}(x)+n$. For zero it is one. A failed check builds no shifted value. | `[proposed]` |
| `make(0, v)` | an empty sequence; `v` is still evaluated | `[decided]` |
| `contents` of an empty sequence | the empty tuple | `[decided]` |
| `for x < 0 from y = 7 do ..` | no turns; the value is 7 | `[decided]` |
| A loop bound that is not a natural | the loop does not run; its value is `none` | `[decided]` |
| A primitive given a value of the wrong kind | `none` | `[decided]` The driver implements this case for `add`, `sub` and `mul`. `[built: milestone B, partial]` |

`none` is the built-in `option.none` holding the empty tuple. A read returning a stored `none` cannot be told by its result from an out-of-range read, so a program that stores `none` checks the length first. `[decided]` An edge result is charged its arguments and one. `[proposed]` A loop whose bound is not a natural has still run $e_1$ and then $e_2$, once each, and what they did stands; only its turns are left out: if $e_1 \Downarrow^{k \to k_a} v_1 \notin \mathbb{N}$ and $e_2 \Downarrow^{k_a \to k'} w_0$, the loop gives `none` with fuel $k'$ (Q-ForNone). `[proposed]`

For the paired schedule an edge that selects the already admitted none pays the specified argument and work charge and has zero construction. An edge that builds a value gives that construction's exact logical size and reserves the result and any scratch under its own row. Thus the tuple returned by division by zero still pays for its header and both slots. An out-of-range write publishes no trail entry. `[proposed]`

**§16.7 Comparing two values.** Inside a run the order of §16.4 is worked out only by the searches of the set operations, and there by one procedure, which both builds are charged for however they find the answer. It visits pairs of values, beginning with the pair it is given:

1. A pair that is one node is equal, and nothing below it is visited.
2. A pair of two kinds is settled by the kinds.
3. Otherwise the pair is compared by what it has of its own: two naturals by size; two byte values by length, then byte by byte; two tuples by length; two cases by choice, then case number; two sets by size; two sequences by name.
4. Where that settles nothing, the parts are visited as pairs, left to right, up to the first pair that is not equal: a case's one value, a tuple's fields, a set's members in their order.

Frames. One frame is held for each pair the procedure is inside, from the pair's visit until it is settled. The frame of a tuple, a case or a set stays held while each of its parts is visited, the last one too; a part's frame is given up before the next part is visited. Step 3 runs in the pair's own frame: comparing two lengths, sizes, case numbers or names holds no further frame, and neither does the search around the comparison.

Bound. Let $\mathrm{ht}(v)$ be the height of $v$, counted as 1 for a value with no parts to visit and 1 more than its highest part otherwise, and $F(v, w)$ the most frames a comparison of $v$ and $w$ holds at once. Then $F(v, w) \le \min(\mathrm{ht}(v), \mathrm{ht}(w))$, so the meter's reservation for a search, $\min(\mathrm{ht}(v), \mathrm{ht}(w)) + 1$, always has at least one frame to spare. Argument: the frames held at any moment belong to a chain of pairs, each a pair of matching parts of the pair before it (step 4), because a part's frame is given up before the next part is visited; a chain of $D$ pairs goes $D - 1$ levels down in both values, so $D \le \mathrm{ht}(v)$ and $D \le \mathrm{ht}(w)$.

Illustration: compare `tuple(tuple(0))` with `tuple(tuple(1))`. At the comparison of 0 and 1 the two outer pair frames are both still held. Three frames are live and the proposed reservation is four.

A frame is a unit of the meter's account and not a measure of a build's storage: a build that holds fewer is charged the same. The charges for its visits and comparisons belong to the proposed meter schedule (under review). `[proposed]`

<a id="ch-17"></a>

## 17. Changing sequences

**§17.1 What a sequence is.** A sequence is an order of positions holding realized values. Formally a value of the kind sequence is a name $\xi$, and the state $\sigma$ maps each name to the tuple $\sigma(\xi) = \langle v_0, \dots, v_{n-1} \rangle$ of what its positions hold now. Changing what a position holds changes the sequence, for every holder, and it stays the same sequence: every holder holds the same $\xi$ and reads the one $\sigma$. A change that happened is a fact whether or not anything later reads it. `[decided]` A sequence keeps its length: $\lvert\sigma(\xi)\rvert$ is the same in every state of a run, and a different length is a distinct sequence. (under the project owner’s delegation and subject to the project owner’s objection) `[decided]` The name for a finite sequence is always “sequence”. `[decided]` What a sequence holds at one moment is a tuple. The decision was to use the first sketch to test inclusion in the first build. The two completed sketches showed no need, so the sequence stays on paper and out of that build. The reconsideration at the first slice 2 search or handler uses the actual program (§19.3). `[decided]`

**§17.2 Names.** A sequence's name shows which run made it. `[decided]` The run part comes from the run's start itself, so two runs from one start name their sequences alike; it does not distinguish two executions of that start. Every declaration in the recorded program counts toward run identity, even an unused helper. `[decided]`

Proposed construction. A name is a pair $\xi = (d, i)$ of a scope $d$ and a count $i \in \mathbb{N}$, and two sequences are the same exactly when their pairs are equal. With $H$ the named hash (the proposed profile of §15.8) and $\ell$ a fixed label,

$$d = H(\ell \,\Vert\, \mathit{program} \,\Vert\, \mathit{entry} \,\Vert\, \mathit{input} \,\Vert\, \mathit{starting\ state})$$

over the bytes of each; $\Vert$ gives the order of the parts only, and how each part is framed is open. So equal starts are the same logical run. A run holds a count $\nu$: a new run has $\nu = 0$; a replay is a new run from a recorded start; going back to a kept point stays in the same run, and a count is never reused. A sequence that comes in keeps its pair; one that already carries the scope just computed is refused. (the bytes and the hash are not fixed) `[proposed]`

For the proposed pairs, the comparison itself has a fixed order: $(d, i) < (d', i')$ when $d$ is shorter than $d'$; or they have equal length and $d$ is smaller byte by byte; or $d = d'$ and $i < i'$. This order is independent of the current run. `[decided]`

Open: the normalization, identity, hash and profile premises of the construction. `[open]` Starts, imported identities, saved states and records must retain a compatible complete canonical, hash and meter profile; changing the function or the encoding cannot silently reuse old names. `[proposed]` Open: complete framing, admission and replay. `[open]`

**§17.3 State, the record and the memo.** A run's starting state $\sigma_0$ gives $\sigma_0(\xi)$ for each sequence $\xi$ the input can reach. A literal in a program holds no sequence. A reachable sequence with no contents given is refused. The count is not part of a starting state. The record of a new run adds to the record of §15.9, which keeps naming the build:

$$\mathit{record}\mathrel{+}=(\text{choice declarations},\sigma_0,d,\nu=0,\mathit{memo}=\emptyset,\text{meter and initial pair},\text{remaining pair},\text{result or stop},\tau_{\mathsf{mw}})$$

The memo starts empty for a fresh run. The ordered trail of makes and writes $\tau_{\mathsf{mw}}$ and the last committed state show what this build did from this start. A resumed run uses its saved state, cache, profile and remaining pair. A new run may replay an old one from the original start under its exact recorded profile. This reservation of record space does not enable changing sequences in the first build. `[proposed]`

State-free test. $\mathrm{sf}(f)$ holds when neither $f$ nor any definition it can call uses `make`, `contents`, the read at a position or the write; a call that cannot be resolved fails the test. Only a definition with $\mathrm{sf}(f)$ may carry the memo mark. `[proposed]` A memo mark on any other definition is refused before the run. (the exact test stays proposed) `[decided]` Every definition that admission and the checking of results run must be state-free (§7.7); work that uses sequences goes to a checker with a record of its own. `[proposed]` The profile condition of §17.2 binds these starts, states and records as well. `[proposed]`

**§17.4 The primitives as transitions.** The primitives on a sequence are `make(n, e)`, `length`, `contents`, a read at a position, a write at a position, and `same`. A step acts on $(\sigma, \nu, \tau)$, with $\tau$ the trail (§18.1) and $\tau \cdot \mathit{entry}$ the trail with one entry added. Arguments run first, left to right, as for every primitive. The table gives each call on the values of its arguments, $\xi$ a sequence name and $n$ the length $\lvert\sigma(\xi)\rvert$; $\mathtt{read}$ and $\mathtt{write}$ stand for names not yet chosen.

| Call | When | Result | State after |
|---|---|---|---|
| $\mathtt{make}(v_1, v)$ | $v_1 \in \mathbb{N}$ | the new $\xi = (d, \nu)$ | $\sigma[\xi \mapsto \langle v, \dots, v \rangle]$ with $v_1$ positions; $\nu + 1$; $\tau \cdot \mathsf{make}(\xi)$ |
| $\mathtt{make}(v_1, v)$ | $v_1 \notin \mathbb{N}$ | `none` | unchanged: no sequence made, no count taken |
| $\mathtt{length}(\xi)$ | always | $n$ | unchanged |
| $\mathtt{contents}(\xi)$ | always | the tuple $\sigma(\xi)$ | unchanged |
| $\mathtt{read}(\xi, i)$ | $i \in \mathbb{N},\ i<n$ | $\sigma(\xi)_i$ | unchanged |
| $\mathtt{read}(\xi, i)$ | otherwise | `none` | unchanged |
| $\mathtt{write}(\xi, i, v)$ | $i \in \mathbb{N},\ i<n$ | `truth.yes` | $\sigma[\xi \mapsto \sigma(\xi)[i := v]]$; $\tau \cdot \mathsf{write}(\xi, i)$ |
| $\mathtt{write}(\xi, i, v)$ | otherwise | `none` | unchanged; no trail entry |
| $\mathtt{same}(v, w)$ | always | `truth.yes` exactly when $\mathrm{node}(v) = \mathrm{node}(w)$ | unchanged |

Standing of the rows. `make(n, e)` evaluates `e` once, after `n`, and gives a new sequence whose `n` positions all hold that value; if `n` is not a natural it gives `none`, makes no sequence and takes no count (§17.2). `[proposed]` Positions count from 0. `[decided]` A program reads a sequence in two ways, the copy `contents(s)` or the read of one position, for a build that has the changing sequence; there is no whole-sequence write. `[decided]` The read has a name of its own that is not the name of reading a tuple; outside the sequence it gives `none`, so a program that stores `none` in a sequence checks the length first, as for a tuple (§16.6). Either way a position that holds a sequence gives that sequence, not what it holds. The read changes nothing. `[proposed]` An out-of-range write returns `none`, without changing state or appending a trail entry. `[decided]` A completed in-range write would return `truth.yes` whatever value it wrote. `length` of a sequence changes nothing. `[proposed]` A write changes $\sigma$ for every holder and gives no new sequence. `[decided]`

Illustration: if two holders share a sequence containing 4 at position 0, `contents` gives a tuple holding 4. Writing 7 at position 0 through either holder changes a later read through the other to 7. The earlier tuple still holds 4. In a sequence of length one, an attempted write to position 1 returns `none` and appends no entry, whereas writing `none` to position 0 succeeds and returns `truth.yes`.

**§17.5 Charges.** A write is charged by the size of its position, as every primitive is charged by the size of its arguments, and a sequence has no last place. `[decided]` Mechanics, in the four parts of a meter entry (arguments $\alpha$; what is built and what is held meanwhile, the two under the bound $\beta$; work $\gamma$, as in §15.6):

$$\gamma_{\mathtt{read}} = 1, \qquad \gamma_{\mathtt{write}} = 1 \text{ for a write that is made, whatever } i, \qquad \text{the size of } i \text{ is paid in } \alpha$$

The write's whole charge has the other parts too. `contents` is charged by the length $\lvert\sigma(\xi)\rvert$ of the tuple it gives. Nothing about a sequence but its name, its length and what its positions hold is part of the state, the record or a kept point. (the numbers are the meter's and are under review) `[proposed]` `contents` of an empty sequence gives the empty tuple. `[decided]`

The meter schedule specifies the four parts of a primitive charge, its four charging stages, the charged comparison and search events (§16.7), and rules for an edge result and a loop bound that is not a natural. The write and `contents` entries above are owed. They use no last-place state, initial position or charge. `[proposed]`

For the paired row keep argument price, result reservation, temporary reservation and scheduled work visible in the work invoice. Give its exact construction price separately. State which logical values the operation creates, including copies, its price-check and scratch bounds, its edge result, and which state and trail changes must commit with it. §16.7's abstract comparison-frame reservation remains separate from a build's actual stack. Set search, a made write, an unchanged or out-of-range edge, and a whole contents copy have distinct rows. `[proposed]`

**§17.6 The read at a position, and names.** The read at a position is part of the design, for a build that has the changing sequence. Adding it changes no result and no charge of a program that does not use it. `[decided]` Before the builds are frozen, check the positional-read decision against the log of occasions that called for a read in place, a checker that reads few positions, a consumer that wants a whole copy, and a stale-copy case. `[proposed]` The write to a sequence should have another word than `set`. `[proposed]` The project owner conditions distinct tuple and sequence read names on the designer and evaluator specifier agreeing. The first agrees and the second has yet to do so. The proposed state-free test (§17.3) distinguishes the reads by name. `[proposed]`

<a id="ch-18"></a>

## 18. The trail a run leaves

**§18.1 The trail.** The trail $\tau$ of a run is, in the order things happened, the fragments it executed:

```
fragment ::= request, answered or still open, with its reply when there is one
           | failure
           | catch
           | resumption of a suspended continuation
           | restoration made in going back
```

Executing a fragment takes $\tau$ to $\tau \cdot \mathit{fragment}$. A suspended continuation adds its fragment when it is resumed and not before. The trail of a whole is the fragments of its parts in the order the reference run executes them. The trail, or the record it is part of, also holds: the final result, or the failure and what it held; which answer met which pick; which values used only once were consumed, value for value and activation for activation; and for each reply from outside its endpoint, version, state and manifest. `[decided]` The projections from these records to §8.10, §9.6 and §20.7 remain to be defined. `[open]`

Before committing a request, reply, visible write, ownership change or other recorded action, secure the bounded capacity for its required record and jointly funded value constructions. Publish the evidence and action at one commit boundary. A cut before publication leaves both absent. A cut after it retains both. The trail can keep a payload live after all local references have gone. Logs, buffered bytes, old and new values, and held accounts must be included in the ceiling of §15.13 wherever the supported run retains them. `[proposed]`

**§18.2 Kept points.** The project owner deferred kept points and going back (§18.3). Reopen them when a measured search or a handler actually has to undo writes to sequences. (later) `[decided]`

In the deferred account, a kept point $K$ is the rest of the run from there, as a value. Restored at $K$: bindings, frames, loop state, handlers, activation and use-once information, the memo's entries, the result so far, and the contents $\sigma_K(\xi)$ of every sequence $\xi$ reachable at the point, where $\sigma_K$ is the sequence state there. Never restored: the count that names new sequences.

Agreement. After going back has finished and been paid for, compare the continuation with a fresh run given the same answers, under a correspondence of names that fixes every sequence made before the point and keeps the order of those made after. First, if every charged input agrees and the fuel left is equal, the two agree in their result or their stop, in what the sequences hold, and in the requests, replies and changes compared. Second, where corresponding names change a charge, two continuations that both finish agree in result, state and observations; their fuel use, and the point at which either runs out, may differ. So equal finite budgets do not by themselves guarantee the same result or stop, the same final state, or the same complete trail. A kept point that holds a value that may not be copied is run once or handed on once (§3.12). `[proposed]`

**§18.3 Going back.** The project owner deferred going back to the same reopening trigger as kept points (§18.2). (later) `[decided]` In the deferred proposal, going back to $K$ goes over the sequences reachable at the point, sequence by sequence in the order of names; a sequence made after the point is left out, since nothing restored holds it. Within a sequence $\xi$ it takes each position $i$ written since the point, from the first position up, and gives it back its value at the point by a write charged as a write; a position that already holds that value is left alone. With $k$ the run's remaining fuel and $q$ the charge of a write at $(\xi, i)$:

$$\frac{\sigma(\xi)_i \ne \sigma_K(\xi)_i \qquad q \le k}{(\sigma, \tau, k) \to (\sigma[\xi \mapsto \sigma(\xi)[i := \sigma_K(\xi)_i]],\ \tau \cdot \mathsf{restoration}(\xi, i),\ k - q)}\ \textsf{(S-Restore)}$$

S-Restore applies only at the least pair $(\xi, i)$ in that order (sequences in the order of names, positions from the first up) with $\xi$ reachable at $K$, position $i$ written since $K$, and $\sigma(\xi)_i \ne \sigma_K(\xi)_i$; so a run that can pay for one write only restores the first such position. `[proposed]` Each step is charged before it is made, from the run's own remaining fuel, and no fuel is returned. If the next step cannot pay its price (either component in the paired profile) the run stops as out of fuel; the steps already made stay made, and the trail holds them. This simple rule needs control of what is restored: it applies only where nothing else can change those positions between the kept point and the end of going back. Otherwise a protocol specified apart must account for the accesses in between and keep what they must observe; §3.10 to §3.13 and §9.8, on ownership and shared state, do not by themselves give that protocol, and none is proposed here. `[proposed]` In the deferred account, the catching handler chooses whether a failed part's writes are kept or undone, and what the host was told stays recorded. `[proposed]`

If restoration is reopened, a saved point cannot increase the run's current work or construction remainder. In S-Restore the price and balance are pairs for the paired profile. A completed write and its trail entry stand if the subsequent write cannot pay both components. The illustration below then assumes an affordable first pair and an unaffordable second pair. The conditions on access, order and the reopening trigger are unchanged. `[proposed]`

Illustration: after $4\to7\to4$ at one position, that position needs no restoration write. If two other positions need writes in order at charges $q_1,q_2>0$ and the remaining fuel is exactly $q_1$, restoration performs the first, records it, then stops before the second.

**§18.4 Entries for writes.** An entry for a write names the sequence by its name and the position, and may hold one of four amounts:

```
entry ::= changed(name, i)                 -- that position i changed
        | changed(name, i, to x)           -- that it changed to x
        | changed(name, i, from y)         -- that it changed from y
        | changed(name, i, from y, to x)   -- from y to x
```

`[decided]` For a stretch of the trail and one position, "from" of the first write and "to" of the last summarize the change between the two ends, for a consumer that looks only at the ends: the writes $w_1 \to v_1, \dots, w_n \to v_n$ to one position, in order, are summarized as $w_1 \to v_n$. If the first entry omits its old value, or the last omits its new value, the missing endpoint cannot be supplied from an intermediate write. What happened between stays in the ordered trail. Between two kept points at most one "from" is needed for each position of a sequence. (as part of the run record) `[decided]` Illustration: a position written from 4 to 7 and then from 7 to 4 is summarized as from 4 to 4, so a consumer of the ends sees no change, while the trail still holds two writes. For the first build the entries for writes are out with changing sequences and have nothing to record until sequences come in; the rest of the trail stays. `[decided]`

# Part V. The plan, the explorer and the optimizer

<a id="ch-19"></a>

## 19. The first five slices

**§19.1 Common frame.**
Five slices, each from source text to machine code, each ending with three checks: the compiled program and the reference run agree on generated inputs; the artefact's manifest $\mathcal{M}$ is printed; the two builds of the evaluator agree. In slices 1 to 3 every claim is settled by a run. `[decided]` Nothing inside slices 1 to 3 is decided for the sake of the Structural Representation Explorer (SRE) without coming to the project owner as its own choice. `[decided]`

Sort binders appear only in signatures. In slices 1 to 3 a claim about a family is checked at each use after substitution. A claim over the sort parameter waits until slice 4 can express it in the chosen logic and check a derivation; checks for individual sorts do not establish it for every sort. `[proposed]`

### Slice 1: the evaluator and the store

**§19.2 Contents and finish check.**
Contents: the evaluator of §15.1, twice; the records of §2.1 (terms, theories and rules with content identity); four kernel programs (the manifest computer; the use-once check, which may be the narrower rule of §1.30; the reference run with the record of its state; the first part of the obligation generator, emitting a membership claim for each application); a plain path to machine code through a checked low-level form, wholly ahead of time in this slice, with the uniform boxed representation and counted references. `[decided]` The plain-path requirement is backend-neutral. `[decided]` Also: a small machine theory for its target, with its decoder, enough for the plain path; data declarations; the host's operations reached through Ask under one fixed bound. `[proposed]`

Done when (1) both builds agree on generated runs, (2) the compiled programs agree with the reference run, (3) the use-once check agrees with the reference run's count of what each generated term consumes (§19.6), and (4) the root manifest gives the backend, the lowering and the reader of text by name, because nothing has evidence yet. Slice 1 needs no foundation, no derivation, no representation but the default, and no planner. `[decided]`

The use-once check and the reference run were sketched in the evaluator's language. Both sketches are done and reviewed; neither showed a need for changing sequences. The project owner required both sketches and their cost account to be finished before the evaluator's core (frames and calls, in milestone B) is written; build set-up and arithmetic may start beside them. `[decided]`

Proposed for full slice 1, after milestone B: at the reference/compiled comparison and replay, check that the record keeps the reference run's observations, request and ownership evidence, and the named lowering and backend; keep visible choices distinct from execution plans in the replay record, the reference meter separate from physical cost, and the plain path runnable for every program. `[proposed]`

For a proposed paired build, compare the same versioned input, work and construction pair, meter descriptor and abstract cache start across the two evaluators. Compare both final balances and the original occurrence of the first unpaid event, its reason, state and published prefix. At an export compare only the observations its contract promises, including later use of a shared remainder. Keep verified physical stops in the resource-stop comparison. Replaying a scalar milestone B receipt uses its recorded scalar schedule. The paired examples and paper trial provide separate expected records for checks still owed. `[proposed]`

**§19.3 Restrictions and choices of the first build.**
The first build excludes changing sequences (§§17.1–17.4), the evaluator’s sequence rules, the run record’s starting-state part, sequence compilation on the C route and trail entries for writes (§18.4). The rest of the trail stays. At the design of slice 2’s first search or handler, use its real program to ask whether this build needs sequences and what waiting costs in rework. `[decided]`

Backend: generated C is the route to qualify for the first compiled demo (for now). `[decided]` Loom writes its own big-number code for every program and ships no big-number library; in development that code is checked against an independent implementation behind one narrow interface. A pinned Clang may be installed only if no suitable C compiler is present. `[decided]` Open: the C compiler and its version. `[open]`

The fixed bound has the permissions of §1.46: one output operation, possible non-termination, no pick, permitted memory stops and separately named stack stops under §8.10 and §8.12, the separate fixed allowance for the literal checks of §7.5, and the unmatched-call failure of §1.51. The one output sends bytes and receives an empty `done` reply per invocation. A bad reply is refused and may be retried, an unanswered request waits, and uncaught failure is reported (§8.9, §8.10, §3.16). `[decided]` Open: the guard-failure question of §1.51; qualifying the C route's guard for a clean stack stop (§10.11); the exact output symbol and signature; the separate depth policy; the complete scope of the bound; the numeric allowance and charging protocol; the remaining host and use-once interfaces. `[open]`

**§19.4 Boundaries and open scope.**
Slice 1 has no program handler. The host answers the output operation (§8.9); program handlers arrive in slice 2 (§19.8). `[proposed]` Slice 1 uses provisional working notation, separately proposed, reviewed and put to the project owner before anything is built on it. Every spelling remains the owner’s to change. This leaves the real written form open. `[decided]` The notation designer chose to refuse quotation in slice 1. `[decided]` Omitting the check cache from slice 1 is proposed. `[proposed]` Its first slice remains open (§5.2). `[open]` Each build records the elaborator’s questions and answers (§13.2). The manifest computer returns the manifest and the uses (§5.4); the uses count with the trusted text (§13.2). `[decided]` Moving the uses result to slice 3 requires a separate scope decision. `[open]` For now the first build excludes functions held in data (§19.5). `[decided]`

**§19.5 Data declarations.**
A theory may declare a sort *data* with its constructors, *finite* with its values, and *use-once* (§1.7). Value parameters may name the sort being declared; sorts may be indexed by terms (§1.3). The proposed declaration account allows a constructor parameter of a use-once sort only where its data sort is declared use-once. `[proposed]` A refusal under that rule names the field (§1.7). `[decided]`

For now the first build refuses a constructor with a bound parameter as unsupported. `[decided]` The alternative would admit it in that build under the working core (§9.2), subject to the census and its review. Under either choice, complete and review the whole-language census (§9.3) before fixing the use-once rules, stored function signature or values a call may accept. The frozen-grammar census extends through size eight, with a blind recount through seven. The whole-language census remains due. `[decided]` Return admission to the project owner once the result note has its review and before those interfaces are fixed. Include when a function held in data counts as consumed. `[proposed]`

For a sort $A$ declared both data and finite: each value given is a constructor term of $A$, admitted as such, and one that is not refuses the declaration; $A$'s values are those given and no other. A constructor's result sort is its data sort at index terms over its own indices and parameters; its application is admitted as in §7.2 with those indices put in. A pattern naming the constructor brings its indices into the rule's context as variables; that the matched argument's sort is the constructor's result sort is a membership claim like any other (§7.6): $\mathsf{yes}$ where the two are one node, otherwise $\mathsf{unknown}$. A consistency account is needed too: every value a constructor $c$ can produce at admitted arguments and indices $\vec u$ belongs to the declared finite collection, $c(\vec u) \in \mathrm{Fin}(A)$. Checking only the given values is insufficient: $\mathrm{Fin}(A) = \{\mathtt{nil}\}$ with constructors `nil` and `cons` is inconsistent when `cons(nil)` is admitted and is a distinct value. The declaration check must detect such contradictions, and constructor admission must not silently get round the finite constraint. `[proposed]` Open: the exact consistency procedure, its evidence, fuel and $\mathsf{unknown}$ outcomes. `[open]` This is neither a completed check nor a new blanket exclusion; the existing attribute syntax remains, and any further restriction on otherwise valid declarations must go to the project owner. `[proposed]`

**§19.6 The use-once check's answer and its agreement with the reference run.**
For a scope in its context the check answers $\mathsf{accept}$ or $\mathsf{refuse}(w, \textit{clause}, \textit{place})$, naming the value, the clause and the place; it gives no count. A binder the narrower rule refuses is refused as a form unsupported in this slice (§10.4). `[proposed]`

Agreement, check (3) of §19.2, is one-way, because the narrower rule refuses right terms by its make (§1.30, §1.32). With $\#_r(w)$ the reference run's count of consumptions of the use-once value $w$ in run $r$ (§1.22), it holds when for every generated term the check accepts and every generated input: $\#_r(w) \le 1$ for every $w$; if $r$ returned, each value it had was consumed once or handed on; and if $r$ failed, ran out of fuel or waits, each value not consumed is named as held, nothing more being asked (§1.23). A refused term whose runs consume rightly is no disagreement. One accepted term with one run that consumes a value twice, or returns with a value neither consumed nor handed on, is a disagreement. The generated terms include negative controls, whose runs do consume wrongly and which the check must refuse: agreement on right terms shows nothing about a check that accepts everything (§13.6). Refused right terms are counted. The declared corpus also has positive controls within the narrower rule, their expected acceptance justified by that rule, which the check must accept; refusing every term fails. Both sets and outcomes are reported. `[proposed]` Open: corpus and coverage qualification. `[open]`

**§19.7 Generation protocol.**
Proposed: (1) Record the generator by hash, and any seed (§4.16). (2) Generate exhaustively up to a stated grammar size, then sample beyond it, with a size reaching each rule and exposing each seeded wrong subject; these are protocol proposals, not a uniquely derived size, and no numeric count or size is supplied. (3) Record every generated subject and its admission result, and admission refusals and causes separately from run comparisons; state generated, admitted, refused and compared members, controls included. (4) For the candidate, report each comparison as agreement, established mismatch, or incomplete under §8.10. An established mismatch fails that candidate; fuel cuts, host waits and permitted resource stops stay incomplete, with reasons; a match omitting use checking is not agreement. (5) Separately test deliberately wrong lowerings: each must establish its expected mismatch. (6) Separately test the source controls of §19.6: negative ones refused, independently justified positive ones accepted; the candidate's no-mismatch rule does not prohibit control success. Evidence covers only the named members (§4.16). `[proposed]` Open: the corpus and coverage bar, including how much incomplete work may remain; one agreement with no observed mismatch does not establish the finish check. `[open]`

Illustration: on a use-once input, `pass(x) = x` hands the value on and `forget(x) = unit` loses it. These source controls require different answers. A deliberately wrong lowering that changes the first output byte has an established mismatch at that byte, even if a later request is still waiting.

### Slices 2 to 5 and after

**§19.8 Slice 2: claims and interpretations.**
Contents: the case split; the reader of evidence at a site; the obligation generator for laws at an interpretation; the use-once check in full, clauses (a) to (d); a status for each law at each interpretation; a search for counterexamples; scope and covering; assumptions and reading at the site; data and folds; effects with handlers; bounds on manifests; selection; the semantic part of the lock; a first proposer of one rewrite, splitting a fold, each step licensed by a law read at its site. Done when a fold over the integers is split, the same fold over floating point is left alone, and the refusal names the law that failed and states what would lift it: in this slice, the $\mathsf{unknown}$ laws on the refused licence. The full query arrives in slice 5. `[decided]` Illustration: with $x = 2^{53}$, $y = 1$, $z = -2^{53}$ both groupings of the integer sum give 1; in binary64 with rounding to nearest, ties to even, $(x + y) + z = 0$ and $x + (y + z) = 1$.

The fixed first-call build with its finish line belongs to slice 2. `[decided]` Its five proposed checks are in §12.4. `[proposed]`

Proposed for slice 2's design: for law and interpretation checks, review how a definition carries its effects, whether it surely ends, what it consumes and what it leaves open. Keep the chosen interpretation and law evidence available at the rewrite site. At the existing design return, consider sites that a claim can name across rebuilds, identity being open in §2.5. Keep a program form late enough that operations retain their theory names for a law read at the site. Check how a program can ask for any best answer or an answer within a stated width. The integer-fold split and floating-point refusal are the existing case. `[proposed]`

Proposed at the first law refusal: compare a mandatory condition with an optional representation; for one candidate satisfying A alone and one satisfying B alone, say why the pair supplies no candidate satisfying both conditions, using the existing refusal explanation. `[proposed]`

**§19.9 Slice 3: representations in the forward form.**
Contents: the first machine theory that holdings are made into, for words and memory, with the first holding; the obligation generator for the clauses of the tracking claim; relation, signature, trackers and clauses F1 to F3; total holdings into sums, such as a machine word or a big integer; guards settled at evaluation; ranges as a lax representation with resolution; the artefact manifest as a polynomial; the operational part of the lock; the harness for the three measurements. Done when a sum over words runs with one guard per element, and with none where ranges are known, and when a representation exact only for what one client reaches is accepted for that client and refused for another. `[decided]` The guards this slice brings are those a representation's tracking claim leaves to be settled at evaluation (§6.1, stage 4); a guard on a membership stands in slice 1 already (§7.6, §10.1). `[proposed]`

Proposed before the representation sheet is fixed: review how it retains the client's observations, guards and the plain-path workload comparison for its regular representation checks. `[proposed]`

At the first client comparison with forward tracking, compare a score-only caller with one whose helper serializes the name. Identify the observation that disqualifies the holding for the second caller and account for effects of producing the field. Bring the field-liveness proposer at the first optional slice 3 layout-proposer demonstration. `[proposed]` Before the uses result is fixed as trusted text, decide its field reporting (§20.12). `[decided]` At the slice 5 interfaces check use of the accepted replacement. At the first actual residual transfer between methods check coverage and reconstruction (§20.36). `[proposed]`

**§19.10 Slice 4: evidence.**
Contents: the derivation checker, which enters the trusted base here; derivation objects; solver certificates with checkers; the three routes recorded; the backward form with B0 to B3 on a late choice. Done when one guard is removed by a theorem, one run record is replayed by both builds, and the cost of replay is measured. `[decided]` The certificate checkers owe the five things of §13.6. `[decided]` The foundation tests come first, and the logic derivations are then built in is the position that survives. `[proposed]` Proposed: use the existing checked-derivation design return to review what the ordinary compiler needs to carry as evidence. `[proposed]`

**§19.11 Slice 5: the planner and a second target.**
Contents: the polynomial read in costs; the four proposer queries in full; a second machine theory; code as a name for its term; a first library of representations that are not layouts, such as graphs under two spectral names. Done when (i) no trusted program changed between slices 4 and 5, and (ii) a proof arrives and a plan changes with no edit to the source. `[decided]` And (iii) when one algorithm is substituted under a theorem of a theory at one interpretation, and refused at a second where a law of the theory is $\mathsf{no}$. `[decided]` An independently recounted finite run (§23.2 row 25) covers all 1,100 simple labelled graphs of up to five vertices: the three laws hold of forests and the algorithm is licensed, and for matchings it is licensed at the 173 graphs where the laws hold and refused at the other 927. That evidence covers those graphs. Check (iii) still requires the theorem in the language. And (iv) when the finish check of §12.5 for a plan chosen in a run is met, if that passage is taken. `[proposed]`

Check (i) does not show that what is trusted did not grow: a second machine theory is a declaration the build takes as true (§10.6, §13.2), and an unchanged hash shows the same bytes and no more (§1.62). `[proposed]`

Proposed: review the planned planner and theorem-backed substitution at their existing interface return. General search, ranking and cost-model tuning can wait for the planner and a workload that warrants them. Bring the finite research cases at the planning trigger of §19.13. `[proposed]`

Proposed matched separator case for the full optional planner: at the first slice 5 planner workload with a handwritten route, compare it with one boundary-counting schema at the same allowance. Pull separator and coverage premises from the requested question, then check the match, bijection and table charge. Try an unsupported question, a wrong separator and an expired budget. Include the cost of rejected candidates. `[proposed]`

**§19.12 Later work.**
After these come the real numbers with enclosures, parallel schedules licensed by exchange laws, hosted foundations, file formats and their migration, the compiler written in Loom, and a rehearsal of changing the foundation. `[decided]`

**§19.13 Where the SRE enters.**
The current slice order stands, finite cases can inform the interfaces, and an early SRE build is ruled out. `[decided]` Open, for the project owner: the SRE's later placement. The suggestion to place the SRE just after slice 3 rests on that slice providing runs, covering facts and forward representations for finite objects. A second suggested order places the SRE and SkeinLab after slice 5. Substitution by a law is in slice 2 and the planner in slice 5 whichever is chosen, so neither waits on this choice. `[open]` Before any SRE building starts, put an externally checkable finish line for each planned stage to the project owner. `[proposed]`

Proposed finish check for the first SRE stage, the counting demonstration: from graph-colouring counts and boundary gluing, build the census table, its rank and algebra, check a minor as §20.9 proposes, seek the addition-contraction identity, find a closure witness against storing only the count, and search for an equality gadget with a checked readout. Each result names its parameters, census and evidence; a black box needs the link of §20.7 before a claim reaches beyond the answers recorded. A census identity remains a conjecture about all graphs until proved; remembered rank and cross-domain claims await checked imports. Its scaling test runs the pipeline on ten parameters on small graphs, recording sizes, budgets and how many yield an interpretable algebra. It runs at the first SRE stage chosen, whose place is open (not run). `[proposed]`

A SkeinLab result here can be an algebra, identity, witness or checked gadget with its stated scope. The count of cases yielding an interpretable algebra measures SkeinLab's mathematical results. Recovering meanings from a fit can be a research result in its own right. `[proposed]` The separate storage-cost study, including whether fewer structure constants reduce cost, is deferred until the compiler is close to finished and the SRE-based optimizer is partly built (deferral). `[decided]`

Bring finite cases when slice 3 meets its finish check and in any case before drafting the slice 5 proposer queries, planner and crossing record. `[decided]` The proposed second client for those interfaces uses a black box, an experiment table, a census and refutations found by question. `[proposed]`

<a id="ch-20"></a>

## 20. The SRE, SkeinLab and the optimizer

### Names, notes and roles

**§20.1 Names.**
SRE is the Structural Representation Explorer, the part that builds and checks representations. It is shared infrastructure for two clients: SkeinLab, a metaprogram that is not part of the compiler, and the compiler's optional optimization paths, called the optimizer until the project owner names them. The plain path always runs without the optimizer. `[decided]`

**§20.2 Notes.**
A note is shared tool metadata recording the nodes it is about, its kind, its method and its content. Estimates and samples record estimated or measured information. Candidates and proposals offer something to be checked and are a main result of a proposer. A note may stand alone, as a candidate theory does. `[decided]`
Uses: the SRE and SkeinLab keep candidates and proposals from their searches as notes (§5.3, §5.6, §20.3); the optimizer uses scores with their methods to order proposals inside a set already fixed by exact checks (§4.18); the estimated benefit passed to the compiler or to a person is a note (§20.25); tests of the trusted base keep the damaged-certificate corpus result as a note (§13.6). §4.1 gives the rule for every note. `[proposed]`

**§20.3 Roles and trust.**
The SRE builds, checks and combines representations of objects. SkeinLab uses the SRE to find questions, laws and theories. Both are libraries and proposers over the store. Neither is trusted: whatever either establishes is a claim that a kernel program checked. Nothing in the rest of the design is specific to them, and the compiler is the first client of every construct they use. `[decided]`

### What the SRE takes and returns

**§20.4 What the SRE submits, and who decides (use by the planner).**

| The SRE submits | Who decides | Against what | What the planner may then do |
| --- | --- | --- | --- |
| A representation $\rho$: target, relation, signature, trackers | The kernel, by sort preservation | The declarations of both theories | Keep it as a proposal |
| That this name names this object | The kernel by computation, or a verified checker run compiled | The relation's definition at this object | Use the name for the questions in the signature |
| That the name answers this question (a tracking law) | The kernel, on a derivation for the sort or on an enumeration with a covering fact | The question's definition in the object's theory | Replace the question by its tracker inside the scope |
| That the name does not answer it: values with one name and no common answer | The kernel, by computing (§4.7) | The same definition | Never use that name for that question |
| A width or a distortion for this object | The kernel, or a checker in exact arithmetic | The definition of the measure | Use the answer at that width |
| An estimate | Nobody | Nothing | Nothing: it guides search only |

Each row of the table has this standing. `[decided]` SkeinLab may report an observation or use it to choose a further experiment, with its method and scope. `[proposed]`

**§20.5 Trial at the first extension that supplies evidence to an existing consumer.**
Offer a lower bound where the consumer asks for exactness, and an exact certificate for the wrong revision; use the claim and site check already in force if they tell the two apart. An obstacle of relational expressivity goes to the comparison of foundations that §1.61 to §1.63 leave open. `[proposed]`

**§20.6 What goes in.**
(i) Any object: a closed term $t$, an interpretation $\iota$ of any theory, or a black box with a set of questions. (ii) An open registry of families, each a target theory with a proposer of representations into it. (iii) A census for each theory, with a record of how it was drawn. (iv) A budget. `[decided]`

### Black boxes

**§20.7 Black box.**
A black box is a theory of declared questions with no rules, asked through an effect. Each answer is a run record whose manifest names the endpoint. From answers alone the SRE has claims about the inputs asked. `[proposed: working rule]` From recorded answers alone, a $\mathsf{yes}$ about every input of a sort $A$ requires that the census is all of $A$ and $A$ has a covering fact; otherwise none, since a second box agrees on the census and differs elsewhere. `[decided]` A $\mathsf{yes}$ about every input is a claim about a definition. One recorded answer can still refute a statement about every answer (§20.8). A commitment made before the census fixes which definition is meant, and no more. The claim reaches the box only through a further claim: this endpoint, at this version and in this state, answers as the definition does; that claim is checked, or trusted by name, or assumed by name. A claim in probability about inputs not asked states how the inputs are drawn. `[proposed: working rule]`
Case: an endpoint commits to the program that always answers 0. It answers 0 to the first question and 1 to the second. The commitment still opens correctly. `[proposed: working rule]`

**§20.8 The black-box limit.**
With no claim tying the endpoint to a definition, the SRE has exactly four things. (1) A $\mathsf{yes}$ for each input asked, as a run record. (2) A $\mathsf{no}$, for the whole sort, to any statement about every answer that one recorded answer refutes. (3) That a name $n$ cannot answer a question: two recorded inputs under $n$ with no common right answer. (4) A lower bound on names: $j$ recorded inputs whose answers to the same experiments disagree in pairs need $j$ names. (3), (4) and any answer given from the record in place of asking again lean on the endpoint answering the same input the same way; that is a claim about the endpoint, and where assumed it is an assumption by name in the manifest and in the semantic part of the lock. Everything else is a candidate. `[proposed]`

**§20.9 Vector names and a rank bound.**
At the first finite SRE stage, try names that are vectors over a declared field, with checked trackers for the named operations. `[proposed]`
Review exact arithmetic when the first SRE stage’s requirements are written. `[decided]` If integers do not suffice, bring the rational model with that stage. `[proposed]`
For summaries of dimension $d$ whose answer on a gluing factors as $f(\mathrm{glue}(G, H)) = \sum_{i=1}^{d} \phi_i(G)\,\psi_i(H)$, both vectors over that field, a checked nonzero $r \times r$ minor of the table of probe-pair answers rules out $d < r$. The record names the field, probes, entries, exact minor check, endpoint assumptions and scope (§20.7). This bounds vector dimension, not the number of names. It proves neither that a candidate tracks nor that a state of dimension $r$ exists; a minimum needs a checked state attaining the bound (not run). `[proposed]` The reason in one line: for probes $G_1, \dots, G_m$ and $H_1, \dots, H_n$ the table $P_{jk} = f(\mathrm{glue}(G_j, H_k))$ is a product of an $m \times d$ and a $d \times n$ matrix, so its rank is at most $d$, and a nonzero $r \times r$ minor gives rank at least $r$. Illustration: if two probes on each side give the identity matrix of order two, its determinant is $1$ over any field. A one-dimensional factorization is impossible. The identity minor gives no tracker for either operation.

### Sheets; coarsest and cheapest

**§20.10 What comes out.**
For each representation, a sheet with one line for each question already named; SkeinLab can also keep a fit or a newly suggested question as a candidate note. A line says whether the answer is exact, within a width, one-sided or not given; it carries the claim and its cost, and says so when it tells the reader nothing. A refutation is a set of values with one name and no common answer, kept with the class of realisers it rules out. Also returned: the coarsest representation that still answers a given set of questions, found by refinement and checked clause by clause. `[decided]`
Checked clause by clause, a representation is shown sound, not coarsest: one with a spare name passes every clause. That it is coarsest is a statement of its own and needs a claim that a kernel program checked (§20.3); without one the sheet does not say coarsest. Where a question has several right answers, exact on a line means the answer given is one of them (§3.2), and the line's claim says so. `[proposed]`
Open: which claim says that a representation is coarsest; it is not chosen here. `[open]`

**§20.11 First family-generated refutation.**
A family generating refutations names the observer and its available observations, the construction that makes the observations agree, and the question that separates the inputs. A claim for the whole construction needs its own evidence. `[proposed]`

**§20.12 Asking for a coarsest representation.**
A writer may ask the compiler to find a representation that answers what one client can reach; `realize ... by coarsest` is a candidate spelling under §1.64. Finite cases enter with slice 3; infinite cases wait until after slice 4 and need evidence for the claimed scope, which a census alone does not give. Search has a stated budget; if no candidate is accepted, the admitted program keeps its ordinary runnable path (§10.1). Tracking clauses show soundness; coarseness needs the separate claim of §20.10. `[proposed]`
Return to field use before the uses reported by the manifest computer’s second result (§5.4) become trusted text. `[decided]` For each pattern matching a constructor, decide whether the result should report which arguments its rule uses. `[proposed]`
Proposed controls, unrun. Give lists two distinct items $a,b$ of weight 1 and try their natural-number total as a summary for append and total weight. Asking for the last item separates $[a]$ from $[b]$ and refutes this summary alone. For pairs $(x,y)$ observed by $x+y$, try the sum with swap and `inc_x`. Adding `double_x` refutes it on $(1,0)$ and $(0,1)$. Slice 3 takes only covered finite cases. Universal list and integer claims wait for later evidence. `[proposed]`

**§20.13 Coarsest representation; coarsest is not cheapest.**
Let $\mathrm{Ans}_q(v)$ be the set of right answers to question $q$ on value $v$. For a name $n$, its block is $[n]=\{v\mid\mathrm{names}(n,v)\}$. When every value in scope has exactly one name, compare the resulting partitions by refinement: one is strictly coarser if every block of the finer partition is contained in a block of the coarser partition and the partitions differ.
Illustration of the limit for overlapping names: consider the constant question and the identity operation on $\{a,b\}$. The covers $\{\{a,b\},\{a\}\}$ and $\{\{a,b\},\{b\}\}$ both work. Each block of either is contained in a block of the other. Mere inequality of the covers would declare each strictly coarser than the other. A containment-based *strict* comparison would have to require containment in one direction and failure in the reverse direction. Which claim certifies coarseness in the permitted class is open (§20.10).
(1) Where each question has one right answer and each operation gives one result, the coarsest representation for a set of questions and operations has as names the classes of $\sim$, where $v \sim w$ iff no run of the operations followed by a question tells them apart: $q(\bar g(v)) = q(\bar g(w))$ for every $q$ and every finite sequence $\bar g$ of operations, the empty one included, any other arguments of an operation being held fixed.
(2) Where a question has several right answers there may be several coarsest representations, none coarser than another, and the classes of $\sim$ need not be finer than such a representation: two values that nothing tells apart may stand under different names of it. There, say which answers are right and what the tracking clauses require before calling a representation coarsest.
(3) A coarsest representation says what suffices and nothing of cost: building a name can cost more than asking the object as it was given. A choice among representations needs a workload $W$: how the object arrives, and how many questions and updates follow. `[proposed]`
Cases. (a) $\mathrm{Ans}(a) = \{0\}$, $\mathrm{Ans}(b) = \{0, 1\}$, $\mathrm{Ans}(c) = \{1\}$: $a, b$ may share a name answering 0, $b, c$ one answering 1; all three may not share one. (b) $3 \times 3$ tables of bits named by their six parities: one question costs 3 reads on the table and 10 by way of the name; six cost 18 and 15. (c) $\mathrm{Ans}$ of $a, b, c, d$ is $\{0, 1\}, \{0, 1\}, \{0\}, \{1\}$, no operation: nothing tells $a$ from $b$, so the classes are $\{a, b\}, \{c\}, \{d\}$; the names $\{a, c\}$ answering 0 and $\{b, d\}$ answering 1 are a representation that cannot be made coarser, since $c$ and $d$ share no answer, and the class $\{a, b\}$ lies inside neither name. `[proposed]` Illustration for (b): the two pairs of figures fit 9 reads to build the name and 1 to ask it, so $j$ questions cost $3j$ on the table against $9 + j$ by the name, and the name is the cheaper from $j = 5$.

**§20.14 The sheet states workload and cost.**
A correct summary may store the answer to its question. The sheet states the workload $W$ and compares the representation’s cost $\mathrm{cost}(\rho,W)$ with $\mathrm{cost}_0(W)$ for asking the original object. If it costs as much or more, report no saving. Before fixing the sheet and the coarsest-representation query in slice 3, run §20.27’s census with and without operations. If the report presents an already supplied answer as a finding, it needs a refusal at reporting. This test is owed. `[decided]` The sheet may still report a structure the representation reveals, with its evidence. Before fixing the slice 3 sheet and coarsest query, also consider listing and charging the original-object reads needed to rebuild an answer for the optimizer’s cost comparison. `[proposed]`

**§20.15 Names need not be classes.**
Where a question has several right answers, one value may stand under two names. A family $\mathcal{U}$ of overlapping sets is a representation when each $U \in \mathcal{U}$ has a common right answer to every question $q$ asked ($\bigcap_{v \in U} \mathrm{Ans}_q(v) \neq \emptyset$) and every operation carries each $U$ into some set of $\mathcal{U}$; read here with each $U$ non-empty and the family covering the values in scope. It can have fewer names than any such partition. For operations of one hidden argument that each give one result there is a greatest such family: the sets that keep a common right answer under every question after every sequence of operations. The greatest is not the one with fewest names; finding the fewest is a search. With an operation of two hidden arguments a greatest family is not shown to exist. Nor with an operation that gives several results: a set may keep a common right answer under every single question after every sequence of operations while no tracker serves it under one name, because the answers to two questions must come from one outcome. Under such a representation the answer for one value can depend on the path that reached it. That is sound only where the meaning leaves the choice of right answer open at each asking; it is a tracker settling an open choice, so it stands in the semantic part of the lock (§11.2). `[proposed]`
Cases. (a) Values $a, b, c$; $g: a \mapsto b,\ b \mapsto c,\ c \mapsto c$; $r: a \mapsto a,\ b \mapsto a,\ c \mapsto b$. The sets $\{a, b\}$ and $\{b, c\}$ are closed and each has a common answer; no partition into two parts is closed with a common answer in each part. So two names against three. Illustration, with answers the case leaves unstated: $\mathrm{Ans}(a) = \{0\}$, $\mathrm{Ans}(b) = \{0, 1\}$, $\mathrm{Ans}(c) = \{1\}$. Then $\{a, b\}$ answers 0 and $\{b, c\}$ answers 1; $g$ and $r$ carry each of the two into one of the two; $\{a, b\} \mid \{c\}$ fails under $g$, $\{a\} \mid \{b, c\}$ under $r$, and $\{a, c\}$ has no common answer. (b) An operation $u$ of several results: $u(a) \in \{00, 11\}$, $u(b) \in \{01, 10\}$, $u$ changes none of those four, and two questions read the two bits, each answering 0 at $a$ and at $b$. Each question alone keeps a common right answer on $\{a, b\}$ after $u$, since either bit may be 0 or 1 from $a$ and from $b$. A name for $u$'s result must answer both: from $a$ the two answers are equal and from $b$ they differ, so no name serves both. `[proposed]`

**§20.16 A line is a reading.**
What a line of a sheet says (exact, within a width, one-sided, refuted or nothing) is a reading of its claims at one state of the store, and is not stored apart from them. `[proposed]`

**§20.17 When accumulated reports are complete.**
At the first reusable domain with §4.2, consider: "A domain merge records the question, scope and evidence of its inputs. Its completion test requires a consistent, certified answer." Try an inconsistent pair, two distinct existential witnesses, and claims with disjoint assumptions. Report the support for a conflict separately from completion, and distinguish a budget stop from a certified result. `[proposed]`

### SkeinLab

**§20.18 SkeinLab's loop.**
Exploration proposes laws and theories through the candidate-theories query, as §5.6 ranks it when that passage's test condition is met. The query for which unknown claims would give a goal proposes what to settle. Worth ranks both. SkeinLab's first duty is finding questions: what the representations distinguish on a census. `[decided]`
The provisional ranking concerns relevance to open goals under §5.6 and its test. A fit may also reveal a common structure or suggest which answer to try. Report what was observed and on which instances. SkeinLab looks for mathematical signals and connections that help find answers otherwise out of reach on hard problems such as the travelling salesman problem. A signal or connection may be a research result in its own right; a claim of cheaper computation needs a workload and a cost comparison. `[proposed]`

**§20.19 First joint-view case.**
Where two observations together answer a question, the account may give a pair of inputs for each observation alone. That observation agrees on the pair while the requested answers differ. The reconstruction specifies which observations it uses. `[proposed]`

**§20.20 Comparing kernels of invariants.**
At the first SRE stage for finding questions, compare the kernels of functional invariants on one named census. Equal kernels suggest equivalence; a strict refinement suggests a map from finer names to coarser names to synthesise and check; incomparable kernels give a separating pair in each direction and a joint-view candidate. Keep their kernel-inclusion order as a candidate catalogue. Each statement carries that census as its scope; beyond it, it is a conjecture until further evidence is checked (not run). `[proposed]` In symbols, for invariants $h_i$ on one census $C$ the kernel is $x \sim_i y \iff h_i(x) = h_i(y)$: $\sim_i\ =\ \sim_j$ suggests equivalence, and $\sim_i\ \subsetneq\ \sim_j$ a map from the names of $h_i$, the finer, to those of $h_j$.

**§20.21 Held-out sets.**
A held-out set is reached only through the operations of a named protocol, and a claim about inputs outside it cites that protocol's theorem. Where no theorem covers the path taken, SkeinLab reports what was observed and no more. (the rule; apart from the counting of looks in §9.15) `[decided]`
Owed: the test of the mechanism for held-out sets: the set is a use-once value of a hidden sort $S$ whose signature is the protocol's operations; the use-once check then holds every client to the protocol, and a protocol that allows a second look hands back a new value to look with (to test). `[proposed]`

**§20.22 Assessing a later research method.**
At the first authorized later research client using an exact classification, check both maps and one client operation. Compare with the false inference that groups of equal size have the same operations. For the first learned-policy comparison, report warranted findings from fresh searches under one allowance. A mathematical result states its scope and evidence; a saving needs its workload and comparison. When a SkeinLab method first combines advice from several views, establish common meaning and equal disclosure; record lineage and adaptive looks. For each conclusion link the signal, alternatives, budget and decision to the relevant evidence (feasibility, optimality, completeness, approximation or a new population). Compare against advice derived from a shared source. At the first disagreement-selected probe, record its question, budget and the outcome that would change the explanation. Under the same disclosure and lineage conditions, match the budget against a control, such as reversing order or retaining every candidate. Later branch removal needs checked coverage (§20.36). `[proposed]`

**§20.23 Four-city paper example, for the next SkeinLab investigation commissioned by the project owner.**
A symmetric complete graph on $A = (0,0)$, $B = (4,0)$, $C = (4,3)$, $D = (0,3)$, the rectangle kept fixed. For $0 \le \lambda \le 3$ the costs are $AB = 4 + \lambda$, $CD = 4$, $AD = BC = 3$, $AC = BD = 5$. The rectangle fit gives exact distances at $\lambda = 0$ and an edge error of $\lambda$ on $AB$ thereafter. Each undirected tour omits a perfect matching, and every omitted matching gives one tour; tour cost = total of all six edges minus the matching's weight:

| Omitted matching | $\{AC, BD\}$ (perimeter) | $\{AB, CD\}$ | $\{AD, BC\}$ |
| --- | --- | --- | --- |
| Tour cost | $14 + \lambda$ | $16$ | $18 + \lambda$ |

The geometric fit favours the perimeter throughout. In the weighted problem it wins below $\lambda = 2$, ties at $\lambda = 2$ and loses above. At the tie, exact methods can give the same cost 16 and different routes under their lawful resolvers. At $\lambda = 3$ a one-tour budget following the geometric order returns a feasible tour of cost 17; checking all three proves 16 on this instance; putting the other candidate first under the same one-tour budget changes the result. `[proposed]`

**§20.24 Controls for the example.**
Move the penalty of 3 from $AB$ to $BC$: the three tour costs become 17, 19, 18, although the mean absolute edge error stays 0.5. A quarter-turn about $A$ preserves distances, sends $AB$ from $(4,0)$ to $(0,4)$ and, under the fixed axes, changes the rightmost set from $\{B, C\}$ to $\{A, B\}$; state the convention if one city must be chosen. The two fits share inputs, and the exact calculation reads all six original weights. The example locates a disagreement and its threshold. Any claim of a speedup needs a workload and a comparison, and any broader claim about the travelling salesman problem needs its own evidence. `[proposed]`

**§20.25 The record that crosses.**
One record crosses to the compiler or to a person: (subject, change, assumptions, what is preserved, evidence, estimated benefit), the last a note (§20.2). `[decided]` These fields describe a proposed change. A result sent to a person can give the fitted structure, connection or signal, its scope and what supports it. An estimate, when offered, is a note. `[proposed]`

**§20.26 A correction across versions.**
At the first checked correction across versions, name both versions, the transport of the old answer and evidence for the value or bound of the correction. At the first concrete precision client, test overlap and transport. Three isolated vertices have eight independent sets. Each of two distinct edges removes two sets; one removal is shared. Both edges leave $8-(2+2-1)=5$. For a change of coordinates, $(10-2)\times2-1=15$; subtracting the untransported corrections from 20 gives $20-2-1=17$. Bring the proposed chain of successively tighter valid bounds when a concrete producer supplies remainder and stopping evidence. Its final level can be exact. `[proposed]`

### Proposers of representations and theories

**§20.27 A table of experiments.**
A name is the tuple of answers to experiments, each a question after a sequence of operations; a failed closure check adds an experiment; the naming relation is the conjunction of the experiments. It is a proposer: its faults waste budget and cannot make a false $\mathsf{yes}$. On an object that can only be asked it ends in candidates, since nothing plays the part of the lift. Nothing else falls with it. `[proposed: working rule]`
The owed trial covers every system of at most four values with one or two unary hidden-argument operations and one question giving a set of right answers at each value. Find the least number of names over closed partitions, the least over closed covers, and the greatest closed family of §20.15. Repeat with a binary hidden-argument operation. Compare each cover’s name runs with the allowed outcomes, using hand-found representations as controls. The trial is proposed and has not run. `[proposed]`

**§20.28 First discovered split offered as a recurrence.**
A proposed branching rule identifies a runnable subproblem for each branch, accounts for every intended result with its required multiplicity, and names a quantity that decreases on every recursive call. `[proposed]`

**§20.29 Candidate theories from a three-valued table.**
A smallest generating set of the implications that hold is a compact form of the kept set of §5.6 and a candidate algorithm for it, not a rival. With $\mathsf{unknown}$ entries there are two tables, so "the" generating set needs care. Its test is a third count in the 56-candidate test of §5.6: the 56 as found, a smallest generating set, and the kept sets with conclusions taken from the unknown-claims query. `[proposed: working rule]`
One proposal for §5.6 supplies induction with the residual goals of failed lifts, with hypotheses indexed by a count. Its test has run and been confirmed on one family (§23.2 row 27): the schema with a parameter is kept, among 25 of 45 in the smaller language and 125 of 882 in the wider, and the language already contained it. That is a schema kept in a declared language, not the finding of that language, nor of one answer. `[proposed]`

**§20.30 Three routes from a definition to an endpoint.**
Checked, trusted, assumed. The first step replays the definition against every recorded answer, and that step alone refuses the case of §20.7. The checked route settles a transcript; a box with state needs a further claim; a verified container image is trust. Owed: the test of the three routes: the three records on that case and on one box with state, to see what each route can and cannot refuse. `[proposed: working rule]`

### The optimizer

**§20.31 General rule.**
$\mathrm{Runs}(t)$ is the set of runs the meaning of $t$ allows. (G1) An optimized run $r$ of $t$ satisfies $r \in \mathrm{Runs}(t)$. (G2) Where the meaning allows one answer, that answer stays. (G3) Where the program states a choice or a width, the optimizer may choose within it. (G4) A transformation is applied only with a checked claim that the new run is one the meaning allows. (G5) A kind of transformation that no rule covers is refused, and the plain path is kept. (G6) A claimed saving names its workload and baseline. (G7) Use the reference-run observations of §1.37, §8.10 and §8.12. §20.33 and §1.37 are the first instances. The rule limits what a transformation may change. `[decided]`
Open: the choice of the optimizer's aim. `[open]`

**§20.32 Reference fuel.**
The evaluator's fuel count $k$ is part of the evaluator's specification, so the rule's account would cover the reference meter's count: a claim settled by a fuel-bounded run would have the same verdict in every build, and only physical time and memory would be free to differ. `[proposed]`

For the paired reference profile, $k$ names both allowances. Replay in two conforming reference builds requires equal reached events, invoices, cuts and balances under equal admissible conditions. `[proposed]` Whether every optimizer rule must preserve an exact reference-budget verdict across compiled builds remains open (§24.1). `[open]` Enforce the particular exported promises of §3.19, including an opted-in meter and any enclosing boundary. A faster host implementation, cheaper work or lower physical peak alone does not establish these claims. `[proposed]`

**§20.33 The optimizer may change the algorithm.**
Another algorithm for $f$ is a representation with unchanged names. The tracker is the replacement program. Its claim says the programs agree on the stated scope (§1.57). `[decided]` This is also a conditional law rewrite. A theory describes a kind of structure (§1.35). Interpreting it at a problem gives a particular structure. Its laws become claims there, and a fast-algorithm theorem transfers under that interpretation (§1.41). `[decided]` The site reads the supporting evidence (§4.5). The SRE proposes the interpretation. The kernel checks each claim. The proposal supplies no evidence. `[decided]` A universal family claim states its domain and needs a checked derivation or a covering fact. A finite census and a paper argument supply neither (§23.2 row 25). `[decided]`

**§20.34 Which witnesses a later condition can use.**
At the first conditional rewrite that uses an observation algebra, compare selecting 0 before a requirement for 1 with applying the requirement to $\{0, 1\}$ before selection: the first has no accepted witness, the second has 1. Use the finite case to check the order of filtering and selection. `[proposed]`

**§20.35 Where the condition of a substituted algorithm is settled.**
One of four ways: (S1) proved for a family, by a derivation; (S2) checked for one object at build or at load, by exhaustion with a covering fact or by a decider named in the manifest; (S3) by a guard before the call, each time, with the cover §3.6 asks; (S4) by a check of the answer after the tracker and before any use of its result, each time: the attempt, then the check, then on rejection the fallback. Limits: (L1) the condition must be the tracker's own, which the plan covers with a branch; written as a membership of the argument in a narrower sort, a failed test would be a failure (§4.10). (L2) (S4) is sound only for a tracker whose manifest holds no effect; that is needed and not enough. `[proposed]`
(L3) For now, neither the attempt nor the check may run if either or anything it calls can make, read or write a sequence. All the other post-check conditions also apply. `[decided]` The exact rule wording awaits review. `[proposed]`
(L4) The attempt and the check must each end, or run under a checked mechanism that gives control back when its bound is spent; else the fallback is never reached. (L5) The fallback must still have its arguments, and every obligation the attempt or the check created must be accounted for. (L6) A rejected answer and a spent bound both go to a fallback that covers them. (L7) For now an attempt that consumes a use-once value is excluded: a restriction chosen to be safe, not a finding that no wider safe form exists. (L8) The rule is about the whole of attempt, check and fallback, not the attempt alone. `[proposed]`
An algorithm whose answer is within a factor of the best is a lax tracker (§3.14) and may replace the exact operation only where the meaning asked for an answer to that width. A problem with several best answers leaves a choice open, and an algorithm settles it: a selection in the semantic part of the lock, unless the choice leaves the manifest by indifference (§11.2). `[proposed]`

**§20.36 A handoff of unfinished work.**
At the first transfer of unfinished work between methods, pass the residual itself. Name the original question, requested observation, subject revision and settled part. Check that the settled and residual parts are disjoint, cover the subject and reconstruct the requested observation. Distinguish an open report from a completed answer. Compare transfer plus checking with restarting on the same workload, under §20.35’s conditions on the attempt, check and fallback. On a triangle with one pendant vertex, fixing the colour of its neighbour in the triangle settles four three-colourings. The disjoint residual has eight, giving twelve. Passing the original twelve gives sixteen. A wrong residual of eight can repeat the four settled solutions and miss four others. At the slice 5 interfaces, show the next stage uses the exact replacement accepted. Later branch removal needs a checked coverage reason. `[proposed]`

**§20.37 What licenses a greedy method.**
A theorem for the structure and the objective in hand, with its conditions checked; never a label, a fingerprint, a confidence, or the fact that local swaps usually work. For a finite, nonempty family of allowed sets in which every part of an allowed set is allowed, the greedy method that takes items in order of falling weight gives an allowed set of greatest total weight, for every nonnegative additive weight, exactly when the family satisfies exchange. Such a family is a matroid. Over its bases, items in order of rising weight give a base of least total weight, and of falling weight one of greatest, for arbitrary real additive weights. The general axioms of a greedoid give no such result, though some greedoids that are not matroids have a theorem of their own for every linear objective. Choosing from an e-graph is a different problem. With every occurrence of a shared part paid for and costs additive, the cheapest choice is found exactly in one pass from the leaves up where the dependencies have no cycle; where they have one, it needs a finite term to extract and costs that give a well-founded optimum, and repeated relaxation to a fixed point is one method. With a shared part paid for once it is NP-hard in general, which rules out a polynomial-time exact algorithm for all general, finitely encoded instances unless P is NP, and does not rule out exact methods on special families. An e-graph is a proposer's working memory and is not where correctness lives. `[proposed]`
Exchange, in its standard statement, for a family $\mathcal{I}$ of sets over a finite ground set:

$$I, J \in \mathcal{I},\ |I| < |J| \ \Longrightarrow\ \exists x \in J \setminus I.\ I \cup \{x\} \in \mathcal{I}.$$

Illustration of the failed premise: the matchings of a path of three edges weighted 2, 3, 2. Greedy takes the middle edge, 3; the two end edges together weigh 4. With $I$ the middle edge alone and $J$ the two ends, no edge of $J$ can be added to $I$, so exchange fails. The one pass from the leaves up, with every occurrence paid and costs additive, computes for each class $c$

$$d(c) = \min_{u \in c} \Bigl( w(u) + \sum_{b \text{ a child position of } u} d(b) \Bigr),$$

a leaf having an empty sum and a class used at two positions being paid twice.

**§20.38 Runnable definitions, optimum witnesses and search recognition.**
(1) A problem stated with nothing to run is refused, on purpose (§10.1, §10.4): every problem comes with a definition that runs, however slowly, and that definition is the reference the fast version is tested against. (2) A problem with several best answers should be stated with `pick` over the best answers and not by an order of search, or an algorithm that returns another best answer is wrong. `[decided]`
(3) Open: recognising a search that a user wrote by hand. Someone must propose that the term equals a library operation, and that is settled by a derivation or by exhaustion on a small sort. `[open]`

# Part VI. Open matters and evidence

<a id="ch-21"></a>

## 21. Open questions on identity, binding and ownership

**§21.1 One node is not one run.**
"$\mathsf{yes}$ because the two sides are one node" is false for a term whose run makes something new. Case: `make(1, 0)` written twice is one node and two sequences, which `same` tells apart; a constant of a use-once sort is the same case (§1.19). Each thing a run makes new has a name of its own: a use-once value in the reference run carries a name as a sequence does (§17.2), and the reference run's count of consumption (§8.8) is keyed by that name and never by content. Reuse of a result (§8.3) is allowed only for a term $t$ with

$$\mathrm{Reuse}(t) \Rightarrow \neg\mathrm{new}(t) \wedge \neg\mathrm{eff}(t) \wedge \neg\mathrm{open}(t) \wedge \neg\mathrm{cons}(t) \wedge \mathrm{copy}(t) \wedge \neg\mathrm{seq}(t),$$

where $\mathrm{new}$: $t$ makes something new; $\mathrm{eff}$: it has an effect; $\mathrm{open}$: it has an open choice; $\mathrm{cons}$: it consumes something use-once; $\mathrm{copy}$: its result may be copied; $\mathrm{seq}$: $t$ or anything it can call reads or writes a sequence. The restriction on sequence access holds for now. `[decided]` Its exact wording awaits review. `[proposed]` That $t$ is state-free (§17.3) is not enough: that test is about sequences and says nothing of a term that makes a value of a use-once sort, has an effect or leaves a choice open. `[decided]`

Proposed separately for laws: every conjunct above, $\neg\mathrm{seq}$ included, also conditions "$\mathsf{yes}$ by identity of node" (§8.4, §14.8). This is a conservative restriction on that proof route, not a further decision, and grants no wider identity licence. Identical effectful computations may have the same run while each executes separately. `[proposed]` Open: whether the extension to laws is necessary, and its exact scope. `[open]`

The name construction (§21.6) and compiled-name relation (§21.8) are proposed. `[proposed]` Return, transfer and packing preserve the value (§21.7). `[decided]` The promised-once function case is open. `[open]`

Owed: the test, over every small term, comparing "one node" with "two runs give the same value". `[open]`

**§21.2 Two live values in one place of the machine.**
Open: two of the meaning's values kept in one place of the machine pass every tracking clause, and a later read returns the wrong one. Case: two cells made with 10 and 20, both named by one slot; reading the first gives 20. `[open]`

Proposed clause. Write $\mathrm{supp}(n)$ for the parts of the machine's state that the name $n$ of a live value rests on. (i) Names of distinct live values do not overlap: $\mathrm{supp}(n_1) \cap \mathrm{supp}(n_2) = \emptyset$. (ii) A tracker $\tilde f$ changes only the parts its own arguments rest on, $\bigcup_i \mathrm{supp}(n_i)$. Settling test: the obligation generator on that two-cell tracker, which must be refused. `[proposed]`

**§21.3 The core let: the choice.**
A core let is added whose body belongs to the enclosing use-once scope, and the example is admitted: `f(h) = let y = work(); use(y,h)`, where `h` must be used once and `work()` returns an ordinary value. `[decided]` The let's record, check and inlining contracts remain open. `[open]` §21.4 proposes its record, run, admission and removal, and §21.5 proposes the use-once clause. `[proposed]` Its test: `square(work(x))` run by a rule step, counting runs of `work`; and the use-once check on a `let` whose body uses an outer use-once value. A related point is answered elsewhere: a use-once value consumed once in each of two branches is two sites in one scope (§1.13), is written as rules that take it as an argument (§1.14), and its remaining case is recorded as refused though right (§1.32). `[proposed]`

**§21.4 The core let: record, run, admission, removal.**
Record. $\mathrm{let}(e, b)$ is a node of its own: an initializer $e$, and a body $b$ with one more variable $x$, which stands for the value of $e$. It is a different node from the applied binder of the same text, and the two differ in the use-once check (§21.5).

Run, for runs that return, in environment $\eta$:

$$\frac{\eta \vdash e \Downarrow v \qquad \eta, x \mapsto v \vdash b \Downarrow w}{\eta \vdash \mathrm{let}(e, b) \Downarrow w}\ \textsf{(T-Let)}$$

$e$ runs first, once, in the let's environment, even where $b$ never reads $x$; reading $x$ runs nothing again (§8.3). A source core let begins no activation: $b$ runs in the activation of the scope the let stands in. This gives no permission to replace an applied binder or erase a called rule's reference activation. A rule step or lowering that binds obtained arguments with a let must retain the reference activation of the replaced call and attribute its consumption there, unless a claim licenses the change (§8.6, §8.10).

Admit a let as the applied binder in §7.3 (F-Beta), in the same ambient context. For an admitted initializer the result sort instantiates the body’s dependent indices:

$$\frac{\Gamma\vdash e\Rightarrow A\qquad\Gamma,x{:}A\vdash b\Rightarrow B}{\Gamma\vdash\mathrm{let}(e,b)\Rightarrow B[x:=e]}\ \textsf{(T-LetAdm)}$$

A let may stand wherever a term may stand, and is how a run is named once (§8.4).

Rule steps. For an ordinary value argument admitted at a sort, a rule step may bind its obtained value with a core let, preserving reference argument order and logical call activations. Case: `square(work(x))` becomes a let of `work(x)` whose body uses its variable twice, and `work` runs once (§1.5). This recipe does not cover a contextual bound argument: its signature, bound-variable sorts and multiplicity must stay attached to its admitted position, and the contextual bound-argument form is kept until an admission-preserving replacement is specified and checked. Nothing here admits a binder or use-once function in a let initializer, or adds a sixth position to §9.2.

Removal. $\mathrm{let}(e, b) \leadsto b[x := e]$ only as §8.6 allows for $e$ (§1.5): never where $e$ has an effect, an open choice or a possible run without end, consumes a use-once value, or makes something new. Slice 1 has no planner, so nothing there removes a let; a let comes from the reader of text or from a rule step.

Effects. The reader makes no let for an effect: an effect's last argument is its bound continuation (§1.6), and text that binds the result of an effect is turned into that continuation (§6.1, stage 1). An effect written inside an initializer is read as one written inside an argument: its continuation is the rest of the scope the let stands in, that is the rest of the initializer and then the let with its body. The reader ends no continuation at a let. So under the narrower rule that form is refused wherever what follows the effect consumes a use-once value bound outside it, as the straight form of §1.30 is. Ending the continuation at the initializer would admit that use after an output in slice 1 and change the scope of a handler’s continuation. The proposal keeps the enclosing scope. The written form and charge of a let are open. `[proposed]`

**§21.5 The let in the use-once check.**
A let's body is not a scope of its own: $e$ and $b$ belong to the scope the let stands in, and that scope's sites are counted through both. So a use-once value bound outside the let and consumed in $b$ has a site of the enclosing scope, and no binder consumes it from outside: `f(h) = let y = work(); use(y, h)` passes clauses (a) and (b), and the narrower rule of §1.30 does not refuse it. `[decided]`

Where $e$ was checked at a use-once sort, $x$ is a use-once value of that scope and has exactly one site in $b$. A value standing as the whole of $b$ has that body position as its one site, and the let's own result has its site where the let stands. Standing as the initializer is the one site of the initializer's node, and the value passes to $x$ without being consumed: binding consumes nothing (§21.7). A let is no exception for any binder: the applied-binder form of the same text, and a continuation, are binders, each body is a scope, and one that consumes a use-once value from outside is refused under the narrower rule. The control that goes with the let's test is that pair: the let accepted, its applied-binder form refused. The decided examples have ordinary initializers. A census must test the proposed reading of clause (a) for a use-once initializer. `[proposed]`

**§21.6 The name of a use-once value.**
The name is a pair of a scope and a count $j \in \mathbb{N}$, as a sequence's is (§17.2). The scope is made from the run's start in the same way, under a fixed label of its own, so no use-once value has the name of a sequence. The count is the reference run's own, kept in its state beside its count of activations (§8.8): it begins at 0, each making takes the next count, and no count is used again. It is not the evaluator's count of sequences, which names what an evaluator program makes, so leaving a sequence out (§8.6) does not move it. No operation gives a program a use-once value's name: it is seen in outcomes, records and comparisons only. A use-once value that comes in from outside keeps the name it came with. The makings in the decided cases follow §21.7; the promised-once function case is open there. `[proposed]` Open: how the host names a use-once value, which belongs to the unwritten host interface. `[open]`

**§21.7 Making, moving and consuming.**
Returning a use-once value, passing it along and putting it inside a datum all move the same value. In particular, recursive passing in `spin(h) = spin(h)` does not consume `h` (§1.22); taking the data apart uses up the data and hands on its fields. So an operation defined by rules makes nothing by returning: it hands on what its right-hand side gave (§1.18). A run *moves* a value, keeping its name and consuming nothing, by binding it to a pattern variable, by passing it as an argument to an operation defined by rules, by putting it in a datum, and by handing it on as a result or in a failure. It *consumes* a datum when a rule's pattern takes it apart, and the fields pass to the pattern's variables under the names they had. `[decided]`

In the proposed accounting, a run *makes* a use-once value at each run of a constructor of a data sort declared use-once (§1.19), and at each run of a closed operation with no rules that returns one; binding a value to a let's variable consumes nothing (§21.5); what a run holds at any moment, an asked run among them, is what it has made or been given and has not consumed (§1.23); and the reference run's count of consumption (§8.8) is a count of consumings, each with the activation it happens in. `[proposed]`

Open: a function promised to be called once, at a parameter of multiplicity $\mathbf{1}$. Does first binding create an obligation, and does handoff preserve it? Check construction, extraction, transfer and call of a constructor-held function. Pass one capture-free function through two successive one-parameters to a single call. Also cover a known rule whose declared-any parameter passes when checked as use-once, and a use-once function applied or returned under the broader rule. The narrow first slice refuses the outside-capturing examples. These controls leave the making event open. `[open]`

First build. A declaration without rules grants no general authority to consume a use-once argument. An operation with no rules that is closed (implemented in the host, or an evaluated definition) takes no use-once value, bare or inside data: its declaration is refused as not yet supported, naming the parameter and the inside sort. An operation run through a selected interpretation whose image has rules goes through the image. `[decided]` Open: the mirror case, a closed operation returning a use-once value; its later shape is to be decided with the split and six ownership questions in §1.28, together with the host ownership interface, before slice 2's interfaces. `[open]`

**§21.8 Matching a compiled run's names to the reference run's.**
A comparison of two runs is under a relation between their names, which is one of the matching choices of §8.10. In slice 1 the relation proposed is equality of names. Both runs begin from one start, so their scopes are equal. The compiled run takes its counts in the reference run's order, because the plain path chooses nothing: no planner moves a term, arguments run left to right (§8.2), each run that makes a value has its own corresponding run (§8.6), and the bound permits no open choice (§1.46). §21.7 supplies the name-preserving account for the decided cases; the promised-once function case is open.

That the order is the same is not taken on trust: the watch reports each making with what made it, and a comparison begins with the two orders of making (§8.13). Before a making-order comparison is marked checked:

- define its maker-provenance projection, and the relation from lowered events to reference production occurrences;
- the projection must distinguish different production occurrences even when constructor, payload and final counts are equal, repeated occurrences in a loop included; constructor kind or creation ordinal alone is insufficient;
- bind the relation to the compared lowering and logical activations;
- include a control that exchanges two same-constructor, equal-payload productions while keeping their source destinations, together with the correct positive control. The reason: after such an exchange the counts, the constructors and the payloads all still agree, so only the relation to the production occurrences can tell the two runs apart.

Until that projection and its actual event correspondence are checked, the making-order comparison is recorded as unchecked. The exact fields and encoding belong to the draft of the interface between the runtime and the reference observer.

A compiled run that stops for a resource has made a first part of what the reference makes, under the same names. A lowering that changes the order in which values are made owes a relation of its own, with its tracking claim; the open point of §8.6, on a sequence that nothing reads, waits for that. `[proposed]`

<a id="ch-22"></a>

## 22. Further proposals and open questions

**§22.1 Replacement searches and shared search checks.**
Proposed for the optimizer:

- (a) Recognizing a search a user wrote by hand takes three separate claims: this program computes this operation; the interpretation satisfies the theory's laws; the replacement tracks it. Equal final values are not the first.
- (b) A call to a named library operation is searched in a stated order: identity, evidence already held, recipes for that operation, cheap refutations, then proofs.
- (c) A failed attempt reports which it was: a checked counterexample, a name too coarse, an obligation left, a form not supported, a budget spent, or a cost observed. A failed induction step is not a refuted law.
- (d) For a stated search objective, a search has one budget for proposing, checking and refining together. Exhausting a grammar shows absence only inside it, only with its covering fact, and only where every candidate was excluded conclusively; a proof left unfinished leaves absence $\mathsf{unknown}$.
- (e) A cost is recorded as a bound, a measurement or an estimate, and each claims something different: a recorded computation establishes the number it returned on the bytes it names (§4.18); a bound covers its stated domain and needs evidence for that domain; an estimate carries its method and does not become a bound.
- (f) Extraction from an equality graph names how shared parts are charged. Case: the minimum on one graph is 8 per occurrence and 5 when each shared part is paid once. The latter extraction costs 10 per occurrence. `[proposed]`

Illustration: choose a single leaf costing 8 or a zero-cost root using the same cost-5 leaf twice. Per occurrence the costs are 8 and 10. Paying once per shared part gives 8 and 5.

Open: that the four routes of §20.35 mix scope, time and kind of evidence. `[open]` Open: a set of seven records for the shared interface. `[open]`

**§22.2 Recovery.**
Open: for the backend, what a compiled program must know at each call that may fail (which roots are live, which are moved or consumed, where they are), and that building the record of what survives cannot itself lose a value when memory runs out. `[open]`

**§22.3 The concurrency core.**
Proposed:

- (a) For §9.12: the carrier of a finished owner is clear or residual, where clear means this owner kept nothing, not that nothing waits; a probe that is pure, total and returns its whole argument; and the missing premise, that wherever an owner returns residual the whole outcome holds a wait. Without that premise a free cell holding a value is residual with no wait.
- (b) Looking at the queue hands the queue back, or the queue is used twice.
- (c) On two processors each real run must match some sequence of picks at whole segments, and a scope ends only when nothing is running, in flight or able to add work. Case: two tasks that each read a counter and write one more give 2 in the core and can give 1 on two processors. `[proposed]`

Open: four things, each filling a place marked as later: a use-once permit that makes "give it back to this cell" enforceable; protocols as a grammar with duals and hidden endpoints; a certificate of progress that names its claim and its assumptions; the price of a scheduler over first-order command tags. `[open]`

**§22.4 Finding laws.**
Proposed:

- (a) A smallest generating set of the implications that hold is a basis of one theory, and is a different result from a set of alternative theories (§20.29).
- (b) A declared language of hypotheses names more than which laws and how long a body: its symbols, its constants, the sizes of terms and clauses, its quantifiers, and how fitting is decided. A length limit alone does not make it finite, and a finite one need not be affordable.
- (c) A failed proof is kept as a residual with its assumptions, and three outcomes are kept apart: a false law, an induction hypothesis too weak, and an attempt not finished. `[proposed]`
- Exact methods come first. A guarantee from samples waits for the first job where an exact check has been measured as unaffordable and the bound has a derivation (§4.19). A timeout alone is insufficient. `[decided]`

**§22.5 Ordering experiments.**
Ordering experiments by a prior is optional. Declare the objective of the ordering. The default is the guaranteed split (§5.7). Policies for different objectives stay separate. `[proposed]`


**§22.6 Building during a run.**
Proposed, filling what §12.2 says is not designed:

- (a) A version of a part is fixed once made; a new one takes new calls and running ones finish where they are; moving a running computation is a separate checked step.
- (b) A version is kept while a frame, a pending return, a closure, a suspended continuation or live code can still enter it.
- (c) Making, checking and publishing a version are separate, and no caller sees one half published.
- (d) A fact learned in a run has a scope; a part built for it is entered only inside that scope or after a test, and falls back otherwise. Case: a sum built for length two gives 11 on $\langle 4, 7 \rangle$ and must give 20 on $\langle 4, 7, 9 \rangle$.
- (e) For builds other than the fixed first-call build: each attempt has a budget and then goes on by the version it has or a fallback; a build that runs out is not a failure of the program.
- (f) The record names each build and each version entered; replaying what a program did, replaying what was planned and reproducing the bytes are three claims.
- (g) "Runs ahead of time" is tested with the ability to publish code taken away. `[proposed]`

For the fixed first-call build of §12.4, a failed build stops the run cleanly, with no spare copy of the function. `[decided]` Open: whether that stop is a resource stop under §3.17. `[open]` Open: taking unit build jobs in fixed slots by the loss each avoids. The two sources for that proposal could not be checked. `[open]`

**§22.7 Look-back.**
Proposed: step 3 of §1.39 is split into terms that are pure and total and the rest, because a kept construction's own run is then part of the claim. A view that respects named laws names them, exports only what respects them, and gives the same answer whatever the optimizer's budget. `[proposed]` Open: what an inspector may see of a variable's number, which is the question of how variables are numbered, from another side. `[open]`

**§22.8 Facets and the manifest.**
Proposed:

- (a) Admission uses one selection of routes for all demands. Case: if one route avoids a write and trusts a forbidden checker and another does the reverse, each demand has a route and the plan is still refused.
- (b) A bound says which of three things it promises about finishing: a bound on runs that return, which holds only if they return; that the run finishes within the bound; or a cap that is enforced, with the stops it permits named. `[proposed]`

Open: a view for what an observer may learn, since a manifest holding "reads a secret" and "writes in public" cannot tell writing 0 from writing the secret. `[open]` Open: a view for what a computation needs from its context. `[open]` Open: whether a reference to a store’s cell can leave its store. The assertion that it can lacks a term showing escape. `[open]` The case for five facets rests on the first of these open items, a view for what an observer may learn (§1.59). §3.19 to §3.21 fix the default observer, the public law and the two-run description; the view itself stays open. (for where the case rests; the view remains open) `[decided]`

<a id="ch-23"></a>

## 23. Working rules and what the finite checks establish

**§23.1 The working rules, their tests, and what falls with each.**
The table gives each working rule’s scope, its checks and its fallback. Some checks have run only on a finite case, are unnamed, or must pass before the rule may be relied on.

| Working rule | Its test | If it falls |
|---|---|---|
| Runs by occurrence: §1.13, §1.15, §1.17, §1.19, §1.21, §8.3, §8.4 (decided) | Owed: rerun comparisons on the whole language, handlers beyond small fixed cases, sort indices, lowering. What has run: §23.2 rows 4 and 17, both reviewed | Use one run for each node and add a table of results to the state of §8.8 |
| Quotation: §1.34 | None named beyond the written form of the mark | The unqualified data rule stands: any node can be read as data (§1.34). Terms, theories, interpretations, representations and derivations are each values of their own sort |
| The store's continuation: §3.11, §3.12 | Checked on two finite models, each reviewed (§23.2 rows 13 and 14). Owed: general capture derivation, the specialising check and its cache, and lowering. `[open]` | §3.13 alone stands |
| A last use: §3.9 | A separate run checked its case. Owed: the footprint record test. | The fallback keeps the old name even after a step with no hidden result. In the `finish` case the value was consumed, so no successor value can relate to that name (§3.9) |
| A manifest entry's source and time: §1.45, §1.46 | Owed: a bound distinguishing a build-time check’s write from a runtime guard’s write. | Every entry counts as acting in the run |
| What a use must assume, on a fixed core: §4.11, §4.12 | Owed: the four cases at the end of §4.12 in slice 4. | Only the first and last rows of the table of §4.11 are used |
| A condition in a signature: §7.8, §7.9 (decided; the test is still owed) | Owed: an index bound and a purity condition: one test a call, each argument run once, evidence at the site removes the test, §4.13 refuses to assume the bound. And the comparison of §7.10 | The failed test goes back to the project owner for a decision; a sort made by a predicate remains the alternative |
| A black box: §20.7 | None named; its case is the control | Nothing else |
| The third way for bound arguments: §14.6 | No specific test is named. | Nothing else |
| Abduction ranks induction: §5.6 (ranking is a provisional decision, to be reconsidered against bounding) | Owed: the 56-candidate test, with the third count of §20.29. Application awaits the unrun test and review of all four counts | The candidate-theories query stays as §5.3 has it |
| Four further rules: §7.10, §20.27, §20.29, §20.30 | Named in each passage | Nothing else |
| The concurrency core: §9.2 to §9.6, §9.8 to §9.11, §9.14 (the design architect’s delegated call) | Owed: the whole-language census with functions held in data, by context. Not run. The three core tests that ran are §23.2 row 18 | §1.4, §1.16, §7.2 and §3.12 stand as they are, and a binder that is neither applied nor a bound argument is refused |
| Look-back that cannot be seen: §1.37, and step 1 of §1.39 | Owed: the §1.37 test with its nine controls. Step 1 of §1.39 needs a census of operations defined by rules, across element sorts and following helpers, and then the theorem. What has run: §23.2 row 28 | The marked laws are used only as any law is, by a proposer, with no mark; step 1 stays a decider named in the manifest |
| Declared look-back by name (§1.38), provisional pending approval and four tests. Only the mark at the call may be relied on meanwhile. | Owed: a written, accepted rule for whether the looked-at argument runs, then four tests against it: a variable in the looked-at argument; an argument with an effect; refusal when the function is handed on; the same answer from a part built during a run. Not run | The quotation written at the call stands alone, and the declared form returns to step 4 of §1.39 as a later step |

Except where a row gives a different standing, the rule in its first column is provisional. `[proposed: working rule]`

**§23.2 The register of run results.**
Read each numerical result with its model, rule and coverage. A result obtained under a different rule bears only on that rule. A finite census establishes its enumerated cases. None of these results proves the general design.

| # | What was checked, on what, with what result and limits | Run under |
|---|---|---|
| 1 | Use-once, the larger model, 657,283 terms: the old count accepted 37,564 wrong; clauses (a) to (d) accepted none and kept 160,022 of 161,498 right; the narrower rule kept 126,014 | One run for each node, sites by identity. The current rule counts occurrences |
| 2 | Use-once, the smaller model, 5,357 terms: the old count accepted 924 wrong; (a) to (d) none, keeping 1,379 of 1,423; rule steps change 3,725 terms, 181 lose acceptance and 282 gain it | As row 1 |
| 3 | A constant read as an outer value only: 4 wrong of the 5,357 of row 2; in a second model 48 wrong of 80,585 | As row 1 |
| 4 | Run by occurrence, count by path, a new value at each run: no wrong term in 110,285 and 486,623 terms, keeping 30,330 of 31,079 and 90,652 of 91,983 right. With a constant as one fixed value, 20,754 wrong. With the rule steps §1.5 allows, no accepted term changes and 222 refused become accepted. A recount of both tests, the first to seven occurrences and the wider to six, agrees on every count | §8.3, §1.13, §1.19 |
| 5 | Without the rule on data with a use-once field, the wider census accepts 8,094 wrong terms | §8.3 |
| 6 | The store's continuation, 276,528 programs: the fixture’s alternative form of the restricted rule corresponding to §3.13, used alone, accepted no wrong term and refused 87,196 of 92,176 right; a rule on the continuation's text alone accepted 2,148 wrong | Fixture’s restricted form only |
| 7 | Forms: of 60,000 random systems 164 pass forward and 33 backward, none wrong. Without B0, 1,017 of 1,256 wrong; in a second count 794 of 811 with an empty name wrong and none of 13 without. Mixed forms print 1 where the meaning prints 0. A late-choice name read twice gives (0, 1). A holding with one name for every integer passes F1 to F3 | §3.7, §3.8, §3.14 |
| 8 | Composites: 427 in one form all pass, none wrong; of 97 forward-then-backward, 17 pass neither form, none wrong. 758 forward first-order systems closed under Close reach no wrong pair; 593 of them had a name that stands for several values, with a two-argument hidden operation and a branch on an observation. Start clause applied only after removal: 6 of 48 leave a bad pair | §14.2, §14.4, §14.5 |
| 9 | Rules on claims: a list of three cases was refused a count because a fourth was missing, and the four-case list was given the count 4; with arbitrary sets as answers 6,257 of 16,838 unanswerable cases had no refuting pair, with intervals none of 36,986; one guard settled five times in a run, $\mathsf{yes}$ four times and then $\mathsf{no}$ | §4.4, §4.8, §4.10 |
| 10 | Queries: the polynomial $96 + 93\,\mathit{comm} + 40\,\mathit{assoc} + 31\,\mathit{assoc}\cdot\mathit{comm}$, with totals 189, 71, 62 and worths 118, 3, 9. An inference, to be confirmed against the run: each route's cost is taken where its claims are $\mathsf{yes}$, the least is kept, and the totals are over two sites, one of which already has comm. Three instances gave 56 candidate theories, among them that every ring commutes, and a fourth removed 7. A power algorithm was refused over floating point, naming four laws that are $\mathsf{no}$ there; over the Gaussian integers its answer was seven claims to settle; a second algorithm had nothing to settle over the integers and was licensed | §5.3, §1.48 |
| 11 | Manifests: a decider entered a manifest only through the evidence of a membership claim; a pick with no continuation is one node; rules tried in order gave two answers on a term with a variable. The failure clause ran on one case with two hosts, and nowhere else, with a client that has no handler: a tracker with another payload is told apart under the host that reports payloads and not under the other, and a tracker that returns where its operation fails is told apart under both | §1.44, §1.53, §8.5, §3.16 |
| 12 | Other bounded results: eleven toy results, the SRE's two small sheets found by hand, the toy's printouts, and the cases against the old count | Various |
| 13 | The store's continuation with supplied capture information: 276,528 annotated terms, 92,176 right and all admitted, 184,352 wrong and all refused. Independent confirmation is reported secondhand. The evidence cited here omits the review itself. Capture placement and ownership were supplied facts of the finite grammar; forgetting inherited capture admits 864 wrong cases. Not established: deriving capture in general, the specialising check and its cache, stops for a resource, native lowering | §3.11 to §3.13 |
| 14 | An inner handler that reads the store: the main term returns only (0, 0) or (1, 1) with sound ownership and is admitted, four of six terms in all; an outer handler that resumes twice gives all four pairs. The independent check covered six terms, with 12 runs on names paired with 12 concrete runs. That four of six terms are admitted says nothing of handlers in general | §3.11 to §3.13 |
| 15 | Agreement at a stop: of four lowerings, the one that consumes the first value and runs out of memory is recorded as stopped for a resource and not as agreement; the three that consume twice, consume an unrelated value, or consume a held value before failing are refused. 28 comparisons, none counting a stop as agreement. The counts exclude a run with an invalid reference. The independent check used 56 replays and 246 instructions, giving five agreements, four stops for a resource, 17 refusals and two inconclusive. For a permitted resource stop the model compares an ordered prefix of requests and final counts value by value; that rule requires neither a step-by-step ownership trace nor equal held sets. Its failure comparisons separately require matching held identities | §8.10, §8.12 |
| 16 | A nested update without a scheduler: the lost update happens, 11 in the meaning against 10 on names, and every first-order check passes; the full clause for a bound argument and its continuation, under one finite reading, already refuses the tracker. On an independent check of that reading, across 100 pairs of callbacks, 400 starts and 102,800 observations, the tracker that writes a stale value fails 8 of 40 related cases and the one that reads again passes 40 of 40. No general relation follows | §3.15, read finitely |
| 17 | Local reuse, 44 independently checked cases. When reuse ignores whether the result may be copied, a single use-once result stands at two places and is consumed twice in two events. With the copyability condition, only the ordinary term is reused. The comparison changes this local condition within the rule for running each occurrence (§8.3) | §8.3 |
| 18 | The concurrency core: 504 and 24 configurations, with all 68 schedulers that dropped or doubled a task refused and no right one refused; with a lock the counter ends at 2, without it at 1 or 2; two tasks that each receive first end with both waits in the store, on the two tapes of that program; the twelve tapes of the two controls complete. Tests 1 to 3 were recounted on a second model, which agrees. Test 4, a parked continuation, judged 120 right and 480 wrong correctly and did not establish that step is unchanged | §9.2 to §9.11 |
| 19 | Three ownership ledgers for hold, one of which fails "cell full" after the callback returns; four owner states for settle; 24 cases comparing frames with environments. These finite checks have no independent replay | §9.7, §9.9, §9.12 |
| 20 | By hand, not run: the cases of §20.15 and §4.9, the induction that needs a stronger invariant, and a worked case of a cheapest connector | §20.15, §4.9, §14.9, §20.33 |
| 21 | In the toy's own form, one term was $\mathsf{yes}$ at one sort by a decider, and $\mathsf{unknown}$ at another with the guard `k = n + m` left over | The toy's form of §7.6 |
| 22 | A count over a term as a tree gave 2 where the graph has 1 | §13.2, interning |
| 23 | A cached sum gives 2 on one shared consumer and 1,073,741,824 on thirty levels, where the set has one member. Three answers agree with the set capped at two on 20,000 random shared terms | The old count; §1.21 |
| 24 | Handlers read as functions that pass their state: the same 600 configurations on the generic evaluator, whose bytes were unchanged and which had no special handler case. 120 admitted and right, 480 refused and wrong, over 6,324 completed answer tapes; a recount on a second interpreter agrees. The checked counts are 41,616 reads and 15,216 calls of the choosing rule. The model supplied source rules for the handlers. Untested: general substitution, writes, stores that interact, a callback whose body is not in the term, recursion, failure, fairness, schedules without end | §9.7 |
| 25 | One algorithm licensed and refused. On all 1,100 simple labelled graphs of up to five vertices, the three laws hold of forests at every graph, and of matchings at 173, with 927 refused. With weights, on the 76 graphs of up to four vertices and every weak order of weights with ties, using the test's tier offset two, 9,396 cases: the greedy choice over forests never differs from a least-cost maximal base, and over matchings it gives 3,687 that are not best and 779 that are another best. These were recounted. The larger weighted count on five vertices had its arithmetic reviewed and was not replayed. The objective is least weight among maximal bases, and orders with ties do not cover every positive weight. That exchange holds for the forests of every finite graph is an argument on paper: the licence for the family, its covering evidence and the derivations are not done | §20.33, §20.37, §19.11 |
| 26 | Close as one fixed program: eighteen descriptions, five accepted, thirteen refused, none $\mathsf{unknown}$; the six required refusals each at its own stage; 45 definitions and 352 obligations. A second interpreter agrees on every verdict. The registry and its covering facts are trusted inputs, and its fuel counts do not use the meter in §15.6 | §13.12 |
| 27 | Abduce, then generalise, on polynomials built by zero, inc, shift and mul_x, with parity at 2: induction on the first residual fails at shift; the statement for every `k` passes; the smaller language keeps 25 of 45 schemas and the wider 125 of 882, the target among them; all 927 candidates were recounted. The general lift is not done | §14.9, §20.29 |
| 28 | Look-back: 23,983 terms in a list grammar of up to nine nodes, where every observation of the written term that was tried gives two answers inside all 15 classes of equal terms, and the value's outer constructor gives one; ten rewrites, of which two right ones change the number or order of visits; 243 operations that use an element only as itself, all commuting with the 27 maps of one sort of three members. The first two parts were recounted exactly, and the 243 under a separately chosen reading of the grammar; two larger inventories were not recounted. Separate controls: a family that depends on the element sort fails 68 comparisons across sorts and none inside one sort; seven laws agree in all 763 pure cases; two maps made one, unguarded, disagree in 4,944 of 28,672 mixed cases | §1.36 to §1.39 |


<a id="ch-24"></a>

## 24. Index of open questions and of tests owed

<a id="open-questions"></a>

### 24.1 Open design choices

Each question below is unresolved in its stated scope. `[open]`

**Terms, ownership and observation** · [Constructs](#ch-1) · [Ownership](#ch-21)

- Under what later rule could a sort index do work? Slice 1 compares plain indices. (§§1.3, 7.14)
- If indices run at calls, how many times do they run? (§§1.3, 7.14)
- Who pays for that index work? (§§1.3, 7.14)
- May a bound argument bind zero variables? (§1.4)
- Should multiplicity `none` promise zero calls? (§§1.4, 1.32)
- Should two branch callbacks have a joint profile promising one call between them? (§1.32)
- Should slice 1 admit straight output followed by use of an outside use-once value? The narrower rule admits the eligible helper form. (§1.31)
- Before slice 2’s interfaces are drafted, will the project owner keep the exactly-once mark or split no-copy from no-drop? Slice 1 keeps one mark. (§§1.28–1.29)
- Should the project owner retain explicit handback or allow extraction from a never-runnable continuation? Return if a frozen residue test refuses an eligible positive encoding under the present check, accepts a control with an independently supported wrong account, or needs a new reference-run operation. Also return if real programs commonly fail unexpectedly while holding live values, before drafting a rule allowing a catcher to return after the failed part held a live value, or by slice 2 review at the latest. An unresolved or unrun case alone does not trigger a return. (§§1.24–1.27)
- How may the scheduler continue after task failure while accounting for its queue and outstanding obligations? (§§1.27, 9.13)
- At a possibly failing call, how does compiled code locate live roots and distinguish moved or consumed ones? (§22.2)
- How can construction of the survivor record preserve every live value if memory runs out? (§22.2)
- Which events create, transfer and discharge a declared-one function’s call obligation, from first binding through handoff and call? (§§8.13, 21.7)
- What entitlement may a theory grant a closed operation taking a use-once value? Slice 1 refuses as unsupported any declaration of a closed operation without rules that takes such inputs, bare or nested. An operation goes through its selected interpretation’s image when that image has rules. (§§1.28, 1.46, 21.7)
- What event records giving out a use-once value through a closed operation? (§§1.28, 21.7)
- Which kinds may the later closed-operation interface discard? (§§1.28, 21.7)
- What ownership effects must a closed operation declare? (§§1.28, 21.7)
- Who may name a constructor, given that a rule naming it can end a token? (§§1.28, 21.7)
- How may a closed operation return a use-once value? Revisit with the usage split and host ownership before slice 2 interfaces. (§§1.28, 1.46, 21.7)
- How is explicit quotation written at the call? (§1.34)
- Are an interpretation and a record of the same carrier, operations and laws one object or two related by a claim? (§§1.35, 14.10)
- For the project owner, does declared look-back take syntax alone, syntax plus one ordinary run, or a mode per declaration with both sets of obligations and tests? The designer recommends one run plus syntax as the first step. Only explicit call-site quotation may be relied on meanwhile. (§§1.38, 23.1)
- How are bound variables numbered, and what of a variable's number may an inspector observe? (§§1.36, 22.7)
- Which surface form and reading into nodes should the project owner accept for terms in rules and cases? Slice 1 uses provisional notation. (§§1.64, 14.10, 19.4)
- How are foreign symbols and duplicate display names resolved? (§§1.64, 2.5)

**Manifests, foundations and records** · [Constructs](#ch-1) · [Records](#ch-2) · [Store](#ch-5)

- Which symbol and signature serve the first output operation? (§§1.6, 1.46, 8.9)
- Which resources, target and tool entries does the fixed bound cover, in which manifest, role and acting time? (§§1.46, 3.17, 19.3)
- Which separate depth policy applies to slice 1? (§§10.11, 19.3)
- What fixed allowance and charging protocol pay for literal checking, including identical treatment across hosts? (§§1.46, 7.5)
- What identifies a manifest entry and how is that identity represented? (§§1.50, 2.1)
- Does the first slice's fixed bound admit failure of a build-inserted membership guard? (§§1.51, 7.6, 7.12)
- Is a draw an unresolved pick over a finite seed sort whose law follows by counting seeds? (§§1.54, 4.19)
- What laws govern draws on infinite carriers once real numbers are available? (§4.19)
- What distortion theory propagates error, separates enclosure from width and covers empty names and one-sided answers? (§§3.14, 4.19)
- What form of width bound accounts for the input widths, values, domains and direction on related names? (§§3.14, 4.19)
- Should a fixed checker take rule forms as data or should each theory have its own checker? (§1.61)
- Which mathematics should enter by default, in full or grown from finite checks? (§§1.61, 14.10)
- Is Home predicative, and what predicativity does each candidate default declare? (§§1.61–1.62)
- Which conversion procedure should the framework use, with termination and confluence obligations, bounded unknown or explicit certificates? (§1.63)
- Which core grammar can the evidence reader use for the middle assumption rows? (§§4.11–4.12)
- Which definitions are unfolded, by what terminating procedure and with what bound? (§4.12)
- Which evidence does each assumption row require? (§4.12)
- Which program or derivation turns a finite run answering no into a proof in the theory? (§4.12)
- Which fields record a sort's literal check? (§§2.4, 7.5)
- Which fields record an operation's conditions? (§§2.4, 7.8)
- Which fields record the manifest variable of a bound parameter? (§§1.46, 2.4)
- Which content determines theory identity for the project owner, including the order of declarations? (§2.5)
- Which theory, declared-symbol and claim-site identities carry across versions or rebuilds? (§§2.5, 14.10, 19.8)
- Which canonical bytes and profiles identify store content and dependencies? (§§2.3, 2.5, 5.1)
- Which bytes represent a recursive group with references by position? (§2.7)
- How can a theory and its declared symbols receive identities without circular dependency? (§2.5)
- At the first family client, should the kernel store an application or check a fully substituted closed declaration? (§§1.3, 2.2, 2.6)
- Once slice 4 can carry and check derivations of claims quantified over sorts, what rule should be proposed for them? (§§1.3, 2.2)
- For the project owner, who may add store items beyond terms, proposals and notes? (§5.1)
- What authenticates a run record's binding to the build it names? (§§4.1, 5.1)
- Before design close, should the project owner keep abduction ranking or exclude candidates unrelated to an open goal? (§§5.6, 20.29)
- Should induction keep every valid implication or require a classifier that covers all positive instances? (§§5.7–5.8)
- Which fields encode the five stage records? (§§2.1, 6.1, 6.4)
- How will source-to-graph correspondence be checked after slice 1? (§§13.3, 14.10)

**Tracking, admission and execution** · [Tracking](#ch-3) · [Admission](#ch-7) · [Reference run](#ch-8) · [Concurrency](#ch-9)

- Can acyclic witness dependencies license mixed tracking directions on a stated scope, given the correlated-start counterexample? (§§3.4, 14.2, 14.10)
- Which slice 4 footprint records what each operation consumes, retains and creates? (§§3.9, 23.1)
- Which separation and update clause prevents two distinguishable live cells sharing a machine slot? (§21.2)
- How can capture of use-once state be derived across all perform sites, aliases, frames and activations? (§§3.10–3.13, 23.1)
- When may a known-rule check specialized to one call be cached? (§3.12)
- How does that check relate to the declared-one boundary? (§§1.16, 3.12)
- Which whole-operation relation covers captured state, repeated or omitted resumptions, effects, use and failure? (§§3.15, 14.4)
- When may a realiser stop for a resource while the meaning continues, beyond the first-build permissions? (§§3.17, 8.12)
- Which well-founded measure justifies unilateral steps in the client comparison and, in the backward form, falls during the search for a predecessor? (§§3.18, 14.3)
- What makes divergence of the client’s run on names correspond exactly to divergence on values, subject to the resource clause? (§§3.18, 14.4)
- What is the reference outcome and manifest entry when admission refuses an evaluated result? (§§7.7, 8.8)
- What is the reference outcome and manifest entry when the literal check on an evaluated result exhausts its allowance? (§§7.5, 7.7, 8.8)
- Which extra runtime membership tests should the project owner allow, on which sorts and with what index access, use-once handling and charges? Proposed review with the ordinary-parameter rule at the end of the slice 1 contract review or upon an earlier first-build refusal solely for lack of a test. (§§7.6, 7.12–7.14)
- Which name relation licenses moving or omitting a sequence-making computation? (§§8.6, 21.8)
- What are the exact request and reply records at the host boundary? (§§3.16, 8.8–8.9)
- How is the instantiated result sort, including substituted indices, encoded at that boundary? (§8.9)
- What identifies the request and its logical activation? (§8.9)
- How does the host complete or end an outstanding request? (§§3.16, 8.9–8.10)
- Which continuation interface commits one admitted reply before resumption? (§8.9)
- What records a reply’s endpoint, version, state and manifest? (§§8.9–8.10, 18.1)
- Which host theory and system-call model cover remaining interactions and uncaught failure? (§§3.16, 8.9, 10.3)
- How does the host name incoming use-once values for reference/compiled comparison? (§§1.46, 8.9, 21.6)
- What ownership interface covers use-once inputs, results, held failure state and transfers at the host boundary? (§§1.46, 3.16, 8.9)
- What tariffs and protocol charge requests, reply admission and resumption? (§8.9)
- What outcome follows an unpaid precommit charge or failed preparation while the host owns the reply? (§8.9)
- Which first exported interfaces supply fixed or caller-selected work and construction allowances, what finite defaults do they publish, and how does the host supply required values? (§§3.19, 8.8–8.9, 15.6)
- Does an elapsed-time policy apply? (§§8.9, 15.9)
- Which refusals require a record and which need only a diagnostic? (§§8.8, 10.4)
- Which report fields and bytes identify subject, phase, enclosing run, location and reason? (§§8.8, 10.4)
- Which fields and bytes bind a resource stop to its permission, run and reference comparison? (§§3.17, 8.10–8.12)
- Which runtime entry interface separates nested pattern inspection from committed destructuring at the selected activation? (§§8.13–8.14)
- Which maker provenance and lowered-event mapping distinguish equal-payload productions across sites and iterations? (§§8.13, 21.8)
- When the frozen-census result note has its review, and before the use-once rules, stored function signature or admission are fixed, should the project owner allow constructors with a bound parameter in slice 1? (§§9.2–9.3, 19.4–19.5)
- Can scope- and activation-preserving substitution replace explicit handler frames? (§§8.8, 9.7, 9.14)
- What calling convention does a separately compiled callback use if it can return pending work? (§9.7)
- Where does a handler clause's own request for the same operation go? (§9.7)
- What use-once permit enforces returning a value to its original cell despite intervening gives? (§§9.8–9.9, 22.3)
- What protocol grammar and indexed family of message kinds and bodies describe a channel? (§§9.10, 22.3)
- How does a link bind its protocol to its hidden endpoints? (§§9.10, 22.3)
- What equations define dual protocols? (§§9.10, 22.3)
- Which membership checks on the index enforce message order and closing? (§§9.10, 22.3)
- What does a certificate of progress establish, and under which scheduling or fairness assumptions? (§§9.11, 22.3)
- How should a wait-capable owner return its entire final carrier, including obligations held by a free cell? (§§9.12, 22.3)
- What links absence of waits in every relevant whole outcome to a clear return by this owner? (§§9.12, 22.3)
- Which pure, total settlement probe hands back the whole carrier even on failure, with what claim about its answer? (§§7.8, 9.12)
- What identifies each fresh run of a job that looks at a held-out set? (§§9.14–9.15)
- How does a result bind to every look behind it, including repeated looks by one job? (§9.15)
- How does the host interface encode failure payloads, including retained and omitted arguments? (§§3.16, 10.3)
- Does each runtime parameter borrow or own its handle? (§10.9)
- Does one theorem cover both kinds of two-run claim, every pair and each by some? It is deferred. (§§3.21, 3.3)

**Compilation, proof and the evaluator** · [Plain compilation](#ch-10) · [First-call builds](#ch-12) · [Proof](#ch-14) · [Evaluator](#ch-15) · [Trail](#ch-18)

- Which C compiler, version, settings, output maps and checked linker transformations qualify the generated-C route? (§§10.6–10.8, 19.2–19.3)
- If C fails qualification, slice 2 runtime builds cost too much or slice 5 plans the second target, which backend should the project owner qualify, given the long-term route of §0.3? That route's producer choice is also revisited if a restricted existing backend meets the same contract at lower total cost, or if the checker or runtime boundary cannot be kept reviewable. (§§0.3, 10.7, 19.3)
- Which explicit machine, loader, ABI, runtime and resource contracts, and which checker, does the long-term route's per-build validation use, first for x86-64? (§§0.3, 10.5, 10.6, 10.7) `[proposed]`
- What reservation and manifest/bound entries cover root entry, prologues, guards, helpers and emergency cleanup? (§§3.17, 4.14, 10.11)
- Who owns generated executable storage and when can it be freed, including when indirect entry is possible? (§§12.2, 22.6)
- Which stop rule applies to first-call build failure, the resource-stop comparison or a separate rule? (§§3.17, 8.12, 12.4, 22.6)
- How does a failed first-call build bind the attempt to the whole stopped run’s held account? (§12.4)
- Which fields and bytes encode the failed first-call attempt? (§12.4)
- Which lock fields describe the fixed first-call build? (§12.4)
- What contract must the first-call loader meet? (§12.4)
- Should fixed build slots take unit jobs by the loss each avoids? The proposal’s two sources could not be checked. (§22.6)
- When the trusted texts are written, is Close counted with the case split, in slice 2, or as an eighth text? (§§13.2, 13.12)
- Which concrete bytes name a starting state in a run record and in Eval? (§§13.7, 17.2–17.3)
- How does an externally written evaluator value map to its interned node? (§15.2)
- What is the byte form of a choice name, alternative count and case number? (§16.2)
- Before either design or implementation closes, should the project owner let `else` cover subjects outside the declared choice? (§16.3)
- What invalid ranges does byte slicing recognize, given its specified `none` edge result? (§§15.8, 16.6)
- How is the byte slice with a start and length spelled? (§15.8)
- Which arguments and costs make up the full meter entry for byte slicing? (§15.8)
- What is the meter entry for byte length? (§15.8)
- The construction unit is the logical cell counted in §15.11. `[decided]` Should the proposed work unit, a table unit of reference work, be adopted? Which paired price rows, counting passes and administrative storage bounds should be adopted for the candidate fragment and the operations beyond it? What bounded evidence of a construction shortfall must a work-refusal record retain when the cheap check leaves the shortfall unknown? Should a later profile refund construction credit when a value dies? (§§15.6, 15.11–15.14)
- Leave for later the optional third limit on live logical storage, including values and stack frames. `[decided]` A design for this option would need an agreed set of roots and a release point, a frame size fixed by the reference, live counts of distinct cells across sharing and retained memo or trail roots, which take time and storage to keep, a third grant and deficit, and, for any claim about machine memory, a qualified conversion and bounds on runtime overhead. (§§15.11, 15.12, 15.13, 15.14) `[proposed]`
- Which natural- and byte-primitive entries complete the common meter? (§§15.6, 17.5)
- What should both builds charge for a loop turn, and in the paired profile, which work invoice and safe advance bound apply to a turn that supplies its index to the body? (§§15.4, 15.6, 15.11)
- Which run-record bytes bind the complete canonical, hash and meter descriptor independently of the executing build? (§§15.9, 17.3)
- Should the proposed SHA3-256 byte profile be adopted? (§15.8)
- What thresholds on the stated workload would reopen the hash choice? (§15.8)
- Should recursion on a component or smaller natural replace the default counted loop given a bound or the nodes? (§§14.10, 15.10)
- When does a client justify introducing a built-in set? (§§16.1, 16.5)
- How should the meter charge set construction? (§§16.5, 17.5)
- Which proposed charges should both builds use for set comparison? (§§16.7, 17.5)
- Which normalization, identity, hash and profile premises reproduce sequence names from equal starts? (§17.2)
- What framing, admission and replay rules govern imported names, saved states and run records across profiles? (§§17.2–17.3)
- If both roles agree to distinct names, which names identify the tuple and sequence reads? (§§17.3–17.6)
- Should a sequence write have another name than `set`, and if so, which? (§17.6)
- What final transitive state-freedom check qualifies a definition for memoization or use in admission? (§§7.7, 17.3)
- Which meter entries for writes and `contents` need replacing to remove last-place state? (§§17.4–17.5)
- When a sketch or program shows a need for direct ordered multiargument memoization, which key identity and arity fee apply? One explicit tuple remains one argument. (§§15.7, 17.3)
- What complete later profile would support zero-argument memoization? (§15.7)
- How are memo entries installed and handled on interruption, warming, resumption and restoration, under the chosen key and charging rules? (§§15.7, 17.3, 18.2)
- Which trail and final-account projections give run agreement, scheduler outcomes and endpoint observations? (§§8.9–8.10, 9.6, 18.1, 20.7)
- When a measured search or handler needs to undo sequence writes, what should a kept point restore, and how should the continuation agree with a fresh run? (§18.2)
- At that reopening, how should restoring reachable positions account for write order, fuel and partial restoration? (§18.3)
- If others may change reachable positions before restoration finishes, which protocol preserves the observations of those intervening accesses? (§18.3)

**Slices, exploration and remaining interfaces** · [Slices](#ch-19) · [Explorer and optimizer](#ch-20) · [Further proposals](#ch-22)

- In which slice should the check cache be introduced? (§§5.2, 19.4)
- How does finite-data consistency checking cover every producible constructor value at admitted indices and arguments, with what evidence, fuel and unknown outcomes? (§19.5)
- What corpus, coverage and allowance for incomplete comparisons qualify the slice 1 source and compiled controls? (§§19.6–19.7)
- Where should the project owner place the SRE later? The current slice order stands, early construction is ruled out and finite cases may inform interfaces. (§§14.10, 19.13)
- Before any SRE building starts, which externally checkable result should the project owner choose for each stage, including the proposed first-stage counting demonstration? (§19.13)
- When the first SRE stage’s requirements are written, do integers suffice for its exact arithmetic, or must a rational model come with it? (§20.9)
- Which claim establishes coarseness for the named questions beyond tracker soundness? (§§20.10, 20.12–20.15)
- Does a greatest closed family exist for an operation taking two hidden arguments? (§20.15)
- Does a greatest closed family exist for multivalued operations when one result name’s answers must share a witness? (§20.15)
- Before the uses result is fixed as trusted text, should it identify the constructor arguments each matching rule uses? (§§5.4, 19.9, 20.12)
- How do reports certify completion at one question and scope across conflicts, distinct witnesses and disjoint assumptions? (§§4.2, 20.17)
- What aim should the optimizer pursue within the runs the program allows? (§20.31)
- At the first client seeking an answer-changing build option, should it be declined or offered as a separate opt-in meaning? (§§11.2, 20.31)
- Must transformations preserve the reference meter’s fuel-bounded verdict across builds? (§20.32)
- What identifies a handwritten search as the named operation before separately licensing its interpretation and replacement? (§§20.38, 22.1)
- How should the four substitution routes distinguish scope, time of settlement and kind of evidence? (§§20.35, 22.1)
- Which of the seven proposed records should form the shared search and substitution interface? (§22.1)
- How far is each conservative restriction on result reuse necessary for proving a law by identity of node? (§§8.4, 14.8, 21.1)
- How is a core let recorded? (§§2.1, 21.3–21.4)
- What admission contract checks a core let, including a use-once initializer? (§§21.3–21.5)
- Which inlining contract preserves evaluation order, logical activation and contextual bound-argument signatures when introducing or removing a let? (§§8.3, 8.6, 21.3–21.5)
- What is the core let’s written form? (§21.4)
- What does executing a core let cost? (§21.4)
- Which view specifies what an observer may learn, including whether secret input affects public output? The case for five facets rests on it. (§§22.8, 1.59)
- Which view describes what a computation needs from its context? (§22.8)
- Can a reference to a store's cell leave that store? (§22.8)

<a id="tests-owed"></a>

### 24.2 Tests owed

Controls on one line belong to the same trial. Later trials carry their triggers.

**Terms, use and look-back** · [Constructs](#ch-1) · [Ownership](#ch-21)

- Check the general declared-residue translation across callers that finish, hand on or add what they owe. Refuse forwarded failure that gives the success callback no site. (§§1.25–1.26)
- Resolve the two outstanding callback probes under declared-residue recovery. (§1.26)
- Measure unplanned failures in real programs holding live values they cannot discard. (§§1.25–1.26)
- For the deferred extraction design, retry a failed parser on its current input. Account for taken and residual duties in an eligible never-runnable continuation. Exclude functions and unnameable sorts. Refuse taking from an answer-taking continuation and then running it. (§1.27)
- Before building the mark split, check captures, functions passed as values, declarations and the new use census. Include resumption counts, a droppable datum enclosing a no-drop field and the no-drop duty of a task. (§§1.28–1.29)
- Generate straight and helper-mediated output with a waiting use-once value. Require the narrower rule’s straight-form refusal. Compare actual use in the admitted fixture, including the held value without a committed reply. (§§1.31, 19.6)
- Compare the full-language use check with actual consumption, including a use-once data field, effects and one use per branch. Count refused right terms. (§§1.32, 14.10)
- Repeat that census with multiplicity `none`. Require zero wrong acceptances and count the right terms recovered. (§1.32)
- Repeat it with joint branch-call profiles, again requiring zero wrong acceptances and counting the right terms recovered. (§1.32)
- In slice 2 write one monoid as an interpretation and as a carrier/operations/laws record. Seek a distinguishing client. (§§1.35, 14.10)
- Exercise construction, extraction and call of a constructor-held one-function, repeated handoff, a checked known-rule any-parameter used once, and applied or returned functions. Distinguish new obligations from transfers and preserve narrow-slice refusals. (§21.7)
- For each marked invisible look-back law, compare full runs on every small term. The simple licence must refuse a false law, an effectful function, fused maps failing with different payloads, a position-sensitive resolver, an omitted element whose function fails or diverges, stranded ownership, merged fresh use-once results, a value held at only one failure and evidence invalid at the new site. Record law, scope, sites, interpretation and expected refusal. (§§1.37, 23.1)
- Against the written, accepted declared-look-back rule, test a variable operand and beta contraction changing the observed syntax. (§§1.38, 23.1)
- Test an effectful operand against that rule, checking capture order against effect elaboration and ordinary evaluation. (§§1.38, 23.1)
- Require refusal when the declared callee is handed on as a function. (§§1.38, 23.1)
- Require the same answer on the fixed graph from a runtime-built part. All four tests must pass against the accepted rule to restore decided standing. (§§1.38, 12.2, 23.1)
- In the proposed paper comparison, predict all four trials under each candidate, including explicit quotation. Add an operand making a fresh use-once value and account for whether it runs and who owns the result. (§1.38)
- Census rule-defined operations across different element sorts, following all helpers, then prove read-off commutation for these rules. Until then, name the syntactic decider. (§§1.39, 23.1)
- Test exchanging an unresolved pick with an independent step under set-of-outcomes semantics, one resumption and unchanged handler/resolver scope. Include duplicate resumption and a resolver crossing. (§1.53)
- For the finite-seed account, refuse a fair coin matched to a constant and accept the coin against its negation with a matching of seeds. (§§1.54, 4.19)

**Manifests, evidence and representation proofs** · [Claims](#ch-4) · [Trusted base](#ch-13) · [Proof](#ch-14)

- For a proposed guarantee from samples or randomized checks, demonstrate that exact checking is unaffordable on the job and derive its bound before building. Until then record only a note. (§§4.17–4.19, 14.10)
- Test a bound that distinguishes the same write in a build-time check and in a guard during a run. (§§1.45–1.46, 23.1)
- Test the record shapes together on a slice 1 program, covering reference state, return, failure, wait, fuel cut and compiled resource stop. (§§2.1, 8.8)
- On the paired profile compare exact and one-short work and construction, both short, nonexchangeable surplus, exact versus reserved natural width, shared fields and repeated intern hits. Check memo and trail retention, a cut on either side of publication, state and held values, controlled host-memory and stack stops, and the separate scalar milestone B records. Include an affordable work invoice with zero construction credit and compare work refusals for add(1,0) and add(1,1) with one construction cell left. Qualify each new primitive's safe price calculation and nonzero temporary workspace, covering the first unpaid event and separately a refusal before entry. (§§3.19, 8.8–8.12, 15.3–15.14, 18.1 and 19.2)
- At the first reusable-declaration client compare a kernel family application with a checked concrete expansion across modules. Account for inspection, checking and sharing, and preserve identical application identity and the complete substituted declaration and obligations. (§§1.3, 2.2, 2.6)
- Add contrary evidence. Replay the former build, retain both manifests, report conflict in the new reading and withhold the licence. (§4.2)
- For values under one name with no common right answer, bind the refutation to one representation and naming relation, one value scope, the interpreted question and its full set of admissible answers, including width where relevant. (§§4.7–4.9)
- Test the machine-model guard rule on a guard and its evidence, including transitive assumptions and the marked theory’s laws. (§4.13)
- In slice 4 check folded and unfolded forms, a hidden quantifier, recursion reaching the unfolding bound and two evidence routes taking different rows for one statement. (§§4.11–4.12, 23.1)
- Remove a guard in slice 4 with a theorem using a classical law and give a derivation of what that use assumes. (§§4.12, 14.10, 19.10)
- Before designing slice 4 trials, state each default’s predicativity. In the translation trial count failures due solely to it. (§§1.61–1.62)
- For each candidate foundation, establish checker soundness or record the assumption. (§1.62)
- Translate 1,000 Lean declarations covering every feature. Count and explain failures by feature as a feasibility measure. (§1.62)
- Write one chapter of mathematics outside matrices in both foundational shapes. (§1.62)
- To claim Lean’s inclusion in Home, prove translation of all guest statements and derivations and agreement of conversion over the asserted domain. (§§1.62–1.63)
- Before drafting slice 4 interfaces, and in any case before the derivation checker enters the trusted base, hash all trusted checker text, including rule application and side checks. Supply Home then Lean as data, compare hashes and explain changes. Establish faithful encodings, actual side checks and absence of hidden axioms. Record all added trusted dependencies. (§§1.61–1.63)
- At that return, account for the termination and confluence the rewriting procedure relies on. A bounded procedure may answer unknown. Measure explicit conversion certificates after sharing. (§1.63)
- Change one declaration in slice 2 and count claims requiring resettlement. (§§2.5, 14.10)
- On the unrun cache example, add a second applicable default and check invalidation wherever uniqueness was read, including a recorded absence. (§§1.42, 5.2)
- At matched budgets compare ranking and exclusion on the 56 candidates. Count missed hypotheses, surviving laws’ ranks and work to reach them, the smallest generating set, and kept sets restricted to conclusions from the unknown-claims query. (§§5.6–5.8, 20.29, 23.1)
- Test the last-use footprint record for consumed, retained and newly produced state, including an operation leaving an empty configuration. (§§3.9, 23.1)
- Give the obligation generator the two-cell tracker that puts both live cells in one slot and reads back the wrong value. Require refusal. (§21.2)
- Establish general capture for store continuations and check the call-specialized rule, its cache and the lowering against reference use. Keep the scope-only restriction as fallback outside the checked domain. (§§3.11–3.13, 23.1)
- Prove composition first on finite single-form systems with one hidden sort. Check random realisers of realisers against the original meaning. Wider claims require identical middle theory, agreement at intermediate observations, no added failures and well-founded measures composed inner first. (§§14.2–14.3, 14.10)
- Prove client transport outside the covered first-order finite Close instances, including any needed bridge to an infinite meaning. Search random small terms targeting one name used twice, two hidden arguments, a branch before a hidden step and a shared node. (§§13.10–13.12, 14.4, 14.10)
- For higher-order transport, local state, effects and nontermination, extend that search to a handler resuming twice or never, an exhausted realiser, a loop and a run without end. Exercise unilateral steps, resource stops and the whole-run relation. (§§3.15–3.18, 14.4, 14.10)
- Test the third bound-argument route on its pure, total, deterministic, unindexed, copyable and droppable fragment. Its certificate covers application, actual binder translation through I/K/S at each used sort, primitives and exported trackers. The particular trial remains unspecified. (§§14.6, 23.1)
- Extend Close beyond its six finite refusal controls to arbitrary descriptions, covers without end with a bridge, failures as outcomes and a second build. (§§13.10–13.12, 23.2)
- In two weeks implement a mutable hash map as a holding of a finite map. Count evidence lines per tracker line. Above about ten to one without a route to automation, keep holdings as named manifest entries. (§14.10)
- Test the three entries of §13.13 on a strict build: a wider promise re-exported by a wrapper, the named reader, and the unsettled tracking of the lowering and the backend. No acceptance may reach a strict build. (§13.13)
- Prove for the language that a checked access restriction gives the two-run argument once, for every provider that keeps the restriction. (§§3.20, 14.4)
- At the first real import, bring one case the strict profile must accept and one it must reject; the profile's full set of trusted readers, checkers and services is chosen with them. (§13.13)
- At the first proposed use of directional progress, bring one uniform-saving positive case and the hidden-selective and host-publication negative cases, all at the same stated limit; if unresolved, keep the plain path. (§3.19)

**Admission, execution and compilation** · [Admission](#ch-7) · [Reference run](#ch-8) · [Plain compilation](#ch-10) · [Slices](#ch-19)

- Test how a value of a data sort crosses the evaluator boundary. Its values are constructor terms. (§7.5)
- For an index bound and a purity condition, check one test per call, one run per argument, site evidence for removal and refusal to assume a machine bound. (§§7.8–7.9, 23.1)
- Write a pure braid and an index bound as signature conditions and predicate sorts. Count records touched and test each form on one condition over two parameters. (§7.10)
- At either proposed review trigger, count first-build refusals solely for lack of a membership test. Bring both written test contracts, for literal checking and comparison with a finite collection. (§7.13)
- Compare occurrences and activations value by value on the full language, general handlers, sort indices and lowering. (§§8.3, 23.1)
- Check nested patterns with a first rejection followed by a match, a catch-all and no match. Consume only at committed destructuring. (§8.13)
- Independently validate acts against reports for the exact watch, entries, lowering and subject. Try two acts reported once, an omitted report and a report without an act. Refuse drop, double use, swapped production order and altered failure holdings. (§8.14)
- Check maker correspondence across two sites, a revisited site and equal starts. Swap equal-payload productions of one constructor, preserving destinations and activations, against a correct control. (§21.8)
- Census and review full-language ownership with functions in data, by context, before fixing the use check, stored signature and legal call positions. (§§9.2–9.3, 19.5, 23.1)
- Check scope and activation before removing handler frames or retaining `step` unchanged. Cover continuation application, successor state, completion without a request, external callbacks, ambient/interacting stores, writes, recursion, nested same-operation handlers, failure, fairness and infinite schedules. (§§9.7, 9.14, 23.2)
- Check scheduler use, whole outcomes and each progress claim separately, with soundness, scope, covers and scheduling assumptions. Include retained waits, returning runs and bounded service under the named resolver. (§§9.11–9.14)
- Check channel transfer of a use-once payload beyond the finite ordinary-message cases. (§9.10)
- Test the byte encoding of the failure payload, including reconstruction of retained argument positions and exclusion of live or nested use-once payloads. (§10.3)
- Qualify a clean C stack stop from before root entry through prologues, guards, enabled helpers and emergency cleanup. Uncontrolled overflow cannot witness it. (§§3.17, 10.11)
- For the proposed first-call example, emit on first call, decode and check before entry, name the build in the run record and compare both the runtime-built and wholly ahead-of-time programs separately to the reference. (§§12.4, 19.8)
- On failed first-call build bind part, call, reached step and reason to all held use-once values, including caller state. Preserve earlier requests and ownership with no entry, transfer or further request. Bind the stop to its comparison whatever the resource classification. (§12.4)
- Test an ahead-of-time build with its ability to publish code removed. (§§12.1, 22.6)
- If the optional slice 5 runtime-planning passage is taken, plan and emit one part during a run, decode and check before entry, compare each build to the reference and replay choices without searching. Build all other parts ahead of time. (§§12.5, 19.11)
- On the slice 1 corpus compare both evaluator builds, compiled with reference runs, and source use checks with actual consumption. Include justified positive, negative and refused-right source controls, wrong lowerings, returns, failures, waits, fuel cuts and resource stops. Count generated, admitted, refused and compared cases. Explain incompleteness. (§§19.2, 19.6–19.7)
- At full slice 1 comparison and replay, check observations, requests, ownership evidence and named lowering and backend. Keep the plain path runnable, visible choices distinct from plans and reference charges separate from physical cost. The root manifest separately names the reader. (§§19.2, 19.4)
- At the first law refusal, compare a mandatory condition with an optional representation using candidates satisfying A alone and B alone. Require the refusal explanation to account for their conjunction. (§19.8)
- At the first forward-tracking comparison use a score-only caller and a helper serializing the name. Identify the disqualifying observation and account for effects of field production. (§19.9)
- For slice 5 algorithm replacement, supply the theorem and covering evidence or derivations for the claimed family. Licence it at one interpretation and refuse it on a failed law at another. The finite forest/matching results cover their named graph domains. (§§19.11, 20.33, 20.37, 23.2)
- At the full optional planner’s first slice 5 workload with a handwritten route, compare that route with boundary counting at equal allowance. Check separator, coverage, bijection and table cost. Include unsupported questions, wrong separators, exhausted budget and refusal costs. (§19.11)
- On ten small numerical kernels measure planning time, guards left and runtime against the plain path. (§14.10)
- Try a coarsest-representation search on graphs of five vertices. (§14.10)
- For one stated term check invariance of its meaning manifest across representations, plans and guard removals. (§14.10)
- Compare the best plan found under one budget with three representations and with one. Require geometric-mean gain ≥1.2 and record exhaustive selections. (§14.10)
- Measure checking cost below 10× and annotation cost below 2× those of a conventional typed language. (§14.10)
- Port 2,000 lines of ordinary higher-order code. Count annotations under the candidate surface syntax. (§§1.64, 14.10)
- Run `square(work(x))` through a rule step and count runs of `work`. (§§1.5, 21.3–21.4)
- Check a let whose body uses an outer use-once value and require refusal of its applied-binder counterpart under the narrower rule. (§§21.3–21.5)
- Census a let with a use-once initializer under the enclosing scope's one-site rule, including moving it to the variable and handing on the result. (§21.5)
- Exhaust the small terms comparing identity of node with equality of the results of two independent runs. (§§8.4, 14.8, 21.1)
- Measure the first-order command-tag scheduler with explicit task state and its separate proof obligation. (§§9.4, 22.3)

**Evaluator, exploration and research trials** · [Evaluator](#ch-15) · [Values](#ch-16) · [Sequences](#ch-17) · [Explorer and optimizer](#ch-20)

- Write trusted graph walks in both recursion forms. Measure against direct builds with the project owner’s reported replay measurements as the reference. (§§13.5, 14.10, 15.10)
- Bring a checker or parser with mixed inputs and compare `none` on an outside subject with letting `else` accept it. (§16.3)
- Qualify the 32-byte SHA3-256 implementation and byte profile across both builds, including inputs, results and metering. Compare speed with BLAKE3 and SHA-512/256 on the stated workload against the thresholds for reconsideration. (§§15.6, 15.8)
- Before adopting sets as a value kind, bring the first slice 1 definition needing one to the project owner. If none does, ask whether sets should wait for such a need. (§§16.1, 16.5–16.7)
- When designing slice 2’s first search or handler, bring the real program to the project owner. Does anything in this build need sequences, and what rework would waiting cost? (§§17.1, 19.3)
- Before freezing sequence builds, check positional reads against logged demand, a sparse reader, a whole-copy consumer and a stale copy. (§17.6)
- When an extension first supplies evidence to an existing consumer, check a lower bound for an exact request and an exact certificate for the wrong revision at the actual use site. (§20.5)
- On the committed constant-zero box answering 0 then 1 and on one stateful box, exercise the checked, trusted and assumed routes. Replay replies and record what each route refuses or assumes. (§§20.7, 20.30)
- At the first finite SRE stage, check a nonzero minor over the declared field for the named probes, scope and endpoint assumptions. Check the vector trackers independently and supply an attaining state before claiming a minimum. (§20.9)
- At the first SRE stage chosen, run the proposed graph-colouring count and boundary-gluing study on ten parameters on small graphs. Record census, rank, budgets, sizes and interpretable algebras. Check the minor, seek addition–contraction and a witness against count-only closure, and check an equality gadget’s readout. (§19.13)
- If pursued after the compiler is nearly finished and the SRE-based optimizer is partly built, measure whether fewer structure constants reduce storage cost. (§19.13)
- On covered finite slice 3 cases, check total-weight names with distinct equal-weight items, append, total and last-item questions. Try a pair’s sum under swap and increment, then double one component to refute the summary. Wider claims require evidence. (§20.12)
- Before fixing the slice 3 sheet and coarsest query, run the experiment-table census with and without operations. Check whether an answer-only summary is reported as a finding and whether the report must refuse it. (§§20.14, 20.27)
- At the first reusable domain using the claim-status reading of §4.2, test inconsistent answers, distinct existential witnesses and disjoint assumptions. Distinguish conflict, spent budget and certified completion. (§20.17)
- At the first SRE question-finding stage compare invariant kernels on one census. Check both separating directions and any synthesized finer-to-coarser map. (§20.20)
- Test held-out access through a use-once value of a hidden sort and the named protocol. A permitted second look receives a new value. Beyond observed inputs the theorem must cover the actual access path. (§20.21)
- When an authorized later research client first uses an exact classification, check both maps and a client operation against the equal-cardinality control. (§20.22)
- At the first learned-policy comparison record warranted findings on fresh searches under one allowance. (§20.22)
- When a SkeinLab method first combines advice from several views, compare evidence for each contribution with shared-source advice under equal disclosure. (§20.22)
- At the first disagreement-selected probe, name the outcome that would change the explanation. Compare the probe with a budget-matched control under the same disclosure and lineage conditions. (§20.22)
- In the next SkeinLab investigation commissioned by the project owner, use the four-city example to check the tour switch and tie. Move the penalty at fixed mean error and rotate geometry under fixed axes. Compare one-tour and exhaustive budgets and record the resolver at equal cost. (§§20.23–20.24)
- At the first checked cross-version correction, name both versions, transport and evidence. At the first concrete precision client test overlapping removals and correction under a change of coordinates. (§20.26)
- For every system of ≤4 values with one or two operations of one hidden argument and one question with a set of right answers for each value, find the fewest names over closed partitions and over closed covers, and the greatest closed family. Repeat with one binary hidden operation. Compare every cover’s name-runs with allowed outcomes, using hand-found representations as controls. (§20.27)
- At the first conditional rewrite using an observation algebra, compare selecting 0 before requiring 1 with filtering {0,1} first. Check which witness remains available. (§20.34)
- At the first transfer of unfinished work between methods, check disjointness, coverage and reconstruction against both wrong residuals. Compare transfer plus checking with restart. Test use of the exact replacement at the slice 5 interfaces and require a checked coverage reason for later branch removal. (§§20.35–20.36)
