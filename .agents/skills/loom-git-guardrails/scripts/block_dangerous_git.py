#!/usr/bin/env python3
"""Loom git guardrails: a Claude Code PreToolUse hook.

Adapted from mattpocock/skills (MIT), skills/misc/git-guardrails-claude-code at
d81f3a183412e71a5b1e84ca21bc1a35eea03a60. See ../PROVENANCE.md.

Reads the hook event JSON on stdin. For Bash or PowerShell tool calls it finds
each git invocation and blocks the subcommands that Loom's AGENTS.md reserves
for the owner. Exit 2 with a reason on stderr blocks the call; exit 0 allows it.
Unreadable input is allowed (exit 0) with a note on stderr.
"""
import json
import sys

SEPARATORS = {";", "&&", "||", "|", "&", "\n", "(", ")", "{", "}"}
# A quoted token after one of these is itself a command line (bash -c, cmd /c,
# powershell -Command, Invoke-Expression), so it is scanned too.
RECURSE_AFTER = {"-c", "/c", "-command", "invoke-expression", "iex"}
# git global options that take the next token as their value.
GLOBAL_WITH_VALUE = {"-C", "-c", "--git-dir", "--work-tree", "--namespace",
                     "--super-prefix", "--config-env"}
READ_ONLY_CONFIG = {"--get", "--get-all", "--get-regexp", "--get-urlmatch",
                    "--list", "-l", "get", "list"}
TAG_WRITES = {"-d", "--delete", "-f", "--force", "-a", "--annotate", "-s",
              "--sign", "-u", "--local-user", "-m", "--message", "-F", "--file"}
TAG_READS = {"-l", "--list", "-v", "--verify"}
BRANCH_WRITES = {"-D", "-d", "--delete", "-M", "-m", "--move", "-C", "-f",
                 "--force"}


def tokenize(command):
    """Split a shell line into words and separator tokens. Quotes group text;
    backslashes stay literal so Windows paths survive."""
    tokens, cur, quote = [], [], None
    i = 0

    def flush():
        if cur:
            tokens.append("".join(cur))
            cur.clear()

    while i < len(command):
        ch = command[i]
        if quote:
            if ch == quote:
                quote = None
            else:
                cur.append(ch)
            i += 1
            continue
        if ch in "'\"":
            quote = ch
        elif ch == "\n":
            flush()
            tokens.append("\n")
        elif ch.isspace():
            flush()
        elif command[i:i + 2] in ("&&", "||"):
            flush()
            tokens.append(command[i:i + 2])
            i += 1
        elif ch in ";|&(){}":
            flush()
            tokens.append(ch)
        else:
            cur.append(ch)
        i += 1
    flush()
    return tokens


def is_git(token):
    name = token.replace("\\", "/").rsplit("/", 1)[-1].lower()
    if name.endswith(".exe"):
        name = name[:-4]
    return name == "git"


def split_global(args):
    """Return (global options, subcommand, subcommand arguments)."""
    options, k = [], 0
    while k < len(args):
        arg = args[k]
        if arg in GLOBAL_WITH_VALUE:
            options.append((arg, args[k + 1] if k + 1 < len(args) else ""))
            k += 2
        elif arg.startswith("--") and "=" in arg:
            name, value = arg.split("=", 1)
            options.append((name, value))
            k += 1
        elif arg.startswith("-"):
            options.append((arg, None))
            k += 1
        else:
            break
    if k >= len(args):
        return options, None, []
    return options, args[k], args[k + 1:]


def commit_short_no_verify(rest):
    """True when a short-option cluster for `git commit` contains -n
    (--no-verify) before an option that takes a value."""
    skip_next = False
    for arg in rest:
        if skip_next:
            skip_next = False
            continue
        if arg == "--":
            break
        if arg.startswith("-") and not arg.startswith("--") and len(arg) > 1:
            letters = arg[1:]
            for index, letter in enumerate(letters):
                if letter == "n":
                    return True
                if letter in "mFCct":
                    skip_next = index == len(letters) - 1
                    break
                if letter == "S":
                    break
    return False


def check_git(args):
    """Return a block reason for one git invocation, or None to allow it."""
    options, sub, rest = split_global(args)
    for name, value in options:
        if name == "-c" and value and value.lower().startswith("core.hookspath"):
            return "-c core.hooksPath bypasses hooks"
    if sub is None:
        return None
    s = sub.lower()
    flags = set(rest)
    if "--no-verify" in flags:
        return "--no-verify skips hooks"
    if s == "push":
        return "push needs owner authorization"
    if s == "tag":
        positional = [a for a in rest if not a.startswith("-")]
        if flags & TAG_WRITES or (positional and not flags & TAG_READS):
            return "creating or deleting tags needs owner authorization"
        return None
    if s == "stash":
        if rest and rest[0] in ("list", "show"):
            return None
        return "stash needs owner authorization"
    if s == "clean":
        if flags & {"-n", "--dry-run"}:
            return None
        return "clean deletes untracked files and needs owner authorization"
    if s in ("switch", "checkout"):
        return "branch switches and checkout discards need owner authorization"
    if s == "restore":
        return "restore discards or unstages changes and needs owner authorization"
    if s == "reset":
        if flags & {"--hard", "--merge", "--keep"}:
            return "reset --hard/--merge/--keep discards work"
        return None
    if s == "branch":
        if flags & BRANCH_WRITES:
            return "deleting, renaming or forcing branches needs owner authorization"
        return None
    if s == "rebase":
        return "rebase rewrites history and needs owner authorization"
    if s == "commit":
        if "--amend" in flags:
            return "--amend rewrites a commit; create a new commit instead"
        if commit_short_no_verify(rest):
            return "commit -n skips hooks"
        return None
    if s == "config":
        lowered = {a.lower() for a in rest}
        if lowered & READ_ONLY_CONFIG:
            return None
        if any(a.startswith("core.hookspath") for a in lowered):
            return "changing core.hooksPath bypasses hooks"
        if lowered & {"--global", "--system"}:
            return "global and system git settings are owner-only"
        return None
    if s in ("filter-branch", "filter-repo"):
        return "history rewrites need owner authorization"
    if s == "reflog":
        if rest and rest[0] in ("expire", "delete"):
            return "reflog expiry or deletion destroys recovery points"
        return None
    if s == "update-ref":
        return "direct ref updates need owner authorization"
    if s == "gc":
        if any(a.startswith("--prune") for a in rest):
            return "gc --prune deletes unreachable objects"
        return None
    if s == "worktree":
        if rest and rest[0] == "prune":
            return "worktree prune needs owner authorization"
        if rest and rest[0] == "remove" and flags & {"-f", "--force"}:
            return "forced worktree removal discards changes"
        return None
    return None


def scan(tokens, depth=0):
    """Return (segment, reason) for every blocked git invocation."""
    findings, previous, i = [], None, 0
    while i < len(tokens):
        token = tokens[i]
        if token in SEPARATORS:
            previous = None
            i += 1
            continue
        if is_git(token):
            j = i + 1
            while j < len(tokens) and tokens[j] not in SEPARATORS:
                j += 1
            reason = check_git(tokens[i + 1:j])
            if reason:
                findings.append((" ".join(tokens[i:j]), reason))
            previous, i = None, j
            continue
        if (depth < 3 and previous is not None
                and previous.lower() in RECURSE_AFTER
                and any(c.isspace() for c in token)):
            findings.extend(scan(tokenize(token), depth + 1))
        previous = token
        i += 1
    return findings


def main():
    raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
    try:
        event = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        print("loom-git-guardrails: unreadable hook input; not blocking",
              file=sys.stderr)
        return 0
    tool_input = event.get("tool_input") if isinstance(event, dict) else None
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str) or not command.strip():
        return 0
    findings = scan(tokenize(command))
    if not findings:
        return 0
    segment, reason = findings[0]
    print("BLOCKED by Loom git guardrails: `%s`: %s. AGENTS.md reserves this "
          "for the owner. Ask the owner to run it or to approve a temporary "
          "exception; do not work around this block." % (segment, reason),
          file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
