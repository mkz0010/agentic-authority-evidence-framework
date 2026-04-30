# v0.5.x Evidence Schema and Example Implementation Readiness Review

**Status:** Temporary, non-normative implementation readiness review

## Purpose

This document records the implementation readiness decision for the v0.5.x evidence schema and examples track.

It follows:

- `docs/en/status/v050x-evidence-example-design-proposal.md`
- `docs/en/status/v050x-evidence-schema-field-proposal.md`
- `docs/en/status/v050x-evidence-schema-and-examples-track-proposal.md`
- `docs/en/status/v050x-next-phase-track-plan.md`

Primary source issues:

- #165 — evidence integrity and tamper-evident evidence
- #167 — approval quality evidence

Secondary source issues:

- #161 — principal context evidence
- #163 — delegation and authority lineage evidence

This document does not update the Evidence Event Schema.

It does not add or modify example JSON files.

It does not update active testing procedures.

It does not close any follow-up issue by itself.

## Readiness Decision

The evidence schema and example track is ready to move from planning documents into a narrow implementation phase.

However, implementation should be split into small PRs.

Recommended sequence:

1. Add optional schema support for the smallest evidence integrity and approval evidence fields.
2. Add or update validator expectations only as needed for those optional fields.
3. Add one tamper-evident evidence example.
4. Add one approval-to-execution binding example.
5. Update related documentation references and status documents.

Do not combine broad schema changes, multiple examples, testing procedure changes, and control catalog changes in one PR.

## Implementation Strategy

### Recommended strategy

Use a schema-first, example-follow-up approach.

Rationale:

- examples should validate against the active Evidence Event Schema;
- schema field shape should be clear before examples depend on it;
- validator behavior should be intentionally updated if new fields are constrained;
- examples should demonstrate the schema rather than silently relying on permissive additional fields;
- smaller PRs reduce review risk.

### Alternative strategy not selected

An example-first strategy is not recommended unless the active schema already permits the planned fields without ambiguity.

Example-first may be acceptable only if:

- the example validates without schema modification;
- the fields are explicitly documented as extension fields;
- no validator ambiguity is introduced;
- the PR clearly states that the example does not make the fields normative.

## Minimal First Schema Implementation Scope

The first schema implementation PR should be narrow.

Recommended first schema scope:

| Field group | Implementation readiness | Notes |
| --- | --- | --- |
| `evidence_integrity` object | Ready for narrow optional schema support | Should be optional and profile-neutral. |
| `evidence_integrity.protected` | Ready | Boolean or equivalent. |
| `evidence_integrity.mechanism` | Ready | Should allow generic mechanism names without requiring one implementation. |
| `evidence_integrity.verification_result` | Ready | Should allow pass, fail, not_checked, partial, unavailable, or equivalent values. |
| `evidence_integrity.proof_ref` | Ready | Should be reference-friendly and mechanism-neutral. |
| `evidence_trust_limitation` or equivalent | Ready with caution | Prefer simple optional representation first. |
| `approval.source_type` | Ready | Needed to distinguish trusted workflow evidence from model-generated claims. |
| `approval.workflow_record_id` or equivalent | Ready | Should reference an approval workflow record, not embed the full record. |
| `approval.trusted_source` or equivalent | Ready with caution | Consider enum or boolean carefully. |
| `approval.canonical_action_id` or `approval.action_digest` | Ready | Should align with existing action identifiers. |
| `approval.enforcement_check_id` or equivalent | Ready | Should show execution-bound approval enforcement linkage. |

## Fields Not Ready for First Schema Implementation

The following field groups should not be included in the first implementation PR.

| Field group | Reason |
| --- | --- |
| Principal context freshness fields | Needs example and profile discussion first. |
| Principal context semantic binding fields | Terminology still needs stabilization. |
| Delegation lineage fields | Should wait for delegation semantics track. |
| Receiving-side validation fields | Should wait for delegation semantics and example design. |
| Detailed retention/redaction objects | May require privacy and retention policy design. |
| Full approval workflow object | Should remain referenced, not embedded. |
| Full delegation graph object | Should remain referenced, not embedded. |
| Mandatory E5 evidence depth field | Needs profile and example guidance first. |

## Minimal First Example Implementation Scope

After schema support is added, examples should be added separately.

Recommended first examples:

1. `examples/agentic-action-evidence-event.integrity-e5.json`
2. `examples/agentic-action-evidence-event.approval-binding.json`

Recommended example order:

1. integrity-focused example first;
2. approval-binding example second.

Rationale:

- evidence integrity is centered on `AAEF-EVD-04`, which already has strong active testing coverage;
- approval-binding may require more careful alignment with approval and authorization fields;
- adding one example at a time keeps validator and review failures easier to diagnose.

## Validator Readiness

Any implementation PR should run:

- `python tools/validate_evidence_schema.py`
- `python tools/validate_testing_procedures.py`
- existing assessment and mapping validators

The first schema implementation PR should decide whether:

- optional fields require schema definitions only;
- validator logic needs to check additional examples;
- new example files should be added to validator discovery automatically;
- invalid examples need updates;
- additional negative schema validation examples are needed.

No validator changes should be made unless required by the schema or example implementation.

## Documentation Update Readiness

The first implementation PR should update documentation only where necessary.

Potential docs to update:

- `CHANGELOG.md`
- `docs/en/status/v050x-evidence-schema-field-proposal.md`
- `docs/en/status/v050x-evidence-example-design-proposal.md`
- `docs/en/status/v050x-follow-up-status.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Do not update broad guidance documents until the implementation shape is stable.

## Implementation Guardrails

The first schema/example implementation wave should follow these guardrails:

- keep all new schema fields optional;
- do not require human approval for all actions;
- do not require cryptographic proof for all evidence events;
- do not encode one tamper-evidence mechanism as the only valid mechanism;
- do not embed complete approval workflow records;
- do not embed complete delegation graphs;
- do not change active testing procedure CSV in the same PR;
- do not add new control IDs in the same PR;
- do not close #161, #163, #165, or #167 in the same PR.

## Recommended Next PRs

Recommended next PR sequence:

### PR A — Add optional evidence integrity and approval evidence schema fields

Expected files:

- Evidence Event Schema file
- validator if needed
- changelog
- status documents if needed

Expected scope:

- optional `evidence_integrity` support;
- optional evidence trust limitation support;
- optional approval evidence source and approval binding references;
- no example files unless required by validator.

### PR B — Add tamper-evident evidence example

Expected files:

- `examples/agentic-action-evidence-event.integrity-e5.json`
- validator updates if needed
- changelog
- status documents if needed

Expected scope:

- one positive example;
- no broad schema redesign.

### PR C — Add approval-to-execution binding example

Expected files:

- `examples/agentic-action-evidence-event.approval-binding.json`
- validator updates if needed
- changelog
- status documents if needed

Expected scope:

- one positive example;
- trusted approval source and approval binding demonstration;
- no broad approval model redesign.

### PR D — Update status after schema/example implementation

Expected files:

- `docs/en/status/v050x-follow-up-status.md`
- `docs/en/status/v050x-incorporation-decision-register.md`
- changelog

Expected scope:

- record what was implemented;
- record remaining open work;
- keep #161, #163, #165, and #167 open unless separately decided.

## Open Questions Before PR A

Before implementing PR A, answer:

- What is the actual Evidence Event Schema file path to modify?
- Does the current schema permit optional nested objects without breaking existing examples?
- Should `evidence_trust_limitation` be a top-level field or nested under an evidence trust object?
- Should approval-related fields live under `approval`, `authorization`, or a separate evidence reference object?
- Should `approval.trusted_source` be boolean, enum, or source-type derived?
- Should `evidence_integrity.mechanism` be free-text, enum, or enum-plus-extension?
- Should `evidence_integrity.proof_ref` be a string, URI, or object?
- Should `verification_result` values be constrained in schema immediately?

## Relationship to Follow-Up Issues

### #165

This readiness review supports #165 by preparing schema and example implementation for tamper-evident evidence and integrity verification.

It does not close #165.

### #167

This readiness review supports #167 by preparing schema and example implementation for trusted approval evidence and approval-to-execution binding.

It does not close #167.

### #161 and #163

This readiness review keeps principal context and delegation lineage schema fields out of the first implementation wave.

It does not close #161 or #163.

## Non-Goals

This readiness review does not:

- update the Evidence Event Schema;
- add evidence examples;
- update active testing procedure CSV;
- add testing procedure rows;
- add candidate IDs to active CSV;
- change control catalog CSV;
- change human-readable control requirements;
- change assessment worksheet;
- change assessment profiles;
- change external framework mapping CSV;
- create GitHub issues;
- close #161, #163, #165, or #167.

It records readiness decisions before the first actual schema or example implementation PR.

## Schema Implementation Progress

The first implementation PR for this track adds optional Evidence Event Schema support for:

- evidence integrity metadata;
- evidence trust limitations;
- approval evidence source references;
- approval-to-action binding references;
- execution-bound approval enforcement references.

This implementation keeps the new schema fields optional and does not add evidence examples in the same change.

## Integrity Example Implementation Progress

The first example PR adds the tamper-evident / integrity-verifiable evidence example:

- `examples/agentic-action-evidence-event.integrity-e5.json`

This follows the planned schema-first, example-follow-up approach.

The approval-to-execution binding example remains pending.

## Approval Binding Example Implementation Progress

The second example PR adds the approval-to-execution binding evidence example:

- `examples/agentic-action-evidence-event.approval-binding.json`

This follows the planned schema-first, example-follow-up approach.

The example demonstrates trusted approval source, approval binding, approval scope, and execution-bound approval enforcement using optional schema fields.
