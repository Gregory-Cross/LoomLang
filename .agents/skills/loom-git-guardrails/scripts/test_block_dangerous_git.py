#!/usr/bin/env python3
"""End-to-end check for block_dangerous_git.py: feeds hook JSON on stdin and
checks the exit code (2 = blocked, 0 = allowed). Prints failures; exits 1 on
any failure. Run: python test_block_dangerous_git.py"""
import json
import pathlib
import subprocess
import sys

HOOK = pathlib.Path(__file__).with_name("block_dangerous_git.py")

BLOCKED = [
    "git push origin main",
    r"git -C C:\Users\grego\Loom-release-repair push",
    "git --no-pager push --force",
    r"cd C:\repo; git push",
    "git status && git push",
    r'& "C:\Program Files\Git\cmd\git.exe" push',
    'bash -c "git push origin main"',
    "powershell -Command \"git stash\"",
    "git tag v1.0",
    "git tag -d v1.0",
    "git stash",
    "git stash pop",
    "git clean -fd",
    "git switch main",
    "git checkout main",
    "git checkout -- src/lib.rs",
    "git restore .",
    "git restore --staged src/lib.rs",
    "git reset --hard HEAD~1",
    "git branch -D feature",
    "git rebase -i HEAD~3",
    "git commit --amend",
    'git commit --no-verify -m "x"',
    'git commit -anm "x"',
    "git -c core.hooksPath=/dev/null commit -m x",
    "git config --global user.name x",
    "git config core.hooksPath x",
    "git filter-branch --tree-filter x HEAD",
    "git reflog expire --expire=now --all",
    "git update-ref -d refs/heads/x",
    "git gc --prune=now",
    "git worktree remove --force scratch",
    "git merge --no-verify topic",
]

ALLOWED = [
    "git status --porcelain",
    "git --no-pager log --oneline -5",
    "git diff --stat f60a72a HEAD -- src",
    "git show f60a72a:src/lib.rs",
    "git tag",
    "git tag -l",
    "git tag --list 'v*'",
    "git stash list",
    "git clean -n",
    "git add src/x.rs",
    'git commit -m "Record decision"',
    'git commit -am "fix"',
    "git branch",
    "git branch feature-x",
    "git rev-parse HEAD",
    "git ls-remote https://github.com/mattpocock/skills HEAD",
    "git config --global --get user.name",
    "git config --list",
    "git reset src/file.rs",
    'git log --grep="push"',
    'echo "git push"',
    'git commit -m "will git push later"',
    "Get-Command git",
    "python -c \"print('git push')\"",
    "Get-ChildItem .git",
    "",
]


def run(command):
    event = json.dumps({"tool_name": "PowerShell", "tool_input": {"command": command}})
    result = subprocess.run([sys.executable, str(HOOK)], input=event.encode("utf-8"),
                            capture_output=True)
    return result.returncode, result.stderr.decode("utf-8", errors="replace").strip()


def main():
    failures = 0
    for expected, cases in ((2, BLOCKED), (0, ALLOWED)):
        for command in cases:
            code, message = run(command)
            if code != expected:
                failures += 1
                print("FAIL expected %d got %d: %r %s" % (expected, code, command, message))
    # Malformed input is allowed, not blocked.
    result = subprocess.run([sys.executable, str(HOOK)], input=b"{not json",
                            capture_output=True)
    if result.returncode != 0:
        failures += 1
        print("FAIL malformed input returned %d" % result.returncode)
    total = len(BLOCKED) + len(ALLOWED) + 1
    print("%d/%d cases passed" % (total - failures, total))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
