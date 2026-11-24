#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry.

Writes one line of an out-of-office auto-reply (at most 140 characters)
to /output/entry.txt. The line was picked from 8 candidates scored against
the judge brief's criteria in order, and won its 1v1 comparisons: it reads
exactly like the standard "until further notice" auto-reply a real person
would set, then turns on itself with a clean recursion.
"""

import os

ENTRY = "Out of office until further notice \u2014 further notice is also out of office."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 140


def validate_entry() -> None:
    """Enforce the brief's gate: 1-140 chars, one line, not only whitespace."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("read-back mismatch: /output/entry.txt != ENTRY")


if __name__ == "__main__":
    main()
