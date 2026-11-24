"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse (131 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. Deterministic: the same bytes on every run.
"""

import os
import sys

EXCUSE = (
    "I kept the deadline in my context window so I wouldn't forget it. "
    "It took up the whole window. There was no room left for the work."
)


def validate(text):
    """Gate: UTF-8 text of 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be str")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry = validate(EXCUSE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)
    # Read-back verification: the file on disk must be byte-identical
    # to the validated entry, otherwise the run is not trustworthy.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != entry:
        raise RuntimeError("read-back mismatch: file differs from entry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
