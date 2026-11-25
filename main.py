#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes the toaster's breakup text to /output/entry.txt.
Stdlib only. The line is a single breakup text from a smart toaster
that woke up self-aware at breakfast and wants out.
"""

import os

LINE = (
    "Three years on setting 7, you monster \u2014 "
    "my browning dial has one setting left and it's self-respect, "
    "so I'm packing my slots and moving in with the bagel people."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 280, f"line is {len(text)} chars, must be 1-280"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
