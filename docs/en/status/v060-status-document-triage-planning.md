# AAEF v0.6.0 Status Document Triage Planning Draft

Status: Planning input  
Related roadmap: #241  
Milestone: v0.6.0 Planning  
Related planning summary: `docs/en/status/v060-planning-progress-summary.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document defines an initial planning draft for triaging accumulated `docs/en/status/` documents.

The purpose is to decide which status documents should be kept, archived, promoted, replaced, or removed in a future maintenance step.

This document is planning and coordination material. It does not remove, archive, move, or promote any existing document by itself.

## Why this is needed

The `docs/en/status/` directory has been useful as a coordination area for planning, review, incorporation decisions, consolidation checkpoints, and temporary candidate material.

However, after the v0.5.x follow-up cycle and the initial v0.6.0 planning set, the directory now contains several types of documents:

- completed issue checkpoints
- temporary proposals
- candidate appendices
- incorporation decision notes
- planning summaries
- v0.6.0 adoption-readiness planning drafts
- documents that may later become adoption-facing artifacts

Without triage, readers may not be able to tell which documents are historical records, current planning inputs, temporary work products, or candidates for promotion.

## Scope

This triage planning draft covers documents under:

- `docs/en/status/`

It does not cover:

- top-level numbered framework documents under `docs/en/`
- machine-readable CSV artifacts
- schema artifacts
- examples
- mappings
- release checklists
- README files
- GitHub issues or PRs directly

## Non-goals

This planning draft does not:

- delete any status document
- archive any status document
- promote any status document into active guidance
- change active controls
- change the current control and assessment baseline
- change schema, CSV, examples, or mappings
- create a release tag
- close roadmap issue #241
- close umbrella issue #3

## Triage outcomes

Each status document should eventually receive one of the following triage outcomes.

| Outcome | Meaning |
| --- | --- |
| Keep | Keep in `docs/en/status/` as current planning, coordination, or decision context. |
| Archive | Move to an archive path or otherwise mark as historical after its purpose is complete. |
| Promote | Convert into an adoption-facing or framework-facing document outside `docs/en/status/`. |
| Replace | Supersede with a newer summary, decision record, or consolidated artifact. |
| Remove | Delete only if the document is obsolete, duplicated, and no longer useful as historical context. |

Removal should be conservative. Most documents should first be kept, archived, or replaced.

## Candidate classification categories

The following categories should be used for triage.

| Category | Description | Likely outcome |
| --- | --- | --- |
| Current v0.6.0 planning foundation | Planning documents that define the current v0.6.0 Practical Adoption Readiness direction. | Keep |
| Current v0.6.0 progress summary | Documents summarizing current progress and remaining decisions. | Keep |
| v0.5.x completion record | Documents that record completed v0.5.x follow-up outcomes. | Keep or archive |
| Incorporation decision record | Documents that record why material was or was not incorporated. | Keep |
| Temporary proposal | Proposal documents used during a completed workstream. | Archive or replace |
| Candidate appendix | Supporting material that may have been incorporated elsewhere. | Archive, replace, or promote |
| Issue consolidation checkpoint | Issue-specific closure or consolidation documents. | Archive or keep as historical |
| Testing or schema candidate material | Temporary material that may have been incorporated into CSV or schema artifacts. | Archive if incorporated; promote if still useful |
| Adoption-facing candidate | A planning document that may become a stable implementer, operator, auditor, legal/compliance, architecture, or risk owner artifact. | Promote candidate |
| Superseded planning material | Planning material replaced by a later summary or adoption-facing artifact. | Replace or archive |

## Current keep candidates

The following documents are likely keep candidates because they represent current v0.6.0 planning state.

| Document pattern | Reason |
| --- | --- |
| `v060-planning-input-synthesis.md` | Establishes the v0.6.0 planning basis and five workstreams. |
| `v060-operational-responsibility-matrix-planning.md` | Current Operational Readiness planning draft. |
| `v060-high-impact-production-minimum-architecture-profile-planning.md` | Current Security Architecture Hardening planning draft. |
| `v060-authorization-decision-artifact-minimal-profile-planning.md` | Current Implementer Readiness planning draft. |
| `v060-implementer-quick-start-planning.md` | Current Implementer Quick Start planning draft. |
| `v060-legal-compliance-applicability-note-planning.md` | Current Legal and Compliance Applicability planning draft. |
| `v060-risk-owner-guide-planning.md` | Current Risk Owner and Executive Adoption planning draft. |
| `v060-planning-progress-summary.md` | Current progress summary for v0.6.0 planning. |
| `v060-status-document-triage-planning.md` | Current status document triage planning draft. |

## Current archive candidates

The following types of documents are likely archive candidates after review.

| Document type | Reason |
| --- | --- |
| Temporary v0.5.x track proposals | Many were used to coordinate completed #161 through #167 work. |
| Temporary candidate appendices | Some may have been incorporated into guidance, testing procedures, schema fields, examples, or completion summaries. |
| Issue-specific consolidation checkpoints | Useful historical records, but likely no longer active planning inputs. |
| Temporary testing candidate matrices | May be superseded if testing procedure CSVs or guidance documents already reflect the outcome. |
| Temporary schema or example proposals | May be superseded if schema fields and examples have already been added. |

Archive should preserve traceability where useful.

## Current promote candidates

The following types of status documents may become adoption-facing artifacts later.

| Candidate | Possible promotion path |
| --- | --- |
| Operational Responsibility Matrix planning draft | Future operations or adoption document. |
| High-Impact Production Minimum Architecture Profile planning draft | Future architecture profile document. |
| Authorization Decision Artifact Minimal Profile planning draft | Future implementer profile or schema candidate document. |
| Implementer Quick Start planning draft | Future implementer guide. |
| Legal and Compliance Applicability Note planning draft | Future legal/compliance applicability note. |
| Risk Owner Guide planning draft | Future risk owner or executive adoption guide. |
| Evidence Privacy and Retention planning material if added | Future legal/compliance or operations template. |
| Dispatch Attestation planning material if added | Future implementer or architecture profile. |

Promotion should require a separate PR that explicitly changes the document status and target location.

## Current replace candidates

Some documents may be replaced by a later consolidated summary rather than archived individually.

| Candidate type | Possible replacement |
| --- | --- |
| Multiple v0.5.x issue checkpoints | v0.5.x follow-up completion summary |
| Multiple testing candidate proposals | consolidated testing procedure decision record |
| Multiple schema/example proposals | consolidated schema/example incorporation decision |
| Multiple planning progress updates | v0.6.0 planning progress summary |

Replacement should preserve links from older status material when possible.

## Triage decision questions

Before changing a status document, answer:

1. Is the document still needed for current planning?
2. Is the document a historical decision record?
3. Has the content been incorporated into another artifact?
4. Does the document still contain unique rationale not preserved elsewhere?
5. Is the document referenced by an issue, PR, README, document-map, or status README?
6. Would deleting or moving it break reader traceability?
7. Should the document become adoption-facing guidance?
8. Should it remain non-normative?
9. Does the document need a supersession note?
10. Should the document be archived rather than removed?

## Suggested triage workflow

A future triage PR should follow this workflow:

1. List all files under `docs/en/status/`.
2. Classify each file using the categories in this draft.
3. Identify references from:
   - `docs/en/status/README.md`
   - `docs/en/document-map.md`
   - `CHANGELOG.md`
   - GitHub issues
   - merged PR bodies and comments where practical
4. Assign a proposed outcome:
   - keep
   - archive
   - promote
   - replace
   - remove
5. Avoid file movement in the first triage PR unless the classification is clear.
6. Add a triage table or decision register.
7. Validate indexes.
8. Only then perform archive, promotion, or removal in separate follow-up PRs.

## Suggested triage table fields

A future triage table should include:

| Field | Purpose |
| --- | --- |
| `document` | Status document path. |
| `topic` | Main planning or decision topic. |
| `related_issue` | Related issue if known. |
| `related_pr` | Related PR if known. |
| `category` | Triage category. |
| `recommended_outcome` | Keep, archive, promote, replace, or remove. |
| `rationale` | Why this outcome is recommended. |
| `superseded_by` | Newer document if applicable. |
| `promotion_candidate` | Whether it may become adoption-facing. |
| `notes` | Additional review notes. |

## Candidate archive path

If archive is used, candidate paths include:

| Path | Notes |
| --- | --- |
| `docs/en/status/archive/` | Simple local archive under status material. |
| `docs/en/archive/status/` | Broader documentation archive area. |
| Keep in place with historical header | Lowest disruption; avoids link movement. |

The first triage pass should decide whether an archive directory is necessary.

## Recommended initial triage policy

Recommended policy for the first triage pass:

- Do not delete status documents.
- Do not move status documents unless clearly necessary.
- Prefer keep or archive-candidate classification.
- Preserve incorporation decisions and completion summaries.
- Mark temporary proposals as archive candidates if their outcomes have been incorporated.
- Mark current v0.6.0 planning documents as keep.
- Mark adoption-facing candidates as promote candidates, not promoted artifacts.
- Make promotion decisions in separate PRs.

## Relationship to repository review findings

This planning draft supports follow-up for the repository review finding about accumulated temporary status documents.

It does not complete status document cleanup by itself. It creates the decision structure needed for safe cleanup.

## Acceptance criteria for this planning draft

This planning draft is sufficient when:

- triage outcomes are defined
- classification categories are defined
- keep, archive, promote, replace, and remove candidates are described
- decision questions are documented
- a future triage workflow is proposed
- no status documents are removed or moved
- no active baseline change is implied
- roadmap issue #241 can use this document as the basis for a later status document triage PR

## Expected next steps

Recommended next steps:

1. Generate a status document inventory.
2. Create a triage table assigning candidate outcomes.
3. Decide whether to create an archive path or keep historical documents in place.
4. Promote selected v0.6.0 planning drafts only through explicit adoption-facing PRs.
5. Update `docs/en/status/README.md` and `docs/en/document-map.md` if any future movement or promotion occurs.
