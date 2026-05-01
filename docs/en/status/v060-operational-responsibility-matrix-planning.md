# AAEF v0.6.0 Operational Responsibility Matrix Planning Draft

Status: Planning input  
Related roadmap: #241  
Related track: #244  
Parent planning synthesis: `docs/en/status/v060-planning-input-synthesis.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document defines the initial planning draft for an AAEF Operational Responsibility Matrix.

The purpose is to clarify who owns, operates, reviews, and responds to the operational responsibilities required for high-impact agentic actions.

This document is planning material. It does not change active controls, assessment criteria, or the current control and assessment baseline.

## Why this is needed first

AAEF v0.6.0 is focused on Practical Adoption Readiness.

For practical adoption, technical implementation is not sufficient by itself. An organization also needs to know:

- who owns the policy that authorizes or blocks agentic actions
- who operates the enforcement point
- who reviews evidence
- who responds when execution does not match authorization
- who approves exceptions
- who accepts residual risk
- who explains the action record to auditors, legal reviewers, executives, or incident responders

Without this responsibility model, implementer guidance can become a technical sample rather than an adoptable operating model.

The Operational Responsibility Matrix is therefore a connecting artifact across v0.6.0 workstreams.

## Scope

This planning draft covers operational responsibility for high-impact agentic actions, including:

- onboarding an agentic system into AAEF scope
- classifying high-impact actions
- configuring authorization and policy rules
- operating tool dispatch enforcement
- verifying backend relying-party behavior
- generating and retaining evidence
- monitoring operational signals
- handling incidents and suspected policy bypass
- managing exceptions and risk acceptances
- supporting audit, legal, compliance, and executive review

## Non-goals

This planning draft does not:

- mandate a specific operations platform
- mandate a specific SIEM, SOAR, ITSM, or ticketing system
- define a full incident response program
- define a complete RACI for every organization
- create a certification scheme
- claim legal or regulatory compliance
- change the current active AAEF baseline

## Responsibility model

The matrix should distinguish between at least four responsibility types:

| Responsibility type | Meaning |
| --- | --- |
| Accountable | Owns the decision, risk, or outcome. |
| Responsible | Performs or operates the activity. |
| Consulted | Provides required input before or during the activity. |
| Informed | Must be notified or able to review the activity. |

AAEF should not assume that the same team performs all four roles.

For example, the team that operates the tool gateway may not be the same team that accepts residual business risk. Similarly, the team that stores evidence may not be the same team that reviews evidence quality.

## Candidate operational roles

The following roles are candidate responsibility holders. Organizations may map them to their own teams, titles, or functions.

| Role | Candidate responsibility |
| --- | --- |
| Risk Owner | Accepts, rejects, or escalates residual risk for high-impact agentic actions. |
| Business Owner | Owns the business process affected by the agentic action. |
| System Owner | Owns the application, platform, or service in which the agent operates. |
| Agent Owner | Owns the agent configuration, intended use, and deployment lifecycle. |
| Policy Owner | Owns authorization policy, approval rules, constraints, and policy updates. |
| Security Architect | Reviews trusted control boundary design, enforcement placement, and hardening assumptions. |
| Tool Gateway Owner | Operates the tool dispatch enforcement point or equivalent mediation layer. |
| Backend Service Owner | Owns the relying-party service that ultimately executes or rejects the requested action. |
| Evidence Owner | Owns evidence event generation, storage, retention, integrity, and retrieval. |
| Operations / SRE | Operates production reliability, rollback, freeze, and escalation procedures. |
| SOC / Incident Response | Monitors alerts, investigates suspicious actions, and coordinates incident response. |
| Legal / Compliance | Reviews applicability, retention, privacy, contractual, and regulatory implications. |
| Auditor / Assessor | Reviews whether evidence supports design and operating effectiveness claims. |
| Vendor / Third-party Owner | Coordinates external agent, SaaS, tool provider, or managed service responsibilities. |

## Candidate operational responsibility matrix

The following matrix is an initial planning draft.

| Operational area | Accountable | Responsible | Consulted | Informed | Expected output |
| --- | --- | --- | --- | --- | --- |
| Agentic system scoping | System Owner | Agent Owner | Security Architect, Legal / Compliance | Risk Owner | Scoped agentic system inventory |
| High-impact action classification | Risk Owner | Business Owner | Security Architect, Legal / Compliance | Auditor / Assessor | High-impact action classification record |
| Authorization policy definition | Policy Owner | Agent Owner | Risk Owner, Security Architect | Operations / SRE | Approved authorization policy |
| Approval workflow definition | Risk Owner | Policy Owner | Business Owner, Legal / Compliance | Auditor / Assessor | Approval workflow and approver criteria |
| Tool dispatch enforcement operation | System Owner | Tool Gateway Owner | Security Architect | Operations / SRE | Enforced tool dispatch boundary |
| Backend relying-party verification | Backend Service Owner | Backend Service Owner | Security Architect, Tool Gateway Owner | Evidence Owner | Backend verification behavior |
| Evidence event generation | Evidence Owner | Tool Gateway Owner, Backend Service Owner | Security Architect | Auditor / Assessor | Action-bound evidence events |
| Evidence retention and retrieval | Evidence Owner | Operations / SRE | Legal / Compliance, Auditor / Assessor | Risk Owner | Retention and retrieval procedure |
| Monitoring and alerting | Operations / SRE | SOC / Incident Response | Security Architect, Evidence Owner | Risk Owner | Monitoring rules and alert handling |
| Policy change management | Policy Owner | Agent Owner | Security Architect, Operations / SRE | Risk Owner | Policy change record |
| Emergency freeze or disablement | System Owner | Operations / SRE | SOC / Incident Response, Security Architect | Risk Owner, Business Owner | Freeze or disablement record |
| Exception approval | Risk Owner | Policy Owner | Legal / Compliance, Security Architect | Auditor / Assessor | Exception record and expiration |
| Incident response | System Owner | SOC / Incident Response | Evidence Owner, Legal / Compliance, Operations / SRE | Risk Owner | Incident record and action reconstruction |
| Audit support | System Owner | Evidence Owner | Policy Owner, Operations / SRE | Risk Owner | Evidence package and assessment support |
| Third-party responsibility review | Vendor / Third-party Owner | Legal / Compliance | Security Architect, System Owner | Risk Owner | Third-party responsibility mapping |

## Minimum operational readiness questions

Before enabling high-impact agentic actions, an organization should be able to answer:

1. Who decides whether an action is high-impact?
2. Who owns the policy that permits or denies the action?
3. Who can approve exceptional execution?
4. Who operates the tool dispatch enforcement point?
5. Who owns the backend service that performs the action?
6. Who verifies that backend execution is bound to authorization?
7. Who owns the evidence store?
8. Who reviews evidence quality?
9. Who is alerted when evidence is missing, inconsistent, or delayed?
10. Who can freeze, disable, or roll back agentic execution?
11. Who investigates suspected unauthorized or mismatched execution?
12. Who accepts residual risk?
13. Who explains the action record to auditors, legal reviewers, or executives?
14. Who owns third-party or SaaS responsibility gaps?
15. Who reviews whether exceptions have expired or become permanent bypasses?

## Operational handoff points

The matrix should support explicit handoff points between workstreams.

### From implementer readiness to operational readiness

Implementation guidance should hand off:

- action request format
- authorization decision format
- dispatch attestation expectations
- evidence event generation points
- backend verification requirements
- failure and non-execution behavior

Operational readiness should define who runs, reviews, and responds to those mechanisms.

### From operational readiness to legal and compliance applicability

Operational readiness should provide:

- responsibility boundaries
- evidence retention expectations
- exception records
- approval records
- incident records
- third-party responsibility mappings

Legal and compliance guidance should use these records to support conservative applicability discussions.

### From operational readiness to security architecture hardening

Operational readiness should identify:

- operational owners for Trusted Control Boundary components
- freeze and rollback owners
- policy change owners
- evidence integrity owners
- monitoring and alert owners

Security architecture guidance should use these ownership mappings to define hardening expectations.

### From operational readiness to risk owner and executive adoption

Operational readiness should provide:

- residual risk visibility
- exception status
- operational metrics
- incident trends
- unresolved responsibility gaps

Risk owner guidance should use these inputs for acceptance, escalation, or refusal decisions.

## Candidate evidence of operational readiness

The following evidence may support future assessment of operational readiness:

| Evidence type | Example |
| --- | --- |
| Ownership record | Named owners for agent, system, policy, evidence, and risk decisions |
| High-impact action register | List of high-impact actions and classification rationale |
| Policy change record | Record of policy version, approver, effective time, and rollback plan |
| Approval workflow record | Approver criteria and approval-to-execution binding expectations |
| Monitoring rule record | Alert definitions for missing evidence, mismatched execution, or policy bypass |
| Exception record | Scope, approver, rationale, expiration, and compensating controls |
| Incident reconstruction record | Evidence chain used to reconstruct a disputed or suspicious action |
| Third-party responsibility map | Responsibility split for SaaS, external agent, tool provider, or managed service components |

## Candidate operating metrics

The following metrics may be useful for future operational guidance:

| Metric | Purpose |
| --- | --- |
| High-impact actions executed | Measures operating volume under AAEF scope |
| High-impact actions blocked | Shows policy enforcement behavior |
| Missing evidence events | Detects evidence pipeline failure |
| Authorization-to-dispatch mismatch rate | Detects execution boundary failures |
| Exception count and age | Detects accumulation of unmanaged bypasses |
| Policy rollback count | Tracks operational instability or policy quality issues |
| Incident reconstruction time | Measures ability to explain what happened |
| Evidence retrieval time | Measures audit and response readiness |
| Stale owner count | Detects responsibility drift |
| Third-party responsibility gaps | Tracks unresolved external dependency risks |

## Initial adoption package shape

The eventual Operational Responsibility Matrix should likely include:

1. a role glossary
2. a responsibility matrix
3. minimum readiness questions
4. handoff points to other v0.6.0 workstreams
5. operational evidence examples
6. candidate metrics
7. exception and incident escalation guidance
8. guidance for adapting the matrix to different organizational sizes

## Open questions

The following questions should be resolved before promoting this planning draft into an adoption-facing artifact:

- Should the matrix use strict RACI terminology, or a simpler accountable/responsible/supporting model?
- Should small organizations be given a simplified role mapping?
- Which responsibilities are minimum expectations for high-impact production use?
- Which responsibilities are recommended rather than required?
- How should outsourced SaaS or external agent providers be represented?
- Should evidence ownership and evidence review be separated?
- Should risk owner acceptance be required before high-impact agentic actions are enabled?
- What operational failures should require emergency freeze or disablement?
- Which metrics should be included in a minimum operational dashboard?

## Acceptance criteria for this planning draft

This planning draft is sufficient when:

- operational responsibility roles are identified
- candidate accountable and responsible owners are mapped
- the matrix supports the five v0.6.0 workstreams
- readiness questions are defined
- candidate evidence and metrics are identified
- no active baseline change is implied
- #244 can use this document as the basis for follow-up PRs

## Expected next steps

Recommended next steps:

1. Review the candidate operational roles and responsibility types.
2. Decide whether the eventual artifact should use RACI or a simpler ownership model.
3. Identify a minimum version of the matrix for high-impact production use.
4. Decide whether the Operational Responsibility Matrix should later move from `docs/en/status/` into an adoption or operations-oriented document path.
5. Use this draft to guide follow-up work on operational readiness checklist, monitoring catalog, and incident response runbook.
