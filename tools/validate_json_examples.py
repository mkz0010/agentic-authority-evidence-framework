#!/usr/bin/env python3
"""Validate JSON example files.

This validator intentionally performs JSON syntax validation only.
Schema validation, cross-reference validation, and controlled vocabulary
validation are explicit follow-up concerns.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    examples_root = repo_root / "examples"

    if not examples_root.exists():
        print("No examples directory found.")
        return 0

    example_files = sorted(examples_root.rglob("*.example.json"))

    if not example_files:
        print("No *.example.json files found.")
        return 0

    errors: list[str] = []

    for path in example_files:
        try:
            with path.open("r", encoding="utf-8") as handle:
                json.load(handle)
        except json.JSONDecodeError as exc:
            rel = path.relative_to(repo_root)
            errors.append(f"{rel}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")
        except OSError as exc:
            rel = path.relative_to(repo_root)
            errors.append(f"{rel}: could not read file: {exc}")

    if errors:
        print("JSON example validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"JSON example validation passed for {len(example_files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
