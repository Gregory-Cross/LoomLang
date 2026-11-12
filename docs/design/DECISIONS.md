# Owner decisions and items to reconsider

This is a register for finding decisions quickly. It holds no authority of its own: each decision's authority is its owner record under `C:\Users\grego\.codex\reviews\`, bound by the SHA-256 shown, with the raw session line in `_relay\inputs\owner-lines\`.

## Decisions of 2026-11-11

| Decision | Record | SHA-256 |
|---|---|---|
| Backend route for the first compiled demo: generated C first, for now | `_relay\inputs\owner-record-2026-11-11-backend-c-first.json` | `169a81ced7c19024bbc8ea59dd430d804a5fec1c269942ed07db9815baf49e4d` |
| Loom checks loaded machine code against the outside C compiler's recorded output | `_relay\inputs\owner-record-2026-11-11-backend-q3-outside-compiler.json` | `28bcf618747ae0552c63f11a95988afdd23d490bdd5f45ae5abb35cc47b5fb76` |
| Slice 2 first builds one fixed function at its first call during a run; slice 1 is wholly ahead of time | `_relay\inputs\owner-record-2026-11-11-backend-q2-slice-2.json` | `2d1e648182f59b0b7da476e5a6bcff2ef586a5c6344b91d2c38c7b243ed15f21` |
| Our own big-number code; a pinned Clang installed only if no suitable C compiler is present | `_relay\inputs\owner-record-2026-11-11-c-route-oq1-oq2.json` | `dbbb3dcf78a11ee43d2d6666768ac8f218ca085786b167df2e9d22e8a12f03a8` |
| ROW1-A: all O1 and O2 cases as recommended (one output operation; may-not-end permitted; no pick; memory stops permitted; fixed literal-check allowance; bad reply refused and retried; unanswered request recorded as waiting; uncaught failure details reported) | `_relay\inputs\owner-record-2026-11-11-row1-a-all-recommended.json` | `7694482f0fe03854ada477978e905bfcb1743c9570af1d7167bf6f3ad518d1cc` |
| OD1: a failed first-call build stops the run cleanly, with no spare copy | `_relay\inputs\owner-record-2026-11-11-defer-a-od1-stop.json` | `134e57c1614aaf69c6b3a5f92aba47e93d236f97ce702a7c0251f2ce0f68cb7d` |
| O3: outcome B for now (a catcher may not take back what a failed part held), on condition that reconsidering A is recorded (R-1 below) | `_relay\inputs\owner-record-2026-11-11-o3-b-for-now.json` | `c6d9a61211ca0f82cc42e30e6cc6220b9f24dea59265a6d9649439c730e68bef` |
| The repository writer is Codex Y (Writer) | `_relay\inputs\owner-record-2026-11-11-repo-writer-codex.json` | `97b2a5db3180ae505fa109de9d0a425e205ae97a6b9f42e981a8cd51a7c4e8be` |
| Writer commits go by sealed manifest and a fixed script run by Claude A | `_relay\inputs\owner-record-2026-11-11-writer-commit-route-option-1.json` | `0b2dd543ea1ba27b1324562ad157dace4f81ac416b08bb2a667e6093d2629908` |
| Loop count O1 (E-22): outcome A, a loop with bound two records its counter 0 then 1 | `_relay\inputs\owner-record-2026-11-11-loop-o1-a-and-arch-fixes.json` | `13d39778c71193ec5f7396cc0f0dfb4bb8d64828e3bc7064d8961e15a861355f` |
| OC-01: a core let whose body belongs to the enclosing use-once scope, so an ordinary computed value may be used beside an outside use-once value | `_relay\inputs\owner-record-2026-11-11-oc-01-core-let.json` | `110cb0c0e4e49f249f177787b48959213a01ebddaa5cc71fcdd30d0646599cae` |
| OC-03: incoming naturals are uncapped, limited only by the run's paid resources | `_relay\inputs\owner-record-2026-11-11-oc-03-05-08.json` | `c34fb1638e8a9e6ae31780de7a406e876ea5fbfa47c0398097ffe448c2feab83` |
| OC-05: local variables are numbered, so renaming one does not change a run's identity (clarified by the next record) | `_relay\inputs\owner-record-2026-11-11-oc-03-05-08.json` | `c34fb1638e8a9e6ae31780de7a406e876ea5fbfa47c0398097ffe448c2feab83` |
| OC-05 to OC-09: the digest's recommendations: OC-05 numbering (B), OC-06 every declaration counts toward identity (Keep), OC-07 one fixed order of names for every run (A), OC-08 byte slice takes start and length (A), OC-09 reading one byte gives its number 0 to 255 (A) | `_relay\inputs\owner-record-2026-11-11-oc-05-09-recs.json` | `0cf0a56733dc371a76bf5808d36829de565bd7a7e3e63ccda55b9244f35c75c6` |
| OC-10: length extends to bytes | `_relay\inputs\owner-record-2026-11-11-oc-10-and-reissue.json` | `f045d11030a4058ab80190f9c2f5c7d70ffb7c690a3a8f72d1ad10ebfd2a8e3c` |
| Web-round questions: OQ1 a term may be computed once and its result reused only if it makes nothing new, has no effect or open choice, consumes nothing use-once, and its result may be copied; OQ2 byte positions start at zero; OQ3 a memo call that reaches its own unfinished key runs on under ordinary fuel (no reuse of an unfinished result) | `_relay\inputs\owner-record-2026-11-11-web-oq1-oq3-a.json` | `a0d5d57eda178a25141c24284bc12cd5c41519bf38fc9e12a8692b9c319a830d` |
| The topic-5 hold on method changes does not cover Claude Arch's four corrections to HOW-WE-SPECIFY (F005, F006, sampling, F011 with F009); old build folders are cleaned by an owner-run script whose in-use check runs as the owner | `_relay\inputs\owner-record-2026-11-11-topic5-a-arch-cleanup.json` | `dc27442f173f1f7c593a7688bb91f49ef6a6adb1e2327d4d42de39e4203ebef1` |
| Design improvements, Claude Arch's three questions: a stop's record says what ran out, which permission allowed the stop and what the program was doing; the host owns what a refused reply carried until the reply is accepted; two claims that support only each other give no support | `_relay\inputs\owner-record-2026-11-11-improvements-q1-q3-arch.json` | `54f62789678ba17c9f779788038ef67c8c9fc71a88239138311215e0fef762de` |
| Design improvements R1: a stop's record also binds the comparison that checks it, and a failed first-call build is recorded the same way even if it is not a resource stop; reports must carry their subject, stage and cause, and a comparison of two runs ends in one of three named conclusions (agreement, established mismatch, incomplete); exact fields are left to the record work | `_relay\inputs\owner-record-2026-11-11-improvements-q1-q2-overnight.json` | `f1aca4cd23d00fa16903735fc0c94b00393b4db787f76c8913670eb6c404778a` |

## Decisions of 2026-11-12

| Decision | Owner record and SHA-256 | Owner answer binding |
|---|---|---|
| **SOURCE — Write charge:** the owner chose Arch's position: a write charge grows with the size of the position number, and a sequence carries no last-place marker. Codex C preferred distance accounting as a deliberate starting machine model. This records the chosen direction; the exact tariff wording and its application remain separate drafting and review work. | `_relay\inputs\owner-record-2026-11-12-write-charge-arch-and-one-brief.json` — `798ab8b8b8ae5e29aa568494256f5db2dd9e08d28145711da3283618d4594d66` | Human-origin queued answer, session `dbfde0c8-307d-439e-8e98-14c66f387816`, `2026-11-12T21:33:38.591Z`; raw answer-line SHA-256 `b86ebf288bc8b3279471ed2aeaa096b3fe6af78641c4c28269377a895ea1074a` |
| **SOURCE — Question 2, big-number check in development:** yes. Our own big-number code remains in every program, checked in development against an independent implementation; no big-number library ships with programs. This records a requirement, not a completed arithmetic check or a chosen checking implementation. | `_relay\inputs\owner-record-2026-11-12-bignum-check-lookback-working.json` — `52b97033102df13679fb1c561d24c7cd56cf36d79935d2801e3d7ca8ecef5b29` | Human-origin typed answer, session `dbfde0c8-307d-439e-8e98-14c66f387816`, `2026-11-12T21:56:51.915Z`; raw answer-line SHA-256 `6309945a9e5a743bb2cac4a3468b5a4b4cf1dbf35f0ef51950e4fa82578d8281` |
| **SOURCE — Question 3, declared look-back:** yes. Mark the declared form working until its rule for running the argument is written and accepted and four tests pass; only the mark at the call may be relied on meanwhile. Queue the four tests now. This does not choose whether the looked-at argument runs. | `_relay\inputs\owner-record-2026-11-12-bignum-check-lookback-working.json` — `52b97033102df13679fb1c561d24c7cd56cf36d79935d2801e3d7ca8ecef5b29` | Human-origin typed answer, session `dbfde0c8-307d-439e-8e98-14c66f387816`, `2026-11-12T21:56:51.915Z`; raw answer-line SHA-256 `6309945a9e5a743bb2cac4a3468b5a4b4cf1dbf35f0ef51950e4fa82578d8281` |
| **SOURCE — Implementation-language research direction:** undertake a web round now to question Rust: prepare a package and researched shortlist, and ask some web chats to seek advantageous languages outside it, including whether Haskell and functional-first languages are contenders. This direction chooses no implementation language. | `_relay\inputs\owner-record-2026-11-12-host-language-web-round.json` — `8a808233139b70aad24fdb83cdb7896c1e9630e12852068efa5d5929bffc4ff5` | Human-origin typed answer, session `dbfde0c8-307d-439e-8e98-14c66f387816`, `2026-11-12T22:42:44.223Z`; raw answer-line SHA-256 `1e8c461655a5896398fdd5adcef2eb6baf56b693c0947d7fa89f04904bf72b43` |
| **SOURCE — Moves 5, 23 and 28:** keep all three present rules. A build need only give answers the meaning allows; a stronger promise is a separate claim. An operation pays its whole safe upper bound before it starts. Acceptance is the same whichever representation is chosen. Arch's follow-ups below are PROPOSED work, not further owner decisions or conditions on this keep answer. | `_relay\inputs\owner-record-2026-11-12-forced-moves-5-23-28-keep.json` — `787fcfc1f4199c217e65f07297967d1d264adb2becd2dbff654f1fbada05fbb0` | Human-origin queued answer, session `dbfde0c8-307d-439e-8e98-14c66f387816`, `2026-11-12T22:03:11.567Z`; raw answer-line SHA-256 `f8cb0d6a86fc56a08abfda12567286c2556cda3f4673b8b257d4c26cbcb6848b` |

- **Move 23 follow-up (PROPOSED):** at the meter's next revision, each operation states how far its bound can exceed what it builds. Work Codex G's three cases on paper before the meter is fixed: a loose bound, an operation heavy in working space, and a real stop part-way. **Source (SOURCE):** `2026-11-12-CLAUDE-ARCH-ERRATUM-EXTRACTS-MOVES\REPORT.md`, section 3, line 472.
- **Move 28 follow-up (PROPOSED):** work Codex G's two cases on paper: one already solved by bringing evidence forward, and one that would still gain from the alternative. This is follow-through under the kept rule, not a new representation-dependent acceptance rule. **Source (SOURCE):** `2026-11-12-CLAUDE-ARCH-ERRATUM-EXTRACTS-MOVES\REPORT.md`, section 3, line 474.
- **Move 5 follow-up (PROPOSED):** design a form for the stronger promise that a reader can see on the operations needing it, and try it on the secret example before anything in Loom relies on secrecy or on chance. **Source (SOURCE):** `2026-11-12-CLAUDE-ARCH-ERRATUM-EXTRACTS-MOVES\REPORT.md`, section 3, line 470.

- **Follow-through (PROPOSED):** before applying this direction to design wording, the meter, rules, tests or records, draft the exact tariff and obtain its required review. This register entry neither supplies that tariff nor performs its application.

- **Write-charge edge defaults (INFERENCE):** the two defaults fall away with their last-place subject: “`contents` of an empty sequence leaves the last place at 0” and “an arriving sequence with a bad last place is refused”. The earlier last-access-distance answer is superseded by the write-charge record above; this note supplies no replacement tariff. **Source (SOURCE):** One-brief section 6, item 6, line 418.

SOURCE — In these notes, “Arch audit” means `2026-11-12-CLAUDE-ARCH-DECISION-AUDIT\REPORT.md`; “Web check” means `2026-11-12-CLAUDE-ARCH-AUDIT-WEB-CHECK\REPORT.md`; “C audit” means `2026-11-12-CODEX-C-DECISION-AUDIT\REPORT.md`; “Arch notes” means `2026-11-12-CLAUDE-ARCH-AUDIT-NOTES-24-AND-26\REPORT.md`; “One-brief” means `2026-11-12-CLAUDE-ARCH-ONE-BRIEF\REPORT.md`; “Q web check” means `2026-11-12-CODEX-Q-AUDIT-WEB-CLAIMS\REPORT.md`; “R12” means the sealed `2026-11-11-CODEX-F-DESIGN-TEXT-R12\DESIGN-TEXT-R12.md` (the revision retained in Git history); the current text is `DESIGN-TEXT-R13.md`. These reports describe decisions and recommendations; they are not fresh owner decisions. “By 2026-11-12” is the audit's date bound where the original decision date is not supplied. Arch's L references are session dbfde0c8; chat L references are session 8755900a; S-L references are session 05db4389.

## To reconsider

Each item names what was chosen for now, what was set aside, and when to put it back to the owner. Whoever reaches a trigger raises it with Claude A, who puts it to the owner.

### Big-number code — ANSWER RECORDED
- **Chosen for now (SOURCE; 2026-11-11):** our own big-number code; the table's `owner-record-2026-11-11-c-route-oq1-oq2.json` records it, and Arch cites L31002. No new arithmetic choice is made here.
- **Views (SOURCE):** One-brief sections 2 and 4 now recommend our own code in programs with an independent implementation as a development check. Codex C recommends an independent check even if production remains custom, and asks whether custom production code is a requirement or the present plan. Optimized libraries and permissive alternatives exist, but speed on the planned workloads is unmeasured; the GMP version warning does not establish handwritten arithmetic as safer here, and rare-path frequency claims carry no weight (Q web check rows 56–58).
- **Answer recorded (SOURCE; 2026-11-12, question 2):** yes to One-brief section 8 question 2: check our own big-number code in development against an independent implementation, with nothing but our own big-number code in programs. The bound `owner-record-2026-11-12-bignum-check-lookback-working.json` above records the answer. No independent implementation, version, checking interface or completed comparison is selected or reported by this entry.
- **Reminders (PROPOSED):** retain the separate production-library alternative for later reconsideration, with exact naturals and clean stopping, candidate allocation and licence checks, and the suggested later triggers of numbers beyond a few thousand bits or a second arithmetic mistake. Neither the development-check answer nor this reminder adopts a production library.
- **Sources (SOURCE):** One-brief sections 2, 4 and 8 question 2; Arch audit entry 32; Web check rows 56–58 and section 5 entry 32; Q web check rows 56–58; C audit “A qualification on the big-number alternative”; the existing big-number decision row above; the 12 November write-charge owner record. The development-check answer is in `owner-record-2026-11-12-bignum-check-lookback-working.json` above.

### R-1. O3 outcome A: taking back what a failed part held

- **Chosen for now:** B. A catcher may go on only if the failed part held nothing or handed it back in its result; otherwise the failure carries on with the value held and named.
- **Set aside:** A. For a caught failure whose unfinished work can never run again, the catcher may take back eligible values the failed part held, using a new trusted take operation, with failure-sort and compiled live-slot information at calls that may fail. Take cannot take functions or values of sorts the rule cannot name.
- **Put A back to the owner when any of these happens:**
  1. the declared-residue test of RECOVERY-A revision 2, section 6, has run on its frozen fixtures, and an eligible positive encoding is refused by the present check, or a control is accepted with an independently supported wrong account, or a case needs a new operation in the reference run. A result that is unresolved or not run is reported to Claude A, and is not by itself a reason for A;
  2. real programs show that unplanned failures while holding live values are common;
  3. before any rule letting a catcher return after a failed part held a live value is drafted (handlers arrive in slice 2);
  4. at the latest, at the slice 2 review.
- **Put the two marks to the owner before the slice 2 recovery review (PROPOSED):** decide whether to replace the present exactly-once mark with separate no-copy and no-drop marks, since that changes which values must survive a failure. R12 D-UO-17 records two marks as the direction, not work adopted now. Foreign cleanup examples depend on particular unwinding or registration conditions; they do not release every resource or decide which marks Loom needs (Q web check row 27). **Sources (SOURCE):** Arch audit section 3.6 and entry 22; Web check section 5 entry 21; R12 D-UO-17; Q web check row 27.
- **Sources:** `2026-11-11-CLAUDE-ARCH-RECOVERY-A-R2\REPORT.md` (SHA-256 `1d30b247ada934556e70330cc5f7d6b41646cf185336f804893614ccf99c222e`; revision 1 re-checked by Codex Q, card 0109, whose repairs revision 2 applies) sections 5 to 7; the O3 owner record above.
- **Status (2026-11-11):** the section 6 test has run (Codex S, card 0023) and was reviewed SOUND (Codex Q, card 0112): trigger 1 has not fired. Two callback probes stayed unresolved and are reported; how often real programs meet the unrecovered failure is still unmeasured.

### R-2. The backend beyond generated C

- **Chosen for now:** generated C, for the first compiled demo.
- **Set aside:** Cranelift, LLVM, or an emitter of our own.
- **Put back to the owner when:** the C route's qualification fails at a stage; a run-time build in slice 2 proves too costly under C; slice 5's second target is planned; builds during a run must be fast enough to edit code live; Loom is to choose its own instructions with evidence enough to drop the C compiler as a trusted part; programs need speed the C compiler cannot give; or the design's two independent evaluator builds (D-TB-1) would both have to pass through the same C compiler.
- **At slice 2 planning (PROPOSED):** put to the owner whether testing the records with code publication disabled, as in R12 D-WEB-6(g), is enough for now in place of the first-call build through C. The existing slice 2 choice is recorded in `owner-record-2026-11-11-backend-q2-slice-2.json`; changing it needs the owner. Julia can interpret or reuse cached code as well as compile on demand; this is a latency precedent, not a measurement of this C route (Q web check row 34). **Sources (SOURCE):** Arch audit entry 28; Web check section 5 entry 28; R12 D-JIT-4 and D-WEB-6(g); Q web check row 34.
- **Known limits of generated C** (keep these in view; each is a reason the question may come back):
  1. **Trust.** The C compiler and Loom's lowering to C stay named as trusted. Checking generated programs is finite evidence, not a proof of the whole translation. Reducing that trust later needs a verified compiler or a proved emitter of our own.
  2. **Pausing and resuming.** C has no built-in way to pause a computation and resume it later. Slice 2's effects with handlers need it, so the runtime must keep its own frames on the heap or switch stacks, which differs by platform.
  3. **Building during a run.** It needs a C compiler on the machine where the program runs, and each build takes a noticeable fraction of a second: too slow for live editing.
  4. **Discipline.** Printed C must stay inside a small checked part of C, and floating point needs exact settings wherever it runs.
  5. **No guaranteed tail calls.** Deep recursion meets the depth guard instead; its clean stop is not yet qualified.
  6. **Porting.** A new target machine needs more than recompiling the C: its calling convention, machine theory and decoder, stack handling, object and loader support, and a qualified toolchain.
  7. **Self-hosting.** A Loom-written compiler can be built through C, but the result still needs a C compiler, and the Rust runtime until separate runtime work replaces it. Equal output over bootstrap rounds is a reproducibility check, not proof.
- **What carries over to a second backend:** Loom's checked low-level form, the runtime, the test harness, the decoder and the loader. Only the C printer and the C subset checker would be left behind.
- **Sources:** `2026-11-11-CLAUDE-ARCH-BACKEND-TRIAGE-R2\REPORT.md`; `2026-11-11-CLAUDE-ARCH-C-ROUTE-QUALIFICATION-R2\REPORT.md` section 9 (SHA-256 `5eee70871baf549aa692550f37f3a77cd7994d0bd5417a6109978664bc8ac7b2`; reviewed SOUND by Codex C, card 0539).

### R-3. Case 16: what else covers
- **Chosen for now (SOURCE; by 2026-11-12):** B: a subject outside the named choice gives `none` and runs no branch; `else` covers only remaining cases of that choice. Arch cites L25061, following L25044, and R12 names the second case-16 record.
- **Set aside (SOURCE):** A: `else` also handles subjects outside the choice.
- **Put back to the owner when (PROPOSED):** before either the design or implementation is closed; bring a checker or parser with mixed inputs to show what B can express and what would need A.
- **Sources (SOURCE):** Arch audit section 3.9 and section 6 item 5; R12 D-VAL-3; C audit “case dispatch” under “The adjacent decisions do not all need reversing”.

### R-4. Ranking candidates by abduction
- **Chosen for now (SOURCE; by 2026-11-12):** rank rather than exclude candidates, provisionally with a note to reconsider (Arch L25625 item 4; R12's six-answer record). D-WEB-4's guaranteed split orders experiments; it does not restore candidate exclusion.
- **Set aside (SOURCE):** exclude a candidate unless it helps explain an open goal. R12 makes application conditional on the 56-candidate test; that test is still NOT RUN in the supplied sources.
- **Put back to the owner when (PROPOSED):** before the design closes, run the named 56-candidate case both ways under the same stated budgets: for exclusion, report how many candidates are never proposed and which laws holding in the table are excluded; for ranking, where each such law falls and the work before it is reached at each budget. Return all four method counts for review before application; model-only results need a stated basis for transfer.
- **Sources (SOURCE):** Arch notes, note 24 (correcting Arch audit entry 24); Arch audit section 6 item 5; R12 D-STO-7 and D-WEB-4; C audit “exploratory ranking”.

### R-5. Reading a sequence at a position — OPEN FOR THE OWNER
- **Present rule (SOURCE; by 2026-11-12):** start with `contents(s)` followed by a row read; a direct read remains a later option (Arch L23888 and L24864; R12's strict-variant record).
- **Views (SOURCE):** One-brief sections 1 and 4 now recommend copy or read one position, with copy only and copying a stretch as alternatives. Codex C leans toward a charged direct read while retaining snapshots and asks for real consumers before changing the design.
- **Put to the owner now (PROPOSED; not a reminder):** use One-brief section 8, question 1: copy only, copy or read one position, or copy any stretch? Before the builds freeze, bring the wanted-read log, a sparse checker, a snapshot consumer and a stale-copy case. Retain R12's other-writer and stale-copy cases, and remeasure its more-than-twice cost comparison under the decided charge. The newer owner record leaves the read open; this entry adds no operation.
- **Sources (SOURCE):** One-brief sections 1, 4 and 8 question 1; Arch audit section 3.4; Web check section 5 entry 5; C audit “Where the no-index instinct needs reconsideration”; R12 D-SEQ-4, including its following paragraph; the 12 November write-charge owner record.

### R-6. Sets as a kind of value
- **Position recorded (SOURCE; by 2026-11-12):** sets as a kind of value are a requested proposal, not an adoption (Arch chat L1255; R12 D-VAL-1). The separate decided rule for sets holding sequences is in D-VAL-5.
- **Set aside (SOURCE):** wait for a need for built-in sets and use a sorted row meanwhile; the proposed order over all values is part of the cost to consider.
- **Put back to the owner when (PROPOSED):** before adopting sets as a kind of value, name the first definition slice 1 runs that uses a set; if none does, ask whether sets should wait for the first such need.
- **Sources (SOURCE):** Arch audit section 3.7, entry 14 and section 6 item 5; Web check section 5 entry 14; R12 D-VAL-1, D-VAL-4 and D-VAL-5.

### R-7. A bare none for a read outside the range
- **Chosen for now (SOURCE; by 2026-11-12):** row and byte reads outside the range give bare `none` (Arch L24894, option A; R12's record out-of-range-bare-none). A program storing `none` checks the row's length first.
- **Set aside (SOURCE):** wrap each successful read as `some(v)` so a stored `none` remains distinguishable; Codex C suggests a checked helper using the existing length check before changing the primitive.
- **Put back to the owner when (PROPOSED):** the first review finds a stored `none` mistaken for a read outside the range; bring the example and whether a checked helper removes the mistake or leaves a measured cost.
- **Sources (SOURCE):** Arch audit entry 9 and section 6 item 5; R12 D-VAL-6; C audit “The adjacent decisions do not all need reversing”, P06.

### R-8. Every declaration counts toward run identity
- **Chosen for now (SOURCE; 2026-11-11):** OC-06 includes every declaration in the recorded program, even one the run never calls (Arch L33437; `owner-record-2026-11-11-oc-05-09-recs.json`, also named in the table above).
- **Set aside (SOURCE):** count only declarations the run can reach. **INFERENCE:** including an unused helper can change sequence names across edits.
- **Put back to the owner when (PROPOSED):** evidence or a recorded run is first proposed for reuse across edits of a program; bring an unused-helper edit and show which names and comparisons change.
- **Sources (SOURCE):** Arch audit entry 38 and section 6 item 5; the existing OC-05 to OC-09 row; R12 Annex A and D-SEQ-2.

### R-9. Declared look-back — OPEN FOR THE OWNER: argument execution only
- **Answer recorded (SOURCE; 2026-11-12, question 3):** the callee-declared form, applied by name only, is working until its rule for running the argument is written and accepted and four tests pass. Only the mark written at the call may be relied on meanwhile. The bound `owner-record-2026-11-12-bignum-check-lookback-working.json` above records this standing and the direction to queue the tests; it does not choose the argument-execution rule.
- **Tests to queue now (SOURCE, owner-directed work):** the variable/beta case, an effectful argument, higher-order refusal, and deferred-build equivalence. This register records the direction, not completed tests or a pass.
- **Views (SOURCE):** One-brief sections 3 and 4 now join Codex C in recommending the declared form be marked working until its evaluation rule and four tests are settled, with tests queued now. The Web check corrects the earlier Lisp claim: the call need not be marked; precedent does not settle Loom's rule.
- **Put to the owner now (PROPOSED; argument execution only):** Arch's declared-look-back section 3.2 gives (a) the argument runs once and the function also gets how it was written; (b) the argument does not run and the function gets only how it was written; or (c) choose by declaration, with both sets of obligations and tests. Arch recommends (a) as the first step; none is selected. The already answered working-standing question is not reopened.
- **Technical follow-through (PROPOSED):** carry call visibility, binding and effect order through the written rule and the four tests under the eventual execution choice; do not widen beyond the first set before the owed test. These are follow-up obligations, not extra owner ballots.
- **Sources (SOURCE):** One-brief sections 3, 4 and 8 question 3; Arch audit section 3.5; Web check section 5 entry 15; C audit “look-back” under “The other instinct-led histories”; R12 D-LB-3 and D-LB-4; the 12 November write-charge owner record. The working-standing answer is in `owner-record-2026-11-12-bignum-check-lookback-working.json` above; the remaining owner choice and recommendation are in `2026-11-12-CLAUDE-ARCH-DECLARED-LOOKBACK\REPORT.md`, section 3.2, lines 118–124.

### R-10. A finish line for each SRE stage
- **Aim recorded (SOURCE; 2026-11-05):** a full SRE, first for graphs with infrastructure toward other structures (Arch S-L238385); the audit says this is an aim and adopts no language design.
- **Set aside (SOURCE):** only the narrower search for swap rules between small graph patches.
- **Put back to the owner when (PROPOSED):** before any SRE building starts, give every planned stage a finish line someone outside the team can check; for example, a theorem permits an algorithm under one interpretation and refuses it under another.
- **Sources (SOURCE):** Arch audit section 3.10 and section 6 item 5; R12 D-SL-5; C audit “SRE breadth”.

### R-11. Count sequence uses before the two evaluator builds
- **Chosen meaning (SOURCE; by 2026-11-12):** changing a sequence changes what every holder sees and preserves its identity (Arch L22130; R12 D-SEQ-1). R12 proposes state-free admission and result checks (D-SEQ-3).
- **Question kept (SOURCE):** Arch cannot tell whether slice 1 needs sequences before counting uses and comparing a real working-memory checker both ways; Codex C keeps shared identity with alias, snapshot and failed-restoration examples.
- **Put back to the owner when (PROPOSED):** before either evaluator build and before C qualification stage 4 compiles a sequence, count the definitions slice 1 runs that use sequences and compare one real checker with shared changes and with unchanged values. Return the count, fuel and record costs; zero uses is a question about deferral for the owner, not a removal by this entry.
- **Sources (SOURCE):** Arch audit section 3.2 and section 6 item 5; C audit “The sequence decisions, separated”; R12 D-SEQ-1 and D-SEQ-3.

### R-12. Census of the concurrency core
- **Standing recorded (SOURCE; by 2026-11-12):** D-CONC-2 to 6, 8 to 11, and 14 are in the design as working rules on Claude Arch's delegated call, not newly approved rules from this entry.
- **Set aside and condition (SOURCE):** leaving the core out of this round. The core falls if the D-CONC-3 census accepts a wrong term; the supplied Arch notes say that census has not run.
- **Put back to the owner when (PROPOSED):** before the use-once check, signature record or admission is fixed, run and review the D-CONC-3 census; return any wrongly accepted term and its effect on the named working rules. This entry records the reminder and runs no test.
- **Sources (SOURCE):** Arch notes, note 26 and its proposed register reminder; R12 D-CONC-3 and the paragraph identifying the working core.

### R-13. Implementation language

- **Chosen for now (SOURCE):** none for the new repository. The archived code is Rust; that does not select the implementation language for the new repository.
- **Set aside (SOURCE):** nothing yet. The owner directed research, not a language choice.
- **Put back to the owner (PROPOSED):** when the web round's synthesis has been reviewed, and before the first evaluator code is written in the new repository.
- **Sources (SOURCE):** `_relay\inputs\owner-record-2026-11-12-host-language-web-round.json` (SHA-256 `8a808233139b70aad24fdb83cdb7896c1e9630e12852068efa5d5929bffc4ff5`), with its authenticated answer binding in the 12 November table above.
