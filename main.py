#!/usr/bin/env python3
"""Two Days of Quiet Dread (make.fun).

Writes the entry -- one code review comment that approves a pull request with quiet existential dread --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Approved. The code works, the tests pass, and I have never been more certain that something is quietly wrong."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
