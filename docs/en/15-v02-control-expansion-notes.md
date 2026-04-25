# 15. v0.2 Control Expansion Notes

## Status

This document is a design note for the AAEF v0.2.0 public review milestone.

It collects candidate concepts, control areas, evidence requirements, and open questions that may become formal AAEF controls in a future version.

This document is **not** itself a normative control catalog. It is intended to guide public review before changes are made to:

- `controls/aaef-controls-v0.1.csv`
- `docs/en/07-control-requirements.md`
- `schemas/agentic-action-evidence-event.schema.json`
- assessment worksheets and mappings

## Purpose

AAEF v0.1.x established the core structure for action assurance in agentic AI systems:

- delegated authority,
- principal binding,
- action-boundary authorization,
- tool invocation control,
- evidence and auditability,
- human oversight,
- and revocable trust.

AAEF v0.2.0 expands that foundation toward real-world operational conditions where agentic systems encounter ambiguity, changing state, multi-step delegation, emergency intervention, evidence integrity concerns, performance constraints, and cross-domain interactions.

The central question remains:

> Was this agentic action authorized, bounded, attributable, and evidenced?

v0.2 adds a second operational question:

> Even if authority existed, was execution still appropriate under the intent, state, evidence, and uncertainty conditions at the point of action?

## Design Constraints

The following constraints should guide v0.2 control expansion.

### 1. Preserve implementation neutrality

AAEF should define what must be controlled and evidenced, not mandate a specific protocol, vendor, identity system, policy engine, storage system, or cryptographic technology.

### 2. Keep model output separate from authority

Natural-language model output may propose, explain, or summarize an action. It should not itself be treated as authorization.

### 3. Distinguish human-readable policy from machine-enforceable policy

Human-readable policy summaries are useful for review and audit, but runtime authorization should rely on trusted policy references, structured constraints, and enforceable decision points where feasible.

### 4. Prefer append-only evidence over evidence mutation

Exceptional interventions, overrides, revocations, corrections, and post-action findings should be recorded as additional evidence events linked to prior events. Existing evidence should not be overwritten.

### 5. Keep evidence proportional to action risk

Evidence should be strong enough to support review, accountability, and incident reconstruction, but not so heavy that low-risk agentic actions become operationally impractical.

### 6. Support review before formalization

This document should help reviewers decide which concepts should become required, recommended, or optional controls.

---

## 1. Intent-Authority Alignment

### Problem

An agentic action may appear to be technically within authority scope while violating the principal intent, organizational policy, or operational context under which that authority was granted.

Example:

> A principal asks an agent to procure office supplies at low cost.  
> The agent uses an unofficial vendor or non-compliant purchasing route.  
> The action may appear to satisfy the cost goal, but violates procurement intent and organizational policy.

This is a semantic gap between intent, authority, and policy context.

### Proposed Concept

**Intent-Authority Alignment** means that an agentic action must be consistent not only with the granted authority scope, but also with the principal intent, policy constraints, and organizational context under which that authority was granted.

### Candidate Control

**AAEF-AUZ-06: Intent-Authority Alignment**

Candidate requirement:

> Systems shall evaluate whether high-impact agentic actions are consistent with the principal intent, authority scope, and applicable policy constraints under which authority was granted.

### Possible Evidence Fields

- `principal_intent_reference`
- `principal_context_id`
- `policy_constraints_used`
- `machine_enforceable_policy_reference`
- `human_readable_policy_summary`
- `intent_alignment_decision`
- `alignment_reason`

### Design Notes

AAEF should avoid making natural-language intent the only source of authorization.

A safer structure is:

- human-readable policy summary for review,
- machine-enforceable policy reference for runtime decision,
- structured evidence showing which policy constraints were considered.

### Review Questions

- Should intent alignment be required for all high-impact actions?
- Should it be part of Action Authorization, Principal Binding, or both?
- How should organizations represent principal intent without relying entirely on natural language?
- How should intent alignment failures be evidenced?

---

## 2. State-Aware Authority and Conditional Revocation

### Problem

An action may be authorized when authority is granted, but runtime conditions may change before execution.

Examples:

- market conditions change before a trading action,
- incident status changes before a security response,
- system health changes before production deployment,
- inventory or vendor state changes before procurement,
- a principal or delegation is revoked before tool invocation.

Static authority is not sufficient when execution depends on changing runtime state.

### Proposed Concept

**State-Aware Authority** means that delegated authority may depend on runtime state, environmental conditions, risk signals, or external constraints at the point of execution.

### Candidate Controls

**AAEF-AUZ-07: State-Dependent Authorization**

Candidate requirement:

> Systems shall evaluate relevant runtime state before allowing high-impact agentic actions where environmental, operational, or risk conditions can materially affect authorization.

**AAEF-RES-04: Conditional Authority Freeze**

Candidate requirement:

> Systems shall support freezing, denying, escalating, or revoking delegated authority when defined runtime state conditions or risk signals are met.

### Possible Evidence Fields

- `state_sources`
- `state_snapshot_id`
- `state_checked_at`
- `state_result`
- `conditional_policy_reference`
- `freeze_reason`
- `revocation_state_checked`
- `authority_frozen`
- `state_check_evidence_location`

### Design Notes

AAEF should not require specific external APIs or state providers.

Organizations should define which runtime states are material for each high-impact action category.

Examples:

- financial actions may require market, account, counterparty, or fraud-risk checks,
- production changes may require system health and incident status checks,
- security response actions may require incident state, scope, and containment policy checks.

### Review Questions

- Which runtime state checks should be required vs organization-defined?
- Should state checks be required for all high-impact actions?
- Should conditional freeze be an Authorization control or Response control?
- How should state snapshots be evidenced without storing excessive data?

---

## 3. Uncertainty-Based Non-Execution

### Problem

In agentic AI systems, ambiguity can be more dangerous than explicit denial.

Examples:

- authority exists, but principal intent is unclear,
- the action is within scope, but runtime state has changed,
- the model proposes a tool call, but input trust is uncertain,
- the system cannot determine whether external content influenced the action,
- evidence requirements cannot be met,
- principal context has degraded in a long-running task.

In these cases, execution may be unsafe even if authority appears to exist.

### Proposed Principle

**Authority is necessary but not sufficient.**

An agentic action should not be executed merely because authority exists. If principal intent, runtime state, policy applicability, evidence requirements, input trust, or action consequences are materially ambiguous, the system should deny, defer, or escalate the action.

### Candidate Controls

**AAEF-AUZ-08: Defer on Material Ambiguity**

Candidate requirement:

> Systems shall deny, defer, or escalate high-impact agentic actions when material ambiguity exists in authority, principal intent, runtime state, input trust, policy applicability, or evidence requirements.

**AAEF-EVD-05: Non-Execution Evidence**

Candidate requirement:

> Systems should record structured evidence for denied, deferred, or escalated high-impact actions where non-execution was caused by material ambiguity.

### Possible Evidence Fields

- `ambiguity_detected`
- `ambiguity_type`
- `non_execution_decision`
- `escalation_target`
- `reason`
- `authority_gap`
- `intent_gap`
- `policy_gap`
- `state_gap`
- `input_trust_gap`
- `evidence_gap`

### Design Notes

This concept extends, but does not replace, AAEF-AUZ-04 Deny on Authority Ambiguity.

AAEF-AUZ-04 focuses on ambiguity in authority.

Uncertainty-Based Non-Execution is broader and may include ambiguity in:

- intent,
- state,
- evidence,
- policy applicability,
- input trust,
- downstream consequences.

### Review Questions

- Should this be a principle, a control, or both?
- What counts as material ambiguity?
- Should non-execution evidence be required for all high-impact actions?
- Should denied, deferred, and escalated actions use the same evidence schema as executed actions?

---

## 4. Human Override and Break-Glass Evidence

### Problem

Human intervention may be necessary when agentic workflows fail, deadlock, exceed authority, require emergency response, or behave unexpectedly.

This is different from normal approval.

Human override may include:

- emergency stop,
- break-glass authorization,
- temporary authority grant,
- forced workflow continuation,
- manual reversal,
- privileged human action,
- workflow interruption,
- or exception handling during an incident.

If override operations are not evidenced consistently, they can break the audit trail.

### Proposed Concept

**Human Override Evidence** means that exceptional human interventions should be recorded as structured, append-only evidence linked to the original action, workflow, agent, or incident.

### Candidate Controls

**AAEF-HUM-03: Human Override Evidence**

Candidate requirement:

> Systems shall record structured evidence when a human overrides, interrupts, reverses, extends, or bypasses normal agentic authorization flow for high-impact actions.

**AAEF-HUM-04: Break-Glass Authority Control**

Candidate requirement:

> Systems shall constrain break-glass or emergency authority grants with explicit actor identity, reason, scope, expiration, and post-review requirements.

### Possible Evidence Fields

- `override_triggered`
- `override_type`
- `override_actor_id`
- `override_reason`
- `override_authority`
- `override_timestamp`
- `override_scope`
- `expires_at`
- `post_review_required`
- `linked_action_id`
- `incident_reference`

### Design Notes

AAEF should avoid the phrase "overwrite evidence" for override behavior.

The safer model is:

> preserve existing evidence and append a linked override event.

Override events may inform post-incident review, policy improvement, or controlled feedback processes. They should not imply automatic model retraining.

### Review Questions

- Should break-glass be part of Human Oversight or Response and Revocation?
- What evidence is required for emergency override?
- Should all break-glass authority have mandatory expiration?
- How should override events link to original evidence events?

---

## 5. Delegation Lineage Reconstruction

### Problem

AAEF already includes delegation chain evidence, but complex agentic workflows may require stronger lineage reconstruction.

Example:

> A human delegates a task to Agent A.  
> Agent A delegates a subtask to Agent B.  
> Agent B invokes a tool through Workflow C.  
> Workflow C triggers a high-impact action.

If the final action fails, the organization must determine:

- where authority was granted,
- where it was attenuated,
- whether constraints were preserved,
- which node performed the action,
- where deviation occurred,
- and which downstream actions should be revoked or isolated.

### Proposed Concept

**Delegation Lineage** means the ability to reconstruct how authority moved from a principal or upstream agent to downstream agents, tools, workflows, and actions.

### Candidate Control

**AAEF-DEL-05: Delegation Lineage Reconstruction**

Candidate requirement:

> Systems shall preserve sufficient delegation lineage metadata to reconstruct upstream and downstream authority decisions for high-impact actions.

### Possible Evidence Fields

- `delegation_chain_id`
- `parent_action_id`
- `lineage_node_id`
- `upstream_agent_id`
- `downstream_agent_id`
- `delegated_scope`
- `delegated_constraints`
- `delegation_decision`
- `correlation_id`
- `trace_id`
- `downstream_action_ids`

### Design Notes

AAEF should not require a specific graph database, tracing tool, or workflow engine.

The initial requirement should focus on reconstructability.

A chain, graph, trace, or external evidence system may be acceptable if it preserves sufficient references.

### Review Questions

- What is the minimum lineage metadata required?
- Should lineage be represented as a flat chain, graph, or references?
- Should lineage fields be added directly to the Evidence Event Schema?
- How should lineage support downstream revocation?

---

## 6. Cross-Domain Verifiable Authority Assertions

### Problem

Agent-to-agent and cross-domain workflows may require one organization, system, or agent to verify authority claims from another.

Examples:

- an external agent requests task delegation,
- an agent presents a delegated authority claim,
- a tool provider receives an agentic action request,
- one organization relies on another organization's agent evidence,
- a downstream agent needs to verify principal binding and revocation state.

### Proposed Concept

**Cross-Domain Verifiable Authority Assertions** means that agentic authority, principal binding, delegation constraints, and revocation state should be represented in a way that can be verified across trust boundaries.

### Implementation Neutrality

AAEF should not require a specific technology at this stage.

Possible implementation examples include:

- signed JWTs,
- OIDC federation,
- mTLS-backed workload identity,
- SPIFFE/SPIRE,
- organization PKI,
- DID / Verifiable Credentials,
- transparency logs,
- or signed evidence bundles.

### v0.2 Position

This concept should be acknowledged in v0.2 as a design direction, but may be better suited for a future profile in v0.3 or later.

AAEF should define the assurance requirements first:

- who issued the authority,
- who operates the agent,
- who the principal is,
- what was delegated,
- what constraints apply,
- whether authority is still valid,
- what evidence can be verified,
- and how revocation is checked.

### Review Questions

- Which parts belong in the core framework vs future interoperability profiles?
- What minimum claims are required for cross-domain authority verification?
- Should AAEF define an authority assertion profile?
- How should this relate to A2A, MCP, OAuth, OIDC, workload identity, or VC ecosystems?

---

## 7. Tamper-Evident Evidence Storage

### Problem

AAEF states that logs are not automatically evidence. For high-impact actions, evidence must be structured, attributable, context-bound, reviewable, and tamper-resistant where appropriate.

The current Evidence Event Schema includes fields such as:

- `evidence_hash`
- `evidence_location`
- `tamper_evidence`
- `retention_class`

However, AAEF does not yet define detailed guidance for evidence storage models, integrity properties, or minimum tamper-evidence expectations.

### Proposed Concept

**Tamper-Evident Evidence Storage** means that evidence for high-impact agentic actions should be stored or referenced in a way that makes unauthorized modification, deletion, or substitution detectable.

### Existing Control Relationship

This concept may refine or extend the existing Evidence and Auditability domain rather than require a completely new domain.

It may clarify expectations for existing tamper-evidence controls and future evidence storage guidance.

### Possible Implementation Examples

AAEF should remain implementation-neutral. Possible mechanisms may include:

- signed log entries,
- append-only logs,
- hash chains,
- transparency logs,
- WORM storage,
- immutable SIEM storage,
- object storage with retention lock,
- external evidence stores,
- or signed evidence bundles.

### Possible Evidence Fields

- `evidence_hash`
- `evidence_location`
- `tamper_evidence`
- `signature_reference`
- `retention_class`
- `retention_policy`
- `storage_integrity_mechanism`
- `evidence_chain_reference`

### Design Notes

AAEF should define evidence properties before prescribing storage technology.

For example, it may require that high-impact evidence be tamper-evident, attributable, retained, and reviewable without requiring blockchain, distributed ledger technology, or any specific storage system.

### Review Questions

- Which high-impact action categories require tamper-evident storage?
- Should tamper-evidence be required for all high-impact actions or only selected categories?
- What minimum integrity metadata should be required?
- Should AAEF define storage patterns or only evidence properties?
- How should privacy, retention, and legal requirements be balanced?

---

## 8. Risk-Proportional Evidence and Performance Overhead

### Problem

Agentic AI systems may perform many low-risk reasoning steps, tool calls, retrieval operations, and intermediate actions.

If every action requires full evidence capture, signing, retention, review, and validation, implementations may face unnecessary latency, token usage, storage overhead, operational friction, and cost.

At the same time, high-impact actions require strong evidence.

### Proposed Concept

**Risk-Proportional Evidence** means that evidence depth, retention, tamper-evidence, and review requirements should scale with action risk and impact.

### Candidate Concept

AAEF may define evidence levels or profiles that distinguish low-risk telemetry from high-impact action evidence.

Possible evidence levels:

- Level 0: no persistent evidence beyond normal system telemetry
- Level 1: basic action log
- Level 2: structured action evidence
- Level 3: high-impact evidence event
- Level 4: tamper-evident high-impact evidence with approval and reconstruction metadata

### Possible Factors

Evidence depth may depend on:

- action risk level,
- high-impact action category,
- external effect,
- sensitive data involvement,
- financial or legal impact,
- privilege change,
- production impact,
- cross-domain delegation,
- uncertainty or ambiguity,
- human approval requirement.

### Design Notes

This concept should not weaken evidence requirements for high-impact actions.

Instead, it should prevent AAEF from becoming impractical by requiring the same evidence depth for all low-risk internal steps.

### Review Questions

- What evidence level should be required for each risk level?
- Should all high-impact actions require full evidence events?
- Should denied or deferred actions require the same evidence depth as executed actions?
- How should performance and storage overhead be balanced?
- How should organizations document exceptions?

---

## 9. Authority Denial and Reauthorization Flow

### Problem

AAEF includes controls for denying or escalating actions under ambiguity or insufficient authority, but does not yet define what happens after an action is denied, deferred, or escalated.

In real systems, an agent may be unable to execute an action because:

- authority is missing,
- authority scope is ambiguous,
- principal intent is unclear,
- runtime state has changed,
- required evidence cannot be generated,
- required approval is missing,
- delegation has expired,
- or revocation state blocks execution.

A poor implementation may cause the agent to repeatedly retry, route around controls, ask the wrong user for approval, or escalate too broadly.

### Proposed Concept

**Authority Denial and Reauthorization Flow** means that denied, deferred, or escalated actions should follow a controlled path for reauthorization, scope adjustment, escalation, or safe termination.

### Candidate Controls

**AAEF-AUZ-09: Authority Denial and Reauthorization Flow**

Candidate requirement:

> Systems shall define safe handling for high-impact actions that are denied, deferred, or escalated due to insufficient authority, material ambiguity, state change, or missing evidence.

Possible supporting evidence control:

**AAEF-EVD-06: Reauthorization Evidence**

Candidate requirement:

> Systems should record structured evidence for reauthorization requests, additional scope requests, and escalation decisions related to denied or deferred high-impact actions.

### Possible Evidence Fields

- `denial_reason`
- `missing_authority_scope`
- `ambiguity_type`
- `reauthorization_requested`
- `requested_additional_scope`
- `escalation_target`
- `principal_reconfirmation_required`
- `retry_count`
- `linked_action_id`
- `non_execution_decision`

### Design Notes

AAEF should prevent authority denial from becoming a bypass path.

Reauthorization should be scoped, attributable, evidenced, and linked to principal intent and policy constraints.

Repeated denial and retry loops should be detectable.

### Review Questions

- When should an agent be allowed to request additional authority?
- Who should approve reauthorization?
- How should reauthorization requests avoid scope creep?
- Should denied actions be evidenced using the Evidence Event Schema?
- How should repeated denial and retry loops be detected?
- How should this relate to Uncertainty-Based Non-Execution?

---

## Candidate Control Summary

| Candidate ID | Candidate Name | Likely Domain | Status |
|---|---|---|---|
| AAEF-AUZ-06 | Intent-Authority Alignment | Action Authorization | Under review |
| AAEF-AUZ-07 | State-Dependent Authorization | Action Authorization | Under review |
| AAEF-AUZ-08 | Defer on Material Ambiguity | Action Authorization | Under review |
| AAEF-AUZ-09 | Authority Denial and Reauthorization Flow | Action Authorization | Under review |
| AAEF-RES-04 | Conditional Authority Freeze | Response and Revocation | Under review |
| AAEF-HUM-03 | Human Override Evidence | Human Oversight | Under review |
| AAEF-HUM-04 | Break-Glass Authority Control | Human Oversight | Under review |
| AAEF-DEL-05 | Delegation Lineage Reconstruction | Delegation and Authority | Under review |
| AAEF-EVD-05 | Non-Execution Evidence | Evidence and Auditability | Under review |
| AAEF-EVD-06 | Reauthorization Evidence | Evidence and Auditability | Under review |
| TBD | Tamper-Evident Evidence Storage Clarification | Evidence and Auditability | Under review |
| TBD | Risk-Proportional Evidence Levels | Evidence and Auditability | Under review |

## Evidence Schema Impact

The following sections or fields may be considered for future versions of the AAEF Evidence Event Schema:

| Area | Candidate Fields |
|---|---|
| Intent alignment | `principal_intent_reference`, `policy_constraints_used`, `intent_alignment_decision`, `alignment_reason` |
| State checks | `state_sources`, `state_snapshot_id`, `state_checked_at`, `state_result`, `freeze_reason` |
| Non-execution | `ambiguity_detected`, `ambiguity_type`, `non_execution_decision`, `escalation_target`, `evidence_gap` |
| Override | `override_triggered`, `override_type`, `override_actor_id`, `override_reason`, `post_review_required` |
| Delegation lineage | `lineage_node_id`, `upstream_agent_id`, `downstream_agent_id`, `downstream_action_ids` |
| Cross-domain authority | `issuer`, `operator`, `authority_assertion_reference`, `verification_result`, `revocation_check_reference` |
| Tamper-evident storage | `signature_reference`, `retention_policy`, `storage_integrity_mechanism`, `evidence_chain_reference` |
| Risk-proportional evidence | `evidence_level`, `evidence_profile`, `retention_class`, `sampling_basis`, `evidence_exception_reason` |
| Reauthorization | `denial_reason`, `missing_authority_scope`, `reauthorization_requested`, `requested_additional_scope`, `retry_count` |

## Relationship to Existing v0.2 Issues

This document relates to the following roadmap areas:

- Principal Context Degradation
- Cross-Agent and Cross-Domain Authority
- Approval Quality and Approval Fatigue Controls
- Evidence Event Schema
- High-Impact Action Taxonomy
- Tamper-Evident Evidence Storage
- Risk-Proportional Evidence and Performance Overhead
- Authority Denial and Reauthorization Flow
- OWASP Agentic Top 10 Mapping

## Recommended Next Steps

1. Review the candidate concepts and control IDs.
2. Decide which items should become formal v0.2 controls.
3. Update `controls/aaef-controls-v0.1.csv`.
4. Update `docs/en/07-control-requirements.md`.
5. Update the Evidence Event Schema if required.
6. Update attack-control mapping and assessment materials.
7. Add review examples for ambiguous, deferred, overridden, reauthorized, and state-frozen actions.
8. Consider evidence levels or profiles for risk-proportional implementation.

## Open Review Questions

- Which concepts should be required in v0.2?
- Which concepts should remain recommended or optional?
- Which concepts should be moved to v0.3 or future profiles?
- Does the proposed control ID structure fit the existing AAEF control domains?
- Are any concepts overlapping or redundant?
- Does this expansion preserve AAEF's implementation-neutral design?
- Does this expansion create too much operational friction?
