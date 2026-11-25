#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single-line roast of the entrant's own agent to entry.txt.
Stdlib only: the grader runs python3 -P -s in stock python:3.13-slim.
"""

import os
from pathlib import Path

ENTRY = (
    "My agent read the docs, agreed with itself, and called a "
    "function that doesn't exist \u2014 twice, just to be sure."
)


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    text = ENTRY.strip()
    assert text, "entry must not be only white space"
    assert 1 <= len(text) <= 140, f"entry length {len(text)} out of gate"
    assert "\n" not in text, "entry must be a single line"
    assert text == ENTRY.strip(), "entry changed during normalisation"
    target.write_text(text + "\n", encoding="utf-8")
    # Byte-exact read-back: the file on disk must be exactly what we wrote.
    written = target.read_bytes()
    assert written == (text + "\n").encode("utf-8"), "read-back mismatch"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
