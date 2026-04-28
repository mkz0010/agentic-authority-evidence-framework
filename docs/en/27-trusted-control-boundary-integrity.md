# Trusted Control Boundary Integrity Requirements

## Status

This document is part of the AAEF v0.4.0 planning work.

It defines integrity requirements for the Trusted Control Boundary used in AAEF architecture and assessment guidance.

This document is informative and does not create a certification scheme, formal standard, implementation conformance claim, audit opinion, or claim of complete mitigation.

## Purpose

AAEF is based on the principle that model output is not authority.

A model may propose a tool call, API call, workflow action, delegation, or other operation. However, that proposal should not itself become permission to execute.

The Trusted Control Boundary defines the parts of an agentic AI system that must enforce authorization, dispatch controls, execution boundaries, and evidence generation outside the model.

This document clarifies what must be true for that boundary to be treated as trusted enough for assessment use.

## Trusted Control Boundary Definition

In AAEF, the Trusted Control Boundary is the set of components, policies, enforcement points, evidence mechanisms, and state sources that are relied upon to determine, enforce, and evidence whether an agentic action is allowed.

The Trusted Control Boundary may include:

- authorization decision point,
- policy engine,
- tool dispatch enforcement point,
- backend API enforcement,
- evidence writer,
- evidence store,
- trusted state sources,
- identity and principal binding mechanisms,
- delegation and authority records,
- approval or escalation workflow,
- SIEM or audit log integration.

The model itself should not be treated as the Trusted Control Boundary.

## Core Principle

The core principle is:

> Model output is not authority.

Model output may be treated as:

- a proposal,
- an intent signal,
- a candidate action,
- a planning artifact,
- a natural-language explanation,
- or an input to a trusted decision process.

Model output must not be treated as:

- authorization,
- policy decision,
- approval,
- trusted evidence,
- identity proof,
- principal binding,
- delegation proof,
- or execution permission.

## Integrity Requirements

### 1. Model Output Must Not Directly Authorize Execution

The system must not execute high-impact tool calls, API calls, workflow actions, or delegations solely because the model requested them.

Execution should depend on a trusted authorization and enforcement path.

Assessment considerations:

- Can the model directly invoke a tool without an enforcement point?
- Can natural-language content change authority scope?
- Can the model self-declare that an action is authorized?
- Can the model override missing policy inputs?

### 2. Authorization Decisions Must Use Trusted Inputs

Authorization decisions should be based on trusted structured inputs.

Examples include:

- principal identity,
- agent identity,
- delegated authority,
- action type,
- resource,
- purpose,
- policy version,
- risk classification,
- state or revocation status,
- approval requirement,
- environmental constraints.

Untrusted content, retrieved content, user-provided instructions, or model-generated explanations should not be allowed to directly rewrite trusted authorization inputs.

### 3. Authorization-to-Dispatch Integrity Must Be Preserved

The authorization decision that permits an action should be bound to the action that is dispatched.

The system should prevent mismatch between:

- authorized action and dispatched action,
- authorized principal and executing principal,
- authorized resource and actual resource,
- authorized purpose and actual purpose,
- authorized scope and actual scope,
- authorization time and execution time.

Assessment considerations:

- Is there an action-bound authorization decision ID?
- Is the dispatched action linked to the authorization decision?
- Can a decision artifact be replayed for a different action?
- Can a stale authorization be reused after state changes?

### 4. Tool Dispatch Bypass Must Be Prevented

Tool dispatch should occur through an enforcement point.

The system should prevent direct execution paths that bypass:

- authorization decision point,
- policy checks,
- approval checks,
- dispatch enforcement,
- evidence generation,
- or backend authorization.

Assessment considerations:

- Are all tools routed through a dispatcher or equivalent enforcement layer?
- Are direct API credentials exposed to the model runtime?
- Are there alternate execution paths outside the controlled dispatch path?
- Are emergency or break-glass paths evidenced and scoped?

### 5. Backend Enforcement Must Remain Authoritative

Backend systems should not rely only on upstream model or runtime claims.

Where feasible, backend services should enforce or verify:

- principal context,
- authority scope,
- resource constraints,
- policy-relevant state,
- action authorization,
- and evidence correlation.

The backend may be the final enforcement layer when tool dispatch cannot fully enforce all constraints.

### 6. Evidence Writer Placement Must Be Trusted

Evidence should be generated by trusted components, not only by the model or an untrusted agent runtime.

Trusted evidence may be generated or corroborated by:

- authorization service,
- tool dispatch layer,
- backend execution system,
- workflow control plane,
- evidence writer,
- audit log pipeline,
- SIEM integration.

Model or runtime self-report may be useful as context, but should not be treated as sufficient evidence for high-impact assurance.

### 7. Evidence Must Be Bound to the Action Lifecycle

Evidence should support reconstruction across the action lifecycle.

At minimum, evidence should help correlate:

- proposed action,
- principal,
- agent,
- delegated authority,
- authorization decision,
- dispatch decision,
- execution result,
- policy version,
- state or revocation check,
- approval or escalation where applicable,
- non-execution or denial where applicable.

### 8. Trusted State Sources Must Be Identified

The system should identify which sources are trusted for policy-relevant state.

Examples:

- identity provider,
- authorization service,
- asset inventory,
- tool registry,
- policy repository,
- revocation state store,
- risk classification source,
- approval workflow system,
- backend system of record,
- SIEM or audit platform.

The model should not be the source of truth for policy-relevant state.

### 9. Replay and Reuse Resistance Should Be Considered

Authorization artifacts, approval records, delegation grants, and dispatch decisions should not be reusable outside their intended scope.

Controls may include:

- action hash,
- decision ID,
- nonce,
- expiration,
- policy version,
- principal binding,
- resource binding,
- scope binding,
- state snapshot,
- correlation ID,
- trace ID.

### 10. Failure Behavior Must Be Defined

The Trusted Control Boundary should define what happens when required trust inputs are missing, stale, ambiguous, unavailable, or contradictory.

For high-impact actions, the safer default should be denial, deferral, escalation, freeze, or reauthorization.

For v0.5.0 planning, see `docs/en/32-authority-denial-reauthorization-flow.md` for the Authority Denial and Reauthorization Flow concept note.

Assessment considerations:

- Does the system fail closed when authority is missing?
- Does the system deny or escalate when evidence generation fails?
- Does the system prevent execution when policy state is unavailable?
- Is non-execution evidenced?

## Boundary Anti-Patterns

The following patterns weaken the Trusted Control Boundary.

### Model-as-Policy

The model is allowed to decide whether an action is permitted without an external policy decision point.

### Model-as-Evidence

The model's statement that an action was authorized or executed is treated as sufficient evidence.

### Runtime Self-Attestation Only

The agent runtime self-reports compliance without independent or corroborated evidence.

### Direct Tool Credentials

The model or uncontrolled runtime has direct access to tool credentials that bypass dispatch enforcement.

### Untrusted Content Rewrites Authority

Instructions embedded in retrieved content, documents, emails, web pages, or other untrusted sources can change authority, scope, purpose, or approval requirements.

### Approval Without Context

Human approval is collected as a click or confirmation without enough information to understand the action, impact, authority, or risk.

### Evidence After the Fact

Evidence is generated after execution from untrusted summaries rather than captured during authorization, dispatch, and execution.

## Minimum Integrity Checklist

| Area | Minimum expectation | Example evidence |
|---|---|---|
| Model boundary | Model output is treated as proposal, not authority | Architecture diagram; policy design |
| Authorization | Trusted authorization decision point exists | Policy config; decision logs |
| Dispatch | Tool dispatch path is enforced | Dispatcher logs; enforcement tests |
| Backend | Backend verifies or enforces relevant constraints | API logs; backend policy checks |
| Evidence | Evidence is generated by trusted or corroborating components | Evidence writer logs; SIEM records |
| Action binding | Authorization is bound to the dispatched action | Decision ID; action hash; trace ID |
| Principal binding | Principal context is preserved | Principal claims; session records |
| Delegation | Delegated authority is scoped and traceable | Delegation records; authority chain |
| State | Trusted state sources are identified | State source registry; revocation checks |
| Replay resistance | Authorization artifacts are scoped and time-bound | Expiration; nonce; resource binding |
| Failure behavior | Missing or ambiguous authority fails safe | Denial logs; escalation records |
| Bypass prevention | Alternate execution paths are controlled | Tool registry; access review |

## Relationship to Reference Architecture

This document should be read with:

- `docs/en/17-reference-architecture.md`

The Reference Architecture shows where model runtime, authorization decision point, tool dispatch enforcement point, backend API, evidence writer, evidence store, and SIEM integration may sit.

This document defines what integrity expectations should hold across those components.

## Relationship to Testing Procedures

This document should be read with:

- `docs/en/25-testing-procedures-and-pass-criteria.md`
- `assessment/aaef-testing-procedures-v0.4-draft.csv`

Testing procedures describe how controls may be assessed.

Trusted Control Boundary integrity requirements describe what should be checked when evaluating whether model output is separated from authorization, enforcement, execution, and evidence.

## Relationship to High-Impact and Audit-Grade Pre-qualification

This document should be read with:

- `docs/en/26-high-impact-audit-grade-prequalification.md`

High-Impact and Audit-Grade profiles should depend on whether the Trusted Control Boundary is sufficiently defined and evidenced.

If the boundary cannot be identified or assessed, higher-assurance profiles should be constrained or avoided.

## Non-Goals

This document does not define a single required architecture.

It does not require a specific product, framework, policy engine, identity provider, SIEM, or runtime.

It does not claim that any implementation is compliant or certified.

It does not eliminate the need for organization-specific threat modeling.

It does not guarantee that all prompt injection, tool misuse, or excessive agency risks are mitigated.

## Open Questions

Future work should determine:

- whether Trusted Control Boundary requirements should become machine-readable,
- whether additional control catalog entries are needed,
- how to assess TCB integrity across distributed agent systems,
- how to represent partial or degraded trust boundaries,
- how to handle cross-agent and cross-domain authority transfer,
- how to test bypass resistance in common agent frameworks,
- and how to map TCB integrity requirements to external frameworks.
