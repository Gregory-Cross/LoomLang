# What must a cheaper representation remember?

*Draft explanation for a first reading of Loom.*

The aim is to replace an object with something cheaper that still answers every question its client can ask, even after an allowed update. ([D-REP-1], [D-ENG-6], [November 9 explanation])
The client is the part of the program using the object. ([D-REP-1])
A **name** stands for an object, and each operation the client can reach has a **tracker** that does its work on names. ([D-REP-1])

One object may have several names, and one name may stand for several objects. ([D-REP-3])
In this explanation, a **fibre** is what you get by holding one side of that relation fixed and seeing what can vary on the other. The November 9 report calls the two directions **gauge** and **loss**. ([D-REP-3], [November 9 explanation])

### Gauge · hold the object fixed

**Worked explanation.** A client keeps counts of red and blue counters in two trays. It can ask for the total or add one red counter. Write the total as a decimal numeral or as tally marks, with an empty tally for zero. ([D-REP-3], [LOSS-01])

Two red and one blue give `3` and `|||`. Read the numeral or count the strokes and the answer is 3. After adding one red, the names become `4` and `||||`, and both readings give 4. Counting the printed characters would fail as a total reader because it gives 1 for `3` and 3 for `|||`. ([D-TR-1], [LOSS-01])

This freedom to choose a presentation while preserving the promised answers is **gauge**. ([D-REP-3], [R-37], [November 9 explanation])
If the client can inspect the spelling as bytes, that reading also needs a tracker. ([D-REP-2])

### Loss · hold the name fixed

**Worked explanation.** Keep the name `3` and write the two counts together as `(red, blue)`. Both `(2, 1)` and `(1, 2)` have that name. Asking how many counters are red requires 2 in the first case and 1 in the second. ([LOSS-01], [D-RL-6])

That distinction is the **loss** for the red-count question. ([D-REP-3], [D-RL-6], [November 9 explanation])

Even if the client asks only for totals, try giving it a new update that doubles the red count. The first new total is `2 × 2 + 1 = 5`. The second is `2 × 1 + 2 = 4`. A tracker starting with `3` cannot give the right new total in both cases. ([LOSS-01], [D-RL-7])

<div style="break-after: page; page-break-after: always;"></div>

## When is a replacement worth using?

When a question allows several answers, each answer the tracker gives must be one the original permits. ([D-TR-1])
A choice the tracker settles that the client could observe is recorded unless it has been shown to make no difference. ([D-LOCK-2])
To show that a name cannot answer a question, give objects with that name for which no allowed answer works in common. ([D-RL-6])

When each object has one right answer, two objects requiring different answers suffice. ([D-RL-7])

### What the saving depends on

The register allows a summary to store a question’s answer and calls for comparing its cost with asking the original object, including cases with no saving. ([R-62])
That comparison depends on how the original arrives and how many questions and updates follow. ([D-ENG-6])
The proposed search needs a separate check before calling a working summary **coarsest**, a claim about how much detail can be discarded. ([D-ENG-5])

**Worked explanation.** Start with each tray count in one memory cell. With no updates, charge one unit per read, addition or write. Asking the trays takes two reads and an addition each time. Building a cached total takes those three steps and one write, then each question takes one read. ([D-ENG-6], [R-62])

For one question, asking the trays costs 3 units against 5 for building and reading the total. For three questions the costs are 9 and 7. The same summary pays off on the second workload. ([D-ENG-6], [R-62])

### Words for reading the design

**Explanation.** The value spaces in the tray example are pairs of nonnegative counts for the trays and single nonnegative counts for totals. The **tuple** `(2, 1)` holds its values in fixed positions, red first and blue second. ([Design vocabulary], [D-VAL-1], [Owner’s rename])

**Theories** name **sorts** of values, the operations on them, and their laws and rules. ([D-TH-1])
**Models** give that vocabulary a meaning, as when a tray count means a natural number and adding a counter means adding one. ([D-FAC-1], [D-TM-3])
**Interpretations** express one theory in the terms of another, preserving sorts, and each translated law becomes a claim to support. ([D-IN-1], [D-IN-2])

The five **facets** distinguish meaning, effects (what running does), usage (what may be copied or dropped), representation (how a value is laid out and computed) and evidence (what is known and why). ([D-FAC-1])
A term’s **manifest** records what it depends on, including what it does, assumes or trusts and when each entry acts. ([D-ROW-1], [D-ROW-8], [Owner’s rename])

<div style="break-after: page; page-break-after: always;"></div>

## What is decided, open or for later?

**Decided.** The number of facets is settled at five. ([D-FAC-1])
The workload comparison for answer caches stands and comes back before the third development stage (slice 3) fixes the results sheet and the request for a coarsest representation. ([R-62])
**Open timing.** The Structural Representation Explorer (SRE) builds, checks and combines representations, and a kernel program checks the claims it establishes. ([D-OPT-1], [D-ENG-1])

The register records graphs as its first application. ([R-10])
The owner has yet to place its first stage, with finite work possible after slice 3 and an earlier plan placing it after slice 5. ([D-SL-8])
The reminder comes due when slice 3 finishes and, in any case, before the relevant slice 5 interfaces are drafted. ([Timing reminder])

### Four proposals in the design text

The register records the owner’s request to draft and review these proposals. ([Register status])
- Search within a budget for a representation that answers what one client can reach. ([LOSS-01])
- Count colourings of graphs joined along a boundary and look for a join that exposes what storing only the count loses. ([LOSS-02])

- Try vector names over a field, such as the rational numbers. When a join multiplies matching entries from the two sides and adds the products, check a lower bound on the number of entries. ([LOSS-03])
- Compare the pairs of objects that each question with one right answer per object distinguishes on a named collection of examples, keeping the conclusion within that collection. ([LOSS-04])

### Later questions in the register

- For the first finite demonstration, one proposal would search for a small object with a chosen algebraic effect and check its result. ([R-28])
- At the first cost study, another would search for a cheaper presentation with the same capabilities. ([R-37])
- Could one tool catch both a reader that gets the total wrong for one spelling and a shared total that hides the red count? ([R-51])

- Under what conditions would allowing more changes of presentation leave the same or fewer distinctions between objects? ([R-53])
- Two further candidates ask how a family of representations could carry changes between related objects, and whether an always-terminating language for indices could establish when dimensions are equal. ([R-35], [R-36])

[D-REP-1]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:263> "D-REP-1, lines 263 to 269"
[D-REP-2]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:271> "D-REP-2, lines 271 to 271"
[D-REP-3]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:273> "D-REP-3, lines 273 to 273"
[D-TR-1]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:372> "D-TR-1, lines 372 to 373"
[D-LOCK-2]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:764> "D-LOCK-2, lines 764 to 764"
[D-RL-6]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:477> "D-RL-6, lines 477 to 478"
[D-RL-7]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:480> "D-RL-7, lines 480 to 481"
[D-ENG-5]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:954> "D-ENG-5, lines 954 to 954"
[D-ENG-6]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:962> "D-ENG-6, lines 962 to 965"
[D-TH-1]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:94> "D-TH-1, lines 94 to 94"
[D-FAC-1]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:302> "D-FAC-1, lines 302 to 305"
[D-TM-3]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:180> "D-TM-3, lines 180 to 180"
[D-IN-1]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:205> "D-IN-1, lines 205 to 205"
[D-IN-2]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:207> "D-IN-2, lines 207 to 207"
[D-VAL-1]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:1050> "D-VAL-1, lines 1050 to 1050"
[D-ROW-1]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:216> "D-ROW-1, lines 216 to 216"
[D-ROW-8]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:231> "D-ROW-8, lines 231 to 231"
[Design vocabulary]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:1458> "Design vocabulary, lines 1458 to 1458"
[D-OPT-1]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:926> "D-OPT-1, lines 926 to 926"
[D-ENG-1]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:928> "D-ENG-1, lines 928 to 928"
[D-SL-8]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:916> "D-SL-8, lines 916 to 916"
[Timing reminder]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:920> "Timing reminder, lines 920 to 920"
[LOSS-01]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:956> "LOSS-01, lines 956 to 960"
[LOSS-02]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:918> "LOSS-02, lines 918 to 918"
[LOSS-03]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:948> "LOSS-03, lines 948 to 952"
[LOSS-04]: <C:/LoomLang/docs/design/DESIGN-TEXT-R19.md:974> "LOSS-04, lines 974 to 974"
[Register status]: <C:/LoomLang/docs/design/DECISIONS.md:340> "Register status, lines 340 to 348"
[R-10]: <C:/LoomLang/docs/design/DECISIONS.md:212> "R-10, lines 212 to 216"
[R-28]: <C:/LoomLang/docs/design/DECISIONS.md:352> "R-28, lines 352 to 358"
[R-35]: <C:/LoomLang/docs/design/DECISIONS.md:408> "R-35, lines 408 to 414"
[R-36]: <C:/LoomLang/docs/design/DECISIONS.md:416> "R-36, lines 416 to 423"
[R-37]: <C:/LoomLang/docs/design/DECISIONS.md:425> "R-37, lines 425 to 431"
[R-51]: <C:/LoomLang/docs/design/DECISIONS.md:538> "R-51, lines 538 to 544"
[R-53]: <C:/LoomLang/docs/design/DECISIONS.md:555> "R-53, lines 555 to 561"
[R-62]: <C:/LoomLang/docs/design/DECISIONS.md:630> "R-62, lines 630 to 635"
[November 9 explanation]: <C:/Users/grego/.codex/reviews/2026-11-09-CLAUDE-CS3-FRESH-REVIEW-R1/REPORT.md:401> "November 9 explanation, proposed explanatory framing, lines 401 to 409"
[Owner’s rename]: <C:/Users/grego/.codex/reviews/_relay/inputs/owner-record-2026-11-17-row-renamed-manifest-tuple.json:1> "Owner’s rename, lines 1 to 1"
