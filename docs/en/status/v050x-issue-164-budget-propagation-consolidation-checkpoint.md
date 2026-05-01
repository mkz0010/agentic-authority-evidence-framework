# v0.5.x Issue #164 Budget Propagation Consolidation Checkpoint

**Status:** Close-readiness checkpoint
**Scope:** #164 — Define cross-agent budget propagation guidance
**Milestone:** v0.5.x Follow-up
**Type:** Temporary status / coordination material

## Purpose

This checkpoint consolidates the v0.5.x follow-up work for cross-agent budget and resource propagation guidance.

It records that the current v0.5.x treatment is sufficient for the present follow-up cycle without adding a new control ID, changing the active testing procedure CSV, changing the Evidence Event Schema, adding evidence examples, adding validator fixtures, changing assessment profiles, or changing external mappings.

It also records that future selected-context guidance, schema candidates, testing candidates, examples, or control refinements may be tracked separately.

## Completed Work

The #164 work stream has produced and connected the following material:

- Cross-Agent Budget Propagation guidance.
- Capability-Scoped Cross-Agent Delegation guidance.
- Cross-Agent Delegation Negative Tests guidance.
- Cross-agent authority lifecycle guidance.
- Cross-agent authority examples.
- Candidate testing material that includes budget or resource propagation failure.
- Follow-up status and incorporation decision register entries.
- Adjacent #162 consolidation decision for capability-scoped cross-agent delegation.
- Adjacent #163 consolidation decision for delegation acceptance/refusal and chain accountability negative tests.

## Guidance Coverage

The existing cross-agent budget propagation guidance covers the major #164 concerns.

Covered guidance areas include:

- delegated agents should not receive unlimited budget, quota, execution time, external API use, tool access, compute, data access, or downstream delegation authority merely because a task was delegated;
- cross-agent delegation should preserve, attenuate, partition, derive, or explicitly reauthorize resource limits;
- missing constraints should not imply unlimited authority;
- conflicting constraints should trigger denial, deferral, escalation, clarification, or reauthorization;
- receiving-side validation should evaluate resource constraints before acceptance or execution;
- enforcement may occur at agent runtime, tool dispatcher, gateway, workflow engine, backend API, policy engine, evidence pipeline, or human approval workflow boundaries;
- budget evidence should support reconstruction of the delegated limit, actual use, enforcement decision, and any expansion approval;
- aggregate resource use across retries, subtasks, parallel calls, and downstream delegations should be considered where applicable;
- downstream agents should receive preserved, attenuated, partitioned, or explicitly reauthorized constraints rather than broader authority automatically;
- AAEF should define authority, constraint, enforcement, and evidence properties without mandating a specific quota, billing, identity, token, gateway, or cryptographic technology.

## Resource Constraint Scope

The guidance already treats budget broadly rather than limiting it to financial spend.

Relevant resource constraint categories include:

- financial budget;
- compute budget;
- token or model budget;
- API budget;
- tool-use budget;
- time budget;
- data access budget;
- operational budget;
- delegation budget;
- review budget.

Organizations may define additional resource categories based on their system, risk, and operating environment.

## Active Coverage

The current active control and testing model can host cross-agent budget propagation as guidance and existing-control refinement for the current v0.5.x cycle.

### `AAEF-DEL-02`

`AAEF-DEL-02` is the primary active row for bounded delegated authority.

It already covers delegated authority constraints such as:

- scope;
- purpose;
- resource;
- action or tool;
- delegatee;
- principal;
- time or expiration;
- policy constraints;
- authority basis linkage;
- prohibition on broadening delegated authority without authorization or reauthorization.

This row can host future budget, quota, rate, tool-use, API-use, compute, time, data access, or delegation-depth refinements if later review requires active testing language.

### `AAEF-DEL-05`

`AAEF-DEL-05` supports cross-agent authority lineage and reconstruction.

It already covers:

- delegated, cross-agent, cross-domain, tool-mediated, and workflow-orchestrated high-impact actions;
- delegated scope and constraints;
- receiving-side verification;
- receiving-side validation source;
- validation result;
- downstream action IDs;
- evidence trust limitations.

This row can host future evidence expectations for propagated resource constraints if later review requires stronger active testing coverage.

### `AAEF-AUZ-09`

`AAEF-AUZ-09` supports bypass resistance where budget expansion, retry, task splitting, or reauthorization could become an authority bypass.

It already covers:

- retry control;
- scope creep;
- unsafe reauthorization;
- task splitting detection;
- linkage to prior denial;
- scoped, attributable reauthorization.

This row can support future active review of aggregate budget tracking, task splitting to bypass budget, and budget expansion reauthorization.

### `AAEF-EVD-05`

`AAEF-EVD-05` supports non-execution evidence where a budget, quota, policy, or authority gap prevents execution.

It already covers:

- denial;
- deferral;
- escalation;
- freeze;
- safe termination;
- authority gaps;
- policy gaps;
- retry correlation;
- task-splitting indicators;
- final non-execution outcome.

### `AAEF-EVD-06`

`AAEF-EVD-06` supports evidence for reauthorization, additional scope requests, retries, and escalation.

It can support future budget expansion review by linking:

- original denial;
- requested additional scope;
- escalation or approval target;
- retry count;
- retry correlation;
- task-splitting indicators;
- decision outcome;
- post-reauthorization effective scope;
- final dispatch or non-execution outcome.

### `AAEF-RES-04`

`AAEF-RES-04` supports response and freeze behavior where downstream delegation, queued actions, or residual authority may need to be contained.

It can support budget propagation review where budget violations, resource exhaustion, or uncontrolled downstream delegation require freezing or limiting dependent action paths.

### `AAEF-HUM-02`

`AAEF-HUM-02` supports review of repeated, high-volume, batched, or task-split approval patterns.

It can support future budget propagation review where repeated budget expansion prompts, rate-limited approvals, approval fatigue, or task splitting affects meaningful human oversight.

## Current Decision

For the current v0.5.x follow-up cycle:

- no new cross-agent budget propagation control ID is required for #164 at this time;
- no new control domain is required for #164 at this time;
- no active control catalog change is required for #164 at this time;
- no active testing procedure CSV change is required for #164 at this time;
- no Evidence Event Schema change is required for #164 at this time;
- no evidence example change is required for #164 at this time;
- no validator fixture change is required for #164 at this time;
- no assessment worksheet change is required for #164 at this time;
- no assessment profile change is required for #164 at this time;
- no external mapping change is required for #164 at this time.

Cross-agent budget propagation remains non-normative guidance and an existing-control refinement candidate for the current cycle.

## Close-Readiness Criteria

#164 can be considered close-ready once this checkpoint is merged and linked from the v0.5.x status materials.

The close rationale is:

- cross-agent budget propagation guidance is defined;
- budget is treated broadly across financial, compute, token, API, tool-use, time, data access, operational, delegation, and review constraints;
- propagation patterns are described;
- receiving-side validation expectations are described;
- enforcement points are described without mandating implementation technology;
- evidence expectations are described as candidates rather than active schema requirements;
- anti-patterns and negative-test relationships are documented;
- no immediate active CSV, schema, example, validator, profile, or mapping change is required for the current v0.5.x follow-up cycle.

## Future Work

Possible future work should be tracked separately from #164 if needed:

- selected high-impact contexts where budget/resource propagation should become active testing guidance;
- future active `AAEF-DEL-02` refinement for budget, quota, rate, tool-use, API-use, compute, time, data access, and delegation-depth constraints;
- future active `AAEF-DEL-05` refinement for propagated resource constraint evidence;
- future active `AAEF-AUZ-09`, `AAEF-EVD-05`, or `AAEF-EVD-06` refinement for budget expansion, aggregate tracking, retry, task splitting, and reauthorization;
- future Evidence Event Schema fields for resource constraint type, ceiling, usage, enforcement result, exceeded budget indicator, or budget expansion approval reference;
- cross-agent budget propagation evidence examples;
- executable or fixture-based tests for missing resource constraints, unbounded downstream resource use, task splitting to bypass budget, and model-estimated cost accepted as enforcement;
- assessment profile guidance for resource-consuming cross-agent workflows;
- broader Cross-Agent and Cross-Domain Authority roadmap work under #3.

## Non-Goals

This checkpoint does not:

- add new active control IDs;
- add a new control domain;
- update active testing procedure CSV rows;
- add active testing procedure rows;
- add candidate IDs to the active CSV;
- change the Evidence Event Schema;
- add evidence examples;
- add validator fixtures;
- update assessment worksheet rows;
- update assessment profiles;
- update external framework mappings;
- require a specific quota, billing, token, identity, gateway, or cryptographic technology;
- require all low-risk delegated actions to carry heavyweight budget metadata;
- mark #3 as completed.
