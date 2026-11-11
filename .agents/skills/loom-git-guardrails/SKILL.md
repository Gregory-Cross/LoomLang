---
name: loom-git-guardrails
description: Install or check the Claude Code hook that blocks git commands Loom reserves for the owner (push, tag, stash, clean, branch switches, history rewrites, hook bypass). Installing it changes Claude settings and needs the owner's approval.
---

# Loom git guardrails

Adapted from mattpocock/skills `git-guardrails-claude-code` (MIT); the pin and changes are in [PROVENANCE.md](PROVENANCE.md).

[`scripts/block_dangerous_git.py`](scripts/block_dangerous_git.py) is a Claude Code PreToolUse hook. It reads the tool call, finds each `git` invocation in a Bash or PowerShell command (including `git -C …`, full paths to `git.exe`, chained commands, and `bash -c`/`powershell -Command`/`Invoke-Expression` strings), and blocks owner-reserved operations with exit code 2 and a reason. It turns AGENTS.md's prose rule ("push, tag, stash, clean, branch switches, destructive … actions require applicable owner authorization"; never skip hooks) into a mechanical check.

## What it blocks

| git command | Blocked | Still allowed |
|---|---|---|
| `push` | always | — |
| `tag` | create, delete, sign, force | `git tag`, `-l/--list`, `-v/--verify` |
| `stash` | everything else | `stash list`, `stash show` |
| `clean` | everything else | `-n`/`--dry-run` |
| `switch`, `checkout`, `restore` | always (branch switches, discarded or unstaged changes) | — |
| `reset` | `--hard`, `--merge`, `--keep` | `--soft`, mixed, pathspec forms |
| `branch` | `-D/-d/--delete`, `-M/-m/--move`, `-C`, `-f/--force` | listing, creating |
| `rebase`, `filter-branch`, `filter-repo`, `update-ref` | always | — |
| `commit` | `--amend`, `-n` in a short-option cluster | ordinary commits |
| any subcommand | `--no-verify`; `-c core.hooksPath=…` | — |
| `config` | `--global`/`--system` writes; `core.hooksPath` writes | `--get…`, `--list`, `get`, `list` |
| `reflog`, `gc`, `worktree` | `reflog expire/delete`; `gc --prune…`; `worktree prune`, `worktree remove --force` | other forms |

It is a guardrail, not a sandbox. Commands hidden in scripts, aliases, variables, `Start-Process` argument lists or other languages are not parsed. Mixed `git reset` without a pathspec still unstages the whole index: leave it to the single repository writer. Codex has its own approval policy; this hook covers Claude Code only.

## Steps

1. **Get the owner's approval and scope.** Installing changes Claude settings. Ask which file: project-shared `C:\Users\grego\Loom-release-repair\.claude\settings.json` (tracked, applies to every Claude session in this repository), project-personal `.claude\settings.local.json`, or user-wide `C:\Users\grego\.claude\settings.json` (all projects). Done when the owner names one.
2. **Verify the script first.** Run `python .agents/skills/loom-git-guardrails/scripts/test_block_dangerous_git.py`. Done when it reports every case passed.
3. **Add the hook.** Merge into the chosen file's `hooks.PreToolUse` array; keep all other settings. Use an absolute path, because hook commands on Windows may not expand `$CLAUDE_PROJECT_DIR`:

   ```json
   {
     "hooks": {
       "PreToolUse": [
         {
           "matcher": "Bash|PowerShell",
           "hooks": [
             {
               "type": "command",
               "command": "python \"C:/Users/grego/Loom-release-repair/.agents/skills/loom-git-guardrails/scripts/block_dangerous_git.py\""
             }
           ]
         }
       ]
     }
   }
   ```

4. **Check it live.** In a new session, ask Claude to run `git stash list` (allowed) and `git push --dry-run` (must be refused with the BLOCKED message). Done when both behave as stated.
5. **Customizing.** Edit `check_git` in the script, add a case to the test file, rerun step 2, and note the change in PROVENANCE.md.

Removing the entry from the settings file disables the hook. An owner-approved exception is best run by the owner directly.
