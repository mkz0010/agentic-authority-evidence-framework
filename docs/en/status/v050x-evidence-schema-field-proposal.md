# v0.5.x Evidence Schema Field Proposal

**Status:** Temporary, non-normative schema field proposal

## Purpose

This document records a decision-layer proposal for potential Evidence Event Schema field additions after the v0.5.x evidence schema and examples track proposal.

It follows:

- `docs/en/status/v050x-evidence-schema-and-examples-track-proposal.md`
- `docs/en/status/v050x-next-phase-track-plan.md`
- `docs/en/status/v050x-incorporation-review-checkpoint.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Primary source issues:

- #165 — evidence integrity and tamper-evident evidence
- #167 — approval quality evidence
- #161 — principal context evidence
- #163 — delegation and authority lineage evidence

This document does not update the Evidence Event Schema.

It does not update evidence examples.

It does not update active testing procedures.

It does not close any follow-up issue by itself.

## Decision Summary

This proposal separates candidate fields into three groups:

| Decision group | Meaning |
| --- | --- |
| First candidate set | Strong candidates for a later schema proposal or example-driven schema extension. |
| Deferred candidates | Potentially useful, but should wait for examples, profile decisions, or terminology stabilization. |
| Not recommended yet | Too broad, redundant, unstable, or likely better represented as external references rather than schema fields. |

The recommended first candidate set is intentionally narrow.

The goal is to support evidence integrity and approval evidence without turning the Evidence Event Schema into a full workflow database.

## Proposed First Candidate Set

The first candidate set should focus on optional, reference-friendly fields that improve auditability without requiring every implementation to expose low-level storage internals.

| Candidate field group | Proposed status | Rationale |
| --- | --- | --- |
| Evidence integrity summary | First candidate | Needed to represent whether audit-grade evidence is integrity-protected. |
| Integrity verification result | First candidate | Needed to show whether integrity was checked and whether verification passed. |
| Evidence proof reference | First candidate | Allows hash chains, signatures, Merkle roots, or external anchors without mandating one mechanism. |
| Evidence trust limitation | First candidate | Already appears as an important concept across evidence integrity and delegation work. |
| Approval evidence source | First candidate | Needed to distinguish trusted approval workflow evidence from model-generated approval claims. |
| Approval-to-action binding reference | First candidate | Needed to support approval quality and approval-to-execution binding. |
| Execution-bound approval enforcement reference | First candidate | Needed to show that approval state was checked before execution. |

## First Candidate Field Details

### Evidence integrity summary

Potential field shape:

- `evidence_integrity.protected`
- `evidence_integrity.mechanism`
- `evidence_integrity.storage_class`
- `evidence_integrity.coverage`

Purpose:

- identify whether the evidence record, or a referenced evidence package, is protected by an integrity mechanism;
- avoid requiring all systems to expose cryptographic internals directly;
- support `AAEF-EVD-04` without making all evidence records audit-grade.

Initial notes:

- `protected` should be boolean or equivalent.
- `mechanism` should allow values such as append-only, write-restricted, signature, hash-chain, merkle-tree, immutable-storage, external-anchor, independent-corroboration, or equivalent.
- `coverage` may be a reference or description of what the integrity mechanism covers.

### Integrity verification result

Potential field shape:

- `evidence_integrity.verification_result`
- `evidence_integrity.verified_at`
- `evidence_integrity.verification_error`
- `evidence_integrity.verification_ref`

Purpose:

- record whether an integrity check was performed;
- distinguish unverified evidence from verified evidence;
- support incident reconstruction and reviewer confidence.

Initial notes:

- `verification_result` should be optional.
- Candidate values may include pass, fail, not_checked, partial, unavailable, or not_applicable.
- The schema should avoid implying that every evidence event must be cryptographically verified at event creation time.

### Evidence proof reference

Potential field shape:

- `evidence_integrity.proof_ref`
- `evidence_integrity.external_anchor_ref`
- `evidence_integrity.chain_ref`

Purpose:

- support hash chain, Merkle root, signature, immutable storage proof, external timestamp, or independent anchor references;
- avoid overfitting the schema to a single tamper-evidence mechanism.

Initial notes:

- A generic `proof_ref` may be more stable than many mechanism-specific fields.
- Mechanism-specific examples can be added later if needed.

### Evidence trust limitation

Potential field shape:

- `evidence_trust_limitation`
- or `evidence_trust.limitations[]`
- or `evidence_trust.source_limitations[]`

Purpose:

- make evidence limitations explicit;
- distinguish trusted enforcement evidence from model self-report, agent runtime self-report, partial logs, or unverifiable evidence;
- support review of delegated, cross-agent, and evidence-integrity-sensitive workflows.

Initial notes:

- This may be a string, enum list, or structured object.
- A structured object may be better long-term, but an example-driven approach should decide the final shape.

### Approval evidence source

Potential field shape:

- `approval.source_type`
- `approval.source_system`
- `approval.workflow_record_id`
- `approval.trusted_source`

Purpose:

- distinguish trusted approval workflow evidence from model-generated summaries or claims;
- support `AAEF-HUM-01`, `AAEF-AUZ-03`, and `AAEF-EVD-03`.

Initial notes:

- This should only be required when approval evidence is relevant.
- It should not make human approval mandatory for all actions.

### Approval-to-action binding reference

Potential field shape:

- `approval.approval_id`
- `approval.canonical_action_id`
- `approval.action_digest`
- `approval.approved_scope`
- `approval.approved_operation_class`

Purpose:

- show what action, scope, or operation class was approved;
- support detection of canonical action mismatch and post-approval material changes.

Initial notes:

- Exact field names should align with existing authorization and action identifiers.
- This may be better represented through references rather than embedding complete approval records.

### Execution-bound approval enforcement reference

Potential field shape:

- `approval.enforcement_check_id`
- `approval.enforcement_result`
- `approval.checked_at_execution_boundary`

Purpose:

- show that approval state was independently verified before execution;
- prevent approval UI state or agent self-report from becoming execution authority.

Initial notes:

- This should reference an enforcement check where available.
- It should not assume a specific architecture.

## Deferred Candidate Fields

The following candidates should be deferred until examples or terminology stabilize.

| Candidate field group | Reason for deferral |
| --- | --- |
| Principal context freshness fields | Useful, but may overlap with authorization tokens, workflow records, or existing principal context evidence. |
| Principal context semantic binding reference | Important conceptually, but terminology may need more stabilization before schema encoding. |
| Delegation acceptance/refusal state | Useful for delegation semantics, but should wait for the delegation semantics track. |
| Receiving-side validation source/result | Strong candidate, but should wait for delegation examples or semantics proposal. |
| Detailed retention and redaction fields | Useful, but may require policy-specific handling and privacy review. |
| Model-generated approval summary flags | Useful, but may be better expressed through approval source trust and evidence trust limitation first. |

## Not Recommended Yet

The following are not recommended for immediate schema proposal.

| Candidate | Reason |
| --- | --- |
| Mandatory cryptographic hash fields for all events | Too prescriptive and may not fit append-only, external anchor, or independent corroboration designs. |
| Mandatory Merkle root fields | Too mechanism-specific for core schema. |
| Full embedded approval workflow record | The evidence event should reference approval records rather than duplicate entire workflow systems. |
| Full embedded delegation chain graph | The evidence event should reference delegation lineage or chain records rather than contain the full graph. |
| Mandatory E5 evidence depth field | Evidence depth needs examples and profile guidance before becoming a schema field. |
| Universal `trusted_source` requirement for all evidence | Trust may be contextual and should be modeled carefully to avoid false assurance. |

## Recommended First Schema Proposal Scope

A later schema proposal PR should be narrow.

Recommended initial scope:

1. Add an optional `evidence_integrity` object.
2. Add optional integrity verification and proof reference fields.
3. Add optional evidence trust limitation representation.
4. Add optional approval evidence source and approval binding references.
5. Avoid adding principal context and delegation lineage fields in the same first schema PR.
6. Add or update examples in a separate PR unless the schema validator requires examples in the same PR.

## Recommended Example Pairing

The first schema proposal should be paired with examples in a controlled way.

Recommended sequence:

1. Schema field proposal document.
2. Example design document for:
   - tamper-evident evidence;
   - approval-to-execution binding.
3. Actual schema/example change PR only after the example design is stable.

This reduces the risk of adding fields that are difficult to explain, validate, or implement.

## Open Questions

Before modifying the schema, reviewers should answer:

- Should `evidence_integrity` be a top-level object or nested under an evidence metadata object?
- Should `evidence_trust_limitation` remain a free-text field, become an enum list, or become a structured object?
- Should approval evidence fields be represented under `approval`, `authorization`, or `evidence`?
- Should `approval.trusted_source` be boolean, enum, or derived from source type?
- Should `approval.action_digest` duplicate or reference an existing action hash field?
- Should integrity verification be recorded at event creation time, review time, or both?
- Should proof references be opaque URIs, evidence object references, or structured records?
- Should example-first validation precede schema changes?

## Relationship to Follow-Up Issues

### #165

This proposal supports #165 by identifying candidate schema fields for tamper-evident evidence, integrity verification, evidence proof references, and trust limitations.

It does not close #165.

### #167

This proposal supports #167 by identifying candidate fields for trusted approval evidence source, approval-to-action binding, and execution-bound approval enforcement.

It does not close #167.

### #161

This proposal acknowledges principal context freshness and degradation fields, but defers schema-level treatment until examples or profile needs are clearer.

It does not close #161.

### #163

This proposal acknowledges delegation lineage and receiving-side validation fields, but defers schema-level treatment until the delegation semantics track is more mature.

It does not close #163.

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

It records candidate schema field decisions before any schema or example implementation PR.
