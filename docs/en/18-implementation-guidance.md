# Implementation Guidance

**Status:** Non-normative implementation guidance

## Purpose

This document provides implementation guidance for applying AAEF concepts in agentic AI systems.

It sits between the reference architecture and open research questions to help implementers understand how the framework can be adopted without treating planning notes, model output, or implementation-specific behavior as authority.

This document does not introduce new control requirements and does not change the control catalog, evidence schema, assessment worksheet, assessment profiles, or testing procedures.

## Implementation Objectives

AAEF implementations should preserve the core separation between:

- model output;
- authority to act;
- tool or action execution;
- evidence generation;
- assessment and audit review.

The main implementation objective is to ensure that agentic actions are authorized, executed, evidenced, and reviewable through trusted components rather than relying on model-generated explanations or agent runtime self-reporting.

## Recommended Adoption Path

A practical implementation can proceed in stages.

| Stage | Objective | Expected result |
| --- | --- | --- |
| Identify authority-bearing actions | Determine which actions require authorization, evidence, or human approval. | High-impact and authority-bearing action inventory. |
| Separate model output from authority | Prevent model output from being treated as authorization. | Authorization decisions come from trusted workflow, policy, backend, or approval components. |
| Place enforcement near execution | Ensure tool dispatch and backend execution check authorization before action. | Action execution is gated by trusted enforcement points. |
| Capture action-bound evidence | Record evidence tied to the specific action, authorization decision, execution result, and relevant context. | Assessment and audit review can reconstruct what happened. |
| Test denial and failure paths | Verify that denied, expired, revoked, frozen, or unauthorized actions do not execute through alternate paths. | Negative tests support control effectiveness. |
| Review evidence quality | Confirm that evidence is independently generated or corroborated where required. | Evidence is not limited to model or runtime self-reporting. |

## Component Placement Guidance

AAEF does not require a specific product architecture, identity system, agent framework, or deployment model.

However, implementers should identify which components perform the following roles:

- principal binding;
- authorization decision;
- policy evaluation;
- tool dispatch enforcement;
- backend execution enforcement;
- human approval collection;
- evidence generation;
- evidence storage;
- assessment review.

In higher-risk systems, these roles should not all be performed by the model or by an untrusted agent runtime alone.

## Minimum Implementation Expectations

A minimal AAEF-aligned implementation should be able to show:

- which actions are authority-bearing;
- which component decides whether an action is authorized;
- which component enforces the decision before execution;
- what evidence is generated for the action;
- whether evidence can be tied to the specific action and authorization context;
- how denied or unauthorized actions are prevented from executing;
- which residual risks remain outside the implementation boundary.

This minimum does not imply certification or full assurance. It provides a starting point for implementation and assessment discussion.

## Common Implementation Anti-Patterns

Implementers should avoid the following patterns:

- treating model output as authorization;
- treating a user prompt as durable authority for future actions;
- relying only on agent runtime logs as evidence;
- allowing tool calls to bypass authorization checks;
- allowing denied actions to be retried through alternate tools;
- using human approval without recording approved action, scope, risk context, and approver identity;
- assuming that framework-level integration automatically satisfies assessment expectations;
- treating non-normative planning material as current control requirements.

## Relationship to the Reference Architecture

The reference architecture describes the conceptual components and trust boundaries used by AAEF.

This implementation guidance explains how those concepts can be adopted incrementally in real systems.

Implementers should read this document together with:

- `docs/en/17-reference-architecture.md`;
- `docs/en/20-assessment-profiles.md`;
- `docs/en/25-testing-procedures-and-pass-criteria.md`;
- `docs/en/27-trusted-control-boundary-integrity.md`;
- `docs/en/33-v050-planning-overview.md`.

## Relationship to v0.5.0 Planning Material

v0.5.0 planning documents remain non-normative unless explicitly incorporated into control, schema, assessment, testing, or release artifacts.

This document may help implementers understand the direction of future planning work, but it does not make any v0.5.0 planning concept mandatory.

## Assessment Use

Assessors may use this document as interpretive guidance when discussing implementation architecture, evidence sources, and action-bound enforcement.

Assessment conclusions should still be based on the applicable control requirements, assessment methodology, testing procedures, evidence schema, and assessment profile in effect for the reviewed version of AAEF.
