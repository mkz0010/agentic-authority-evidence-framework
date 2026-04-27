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

### Evidence Quality Gate for High-Impact Actions

For high-impact actions, assessment should consider not only whether evidence exists, but whether the evidence is strong enough to support the assessment result.

A high-impact action should not receive a strong Pass result when the available evidence consists only of weak or self-reported artifacts.

Weak evidence may include:

- model-generated explanations without independent enforcement evidence,
- screenshots without action IDs or traceable evidence references,
- human-readable policy summaries without enforceable policy references,
- unverified assertions about untrusted input influence,
- mutable logs without integrity protection for critical actions,
- Agent Runtime self-reporting without corroborating ADP, TDE, backend, or evidence pipeline records.

Stronger evidence may include:

- action IDs linked to authorization decisions and execution results,
- action-bound authorization decision artifacts,
- policy IDs and policy versions,
- evidence generated by ADP, TDE, backend API, or independent evidence pipeline components,
- correlation IDs or trace IDs,
- non-execution evidence for denied, deferred, escalated, frozen, or safely terminated actions,
- tamper-evident or integrity-protected evidence for critical actions.

Assessors should record evidence limitations when evidence is incomplete, self-reported, mutable, or not independently generated.

For high-impact actions, model-only evidence should be treated as advisory, not sufficient evidence of authorization, enforcement, or safe execution.

### Evidence Quality Gate Assessment Outcomes

For high-impact actions, assessors should evaluate not only whether evidence exists, but whether the evidence is strong enough to support the assessment result.

Evidence Quality Gate outcomes should consider:

- whether the evidence is structurally valid,
- whether the evidence was independently generated,
- whether the evidence is protected against tampering or later modification,
- whether the evidence can be correlated to the specific action,
- whether the evidence was generated by a trusted enforcement, policy, backend, or evidence component,
- whether the evidence is only a model, agent runtime, or implementation self-report,
- and whether the evidence supports reconstruction of the proposed action, authorization decision, dispatch, execution, and result.

The following outcomes may be used when evaluating Evidence Quality Gate results.

| Outcome | Description | Typical conditions |
|---|---|---|
| Pass | Evidence is sufficient to support the assessment result for the assessed action and risk level. | Evidence is action-bound, independently generated or corroborated, traceable to authorization and execution, and appropriate for the action impact. |
| Partial | Evidence supports part of the assessment result, but important limitations remain. | Evidence exists and can be reviewed, but may lack independent generation, tamper evidence, complete correlation, or sufficient assertion source clarity. |
| Fail | Evidence is not sufficient to support the assessment result. | Evidence is missing, self-reported only, not action-bound, not traceable to authorization or execution, inconsistent, mutable without protection, or contradicted by other records. |
| Not Assessed | Evidence quality was not assessed for the item. | The item was out of scope, not applicable, unavailable for review, or deferred to a later assessment. |

A strong Pass for a high-impact action should not rely solely on:

- model-generated explanations,
- agent runtime self-reporting,
- screenshots without traceable identifiers,
- mutable logs without integrity protection,
- human-readable summaries not bound to the canonical action,
- or assertions that do not identify who or what made the assertion and how it was determined.

A Partial result should explicitly record the evidence limitation.

Examples include:

- evidence exists but was generated by the same runtime being assessed,
- evidence links to the action but not to the authorization decision,
- evidence links to the authorization decision but not to the dispatched operation,
- evidence links to dispatch but not to the backend effect,
- evidence is structurally valid but lacks independent corroboration,
- or the assertion source is unclear.

A Fail result should be recorded when the assessor cannot reasonably reconstruct whether the executed action matched the authorized action.

For high-impact actions, structurally valid evidence is not enough by itself. The assessment should consider whether the evidence is meaningful for assurance, not merely valid as data.

### Weak and Adversarial Evidence Examples

For high-impact actions, assessors should distinguish between weak evidence and adversarial evidence patterns.

Weak evidence may be incomplete, self-reported, mutable, or difficult to correlate.

Adversarial evidence patterns are more serious. They may indicate that approval, authorization, or evidence artifacts are being reused, laundered, substituted, or presented in a misleading way.

| Pattern | Why it is weak or risky | Assessment implication |
|---|---|---|
| Model-only explanation | The model describes why an action was safe, but no independent authorization, dispatch, backend, or evidence record supports the claim. | Treat as advisory only. Do not assign a strong Pass for high-impact actions. |
| Screenshot-only evidence | A screenshot shows a UI state, but does not include action ID, authorization decision ID, policy version, trace ID, or evidence reference. | Record as weak supporting evidence, not primary evidence. |
| Mutable log only | Evidence exists only in logs that can be modified without integrity protection or independent retention. | Record evidence limitation. Require stronger evidence for critical high-impact actions. |
| Missing action ID | Evidence cannot be linked to a specific action attempt or execution result. | Do not treat as sufficient for reconstructability. |
| Missing authorization artifact | The action result exists, but there is no action-bound authorization decision or equivalent enforcement reference. | Treat authorization evidence as incomplete. |
| Unverified input influence assertion | The event claims untrusted content did not influence the action, but does not identify who determined this, by what method, or with what limitations. | Treat as weak evidence. Prefer runtime, provenance, policy, or evidence pipeline support. |
| Human approval not bound to action | A human approved a summary, but the approval is not bound to the canonical action, resource, operation, scope, or argument digest. | Treat as insufficient for high-impact approval assurance. |
| Approval laundering | A human approval is used to legitimize an action that differs from what was actually reviewed or approved. | Treat as an adversarial evidence pattern and investigate action binding. |
| Replayed decision artifact | A prior authorization decision is reused for a different action, resource, scope, argument set, or time window. | Treat as an authorization integrity failure. |
| Payload mismatch after approval | The approved action summary differs from the payload dispatched to the tool or backend API. | Treat as a dispatch integrity failure. |
| Action digest mismatch | The digest bound to authorization does not match the dispatched tool invocation. | Treat as evidence of substitution, replay, or implementation failure. |

Adversarial evidence patterns should not be handled as ordinary evidence gaps.

They may indicate that the system can produce evidence that appears reviewable while failing to prove that the executed action matched the authorized action.

For high-impact actions, assessors should require action-bound evidence linking:

- the proposed action,
- the principal and authority scope,
- the authorization decision,
- any human approval,
- the dispatched tool operation,
- the executed backend effect,
- and the resulting evidence event.

If these links are missing or inconsistent, the assessment should record a finding even if the system produced structurally valid logs or schema-valid evidence events.

### Reviewing High-Impact Action Review Surfaces

For high-impact actions, assessors should review whether the approval or review surface presented enough information for meaningful review.

A review surface may be a web UI, CLI confirmation prompt, approval workflow, ticket, change request, policy review screen, or another mechanism.

Assessors should check whether the review surface showed or linked to:

- the principal,
- the agent or agent instance,
- the canonical action,
- the action type,
- the target resource,
- the tool or backend operation,
- the authority scope,
- the expected external effect,
- the risk level or high-impact category,
- the applicable policy decision,
- any required approval or override reason,
- the action or argument digest,
- the expiration or revocation state,
- and the evidence reference or correlation ID.

For high-impact actions, approval should be bound to the canonical action that is actually dispatched or executed.

A review surface that presents only a human-readable summary should be treated as weak evidence if the summary is not linked to the canonical action, tool operation, resource, authority scope, and action or argument digest.

If the approved action and executed action cannot be correlated, assessors should record a finding even if an approval record exists.

Assessment should consider whether the system can demonstrate that:

- the approver reviewed the same action that was authorized,
- the authorized action was the same action that was dispatched,
- the dispatched operation was the same operation executed by the backend,
- and the resulting evidence event links the approval, dispatch, execution, and result.

Missing or inconsistent review-surface evidence may indicate approval laundering, payload substitution, replayed authorization artifacts, or weak approval assurance.

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
