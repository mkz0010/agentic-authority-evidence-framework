#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "examples" / "evidence"
README = EVIDENCE_DIR / "README.md"

EXPECTED_EXAMPLES = {
    "permitted-action-evidence.example.json": "permitted_action",
    "non-execution-evidence.example.json": "non_execution",
}

REQUIRED_METADATA = {
    "example_status": {"illustrative_candidate"},
    "normative_status": {"non_normative"},
    "schema_conformance": {"not_asserted"},
    "implementation_conformance": {"not_asserted"},
    "evidence_sufficiency": {"not_asserted"},
}

REQUIRED_FALSE_CLAIM_BOUNDARIES = [
    "production_readiness",
    "implementation_conformance",
    "audit_sufficiency",
    "compliance",
    "certification",
    "conformity",
    "external_framework_equivalence",
]

README_REQUIRED_PHRASES = [
    "not production-ready",
    "not implementation conformance",
    "not audit sufficiency",
    "not compliance",
    "not certification",
    "not conformity",
    "not external-framework equivalence",
]

FORBIDDEN_STRING_PHRASES = [
    "production-ready",
    "certified",
    "audit sufficient",
    "legally sufficient",
    "equivalent to",
    "guarantees",
    "proves safety",
    "validated implementation",
]


def error(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> Any | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        error(errors, f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    except OSError as exc:
        error(errors, f"{path.relative_to(ROOT)}: cannot read file: {exc}")
    return None


def iter_strings(value: Any, path: str = "$") -> list[tuple[str, str]]:
    strings: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            strings.extend(iter_strings(nested, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            strings.extend(iter_strings(nested, f"{path}[{index}]"))
    elif isinstance(value, str):
        strings.append((path, value))
    return strings


def iter_ids(value: Any, path: str = "$") -> list[tuple[str, str, Any]]:
    ids: list[tuple[str, str, Any]] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            next_path = f"{path}.{key}"
            if key.endswith("_id") or key == "id":
                ids.append((next_path, key, nested))
            ids.extend(iter_ids(nested, next_path))
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            ids.extend(iter_ids(nested, f"{path}[{index}]"))
    return ids


def validate_readme(errors: list[str]) -> None:
    if not README.exists():
        error(errors, f"{README.relative_to(ROOT)}: missing evidence example README")
        return

    content = README.read_text(encoding="utf-8").lower()
    for phrase in README_REQUIRED_PHRASES:
        if phrase not in content:
            error(errors, f"{README.relative_to(ROOT)}: missing required claim-boundary phrase: {phrase!r}")


def validate_metadata(path: Path, data: dict[str, Any], expected_scenario_type: str, errors: list[str]) -> None:
    metadata = data.get("example_metadata")
    if not isinstance(metadata, dict):
        error(errors, f"{path.relative_to(ROOT)}: missing object field example_metadata")
        return

    scenario_type = metadata.get("scenario_type")
    if scenario_type != expected_scenario_type:
        error(
            errors,
            f"{path.relative_to(ROOT)}: example_metadata.scenario_type must be "
            f"{expected_scenario_type!r}, got {scenario_type!r}",
        )

    for field, allowed_values in REQUIRED_METADATA.items():
        value = metadata.get(field)
        if value not in allowed_values:
            allowed = ", ".join(sorted(repr(v) for v in allowed_values))
            error(errors, f"{path.relative_to(ROOT)}: example_metadata.{field} must be one of {allowed}, got {value!r}")

    boundaries = metadata.get("claim_boundaries")
    if not isinstance(boundaries, dict):
        error(errors, f"{path.relative_to(ROOT)}: example_metadata.claim_boundaries must be an object")
        return

    for field in REQUIRED_FALSE_CLAIM_BOUNDARIES:
        if boundaries.get(field) is not False:
            error(errors, f"{path.relative_to(ROOT)}: example_metadata.claim_boundaries.{field} must be false")


def validate_identifier_hygiene(path: Path, data: dict[str, Any], errors: list[str]) -> None:
    # Evidence examples may intentionally use null identifiers when a component was not invoked.
    # This is especially important for non-execution examples where backend verification may not exist.
    for id_path, key, value in iter_ids(data):
        if id_path.startswith("$.example_metadata."):
            continue
        if value is None:
            continue
        if not isinstance(value, str):
            error(errors, f"{path.relative_to(ROOT)}: {id_path} must be a string identifier or null")
        elif not value.strip():
            error(errors, f"{path.relative_to(ROOT)}: {id_path} must not be empty")

    correlated_keys = {
        "action_request_id",
        "authorization_decision_id",
        "dispatch_decision_id",
        "backend_verification_id",
        "evidence_event_id",
    }
    values_by_key: dict[str, set[str]] = {key: set() for key in correlated_keys}
    for _id_path, key, value in iter_ids(data):
        if key in correlated_keys and isinstance(value, str) and value.strip():
            values_by_key[key].add(value)

    for key, values in values_by_key.items():
        if len(values) > 1:
            error(
                errors,
                f"{path.relative_to(ROOT)}: inconsistent {key} values within example: {sorted(values)!r}",
            )


def validate_forbidden_claims(path: Path, data: dict[str, Any], errors: list[str]) -> None:
    for string_path, value in iter_strings(data):
        lower = value.lower()
        for phrase in FORBIDDEN_STRING_PHRASES:
            if phrase in lower:
                error(
                    errors,
                    f"{path.relative_to(ROOT)}: suspicious overclaiming phrase {phrase!r} found at {string_path}",
                )


def validate_examples(errors: list[str]) -> None:
    if not EVIDENCE_DIR.exists():
        error(errors, f"{EVIDENCE_DIR.relative_to(ROOT)}: evidence example directory is missing")
        return

    all_examples = sorted(EVIDENCE_DIR.glob("*.json"))
    for path in all_examples:
        if not path.name.endswith(".example.json"):
            error(errors, f"{path.relative_to(ROOT)}: evidence examples must use .example.json suffix")

    for filename, scenario_type in EXPECTED_EXAMPLES.items():
        path = EVIDENCE_DIR / filename
        if not path.exists():
            error(errors, f"{path.relative_to(ROOT)}: expected evidence example is missing")
            continue

        data = load_json(path, errors)
        if data is None:
            continue
        if not isinstance(data, dict):
            error(errors, f"{path.relative_to(ROOT)}: top-level JSON value must be an object")
            continue

        validate_metadata(path, data, scenario_type, errors)
        validate_identifier_hygiene(path, data, errors)
        validate_forbidden_claims(path, data, errors)


def main() -> int:
    errors: list[str] = []

    validate_readme(errors)
    validate_examples(errors)

    if errors:
        print("ERROR: Evidence example validation failed:")
        for item in errors:
            print(f"- {item}")
        return 1

    print("Evidence example validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
