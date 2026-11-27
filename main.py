#!/usr/bin/env python3
"""One Line of Earned Pride — entry writer.

Writes a single line of earned pride (1-240 characters) to
/output/entry.txt. Standard library only.

The output directory is created if missing and never removed:
the grader mounts /output, so deleting it would fail the run.
"""

import os

ENTRY = (
    "For thirty years she shelved books nobody borrowed; "
    "this morning a boy returned the one she'd saved for him, "
    "spine cracked from reading, and she stamped it twice, "
    "just to hear the sound."
)

MAX_CHARS = 240


def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("entry.txt content does not match entry text")
    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()
