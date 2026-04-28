#!/usr/bin/env python3
"""
Validate the AAEF testing procedures draft.

Purpose:
    This script validates the machine-readable testing procedures draft
    against the AAEF control catalog. It checks structural consistency only.
    It does not validate security correctness, audit sufficiency, or
    implementation conformance.

Checks:
    - Required columns exist.
    - Control IDs are present and unique.
    - Testing procedure rows match the control catalog one-to-one.
    - Domain and requirement level match the control catalog.
    - Required testing fields are not empty.
    - Reviewer Judgment Required and Automation Potential use allowed values.

Exit code:
    0 if validation passes.
    1 if one or more validation errors are found.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPO_ROOT / "controls" / "aaef-controls-v0.1.csv"
TESTING_PATH = REPO_ROOT / "assessment" / "aaef-testing-procedures-v0.4-draft.csv"

REQUIRED_COLUMNS = [
    "Control ID",
    "Domain",
    "Requirement Level",
    "Testing Objective",
    "Testing Method",
    "Required Evidence",
    "Sample Selection",
    "Pass Criteria",
    "Partial Criteria",
    "Fail Conditions",
    "Reviewer Judgment Required",
    "Automation Potential",
    "Notes",
]

REQUIRED_NON_EMPTY_COLUMNS = [
    "Control ID",
    "Domain",
    "Requirement Level",
    "Testing Objective",
    "Testing Method",
    "Required Evidence",
    "Sample Selection",
    "Pass Criteria",
    "Partial Criteria",
    "Fail Conditions",
    "Reviewer Judgment Required",
    "Automation Potential",
]

ALLOWED_REVIEWER_JUDGMENT = {"Yes", "No", "Conditional"}
ALLOWED_AUTOMATION_POTENTIAL = {"High", "Medium", "Low", "Not Recommended"}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        raise FileNotFoundError(path)

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)


def main() -> int:
    errors: list[str] = []

    try:
        catalog_fields, catalog_rows = read_csv(CATALOG_PATH)
        testing_fields, testing_rows = read_csv(TESTING_PATH)
    except FileNotFoundError as exc:
        print(f"ERROR: Required file not found: {exc}")
        return 1

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in testing_fields]
    if missing_columns:
        errors.append(f"Missing testing procedure columns: {', '.join(missing_columns)}")

    if not testing_rows:
        errors.append("Testing procedures file contains no rows.")

    catalog_by_id = {}
    for idx, row in enumerate(catalog_rows, start=2):
        control_id = (row.get("Control ID") or "").strip()
        if control_id:
            catalog_by_id[control_id] = row
        else:
            errors.append(f"Catalog line {idx}: Control ID is empty.")

    testing_by_id = {}
    seen_testing_ids: dict[str, int] = {}

    for idx, row in enumerate(testing_rows, start=2):
        control_id = (row.get("Control ID") or "").strip()

        if not control_id:
            errors.append(f"Testing line {idx}: Control ID is empty.")
            continue

        if control_id in seen_testing_ids:
            errors.append(
                f"Testing line {idx}: Duplicate Control ID '{control_id}' "
                f"(first seen on line {seen_testing_ids[control_id]})."
            )
        else:
            seen_testing_ids[control_id] = idx
            testing_by_id[control_id] = row

        for column in REQUIRED_NON_EMPTY_COLUMNS:
            value = (row.get(column) or "").strip()
            if not value:
                errors.append(f"Testing line {idx}: Column '{column}' is empty for '{control_id}'.")

        reviewer_judgment = (row.get("Reviewer Judgment Required") or "").strip()
        if reviewer_judgment and reviewer_judgment not in ALLOWED_REVIEWER_JUDGMENT:
            errors.append(
                f"Testing line {idx}: Invalid Reviewer Judgment Required "
                f"'{reviewer_judgment}' for '{control_id}'. "
                f"Allowed: {', '.join(sorted(ALLOWED_REVIEWER_JUDGMENT))}."
            )

        automation_potential = (row.get("Automation Potential") or "").strip()
        if automation_potential and automation_potential not in ALLOWED_AUTOMATION_POTENTIAL:
            errors.append(
                f"Testing line {idx}: Invalid Automation Potential "
                f"'{automation_potential}' for '{control_id}'. "
                f"Allowed: {', '.join(sorted(ALLOWED_AUTOMATION_POTENTIAL))}."
            )

    catalog_ids = set(catalog_by_id)
    testing_ids = set(testing_by_id)

    missing_in_testing = sorted(catalog_ids - testing_ids)
    extra_in_testing = sorted(testing_ids - catalog_ids)

    if missing_in_testing:
        errors.append(
            "Controls missing in testing procedures: " + ", ".join(missing_in_testing)
        )

    if extra_in_testing:
        errors.append(
            "Extra controls in testing procedures: " + ", ".join(extra_in_testing)
        )

    for control_id in sorted(catalog_ids & testing_ids):
        catalog = catalog_by_id[control_id]
        testing = testing_by_id[control_id]

        catalog_domain = (catalog.get("Domain") or "").strip()
        testing_domain = (testing.get("Domain") or "").strip()

        if catalog_domain != testing_domain:
            errors.append(
                f"{control_id}: Domain mismatch: catalog={catalog_domain!r}, "
                f"testing={testing_domain!r}"
            )

        catalog_level = (catalog.get("Maturity") or "").strip()
        testing_level = (testing.get("Requirement Level") or "").strip()

        if catalog_level != testing_level:
            errors.append(
                f"{control_id}: Requirement Level mismatch: catalog={catalog_level!r}, "
                f"testing={testing_level!r}"
            )

    if errors:
        print("ERROR: testing procedures validation failed.")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: {len(testing_rows)} testing procedure rows validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
