#!/usr/bin/env python3
"""
Validate the AAEF external framework mapping draft.

Purpose:
    This script validates the machine-readable external framework mapping draft.
    It checks structural consistency only. It does not validate compliance,
    audit sufficiency, or correctness of external framework interpretation.

Checks:
    - Required columns exist.
    - Mapping IDs are present and unique.
    - Relationship Type, Mapping Confidence, and Mapping Status use allowed values.
    - Referenced AAEF control IDs exist in the control catalog.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPO_ROOT / "controls" / "aaef-controls-v0.1.csv"
MAPPING_PATH = REPO_ROOT / "mappings" / "aaef-external-framework-mapping-v0.4-draft.csv"

REQUIRED_COLUMNS = [
    "Mapping ID",
    "External Framework",
    "External Version",
    "External Reference ID",
    "External Reference Title",
    "AAEF References",
    "AAEF Control IDs",
    "Relationship Type",
    "Mapping Confidence",
    "Mapping Status",
    "Mapping Rationale",
    "Limitations",
    "Notes",
]

REQUIRED_NON_EMPTY_COLUMNS = [
    "Mapping ID",
    "External Framework",
    "External Version",
    "External Reference ID",
    "External Reference Title",
    "AAEF References",
    "Relationship Type",
    "Mapping Confidence",
    "Mapping Status",
    "Mapping Rationale",
    "Limitations",
]

ALLOWED_RELATIONSHIP_TYPES = {
    "Supports",
    "Partially Supports",
    "Related",
    "Contextual",
    "Not Equivalent",
    "Out of Scope",
}

ALLOWED_MAPPING_CONFIDENCE = {"High", "Medium", "Low", "Needs Review"}

ALLOWED_MAPPING_STATUS = {
    "Draft",
    "Review Needed",
    "Reviewed",
    "Deprecated",
    "Superseded",
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        raise FileNotFoundError(path)

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)


def split_semicolon_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def main() -> int:
    errors: list[str] = []

    try:
        catalog_fields, catalog_rows = read_csv(CATALOG_PATH)
        mapping_fields, mapping_rows = read_csv(MAPPING_PATH)
    except FileNotFoundError as exc:
        print(f"ERROR: Required file not found: {exc}")
        return 1

    catalog_ids = {
        (row.get("Control ID") or "").strip()
        for row in catalog_rows
        if (row.get("Control ID") or "").strip()
    }

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in mapping_fields]
    if missing_columns:
        errors.append(f"Missing external mapping columns: {', '.join(missing_columns)}")

    if not mapping_rows:
        errors.append("External mapping file contains no rows.")

    seen_mapping_ids: dict[str, int] = {}

    for idx, row in enumerate(mapping_rows, start=2):
        mapping_id = (row.get("Mapping ID") or "").strip()

        if not mapping_id:
            errors.append(f"Mapping line {idx}: Mapping ID is empty.")
            continue

        if mapping_id in seen_mapping_ids:
            errors.append(
                f"Mapping line {idx}: Duplicate Mapping ID '{mapping_id}' "
                f"(first seen on line {seen_mapping_ids[mapping_id]})."
            )
        else:
            seen_mapping_ids[mapping_id] = idx

        for column in REQUIRED_NON_EMPTY_COLUMNS:
            value = (row.get(column) or "").strip()
            if not value:
                errors.append(f"Mapping line {idx}: Column '{column}' is empty for '{mapping_id}'.")

        relationship = (row.get("Relationship Type") or "").strip()
        if relationship and relationship not in ALLOWED_RELATIONSHIP_TYPES:
            errors.append(
                f"Mapping line {idx}: Invalid Relationship Type '{relationship}' "
                f"for '{mapping_id}'. Allowed: {', '.join(sorted(ALLOWED_RELATIONSHIP_TYPES))}."
            )

        confidence = (row.get("Mapping Confidence") or "").strip()
        if confidence and confidence not in ALLOWED_MAPPING_CONFIDENCE:
            errors.append(
                f"Mapping line {idx}: Invalid Mapping Confidence '{confidence}' "
                f"for '{mapping_id}'. Allowed: {', '.join(sorted(ALLOWED_MAPPING_CONFIDENCE))}."
            )

        status = (row.get("Mapping Status") or "").strip()
        if status and status not in ALLOWED_MAPPING_STATUS:
            errors.append(
                f"Mapping line {idx}: Invalid Mapping Status '{status}' "
                f"for '{mapping_id}'. Allowed: {', '.join(sorted(ALLOWED_MAPPING_STATUS))}."
            )

        control_ids = split_semicolon_values(row.get("AAEF Control IDs") or "")
        for control_id in control_ids:
            if control_id not in catalog_ids:
                errors.append(
                    f"Mapping line {idx}: Unknown AAEF Control ID '{control_id}' "
                    f"for '{mapping_id}'."
                )

    if errors:
        print("ERROR: external framework mapping validation failed.")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: {len(mapping_rows)} external framework mapping rows validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
