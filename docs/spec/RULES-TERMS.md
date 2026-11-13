# Terms and theories rules, revision 2, part 1

INFERENCE — DRAFT. Twelve rules, TERM-001 to TERM-012. They transcribe five passages of design text R13: D-TH-1, D-TH-2, D-TH-3, D-TH-4 and D-TH-6. Nothing here is reviewed, adopted or approved. PROPOSED — TERM-003 alone carries the marked provisional I-A restriction beside TG-011; all other rules choose nothing R13 leaves open. [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A] Part 2 (D-TH-5 and D-TH-7) is a later card.

SOURCE — R13 is `DESIGN-TEXT-R13.md`, SHA-256 `20c980f9bdeefe1e84320c50f444bb75ef18f2b96f2b7eadb6c5dd29722444ce`. Each rule's "from" names an R13 anchor. A line number beside an anchor is a physical line of that file and is a locator only. R13's own tag for the words is kept beside each rule. R13 itself waits on an independent review.

SOURCE — The form of a rule follows `HOW-WE-SPECIFY.md` lines 54 to 80: one obligation in each rule; kind; subject; from; text; case; excludes. Standing is `draft` for every rule here. No passage in scope carries a working or waiting tag on a sentence that a rule states. The one sentence that goes to test (a third multiplicity) has no rule. It is gap TG-003.

SOURCE / INFERENCE — Committed rules are cited and not repeated. REC-001 holds the node shape of a binder and its count. REC-002 to REC-004 hold variable numbering, environments and the binding checks. No committed rule was found that states what a theory, a law, a multiplicity or an effect is. `REPORT.md` says how far that search went.

PROPOSED — Cases use small invented symbols such as `vector`, `twice`, `out` and `assoc`. They are examples for a reader. They are not Loom syntax and add no vocabulary. The surface syntax is open in R13 (D-SYN-1).

SOURCE — Slice 1 has no quotation form. [register: `2026-11-12-CODEX-F-REGISTER-EDIT-7-HOST-LANGUAGE\DECISIONS.postimage.md` (SHA-256 `6ed970ec3dfcefe083c2c99521595e887ff1fb9473a9cff932f1b47e12128383`), row 48; recorded there as Claude Arch's own call with S-A.]

## TERM-001 — A theory is a vocabulary of four kinds of member

- revision: 1
- standing: draft
- kind: definition
- subject: a theory
- from: SOURCE R13 D-TH-1 (line 91), first sentence. R13 tag: `D L15, L23 | kept`.
- text: A theory is a vocabulary. Its members are sorts, operations, laws and rules.
- case: A theory of counters has the sort `counter`, the operation `next`, the law that `next` never gives its argument back, and the rule `next(n) = n + 1`. Each of the four is a member of that theory.
- excludes: Reading a theory as a set of values, so that the sort is the theory and the operation, law and rule are outside it.
- gaps: TG-002 (theory identity); TG-005 (whether constructors count among a theory's operation members); TG-008 (using another theory's symbols); TG-012 (declaration order and duplicate names).

## TERM-002 — The same construct serves every subject matter

- revision: 1
- standing: draft
- kind: definition
- subject: a theory
- from: SOURCE R13 D-TH-1 (line 91), second sentence. R13 tag: `D L15, L23 | kept`.
- text: The integers, a mutable store, a logic, an instruction set and a file format are all theories.
- case: An instruction set is given as a theory: its sorts, its operations, its laws and its rules. Nothing else is needed to state it.
- excludes: Giving an instruction set or a file format a construct of its own that is not a theory.
- gaps: none.

## TERM-003 — A sort may be indexed by terms

- revision: 3
- standing: draft
- kind: permission
- subject: the declaration of a sort
- from: SOURCE R13 D-TH-2 (line 93). R13 tag: `D L17 | kept`. PROPOSED — The marked restriction below is from gap TG-011 under [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A].
- text: A sort may be indexed by terms. PROPOSED — Marked restriction (standing: DRAFT; kind: requirement; subject: an index term admitted for a sort): A plain index only: it may depend on earlier arguments, has no effect or open choice, makes and consumes no use-once value or sequence, and gives a result that may be copied. [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A]
- case: A theory declares the sort `vector` with one index, a length n. The declaration is a sort declaration of the language. R13's own example is "a vector of length n". PROPOSED — Restriction case (invented notation): probe is declared effectful; vector(probe(n)) is proposed as an indexed sort, with n an earlier ordinary argument. The proposed index is refused for the effect premise alone; this case runs no computation and chooses no timing or charge. [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A]
- excludes: A language in which no sort can carry an index, so that the length of a vector cannot appear in its sort. PROPOSED — Restriction excludes: admitting the proposed vector(probe(n)) index despite probe being declared effectful. [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A]
- gaps: TG-001 (whether slice 1 admits an indexed sort, and how two index terms are compared); TG-011 (what an index term may be). PROPOSED — TG-011 remains OPEN pending owner confirmation; timing, fuel and repeated reads of an index still need rules under either answer. [provisional: Claude Arch under the owner's overnight record, card 0117, question I: I-A] [P0117:I-A]

## TERM-004 — An operation may bind variables

- revision: 1
- standing: draft
- kind: permission
- subject: the declaration of an operation
- from: SOURCE R13 D-TH-3 (line 95), first sentence. R13 tag: `D L18; C6 | fold`.
- text: An operation may bind variables.
- note: INFERENCE An argument in which the operation binds variables is what R13 goes on to call a bound argument. R13 uses the name and does not define it.
- case: The operation `twice` takes one bound argument with one variable. In `twice(x. f(x))` the variable x is bound by `twice` in that argument.
- excludes: Forbidding an operation from binding variables in any argument, so that the declaration of twice with its one-variable bound argument is refused.
- gaps: none. The node shape of a written binder, and its count, are REC-001 and are not repeated here.

## TERM-005 — A bound argument's multiplicity is declared in the operation's signature

- revision: 1
- standing: draft
- kind: requirement
- subject: the signature of an operation that has a bound argument
- from: SOURCE R13 D-TH-3 (line 95), second sentence. R13 tag: `D L18; C6 | fold`. Beside it: R13 D-REC-3 (line 1069), "A bound argument's multiplicity is in the signature of its operation."
- text: A bound argument carries a multiplicity. The multiplicity is declared in the signature of the operation.
- case: The signature of `twice` declares its bound argument with multiplicity any. A reader of the signature alone, without the rules of `twice`, can say which multiplicity the argument has.
- excludes: A multiplicity worked out from the operation's rules or from its uses, with nothing declared in the signature.
- gaps: TG-004 (whether omitted source spelling elaborates to an explicit multiplicity in the operation's signature).

## TERM-006 — What a multiplicity says

- revision: 1
- standing: draft
- kind: definition
- subject: the multiplicity of a bound argument
- from: SOURCE R13 D-TH-3 (line 95), second sentence. R13 tag: `D L18; C6 | fold`.
- text: The multiplicity of a bound argument says how many times the operation calls that argument.
- case: `relay` declares its bound argument h with multiplicity one. That says `relay` calls h once. R13's case at D-UO-3 (line 129) is `relay(h) = twice(h)`, whose run calls h twice. The declaration and the run differ, and the use-once check is what finds it.
- excludes: Reading the multiplicity as how many times the argument occurs in the source text, or as how many values it returns.
- gaps: TG-010 (what one requires where a run does not end). The check that a rule keeps a declared multiplicity belongs to the use-once rules (D-UO-3, D-UO-5).

## TERM-007 — A multiplicity is one or any

- revision: 1
- standing: draft
- kind: requirement
- subject: the signature of an operation that has a bound argument
- from: SOURCE R13 D-TH-3 (line 95), third sentence. R13 tag: `D L18; C6 | fold`. Beside it: R13 D-REC-1 (line 1053), `multiplicity: one | any`.
- text: A multiplicity is one or any.
- note: INFERENCE "one or any" is read as closed: there is no other value. The record line `multiplicity: one | any` reads the same way.
- case: A signature declares a bound argument with multiplicity one. Another declares one with multiplicity any. Both are signatures. A signature that declares a bound argument with multiplicity two is not.
- excludes: A third value, such as a count or a range.
- gaps: TG-003 (R13 sends a third value, none, to test; until that test is run and taken, this rule stands with two values).

## TERM-008 — A law is a statement the theory asserts

- revision: 1
- standing: draft
- kind: definition
- subject: a law of a theory
- from: SOURCE R13 D-TH-4 (line 97). R13 tag: `D L19 | kept`. Beside it: R13 D-REC-1 (line 1046), where `law` is one of the kinds of a declared symbol.
- text: A law is a statement the theory asserts. A law is declared in its theory, as a sort and an operation are.
- case: A theory of joining declares the law `assoc`: joining a with the join of b and c is the same as joining the join of a and b with c. `assoc` is a member of the theory, and it is a statement. It is not a step of a run.
- excludes: Treating a declared law as a rule, so that the reference run rewrites by it.
- gaps: none. Whether a law holds at an interpretation is a claim (D-IN-2) and belongs to the claims rules.

## TERM-009 — An effect is an operation whose last argument is a bound continuation

- revision: 1
- standing: draft
- kind: definition
- subject: the declaration of an effect
- from: SOURCE R13 D-TH-6 (line 102), first sentence. R13 tag: `D L20; C6 | fold`.
- text: An effect is an operation whose last argument is a bound continuation.
- case: `out` takes a value and then a bound continuation k. `out` is an effect. An operation `size` that takes a value and no continuation is not an effect.
- excludes: An effect whose continuation is not its last argument, or an effect with no continuation.
- gaps: TG-006 (the symbol and signature of slice 1's one output operation are open in R13).

## TERM-010 — The order of effects is written into the term

- revision: 1
- standing: draft
- kind: requirement
- subject: a term containing effects
- from: SOURCE R13 D-TH-6 (line 102), first sentence, "so order is written into the term". R13 tag: `D L20; C6 | fold`. Beside it: R13 D-UO-14 (line 166), "everything after an effect is inside its continuation".
- text: Order is written into the term. What runs after an effect is inside that effect's continuation.
- case: `out(1, k1)`, where the body of k1 is `out(2, k2)`. The term itself says that 1 is put out before 2. No rule outside the term is needed to order them.
- excludes: Two effects that stand side by side in a term, with their order left to a build.
- gaps: TG-007 (where an effect may stand after the reader). How source text with an effect inside an argument becomes continuations is D-STG-1, stage 1, and belongs to the reader of text.

## TERM-011 — Every interpretation of an effect owes the continuation's multiplicity

- revision: 1
- standing: draft
- kind: requirement
- subject: an interpretation of an effect
- from: SOURCE R13 D-TH-6 (line 102), second sentence, first half. R13 tag: `D L20; C6 | fold`.
- text: The multiplicity of an effect's continuation is owed by every interpretation of the effect.
- case: `out` declares its continuation with multiplicity one. An interpretation of `out` that calls the continuation twice does not keep what the effect declares.
- excludes: An interpretation that is free of the declared multiplicity because it is an interpretation and not the operation itself.
- gaps: TG-009 (interpretations that are not rules); none for the obligation stated here. It applies to every interpretation of an effect, without a slice exemption. Slice 2 adds effects with handlers (D-SL-2); the exact slice 1 output signature remains TG-006.

## TERM-012 — A handler is a rule, and the use-once check counts the continuation in it

- revision: 1
- standing: draft
- kind: requirement
- subject: the use-once checker when it checks a handler of an effect
- from: SOURCE R13 D-TH-6 (line 102), second sentence, second half. R13 tag: `D L20; C6 | fold`. Beside it: R13 D-UO-3 (line 128), clause (b).
- text: The use-once checker checks a handler as a rule. Clause (b) of D-UO-3 counts the continuation in it.
- case: A handler for `out` is the rule `out(v, k) = k(unit)`. The continuation k is a pattern variable of that rule. With multiplicity one it has exactly one site on the right-hand side, and this rule has one.
- excludes: A handler checked by some means other than as a rule, so that its continuation is not counted.
- gaps: TG-009 (interpretations that are not rules). The clause itself is D-UO-3 and belongs to the use-once rules; it is cited here and not restated. First needed in slice 2.

END OF RULES-TERMS
