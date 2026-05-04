# v1.0.0 Control Catalog Readiness Review

## Purpose

This document reviews control catalog readiness for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- `docs/en/status/v100-baseline-scope-and-promotion-decision.md`
- `docs/en/status/v100-promoted-artifact-candidate-inventory.md`
- `docs/en/status/v100-planning-only-and-future-work-register.md`
- `docs/en/status/v100-claim-boundary-and-non-goal-checklist.md`
- `docs/en/status/v100-baseline-scope-close-readiness-checklist.md`
- `docs/en/status/post-v070-version-status-and-baseline-reference-note.md`

The goal is to review whether the current control catalog is ready to support v1.0.0 planning, whether control IDs should remain stable, whether any wording requires later review, and whether any planning concepts should be considered for future promotion.

This document is readiness-review material only. It does not update the control catalog, active baseline, evidence schema, assessment artifacts, testing procedures, examples, fixtures, validators, release tags, or GitHub Releases.

## Current posture

As of this review:

- v1.0.0 path planning is active under roadmap #350.
- #351 completed baseline-scope and promotion-decision planning.
- #357 is reviewing control catalog and baseline artifact readiness.
- The active control and assessment baseline has not been changed by #351 or #357.
- The control catalog is not updated by this document.
- Any future v1.0.0 baseline change must be explicit.

## Review posture

The recommended posture is:

> Treat the current control catalog as a baseline-relevant artifact requiring stability review before v1.0.0.
>
> Do not update control IDs or control wording implicitly.
>
> Treat new v0.5.x, v0.6.x, and v0.7.0 concepts as promotion candidates only, not as already-promoted control requirements.

This keeps v1.0.0 planning conservative while allowing later readiness tracks to decide whether updates are needed.

## Review targets

This review considers:

- control catalog stability,
- control ID stability,
- control wording stability,
- relationship between control requirements and planning artifacts,
- relationship to evidence schema,
- relationship to assessment artifacts,
- relationship to testing procedures,
- relationship to examples and validators,
- future baseline update options, and
- claim-boundary preservation.

## Control catalog readiness summary

| Review area | Initial readiness posture | Follow-up need |
| --- | --- | --- |
| Current control catalog existence | Ready for review | No immediate change in this artifact. |
| Control ID stability | Preserve by default | Add separate control ID stability note if needed. |
| Control wording | Review-readiness candidate | Do not update without targeted PR. |
| New v0.5.x planning concepts | Promotion candidates only | Review before adding to controls. |
| New v0.6.x adoption concepts | Stable guidance / review candidates | Do not convert to controls automatically. |
| New v0.7.0 reconstruction and decision-support concepts | Strong stable guidance candidates | Review before converting to controls or assessment criteria. |
| Evidence schema relationship | Requires separate readiness review | Do not update schema here. |
| Assessment artifact relationship | Requires separate readiness review | Do not update assessment artifacts here. |
| Testing procedure relationship | Requires separate readiness review | Do not update testing procedures here. |
| Validator relationship | Scope-bounded | Passing validators should not imply control conformance. |
| External mapping relationship | Contextual only | No equivalence or compliance claim. |

## Control ID stability review

Control IDs should remain stable by default.

Rationale:

- Control IDs are likely referenced by documentation, examples, mappings, worksheets, validators, and user workflows.
- ID churn can reduce traceability.
- v1.0.0 should avoid unnecessary renumbering unless there is a strong reason.
- New conceptual material can often be handled through guidance, notes, examples, or future controls rather than ID changes.

Readiness questions:

- Are current control IDs stable enough for v1.0.0 planning?
- Are any IDs obsolete or misleading?
- Would renumbering create more confusion than benefit?
- Can candidate new material be handled as guidance rather than control ID changes?
- If new controls are later needed, should they be appended rather than inserted?

Initial recommendation:

- Preserve current control IDs unless a later dedicated control catalog update PR explicitly changes them.
- If changes are considered, add a separate control ID stability note before making changes.

## Control wording readiness review

Control wording should not be updated casually during v1.0.0 planning.

Readiness questions:

- Is existing wording still aligned with the AAEF thesis that model output is not authority?
- Does wording still separate authority, decision, execution, and evidence?
- Does wording avoid implying implementation conformance or production readiness?
- Does wording avoid certification, compliance, audit sufficiency, legal sufficiency, or external-framework equivalence?
- Are any controls too vague for v1.0.0 stable baseline usage?
- Are any controls too implementation-specific?
- Are any controls missing explicit evidence or authorization boundaries?

Initial recommendation:

- Treat control wording as review-ready, not automatically changed.
- Use later targeted PRs for any wording changes.
- Preserve conservative claim boundaries.

## Candidate concept promotion review

Several mature planning concepts may be relevant to future control or baseline review.

However, they should not become control requirements automatically.

### Strong candidates for stable guidance review

The following are strong candidates for stable guidance review:

- evidence gap classification,
- operational reconstruction,
- operational reconstruction handoff,
- residual uncertainty handling,
- risk-owner decision package checklist,
- risk-owner decision matrix,
- validator scope boundaries,
- prototype/reference boundaries, and
- component responsibility review.

Initial posture:

- Strong guidance candidates.
- Not automatically control requirements.
- May inform future assessment or guidance updates.

### Review candidates for later baseline consideration

The following may require later baseline consideration:

- authorization decision and tool dispatch separation,
- backend verification responsibility,
- component responsibility boundaries,
- action-bound evidence requirements,
- non-execution and blocked-action review,
- human approval evidence and accountability,
- delegated-principal context, and
- high-impact action decision support.

Initial posture:

- Review candidates.
- Require careful mapping to existing controls before promotion.

### Likely future-work domains

The following should not be forced into control catalog updates for v1.0.0 unless separately scoped:

- Memory and Retrieval,
- advanced cross-agent / cross-domain delegation,
- approval laundering and approval fatigue formal testing,
- semantic validators,
- production reference implementation,
- empirical validation,
- certification or compliance structure,
- audit sufficiency model,
- legal sufficiency model, and
- external-framework equivalence.

Initial posture:

- Future work or non-goal unless separately scoped.

## Relationship to evidence schema

The control catalog and evidence schema are related but should not be collapsed.

Control catalog review asks:

- What requirements or expectations exist?

Evidence schema review asks:

- What evidence attributes can represent action, authority, execution, and review?

Readiness posture:

- Do not update the evidence schema in this control catalog review.
- Later evidence schema readiness work should consider whether current schema fields support v1.0.0 control and guidance posture.
- Schema validity should not be treated as evidence sufficiency or implementation conformance.

## Relationship to assessment artifacts

Control catalog readiness should inform assessment artifact review, but it should not update assessment artifacts directly.

Assessment readiness should later review:

- assessment quick start,
- assessment worksheets,
- assessment profiles,
- testing procedures,
- pass/fail criteria,
- reviewer evidence requests, and
- relationship to stable guidance candidates.

Readiness posture:

- Do not update assessment artifacts in this review.
- Later assessment readiness work should decide whether control catalog posture requires assessment updates.

## Relationship to testing procedures

Testing procedures should remain aligned with control wording and claim boundaries.

Readiness questions:

- Are testing procedures specific enough for stable use?
- Do testing procedures avoid certification or compliance claims?
- Do they distinguish evidence presence from evidence sufficiency?
- Do they cover non-execution and blocked-action cases where relevant?
- Do they avoid implying production readiness or implementation conformance?

Initial recommendation:

- Treat testing procedures as a separate readiness track.
- Do not update them in this control catalog review.

## Relationship to validators

Validators are useful but bounded.

Validator readiness should not be confused with control catalog readiness.

Safe posture:

- Validators check repository artifact structure and scoped consistency.
- Passing validators does not prove implementation conformance.
- Passing validators does not prove operational effectiveness.
- Passing validators does not prove evidence sufficiency.
- Passing validators does not prove semantic correctness.

Initial recommendation:

- Preserve validator claim boundaries.
- Review validator scope separately if v1.0.0 release gates are later defined.

## Relationship to examples and fixtures

Examples and fixtures can help users understand expected artifacts.

They should not be treated as complete implementation coverage.

Readiness questions:

- Which examples are needed for v1.0.0 usability?
- Are negative examples sufficient?
- Are non-execution examples sufficient?
- Are decision package examples needed?
- Are reconstruction examples needed?
- Are examples aligned with control and evidence expectations?

Initial recommendation:

- Review examples and fixtures separately.
- Do not add examples or fixtures in this control catalog readiness review.

## Relationship to baseline artifacts

Baseline-related artifacts may include:

- control catalog,
- evidence schema,
- assessment artifacts,
- testing procedures,
- examples,
- validators,
- README / overview entry points,
- document map,
- status reference notes, and
- release notes.

This review only covers control catalog readiness.

It does not decide final v1.0.0 baseline composition.

## Baseline update options

This review leaves several options open.

### Option A: Preserve current control catalog unchanged

Meaning:

- v1.0.0 does not update the control catalog.
- v1.0.0 may stabilize guidance, status references, or release communication without changing controls.

Benefits:

- Low churn.
- Preserves ID stability.
- Avoids rushed control changes.

Risks:

- Some mature v0.7.0 concepts may remain outside baseline controls.

### Option B: Update wording only

Meaning:

- Control IDs remain stable.
- Select wording is clarified.
- No major structural control catalog redesign occurs.

Benefits:

- Improves clarity.
- Maintains traceability.

Risks:

- Requires careful review to avoid unintended baseline expansion.

### Option C: Add new controls later

Meaning:

- New controls are introduced for mature concepts that cannot be handled as guidance.

Benefits:

- Captures important concepts more directly.

Risks:

- Increases scope.
- Requires evidence schema, assessment, testing, mapping, and validator review.

### Option D: Defer control catalog updates beyond v1.0.0

Meaning:

- v1.0.0 focuses on stable guidance and release posture.
- Control catalog changes are deferred.

Benefits:

- Keeps v1.0.0 achievable.
- Avoids destabilizing baseline.

Risks:

- v1.0.0 may be less ambitious as a baseline update.

## Initial recommendation

The initial recommendation is:

> Preserve the current control catalog by default while reviewing whether targeted wording changes or later control additions are needed.
>
> Do not change control IDs during #357 unless a dedicated control ID stability review supports doing so.
>
> Treat mature v0.7.0 reconstruction and risk-owner decision support materials as strong stable guidance candidates before considering control-level promotion.
>
> Defer broad or unresolved domains beyond v1.0.0 unless separately scoped.

This keeps the path toward v1.0.0 usable without creating uncontrolled baseline churn.

## Claim boundaries

This review does not claim:

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
- automated risk acceptance,
- control conformance,
- complete risk mitigation,
- complete operational reconstruction, or
- complete root-cause analysis.

## Recommended follow-up work

Recommended #357 follow-up candidates:

- baseline artifact readiness review,
- control ID stability note,
- baseline update decision options,
- control catalog close-readiness checklist.

Recommended later roadmap #350 tracks:

- evidence schema, examples, and validator readiness review,
- assessment artifact and testing procedure readiness review,
- implementation and adoption guidance readiness review,
- release readiness and communication planning,
- final v1.0.0 release decision.

## Review questions

Reviewers should be able to answer:

- Does this review preserve control catalog stability?
- Does it avoid implicitly updating the active baseline?
- Does it distinguish control requirements from planning and guidance materials?
- Does it identify mature concepts that may inform future promotion?
- Does it identify domains that should remain future work?
- Does it preserve claim boundaries?
- Does it clarify relationships to evidence schema, assessment artifacts, testing procedures, examples, and validators?
- Does it provide enough direction for later #357 artifacts?

## Scope reminder

This artifact is readiness-review material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, or GitHub Releases.

It does not establish operational readiness, production readiness, implementation conformance, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
