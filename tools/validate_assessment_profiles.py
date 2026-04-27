import csv
import sys
from pathlib import Path

CONTROL_PATH = Path("controls/aaef-controls-v0.1.csv")
MAPPING_PATH = Path("assessment/aaef-assessment-profiles-v0.3-draft.csv")

REQUIRED_FIELDS = [
    "Control ID",
    "Domain",
    "Lite Applicability",
    "Standard Applicability",
    "High-Impact Applicability",
    "Audit-Grade Applicability",
    "Profile Notes",
]

ALLOWED_VALUES = {
    "Required",
    "Recommended",
    "Optional",
    "Context-Dependent",
    "Not Applicable",
}

PROFILE_FIELDS = [
    "Lite Applicability",
    "Standard Applicability",
    "High-Impact Applicability",
    "Audit-Grade Applicability",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_csv(path: Path):
    if not path.exists():
        fail(f"missing file: {path}")

    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def main() -> None:
    controls = read_csv(CONTROL_PATH)
    mappings = read_csv(MAPPING_PATH)

    if not controls:
        fail("control catalog is empty")

    if not mappings:
        fail("assessment profile mapping is empty")

    mapping_fields = list(mappings[0].keys())

    for field in REQUIRED_FIELDS:
        if field not in mapping_fields:
            fail(f"missing required field in profile mapping: {field}")

    control_domains = {}
    for row in controls:
        control_id = row.get("Control ID", "").strip()
        domain = row.get("Domain", "").strip()

        if not control_id:
            fail("control catalog contains a row without Control ID")

        if control_id in control_domains:
            fail(f"duplicate Control ID in control catalog: {control_id}")

        control_domains[control_id] = domain

    seen = set()

    for row in mappings:
        control_id = row.get("Control ID", "").strip()
        domain = row.get("Domain", "").strip()

        if not control_id:
            fail("profile mapping contains a row without Control ID")

        if control_id in seen:
            fail(f"duplicate Control ID in profile mapping: {control_id}")

        if control_id not in control_domains:
            fail(f"profile mapping contains unknown Control ID: {control_id}")

        if domain != control_domains[control_id]:
            fail(
                f"domain mismatch for {control_id}: "
                f"mapping has {domain!r}, catalog has {control_domains[control_id]!r}"
            )

        for field in PROFILE_FIELDS:
            value = row.get(field, "").strip()
            if value not in ALLOWED_VALUES:
                fail(
                    f"invalid value for {control_id} / {field}: {value!r}; "
                    f"allowed values: {sorted(ALLOWED_VALUES)}"
                )

        if not row.get("Profile Notes", "").strip():
            fail(f"missing Profile Notes for {control_id}")

        seen.add(control_id)

    missing = set(control_domains) - seen
    extra = seen - set(control_domains)

    if missing:
        fail(f"profile mapping is missing controls: {sorted(missing)}")

    if extra:
        fail(f"profile mapping contains extra controls: {sorted(extra)}")

    print(f"OK: {len(mappings)} assessment profile mapping rows validated.")


if __name__ == "__main__":
    main()
