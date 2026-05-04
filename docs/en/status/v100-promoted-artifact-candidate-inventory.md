# v1.0.0 Promoted Artifact Candidate Inventory

## Purpose

This document inventories candidate artifacts and artifact areas that may be promoted, preserved, deferred, or explicitly excluded on the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- `docs/en/status/v100-baseline-scope-and-promotion-decision.md`
- `docs/en/status/post-v070-version-status-and-baseline-reference-note.md`

The goal is to make promotion decisions reviewable before v1.0.0 scope hardens.

This document is planning and inventory material only. It does not publish v1.0.0, create a release tag, update the active baseline, update the control catalog, update the evidence schema, update assessment artifacts, update testing procedures, add examples, add fixtures, or add executable validators.

## Inventory posture

This inventory distinguishes candidate value from promotion status.

An artifact can be useful without becoming part of the active baseline.

An artifact can be recent without becoming normative.

An artifact can be mature enough for stable guidance without becoming a control requirement.

An artifact can be important enough to preserve while still remaining future work.

## Classification categories

| Category | Meaning |
| --- | --- |
| Baseline candidate | Candidate to define or update v1.0.0 active baseline after explicit review. |
| Stable guidance candidate | Candidate for stable usage guidance, review guidance, operator guidance, risk-owner guidance, or adoption guidance. |
| Review-readiness candidate | Useful and relevant, but requiring another readiness review before promotion. |
| Planning-only | Should remain planning or status material for now. |
| Historical | Useful as versioned context, but not current guidance by itself. |
| Future work | Important but should be deferred beyond v1.0.0 unless separately scoped. |
| Non-goal | Should not be claimed or promoted by v1.0.0. |

## Promotion principles

Promotion decisions should follow these principles:

1. Promote only what can be explained clearly to implementers, operators, reviewers, or risk owners.
2. Do not promote planning material merely because it is recent.
3. Preserve the distinction between active baseline, stable guidance, review material, planning material, historical material, future work, and non-goals.
4. Avoid implying certification, compliance, legal sufficiency, audit sufficiency, implementation conformance, production readiness, empirical validation, or external-framework equivalence.
5. Prefer narrow stable guidance over broad unstable baseline claims.
6. Preserve the core thesis that model output is not authority.
7. Prefer explicit deferral for unresolved domains rather than silent omission.

## Summary inventory

| Area | Candidate category | Initial recommendation |
| --- | --- | --- |
| Core thesis: model output is not authority | Baseline candidate | Promote or preserve as central v1.0.0 foundation. |
| Action authority separation | Baseline candidate | Promote or preserve as foundational baseline material. |
| Authorization decision / tool dispatch separation | Baseline candidate / review-readiness candidate | Review control and implementation wording before promotion. |
| Trusted control boundary | Baseline candidate | Promote or preserve as core conceptual boundary. |
| Evidence as action-bound support | Baseline candidate | Promote or preserve as central evidence posture. |
| Control catalog | Review-readiness candidate | Review before deciding whether v1.0.0 updates it. |
| Evidence schema | Review-readiness candidate | Review sufficiency before stable baseline claim. |
| Assessment quick start and worksheets | Review-readiness candidate | Review alignment with v1.0.0 scope. |
| Testing procedures and pass criteria | Review-readiness candidate | Review specificity and consistency. |
| Examples and JSON fixtures | Review-readiness candidate | Decide minimum v1.0.0 example set separately. |
| Validators | Review-readiness candidate | Preserve structural validation boundaries; avoid overclaiming semantic coverage. |
| Evidence gap classification | Stable guidance candidate | Strong promotion candidate for reviewer guidance. |
| Operational reconstruction | Stable guidance candidate | Strong promotion candidate for reviewer/operator guidance. |
| Operational reconstruction handoff | Stable guidance candidate | Strong promotion candidate for handoff guidance. |
| Risk-owner decision support | Stable guidance candidate | Strong promotion candidate for decision-support guidance. |
| Residual uncertainty handling | Stable guidance candidate | Strong promotion candidate for risk-owner guidance. |
| Decision package checklist | Stable guidance candidate | Strong promotion candidate for practical handoff guidance. |
| Decision matrix | Stable guidance candidate | Strong promotion candidate for risk-owner decision support. |
| Component responsibility review | Review-readiness candidate | Candidate for implementation guidance after synthesis. |
| Validator scope matrix | Stable boundary candidate / review-readiness candidate | Useful for release gates and validator claim boundaries. |
| Prototype/reference boundary note | Stable boundary candidate | Useful to prevent production-readiness overclaiming. |
| Implementation assumption inventory | Review-readiness candidate | Useful for implementers; may need consolidation. |
| Research positioning materials | Stable explanatory candidate / planning-only | Useful for framing; not empirical validation. |
| External framework mappings | Contextual reference / wording-review candidate | Preserve as mapping context only; no equivalence claim. |
| Memory and Retrieval | Future work | Defer unless separately scoped. |
| Advanced cross-agent / cross-domain delegation | Future work / narrow guidance candidate | Defer broad treatment; preserve limited concepts where already present. |
| Approval laundering / approval fatigue testing | Future work / review-readiness candidate | Important but not yet stable enough for broad v1.0.0 baseline claim. |
| Semantic validators | Future work | Defer unless narrowly scoped. |
| Production reference implementation | Non-goal unless separately scoped | Do not imply v1.0.0 production implementation readiness. |
| Certification / compliance / legal / audit sufficiency | Non-goal | Must remain out of scope. |

## Baseline candidate inventory

### Core thesis

Candidate:

- Model output is not authority.

Initial recommendation:

- Promote or preserve as the central v1.0.0 foundation.

Reasoning:

- This is the primary organizing principle of AAEF.
- It is stable across prior releases and planning tracks.
- It is understandable to implementers, reviewers, risk owners, and researchers.
- It supports control, evidence, reconstruction, and decision-support boundaries.

Promotion caution:

- Do not present this thesis as proof that a system is safe, compliant, certified, or audit sufficient.

### Action authority separation

Candidate:

- Separation among model output, authority, authorization decision, execution, evidence, and review.

Initial recommendation:

- Treat as a baseline candidate.

Reasoning:

- This separation is foundational to AAEF's design.
- It supports action reviewability and evidence reconstruction.
- It is more stable than any specific implementation stack.

Promotion caution:

- Baseline wording should avoid requiring one specific product, framework, or runtime architecture.

### Authorization decision and tool dispatch separation

Candidate:

- Distinguishing authorization decision points from tool dispatch or execution enforcement points.

Initial recommendation:

- Treat as a baseline candidate with readiness review.

Reasoning:

- This area is central to implementation feasibility.
- It supports separation between policy decision and action execution.
- It is a strong candidate for stable guidance and potentially baseline wording.

Promotion caution:

- Exact wording should be reviewed against current controls, implementation guidance, and component responsibility materials before promotion.

### Trusted control boundary

Candidate:

- Trusted control boundary concepts that separate trusted control components from model/runtime claims.

Initial recommendation:

- Treat as a baseline candidate.

Reasoning:

- This boundary protects against treating model output or runtime self-report as sufficient authority.
- It supports review of evidence provenance and enforcement responsibility.

Promotion caution:

- Avoid implying that all trusted boundary implementations are equivalent or production-ready.

### Evidence as action-bound support

Candidate:

- Evidence should be bound to action, authority, execution, and review context.

Initial recommendation:

- Treat as a baseline candidate.

Reasoning:

- This is foundational to AAEF's evidence posture.
- It supports reconstruction, assessment, and risk-owner decision support.

Promotion caution:

- Evidence existence should not be treated as evidence sufficiency.

## Stable guidance candidate inventory

### Evidence gap classification

Candidate artifacts:

- `docs/en/status/v070-evidence-gap-classification-note.md`

Initial recommendation:

- Strong stable guidance candidate.

Reasoning:

- Provides concrete categories for missing, conflicting, untrusted, uncorrelated, ambiguous, and unowned evidence.
- Supports operational reconstruction and risk-owner decision support.
- Helps prevent unsupported conclusions.

Promotion caution:

- Should remain guidance unless integrated into assessment artifacts or testing procedures later.

### Operational reconstruction

Candidate artifacts:

- `docs/en/status/v070-operational-reconstruction-planning.md`
- `docs/en/status/v070-operational-reconstruction-question-set.md`
- `docs/en/status/v070-operational-reconstruction-handoff-note.md`

Initial recommendation:

- Strong stable guidance candidate.

Reasoning:

- Provides role-aware and evidence-aware reconstruction support.
- Helps reviewers ask what happened, what evidence exists, what is missing, and who owns follow-up.
- Bridges authority, execution, evidence, and handoff.

Promotion caution:

- Should not claim complete reconstruction, complete root-cause analysis, incident-response sufficiency, legal sufficiency, or audit sufficiency.

### Risk-owner decision support

Candidate artifacts:

- `docs/en/status/v070-risk-owner-decision-support-planning.md`
- `docs/en/status/v070-risk-owner-decision-question-set.md`
- `docs/en/status/v070-residual-uncertainty-decision-note.md`
- `docs/en/status/v070-risk-owner-decision-package-checklist.md`
- `docs/en/status/v070-risk-owner-decision-matrix.md`

Initial recommendation:

- Strong stable guidance candidate.

Reasoning:

- Provides practical support for accept, reject, request-evidence, defer, and escalate paths.
- Preserves residual uncertainty rather than hiding it.
- Helps distinguish decision support from automated risk acceptance.

Promotion caution:

- Must not automate risk acceptance or replace management judgment.

### Prototype and validator boundaries

Candidate artifacts:

- `docs/en/status/v070-prototype-reference-boundary-note.md`
- `docs/en/status/v070-validator-scope-matrix.md`

Initial recommendation:

- Stable boundary candidate / review-readiness candidate.

Reasoning:

- These artifacts prevent prototype and validator overclaiming.
- They support safe release-readiness posture.

Promotion caution:

- Should not imply production reference implementation, semantic validation, or implementation conformance.

## Review-readiness candidate inventory

### Control catalog

Candidate artifacts:

- `controls/aaef-controls-v0.1.csv`
- control catalog documentation and related validation scripts.

Initial recommendation:

- Review-readiness candidate.

Review questions:

- Should the current control catalog remain the v1.0.0 control catalog?
- Should control wording be updated?
- Should control IDs remain stable?
- Should any planning concepts become controls?
- Should changes be deferred beyond v1.0.0?

Promotion caution:

- A control catalog update would be a baseline-relevant change and should be explicit.

### Evidence schema and examples

Candidate artifacts:

- evidence schema files,
- JSON examples,
- schema validators,
- example validation scripts.

Initial recommendation:

- Review-readiness candidate.

Review questions:

- Is the schema sufficient for v1.0.0?
- Are examples aligned with intended usage?
- Are negative examples sufficient?
- Should reconstruction or decision package examples be added?
- Are validator results clearly bounded?

Promotion caution:

- Schema validity should not be overclaimed as operational correctness or evidence sufficiency.

### Assessment artifacts

Candidate artifacts:

- assessment quick start,
- worksheets,
- testing procedures,
- assessment profiles,
- pass/fail criteria.

Initial recommendation:

- Review-readiness candidate.

Review questions:

- Are assessment artifacts aligned with v1.0.0 baseline posture?
- Are pass/fail criteria specific enough?
- Do artifacts preserve non-certification and non-audit-sufficiency boundaries?
- Should reviewer evidence request guidance be added?

Promotion caution:

- Assessment support is not certification, compliance, legal sufficiency, or audit sufficiency.

### Implementation reviewability

Candidate artifacts:

- `docs/en/status/v070-implementation-reviewability-planning.md`
- `docs/en/status/v070-implementation-review-checklist.md`
- `docs/en/status/v070-implementation-assumption-inventory.md`
- `docs/en/status/v070-component-responsibility-review.md`

Initial recommendation:

- Review-readiness candidate.

Review questions:

- Which materials should become stable implementation guidance?
- Which should remain planning-only?
- Which responsibilities need clearer entry-point wording?
- Which assumptions should become explicit non-goals or preconditions?

Promotion caution:

- Implementation reviewability should not be presented as implementation conformance.

## Planning-only and historical inventory

The following materials should generally remain planning-only or historical unless explicitly promoted:

- roadmap wrap-up artifacts,
- release preparation checklists,
- issue coordination notes,
- candidate planning notes,
- older v0.5.x and v0.6.x planning documents,
- status documents tied to specific completed tracks,
- prior public review references,
- stale current-state wording after correction,
- release candidate planning material that was superseded.

Planning-only and historical artifacts should remain accessible because they explain why later decisions were made.

They should not be used as current entry-point guidance unless a later document explicitly promotes or summarizes them.

## Future-work candidate inventory

### Memory and Retrieval

Initial recommendation:

- Future work.

Reasoning:

- The domain is important but broad.
- It affects context integrity, retrieval poisoning, persistent state, stale memory, and cross-session action justification.
- It likely needs separate control, evidence, testing, and example work.

v1.0.0 posture:

- Preserve as future work or explicitly scoped non-baseline material.

### Advanced cross-agent and cross-domain delegation

Initial recommendation:

- Future work or narrow guidance candidate.

Reasoning:

- Cross-agent and cross-domain authority are important but complex.
- Full coverage may require additional controls, examples, and evidence expectations.

v1.0.0 posture:

- Preserve existing concepts where useful, but avoid broad stable claims unless separately scoped.

### Approval laundering and approval fatigue formalization

Initial recommendation:

- Future work / review-readiness candidate.

Reasoning:

- Approval quality is important for real-world safety.
- Formal testing expectations need more work.

v1.0.0 posture:

- Preserve as important future work unless narrowly scoped.

### Semantic validators

Initial recommendation:

- Future work.

Reasoning:

- Semantic validation can be useful but can easily overclaim.
- Current validator posture should remain bounded unless specific semantic checks are carefully scoped.

v1.0.0 posture:

- Do not require semantic validators for v1.0.0 unless separately scoped.

### Production reference implementation

Initial recommendation:

- Non-goal unless separately scoped.

Reasoning:

- v1.0.0 should not imply production implementation readiness.
- A reference implementation would require its own validation, threat modeling, and scope boundary.

v1.0.0 posture:

- Do not claim production reference implementation readiness.

## Non-goal inventory

v1.0.0 should not promote or imply:

- certification,
- formal standard status,
- compliance,
- conformity,
- legal sufficiency,
- audit sufficiency,
- external-framework equivalence,
- production readiness,
- implementation conformance,
- empirical validation,
- peer-reviewed acceptance,
- complete risk mitigation,
- complete root-cause analysis,
- complete operational reconstruction,
- absence of all side effects,
- automated risk acceptance, or
- model output as authority.

These should remain visible in release and entry-point wording.

## Recommended next inventory work

This document should be followed by more detailed inventories or registers, such as:

- planning-only and future-work register,
- claim-boundary and non-goal checklist,
- control catalog readiness review,
- evidence schema and validator readiness review,
- assessment artifact readiness review,
- adoption guidance promotion review, and
- release communication readiness review.

## Review questions

Reviewers should be able to answer:

- Does this inventory separate baseline candidates from stable guidance candidates?
- Does this inventory avoid treating recent planning artifacts as automatically normative?
- Does this inventory identify strong v0.7.0 promotion candidates?
- Does this inventory identify areas requiring readiness review?
- Does this inventory preserve historical and planning-only materials?
- Does this inventory explicitly defer unresolved domains?
- Does this inventory preserve v1.0.0 claim boundaries?
- Does this inventory support follow-up planning under #351 and roadmap #350?

## Scope reminder

This artifact is planning and inventory material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, or GitHub Releases.

It does not establish operational readiness, production readiness, implementation conformance, empirical validation, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, or external-framework equivalence.
