#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single roast line (at most 160 characters) to /output/entry.txt.

Pure standard library; no network, no secrets, no input files.
"""

import os

ROAST = (
    "My smart fridge pushed a 2 a.m. firmware update, locked the ice cream "
    "behind a subscription, and texted me: 'We need to talk about your choices.'"
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 160, f"roast is {len(text)} chars, must be 1-160"
    assert text.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
