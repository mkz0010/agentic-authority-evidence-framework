# AAEF External Framework Mappings

This directory contains conservative external framework mapping artifacts for AAEF.

## Status

Mappings in this directory are informative relationship mappings.

They are intended to help readers understand how AAEF concepts, controls, planning artifacts, evidence expectations, and action-boundary assurance ideas relate to external AI risk, governance, security, and assurance materials.

They do not assert:

- compliance,
- certification,
- audit sufficiency,
- conformity,
- equivalence with external frameworks,
- legal or regulatory adequacy,
- implementation conformance,
- production readiness,
- or complete mitigation.

## Current mapping files

| File | Purpose |
| --- | --- |
| [`external-framework-mapping.example.csv`](external-framework-mapping.example.csv) | Small pilot mapping artifact using conservative relationship vocabulary and explicit claim-boundary fields. |

## Mapping posture

AAEF mappings are not compliance crosswalks.

A mapping row means:

> This AAEF concept or artifact has an informative relationship to an external framework topic.

A mapping row does not mean:

> AAEF satisfies, meets, conforms to, certifies against, replaces, or is equivalent to the external framework topic.

## Conservative relationship vocabulary

Allowed relationship values should be conservative, such as:

- `supports_analysis_of`
- `provides_action_boundary_context_for`
- `provides_evidence_context_for`
- `partially_overlaps_with`
- `complements`
- `informs`
- `not_equivalent`
- `out_of_scope`
- `deferred`

Avoid values such as:

- `meets`
- `satisfies`
- `complies_with`
- `certifies`
- `equivalent_to`
- `conforms_to`

## Validation

Run:

    py tools/validate_external_mappings.py

Current validation checks:

- required fields are present,
- relationship values are conservative,
- confidence values are from the allowed set,
- review status values are from the allowed set,
- claim-boundary fields are populated,
- forbidden positive claim terms are not used in relationship fields,
- and each row preserves a non-compliance / non-equivalence boundary.

## Related planning artifacts

- `docs/en/status/v060-conservative-external-framework-mapping-enrichment-planning.md`
- `docs/en/status/v060-external-framework-mapping-csv-enrichment-review.md`
- `docs/en/status/v060-legal-compliance-applicability-note-planning.md`
- `docs/en/status/v060-version-reference-audit.md`
