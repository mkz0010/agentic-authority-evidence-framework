# v1.0.0 Evidence Schema Readiness Review

## Purpose

This document reviews evidence schema readiness for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- `docs/en/status/v100-baseline-artifact-readiness-review.md`
- `docs/en/status/v100-baseline-update-decision-options.md`
- `docs/en/status/v100-control-catalog-and-baseline-artifact-close-readiness-checklist.md`

The goal is to review whether the current evidence schema is ready for v1.0.0 planning, what it appears to support, what should remain unchanged by default, and what may require later review before any schema update decision.

This document is readiness-review material only. It does not update the evidence schema, examples, fixtures, validators, active baseline, control catalog, assessment artifacts, testing procedures, release tags, or GitHub Releases.

## Current posture

As of this review:

- v1.0.0 path planning is active under roadmap #350.
- #351 completed baseline-scope and promotion-decision planning.
- #357 completed control catalog and baseline artifact readiness review.
- #363 is reviewing evidence schema, examples, fixtures, and validator readiness.
- The current control catalog and control IDs are preserved by default for v1.0.0 planning.
- The active control and assessment baseline has not been changed by #351, #357, #363, or this artifact.
- The evidence schema is not updated by this document.
- Any future v1.0.0 evidence schema update must be explicit.

## Review posture

The recommended posture is:

> Treat the evidence schema as a baseline-relevant artifact that should remain stable by default until evidence schema, examples, and validators have been reviewed together.
>
> Do not treat schema validity as evidence sufficiency, implementation conformance, operational readiness, semantic correctness, audit sufficiency, legal sufficiency, or control conformance.
>
> Use this readiness review to identify whether later targeted schema updates are needed.

This posture keeps the v1.0.0 path conservative while preserving room for practical improvements.

## Evidence schema readiness summary

| Review area | Initial readiness posture | Follow-up need |
| --- | --- | --- |
| Basic action evidence representation | Ready for review | Confirm alignment with examples and validators. |
| Authorization and authority context | Ready for review | Confirm support for action-bound authority evidence. |
| Execution and backend result context | Ready for review | Confirm support for permitted, denied, and non-executed actions. |
| Non-execution and blocked-action representation | Review-readiness candidate | Check examples and assessment expectations. |
| Evidence gap classification support | Review-readiness candidate | Check whether schema fields support gap documentation or require guidance. |
| Operational reconstruction support | Review-readiness candidate | Check timeline, decision, enforcement, backend, and evidence chain needs. |
| Risk-owner decision support | Review-readiness candidate | Check decision package and residual uncertainty needs. |
| Validator support | Structurally supported by current validators | Keep validator claims bounded. |
| Example coverage | Requires separate review | Do not update examples here. |
| Future semantic checks | Future work | Avoid false assurance. |

## Evidence schema role

The evidence schema should support structured evidence about AI-agent actions.

For v1.0.0 planning, schema readiness should be evaluated against whether the schema can help represent:

- what action was requested,
- who or what requested the action,
- on whose behalf the action was requested,
- what authority context was used,
- what authorization or policy decision was made,
- whether dispatch was allowed, denied, held, or blocked,
- whether the backend accepted or rejected the action,
- what execution result was observed,
- what evidence was produced,
- what evidence is missing or conflicting,
- what residual uncertainty remains, and
- what reviewer or risk-owner decision may follow.

The schema does not need to answer all of these by itself.

Some topics may be handled through guidance, examples, assessment artifacts, testing procedures, or operational reconstruction materials.

## Action and request context readiness

Readiness questions:

- Does the schema represent the action or requested action clearly enough?
- Does it support action type, target, scope, timing, and requested outcome?
- Does it distinguish a model-generated proposal from an authorized action?
- Does it support correlation between request, authorization decision, dispatch, backend result, and evidence event?
- Does it support traceability across action-bound records?

Initial assessment:

- The schema appears ready for review as an action-evidence structure.
- v1.0.0 should avoid claiming that schema structure alone proves action correctness or authorization sufficiency.
- Later examples should demonstrate permitted, denied, non-executed, and high-impact cases where appropriate.

## Authority and authorization context readiness

Readiness questions:

- Does the schema represent authority context separately from model output?
- Does it support authorization decision identifiers or equivalent links?
- Does it support policy or rule context without exposing inappropriate sensitive details?
- Does it distinguish trusted authorization inputs from untrusted content influence?
- Does it support principal, delegation, and scope context at an appropriate level?

Initial assessment:

- Authority and authorization fields should be reviewed for v1.0.0 stability.
- If fields are sufficient, v1.0.0 may preserve the schema unchanged.
- If fields are insufficient, later targeted schema updates should be scoped separately.
- Schema language must preserve the AAEF principle that model output is not authority.

## Execution and backend result readiness

Readiness questions:

- Does the schema represent whether an action was dispatched?
- Does it distinguish dispatch decision from backend acceptance?
- Does it support backend verification or relying-party result context?
- Does it support error, rejection, denial, hold, blocked, or non-execution outcomes?
- Does it avoid implying that dispatch equals successful execution?

Initial assessment:

- Execution and backend result relationships are important for v1.0.0 usability.
- Later examples and validators should preserve the distinction between request, authorization, dispatch, backend acceptance, and observed result.
- Schema validity should not imply backend correctness or absence of side effects.

## Non-execution, denial, hold, and blocked-action readiness

Readiness questions:

- Can the schema represent actions that were not executed?
- Can it represent denied actions?
- Can it represent held or pending actions?
- Can it represent blocked dispatch?
- Can it represent backend rejection?
- Can it represent human approval required but not granted?
- Can it represent non-execution evidence without treating absence of execution as proof of safety?

Initial assessment:

- Non-execution is important enough for separate example and validator review.
- If schema fields already support these outcomes, examples should make that clear.
- If not, a later schema update option may be needed.
- v1.0.0 should avoid implying complete non-execution proof unless supported by evidence.

## Evidence gap readiness

Readiness questions:

- Can the schema represent missing evidence?
- Can it link evidence gaps to action request, authority, decision, enforcement, backend, execution, or timeline dimensions?
- Can it represent conflicting evidence?
- Can it represent untrusted self-report?
- Can it represent uncorrelated evidence?
- Can it preserve residual uncertainty?

Initial assessment:

- Evidence gap classification is a strong v0.7.0 stable guidance candidate.
- It may not need to become schema fields immediately.
- v1.0.0 may preserve evidence gap handling as guidance unless a targeted schema update is later scoped.
- If schema fields are added later, validators and examples must be reviewed together.

## Operational reconstruction readiness

Readiness questions:

- Does the schema support reconstruction of an action timeline?
- Does it support authority chain reconstruction?
- Does it support decision chain reconstruction?
- Does it support execution and non-execution reconstruction?
- Does it support correlation among request, authorization, dispatch, backend, evidence, and review records?
- Does it support recording residual uncertainty and unsupported conclusions?

Initial assessment:

- Operational reconstruction likely depends on schema plus guidance, examples, and assessment artifacts.
- Schema alone should not be described as complete reconstruction capability.
- Later examples may help show how reconstruction-supporting records can be structured.
- v1.0.0 should avoid complete reconstruction or complete root-cause analysis claims.

## Risk-owner decision support readiness

Readiness questions:

- Does the schema support enough context for risk-owner review?
- Does it connect evidence state to residual uncertainty?
- Does it support accept, reject, request-evidence, defer, or escalate decision patterns?
- Does it support decision record linkage?
- Does it avoid automating risk acceptance?

Initial assessment:

- Risk-owner decision support may be handled through guidance and decision package material rather than schema changes.
- If examples are added later, they should show how evidence records can support decision packages without replacing human judgment.
- v1.0.0 should preserve the boundary that risk-owner decision support is not automated risk acceptance.

## Validator relationship

Current validators support repository artifact checks.

Readiness questions:

- What aspects of schema validity are currently checked?
- Are example files checked against schema expectations?
- Are invalid examples expected to fail?
- Are validator messages actionable?
- Are validator limitations documented?
- Do validators avoid semantic correctness claims?

Initial assessment:

- Validator readiness should be reviewed separately under #363.
- Passing validators should remain a scoped repository check.
- Passing validators must not imply operational readiness, implementation conformance, evidence sufficiency, semantic correctness, audit sufficiency, legal sufficiency, or control conformance.

## Example relationship

Examples are important for schema usability.

Readiness questions:

- Do existing examples cover common positive cases?
- Do examples cover invalid or negative cases?
- Do examples cover high-impact actions carefully?
- Do examples cover denied, held, blocked, and non-executed outcomes?
- Do examples show evidence gaps or residual uncertainty?
- Are examples clearly marked as illustrative or scoped fixtures?
- Are examples aligned with schema and validators?

Initial assessment:

- Examples and fixtures require a separate readiness review.
- This document does not add examples.
- Example coverage should be increased only with clear claim boundaries.

## Evidence schema update options

This review leaves several options open.

### Option A: Preserve evidence schema unchanged

Meaning:

- Current evidence schema remains unchanged for v1.0.0.
- v1.0.0 may improve guidance, examples, or release communication without schema changes.

Benefits:

- Lowest schema churn.
- Preserves existing examples and validators.
- Reduces release coordination cost.

Risks:

- Some mature v0.7.0 reconstruction or decision-support concepts may remain guidance-only.

### Option B: Preserve schema and add guidance/examples later

Meaning:

- Schema remains unchanged.
- Examples, fixtures, or guidance explain how existing fields support current concepts.

Benefits:

- Improves usability without schema churn.
- Keeps validators stable.

Risks:

- Requires careful example wording to avoid implying schema completeness.

### Option C: Targeted schema clarification

Meaning:

- Schema wording, descriptions, or documentation are clarified without major structural change.

Benefits:

- Improves clarity.
- May align schema documentation with v1.0.0 posture.

Risks:

- Requires example and validator impact review.

### Option D: Selected schema field update

Meaning:

- New or refined fields are added for specific concepts such as non-execution, evidence gaps, residual uncertainty, or decision linkage.

Benefits:

- Stronger structured support for mature concepts.

Risks:

- Higher coordination cost.
- Requires examples, validators, assessment artifacts, testing procedures, and release notes to be reviewed.

### Option E: Broader schema redesign

Meaning:

- Evidence schema is redesigned for v1.0.0.

Benefits:

- Potentially more complete structure.

Risks:

- High scope creep risk.
- High validator and example update cost.
- Not recommended without a dedicated roadmap.

## Initial recommendation

The initial recommendation is:

> Preserve the current evidence schema by default while reviewing examples, fixtures, and validators together.
>
> Treat targeted schema clarification or selected field updates as later decisions only after example and validator readiness review.
>
> Do not pursue broad schema redesign by default for v1.0.0.

This keeps the path toward v1.0.0 achievable while preserving room for targeted improvement.

## Follow-up candidates for #363

Recommended #363 follow-up candidates:

- examples and fixtures readiness review,
- validator readiness and scope review,
- evidence schema / example / validator decision options,
- evidence schema, examples, and validator close-readiness checklist.

## Follow-up candidates for roadmap #350

Recommended later roadmap tracks:

- assessment artifact and testing procedure readiness review,
- implementation and adoption guidance readiness review,
- release readiness and communication planning,
- final v1.0.0 release decision.

## Claim boundaries

This review does not claim:

- v1.0.0 release,
- active baseline update,
- control catalog update,
- control ID update,
- evidence schema update,
- assessment artifact update,
- testing procedure update,
- example or fixture coverage,
- validator sufficiency,
- evidence sufficiency,
- semantic correctness,
- operational readiness,
- production readiness,
- implementation conformance,
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

- Does this review preserve evidence schema stability?
- Does it avoid implicitly updating the active baseline?
- Does it distinguish schema validity from evidence sufficiency?
- Does it distinguish repository validation from implementation conformance?
- Does it identify readiness questions for non-execution, evidence gaps, reconstruction, and risk-owner decision support?
- Does it identify example and validator follow-up needs?
- Does it preserve claim boundaries?
- Does it provide enough direction for later #363 artifacts?

## Scope reminder

This artifact is readiness-review material only.

It does not update the active control and assessment baseline, control catalog, control IDs, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, GitHub Releases, README release posture, or citation status.

It does not establish evidence sufficiency, semantic correctness, operational readiness, production readiness, implementation conformance, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
