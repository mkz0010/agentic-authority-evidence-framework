# 02. Core Principles

AAEF is based on the following principles.

## Principle 1: Model Output Is Not Authority

A model output is not authority.

An AI agent may recommend, plan, summarize, or decide that an action should be taken. That does not mean the organization has authorized the action.

For high-impact actions, model output must not be directly converted into tool execution authority. Authorization must be evaluated separately at the action boundary.

## Principle 2: Delegation Must Be Attenuated

Delegation must reduce authority, not expand it.

When an agent delegates to another agent, tool, service, or workflow, the delegated authority must be a subset of the authority held by the delegating party.

Delegation should be constrained by:

- action type,
- resource,
- purpose,
- duration,
- maximum amount,
- maximum count,
- delegation depth,
- redelegation permission,
- and revocation conditions.

If authority increases through delegation, the system has created an escalation path.

## Principle 3: Authorization Must Be Enforced at the Action Boundary

Authorization must be enforced when an action is attempted, not only when a conversation begins.

For every high-impact action, the system should evaluate:

- agent identity,
- agent instance,
- principal,
- operator,
- requested action,
- target resource,
- authority scope,
- purpose,
- risk level,
- required approval,
- evidence requirement,
- and revocation status.

AAEF distinguishes between the authorization layer and the tool dispatch layer. The authorization layer decides whether an action is permitted based on trusted policy inputs and system state. The tool dispatch layer ensures that a tool is not executed merely because untrusted content caused the model to request it. Both layers are necessary for high-impact actions.

## Principle 4: Evidence Must Be Verifiable

Logs are not automatically evidence.

Operational logs may be an important evidence source, but they become useful evidence for agentic action assurance only when they are sufficiently structured, attributable, context-bound, reviewable, and protected against undetected alteration to a degree appropriate for the action risk.

For AAEF, evidence should support verification of at least:

- which agent and agent instance acted,
- which principal the action was bound to,
- what authority scope applied,
- what action was requested,
- what policy decision was made,
- whether approval was required and obtained,
- what tool or external system was invoked,
- what result occurred,
- and whether trust or authority was later revoked.

A SIEM event, application log, workflow trace, or audit record may satisfy part of this requirement. However, a raw log line that cannot be linked to authority, principal, decision, and result is not sufficient by itself for high-impact agentic action assurance.

For high-impact actions, evidence should be structured, retained, attributable, and tamper-evident where appropriate.

## Principle 5: Trust Must Be Revocable

Trust must not be permanent.

An organization must be able to revoke:

- agent identity,
- agent instance trust,
- delegated authority,
- tokens or credentials,
- tool permissions,
- memory access,
- data access,
- and downstream delegations.

If trust cannot be revoked, it cannot be safely granted.

## Principle 6: Human Approval Must Be Risk-Proportional

Human approval should be based on risk.

Low-risk actions may require logging only. Medium-risk actions may require additional evidence or policy checks. High-risk actions may require explicit human approval. Critical actions may require multi-party approval, separation of duties, or out-of-band confirmation.

Friction is not latency for its own sake. Friction is risk-proportional verification.

## Principle 7: Agent Autonomy Requires Stronger Boundaries

AAEF does not exist to prevent AI agents from being useful.

The purpose of AAEF is to allow organizations to grant greater autonomy safely by defining the conditions under which authority can be delegated, actions can be executed, evidence can be verified, and trust can be revoked.
