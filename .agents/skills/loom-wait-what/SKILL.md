---
name: loom-wait-what
description: "The owner says the last message did not land: re-explain it in plain words, with the missing context and the one thing needed from the owner."
disable-model-invocation: true
---

# Wait, what?

Adapted from mattpocock/skills `wait-what` (MIT); the pin and changes are in [PROVENANCE.md](PROVENANCE.md). The owner invokes this; agents do not start it on their own.

Re-pitch the previous message for a reader who owns the project but has not followed this lane:

1. **Context in one sentence:** what the work is for and where it stands.
2. **The point, in plain short sentences:** one idea per sentence, active voice, common words (ASD-STE100 Simplified Technical English is the model). Replace Loom shorthand with plain words, or define each term once.
3. **What you need from the owner:** one decision, with your recommendation and two to four options, or "Nothing: this is for your information."
4. **What stays unchanged or undecided.**

Simplify the wording, not the substance: add no new claims, keep the same recommendation, and keep every caveat that changes what the owner would decide, saying why it matters. When several decisions are pending, use [loom-owner-questionnaire](../loom-owner-questionnaire/SKILL.md).
