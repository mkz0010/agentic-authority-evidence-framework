# v0.5.0 Release Preparation Checklist

**Status:** Non-normative release preparation checklist

> **Planning status:** This document supports v0.5.0 release preparation. It does not create new control requirements and does not change the v0.4.1 Public Review Draft baseline unless explicitly incorporated into release artifacts.

## Purpose

This document provides a release preparation checklist and draft release note structure for AAEF v0.5.0.

The purpose is to ensure that v0.5.0 is released consistently as a planning-model and design-clarification release.

## Release Positioning

AAEF v0.5.0 should be positioned as a non-normative planning and design-clarification release.

It adds planning models and incorporation guidance for future work, but does not itself change the current v0.4.1 normative or assessment artifacts.

The release should clearly communicate that v0.5.0 does not change:

- the control catalog CSV;
- the human-readable control requirements;
- the assessment worksheet;
- the assessment profiles;
- the testing procedure CSV;
- the evidence schema;
- the evidence examples;
- the external framework mapping CSV.

## Release Artifacts to Review

Before creating the v0.5.0 release, review the following documents.

| Artifact | Review objective |
| --- | --- |
| `README.md` | Confirm current status, repository tree, planning material boundary, and release positioning. |
| `CHANGELOG.md` | Confirm v0.5.0 entries are complete and grouped appropriately. |
| `docs/en/33-v050-planning-overview.md` | Confirm all v0.5.0 planning materials are listed and scoped correctly. |
| `docs/en/34-v050-control-design-options.md` | Confirm incorporation rules and outcome register remain aligned with release scope. |
| `docs/en/50-authority-lifecycle-model.md` | Confirm authority lifecycle model remains non-normative. |
| `docs/en/51-evidence-integrity-levels.md` | Confirm evidence integrity model remains non-normative. |
| `docs/en/52-approval-quality-model.md` | Confirm approval quality model remains non-normative. |
| `docs/en/53-v050-release-scope-decision.md` | Confirm release scope decision reflects the intended v0.5.0 release boundary. |
| `docs/en/54-v050-release-preparation-checklist.md` | Confirm this checklist reflects the final release process. |

## Validation Checklist

Run the standard validators before release.

    python tools/validate_assessment_profiles.py
    python tools/validate_assessment_worksheet.py
    python tools/validate_control_catalog.py
    python tools/validate_testing_procedures.py
    python tools/validate_external_mappings.py
    python tools/validate_evidence_schema.py

Expected result:

    OK: 44 assessment profile mapping rows validated.
    OK: 44 assessment worksheet rows validated.
    OK: 44 controls validated.
    OK: 44 testing procedure rows validated.
    OK: 10 external framework mapping rows validated.
    OK: evidence schema and examples validated.

Also run:

    git diff --check

The GitHub Actions workflow `Validate AAEF Artifacts` should pass before the release is created.

## Issue Review Checklist

The current v0.5.0 planning issues should be reviewed after the release scope decision.

For each issue, decide whether to:

- close as addressed by v0.5.0 non-normative planning material;
- keep open as a v0.5.x follow-up;
- split into a narrower implementation, testing, evidence, or control-design issue;
- defer as future research or implementation guidance.

Current planning issue themes:

| Issue theme | Suggested release-time handling |
| --- | --- |
| Principal Context Degradation | Consider closing as planning-model addressed, or convert remaining work into testing/control refinement follow-up. |
| Cross-Agent and Cross-Domain Authority | Keep or split into follow-up work for capability-scoped delegation, explicit acceptance/refusal, chain limits, and budget propagation. |
| Authority Denial and Reauthorization Flow | Consider follow-up work for testing procedures and negative tests. |
| Risk-Proportional Evidence and Performance Overhead | Consider follow-up work for assessment profile and evidence guidance refinement. |
| Tamper-Evident Evidence Storage | Consider follow-up work for EIL-3/EIL-4 use in high-impact or audit-grade contexts. |
| Approval Quality and Approval Fatigue | Consider follow-up work for HUM refinement, testing criteria, or approval evidence expectations. |

## Follow-Up Issue Candidates

The following v0.5.x follow-up issues may be created after v0.5.0 release preparation.

| Candidate issue | Candidate labels |
| --- | --- |
| Refine principal context degradation testing criteria | `testing`, `planning`, `v0.5.x` |
| Define cross-agent capability-scoped delegation controls | `authority`, `control`, `planning`, `v0.5.x` |
| Add delegation acceptance/refusal negative tests | `testing`, `authority`, `v0.5.x` |
| Define cross-agent budget propagation guidance | `authority`, `governance`, `v0.5.x` |
| Evaluate evidence integrity levels for high-impact profiles | `evidence`, `assessment`, `v0.5.x` |
| Define tamper-evident evidence requirements for selected contexts | `evidence`, `testing`, `v0.5.x` |
| Refine approval quality testing and evidence expectations | `control`, `testing`, `v0.5.x` |

## Draft v0.5.0 Release Notes

The following text may be used as a starting point for the GitHub Release description.

### AAEF v0.5.0 Public Review Draft

AAEF v0.5.0 is a planning and design-clarification release.

This release adds non-normative planning models and incorporation guidance for future AAEF development. It does not change the v0.4.1 control catalog, evidence schema, assessment worksheet, assessment profiles, testing procedures, evidence examples, or external framework mapping CSV.

### Highlights

- Added a v0.5.0 planning overview and planning material boundary.
- Added incorporation rules for deciding when planning concepts become guidance, testing refinements, evidence refinements, existing control refinements, or new control candidates.
- Added a preliminary incorporation outcome register for current v0.5.0 planning themes.
- Added an Authority Lifecycle Model covering principal context degradation, cross-agent authority, denial, freeze, revocation, expiry, and reauthorization.
- Added cross-agent authority lifecycle guidance for capability-scoped delegation, explicit acceptance/refusal, delegation chain limits, accountability, and budget propagation.
- Added an Evidence Integrity Levels model covering risk-proportional evidence, tamper-evident evidence, and performance overhead tradeoffs.
- Added an Approval Quality Model covering meaningful approval, context sufficiency, approval fatigue, batch approval risk, approval states, and approval evidence expectations.
- Added a v0.5.0 release scope decision record.
- Added implementation guidance and resolved the documentation numbering gap.

### Non-Normative Scope

The new v0.5.0 planning materials are non-normative unless explicitly incorporated into future normative or assessment artifacts.

This release does not add new control IDs, change existing control requirements, change required schema fields, or change testing procedure pass/fail criteria.

### Validation

The release should be validated with the standard AAEF artifact validators and the GitHub Actions `Validate AAEF Artifacts` workflow.

## Release Creation Checklist

Before publishing the release:

- confirm `main` is clean and synchronized with `origin/main`;
- confirm `Validate AAEF Artifacts` is passing;
- confirm `CHANGELOG.md` contains the final v0.5.0 entry;
- confirm README status and planning material boundary are accurate;
- confirm release notes do not imply certification, compliance equivalence, or audit sufficiency;
- create the `v0.5.0` tag;
- publish the GitHub Release with the final release notes;
- review related v0.5.0 planning issues and close, split, or defer as appropriate.

## Relationship to Future Work

v0.5.0 provides the planning foundation for later v0.5.x work.

Future releases may incorporate selected planning concepts into:

- control requirements;
- testing procedures;
- evidence expectations;
- assessment profiles;
- evidence schema candidates;
- implementation guidance;
- external mapping caveats.

Any such incorporation should follow the rules in `docs/en/34-v050-control-design-options.md` and the scope decision in `docs/en/53-v050-release-scope-decision.md`.
