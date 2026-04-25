# 10. Maintenance and Validation

## Purpose of the Control Catalog Validator

AAEF uses `controls/aaef-controls-v0.1.csv` as the machine-readable control catalog.

The validator in `tools/validate_control_catalog.py` exists to protect the structural integrity of that catalog.

It does **not** prove that a control is correct, complete, effective, or suitable for a specific organization. It only checks that the catalog remains consistent enough to be referenced, reviewed, mapped, and maintained.

## How to Run the Validator

Run the validator with:

```bash
python tools/validate_control_catalog.py
```

The recommended execution location is the repository root. The script also resolves the catalog path relative to its own location, so it should not fail solely because it was launched from another working directory.

## What the Validator Checks

The validator checks:

- required columns exist,
- control IDs are present and unique,
- control IDs follow the expected `AAEF-<DOMAIN>-NN` format,
- domain codes are from the allowed domain set,
- domain names match domain codes,
- maturity values are valid,
- required fields are not empty.

## Why This Matters

AAEF is intended to be a public review draft and, eventually, a practical control profile.

For that to work, controls must be stable and referenceable. A reviewer should be able to cite `AAEF-AUZ-05` or `AAEF-EVD-02` without worrying that the same ID refers to multiple controls, that a domain name drifted, or that a required field is missing.

The validator is therefore a lightweight quality gate. It is a maintenance aid, not a security assessment tool.

## Why Keep It in v0.1?

In v0.1, the validator is intentionally narrow. It reduces accidental formatting and catalog errors without attempting to automate judgment.

This is useful because AAEF is expected to receive feedback in the form of new controls, revised controls, and mapping proposals. A small validation script helps keep those contributions reviewable.

## What It Does Not Do

The validator does not:

- validate whether a control is technically sufficient,
- validate whether a control maps correctly to a threat,
- validate whether an implementation conforms to AAEF,
- validate legal, regulatory, or audit sufficiency,
- replace expert review.

## Future Improvements

Future versions may add:

- cross-checking Markdown summaries against the CSV catalog,
- threat-to-control mapping validation,
- evidence field validation,
- schema validation for example evidence events,
- severity or assurance-level consistency checks.
