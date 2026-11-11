# Provenance: loom-owner-questionnaire

**Upstream:** https://github.com/mattpocock/skills, commit `d81f3a183412e71a5b1e84ca21bc1a35eea03a60` (resolved with `git ls-remote` and a shallow clone on 2026-10-02). It is not installed through the plugin or `npx skills`, and nothing updates automatically.

**License:** MIT, Copyright (c) 2026 Matt Pocock. The full text is in [LICENSE-upstream.txt](LICENSE-upstream.txt) (SHA-256 `4981c5f6a90eb3a969dacabb9350f5a75695ff3910b39b6534952908dfdc5ff7`). Loom's changes are under the same notice.

| Upstream file | SHA-256 | Exact copy |
|---|---|---|
| `skills/productivity/to-questionnaire/SKILL.md` | `77825120815c21400f82e2794faf342d1d1a4ab1493be3fe061857885d26b768` | `upstream/SKILL.md.orig` |
| `skills/productivity/to-questionnaire/agents/openai.yaml` | `0b5ed84d805809777a15371c946a70f98321e3c6400fce5fcd74df71d40e860b` | `upstream/openai.yaml.orig` |

## Loom changes

- **The recipient is fixed as the owner.** The questions target decisions only the owner can make, and agents settle facts from source first. Upstream instead interviews the user about the recipient and the gap.
- **The owner's decision style is built in:** plain words first; one decision per question; two to four options with the recommendation first and a reason; what each option changes and leaves open; "Explain this more simply" and "You decide" always allowed and recorded as answers, not selections.
- **Authority guard:** no option may grant authority beyond its question.
- **Delivery and records follow Loom's workflow:** a fresh `.codex\reviews` folder with SHA-256 hashes, never the repository and never a ZIP. Answers are recorded verbatim, selected and not selected, and routed to the repository record writer.
- **Template** gains Sources, recommended options and "Not decided here".
- **Model invocation is allowed**, because coordinating agents prepare owner decisions; Codex implicit invocation stays disabled.

## Updating

Never update in place from upstream. Clone a newer commit into scratch space, diff it against `upstream/*.orig`, port the wanted changes deliberately, and update this file's commit and hashes.
