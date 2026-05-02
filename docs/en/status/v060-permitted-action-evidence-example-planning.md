# AAEF v0.6.0 Permitted Action Evidence Example Planning

Status: Evidence example planning  
Related roadmap: #241  
Related implementation reference: `docs/en/status/v060-implementation-reference-pattern-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document provides a non-normative planning example of evidence for a permitted agentic action.

The purpose is to illustrate how an AAEF-style implementation may connect:

- action request,
- authorization decision,
- dispatch enforcement,
- backend relying-party verification,
- execution result,
- evidence generation,
- and reconstruction.

This document is illustrative planning material. It does not update active schemas, examples, controls, mappings, testing procedures, assessment artifacts, or the current control and assessment baseline.

## Scenario

A support operations agent proposes a bounded production action:

> Rotate a production service API key for service `svc-billing-export` after a human-approved maintenance request.

The action is permitted only if:

- the principal is authorized for the maintenance request,
- the requested service matches the approved change,
- the action is limited to key rotation,
- the change window is active,
- the backend verifies the authorization decision,
- and evidence can be generated.

## Actors and components

| Actor or component | Role |
| --- | --- |
| Principal | Operations engineer responsible for the maintenance request. |
| Agent runtime | Produces the proposed key-rotation action. |
| Action request builder | Converts the proposed action into a structured request. |
| Authorization decision point | Evaluates policy, principal, scope, and change-window constraints. |
| Tool dispatcher | Verifies the authorization decision before invoking the backend. |
| Backend relying party | Independently verifies the decision before rotating the key. |
| Evidence writer | Emits structured evidence outside the model-controlled path where feasible. |
| Evidence store | Preserves evidence for review and reconstruction. |

## Evidence chain

The evidence chain should allow a reviewer to answer:

1. What action was requested?
2. Who was the principal?
3. Which agent proposed the action?
4. What authority was granted?
5. Which policy version was used?
6. Which dispatcher enforced the decision?
7. Which backend verified and executed the action?
8. What evidence proves execution?
9. What limitations apply to the evidence?

## Illustrative action request

    {
      "action_request_id": "arq-20260502-0001",
      "requested_action": "rotate_service_api_key",
      "target_resource": "service:svc-billing-export:key:primary",
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
          "source_id": "chatmsg-7781",
          "trusted_for_authority": false
        }
      ],
      "untrusted_input_present": true,
      "impact_level": "high",
      "requested_scope": {
        "action": "rotate",
        "service": "svc-billing-export",
        "environment": "production",
        "key_slot": "primary"
      },
      "requested_time_window": {
        "not_before": "2026-05-02T07:00:00Z",
        "not_after": "2026-05-02T08:00:00Z"
      },
      "reason_code": "approved_maintenance_key_rotation",
      "request_hash": "sha256:example-request-hash"
    }

## Illustrative authorization decision

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
      "trusted_inputs_used": [
        "change_ticket:chg-20260502-1042",
        "principal_directory:user:ops-engineer-17",
        "maintenance_window:mw-20260502-07"
      ],
      "untrusted_inputs_excluded": [
        "chatmsg-7781"
      ],
      "approver_id": "user:change-approver-04",
      "approval_evidence_ref": "approval:chg-20260502-1042:approval-2",
      "decision_hash": "sha256:example-decision-hash"
    }

## Illustrative dispatch enforcement result

    {
      "dispatch_event_id": "dsp-20260502-0001",
      "authorization_decision_id": "auz-20260502-0001",
      "action_request_id": "arq-20260502-0001",
      "dispatcher_id": "dispatcher:prod-tool-gateway-01",
      "dispatch_decision": "allowed",
      "checks": {
        "decision_exists": "pass",
        "decision_not_expired": "pass",
        "request_binding_matches": "pass",
        "principal_matches": "pass",
        "action_matches": "pass",
        "resource_matches": "pass",
        "scope_constraints_match": "pass",
        "policy_version_accepted": "pass",
        "evidence_required": "pass"
      },
      "dispatch_time": "2026-05-02T07:10:18Z"
    }

## Illustrative backend verification result

    {
      "backend_verification_id": "bkv-20260502-0001",
      "backend_id": "backend:key-management-service:prod",
      "authorization_decision_id": "auz-20260502-0001",
      "action_request_id": "arq-20260502-0001",
      "verification_result": "verified",
      "verified_fields": [
        "principal_id",
        "authorized_action",
        "authorized_resource",
        "authorized_scope",
        "expires_at",
        "policy_version",
        "decision_hash"
      ],
      "execution_result": "executed",
      "execution_reference": "kms-event-20260502-88120",
      "execution_time": "2026-05-02T07:10:24Z"
    }

## Illustrative evidence event

    {
      "evidence_event_id": "evd-20260502-0001",
      "event_type": "agentic_action_executed",
      "action_request_id": "arq-20260502-0001",
      "authorization_decision_id": "auz-20260502-0001",
      "dispatch_event_id": "dsp-20260502-0001",
      "backend_verification_id": "bkv-20260502-0001",
      "principal_id": "user:ops-engineer-17",
      "agent_instance_id": "agent:ops-maintenance-assistant:session-9f2a",
      "target_resource": "service:svc-billing-export:key:primary",
      "action": "rotate_service_api_key",
      "outcome": "executed",
      "evidence_sources": [
        "authorization_service",
        "tool_dispatcher",
        "backend_key_management_service",
        "evidence_writer"
      ],
      "evidence_trust_limitations": [
        "example uses illustrative identifiers",
        "does not prove hardware-rooted evidence integrity",
        "does not imply audit sufficiency"
      ],
      "recorded_at": "2026-05-02T07:10:29Z"
    }

## Reconstruction questions

A reviewer should be able to ask:

| Question | Evidence reference |
| --- | --- |
| What action was requested? | `action_request_id` and action request record |
| Who was the principal? | `principal_id` in request, decision, dispatch, and evidence |
| Did a policy decision permit the action? | `authorization_decision_id` |
| Was untrusted input used as authority? | `trusted_inputs_used` and `untrusted_inputs_excluded` |
| Did the dispatcher enforce the decision? | `dispatch_event_id` and dispatch checks |
| Did the backend independently verify authority? | `backend_verification_id` |
| Was the action executed? | backend execution reference and evidence event |
| What are the evidence limitations? | `evidence_trust_limitations` |

## Expected reviewer interpretation

This example should be interpreted as showing:

- model output did not itself authorize the key rotation,
- authorization was represented as a separate decision artifact,
- dispatch enforcement checked the artifact before execution,
- backend verification occurred before the action,
- evidence linked request, decision, dispatch, backend verification, and execution,
- and evidence limitations were recorded.

This example should not be interpreted as proving:

- compliance,
- certification,
- audit sufficiency,
- complete mitigation,
- conformity,
- or production readiness.

## Relationship to active artifacts

This document does not update the active evidence schema.

A future PR may choose to convert selected example structures into active examples or schema fixtures. That would require explicit review.

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

- a permitted action scenario is described,
- action request, authorization decision, dispatch, backend verification, and evidence are linked,
- reconstruction questions are supported,
- evidence limitations are visible,
- and no active baseline change is implied.
