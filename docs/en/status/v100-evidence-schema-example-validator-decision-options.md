# v1.0.0 Evidence Schema, Example, and Validator Decision Options

## Purpose

This document records decision options for evidence schema, examples, fixtures, and validators on the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`
- `docs/en/status/v100-evidence-schema-readiness-review.md`
- `docs/en/status/v100-examples-and-fixtures-readiness-review.md`
- `docs/en/status/v100-validator-readiness-and-scope-review.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`

The goal is to make schema, example, fixture, and validator update or non-update choices explicit before any v1.0.0 release-readiness decision.

This document is readiness-review and decision-support material only. It does not update the evidence schema, add examples, add fixtures, update validators, update the active baseline, update the control catalog, update assessment artifacts, update testing procedures, create release tags, or publish GitHub Releases.

## Current posture

As of this review:

- v1.0.0 path planning is active under roadmap #350.
- #363 has reviewed evidence schema readiness at the planning level.
- #363 has reviewed examples and fixtures readiness at the planning level.
- #363 has reviewed validator readiness and scope boundaries at the planning level.
- The current evidence schema is recommended to be preserved by default unless a later targeted update is explicitly scoped.
- Current examples and fixtures are recommended to be preserved by default while targeted additions are reviewed together with validator readiness.
- Current validators are recommended to be preserved by default while validator scope is documented clearly.
- The active control and assessment baseline has not been changed by #363.
- Any future schema, example, fixture, or validator update must be explicit.

## Decision posture

The recommended posture is:

> Keep evidence schema, example, fixture, and validator choices explicit.
>
> Do not allow v1.0.0 planning maturity, example availability, or validator success to imply evidence sufficiency, semantic correctness, implementation conformance, operational readiness, production readiness, audit sufficiency, legal sufficiency, control conformance, certification, compliance, conformity, or external-framework equivalence.
>
> Prefer stability and scoped guidance before adding schema fields, new scenario fixtures, or broader validators.

This keeps the v1.0.0 path usable without creating false assurance.

## Decision options summary

| Option | Summary | Initial posture |
| --- | --- | --- |
| Option A | Preserve current schema, examples, fixtures, and validators unchanged. | Safest stability option. |
| Option B | Preserve artifacts and add explanatory guidance only. | Strong low-churn usability option. |
| Option C | Add selected examples later. | Useful if narrowly scoped. |
| Option D | Add selected scenario fixtures later. | Useful but higher maintenance. |
| Option E | Add targeted validator checks later. | Useful only after example/fixture scope is explicit. |
| Option F | Apply targeted schema clarification later. | Possible after example/validator impact review. |
| Option G | Add selected schema fields later. | Higher coordination cost. |
| Option H | Broader schema/example/validator redesign. | Not recommended by default. |
| Option I | Broad semantic validator expansion. | Future work by default due to false-assurance risk. |

## Option A: Preserve current artifacts unchanged

Meaning:

- Evidence schema remains unchanged.
- Current examples remain unchanged.
- No scenario fixtures are added.
- Validators remain unchanged.
- v1.0.0 may still use current validation as repository hygiene.

Benefits:

- Lowest churn.
- Preserves current validator behavior.
- Reduces risk of accidental baseline or schema drift.
- Keeps v1.0.0 path achievable.

Risks:

- Some practical scenario gaps remain unaddressed.
- Non-execution, evidence gaps, operational reconstruction, and risk-owner decision support may remain guidance-only.
- Users may want more concrete examples.

Best fit when:

- maintainers prioritize stability;
- later schema/example/validator tracks are expected; and
- v1.0.0 does not need expanded scenario coverage.

## Option B: Preserve artifacts and add explanatory guidance only

Meaning:

- Evidence schema, examples, fixtures, and validators remain unchanged.
- Documentation explains how to read current examples and validator outputs.
- Release communication clarifies what validation does and does not prove.

Benefits:

- Improves usability without file or validator churn.
- Reduces false-assurance risk.
- Helps users distinguish schema validity from evidence sufficiency.

Risks:

- Does not provide new concrete examples.
- Does not mechanically check additional scenarios.

Best fit when:

- current artifacts are structurally sufficient;
- user interpretation needs improvement; and
- release communication clarity is the priority.

## Option C: Add selected examples later

Meaning:

- Add a small number of targeted examples after separate scoped review.
- Candidate examples may include denied, held, blocked, non-executed, evidence gap, operational reconstruction, or risk-owner decision package examples.

Benefits:

- Improves practical usability.
- Makes mature v0.7.0 concepts easier to understand.
- Can support future validator work.

Risks:

- Requires schema alignment review.
- Requires validator impact review.
- May be mistaken for complete scenario coverage if not clearly bounded.

Best fit when:

- concrete examples are needed for user understanding;
- scope is narrow; and
- claim boundaries are explicit.

## Option D: Add selected scenario fixtures later

Meaning:

- Add structured multi-file fixtures for selected scenarios.
- Candidate fixture paths may include permitted, denied, held, blocked, non-executed, or backend-rejected flows.

Benefits:

- Supports cross-artifact consistency review.
- Helps future fixture validators.
- Can make operational reconstruction examples more concrete.

Risks:

- Higher maintenance cost.
- May be mistaken for reference implementation or complete scenario coverage.
- Requires careful prototype/reference boundary wording.

Best fit when:

- future validators need multi-file fixtures;
- walkthroughs need structured examples; and
- maintainers are ready to preserve fixture scope boundaries.

## Option E: Add targeted validator checks later

Meaning:

- Add narrow validators only after targeted examples, fixtures, or schema expectations are explicit.
- Candidate checks may include required index registration, expected invalid example failure, scoped enum consistency, fixture cross-reference consistency, or prohibited overclaim wording.

Benefits:

- Improves repository hygiene.
- Reduces drift.
- Helps maintain release discipline.

Risks:

- Can create false assurance if described too broadly.
- Adds maintenance burden.
- May be mistaken for semantic correctness or evidence sufficiency.

Best fit when:

- checks are narrow and actionable;
- validator outputs are clear; and
- claim boundaries are documented.

## Option F: Apply targeted schema clarification later

Meaning:

- Clarify schema documentation or field descriptions without major structural change.
- Control IDs, control catalog, and active baseline remain unchanged unless separately updated.

Benefits:

- Improves interpretation.
- May align schema documentation with v1.0.0 guidance.
- Lower risk than adding new fields.

Risks:

- Still requires example and validator impact review.
- Could unintentionally broaden or narrow meaning.

Best fit when:

- existing fields are adequate but unclear;
- examples reveal interpretation ambiguity; and
- validators do not need major changes.

## Option G: Add selected schema fields later

Meaning:

- Add or refine schema fields for specific mature concepts.
- Candidate areas include non-execution, held/blocked outcomes, evidence gaps, residual uncertainty, operational reconstruction links, or risk-owner decision record links.

Benefits:

- Stronger structured support for mature concepts.
- Can improve example and validator clarity.

Risks:

- Higher coordination cost.
- Requires updates to examples, validators, documentation, possibly assessment artifacts and testing procedures.
- May delay v1.0.0.

Best fit when:

- current schema cannot represent important v1.0.0 needs;
- examples and validators are ready to move together; and
- release communication can clearly state the change.

## Option H: Broader schema/example/validator redesign

Meaning:

- Evidence schema, examples, fixtures, and validators are redesigned together.

Benefits:

- Potentially stronger long-term architecture.
- Could align mature concepts more comprehensively.

Risks:

- High scope creep.
- High maintenance cost.
- High false-assurance risk if rushed.
- Likely requires a dedicated roadmap, migration notes, and broader testing.

Initial posture:

- Not recommended by default for v1.0.0.

## Option I: Broad semantic validator expansion

Meaning:

- Attempt to validate deeper meaning, sufficiency, correctness, or assurance properties.

Benefits:

- Potentially useful if narrowly constrained in future work.

Risks:

- Very high false-assurance risk.
- Semantic correctness is context-dependent.
- Evidence sufficiency requires reviewer judgment.
- Operational truth cannot be proven from static repository files.
- Risk-owner judgment cannot be replaced by structural validation.

Initial posture:

- Future work by default.
- Do not pursue broad semantic validators by default for v1.0.0.

## Dependency impact matrix

| Change type | Schema impact | Example/fixture impact | Validator impact | Release communication impact |
| --- | --- | --- | --- | --- |
| Preserve unchanged | None | None | None | Clarify validation limits only. |
| Guidance only | None | None | None | Explain artifact interpretation. |
| Add selected examples | Usually none or low | Targeted additions | May require example validation updates | Must state examples are illustrative. |
| Add scenario fixtures | Possible alignment review | New fixture set | May require fixture validators | Must avoid reference implementation claims. |
| Add targeted validators | Usually none | May require expected files | New or changed checks | Must state validator scope. |
| Schema clarification | Documentation-level | May require example wording review | May require validator wording review | Must disclose clarification. |
| Selected schema field update | Medium/high | Requires example updates | Requires validator updates | Must disclose schema change. |
| Broad redesign | High | High | High | Requires detailed release/migration communication. |
| Semantic validators | Variable | Variable | High | Must avoid assurance overclaims. |

## Option comparison

| Criterion | A | B | C | D | E | F | G | H | I |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Churn | Very low | Low | Medium | Medium-high | Medium | Medium | High | Very high | High |
| Usability gain | Low | Medium | High | High | Medium | Medium | High | High | Uncertain |
| False-assurance risk | Low | Low | Medium | Medium | Medium-high | Medium | Medium-high | High | Very high |
| Maintenance cost | Low | Low | Medium | High | Medium | Medium | High | Very high | High |
| Fit for near-term v1.0.0 | Strong | Strong | Possible | Later | Later | Possible | Later | Weak | Weak |

## Initial recommendation

The initial recommendation for #363 is:

> Prefer Option B as the near-term v1.0.0 posture:
>
> preserve the current evidence schema, examples, fixtures, and validators while improving explanatory guidance and release communication about their scope.
>
> Keep Option C and Option E available for later targeted updates if selected examples or scoped validator checks become necessary.
>
> Treat Option F as possible if schema wording ambiguity is identified.
>
> Treat Option G as a later decision only after examples and validators are ready.
>
> Do not choose Option H or Option I by default.

This recommendation keeps v1.0.0 achievable while preserving a clear path for targeted future improvements.

## Candidate near-term path

A reasonable path is:

1. Complete evidence schema readiness review.
2. Complete examples and fixtures readiness review.
3. Complete validator readiness and scope review.
4. Document decision options in this note.
5. Close #363 after close-readiness review.
6. Continue later roadmap #350 work on assessment/testing readiness.
7. Decide later whether v1.0.0 needs targeted schema/example/validator changes before release.

## Release communication implications

Any future v1.0.0 release communication should state:

- whether the evidence schema changed;
- whether examples changed;
- whether fixtures changed;
- whether validators changed;
- which validators were run;
- what passing validation means;
- what passing validation does not mean;
- whether active baseline changed;
- whether examples are illustrative;
- whether fixtures are scoped or prototype material;
- whether any schema/example/validator changes are release-blocking; and
- which assurance claims are not made.

## Recommended decision language

Recommended near-term wording:

> For v1.0.0 planning, preserve the current evidence schema, examples, fixtures, and validators by default.
>
> Treat current validators as scoped repository hygiene checks.
>
> Treat current examples as illustrative or scoped artifacts.
>
> Do not treat schema validity, example validity, fixture consistency, or validator success as evidence sufficiency, semantic correctness, implementation conformance, operational readiness, production readiness, audit sufficiency, legal sufficiency, control conformance, certification, compliance, conformity, or external-framework equivalence.
>
> Consider targeted examples or validators only after the scenario, expected check, maintenance cost, and false-assurance risk are explicit.

## Follow-up candidates for #363

Recommended #363 follow-up:

- evidence schema, examples, and validator close-readiness checklist.

Optional follow-up candidates:

- minimum v1.0.0 example set decision note,
- validator scope matrix,
- evidence gap example candidate note,
- non-execution fixture candidate note,
- risk-owner decision package example candidate note.

## Follow-up candidates for roadmap #350

Recommended later roadmap tracks:

- assessment artifact and testing procedure readiness review,
- implementation and adoption guidance readiness review,
- release readiness and communication planning,
- final v1.0.0 release decision.

## Claim boundaries

This decision-options note does not claim:

- v1.0.0 release,
- active baseline update,
- evidence schema update,
- example update,
- fixture update,
- validator update,
- validator sufficiency,
- evidence sufficiency,
- semantic correctness,
- example coverage completeness,
- fixture coverage completeness,
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

- Does this note make schema, example, fixture, and validator options explicit?
- Does it avoid implicitly updating the evidence schema?
- Does it avoid implicitly adding examples or fixtures?
- Does it avoid implicitly changing validators?
- Does it distinguish repository validation from implementation assurance?
- Does it identify false-assurance and maintenance tradeoffs?
- Does it preserve claim boundaries?
- Does it provide enough direction for #363 close-readiness?

## Scope reminder

This artifact is readiness-review and decision-support material only.

It does not update the active control and assessment baseline, control catalog, control IDs, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, GitHub Releases, README release posture, or citation status.

It does not establish validator sufficiency, evidence sufficiency, semantic correctness, example coverage completeness, fixture coverage completeness, operational readiness, production readiness, implementation conformance, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
