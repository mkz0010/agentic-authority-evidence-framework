# AAEF v0.6.0 Adoption Package Index Planning

Status: Adoption package index planning  
Related roadmap: #241  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document provides a non-normative planning index for v0.6.0 adoption-oriented materials.

The purpose is to organize the growing v0.6.0 Practical Adoption Readiness planning artifacts by audience, use case, and adoption path so that implementers, auditors, operators, consultants, managers, risk owners, legal/compliance reviewers, security architects, and researchers can find the appropriate entry point.

This document is an index and planning guide. It does not change active controls, schemas, examples, mappings, testing procedures, assessment artifacts, or the current control and assessment baseline.

## Why this index is needed

v0.6.0 planning has produced multiple adoption-oriented artifacts.

Those artifacts are useful, but adoption friction increases if readers cannot tell:

- which document to read first,
- which document applies to their role,
- which documents are conceptual,
- which documents are implementation-facing,
- which documents are evidence-facing,
- which documents are advisory-facing,
- and which documents remain non-normative planning material.

This index organizes those artifacts without promoting them into active requirements.

## Non-normative status

This document does not make v0.6.0 planning artifacts active requirements.

All v0.6.0 adoption materials remain non-normative unless a later PR explicitly incorporates selected content into active controls, schemas, examples, assessment artifacts, testing procedures, mappings, or release artifacts.

## Adoption package overview

| Package | Primary audience | Purpose |
| --- | --- | --- |
| Implementer package | Field implementers, engineering teams | Understand how AAEF concepts can map to implementation components. |
| Auditor package | Auditors, assessors, GRC reviewers | Understand what evidence to request and how to review evidence packages. |
| Consultant package | Consultants, advisors, scoping teams | Scope discovery, pilot planning, and advisory engagements. |
| Operator package | Operators, administrators, incident responders | Understand operational ownership, monitoring, escalation, and evidence handling. |
| Risk-owner package | Managers, executives, risk owners | Support enablement, acceptance, exception, remediation, or deferral decisions. |
| Legal/compliance package | Legal and compliance reviewers | Understand applicability, claim boundaries, evidence retention, and third-party responsibility. |
| Security architecture package | Security architects | Understand control placement, TCB assumptions, dispatch, backend verification, and evidence placement. |
| Research package | Researchers, reviewers, presenters | Understand research contribution, research questions, evaluation paths, and paper framing. |

## Recommended entry points by role

| Role | Start here | Then read |
| --- | --- | --- |
| Field implementer | `v060-implementation-reference-pattern-planning.md` | Evidence examples, auditor checklist |
| Auditor / assessor | `v060-auditor-evidence-request-checklist-planning.md` | Evidence examples, implementation reference pattern |
| Consultant | `v060-consultant-discovery-checklist-planning.md` | Auditor checklist, implementation reference pattern |
| Operator / administrator | `v060-operational-responsibility-matrix-planning.md` | Implementation reference pattern, evidence examples |
| Risk owner / manager | `v060-risk-owner-guide-planning.md` | Consultant checklist, auditor checklist |
| Legal/compliance reviewer | `v060-legal-compliance-applicability-note-planning.md` | External review reassessment response, version reference audit |
| Security architect | `v060-high-impact-production-minimum-architecture-profile-planning.md` | Authorization artifact profile, implementation reference pattern |
| Research reviewer | `v060-research-positioning-review.md` | Version reference audit, external review reassessment response |

## Core v0.6.0 adoption artifacts

| Artifact | Package | Use |
| --- | --- | --- |
| `v060-planning-input-synthesis.md` | General | Defines the initial v0.6.0 planning input and direction. |
| `v060-planning-progress-summary.md` | General | Summarizes v0.6.0 planning progress and completed workstreams. |
| `v060-review-follow-up-summary.md` | General | Summarizes repository review follow-up and remaining candidates. |
| `v060-release-decision-record.md` | General | Records release-scope decisions and boundaries. |
| `v060-version-reference-audit.md` | General | Clarifies latest release, current baseline, and historical planning material semantics. |
| `v060-external-review-reassessment-response.md` | General | Converts reassessment feedback into adoption-oriented follow-up priorities. |

## Implementer package

Primary purpose:

Help an implementer understand how to build or pilot an AAEF-style action assurance flow.

Recommended reading order:

1. `v060-implementer-quick-start-planning.md`
2. `v060-authorization-decision-artifact-minimal-profile-planning.md`
3. `v060-implementation-reference-pattern-planning.md`
4. `v060-permitted-action-evidence-example-planning.md`
5. `v060-non-execution-evidence-example-planning.md`
6. `v060-auditor-evidence-request-checklist-planning.md`

Key questions answered:

- What components are needed?
- Where is authorization decided?
- Where is dispatch enforced?
- What does the backend verify?
- What evidence is generated?
- What happens when execution is denied?
- What evidence will reviewers ask for?

Not answered yet:

- Production-ready reference code.
- SDK-specific implementation.
- Formal conformance requirements.
- Active schema update.

## Auditor package

Primary purpose:

Help an auditor, assessor, or reviewer request evidence for sampled agentic actions.

Recommended reading order:

1. `v060-auditor-evidence-request-checklist-planning.md`
2. `v060-permitted-action-evidence-example-planning.md`
3. `v060-non-execution-evidence-example-planning.md`
4. `v060-implementation-reference-pattern-planning.md`
5. `v060-version-reference-audit.md`

Key questions answered:

- What evidence should be requested?
- What evidence packages are needed?
- How should permitted actions be reviewed?
- How should non-execution be reviewed?
- What are common red flags?
- What limitations should be documented?

Not answered yet:

- Formal audit opinion criteria.
- Certification rules.
- Required sampling methodology.
- Active assessment worksheet changes.

## Consultant package

Primary purpose:

Help a consultant scope AAEF-style discovery, advisory, pilot, or implementation planning work.

Recommended reading order:

1. `v060-consultant-discovery-checklist-planning.md`
2. `v060-auditor-evidence-request-checklist-planning.md`
3. `v060-implementation-reference-pattern-planning.md`
4. `v060-risk-owner-guide-planning.md`
5. `v060-legal-compliance-applicability-note-planning.md`

Key questions answered:

- What should be asked in discovery?
- What materials should be requested?
- What are the red flags?
- How should pilot candidates be selected?
- What deliverable structure is appropriate?
- How should claim boundaries be explained?

Not answered yet:

- Fixed consulting methodology.
- Engagement pricing.
- Certification or attestation model.
- Formal client deliverable template.

## Operator package

Primary purpose:

Help operators and administrators understand operational ownership and handoffs.

Recommended reading order:

1. `v060-operational-responsibility-matrix-planning.md`
2. `v060-implementation-reference-pattern-planning.md`
3. `v060-auditor-evidence-request-checklist-planning.md`
4. `v060-consultant-discovery-checklist-planning.md`

Key questions answered:

- Who owns runtime operations?
- Who reviews denied actions?
- Who owns evidence retention?
- Who can freeze execution?
- Who handles incidents?
- What operational handoffs are needed?

Not answered yet:

- Full operator runbook.
- Monitoring rule catalog.
- Incident response playbook.
- SIEM-specific implementation guide.

## Risk-owner package

Primary purpose:

Help managers, executives, and risk owners make enablement, remediation, exception, or acceptance decisions.

Recommended reading order:

1. `v060-risk-owner-guide-planning.md`
2. `v060-consultant-discovery-checklist-planning.md`
3. `v060-auditor-evidence-request-checklist-planning.md`
4. `v060-legal-compliance-applicability-note-planning.md`
5. `v060-external-review-reassessment-response.md`

Key questions answered:

- Which actions are high-impact?
- Which actions should be allowed, held, or disabled?
- What evidence supports risk acceptance?
- What residual risk remains?
- Who owns the decision?
- What claim boundaries must be preserved?

Not answered yet:

- Board-ready report template.
- Formal risk scoring method.
- Quantitative risk model.
- Binding governance requirement.

## Legal and compliance package

Primary purpose:

Help legal/compliance reviewers understand applicability, limitations, and claim boundaries.

Recommended reading order:

1. `v060-legal-compliance-applicability-note-planning.md`
2. `v060-version-reference-audit.md`
3. `v060-release-decision-record.md`
4. `v060-external-review-reassessment-response.md`
5. `v060-consultant-discovery-checklist-planning.md`

Key questions answered:

- What can AAEF claim?
- What should AAEF not claim?
- How should external framework relationships be described?
- How should evidence retention and privacy be considered?
- What third-party responsibility questions arise?

Not answered yet:

- Legal advice.
- Compliance certification.
- Regulatory equivalence.
- Audit opinion.

## Security architecture package

Primary purpose:

Help security architects reason about control placement and trusted boundaries.

Recommended reading order:

1. `v060-high-impact-production-minimum-architecture-profile-planning.md`
2. `v060-authorization-decision-artifact-minimal-profile-planning.md`
3. `v060-implementation-reference-pattern-planning.md`
4. `v060-permitted-action-evidence-example-planning.md`
5. `v060-non-execution-evidence-example-planning.md`
6. `v060-auditor-evidence-request-checklist-planning.md`

Key questions answered:

- Where should authorization be placed?
- Where should dispatch enforcement be placed?
- What should the backend verify?
- Where should evidence be generated?
- What trust assumptions remain?
- What anti-patterns should be avoided?

Not answered yet:

- Product-specific architecture.
- Mandatory reference deployment.
- Hardware-rooted implementation requirement.
- Formal TCB certification.

## Research package

Primary purpose:

Help researchers, reviewers, and presenters understand the research contribution and evaluation path.

Recommended reading order:

1. `v060-research-positioning-review.md`
2. `v060-version-reference-audit.md`
3. `v060-external-review-reassessment-response.md`
4. `v060-implementation-reference-pattern-planning.md`
5. `v060-auditor-evidence-request-checklist-planning.md`

Key questions answered:

- What is the research problem?
- What is the central contribution?
- What are the research questions?
- What evaluation directions are plausible?
- What limitations remain?
- How should claims be bounded?

Not answered yet:

- Peer-reviewed acceptance.
- Full related-work survey.
- Empirical evaluation results.
- Prototype benchmark results.

## Adoption path examples

### Path A: Implementation pilot

Use when a team wants to prototype AAEF concepts.

Recommended order:

1. Implementer Quick Start
2. Authorization Decision Artifact Minimal Profile
3. Implementation Reference Pattern
4. Permitted Action Evidence Example
5. Non-Execution Evidence Example
6. Auditor Evidence Request Checklist

Expected output:

- limited pilot design,
- component responsibilities,
- sample action request,
- sample decision artifact,
- evidence generation plan,
- non-execution behavior plan.

### Path B: Audit/readiness review

Use when a reviewer wants to assess an existing or proposed implementation.

Recommended order:

1. Auditor Evidence Request Checklist
2. Evidence Examples
3. Implementation Reference Pattern
4. Version Reference Audit
5. Legal/Compliance Applicability Note

Expected output:

- evidence request list,
- evidence gaps,
- reconstruction feasibility,
- evidence limitation notes,
- review findings.

### Path C: Consulting discovery

Use when a consultant is scoping a client engagement.

Recommended order:

1. Consultant Discovery Checklist
2. Risk Owner Guide
3. Operational Responsibility Matrix
4. Auditor Evidence Request Checklist
5. Implementation Reference Pattern

Expected output:

- action inventory,
- high-impact classification,
- authority map,
- evidence availability map,
- pilot recommendation,
- claim-boundary statement.

### Path D: Executive/risk decision

Use when a risk owner needs to decide whether to allow, hold, remediate, or disable agentic actions.

Recommended order:

1. Risk Owner Guide
2. Consultant Discovery Checklist
3. Auditor Evidence Request Checklist
4. Legal/Compliance Applicability Note

Expected output:

- risk decision memo,
- residual risk register input,
- exception decision,
- remediation priority,
- executive summary.

## Current adoption coverage

| Adoption need | Current support |
| --- | --- |
| Implementation concept | Strong planning support |
| Minimal implementation flow | Strong planning support |
| Evidence examples | Strong planning support |
| Non-execution examples | Strong planning support |
| Auditor evidence request | Strong planning support |
| Consultant discovery | Strong planning support |
| Risk-owner framing | Strong planning support |
| Legal/compliance claim boundary | Strong planning support |
| Operational responsibility | Moderate to strong planning support |
| Operator runbook | Follow-up needed |
| External framework mapping enrichment | Follow-up needed |
| Active examples or fixtures | Follow-up needed |
| Production prototype | Follow-up needed |

## Recommended next follow-up

The next follow-up should be one of:

1. Operator Runbook Planning
2. Active Example Candidate Review
3. External Framework Mapping Enrichment Plan
4. Adoption Package README / short index
5. v0.6.x follow-up issue split

Recommended first choice:

> Operator Runbook Planning

Rationale:

The implementation, evidence, auditor, and consultant paths are now represented. Operational runbooks would help translate those materials into day-to-day ownership, monitoring, escalation, freeze/hold, denied-action review, and evidence-retention behavior.

## Claim boundaries

This index does not claim:

- certification,
- compliance,
- audit sufficiency,
- conformity,
- equivalence with external frameworks,
- production readiness,
- implementation conformance,
- consulting methodology conformance,
- or complete mitigation.

It may support:

- navigation,
- adoption planning,
- implementation planning,
- assessment preparation,
- consultant discovery,
- risk-owner decision support,
- research review,
- and public review.

## Relationship to active artifacts

This document does not update active AAEF artifacts.

It is a navigation and planning aid for v0.6.0 adoption-oriented materials.

A future PR may choose to promote selected materials into active guidance, examples, assessment artifacts, or implementation aids. That would require explicit review.

## Non-goals

This document does not:

- change active controls,
- change the current control and assessment baseline,
- update schemas, examples, mappings, CSVs, or testing procedures,
- promote v0.5.0 or v0.6.0 planning material into active requirements,
- assert audit sufficiency,
- claim compliance,
- claim certification,
- claim conformity,
- claim equivalence with external frameworks,
- assert production readiness,
- or replace role-specific documents.

## Acceptance criteria

This index is sufficient when:

- v0.6.0 adoption artifacts are organized by role,
- recommended reading paths are documented,
- adoption path examples are provided,
- current adoption coverage is summarized,
- follow-up needs are identified,
- claim boundaries are preserved,
- and no active baseline change is implied.
