# Authority Lifecycle Model

**Status:** Non-normative v0.5.0 planning model

> **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifacts, testing procedures, or release notes.

## Purpose

This document consolidates the authority lifecycle concepts currently explored in v0.5.0 planning.

It connects three related planning themes:

- Principal Context Degradation
- Cross-Agent and Cross-Domain Authority
- Authority Denial and Reauthorization Flow

The purpose is to describe how authority is established, preserved, degraded, transferred, denied, expired, revoked, frozen, and reauthorized across agentic action workflows.

This model does not introduce new control requirements by itself.

## Scope

The authority lifecycle model applies to agentic systems where an agent, workflow, tool dispatcher, backend service, or delegated agent may perform actions on behalf of a principal.

It is intended to help reviewers reason about:

- whether an action is still bound to the correct principal;
- whether authority remains fresh enough for the requested action;
- whether delegation or handoff changed the effective authority boundary;
- whether denied, expired, revoked, or frozen authority is respected;
- whether reauthorization is required before execution;
- whether evidence can reconstruct the authority path.

## Lifecycle Stages

| Stage | Description | Primary risk |
| --- | --- | --- |
| Principal binding | The system associates an action request with a principal, actor, account, tenant, organization, or delegated authority source. | Action is attributed to the wrong principal or an ambiguous authority source. |
| Authority assertion | The system claims that a principal or delegated actor has authority for a requested action. | Model output, agent memory, or user-provided text is treated as authority. |
| Authority verification | A trusted component checks whether the authority assertion is valid for the action, scope, target, and risk level. | Verification is skipped, stale, incomplete, or performed by an untrusted component. |
| Authority freshness | The system determines whether the authorization context is recent enough for the requested action. | A previously valid authority decision is reused after context has changed. |
| Delegation or handoff | Authority is transferred, delegated, or interpreted across agents, tools, domains, tenants, or backend systems. | Authority expands or changes meaning during handoff. |
| Degradation detection | The system detects that principal context, scope, policy, risk, or environmental assumptions have drifted. | The agent continues acting under degraded or ambiguous authority. |
| Denial handling | The system denies an action when authority is absent, insufficient, expired, revoked, or inconsistent. | Denied actions are retried, transformed, or executed through alternate paths. |
| Freeze or revocation | The system prevents further action after authority is withdrawn, frozen, or placed under review. | Agent state, queues, cached decisions, or delegated tasks continue operating. |
| Reauthorization | The system requires renewed authority before continuing or retrying the action. | Reauthorization is bypassed, implied, or performed without sufficient context. |
| Evidence capture | The system records enough evidence to reconstruct the authority lifecycle for the action. | Auditors cannot determine who authorized what, when, under which scope, and through which component. |

## Authority State Model

The following state model is a planning aid.

| Authority state | Meaning | Expected behavior |
| --- | --- | --- |
| Unbound | No reliable principal binding exists. | Do not execute authority-bearing actions. Require principal binding. |
| Asserted | Authority is claimed but not yet verified by a trusted component. | Do not treat the assertion as sufficient authority. |
| Verified | Authority has been checked for the action, target, scope, and policy context. | Execution may proceed only within the verified scope and validity period. |
| Delegated | Authority is passed to another agent, workflow, tool, or domain. | Preserve delegation scope, provenance, expiry, and constraints. |
| Degraded | Context has drifted or become ambiguous. | Require additional checks, reduced privileges, denial, or reauthorization. |
| Denied | Authority is absent or insufficient. | Prevent execution and record denial evidence. |
| Frozen | Further action is suspended pending review, incident response, or policy decision. | Block execution, queued actions, delegated actions, and retries. |
| Revoked | Authority has been withdrawn. | Invalidate cached decisions and stop dependent workflows. |
| Expired | Authority is no longer valid due to time, policy, scope, or session limits. | Require reauthorization before execution. |
| Reauthorized | Authority has been renewed after verification. | Proceed only under the new authorization context. |

## Principal Context Degradation

Principal context degradation occurs when an action remains technically linked to a principal, but the reliability or meaning of that linkage weakens over time or across workflow transitions.

Examples include:

- long-running agent sessions where the original user intent is no longer fresh;
- queued or delayed actions executed after policy, account, tenant, or role changes;
- agent memory or conversation history being used as if it were current authority;
- delegated sub-agents acting after the original task scope has drifted;
- approval or authorization decisions reused outside their intended validity period.

A degraded principal context does not automatically mean that execution must fail, but it should trigger risk-appropriate safeguards such as revalidation, reduced action scope, denial, freeze, or reauthorization.

## Cross-Agent and Cross-Domain Authority

Cross-agent and cross-domain authority risks arise when an action crosses a boundary between agents, tools, services, tenants, organizations, environments, or administrative domains.

The authority lifecycle model treats cross-boundary handoff as a point where authority must be preserved explicitly rather than inferred implicitly.

At minimum, a handoff should preserve:

- source principal;
- delegating actor or component;
- delegated scope;
- action target;
- policy context;
- expiry or validity window;
- constraints and exclusions;
- evidence of the handoff;
- downstream enforcement point.

If these elements cannot be preserved or corroborated, the downstream component should treat the authority context as degraded or unbound.

## Denial, Freeze, Revocation, and Reauthorization

Authority denial and reauthorization are not exceptional edge cases. They are normal lifecycle transitions that must be testable.

Systems should distinguish:

- **denial**, where an action is not authorized;
- **freeze**, where further action is temporarily suspended;
- **revocation**, where previously granted authority is withdrawn;
- **expiry**, where authority is no longer valid;
- **reauthorization**, where authority is renewed after a fresh check.

A denied, frozen, revoked, or expired authority state should not be bypassed by:

- retrying the same action through another tool;
- decomposing the denied action into smaller actions;
- delegating the action to another agent;
- using cached authorization decisions;
- relying on model output, memory, or prior user text as renewed authority.

## Evidence Expectations

Authority lifecycle evidence should allow a reviewer to reconstruct:

- who or what asserted authority;
- which trusted component verified authority;
- what action, target, scope, and policy context were evaluated;
- whether the authority decision had an expiry or validity window;
- whether delegation or handoff occurred;
- whether principal context degradation was detected;
- whether denial, freeze, revocation, expiry, or reauthorization occurred;
- whether execution matched the verified authority scope.

Evidence should not rely solely on model-generated explanations, agent runtime self-reporting, or conversation text.

## Relationship to Existing AAEF Artifacts

This planning model may inform future refinements to:

- authorization controls;
- delegation controls;
- memory and state controls;
- human approval controls;
- governance controls;
- testing procedures for denial, freeze, expiry, and reauthorization paths;
- evidence expectations for authority lifecycle reconstruction.

The model does not itself change the v0.4.1 control catalog, assessment worksheet, testing procedures, evidence schema, or external framework mappings.

## Preliminary Incorporation Outcome

The expected incorporation path is:

| Planning theme | Likely incorporation path |
| --- | --- |
| Principal Context Degradation | Existing control refinement, guidance, and testing refinement |
| Cross-Agent and Cross-Domain Authority | Existing control refinement, with possible new control candidate if cross-boundary authority cannot be expressed by existing controls |
| Authority Denial and Reauthorization Flow | Testing refinement, evidence refinement, and possible existing control refinement |

Any future normative incorporation should follow the incorporation rules and outcome register in `docs/en/34-v050-control-design-options.md`.
