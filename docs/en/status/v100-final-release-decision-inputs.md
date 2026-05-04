# v1.0.0 Final Release Decision Inputs

## Purpose

This document records the final release decision inputs for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #380, `[Track] v1.0.0: Release Readiness and Communication Planning`
- `docs/en/status/v100-release-readiness-review.md`
- `docs/en/status/v100-release-communication-boundary-note.md`
- `docs/en/status/v100-readme-citation-release-note-update-options.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- completed track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`
- completed track #369, `[Track] v1.0.0: Assessment Artifact and Testing Procedure Readiness Review`
- completed track #374, `[Track] v1.0.0: Implementation and Adoption Guidance Readiness Review`

The goal is to collect the decision inputs maintainers need before deciding whether to perform a v1.0.0 release action.

This document is release decision input material only. It does not publish v1.0.0, create a release tag, publish a GitHub Release, update README release posture, update citation status, publish release notes, change the active baseline, update baseline artifacts, approve public announcement text, or make readiness, conformance, certification, compliance, audit, legal, or external-framework equivalence claims.

## Meaning of "final"

In this document, "final" means the final set of decision inputs required before maintainers decide whether to publish AAEF v1.0.0.

It does not mean that v1.0.0 is published by this document.

It does not create a release tag, publish a GitHub Release, update README release posture, update citation status, publish release notes, change the active baseline, update the control catalog, update control IDs, update the evidence schema, update assessment artifacts, update testing procedures, add validators, add examples, add fixtures, or approve public announcement text.

The final release decision remains a later explicit maintainer decision.

## Decision sequence

The intended sequence is:

1. Complete release readiness review.
2. Complete release communication boundary review.
3. Complete README, citation, and release-note update options.
4. Document final release decision inputs in this file.
5. Complete release readiness close-readiness review.
6. Decide whether to perform a v1.0.0 release action.
7. If approved, perform explicit release actions such as README update, citation update, release-note publication, tag creation, GitHub Release publication, and roadmap closure.

This document is step 4. It is not step 6 or step 7.

## Current posture

As of this note:

- v1.0.0 path planning is active under roadmap #350.
- #380 is reviewing release readiness and communication planning.
- Release readiness has been reviewed at the planning level.
- Release communication boundaries have been documented at the planning level.
- README, citation, and release-note update options have been documented at the planning level.
- README release posture has not been updated by #380.
- Citation status has not been updated by #380.
- Release notes have not been published by #380.
- No v1.0.0 release tag has been created by #380.
- No GitHub Release has been published by #380.
- The active control and assessment baseline has not been changed by completed v1.0.0 readiness tracks.
- Any future release action must be explicit.

## Final release decision question

The decision this document prepares for is:

> Should maintainers proceed with an explicit AAEF v1.0.0 release action, and if so, under what scope, baseline posture, communication boundaries, and artifact update plan?

This decision has not been made by this document.

## Decision inputs summary

| Decision input | Current status | Release decision implication |
| --- | --- | --- |
| Completed readiness tracks | #351, #357, #363, #369, and #374 complete | Provides release-decision input, not release action. |
| Release readiness review | Complete under #380 | Identifies release decision areas and boundaries. |
| Release communication boundaries | Complete under #380 | Defines safe/unsafe wording. |
| README/citation/release-note update options | Complete under #380 | Identifies update choices and risks. |
| Active baseline decision | Still explicit final decision | Must be stated before release action. |
| README release posture decision | Still explicit final decision | Must be chosen before README update. |
| Citation status decision | Still explicit final decision | Must be chosen before citation update. |
| Release-note decision | Still explicit final decision | Must be chosen before release publication. |
| Tag/GitHub Release decision | Still explicit final decision | Must be explicit before publication. |
| Public announcement decision | Optional later decision | Must remain claim-boundary-first. |
| Roadmap #350 closure decision | Later decision | Should follow release readiness close-readiness and final release action decision. |

## Required final maintainer decisions

Before a v1.0.0 release action, maintainers should explicitly decide:

1. Whether to publish AAEF v1.0.0.
2. Whether to create a `v1.0.0` tag.
3. Whether to publish a GitHub Release.
4. Whether the active control and assessment baseline changes or remains unchanged.
5. Whether README release posture changes or remains unchanged.
6. Whether localized README files, if present, need aligned updates.
7. Whether citation status changes or remains unchanged.
8. Whether release notes are published.
9. Whether any public announcement text is approved.
10. Whether #350 should remain open after release action or close after release completion.
11. Whether any deferred future-work candidates should be converted into follow-up issues.
12. Whether any release-facing claim-boundary wording needs additional review.

## Active baseline decision input

Maintainers should decide one of the following:

### Option A: Preserve active baseline unchanged

Meaning:

- v1.0.0 does not change the active control and assessment baseline.
- Current control catalog, evidence schema, assessment artifacts, and testing procedures remain the active baseline unless a later release explicitly changes them.
- v1.0.0 may still publish release-readiness and communication-planning artifacts.

Benefits:

- Lowest baseline-change risk.
- Aligns with completed readiness-track posture.
- Avoids implicit baseline update.
- Keeps release scope conservative.

Risks:

- Some readers may expect v1.0.0 to update the active baseline.
- Release communication must clearly explain the distinction between release version and active baseline.

### Option B: Update active baseline through explicitly listed artifacts

Meaning:

- v1.0.0 changes the active baseline through specific artifacts.
- The changed artifacts must be listed.
- Control catalog, control IDs, evidence schema, assessment artifacts, and testing procedures must be checked for consistency.

Benefits:

- Stronger release-significance signal.
- Clearer if maintainers intend v1.0.0 to be the new baseline.

Risks:

- Higher review burden.
- Higher consistency burden.
- Higher communication risk.
- Not supported unless the actual baseline-updating artifacts are explicitly scoped.

Initial input:

- Based on the completed readiness tracks, Option A appears to be the safer near-term path unless maintainers explicitly decide to add baseline-updating work before release.

## README release posture decision input

Maintainers should decide one of the following:

### Option A: Preserve README release posture unchanged until actual release action

Meaning:

- README is not updated by this decision-input document.
- README update waits for final release action.

Initial input:

- Recommended until release action is explicitly approved.

### Option B: Prepare README update PR as part of release action

Meaning:

- README release posture update is drafted and reviewed as a separate release-facing PR.
- The PR states release status and active baseline posture clearly.

Initial input:

- Appropriate only after final release decision inputs and close-readiness are complete.

### Option C: Update README before release action

Meaning:

- README is updated before tag/GitHub Release.

Initial input:

- Not recommended by default because it may imply release publication or baseline change.

## Citation status decision input

Maintainers should decide one of the following:

### Option A: Preserve citation status unchanged

Meaning:

- Citation status remains unchanged.
- No v1.0.0 citation update occurs until release action is approved.

Initial input:

- Recommended until tag/GitHub Release decision is explicit.

### Option B: Update citation as part of release action

Meaning:

- Citation information is aligned with actual tag, release date, and GitHub Release.

Initial input:

- Appropriate if v1.0.0 is actually published.

### Option C: Update citation before release action

Meaning:

- Citation material is updated before tag/GitHub Release.

Initial input:

- Not recommended by default because it may imply publication before release.

## Release-note decision input

Maintainers should decide one of the following:

### Option A: Do not publish release notes yet

Meaning:

- Release notes remain unpublished during decision-input and close-readiness work.

Initial input:

- Recommended until final release action is approved.

### Option B: Draft release notes but do not publish

Meaning:

- Release notes are prepared as draft material.
- They remain clearly unpublished until tag/GitHub Release action.

Initial input:

- Useful if maintainers want review before release.

### Option C: Publish release notes as part of GitHub Release

Meaning:

- Release notes are published when the release tag/GitHub Release is created.

Initial input:

- Appropriate only after final release action approval.

## GitHub Release and tag decision input

Maintainers should decide one of the following:

### Option A: Do not create tag or GitHub Release yet

Meaning:

- Continue #380 planning and close-readiness first.

Initial input:

- Recommended until release readiness close-readiness is complete.

### Option B: Create tag and GitHub Release after close-readiness

Meaning:

- Perform explicit v1.0.0 release action after final review.

Initial input:

- Candidate path if release readiness close-readiness confirms no blockers.

### Option C: Defer v1.0.0 release beyond #380

Meaning:

- Close #380 as planning complete but leave #350 open for future release action.

Initial input:

- Available if maintainers want additional release-facing work before publication.

## Public announcement decision input

Maintainers should decide one of the following:

### Option A: No public announcement yet

Meaning:

- No public announcement text is approved during #380.

Initial input:

- Safe default.

### Option B: Prepare public announcement draft planning

Meaning:

- Draft public announcement options but do not publish.

Initial input:

- Useful if release action is approaching.

### Option C: Approve public announcement as part of release action

Meaning:

- Public communication is approved with release notes and GitHub Release.

Initial input:

- Appropriate only after release action is approved.

## Release scope decision input

Maintainers should decide whether the v1.0.0 release scope is:

### Option A: Release-readiness and stable-path publication

Meaning:

- v1.0.0 publishes the result of readiness planning and communication boundaries.
- Active baseline remains unchanged unless explicitly stated.
- The release emphasizes conservative scope and future work.

Initial input:

- Strong conservative candidate.

### Option B: Active baseline update release

Meaning:

- v1.0.0 updates the active baseline.
- Requires explicit baseline artifact updates.

Initial input:

- Not recommended unless additional baseline-updating PRs are scoped.

### Option C: Defer release

Meaning:

- Do not publish v1.0.0 yet.
- Continue roadmap #350 with additional preparation.

Initial input:

- Available if maintainers want more final release work.

## Release blocker checklist

Before release action, confirm:

- Is #380 complete or close-ready?
- Is release readiness close-readiness complete?
- Is the active baseline decision explicit?
- Is README release posture decision explicit?
- Is citation status decision explicit?
- Is release-note decision explicit?
- Is tag/GitHub Release decision explicit?
- Is public announcement decision explicit?
- Are claim boundaries preserved?
- Are non-goals stated?
- Are validation expectations clear?
- Are release artifacts listed?
- Are deferred follow-up items identified?
- Are completed readiness tracks described as decision inputs rather than proof?
- Are examples described as illustrative?
- Are validators described as repository hygiene?
- Are assessment/testing artifacts described as reviewer support?
- Are external mappings described conservatively?

## Candidate release action package

If maintainers decide to publish v1.0.0, the release action package may include:

- README release-posture update PR, if selected;
- localized README alignment update, if selected;
- citation update PR, if selected;
- release notes draft;
- final local validation;
- final GitHub Actions validation;
- release tag creation;
- GitHub Release publication;
- #350 roadmap close-readiness or closure comment;
- public announcement draft, if selected.

This document does not perform any of these actions.

## Minimum safe release-note inputs

If release notes are later published, they should include:

- release title;
- release scope;
- active baseline posture;
- completed readiness-track summary;
- artifacts added or updated;
- artifacts explicitly not changed;
- validation performed;
- claim boundaries;
- non-goals;
- follow-up work.

## Minimum safe active-baseline wording

If active baseline remains unchanged, safe wording may include:

> This release does not change the active control and assessment baseline.

If more detail is needed:

> AAEF v1.0.0 preserves the existing active control and assessment baseline while documenting release-readiness, communication boundaries, and final release decision inputs for the stable release path.

This wording should be used only if maintainers explicitly choose the active-baseline-unchanged release path.

## Minimum safe non-goal wording

Release-facing artifacts should preserve wording that AAEF does not claim:

- certification,
- compliance,
- conformity,
- audit sufficiency,
- legal sufficiency,
- implementation readiness,
- adoption readiness,
- operational readiness,
- production readiness,
- implementation conformance,
- assessment sufficiency,
- testing sufficiency,
- evidence sufficiency,
- semantic correctness,
- empirical validation,
- peer-reviewed acceptance,
- automated risk acceptance,
- control conformance,
- external-framework equivalence.

## Recommended final decision input posture

The recommended posture for maintainers is:

> Treat this document as the final pre-release decision-input package, not as release action.
>
> Preserve README release posture, citation status, release notes, tag, GitHub Release, and active baseline unchanged until release readiness close-readiness is complete and maintainers explicitly decide whether to publish v1.0.0.
>
> If v1.0.0 is published, prefer a conservative release scope that preserves the active baseline unless separate baseline-updating work is explicitly scoped.
>
> Keep release-facing wording claim-boundary-first.

## Relationship to release readiness close-readiness checklist

This document should feed into `docs/en/status/v100-release-readiness-close-readiness-checklist.md`.

The close-readiness checklist should confirm:

- release readiness review exists;
- release communication boundary note exists;
- README/citation/release-note update options exist;
- final release decision inputs are documented;
- claim boundaries are preserved;
- remaining release action decisions are explicit;
- #380 can be closed if maintainers accept that release readiness and communication planning are complete.

## Relationship to roadmap #350

Roadmap #350 should remain open until maintainers decide whether:

- #380 completion is sufficient for release-readiness planning;
- additional release action work is needed;
- v1.0.0 should be published now;
- v1.0.0 should be deferred;
- #350 should close after release action or remain open for final release execution.

This document does not close #350.

## Claim boundaries

This decision-input note does not claim:

- v1.0.0 release,
- release tag creation,
- GitHub Release publication,
- active baseline update,
- control catalog update,
- control ID update,
- evidence schema update,
- assessment artifact update,
- testing procedure update,
- validator update,
- example update,
- fixture update,
- README release posture update,
- navigation update,
- citation status update,
- release-note publication,
- public announcement approval,
- implementation readiness,
- adoption readiness,
- operational readiness,
- production readiness,
- implementation conformance,
- assessment sufficiency,
- testing sufficiency,
- evidence sufficiency,
- semantic correctness,
- empirical validation,
- peer-reviewed acceptance,
- certification,
- compliance,
- conformity,
- audit sufficiency,
- legal sufficiency,
- automated risk acceptance,
- control conformance, or
- external-framework equivalence.

## Review questions

Reviewers should be able to answer:

- Is the meaning of "final" clear?
- Does this document distinguish final release decision inputs from release action?
- Does it identify the required maintainer decisions?
- Does it preserve active baseline decision boundaries?
- Does it preserve README, citation, and release-note boundaries?
- Does it preserve GitHub Release and tag boundaries?
- Does it preserve public announcement boundaries?
- Does it identify release blocker checks?
- Does it identify a candidate release action package without performing it?
- Does it preserve claim boundaries?
- Does it provide enough direction for release readiness close-readiness?

## Scope reminder

This artifact is release decision input material only.

It does not publish v1.0.0, create a release tag, publish a GitHub Release, update README release posture, update navigation, update citation status, publish release notes, approve public announcement text, update the active control and assessment baseline, update the control catalog, update control IDs, update the evidence schema, update assessment artifacts, update testing procedures, add executable validators, add executable prototypes, add scenario fixtures, add JSON examples, or establish readiness, conformance, certification, compliance, audit, legal, control conformance, or external-framework equivalence claims.
