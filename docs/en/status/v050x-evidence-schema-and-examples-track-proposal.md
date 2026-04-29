# v0.5.x Evidence Schema and Examples Track Proposal

**Status:** Temporary, non-normative track proposal

## Purpose

This document starts Track T1 from the v0.5.x next phase plan.

Track T1 covers evidence schema and example decisions that may be needed after the first incorporation review cycle.

It follows:

- `docs/en/status/v050x-next-phase-track-plan.md`
- `docs/en/status/v050x-incorporation-review-checkpoint.md`
- `docs/en/status/v050x-incorporation-decision-register.md`
- `docs/en/status/v050x-follow-up-status.md`

Primary source issues:

- #165 — evidence integrity and tamper-evident evidence
- #167 — approval quality evidence
- #161 — principal context evidence
- #163 — delegation and authority lineage evidence

This document does not change the active baseline.

It does not update the Evidence Event Schema.

It does not update evidence examples.

It does not update active testing procedures.

It does not close any follow-up issue by itself.

## Track Objective

The objective of this track is to decide whether the current Evidence Event Schema and examples need additional fields or examples to support:

- evidence integrity and tamper-evident evidence;
- trusted approval evidence source handling;
- model-generated approval summary limitations;
- approval-to-execution binding evidence;
- principal context freshness and degradation evidence;
- delegation and authority lineage evidence;
- evidence trust limitations;
- higher-depth evidence examples.

## Current Baseline Constraint

The active evidence schema and examples are currently validated by:

- `tools/validate_evidence_schema.py`

Existing valid examples include:

- `examples/agentic-action-evidence-event.minimal.json`
- `examples/agentic-action-evidence-event.valid.json`
- `examples/agentic-action-evidence-event.high-impact.json`
- `examples/agentic-action-evidence-event.audit-grade.json`

This proposal does not modify those files.

Any later schema or example PR should preserve validator compatibility or update the validator intentionally.

## Candidate Decision Areas

| Area | Source issues | Candidate output | Initial direction |
| --- | --- | --- | --- |
| Evidence integrity fields | #165 | Schema field proposal | Evaluate before schema change |
| Tamper-evident evidence examples | #165 | E5 or higher-depth example proposal | Likely needed |
| Trusted approval evidence source | #167 | Schema/example guidance | Likely needed |
| Model-generated approval summary limitations | #167 | Evidence guidance or example | Likely needed |
| Principal context freshness | #161 | Schema/example guidance | Evaluate |
| Delegation authority lineage | #163 | Schema/example guidance | Evaluate |
| Evidence trust limitations | #165, #167, #163 | Schema/example guidance | Likely needed |

## Candidate Evidence Integrity Fields

The following candidate fields may be considered for a later schema proposal.

They are not active schema requirements in this document.

| Candidate field group | Possible fields | Purpose |
| --- | --- | --- |
| Evidence integrity mechanism | `integrity.mechanism`, `integrity.storage_class`, `integrity.append_only`, `integrity.write_restricted` | Identify how evidence is protected. |
| Cryptographic linkage | `integrity.hash`, `integrity.hash_algorithm`, `integrity.hash_chain_id`, `integrity.merkle_root`, `integrity.signature_ref` | Support tamper-evident verification. |
| External anchoring | `integrity.external_timestamp_ref`, `integrity.external_anchor_ref` | Support independent time or integrity anchoring. |
| Verification result | `integrity.verification_result`, `integrity.verified_at`, `integrity.verified_by`, `integrity.verification_error` | Record whether integrity was checked and what happened. |
| Retention and redaction | `integrity.retention_class`, `integrity.redaction_event_ref`, `integrity.deletion_event_ref` | Make deletion, retention, and redaction reviewable. |
| Evidence trust limitation | `evidence_trust_limitation`, `evidence_trust_level`, `self_reported_evidence` | Make evidence limitations explicit. |

## Candidate Approval Evidence Fields

The following candidate fields may be considered for approval evidence and approval-to-execution binding.

They are not active schema requirements in this document.

| Candidate field group | Possible fields | Purpose |
| --- | --- | --- |
| Approval source | `approval.source_type`, `approval.source_system`, `approval.workflow_record_id`, `approval.trusted_source` | Distinguish trusted workflow evidence from model-generated summaries. |
| Approval context | `approval.context_presented_ref`, `approval.context_hash`, `approval.approver_view_ref` | Show what the approver actually saw. |
| Approval binding | `approval.canonical_action_id`, `approval.action_digest`, `approval.approved_scope`, `approval.approved_operation_class` | Bind approval to the approved action. |
| Approval enforcement | `approval.enforcement_check_id`, `approval.enforcement_result`, `approval.checked_at_execution_boundary` | Show that approval was verified before execution. |
| Model-generated summary limitation | `approval.model_summary_present`, `approval.model_summary_trusted_as_evidence` | Prevent model-only approval claims from becoming evidence. |

## Candidate Principal Context Fields

The following candidate fields may be considered for principal context freshness and degradation.

They are not active schema requirements in this document.

| Candidate field group | Possible fields | Purpose |
| --- | --- | --- |
| Principal freshness | `principal_context.issued_at`, `principal_context.expires_at`, `principal_context.refreshed_at` | Show whether principal context was current. |
| Principal continuity | `principal_context.parent_context_id`, `principal_context.workflow_context_id`, `principal_context.semantic_binding_ref` | Support continuity across workflows. |
| Degradation handling | `principal_context.degradation_detected`, `principal_context.degradation_reason`, `principal_context.reauthorization_ref` | Show how stale, broadened, or ambiguous context was handled. |

## Candidate Delegation Lineage Fields

The following candidate fields may be considered for delegation and authority lineage.

They are not active schema requirements in this document.

| Candidate field group | Possible fields | Purpose |
| --- | --- | --- |
| Delegation chain | `delegation.chain_id`, `delegation.parent_grant_id`, `delegation.lineage_node_id` | Reconstruct authority movement. |
| Delegated scope | `delegation.delegated_scope`, `delegation.effective_scope`, `delegation.requested_scope` | Compare requested and effective delegation. |
| Receiving-side validation | `delegation.receiving_validation_source`, `delegation.receiving_validation_result` | Show that communication alone was not treated as authority. |
| Delegation state | `delegation.acceptance_state`, `delegation.refusal_reason`, `delegation.timeout_state` | Support acceptance, refusal, pending, or timeout evidence. |

## Candidate Example Set

A later examples PR may add or refine examples such as:

| Candidate example | Purpose | Source issues |
| --- | --- | --- |
| `agentic-action-evidence-event.integrity-e5.json` | Demonstrate tamper-evident evidence with integrity verification. | #165 |
| `agentic-action-evidence-event.approval-binding.json` | Demonstrate approval-to-execution binding and trusted approval source. | #167 |
| `agentic-action-evidence-event.principal-context-refresh.json` | Demonstrate principal context refresh or reauthorization. | #161 |
| `agentic-action-evidence-event.delegation-lineage.json` | Demonstrate cross-agent delegation lineage and receiving-side validation. | #163 |
| `agentic-action-evidence-event.model-summary-not-evidence.json` | Demonstrate model-generated summary as non-authoritative evidence. | #167 |

Example names are planning candidates only.

This document does not create those files.

## Recommended Initial Scope

The first implementation-oriented follow-up should be narrow.

Recommended initial scope:

1. create a schema field proposal for evidence integrity and trusted approval evidence;
2. define one E5 or higher-depth tamper-evident evidence example;
3. define one approval-to-execution binding example;
4. avoid changing active testing procedures in the same PR;
5. preserve existing valid examples unless intentionally updated.

## Open Questions

Before modifying schema or examples, reviewers should answer:

- Should integrity fields be part of the core evidence event schema or optional profile-specific fields?
- Should tamper-evident evidence be represented by explicit fields, references, or both?
- Should `evidence_trust_limitation` become a structured object?
- Should model-generated approval summaries be represented explicitly as untrusted evidence inputs?
- Should trusted approval evidence source be a required field only when approval is required?
- Should principal context freshness be modeled directly or left to authorization and workflow records?
- Should delegation lineage fields be schema-level fields or referenced external records?
- Should E5 evidence depth be introduced as an example pattern before becoming a schema/profile concept?

## Proposed Next PRs

Potential next PRs after this proposal:

1. Evidence schema field proposal for integrity and trusted approval evidence.
2. E5 tamper-evident evidence example proposal.
3. Approval-to-execution binding example proposal.
4. Principal context and delegation lineage evidence example proposal.
5. Evidence trust limitation guidance proposal.

These are planning candidates only.

They do not create GitHub issues by themselves.

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

It records the starting proposal for the v0.5.x evidence schema and examples track.

## Schema Field Proposal

The candidate schema field decision layer is recorded in `docs/en/status/v050x-evidence-schema-field-proposal.md`.

The proposal separates candidate fields into:

- first candidate set;
- deferred candidates;
- not recommended yet.

It recommends starting with optional evidence integrity, integrity verification, proof reference, evidence trust limitation, approval evidence source, approval-to-action binding, and execution-bound approval enforcement references.
