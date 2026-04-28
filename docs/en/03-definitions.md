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

## Action Assurance

The ability to verify that an agentic action was performed by an identified agent, on behalf of a known principal, within delegated authority, allowed at the point of execution, recorded with sufficient evidence, and subject to revocation and review.
