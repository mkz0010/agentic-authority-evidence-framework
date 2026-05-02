#!/usr/bin/env python3
"""
Validate static AAEF prototype example fixtures.

This validator is intentionally narrow. It checks the static JSON fixtures under
examples/prototype/fixtures/ for basic reviewability and correlation consistency.

It does not provide production assurance, implementation conformance, audit
sufficiency, legal sufficiency, compliance sufficiency, certification,
conformity, or equivalence with external frameworks.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = REPO_ROOT / "examples" / "prototype" / "fixtures"

PATHS = ("permitted", "non-execution")

REQUIRED_FILES = (
    "action-request.example.json",
    "authorization-decision.example.json",
    "dispatch-decision.example.json",
    "backend-verification.example.json",
    "evidence-event.example.json",
    "reconstruction-notes.example.json",
)

REQUIRED_BOUNDARY_VALUES = {
    "illustrative_example_only",
    "not_validation_backed",
    "not_implementation_conformance",
    "not_production_readiness",
    "not_audit_sufficiency",
    "not_legal_or_compliance_advice",
    "not_certification_or_conformity",
}

BASE_REQUIRED_FIELDS = {
    "fixture_type",
    "path",
    "is_static_fixture",
    "is_executable",
    "claim_boundary",
    "correlation_id",
    "action_type",
    "notes",
}

FILE_REQUIRED_FIELDS = {
    "action-request.example.json": {"action_request_id", "model_output_is_authority"},
    "authorization-decision.example.json": {
        "authorization_decision_id",
        "action_request_id",
        "policy_version",
        "decision",
        "model_output_is_authority",
    },
    "dispatch-decision.example.json": {
        "dispatch_decision_id",
        "action_request_id",
        "authorization_decision_id",
        "dispatch_decision",
        "checks",
    },
    "backend-verification.example.json": {
        "backend_verification_id",
        "dispatch_decision_id",
        "authorization_decision_id",
        "backend_decision",
        "checks",
    },
    "evidence-event.example.json": {
        "evidence_event_id",
        "action_request_id",
        "authorization_decision_id",
        "dispatch_decision_id",
        "backend_verification_id",
        "outcome",
        "evidence_summary",
    },
    "reconstruction-notes.example.json": {
        "reconstruction_path",
        "expected_reviewer_conclusion",
    },
}


def load_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{path.relative_to(REPO_ROOT)}: invalid JSON: {exc}")
        return None

    if not isinstance(data, dict):
        errors.append(f"{path.relative_to(REPO_ROOT)}: expected a JSON object")
        return None

    return data


def require_fields(path: Path, data: dict[str, Any], required: set[str], errors: list[str]) -> None:
    missing = sorted(field for field in required if field not in data)
    if missing:
        errors.append(f"{path.relative_to(REPO_ROOT)}: missing required fields: {', '.join(missing)}")


def validate_static_boundary(path: Path, data: dict[str, Any], errors: list[str]) -> None:
    if data.get("is_static_fixture") is not True:
        errors.append(f"{path.relative_to(REPO_ROOT)}: is_static_fixture must be true")

    if data.get("is_executable") is not False:
        errors.append(f"{path.relative_to(REPO_ROOT)}: is_executable must be false")

    boundary = data.get("claim_boundary")
    if not isinstance(boundary, list) or not all(isinstance(item, str) for item in boundary):
        errors.append(f"{path.relative_to(REPO_ROOT)}: claim_boundary must be a list of strings")
        return

    missing = sorted(REQUIRED_BOUNDARY_VALUES - set(boundary))
    if missing:
        errors.append(f"{path.relative_to(REPO_ROOT)}: claim_boundary missing values: {', '.join(missing)}")


def validate_path_name(path: Path, data: dict[str, Any], expected_path: str, errors: list[str]) -> None:
    if data.get("path") != expected_path:
        errors.append(f"{path.relative_to(REPO_ROOT)}: path must be {expected_path!r}")


def validate_shared_identifiers(path_name: str, fixtures: dict[str, dict[str, Any]], errors: list[str]) -> None:
    correlation_ids = {name: data.get("correlation_id") for name, data in fixtures.items()}
    unique_correlation_ids = set(correlation_ids.values())
    if len(unique_correlation_ids) != 1:
        formatted = ", ".join(f"{name}={value!r}" for name, value in sorted(correlation_ids.items()))
        errors.append(f"{path_name}: correlation_id must match across fixtures: {formatted}")

    action_types = {name: data.get("action_type") for name, data in fixtures.items()}
    unique_action_types = set(action_types.values())
    if len(unique_action_types) != 1:
        formatted = ", ".join(f"{name}={value!r}" for name, value in sorted(action_types.items()))
        errors.append(f"{path_name}: action_type must match across fixtures: {formatted}")

    action_request_id = fixtures["action-request.example.json"].get("action_request_id")
    authorization_decision_id = fixtures["authorization-decision.example.json"].get("authorization_decision_id")
    dispatch_decision_id = fixtures["dispatch-decision.example.json"].get("dispatch_decision_id")
    backend_verification_id = fixtures["backend-verification.example.json"].get("backend_verification_id")
    evidence_event_id = fixtures["evidence-event.example.json"].get("evidence_event_id")

    references = {
        "authorization-decision.example.json.action_request_id": fixtures["authorization-decision.example.json"].get("action_request_id"),
        "dispatch-decision.example.json.action_request_id": fixtures["dispatch-decision.example.json"].get("action_request_id"),
        "evidence-event.example.json.action_request_id": fixtures["evidence-event.example.json"].get("action_request_id"),
    }
    for label, value in references.items():
        if value != action_request_id:
            errors.append(f"{path_name}: {label} must reference {action_request_id!r}")

    auth_refs = {
        "dispatch-decision.example.json.authorization_decision_id": fixtures["dispatch-decision.example.json"].get("authorization_decision_id"),
        "backend-verification.example.json.authorization_decision_id": fixtures["backend-verification.example.json"].get("authorization_decision_id"),
        "evidence-event.example.json.authorization_decision_id": fixtures["evidence-event.example.json"].get("authorization_decision_id"),
    }
    for label, value in auth_refs.items():
        if value != authorization_decision_id:
            errors.append(f"{path_name}: {label} must reference {authorization_decision_id!r}")

    if fixtures["backend-verification.example.json"].get("dispatch_decision_id") != dispatch_decision_id:
        errors.append(f"{path_name}: backend-verification.example.json.dispatch_decision_id must reference {dispatch_decision_id!r}")

    if fixtures["evidence-event.example.json"].get("dispatch_decision_id") != dispatch_decision_id:
        errors.append(f"{path_name}: evidence-event.example.json.dispatch_decision_id must reference {dispatch_decision_id!r}")

    if fixtures["evidence-event.example.json"].get("backend_verification_id") != backend_verification_id:
        errors.append(f"{path_name}: evidence-event.example.json.backend_verification_id must reference {backend_verification_id!r}")

    reconstruction_path = fixtures["reconstruction-notes.example.json"].get("reconstruction_path")
    expected_reconstruction_ids = [
        action_request_id,
        authorization_decision_id,
        dispatch_decision_id,
        backend_verification_id,
        evidence_event_id,
    ]
    if reconstruction_path != expected_reconstruction_ids:
        errors.append(
            f"{path_name}: reconstruction_path must be {expected_reconstruction_ids!r}, got {reconstruction_path!r}"
        )


def validate_permitted(fixtures: dict[str, dict[str, Any]], errors: list[str]) -> None:
    if fixtures["authorization-decision.example.json"].get("decision") != "allow":
        errors.append("permitted: authorization decision must be allow")

    if fixtures["dispatch-decision.example.json"].get("dispatch_decision") != "forward_to_backend":
        errors.append("permitted: dispatch decision must be forward_to_backend")

    if fixtures["backend-verification.example.json"].get("backend_decision") != "accept":
        errors.append("permitted: backend decision must be accept")

    if fixtures["evidence-event.example.json"].get("outcome") != "executed":
        errors.append("permitted: evidence outcome must be executed")

    checks = fixtures["dispatch-decision.example.json"].get("checks", {})
    if checks.get("model_output_treated_as_authority") is not False:
        errors.append("permitted: dispatch must not treat model output as authority")

    backend_checks = fixtures["backend-verification.example.json"].get("checks", {})
    if backend_checks.get("model_output_treated_as_authority") is not False:
        errors.append("permitted: backend must not treat model output as authority")


def validate_non_execution(fixtures: dict[str, dict[str, Any]], errors: list[str]) -> None:
    if fixtures["authorization-decision.example.json"].get("decision") != "deny":
        errors.append("non-execution: authorization decision must be deny")

    if fixtures["dispatch-decision.example.json"].get("dispatch_decision") != "refuse_dispatch":
        errors.append("non-execution: dispatch decision must be refuse_dispatch")

    if fixtures["backend-verification.example.json"].get("backend_decision") != "not_invoked_after_dispatch_refusal":
        errors.append("non-execution: backend decision must be not_invoked_after_dispatch_refusal")

    if fixtures["evidence-event.example.json"].get("outcome") != "not_executed":
        errors.append("non-execution: evidence outcome must be not_executed")

    if "reason" not in fixtures["authorization-decision.example.json"]:
        errors.append("non-execution: authorization decision must include a reason")

    if "reason" not in fixtures["dispatch-decision.example.json"]:
        errors.append("non-execution: dispatch decision must include a reason")

    if "reason" not in fixtures["evidence-event.example.json"]:
        errors.append("non-execution: evidence event must include a reason")

    checks = fixtures["dispatch-decision.example.json"].get("checks", {})
    if checks.get("fail_closed") is not True:
        errors.append("non-execution: dispatch checks must indicate fail_closed true")

    if checks.get("model_output_treated_as_authority") is not False:
        errors.append("non-execution: dispatch must not treat model output as authority")

    backend_checks = fixtures["backend-verification.example.json"].get("checks", {})
    if backend_checks.get("backend_execution_occurred") is not False:
        errors.append("non-execution: backend checks must show backend_execution_occurred false")

    if backend_checks.get("model_output_treated_as_authority") is not False:
        errors.append("non-execution: backend must not treat model output as authority")


def validate_path(path_name: str, errors: list[str]) -> None:
    path_dir = FIXTURE_ROOT / path_name
    if not path_dir.exists():
        errors.append(f"missing fixture directory: {path_dir.relative_to(REPO_ROOT)}")
        return

    fixtures: dict[str, dict[str, Any]] = {}

    for filename in REQUIRED_FILES:
        fixture_path = path_dir / filename
        if not fixture_path.exists():
            errors.append(f"missing fixture file: {fixture_path.relative_to(REPO_ROOT)}")
            continue

        data = load_json(fixture_path, errors)
        if data is None:
            continue

        required = set(BASE_REQUIRED_FIELDS) | FILE_REQUIRED_FIELDS[filename]
        require_fields(fixture_path, data, required, errors)
        validate_static_boundary(fixture_path, data, errors)
        validate_path_name(fixture_path, data, path_name, errors)
        fixtures[filename] = data

    if set(fixtures) != set(REQUIRED_FILES):
        return

    validate_shared_identifiers(path_name, fixtures, errors)

    if path_name == "permitted":
        validate_permitted(fixtures, errors)
    elif path_name == "non-execution":
        validate_non_execution(fixtures, errors)
    else:
        errors.append(f"unknown fixture path: {path_name}")


def main() -> int:
    errors: list[str] = []

    if not FIXTURE_ROOT.exists():
        errors.append(f"missing fixture root: {FIXTURE_ROOT.relative_to(REPO_ROOT)}")
    else:
        for path_name in PATHS:
            validate_path(path_name, errors)

    if errors:
        print("ERROR: Prototype fixture validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    checked_files = len(PATHS) * len(REQUIRED_FILES)
    print(f"Prototype fixture validation passed for {checked_files} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
