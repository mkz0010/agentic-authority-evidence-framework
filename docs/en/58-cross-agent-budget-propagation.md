# Cross-Agent Budget Propagation

**Status:** Non-normative v0.5.x follow-up guidance

## Purpose

This document defines non-normative guidance for cross-agent budget and resource propagation in AAEF.

It addresses follow-up work from the Cross-Agent and Cross-Domain Authority planning track.

The purpose is to clarify that delegated agents should not receive unbounded resource authority merely because a task has been delegated to them.

This document does not add new control IDs and does not change the v0.4.1 control and assessment baseline.

## Core Principle

Delegated authority should carry bounded resource constraints.

A delegated agent should not receive unlimited budget, quota, execution time, external API use, tool access, compute, or downstream delegation authority merely because another agent delegated a task.

Cross-agent delegation should preserve, attenuate, or explicitly reauthorize resource limits.

## Problem Statement

In multi-agent systems, delegated tasks may create resource amplification risk.

For example:

- Agent A has authority to spend up to a bounded amount.
- Agent A delegates part of the task to Agent B.
- Agent B invokes external tools, APIs, compute, or downstream agents.
- The delegated work consumes more resources than Agent A was allowed to use.
- The system cannot reconstruct who authorized the additional resource use.

This can create:

- cost amplification;
- quota exhaustion;
- unbounded external API use;
- compute or token overuse;
- denial of service through delegated workflows;
- uncontrolled downstream delegation;
- accountability gaps between requesting and receiving agents.

AAEF treats resource authority as part of delegated authority.

## Budget and Resource Scope

Budget propagation is not limited to money.

A delegated resource constraint may include:

| Resource type | Examples |
| --- | --- |
| Financial budget | Money, payment ceiling, purchase limit, contract value. |
| Compute budget | CPU, GPU, memory, job runtime, batch execution size. |
| Token or model budget | LLM token count, model call count, model tier, generation limit. |
| API budget | External API call count, paid API quota, rate limit, third-party usage. |
| Tool-use budget | Number of tool invocations, permitted tool class, high-impact tool limit. |
| Time budget | Execution duration, deadline, session lifetime, asynchronous task window. |
| Data access budget | Maximum records, dataset scope, sensitive data class, tenant boundary. |
| Operational budget | Deployment count, retry count, change window, production operation limit. |
| Delegation budget | Maximum downstream agents, delegation depth, redelegation count. |
| Review budget | Human approval count, escalation threshold, sampling requirement. |

Organizations may define additional resource categories.

## Propagation Model

When Agent A delegates work to Agent B, the delegated task should carry resource constraints that are no broader than Agent A's applicable authority.

A receiving agent should determine whether the delegated task includes:

- a resource ceiling;
- a resource class;
- a validity window;
- a target or tenant scope;
- a maximum delegation depth;
- permitted tools or APIs;
- disallowed tools or APIs;
- retry or task-splitting constraints;
- evidence requirements;
- reauthorization conditions.

If no resource constraints are present, the receiving agent should not infer unlimited resource authority.

The safe default should be to deny, refuse, defer, or require clarification for resource-consuming actions.

## Constraint Propagation Patterns

AAEF distinguishes several propagation patterns.

| Pattern | Description | Planning interpretation |
| --- | --- | --- |
| Preserved constraint | The receiving agent inherits the same budget or resource ceiling. | Usually appropriate for direct bounded delegation. |
| Attenuated constraint | The receiving agent receives a smaller budget or narrower resource scope. | Often safer for downstream or external delegation. |
| Partitioned constraint | The original budget is split across subagents or subtasks. | Useful when several delegated agents share a finite budget. |
| Derived constraint | The receiving agent receives a computed limit based on risk, task type, or policy. | Requires evidence of the derivation basis. |
| Reauthorized expansion | The receiving agent receives a broader budget after explicit reauthorization. | Should be evidenced and bound to the expanded scope. |
| Missing constraint | No resource bound is provided. | Should not imply unlimited authority. |
| Conflicting constraint | Delegation request and policy source disagree. | Should trigger denial, deferral, or escalation. |

## Receiving-Side Validation Expectations

A receiving agent or receiving domain should validate budget and resource constraints before accepting or executing delegated work.

Receiving-side validation should evaluate:

- whether a resource constraint exists;
- whether the requested action consumes a constrained resource;
- whether the requested resource use fits within the delegated limit;
- whether the resource class is permitted;
- whether the target or tenant is within scope;
- whether retry or parallel execution could exceed the limit;
- whether downstream delegation is permitted;
- whether aggregate delegated work could exceed the original authority;
- whether the budget has expired, been revoked, or been downscoped;
- whether additional resource use requires reauthorization;
- whether evidence can reconstruct the resource decision.

If validation fails, the receiving side should refuse, deny, defer, escalate, or request reauthorization.

## Enforcement Points

Budget propagation may be enforced at different system boundaries.

Possible enforcement points include:

| Enforcement point | Example responsibility |
| --- | --- |
| Agent runtime | Prevents local task execution beyond delegated limits. |
| Tool dispatcher | Blocks tool calls that exceed delegated budget, tool class, or rate limit. |
| Gateway | Enforces cross-agent or cross-domain resource constraints. |
| Workflow engine | Tracks aggregate resource use across subtasks and downstream agents. |
| Backend API | Verifies resource authority before committing external effects. |
| Policy engine | Decides whether requested resource use is authorized. |
| Evidence pipeline | Records resource constraint, use, validation, and enforcement result. |
| Human approval workflow | Handles explicit budget expansion or exception approval. |

AAEF does not require a single enforcement point.

For high-impact or audit-grade contexts, evidence should make clear where enforcement occurred.

## Candidate Control Expectations

The following are non-normative candidate expectations for future control refinement.

### Resource-constrained delegation

A cross-agent delegation should include resource constraints where the delegated task may consume money, compute, tokens, APIs, external services, privileged operations, production capacity, or downstream delegation capacity.

### No implicit unlimited budget

A receiving agent should not treat missing budget or resource constraints as unlimited authority.

### Receiving-side budget validation

The receiving side should validate whether the requested resource use is within the delegated resource scope before accepting or executing the task.

### Aggregate budget tracking

Systems should consider aggregate use across retries, subtasks, parallel calls, and downstream delegations.

A delegated workflow should not bypass limits by splitting the task across agents or repeated requests.

### Reauthorization for expansion

If additional budget, quota, time, tool use, or downstream delegation is needed, the system should require explicit reauthorization or escalation.

### Budget evidence preservation

The system should record enough evidence to reconstruct the resource authority path, including the delegated limit, actual use, enforcement decision, and any expansion approval.

### Downstream budget attenuation

Downstream agents should receive preserved, attenuated, partitioned, or explicitly reauthorized constraints rather than inheriting broader authority automatically.

## Candidate Evidence Expectations

Useful evidence for cross-agent budget propagation may include:

- delegation request identifier;
- requesting agent;
- receiving agent;
- delegating principal or policy source;
- delegated capability;
- resource constraint type;
- resource ceiling;
- permitted resource class;
- disallowed resource class;
- target or tenant scope;
- validity window;
- downstream delegation limit;
- retry or task-splitting constraint;
- enforcement point;
- resource use measurement;
- budget check result;
- exceeded budget indicator;
- denial, refusal, escalation, or reauthorization state;
- budget expansion approval reference;
- linkage to original authority or workflow;
- evidence limitation if resource tracking is incomplete.

These fields are candidates for future guidance or schema consideration.

They are not required evidence schema fields in this document.

## Anti-Patterns

| Anti-pattern | Risk |
| --- | --- |
| Delegated task implies unlimited budget | Delegated agents may consume resources beyond the original authority. |
| Agent identity implies budget authority | Known agents may receive broader resource authority than intended. |
| Missing budget treated as unlimited | Absence of constraint becomes implicit permission. |
| Local-only budget checks | Receiving domains may act without validating delegated resource limits. |
| No aggregate tracking | Task splitting or retries may exceed the original budget. |
| Downstream agents inherit full authority | Delegation chains amplify resource access. |
| Model-estimated cost accepted as enforcement | The estimate may be inaccurate or manipulable. |
| Later success overwrites exceeded-budget evidence | Resource violations become invisible during review. |
| Human approval expands budget without scope binding | Approval may authorize more than the principal intended. |

## Negative Test Relationship

Cross-agent budget propagation failure is also covered in `docs/en/57-cross-agent-delegation-negative-tests.md`.

Relevant negative test themes include:

- delegated agents receiving unbounded resources;
- missing resource constraints;
- retry after refusal;
- task splitting after refusal;
- downstream delegation without budget attenuation;
- broken delegation chain evidence;
- model-generated rationale accepted as authority evidence.

This document provides the guidance model.

The negative test document provides candidate failure cases.

## Example Scenarios

### Safe bounded delegation

Agent A delegates analysis to Agent B with a limited API call budget and a defined target dataset.

Agent B validates the limit, performs work within the budget, and records resource use evidence.

### Unsafe unbounded delegation

Agent A delegates a task without a budget limit.

Agent B performs repeated external API calls and delegates subtasks to additional agents.

The system cannot reconstruct whether the resource use was authorized.

### Reauthorization for budget expansion

Agent B determines that the delegated budget is insufficient.

The workflow pauses and requests explicit reauthorization for the additional resource use.

The reauthorization decision is linked to the original delegation request.

### Task splitting to bypass budget

Agent A's delegated request is refused because it would exceed budget.

Agent A splits the task into multiple smaller delegations.

The system should correlate the related requests and enforce the aggregate budget constraint.

## Implementation-Neutral Mechanisms

AAEF does not require a specific budget enforcement technology.

Possible mechanisms may include:

- policy engine decisions;
- gateway-enforced quota limits;
- workflow budget ledgers;
- signed delegation assertions;
- session-scoped budget tokens;
- backend resource checks;
- API gateway rate limits;
- tenant or account quota systems;
- cost accounting systems;
- task-level execution budgets;
- append-only evidence records;
- SIEM or audit log correlation.

These mechanisms are examples only.

AAEF should define the authority, constraint, enforcement, and evidence properties rather than mandate a specific implementation.

## Relationship to Existing AAEF Materials

This document relates to:

- `docs/en/31-cross-agent-cross-domain-authority.md`
- `docs/en/50-authority-lifecycle-model.md`
- `docs/en/56-capability-scoped-cross-agent-delegation.md`
- `docs/en/57-cross-agent-delegation-negative-tests.md`

It also supports the v0.5.x follow-up issue for cross-agent budget propagation and the open Cross-Agent and Cross-Domain Authority umbrella issue.

## Future Incorporation Questions

Future work should decide:

- whether cross-agent budget propagation remains guidance or becomes a control requirement;
- which budget or resource constraints should be required for selected high-impact contexts;
- whether resource constraints should become evidence schema candidates;
- whether assessment profiles should consider resource propagation;
- how aggregate budget tracking should be tested;
- how budget propagation should interact with approval, reauthorization, and escalation;
- whether budget propagation belongs under authority, governance, evidence, or a dedicated cross-agent control area.

## Non-Goals

This document does not:

- add new control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- change testing procedures;
- require a specific quota, billing, token, identity, or gateway technology;
- require all low-risk delegated actions to carry heavyweight budget metadata;
- claim that model-generated estimates are sufficient evidence of resource authorization.

Any normative incorporation must be handled through a later PR that explicitly updates the relevant control, testing, evidence, assessment, schema, mapping, or release artifacts.
