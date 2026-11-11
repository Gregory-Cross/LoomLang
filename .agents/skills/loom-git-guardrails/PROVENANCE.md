# Provenance: loom-git-guardrails

**Upstream:** https://github.com/mattpocock/skills, commit `d81f3a183412e71a5b1e84ca21bc1a35eea03a60` (resolved with `git ls-remote` and a shallow clone on 2026-10-02). It is not installed through the plugin or `npx skills`, and nothing updates automatically.

**License:** MIT, Copyright (c) 2026 Matt Pocock. The full text is in [LICENSE-upstream.txt](LICENSE-upstream.txt) (SHA-256 `4981c5f6a90eb3a969dacabb9350f5a75695ff3910b39b6534952908dfdc5ff7`). Loom's changes are under the same notice.

| Upstream file | SHA-256 | Exact copy |
|---|---|---|
| `skills/misc/git-guardrails-claude-code/SKILL.md` | `12d335b84bcf984b213b527014262233f27ffa1eb807db466832ff711b96f41f` | `upstream/SKILL.md.orig` |
| `skills/misc/git-guardrails-claude-code/agents/openai.yaml` | `9151961c68ab52e07e2463df15e8ff7c9331c3b7afbf716c3461623f87c57c14` | `upstream/openai.yaml.orig` |
| `skills/misc/git-guardrails-claude-code/scripts/block-dangerous-git.sh` | `bb5dc3a96ae81924ff3b88b959979b4eb68b7810f6fa9bd395fb8f781e0d8c12` | `upstream/block-dangerous-git.sh.orig` |

## Loom changes

- **Ported** from bash + `jq` + `grep -E` to Python (`scripts/block_dangerous_git.py`). It now works for PowerShell as well as Bash commands (matcher `Bash|PowerShell`) on this Windows machine, with no `jq` dependency.
- **Command-aware parsing** replaces substring regexes. The hook skips git's global options (`-C`, `-c`, `--git-dir`, …), recognizes full `git.exe` paths and chained commands, and scans `bash -c`/`powershell -Command`/`Invoke-Expression` strings. Arguments that merely contain words such as `push` (`git log --grep=push`) are no longer blocked.
- **Block list extended** to AGENTS.md's owner-reserved operations: tag creation and deletion, stash, every clean except dry runs, `switch`, all `checkout`/`restore`, `rebase`, history-rewrite tools, `update-ref`, `commit --amend`, `--no-verify` and `commit -n`, `core.hooksPath` overrides, global and system config writes, reflog expiry, `gc --prune`, and forced worktree removal. Read-only forms stay allowed.
- **Install steps** rewritten for Loom: owner approval first, an absolute path in the hook command, a test script (`scripts/test_block_dangerous_git.py`, 60 cases), and a live check.
- **Codex metadata:** implicit invocation disabled, matching Loom's other skills.

## Updating

Never update in place from upstream. To consider a newer upstream:
1. Clone the new commit into scratch space outside the repository.
2. Diff it against `upstream/*.orig`.
3. Port the wanted changes deliberately and rerun the test script.
4. Replace the `.orig` copies, and update this file's commit and hashes.
