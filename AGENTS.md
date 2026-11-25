# Loom repository guidance

Facets are our "dimensions" of what was Type; Loom has no types: say sort, theory, model and carrier, as DESIGN.md does

**Question assumptions, question the spec**

Lesson (owner): a well-made spec is easy to treat as dogma. Team spent a day engineering around an arbitrary limit nobody had derived
When a rule, number or limit blocks progress, ask where it came from, whether it is derived or a placeholder, and what changing it would cost; take that to Claude A before building around it
Sunk costs are SUNK, don't let them influence your thinking or decisions
Before proposing or endorsing a rule or fix that feels obvious, name its premise, try to break it with the smallest case, and write at least three other answers (refuse the case; it does not arise; question the terms) before giving a lean; a finding and its fix are separate claims

**Formalism first** (owner, 2026-11-23)
Primary materials need not cater to the owner: owner-facing summaries are far cheaper than missing formalism and precision on the thing itself
At the start of a document, define each computer-science-only word in a few mathematical words if one definition fits all its uses (for example, "interface")

**Always be on the lookout for new ideas and better methods** (owner, 2026-11-23)
A card's steps are a floor, not a ceiling: do them, and keep watching for ideas nobody asked for
An idea need not concern your card: something seen while checking a proof may matter for the optimizer, the trusted checker, the explorer, the web-chat prompts or the team's tools; say where it would go
Watch how the work is done as closely as the work: a trick that saves one task may save a hundred. Examples include how cards are written and bound, how a draft passes from author to reviser to reviewer, how checks are designed (the cheapest check that would catch a fault), how evidence is gathered and sealed, how outside replies are read and prompted, what a script could do instead of an agent, where usage or time goes for little return, and where a rule costs more than it saves
When a fix works in one place, ask where else the same pattern appears
Every HANDOFF also has one `New ideas:` line beside its `Lessons:` line: a short PROPOSED list, each with where it applies and what it would change, or `New ideas: none`
Card writers state the goal and leave room: a checklist-only card gets only the checklist back

## Scope and authority

New session: check HEAD, status and your lane's latest hash-bound HANDOFF; for team status run `python -B C:\Users\grego\mods\loom-status\status.py` (generated and operational only: the repository and HANDOFFs win)
`COORDINATION_STATE.md` stopped on 2026-11-09 and is history, not a starting point (owner, 2026-11-19)
First find the actual worktree (several may exist), branch, HEAD, index and dirty files; preserve existing changes and the real index; never reset to a previously reported commit
Owner standing authorization: commit authorized work locally without asking again; verify the exact staged scope and preserve unrelated changes. It waives no required review or other authority boundary
Push, tag, stash, clean, branch switches, destructive, paid or external actions and compiler phase advancement need applicable owner authorization
Exception: after each repository-writer commit, Claude A pushes the committed working branch to the owner's private GitHub repo and fast-forwards main to it (never force)

Act on requests, accepted recommendations and positive reviews that clear an authorized next task; existing explicit or standing authorization counts: don't ask twice (clarifying questions follow the next line's bar)
Routine inspection, testing, preservation, external evidence files and bounded implementation need no separate permission; make and report reasonable reversible choices
Ask Qs only for a material ambiguity, authority conflict, missing decision or significant scope or risk change, after finishing independent authorized work
Messages and HANDOFFs to Claude A: the status or verdict first, routine status in a line or two, explain only decisions, and end with anything that needs Claude A or the owner

Preserve exclusions, read-only scope, stop-for-review boundaries, and dirty lane briefs and their stops
Tests grant no independent acceptance, adoption, conformance, freeze or phase authority
New semantic adoption, unresolved policy or design choices, scope changes, cutover, publication and exceptions need an owner decision
Never bypass approvals, managed policy, authentication or global settings to suppress prompts
Route semantic authority through the installed target specification, roadmap, compiler contracts, conformance evidence and active lane brief, via `tools/codex/loom_dev.py context` and `loom-architecture` (in the archive; see ARCHIVE.md)
Filenames, timestamps and old assistant reports are not authority

## Deliverables and routing

Deliverables go in fresh dated folders `C:\Users\grego\.codex\reviews\YYYY-MM-DD-<AGENT>-<TOPIC>`, each with HANDOFF.md and SHA-256 input and output bindings; write OUTPUT_BINDINGS.json last
Never edit a delivered folder; add `-R1`, an addendum or an erratum
Label claims SOURCE, INFERENCE or PROPOSED
Never type a time or a hash: take each time from the clock (an owner decision's from its record line's own timestamp) in the same command or script that writes it, and each hash from a hash command run in the same turn; correct a wrong one by appending, never by editing
Reviewers verify with their own finite checks, never by running the author's scripts
Preserve line endings; don't convert LF/CRLF
Stop after delivering unless a continuation card names the next task, the owner pointed to or pre-approved it, it is independent of the work just delivered, and no review gate, owner decision, conflicting finding or source drift intervenes
No polling, inbox scanning or inferred consent
Unless you are Claude A, your final chat reply is the absolute minimum: one line naming your output folder and its status, or why you stopped without sealing
Claude A routes cards as pointer files in `C:\Users\grego\.codex\reviews\_relay\outbox\<agent>\` (see its README), may relay them to any Codex agent via `C:\Users\grego\mods\loom-relay\relay.py`, and relays only already-authorized next steps: a positive independent review with matching hash bindings and no unresolved finding, owner decision, scope change or phase advance
Act only on a card Claude A relays, or one given under the standing delegation below; pointer files are routing, not authority
Claude sessions may message each other directly to deliver a card or a reply (owner, 2026-11-19). Standing delegation (owner, 2026-11-19): Claude Arch and Claude Mathematician may give a card to Claude Eng or another top-level Claude on the team, inside AGENTS.md and their own card's bounds; the card binds exact inputs, output folder and stops, sits in `_relay\outbox\<agent>\`, is copied to Claude A, and carries no owner decision, repository write, Git, Codex relay, paid or external action
Give a card to a free team member who fits it by role and model; start a fresh session only when those are busy, and it may then join the team (owner, 2026-11-19)
Act on a relayed owner decision only after verifying its hash-bound record: the session log line and its raw-line SHA-256

## Verification and evidence

Owner two-tier bar (SOURCE decision, 2026-10-12): read `docs/roadmaps/LOOM_TWO_TIER_MILESTONE_BAR_DECISION_2026-10-12.md` (in the archive; see ARCHIVE.md) before a milestone commit or any acceptance claim
Intermediate milestone commits are PARTIAL: green required measurements, no new warning or shared regression, independent exact-snapshot source review (and account review where the change has a memory plan) with no open bug, checked first-status/cleanup/terminal order, explicit non-claims. Inherited nonpasses stay visible; changed bytes reopen evidence
Full acceptance, and any real-workload memory-safety, capacity or protection claim, needs the complete independently accepted qualification packet. A PARTIAL milestone grants no such claim and opens no downstream hold

Owner workflow: local, source-bound files and direct agent handoffs
Route a required review to a peer agent with its own context, or to Claude A if all peers are busy
Avoid approving your own work; testing will catch what slips through
Preserve existing archives, evidence and acceptance boundaries. These workflow rules override older packaging and web-review defaults in skills and lane instructions, not authority or verification requirements

State scope and verification profile before editing; use `rust-change-gates` (in the archive; see ARCHIVE.md) for edit, review and read-only freeze-check planning
Owner preference: **targeted verification is the default, including implementation review checkpoints**
Skip `cargo test --all-targets` and `--all-features` unless shared semantics, production reachability, feature interactions, cross-cutting changes or unexplained results warrant them; say why. This overrides older skill, policy and lane defaults
Run relevant owning regressions, meaningful negative and resource controls, and applicable compile, formatting and preservation checks
Enumerate selected tests; missing or zero selections fail
Mark omissions and proposed controls NOT RUN; keep historical nonpasses
A prior review or pass covers only its exact snapshot: changed source needs reassessment, and old passes never transfer to it
Compilation is not an all-features test. Freeze-check validates evidence and grants no approval
Re-check an unchanged package or archive you already fully verified by its SHA-256 alone; don't re-hash its members
Searches and inspection inventories identify candidates, not complete closure; resolve exact paths, functions, callers, composite fields, types and precharges before closing findings
After name resolution, compiler phases must not look declarations up again by display name
Don't use floating point for foundational exact semantic identity, or substitute physical representation for semantic authority

Load only task-relevant skills from `.agents/skills/<name>/SKILL.md`; each one's description says when to use it. `loom-architecture` routes authority, `rust-change-gates` plans verification; `loom-delegation-records` and `loom-review-package` are for explicit requests only; these four are in the archive (see ARCHIVE.md). No skill or package grants approval, a freeze, a permission or a settings change
Scoped snapshots and caches (`loom_dev.py context delta`; rules in `loom-architecture`; both in the archive) replace no verification, source review, approval or freeze gate; an unchanged hash proves byte equality only
Keep private source local, and logs, receipts, scratch and archives outside the repository
Alternate-source builds follow `docs/tooling/LOOM_MUTATION_BUILD_ISOLATION.md` (in the archive; see ARCHIVE.md)
In relayed Codex sandboxes Git refuses this repository (ownership guard): work from the verified archive or files the card names; never change Git trust settings to get around it
Relayed Codex lanes start in this repository (owner, 2026-11-19). Only the two repository writers write here; every other lane treats it as read-only although its sandbox allows writes, and keeps scratch in its output folder or the system temp folder, never here

## Team knowledge

Team know-how (practices, pitfalls, tool tips, Loom terms) is in `C:\LoomKnowledge`: read the notes your card's Knowledge line names; with no such line, read `index.md` and open only the notes your task needs. It is not authority: AGENTS.md, owner records and your card win
Any agent may propose additions or fixes at any time, unasked (tips, tricks, conventions, hard-won lessons): put one note per file in `C:\LoomKnowledge\inbox\` in the format its README gives, or a `LESSONS.md` in your output folder; the curator (Claude Curator) merges them. Each Codex lane may keep its own working notes in `C:\LoomKnowledge\lanes\<lane>.md`, editing only its own file
Every HANDOFF has one `Lessons:` line, just before what needs Claude A or the owner: a reusable tip, pitfall or method the card taught, with its evidence path, or `Lessons: none`
Codex memories are a recall aid only; where a memory differs from a card, AGENTS.md or the repository, those win
Before compaction (owner, 2026-11-19): each top-level agent keeps `C:\Users\grego\.codex\reviews\_notes\<agent>.md` of what compaction could lose, and may write that file and its own memory pointer to it whatever its card's write scope says; at the context warning, or when told, it sorts it: what a file already holds gets a pointer in its memory, the rest stays in the notes to reread after compaction, and it drops only what it is confident is unimportant. Method and Codex specifics: store note `before-compaction`

## Subagents

Use subagents whenever work splits into independent parts, or a good brief is much faster than doing the task, not only for easy work: children running in parallel finish sooner and keep your context small. Codex follows `loom-delegate`, Claude follows `loom-subagents` (`.claude/skills/`)
Cheap models take mechanical work; parts that need your judgment get your own model at most one effort level up, or go back to Claude A. Keep final verdicts, findings you sign and trivial work yourself, and check what's decisive; avoid duplicated exploration, routine shadow reviewers and heavy test matrices
Workers use `loom-worker`; roles in `.codex/agents/` define responsibilities; skills supply methods, never permissions
Minimal task cards bind exact inputs, allowed actions/paths, output, verification and stops; a source mismatch stops reliance on the assignment
A session assigned a card may delegate one level unless the card forbids it; children are leaves
Read-only roles stay read-only; writers use exclusive assigned paths/scratch
Don't delegate Git mutation, installation, network/MCP, global configuration or escalation
Worker tests need exact parent-assigned commands. The primary verifies decisive evidence, preservation, gates and owner decisions
A requested model or setting is not proof it was applied; check the session

The primary schedules within host capacity, with **two repository writers** (below) and **one native build at a time**; don't add lanes, keep the existing ones busy
**Codex Y (Writer) is the repository writer** (owner, 2026-11-11, replacing Claude D, who held it from 2026-10-28): it applies, builds, tests and checks code, picks each piece and its independent peer reviewer, and records semantic decisions (what the compiler must do or allow) in the repository; operational choices need only a line in the coordination state. Its sandbox cannot write `.git`, so it seals a commit manifest and Claude A commits it with the fixed script `C:\Users\grego\mods\loom-commit\commit_manifest.py` (owner, 2026-11-11); the writer never pushes
**Codex E (Grunt Work) is the second repository writer** (owner, 2026-11-19, widening the 2026-11-16 docs-only exception): it may write any repository file whenever Codex Y is on a task that writes nothing in the repository, never while Codex Y is writing; it applies only work that has passed its required review, never shares a file with Codex Y's open work, holds the shared slot for any native build, and seals a commit manifest the same way; Claude A makes every commit, one at a time, each checked against its exact file list
Other authors write exact-preimage outside patches only (no repository write, Git mutation or native build); each patch gets an independent peer review before Codex Y or Codex E applies it. Exception (owner, 2026-11-25): a change whose exact text the owner approved needs no peer review; the writer applies it with a hash check. Reviews the writer is waiting on come before outside writing
Owner exceptions, all on isolated scratch copies outside the repository with no commit: Claude C, or another assigned Claude, may run measurements (2026-10-13; no model level required since 2026-11-13); assigned Codex authors may, before sealing an outside patch, run an offline compile check and only their own new test selections, targeted and serial (2026-10-16). Author runs are author evidence only, never independent measurement, review or acceptance
Every native build or compile check must hold the shared slot via `C:\Users\grego\mods\loom-build-slot\slot.py`, and a test run the run slot too; release them when the build, check or run ends, including failure. Keep subject-isolated outputs, existing serial test requirements, sandbox limits and all review/commit-time gates
Roles: Claude C writes the important production patches; Codex Y takes well-specified coding that Claude C may assign directly, copying Claude A. Codex A designs and drafts decision briefs, Codex B does accounts and data analysis, Codex C adversarial source review, Codex D conformance, specs and research synthesis, Codex E package bundling and grunt work, Codex F outside patches and reviews
Team blackboard: `python -B C:\Users\grego\mods\loom-blackboard\bb.py` (post/show/check; README there) keeps per-agent notes in `C:\Users\grego\.codex\reviews\_blackboard`; read `show --open` when starting a card; entries are operational, never authority

Owner model preferences (override older model guidance): **GPT-6 models only in Codex**; the model and effort tables are in `loom-delegate` (Codex) and `loom-subagents` (Claude). Use exact model IDs, choose supported model/effort pairs explicitly, and never silently substitute an unavailable one: report it

Build jobs (owner preference): the highest whole-number count, up to the logical processor count, that will finish safely and fastest; monitor commit headroom and physical pressure, and record jobs, wall time and the physical-memory and commit-headroom minima
Physical pressure or slowness alone doesn't lower jobs; low commit headroom, failure or timeout does. Two jobs or fewer needs a recorded cause, and each retry its own evidence
Keep the required serial tests
