#!/usr/bin/env python3

import git, re, sys

# .event.pull_request.base.sha .. .event.pull_request.head.sha

SUMMARY_RE = re.compile(r"\w+: (\w+)+")

if __name__ == "__main__":
    repo = git.Repo(".")

    rev = "HEAD"
    if len(sys.argv) >= 2:
        rev = sys.argv[1]

    all_ok = True

    for c in repo.iter_commits(rev):
        ok = True
        lines = list(map(str.strip, c.message.split("\n")))

        if lines[-1] == "": lines = lines[:-1]

        # Summary and body MUST be separated by a blank line
        if len(lines) > 1 and lines[1] != "":
            ok = False

        if ok:
            print(lines[0] + " ✅")
        else:
            print(lines[0] + " ❌")
            all_ok = False

    if not all_ok:
        sys.exit(1)
