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

## Recommended Reading Order

The v0.5.0 planning materials are intended to be read in the following order.

1. Start with this overview to understand the planning scope, current status, and remaining work.
2. Read the core concept notes to understand the authority, denial, reauthorization, and cross-domain design problems.
3. Read the planning profiles to understand candidate control, evidence, and assessment design options.
4. Read the example documents to understand how the planning concepts may appear in review, assessment, or incident reconstruction.
5. Read the schema field candidates last, because they are planning candidates and do not change the current Evidence Event Schema.

## v0.5.0 Planning Document Index

### Overview and Control Design

| Document | Purpose |
| --- | --- |
| `docs/en/33-v050-planning-overview.md` | Overall v0.5.0 planning scope, status, examples, and remaining work. |
| `docs/en/34-v050-control-design-options.md` | Candidate control design options for future v0.5.0 work. |

### Core Concept Notes

| Document | Purpose |
| --- | --- |
| `docs/en/31-cross-agent-cross-domain-authority.md` | Cross-agent and cross-domain authority planning concept. |
| `docs/en/32-authority-denial-reauthorization-flow.md` | Authority denial, non-execution, retry, and reauthorization flow planning concept. |
| `docs/en/39-approval-quality-approval-fatigue.md` | Approval quality, blind approval, approval fatigue, and meaningful human review planning concept. |

### Planning Profiles and Assessment Guidance

| Document | Purpose |
| --- | --- |
| `docs/en/35-authority-assertion-profile.md` | Candidate authority assertion profile for cross-agent and cross-domain authority claims. |
| `docs/en/36-risk-proportional-evidence-profile.md` | Risk-proportional evidence depth planning profile. |
| `docs/en/37-tamper-evident-evidence-storage.md` | Tamper-evident evidence storage planning profile. |
| `docs/en/43-risk-proportional-evidence-assessment-guidance.md` | Assessment guidance for applying E0 through E5 evidence depth levels. |

### Field Candidates

| Document | Purpose |
| --- | --- |
| `docs/en/38-v050-evidence-schema-field-candidates.md` | Candidate Evidence Event Schema fields for future schema refinement. |

### Non-Normative Examples

| Document | Purpose |
| --- | --- |
| `docs/en/40-approval-evidence-examples.md` | Approval evidence, weak approval, approval laundering, and approval fatigue examples. |
| `docs/en/41-non-execution-reauthorization-examples.md` | Denial, deferral, safe termination, retry, task splitting, and reauthorization examples. |
| `docs/en/42-tamper-evident-evidence-examples.md` | Tamper-evident, independently corroborated, replay, omission, and integrity verification examples. |
| `docs/en/44-evidence-depth-examples.md` | E3, E4, and E5 evidence depth examples. |

These documents are non-normative planning materials unless otherwise stated. They are intended to support discussion before future schema, control, testing, or assessment changes are adopted.

## Current Planning Status

The following table summarizes selected v0.5.0 planning threads and their current status.

| Issue / Thread | Area | Completed Planning Work | Remaining Planning Work |
| --- | --- | --- | --- |
| #2 | Principal Context Degradation | Concept note added; planning definitions and related control language strengthened in the v0.5.0 planning cycle. | Schema decisions, assessment guidance, and additional negative tests remain. |
| #3 | Cross-Agent and Cross-Domain Authority | Concept note added; authority assertion planning profile added; cross-agent authority lineage strengthened. | Schema decisions, assessment guidance, and additional delegation or lineage negative tests remain. |
| #6 | Approval quality and approval fatigue | Approval quality concept added; `AAEF-AUZ-03`, `AAEF-HUM-01`, and `AAEF-HUM-02` strengthened; approval evidence examples added. | Approval quality metrics, approval fatigue assessment guidance, approval laundering negative tests, and potential dedicated approval quality control decisions remain. |
| #19 | Tamper-evident evidence storage | Tamper-evident evidence storage profile added; `AAEF-EVD-04` strengthened; tamper-evident evidence examples added. | Evidence integrity schema field decisions, negative tests for tampering and replay, and incident-response evidence preservation guidance remain. |
| #20 | Risk-proportional evidence depth | Risk-proportional evidence profile added; assessment guidance added; evidence depth field candidates added; evidence depth examples added. | Schema adoption decisions for `evidence_depth_level`, required depth by action class, assessment profile integration, and JSON examples remain. |
| #21 | Authority denial and reauthorization flow | Authority denial and reauthorization concept added; `AAEF-EVD-05` and `AAEF-EVD-06` strengthened; non-execution and reauthorization examples added. | Non-execution and reauthorization JSON examples, retry and task-splitting negative tests, and schema field decisions remain. |

These items remain planning work. They do not establish certification requirements or final schema requirements.


## Planning Examples

The following non-normative example documents illustrate how selected v0.5.0 planning concepts may be reviewed in practice.

- Approval evidence examples: `docs/en/40-approval-evidence-examples.md`
- Non-execution and reauthorization examples: `docs/en/41-non-execution-reauthorization-examples.md`
- Tamper-evident evidence examples: `docs/en/42-tamper-evident-evidence-examples.md`
- Risk-proportional evidence assessment guidance: `docs/en/43-risk-proportional-evidence-assessment-guidance.md`
- Evidence depth examples: `docs/en/44-evidence-depth-examples.md`
- Principal context degradation examples: `docs/en/45-principal-context-degradation-examples.md`
- Cross-agent authority examples: `docs/en/46-cross-agent-authority-examples.md`
