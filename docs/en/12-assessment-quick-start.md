# 12. Assessment Quick Start

## Status

This document is an initial assessment quick start for AAEF v0.2 public review.

It is intended to help reviewers, implementers, security teams, AI governance teams, and auditors begin using AAEF as an assessment aid.

This document is not a certification scheme, legal standard, or complete audit procedure.

Related worksheet:

- `assessment/aaef-assessment-worksheet-v0.2-draft.csv`

## Purpose

AAEF defines controls for agentic AI action assurance.

The assessment quick start helps answer:

- which AAEF controls apply,
- what evidence should be reviewed,
- where findings should be recorded,
- what residual risk remains,
- and what remediation may be needed.

The goal is to make AAEF usable as a practical review framework without implying that a simple checklist proves a system is secure.

## Recommended Assessment Scope

Before assessing controls, define the assessment scope.

At minimum, identify:

- system or agent name,
- agent owner,
- business process,
- deployment environment,
- connected tools,
- external systems,
- high-impact action categories,
- principal types,
- delegation flows,
- evidence storage location,
- approval workflows,
- revocation and isolation mechanisms,
- and assessment period.

## Suggested Assessment Roles

Typical roles include:

| Role | Responsibility |
|---|---|
| System Owner | Confirms system purpose, business process, and risk acceptance |
| Agent / Platform Engineer | Explains runtime architecture, tool dispatch, policy enforcement, and evidence generation |
| Security Reviewer | Reviews threat model, control design, authorization boundaries, and residual risk |
| AI Governance Reviewer | Reviews high-impact action definitions, human oversight, and policy alignment |
| Auditor / Assessor | Reviews evidence, control operation, and findings |
| Incident / Operations Owner | Reviews revocation, isolation, break-glass, and reconstruction readiness |

## Assessment Workflow

### 1. Define the assessment target

Document the agentic system, workflow, or integration being assessed.

Recommended fields:

- agent system name,
- owner,
- runtime or platform,
- connected tools,
- external systems,
- data classes,
- high-impact action categories,
- deployment status,
- assessment period.

### 2. Identify high-impact actions

Use the High-Impact Action Taxonomy to identify actions that require stronger authorization, approval, evidence, and review.

Relevant categories include:

- external communication,
- sensitive data access or export,
- payment, purchase, or financial commitment,
- access rights or privilege change,
- production system change,
- code commit, merge, deployment, or execution,
- legal, contractual, or regulatory commitment,
- customer-impacting decision or action,
- security response, blocking, or containment,
- persistent memory write or trust-state update,
- external agent delegation or cross-domain agent action.

### 3. Map tools and workflows to controls

For each high-impact action, map:

- tool or API,
- action type,
- target resource,
- principal,
- authority scope,
- approval requirement,
- evidence requirement,
- revocation or freeze path.

### 4. Review control applicability

Not every control applies to every system.

For each control, record:

- Applicable,
- Not Applicable,
- Partially Applicable,
- Not Assessed.

If a control is not applicable, record the reason.

### 5. Review evidence

Evidence may include:

- control configuration,
- policy definitions,
- authority grants,
- authorization decision logs,
- evidence event records,
- approval records,
- delegation records,
- revocation logs,
- override or break-glass records,
- test results,
- incident reconstruction artifacts,
- diagrams or architecture documentation.

For evidence events, prefer structured evidence that can be tied to:

- agent identity,
- principal,
- action,
- resource,
- authority scope,
- authorization decision,
- approval,
- result,
- and timestamp.

### 6. Evaluate findings

Assessment results may use the following values:

| Result | Meaning |
|---|---|
| Pass | Control is implemented and evidence supports operation |
| Partial | Control is partially implemented or evidence is incomplete |
| Fail | Control is missing or ineffective |
| Not Applicable | Control does not apply to the assessed system |
| Not Assessed | Control was not assessed in this review |

### 7. Record residual risk

For each finding, document residual risk.

Examples:

- model self-assessment is still used for some review context,
- semantic ambiguity cannot be fully eliminated,
- revocation may not reach in-flight actions immediately,
- approval fatigue remains possible,
- evidence may not be tamper-evident for all action categories,
- cross-domain agent evidence is not independently verifiable,
- delegation lineage may be incomplete across external systems.

### 8. Define remediation

For each finding, record:

- owner,
- remediation action,
- target date,
- priority,
- related issue or ticket,
- acceptance criteria.

## Evidence Quality Guidance

Assessment should distinguish evidence quality.

### Stronger evidence

Examples:

- machine-enforceable policy references,
- action-bound authorization decision artifacts,
- structured authority grants,
- signed or tamper-evident evidence records,
- runtime state snapshots,
- independent input tracking,
- approval records linked to specific action IDs,
- revocation logs linked to affected delegations,
- repeatable test results.

### Weaker evidence

Examples:

- screenshots without context,
- model-generated explanations only,
- human-readable policy summaries without enforceable references,
- logs that are not linked to action IDs,
- evidence without timestamps,
- evidence without principal binding,
- unverified assertions that untrusted content did not influence an action.

Weak evidence may still be useful, but assessors should document its limitations.

## Assessment Worksheet Columns

The worksheet includes the following columns:

| Column | Purpose |
|---|---|
| Control ID | AAEF control identifier |
| Domain | Control domain |
| Maturity | Required, Recommended, or Optional |
| Requirement Summary | Short control requirement summary |
| Applicability | Applicability decision |
| Assessment Result | Pass, Partial, Fail, Not Applicable, or Not Assessed |
| Evidence Reviewed | Evidence reviewed by assessor |
| Finding Summary | Short description of finding |
| Residual Risk | Remaining risk after review |
| Remediation Notes | Required remediation or improvement |
| Owner | Responsible owner |
| Target Date | Remediation target date |
| Priority | Remediation priority |
| Related Threats | Related AAEF threat areas |
| Assurance Type | Preventive, Detective, Evidentiary, Responsive, or Governance |
| Implementation Assumptions | Assumptions required for the control to be effective |
| Notes | Additional assessment notes |

## Suggested Review Cadence

Recommended review triggers include:

- before production deployment,
- before enabling high-impact actions,
- after adding new tools,
- after adding cross-agent delegation,
- after significant policy changes,
- after security incidents,
- after major model or runtime changes,
- periodically for production systems.

## Limitations

This quick start does not prove compliance or system safety.

It should be used with:

- system architecture review,
- threat modeling,
- evidence validation,
- control testing,
- incident response planning,
- and organization-specific legal, regulatory, and compliance requirements.

## Next Steps

1. Copy the worksheet.
2. Define the assessment scope.
3. Identify high-impact actions.
4. Mark control applicability.
5. Review evidence.
6. Record findings and residual risk.
7. Track remediation.
8. Reassess after material changes.
