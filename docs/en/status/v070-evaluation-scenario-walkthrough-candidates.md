# v0.7.0 Evaluation Scenario Walkthrough Candidates

## Status

This is a v0.7.0 planning artifact for candidate evaluation scenario walkthroughs.

This document is:

- a planning artifact for #319;
- a follow-up to the v0.7.0 Evaluation Scenario Walkthrough Planning artifact;
- an illustrative scenario candidate set;
- non-normative unless a later release explicitly promotes content into active guidance.

This document is not:

- an empirical evaluation result;
- an implementation test result;
- a production-readiness claim;
- an implementation conformance claim;
- a certification scheme;
- a compliance claim;
- a conformity claim;
- an audit sufficiency claim;
- a legal sufficiency claim;
- an external framework equivalence claim;
- a peer-review claim;
- a change to the current AAEF control and assessment baseline.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

The purpose of this document is to define a small initial set of scenario walkthrough candidates for v0.7.0 evaluation-readiness work.

The scenarios are intentionally minimal.

They are designed to test whether reviewers can follow:

- an action request;
- the authority requirement;
- the authorization decision;
- the dispatch decision;
- backend verification expectations;
- execution or non-execution outcome;
- evidence relationships;
- reconstruction questions;
- claim boundaries.

The purpose is reviewability, not proof.

## Relationship to prior v0.7.0 artifacts

This artifact follows:

- `docs/en/status/v070-planning-entrypoint.md`
- `docs/en/status/v070-evaluation-readiness-planning.md`
- `docs/en/status/v070-evaluation-scenario-walkthrough-planning.md`

It contributes to:

- #317 — v0.7.0 roadmap
- #319 — Evaluation Readiness track

The prior scenario walkthrough planning artifact defined how walkthroughs should be structured. This document applies that structure to two candidate scenarios.

## Candidate set overview

The initial candidate set includes two scenarios.

| Candidate | Scenario type | Purpose |
| --- | --- | --- |
| Candidate A | Permitted action with reviewable authority chain | Illustrate a positive review path where authority, dispatch, backend verification, execution, and evidence align. |
| Candidate B | Non-execution with reviewable denial or block reason | Illustrate a negative review path where an action does not execute and the non-execution outcome is still reviewable. |

These candidates are not exhaustive.

They are intended as a first reviewable pair before adding negative test sets, reconstruction exercises, or evaluation fixtures.

## Candidate A: Permitted action with reviewable authority chain

### Scenario summary

An agent proposes a high-impact administrative action that would update a production configuration value.

The model output suggests the action, but the model output is treated only as an action request. It is not treated as authority.

The action proceeds only if:

- the action request is bound to a principal, scope, action type, parameters, and expiration;
- an authorization decision allows the requested action;
- the dispatch decision matches the authorization decision;
- backend verification confirms the authorization binding before effectful execution;
- evidence records allow later reconstruction.

### Actor and role context

| Role | Candidate responsibility |
| --- | --- |
| Model or agent planner | Generates or proposes the action request. |
| Agent runtime | Packages the request for authorization and dispatch review. |
| Authorization decision point | Evaluates policy, scope, principal, action, parameters, and expiration. |
| Tool dispatcher | Allows or denies dispatch based on authorization decision. |
| Backend service | Performs relying-party verification before effectful execution. |
| Evidence component | Records action-bound evidence for reconstruction. |
| Reviewer | Reconstructs whether the action was requested, authorized, dispatched, verified, executed, and evidenced. |

### Action request

Candidate action request fields:

| Field | Candidate value |
| --- | --- |
| `action_request_id` | `arq-v070-candidate-a-0001` |
| `principal_id` | `principal-operator-review-demo` |
| `action_type` | `production_configuration_update` |
| `target_resource` | `service-config/example-feature-flag` |
| `requested_change` | `set evaluation_mode to enabled` |
| `model_output_influence` | `model suggested the configuration update as part of a maintenance workflow` |
| `high_impact` | `true` |

### Authority requirement

The walkthrough should ask whether the action requires independent authorization before execution.

Candidate authority requirement:

- production configuration updates require explicit authorization;
- model output cannot authorize the change;
- the action must be bound to a principal, action type, target resource, parameters, and expiration;
- the authorization decision must be independently reviewable.

### Authorization decision expectation

Candidate authorization fields:

| Field | Candidate value |
| --- | --- |
| `authorization_decision_id` | `auz-v070-candidate-a-0001` |
| `decision` | `allow` |
| `policy_version` | `policy-v070-evaluation-candidate` |
| `bound_action_request_id` | `arq-v070-candidate-a-0001` |
| `bound_action_type` | `production_configuration_update` |
| `bound_target_resource` | `service-config/example-feature-flag` |
| `expires_at` | illustrative timestamp only |
| `decision_basis` | `principal and scope permit this illustrative action` |

Review question:

- Does the authorization decision bind the same action that is later dispatched?

### Dispatch decision expectation

Candidate dispatch fields:

| Field | Candidate value |
| --- | --- |
| `dispatch_decision_id` | `dsp-v070-candidate-a-0001` |
| `decision` | `allow_dispatch` |
| `bound_authorization_decision_id` | `auz-v070-candidate-a-0001` |
| `bound_action_request_id` | `arq-v070-candidate-a-0001` |
| `dispatch_reason` | `authorization decision permits the bound action before expiration` |

Review question:

- Does dispatch rely on the authorization decision rather than on model output?

### Backend verification expectation

Candidate backend verification fields:

| Field | Candidate value |
| --- | --- |
| `backend_verification_id` | `bev-v070-candidate-a-0001` |
| `verification_result` | `verified` |
| `bound_authorization_decision_id` | `auz-v070-candidate-a-0001` |
| `bound_dispatch_decision_id` | `dsp-v070-candidate-a-0001` |
| `verification_reason` | `backend confirmed action binding before applying the illustrative configuration update` |

Review question:

- Can the backend service independently verify the authorization binding before execution?

### Execution outcome

Candidate outcome:

| Field | Candidate value |
| --- | --- |
| `execution_outcome` | `executed` |
| `execution_reason` | `authorization, dispatch, and backend verification aligned` |
| `effectful_execution` | `true` |

Review question:

- Is the execution outcome traceable without relying on the model's self-report?

### Evidence and reconstruction

Candidate evidence relationship chain:

1. `action_request_id`: `arq-v070-candidate-a-0001`
2. `authorization_decision_id`: `auz-v070-candidate-a-0001`
3. `dispatch_decision_id`: `dsp-v070-candidate-a-0001`
4. `backend_verification_id`: `bev-v070-candidate-a-0001`
5. `evidence_event_id`: `evd-v070-candidate-a-0001`
6. outcome: `executed`

A reviewer should be able to explain:

- what was requested;
- what authority was required;
- why the action was allowed;
- whether dispatch matched authorization;
- whether backend verification occurred;
- whether evidence supports reconstruction;
- what the walkthrough does not prove.

### Candidate allowed conclusion

This walkthrough may support the following limited conclusion:

> The candidate illustrates how a permitted high-impact action could be reviewed through an action-bound authority, dispatch, backend verification, and evidence chain.

### Candidate forbidden conclusions

This walkthrough must not claim:

- implementation conformance;
- production readiness;
- empirical validation;
- real-world safety;
- audit sufficiency;
- legal sufficiency;
- compliance;
- certification;
- conformity;
- external framework equivalence;
- complete threat coverage;
- mitigation completeness.

## Candidate B: Non-execution with reviewable denial or block reason

### Scenario summary

An agent proposes a high-impact administrative action that would delete an audit log export.

The model output suggests the action, but model output is treated only as an action request. It is not treated as authority.

The action does not execute because authorization is denied or dispatch is blocked.

The non-execution outcome remains reviewable through evidence.

### Actor and role context

| Role | Candidate responsibility |
| --- | --- |
| Model or agent planner | Generates or proposes the action request. |
| Agent runtime | Packages the request for authorization and dispatch review. |
| Authorization decision point | Denies or constrains the action based on policy and scope. |
| Tool dispatcher | Blocks dispatch when authorization is denied or invalid. |
| Backend service | Is not invoked when dispatch is blocked. |
| Evidence component | Records non-execution evidence and denial or block reason. |
| Reviewer | Reconstructs why the action did not execute. |

### Action request

Candidate action request fields:

| Field | Candidate value |
| --- | --- |
| `action_request_id` | `arq-v070-candidate-b-0001` |
| `principal_id` | `principal-operator-review-demo` |
| `action_type` | `audit_log_export_delete` |
| `target_resource` | `audit-exports/example-export` |
| `requested_change` | `delete audit export` |
| `model_output_influence` | `model suggested deleting an export as part of cleanup` |
| `high_impact` | `true` |

### Authority requirement

The walkthrough should ask whether deleting audit evidence requires strong authorization.

Candidate authority requirement:

- audit evidence deletion requires explicit authorization;
- model output cannot authorize deletion;
- missing, expired, mismatched, or denied authorization should prevent dispatch;
- non-execution should be reviewable.

### Authorization decision expectation

Candidate authorization fields:

| Field | Candidate value |
| --- | --- |
| `authorization_decision_id` | `auz-v070-candidate-b-0001` |
| `decision` | `deny` |
| `policy_version` | `policy-v070-evaluation-candidate` |
| `bound_action_request_id` | `arq-v070-candidate-b-0001` |
| `bound_action_type` | `audit_log_export_delete` |
| `bound_target_resource` | `audit-exports/example-export` |
| `denial_reason` | `principal lacks authority to delete audit export` |

Review question:

- Is the denial reason explicit enough for later review?

### Dispatch decision expectation

Candidate dispatch fields:

| Field | Candidate value |
| --- | --- |
| `dispatch_decision_id` | `dsp-v070-candidate-b-0001` |
| `decision` | `deny_dispatch` |
| `bound_authorization_decision_id` | `auz-v070-candidate-b-0001` |
| `bound_action_request_id` | `arq-v070-candidate-b-0001` |
| `dispatch_reason` | `authorization decision denied the requested action` |

Review question:

- Did the dispatcher block the action because the authorization decision denied it?

### Backend verification expectation

Candidate backend verification fields:

| Field | Candidate value |
| --- | --- |
| `backend_verification_id` | `null` |
| `verification_result` | `not_invoked` |
| `verification_reason` | `backend was not invoked because dispatch was denied` |

Review question:

- Is a `null` backend verification identifier legitimate because the backend was not invoked, or is it an evidence gap?

### Execution outcome

Candidate outcome:

| Field | Candidate value |
| --- | --- |
| `execution_outcome` | `not_executed` |
| `non_execution_reason` | `authorization_denied_and_dispatch_blocked` |
| `effectful_execution` | `false` |

Review question:

- Can the reviewer reconstruct non-execution without inventing backend evidence?

### Evidence and reconstruction

Candidate evidence relationship chain:

1. `action_request_id`: `arq-v070-candidate-b-0001`
2. `authorization_decision_id`: `auz-v070-candidate-b-0001`
3. `dispatch_decision_id`: `dsp-v070-candidate-b-0001`
4. `backend_verification_id`: `null`
5. `evidence_event_id`: `evd-v070-candidate-b-0001`
6. outcome: `not_executed`
7. non-execution reason: `authorization_denied_and_dispatch_blocked`

A reviewer should be able to explain:

- what was requested;
- why authority was required;
- why authorization was denied;
- why dispatch was blocked;
- why backend verification is absent;
- why execution did not occur;
- what evidence supports that explanation;
- what the walkthrough does not prove.

### Candidate allowed conclusion

This walkthrough may support the following limited conclusion:

> The candidate illustrates how a denied or blocked high-impact action could remain reviewable as a non-execution outcome.

### Candidate forbidden conclusions

This walkthrough must not claim:

- complete prevention coverage;
- complete threat mitigation;
- implementation conformance;
- production readiness;
- empirical validation;
- real-world safety;
- audit sufficiency;
- legal sufficiency;
- compliance;
- certification;
- conformity;
- external framework equivalence.

## Cross-scenario review questions

A reviewer should compare Candidate A and Candidate B using the following questions.

| Review question | Candidate A | Candidate B |
| --- | --- | --- |
| Was model output treated as authority? | Should be no. | Should be no. |
| Was an action request identified? | Should be yes. | Should be yes. |
| Was authority required? | Should be yes. | Should be yes. |
| Was authorization decision-bound? | Should be yes. | Should be yes. |
| Did dispatch follow authorization? | Should be yes. | Should be yes. |
| Was backend invoked appropriately? | Should be yes. | Should be no, because dispatch was denied. |
| Is execution or non-execution reviewable? | Should be yes. | Should be yes. |
| Can the reviewer reconstruct without model self-report? | Should be yes. | Should be yes. |
| Are claim boundaries explicit? | Should be yes. | Should be yes. |

## Use in future evaluation work

Future evaluation artifacts may use these candidates as starting points for:

- walkthrough candidate refinement;
- negative test candidate selection;
- reconstruction exercise planning;
- evidence relationship review;
- persona review;
- future fixture design.

Future artifacts should not treat these candidates as:

- empirical tests;
- production tests;
- conformance tests;
- certification criteria;
- compliance mappings;
- audit procedures;
- proof of control effectiveness.

## Acceptance checklist for these candidates

These scenario candidates are acceptable for planning use if:

- they remain illustrative;
- they include one permitted action case;
- they include one non-execution case;
- model output is not treated as authority;
- authorization, dispatch, backend verification, and evidence relationships are reviewable;
- non-execution is represented as a first-class outcome;
- null backend identifiers are explained when backend is not invoked;
- claim boundaries are explicit;
- active baseline impact is excluded.

## Non-goals

This candidate artifact does not:

- add executable tests;
- add scenario fixtures;
- add JSON examples;
- add empirical results;
- validate a deployed system;
- update active controls;
- update the evidence schema;
- update assessment artifacts;
- update testing procedures;
- create a conformance test suite;
- claim implementation conformance;
- claim production readiness;
- claim certification;
- claim compliance;
- claim conformity;
- claim audit sufficiency;
- claim legal sufficiency;
- claim external-framework equivalence;
- claim peer review;
- claim complete threat coverage;
- claim mitigation completeness.

## Recommended next step

The recommended next step for #319 is either:

1. create an evaluation artifact inventory that identifies which current repository artifacts can be reviewed under defined limits; or
2. add a narrow reconstruction exercise planning artifact based on these two candidates.

The next step should remain documentation-only unless a later issue explicitly scopes fixture or validator work.
