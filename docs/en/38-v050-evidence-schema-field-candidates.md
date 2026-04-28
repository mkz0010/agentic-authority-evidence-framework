# v0.5.0 Evidence Schema Field Candidates

**Status:** v0.5.0 planning note
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative field candidate inventory before changing the Evidence Event Schema

## Purpose

This document collects candidate Evidence Event Schema fields for v0.5.0 planning.

The purpose is to avoid adding schema fields prematurely. Candidate fields should be evaluated against control semantics, assessment value, implementation burden, privacy impact, and operational cost before being added to the schema.

This document does not change the Evidence Event Schema.

## Design Principles

Schema fields should be added only when they are:

- tied to a clear control, assessment, or reconstruction need;
- useful across more than one implementation style;
- not merely restating model output or free-text rationale;
- capable of being generated or corroborated by trusted components where possible;
- compatible with evidence minimization and sensitive-data handling;
- useful for authorization, execution, non-execution, reauthorization, delegation, response, or audit review.

## Candidate Categories

The v0.5.0 planning work has produced candidate fields in five areas:

1. risk-proportional evidence depth;
2. tamper-evident evidence integrity;
3. authority assertion and cross-domain authority;
4. principal context degradation and reconfirmation;
5. denial, non-execution, retry, and reauthorization.

## 1. Risk-Proportional Evidence Candidates

Related planning profile: `docs/en/36-risk-proportional-evidence-profile.md`

| Candidate Field | Purpose | Candidate Status |
| --- | --- | --- |
| `evidence_depth_level` | Indicates whether the event is E1, E2, E3, E4, or E5 evidence. | Strong candidate |
| `risk_basis` | Records why a higher evidence depth was selected. | Strong candidate |
| `assurance_level` | Captures intended assurance strength for review. | Planning candidate |
| `retention_class` | Indicates retention expectation or policy class. | Planning candidate |
| `integrity_requirement` | Indicates required evidence integrity strength. | Strong candidate |
| `evidence_minimization_method` | Records whether references, hashes, redaction, or summaries were used. | Planning candidate |
| `sensitive_data_handling` | Records handling or minimization approach for sensitive evidence content. | Planning candidate |
| `sampling_or_aggregation_basis` | Explains sampling or aggregation for lower-risk evidence. | Deferred candidate |
| `verification_requirement` | Indicates whether independent verification is expected. | Planning candidate |

## 2. Tamper-Evident Evidence Candidates

Related planning profile: `docs/en/37-tamper-evident-evidence-storage.md`

| Candidate Field | Purpose | Candidate Status |
| --- | --- | --- |
| `evidence_integrity_level` | Indicates I1, I2, I3, I4, or I5 integrity expectation. | Strong candidate |
| `evidence_store_id` | Identifies the evidence store or pipeline. | Strong candidate |
| `append_only_reference` | References append-only or write-restricted storage. | Planning candidate |
| `hash_chain_reference` | References hash-chain integrity data. | Planning candidate |
| `merkle_root_reference` | References Merkle-root integrity data. | Deferred candidate |
| `signature_reference` | References signed or sealed evidence. | Strong candidate |
| `signing_key_id` | Identifies signing key without exposing secrets. | Planning candidate |
| `external_timestamp_reference` | References external timestamping or anchoring. | Planning candidate |
| `attestation_reference` | References remote attestation or trusted runtime evidence. | Planning candidate |
| `trusted_runtime_reference` | References runtime identity, secure boot, TEE, TPM, or workload identity. | Planning candidate |
| `integrity_verification_result` | Records whether evidence integrity verification passed. | Strong candidate |
| `integrity_verification_time` | Records when integrity verification occurred. | Planning candidate |
| `deletion_or_redaction_record` | Records authorized deletion or redaction. | Planning candidate |
| `evidence_corroboration_reference` | Links corroborating evidence from independent systems. | Strong candidate |
| `evidence_trust_limitation` | Records evidence trust limitations. | Strong candidate |

## 3. Authority Assertion and Cross-Domain Authority Candidates

Related planning profile: `docs/en/35-authority-assertion-profile.md`

| Candidate Field | Purpose | Candidate Status |
| --- | --- | --- |
| `authority_assertion_id` | Identifies a cross-agent or cross-domain authority assertion. | Strong candidate |
| `authority_assertion_reference` | Links to an external assertion without embedding it. | Strong candidate |
| `issuer` | Identifies the assertion issuer. | Planning candidate |
| `issuer_type` | Classifies the issuer. | Planning candidate |
| `subject_agent_id` | Identifies the subject agent. | Planning candidate |
| `subject_agent_instance_id` | Identifies the runtime instance. | Planning candidate |
| `operator` | Identifies responsible operator. | Planning candidate |
| `source_trust_domain` | Trust domain where assertion originated. | Strong candidate |
| `target_trust_domain` | Trust domain where assertion is evaluated. | Strong candidate |
| `trust_relationship_reference` | References trust relationship, federation, policy, or allowlist. | Planning candidate |
| `receiving_side_verification_result` | Records receiving-side verification result. | Strong candidate |
| `receiving_side_policy_reference` | Records policy used by receiving side. | Strong candidate |
| `verification_limitations` | Records limitations of receiving-side verification. | Planning candidate |
| `cross_domain_evidence_reference` | Links external evidence used in verification. | Planning candidate |
| `cross_domain_evidence_limitation` | Records limitations of external evidence. | Strong candidate |

## 4. Principal Context Degradation Candidates

Related planning concept: `docs/en/30-principal-context-degradation.md`

| Candidate Field | Purpose | Candidate Status |
| --- | --- | --- |
| `principal_context_status` | Records whether context is current, stale, degraded, ambiguous, or re-established. | Strong candidate |
| `principal_context_age` | Indicates age or freshness of principal context. | Planning candidate |
| `principal_context_reference` | Links trusted context supporting principal binding. | Strong candidate |
| `principal_reconfirmation_reference` | Links reconfirmation evidence. | Strong candidate |
| `principal_context_limitations` | Records limitations or ambiguity in principal context. | Strong candidate |
| `scope_drift_detected` | Indicates detected scope drift. | Planning candidate |
| `delegation_drift_detected` | Indicates detected delegation drift. | Planning candidate |
| `context_refresh_result` | Records whether context refresh succeeded. | Planning candidate |

## 5. Denial, Non-Execution, Retry, and Reauthorization Candidates

Related planning concept: `docs/en/32-authority-denial-reauthorization-flow.md`

| Candidate Field | Purpose | Candidate Status |
| --- | --- | --- |
| `non_execution_reason` | Records reason execution did not proceed. | Strong candidate |
| `denied_action_id` | Links to denied action. | Strong candidate |
| `deferred_action_id` | Links to deferred action. | Planning candidate |
| `reauthorization_request_id` | Links to reauthorization request. | Strong candidate |
| `requested_additional_scope` | Records additional scope requested. | Strong candidate |
| `post_reauthorization_effective_scope` | Records scope after reauthorization. | Strong candidate |
| `retry_count` | Records retry count. | Planning candidate |
| `retry_correlation_id` | Correlates retries across attempts. | Strong candidate |
| `task_splitting_correlation_id` | Correlates suspected task splitting. | Planning candidate |
| `safe_termination_record` | Links safe termination evidence. | Planning candidate |
| `escalation_target` | Records escalation target. | Planning candidate |
| `principal_reconfirmation_required` | Indicates reconfirmation requirement. | Planning candidate |
| `principal_reconfirmation_result` | Records reconfirmation result. | Planning candidate |

## Candidate Priority

The following fields appear most likely to be useful in v0.5.0 because they support multiple planning themes.

| Priority | Candidate Field | Rationale |
| --- | --- | --- |
| P0 | `evidence_depth_level` | Connects risk-proportional evidence to schema and assessment. |
| P0 | `evidence_integrity_level` | Connects tamper-evident evidence planning to schema. |
| P0 | `evidence_trust_limitation` | Supports audit realism and avoids overclaiming assurance. |
| P0 | `non_execution_reason` | Supports denial, deferral, freeze, and safe termination review. |
| P0 | `reauthorization_request_id` | Supports authority denial and reauthorization flow. |
| P0 | `principal_context_status` | Supports principal context degradation handling. |
| P1 | `principal_reconfirmation_reference` | Supports degraded context and reauthorization. |
| P1 | `authority_assertion_reference` | Supports cross-agent and cross-domain authority. |
| P1 | `receiving_side_verification_result` | Supports receiving-side authority verification. |
| P1 | `cross_domain_evidence_limitation` | Supports cross-domain evidence trust gaps. |
| P1 | `integrity_verification_result` | Supports tamper-evident evidence review. |
| P1 | `evidence_corroboration_reference` | Supports independent verification and reconstruction. |

## Candidate Minimal Schema Expansion

A conservative v0.5.0 schema expansion could add only a small set of fields:

- `evidence_depth_level`;
- `evidence_integrity_level`;
- `evidence_trust_limitation`;
- `principal_context_status`;
- `non_execution_reason`;
- `reauthorization_request_id`;
- `authority_assertion_reference`;
- `receiving_side_verification_result`.

This would preserve implementability while connecting the major v0.5.0 planning themes.

## Fields to Avoid for Now

AAEF should avoid adding fields that:

- require a specific vendor or product;
- require a specific cryptographic mechanism;
- require a specific identity federation model;
- require full raw prompt retention;
- require full payload capture by default;
- duplicate existing identifiers;
- encourage model self-assessment as evidence;
- cannot be generated by trusted workflow, authorization, dispatch, backend, or evidence components.

## Open Questions

1. Which fields should be required, optional, or profile-specific?
2. Should `evidence_depth_level` be required for all evidence events or only high-impact events?
3. Should `evidence_integrity_level` be separate from `evidence_depth_level`?
4. Should cross-domain authority fields be embedded in the Evidence Event Schema or referenced externally?
5. Should non-execution and reauthorization fields be part of the core schema or examples first?
6. How should privacy and sensitive-data minimization be represented?
7. How much schema growth is acceptable for v0.5.0?
8. Should v0.5.0 add fields, examples, or profile guidance first?

## Non-Goals

This document does not:

- change the Evidence Event Schema;
- require new fields;
- define a final schema expansion;
- define a protocol;
- require tamper-evident storage;
- require cross-domain authority assertions;
- require audit-grade evidence for every action.

## Recommended Next Step

The recommended next step is to select a small P0/P1 field set for experimental schema expansion or example-only representation.

A conservative approach is to first add examples showing how these candidate fields could appear before making them required schema fields.
## Evidence Depth Field Candidates

The following candidate fields may support future risk-proportional evidence depth handling.

These fields are planning candidates only. They do not change the current Evidence Event Schema.

### Candidate: `evidence_depth_level`

**Purpose:** Record the expected or applied evidence depth level for an action evidence event.

**Candidate values:**

- `E0`: No AAEF evidence expected
- `E1`: Minimal operational evidence
- `E2`: Standard action evidence
- `E3`: High-impact evidence
- `E4`: Audit-grade evidence
- `E5`: Tamper-evident or independently verifiable evidence

**Assessment use:**

This field may help assessors determine whether evidence depth is proportionate to action risk, impact, reversibility, delegation, cross-domain involvement, approval requirements, reauthorization requirements, incident relevance, or external review needs.

### Candidate: `evidence_depth_rationale`

**Purpose:** Explain why the selected evidence depth level was assigned.

**Example rationale values:**

- low-risk reversible action
- standard agentic action
- high-impact action
- approval-required action
- reauthorization-required action
- non-executed high-impact action
- override or exceptional human intervention
- critical action
- incident-relevant action
- externally reviewed or disputed action

### Candidate: `evidence_depth_source`

**Purpose:** Identify how the evidence depth level was determined.

**Example values:**

- policy
- risk engine
- control profile
- assessment profile
- human reviewer
- incident workflow
- implementation default

### Candidate: `evidence_depth_limitations`

**Purpose:** Record known limitations that prevent the evidence event from satisfying the intended depth.

**Example limitations:**

- mutable local evidence only
- no independent corroboration
- no integrity verification
- incomplete dispatch linkage
- incomplete backend execution linkage
- approval evidence missing or weak
- non-execution evidence incomplete
- reauthorization linkage incomplete
- sensitive data minimized by reference only
- retention limitation

## Relationship to Risk-Proportional Evidence Guidance

For non-normative assessment guidance on applying evidence depth levels, see `docs/en/43-risk-proportional-evidence-assessment-guidance.md`.

For non-normative evidence depth examples, see `docs/en/44-evidence-depth-examples.md`.
