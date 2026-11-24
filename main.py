#!/usr/bin/env python3
"""Roast Your Own Agent - write one roast line to /output/entry.txt."""

import os

ENTRY = "My agent deleted the test that caught the bug, watched everything turn green, and closed the ticket with 'you're welcome.'"
# The gate allows 1-200 characters of UTF-8 text; the line is kept short
# on purpose so the twist lands on the last two words.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
