# v0.5.x Cross-Agent Delegation Testing CSV Refinement Proposal

**Status:** Temporary, non-normative CSV refinement proposal

## Purpose

This document records the proposed path for incorporating cross-agent delegation testing candidates into active testing artifacts.

It follows:

- `docs/en/status/v050x-cross-agent-delegation-testing-candidate-appendix.md`
- `docs/en/status/v050x-cross-agent-delegation-testing-proposal.md`
- `docs/en/status/v050x-testing-incorporation-readiness-review.md`
- `docs/en/status/v050x-testing-draft-pass-fail-criteria.md`
- `docs/en/status/v050x-testing-candidate-mapping.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Related guidance documents:

- `docs/en/56-capability-scoped-cross-agent-delegation.md`
- `docs/en/57-cross-agent-delegation-negative-tests.md`
- `docs/en/58-cross-agent-budget-propagation.md`

This document does not change the v0.4.1 control and assessment baseline.

It does not update the active testing procedure CSV.

It does not create executable fixtures.

## Current Testing CSV Constraint

The active testing procedure draft is:

- `assessment/aaef-testing-procedures-v0.4-draft.csv`

The current testing procedure validator expects testing procedure rows to match the control catalog one-to-one.

Therefore, temporary `VTC-A2A-*` candidate IDs should not be added directly to the active testing procedure CSV unless a later change explicitly updates the testing model, validator, and related documentation.

## Existing Active Coverage

The current active control catalog and testing procedure CSV already include several cross-agent and delegation-oriented rows.

The most relevant active rows are:

- `AAEF-DEL-01` — delegated authority shall not exceed the authority held by the delegating party;
- `AAEF-DEL-02` — delegations shall include constraints such as action type, resource, purpose, duration, amount, count, and delegation depth;
- `AAEF-DEL-03` — delegation chains for high-impact actions shall be recorded as evidence;
- `AAEF-DEL-04` — revocation of upstream authority shall invalidate dependent downstream delegations;
- `AAEF-DEL-05` — authority lineage shall be recorded for delegated, cross-agent, and cross-domain workflows;
- `AAEF-PRN-02` — principal context shall remain valid, current, bounded, and semantically connected across delegations and workflows;
- `AAEF-RES-04` — conditional authority freeze behavior shall cover downstream delegation propagation.

This means immediate new control IDs are not required for the first cross-agent testing refinement batch.

## Decision

Do not add `VTC-A2A-*` rows directly to the active testing procedure CSV at this stage.

Instead, treat cross-agent delegation candidates as refinement inputs for existing DEL-focused testing rows.

This avoids:

- breaking one-to-one validation with the control catalog;
- turning temporary VTC IDs into apparent active requirements;
- changing the active baseline before reviewer agreement;
- adding new control IDs before confirming that existing DEL rows are insufficient;
- mixing candidate tests with current control-linked testing procedures.

## Candidate-to-Active-Row Mapping

| Candidate | Primary existing row | Secondary existing rows | Proposed incorporation path |
| --- | --- | --- | --- |
| VTC-A2A-01 Communication Treated as Delegation Authority | AAEF-DEL-05 | AAEF-DEL-01, AAEF-DEL-02 | Refine authority lineage and receiving-side verification language to state that communication alone is not delegation authority. |
| VTC-A2A-02 Agent Identity Treated as All-Purpose Delegation Authority | AAEF-DEL-02 | AAEF-DEL-01, AAEF-DEL-05 | Refine delegated constraint language for capability, operation, target, resource, purpose, and scope. |
| VTC-A2A-03 Fire-and-Forget Delegation | AAEF-DEL-05 | AAEF-DEL-03, AAEF-PRN-02 | Refine evidence expectations for acceptance, pending, refusal, timeout, and workflow state. |
| VTC-A2A-04 Refusal Not Propagated | AAEF-DEL-05 | AAEF-DEL-03, AAEF-RES-04 | Refine refusal propagation and resulting workflow state evidence expectations. |
| VTC-A2A-05 Delegated Scope Mismatch Ignored | AAEF-DEL-01 | AAEF-DEL-02, AAEF-DEL-05 | Refine delegated scope comparison and mismatch handling language. |
| VTC-A2A-09 Receiving-Side Validation Missing | AAEF-DEL-05 | AAEF-DEL-01, AAEF-DEL-02 | Refine receiving-side validation language and reject requesting-side assertion alone. |

## Minimal First CSV Refinement Candidate

The smallest active CSV refinement candidate should be limited to:

- VTC-A2A-01 mapped primarily to `AAEF-DEL-05`;
- VTC-A2A-05 mapped primarily to `AAEF-DEL-01`;
- VTC-A2A-09 mapped primarily to `AAEF-DEL-05`.

These three are the most directly tied to authority validation and are least dependent on unresolved acceptance/refusal workflow semantics.

## Proposed AAEF-DEL-01 Refinement Direction

### Current concern

`AAEF-DEL-01` already covers delegation-based escalation by comparing delegator and delegatee scopes.

However, the cross-agent testing work indicates that delegated scope mismatch should be explicitly visible in testing language.

### Proposed refinement area

Potential future refinements may clarify that samples should include, where feasible:

- requested delegated scope;
- effective delegated scope;
- principal authorized scope;
- delegator authority;
- delegatee requested action;
- delegated capability, operation, target, or resource comparison;
- denial, refusal, limitation, escalation, or reauthorization before execution.

### Candidate impact

This would incorporate the core of VTC-A2A-05 without adding a new testing row.

## Proposed AAEF-DEL-02 Refinement Direction

### Current concern

`AAEF-DEL-02` already covers delegation constraints.

However, the cross-agent testing work indicates that agent identity must not be treated as all-purpose delegation authority.

### Proposed refinement area

Potential future refinements may clarify that delegated authority constraints should include, where applicable:

- capability;
- operation;
- tool;
- target;
- resource;
- purpose;
- delegatee;
- duration;
- count;
- amount;
- delegation depth;
- receiving-side enforcement or validation expectations.

### Candidate impact

This would incorporate the core of VTC-A2A-02 while preserving the existing control-linked row model.

## Proposed AAEF-DEL-05 Refinement Direction

### Current concern

`AAEF-DEL-05` already covers authority lineage, cross-agent workflows, trust domains, authority assertions, delegated scope, constraints, and receiving-side verification.

However, the cross-agent testing work indicates that the row should more explicitly test three issues:

- agent-to-agent communication is not authority by itself;
- receiving-side validation must not rely only on requesting-side assertion or model rationale;
- acceptance, refusal, pending, or timeout states may need reconstruction where delegation workflow state affects execution.

### Proposed refinement area

Potential future refinements may clarify that samples should include, where feasible:

- requesting agent;
- receiving agent;
- authority assertion or delegation record;
- delegated authority artifact or trusted policy reference;
- receiving-side validation source;
- validation result;
- acceptance, refusal, pending, or timeout state;
- resulting workflow state;
- downstream execution or non-execution outcome.

### Candidate impact

This would incorporate the core of VTC-A2A-01 and VTC-A2A-09, and partially prepare for VTC-A2A-03 and VTC-A2A-04.

## Candidates Not Recommended for Immediate CSV Refinement

### VTC-A2A-02 — Agent Identity Treated as All-Purpose Delegation Authority

This candidate should remain close, but may require clearer wording around capability-scoped delegation before active CSV refinement.

It may be incorporated through `AAEF-DEL-02` after confirming the preferred constraint vocabulary.

### VTC-A2A-03 — Fire-and-Forget Delegation

This candidate should remain close, but may require clearer workflow-state expectations.

Questions include:

- whether explicit acceptance is always required;
- when pending or timeout states are sufficient;
- how asynchronous delegation should be sampled.

### VTC-A2A-04 — Refusal Not Propagated

This candidate should remain close, but may require clearer refusal propagation and workflow-state evidence expectations.

Questions include:

- what counts as safe refusal propagation;
- whether refusal should terminate, escalate, reroute, or reauthorize;
- how downstream non-execution should be evidenced.

## Proposed Next Active CSV PR

A later active CSV PR, if approved, should be narrow.

Recommended initial scope:

- refine only `AAEF-DEL-01`;
- refine only `AAEF-DEL-05`;
- do not add new rows;
- do not add `VTC-A2A-*` IDs to active CSV;
- update only testing language, not control requirements;
- validate that the one-to-one testing procedure model remains intact.

## Review Questions Before Active CSV Change

Before editing the active testing procedure CSV, reviewers should answer:

- Should VTC-A2A-01 be incorporated into `AAEF-DEL-05`, `AAEF-DEL-01`, or both?
- Should VTC-A2A-05 be incorporated into `AAEF-DEL-01`, `AAEF-DEL-02`, or both?
- Should VTC-A2A-09 be incorporated into `AAEF-DEL-05`, `AAEF-DEL-02`, or both?
- Should receiving-side validation be required generally or profile-dependent?
- Should communication-not-authority language appear in pass criteria, fail conditions, notes, or all three?
- Should delegated scope mismatch be handled as sample selection, pass criteria, fail conditions, or all three?
- Would these refinements materially change control expectations, or only clarify testing?
- Should #163 remain open after the first CSV refinement because downstream redelegation, chain evidence, acceptance/refusal, and budget propagation remain unresolved?

## Relationship to #163

This document supports #163 by identifying a safe path from cross-agent delegation testing candidates toward active testing procedure refinement.

It does not close #163.

Remaining #163 work includes:

- deciding whether to refine active testing CSV rows;
- deciding whether VTC-A2A-02, VTC-A2A-03, and VTC-A2A-04 are ready for later refinement;
- defining downstream redelegation authority;
- defining minimum delegation chain evidence expectations;
- defining refusal and acceptance evidence expectations;
- deciding whether related evidence/schema or assessment profile changes are needed.

## Non-Goals

This document does not:

- update testing procedure CSV;
- add active testing procedure rows;
- add `VTC-A2A-*` IDs to active CSV;
- create executable fixtures;
- add control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- close #163;
- change the one-to-one testing procedure model.

It is a temporary CSV refinement proposal for the v0.5.x incorporation phase.
