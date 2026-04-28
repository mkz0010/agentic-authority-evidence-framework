# v0.5.0 Planning Overview

**Status:** v0.5.0 planning overview
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Planning document for the next major public review design cycle

## Purpose

This document summarizes the intended direction for AAEF v0.5.0 planning.

AAEF v0.4.0 and v0.4.1 focused on enterprise assessment usability, control-specific testing criteria, external mapping methodology, and public review refinement.

AAEF v0.5.0 planning shifts toward deeper authority semantics for agentic AI systems, especially where authority changes over time, crosses agents, crosses domains, or is denied and re-requested.

This document does not add new controls, schema fields, or assessment requirements by itself. It organizes the main design themes that may later become control, schema, testing, or architecture refinements.

For control design tradeoffs before changing the catalog, see `docs/en/34-v050-control-design-options.md`.

## v0.5.0 Core Design Themes

The initial v0.5.0 planning work is organized around three related concepts:

1. Principal Context Degradation
2. Cross-Agent and Cross-Domain Authority
3. Authority Denial and Reauthorization Flow
4. Risk-Proportional Evidence and Performance Overhead
5. Tamper-Evident Evidence Storage
6. Approval Quality and Approval Fatigue

Together, these concepts refine AAEF's core claim that model output is not authority.

For approval quality and approval fatigue planning, see `docs/en/39-approval-quality-approval-fatigue.md`.

They focus on whether authority remains valid, traceable, bounded, and reviewable across time, delegation, agent boundaries, trust domains, and denial or reauthorization paths.

## Theme 1: Principal Context Degradation

See: `docs/en/30-principal-context-degradation.md`

Principal Context Degradation addresses cases where principal context is technically present but no longer sufficient for safe authorization.

This may occur because of:

- temporal staleness;
- semantic drift;
- scope drift;
- delegation drift;
- context substitution;
- runtime state change.

The main design question is whether AAEF should treat degraded principal context as:

- an ambiguity condition;
- a reauthorization trigger;
- a reason for denial or escalation;
- an evidence requirement;
- a dedicated control requirement;
- or a strengthening of existing Principal Binding controls.

## Theme 2: Cross-Agent and Cross-Domain Authority

See: `docs/en/31-cross-agent-cross-domain-authority.md`

For the non-normative authority assertion planning profile, see `docs/en/35-authority-assertion-profile.md`.

Cross-Agent and Cross-Domain Authority addresses cases where one agent, workflow, system, or organization relies on another agent's identity, authority claims, delegated scope, evidence, or execution results.

The core principle is:

> Agent-to-agent communication does not imply authority.

The main design question is whether AAEF should define stronger guidance for:

- cross-agent authority verification;
- receiving-side authorization;
- external agent identity and operator accountability;
- cross-domain authority assertions;
- delegation acceptance policy;
- cross-domain evidence exchange;
- revocation and freeze propagation across trust boundaries.

## Theme 3: Authority Denial and Reauthorization Flow

See: `docs/en/32-authority-denial-reauthorization-flow.md`

For the non-normative risk-proportional evidence planning profile, see `docs/en/36-risk-proportional-evidence-profile.md`.

Authority Denial and Reauthorization Flow addresses what happens after a high-impact action is denied, deferred, escalated, or found to have insufficient authority.

The core principle is:

> A denied action must not become an alternate path to execution.

The main design question is whether AAEF should strengthen guidance for:

- scoped reauthorization;
- principal reconfirmation;
- retry controls;
- task splitting detection;
- safe termination;
- non-execution evidence;
- reauthorization evidence;
- linkage between denial, escalation, reauthorization, and final execution or non-execution outcomes.

## Relationship Among the Three Themes

These themes are intentionally connected.

| Theme | Key dependency |
| --- | --- |
| Principal Context Degradation | May trigger denial, escalation, or reauthorization when context is stale or ambiguous. |
| Cross-Agent and Cross-Domain Authority | May cause principal context loss, delegation drift, evidence trust gaps, or revocation propagation gaps. |
| Authority Denial and Reauthorization Flow | Provides the controlled path when authority is insufficient, degraded, ambiguous, or unverifiable. |

A future v0.5.0 design should avoid treating these as isolated features.

For example:

- degraded principal context in a long-running workflow may require scoped reauthorization;
- cross-domain authority gaps may require receiving-side denial or external evidence verification;
- repeated denial in a cross-agent workflow may indicate attempted policy bypass or task splitting;
- revocation in one domain may require downstream freeze, denial, or residual-risk evidence in another domain.

## Candidate v0.5.0 Refinement Areas

Future v0.5.0 work may refine the following areas.

### Definitions

Candidate additions or refinements:

- Principal Context Degradation
- Cross-Agent and Cross-Domain Authority
- Authority Assertion
- Reauthorization Flow
- Principal Reconfirmation
- Delegation Drift
- Scope Drift
- Evidence Trust Gap

### Control Requirements

Candidate approaches:

- strengthen `AAEF-PRN-02`;
- strengthen `AAEF-DEL-*` controls for cross-agent and cross-domain delegation;
- strengthen `AAEF-AUZ-09`;
- strengthen `AAEF-EVD-05` and `AAEF-EVD-06`;
- add dedicated cross-agent authority controls if necessary;
- avoid unnecessary control sprawl where existing controls can be clarified.

### Evidence Schema

Candidate evidence topics:

- context age;
- principal reconfirmation;
- degradation assessment result;
- authority assertion reference;
- authority verification result;
- cross-domain evidence reference;
- related prior denial IDs;
- task splitting correlation;
- post-reauthorization effective scope;
- residual trust limitation.

Schema additions should be made only where they can be generated by trusted workflow, authorization, evidence, or enforcement components. They should not rely solely on model self-assessment.

### Testing Procedures

Candidate testing refinements:

- long-running workflow context freshness tests;
- cross-agent delegation tests;
- receiving-side authorization tests;
- denied action retry tests;
- scope creep and task splitting tests;
- principal reconfirmation tests;
- reauthorization evidence linkage tests;
- cross-domain evidence limitation tests.

### Reference Architecture

Candidate architecture refinements:

- receiving-side enforcement point guidance;
- cross-domain authority verification placement;
- authority assertion validation;
- reauthorization path handling;
- denial and non-execution evidence generation;
- revocation and freeze propagation assumptions.

## Non-Goals for v0.5.0 Planning

v0.5.0 planning should not assume that AAEF will define:

- a universal agent-to-agent protocol;
- a universal identity system;
- a universal cross-domain trust fabric;
- a certification scheme;
- a complete AI governance framework;
- a complete implementation of external frameworks;
- model self-assessment as authority;
- instantaneous global revocation across distributed systems.

AAEF should remain focused on agentic action assurance.

## Proposed v0.5.0 Planning Sequence

A conservative sequence is:

1. Establish concept notes.
2. Decide whether each concept requires new controls or strengthened existing controls.
3. Identify minimum evidence schema changes.
4. Update testing procedures only after control semantics are stable.
5. Update reference architecture and assessment guidance.
6. Prepare a v0.5.0 public review release once the design is coherent.

## Current Planning Status

| Issue | Topic | Status |
| --- | --- | --- |
| #2 | Principal Context Degradation | Concept note added; follow-up control and schema decisions remain. |
| #3 | Cross-Agent and Cross-Domain Authority | Concept note added; follow-up control and schema decisions remain. |
| #21 | Authority Denial and Reauthorization Flow | Concept note added; follow-up control, testing, and schema decisions remain. |

Additional v0.5.x topics may include approval quality, tamper-evident evidence storage, and risk-proportional evidence overhead.
