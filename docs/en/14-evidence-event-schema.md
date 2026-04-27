# 14. Evidence Event Schema

## Status

This document defines the initial draft of the **AAEF Agentic Action Evidence Event Schema** for public review.

Schema file:

- `schemas/agentic-action-evidence-event.schema.json`

Examples:

- `examples/agentic-action-evidence-event.minimal.json`
- `examples/agentic-action-evidence-event.valid.json`
- `examples/agentic-action-evidence-event.invalid.json`

This schema is intended for AAEF v0.2.0 discussion and review. It is not a certification format and does not guarantee compliance by itself.

## Purpose

AAEF focuses on action assurance for agentic AI systems.

The evidence event schema provides a structured way to record high-impact agentic actions so that an organization can later answer:

1. Who or what acted?
2. On whose behalf did it act?
3. What authority did it have?
4. Was the action allowed at the point of execution?
5. What evidence proves what happened?

The schema is designed to support:

- logging design,
- audit review,
- SIEM or evidence pipeline integration,
- incident reconstruction,
- control testing,
- and future interoperability discussion.

## Design Principles

### 1. Evidence should be structured

A log line such as `send_email success` is not enough for action assurance.

For high-impact actions, evidence should include identity, principal, authority, requested action, authorization decision, result, and evidence metadata.

### 2. Model output is not authority

The schema records the requested action and the authorization decision separately.

A model may propose an action, but the evidence event should show whether that action was authorized at the action boundary.

### 3. Trusted and untrusted inputs should be distinguishable

Agentic AI systems may process external emails, web pages, tickets, documents, tool results, retrieved content, or memory.

The schema includes:

- `trusted_inputs_used`
- `untrusted_inputs_excluded`
- `context.input_sources`
- `untrusted_content_influenced_action`

These fields help show whether untrusted content influenced a high-impact action or was excluded from authorization.

### 4. Evidence should support privacy and minimization

The schema allows references and digests rather than requiring raw sensitive content.

Examples:

- `argument_digest`
- `content_digest`
- `result_digest`
- `evidence_location`
- `privacy_notes`

Implementations should avoid storing unnecessary sensitive data in evidence events.

### 5. Evidence should support incident reconstruction

The schema includes fields such as:

- `correlation_id`
- `trace_id`
- `delegation_chain_id`
- `parent_action_id`
- `tool_result_reference`
- `revocation_reference`
- `incident_reference`

These fields support reconstruction of action sequences, delegation chains, and response actions.


### 6. Evidence assertions should identify their source and limits

Some evidence fields are assertions rather than direct facts.

For example, `untrusted_content_influenced_action: false` is only meaningful if the event also shows who or what determined that assertion, what method was used, the confidence level, and known limitations.

The schema therefore supports `input_influence_assessment` to record:

- `determined_by`
- `method`
- `confidence`
- `limitations`

This is intended to avoid treating model self-reporting as sufficient evidence for high-impact actions.

### 7. Authorization decisions should be bound to actions

AAEF separates model output from authority.

For high-impact actions, an authorization decision should not be treated as a free-floating `allow` value. It should be bound to the action, principal, resource, authority scope, and issuing decision point where feasible.

The schema therefore supports `authorization_decision_artifact`.

### 8. Non-execution and override events are evidence

An action that was denied, deferred, escalated, frozen, or safely terminated may still be security-relevant.

The schema therefore supports optional sections for:

- `non_execution`
- `reauthorization`
- `override`

These sections support review of denied actions, safe termination, scoped reauthorization, human override, and break-glass operations.

## Required Top-Level Fields

The initial schema requires:

- `schema`
- `schema_version`
- `action_id`
- `timestamp`
- `agent`
- `principal`
- `delegation`
- `requested_action`
- `authorization`
- `result`
- `evidence`

Optional sections include:

- `approval`
- `context`
- `response`
- `extensions`

## Required Evidence Content

The schema is aligned with AAEF-EVD-02.

For high-impact actions, evidence should include at minimum:

- agent identity,
- agent instance,
- principal,
- requested action,
- resource,
- authority scope,
- authorization decision,
- timestamp,
- and result.

## Relationship to Existing Example

AAEF v0.1.x included:

- `examples/agentic-action-evidence-event.json`

That example demonstrated the concept.

This schema turns the evidence event into a structured draft format that can be validated and reviewed.


## Evidence Event Expansion Sections

The evidence event schema includes optional sections and objects introduced during the v0.2 public review expansion.

### Authorization Decision Artifact

`authorization.authorization_decision_artifact` can be used to record an action-bound decision artifact.

It may include:

- `decision_id`
- `decision`
- `bound_action_digest`
- `principal_id`
- `authority_scope`
- `resource`
- `expires_at`
- `issuer`
- `signature_reference`

This supports integrity between authorization and tool dispatch by making it easier to detect decision reuse, replay, or substitution.

### Intent Alignment

`authorization.intent_alignment` can be used to record how intent-authority alignment was evaluated.

It may include:

- `principal_intent_reference`
- `policy_constraints_used`
- `machine_enforceable_policy_reference`
- `human_readable_policy_summary`
- `alignment_decision`
- `alignment_reason`
- `model_self_assessment_only`

The field `model_self_assessment_only` is included to make reliance on model self-assessment visible. For high-assurance actions, implementers should avoid relying solely on model self-assessment.

### State Checks

`authorization.state_checks` can be used to record runtime state checks that affected authorization.

Examples include:

- revocation state,
- incident status,
- system health,
- approved vendor status,
- account state,
- fraud risk,
- market state,
- or other organization-defined state sources.

### Input Influence Assessment

`context.input_influence_assessment` can be used to record who or what determined whether untrusted content influenced an action.

This is more reviewable than a standalone boolean because it records method, confidence, and limitations.

### Delegation Lineage

`delegation.delegation_lineage` can be used to record lineage nodes for reconstructing upstream and downstream authority decisions.

AAEF requires reconstructability, not a specific graph database or tracing tool.

### Human Override

`override` can be used to record human override or break-glass context.

It is intended to be append-only and linked to original actions or incidents, not to overwrite prior evidence.

### Non-Execution

`non_execution` can be used to record denied, deferred, escalated, frozen, or safely terminated high-impact actions.

### Reauthorization

`reauthorization` can be used to record scoped reauthorization requests, retry counts, principal reconfirmation, and reauthorization decisions.


## Validation

The schema uses JSON Schema Draft 2020-12.

Possible validation tools include:

- `ajv`
- Python `jsonschema`
- IDE or editor JSON Schema support

Example with `ajv`:

```bash
ajv validate -s schemas/agentic-action-evidence-event.schema.json -d examples/agentic-action-evidence-event.valid.json
```

Example with Python:

```bash
python -m jsonschema schemas/agentic-action-evidence-event.schema.json -i examples/agentic-action-evidence-event.valid.json
```

Validation confirms structural conformance only.

It does not prove that:

- the action was safe,
- the authorization was correct,
- the evidence is complete,
- the implementation conforms to AAEF,
- or the organization is compliant with any law or standard.

## Evidence Event Schema Profiles

The Evidence Event Schema is intended to support multiple implementation depths.

A single JSON Schema can provide structural consistency, but different deployment contexts require different evidence expectations. For this reason, AAEF distinguishes between schema validity and evidence profile strength.

A valid evidence event is not automatically sufficient for every assurance use case.

Implementations should select an evidence profile based on action impact, regulatory context, audit needs, and operational risk.

### Profile Examples

The examples below illustrate different Evidence Event Schema usage levels.

| Profile | Example | Purpose |
|---|---|---|
| Minimal | [`agentic-action-evidence-event.minimal.json`](../../examples/agentic-action-evidence-event.minimal.json) | Shows the minimum structurally valid evidence event. |
| General valid example | [`agentic-action-evidence-event.valid.json`](../../examples/agentic-action-evidence-event.valid.json) | Shows a broader valid event with optional sections. |
| High-Impact | [`agentic-action-evidence-event.high-impact.json`](../../examples/agentic-action-evidence-event.high-impact.json) | Demonstrates high-impact action evidence with authorization artifact, approval, input influence assessment, and traceability. |
| Audit-Grade | [`agentic-action-evidence-event.audit-grade.json`](../../examples/agentic-action-evidence-event.audit-grade.json) | Demonstrates stronger integrity, provenance, retention, reviewability, and profile metadata through schema-valid extensions. |

These examples are illustrative profiles, not separate certification levels.

Schema validation confirms structural validity only. Evidence profile strength depends on the trustworthiness of the components that generated, protected, correlated, and retained the evidence.

### Minimal Evidence Profile

The Minimal Evidence Profile is intended for pilots, prototypes, internal reviews, and low-to-medium impact agentic actions.

It should preserve enough information to answer the basic AAEF questions:

- who or what acted,
- on whose behalf the action was attempted,
- what action was requested,
- what authorization decision was made,
- whether the action executed,
- and where the evidence can be reviewed.

This profile is useful for early adoption, but it should not be treated as sufficient for high-impact or regulated workflows without additional controls.

### High-Impact Evidence Profile

The High-Impact Evidence Profile is intended for agentic actions that may affect external parties, sensitive data, privileges, production systems, financial outcomes, legal commitments, persistent memory, or downstream delegation.

For high-impact actions, evidence should include stronger linkage between the proposed action, authorization decision, dispatch enforcement, and execution result.

High-impact evidence should include or reference:

- event type,
- policy ID and policy version,
- authorization decision timestamp,
- authorization decision artifact or equivalent decision reference,
- requested tool name and operation,
- target resource,
- principal and authority scope,
- action or argument digest,
- correlation ID or trace ID,
- input source and influence assessment where relevant,
- revocation or freeze state checks where relevant,
- and non-execution evidence for denied, deferred, escalated, frozen, or safely terminated actions.

For high-impact actions, model-generated explanations or model self-assessment alone should not be treated as sufficient authorization or evidence.

### Audit-Grade Evidence Profile

The Audit-Grade Evidence Profile is intended for regulated, critical, externally reviewed, or incident-reconstruction use cases.

Audit-grade evidence should strengthen integrity, provenance, retention, and reviewability.

Audit-grade evidence should include or reference:

- evidence ID,
- evidence location,
- evidence hash or digest,
- digest algorithm,
- canonicalization method where digests are used,
- tamper-evidence or equivalent integrity protection,
- retention class,
- data classification,
- redaction policy where applicable,
- source component or collection point,
- and evidence generation status.

For critical high-impact actions, an assessment should not assign a strong Pass result if evidence consists only of mutable logs, screenshots without action IDs, model-generated explanations, human-readable policy summaries without enforceable references, or unverified assertions about input influence.

### Non-Execution Evidence Profile

AAEF treats non-execution as evidence-relevant.

Denied, deferred, escalated, frozen, safely terminated, or reauthorization-required actions should produce evidence events or evidence references sufficient to reconstruct:

- what action was attempted,
- why it was not executed,
- which authorization, policy, state, evidence, or input-trust gap caused non-execution,
- whether human review or reauthorization was required,
- and whether any external effect occurred.

This is important because blocked high-impact actions may indicate attempted misuse, prompt injection, policy gaps, missing authority, stale delegation, or unsafe runtime state.

### Override and Break-Glass Evidence Profile

Override and break-glass actions require stronger evidence than ordinary approvals.

Where override or break-glass behavior is used, evidence should include or reference:

- override type,
- override actor,
- override authority,
- override reason,
- override scope,
- override timestamp,
- expiration,
- linked action ID,
- post-review requirement,
- and incident or emergency reference where applicable.

Forced continuation, temporary authority grants, or manual reversals should be reconstructable after the fact.

A human-readable override reason alone is not sufficient evidence unless it is linked to the canonical action, authority scope, actor identity, and review process.

## Evidence Assertion Sources and Input Influence Assessment

Evidence events may contain both observed facts and derived assertions.

For example:

- a Tool Dispatch Enforcement Point may observe that a dispatch request was blocked,
- an Authorization Decision Point may observe that a policy decision was `deny`,
- a runtime input tracker may observe that untrusted retrieved content was present in context,
- a policy engine may infer that untrusted input was relevant to a requested high-impact action,
- a model may claim that it was or was not influenced by a source.

These are not equivalent evidence sources.

AAEF evidence should distinguish between:

- what was directly observed,
- what was inferred by a trusted runtime, policy, provenance, or evidence component,
- what was asserted by the model,
- what was asserted by a human reviewer,
- and what could not be determined.

### Recommended Assertion Metadata

Where an evidence event includes an assertion about input influence, evidence quality, authorization context, or trust state, the event should identify the source and method of that assertion.

Recommended fields include:

```yaml
input_influence_assessment:
  determined_by: runtime_input_tracker | policy_engine | provenance_metadata | evidence_pipeline | human_review | model | mixed | unknown
  method: source_tracking | taint_tracking | retrieval_provenance | policy_evaluation | semantic_review | model_self_assessment | manual_review | best_effort
  confidence: high | medium | low | unknown
  limitations: string
```

Implementations may use different field names, but they should preserve the same assurance meaning:

- who or what made the assertion,
- how the assertion was determined,
- how much confidence should be placed in it,
- and what limitations apply.

### Model Assertions Are Advisory for High-Impact Actions

For high-impact actions, model-provided claims about input influence should be treated as advisory unless corroborated by trusted runtime, provenance, policy, human review, or evidence pipeline sources.

A model-only assertion such as:

```text
The action was not influenced by untrusted content.
```

should not be treated as sufficient evidence that untrusted content did not influence a high-impact action.

This is especially important for prompt injection and indirect prompt injection scenarios, where the model may be the compromised or influenced component.

### Conservative Source Tracking

AAEF does not require implementations to prove semantic influence with perfect certainty.

In many systems, it is not possible to prove whether a specific token, document, email, web page, memory item, or retrieved passage semantically influenced a model-generated action.

However, implementations can still preserve useful evidence by tracking:

- which sources were present in context,
- which sources were retrieved,
- which sources were untrusted,
- which sources were excluded,
- which sources contributed to tool arguments,
- which policy or runtime component made the influence determination,
- and what limitations apply.

For high-impact actions, conservative source tracking is preferable to unsupported claims of non-influence.

### Evidence Review Implication

Assessors should treat input influence assertions differently depending on their source.

In general:

- runtime, provenance, policy, TDE, backend, or evidence pipeline assertions provide stronger evidence,
- human review may provide useful supporting evidence when the reviewed payload and action context are clear,
- model self-assessment alone provides weak evidence,
- missing assertion source or method should be treated as an evidence limitation.

Evidence events should make these distinctions visible enough to support review, audit, and incident reconstruction.

## Profile Guidance and Schema Validation Limits

Schema validation confirms that an evidence event is structurally valid.

Schema validation does not prove that:

- the action was safe,
- the authorization decision was correct,
- the evidence is complete,
- the evidence was generated by a trusted component,
- the evidence has not been tampered with,
- or the implementation conforms to AAEF.

Evidence quality depends on the trustworthiness of the components that generated, protected, correlated, and retained the evidence.

AAEF evidence supports reviewability and reconstructability. It does not establish truth by itself.

## Open Questions for Review

Feedback is welcome on:

- Which fields should be required?
- Should `delegation` be required for all high-impact actions, or should authority be represented separately?
- How should privacy-preserving evidence be represented?
- Should raw tool arguments ever be stored?
- Should signatures or tamper-evidence be specified more strictly?
- How should cross-agent evidence be represented?
- How should long-running tasks and principal context degradation be represented?
- Should denied actions and executed actions use the same schema?
- Should the schema be split into action attempt, authorization decision, and execution result events?

## Future Work

Future versions may add:

- Tool Invocation Evidence Profile
- Cross-Agent Evidence Profile
- Principal Context Degradation fields
- High-Impact Action Taxonomy integration
- JSON Schema validation workflow
- example invalid events
- schema-level Evidence assertion source and input influence determination
- Authorization decision artifact profile
- Override, non-execution, and reauthorization examples
- schema versioning policy
