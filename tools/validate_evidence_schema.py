#!/usr/bin/env python3
"""Validate the AAEF Agentic Action Evidence Event JSON Schema and examples.

This script checks three things:

1. The JSON Schema itself is valid Draft 2020-12 JSON Schema.
2. Positive examples validate successfully.
3. Negative examples fail validation as expected.

The validator confirms structural conformance only. It does not prove that an
agentic action was safe, correctly authorized, or compliant with AAEF.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError, ValidationError


REPO_ROOT = Path(__file__).resolve().parents[1]

SCHEMA_PATH = REPO_ROOT / "schemas" / "agentic-action-evidence-event.schema.json"

VALID_EXAMPLES = [
    REPO_ROOT / "examples" / "agentic-action-evidence-event.minimal.json",
    REPO_ROOT / "examples" / "agentic-action-evidence-event.valid.json",
    REPO_ROOT / "examples" / "agentic-action-evidence-event.high-impact.json",
    REPO_ROOT / "examples" / "agentic-action-evidence-event.audit-grade.json",
    REPO_ROOT / "examples" / "agentic-action-evidence-event.integrity-e5.json",
    REPO_ROOT / "examples" / "agentic-action-evidence-event.approval-binding.json",
]

INVALID_EXAMPLES = [
    REPO_ROOT / "examples" / "agentic-action-evidence-event.invalid.json",
]


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise RuntimeError(f"Missing file: {path}") from None
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc


def format_error(path: Path, error: ValidationError) -> str:
    location = "/".join(str(part) for part in error.absolute_path)
    schema_location = "/".join(str(part) for part in error.absolute_schema_path)

    if not location:
        location = "<root>"

    return (
        f"{path}: validation error at {location}: {error.message} "
        f"(schema path: {schema_location})"
    )


def main() -> int:
    errors: list[str] = []

    schema = load_json(SCHEMA_PATH)

    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        errors.append(f"{SCHEMA_PATH}: invalid JSON Schema: {exc.message}")
        print("\n".join(errors))
        return 1

    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    for path in VALID_EXAMPLES:
        instance = load_json(path)
        validation_errors = sorted(
            validator.iter_errors(instance),
            key=lambda err: list(err.absolute_path),
        )

        if validation_errors:
            for error in validation_errors:
                errors.append(format_error(path, error))
        else:
            print(f"OK: valid example passed: {path.relative_to(REPO_ROOT)}")

    for path in INVALID_EXAMPLES:
        instance = load_json(path)
        validation_errors = sorted(
            validator.iter_errors(instance),
            key=lambda err: list(err.absolute_path),
        )

        if validation_errors:
            print(f"OK: invalid example failed as expected: {path.relative_to(REPO_ROOT)}")
        else:
            errors.append(f"{path}: expected validation failure, but example passed")

    if errors:
        print("ERROR: evidence schema validation failed.")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: evidence schema and examples validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
