---
name: loom-subagents
description: Use in a Loom Claude session whenever work splits into parts that can run at once, whenever briefing a task is much faster than doing it, and before a long read, a wide search or bulky mechanical work. Sends the work to subagents (cheap ones for mechanical work, your own model and effort for parts that need it) and checks what comes back. Keeps the session's context small and finishes sooner. Not for final verdicts, assigned reviews, measurement or commits.
---

# Subagents for Claude sessions

A subagent is more than a cheaper pair of hands for easy work. Use one when writing a good brief takes much less time than doing the task. Use one above all when the work splits into parts that don't wait on each other. Three children reading three packages finish in the time one would take, while you get on with your own part.

A child also saves twice. Its reading stays out of your context, and every later message of yours pays for that context, so you gain time now and usage later.

Hard work qualifies too. A well-briefed child on your own model and effort can work through one part of an analysis while you work through another. You keep the judgment that joins the parts.

Skip a child in three cases:
- the brief would take about as long as the work;
- nothing else can move until you have the result;
- you need the reading in your own context to judge it.

**Always name the model.** A `general-purpose` child inherits your model unless you say otherwise. That is why most past subagent use ran on the parent's Opus or Fable, even for rote work.

## What to send

- **Send:**
  - independent parts of a larger task, run side by side;
  - a first pass over one part of a hard question;
  - listing, counting, hashing and byte checks over many files;
  - finding where something is across many files;
  - reading a long document or package to pull out named facts;
  - summarizing a finished log;
  - checking a list of citations against their sources.
- **Keep:** the final verdict, findings you will sign, owner or authority questions, and the review or measurement your card gives you. A child may gather evidence or draft a part for these, but the judgment and the check stay yours. Also keep anything you could finish faster than you could brief it, and any read you need in your own context.

## Which child

| Work | Agent tool call |
|---|---|
| Purely rote, fully specified | `subagent_type: "rote-haiku"`, `effort: "high"` |
| Rote, where a slip is possible | `subagent_type: "rote-haiku"` (Haiku 5.5 at `max`, its own setting) |
| Finding things across many files | `subagent_type: "Explore"`, `model: "haiku"`, `effort: "xhigh"` |
| Bounded reading that needs some sense | `subagent_type: "general-purpose"`, `model: "haiku"`, `effort: "max"`, the cheap default; or `model: "sonnet"`, `effort: "low"` (`"medium"` when long) where nuance in reading or wording matters |
| The same, with intricate rules | `subagent_type: "general-purpose"`, `model: "opus"`, `effort: "low"` (owner, 2026-11-10: Opus 5.5 `low` dominates Sonnet `high` on the Artificial Analysis index); never Sonnet above `medium` |
| A part that needs your judgment | `subagent_type: "general-purpose"`, `model` set to your own, `effort` your own or one level up (for example `model: "fable"`, `effort: "xhigh"` from `high`) |
| The same, when the child needs your conversation | `subagent_type: "fork"`: it runs on your model and effort and carries your context, so it costs about what you do |

Owner, 2026-11-10: Haiku 5.5 is good at rote work, and at `max` it scores slightly above Sonnet `low` on the Artificial Analysis index at far less cost. Sonnet has strengths those benchmarks don't capture.

Set `effort` as the table says; this skill is the instruction the tool asks for. **Rule of thumb (owner, 2026-11-10): same model, at most one effort level up, or send it back to Claude A.** Send independent children in one message so they run at once, and keep working while they do.

Top-level Claude sessions (owner, 2026-11-09; moved from AGENTS.md) run Fable 5.2 (`claude-fable-5-2`) at `low` to `high`, or Opus 5.5 at `low` to `high` for cheaper work. When Fable usage runs very low, any Opus effort may stand in. Claude A sets this when it starts a lane; you don't change your own.

## The brief

The child knows only what you tell it. Give it one goal, exact paths, what you've already ruled out, and the output's shape and size limit. Ask for conclusions with paths and line numbers, not file dumps. Batch related questions into one child, and run independent ones in parallel.

Pass on your card's limits, plus these: read-only unless told to write one named file outside the repository; no Git mutation, builds, slots, network, settings changes or messages to other agents; delete or move nothing; stay out of `withheld\`, `ANSWERS\`, credential files and anything else the card excludes.

## Check before relying on it

Re-derive a sample yourself, such as a re-hash, a grep or a spot read, and check everything decisive in full. A child's word isn't evidence. If the sample fails, do that part yourself.

## What this doesn't change

- A child under you isn't an independent reviewer.
- Non-author measurements stay with Claude C, or a Claude on Fable `high`. Native builds and slots stay with the session holding the card.
- Commits stay with Claude D.

## Report

One line in your HANDOFF: what went to which child, and what you checked. No grades or telemetry.
