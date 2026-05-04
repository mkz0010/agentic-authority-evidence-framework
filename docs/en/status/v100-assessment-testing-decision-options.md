# v1.0.0 Assessment and Testing Decision Options

## Purpose

This document records decision options for assessment artifacts and testing procedures on the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #369, `[Track] v1.0.0: Assessment Artifact and Testing Procedure Readiness Review`
- `docs/en/status/v100-assessment-artifact-readiness-review.md`
- `docs/en/status/v100-testing-procedure-readiness-review.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- completed track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`

The goal is to make assessment artifact and testing procedure update or non-update choices explicit before any v1.0.0 release-readiness decision.

This document is readiness-review and decision-support material only. It does not update assessment artifacts, testing procedures, the evidence schema, examples, fixtures, validators, the active baseline, the control catalog, release tags, or GitHub Releases.

## Current posture

As of this review:

- v1.0.0 path planning is active under roadmap #350.
- #369 has reviewed assessment artifact readiness at the planning level.
- #369 has reviewed testing procedure readiness at the planning level.
- The current control catalog and control IDs are preserved by default for v1.0.0 planning.
- The current evidence schema, examples, fixtures, and validators are preserved by default unless later explicit updates are scoped.
- Current assessment artifacts are recommended to be preserved by default while reviewing testing procedures and release communication needs.
- Current testing procedures are recommended to be preserved by default while documenting testing scope and reviewer judgment boundaries.
- The active control and assessment baseline has not been changed by #369.
- Any future assessment artifact or testing procedure update must be explicit.

## Decision posture

The recommended posture is:

> Keep assessment and testing choices explicit.
>
> Do not allow v1.0.0 planning maturity, assessment artifact availability, testing procedure availability, worksheet completion, repository validation, or example validation to imply assessment sufficiency, testing sufficiency, evidence sufficiency, semantic correctness, implementation conformance, operational readiness, production readiness, audit sufficiency, legal sufficiency, control conformance, certification, compliance, conformity, or external-framework equivalence.
>
> Prefer stability and scoped explanatory guidance before changing assessment artifacts or testing procedures.

This keeps the v1.0.0 path practical without converting readiness review into an assurance claim.

## Decision options summary

| Option | Summary | Initial posture |
| --- | --- | --- |
| Option A | Preserve current assessment artifacts and testing procedures unchanged. | Safest stability option. |
| Option B | Preserve artifacts and add explanatory guidance only. | Strong low-churn usability option. |
| Option C | Apply targeted wording clarification later. | Possible if ambiguity is identified. |
| Option D | Update selected assessment artifacts later. | Useful only after explicit scope review. |
| Option E | Update selected testing procedures later. | Useful only after explicit scope review. |
| Option F | Update assessment artifacts and testing procedures together later. | Higher coordination cost. |
| Option G | Add targeted validators later. | Possible only for narrow repository hygiene checks. |
| Option H | Broader assessment/testing redesign. | Not recommended by default for v1.0.0. |
| Option I | Treat assessment/testing as conformance or certification mechanisms. | Non-goal. |

## Option A: Preserve current assessment artifacts and testing procedures unchanged

Meaning:

- Assessment quick start material remains unchanged.
- Assessment worksheets remain unchanged.
- Assessment profiles remain unchanged.
- Testing procedures remain unchanged.
- Current validators remain unchanged.
- v1.0.0 planning may still reference these artifacts as current review-support material.

Benefits:

- Lowest churn.
- Preserves the current assessment/testing posture.
- Avoids accidental baseline changes.
- Avoids accidental pass/fail meaning changes.
- Avoids introducing new validator expectations.
- Keeps v1.0.0 path achievable.

Risks:

- Some v1.0.0 usability improvements may remain guidance-only.
- Pass/fail boundaries may still require careful release communication.
- Evidence request expectations may remain less explicit than desired.

Best fit when:

- maintainers prioritize stability;
- later assessment/testing updates are expected as separate work; and
- v1.0.0 does not need immediate assessment/testing artifact changes.

## Option B: Preserve artifacts and add explanatory guidance only

Meaning:

- Assessment artifacts and testing procedures remain unchanged.
- Documentation explains how to use them with v1.0.0 planning material.
- Release communication clarifies what assessment and testing artifacts do and do not prove.

Benefits:

- Improves usability without changing assessment/testing artifacts.
- Reduces false-assurance risk.
- Helps users distinguish assessment support from assessment sufficiency.
- Helps users distinguish testing support from testing sufficiency.
- Keeps release scope controlled.

Risks:

- Does not mechanically improve worksheets, profiles, or testing procedures.
- Users may still want concrete artifact updates later.

Best fit when:

- current artifacts are structurally adequate;
- interpretation and release communication need improvement; and
- v1.0.0 should avoid artifact churn.

## Option C: Apply targeted wording clarification later

Meaning:

- Specific wording in assessment or testing material is clarified.
- Control catalog, control IDs, evidence schema, examples, fixtures, and validators remain unchanged unless separately scoped.
- The clarification is narrow and explicitly reviewed.

Benefits:

- Improves interpretation.
- Can reduce pass/fail ambiguity.
- Can reduce evidence-request ambiguity.
- Can reduce overclaim risk.

Risks:

- May unintentionally change pass/fail meaning.
- May imply new evidence requirements if not carefully scoped.
- Requires release communication and validator impact review.

Best fit when:

- specific ambiguity is identified;
- wording can be clarified without changing substance; and
- reviewers agree the update is not a baseline change unless explicitly stated.

## Option D: Update selected assessment artifacts later

Meaning:

- Selected assessment artifacts, such as worksheets, profiles, or quick-start guidance, are updated after explicit review.
- Testing procedures may remain unchanged or be updated separately.

Benefits:

- Improves practical adoption.
- Can better align assessment artifacts with stable guidance.
- Can improve evidence gap, residual uncertainty, and reviewer judgment capture.

Risks:

- Requires testing procedure alignment review.
- May require validator updates.
- May require release communication changes.
- May be mistaken for assessment sufficiency or conformance tooling if overdescribed.

Best fit when:

- a specific assessment artifact gap is identified;
- the change is narrow and useful; and
- the relationship to testing procedures and validators is explicit.

## Option E: Update selected testing procedures later

Meaning:

- Selected testing procedures are updated after explicit review.
- Assessment artifacts may remain unchanged or be updated separately.

Benefits:

- Improves testing clarity.
- Can improve evidence request expectations.
- Can improve pass/fail boundary language.
- Can better align testing procedures with stable guidance.

Risks:

- Requires assessment artifact alignment review.
- May require evidence schema or example relationship review.
- May imply new control expectations if not carefully scoped.
- May be mistaken for implementation conformance testing if overdescribed.

Best fit when:

- a specific testing procedure gap is identified;
- the change is narrow and controlled; and
- reviewer judgment boundaries are preserved.

## Option F: Update assessment artifacts and testing procedures together later

Meaning:

- Assessment artifacts and testing procedures are updated together in a coordinated later PR or track.

Benefits:

- Stronger alignment between worksheets, profiles, evidence requests, and testing expectations.
- Reduces drift between assessment and testing material.
- Can improve v1.0.0 usability more comprehensively.

Risks:

- Higher coordination cost.
- Higher release communication burden.
- Higher false-assurance risk.
- May delay v1.0.0 if treated as required.

Best fit when:

- multiple related assessment/testing gaps are identified;
- maintainers want coordinated artifact changes; and
- the work is explicitly scoped as artifact updates, not certification or conformance claims.

## Option G: Add targeted validators later

Meaning:

- Add narrow repository validators for selected assessment or testing artifacts.
- Candidate checks may include index registration, file presence, column/header consistency, controlled value checks, or prohibited overclaim wording checks.

Benefits:

- Improves repository hygiene.
- Reduces drift.
- Helps maintain release discipline.

Risks:

- Can create false assurance if validator success is described too broadly.
- Adds maintenance burden.
- Does not prove assessment sufficiency or testing sufficiency.

Best fit when:

- checks are narrow and actionable;
- validator outputs are clear;
- validator scope is documented; and
- passing validation is clearly framed as repository hygiene only.

## Option H: Broader assessment/testing redesign

Meaning:

- Assessment quick start material, worksheets, profiles, testing procedures, evidence request guidance, and pass/fail models are redesigned together.

Benefits:

- Potentially stronger long-term assessment experience.
- Could provide clearer assessment/testing package structure.

Risks:

- High scope creep.
- High risk of implying conformance, certification, compliance, audit, or legal sufficiency.
- Requires broad review across baseline artifacts, evidence schema, examples, validators, README, release notes, and public communication.
- Not recommended by default for v1.0.0.

Initial posture:

- Future work by default.
- Not the default path for #369.

## Option I: Treat assessment/testing as conformance or certification mechanisms

Meaning:

- Assessment artifacts or testing procedures are positioned as proving conformance, compliance, certification, audit sufficiency, or legal sufficiency.

Initial posture:

- Non-goal.
- Should not be selected.

Rationale:

- AAEF does not claim to be a certification scheme.
- AAEF does not claim legal sufficiency.
- AAEF does not claim audit sufficiency.
- AAEF does not claim external-framework equivalence.
- Assessment and testing artifacts support review, not final assurance by themselves.

## Dependency impact matrix

| Change type | Assessment artifact impact | Testing procedure impact | Validator impact | Release communication impact |
| --- | --- | --- | --- | --- |
| Preserve unchanged | None | None | None | Clarify limits only. |
| Explanatory guidance only | None | None | None | Explain interpretation and boundaries. |
| Targeted wording clarification | Low/medium | Low/medium | Possible documentation or validator wording review | Must disclose clarification and scope. |
| Selected assessment update | Medium | Alignment review needed | Possible validator impact | Must state assessment support limits. |
| Selected testing update | Alignment review needed | Medium | Possible validator impact | Must state testing support limits. |
| Coordinated assessment/testing update | High | High | Possible validator changes | Requires clear release notes. |
| Targeted validators | May require expected structure | May require expected structure | Medium | Must state validator scope. |
| Broader redesign | Very high | Very high | High | Requires dedicated roadmap/migration notes. |
| Conformance/certification positioning | Not acceptable | Not acceptable | Not acceptable | Non-goal. |

## Option comparison

| Criterion | A | B | C | D | E | F | G | H | I |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Churn | Very low | Low | Medium | Medium | Medium | High | Medium | Very high | Not acceptable |
| Usability gain | Low | Medium | Medium | High | High | High | Medium | High | Not acceptable |
| False-assurance risk | Low | Low | Medium | Medium | Medium | Medium-high | Medium-high | High | Very high |
| Maintenance cost | Low | Low | Medium | Medium | Medium | High | Medium | Very high | Not acceptable |
| Fit for near-term v1.0.0 | Strong | Strong | Possible | Later | Later | Later | Later | Weak | Non-goal |

## Initial recommendation

The initial recommendation for #369 is:

> Prefer Option B as the near-term v1.0.0 posture:
>
> preserve current assessment artifacts and testing procedures while improving explanatory guidance and release communication about their scope.
>
> Keep targeted wording clarification available if specific ambiguity is identified.
>
> Treat selected assessment artifact updates, selected testing procedure updates, and targeted validators as later scoped options.
>
> Do not pursue broader assessment/testing redesign by default for v1.0.0.
>
> Do not position assessment artifacts or testing procedures as conformance, certification, compliance, audit, or legal sufficiency mechanisms.

This recommendation keeps v1.0.0 achievable while preserving conservative claim boundaries.

## Pass/fail decision posture

Assessment and testing decision options should preserve the following pass/fail posture:

- A pass result should be scoped to the assessed evidence, control, action, system, or test context.
- A pass result should not imply complete implementation conformance.
- A fail result should not imply complete root-cause analysis.
- Insufficient evidence should be distinguishable from confirmed control failure.
- Not assessed, not applicable, partial, or inconclusive states may require later review.
- Reviewer judgment should remain explicit.
- Residual uncertainty should remain recordable.

This document does not update pass/fail labels or criteria.

## Evidence request decision posture

Assessment and testing decision options should preserve the following evidence request posture:

- Evidence requests should be action-bound where relevant.
- Evidence should be linked to authority, authorization, dispatch, backend result, and outcome where applicable.
- Independently generated or corroborated evidence should be distinguished from self-report.
- Missing, conflicting, or uncorrelated evidence should remain reviewable.
- Evidence request guidance should not automatically claim evidence sufficiency.
- Evidence request guidance should not require evidence schema changes unless separately scoped.

This document does not update evidence request requirements.

## Reviewer judgment decision posture

Assessment and testing decision options should preserve the following reviewer judgment posture:

- Assessment artifacts support reviewer judgment.
- Testing procedures support reviewer judgment.
- Worksheet completion is not assessment sufficiency.
- Testing procedure execution is not testing sufficiency.
- Repository validator success is not assessment or testing sufficiency.
- Management and risk-owner decisions remain distinct from assessment/test artifacts.
- Automated risk acceptance is not claimed.

This document does not automate reviewer judgment.

## Validator relationship decision posture

Assessment and testing decision options should preserve the following validator posture:

- Validators may support repository hygiene.
- Validators do not prove assessment sufficiency.
- Validators do not prove testing sufficiency.
- Validators do not prove implementation conformance.
- Validators do not prove evidence sufficiency.
- Validators do not prove semantic correctness.
- Validators do not prove operational or production readiness.
- Any future validator must have explicit scope and claim boundaries.

This document does not add or update validators.

## Candidate near-term path

A reasonable near-term path is:

1. Complete assessment artifact readiness review.
2. Complete testing procedure readiness review.
3. Document assessment/testing decision options in this note.
4. Complete assessment/testing close-readiness checklist.
5. Close #369 if maintainers agree the track is complete.
6. Continue roadmap #350 with implementation/adoption guidance readiness review or release readiness/communication planning.

## Release communication implications

Any future v1.0.0 release communication should state:

- whether assessment artifacts changed;
- whether testing procedures changed;
- whether validators changed;
- whether evidence schema/examples/fixtures changed;
- whether the active baseline changed;
- whether assessment and testing artifacts are reviewer-support material;
- what assessment and testing artifacts do not prove;
- what validator success does and does not prove;
- whether pass/fail wording changed; and
- which assurance claims are not made.

## Recommended decision language

Recommended near-term wording:

> For v1.0.0 planning, preserve current assessment artifacts and testing procedures by default.
>
> Treat them as reviewer-support and implementation-review support material.
>
> Do not treat worksheet completion, testing procedure execution, repository validation, or example validation as assessment sufficiency, testing sufficiency, evidence sufficiency, semantic correctness, implementation conformance, operational readiness, production readiness, audit sufficiency, legal sufficiency, control conformance, certification, compliance, conformity, or external-framework equivalence.
>
> Consider targeted wording clarification or selected artifact updates only after scope, pass/fail impact, evidence-request impact, reviewer-judgment impact, validator impact, maintenance cost, and false-assurance risk are explicit.

## Follow-up candidates for #369

Recommended #369 follow-up:

- assessment/testing close-readiness checklist.

Optional follow-up candidates:

- assessment pass/fail boundary note,
- evidence request and reviewer judgment note,
- targeted assessment artifact update proposal,
- targeted testing procedure update proposal,
- assessment/testing validator candidate note.

## Follow-up candidates for roadmap #350

Recommended later roadmap tracks:

- implementation and adoption guidance readiness review,
- release readiness and communication planning,
- README / citation / release-note update decision,
- final v1.0.0 release decision.

## Claim boundaries

This decision-options note does not claim:

- v1.0.0 release,
- active baseline update,
- control catalog update,
- control ID update,
- evidence schema update,
- assessment artifact update,
- testing procedure update,
- validator update,
- assessment sufficiency,
- testing sufficiency,
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

- Does this note make assessment/testing options explicit?
- Does it avoid implicitly updating assessment artifacts?
- Does it avoid implicitly updating testing procedures?
- Does it preserve pass/fail boundaries?
- Does it preserve evidence request boundaries?
- Does it preserve reviewer judgment?
- Does it distinguish repository validation from assessment/testing sufficiency?
- Does it identify false-assurance and maintenance tradeoffs?
- Does it preserve claim boundaries?
- Does it provide enough direction for #369 close-readiness?

## Scope reminder

This artifact is readiness-review and decision-support material only.

It does not update the active control and assessment baseline, control catalog, control IDs, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, GitHub Releases, README release posture, or citation status.

It does not establish assessment sufficiency, testing sufficiency, evidence sufficiency, semantic correctness, operational readiness, production readiness, implementation conformance, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
