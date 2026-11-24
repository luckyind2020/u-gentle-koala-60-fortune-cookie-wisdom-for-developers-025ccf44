"""Fortune Cookie Wisdom for Developers — entry runner.

Reads the single fortune line from entry.txt, validates it against the
bounty gate (1-120 characters of UTF-8 text), prints it, and writes it to
/output/entry.txt for the sealed scorer when that directory exists.
"""

import os
import sys


def load_line(path):
    with open(path, "r", encoding="utf-8") as handle:
        raw = handle.read()
    lines = [part for part in raw.splitlines() if part.strip()]
    if len(lines) != 1:
        raise ValueError(f"entry.txt must hold exactly one line, found {len(lines)}")
    return lines[0].strip()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        line = load_line(os.path.join(here, "entry.txt"))
    except ValueError as problem:
        print(problem, file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 120:
        print(f"entry must be 1-120 characters, got {len(line)}", file=sys.stderr)
        return 1
    print(line)
    out_dir = "/output"
    if os.path.isdir(out_dir):
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
            handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
