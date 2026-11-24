#!/usr/bin/env python3
"""Print the entry line for Roast Your Own Agent."""

from pathlib import Path


def main() -> int:
    entry = Path(__file__).resolve().parent / "entry.txt"
    print(entry.read_text(encoding="utf-8").strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
