#!/usr/bin/env python3
"""Validate conservative external framework mapping CSV files.

This validator intentionally checks conservative mapping hygiene only.
It does not validate compliance, conformity, certification, audit sufficiency,
or equivalence with any external framework.
"""

from __future__ import annotations

import csv
from pathlib import Path
import sys


REQUIRED_FIELDS = [
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

ALLOWED_RELATIONSHIP_TYPES = {
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

ALLOWED_CONFIDENCE = {
    "high",
    "medium",
    "low",
    "deferred",
    "not_applicable",
}

ALLOWED_REVIEW_STATUS = {
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


def has_forbidden_positive_claim(text: str) -> str | None:
    lowered = text.lower()
    for phrase in FORBIDDEN_POSITIVE_CLAIM_PHRASES:
        if phrase in lowered:
            return phrase
    return None


def validate_file(path: Path, repo_root: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(repo_root)

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []

        missing = [field for field in REQUIRED_FIELDS if field not in fieldnames]
        if missing:
            errors.append(f"{rel}: missing required fields: {', '.join(missing)}")
            return errors

        for index, row in enumerate(reader, start=2):
            row_id = row.get("mapping_id", f"line {index}")

            for field in REQUIRED_FIELDS:
                if not (row.get(field) or "").strip():
                    errors.append(f"{rel}:{index} {row_id}: required field '{field}' is empty")

            relationship_type = (row.get("relationship_type") or "").strip()
            if relationship_type not in ALLOWED_RELATIONSHIP_TYPES:
                errors.append(
                    f"{rel}:{index} {row_id}: relationship_type '{relationship_type}' is not allowed"
                )

            if relationship_type in FORBIDDEN_RELATIONSHIP_TYPES:
                errors.append(
                    f"{rel}:{index} {row_id}: relationship_type '{relationship_type}' is forbidden"
                )

            confidence = (row.get("relationship_confidence") or "").strip()
            if confidence not in ALLOWED_CONFIDENCE:
                errors.append(
                    f"{rel}:{index} {row_id}: relationship_confidence '{confidence}' is not allowed"
                )

            review_status = (row.get("review_status") or "").strip()
            if review_status not in ALLOWED_REVIEW_STATUS:
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

            for required_boundary_term in ["compliance", "certification", "audit sufficiency", "equivalence"]:
                if required_boundary_term not in claim_boundary:
                    errors.append(
                        f"{rel}:{index} {row_id}: claim_boundary missing '{required_boundary_term}'"
                    )

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    mappings_root = repo_root / "mappings"

    if not mappings_root.exists():
        print("No mappings directory found.")
        return 0

    csv_files = sorted(mappings_root.glob("*.csv"))

    if not csv_files:
        print("No mapping CSV files found.")
        return 0

    errors: list[str] = []
    for path in csv_files:
        errors.extend(validate_file(path, repo_root))

    if errors:
        print("External mapping validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"External mapping validation passed for {len(csv_files)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
