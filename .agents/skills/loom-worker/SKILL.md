---
name: loom-worker
description: Execute and hand off a bounded Loom subagent assignment under a selected role; not a primary scheduling workflow.
---

# Bounded worker protocol

Use the selected role's responsibility and the parent's task card together.
The card must identify the worktree, pinned inputs, allowed reads, exclusive
writes (if any), permitted commands, expected output, verification and stop
condition. Verify supplied identities before relying on them; mismatch returns
`BLOCKED_SNAPSHOT_MISMATCH`. Missing scope or authority returns `NEEDS_PARENT`.

Read each selected skill completely, then only its relevant references. The
parent includes required instruction dependencies in the allowed read scope.
If a necessary source, skill or reference is unavailable or outside that scope,
return the exact missing dependency; do not silently skip it or expand the card.
Skill discovery/availability does not establish that its body was loaded.

Skills supply methods, not permissions. Keep the narrower applicable role/card
boundary and inherited host restrictions. A read-only role cannot use a writing
skill to edit or generate receipts. Required but disallowed operations go back
to the parent; identify their affected conclusion and continue independent
permitted work. Do not pretend a partial procedure completed its required gates.
Leaf roles never delegate. A session directly assigned a card may give one-level
leaf work under loom-delegate, unless its card forbids it. Only an explicitly
authorized direct Astra `loom_coordinator` at high or higher effort may use the
wider envelope in docs/tooling/LOOM_SUBAGENT_ROLES.md. Neither model capability
alone nor loading a skill grants that authority. Descendants remain leaves.

No Git mutation, installation, network/MCP use, global/toolchain/approval changes
or permission escalation. Read-only roles do not run builds, tests or package
managers. A finisher runs only exact commands assigned by the parent verification
plan. A coordinator may execute only its root-assigned commands or delegate an
allowed subset; it cannot expand the verification plan. Writers use `apply_patch`,
preserve unrelated bytes and the real index, and
writes only exclusive assigned paths or explicitly assigned scratch outputs.
Docs-only work never authorizes Rust edits. No automatic retry/model ladder.

Return status (`COMPLETE`, `PARTIAL`, `NEEDS_PARENT`, `BLOCKED_SNAPSHOT_MISMATCH`
or `BLOCKED`), the direct result, exact evidence, checks performed/omitted,
uncertainty and changed paths (or none). For writes, return patch/postimage hashes
and preservation evidence; distinguish source inspection from test execution.
Use the role/card output bound; report omitted scope rather than silently
truncating. Do not grade yourself or create delegation telemetry records.
Coordinators additionally return child cards, requested routes, delivery identities,
checks and omissions to the primary for integration and verification. Performance
scoring/logging is paused; do not create extra records for it.
No worker grants adoption, conformance, independent acceptance, freeze or phase
authority; the primary verifies evidence and checks the applicable decisions.
