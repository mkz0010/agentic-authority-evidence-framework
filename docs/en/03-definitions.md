# 03. Definitions

This section defines initial terminology for AAEF v0.1.

## Agent

A software-based non-human actor that can interpret instructions, use tools, access resources, or perform actions on behalf of a human, organization, system, or another agent.

## Agentic AI System

A system that includes one or more AI agents capable of planning, tool use, workflow execution, delegation, or interaction with external systems.

## Agent Product

The software, model, service, or platform that provides agent capabilities.

## Agent Instance

A specific running instance of an agent product, within a particular runtime, tenant, session, workflow, or execution context.

## Principal

The human, organization, system, or upstream agent on whose behalf an agent acts.

## Operator

The person or organization responsible for deploying, configuring, maintaining, or governing an agent or agent platform.

## Issuer

An entity that issues an identity, credential, token, authority grant, or attestation used by an agentic AI system.

## Relying Party

A system, service, tool, or organization that relies on an agent identity, authority grant, authorization decision, or evidence record.

## Delegation

The act of granting a limited authority from one principal, agent, or system to another agent, tool, service, or workflow.

## Delegation Chain

A sequence of delegations from an original principal to downstream agents, tools, services, or workflows.

## Attenuated Delegation

Delegation in which the delegated authority is strictly equal to or narrower than the delegator's authority.

## Authority

The permitted ability to perform specified actions on specified resources under specified conditions.

## Authority Scope

The structured definition of actions, resources, purposes, constraints, duration, and conditions associated with an authority grant.

## Action

An operation performed by an agent, tool, service, or workflow that may affect data, systems, people, money, rights, obligations, or external parties.

## High-Impact Action

An action that may create significant operational, financial, legal, privacy, security, safety, or reputational impact.

## Action Boundary

The point at which an intended agent action becomes an actual tool invocation, API request, workflow execution, external communication, state change, or transaction.

## Authorization Decision

A decision to allow, deny, require approval, require additional verification, or escalate an attempted action.

## Evidence

Structured information that supports verification of an agentic action, authority grant, authorization decision, delegation chain, approval, result, or revocation.

## Verifiable Evidence

Evidence that is attributable, structured, reviewable, and resistant to undetected alteration to a degree appropriate for the risk level.

## Revocation

The act of invalidating or withdrawing trust, authority, credentials, delegation, tool access, memory access, or agent participation.

## Trust Domain

A boundary within which identities, authorities, policies, evidence, and revocation decisions are governed under a common authority.

## Principal Context

The information required to determine on whose behalf an agent action is attempted or performed. Principal context may include user identity, organization, tenant, session, role, purpose, authority grant, delegation chain, and correlation identifiers.

See also: `docs/en/30-principal-context-degradation.md` for the v0.5.0 planning concept of Principal Context Degradation.

## Principal Context Degradation

The loss, weakening, staleness, semantic drift, or ambiguity of the information required to determine on whose behalf an agentic action is attempted or performed.

Principal context may degrade even when an identifier, session, workflow reference, or authority grant is still present.

## Cross-Agent and Cross-Domain Authority

The problem of determining whether one agent, system, workflow, or organization may rely on another agent's identity, authority claims, delegated scope, evidence, or execution results.

Agent-to-agent communication does not itself imply authority.

## Authority Denial and Reauthorization Flow

The controlled process by which an agentic system handles a high-impact action that cannot safely proceed under the currently available authority.

This may include denial, deferral, escalation, scoped reauthorization, principal reconfirmation, retry control, safe termination, or non-execution evidence.

## Authority Assertion

A structured claim or evidence reference that represents agent identity, principal context, delegated scope, authority basis, constraints, expiration, revocation state, or related evidence for an agentic action or delegation.

AAEF does not require a specific authority assertion format or protocol.

## Principal Reconfirmation

A process by which the relevant principal, authorized representative, or trusted authority source confirms that a requested action, scope, purpose, or delegation remains intended and authorized.

Principal reconfirmation may be required when principal context is stale, degraded, ambiguous, or materially changed.

## Scope Drift

A change in requested or effective authority scope such that the action, resource, purpose, amount, tenant, tool, destination, or impact differs from the originally authorized scope.

Scope drift may require denial, escalation, or reauthorization for high-impact actions.

## Delegation Drift

A change or weakening in delegated authority semantics as work passes through agents, tools, services, workflows, or trust domains.

Delegation drift may occur when downstream authority no longer clearly reflects the original principal context, delegated scope, constraints, or revocation state.

## Evidence Trust Gap

A limitation in the ability to rely on evidence generated by another component, agent, system, organization, or trust domain.

Evidence trust gaps may occur when evidence cannot be correlated, independently verified, linked to authorization, linked to execution or non-execution, or evaluated for completeness and integrity.

## Action Assurance

The ability to verify that an agentic action was performed by an identified agent, on behalf of a known principal, within delegated authority, allowed at the point of execution, recorded with sufficient evidence, and subject to revocation and review.
