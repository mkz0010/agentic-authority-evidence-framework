#!/usr/bin/env python3
"""
Validate the AAEF control catalog.

Purpose:
    This script is a lightweight quality gate for the machine-readable
    control catalog. It may be run from the repository root with
    `python tools/validate_control_catalog.py`; it also resolves the
    catalog path relative to this script, so it does not depend on the
    current working directory. It does not validate the security correctness of AAEF
    controls. It only checks structural consistency so that the catalog can
    be referenced, mapped, and reviewed reliably.

Checks:
    - Required columns exist.
    - Control IDs are present and unique.
    - Control IDs follow the expected AAEF-<DOMAIN>-NN format.
    - Domain codes are from the allowed domain set.
    - Domain names match domain codes.
    - Maturity values are valid.
    - Required fields are not empty.

Exit code:
    0 if validation passes.
    1 if one or more validation errors are found.

The script reports all detected errors before exiting so contributors can
fix multiple issues in one pass.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPO_ROOT / "controls" / "aaef-controls-v0.1.csv"

REQUIRED_COLUMNS = [
    "Control ID",
    "Domain",
    "Requirement",
    "Objective",
    "Applicability",
    "Testing Procedure",
    "Evidence Examples",
    "Maturity",
]

ALLOWED_DOMAINS = {
    "GOV": "Governance",
    "ID": "Agent Identity",
    "PRN": "Principal Binding",
    "DEL": "Delegation and Authority",
    "AUZ": "Action Authorization",
    "TOOL": "Tool and Action Boundary",
    "MEM": "Memory and Retrieval",
    "EVD": "Evidence and Auditability",
    "HUM": "Human Oversight",
    "RES": "Response and Revocation",
}

ALLOWED_MATURITY = {"Required", "Recommended", "Optional"}

CONTROL_ID_RE = re.compile(r"^AAEF-([A-Z]{2,5})-(\d{2})$")


def main() -> int:
    errors: list[str] = []

    if not CATALOG_PATH.exists():
        print(f"ERROR: Catalog not found: {CATALOG_PATH}")
        return 1

    with CATALOG_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    actual_columns = reader.fieldnames or []
    missing_columns = [c for c in REQUIRED_COLUMNS if c not in actual_columns]
    if missing_columns:
        errors.append(f"Missing required columns: {', '.join(missing_columns)}")

    if not rows:
        errors.append("Catalog contains no control rows.")

    seen_ids: dict[str, int] = {}

    for idx, row in enumerate(rows, start=2):  # header is line 1
        control_id = (row.get("Control ID") or "").strip()
        domain_name = (row.get("Domain") or "").strip()
        maturity = (row.get("Maturity") or "").strip()

        if not control_id:
            errors.append(f"Line {idx}: Control ID is empty.")
            continue

        if control_id in seen_ids:
            errors.append(
                f"Line {idx}: Duplicate Control ID '{control_id}' "
                f"(first seen on line {seen_ids[control_id]})."
            )
        else:
            seen_ids[control_id] = idx

        match = CONTROL_ID_RE.match(control_id)
        if not match:
            errors.append(
                f"Line {idx}: Control ID '{control_id}' does not match "
                "AAEF-<DOMAIN>-NN format."
            )
            continue

        domain_code = match.group(1)
        if domain_code not in ALLOWED_DOMAINS:
            errors.append(
                f"Line {idx}: Unknown domain code '{domain_code}' in Control ID "
                f"'{control_id}'. Allowed: {', '.join(sorted(ALLOWED_DOMAINS))}."
            )
        else:
            expected_domain_name = ALLOWED_DOMAINS[domain_code]
            if domain_name != expected_domain_name:
                errors.append(
                    f"Line {idx}: Domain for '{control_id}' is '{domain_name}', "
                    f"expected '{expected_domain_name}'."
                )

        if maturity not in ALLOWED_MATURITY:
            errors.append(
                f"Line {idx}: Invalid Maturity '{maturity}' for '{control_id}'. "
                f"Allowed: {', '.join(sorted(ALLOWED_MATURITY))}."
            )

        for col in REQUIRED_COLUMNS:
            value = (row.get(col) or "").strip()
            if not value:
                errors.append(f"Line {idx}: Column '{col}' is empty for '{control_id}'.")

    if errors:
        print(f"ERROR: {len(errors)} validation issue(s) found in {CATALOG_PATH}:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: {len(rows)} controls validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
