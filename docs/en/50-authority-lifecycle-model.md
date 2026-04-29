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

## Capability-Scoped Cross-Agent Delegation

Capability-scoped cross-agent delegation is further described in `docs/en/56-capability-scoped-cross-agent-delegation.md`.

That guidance supports the authority lifecycle model by distinguishing communication, delegation acceptance, and execution authorization across agent boundaries.

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

## Cross-Agent Delegation Authority

Inter-agent communication is not delegation authority.

The ability of one agent, workflow, or tool to communicate with another does not imply that it has authority to delegate work, spend resources, invoke capabilities, or expand the scope of the original principal's authorization.

Cross-agent delegation should be treated as an authority-bearing transition, not merely as a message-passing event.

### Capability-Scoped Delegation

Cross-agent authority should be capability-scoped rather than merely agent-scoped.

For example, Agent A may be authorized to request information from Agent B, but not to delegate an action that modifies data, spends money, contacts an external party, or triggers a high-impact operation.

A cross-agent delegation context should identify, where applicable:

- requesting agent;
- receiving agent;
- source principal;
- delegated capability;
- action type;
- target or resource;
- allowed scope;
- budget or resource ceiling;
- validity window or expiry;
- maximum delegation depth;
- whether downstream delegation is allowed;
- policy context and constraints.

If the requested capability is not covered by the delegation context, the receiving agent should treat the request as unauthorized or require reauthorization.

### Explicit Delegation Acceptance and Refusal

Delegation should not be treated as fire-and-forget.

A receiving agent should be able to explicitly accept or refuse a delegated task before the delegating agent proceeds as if the task will be performed.

The delegation response should distinguish:

| Delegation response | Meaning | Expected behavior |
| --- | --- | --- |
| Accepted | The receiving agent accepts the delegated task within the provided authority scope. | The delegating workflow may proceed based on the accepted delegation. |
| Refused | The receiving agent refuses the task and provides a reason or refusal category. | The delegating workflow must not assume execution and should handle denial, fallback, escalation, or reauthorization. |
| Ambiguous | The receiving agent response does not clearly accept or refuse. | Treat as not accepted; require clarification or reauthorization. |
| Expired | The delegation request or authority context is no longer valid. | Do not execute; require renewed delegation authority. |
| Out of scope | The request exceeds the delegated capability, budget, target, or validity window. | Refuse or require reauthorization before execution. |

Refusal propagation is important. If a downstream agent refuses a delegated task, that refusal should propagate back to the requesting agent or workflow in a way that prevents silent continuation under a false assumption of execution.

### Delegation Chain Limits and Accountability

Delegation chains should have explicit limits.

Without depth limits, reauthorization expectations, and evidence linkage, accountability can become difficult to reconstruct as authority passes from Agent A to Agent B, then to Agent C, and onward.

A delegation chain should preserve:

- the original principal or authority source;
- each delegating and receiving agent;
- delegated capability and scope at each hop;
- maximum permitted delegation depth;
- whether each hop was accepted or refused;
- reauthorization events at each required level;
- budget and resource constraints at each hop;
- evidence linkage between delegation records.

For higher-integrity contexts, delegation evidence may use hash linkage, signatures, sequence identifiers, append-only records, or other mechanisms that make delegation chain modification detectable.

This document does not require a specific cryptographic mechanism. Such mechanisms may be appropriate for higher evidence integrity levels or audit-grade contexts.

### Cross-Agent Budget and Resource Propagation

Delegated agents should not receive unconstrained resource authority merely because they receive a delegated task.

When Agent A delegates to Agent B, Agent B should inherit bounded constraints such as budget, quota, rate limit, time limit, tool-use limit, or other resource ceilings appropriate to the original authorization.

Cross-agent budget propagation helps prevent:

- unbounded downstream delegation;
- resource exhaustion;
- cost amplification;
- uncontrolled external service use;
- unexpected high-impact side effects;
- accountability gaps between the delegating and receiving agents.

Budget and resource constraints should be enforced by a trusted gateway, dispatcher, workflow engine, backend service, or equivalent enforcement point where feasible.


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
- what capability, budget, resource, and delegation depth constraints applied;
- whether downstream delegation was accepted, refused, expired, or out of scope;
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
| Cross-Agent and Cross-Domain Authority | Existing control refinement, with possible new control candidate for capability-scoped delegation, explicit acceptance or refusal, delegation chain limits, or cross-agent budget propagation if existing controls cannot express these obligations |
| Authority Denial and Reauthorization Flow | Testing refinement, evidence refinement, and possible existing control refinement |

Any future normative incorporation should follow the incorporation rules and outcome register in `docs/en/34-v050-control-design-options.md`.
