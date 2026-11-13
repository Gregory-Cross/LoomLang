SOURCE — Three author objections; all31 W changes applied exactly, including the objected wording. No alternative repair was inserted. Codex C disposition pending.

# SOURCE / INFERENCE — Author objections for Codex C

## SOURCE — OB01: W30 does not preserve the checked first sentence verbatim

SOURCE — Eng REPORT.md L16 says all four overlapping changes leave Codex C's repaired sentences as they are. W30, Eng L695–707 and finding4.1/5.5, explicitly replaces this sentence at R2 PROPOSAL.md:228:

```text
Resolve technical O01–O07/O09–O10/O12–O13/O15, or retain explicit alternatives.
```

SOURCE — Exact applied R3 sentence, still at P:228:

```text
Resolve technical O01–O07/O09–O10/O12–O13/O15–O17, or retain explicit alternatives.
```

SOURCE — Codex C's supplied R2 recheck identifies P:228 at L17 and discusses it at L48. The original first-sentence bytes occur once in R2 and zero times in R3; the exact new sentence occurs once. The second sentence about authority, complete profile/header/grammar and C1 waiting is preserved verbatim. W30 was applied, not skipped.

INFERENCE — O15 remains included in the expanded range, but that is a dependency-preservation argument, not word-for-word preservation. The objection is to the blanket preservation claim; it does not assert the expansion is an improper edit. The card's literal preservation check cannot pass for this sentence while also applying W30 exactly.

PROPOSED — Codex C should explicitly assess the expanded P1 dependencies and record this as a changed checked sentence. This author supplies no substitute wording or claim that the earlier pass transfers.

## INFERENCE — OB02: W16's symbol inventory is not by itself the complete separation proof

SOURCE — W16, Eng REPORT L511–523, finding3.3, is applied exactly at R3 P:213. It says the demonstration is read from linked artifacts and that the evaluator's linked program contains no symbol of the runtime's arithmetic module.

INFERENCE — A negative inventory of symbol names alone need not establish absence of reachable code from that module. The reasoning also needs premises about the pinned compilation/link process: for example, whether module code can be inlined, internalized or left without the identifying symbols in the inspected artifact. The supplied exact words do not state those premises or a complete code-origin/reachability check. A symbol check can be useful evidence while remaining insufficient as the whole demonstration. No actual artifact or toolchain was inspected here.

PROPOSED — Codex C should decide whether W16 is adequately qualified as one required artifact check, or needs further words before being used as the separation criterion. The stronger existing requirement to demonstrate separation remains; this author has not weakened it or changed the prescribed W16 text.

## SOURCE / INFERENCE — OB03: W17 couples distinct address and thread constraints too categorically

SOURCE — W17 adds O16 at R3 OPEN.md:26. Its alternative C joins a moving collector and tasks that move between operating-system threads with “or”, then says a handle can no longer be a raw box address and O02 A no longer holds, requiring the declarations and O02 to reopen. Eng's own host-assumption table at REPORT L743 allows pinned objects or a table of indices for a moving collector. W23, applied at O:12, expressly permits pinning a task to keep a run on one operating-system thread.

INFERENCE — Address stability and same-thread run lookup are distinct obligations. Thread migration alone does not logically imply box movement; conversely, the source's pinned-object possibility is not represented in O16 C's categorical raw-address conclusion. A pinned-task condition is also already an explicit option in W23. An unpinned implementation may indeed require a different interface, but the supplied alternatives do not establish that every implementation in either broad language category must change all those parts.

PROPOSED — Codex C should reconcile O16 C with the source's pinning possibilities and W23 before treating it as an unavoidable ABI bill in the language comparison. No language, pinning implementation, moving collector or alternative ABI is selected here. W17 remains applied exactly for that review.

SOURCE — These are author observations within the requested objection route, not an independent review, disposition of Eng's findings or authority to alter the31 prescribed words. O17's separate runtime-precondition decision remains with Claude Arch. No new owner decision was authenticated or enacted.

# SOURCE - R4 objection dispositions from Codex C card 0561

SOURCE - The preceding bytes are unchanged R3 history. These exact ruling records supersede its pending disposition requests. OB01 is KEEP AS APPLIED; OB02 and OB03 use the F01 and F02 replacements already applied once in PROPOSAL.md and OPEN.md. They are not extra operative subject repairs.

```json
[
  {
    "id": "OB01",
    "claim": "SOURCE / INFERENCE",
    "ruling": "KEEP AS APPLIED",
    "W": "W30",
    "reason": "The author correctly rejects Eng L16's blanket literal-preservation claim. W30 changes P228, retains O15 and adds the new open dependencies without selecting them. Rechecked on its own bytes; the R2 verdict does not transfer.",
    "exact_words_kept": "Resolve technical O01–O07/O09–O10/O12–O13/O15–O17, or retain explicit alternatives."
  },
  {
    "id": "OB02",
    "claim": "INFERENCE / PROPOSED",
    "ruling": "REPLACE",
    "W": "W16",
    "repair": "F01",
    "reason": "A name inventory need not retain code provenance through compilation or linking. Removing or changing identifying names does not remove incorporated arithmetic code. The original separation requirement stays; the evidence must cover the transformations and reachable implementation.",
    "exact_replacement_words": "The evaluator's arithmetic path must demonstrably not call this runtime's arithmetic module. Bind the evaluator arithmetic sources, compiler and linker inputs and options, dependency closure and resulting artifacts, and show that the evaluator arithmetic uses a separate implementation with no call or incorporated code from this runtime's arithmetic module. The evidence must account for inlining, internalization, symbol stripping or renaming, and separately linked dependencies under those exact tools. Symbol and link-map inspection are supporting checks; absence of identifying symbol names alone is not the demonstration. Source intent or a source-level module boundary alone is also insufficient. If code origin or a reachable dependency is unaccounted for, separation remains NOT DONE."
  },
  {
    "id": "OB03",
    "claim": "INFERENCE / PROPOSED",
    "ruling": "REPLACE",
    "W": "W17",
    "repair": "F02",
    "reason": "Address stability and thread affinity are independent premises. O02/W23 already permits task pinning, and Eng L743 mentions pinned objects. O16 also must qualify Rust-specific OPEN rows, not only PROPOSAL sentences. The replacement keeps every implementation choice open.",
    "exact_replacement_words": "| O16 — Arch, after the owner's host-language decision: implementation language of the runtime and its driver | A: Rust, as one candidate: C-convention exports, a private run kept on one operating-system thread, qualified panic containment and a private double-width accumulator. B: C or another implementation language, with the same C-compatible declarations only after its address stability, run lookup, containment, exact arithmetic, size limits, aliasing, cleanup and stack obligations are restated and qualified. C: an implementation that cannot meet one or more of those premises requires a separately reviewed adaptation. A moving collector may retain raw box-address handles if the boxes are kept at stable addresses for every required lifetime; otherwise the handle representation and its contracts reopen. Task migration is a separate question: pin the run to one operating-system thread for O02 A, or reopen run lookup and consider O02 B. Task migration alone does not imply that boxes move. Only an adaptation that changes boundary carriers or arguments changes the declarations; no such adaptation is selected here. | No language is selected or recommended while the owner's host-language round is open. All Rust-specific wording in PROPOSAL.md and OPEN.md, including the Rust target, driver and panic wording in O01/O02/O09, describes candidate A only; it is not a prerequisite for another language. The 25 declarations, marks, grammar and Q01–Q11 are conditional on the stated interface obligations, not on a language name. Pinning, stable storage or indirection each carries its own lifetime, resource and implementation proof; none is supplied by this row. Candidate P keeps driver lifecycle work on the runtime side without a new C driver ABI. The compiler's language does not select the runtime's, because they communicate through bound artifact files (section 5). |"
  }
]
```
