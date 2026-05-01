# v0.5.x Issue #162 Cross-Agent Capability-Scoped Delegation Consolidation Checkpoint

**Status:** Close-readiness checkpoint
**Scope:** #162 — Define cross-agent capability-scoped delegation controls
**Milestone:** v0.5.x Follow-up
**Type:** Temporary status / coordination material

## Purpose

This checkpoint consolidates the v0.5.x follow-up work for cross-agent capability-scoped delegation controls.

It records that the current v0.5.x treatment of capability-scoped cross-agent delegation is sufficient for the present follow-up cycle without adding a new control ID, a new control domain, or active catalog changes.

The checkpoint also records that future work may still define a dedicated cross-agent authority control area if later review shows that existing delegation, authorization, evidence, response, and governance controls cannot express the required obligations clearly enough.

## Completed Work

The #162 work stream has produced and connected the following material:

- Cross-Agent and Cross-Domain Authority planning material.
- Capability-Scoped Cross-Agent Delegation guidance.
- Cross-Agent Delegation Negative Tests guidance.
- Cross-Agent Budget Propagation guidance.
- Cross-agent authority examples.
- Authority assertion planning profile.
- Cross-agent delegation testing proposal.
- Cross-agent delegation candidate appendix.
- Cross-agent delegation CSV refinement proposal.
- First active testing procedure refinement for cross-agent delegation expectations.
- Follow-up status and incorporation decision register entries.

## Design Decision

For the current v0.5.x follow-up cycle, capability-scoped cross-agent delegation should remain an existing-control refinement and guidance concept.

AAEF should not add a new cross-agent control domain or new dedicated cross-agent control IDs in this cycle.

The current decision is:

- use existing `AAEF-DEL-*` controls as the primary home for delegated authority constraints;
- use `AAEF-AUZ-*` controls for action-specific authorization and receiving-side enforcement;
- use `AAEF-EVD-*` controls for evidence, lineage, reconstruction, non-execution, and reauthorization records;
- use `AAEF-PRN-*` controls where principal context must remain valid across delegation;
- use `AAEF-RES-*` controls where revocation, freeze, or propagation behavior affects downstream delegation;
- keep a possible future cross-agent authority control area as a candidate for later design work.

## Core Principle

Inter-agent communication is not delegation authority.

A requesting agent may be allowed to communicate with another agent without being allowed to delegate work, spend resources, invoke high-impact capabilities, expand the original principal's authority, or cause a receiving agent to act.

A receiving agent, gateway, workflow, or backend component should not treat the following as sufficient delegation authority by themselves:

- message delivery;
- agent-to-agent reachability;
- authenticated communication channel;
- known requesting agent identity;
- requesting-side assertion;
- model-generated rationale;
- free-text instruction;
- external authority claim that has not been validated by the receiving side.

## Capability-Scoped Delegation Expectations

Capability-scoped cross-agent delegation should be evaluated at the capability, action, resource, target, operation, and constraint level rather than merely at the agent identity level.

Where applicable, a cross-agent delegation context should identify:

- original principal;
- requesting or delegating agent;
- receiving agent, service, workflow, or domain;
- delegated capability or capability class;
- allowed operation class;
- target resource or resource class;
- purpose or task scope;
- tenant, organization, workspace, environment, or trust domain;
- time window, expiration, freshness, or validity condition;
- resource, budget, quota, count, or rate constraints where applicable;
- whether downstream delegation is allowed;
- downstream delegation depth or chain limits where applicable;
- authority assertion or delegation record reference;
- revocation, freeze, or downscope state;
- receiving-side validation result;
- execution, refusal, denial, deferral, escalation, reauthorization, or non-execution outcome.

## Active Testing Coverage

The current active testing procedure model already covers the core #162 concerns through existing rows.

### `AAEF-DEL-01`

`AAEF-DEL-01` covers delegation-based escalation and delegated scope mismatch.

Current coverage includes:

- delegator and delegatee authority comparison;
- principal authorized scope comparison;
- delegated capability, operation, target, and resource comparison;
- requested delegated scope versus effective delegated scope;
- cross-agent delegated requests;
- high-impact delegated actions;
- denial, refusal, limitation, escalation, or reauthorization where delegated authority would exceed the allowed scope;
- failure when broader authority is obtained from model output, requesting-side assertion, agent identity, or untrusted content.

### `AAEF-DEL-02`

`AAEF-DEL-02` remains the general bounded delegated authority row.

Current coverage includes:

- scope;
- purpose;
- resource;
- action or tool;
- delegatee;
- principal;
- time or expiration;
- policy constraints;
- linkage to authority basis;
- prohibition on broadening without authorization or reauthorization.

This row can be refined later if #163, #164, public review, or implementation feedback shows that capability-scoped delegation needs more explicit active CSV treatment.

### `AAEF-DEL-05`

`AAEF-DEL-05` is the primary active row for cross-agent and cross-domain authority lineage.

Current coverage includes:

- delegated, cross-agent, cross-domain, tool-mediated, and workflow-orchestrated high-impact actions;
- principal, upstream agent, external or downstream agent, and trust domain;
- authority assertion or delegation record;
- delegated scope and constraints;
- receiving-side verification;
- receiving-side validation source;
- validation result;
- acceptance, refusal, pending, or timeout state where applicable;
- downstream action IDs;
- evidence trust limitations;
- non-treatment of agent-to-agent communication, requesting-side assertion, message content, model rationale, or agent identity as authority without trusted validation.

### Supporting Rows

The current model is also supported by:

- `AAEF-PRN-02` for principal context validity across delegations and workflows;
- `AAEF-DEL-04` for upstream revocation, freeze, expiration, or authority reduction invalidating downstream delegated authority;
- `AAEF-AUZ-03`, `AAEF-AUZ-07`, and `AAEF-AUZ-09` for action-specific approval, state-aware authorization, denial handling, reauthorization, and bypass resistance;
- `AAEF-EVD-04`, `AAEF-EVD-05`, and `AAEF-EVD-06` for evidence integrity, non-execution evidence, reauthorization evidence, and retry / task-splitting correlation;
- `AAEF-RES-04` for freeze behavior, downstream delegation propagation, and residual risk.

## Current Decision

For the current v0.5.x follow-up cycle:

- no new cross-agent control domain is required for #162;
- no new dedicated cross-agent control ID is required for #162;
- no active control catalog change is required for #162;
- no further active testing procedure CSV change is required for #162 at this time;
- no Evidence Event Schema change is required for #162 at this time;
- no evidence example change is required for #162 at this time;
- no validator fixture change is required for #162 at this time;
- no assessment worksheet change is required for #162 at this time;
- no assessment profile change is required for #162 at this time;
- no external mapping change is required for #162 at this time.

Capability-scoped cross-agent delegation remains a cross-cutting authority lifecycle concept and existing-control refinement path.

A future dedicated cross-agent authority control area remains possible, but should be based on later review of #163, #164, implementation experience, and public feedback.

## Close-Readiness Criteria

#162 can be considered close-ready once this checkpoint is merged and linked from the v0.5.x status materials.

The close rationale is:

- the capability-scoped delegation guidance exists;
- the core principle that inter-agent communication is not delegation authority is documented;
- cross-agent authority examples exist;
- authority assertion planning material exists;
- cross-agent delegation testing proposal and candidate appendix material exist;
- active testing procedures already incorporate the first cross-agent delegation expectations;
- the current cycle has an explicit decision not to add new cross-agent control IDs or a new control domain yet;
- remaining acceptance/refusal, chain accountability, downstream redelegation, and budget propagation work is better tracked under #163 and #164.

## Future Work

Possible future work should be tracked separately from #162 if needed:

- stable cross-agent authority assessment guidance extraction;
- future dedicated cross-agent authority control domain or control IDs;
- additional `AAEF-DEL-02` refinement for capability-scoped delegation constraints;
- future authority assertion fields in the Evidence Event Schema;
- cross-agent authority evidence examples;
- executable or fixture-based tests for communication mistaken as authority, identity-as-authority, missing receiving-side validation, stale authority assertions, and overbroad delegated capabilities;
- downstream redelegation semantics under #163;
- budget, quota, tool-use, API-use, compute, time, data access, and downstream delegation limits under #164.

## Non-Goals

This checkpoint does not:

- add a new cross-agent control domain;
- add new active control IDs;
- add active testing procedure rows;
- add candidate IDs to the active CSV;
- change the Evidence Event Schema;
- add evidence examples;
- add validator fixtures;
- require a specific credential technology;
- require JWT, DID/VC, SPIFFE/SPIRE, mTLS, organization PKI, or transparency logs;
- mark #163, #164, or #3 as completed.
