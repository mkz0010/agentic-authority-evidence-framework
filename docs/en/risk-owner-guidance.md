# Risk-Owner Guidance

This document provides risk-owner-facing guidance for AAEF-style adoption, exception, residual-risk, and escalation decisions.

It is intended to help risk owners decide whether an agentic action system is acceptable for a defined use case without treating model output as authority.

## Status and claim boundary

This guidance is part of the AAEF documentation set, but it does not change the current control and assessment baseline.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

This document does not define:

- new controls,
- new evidence schema requirements,
- new assessment procedures,
- new testing procedures,
- production readiness requirements,
- audit sufficiency requirements,
- legal requirements,
- compliance requirements,
- certification criteria,
- conformity criteria, or
- equivalence claims with external frameworks.

This document is tool-neutral risk-owner guidance. Organizations should adapt it to their own governance model, risk ownership structure, approval authorities, legal obligations, compliance obligations, operational model, and business context.

## Purpose

The purpose of risk-owner guidance is to give risk owners a practical decision path for agentic action systems.

Risk owners should be able to answer:

- What action or use case is being considered?
- What business value or operational need is being supported?
- What high-impact or sensitive actions may occur?
- Who has authority to approve or restrict those actions?
- What evidence supports the adoption decision?
- What operational signals must be reviewed after adoption?
- What residual risk remains?
- What exceptions, conditions, or time limits apply?
- When should execution be restricted, paused, escalated, or rejected?
- What claim boundaries apply?

The central principle remains:

> Model output is not authority.

A model, agent, or prompt may recommend, explain, summarize, or propose. It does not by itself authorize action execution or risk acceptance.

## Scope

This guidance covers risk-owner review activities for AAEF-style systems, including:

- risk-owner role context,
- adoption decision path,
- high-impact action review,
- evidence request questions,
- residual risk review,
- exception handling questions,
- freeze, hold, and escalation decision points,
- decision memo structure,
- executive and board reporting considerations, and
- non-goals and claim boundaries.

This guidance does not prescribe a quantitative risk model, mandatory approval thresholds, organization-specific governance roles, legal conclusions, compliance conclusions, audit opinions, or production readiness criteria.

## Risk-owner role context

A risk owner is a person or group accountable for deciding whether a defined agentic action use case is acceptable within a business, operational, security, legal, or governance context.

The risk owner is not assumed to be:

- the model developer,
- the implementation engineer,
- the operator,
- the auditor,
- the legal owner,
- the compliance owner,
- the security architect, or
- the system administrator.

Depending on the organization, these roles may overlap. When they overlap, the overlap should be explicit rather than implicit.

The risk owner should focus on the decision being made, the evidence supporting that decision, the remaining risk, and the conditions under which the decision remains valid.

## Risk-owner decision path

A risk-owner decision should follow a clear path.

Recommended decision path:

1. Define the use case.
2. Identify the action types.
3. Identify high-impact or sensitive actions.
4. Identify affected systems, users, resources, and business processes.
5. Identify who or what may initiate actions.
6. Identify who has authority to approve, restrict, or reject actions.
7. Review authorization and enforcement design at a decision level.
8. Review evidence availability and reconstruction expectations.
9. Review operator monitoring and escalation expectations.
10. Identify residual risk.
11. Decide whether to approve, restrict, defer, reject, or require additional controls.
12. Record decision conditions and review triggers.

The decision path should avoid treating model confidence, model explanation, or agent narrative as sufficient authority.

## Candidate decision outcomes

Risk owners may select among outcomes such as:

- approve for limited pilot,
- approve with restrictions,
- approve for a defined action class only,
- approve for a defined user group only,
- approve with additional evidence requirements,
- approve with additional operator review requirements,
- defer pending additional evidence,
- require additional controls,
- require security, legal, compliance, or operational review,
- reject the use case,
- freeze or hold further execution, or
- accept residual risk with documented conditions.

These outcomes are illustrative. This document does not define organization-specific approval authority or override internal governance.

## Adoption decision questions

Risk owners should ask:

- What action is the agentic system expected to perform?
- What is the business purpose of the action?
- What could go wrong if the action is executed incorrectly?
- What could go wrong if the action is not executed?
- Does the action affect money, access, safety, privacy, legal obligations, customer impact, production systems, regulated data, or external commitments?
- Is the action reversible?
- Is there a human approval step?
- If there is human approval, what exactly is the human approving?
- Is the human approving a model narrative, or an action-bound request with authority context?
- Can the system refuse execution when authority is missing, expired, or invalid?
- Can the action be reconstructed after execution or non-execution?
- Who owns residual risk?

A risk owner should be especially cautious when a use case depends on model-generated text being treated as approval, policy, evidence, or authority.

## High-impact action review

Risk owners should identify whether the use case includes high-impact or sensitive actions.

Examples may include actions that affect:

- financial transfers,
- production changes,
- customer communications,
- access grants,
- identity or privilege changes,
- regulated data,
- contractual commitments,
- safety-relevant workflows,
- legal or compliance obligations,
- system availability,
- irreversible operations, or
- external third parties.

This list is illustrative. Each organization should define its own high-impact action categories.

For high-impact actions, risk owners should ask:

- Is authority separated from model output?
- Is dispatch enforcement required before execution?
- Does the backend verify authority where applicable?
- Is evidence generated independently of the model where possible?
- Can denied and non-executed actions be reviewed?
- Can the organization reconstruct what happened?
- Are escalation and freeze or hold paths defined?
- Are residual risks explicitly accepted?

## Evidence request questions

Risk owners should request evidence that supports the adoption or exception decision.

Recommended evidence request questions:

### Action scope

- What actions can the system request?
- What actions can the system execute?
- What systems, resources, accounts, or data can be affected?
- What actions are explicitly out of scope?

### Authority

- Who or what can authorize the action?
- How is authorization represented?
- Is authorization action-bound?
- Is authorization time-bound or revocable?
- Can authority be distinguished from model output?

### Enforcement

- What component enforces the decision before execution?
- Can execution bypass enforcement?
- What happens if authorization evidence is missing, expired, malformed, or invalid?
- Does the system fail closed for actions that require authority?

### Backend verification

- Does the backend verify authority, or only trust the caller?
- Are backend records correlatable with upstream action and authorization records?
- Are backend rejections visible to operators or reviewers?

### Evidence and reconstruction

- What evidence is generated for executed actions?
- What evidence is generated for denied or non-executed actions?
- Where is evidence stored?
- Can records be correlated across request, authorization, dispatch, backend, and outcome?
- Can a reviewer reconstruct what happened without relying on model narrative alone?

### Operations

- Who reviews operational signals?
- What signals are reviewed daily or periodically?
- What triggers escalation?
- What happens when evidence is unavailable?
- What happens when repeated denial or non-execution occurs?

Evidence requested for risk decisions is not automatically sufficient for audit, certification, compliance, conformity, or legal conclusions.

## Residual risk review

Risk owners should identify residual risk after considering controls, evidence, and operating assumptions.

Residual risk topics may include:

- authority bypass risk,
- over-broad action scope,
- unclear principal context,
- excessive delegation,
- backend trust without verification,
- incomplete evidence generation,
- evidence availability failure,
- reconstruction gaps,
- model narrative being mistaken for authority,
- human approval ambiguity,
- operational monitoring gaps,
- exception sprawl,
- third-party dependency risk,
- unclear risk ownership, and
- mismatch between business urgency and assurance maturity.

Residual risk should be recorded in a way that connects to the specific use case and action class.

## Exception handling questions

Exceptions should be explicit, time-bounded where appropriate, and assigned to an owner.

Risk owners should ask:

- What requirement, control expectation, evidence expectation, or operating expectation is being excepted?
- Why is the exception needed?
- What action class or system does the exception apply to?
- What risk is introduced by the exception?
- Who owns the exception?
- What compensating measures exist?
- What evidence will be retained during the exception period?
- What is the review date or expiration condition?
- What would cause the exception to be revoked?
- Is the exception being used to normalize lack of authority, enforcement, or evidence?

An exception should not silently convert model output into authority.

## Freeze, hold, and escalation decision points

This guidance does not define mandatory freeze criteria or incident response procedures.

Risk owners should consider whether freeze, hold, or escalation review is appropriate when there are signals such as:

- high-impact actions without reconstructable evidence,
- execution without valid authority linkage,
- suspected dispatch bypass,
- backend execution without expected verification,
- repeated evidence generation failures,
- inability to determine whether actions were authorized,
- repeated high-impact non-execution affecting critical workflows,
- suspected evidence tampering or loss,
- authority expiration or revocation not respected,
- monitoring outage affecting high-impact action review,
- unclear ownership of residual risk, or
- unresolved ambiguity about whether model output was treated as authority.

Freeze or hold authority should follow the organization’s governance model. This document does not create emergency authority by itself.

## Decision memo structure

A risk-owner decision memo may include:

1. Decision title.
2. Decision owner.
3. Date and review period.
4. Use case summary.
5. Action scope.
6. High-impact action classification.
7. Affected systems, users, data, or business processes.
8. Authority model summary.
9. Enforcement model summary.
10. Evidence and reconstruction summary.
11. Operational review expectations.
12. Exceptions or conditions.
13. Residual risk.
14. Required follow-up actions.
15. Decision outcome.
16. Review trigger or expiration condition.

The memo should distinguish between:

- what the model says,
- what the system is authorized to do,
- what enforcement actually allows,
- what evidence shows, and
- what residual risk the organization accepts.

## Executive and board reporting considerations

Executive or board-level reporting should focus on decision quality, exposure, and residual risk rather than implementation details alone.

Useful reporting categories may include:

- number of approved agentic action use cases,
- number of restricted or deferred use cases,
- number of high-impact action classes approved,
- number of open exceptions,
- number of expired or overdue exceptions,
- unresolved evidence or reconstruction gaps,
- material operational incidents or escalations,
- use cases requiring legal, compliance, or security review,
- residual risks accepted by risk owners,
- recurring themes requiring governance attention, and
- adoption areas blocked by insufficient authority, enforcement, evidence, or reconstruction readiness.

These categories are illustrative. They are not compliance metrics by themselves.

## Relationship to operator guidance

Operator guidance supports day-to-day review of action execution, non-execution, evidence availability, and reconstruction readiness.

Risk-owner guidance supports adoption, exception, escalation, and residual-risk decisions.

Risk owners may use operator signals as decision inputs, but should not require operator guidance to become a substitute for risk ownership.

## Relationship to legal and compliance review

Risk owners should involve legal or compliance owners when agentic actions may affect legal obligations, regulatory obligations, contractual duties, privacy obligations, data handling, retention duties, audit commitments, or external reporting.

AAEF materials may help structure questions and evidence requests. They do not provide legal advice or compliance determinations.

External framework mappings should remain informative relationship mappings, not compliance crosswalks or equivalence claims.

## Relationship to implementation review

Risk owners should request implementation evidence where needed, but this document is not an implementation guide.

Implementation-facing details should remain in implementation guidance, architecture guidance, examples, schemas, validation tools, and system-specific design documents.

Risk-owner review should focus on whether implementation evidence is sufficient to support the decision being made.

## Non-goals

This document does not provide:

- quantitative risk scoring,
- mandatory approval thresholds,
- organization-specific risk appetite,
- organization-specific approval authority,
- legal advice,
- compliance advice,
- audit opinions,
- certification criteria,
- conformity assessment criteria,
- production readiness criteria,
- implementation conformance criteria,
- SIEM queries,
- SOAR playbooks,
- staffing models,
- retention schedules,
- incident response procedures, or
- equivalence mappings to external frameworks.

## Relationship to AAEF baseline

This document is intended to help risk owners apply AAEF concepts in adoption and residual-risk review.

It does not update the control catalog, evidence schema, assessment artifacts, or testing procedures.

Where this document conflicts with a current active baseline artifact, the active baseline artifact takes precedence unless a later release explicitly changes that baseline.

## Summary

Risk owners should make agentic action decisions by focusing on authority, enforcement, evidence, reconstruction, and residual risk.

The basic review posture is:

- model output may explain or propose,
- authority must be separately established,
- execution must pass through enforceable boundaries,
- evidence must be available for review,
- actions should be reconstructable after the fact, and
- residual risk must be owned explicitly.

This is the risk-owner expression of the AAEF principle:

> Model output is not authority.
