# AAEF v0.6.0 Authorization Decision Artifact Minimal Profile Planning Draft

Status: Planning input  
Related roadmap: #241  
Related track: #243  
Related architecture track: #246  
Parent planning synthesis: `docs/en/status/v060-planning-input-synthesis.md`  
Related architecture planning: `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document defines an initial planning draft for a minimal Authorization Decision Artifact profile.

The purpose is to identify the minimum structured authorization decision data needed to bind a high-impact agentic action request to dispatch, backend verification, evidence generation, and later review.

This document is planning material. It does not change active controls, assessment criteria, schema requirements, or the current control and assessment baseline.

## Why this is needed

AAEF v0.6.0 is moving toward Practical Adoption Readiness.

The High-Impact Production Minimum Architecture Profile identifies that production deployments need explicit authorization decisions, mediated dispatch, backend relying-party verification, and trusted evidence generation.

Those mechanisms need a common artifact to bind them together.

A minimal Authorization Decision Artifact helps answer:

- what action was authorized or denied
- who or what the decision applies to
- which policy version was used
- what scope and constraints apply
- when the decision was issued and when it expires
- whether dispatch and backend execution match the decision
- what evidence should be generated or linked

## Scope

This planning draft covers candidate fields and validation expectations for a minimal authorization decision artifact used in high-impact agentic action assurance.

The draft focuses on:

- artifact identity
- issuer identity
- decision subject
- action scope
- policy version
- decision result
- time bounds
- action binding
- constraints
- evidence expectations
- backend verification support
- dispatch verification support

## Non-goals

This planning draft does not:

- define a final JSON schema
- define a complete SDK
- mandate a specific policy engine
- mandate a specific signature or token format
- require a specific identity provider
- change the current active AAEF baseline
- create certification or legal compliance claims

## Core principle

The artifact should preserve the AAEF principle:

> Model output is not authority.

The artifact should therefore be issued by a trusted authorization component, not by the model output itself.

The agent runtime may request an action, but the Authorization Decision Artifact should represent an authorization-layer decision over that request.

## Candidate minimal field set

The following fields are candidates for the minimal profile.

| Field | Purpose |
| --- | --- |
| `authorization_decision_id` | Unique identifier for the decision. |
| `decision_issuer` | Trusted component that issued the decision. |
| `decision_result` | Whether the request was allowed, denied, requires approval, or requires reauthorization. |
| `principal_id` | Principal on whose behalf the action is requested or authorized. |
| `agent_id` | Agent, workflow, or runtime requesting or preparing the action. |
| `action_type` | Type of action being authorized. |
| `resource_id` | Target resource, system, record, account, or environment. |
| `action_hash` | Canonical binding to the requested action payload or normalized action request. |
| `policy_version` | Policy version used for the decision. |
| `issued_at` | Time the decision was issued. |
| `expires_at` | Time after which the decision is no longer valid. |
| `constraints` | Limits, conditions, approval requirements, or execution boundaries. |
| `evidence_required` | Whether evidence must be generated or linked for execution. |
| `correlation_id` | Cross-system identifier for request, decision, dispatch, execution, and evidence. |

## Candidate recommended fields

The following fields may be recommended rather than required in a minimal profile.

| Field | Purpose |
| --- | --- |
| `risk_tier` | Indicates action impact or risk tier. |
| `approval_id` | Links to human or organizational approval where required. |
| `delegation_id` | Links to delegated authority where applicable. |
| `request_id` | Links to the normalized action request. |
| `dispatch_id` | Links to mediated dispatch. |
| `backend_verification_required` | Indicates whether backend relying-party verification is expected. |
| `non_execution_evidence_required` | Indicates whether refusal, denial, or non-execution must produce evidence. |
| `limitations` | Records known limitations in the decision or context. |

## Candidate decision results

The minimal profile should support more than simple allow/deny behavior.

Candidate values:

| Value | Meaning |
| --- | --- |
| `allow` | Action may proceed within the decision scope and constraints. |
| `deny` | Action must not proceed. |
| `approval_required` | Action requires approval before dispatch or execution. |
| `reauthorization_required` | Existing authorization is insufficient or expired. |
| `not_applicable` | Request is outside the decision point's scope. |

## Candidate validation expectations

Before tool dispatch, the enforcement point should verify:

- the artifact is present when required
- `decision_result` allows dispatch
- `authorization_decision_id` is unique or otherwise traceable
- `decision_issuer` is trusted
- `principal_id` matches the authorized principal
- `agent_id` is in scope
- `action_type` matches the requested tool or operation
- `resource_id` is within authorized scope
- `action_hash` matches the normalized action request
- `policy_version` is known
- `expires_at` has not passed
- constraints are satisfied
- evidence requirements are understood

Before backend execution, the relying party should verify:

- the execution request is bound to the same decision
- the action, resource, principal, and constraints still match
- the decision has not expired
- the dispatch path is expected
- execution can produce or link required evidence

## Candidate canonical JSON shape

This shape is illustrative and planning-only.

~~~~json
{
  "authorization_decision_id": "adz_2026_000001",
  "decision_issuer": "aaef-authorization-service",
  "decision_result": "allow",
  "principal_id": "user_12345",
  "agent_id": "agent_invoice_ops",
  "action_type": "payment.release",
  "resource_id": "invoice_98765",
  "action_hash": "sha256:example",
  "policy_version": "policy-v12",
  "issued_at": "2026-05-01T16:00:00Z",
  "expires_at": "2026-05-01T16:05:00Z",
  "constraints": {
    "max_amount": "100000",
    "currency": "JPY",
    "approved_payee_only": true
  },
  "evidence_required": true,
  "correlation_id": "corr_2026_000001"
}
~~~~

## Relationship to dispatch attestation

The dispatch layer should not merely record that a tool was called.

It should be able to attest that dispatch was based on a valid Authorization Decision Artifact.

A future Dispatch Attestation profile may include:

- `dispatch_id`
- `authorization_decision_id`
- `correlation_id`
- `tool_name`
- `action_type`
- `resource_id`
- `dispatch_time`
- `dispatch_result`
- `dispatch_enforcement_component`
- `evidence_event_id`

## Relationship to backend relying-party verification

The backend relying party should not treat the agent runtime or gateway assertion as sufficient authority.

The backend should verify relevant fields from the Authorization Decision Artifact before execution.

This planning draft therefore supports future backend verification examples and implementer quick-start guidance.

## Relationship to evidence

Evidence should be able to reconstruct the path from:

1. action request
2. authorization decision
3. approval where applicable
4. dispatch enforcement
5. backend verification
6. execution, refusal, non-execution, override, or reauthorization

The Authorization Decision Artifact should provide stable identifiers and bindings for that reconstruction.

## Candidate anti-patterns

| Anti-pattern | Risk |
| --- | --- |
| Natural-language approval only | Approval cannot be reliably bound to the executed action. |
| No expiration | Stale decisions can be reused. |
| No action hash | Requested and executed actions may diverge. |
| Agent-issued authorization | Model output becomes authority. |
| Backend does not verify decision | Gateway bypass or replay may not be detected. |
| No policy version | Decision cannot be tied to a known policy basis. |
| No evidence linkage | Later review cannot reconstruct the action path. |

## Open questions

The following questions should be resolved before turning this planning draft into an adoption-facing artifact:

- Which fields are truly required for the minimal profile?
- Should the profile define a JSON schema in v0.6.0?
- Should signature, MAC, or token binding be recommended or deferred?
- Should `action_hash` be required for all high-impact actions?
- Should `expires_at` always be mandatory?
- How should approvals, delegation, and override decisions be represented?
- Should denied and non-executed actions use the same artifact shape?
- How should this profile relate to the existing Evidence Event Schema?
- Which examples should be included in Implementer Quick Start?

## Acceptance criteria for this planning draft

This planning draft is sufficient when:

- candidate minimal fields are identified
- candidate recommended fields are identified
- dispatch validation expectations are described
- backend verification expectations are described
- evidence linkage expectations are described
- anti-patterns are documented
- no active baseline change is implied
- #243 can use this document as input for Implementer Quick Start and related profiles

## Expected next steps

Recommended next steps:

1. Review the minimal and recommended field sets.
2. Decide whether a v0.6.0 JSON schema candidate should be created.
3. Use this profile as the basis for Implementer Quick Start.
4. Coordinate with the architecture profile for backend relying-party verification.
5. Coordinate with evidence guidance before changing active schema artifacts.
