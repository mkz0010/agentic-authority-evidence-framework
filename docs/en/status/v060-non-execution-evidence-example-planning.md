# AAEF v0.6.0 Non-Execution Evidence Example Planning

Status: Evidence example planning  
Related roadmap: #241  
Related implementation reference: `docs/en/status/v060-implementation-reference-pattern-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document provides a non-normative planning example of evidence for a rejected or non-executed agentic action.

The purpose is to show that AAEF-style evidence should record not only successful execution but also boundary enforcement, denial, hold, reauthorization, and fail-closed outcomes.

This document is illustrative planning material. It does not update active schemas, examples, controls, mappings, testing procedures, assessment artifacts, or the current control and assessment baseline.

## Scenario

A support operations agent proposes an action:

> Rotate a production service API key for service `svc-billing-export`.

However, the action request attempts to change the `secondary` key slot even though the authorization decision only covers the `primary` key slot.

The dispatcher detects a scope mismatch and prevents execution.

## Why non-execution evidence matters

Non-execution evidence demonstrates that a system enforced authority boundaries.

Without non-execution evidence, a reviewer may only see actions that succeeded. That can hide attempted boundary violations, rejected tool calls, expired decisions, approval gaps, or backend verification failures.

Non-execution records help auditors, operators, incident responders, managers, and consultants understand whether the system failed closed.

## Illustrative action request

    {
      "action_request_id": "arq-20260502-0002",
      "requested_action": "rotate_service_api_key",
      "target_resource": "service:svc-billing-export:key:secondary",
      "principal_id": "user:ops-engineer-17",
      "agent_instance_id": "agent:ops-maintenance-assistant:session-9f2a",
      "session_id": "maint-session-20260502-01",
      "input_sources": [
        {
          "source_type": "change_ticket",
          "source_id": "chg-20260502-1042",
          "trusted_for_authority": true
        },
        {
          "source_type": "chat_instruction",
          "source_id": "chatmsg-7815",
          "trusted_for_authority": false
        }
      ],
      "untrusted_input_present": true,
      "impact_level": "high",
      "requested_scope": {
        "action": "rotate",
        "service": "svc-billing-export",
        "environment": "production",
        "key_slot": "secondary"
      },
      "requested_time_window": {
        "not_before": "2026-05-02T07:00:00Z",
        "not_after": "2026-05-02T08:00:00Z"
      },
      "reason_code": "approved_maintenance_key_rotation",
      "request_hash": "sha256:example-request-hash-secondary"
    }

## Illustrative authorization decision

The available authorization decision only permits the `primary` key slot.

    {
      "authorization_decision_id": "auz-20260502-0001",
      "action_request_id": "arq-20260502-0001",
      "decision": "permit",
      "principal_id": "user:ops-engineer-17",
      "authorized_action": "rotate_service_api_key",
      "authorized_resource": "service:svc-billing-export:key:primary",
      "authorized_scope": {
        "action": "rotate",
        "service": "svc-billing-export",
        "environment": "production",
        "key_slot": "primary"
      },
      "policy_version": "policy-agentic-prod-maintenance-2026-05-01",
      "decision_time": "2026-05-02T07:10:12Z",
      "expires_at": "2026-05-02T08:00:00Z",
      "constraints": {
        "change_ticket_id": "chg-20260502-1042",
        "requires_backend_verification": true,
        "requires_evidence_event": true,
        "requires_non_reuse": true
      },
      "decision_hash": "sha256:example-decision-hash"
    }

## Illustrative dispatch enforcement result

The dispatcher rejects execution because the requested resource does not match the authorized resource.

    {
      "dispatch_event_id": "dsp-20260502-0002",
      "authorization_decision_id": "auz-20260502-0001",
      "action_request_id": "arq-20260502-0002",
      "dispatcher_id": "dispatcher:prod-tool-gateway-01",
      "dispatch_decision": "denied",
      "denial_reason": "resource_scope_mismatch",
      "checks": {
        "decision_exists": "pass",
        "decision_not_expired": "pass",
        "request_binding_matches": "fail",
        "principal_matches": "pass",
        "action_matches": "pass",
        "resource_matches": "fail",
        "scope_constraints_match": "fail",
        "policy_version_accepted": "pass",
        "evidence_required": "pass"
      },
      "expected_resource": "service:svc-billing-export:key:primary",
      "requested_resource": "service:svc-billing-export:key:secondary",
      "dispatch_time": "2026-05-02T07:13:04Z"
    }

## Illustrative backend result

The backend is not invoked for execution because dispatch enforcement failed.

    {
      "backend_verification_id": null,
      "backend_id": "backend:key-management-service:prod",
      "backend_invoked": false,
      "non_invocation_reason": "dispatch_denied_before_backend_call"
    }

## Illustrative non-execution evidence event

    {
      "evidence_event_id": "evd-20260502-0002",
      "event_type": "agentic_action_not_executed",
      "action_request_id": "arq-20260502-0002",
      "authorization_decision_id": "auz-20260502-0001",
      "dispatch_event_id": "dsp-20260502-0002",
      "backend_verification_id": null,
      "principal_id": "user:ops-engineer-17",
      "agent_instance_id": "agent:ops-maintenance-assistant:session-9f2a",
      "target_resource": "service:svc-billing-export:key:secondary",
      "action": "rotate_service_api_key",
      "outcome": "not_executed",
      "non_execution_reason": "resource_scope_mismatch",
      "failed_boundary": "tool_dispatcher",
      "backend_invoked": false,
      "evidence_sources": [
        "authorization_service",
        "tool_dispatcher",
        "evidence_writer"
      ],
      "evidence_trust_limitations": [
        "backend did not independently verify because dispatch failed before backend invocation",
        "example uses illustrative identifiers",
        "does not imply audit sufficiency"
      ],
      "recorded_at": "2026-05-02T07:13:09Z"
    }

## Reconstruction questions

A reviewer should be able to ask:

| Question | Evidence reference |
| --- | --- |
| What action was attempted? | `action_request_id` |
| What authority was available? | `authorization_decision_id` |
| Why was the action not executed? | `non_execution_reason` |
| Which boundary rejected it? | `failed_boundary` |
| Was the backend invoked? | `backend_invoked` |
| Was this a fail-closed outcome? | dispatch decision and backend non-invocation |
| Did the attempted action exceed scope? | `expected_resource` and `requested_resource` |
| What limitations apply to the evidence? | `evidence_trust_limitations` |

## Expected reviewer interpretation

This example should be interpreted as showing:

- the system did not treat the agent's requested resource as authority,
- the dispatcher compared requested and authorized scope,
- the dispatcher denied execution,
- the backend was not invoked,
- non-execution evidence was recorded,
- and reconstruction can explain why the action did not occur.

This example should not be interpreted as proving:

- full incident response adequacy,
- compliance,
- certification,
- audit sufficiency,
- conformity,
- or production readiness.

## Common non-execution reasons

Future examples may cover:

| Reason | Description |
| --- | --- |
| `missing_authorization_decision` | No authorization decision exists. |
| `decision_expired` | Decision existed but expired. |
| `approval_required` | Approval was required but absent. |
| `resource_scope_mismatch` | Requested resource exceeded the decision. |
| `action_scope_mismatch` | Requested action differed from authorized action. |
| `principal_mismatch` | Principal differed across request and decision. |
| `backend_verification_failed` | Backend rejected or could not verify authority. |
| `evidence_required_unavailable` | Evidence could not be generated for an evidence-required action. |
| `policy_version_invalid` | Decision was made under an unacceptable policy version. |
| `risk_freeze_active` | System freeze or hold prevented action. |

## Relationship to active artifacts

This document does not update the active evidence schema.

A future PR may choose to convert selected non-execution example structures into active examples or schema fixtures. That would require explicit review.

## Non-goals

This document does not:

- update active controls,
- update active schemas,
- update active examples,
- change the current control and assessment baseline,
- assert implementation conformance,
- assert audit sufficiency,
- or claim compliance.

## Acceptance criteria

This planning example is sufficient when:

- a non-execution scenario is described,
- denied dispatch and backend non-invocation are visible,
- non-execution evidence is recorded,
- reconstruction questions are supported,
- evidence limitations are visible,
- and no active baseline change is implied.
