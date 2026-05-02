# AAEF v0.6.0 Release Notes Draft

Status: Release notes draft  
Related roadmap: #241  
Milestone: v0.6.0 Planning  
Related release preparation: `docs/en/status/v060-release-preparation-planning.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document provides a draft release note for a possible AAEF v0.6.0 planning release.

It is intended to be reviewed before any GitHub release, release tag, changelog release-section conversion, README update, or citation update.

This document does not create a release, create a tag, change active controls, change the current control and assessment baseline, or promote planning material into active requirements.

## Draft release title

AAEF v0.6.0 Practical Adoption Readiness Planning Release

## Draft release status

AAEF v0.6.0 is a planning and adoption-readiness release.

It organizes implementer, operator, legal/compliance, security architecture, and risk owner planning artifacts for future adoption-facing refinement.

It does not, by itself, change the current active control and assessment baseline.

## What this release is

AAEF v0.6.0 is intended to document the transition from:

> action assurance concept and planning

toward:

> adoptable implementation, operation, audit, legal/compliance, architecture, and governance packages

The release records the initial Practical Adoption Readiness planning set and repository review follow-up needed before selected material can be promoted into more stable adoption-facing artifacts.

## What this release is not

AAEF v0.6.0 is not:

- a new certification scheme
- a legal or regulatory compliance claim
- an audit opinion
- a conformity assessment
- an equivalence claim with external frameworks
- a replacement for external standards
- a replacement for legal, compliance, risk, or audit judgment
- an automatic change to the current active control and assessment baseline
- a promotion of all planning drafts into active requirements

## Current baseline note

Unless explicitly updated in active artifacts, the current control and assessment baseline remains unchanged.

v0.6.0 planning artifacts are non-normative planning material until later PRs promote selected material into active guidance, controls, schemas, assessment methods, testing procedures, examples, or release artifacts.

## Major additions

### Practical Adoption Readiness planning foundation

This release adds the v0.6.0 planning input synthesis and progress summaries that define Practical Adoption Readiness as the central v0.6.0 planning direction.

Key artifacts:

- `docs/en/status/v060-planning-input-synthesis.md`
- `docs/en/status/v060-planning-progress-summary.md`
- `docs/en/status/v060-review-follow-up-summary.md`
- `docs/en/status/v060-release-preparation-planning.md`

### Five-pillar adoption readiness planning set

This release adds initial planning artifacts across five workstreams.

| Workstream | Planning artifact |
| --- | --- |
| Implementer Readiness | `docs/en/status/v060-authorization-decision-artifact-minimal-profile-planning.md` and `docs/en/status/v060-implementer-quick-start-planning.md` |
| Operational Readiness | `docs/en/status/v060-operational-responsibility-matrix-planning.md` |
| Legal and Compliance Applicability | `docs/en/status/v060-legal-compliance-applicability-note-planning.md` |
| Security Architecture Hardening | `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md` |
| Risk Owner and Executive Adoption | `docs/en/status/v060-risk-owner-guide-planning.md` |

### Implementer readiness

The implementer planning materials define candidate implementation expectations for:

- canonical action request flow
- authorization decision artifact usage
- dispatch validation
- backend relying-party verification
- evidence linkage
- non-execution behavior
- reconstruction support

These materials are planning drafts, not yet active implementation requirements.

### Operational readiness

The operational planning material defines candidate operating responsibilities for:

- operational roles
- responsibility boundaries
- readiness questions
- handoff points
- evidence examples
- operating metrics

This material is intended to support future Day-2 operations guidance.

### Legal and compliance applicability

The legal/compliance planning material defines conservative applicability positioning.

It emphasizes that AAEF may support evidence, accountability, responsibility-boundary, and assessment discussions, but does not itself establish legal compliance, regulatory conformity, certification, or audit sufficiency.

### Security architecture hardening

The architecture planning material defines candidate minimum production architecture expectations for high-impact agentic action assurance, including:

- Trusted Control Boundary assumptions
- authorization and dispatch placement
- backend verification
- evidence and monitoring expectations
- freeze and incident considerations
- architecture anti-patterns

### Risk owner and executive adoption

The risk owner planning material defines candidate decision support for high-impact agentic actions, including:

- decision inputs
- decision outcomes
- high-impact action decision matrix
- risk acceptance memo structure
- residual risk register fields
- KRIs and KPIs
- exception management
- board and executive reporting considerations

## Repository review follow-up

This release also records follow-up work for repository review findings.

| Finding | Result |
| --- | --- |
| F-01 document-map missing core docs | Addressed and regression-protected. |
| F-05 document-map missing non-normative planning / guidance docs | Addressed and regression-protected. |
| F-02 CHANGELOG Unreleased accumulation | Partially addressed through Unreleased consolidation. |
| F-04 status document accumulation | Triage planning, inventory, decision register, and archive-readiness review added. |
| F-03 external framework mapping CSV enrichment | Conservative mapping enrichment review basis added. |

## Document-map and validation improvements

This release includes repository structure improvements:

- missing top-level numbered English documents were registered in `docs/en/document-map.md`
- Markdown index validation was strengthened
- top-level numbered English docs under `docs/en/` must now be represented in `docs/en/document-map.md`
- status document indexes and document-map rows continue to be validated

## Status document triage

This release includes a planning-only triage sequence for accumulated status documents:

- `docs/en/status/v060-status-document-triage-planning.md`
- `docs/en/status/v060-status-document-inventory-planning.md`
- `docs/en/status/v060-status-document-triage-decision-register.md`
- `docs/en/status/v060-status-document-archive-readiness-review.md`

The current recommendation is not to move archive-later status documents yet.

The archive-readiness review found that all 36 archive-later documents still have other status-document references. Future archive work should first define a historical-header, supersession-header, or reference-update strategy.

## External framework mapping

This release includes a conservative planning review for external framework mapping CSV enrichment:

- `docs/en/status/v060-external-framework-mapping-csv-enrichment-review.md`

The review identified:

- 2 mapping CSV candidates
- 9 mapping Markdown candidates

Future mapping enrichment should avoid compliance, equivalence, audit sufficiency, certification, or conformity claims.

## Validation summary

The release preparation work expects the following validation before final release:

    py tools/validate_markdown_indexes.py

Expected result:

    OK: Markdown indexes validated.

Additional release preparation checks should confirm:

- working tree is clean
- `main` is synchronized with `origin/main`
- GitHub Actions checks are passing
- `CHANGELOG.md` accurately represents the intended release scope
- README status language does not imply an active baseline change
- release notes preserve baseline and claim boundaries
- no certification, compliance, equivalence, audit sufficiency, conformity, or legal claim is introduced

## Known non-goals and deferred work

The following work is deferred unless later PRs explicitly handle it:

- promotion of planning drafts into adoption-facing active artifacts
- external framework mapping CSV enrichment
- conservative mapping CSV validation
- movement or archival of status documents
- historical or supersession header policy for status documents
- v0.6.x follow-up issues for adoption-facing packages
- closing roadmap issue #241
- closing umbrella issue #3
- changing the current active control and assessment baseline

## Candidate post-release follow-up

Possible post-release follow-up areas:

1. Promote selected v0.6.0 planning drafts into adoption-facing documents.
2. Define conservative mapping CSV structure and validation.
3. Add historical or supersession headers for status documents before any movement.
4. Split v0.6.x follow-up issues for implementer, operator, legal/compliance, architecture, and risk owner adoption packages.
5. Decide whether release notes should be added to a stable `docs/en/release/` path.
6. Decide whether `CITATION.cff` should be updated for v0.6.0.

## Draft GitHub release body

The following text may be adapted for a GitHub release body after final review.

### AAEF v0.6.0 Practical Adoption Readiness Planning Release

AAEF v0.6.0 is a planning and adoption-readiness release.

It organizes implementer, operator, legal/compliance, security architecture, and risk owner planning artifacts for future adoption-facing refinement. It does not, by itself, change the current active control and assessment baseline.

#### Highlights

- Added the v0.6.0 Practical Adoption Readiness planning foundation.
- Added initial planning artifacts across Implementer Readiness, Operational Readiness, Legal and Compliance Applicability, Security Architecture Hardening, and Risk Owner and Executive Adoption.
- Added planning drafts for authorization decision artifacts, implementer quick start, operational responsibility, production architecture, legal/compliance applicability, and risk owner decision support.
- Addressed and regression-protected document-map coverage findings.
- Consolidated CHANGELOG Unreleased entries for v0.6.0 planning.
- Added status document triage planning, inventory, decision register, and archive-readiness review.
- Added a conservative external framework mapping CSV enrichment review.
- Added release preparation planning.

#### Baseline and claim boundary

Unless explicitly updated in active artifacts, the current control and assessment baseline remains unchanged.

AAEF does not create a certification scheme, legal compliance claim, audit opinion, conformity assessment, or equivalence claim with external frameworks. External framework mapping materials are informative alignment aids only.

#### Recommended next steps

Future v0.6.x work should decide which planning drafts to promote into adoption-facing artifacts, whether to enrich external mapping CSVs under conservative claim boundaries, and how to handle historical or supersession headers for accumulated status documents.

## Acceptance criteria for this draft

This release notes draft is sufficient when:

- release status is clear
- baseline-change boundaries are clear
- certification, compliance, equivalence, conformity, and audit-sufficiency claims are avoided
- major v0.6.0 planning additions are summarized
- repository review follow-up is summarized
- deferred work is identified
- no release action is performed
- no tag is created
