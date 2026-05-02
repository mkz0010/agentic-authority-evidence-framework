# AAEF v0.6.0 Review Follow-up Summary

Status: Planning summary  
Related roadmap: #241  
Milestone: v0.6.0 Planning  
Related planning summary: `docs/en/status/v060-planning-progress-summary.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document summarizes the current state of repository review follow-up work performed during v0.6.0 Planning.

It records what has been addressed, what has been regression-protected, what has been partially addressed, and what remains as future follow-up.

This document is planning and coordination material. It does not change active controls, assessment criteria, schema requirements, external mappings, legal claims, or the current control and assessment baseline.

## Review follow-up overview

The review follow-up work has focused on the following findings:

| Finding | Theme | Current status |
| --- | --- | --- |
| F-01 | `document-map.md` missing core documents | Addressed and regression-protected |
| F-02 | `CHANGELOG.md` Unreleased accumulation and release-boundary clarity | Partially addressed |
| F-03 | External framework mapping CSV enrichment | Review basis established |
| F-04 | Accumulated temporary `docs/en/status/` documents | Triage model, inventory, decision register, and archive-readiness review established |
| F-05 | `document-map.md` missing non-normative planning / guidance documents | Addressed and regression-protected |

## F-01 and F-05: document-map coverage

### Work completed

| PR | Result |
| --- | --- |
| #254 | Registered missing top-level numbered English documents in `docs/en/document-map.md`. |
| #255 | Strengthened `tools/validate_markdown_indexes.py` so future top-level `docs/en/NN-*.md` files must be represented in `docs/en/document-map.md`. |

### Current status

F-01 and F-05 are considered addressed and regression-protected.

The current behavior is:

- all 63 top-level numbered English docs are represented in `docs/en/document-map.md`
- future omissions should be detected by validation
- the fix is tooling-supported rather than one-time manual cleanup only

### Remaining follow-up

No immediate follow-up is required for F-01 or F-05 unless the document map structure changes again.

## F-02: CHANGELOG Unreleased accumulation

### Work completed

| PR | Result |
| --- | --- |
| #257 | Reorganized `CHANGELOG.md` Unreleased into clearer semantic groups and added v0.6.0 Planning and Adoption Readiness entries. |

### Current status

F-02 is partially addressed.

The Unreleased section is now more readable and records the v0.6.0 planning work, but final release-boundary work remains pending until a release decision is made.

### Remaining follow-up

Future release preparation should decide:

- whether the current Unreleased entries are sufficient for a v0.6.0 planning release
- whether additional release notes are needed
- whether temporary planning entries should remain grouped or be moved into a release section
- whether a release checklist should include a final Unreleased review step

## F-03: external framework mapping CSV enrichment

### Work completed

| PR | Result |
| --- | --- |
| #262 | Added `docs/en/status/v060-external-framework-mapping-csv-enrichment-review.md`. |

### Current status

F-03 now has a conservative planning and review basis.

The review identified:

- 2 mapping CSV candidates
- 9 mapping Markdown candidates
- conservative enrichment principles
- candidate enrichment columns
- candidate enrichment targets
- non-goals and claim boundaries

### Remaining follow-up

Future work may include:

- selecting the first mapping CSV to enrich
- deciding whether to extend an existing CSV or create a dedicated enrichment CSV
- defining required conservative mapping columns
- adding mapping validation if the CSV structure becomes stable
- keeping mapping claims aligned with the Legal and Compliance Applicability planning draft
- avoiding compliance, equivalence, audit sufficiency, certification, or conformity claims

## F-04: accumulated temporary status documents

### Work completed

| PR | Result |
| --- | --- |
| #258 | Added the Status Document Triage planning draft. |
| #259 | Generated an inventory of 52 status documents. |
| #260 | Converted the generated inventory into a conservative triage decision register. |
| #261 | Reviewed archive readiness for the `archive later` documents. |

### Current status

F-04 has a strong planning and review basis, but actual movement has intentionally not started.

The current decision register result is:

| Candidate decision | Count |
| --- | ---: |
| `archive later` | 36 |
| `keep` | 15 |
| `replace later` | 1 |

The archive readiness review found:

| Metric | Count |
| --- | ---: |
| Archive-later documents reviewed | 36 |
| No non-index references detected | 0 |
| Non-index references detected | 36 |
| CHANGELOG references detected | 0 |
| Other status document references detected | 36 |

### Current recommendation

Do not move archive-later status documents yet.

All 36 archive-later documents still have status-document references. Future archive work should first decide whether to:

- add historical headers in place
- add supersession headers in place
- update status-document references before movement
- create an archive path
- move documents in small batches
- defer archive movement until release preparation

## Current non-goals

This follow-up summary does not:

- change active controls
- change the current control and assessment baseline
- modify external mapping CSV rows
- modify schemas, examples, or assessment artifacts
- move, delete, archive, replace, or promote status documents
- create a release tag
- claim compliance with external frameworks
- claim equivalence with external controls
- introduce certification, audit sufficiency, conformity, or legal compliance claims

## Current follow-up status

| Area | Status | Suggested next step |
| --- | --- | --- |
| Document-map coverage | Addressed and regression-protected | No immediate action unless document-map structure changes |
| Changelog release-boundary clarity | Partially addressed | Revisit during v0.6.0 release preparation |
| External mapping CSV enrichment | Planning/review basis established | Select first CSV and define conservative enrichment structure |
| Status document triage | Planning, inventory, decision register, and archive-readiness review complete | Decide historical/supersession header policy before moving files |
| v0.6.0 adoption-facing artifacts | Planning drafts exist | Decide which planning drafts should be promoted later |

## Suggested next planning decisions

Recommended next planning decisions:

1. Decide whether to start actual external mapping CSV enrichment.
2. Decide whether to add validation for conservative mapping CSV columns.
3. Decide whether status documents should receive historical headers before any movement.
4. Decide whether v0.6.0 planning should next promote selected adoption-facing artifacts.
5. Decide whether a v0.6.0 release preparation checklist is needed.

## Acceptance criteria for this summary

This summary is sufficient when:

- F-01 through F-05 are listed
- completed PRs are mapped to findings
- addressed, partially addressed, and remaining follow-up states are clear
- no active baseline change is implied
- no external compliance or equivalence claim is introduced
- roadmap issue #241 can use this document as a review follow-up status reference
