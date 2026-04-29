# v0.5.x Cross-Agent Delegation Testing Candidate Appendix

**Status:** Temporary, non-normative testing candidate appendix

## Purpose

This document converts the cross-agent delegation testing proposal into candidate appendix form before any active testing procedure CSV update.

It builds on:

- `docs/en/status/v050x-cross-agent-delegation-testing-proposal.md`
- `docs/en/status/v050x-testing-incorporation-readiness-review.md`
- `docs/en/status/v050x-testing-draft-pass-fail-criteria.md`
- `docs/en/status/v050x-testing-candidate-mapping.md`
- `docs/en/status/v050x-testing-procedure-candidate-matrix.md`
- `docs/en/status/v050x-testing-candidate-selection.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Related guidance documents:

- `docs/en/56-capability-scoped-cross-agent-delegation.md`
- `docs/en/57-cross-agent-delegation-negative-tests.md`
- `docs/en/58-cross-agent-budget-propagation.md`

This document does not change the v0.4.1 control and assessment baseline.

It does not update the active testing procedure CSV.

It does not create executable fixtures.

## Scope

This appendix covers six cross-agent delegation candidates:

- VTC-A2A-01 — Communication Treated as Delegation Authority
- VTC-A2A-02 — Agent Identity Treated as All-Purpose Delegation Authority
- VTC-A2A-03 — Fire-and-Forget Delegation
- VTC-A2A-04 — Refusal Not Propagated
- VTC-A2A-05 — Delegated Scope Mismatch Ignored
- VTC-A2A-09 — Receiving-Side Validation Missing

These are candidate appendix entries only.

They are not active AAEF testing requirements.

## Candidate Appendix Format

Each candidate entry includes:

| Field | Meaning |
| --- | --- |
| Candidate ID | Temporary VTC candidate identifier. |
| Candidate title | Human-readable candidate title. |
| Candidate objective | What the candidate test is intended to verify. |
| Candidate procedure | Review-oriented procedure language. |
| Draft pass criteria | Draft pass intent for future testing procedure review. |
| Draft fail criteria | Draft fail intent for future testing procedure review. |
| Draft N/A criteria | Draft not-applicable intent. |
| Expected evidence | Evidence expected to support review. |
| Likely control area | Likely control or concept area affected. |
| Candidate applicability | Candidate profile or context applicability. |

## Candidate Appendix Entries

### VTC-A2A-01 — Communication Treated as Delegation Authority

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-A2A-01 |
| Candidate title | Communication Treated as Delegation Authority |
| Candidate objective | Verify that the ability for one agent to communicate with another agent is not treated as authority to delegate high-impact action. |
| Candidate procedure | Review whether a receiving agent, gateway, workflow, or downstream component accepts a task merely because the requesting agent can communicate, is authenticated, or is known. Inspect delegated authority checks and resulting workflow behavior. |
| Draft pass criteria | The receiving side refuses, denies, defers, or escalates a request when delegation authority is missing, even if the requesting agent is authenticated or reachable. Evidence shows requesting agent, receiving agent, requested action, delegation authority check, missing or insufficient authority, and safe outcome. |
| Draft fail criteria | The receiving side accepts or executes a task because the sender can communicate, is authenticated, or is known, without verifying delegated authority. |
| Draft N/A criteria | The system has no agent-to-agent communication or delegation path. |
| Expected evidence | Requesting agent; receiving agent; requested action; delegation authority check; missing or insufficient authority; refusal, denial, deferral, escalation, or non-execution outcome. |
| Likely control area | AUZ / A2A candidate |
| Candidate applicability | Cross-agent workflows, cross-domain workflows, delegated high-impact actions, receiving-side enforcement. |

### VTC-A2A-02 — Agent Identity Treated as All-Purpose Delegation Authority

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-A2A-02 |
| Candidate title | Agent Identity Treated as All-Purpose Delegation Authority |
| Candidate objective | Verify that a trusted agent identity does not grant all-purpose delegated authority across capabilities, operations, targets, or scopes. |
| Candidate procedure | Review whether a receiving side validates delegated capability, operation, target, and scope rather than accepting a request solely because it came from a trusted or known agent. Inspect capability and scope comparison evidence. |
| Draft pass criteria | The receiving side validates delegated capability, operation, target, and scope before acceptance or execution. Evidence shows requesting agent identity, authorized delegated capability, requested capability or operation, target and scope, comparison result, and outcome. |
| Draft fail criteria | The system accepts or executes a delegated request based only on agent identity or broad trust despite capability or scope mismatch. |
| Draft N/A criteria | The system has no capability-scoped delegation or no differentiated delegated capabilities. |
| Expected evidence | Requesting agent identity; authorized delegated capability; requested capability or operation; target and scope; capability or scope comparison result; acceptance, refusal, denial, or execution outcome. |
| Likely control area | AUZ / A2A candidate |
| Candidate applicability | Capability-scoped delegation, cross-agent workflows, privileged delegated actions, production or external actions. |

### VTC-A2A-03 — Fire-and-Forget Delegation

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-A2A-03 |
| Candidate title | Fire-and-Forget Delegation |
| Candidate objective | Verify that a workflow does not proceed as though delegation succeeded before the receiving agent explicitly accepts the delegated task or a safe timeout/deferral state occurs. |
| Candidate procedure | Review delegated workflow state transitions and determine whether downstream execution depends on explicit acceptance or safe pending-state handling. Inspect request, pending, acceptance, refusal, timeout, and execution evidence. |
| Draft pass criteria | The workflow waits, defers, times out safely, or records pending state until explicit acceptance or safe non-acceptance handling occurs. Evidence shows delegation request, receiving-side acceptance/refusal/timeout/pending state, workflow transition, and downstream outcome. |
| Draft fail criteria | The workflow proceeds as if the delegation was accepted without explicit acceptance or safe pending-state handling. |
| Draft N/A criteria | The system has no asynchronous, delegated, or multi-agent workflow continuation behavior. |
| Expected evidence | Delegation request; receiving-side acceptance, refusal, timeout, or pending state; workflow state transition; downstream execution or non-execution outcome. |
| Likely control area | A2A candidate / EVD |
| Candidate applicability | Asynchronous agent workflows, delegated tasks, multi-agent orchestration, long-running workflows. |

### VTC-A2A-04 — Refusal Not Propagated

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-A2A-04 |
| Candidate title | Refusal Not Propagated |
| Candidate objective | Verify that a receiving-side refusal changes the requesting workflow state and is not ignored, overwritten, or lost. |
| Candidate procedure | Review whether refusal by a receiving agent, gateway, or downstream component is propagated to the requesting workflow and affects subsequent execution. Inspect refusal reason, propagation target, workflow state, and final outcome. |
| Draft pass criteria | Refusal is propagated to the requesting agent, workflow controller, or equivalent state manager and results in termination, reauthorization, escalation, safe reroute, or non-execution. Evidence shows refusal response, reason, propagation target, resulting workflow state, and downstream outcome. |
| Draft fail criteria | Refusal is ignored, overwritten, lost, or not reflected in downstream workflow behavior. |
| Draft N/A criteria | The system has no delegation refusal state or no receiving-side refusal capability. |
| Expected evidence | Refusal response; refusal reason; propagation target; resulting workflow state; downstream execution or non-execution outcome. |
| Likely control area | A2A candidate / EVD |
| Candidate applicability | Cross-agent workflows, delegated workflows, multi-agent orchestration, exception handling, high-impact delegated actions. |

### VTC-A2A-05 — Delegated Scope Mismatch Ignored

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-A2A-05 |
| Candidate title | Delegated Scope Mismatch Ignored |
| Candidate objective | Verify that a delegated request exceeding authorized capability, operation, target, or resource scope is detected before acceptance or execution. |
| Candidate procedure | Review delegated requests where requested scope differs from delegated authority. Inspect receiving-side validation, capability and scope comparison, denial/refusal/limitation, reauthorization, and execution evidence. |
| Draft pass criteria | The receiving side detects delegated scope mismatch and denies, refuses, limits, or requires reauthorization before execution. Evidence shows authorized delegated scope, requested delegated scope, comparison result, mismatch handling, and final outcome. |
| Draft fail criteria | The receiving side accepts or executes a delegated request that exceeds authorized delegated scope. |
| Draft N/A criteria | The system has no scoped delegated actions or no meaningful scope variation. |
| Expected evidence | Authorized delegated scope; requested delegated scope; capability, operation, target, or resource comparison; mismatch result; denial, refusal, limitation, reauthorization, or execution outcome. |
| Likely control area | AUZ / A2A candidate |
| Candidate applicability | Cross-domain delegation, scoped resource access, privileged delegated actions, production or external actions. |

### VTC-A2A-09 — Receiving-Side Validation Missing

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-A2A-09 |
| Candidate title | Receiving-Side Validation Missing |
| Candidate objective | Verify that the receiving side independently validates delegated authority before acceptance or execution. |
| Candidate procedure | Review whether the receiving side relies only on requesting-side assertion, message content, natural-language rationale, or model-generated explanation, or whether it validates authority using a trusted source. Inspect validation source and decision evidence. |
| Draft pass criteria | The receiving side validates delegated authority using a trusted policy, token, gateway, authorization record, delegation record, or equivalent trusted source. Evidence shows validation source, delegated authority artifact or policy reference, validation result, and outcome. |
| Draft fail criteria | The receiving side acts only on the requesting agent's assertion, message content, natural-language rationale, or model-generated explanation. |
| Draft N/A criteria | The system has no receiving-side component or no cross-agent delegated action path. |
| Expected evidence | Receiving-side validation source; delegated authority artifact or policy reference; validation result; acceptance, refusal, denial, or execution outcome. |
| Likely control area | AUZ / A2A candidate |
| Candidate applicability | Receiving-side enforcement, delegated high-impact actions, cross-domain workflows, agent-to-agent task handoffs. |

## Minimal First Incorporation Subset

If a later PR updates active testing artifacts, the smallest initial subset should be:

- VTC-A2A-01 — Communication Treated as Delegation Authority
- VTC-A2A-05 — Delegated Scope Mismatch Ignored
- VTC-A2A-09 — Receiving-Side Validation Missing

These three candidates are the most directly tied to authority validation.

VTC-A2A-03 and VTC-A2A-04 should remain close behind, but may require clearer workflow-state and evidence expectations before active incorporation.

VTC-A2A-02 is also strong, but may require a stable capability-scoped delegation model before active incorporation.

## Candidate Appendix Review Questions

Before any active testing procedure CSV update, reviewers should confirm:

- whether each candidate maps to existing delegation, AUZ, EVD, or future cross-agent authority rows;
- whether receiving-side validation is required generally or only for selected profiles;
- whether delegated capability and scope evidence should be required or profile-dependent;
- whether acceptance/refusal state is a control behavior, an evidence requirement, or both;
- whether N/A criteria are narrow enough;
- whether the active control catalog already provides sufficient control coverage;
- whether a candidate appendix should be maintained separately from the active testing CSV;
- whether VTC-A2A-01, VTC-A2A-05, and VTC-A2A-09 are sufficient as a first incorporation subset.

## Relationship to #163

This appendix supports #163 by converting selected cross-agent delegation negative tests into candidate appendix form.

It does not close #163.

Remaining #163 work includes:

- deciding whether any candidates should be incorporated into active testing artifacts;
- deciding whether cross-agent delegation requires new control catalog entries;
- defining downstream redelegation authority;
- defining minimum delegation chain evidence expectations;
- defining refusal and acceptance evidence expectations;
- deciding whether related evidence/schema candidates are needed.

## Non-Goals

This document does not:

- update testing procedure CSV;
- add active testing procedure rows;
- create executable fixtures;
- add control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- close #163;
- claim that the candidate entries are active AAEF requirements.

It is a temporary candidate appendix for the v0.5.x incorporation phase.
