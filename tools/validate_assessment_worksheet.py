import csv
import sys
from pathlib import Path

CATALOG_PATH = Path("controls/aaef-controls-v0.1.csv")
WORKSHEET_PATH = Path("assessment/aaef-assessment-worksheet-v0.2-draft.csv")

REQUIRED_WORKSHEET_COLUMNS = [
    "Control ID",
    "Domain",
    "Requirement Level",
    "Requirement Summary",
    "Applicability",
    "Assessment Result",
    "Evidence Reviewed",
    "Finding Summary",
    "Residual Risk",
    "Remediation Notes",
    "Owner",
    "Target Date",
    "Priority",
    "Related Threats",
    "Assurance Type",
    "Implementation Assumptions",
    "Notes",
]

def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)

def main():
    errors = []

    catalog_fields, catalog_rows = read_csv(CATALOG_PATH)
    worksheet_fields, worksheet_rows = read_csv(WORKSHEET_PATH)

    missing_columns = [
        column for column in REQUIRED_WORKSHEET_COLUMNS
        if column not in worksheet_fields
    ]

    if missing_columns:
        errors.append(f"Missing worksheet columns: {', '.join(missing_columns)}")

    catalog_by_id = {row["Control ID"]: row for row in catalog_rows}
    worksheet_by_id = {row["Control ID"]: row for row in worksheet_rows}

    catalog_ids = set(catalog_by_id)
    worksheet_ids = set(worksheet_by_id)

    missing_in_worksheet = sorted(catalog_ids - worksheet_ids)
    extra_in_worksheet = sorted(worksheet_ids - catalog_ids)

    if missing_in_worksheet:
        errors.append(
            "Controls missing in worksheet: " + ", ".join(missing_in_worksheet)
        )

    if extra_in_worksheet:
        errors.append(
            "Extra controls in worksheet: " + ", ".join(extra_in_worksheet)
        )

    for cid in sorted(catalog_ids & worksheet_ids):
        catalog = catalog_by_id[cid]
        worksheet = worksheet_by_id[cid]

        catalog_domain = catalog.get("Domain", "").strip()
        worksheet_domain = worksheet.get("Domain", "").strip()

        if catalog_domain != worksheet_domain:
            errors.append(
                f"{cid}: Domain mismatch: catalog={catalog_domain!r}, worksheet={worksheet_domain!r}"
            )

        catalog_level = catalog.get("Maturity", "").strip()
        worksheet_level = worksheet.get("Requirement Level", "").strip()

        if catalog_level != worksheet_level:
            errors.append(
                f"{cid}: Requirement Level mismatch: catalog={catalog_level!r}, worksheet={worksheet_level!r}"
            )

        if not worksheet.get("Requirement Summary", "").strip():
            errors.append(f"{cid}: Requirement Summary is empty")

    if errors:
        print("ERROR: assessment worksheet validation failed.")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print(f"OK: {len(catalog_rows)} assessment worksheet rows validated.")

if __name__ == "__main__":
    main()
