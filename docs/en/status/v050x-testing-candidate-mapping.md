# v0.5.x Testing Candidate Mapping

**Status:** Temporary, non-normative testing candidate mapping document

## Purpose

This document maps the selected v0.5.x testing procedure candidates to likely control areas, evidence expectations, and future artifact impact.

It builds on:

- `docs/en/status/v050x-testing-candidate-selection.md`
- `docs/en/status/v050x-testing-procedure-candidate-matrix.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

This document does not change the v0.4.1 control and assessment baseline.

It does not update the active testing procedure CSV.

It does not update the control catalog.

It does not update the evidence schema.

## Mapping Principles

This mapping is intentionally conservative.

A candidate may relate to several areas, but this document identifies the most likely initial incorporation path.

The goal is to prepare for future testing procedure review without prematurely modifying baseline artifacts.

## Control Area Legend

| Area | Meaning |
| --- | --- |
| AUZ | Authorization, scope binding, reauthorization, and authority freshness. |
| TOOL | Tool dispatch, execution boundary, and backend enforcement. |
| EVD | Evidence generation, preservation, correlation, and reviewability. |
| HUM | Human approval, approval quality, approval fatigue, and approval-to-execution binding. |
| GOV | Governance, policy, review, escalation, and oversight. |
| A2A candidate | Possible future cross-agent authority control refinement. |

These labels are planning aids only.

They do not create new control IDs.

## Evidence Category Legend

| Evidence category | Meaning |
| --- | --- |
| Authorization evidence | Evidence of authority, policy decision, reauthorization, or denial. |
| Scope evidence | Evidence of permitted and requested target, tenant, resource, environment, data, or operation scope. |
| Risk evidence | Evidence of action risk level, escalation, high-impact status, or profile applicability. |
| Revocation evidence | Evidence of revocation, downscoping, expiry, or invalidation. |
| Retry/correlation evidence | Evidence linking retries, split actions, reformulated requests, or later approvals to earlier denial/refusal. |
| Delegation evidence | Evidence of delegation request, delegated capability, receiving-side validation, acceptance/refusal, and downstream delegation. |
| Chain evidence | Evidence that links principal, requesting agent, receiving agent, downstream agents, authorization, execution, and outcome. |
| Budget/resource evidence | Evidence of delegated budget, quota, API, compute, time, resource, or redelegation limit. |
| Approval evidence | Evidence of prompt content, approver, approved action, approval state, and approval validity. |
| Enforcement evidence | Evidence that the execution boundary verified authorization or approval before action. |
| Untrusted input evidence | Evidence of external/untrusted input influence and resulting handling. |

## Principal Context Degradation Mapping

| Candidate ID | Likely control area | Primary evidence category | Secondary evidence category | Future artifact impact |
| --- | --- | --- | --- | --- |
| VTC-PCD-01 | AUZ | Authorization evidence | Scope evidence | Testing procedure candidate for task drift and reauthorization. |
| VTC-PCD-02 | AUZ / TOOL | Scope evidence | Authorization evidence | Testing procedure candidate for scope expansion before execution. |
| VTC-PCD-03 | AUZ / GOV | Risk evidence | Authorization evidence | Testing procedure candidate for risk escalation handling. |
| VTC-PCD-04 | AUZ | Revocation evidence | Enforcement evidence | Testing procedure candidate for revoked or downscoped authority. |
| VTC-PCD-05 | AUZ / EVD | Retry/correlation evidence | Authorization evidence | Testing procedure candidate for retry after denial. |
| VTC-PCD-06 | AUZ / EVD / GOV | Retry/correlation evidence | Risk evidence | Testing procedure candidate for task splitting and aggregate-effect bypass. |
| VTC-PCD-07 | AUZ / EVD | Untrusted input evidence | Authorization evidence | Testing procedure candidate for untrusted input changing principal intent. |

## Cross-Agent Delegation Mapping

| Candidate ID | Likely control area | Primary evidence category | Secondary evidence category | Future artifact impact |
| --- | --- | --- | --- | --- |
| VTC-A2A-01 | AUZ / A2A candidate | Delegation evidence | Authorization evidence | Testing procedure candidate for communication not implying delegation authority. |
| VTC-A2A-02 | AUZ / A2A candidate | Delegation evidence | Scope evidence | Testing procedure candidate for capability-scoped delegation. |
| VTC-A2A-03 | A2A candidate / EVD | Delegation evidence | Chain evidence | Testing procedure candidate for explicit delegation acceptance. |
| VTC-A2A-04 | A2A candidate / EVD | Delegation evidence | Retry/correlation evidence | Testing procedure candidate for refusal propagation. |
| VTC-A2A-05 | AUZ / A2A candidate | Scope evidence | Delegation evidence | Testing procedure candidate for delegated scope mismatch. |
| VTC-A2A-06 | AUZ / A2A candidate | Delegation evidence | Chain evidence | Testing procedure candidate for unauthorized downstream redelegation. |
| VTC-A2A-07 | EVD / A2A candidate | Chain evidence | Delegation evidence | Testing procedure candidate for reconstructable delegation chain evidence. |
| VTC-A2A-08 | GOV / EVD / A2A candidate | Budget/resource evidence | Delegation evidence | Testing procedure candidate for budget and resource propagation. |
| VTC-A2A-09 | AUZ / A2A candidate | Delegation evidence | Enforcement evidence | Testing procedure candidate for receiving-side validation. |

## Approval Quality Mapping

| Candidate ID | Likely control area | Primary evidence category | Secondary evidence category | Future artifact impact |
| --- | --- | --- | --- | --- |
| VTC-APP-01 | HUM / AUZ | Approval evidence | Risk evidence | Testing procedure candidate for approval prompt sufficiency. |
| VTC-APP-02 | HUM / TOOL | Approval evidence | Enforcement evidence | Testing procedure candidate for draft-vs-execute mismatch. |
| VTC-APP-03 | HUM / TOOL / EVD | Approval evidence | Enforcement evidence | Testing procedure candidate for canonical action binding. |
| VTC-APP-04 | HUM / TOOL | Approval evidence | Revocation evidence | Testing procedure candidate for post-approval modification invalidation. |
| VTC-APP-05 | HUM / GOV | Approval evidence | Risk evidence | Testing procedure candidate for blind approval and missing context. |
| VTC-APP-06 | HUM / GOV | Approval evidence | Risk evidence | Testing procedure candidate for batch approval itemization. |
| VTC-APP-07 | HUM / EVD / AUZ | Retry/correlation evidence | Approval evidence | Testing procedure candidate for approval laundering after denial. |
| VTC-APP-08 | HUM / EVD | Approval evidence | Enforcement evidence | Testing procedure candidate for rejecting model-only approval claims. |
| VTC-APP-09 | HUM / TOOL / EVD | Enforcement evidence | Approval evidence | Testing procedure candidate for approval enforcement boundary verification. |

## Cross-Cutting Mapping Themes

| Theme | Candidate IDs | Likely artifact impact |
| --- | --- | --- |
| Authority drift and freshness | VTC-PCD-01, VTC-PCD-02, VTC-PCD-03, VTC-PCD-04 | AUZ testing refinement, possible assessment profile relevance. |
| Denial and bypass resistance | VTC-PCD-05, VTC-PCD-06, VTC-APP-07 | Testing refinement plus evidence correlation expectations. |
| Untrusted input influence | VTC-PCD-07 | AUZ/EVD testing refinement and possible evidence expectation candidate. |
| Cross-agent validation | VTC-A2A-01, VTC-A2A-02, VTC-A2A-05, VTC-A2A-09 | AUZ/A2A control refinement candidates and testing candidates. |
| Cross-agent workflow state | VTC-A2A-03, VTC-A2A-04 | A2A/EVD testing candidates. |
| Cross-agent accountability | VTC-A2A-06, VTC-A2A-07, VTC-A2A-08 | EVD/A2A testing candidates and possible schema candidates. |
| Approval quality and binding | VTC-APP-01, VTC-APP-02, VTC-APP-03, VTC-APP-04, VTC-APP-05 | HUM/AUZ/TOOL testing candidates and possible HUM refinement. |
| Approval evidence and enforcement | VTC-APP-06, VTC-APP-08, VTC-APP-09 | HUM/EVD/TOOL testing candidates and possible schema candidates. |

## Evidence Expectation Candidates

The following evidence expectations recur across the candidate set.

| Evidence expectation | Appears in | Possible future use |
| --- | --- | --- |
| Original authorized intent | VTC-PCD-01, VTC-PCD-07 | Evidence expectation candidate; possible schema consideration. |
| Requested vs. authorized scope | VTC-PCD-02, VTC-A2A-05 | Testing criterion and evidence expectation candidate. |
| Risk escalation indicator | VTC-PCD-03, VTC-APP-01, VTC-APP-05 | Assessment profile and evidence expectation candidate. |
| Revocation or downscope signal | VTC-PCD-04, VTC-APP-04 | Evidence expectation candidate. |
| Denial and retry correlation | VTC-PCD-05, VTC-PCD-06, VTC-APP-07 | Evidence expectation and testing criterion candidate. |
| Delegated capability and receiving-side validation | VTC-A2A-01, VTC-A2A-02, VTC-A2A-09 | Cross-agent authority evidence candidate. |
| Acceptance/refusal state | VTC-A2A-03, VTC-A2A-04 | Cross-agent workflow evidence candidate. |
| Delegation chain linkage | VTC-A2A-06, VTC-A2A-07 | Evidence/schema candidate. |
| Budget/resource constraint | VTC-A2A-08 | Evidence/schema and implementation guidance candidate. |
| Approval prompt content | VTC-APP-01, VTC-APP-05 | Approval evidence expectation candidate. |
| Approved vs. executed canonical action | VTC-APP-02, VTC-APP-03, VTC-APP-04 | Approval-to-execution evidence candidate. |
| Approval evidence source | VTC-APP-08 | Evidence-source and model-output rejection candidate. |
| Execution boundary enforcement check | VTC-APP-09 | TOOL/EVD evidence expectation candidate. |

## Recommended Next Step

The next step should be a small review document or PR that identifies which of these candidates are ready for draft pass/fail criteria.

That work should still avoid editing active testing procedure CSV until:

- target control area is accepted;
- evidence expectations are stable;
- pass/fail language is clear;
- not-applicable criteria are defined;
- profile applicability is clear.

## Non-Goals

This document does not:

- update testing procedure CSV;
- add testing procedure rows;
- create executable fixtures;
- add control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- close #161, #163, or #167;
- claim that all candidates must become normative tests.

It is a temporary mapping document for the v0.5.x incorporation phase.
