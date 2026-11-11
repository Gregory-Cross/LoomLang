---
name: loom-owner-questionnaire
description: Turn the open decisions only the owner can make into one plain-language questionnaire with a recommendation per question, then record the answers exactly. Selects nothing itself.
---

# Owner decision questionnaire

Adapted from mattpocock/skills `to-questionnaire` (MIT); the pin and changes are in [PROVENANCE.md](PROVENANCE.md).

Use this when work is blocked on decisions that only the owner can make. The owner holds authority, not the lane's detail: write for a capable reader who has not followed it.

**Find facts yourself; ask only decisions.** Collect the decisions from the bound sources (reviews, HANDOFFs, decision records) and settle every factual question from source first. A question a reviewer or the source can answer does not go to the owner.

1. **Name the decisions.** For each: the one choice needed, its source (path and SHA-256 prefix), what it blocks, and who acts on the answer. Done when every item is a single decision, not a topic.
2. **Draft the questionnaire** from the template below. Order questions by what their answers unblock, most first; group under `##` themes only when there are more than four. Done when each listed decision has exactly one question.
3. **Deliver it.** Write `QUESTIONNAIRE.md` and a `HANDOFF.md` with SHA-256 hashes in a fresh `C:\Users\grego\.codex\reviews\<YYYY-MM-DD>-<ROLE>-OWNER-QUESTIONNAIRE-<SLUG>\` folder: never in the repository and never as a ZIP. In an interactive session the same questions may be asked with the session's question tool instead; the record in step 4 is still required. Done when the owner has the questions.
4. **Record the answers exactly.** Write the questions and answers verbatim, what was selected and what was not, and route the record to whoever writes the repository decision record (normally Codex A, coordinated by Claude A). "Explain this more simply" and "You decide" are answers, not selections. An answer authorizes only what its question asked. Done when the record exists with hashes.

## Question rules

- Plain words first: two or three sentences on what is happening and why it matters, before any Loom term. Define each term at first use or link its source.
- One decision per question. Give two to four short options, the recommended one first and marked "(Recommended)" with a one-line reason.
- Say what each option changes and what it leaves undecided.
- Always allow "Explain this more simply" and "You decide (take the recommendation)".
- No option grants authority beyond its question: push, phase advancement, limit changes and adoption need their own explicit question.

## Template

<questionnaire-template>

# <Decision title in plain words>

**Purpose:** the decision and what it unblocks.
**From:** <role>, **To:** the owner, **How your answers will be used:** <who records them; what changes>
**Sources:** <paths and SHA-256 prefixes>

## Context

One short paragraph someone new to the lane can follow.

## How to answer

Reply with an option letter or in your own words. "Explain this more simply" or "You decide" are fine. Partial answers help; nothing here is decided until you answer.

## <Theme>

### 1. <Question in plain words>

<Two or three sentences: what it is and why it matters now.>

- **A. <Option> (Recommended):** <what it changes>. Why: <one line>.
- **B. <Option>:** <what it changes>.
- **Not decided here:** <adjacent choices that stay open>.

> Answer:

## Anything else?

Anything we didn't ask that you want considered?

</questionnaire-template>

When the owner says a message did not land, use [loom-wait-what](../loom-wait-what/SKILL.md).
