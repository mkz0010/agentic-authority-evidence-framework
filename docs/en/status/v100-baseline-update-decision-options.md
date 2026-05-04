# v1.0.0 Baseline Update Decision Options

## Purpose

This document records baseline update decision options for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- `docs/en/status/v100-control-catalog-readiness-review.md`
- `docs/en/status/v100-baseline-artifact-readiness-review.md`
- `docs/en/status/v100-control-id-stability-note.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`

The goal is to make the main v1.0.0 baseline update options reviewable before any release-readiness or final release decision.

This document is readiness-review and decision-support material only. It does not update the active baseline, control catalog, control IDs, control wording, evidence schema, assessment artifacts, testing procedures, examples, fixtures, validators, release tags, or GitHub Releases.

## Current posture

As of this review:

- v1.0.0 path planning is active under roadmap #350.
- #351 completed baseline-scope and promotion-decision planning.
- #357 is reviewing control catalog and baseline artifact readiness.
- The current control catalog is recommended to be preserved by default unless a later explicit update is scoped.
- Existing control IDs are recommended to remain stable by default.
- The active control and assessment baseline has not been changed by #351, #357, or this artifact.
- Any future v1.0.0 baseline update must be explicit.

## Decision posture

The recommended posture is:

> Keep baseline update choices explicit.
>
> Do not allow roadmap completion, guidance maturity, artifact freshness, or validator success to imply a baseline update.
>
> Decide separately whether v1.0.0 preserves the active baseline, promotes stable guidance, clarifies wording, updates selected baseline artifacts, or defers baseline changes beyond v1.0.0.

This keeps the v1.0.0 path usable without creating accidental baseline drift.

## Decision options summary

| Option | Summary | Initial posture |
| --- | --- | --- |
| Option A | Preserve active baseline unchanged. | Safest baseline-stability option. |
| Option B | Preserve control catalog and promote selected stable guidance. | Strong practical usability option. |
| Option C | Preserve control IDs and apply targeted wording clarifications. | Possible later, but requires targeted review. |
| Option D | Update selected baseline artifacts. | Higher impact; requires coordinated readiness reviews. |
| Option E | Broader baseline update. | Highest coordination cost; not recommended without additional tracks. |
| Option F | Defer baseline update beyond v1.0.0. | Viable if v1.0.0 focuses on status, guidance, and release posture. |

## Option A: Preserve active baseline unchanged

Meaning:

- v1.0.0 does not update the active control and assessment baseline.
- Control catalog remains unchanged.
- Evidence schema remains unchanged.
- Assessment artifacts remain unchanged.
- Testing procedures remain unchanged.
- Existing examples and validators remain unchanged unless addressed separately.
- v1.0.0 may still improve status references, navigation, and release communication.

Benefits:

- Lowest baseline churn.
- Preserves control ID stability.
- Reduces dependency updates.
- Simplifies release communication.
- Avoids rushing control, schema, assessment, or testing changes.

Risks:

- v1.0.0 may appear less substantive as a baseline milestone.
- Mature v0.7.0 reconstruction and risk-owner decision support materials remain outside active baseline artifacts.
- Some users may expect v1.0.0 to update more than status and planning posture.

Required wording:

- Clearly state that the active baseline is preserved.
- Clearly state what v1.0.0 does stabilize, if anything.
- Avoid presenting stable guidance as active baseline.

Best fit when:

- maintainers prioritize stability and traceability,
- the release path should avoid control/schema churn, and
- later readiness tracks are expected.

## Option B: Preserve control catalog and promote selected stable guidance

Meaning:

- Control catalog remains unchanged.
- Control IDs remain unchanged.
- Selected mature planning materials may be promoted into stable guidance or recommended reading paths.
- Evidence gap classification, operational reconstruction, and risk-owner decision support may become stable guidance candidates.
- Active baseline artifacts remain unchanged unless separately updated.

Benefits:

- Improves practical usability without changing controls.
- Preserves control ID stability.
- Allows v0.7.0 mature materials to become more discoverable.
- Supports implementers, reviewers, operators, and risk owners.
- Avoids control catalog churn.

Risks:

- Requires careful wording to distinguish stable guidance from active baseline.
- May require README, document map, and release-note clarity.
- Could confuse users if guidance and baseline boundaries are not clearly stated.

Required follow-up:

- implementation/adoption guidance readiness review,
- reviewer/operator/risk-owner guidance alignment,
- release communication boundary review,
- README and entry-point update review.

Best fit when:

- v1.0.0 should be usable,
- baseline churn should remain low, and
- mature v0.7.0 materials should be easier to use.

## Option C: Preserve control IDs and apply targeted wording clarifications

Meaning:

- Existing control IDs remain stable.
- Select control catalog wording or baseline-adjacent wording may be clarified.
- No control renumbering occurs.
- No broad control catalog redesign occurs.

Benefits:

- Improves clarity while preserving traceability.
- Allows v1.0.0 wording to align with current framework maturity.
- Reduces risk compared with adding or renumbering controls.

Risks:

- Still changes baseline-relevant wording.
- May require updates to evidence schema discussion, assessment artifacts, testing procedures, mappings, README, and release notes.
- Could unintentionally broaden or narrow requirements if wording is not reviewed carefully.

Required follow-up:

- targeted control wording review,
- control ID stability confirmation,
- assessment and testing impact review,
- mapping impact review,
- release-note impact review.

Best fit when:

- current wording is mostly stable,
- a small number of clarifications materially improve usability, and
- maintainers are ready to review dependent artifacts.

## Option D: Update selected baseline artifacts

Meaning:

- One or more baseline-relevant artifacts are updated.
- Potential targets include control catalog wording, evidence schema, assessment artifacts, testing procedures, examples, or validators.
- Updates are selected and coordinated, not broad redesigns.

Benefits:

- More substantive v1.0.0 baseline improvement.
- Can align control, evidence, assessment, and validation artifacts.
- Can incorporate mature planning results into baseline-adjacent artifacts.

Risks:

- Higher coordination cost.
- Requires careful dependency review.
- May delay v1.0.0 release.
- Requires stronger validation and release communication.
- Increases chance of implicit conformance or readiness overclaims.

Required follow-up:

- evidence schema readiness review,
- examples and validator readiness review,
- assessment artifact readiness review,
- testing procedure readiness review,
- release readiness checklist,
- claim-boundary review.

Best fit when:

- maintainers decide v1.0.0 should be a substantive baseline update,
- dependencies can be reviewed in time, and
- release communication can clearly state what changed.

## Option E: Broader baseline update

Meaning:

- Control catalog, evidence schema, assessment artifacts, testing procedures, examples, and validators may be updated together.
- v1.0.0 becomes a more ambitious baseline release.

Benefits:

- Stronger alignment across baseline artifacts.
- More complete v1.0.0 baseline story.
- Potentially more useful for adoption if carefully executed.

Risks:

- Highest coordination cost.
- Highest risk of scope creep.
- Requires significant validation and review.
- May require mapping updates, README rewrites, release-note detail, and migration guidance.
- Could delay v1.0.0 substantially.
- Increases risk of overclaiming production readiness, implementation conformance, compliance, audit sufficiency, or legal sufficiency.

Required follow-up:

- dedicated baseline update roadmap,
- control catalog update PRs,
- schema update PRs,
- assessment/testing update PRs,
- example/validator update PRs,
- migration or change summary,
- release-readiness review,
- public communication boundary review.

Best fit when:

- maintainers intentionally choose a larger v1.0.0 scope and accept the coordination cost.

Initial recommendation:

- Do not choose this option by default during #357.

## Option F: Defer baseline update beyond v1.0.0

Meaning:

- v1.0.0 does not update active baseline artifacts.
- v1.0.0 focuses on clarified status, guidance, navigation, readiness planning, and release communication.
- Baseline artifact updates are deferred to a later roadmap.

Benefits:

- Keeps v1.0.0 achievable.
- Preserves current baseline stability.
- Avoids rushed control, schema, assessment, or testing changes.
- Allows later readiness tracks to mature.

Risks:

- May underuse the v1.0.0 milestone.
- Users may expect more from a v1.0.0 label.
- Requires very clear release communication.

Required wording:

- v1.0.0 is a stable public reference or planning milestone only if that is the decision.
- Active baseline remains unchanged.
- Later roadmap will handle baseline changes.

Best fit when:

- release timing matters,
- baseline artifacts are not ready for coordinated update, and
- conservative claim boundaries are prioritized.

## Dependency impact matrix

| Option | Control catalog | Control IDs | Evidence schema | Assessment artifacts | Testing procedures | Examples / fixtures | Validators | README / release notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A: Preserve baseline unchanged | No change | No change | No change | No change | No change | No change | No change | Clarify status only |
| B: Promote stable guidance | No change | No change | No change unless separately scoped | No change unless separately scoped | No change unless separately scoped | Optional later | Optional later | Update wording carefully |
| C: Targeted wording clarification | Targeted wording review | Stable | Impact review required | Impact review required | Impact review required | May require updates | May require updates | Must disclose clearly |
| D: Selected baseline artifact update | Possible targeted update | Prefer stable | Possible update | Possible update | Possible update | Possible update | Possible update | Detailed release notes required |
| E: Broader baseline update | Likely update | Avoid churn but review | Likely update | Likely update | Likely update | Likely update | Likely update | Full release communication required |
| F: Defer baseline update | No change | No change | No change | No change | No change | No change | No change | Explain deferral |

## Option comparison

| Criterion | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- |
| Baseline stability | High | High | Medium-high | Medium | Low-medium | High |
| Practical usability gain | Low-medium | High | Medium | High | High | Medium |
| Coordination cost | Low | Medium | Medium | High | Very high | Low |
| Risk of scope creep | Low | Medium | Medium | High | Very high | Low |
| Release communication complexity | Low | Medium | Medium | High | Very high | Medium |
| Fit with current #357 posture | Strong | Strong | Possible | Later review | Not default | Possible |

## Initial recommendation

The initial recommendation for #357 is:

> Prefer Option B as the leading v1.0.0 path candidate:
>
> preserve the current control catalog and control IDs by default, while promoting selected mature materials as stable guidance only after separate guidance/adoption readiness review.
>
> Keep Option A and Option F available if maintainers decide that v1.0.0 should avoid baseline-related promotion.
>
> Treat Option C or Option D as possible later decisions only after targeted readiness reviews.
>
> Do not choose Option E by default.

This keeps v1.0.0 useful while limiting baseline churn.

## Recommended near-term path

A reasonable near-term path is:

1. Complete #357 with control catalog, baseline artifact, control ID, and decision option reviews.
2. Open a later evidence schema, examples, and validator readiness track.
3. Open a later assessment artifact and testing procedure readiness track.
4. Open a later implementation/adoption guidance readiness track.
5. Decide whether stable guidance promotion is enough for v1.0.0.
6. Only then decide whether active baseline artifacts should change before release.

## Release communication implications

Any v1.0.0 release communication should state:

- whether v1.0.0 changes the active baseline,
- whether the control catalog changed,
- whether control IDs changed,
- whether the evidence schema changed,
- whether assessment artifacts changed,
- whether testing procedures changed,
- whether examples or validators changed,
- what materials are stable guidance,
- what materials remain planning-only or historical,
- what domains are future work, and
- what claims are not made.

## Claim boundaries

This decision-options note does not claim:

- v1.0.0 release,
- active baseline update,
- control catalog update,
- control ID update,
- control wording update,
- evidence schema update,
- assessment artifact update,
- testing procedure update,
- example or fixture coverage,
- validator sufficiency,
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

## Relationship to #357 close-readiness

This note supports #357 close-readiness by documenting the main baseline update options and their tradeoffs.

#357 can later close once maintainers agree that:

- control catalog readiness has been reviewed,
- baseline artifact readiness has been reviewed,
- control ID stability has been reviewed,
- baseline update options have been documented,
- claim boundaries are preserved, and
- follow-up v1.0.0 tracks are clear.

## Review questions

Reviewers should be able to answer:

- Does this note make baseline update options explicit?
- Does it avoid implicitly selecting a baseline update?
- Does it distinguish stable guidance promotion from baseline artifact update?
- Does it preserve control ID stability by default?
- Does it clarify dependency impacts for each option?
- Does it preserve claim boundaries?
- Does it support later v1.0.0 readiness tracks?
- Does it provide enough direction for #357 close-readiness?

## Scope reminder

This artifact is readiness-review and decision-support material only.

It does not update the active control and assessment baseline, control catalog, control IDs, control wording, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, GitHub Releases, README release posture, or citation status.

It does not establish operational readiness, production readiness, implementation conformance, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
