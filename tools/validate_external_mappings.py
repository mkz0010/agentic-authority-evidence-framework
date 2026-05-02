#!/usr/bin/env python3
"""Validate AAEF external framework mapping files.

This validator supports both:
- the existing legacy external framework mapping draft; and
- the v0.6.x conservative external mapping pilot.

It checks mapping hygiene only. It does not validate compliance,
conformity, certification, audit sufficiency, or equivalence with any
external framework.
"""

from __future__ import annotations

import csv
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPO_ROOT / "controls" / "aaef-controls-v0.1.csv"
MAPPINGS_ROOT = REPO_ROOT / "mappings"

LEGACY_MAPPING_NAME = "aaef-external-framework-mapping-v0.4-draft.csv"

LEGACY_REQUIRED_COLUMNS = [
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

LEGACY_REQUIRED_NON_EMPTY_COLUMNS = [
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

LEGACY_ALLOWED_RELATIONSHIP_TYPES = {
    "Supports",
    "Partially Supports",
    "Related",
    "Contextual",
    "Not Equivalent",
    "Out of Scope",
}

LEGACY_ALLOWED_MAPPING_CONFIDENCE = {"High", "Medium", "Low", "Needs Review"}

LEGACY_ALLOWED_MAPPING_STATUS = {
    "Draft",
    "Review Needed",
    "Reviewed",
    "Deprecated",
    "Superseded",
}

CONSERVATIVE_REQUIRED_FIELDS = [
    "mapping_id",
    "external_framework",
    "external_version_or_date",
    "external_reference_id",
    "external_reference_title",
    "aaef_reference_type",
    "aaef_reference_id",
    "aaef_reference_status",
    "relationship_type",
    "relationship_confidence",
    "mapping_rationale",
    "scope_limitations",
    "claim_boundary",
    "review_status",
]

CONSERVATIVE_ALLOWED_RELATIONSHIP_TYPES = {
    "supports_analysis_of",
    "provides_action_boundary_context_for",
    "provides_evidence_context_for",
    "partially_overlaps_with",
    "complements",
    "informs",
    "not_equivalent",
    "out_of_scope",
    "deferred",
}

CONSERVATIVE_ALLOWED_CONFIDENCE = {
    "high",
    "medium",
    "low",
    "deferred",
    "not_applicable",
}

CONSERVATIVE_ALLOWED_REVIEW_STATUS = {
    "draft",
    "reviewed",
    "deferred",
    "rejected",
}

FORBIDDEN_RELATIONSHIP_TYPES = {
    "meets",
    "satisfies",
    "complies_with",
    "certifies",
    "equivalent_to",
    "conforms_to",
}

FORBIDDEN_POSITIVE_CLAIM_PHRASES = [
    "is equivalent to",
    "equivalent to",
    "complies with",
    "compliant with",
    "certified against",
    "certifies against",
    "conforms to",
    "satisfies",
    "meets",
    "proves compliance",
    "proves conformity",
    "provides audit sufficiency",
]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        raise FileNotFoundError(path)

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def split_semicolon_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def has_forbidden_positive_claim(text: str) -> str | None:
    lowered = text.lower()
    for phrase in FORBIDDEN_POSITIVE_CLAIM_PHRASES:
        if phrase in lowered:
            return phrase
    return None


def validate_legacy_mapping(path: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(REPO_ROOT)

    try:
        catalog_fields, catalog_rows = read_csv(CATALOG_PATH)
        mapping_fields, mapping_rows = read_csv(path)
    except FileNotFoundError as exc:
        return [f"Required file not found: {exc}"]

    catalog_ids = {
        (row.get("Control ID") or "").strip()
        for row in catalog_rows
        if (row.get("Control ID") or "").strip()
    }

    missing_columns = [
        column for column in LEGACY_REQUIRED_COLUMNS if column not in mapping_fields
    ]
    if missing_columns:
        errors.append(f"{rel}: missing legacy mapping columns: {', '.join(missing_columns)}")
        return errors

    if not mapping_rows:
        errors.append(f"{rel}: mapping file contains no rows")

    seen_mapping_ids: dict[str, int] = {}

    for index, row in enumerate(mapping_rows, start=2):
        mapping_id = (row.get("Mapping ID") or "").strip()

        if not mapping_id:
            errors.append(f"{rel}:{index}: Mapping ID is empty")
            continue

        if mapping_id in seen_mapping_ids:
            errors.append(
                f"{rel}:{index}: duplicate Mapping ID '{mapping_id}' "
                f"(first seen on line {seen_mapping_ids[mapping_id]})"
            )
        else:
            seen_mapping_ids[mapping_id] = index

        for column in LEGACY_REQUIRED_NON_EMPTY_COLUMNS:
            value = (row.get(column) or "").strip()
            if not value:
                errors.append(f"{rel}:{index} {mapping_id}: column '{column}' is empty")

        relationship = (row.get("Relationship Type") or "").strip()
        if relationship and relationship not in LEGACY_ALLOWED_RELATIONSHIP_TYPES:
            errors.append(
                f"{rel}:{index} {mapping_id}: invalid Relationship Type '{relationship}'"
            )

        confidence = (row.get("Mapping Confidence") or "").strip()
        if confidence and confidence not in LEGACY_ALLOWED_MAPPING_CONFIDENCE:
            errors.append(
                f"{rel}:{index} {mapping_id}: invalid Mapping Confidence '{confidence}'"
            )

        status = (row.get("Mapping Status") or "").strip()
        if status and status not in LEGACY_ALLOWED_MAPPING_STATUS:
            errors.append(
                f"{rel}:{index} {mapping_id}: invalid Mapping Status '{status}'"
            )

        control_ids = split_semicolon_values(row.get("AAEF Control IDs") or "")
        for control_id in control_ids:
            if control_id not in catalog_ids:
                errors.append(
                    f"{rel}:{index} {mapping_id}: unknown AAEF Control ID '{control_id}'"
                )

    return errors


def validate_conservative_mapping(path: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(REPO_ROOT)

    fields, rows = read_csv(path)

    missing = [field for field in CONSERVATIVE_REQUIRED_FIELDS if field not in fields]
    if missing:
        errors.append(f"{rel}: missing required fields: {', '.join(missing)}")
        return errors

    if not rows:
        errors.append(f"{rel}: mapping file contains no rows")

    seen_mapping_ids: dict[str, int] = {}

    for index, row in enumerate(rows, start=2):
        row_id = (row.get("mapping_id") or f"line {index}").strip()

        if row_id in seen_mapping_ids:
            errors.append(
                f"{rel}:{index} {row_id}: duplicate mapping_id "
                f"(first seen on line {seen_mapping_ids[row_id]})"
            )
        else:
            seen_mapping_ids[row_id] = index

        for field in CONSERVATIVE_REQUIRED_FIELDS:
            if not (row.get(field) or "").strip():
                errors.append(f"{rel}:{index} {row_id}: required field '{field}' is empty")

        relationship_type = (row.get("relationship_type") or "").strip()
        if relationship_type not in CONSERVATIVE_ALLOWED_RELATIONSHIP_TYPES:
            errors.append(
                f"{rel}:{index} {row_id}: relationship_type '{relationship_type}' is not allowed"
            )

        if relationship_type in FORBIDDEN_RELATIONSHIP_TYPES:
            errors.append(
                f"{rel}:{index} {row_id}: relationship_type '{relationship_type}' is forbidden"
            )

        confidence = (row.get("relationship_confidence") or "").strip()
        if confidence not in CONSERVATIVE_ALLOWED_CONFIDENCE:
            errors.append(
                f"{rel}:{index} {row_id}: relationship_confidence '{confidence}' is not allowed"
            )

        review_status = (row.get("review_status") or "").strip()
        if review_status not in CONSERVATIVE_ALLOWED_REVIEW_STATUS:
            errors.append(
                f"{rel}:{index} {row_id}: review_status '{review_status}' is not allowed"
            )

        for field in ["mapping_rationale", "scope_limitations"]:
            phrase = has_forbidden_positive_claim(row.get(field) or "")
            if phrase:
                errors.append(
                    f"{rel}:{index} {row_id}: field '{field}' contains forbidden positive claim phrase '{phrase}'"
                )

        claim_boundary = (row.get("claim_boundary") or "").lower()
        if "does not assert" not in claim_boundary:
            errors.append(
                f"{rel}:{index} {row_id}: claim_boundary must explicitly say 'does not assert'"
            )

        for required_boundary_term in [
            "compliance",
            "certification",
            "audit sufficiency",
            "equivalence",
        ]:
            if required_boundary_term not in claim_boundary:
                errors.append(
                    f"{rel}:{index} {row_id}: claim_boundary missing '{required_boundary_term}'"
                )

    return errors


def main() -> int:
    if not MAPPINGS_ROOT.exists():
        print("No mappings directory found.")
        return 0

    errors: list[str] = []
    validated_files: list[str] = []
    skipped_files: list[str] = []

    for path in sorted(MAPPINGS_ROOT.glob("*.csv")):
        if path.name == LEGACY_MAPPING_NAME:
            errors.extend(validate_legacy_mapping(path))
            validated_files.append(str(path.relative_to(REPO_ROOT)))
        elif path.name.startswith("external-framework-mapping") and path.name.endswith(".csv"):
            errors.extend(validate_conservative_mapping(path))
            validated_files.append(str(path.relative_to(REPO_ROOT)))
        else:
            skipped_files.append(str(path.relative_to(REPO_ROOT)))

    if errors:
        print("External mapping validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    if validated_files:
        print("External mapping validation passed for:")
        for rel in validated_files:
            print(f"- {rel}")
    else:
        print("No external mapping CSV files found.")

    if skipped_files:
        print("Skipped non-external mapping CSV files:")
        for rel in skipped_files:
            print(f"- {rel}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
