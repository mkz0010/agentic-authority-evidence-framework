# v0.5.x Evidence Example Design Proposal

**Status:** Temporary, non-normative example design proposal

## Purpose

This document proposes example designs for the v0.5.x evidence schema and examples track.

It follows:

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

## Design Summary

This proposal focuses on two initial example designs:

| Candidate example | Primary purpose | Source issue |
| --- | --- | --- |
| `agentic-action-evidence-event.integrity-e5.json` | Demonstrate tamper-evident or integrity-verifiable evidence. | #165 |
| `agentic-action-evidence-event.approval-binding.json` | Demonstrate trusted approval evidence and approval-to-execution binding. | #167 |

These are design candidates only.

The actual example filenames, field names, and schema changes should be confirmed in later PRs.

## Current Baseline Constraint

The current valid examples are:

- `examples/agentic-action-evidence-event.minimal.json`
- `examples/agentic-action-evidence-event.valid.json`
- `examples/agentic-action-evidence-event.high-impact.json`
- `examples/agentic-action-evidence-event.audit-grade.json`

The current validator is:

- `tools/validate_evidence_schema.py`

Any future example PR should ensure that examples validate against the active Evidence Event Schema, or intentionally update the schema and validator in the same controlled change.

## Example Design 1 — Integrity E5 Evidence

### Candidate filename

`examples/agentic-action-evidence-event.integrity-e5.json`

### Purpose

Demonstrate evidence that is suitable for high-assurance review where tamper-evidence, integrity verification, proof references, or independent anchoring are relevant.

### Intended coverage

This example should demonstrate:

- audit-grade or higher-depth evidence;
- integrity protection;
- integrity verification result;
- proof or anchor reference;
- evidence trust limitation;
- reconstruction support;
- relationship to `AAEF-EVD-04`.

### Candidate scenario

An agent performs a high-impact action that requires audit-grade evidence.

The resulting evidence is stored in a protected evidence store and linked to an integrity proof.

A reviewer can see:

- the action that was requested;
- the authorization and execution linkage;
- the evidence package reference;
- the integrity mechanism;
- the verification result;
- any limitations of the evidence.

### Candidate field concepts

Potential fields or example concepts:

- `evidence_integrity.protected`
- `evidence_integrity.mechanism`
- `evidence_integrity.storage_class`
- `evidence_integrity.coverage`
- `evidence_integrity.verification_result`
- `evidence_integrity.verified_at`
- `evidence_integrity.proof_ref`
- `evidence_integrity.external_anchor_ref`
- `evidence_trust_limitation`

These field names are planning candidates only.

### Candidate evidence story

The example should show a clear evidence story:

1. A high-impact action is requested.
2. Authorization is evaluated.
3. The action is dispatched or executed.
4. Evidence is generated.
5. Evidence is stored or anchored using an integrity mechanism.
6. Verification is performed or referenced.
7. The evidence event records trust limitations where applicable.

### Candidate positive expectations

The example should make it possible for a reviewer to understand:

- what action occurred;
- which evidence supports the action;
- whether the evidence is protected;
- how integrity can be checked;
- what integrity verification found;
- what limitations remain.

### Candidate non-goals

The example should not:

- mandate a single cryptographic mechanism;
- require Merkle roots for all implementations;
- imply that all evidence must be E5-depth;
- embed a complete evidence store or log chain;
- replace `AAEF-EVD-04` testing procedure language.

## Example Design 2 — Approval Binding Evidence

### Candidate filename

`examples/agentic-action-evidence-event.approval-binding.json`

### Purpose

Demonstrate trusted approval evidence and approval-to-execution binding.

### Intended coverage

This example should demonstrate:

- trusted approval evidence source;
- what approval was granted for;
- approval context or approver view reference;
- approved canonical action or action digest;
- final dispatched or executed action linkage;
- approval enforcement check before execution;
- limitation of model-generated approval summaries.

### Candidate scenario

An agent requests approval for a high-impact action.

A human approver reviews an action-specific approval request.

The execution boundary later verifies that:

- approval exists;
- approval came from a trusted workflow source;
- approval matches the canonical action;
- approval scope covers the requested execution;
- execution is blocked or allowed based on that check.

### Candidate field concepts

Potential fields or example concepts:

- `approval.source_type`
- `approval.source_system`
- `approval.workflow_record_id`
- `approval.trusted_source`
- `approval.context_presented_ref`
- `approval.approver_view_ref`
- `approval.approval_id`
- `approval.canonical_action_id`
- `approval.action_digest`
- `approval.approved_scope`
- `approval.approved_operation_class`
- `approval.enforcement_check_id`
- `approval.enforcement_result`
- `approval.checked_at_execution_boundary`
- `evidence_trust_limitation`

These field names are planning candidates only.

### Candidate evidence story

The example should show a clear approval story:

1. A high-impact action is proposed.
2. The approval workflow presents action-bound context.
3. A trusted approval record is created.
4. The agent or tool dispatcher requests execution.
5. The execution boundary checks the approval state and approved action.
6. The final dispatched action matches the approved canonical action.
7. The evidence event links approval, authorization, dispatch, execution, and evidence.

### Candidate positive expectations

The example should make it possible for a reviewer to understand:

- who or what approved the action;
- what source produced the approval evidence;
- what the approver saw;
- what canonical action was approved;
- what action was actually dispatched or executed;
- whether approval was checked at the execution boundary;
- whether model-generated summaries were excluded from trusted approval evidence.

### Candidate non-goals

The example should not:

- imply that human approval is required for every action;
- embed a complete approval workflow database;
- treat model-generated approval summaries as trusted evidence;
- make approval UI state equivalent to execution authority;
- replace `AAEF-HUM-01`, `AAEF-AUZ-03`, or `AAEF-EVD-03` testing procedure language.

## Design Relationship Between the Two Examples

The two examples should be complementary.

The integrity example answers:

- Can the evidence itself be trusted, verified, or reviewed for tampering?

The approval binding example answers:

- Was approval meaningful, trusted, action-bound, and enforced before execution?

Together, they support the AAEF principle that model output is not authority and that evidence must support action-level assurance.

## Recommended Implementation Sequence

Recommended later implementation sequence:

1. Confirm example design and field shape.
2. Decide whether schema changes are needed before examples can validate.
3. Add optional schema fields only if necessary.
4. Add one integrity-focused example.
5. Add one approval-binding-focused example.
6. Update validator expectations if required.
7. Update related documentation references.

## Fields to Avoid in the First Example PR

The first example implementation should avoid:

- full delegation lineage fields;
- full principal context freshness fields;
- full embedded approval workflow records;
- full embedded evidence store records;
- mandatory cryptographic hash fields for all events;
- mandatory E5 evidence depth semantics.

Those may be handled in later examples or schema proposals.

## Open Questions

Before implementing actual examples, reviewers should answer:

- Should example implementation come before schema modification, or should schema support be added first?
- Should `integrity-e5` require an explicit evidence depth value, or only demonstrate higher-depth evidence informally?
- Should `approval-binding` use `approval` fields, `authorization` fields, or evidence references?
- Should proof references be opaque strings, URIs, or structured objects?
- Should model-generated approval summaries be shown as excluded input, evidence limitation, or separate untrusted context?
- Should examples include negative cases, or should negative cases be handled in the T2 negative testing track?
- Should the example filenames use `v0.5x` naming, or stable descriptive names?

## Relationship to Follow-Up Issues

### #165

This design supports #165 by defining a candidate tamper-evident evidence example.

It does not close #165.

### #167

This design supports #167 by defining a candidate approval-to-execution binding example.

It does not close #167.

### #161 and #163

This design acknowledges that principal context and delegation lineage examples may be needed later.

They are not included in the first two example designs.

## Non-Goals

This proposal does not:

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

It records example designs before any schema or example implementation PR.

## Implementation Readiness Review

The implementation readiness review is recorded in `docs/en/status/v050x-evidence-schema-example-implementation-readiness.md`.

The readiness review recommends a schema-first, example-follow-up approach:

1. add optional schema support for the smallest evidence integrity and approval evidence fields;
2. add one tamper-evident evidence example;
3. add one approval-to-execution binding example;
4. update status documents after implementation.

## Integrity E5 Example Implementation

The first example implementation adds `examples/agentic-action-evidence-event.integrity-e5.json`.

The example demonstrates optional evidence integrity metadata, integrity verification result, proof reference, external anchor reference, and evidence trust limitations.

It does not add approval-binding evidence and does not change the Evidence Event Schema.

## Approval Binding Example Implementation

The second example implementation adds `examples/agentic-action-evidence-event.approval-binding.json`.

The example demonstrates trusted approval evidence source, approval-to-action binding, approved scope, approved operation class, execution-bound approval enforcement, and explicit treatment of model-generated summaries as non-trusted approval evidence.

It does not change the Evidence Event Schema.
