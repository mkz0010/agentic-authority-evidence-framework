# Authority Assertion Profile

**Status:** v0.5.0 planning profile
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative planning profile for cross-agent and cross-domain authority assertions

## Purpose

This document defines a non-normative Authority Assertion Profile for AAEF v0.5.0 planning.

The purpose is to describe the information that may be needed when one agent, workflow, system, organization, or trust domain relies on another agent's authority claim, delegation claim, evidence reference, or execution request.

This document does not define a required protocol, credential format, token format, schema, control, or conformance requirement.

It is intended to support future design work for:

- cross-agent and cross-domain authority verification;
- receiving-side authorization;
- delegation lineage;
- principal context preservation;
- evidence trust limitations;
- reauthorization and denial handling;
- future evidence schema refinement.

## Core Principle

Agent-to-agent communication does not imply authority.

An authority assertion is not authority by itself. It is a structured claim or evidence reference that may help a receiving system decide whether the requested action can be independently authorized, denied, deferred, escalated, or reauthorized.

## Relationship to Existing AAEF Concepts

This profile supports the following AAEF concepts:

- `AAEF-PRN-02`: principal context validity and continuity;
- `AAEF-DEL-05`: authority lineage across delegated, cross-agent, and cross-domain workflows;
- `AAEF-AUZ-01`: authorization at the point of execution;
- `AAEF-AUZ-08`: safe handling of material ambiguity;
- `AAEF-AUZ-09`: authority denial and reauthorization flow;
- `AAEF-EVD-01` through `AAEF-EVD-06`: evidence and auditability;
- `HIA-A2A`: external agent delegation or cross-domain agent action.

For the related planning concept, see `docs/en/31-cross-agent-cross-domain-authority.md`.

## Candidate Authority Assertion Fields

The following fields are planning candidates only.

### Assertion Identity

| Field | Purpose |
| --- | --- |
| `authority_assertion_id` | Unique identifier for the assertion. |
| `issuer` | Entity that issued the assertion. |
| `issuer_type` | Organization, system, agent operator, identity provider, authorization service, or other issuer class. |
| `issued_at` | Time the assertion was created. |
| `expires_at` | Time after which the assertion should not be relied upon. |
| `assertion_version` | Version of the assertion format or profile. |
| `integrity_reference` | Signature, hash, attestation reference, or other integrity mechanism where applicable. |

### Subject Agent and Operator

| Field | Purpose |
| --- | --- |
| `subject_agent_id` | Agent or agent instance the assertion is about. |
| `subject_agent_instance_id` | Runtime instance, session, or execution identity where available. |
| `operator` | Entity responsible for operating the subject agent. |
| `operator_contact_or_escalation` | Contact, escalation route, or incident response reference where appropriate. |
| `environment` | Production, staging, tenant, region, vendor environment, or other execution environment. |

### Principal Context

| Field | Purpose |
| --- | --- |
| `principal_id` | Principal on whose behalf the action or delegation is claimed. |
| `principal_type` | User, service account, organization, tenant, role, customer, or other principal type. |
| `principal_context_reference` | Reference to trusted context supporting the principal binding. |
| `principal_reconfirmation_reference` | Reference to reconfirmation when principal context is stale, ambiguous, degraded, or materially changed. |
| `principal_context_limitations` | Known limitations, uncertainty, or trust gaps in the principal context. |

### Delegated Scope

| Field | Purpose |
| --- | --- |
| `delegator` | Entity or agent that delegated authority. |
| `delegatee` | Entity or agent receiving delegated authority. |
| `delegated_actions` | Action types or operations covered by the assertion. |
| `resources` | Resources, objects, accounts, tenants, datasets, tools, or systems covered by the scope. |
| `purpose` | Purpose, business process, task, or workflow context. |
| `constraints` | Limits such as amount, count, time, depth, tool, tenant, environment, or approval condition. |
| `delegation_depth` | Current depth of delegation where relevant. |
| `redelegation_allowed` | Whether further delegation is allowed. |
| `effective_scope` | The authority scope that remains after constraints and receiving-side policy evaluation. |

### Trust Domain and Receiving-Side Verification

| Field | Purpose |
| --- | --- |
| `source_trust_domain` | Trust domain where the assertion originated. |
| `target_trust_domain` | Trust domain where the assertion is being evaluated. |
| `trust_relationship_reference` | Contract, federation, allowlist, policy, or trust configuration reference. |
| `receiving_side_verification_result` | Result of receiving-side verification. |
| `receiving_side_policy_reference` | Policy version or rule set used by the receiving side. |
| `verification_time` | Time at which the receiving side verified the assertion. |
| `verification_limitations` | Limitations or assumptions in the verification process. |

### Evidence References

| Field | Purpose |
| --- | --- |
| `authorization_decision_id` | Related authorization decision where available. |
| `delegation_record_id` | Related delegation record or grant. |
| `evidence_event_id` | Related AAEF evidence event. |
| `correlation_id` | Correlation identifier linking workflow steps. |
| `trace_id` | Trace identifier for distributed workflows. |
| `parent_action_id` | Upstream action or request that caused this assertion to be used. |
| `downstream_action_ids` | Downstream actions that relied on this assertion. |
| `evidence_trust_limitation` | Limitation on evidence reliability, completeness, independence, or verifiability. |

### Revocation, Freeze, and Reauthorization

| Field | Purpose |
| --- | --- |
| `revocation_status` | Current known revocation state. |
| `revocation_check_reference` | Reference to revocation, freeze, or authority-state check. |
| `freeze_status` | Whether related authority is frozen or conditionally constrained. |
| `reauthorization_required` | Whether receiving-side evaluation requires reauthorization. |
| `reauthorization_request_id` | Related reauthorization request where applicable. |
| `denied_action_id` | Related denied or deferred action where applicable. |
| `post_reauthorization_effective_scope` | Scope after reauthorization, if granted. |

## Receiving-Side Evaluation Questions

A receiving system should be able to answer:

1. Who issued the assertion?
2. Which agent or agent instance is the assertion about?
3. Who operates the agent?
4. On whose behalf is the action or delegation claimed?
5. What action, resource, purpose, and scope are covered?
6. What constraints apply?
7. Is redelegation allowed?
8. Has the assertion expired or been revoked?
9. Is principal context still current and bounded?
10. What evidence supports the assertion?
11. What evidence limitations remain?
12. Which receiving-side policy evaluated the assertion?
13. Was the request authorized, denied, deferred, escalated, or reauthorized?
14. Can downstream actions be traced back to this assertion?
15. Can the receiving side reconstruct the authority lineage after an incident?

## Safe Handling Expectations

A receiving system should not treat an authority assertion as sufficient when:

- the issuer is unknown or untrusted;
- the subject agent identity is ambiguous;
- the operator is unknown;
- the principal context is missing, stale, degraded, or unverifiable;
- delegated scope is broad, implicit, or unbounded;
- the assertion is expired or revocation state is unknown;
- redelegation semantics are unclear;
- evidence is self-reported only and cannot be correlated;
- receiving-side policy cannot verify the assertion;
- the assertion conflicts with local policy, state, or risk signals.

For high-impact actions, the safer outcome should be denial, deferral, escalation, freeze, scoped reauthorization, or safe termination.

## Non-Goals

This profile does not require:

- a universal agent-to-agent protocol;
- a universal credential format;
- a universal identity federation model;
- a universal cross-domain trust fabric;
- a specific signature format;
- a specific graph database;
- a specific tracing product;
- automatic trust in external agents;
- model self-assessment of authority.

## Future Work

Future AAEF work may decide whether to:

- add selected fields to the Evidence Event Schema;
- define a dedicated cross-agent authority evidence profile;
- add dedicated cross-agent or cross-domain controls;
- define examples for external agent delegation;
- define negative tests for forged, stale, or overbroad authority assertions;
- map this profile to identity, federation, attestation, or authorization technologies.
