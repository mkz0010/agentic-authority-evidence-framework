# v0.5.x AAEF-EVD-01 Evidence Sufficiency and Limitation Review Proposal

**Status:** Temporary, non-normative review proposal

## Purpose

This document reviews whether `AAEF-EVD-01` should receive evidence sufficiency or evidence limitation refinement after the v0.5.x evidence integrity follow-up work.

It follows:

- `docs/en/status/v050x-evidence-integrity-negative-tests-track-proposal.md`
- `docs/en/status/v050x-evidence-integrity-negative-tests-candidate-appendix.md`
- `docs/en/status/v050x-evidence-integrity-negative-tests-csv-refinement-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md`
- `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md`
- `docs/en/status/v050x-negative-evidence-examples-fixtures-decision-proposal.md`
- `docs/en/status/v050x-follow-up-status.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Primary source issue:

- #165 — evidence integrity and tamper-evident evidence

Primary active row under review:

- `AAEF-EVD-01`

Related active row:

- `AAEF-EVD-04`

This proposal does not update active testing procedures.

It does not update the Evidence Event Schema.

It does not add evidence examples.

It does not add validator fixtures.

It does not close #165 by itself.

## Review Context

Recent v0.5.x work addressed several evidence integrity topics:

- optional evidence integrity schema fields;
- integrity-focused positive example;
- approval binding example;
- evidence integrity negative test candidates;
- active `AAEF-EVD-04` review;
- incident-response evidence preservation guidance;
- incident-response preservation candidate appendix;
- evidence depth / E5 decision;
- negative examples and validator fixtures decision.

That work clarified an important distinction:

- `AAEF-EVD-04` concerns integrity and tamper-evidence;
- `AAEF-EVD-01` concerns whether evidence is sufficient to support an assessment result.

Evidence can be structurally valid and integrity-protected while still being insufficient.

Evidence can also be sufficient for a low-risk review but insufficient for a high-impact disputed action.

## Review Question

Should `AAEF-EVD-01` be refined to more explicitly cover evidence sufficiency and evidence limitation handling?

This review focuses on whether the active testing language should better distinguish:

- evidence existence;
- evidence integrity;
- evidence independence;
- evidence completeness;
- evidence action-binding;
- evidence trust limitations;
- assessment confidence.

## Key Distinction

Evidence sufficiency is not the same as evidence integrity.

| Concept | Primary concern | Example |
| --- | --- | --- |
| Evidence existence | Whether evidence exists at all | A log entry exists for an action. |
| Evidence integrity | Whether evidence was protected from alteration or omission | A proof reference verifies the evidence package. |
| Evidence independence | Whether evidence is generated or corroborated outside the model or agent runtime | Backend execution log corroborates a tool call. |
| Evidence completeness | Whether required parts of the action story are present | Authorization, dispatch, execution, and non-execution records are present. |
| Evidence action-binding | Whether evidence refers to the assessed action | Approval record matches the action digest. |
| Evidence limitation | Whether missing, weak, partial, or unverifiable evidence is disclosed | Verification unavailable; model summary only. |
| Evidence sufficiency | Whether the available evidence can support the assessment conclusion | Evidence is sufficient for the action risk and claim. |

## Candidate Sufficiency Concerns

`AAEF-EVD-01` may need to make the following concepts more explicit:

| Concern | Description | Potential relevance |
| --- | --- | --- |
| Action-bound evidence | Evidence should be tied to the assessed action, not a generic system state. | High |
| Independently generated or corroborated evidence | Evidence should not rely only on model or agent self-report. | High |
| Evidence limitation disclosure | Missing, partial, unverifiable, or weak evidence should be recorded. | High |
| Risk-proportionate evidence | Higher-impact actions require stronger evidence. | Medium |
| Evidence completeness | The evidence package should cover relevant authorization, approval, dispatch, execution, or non-execution records. | High |
| Evidence confidence | Assessment confidence should be reduced when evidence is partial. | Medium |
| Evidence source trust | Evidence source should be understood and not overclaimed. | High |
| Model-output boundary | Model-generated summaries should not be treated as authority or independent evidence. | High |

## Proposed Decision Options

### Option A — No active change

Keep `AAEF-EVD-01` unchanged.

Use existing guidance, examples, and status documents to explain sufficiency and limitation concepts.

Benefits:

- avoids unnecessary CSV churn;
- preserves current active baseline;
- avoids broadening #165 too much.

Risks:

- sufficiency and limitation expectations may remain less visible;
- reviewers may overtrust schema-valid or integrity-protected evidence;
- distinction between integrity and sufficiency may not be clear enough.

### Option B — Narrow active CSV refinement

Refine `AAEF-EVD-01` testing criteria to explicitly mention evidence limitations and reduced assurance.

Possible direction:

> Verify that evidence is sufficient for the assessed action and risk level, is action-bound, and records material trust limitations such as missing, partial, unverifiable, model-generated, self-reported, or non-corroborated evidence.

Benefits:

- makes sufficiency boundary explicit;
- reinforces “schema-valid is not sufficient”;
- reinforces “model output is not authority”;
- supports future reviewer guidance.

Risks:

- may overlap with existing row language;
- may require careful wording to avoid making all evidence requirements too heavy.

### Option C — Guidance-only refinement

Do not change active CSV, but create guidance explaining evidence sufficiency and limitation review.

Benefits:

- provides reviewer-facing clarity;
- avoids active CSV changes;
- can be expanded into quick-start material later.

Risks:

- active testing procedure remains less explicit;
- guidance may be overlooked by implementers.

## Recommended Direction

Recommended current direction:

- Create this review proposal first.
- Review the current `AAEF-EVD-01` active testing row.
- If the active row already covers sufficiency, action-binding, independence, and limitations well enough, record a no-change decision.
- If not, create a narrow CSV refinement proposal before changing the active CSV.

Do not change active CSV in this proposal.

## Candidate Review Criteria

When reviewing `AAEF-EVD-01`, use the following criteria:

| Criterion | Review question |
| --- | --- |
| Sufficiency | Does the row require evidence sufficient for the assessed action and risk level? |
| Action-binding | Does the row require evidence to be tied to the specific action under assessment? |
| Independence / corroboration | Does the row avoid accepting only model or agent self-report as sufficient evidence? |
| Limitation handling | Does the row require missing, partial, unverifiable, or weak evidence to reduce assurance? |
| Completeness | Does the row consider whether the action story is complete enough for assessment? |
| Risk proportionality | Does the row allow stronger evidence expectations for higher-impact actions? |
| Boundary clarity | Does the row distinguish evidence sufficiency from schema validity and evidence integrity? |

## Potential Minimal Refinement Direction

If refinement is needed later, keep it narrow.

Potential testing direction:

> Verify that evidence supporting the assessment result is sufficient for the assessed action and risk level, is action-bound, and identifies material limitations such as missing, partial, unverifiable, model-generated, self-reported, or non-corroborated evidence.

Potential pass direction:

> Pass when evidence is action-bound, appropriate for the action risk, independently generated or corroborated where needed, and any material evidence limitations are disclosed and reflected in the assessment result.

Potential fail direction:

> Fail when assessment conclusions rely on missing, generic, unverifiable, model-generated, self-reported, or non-corroborated evidence without recording limitations or reducing assurance.

This wording is a proposal only.

## Relationship to `AAEF-EVD-04`

`AAEF-EVD-04` focuses on evidence integrity and tamper-evidence.

`AAEF-EVD-01` should remain focused on evidence sufficiency.

A record can pass schema validation and integrity checks but still fail sufficiency review if it does not support the claimed assessment result.

## Relationship to Negative Examples and Validator Fixtures

The negative examples / validator fixtures decision proposal concluded that semantic evidence failures should not be treated as JSON Schema failures.

This review continues that boundary:

- validator confirms structure;
- `AAEF-EVD-04` addresses integrity;
- `AAEF-EVD-01` addresses sufficiency and limitation handling;
- assessment determines whether the evidence can support the conclusion.

## Relationship to Evidence Depth / E5

Evidence depth terminology may help reviewers discuss sufficiency.

However, `AAEF-EVD-01` should not require E5 or any evidence-depth certification level.

If evidence depth is referenced later, it should remain explanatory and risk-proportionate.

## Relationship to #165

This proposal advances #165 by opening the final evidence sufficiency / limitation review path.

It does not close #165.

Remaining #165 work may include:

- reviewing the active `AAEF-EVD-01` row;
- deciding whether a CSV refinement proposal is needed;
- possible future evidence sufficiency guidance;
- temporary-document consolidation after the current follow-up cycle.

## Non-Goals

This proposal does not:

- update active testing procedure CSV;
- add testing procedure rows;
- add candidate IDs to active CSV;
- update the Evidence Event Schema;
- add evidence examples;
- add validator fixtures;
- update `tools/validate_evidence_schema.py`;
- create an evidence depth certification scale;
- change control catalog CSV;
- change human-readable control requirements;
- change assessment worksheet;
- change assessment profiles;
- change external framework mapping CSV;
- create GitHub issues;
- close #161, #163, #165, or #167.

It records the `AAEF-EVD-01` evidence sufficiency and limitation review proposal before any active incorporation decision.
