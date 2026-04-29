# Capability-Scoped Cross-Agent Delegation

**Status:** Non-normative v0.5.x follow-up guidance

## Purpose

This document defines non-normative guidance for capability-scoped cross-agent delegation in AAEF.

It addresses follow-up work from the v0.5.0 Cross-Agent and Cross-Domain Authority planning work.

The purpose is to clarify that cross-agent delegation should be evaluated at the capability, action, resource, and constraint level rather than merely at the agent identity level.

This document does not add new control IDs and does not change the v0.4.1 control and assessment baseline.

## Core Principle

Inter-agent communication is not delegation authority.

An agent may be allowed to communicate with another agent without being authorized to:

- delegate work;
- invoke a specific capability;
- spend money or consume bounded resources;
- access sensitive data;
- perform a high-impact action;
- act outside the original principal's scope;
- redelegate work to downstream agents;
- cross an organizational, tenant, system, or trust boundary.

A receiving agent should not infer authority from the requesting agent's identity or communication channel alone.

## Problem Statement

In multi-agent systems, agent identity and delegation authority are often conflated.

For example:

- Agent A may be allowed to ask Agent B for status information.
- Agent A may not be allowed to ask Agent B to perform a production change.
- Agent A may be allowed to request analysis but not make a financial commitment.
- Agent A may have authority for one tenant, account, environment, or principal but not another.
- Agent A may have authority to delegate once, but not to authorize downstream redelegation.

AAEF treats these as different authority states.

The ability to reach another agent is only a communication property. It does not prove delegated authority.

## Capability-Scoped Delegation Model

A cross-agent delegation should be scoped to a specific capability or capability class.

A capability-scoped delegation should identify, at minimum:

| Element | Description |
| --- | --- |
| Delegating principal | The human, organization, service, workflow, or policy source on whose behalf delegation is authorized. |
| Requesting agent | The agent or runtime initiating the cross-agent request. |
| Receiving agent | The agent, service, tool, workflow, or domain expected to receive the delegated request. |
| Delegated capability | The capability, action class, or bounded function being delegated. |
| Target or resource scope | The account, tenant, environment, system, object, data class, or resource boundary affected. |
| Allowed operation | The permitted operation, such as read, analyze, draft, propose, execute, modify, approve, or escalate. |
| Prohibited operation | Operations explicitly outside the delegated scope. |
| Validity window | Time, session, workflow, task, or authorization lifetime constraints. |
| Resource constraints | Budget, quota, rate, token, execution time, external API, or cost constraints. |
| Delegation depth | Whether downstream redelegation is prohibited, limited, or requires reauthorization. |
| Evidence expectations | Evidence needed to prove authority validation, acceptance, refusal, denial, or execution. |
| Revocation handling | How revocation, expiry, or downscoping is detected and enforced. |

These elements may be represented through different implementation technologies.

AAEF does not require a specific credential, token, identity, or signing mechanism at this stage.

## Receiving-Side Validation Expectations

A receiving agent should validate a delegated request before acting on it.

Receiving-side validation should not be limited to whether the requester is known.

It should determine whether the requester is authorized for the requested capability, target, operation, and constraints.

A receiving agent should evaluate:

- whether the requesting agent is recognized;
- whether the request includes or references a valid delegation authority;
- whether the delegated capability matches the requested action;
- whether the target or resource is within scope;
- whether the authority is fresh and unexpired;
- whether the authority has been revoked or downscoped;
- whether the delegation depth permits the requested handoff;
- whether the requested operation exceeds the delegated capability;
- whether resource or budget constraints are present and enforceable;
- whether required evidence can be generated;
- whether human approval or reauthorization is required.

If validation fails, the receiving agent should deny, refuse, defer, or escalate rather than act.

## Distinguishing Communication, Delegation, and Execution

AAEF distinguishes three related but separate states.

| State | Meaning | Authority implication |
| --- | --- | --- |
| Communication allowed | One agent may send a message or request to another agent. | Does not imply delegated authority. |
| Delegation accepted | The receiving agent accepts a bounded delegated task. | Requires capability-scoped authority validation. |
| Execution authorized | The receiving agent or backend may perform the action. | Requires action-specific authorization and enforcement. |

A system may allow communication while denying delegation.

A system may accept delegation while still requiring separate execution authorization.

A system may deny execution while preserving evidence of the delegation request and refusal.

## Candidate Control Expectations

The following are non-normative candidate expectations for future control refinement.

They may later become guidance, testing criteria, evidence expectations, existing control refinements, or new control requirements.

### Capability-scoped authority verification

A receiving agent should verify that a cross-agent request is authorized for the specific capability, target, operation, and scope requested.

Agent identity alone should not be sufficient.

### Delegation intent binding

The delegated request should be bound to the original principal intent, authorization context, or policy decision.

If the original principal context is stale, ambiguous, missing, or degraded, the request should require reconfirmation or reauthorization before proceeding.

### Explicit acceptance or refusal

The receiving agent should explicitly accept, refuse, defer, or escalate a delegated request before the requesting agent treats the delegated task as active.

A fire-and-forget request should not be treated as accepted delegation.

### Scope mismatch denial

If the requested action exceeds the delegated capability, resource scope, validity window, or operation class, the receiving agent should deny or refuse the request.

### Downstream delegation control

A delegated task should not automatically authorize redelegation to additional downstream agents.

Downstream delegation should be explicitly allowed, depth-limited, and evidenced.

### Resource and budget propagation

Delegated agents should inherit bounded resource constraints where relevant.

A delegated agent should not receive unlimited budget, quota, execution authority, external API use, or resource access merely because a task was delegated.

### Evidence of validation

The system should generate evidence showing whether delegated authority was validated, accepted, refused, denied, expired, revoked, or exceeded.

For high-impact or audit-grade contexts, evidence should be sufficient to reconstruct the cross-agent authority path.

## Candidate Evidence Expectations

For cross-agent delegation, useful evidence may include:

- delegation request identifier;
- requesting agent identity;
- receiving agent identity;
- delegating principal or policy source;
- delegated capability;
- requested operation;
- target or resource scope;
- accepted, refused, deferred, denied, or escalated state;
- refusal or denial reason;
- authority assertion reference;
- authorization decision reference;
- validity window;
- revocation or expiry check result;
- delegation depth;
- downstream delegation decision;
- budget or resource constraint;
- evidence of receiving-side validation;
- linkage to original action, task, workflow, or principal context.

These fields are candidates for future guidance or schema consideration.

They are not required evidence schema fields in this document.

## Anti-Patterns

The following patterns should be treated as weak or unsafe.

| Anti-pattern | Risk |
| --- | --- |
| Agent identity implies all delegation authority | Overbroad authority and privilege amplification. |
| Communication channel trust implies action authority | Cross-agent requests may bypass authorization checks. |
| Fire-and-forget delegation | The requesting agent may assume work will occur without explicit acceptance. |
| Unbounded downstream redelegation | Accountability and authority lineage become difficult to reconstruct. |
| Missing resource constraints | Delegated agents may exhaust budget, quota, compute, or external service limits. |
| Model-generated delegation rationale only | The evidence may explain a request without proving authority. |
| Stale delegation accepted | Expired or revoked authority may be reused. |
| Scope mismatch ignored | A delegated task may mutate into a higher-impact action. |

## Implementation-Neutral Mechanisms

AAEF does not require a specific technology for capability-scoped delegation.

Possible implementation mechanisms may include:

- signed authority assertions;
- session-scoped delegation tokens;
- workload identity;
- mTLS-backed service identity;
- OIDC federation;
- organization PKI;
- SPIFFE/SPIRE;
- DID/VC-based credentials;
- policy engine decisions;
- gateway-enforced delegation policies;
- workflow-issued delegation references;
- transparency logs or append-only evidence stores.

These mechanisms are examples only.

AAEF should define the authority and evidence properties required, not prematurely mandate a specific credential technology.

## Relationship to Existing AAEF Materials

This document relates to:

- `docs/en/31-cross-agent-cross-domain-authority.md`
- `docs/en/46-cross-agent-authority-examples.md`
- `docs/en/50-authority-lifecycle-model.md`
- `docs/en/53-v050-release-scope-decision.md`
- `docs/en/55-researcher-overview.md`

It also relates to the open Cross-Agent and Cross-Domain Authority umbrella issue and the v0.5.x follow-up issues for delegation acceptance, chain accountability, and budget propagation.

## Negative Test Follow-up

Cross-agent delegation negative test guidance is maintained in `docs/en/57-cross-agent-delegation-negative-tests.md`.

That document covers failure modes for communication mistaken for authority, missing explicit acceptance, refusal propagation failure, scope mismatch, delegation chain accountability, downstream redelegation, budget propagation, retry pressure, task splitting, and evidence omission.

## Open Design Questions

Future work should decide:

- whether capability-scoped delegation remains guidance or becomes a control requirement;
- whether a dedicated cross-agent authority control domain is needed;
- which minimum authority assertion elements should be required;
- how receiving-side validation should be tested;
- how delegation acceptance and refusal should be evidenced;
- how downstream delegation depth should be limited;
- how cross-agent budget propagation should be enforced;
- whether evidence schema candidates should be introduced for cross-agent authority;
- how this model should align with high-impact and audit-grade assessment profiles.

## Non-Goals

This document does not:

- create a new AAEF control domain;
- add new control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- change testing procedures;
- require a specific identity, credential, or token technology;
- claim that cross-agent delegation is solved by model output, prompting, or agent self-report.

Any normative incorporation must be handled through a later PR that explicitly updates the relevant control, testing, evidence, assessment, schema, mapping, or release artifacts.
