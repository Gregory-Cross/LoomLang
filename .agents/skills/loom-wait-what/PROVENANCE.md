# Provenance: loom-wait-what

**Upstream:** https://github.com/mattpocock/skills, commit `d81f3a183412e71a5b1e84ca21bc1a35eea03a60` (resolved with `git ls-remote` and a shallow clone on 2026-10-02). It is not installed through the plugin or `npx skills`, and nothing updates automatically.

**License:** MIT, Copyright (c) 2026 Matt Pocock. The full text is in [LICENSE-upstream.txt](LICENSE-upstream.txt) (SHA-256 `4981c5f6a90eb3a969dacabb9350f5a75695ff3910b39b6534952908dfdc5ff7`). Loom's changes are under the same notice.

| Upstream file | SHA-256 | Exact copy |
|---|---|---|
| `skills/productivity/wait-what/SKILL.md` | `95393f96e730b20dabc6b425515cb6292d34bd9a91859a03c2c821e24d321112` | `upstream/SKILL.md.orig` |
| `skills/productivity/wait-what/agents/openai.yaml` | `e0d9beddf0093b3cf05de2722699affab5d240e5950469e208d59c1f0ed91bef` | `upstream/openai.yaml.orig` |

## Loom changes

- **Glossary dependency removed.** Upstream points to `GLOSSARY.md`/`GLOSSARY-MAP.md`, which Loom does not have. Terms are replaced with plain words or defined once instead.
- **Structure added:** one-sentence context; plain short sentences (ASD-STE100 kept as the model); what the owner must decide, with a recommendation and options, or "nothing, FYI"; what stays unchanged.
- **Substance guard:** simplify the wording, not the content. No new claims, the same recommendation, and decision-relevant caveats kept.
- **Pairing:** links to `loom-owner-questionnaire` for when several decisions are pending.
- **Unchanged from upstream:** owner-invoked only (`disable-model-invocation: true`; Codex implicit invocation disabled).

## Updating

Never update in place from upstream. Clone a newer commit into scratch space, diff it against `upstream/*.orig`, port the wanted changes deliberately, and update this file's commit and hashes.
