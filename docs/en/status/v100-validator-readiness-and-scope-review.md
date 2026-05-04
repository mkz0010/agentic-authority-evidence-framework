# v1.0.0 Validator Readiness and Scope Review

## Purpose

This document reviews validator readiness and validator scope boundaries for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`
- `docs/en/status/v100-evidence-schema-readiness-review.md`
- `docs/en/status/v100-examples-and-fixtures-readiness-review.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`

The goal is to review what current validators support for v1.0.0 planning, what they intentionally do not prove, what validator scope boundaries must be preserved, and what later validator work may be needed.

This document is readiness-review material only. It does not add executable validators, update existing validators, update the evidence schema, add examples, add fixtures, update the active baseline, update the control catalog, update assessment artifacts, update testing procedures, create release tags, or publish GitHub Releases.

## Current posture

As of this review:

- v1.0.0 path planning is active under roadmap #350.
- #363 is reviewing evidence schema, examples, fixtures, and validator readiness.
- Evidence schema readiness has been reviewed at the planning level.
- Examples and fixtures readiness has been reviewed at the planning level.
- Current validators support repository artifact consistency checks.
- Current validators should not be treated as proof of operational effectiveness, evidence sufficiency, semantic correctness, implementation conformance, production readiness, audit sufficiency, legal sufficiency, control conformance, certification, compliance, conformity, or external-framework equivalence.
- Validators are not updated by this document.
- Any future validator expansion must be explicit.

## Review posture

The recommended posture is:

> Treat validators as repository artifact checks with explicit scope.
>
> Preserve the boundary that passing validation means the checked files satisfy the validator's defined checks, not that an implementation is conformant, operationally ready, semantically correct, legally sufficient, audit sufficient, or safe.
>
> Review validator expansion only when the expected check, false-assurance risk, and claim boundary are explicit.

This posture supports v1.0.0 release discipline without turning repository validation into an overclaim.

## Validator readiness summary

| Validator or validator family | Current readiness posture | Boundary |
| --- | --- | --- |
| `tools/validate_markdown_indexes.py` | Ready as navigation/index consistency support. | Does not prove document correctness or baseline status. |
| `tools/validate_json_examples.py` | Ready as JSON example parse/structure support. | Does not prove evidence sufficiency or semantic correctness. |
| `tools/validate_evidence_schema.py` | Ready as evidence schema/example validation support. | Does not prove operational readiness or control conformance. |
| Evidence example validation | Ready for scoped example hygiene. | Does not prove complete example coverage. |
| Assessment/profile validators | Ready within existing repository scope where applicable. | Does not prove assessment sufficiency. |
| External mapping validators | Ready within mapping-format scope where applicable. | Does not prove compliance or equivalence. |
| Future fixture validators | Review-readiness candidate. | Must avoid reference-implementation or scenario-completeness claims. |
| Future semantic validators | Future work by default. | High false-assurance risk unless narrowly scoped. |

## What validators currently support

Current validators can support v1.0.0 planning by checking repository artifacts for scoped consistency.

They may help confirm:

- required files are discoverable in markdown indexes;
- JSON examples are parseable and structurally valid where checked;
- invalid examples fail as expected where included;
- evidence schema examples remain aligned with schema expectations where validated;
- mapped files remain in expected repository locations;
- repository documentation navigation remains less likely to drift; and
- release-supporting documentation references are less likely to omit newly added artifacts.

This is useful for release hygiene and reviewability.

It is not the same as implementation assurance.

## What validators do not prove

Validators should not be described as proving:

- evidence sufficiency,
- semantic correctness,
- operational readiness,
- production readiness,
- implementation conformance,
- control conformance,
- complete scenario coverage,
- complete example coverage,
- complete fixture coverage,
- complete reconstruction,
- complete root-cause analysis,
- audit sufficiency,
- legal sufficiency,
- automated risk acceptance,
- certification,
- compliance,
- conformity, or
- external-framework equivalence.

These boundaries should be preserved in README, release notes, status artifacts, and public communication.

## Markdown index validator readiness

`tools/validate_markdown_indexes.py` supports navigation and discoverability.

Readiness questions:

- Does it catch missing status document registrations?
- Does it catch missing document-map entries where scoped?
- Does it support traceability for v1.0.0 planning artifacts?
- Are failures actionable?
- Are scope limits clear?

Initial assessment:

- Ready as release-supporting repository hygiene.
- Useful for ensuring newly added planning artifacts are discoverable.
- Does not prove that indexed documents are correct, normative, current, or baseline.

Boundary:

- Passing markdown index validation means scoped index checks passed.
- It does not mean the repository's active baseline changed.
- It does not mean documents are authoritative beyond their stated scope.

## JSON example validator readiness

`tools/validate_json_examples.py` supports JSON example parse and structure checks.

Readiness questions:

- Does it check expected JSON example files?
- Does it catch invalid JSON or expected invalid examples?
- Are validator outputs clear enough for maintainers?
- Does it preserve the distinction between valid JSON and sufficient evidence?
- Does it avoid implying complete scenario coverage?

Initial assessment:

- Ready as scoped JSON example validation.
- Useful for preventing obvious example drift.
- Should remain bounded as structural/example validation.

Boundary:

- Passing JSON example validation does not prove evidence sufficiency.
- Passing JSON example validation does not prove the represented action was authorized, executed correctly, safe, or review-complete.

## Evidence schema validator readiness

`tools/validate_evidence_schema.py` supports evidence schema and evidence example validation.

Readiness questions:

- Does it check the current schema and examples consistently?
- Does it verify valid examples pass?
- Does it verify invalid examples fail where applicable?
- Are failure messages actionable?
- Are schema and example expectations clear?
- Does it avoid semantic overclaims?

Initial assessment:

- Ready as scoped schema/example validation support.
- Important for v1.0.0 evidence schema readiness.
- Should not be expanded without reviewing example and fixture impacts.

Boundary:

- Passing evidence schema validation means files satisfy current validator checks.
- It does not prove action correctness, authorization sufficiency, backend truth, operational effectiveness, audit sufficiency, legal sufficiency, semantic correctness, implementation conformance, or control conformance.

## Example and fixture validator relationship

Example and fixture readiness depends on validator clarity.

Readiness questions:

- Which examples are validator-covered?
- Which examples are illustrative only?
- Which invalid examples are expected to fail?
- Are scenario fixtures validated?
- Are cross-file consistency checks present?
- Are scenario types such as permitted, denied, held, blocked, and non-executed represented?
- Do validators avoid implying that covered examples are complete?

Initial assessment:

- Current examples appear ready for scoped validation review.
- Future fixture validators may be useful if scenario fixtures are added.
- Validator expansion should follow example/fixture scope decisions, not precede them.

Boundary:

- Validator-covered examples are not evidence of real-world implementation.
- Fixture consistency is not production reference implementation proof.
- Scenario fixture validation is not complete scenario coverage.

## Assessment and testing validator relationship

Validators can support assessment artifact hygiene, but they do not replace assessment.

Readiness questions:

- Do any validators check assessment worksheets, profiles, or testing procedures?
- Are assessment artifact checks structural or semantic?
- Do validator names and outputs avoid implying assessment sufficiency?
- Are pass/fail criteria still reviewer-controlled?
- Do validators preserve management and reviewer judgment?

Initial assessment:

- Assessment and testing readiness should be reviewed under a later roadmap #350 track.
- Any assessment validator expansion should be scoped carefully.
- Validators should not be described as automated assessment or automated certification.

Boundary:

- Repository assessment validators are not assessor judgment.
- They do not prove controls operate.
- They do not establish compliance, conformity, audit sufficiency, legal sufficiency, or certification.

## External mapping validator relationship

External mapping validators can help preserve mapping format and references.

Readiness questions:

- Do mapping validators check only format and scoped consistency?
- Do they avoid equivalence claims?
- Do they avoid compliance claims?
- Do they avoid substitutability claims?
- Are mapping rows worded conservatively?
- Are failures actionable?

Initial assessment:

- External mapping validation should remain conservative.
- Mapping validation should not imply external-framework equivalence.

Boundary:

- Passing mapping validation does not prove compliance with mapped frameworks.
- Passing mapping validation does not prove equivalence, conformity, or audit sufficiency.

## False-assurance risks

Validator expansion can create false assurance if users misunderstand passing checks.

Key risks:

- treating schema validity as evidence sufficiency;
- treating example validity as implementation correctness;
- treating fixture consistency as production readiness;
- treating mapping validation as external-framework equivalence;
- treating assessment artifact validation as audit sufficiency;
- treating markdown index validation as baseline status;
- treating validator success as semantic correctness; and
- treating repository checks as operational assurance.

Mitigation:

- name validators and outputs carefully;
- document validator scope;
- keep claim boundaries in README/release notes;
- avoid broad semantic validators unless narrowly scoped;
- include invalid examples where useful;
- keep validator failure messages actionable; and
- separate repository hygiene from implementation assurance.

## Future validator expansion candidates

Potential future validator work may include:

- example coverage inventory checks,
- fixture consistency checks,
- denied/non-executed scenario fixture checks,
- evidence gap example structure checks,
- risk-owner decision package example checks,
- release-readiness index checks,
- claim-boundary wording checks for examples or mappings, and
- validator scope documentation checks.

These should be scoped separately.

They should not be added by this readiness review.

## Semantic validator posture

Semantic validators should remain future work by default.

Rationale:

- semantic checks can easily overclaim;
- semantic correctness is context-dependent;
- evidence sufficiency requires reviewer judgment;
- operational truth cannot be fully determined from static repository files;
- risk-owner decision support cannot be reduced to structural validation; and
- broad semantic validation may create false confidence.

Possible narrow exceptions:

- prohibited wording checks,
- required disclaimer presence checks,
- known field consistency checks,
- known enum consistency checks,
- scoped cross-file reference checks.

Even narrow semantic-like checks should be described as scoped repository checks, not semantic assurance.

## Validator update options

This review leaves several options open.

### Option A: Preserve current validators unchanged

Meaning:

- Current validators remain unchanged for v1.0.0.
- Validator scope is documented and bounded.

Benefits:

- Lowest implementation churn.
- Avoids false-assurance risk from new checks.
- Keeps v1.0.0 path achievable.

Risks:

- Some example/fixture gaps may remain unchecked.

### Option B: Preserve validators and improve validator documentation

Meaning:

- No validator behavior changes.
- Documentation clarifies what validators do and do not prove.

Benefits:

- Improves release communication.
- Reduces false assurance without code changes.

Risks:

- Does not improve mechanical coverage.

### Option C: Add targeted validator checks later

Meaning:

- Add narrow checks for specific examples, fixtures, or references.

Benefits:

- Improves repository hygiene.
- Can support targeted v1.0.0 usability improvements.

Risks:

- Requires careful scope and claim-boundary wording.
- Requires maintenance.

### Option D: Add broader fixture validators later

Meaning:

- Add multi-file scenario validation.

Benefits:

- Supports scenario walkthroughs.
- Helps detect cross-file drift.

Risks:

- Higher complexity.
- May be mistaken for reference implementation assurance.

### Option E: Add broad semantic validators

Meaning:

- Attempt to validate deeper meaning, sufficiency, or correctness.

Benefits:

- Potentially powerful if narrowly defined.

Risks:

- High false-assurance risk.
- Not recommended by default for v1.0.0.

## Initial recommendation

The initial recommendation is:

> Preserve current validators by default and document their scope clearly.
>
> Treat validator documentation and claim-boundary clarity as higher priority than broad validator expansion for v1.0.0.
>
> Consider targeted validator additions only after example, fixture, schema, and release-readiness needs are explicit.
>
> Do not pursue broad semantic validators by default.

This keeps v1.0.0 validation useful while avoiding overclaiming.

## Relationship to release communication

Release communication should state:

- which validators were run;
- what validator success means;
- what validator success does not mean;
- whether validators changed in the release;
- whether examples or schema changed;
- whether active baseline changed;
- whether validator success is a release hygiene signal only; and
- which assurance claims are not made.

Validation wording should be especially careful for v1.0.0 because users may interpret a stable release label as stronger assurance than intended.

## Recommended follow-up work for #363

Recommended #363 follow-up candidates:

- evidence schema / example / validator decision options,
- evidence schema, examples, and validator close-readiness checklist.

Optional follow-up candidates:

- validator scope matrix,
- validator claim-boundary checklist,
- minimum v1.0.0 validator set note,
- future fixture validator candidate note.

## Claim boundaries

This review does not claim:

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

- Does this review clarify what validators currently support?
- Does it clarify what validators do not prove?
- Does it preserve the distinction between repository validation and implementation assurance?
- Does it identify false-assurance risks?
- Does it clarify relationships to schema, examples, fixtures, assessment artifacts, testing procedures, and mappings?
- Does it avoid broad semantic validator overclaims?
- Does it preserve claim boundaries?
- Does it provide enough direction for later #363 artifacts?

## Scope reminder

This artifact is readiness-review material only.

It does not update the active control and assessment baseline, control catalog, control IDs, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, GitHub Releases, README release posture, or citation status.

It does not establish validator sufficiency, evidence sufficiency, semantic correctness, example coverage completeness, fixture coverage completeness, operational readiness, production readiness, implementation conformance, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
