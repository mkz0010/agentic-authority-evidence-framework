# Principal Context Degradation

**Status:** Non-normative v0.5.0 planning concept note
**AAEF baseline:** v0.4.1 Public Review Draft
**Issue context:** #2

> **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifacts, testing procedures, or release notes.

## Purpose

This note defines Principal Context Degradation as a v0.5.0 planning concept for AAEF.

It explains how principal context can weaken, drift, become stale, or become ambiguous during long-running, delegated, asynchronous, or multi-agent workflows.

This document does not add new control requirements yet. It is intended to prepare future refinements to Principal Binding, Delegation and Authority, Action Authorization, Evidence, and Response controls.

## Definition

**Principal Context Degradation** is the loss, weakening, staleness, semantic drift, or ambiguity of the information required to determine on whose behalf an agentic action is attempted or performed.

Principal context may degrade even when some identifier is still present.

For example, a workflow may still carry a user ID or session ID, while the actual authority, purpose, scope, approval basis, or business intent has become too stale or ambiguous to safely authorize a high-impact action.

## Relationship to Principal Context

AAEF already defines principal context as the information required to determine on whose behalf an agent action is attempted or performed.

Principal context may include:

- user identity;
- organization or tenant;
- session;
- role;
- purpose;
- authority grant;
- delegation chain;
- workflow or correlation identifiers.

Principal Context Degradation focuses on whether that context remains sufficiently current, specific, bounded, and semantically connected to the action being attempted.

## Why This Matters

Agentic AI systems may operate across:

- long-running tasks;
- asynchronous workflows;
- background jobs;
- tool chains;
- queues;
- delegated subtasks;
- multi-agent workflows;
- retries and reauthorization flows;
- memory or retrieval influenced actions;
- cross-domain agent interactions.

In these environments, the original principal intent may become distant from the final action.

A high-impact action should not be authorized only because some prior principal context still exists. The system should evaluate whether the principal context remains valid for the specific action, resource, purpose, risk, and runtime state.

## Degradation Patterns

Principal context may degrade through several patterns.

### 1. Temporal Staleness

Authority, intent, approval, or session context becomes old enough that it may no longer reflect the principal's current intent or authorization.

Examples:

- a task continues hours or days after the original request;
- a scheduled agent resumes after the principal's role changed;
- an approval is reused after relevant business state changed.

### 2. Semantic Drift

The workflow objective changes gradually until the final action no longer matches the original principal intent.

Examples:

- a research task becomes a production change;
- a summarization task becomes an outbound communication;
- a recommendation task becomes an external transaction.

### 3. Scope Drift

The action expands beyond the originally authorized resource, amount, tool, destination, tenant, or purpose.

Examples:

- a task authorized for one repository affects multiple repositories;
- a task authorized for read-only analysis attempts a write operation;
- a delegated workflow expands from one customer record to a broader dataset.

### 4. Delegation Drift

Authority becomes unclear as work passes through agents, tools, services, or workflow steps.

Examples:

- downstream agents cannot identify the original principal;
- delegation depth exceeds the intended boundary;
- redelegation changes the action purpose or authority scope.

### 5. Context Substitution

Agent identity, tool identity, workflow identity, or model-generated rationale replaces principal context.

Examples:

- logs show which agent acted but not on whose behalf;
- the model explains why it acted, but no trusted principal authority record exists;
- a service account executes a high-impact action without traceable user or organizational authority.

### 6. Runtime State Change

Material state changes make previously valid context insufficient.

Examples:

- revocation occurs after authorization but before execution;
- policy version changes;
- a risk signal changes;
- the target resource changes;
- required evidence is missing or no longer valid.

## Relationship to Existing AAEF Controls

Principal Context Degradation is not a replacement for existing controls. It clarifies a failure mode that cuts across several control domains.

| Existing area | Relationship |
| --- | --- |
| `AAEF-PRN-01` | Requires each high-impact action to be bound to a principal. Degradation asks whether that binding remains meaningful at execution time. |
| `AAEF-PRN-02` | Requires principal context preservation across tools, workflows, and delegations. Degradation extends this from preservation to validity, freshness, and semantic continuity. |
| `AAEF-DEL-*` | Delegation controls help preserve authority lineage. Degradation asks whether downstream authority still reflects the original principal context and constraints. |
| `AAEF-AUZ-*` | Authorization controls should treat degraded principal context as ambiguity, missing authority, or a reauthorization trigger. |
| `AAEF-EVD-*` | Evidence should show how principal context was carried, refreshed, reconfirmed, or judged insufficient. |
| `AAEF-RES-*` | Revocation, freeze, denial, and isolation may be required when context degradation is detected. |

## Suggested Authorization Behavior

For high-impact actions, systems should treat material Principal Context Degradation as a reason to deny, defer, escalate, freeze, or require scoped reauthorization.

A system should not proceed with a high-impact action if it cannot determine:

- who or what the principal is;
- what authority basis applies;
- whether the authority is current;
- whether the action still matches the original purpose;
- whether delegation constraints still apply;
- whether relevant runtime state has changed;
- whether required evidence is available.

## Evidence Considerations

Future evidence refinements may need to represent:

- principal context reference;
- principal context age;
- authority grant age;
- original purpose;
- current requested purpose;
- purpose drift indicator;
- scope drift indicator;
- delegation depth;
- context refresh or reconfirmation event;
- reauthorization trigger;
- degradation assessment result;
- action taken after degradation was detected.

These fields should be added only if they can be generated by trusted workflow, authorization, evidence, or enforcement components. They should not depend solely on model self-assessment.

## Assessment Questions

Reviewers may ask:

1. Can high-impact actions be traced to the original principal and authority basis?
2. Does the system distinguish preserved context from valid context?
3. Are long-running workflows subject to context freshness or reauthorization rules?
4. Can delegated workflows prove that downstream actions remain within original authority constraints?
5. Are semantic drift and scope drift detected before high-impact execution?
6. Does missing or stale principal context cause denial, deferral, escalation, freeze, or reauthorization?
7. Is principal context degradation evidenced in a way that supports incident reconstruction?

## Non-Goals

This concept does not require:

- a specific identity protocol;
- a specific tracing system;
- a graph database;
- universal real-time revocation;
- model self-assessment of authority;
- storing sensitive principal data in evidence records.

Implementations may use privacy-preserving references, signed claims, correlation IDs, trace IDs, session-scoped authority tokens, workflow metadata, or structured delegation records.

## Future Work

Future v0.5.0 work may include:

- adding a formal definition to the definitions document;
- adding a dedicated control or strengthening `AAEF-PRN-02`;
- defining context freshness and degradation thresholds;
- adding evidence schema fields for context age, drift, and reconfirmation;
- integrating Principal Context Degradation with Authority Denial and Reauthorization Flow;
- connecting this concept to Cross-Agent and Cross-Domain Authority.

For v0.5.0 Principal Context Degradation examples, see `docs/en/45-principal-context-degradation-examples.md`.
