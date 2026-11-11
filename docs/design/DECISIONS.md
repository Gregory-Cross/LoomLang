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

## To reconsider

Each item names what was chosen for now, what was set aside, and when to put it back to the owner. Whoever reaches a trigger raises it with Claude A, who puts it to the owner.

### R-1. O3 outcome A: taking back what a failed part held

- **Chosen for now:** B. A catcher may go on only if the failed part held nothing or handed it back in its result; otherwise the failure carries on with the value held and named.
- **Set aside:** A. The catcher may take back what the failed part held, using a new trusted take operation and live-slot bookkeeping in compiled programs.
- **Put A back to the owner when any of these happens:**
  1. the declared-residue test of RECOVERY-A section 6 fails or is inconclusive;
  2. real programs show that unplanned failures while holding live values are common;
  3. before any rule letting a catcher return after a failed part held a live value is drafted (handlers arrive in slice 2);
  4. at the latest, at the slice 2 review.
- **Sources:** `2026-11-11-CLAUDE-ARCH-RECOVERY-A\REPORT.md` sections 5 to 7; the O3 owner record above.

### R-2. The backend beyond generated C

- **Chosen for now:** generated C, for the first compiled demo.
- **Set aside:** Cranelift, LLVM, or an emitter of our own.
- **Put back to the owner when:** the C route's qualification fails at a stage; a run-time build in slice 2 proves too costly under C; or slice 5's second target is planned.
- **Sources:** `2026-11-11-CLAUDE-ARCH-BACKEND-TRIAGE-R2\REPORT.md`; the C-route plan revisions.
