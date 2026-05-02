# AAEF v0.6.0 Planning Progress Summary

Status: Planning summary  
Related roadmap: #241  
Milestone: v0.6.0 Planning  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document summarizes the current progress of AAEF v0.6.0 Planning.

It records the initial five-pillar planning set, the repository review follow-up completed for document-map coverage, and the remaining planning follow-up candidates.

This document is planning and coordination material. It does not change active controls, assessment criteria, schema requirements, legal obligations, or the current control and assessment baseline.

## Current planning position

AAEF v0.6.0 is being planned as:

**AAEF v0.6.0: Practical Adoption Readiness**

The planning direction is to move from:

> action assurance concept and planning

toward:

> adoptable implementation, operation, audit, legal/compliance, architecture, and governance packages

v0.6.0 remains planning-oriented at this stage. The current active baseline is not changed unless active artifacts are explicitly updated in later PRs.

## Completed initial planning foundation

The initial planning foundation has been established through the following merged PRs.

| PR | Artifact | Purpose |
| --- | --- | --- |
| #242 | `docs/en/status/v060-planning-input-synthesis.md` | Establishes the v0.6.0 Practical Adoption Readiness theme and synthesizes stakeholder feedback. |
| #248 | `docs/en/status/v060-operational-responsibility-matrix-planning.md` | Defines candidate operational roles, responsibility boundaries, readiness questions, evidence examples, and operating metrics. |
| #249 | `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md` | Defines candidate minimum production architecture expectations for high-impact agentic action assurance. |
| #250 | `docs/en/status/v060-authorization-decision-artifact-minimal-profile-planning.md` | Defines candidate minimal authorization decision fields, validation expectations, dispatch binding, backend verification, and evidence linkage. |
| #251 | `docs/en/status/v060-implementer-quick-start-planning.md` | Defines a candidate implementation path from action request through authorization, dispatch, backend verification, evidence, monitoring, and reconstruction. |
| #252 | `docs/en/status/v060-legal-compliance-applicability-note-planning.md` | Defines conservative legal/compliance applicability positioning, claim boundaries, responsibility boundaries, and anti-patterns. |
| #253 | `docs/en/status/v060-risk-owner-guide-planning.md` | Defines candidate risk owner decision inputs, decision outcomes, risk acceptance structure, residual risk tracking, KRIs/KPIs, and executive reporting considerations. |

## Five-pillar planning coverage

The initial v0.6.0 five-pillar planning set now has at least one planning artifact for each workstream.

| Workstream | Initial planning artifact | Status |
| --- | --- | --- |
| Implementer Readiness | Implementer Quick Start and Authorization Decision Artifact Minimal Profile | Initial planning drafts added |
| Operational Readiness | Operational Responsibility Matrix | Initial planning draft added |
| Legal and Compliance Applicability | Legal and Compliance Applicability Note | Initial planning draft added |
| Security Architecture Hardening | High-Impact Production Minimum Architecture Profile | Initial planning draft added |
| Risk Owner and Executive Adoption | Risk Owner Guide | Initial planning draft added |

## Cross-workstream integration

The planning artifacts are intended to reinforce each other.

### Implementer Readiness

The implementer planning drafts define the minimum technical path from action request to authorization decision, dispatch enforcement, backend verification, evidence generation, and reconstruction.

### Operational Readiness

The operational planning draft defines who owns, operates, reviews, and responds to the responsibilities created by the implementation and architecture model.

### Security Architecture Hardening

The architecture planning draft defines the candidate minimum production structure needed for high-impact agentic action assurance.

### Legal and Compliance Applicability

The legal/compliance planning draft defines conservative claim boundaries and clarifies that AAEF supports review and evidence discussions without claiming legal compliance or certification.

### Risk Owner and Executive Adoption

The risk owner planning draft translates technical, operational, legal/compliance, and architecture inputs into decision support for high-impact agentic actions.

## Repository review follow-up completed

A repository review identified document-map coverage gaps affecting both core numbered documents and non-normative planning/guidance documents.

The following follow-up work has been completed.

| PR | Purpose | Result |
| --- | --- | --- |
| #254 | Registered missing numbered docs in `docs/en/document-map.md` | All 63 top-level numbered English docs are represented in the document map. |
| #255 | Strengthened `tools/validate_markdown_indexes.py` | Future top-level `docs/en/NN-*.md` files must be represented in `docs/en/document-map.md`. |

## Addressed repository review findings

The following review findings are considered addressed and regression-protected.

| Finding | Summary | Current status |
| --- | --- | --- |
| F-01 | `document-map.md` missing core docs | Addressed by #254 and regression-protected by #255 |
| F-05 | `document-map.md` missing non-normative planning / guidance docs | Addressed by #254 and regression-protected by #255 |

## Current non-goals

The completed planning work does not:

- change active controls
- change the current control and assessment baseline
- promote planning drafts into active requirements
- create a certification scheme
- claim legal or regulatory compliance
- replace external standards, audit judgment, legal review, or enterprise risk management
- eliminate residual risk
- remove or archive existing status documents

## Remaining repository review follow-up candidates

The following review follow-up items remain candidates for v0.6.0 planning.

| Candidate | Related review theme | Suggested next action |
| --- | --- | --- |
| CHANGELOG / Unreleased cleanup | Release boundary clarity | Decide how to group v0.6.0 planning entries and whether to prepare a release-boundary cleanup PR. |
| Status document triage | Temporary status document accumulation | Classify status docs as keep, archive, promote, or replace. |
| External framework mapping CSV enrichment | Machine-readable mapping coverage | Decide whether to expand CSV mappings after external framework references stabilize. |
| v0.6.0 adoption artifact promotion | Planning-to-adoption transition | Decide which planning drafts should become adoption-facing documents. |
| Release checklist updates | Process hardening | Add document-map coverage, Unreleased cleanup, and status triage checks to release preparation guidance. |

## Suggested next planning decisions

Recommended next planning decisions:

1. Decide whether to turn selected planning drafts into adoption-facing artifacts.
2. Decide whether to add follow-up templates such as:
   - Dispatch Attestation Profile
   - Backend Relying-Party Verification Example
   - Evidence Privacy and Retention Policy
   - Risk Acceptance Memo
   - Executive One-Pager
3. Decide how to handle CHANGELOG / Unreleased entries for v0.6.0 planning.
4. Decide how to triage accumulated status documents.
5. Decide whether external framework mapping CSV enrichment belongs in v0.6.0 or a later mapping-focused cycle.

## Acceptance criteria for this summary

This summary is sufficient when:

- the initial v0.6.0 five-pillar planning artifacts are listed
- document-map review findings F-01 and F-05 are recorded as addressed
- validator regression protection is recorded
- remaining review follow-up candidates are identified
- no active baseline change is implied
- roadmap issue #241 can use this summary as a current progress reference
