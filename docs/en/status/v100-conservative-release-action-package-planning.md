# v1.0.0 Conservative Release Action Package Planning

## Purpose

This document records the conservative release action package planning for AAEF v1.0.0.

It supports roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`.

It follows:

- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- completed track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`
- completed track #369, `[Track] v1.0.0: Assessment Artifact and Testing Procedure Readiness Review`
- completed track #374, `[Track] v1.0.0: Implementation and Adoption Guidance Readiness Review`
- completed track #380, `[Track] v1.0.0: Release Readiness and Communication Planning`
- `docs/en/status/v100-release-action-or-deferral-decision-note.md`

The goal is to define the release action package for Option A:

> proceed toward explicit AAEF v1.0.0 release action with the active control and assessment baseline unchanged.

This document is release action planning material only. It does not publish v1.0.0, create a release tag, publish a GitHub Release, update README release posture, update citation status, publish release notes, change the active baseline, or approve public announcement text.

## Selected roadmap direction

The selected roadmap direction is:

> Option A: conservative release action with active baseline unchanged.

This means:

- proceed toward an explicit AAEF v1.0.0 release action;
- preserve the active control and assessment baseline unchanged;
- prepare release-facing artifacts deliberately;
- state clearly what changed and what did not change;
- preserve claim boundaries;
- avoid baseline updates unless separately scoped;
- avoid unsupported readiness, conformance, certification, compliance, audit, legal, or external-framework equivalence claims.

This document records the planned release action package. It does not execute that package.

## Active baseline posture

The conservative v1.0.0 release action package should use this baseline posture:

> AAEF v1.0.0 does not change the active control and assessment baseline.

This means:

- the control catalog is not updated by this release action package unless a later explicit PR changes it;
- control IDs are not changed;
- the evidence schema is not updated;
- assessment artifacts are not updated;
- testing procedures are not updated;
- examples and fixtures are not added or changed by this package unless separately scoped;
- validators are not added or changed by this package unless separately scoped;
- implementation/adoption guidance is not updated by this package unless separately scoped.

The release may still publish or summarize readiness-review outputs, but those outputs are not active baseline changes by themselves.

## Release action package components

The conservative release action package may include the following explicit components.

| Component | Planned posture |
| --- | --- |
| README release posture | Decide explicitly before release action. Default: avoid broad README rewrite. |
| Localized README alignment | Only if README release posture changes. |
| Citation status | Decide explicitly before release action. Default: update only if tag/GitHub Release is actually created. |
| Release notes | Prepare and publish only as part of GitHub Release action. |
| Release tag | Create only after final validation and explicit maintainer decision. |
| GitHub Release | Publish only with reviewed release notes and claim boundaries. |
| Public announcement | Optional. Not approved by this document. |
| Roadmap #350 closure | Close only after release action is completed or explicitly deferred. |

## Minimum release action sequence

A conservative release action sequence is:

1. Confirm `main` is clean and synchronized with `origin/main`.
2. Confirm all v1.0.0 readiness-review tracks are closed.
3. Confirm #350 is the only open `v1.0.0` issue.
4. Prepare release notes / GitHub Release body.
5. Decide whether README release posture changes.
6. Decide whether citation status changes.
7. Run local validators.
8. Create a release preparation PR if repository files change.
9. Merge release preparation PR, if used.
10. Create and push `v1.0.0` tag only after final approval.
11. Publish GitHub Release only after release notes are reviewed.
12. Comment on #350 with release action summary.
13. Close #350 only if roadmap is complete.

This document does not perform any of these actions.

## Minimal safe release-note structure

A conservative GitHub Release body should include:

1. Summary
2. Release scope
3. Active baseline posture
4. Completed v1.0.0 readiness-review tracks
5. Added or updated artifacts
6. Artifacts explicitly not changed
7. Validation
8. Claim boundaries
9. Non-goals
10. Follow-up work

The release notes should state clearly:

> This release does not change the active control and assessment baseline.

They should also state that v1.0.0 does not by itself establish implementation readiness, adoption readiness, operational readiness, production readiness, implementation conformance, assessment sufficiency, testing sufficiency, evidence sufficiency, semantic correctness, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.

## Candidate release title

Candidate GitHub Release title:

> AAEF v1.0.0 Stable Release Path Planning Release

Alternative title:

> AAEF v1.0.0 Conservative Release Action with Active Baseline Unchanged

Initial preference:

> AAEF v1.0.0 Stable Release Path Planning Release

This title emphasizes that the release is stable-path and planning/readiness oriented, without implying a baseline update.

## Candidate release summary

Candidate release summary:

> AAEF v1.0.0 records the completed stable release path planning and readiness-review work for the Agentic Authority & Evidence Framework.
>
> This release preserves the active control and assessment baseline unchanged while documenting baseline scope, control catalog readiness, evidence schema/example/validator readiness, assessment/testing readiness, implementation/adoption guidance readiness, release communication boundaries, final release decision inputs, and release action planning.
>
> AAEF continues to center the principle that model output is not authority. The framework focuses on action authority, execution boundaries, evidence, reviewability, and risk-owner decision support.

This wording should be reviewed again before GitHub Release publication.

## Completed readiness-review tracks to summarize

Release notes should summarize these completed tracks:

- #351 Baseline Scope and Promotion Decision
- #357 Control Catalog and Baseline Artifact Readiness Review
- #363 Evidence Schema, Examples, and Validator Readiness Review
- #369 Assessment Artifact and Testing Procedure Readiness Review
- #374 Implementation and Adoption Guidance Readiness Review
- #380 Release Readiness and Communication Planning

Each should be described as readiness-review or decision-support work, not as certification, conformance, audit, legal, or equivalence proof.

## Artifacts added during v1.0.0 readiness path

Release notes may reference the v1.0.0 status artifacts registered in:

- `docs/en/status/README.md`
- `docs/en/document-map.md`

The release notes should not list every artifact if that would obscure the release boundary. A concise summary with links to status and document-map entries may be preferable.

## Artifacts explicitly not changed

The release notes should explicitly state that v1.0.0 does not change:

- active control and assessment baseline,
- control catalog,
- control IDs,
- evidence schema,
- assessment artifacts,
- testing procedures,
- executable validators,
- executable prototypes,
- scenario fixtures,
- JSON examples,
- README release posture, unless a later release preparation PR explicitly updates it,
- citation status, unless a later release preparation PR explicitly updates it.

If README or citation files are updated as part of the eventual release action, the release notes should say exactly what changed and what did not change.

## README decision

Default recommendation:

> Do not perform a broad README rewrite as part of the conservative release action package.

Possible narrow README update, if maintainers want it:

- add or update a short release status line;
- point to release notes;
- clarify active baseline unchanged;
- preserve existing non-goal and claim-boundary language.

If no README update is made, release notes must carry the release posture clearly.

## Citation decision

Default recommendation:

> Update citation status only if a `v1.0.0` tag and GitHub Release are actually created.

Citation wording must not imply:

- peer-reviewed acceptance,
- empirical validation,
- standardization,
- external endorsement,
- certification,
- compliance,
- conformity,
- audit sufficiency,
- legal sufficiency.

If citation files are not updated, release notes should not imply citation status changed.

## Tag and GitHub Release decision

A `v1.0.0` tag should be created only after:

- final local validation passes;
- GitHub Actions pass on any release preparation PR;
- release notes are reviewed;
- active baseline wording is explicit;
- claim boundaries are included;
- maintainers explicitly approve publication.

GitHub Release publication should use the reviewed release notes.

## Validation expectations

Before tag or GitHub Release publication, run:

- `py tools/validate_markdown_indexes.py`
- `py tools/validate_json_examples.py`
- `py tools/validate_evidence_schema.py`

If a release preparation PR changes additional validated files, run the relevant validators as well.

GitHub Actions should pass before tag creation.

## #350 closure expectations

Roadmap #350 should close only after maintainers decide one of the following:

- v1.0.0 release action is complete; or
- v1.0.0 release action is explicitly deferred and roadmap closure is still appropriate; or
- the roadmap is replaced by a new release execution issue.

If v1.0.0 is published, #350 closure should include:

- release tag,
- GitHub Release URL,
- active baseline posture,
- release summary,
- validation performed,
- preserved claim boundaries,
- follow-up work.

## Conservative release action readiness checklist

Before proceeding to tag/GitHub Release, confirm:

- [ ] `main` is clean.
- [ ] `main` is synchronized with `origin/main`.
- [ ] all intended v1.0.0 readiness-review tracks are closed.
- [ ] #350 is the only open `v1.0.0` issue.
- [ ] release notes are drafted.
- [ ] active baseline unchanged wording is included.
- [ ] artifacts not changed are listed.
- [ ] claim boundaries are included.
- [ ] README decision is explicit.
- [ ] citation decision is explicit.
- [ ] tag/GitHub Release decision is explicit.
- [ ] local validators pass.
- [ ] GitHub Actions pass.
- [ ] release publication is explicitly approved.

## Non-goals

The conservative release action package does not aim to:

- update the active baseline,
- update the control catalog,
- change control IDs,
- update the evidence schema,
- update assessment artifacts,
- update testing procedures,
- add new validators,
- add new examples or fixtures,
- redesign README/navigation,
- claim implementation readiness,
- claim adoption readiness,
- claim operational readiness,
- claim production readiness,
- claim implementation conformance,
- claim certification,
- claim compliance,
- claim conformity,
- claim audit sufficiency,
- claim legal sufficiency,
- claim automated risk acceptance,
- claim control conformance,
- claim external-framework equivalence.

## Claim boundaries

This planning note does not claim:

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

- Does this note clearly select the conservative release action path?
- Does it preserve active baseline unchanged?
- Does it distinguish release action planning from actual release action?
- Does it identify release package components?
- Does it identify minimum release-note content?
- Does it identify validation expectations?
- Does it preserve README, citation, tag, GitHub Release, and public announcement boundaries?
- Does it preserve claim boundaries?
- Does it provide enough direction for the actual release preparation step?

## Scope reminder

This artifact is release action planning material only.

It does not publish v1.0.0, create a release tag, publish a GitHub Release, update README release posture, update citation status, publish release notes, approve public announcement text, update the active control and assessment baseline, update the control catalog, update control IDs, update the evidence schema, update assessment artifacts, update testing procedures, add executable validators, add executable prototypes, add scenario fixtures, add JSON examples, update implementation guidance, update adoption guidance, update role guidance, or establish readiness, conformance, certification, compliance, audit, legal, control conformance, automated risk acceptance, or external-framework equivalence claims.
