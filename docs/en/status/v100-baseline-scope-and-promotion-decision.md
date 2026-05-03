# v1.0.0 Baseline Scope and Promotion Decision

## Purpose

This document defines the initial baseline scope and promotion decision posture for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- `docs/en/status/post-v070-version-status-and-baseline-reference-note.md`
- `docs/en/status/v070-roadmap-wrap-up-and-release-readiness-note.md`

The goal is to decide how AAEF should approach v1.0.0 as a usable stable public baseline without accidentally treating planning material as already normative, implemented, certified, compliant, audit-sufficient, legally sufficient, or externally equivalent.

This document is planning and decision-support material only. It does not itself publish v1.0.0, create a release tag, update the active baseline, update the control catalog, update the evidence schema, update assessment artifacts, update testing procedures, add examples, add fixtures, or add executable validators.

## Current posture

As of this decision note:

- the latest completed planning roadmap is v0.7.0;
- v0.7.0 does not automatically change the active control and assessment baseline;
- v1.0.0 path work is not yet current, active, or baseline;
- published-release status is determined by GitHub Releases, tags, release notes, and explicit release artifacts;
- any v1.0.0 baseline change must be explicit; and
- planning, reviewability, reconstruction, and decision-support artifacts may be newer than the active baseline without automatically replacing it.

## Working definition of v1.0.0 usability

For planning purposes, v1.0.0 should mean that AAEF can be used as a stable public reference for understanding and reviewing AI-agent action authority, execution boundaries, evidence expectations, operational reconstruction, and risk-owner decision support.

Usable does not mean:

- certification scheme,
- formal standard,
- legal sufficiency,
- audit sufficiency,
- compliance assurance,
- external-framework equivalence,
- production readiness,
- implementation conformance,
- empirical validation, or
- proof that all AI-agent risks are mitigated.

A v1.0.0 usable baseline should allow a reader to answer:

- What is the core thesis?
- What is the active baseline?
- What controls or guidance should be read first?
- What evidence should be expected for an action?
- What evidence gaps matter?
- What decisions belong to risk owners?
- What remains future work?
- What claims are explicitly not made?

## Baseline decision posture

The recommended posture is:

> v1.0.0 should be planned as a stable public baseline candidate, but the active baseline must not be changed implicitly.
>
> Baseline update, artifact promotion, and future-work deferral must be explicit.

This means:

- v1.0.0 may update the active baseline later;
- this track should first define what would be promoted, deferred, or preserved;
- no single planning artifact automatically becomes baseline merely because it is recent;
- historical artifacts should remain historical unless explicitly promoted; and
- high-uncertainty domains should be deferred or scoped narrowly rather than forced into v1.0.0.

## Scope categories

Artifacts and domains should be classified into one of the following categories.

| Category | Meaning |
| --- | --- |
| Baseline candidate | Strong candidate to define or update the v1.0.0 active baseline after explicit review. |
| Stable guidance candidate | Candidate for stable guidance, reading path, implementation guidance, operator guidance, reviewer guidance, or risk-owner guidance, but not necessarily baseline. |
| Review-readiness candidate | Useful for v1.0.0 review, but requiring another readiness review before promotion. |
| Planning-only | Should remain planning or status material for now. |
| Historical | Should remain as versioned historical context. |
| Future work | Important but should be explicitly deferred beyond v1.0.0 unless separately scoped. |
| Non-goal | Should not be claimed by v1.0.0. |

## Initial promotion decision matrix

| Area | Initial posture | Rationale |
| --- | --- | --- |
| Model output is not authority | Baseline candidate | This remains the core thesis and should be preserved as a stable foundation. |
| Action authority separation | Baseline candidate | The framework depends on separating model output, authority, execution, and evidence. |
| Authorization decision vs tool dispatch separation | Baseline candidate / review-readiness candidate | Strong conceptual foundation; exact baseline wording should be reviewed against control catalog and implementation guidance. |
| Trusted control boundary | Baseline candidate | Central to AAEF's action-authority framing. |
| Evidence event schema | Review-readiness candidate | Existing schema is important, but v1.0.0 should review whether fields remain sufficient before claiming stable baseline status. |
| Evidence gap classification | Strong stable guidance candidate | v0.7.0 made this area concrete and useful; promotion should be reviewed for stable guidance or assessment support. |
| Operational reconstruction | Strong stable guidance candidate | Mature v0.7.0 area; likely useful for reviewer, operator, and risk-owner workflows. |
| Risk-owner decision support | Strong stable guidance candidate | Mature v0.7.0 area; useful for residual uncertainty handling and decision records. |
| Decision package checklist | Strong stable guidance candidate | Useful as a practical handoff artifact, but should preserve non-automation and non-legal/audit boundaries. |
| Decision matrix | Strong stable guidance candidate | Useful for accept/reject/request-evidence/defer/escalate paths; should remain decision support, not automated risk acceptance. |
| Component responsibility review | Review-readiness candidate | Important for implementation reviewability; may become stable implementation guidance after responsibility wording review. |
| Validator scope matrix | Review-readiness candidate | Useful for release gates; must not overclaim validator coverage. |
| Prototype/reference boundary note | Stable boundary candidate | Important to prevent prototype material from being mistaken for production implementation. |
| Implementation assumption inventory | Review-readiness candidate | Useful for implementers; likely needs synthesis before stable guidance. |
| Research positioning materials | Stable explanatory candidate / planning-only | Useful for research framing, but not empirical validation or peer-review claim. |
| External framework mappings | Wording-review candidate | Useful as contextual mapping only; no equivalence claim. |
| Assessment artifacts | Review-readiness candidate | Must be checked for consistency with any v1.0.0 baseline posture. |
| Testing procedures | Review-readiness candidate | May require specificity review before v1.0.0. |
| Examples and JSON fixtures | Review-readiness candidate | Existing examples are useful; v1.0.0 may need a minimum example set decision. |
| Memory and Retrieval | Future work | Important but not mature enough to force into v1.0.0 baseline without separate scope. |
| Advanced cross-agent / cross-domain delegation | Future work / narrow guidance candidate | Important but broad; may be deferred or scoped narrowly. |
| Approval laundering / approval fatigue formal testing | Future work / review-readiness candidate | Important, but formal testing and assessment expectations need more work. |
| Semantic validators | Future work | High risk of overclaiming; should not block v1.0.0 unless narrowly scoped. |
| Production reference implementation | Non-goal unless separately scoped | v1.0.0 should not imply production implementation readiness. |
| Certification / compliance / audit sufficiency | Non-goal | Must remain explicitly out of scope. |
| Legal sufficiency | Non-goal | Must remain explicitly out of scope. |

## Baseline candidate areas

The following areas are strong baseline candidates for v1.0.0 planning review:

1. Model output is not authority.
2. Action authority separation.
3. Authorization decision separation.
4. Tool dispatch / execution boundary separation.
5. Trusted control boundary.
6. Evidence as action-bound support rather than model self-report.
7. Human and risk-owner decision accountability boundaries.
8. Explicit non-certification and non-compliance posture.

These areas appear foundational enough that v1.0.0 should either promote them clearly or explain why they remain unchanged from an earlier active baseline.

## Stable guidance candidate areas

The following areas appear strong candidates for stable guidance, even if they do not define the active baseline by themselves:

1. Evidence gap classification.
2. Operational reconstruction question sets.
3. Operational reconstruction handoff.
4. Residual uncertainty decision handling.
5. Risk-owner decision package checklist.
6. Risk-owner decision matrix.
7. Component responsibility review.
8. Prototype/reference boundary guidance.
9. Validator scope and claim-boundary guidance.

These areas help make AAEF usable by implementers, reviewers, operators, and risk owners.

## Review-readiness areas

The following areas should be reviewed before deciding whether to promote them:

1. Control catalog wording and control ID stability.
2. Evidence schema sufficiency.
3. Assessment quick start and assessment worksheet alignment.
4. Testing procedure specificity.
5. Assessment profile consistency.
6. Example and JSON fixture coverage.
7. Validator scope and release-gate expectations.
8. README, document map, and citation wording.
9. Operator and risk-owner guidance alignment.

These should likely become follow-up v1.0.0 tracks.

## Planning-only and historical areas

Some versioned files should remain planning-only or historical.

A file should remain planning-only when:

- it records a roadmap decision,
- it documents a candidate path,
- it describes readiness or future work,
- it is intentionally non-normative,
- it is not integrated into baseline artifacts, or
- it would overclaim maturity if promoted.

A file should remain historical when:

- it describes a prior version's release preparation,
- it is superseded by later planning,
- it is useful as context but not current guidance,
- it contains version-specific status, or
- it should not be used as current entry-point guidance.

Historical and planning-only files should not be deleted merely because v1.0.0 planning begins.

## Deferred domain candidates

The following domains should likely be deferred beyond v1.0.0 unless a later track explicitly scopes them:

### Memory and Retrieval

Memory and Retrieval remains important but large.

It affects context integrity, persistent memory, retrieval poisoning, stale context, cross-session contamination, and action justification. It should not be forced into the v1.0.0 baseline unless a separate scope is created.

### Advanced cross-agent / cross-domain delegation

Cross-agent and cross-domain authority are important, but full treatment may require additional controls, examples, testing procedures, and evidence expectations.

v1.0.0 may preserve existing concepts while deferring advanced coverage.

### Approval laundering and approval fatigue testing

Approval quality is important, but formal testing for laundering, fatigue, and rubber-stamp approval should likely remain future work unless narrowly scoped.

### Semantic validators

Semantic validators may be useful later but carry a high risk of overclaiming.

v1.0.0 should preserve validator scope boundaries unless specific semantic checks are carefully scoped.

### Production reference implementation

v1.0.0 should not imply production reference implementation readiness unless a separate implementation track explicitly delivers and validates it.

## Explicit non-goals for v1.0.0

v1.0.0 should not claim:

- certification,
- compliance,
- conformity,
- audit sufficiency,
- legal sufficiency,
- external-framework equivalence,
- production readiness,
- implementation conformance,
- empirical validation,
- peer-reviewed acceptance,
- complete risk mitigation,
- complete root-cause analysis,
- complete operational reconstruction,
- complete side-effect absence,
- automated risk acceptance, or
- model output as authority.

These non-goals should remain visible in release communication and entry-point documentation.

## Candidate follow-up tracks

This decision note suggests the following follow-up tracks under roadmap #350:

1. v1.0.0 Control Catalog and Baseline Artifact Readiness.
2. v1.0.0 Evidence Schema, Examples, and Validator Readiness.
3. v1.0.0 Assessment Artifact and Testing Procedure Readiness.
4. v1.0.0 Implementation and Adoption Guidance Readiness.
5. v1.0.0 Deferred Domains and Non-Goals Register.
6. v1.0.0 Release Readiness and Communication.

These tracks should be opened only as needed and should preserve the distinction between baseline, stable guidance, review material, planning-only material, historical context, future work, and non-goals.

## Initial decision

The initial decision for #351 is:

> v1.0.0 should be planned as a usable stable public baseline candidate.
>
> Baseline update is possible but not yet made.
>
> Promotion should focus first on foundational authority/evidence boundaries and mature v0.7.0 reviewability materials.
>
> High-uncertainty domains should be explicitly deferred unless separately scoped.
>
> Claim boundaries must remain conservative.

This decision supports continued v1.0.0 planning without prematurely changing the active baseline.

## Review questions

Reviewers should be able to answer:

- Does this note distinguish baseline candidate from stable guidance candidate?
- Does this note avoid implicitly updating the active baseline?
- Does this note identify strong promotion candidates from v0.7.0?
- Does this note identify areas needing readiness review?
- Does this note identify future-work and non-goal areas?
- Does this note preserve historical planning artifacts?
- Does this note support a usable v1.0.0 path without overclaiming?
- Does this note provide enough direction for follow-up v1.0.0 tracks?

## Scope reminder

This artifact is planning and decision-support material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, or GitHub Releases.

It does not establish operational readiness, production readiness, implementation conformance, empirical validation, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, or external-framework equivalence.
