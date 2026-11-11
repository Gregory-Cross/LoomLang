---
name: loom-delegate
description: Split a Codex card's work across subagents and check what comes back. Independent parts run at once, at your own model and effort when they need it, and bulky mechanical work goes to a cheap Terra leaf. Use it whenever work splits into parts or briefing a task is much faster than doing it. Also plan, dispatch and integrate larger Loom subagent work as the primary or an explicitly authorized direct Astra coordinator.
---

# Compose and delegate

## When a child pays

A subagent is more than a cheaper pair of hands for easy work. Use one when writing a good brief takes much less time than doing the task. Use one above all when the work splits into parts that don't wait on each other. Three children reading three packages finish in the time one would take, while you get on with your own part.

A child also saves twice. Its reading stays out of your context, and every later step of yours pays for that context, so you gain time now and usage later.

Hard work qualifies too. A well-briefed child at your own model and effort can work through one part while you work through another. You keep the judgment that joins the parts.

Skip a child in three cases:
- the brief would take about as long as the work;
- nothing else can move until you have the result;
- you need the reading in your own context to judge it.

AGENTS.md lets a session assigned a card delegate one level, unless the card forbids it.

- **Send:**
  - independent parts of a larger task, run side by side;
  - a first pass over one part of a hard question;
  - inventories, counts and hash tables over many files;
  - pulling named facts or passages out of long documents;
  - summarizing a finished log;
  - checking a list of citations against their sources;
  - mechanical tables or file sets built by exact rules.
- **Keep:** the final verdict, findings you will sign, owner or authority questions, and an independent review the card gives you. A child may gather evidence or draft a part for these, but the judgment and the check stay yours. Also keep anything you could finish faster than you could brief it.
- **Model:** set both model and effort on every spawn, because the fallback is Sol `xhigh`.
  - Mechanical work: `gpt-6.1-terra` at `low` when it is purely rote, at `medium` when anything in it could go wrong, and at `high` when the rules are intricate. Don't use `gpt-6-luna` (owner, 2026-11-10: not until a new version).
  - A part that needs your judgment: your own model, at your effort or one level up. **Rule of thumb (owner, 2026-11-10): same model, at most one effort level up, or send it back to Claude A.**
  - If a pair is refused, do the work yourself and say so; never substitute silently.
- **Run independent children at once,** and work on your own part while they run.
- **Keep the child small:** use `fork_turns="none"`. Give it one outcome, exact input paths or hashes, the output's shape and size limit, where it may write (its own scratch only), and this line: "You are a leaf: no subagents, Git, network, native builds, slots or repository writes." Batch related questions into one child. Don't pass it the card or this conversation.
- **Check before relying on it:** re-derive a sample with your own finite check, such as a re-hash, a regex or a spot read, and check everything decisive in full. A child's word is not evidence. If the sample fails, do that part yourself rather than stepping up through models.
- **Time:** waiting for children counts against your card's seal target. Children running in parallel usually shorten it.
- **Report:** one line in the HANDOFF: what went to which child, the requested model and effort (and the effective ones if exposed), and what you checked. No grades or telemetry.

The rest of this skill covers larger splits and the coordinator envelope.

## Larger splits

Use this workflow when useful independent work can run while the primary works.
Do not manufacture a split for a trivial tool operation or force every task
through every role. Keep tiny tasks local and batch related questions when that
saves context and integration work. The primary owns the team plan and may grant a direct Astra
coordinator the bounded delegation envelope in the role guide. Children and other
workers return scheduling needs; loading this skill does not grant delegation authority.

## Choose the entry point

- **Skill-first:** start from the requested workflow and its required outputs.
  Assign useful independent steps to suitable roles, and keep dependent steps
  ordered. For example, a documentation handoff may need an investigator's
  evidence before a finisher edits, followed by a reviewer checking that postimage.
- **Role-first:** start from one responsibility, such as reviewing a source-bound
  report. Load that role and only the procedures needed for its specific question.

Select from the [role guide](../../../docs/tooling/LOOM_SUBAGENT_ROLES.md).
Roles define responsibilities and boundaries; skills define methods. Choose a
supported model/effort pair separately using the table below and the guide. Named-role
pins can defeat explicit model selection, so the project roles are unpinned.
If the host lacks a named-role selector, read and pass the role instructions
explicitly, with selected skills and task card; do not claim native TOML loading
or sandbox application. Never invent spawn parameters or alter host permissions.

Owner model preferences (moved from AGENTS.md, 2026-11-09). GPT-6 models only:

| Model | Use | Efforts |
|---|---|---|
| `gpt-6-luna` | Not used until a new version (owner, 2026-11-10) | none |
| `gpt-6.1-terra` | Default for cheap subagents and bounded mechanical work: `low` for purely rote work, `medium` where anything could go wrong | `low`, `medium`, `high` |
| `gpt-6.1-sol` | Default workhorse: coding, tracing, specs and reviews. Raise effort with complexity | `low` to `max`, `ultra` |
| `gpt-6-astra` | Hardest reasoning, planning, debugging, architecture and proofs; or when speed matters | `high`, `xhigh`, `max`, `ultra` |

Prefer Sol two or three effort levels higher over Astra: it is competitive, just
slower. Use Astra when other critical work is waiting. A child follows the rule of
thumb above (same model, at most one effort level up, or back to Claude A). Use
`ultra` only when a card asks for it. Higher effort cannot fix missing inputs.

## Bind and dispatch

Give each assignment a unique task-instance ID and a compact task card:

- one concrete outcome and a few proportionate success criteria;
- exact worktree and scoped input hashes or a source-bound inventory;
- role, selected skill paths and the needed instruction/reference dependencies;
- allowed reads, exclusive writes or scratch outputs, and exact permitted commands;
- output/size limit, verification owner/scope, stop condition and material exclusions;
- requested model/effort and a short task-fit reason.

For a coordinator also bind its direct-parent identity, authorized child roles,
reserved team slots, writer-slot owner and transfer protocol, exact child command
allowlist, and the root-owned verification/acceptance boundary. Children receive
their parent task-instance ID and an explicit leaf/no-delegation restriction.

Include selected skill bodies or exact accessible paths; minimal context still
needs all applicable instructions. Do not include the whole conversation or
review archive. Use `fork_turns="none"` or verified minimal history. Reuse an
idle agent only when its existing context is relevant. Choose team size from
useful independent work, coordination cost and available host capacity; there is
no repository count cap. The one active repository writer may be the primary, coordinator or a
leaf, never two at once. Transfer the slot explicitly after the prior owner stops.
Keep heavy compiler matrices singular. Check open retained sessions as well as
active work; a host refusal is not permission to spawn around its cap. For a
transient model-capacity failure, the owner authorizes retrying the same still-useful
assignment with backoff while other work continues. Report material dispatch blockers;
check status before retrying and do not duplicate an active task or switch models
without a fresh selection decision.

Performance scoring/logging is paused by owner direction (2026-09-15). Do not
load the records workflow or create grading/telemetry events for ordinary tasks.
Keep route reasons in the normal task card. A coordinator supplies child cards
and exact results for integration, not grading. Historical analysis or explicit
resumption uses [loom-delegation-records](../loom-delegation-records/SKILL.md).
A source
mismatch stops the assignment; refresh its input authority before resuming.

## Integrate and verify

Read every changed path and decisive evidence. Check required answers, qualifiers,
preserved bytes and the assigned verification; passing tests alone do not establish
quality. Use [loom-source-evidence](../loom-source-evidence/SKILL.md) for material
claim checks and [rust-change-gates](../rust-change-gates/SKILL.md) for an applicable
verification plan. Required operations outside worker permissions stay with the
primary; a delegated report does not replace a mandatory gate.

Bind downstream tasks to the actual returned or integrated bytes. If the primary
changes a reviewed artifact, prior review covers only its earlier subject.
Retain the delivered artifact and relevant defects when repairing it; this is
ordinary engineering evidence, not a requirement for performance records.
Check applicable owner decisions and independent acceptance separately.
Only when a review package is requested or required, explicitly invoke
[loom-review-package](../loom-review-package/SKILL.md); do not package every task.
Finish with the result, checks/omissions and any actual blocker, not an invented
adoption, freeze, production or publication claim.
