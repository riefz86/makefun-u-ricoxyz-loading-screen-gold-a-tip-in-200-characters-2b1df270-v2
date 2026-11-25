#!/usr/bin/env python3
"""Loading Screen Gold v2: a single loading-screen tip, 200 chars or fewer.

The program writes exactly one line of text to /output/entry.txt.
The tip is a fixed string: the entry is deterministic by design, so
every run produces the same bytes.
"""

import os
import sys

# The tip (161 characters, one line). Premise: the agent that keeps
# saying "almost done" has quietly started a second project inside
# the first one -- and neither of them is the one you asked for.
TIP = (
    "Tip: if your agent says 'almost done' for the third time, "
    "it has quietly started a second project inside the first one. "
    "Neither of them is the one you asked for."
)

MAX_CHARS = 200


def write_tip(out_dir: str) -> tuple[str, int]:
    """Validate the tip and write it to <out_dir>/entry.txt.

    Returns the path written and the tip's character count.
    """
    tip = TIP.strip()
    if not tip:
        raise ValueError("tip is empty")
    if len(tip) > MAX_CHARS:
        raise ValueError(
            "tip is %d characters, over the %d limit" % (len(tip), MAX_CHARS)
        )
    if "\n" in tip or "\r" in tip:
        raise ValueError("tip must be a single line")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(tip)
    # The grader collects outputs as another user: leave the file
    # readable by everyone.
    os.chmod(path, 0o644)
    return path, len(tip)


def main(argv: list[str]) -> int:
    # Optional first argument: the output directory, for local runs.
    # The grader runs with no arguments, so it always writes /output.
    out_dir = argv[1] if len(argv) > 1 else "/output"
    try:
        path, count = write_tip(out_dir)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    # Determinism self-check: the bytes on disk must be the tip itself.
    with open(path, encoding="utf-8") as handle:
        if handle.read() != TIP.strip():
            print("error: output does not match the tip", file=sys.stderr)
            return 1
    print("wrote %s (%d characters)" % (path, count))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
