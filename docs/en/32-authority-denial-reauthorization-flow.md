# Authority Denial and Reauthorization Flow

**Status:** v0.5.0 planning concept note
**AAEF baseline:** v0.4.1 Public Review Draft
**Issue context:** #21

## Purpose

This note defines Authority Denial and Reauthorization Flow as a v0.5.0 planning concept for AAEF.

It explains how high-impact agentic actions should be handled when authority is missing, insufficient, ambiguous, stale, denied, deferred, or materially changed before execution.

AAEF already includes related controls such as `AAEF-AUZ-09` and `AAEF-EVD-06`. This document does not add new controls or schema fields yet. It clarifies the concept and prepares future refinements to authorization, evidence, response, and testing guidance.

## Definition

**Authority Denial and Reauthorization Flow** is the controlled process by which an agentic system handles a high-impact action that cannot safely proceed under the currently available authority.

This includes cases where the system must:

- deny the action;
- defer the action;
- escalate the action;
- request scoped reauthorization;
- request principal reconfirmation;
- narrow the requested action;
- terminate safely;
- freeze or isolate affected authority;
- record non-execution and reauthorization evidence.

## Core Principle

A denied action must not become an alternate path to execution.

If a high-impact action is denied, deferred, or escalated, the agent should not be able to bypass that outcome through repeated retries, task splitting, scope creep, prompt reformulation, alternate tools, or unbounded reauthorization requests.

Reauthorization should be scoped, attributable, evidenced, and linked to the original denied or deferred action.

## Why This Matters

Agentic AI systems often continue working after encountering a denial, error, missing permission, missing evidence, or ambiguous authority state.

Without a controlled flow, a denial can become a bypass opportunity.

Examples:

- an agent retries a denied action with slightly different parameters;
- an agent splits a denied high-impact action into smaller actions;
- an agent asks a human for broader approval than originally needed;
- an agent changes tools after one tool path is denied;
- an agent treats a denied action as a reason to request excessive authority;
- a workflow continues after principal context has degraded;
- missing evidence is converted into an informal approval request.

AAEF should treat these cases as authorization and evidence events, not merely application errors.

## Denial and Reauthorization Patterns

### 1. Safe Denial

The system determines that authority is missing, insufficient, revoked, expired, ambiguous, or out of scope, and the action does not execute.

Expected behavior:

- execution is blocked;
- denial reason is recorded;
- principal and requested action are recorded where appropriate;
- related workflow state is preserved for review.

### 2. Deferral

The system cannot safely authorize the action yet, but the action may proceed later if missing context, evidence, approval, or runtime state is resolved.

Expected behavior:

- action is not executed during uncertainty;
- required missing inputs are identified;
- deferral state is recorded;
- execution requires a new authorization decision.

### 3. Escalation

The system routes the action to a human, higher authority, policy owner, security operator, or governance process.

Expected behavior:

- escalation target is recorded;
- escalation scope is bounded;
- the agent cannot broaden the requested authority during escalation;
- escalation outcome is linked to the original action.

### 4. Scoped Reauthorization

The system requests renewed or additional authority for a specific action, scope, resource, purpose, and risk level.

Expected behavior:

- requested additional scope is explicit;
- the request is linked to the original denial or deferral;
- principal reconfirmation is required where appropriate;
- the reauthorization decision is recorded;
- the new authority cannot silently exceed the requested scope.

### 5. Retry Control

The system allows retry only when retry does not bypass the denial reason.

Expected behavior:

- retry count is tracked;
- retry reason is recorded;
- repeated denials trigger escalation or termination;
- alternate tool paths do not bypass the original authorization decision.

### 6. Task Splitting Detection

The system detects attempts to split a denied high-impact action into smaller actions that have the same effective impact.

Expected behavior:

- related actions are correlated;
- cumulative impact is evaluated;
- prior denial context is considered;
- suspicious splitting is denied, escalated, or investigated.

### 7. Safe Termination

The system ends the workflow without execution when reauthorization is not appropriate.

Expected behavior:

- termination reason is recorded;
- partial state is handled safely;
- no further high-impact action occurs from the denied request;
- evidence is preserved.

## Relationship to Existing AAEF Controls

| Existing area | Relationship |
| --- | --- |
| `AAEF-AUZ-04` | Missing or ambiguous authority should fail safe through denial, deferral, escalation, freeze, or reauthorization. |
| `AAEF-AUZ-08` | Material ambiguity should not be resolved by model assertion alone. Denial or reauthorization may be required. |
| `AAEF-AUZ-09` | Primary existing control for safe handling of denied, deferred, escalated, retried, or reauthorization-required actions. |
| `AAEF-EVD-06` | Primary existing evidence control for reauthorization requests, additional scope requests, principal reconfirmation, retry count, and escalation decisions. |
| `AAEF-PRN-02` | Principal context preservation affects whether reauthorization can be trusted or whether principal reconfirmation is needed. |
| `AAEF-DEL-*` | Delegation constraints affect whether a downstream agent may request additional authority or reauthorization. |
| `AAEF-RES-*` | Freeze, isolation, containment, or revocation may be required when denial indicates risk, compromise, or unsafe runtime state. |
| Principal Context Degradation | Degraded principal context may trigger denial, deferral, escalation, or scoped reauthorization. |
| Cross-Agent and Cross-Domain Authority | Cross-domain authority gaps may require receiving-side denial, reauthorization, or external evidence verification. |

## Suggested Authorization Behavior

For high-impact actions, systems should deny, defer, escalate, freeze, or require scoped reauthorization when:

- authority is missing;
- authority is insufficient;
- authority is expired;
- authority has been revoked;
- principal context is missing or degraded;
- requested scope exceeds granted scope;
- delegation constraints are unclear or exceeded;
- runtime state has materially changed;
- policy applicability is ambiguous;
- required evidence is missing;
- prior denial is being retried without resolution;
- a similar denied action is being split into smaller actions.

The system should not rely on model-generated explanations as sufficient reauthorization.

## Evidence Considerations

Future evidence refinements may need to represent:

- denied action ID;
- denial reason;
- missing authority scope;
- ambiguity category;
- deferral reason;
- escalation target;
- reauthorization request ID;
- requested additional scope;
- principal reconfirmation reference;
- approver or authority source;
- retry count;
- related prior denial IDs;
- task splitting correlation;
- reauthorization decision;
- post-reauthorization effective scope;
- safe termination record.

These fields should be generated by trusted workflow, authorization, evidence, or enforcement components. They should not depend solely on model self-report.

## Assessment Questions

Reviewers may ask:

1. Are denied high-impact actions prevented from executing?
2. Are denial reasons recorded in structured evidence?
3. Can the system distinguish denial, deferral, escalation, reauthorization, retry, and safe termination?
4. Are reauthorization requests scoped and linked to the original denied action?
5. Is principal reconfirmation required when principal context is stale, ambiguous, or degraded?
6. Are retry loops and repeated denials detectable?
7. Can agents bypass denial by switching tools, splitting tasks, or reformulating the request?
8. Are escalation decisions attributable and reviewable?
9. Does reauthorization produce a new authorization decision rather than modifying the original denial silently?
10. Is non-execution evidence preserved for incident reconstruction?

## Non-Goals

This concept does not require:

- a specific approval workflow tool;
- a specific human review interface;
- universal real-time revocation;
- automatic approval of reauthorization requests;
- storing sensitive approval data directly in evidence records;
- allowing the model to self-authorize additional scope.

Implementations may use workflow metadata, authorization decision artifacts, denial records, escalation records, approval records, signed claims, policy decision logs, and evidence references.

## Future Work

Future v0.5.0 work may include:

- strengthening `AAEF-AUZ-09`;
- strengthening `AAEF-EVD-06`;
- adding testing procedure refinements for retry loops, scope creep, and task splitting;
- adding evidence schema fields for denial and reauthorization paths;
- integrating this concept with Principal Context Degradation;
- integrating this concept with Cross-Agent and Cross-Domain Authority;
- defining safe reauthorization examples for long-running and delegated workflows.
## Related Examples

For non-normative non-execution and reauthorization examples, see `docs/en/41-non-execution-reauthorization-examples.md`.
