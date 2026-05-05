# v1.0.0 Release Action or Deferral Decision Note

## Purpose

This document records decision options after completion of the v1.0.0 readiness-review tracks.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- completed track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`
- completed track #369, `[Track] v1.0.0: Assessment Artifact and Testing Procedure Readiness Review`
- completed track #374, `[Track] v1.0.0: Implementation and Adoption Guidance Readiness Review`
- completed track #380, `[Track] v1.0.0: Release Readiness and Communication Planning`

The goal is to make the next roadmap-level choice explicit:

- proceed to an explicit v1.0.0 release action,
- defer v1.0.0 release action while keeping roadmap #350 open,
- add additional release-facing planning before release action, or
- explicitly scope baseline-updating release work before publication.

This document is decision-support material only. It does not publish v1.0.0, create a release tag, publish a GitHub Release, update README release posture, update citation status, publish release notes, change the active baseline, or approve public announcement text.

## Current posture

As of this note:

- All planned v1.0.0 readiness-review tracks have been completed.
- Only roadmap #350 remains open under the `v1.0.0` label.
- The active control and assessment baseline has not been changed by completed readiness-review tracks.
- README release posture has not been updated by completed readiness-review tracks.
- Citation status has not been updated by completed readiness-review tracks.
- Release notes have not been published by completed readiness-review tracks.
- No v1.0.0 release tag has been created by completed readiness-review tracks.
- No GitHub Release has been published by completed readiness-review tracks.
- Any release action remains a later explicit maintainer decision.

## Meaning of release action

In this document, "release action" means one or more explicit maintainer actions such as:

- updating README release posture,
- updating localized README files,
- updating citation status,
- preparing or publishing release notes,
- creating a `v1.0.0` tag,
- publishing a GitHub Release,
- approving public announcement text,
- closing roadmap #350 as release complete.

Readiness-track completion is not release action.

This document does not perform release action.

## Decision question

The roadmap-level decision is:

> Should maintainers proceed toward explicit AAEF v1.0.0 release action now, defer release action, add another release-facing planning artifact, or scope baseline-updating work before publication?

This decision should be made before preparing release notes, tagging, publishing a GitHub Release, updating README release posture, or closing roadmap #350.

## Decision options summary

| Option | Summary | Initial posture |
| --- | --- | --- |
| Option A | Proceed to explicit v1.0.0 release action with active baseline unchanged. | Conservative release candidate. |
| Option B | Defer release action while keeping #350 open. | Safe if maintainers want more time. |
| Option C | Add additional release-facing planning before release action. | Useful if wording or announcement precision is needed. |
| Option D | Scope a baseline-updating v1.0.0 release before publication. | Higher burden; not recommended unless explicitly needed. |
| Option E | Publish v1.0.0 without explicit release package and boundaries. | Non-goal. |

## Option A: Proceed to explicit v1.0.0 release action with active baseline unchanged

Meaning:

- Maintainers decide to publish AAEF v1.0.0.
- The active control and assessment baseline remains unchanged unless release artifacts explicitly state otherwise.
- Release-facing artifacts are prepared through explicit scoped actions.
- Release notes explain what changed and what did not change.
- README, citation, tag, and GitHub Release updates are handled deliberately.

Candidate release action package:

1. Confirm clean local working tree and synchronized `main`.
2. Run local validation.
3. Prepare release notes with active-baseline-unchanged wording.
4. Decide whether README release posture should be updated.
5. Decide whether citation status should be updated.
6. Create a `v1.0.0` tag if approved.
7. Publish GitHub Release if approved.
8. Comment on #350 with release action summary.
9. Close #350 if maintainers decide roadmap is complete.

Benefits:

- Converts completed readiness planning into a visible release.
- Provides a clear stable milestone.
- Preserves conservative baseline posture.
- Avoids creating a baseline update without explicit baseline work.

Risks:

- Some readers may expect v1.0.0 to update the active baseline.
- Release notes and README wording must be very clear.
- Public messaging must avoid overclaiming readiness, conformance, certification, compliance, audit, legal, or equivalence status.

Initial assessment:

- This is a viable conservative path if maintainers want to publish v1.0.0 now.
- It should only proceed with explicit release notes, tag/GitHub Release decision, and active-baseline wording.

## Option B: Defer release action while keeping #350 open

Meaning:

- Do not publish v1.0.0 yet.
- Do not create a release tag.
- Do not publish a GitHub Release.
- Keep #350 open.
- Use completed readiness tracks as preparation for later release action.

Benefits:

- Safest if maintainers want more reflection.
- Avoids rushing public release communication.
- Allows additional review of README, citation, release notes, or public announcement wording.
- Allows more time to decide whether active baseline should remain unchanged or be updated.

Risks:

- v1.0.0 planning remains open longer.
- The project may appear to be waiting at the final release decision stage.
- More planning may reduce momentum if not bounded.

Initial assessment:

- Appropriate if maintainers are not ready to publish v1.0.0 immediately.
- Should include a short #350 comment explaining the deferral reason and next decision point.

## Option C: Add additional release-facing planning before release action

Meaning:

- Add one more planning artifact before release action.
- Candidate artifacts may include:
  - public announcement draft planning,
  - active baseline wording decision note,
  - final roadmap close-readiness checklist,
  - release action package checklist,
  - release notes draft planning.

Benefits:

- Improves precision before public release.
- Useful if communication risk remains high.
- Can separate announcement wording from release notes.
- Can clarify active baseline wording before tag/GitHub Release.

Risks:

- May become repetitive if the release decision is already clear.
- May delay release action.
- Should remain bounded to avoid planning drift.

Initial assessment:

- Useful only if maintainers identify a specific remaining ambiguity.
- Not required by #380, which is already closed as complete.

## Option D: Scope a baseline-updating v1.0.0 release before publication

Meaning:

- v1.0.0 would update the active control and assessment baseline.
- Baseline-updating artifacts would need explicit PRs.
- Control catalog, control IDs, evidence schema, assessment artifacts, testing procedures, examples, validators, README, citation, and release notes would need consistency review.

Benefits:

- Makes v1.0.0 a stronger baseline milestone.
- May align with reader expectations for a major version.

Risks:

- High review burden.
- High risk of accidental inconsistency.
- Higher chance of claim-boundary confusion.
- Contradicts the conservative default posture established by completed readiness tracks unless separately scoped.

Initial assessment:

- Not recommended unless maintainers explicitly want v1.0.0 to update active baseline artifacts.

## Option E: Publish v1.0.0 without explicit release package and boundaries

Meaning:

- Create tag or GitHub Release without explicit active-baseline wording, release notes, scope boundaries, or claim boundaries.

Initial posture:

- Non-goal.
- Should not be selected.

Rationale:

- Would create public communication risk.
- Could imply active baseline changes that were not made.
- Could imply readiness or conformance claims that AAEF does not make.
- Would weaken the release discipline established by #380.

## Recommended decision posture

The recommended posture is:

> Choose between Option A and Option B explicitly.
>
> If publishing now, proceed with a conservative v1.0.0 release action package that preserves the active baseline unless explicitly changed.
>
> If not publishing now, keep #350 open and record the reason for deferral.
>
> Use Option C only if a specific remaining release-facing ambiguity needs one more artifact.
>
> Avoid Option D unless maintainers intentionally scope baseline-updating work.
>
> Do not use Option E.

## Minimum conditions before Option A

Before proceeding to release action, confirm:

- `main` is clean and synchronized with `origin/main`;
- all intended v1.0.0 readiness tracks are closed;
- #350 is the only open `v1.0.0` issue;
- release readiness and communication planning are complete;
- active baseline posture is explicit;
- release notes can state what changed and what did not change;
- README release posture decision is explicit;
- citation decision is explicit;
- tag/GitHub Release decision is explicit;
- claim boundaries are included in release notes;
- no unsupported readiness, conformance, certification, compliance, audit, legal, or equivalence claims are made.

## Candidate release-action sequence if Option A is selected

A conservative sequence is:

1. Create a release action preparation branch.
2. Draft release notes or GitHub Release body.
3. Decide whether README release posture changes.
4. Decide whether citation status changes.
5. Run local validators.
6. Create release action PR if README/citation/release-note files are changed.
7. Merge release action PR.
8. Create and push `v1.0.0` tag if approved.
9. Publish GitHub Release if approved.
10. Comment on #350 with release action summary.
11. Close #350 if roadmap is complete.

This note does not perform these actions.

## Candidate deferral sequence if Option B is selected

A conservative deferral sequence is:

1. Comment on #350 that release readiness planning is complete.
2. State that release action is deferred.
3. Identify the reason for deferral.
4. Identify the next trigger for release action.
5. Keep #350 open.
6. Avoid tag, GitHub Release, README release posture update, citation update, and release-note publication.

This note does not perform these actions.

## Claim boundaries

This decision note does not claim:

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

- Does this note make the next roadmap-level decision explicit?
- Does it distinguish release action from completed readiness planning?
- Does it identify release, deferral, additional planning, and baseline-update options?
- Does it preserve active baseline boundaries?
- Does it preserve README, citation, release-note, tag, and GitHub Release boundaries?
- Does it avoid unsupported release-facing claims?
- Does it provide enough direction for the next #350 action?

## Scope reminder

This artifact is decision-support material only.

It does not publish v1.0.0, create a release tag, publish a GitHub Release, update README release posture, update citation status, publish release notes, approve public announcement text, update the active control and assessment baseline, update the control catalog, update control IDs, update the evidence schema, update assessment artifacts, update testing procedures, add executable validators, add executable prototypes, add scenario fixtures, add JSON examples, update implementation guidance, update adoption guidance, update role guidance, or establish readiness, conformance, certification, compliance, audit, legal, control conformance, automated risk acceptance, or external-framework equivalence claims.
