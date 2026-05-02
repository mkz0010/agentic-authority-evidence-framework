# AAEF v0.6.0 Implementation Reference Pattern Planning

Status: Implementation reference planning  
Related roadmap: #241  
Related reassessment response: `docs/en/status/v060-external-review-reassessment-response.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document defines a non-normative implementation reference pattern for applying AAEF concepts to a minimal agentic AI action flow.

The purpose is to bridge AAEF from conceptual control and evidence requirements toward an implementable pattern that field implementers, auditors, operators, managers, consultants, and researchers can review.

This document is planning and illustrative material. It does not change active controls, schemas, examples, testing procedures, mappings, assessment artifacts, or the current control and assessment baseline.

## Why this artifact is needed

External reassessment identified implementation feasibility as the first adoption priority.

AAEF is conceptually strong, but adoption requires a clearer bridge from framework concepts to implementation patterns.

This document responds to that gap by describing a minimal implementation pattern for:

1. action request,
2. authorization decision artifact,
3. dispatch enforcement,
4. backend relying-party verification,
5. evidence event generation,
6. non-execution behavior,
7. reconstruction and review.

The pattern is intentionally implementation-neutral. It does not require a specific SDK, cloud provider, policy engine, orchestration framework, or agent platform.

## Non-normative status

This document is not an implementation conformance profile.

It does not claim that a system implementing this pattern is AAEF-certified, compliant, conformant, audit-ready, or equivalent to any external framework.

The pattern is intended to help readers understand how AAEF concepts may be implemented and assessed.

## Minimal reference flow

A minimal AAEF-style implementation flow contains the following stages.

| Stage | Purpose |
| --- | --- |
| 1. Action request | Capture the proposed agentic action and its context before execution. |
| 2. Authorization decision | Produce an explicit decision artifact outside the model output itself. |
| 3. Dispatch enforcement | Permit, deny, or hold the action at the execution boundary. |
| 4. Backend relying-party verification | Let the receiving backend verify that the action is authorized. |
| 5. Evidence generation | Record structured evidence for the action or non-execution. |
| 6. Failure / non-execution handling | Fail closed when authorization, dispatch, backend verification, or evidence requirements are not met. |
| 7. Reconstruction | Use evidence to reconstruct who acted, on whose behalf, with what authority, and what happened. |

## Reference components

A minimal implementation may use the following logical components.

| Component | Responsibility | Trust consideration |
| --- | --- | --- |
| Agent runtime | Produces proposed actions or tool-call requests. | Should not be treated as the authority source. |
| Action request builder | Normalizes the proposed action into a structured request. | Should separate model output from policy inputs. |
| Authorization decision point | Evaluates the action against policy, principal context, scope, and risk. | Should not rely on natural-language content alone. |
| Authorization decision artifact | Records the authorization result, scope, constraints, expiry, and identifiers. | Should be bound to the action and protected from reuse or tampering. |
| Tool dispatcher / execution gateway | Enforces the decision before invoking a tool or backend. | Should fail closed when the decision is missing, expired, mismatched, or invalid. |
| Backend relying party | Independently verifies the decision or delegated authorization before performing the action. | Should not rely solely on the agent runtime's assertion. |
| Evidence writer | Emits structured evidence event records. | Should be outside the model-controlled path where feasible. |
| Evidence store | Stores evidence for review, reconstruction, and incident response. | Should preserve integrity, retention, and access boundaries. |
| Review / reconstruction interface | Supports audit, incident review, and risk-owner decision review. | Should expose evidence without overstating assurance. |

## Reference sequence

A minimal sequence is:

1. The agent proposes an action.
2. The action request builder creates a structured action request.
3. The authorization decision point evaluates the request.
4. The decision point emits an authorization decision artifact.
5. The dispatcher validates the artifact before execution.
6. The backend relying party verifies the action, decision, scope, and constraints.
7. The backend performs the action only if verification succeeds.
8. The evidence writer records execution or non-execution evidence.
9. The evidence store preserves the event.
10. Reviewers reconstruct the action from evidence.

## Text sequence diagram

    User / Principal
        |
        v
    Agent Runtime
        |
        | proposed action
        v
    Action Request Builder
        |
        | structured action request
        v
    Authorization Decision Point
        |
        | authorization decision artifact
        v
    Tool Dispatcher / Execution Gateway
        |
        | verified dispatch
        v
    Backend Relying Party
        |
        | action result / denial
        v
    Evidence Writer
        |
        | evidence event
        v
    Evidence Store
        |
        v
    Review / Reconstruction

## Action request shape

An illustrative action request may include:

| Field | Purpose |
| --- | --- |
| `action_request_id` | Unique identifier for the proposed action. |
| `requested_action` | Canonical action name or type. |
| `target_resource` | Resource, system, account, dataset, or object affected. |
| `principal_id` | Principal on whose behalf the action is requested. |
| `agent_instance_id` | Agent or runtime instance proposing the action. |
| `session_id` | Session, task, or workflow context. |
| `input_sources` | Sources influencing the proposed action. |
| `untrusted_input_present` | Whether untrusted content influenced the request. |
| `impact_level` | Organizational impact classification. |
| `requested_scope` | Scope of requested authority. |
| `requested_time_window` | Time window for execution. |
| `reason_code` | Structured reason, not free-text-only authority. |
| `request_hash` | Hash or canonical digest of the request. |

This shape is illustrative and does not replace active schema artifacts.

## Authorization decision artifact shape

An illustrative authorization decision artifact may include:

| Field | Purpose |
| --- | --- |
| `authorization_decision_id` | Unique decision identifier. |
| `action_request_id` | Link to the request being authorized. |
| `decision` | Permit, deny, hold, require approval, or require reauthorization. |
| `principal_id` | Principal bound to the decision. |
| `authorized_action` | Canonical action permitted or denied. |
| `authorized_resource` | Resource or resource pattern covered by the decision. |
| `authorized_scope` | Scope and limits of authority. |
| `policy_version` | Policy or rule set used for the decision. |
| `decision_time` | Time of decision. |
| `expires_at` | Expiration time for the decision. |
| `constraints` | Conditions such as amount, destination, tool, tenant, or environment limits. |
| `trusted_inputs_used` | Trusted inputs used in the decision. |
| `untrusted_inputs_excluded` | Untrusted inputs explicitly excluded from authority. |
| `decision_hash` | Integrity binding for the decision artifact. |
| `approver_id` | Human or system approver where applicable. |
| `approval_evidence_ref` | Reference to approval evidence where applicable. |

This planning shape aligns with v0.6.0 authorization decision artifact planning but does not make it active schema.

## Dispatch enforcement checks

The dispatcher or execution gateway should check at least:

| Check | Example failure |
| --- | --- |
| Decision exists | No authorization decision artifact is present. |
| Decision matches request | Decision does not match `action_request_id` or request hash. |
| Decision permits action | Decision is deny, hold, expired, or require approval. |
| Principal matches | Principal differs from the decision artifact. |
| Action matches | Requested tool/action differs from authorized action. |
| Resource matches | Target resource is outside authorized scope. |
| Scope matches | Amount, tenant, environment, or time window exceeds constraints. |
| Policy version acceptable | Decision was made under obsolete or disallowed policy. |
| Expiry valid | Decision has expired. |
| Evidence requirement satisfiable | Required evidence cannot be generated or linked. |

The dispatcher should fail closed when a required check fails.

## Backend relying-party verification

The backend receiving an action should not rely only on the agent runtime's statement that an action is authorized.

A backend relying party should verify:

- the decision identifier,
- action request binding,
- principal binding,
- authorized action,
- authorized resource,
- authorized scope,
- expiry,
- policy version,
- replay protection,
- and evidence linkage requirements where applicable.

This may be implemented through token introspection, signed decision artifacts, policy service lookup, mTLS-bound requests, internal authorization APIs, or other mechanisms.

This document does not require a specific verification mechanism.

## Evidence event expectations

Evidence should allow a reviewer to answer:

1. What action was requested?
2. What decision was made?
3. Which policy or rule set was used?
4. Who or what was the principal?
5. Which agent or runtime proposed the action?
6. What dispatcher or gateway enforced the decision?
7. What backend performed or rejected the action?
8. What evidence proves execution or non-execution?
9. Were untrusted inputs involved?
10. What limitations apply to the evidence?

An evidence event should link to:

- action request,
- authorization decision,
- dispatch decision,
- backend verification result,
- execution result or non-execution reason,
- and evidence trust limitations.

## Non-execution behavior

AAEF implementation patterns should treat non-execution as an important outcome.

A non-execution event should be recorded when:

- authorization is missing,
- authorization is denied,
- approval is required but absent,
- decision is expired,
- request and decision do not match,
- scope is exceeded,
- backend verification fails,
- evidence cannot be generated,
- policy version is invalid,
- or the system freezes execution due to risk.

Non-execution evidence is important because it shows that a system enforced boundaries rather than merely logging successful actions.

## Reconstruction path

A reviewer should be able to reconstruct the action chain by following:

1. `action_request_id`,
2. `authorization_decision_id`,
3. dispatch event identifier,
4. backend verification identifier,
5. execution or non-execution evidence event,
6. evidence storage reference,
7. incident or review record.

The reconstruction should support review by implementers, auditors, operators, risk owners, consultants, and incident responders.

## Failure modes

The following failure modes should be considered.

| Failure mode | Risk | Expected behavior |
| --- | --- | --- |
| Model output treated as authority | Prompt or context content becomes executable authority. | Require explicit authorization artifact. |
| Missing decision artifact | Dispatcher cannot prove authorization. | Fail closed and record non-execution. |
| Expired decision | Old authorization is reused. | Reject and require reauthorization. |
| Action mismatch | Decision authorizes one action but dispatcher executes another. | Reject and record mismatch. |
| Scope expansion | Agent expands resource, amount, tenant, or time scope. | Reject or require new authorization. |
| Backend trusts runtime assertion only | Agent runtime becomes de facto authority. | Require backend verification. |
| Evidence generated only by agent runtime | Evidence may be self-referential or untrusted. | Record evidence limitation and strengthen writer placement. |
| Evidence missing | Action cannot be reconstructed. | Fail closed for evidence-required actions. |
| Replay of decision artifact | Old decision is reused for a new action. | Bind decision to request hash and expiry. |
| Human approval laundering | Broad or ambiguous approval is reused. | Bind approval to specific action, scope, and time. |

## Persona-specific use

### Field implementer

A field implementer can use this pattern to identify:

- components to build,
- checks to implement,
- identifiers to propagate,
- failure paths to handle,
- evidence events to emit,
- and reconstruction queries to support.

### Security architect

A security architect can use this pattern to reason about:

- control placement,
- trusted control boundaries,
- dispatcher placement,
- backend relying-party verification,
- evidence writer placement,
- and residual trust assumptions.

### Operator / administrator

An operator can use this pattern to prepare:

- operational ownership,
- monitoring requirements,
- failure handling procedures,
- freeze or hold behavior,
- evidence retention expectations,
- and incident response handoffs.

### Auditor / assessor

An auditor or assessor can use this pattern to ask:

- where authorization decisions are made,
- what evidence proves the decision,
- where dispatch enforcement happens,
- whether backend verification is independent,
- whether evidence is sufficient for reconstruction,
- and what evidence trust limitations exist.

### Manager / risk owner

A manager or risk owner can use this pattern to decide:

- whether a high-impact action should be allowed,
- whether approval is meaningful,
- whether residual risk is acceptable,
- whether additional controls are needed,
- and whether evidence is adequate for accountability.

### Consultant

A consultant can use this pattern for discovery:

- What actions can the agent perform?
- Which actions are high-impact?
- Who is the principal?
- Where is authorization decided?
- Where is dispatch enforced?
- Does the backend independently verify authority?
- What evidence exists?
- Can the action be reconstructed?
- What assumptions limit assurance?

## Relationship to v0.4.1 baseline

This document does not update the v0.4.1 baseline.

It is intended to illustrate how current AAEF concepts may be implemented and reviewed.

Any future promotion into active controls, schema requirements, examples, testing procedures, or assessment artifacts must be handled through explicit PRs.

## Relationship to v0.6.0 planning materials

This document supports v0.6.0 Practical Adoption Readiness by connecting:

- authorization decision artifact planning,
- implementer quick start planning,
- operational responsibility planning,
- high-impact production architecture planning,
- legal/compliance applicability planning,
- risk owner planning,
- and external review reassessment response.

It remains non-normative planning material.

## Candidate future artifacts

This pattern may later support:

- a concrete minimal prototype,
- an implementation checklist,
- an evidence example,
- a non-execution example,
- a backend verification example,
- an auditor evidence request list,
- a consultant discovery worksheet,
- and a risk-owner decision memo template.

## Claim boundaries

This document does not claim:

- certification,
- legal compliance,
- regulatory compliance,
- audit sufficiency,
- conformity,
- equivalence with external frameworks,
- production readiness,
- complete mitigation,
- or implementation conformance.

It may support:

- planning,
- implementation discussion,
- assessment discussion,
- evidence design,
- reconstruction analysis,
- risk decision support,
- and public review.

## Recommended next steps

Recommended next steps:

1. Review this pattern against existing v0.4.1 controls.
2. Identify which fields can be illustrated through examples.
3. Create a minimal evidence example for a permitted action.
4. Create a minimal non-execution evidence example.
5. Create an auditor-facing evidence request checklist.
6. Create a consultant-facing discovery checklist.
7. Decide whether a prototype should be implemented in a separate repository or under examples.

## Non-goals

This document does not:

- change active controls,
- change the current control and assessment baseline,
- update schemas, examples, mappings, CSVs, or testing procedures,
- promote v0.5.0 or v0.6.0 planning material into active requirements,
- require a specific SDK, cloud, policy engine, or agent framework,
- certify an implementation,
- claim compliance,
- provide an audit opinion,
- claim conformity,
- claim equivalence with external frameworks,
- or assert production readiness.

## Acceptance criteria

This planning artifact is sufficient when:

- a minimal AAEF-style implementation flow is described,
- reference components are identified,
- dispatch and backend verification expectations are explained,
- evidence and non-execution behavior are described,
- reconstruction path is identified,
- persona-specific use is explained,
- failure modes are documented,
- claim boundaries are preserved,
- and no active baseline change is implied.
