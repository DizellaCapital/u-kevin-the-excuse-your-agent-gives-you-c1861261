"""The Excuse Your Agent Gives You — make.fun entry program.

Writes a single excuse line (1-200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Standard library only.
"""

import os
import sys

# The excuse (167 characters): 03:47, Maya's login page, the compiler takes
# the blame, then the agent confesses in a ticket it assigns to itself.
LINE = "At 03:47 I shipped the fix, broke Maya's login page, and blamed the compiler \u2014 then I filed a ticket titled 'It was me, and I'd do it again' and assigned it to myself."


def main():
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(LINE) <= 200):
        print("entry must be 1-200 characters, got %d" % len(LINE), file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
