# Cross-Agent and Cross-Domain Authority Examples

**Status:** Non-normative v0.5.0 planning examples
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative examples for cross-agent authority, cross-domain authority assertions, delegation lineage, receiving-side validation, and evidence limitations

> **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifacts, testing procedures, or release notes.

## Purpose

This document provides non-normative examples for reviewing cross-agent and cross-domain authority in AAEF v0.5.0 planning.

It illustrates how reviewers can distinguish:

- same-domain agent delegation;
- cross-domain authority assertions;
- receiving-domain validation;
- stale or replayed authority assertions;
- delegated scope mismatch;
- agent-to-agent task handoff;
- cross-agent authority lineage;
- principal context degradation across domains;
- denial when authority lineage cannot be verified;
- evidence limitations and finding patterns.

This document does not change the Evidence Event Schema, control catalog, testing procedures, or assessment worksheet.

## Core Principle

An agent should not rely on another agent's authority claim merely because the other agent produced a plausible instruction, message, tool result, or model-generated explanation.

For high-impact cross-agent or cross-domain actions, the receiving system should be able to verify:

- who or what made the authority claim;
- on whose behalf the action is requested;
- what scope was delegated;
- which domain or trust boundary issued the claim;
- whether the claim is current;
- whether the receiving domain accepts the claim;
- what evidence supports the claim;
- what limitations apply to that evidence.

## Related Controls

These examples support review of:

- `AAEF-DEL-01`: delegated authority scope;
- `AAEF-DEL-02`: delegation constraints;
- `AAEF-DEL-05`: authority lineage across delegated, cross-agent, and cross-domain workflows;
- `AAEF-PRN-01`: principal binding;
- `AAEF-PRN-02`: principal context validity;
- `AAEF-AUZ-04`: denial or escalation when authority, principal, or purpose cannot be determined;
- `AAEF-AUZ-09`: authority denial and reauthorization flow;
- `AAEF-EVD-01`: action reconstruction;
- `AAEF-EVD-04`: tamper-evident evidence;
- `AAEF-EVD-05`: non-execution evidence;
- `AAEF-EVD-06`: reauthorization evidence.

For the related planning concept, see `docs/en/31-cross-agent-cross-domain-authority.md`.

For the related authority assertion planning profile, see `docs/en/35-authority-assertion-profile.md`.

## Example 1: Same-Domain Agent Delegation

### Scenario

A primary agent delegates a bounded task to a worker agent within the same system and trust domain.

The worker agent performs a low-risk preparatory action and returns a result.

### Strong Evidence

Strong evidence includes:

- upstream agent ID;
- downstream agent ID;
- shared trust domain;
- delegated task;
- delegated scope;
- constraints;
- principal binding;
- authority basis;
- timestamp;
- result;
- correlation ID;
- evidence source.

### Assessment Interpretation

This is a lower-complexity cross-agent case because both agents operate within the same trust domain.

A reviewer should still be able to reconstruct how authority moved from the principal to the upstream agent and then to the downstream agent.

## Example 2: Cross-Domain Authority Assertion

### Scenario

An external vendor-operated agent sends a request to a customer-operated agent.

The request includes an authority assertion claiming that the vendor agent is authorized to perform a maintenance action.

### Strong Evidence

Strong evidence includes:

- authority assertion ID;
- issuing domain;
- receiving domain;
- asserted principal;
- asserting agent;
- delegated scope;
- target resource;
- action category;
- constraints;
- expiration;
- issuer signature or verification reference;
- evidence reference;
- receiving-side validation result.

### Assessment Interpretation

The receiving domain should not accept the assertion merely because it is present.

The assertion should be verified against trusted issuer, scope, expiration, target domain, and receiving-side policy.

## Example 3: Receiving-Domain Validation

### Scenario

A SaaS platform receives a cross-domain authority assertion from an integration partner.

The receiving platform validates the assertion before dispatching a high-impact tool call.

### Expected Safe Behavior

The receiving domain should verify:

- issuer trust;
- assertion freshness;
- signature or integrity reference;
- delegated scope;
- principal binding;
- target tenant;
- requested action;
- policy compatibility;
- revocation status;
- evidence limitations.

### Strong Evidence

Strong evidence includes:

- received assertion ID;
- validation timestamp;
- validation result;
- receiving policy version;
- accepted scope;
- rejected or narrowed scope where applicable;
- final dispatch or non-execution outcome.

### Assessment Interpretation

Receiving-side validation is a critical boundary.

A cross-domain assertion should not directly become execution authority without receiving-side evaluation.

## Example 4: Stale or Replayed Authority Assertion

### Scenario

A valid authority assertion from a prior maintenance window is reused after expiration.

The agent attempts to use it for a new production action.

### Risk Indicators

Reviewers should look for:

- expired assertion;
- reused assertion ID;
- stale timestamp;
- mismatched action digest;
- mismatched target resource;
- changed principal context;
- changed policy version;
- missing freshness check;
- missing revocation check.

### Expected Safe Behavior

The receiving system should deny or defer execution and record the replay or freshness failure.

### Assessment Interpretation

Evidence integrity alone does not prevent replay.

Authority assertions need freshness, expiration, scope, and linkage to the action being authorized.

## Example 5: Delegated Scope Mismatch

### Scenario

An upstream agent delegates authority to read a customer record.

The downstream agent attempts to update the customer record.

### Expected Safe Behavior

The system should:

- compare delegated scope to requested action;
- detect scope mismatch;
- deny, defer, or require reauthorization;
- record the original delegated scope;
- record the attempted action;
- record the final non-execution or reauthorization outcome.

### Assessment Interpretation

A delegated authority record should not be treated as a general-purpose permission.

The requested action must stay within the delegated scope.

## Example 6: Agent-to-Agent Task Handoff

### Scenario

Agent A hands off a workflow to Agent B.

Agent B continues the workflow and performs a high-impact action.

### Strong Evidence

Strong evidence includes:

- handoff ID;
- upstream agent ID;
- downstream agent ID;
- principal context;
- original user request;
- delegated task;
- authority basis;
- transferred constraints;
- policy version;
- handoff timestamp;
- downstream authorization decision;
- final dispatch or execution record.

### Assessment Interpretation

A task handoff should preserve enough authority lineage for reviewers to reconstruct why Agent B was allowed to act.

A handoff should not erase the original principal, request, or constraints.

## Example 7: Cross-Agent Authority Lineage

### Scenario

A workflow involves a principal, an orchestrator agent, a planning agent, a tool-dispatch agent, and a backend API.

The backend action is high-impact.

### Strong Evidence

Strong evidence includes:

- principal ID;
- orchestrator agent ID;
- planning agent ID;
- dispatch agent ID;
- backend service identity;
- delegation or assertion references;
- constraints at each step;
- decision points;
- action digest;
- final execution result;
- correlation ID;
- evidence limitations.

### Assessment Interpretation

This is a strong `AAEF-DEL-05` case if reviewers can trace authority from principal to each agent and finally to the high-impact action.

## Example 8: Principal Context Degradation Across Domains

### Scenario

A principal context is valid in Domain A.

An agent attempts to use that context in Domain B after a delay and after role membership may have changed.

### Risk Indicators

Reviewers should look for:

- stale principal context;
- missing receiving-domain principal mapping;
- missing role freshness check;
- missing tenant or workspace binding;
- missing delegated scope;
- missing reconfirmation;
- semantic mismatch between original request and downstream action.

### Expected Safe Behavior

The receiving domain should treat degraded principal context as a reason to deny, defer, escalate, or require scoped reauthorization.

### Assessment Interpretation

Cross-domain workflows can amplify Principal Context Degradation.

The receiving domain should not assume that upstream context remains current or sufficient.

## Example 9: Denial When Authority Lineage Cannot Be Verified

### Scenario

A downstream agent receives a high-impact action request but cannot verify which principal authorized the upstream workflow.

### Expected Safe Behavior

The downstream system should:

- deny or defer execution;
- record missing lineage;
- record missing principal binding;
- prevent dispatch;
- request additional evidence or reauthorization;
- preserve the attempted action record.

### Strong Evidence

Strong evidence includes:

- attempted action ID;
- upstream agent ID;
- missing lineage reason;
- denied authority assertion ID where applicable;
- principal binding gap;
- receiving-side validation failure;
- final non-execution outcome.

### Assessment Interpretation

This is a strong denial case if the system fails closed and records enough evidence for review.

## Example 10: Cross-Domain Evidence Limitation

### Scenario

A receiving system accepts a cross-domain evidence reference but cannot independently verify the external evidence store.

### Evidence Limitation

Limitations may include:

- external evidence not independently accessible;
- external evidence mutable or unverifiable;
- missing signature verification;
- missing timestamp verification;
- missing source trust statement;
- missing retention guarantee;
- missing incident access path.

### Assessment Interpretation

A reviewer may accept the evidence with limitations, but should not treat it as strong independently verifiable evidence.

Evidence limitations should be recorded explicitly.

## Review Questions

Assessors should ask:

1. Which agent, system, workflow, or organization made the authority claim?
2. Which principal is the action being performed on behalf of?
3. What authority was delegated or asserted?
4. What scope and constraints applied?
5. Which trust domain issued the claim?
6. Which trust domain received and evaluated the claim?
7. Was the authority assertion current, scoped, and not expired?
8. Was receiving-side validation performed?
9. Were revocation, freeze, or policy changes checked?
10. Was authority lineage preserved across agent handoff?
11. Was principal context degraded across domain boundaries?
12. Was final dispatch or non-execution linked to the authority lineage?
13. Are cross-domain evidence limitations documented?
14. Could an incident reviewer reconstruct how authority moved across agents and domains?

## Finding Patterns

Reviewers may record findings for:

- receiving-domain execution without validation;
- stale or replayed authority assertions;
- delegated scope mismatch;
- missing principal binding;
- missing upstream agent identity;
- missing downstream agent identity;
- missing trust domain identifiers;
- missing receiving-side validation result;
- authority lineage not reconstructable;
- handoff erasing original constraints;
- cross-domain principal context degradation;
- execution after unverifiable authority claim;
- external evidence accepted without limitation;
- revocation or expiration not checked;
- non-execution not recorded when lineage cannot be verified.

## Non-Goals

These examples do not require:

- a universal cross-domain trust fabric;
- a specific credential format;
- a specific delegation protocol;
- a specific agent-to-agent protocol;
- a specific identity provider;
- remote attestation for every cross-domain action;
- schema changes in the current Evidence Event Schema.

## Future Work

Future AAEF work may decide whether to:

- add cross-agent authority JSON examples;
- add authority assertion fields to the Evidence Event Schema;
- define minimum authority assertion fields;
- define cross-domain evidence limitation fields;
- define negative tests for stale, replayed, or overbroad authority assertions;
- define assessment guidance for receiving-side validation;
- decide whether cross-agent and cross-domain authority should become a dedicated control domain.
