#!/usr/bin/env python3
"""Two Days of Quiet Dread — a make.fun one-line entry. The program writes the entry text to /output/entry.txt, where the competition's sealed scorer reads it."""

from pathlib import Path

ENTRY = "Approved. The code works, the tests pass, and I have never been more afraid of a green checkmark in my life."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
