# AAEF v0.6.0 Planning Input Synthesis

Status: Planning input  
Related roadmap: #241  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document synthesizes planning input for AAEF v0.6.0.

The purpose of v0.6.0 is to convert selected v0.5.0 and v0.5.x planning material into practical adoption packages that can be evaluated by implementers, operators, auditors, legal and compliance teams, security architects, and risk owners.

v0.6.0 should not be treated as a direct expansion of the active control baseline by default. Instead, it should define the adoption-facing materials needed before selected planning concepts can be promoted into active artifacts in a future release.

## Planning theme

The proposed v0.6.0 theme is:

**AAEF v0.6.0: Practical Adoption Readiness**

This reflects a transition from:

> action assurance concept and planning

toward:

> adoptable implementation, operation, audit, and governance packages

## Baseline position

v0.6.0 planning does not automatically change the current control and assessment baseline.

The current active baseline remains the latest explicitly designated control and assessment baseline until active artifacts are updated.

v0.6.0 should therefore distinguish between:

- current active requirements
- planning concepts
- candidate guidance
- adoption support materials
- future candidate controls or profiles

This distinction is important because v0.6.0 is expected to package and evaluate adoption readiness without overstating normative status.

## Consolidated feedback themes

### 1. Existing standards auditor perspective

AAEF should not be positioned as a replacement for ISO 42001, NIST AI RMF, EU AI Act obligations, OWASP guidance, CSA guidance, or other existing standards.

However, AAEF can provide value as a supplementary audit and assessment layer for agentic action evidence.

The strongest audit-facing value is the ability to explain:

- who or what authorized an agentic action
- what action was requested
- what policy and context were used
- what was dispatched
- whether execution matched authorization
- what evidence supports the action record
- what evidence supports non-execution, refusal, override, or reauthorization

Planning implications:

- define an External Audit Pack
- define a Control-to-Evidence Matrix
- define a Testing Procedure Workbook
- define Evidence Population Definition guidance
- define Sample Selection Methodology guidance
- distinguish Design Effectiveness from Operating Effectiveness
- maintain conservative crosswalk language

### 2. Implementer perspective

AAEF appears implementable, but the current materials are not yet a direct SDK or implementation specification.

Implementers need practical entry points that show how AAEF concepts map to requests, authorization decisions, dispatch enforcement, backend verification, and evidence validation.

Planning implications:

- define an Implementer Quick Start
- define a Canonical Action Request JSON profile
- define an Authorization Decision Artifact minimal profile
- define a Dispatch Attestation profile
- define profile-aware evidence validation guidance
- provide a Reference Adapter or generic REST gateway example

### 3. Operational owner perspective

AAEF can become a production operations anchor for high-impact agentic actions, but Day-2 operations guidance needs to be made explicit.

Operational teams need to know who owns policies, evidence, alert handling, exception handling, retention, rollback, and incident response.

Planning implications:

- define an Operational Responsibility Matrix
- define an Operational Readiness Checklist
- define an Agentic Incident Response Runbook
- define a Monitoring and Alert Catalog
- define Evidence Retention and Cost Guidance
- define Policy Change and Rollback Guidance
- define Operational Metrics, SLO, and SLA examples

### 4. Legal and compliance perspective

AAEF should not claim legal compliance or certification.

Its legal and compliance value is to support explanations of authority, responsibility, evidence, accountability, and residual risk for agentic actions.

AAEF should use conservative language such as:

- AAEF supports assessment of a topic.
- AAEF may support evidence collection for a topic.
- AAEF can help demonstrate how authority and evidence were handled.

AAEF should avoid unsupported language such as:

- AAEF satisfies a legal requirement.
- AAEF guarantees compliance.
- AAEF certifies a system or organization.

Planning implications:

- define a Legal and Compliance Applicability Note
- define an Evidence Privacy and Retention Policy template
- define a Contractual Control Addendum
- define a SaaS / external agent responsibility matrix
- define a DPIA / AI Impact Assessment support template

### 5. Security architect perspective

AAEF's boundary model is a strong basis for agentic action assurance.

The next requirement is to clarify minimum production architecture expectations, especially for the Trusted Control Boundary, authorization artifacts, relying-party verification, tool gateways, policy engines, and SIEM placement.

Planning implications:

- classify current Architecture Requirements, Planning Concepts, and Future Candidates
- define a High-Impact Production Minimum Architecture Profile
- define a TCB Hardening Profile
- define an Authorization Decision Artifact minimal profile
- define Backend Relying Party Verification examples
- define MCP, tool gateway, policy engine, and SIEM reference placement examples

### 6. Risk owner and executive perspective

AAEF can support risk ownership for high-impact AI agent actions, but executive-facing materials must be compressed and decision-oriented.

Risk owners need adoption decision support, risk acceptance structure, residual risk visibility, exception handling, and board-level reporting language.

Planning implications:

- define an Executive One-Pager
- define a Risk Owner Guide
- define a High-Impact Action Decision Matrix
- define an AI Agent Risk Acceptance Memo
- define a Residual Risk Register Template
- define KRI and KPI examples
- define a Board Reporting Template
- define an Exception Management Process

## Proposed v0.6.0 workstreams

v0.6.0 planning is organized into five workstreams.

### Workstream 1: Implementer Readiness

Goal: make AAEF implementable by engineering teams without requiring them to infer core request, decision, dispatch, and evidence structures from conceptual documents alone.

Initial candidate artifact:

- Implementer Quick Start

Supporting candidate artifacts:

- Canonical Action Request JSON
- Authorization Decision Artifact minimal profile
- Dispatch Attestation profile
- profile-aware evidence validation
- reference adapter or generic REST gateway example

### Workstream 2: Operational Readiness

Goal: make AAEF operable in production environments after initial implementation.

Initial candidate artifact:

- Operational Responsibility Matrix

Supporting candidate artifacts:

- Operational Readiness Checklist
- Agentic Incident Response Runbook
- Monitoring and Alert Catalog
- Evidence Retention and Cost Guidance
- Policy Change and Rollback Guidance
- Operational Metrics, SLO, and SLA examples

### Workstream 3: Legal and Compliance Applicability

Goal: make AAEF usable in legal, compliance, contractual, and governance discussions without overstating compliance claims.

Initial candidate artifact:

- Legal and Compliance Applicability Note

Supporting candidate artifacts:

- Evidence Privacy and Retention Policy
- Contractual Control Addendum
- SaaS / external agent responsibility matrix
- DPIA / AI Impact Assessment support template

### Workstream 4: Security Architecture Hardening

Goal: clarify the minimum production architecture expectations for high-impact agentic action assurance.

Initial candidate artifact:

- High-Impact Production Minimum Architecture Profile

Supporting candidate artifacts:

- TCB Hardening Profile
- Authorization Decision Artifact minimal profile
- Backend Relying Party Verification example
- MCP / tool gateway / policy engine / SIEM reference placement examples

### Workstream 5: Risk Owner and Executive Adoption

Goal: make AAEF understandable and actionable for risk owners and executive decision-makers.

Initial candidate artifact:

- Risk Owner Guide

Supporting candidate artifacts:

- Executive One-Pager
- High-Impact Action Decision Matrix
- AI Agent Risk Acceptance Memo
- Residual Risk Register Template
- KRI and KPI examples
- Board Reporting Template
- Exception Management Process

## Initial prioritization

The first v0.6.0 planning outputs should be small, decision-oriented, and adoption-facing.

Recommended initial artifact sequence:

1. Implementer Quick Start
2. Operational Responsibility Matrix
3. Legal and Compliance Applicability Note
4. High-Impact Production Minimum Architecture Profile
5. Risk Owner Guide

This sequence gives each adoption audience a concrete entry point while avoiding a premature expansion of active controls.

## Non-goals for v0.6.0 planning

v0.6.0 planning should not:

- automatically promote all v0.5.0 or v0.5.x planning material into active controls
- close the broader cross-agent and cross-domain roadmap issue by default
- create a certification scheme
- claim direct legal or regulatory compliance
- imply that external standards are replaced by AAEF
- imply that the current active baseline has changed unless active artifacts are explicitly updated
- mix implementation guidance, audit guidance, legal applicability, and executive materials into a single undifferentiated document

## Relationship to the v0.5.x follow-up cycle

The v0.5.x follow-up cycle refined planning concepts around cross-agent authority, delegation, evidence integrity, tamper-evident selected contexts, approval quality, and related assessment expectations.

v0.6.0 should use those refinements as planning input, but its focus is different.

The v0.5.x follow-up cycle asked:

> What concepts and safeguards need to exist?

v0.6.0 planning asks:

> What packages are needed for practical adoption, implementation, operation, audit, legal review, architecture review, and risk ownership?

## Expected next steps

The expected next steps are:

1. Create child track issues for the five v0.6.0 workstreams.
2. Define the first adoption-facing artifact for each workstream.
3. Keep roadmap issue #241 as the coordination point for v0.6.0 planning.
4. Record the relationship between v0.6.0 and the broader cross-agent roadmap.
5. Avoid baseline changes until candidate artifacts are reviewed and intentionally promoted.

## Acceptance criteria for this planning synthesis

This synthesis is sufficient for initial v0.6.0 planning when:

- the five workstreams are defined
- the major stakeholder perspectives are captured
- conservative positioning boundaries are recorded
- non-goals are explicit
- the first candidate adoption artifacts are identified
- roadmap issue #241 can use this document as planning input
