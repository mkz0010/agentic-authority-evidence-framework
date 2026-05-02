# Operator Guidance

This document provides operator-facing guidance for day-to-day review of AAEF-style agentic action assurance records.

It is intended to help operators review action execution, non-execution, evidence availability, and reconstruction readiness without turning model output into authority.

## Status and claim boundary

This guidance is part of the AAEF documentation set, but it does not change the current control and assessment baseline.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

This document does not define:

- new controls,
- new evidence schema requirements,
- new assessment procedures,
- production readiness requirements,
- audit sufficiency requirements,
- compliance requirements,
- certification criteria,
- conformity criteria, or
- equivalence claims with external frameworks.

This document is tool-neutral operational guidance. Organizations should adapt it to their own systems, risk model, operational responsibilities, monitoring stack, and legal or compliance obligations.

## Purpose

The purpose of operator guidance is to give operators a practical review path for agentic actions.

Operators should be able to answer:

- Was the action bound to a valid authority decision?
- Was the action executed through the expected enforcement path?
- Was evidence generated and preserved for the action?
- Can the action be reconstructed from available records?
- Were denied, blocked, expired, or non-executed actions handled safely?
- Are there signals that require escalation, freeze, hold, or further review?

The central principle remains:

> Model output is not authority.

A model, agent, or prompt may propose an action. It does not by itself authorize the action.

## Scope

This guidance covers operator review activities for AAEF-style systems, including:

- daily review questions,
- recurring evidence review categories,
- denied and non-executed action review,
- evidence availability checks,
- reconstruction checks,
- high-level freeze and hold review,
- handoff points, and
- illustrative operational metrics categories.

This guidance does not prescribe product-specific monitoring rules, SIEM queries, SOAR playbooks, staffing models, retention periods, or incident response procedures.

## Operator role context

An operator is a person or team responsible for observing, reviewing, and escalating the operational behavior of an agentic action assurance environment.

The operator is not assumed to be:

- the model developer,
- the application developer,
- the backend system owner,
- the risk owner,
- the auditor,
- the legal owner, or
- the final business approver.

Depending on the organization, these roles may overlap. When they overlap, the overlap should be explicit rather than implicit.

Operators should focus on whether the system behaved according to expected authority, enforcement, evidence, and reconstruction boundaries.

## Daily review questions

A daily operator review should focus on whether recent agentic actions appear reviewable, bounded, and reconstructable.

Recommended daily questions:

1. Were high-impact or sensitive actions executed during the review period?
2. For executed actions, is there an associated authorization decision record or equivalent authority artifact?
3. Did execution occur through the expected dispatch or enforcement path?
4. Were any actions blocked, denied, expired, or not executed?
5. Do non-executed actions have evidence explaining why execution did not occur?
6. Are there missing, incomplete, malformed, or inaccessible evidence records?
7. Are there actions that cannot be reconstructed from available records?
8. Are there repeated failures involving the same action type, principal, policy, tool, backend, or enforcement point?
9. Are there actions that appear inconsistent with approved authority, policy version, or expected scope?
10. Are there review items that should be escalated to a risk owner, system owner, security owner, or business owner?

The goal is not to re-authorize every action manually. The goal is to identify whether the operational record remains bounded and reviewable.

## Recurring evidence review categories

Operators should periodically review evidence across categories rather than only reviewing individual incidents.

Recommended review categories include:

### Action request evidence

Review whether action requests are sufficiently traceable.

Questions:

- Is the action request identifiable?
- Is the requested action type clear?
- Is the requesting principal or initiating context recorded?
- Is the requested target, resource, or backend system identifiable where applicable?
- Is the request distinguishable from model-generated narrative or untrusted content?

### Authorization decision evidence

Review whether action execution can be tied to a decision or authority artifact.

Questions:

- Is there an authorization decision identifier or equivalent reference?
- Is the decision outcome clear?
- Is the decision scoped to the action that was executed or blocked?
- Is the policy, rule, approval, or authority basis identifiable?
- Is the decision expired, superseded, revoked, or otherwise invalid at execution time?

### Dispatch and enforcement evidence

Review whether the action passed through an expected enforcement boundary.

Questions:

- Is the dispatch or enforcement component identifiable?
- Did the enforcement component verify the authorization decision before execution?
- Was the action blocked if required authorization evidence was absent or invalid?
- Is there evidence that execution did not rely only on model output?
- Are bypass paths visible or reasonably excluded by the available evidence?

### Backend relying-party evidence

Review whether backend systems treated authorization as something to verify, not merely trust.

Questions:

- Did the backend receive or verify an authorization decision, token, signature, policy reference, or equivalent control artifact?
- Did the backend reject missing, expired, malformed, or unauthorized requests where expected?
- Can backend records be correlated with dispatch and evidence records?
- Are there backend actions that lack corresponding upstream authority records?

### Execution evidence

Review whether completed actions are traceable.

Questions:

- Is the execution outcome recorded?
- Is the execution timestamp or time range available?
- Is the acting component identifiable?
- Is the target system or resource identifiable where applicable?
- Can the execution be correlated to request, authorization, dispatch, and backend records?

### Non-execution evidence

Review whether blocked, denied, expired, failed, or abandoned actions are explainable.

Questions:

- Is the non-execution outcome recorded?
- Is the reason category visible?
- Is the failure mode distinguishable from normal denial, policy refusal, malformed request, expired authority, backend rejection, or system error?
- Is there evidence that fail-closed behavior occurred where expected?
- Is escalation needed if non-execution indicates a policy, enforcement, or availability issue?

## Denied and non-executed action review

Denied and non-executed actions are important because they show whether the system refuses unsafe or unauthorized execution.

Operators should not treat non-execution as noise by default.

Review denied and non-executed actions for:

- repeated attempts to execute unauthorized actions,
- repeated expired authorization decisions,
- repeated malformed action requests,
- repeated backend verification failures,
- evidence generation failures,
- unexpected user or agent retry behavior,
- attempts to bypass dispatch enforcement,
- mismatches between model intent and authorized action scope, and
- denial patterns that may indicate user harm, business disruption, or policy misconfiguration.

A non-executed action may be a healthy control outcome. It may also be the first visible signal of misuse, integration failure, or operational drift.

## Evidence availability and reconstruction checks

Operators should periodically confirm that action records are reconstructable.

A reconstructable action should allow a reviewer to connect:

1. the action request,
2. the principal or initiating context,
3. the authorization decision or authority artifact,
4. the dispatch or enforcement decision,
5. the backend verification behavior where applicable,
6. the execution or non-execution result, and
7. the evidence storage or integrity context.

Operators should look for reconstruction gaps such as:

- missing request identifiers,
- missing authorization decision references,
- missing policy versions,
- missing dispatch records,
- missing backend correlation records,
- missing execution outcome records,
- inconsistent timestamps,
- ambiguous principal context,
- inaccessible evidence storage,
- evidence generated only by the agent runtime without independent corroboration, and
- records that cannot be correlated across components.

If an action cannot be reconstructed, the operator should treat that as an evidence quality issue even if the action outcome appears successful.

## High-level freeze and hold review

A freeze or hold is an operational decision to pause, restrict, or review action execution.

This guidance does not define mandatory freeze criteria or incident response procedures. Those criteria are organization-specific.

Operators should consider whether escalation for freeze or hold review is appropriate when there are signals such as:

- repeated high-impact actions without reconstructable evidence,
- repeated execution without valid authorization linkage,
- repeated backend verification failure,
- suspected dispatch bypass,
- suspected evidence tampering or evidence loss,
- unexpected action execution after authority expiration or revocation,
- repeated non-execution that affects critical business workflows,
- inability to determine whether actions were authorized,
- monitoring or evidence pipeline outage affecting high-impact action review, or
- unresolved ambiguity about whether model output was treated as authority.

The operator should not independently invent emergency authority unless the organization has assigned that responsibility.

## Handoff points

Operator review often creates handoff needs.

Recommended handoff categories:

### To system owners

Use when the issue appears related to application behavior, integration, backend verification, dispatch enforcement, logging, or evidence generation.

### To risk owners

Use when the issue affects risk acceptance, high-impact action policy, business impact, exception handling, or residual risk decisions.

### To security owners

Use when the issue suggests misuse, bypass, tampering, abuse, privilege escalation, adversarial input, or suspicious operational behavior.

### To compliance or legal owners

Use when the issue may affect regulatory duties, contractual obligations, evidence retention, data handling, audit commitments, or external reporting duties.

### To auditors or reviewers

Use when an assessment, review, or assurance process needs evidence clarification or reconstruction support.

The handoff should include enough context to avoid relying on model narrative as the source of truth.

Recommended handoff context:

- action or event identifier,
- time range,
- action type,
- affected system or resource,
- available authority or decision reference,
- execution or non-execution outcome,
- evidence records reviewed,
- reconstruction gaps,
- suspected boundary issue, and
- requested decision or review.

## Illustrative operational metrics categories

This document does not prescribe thresholds.

Organizations may define metrics categories such as:

- number of executed actions reviewed,
- number of high-impact actions reviewed,
- number of denied or non-executed actions reviewed,
- number of actions missing authorization linkage,
- number of actions missing dispatch evidence,
- number of actions missing backend verification evidence,
- number of actions with incomplete reconstruction,
- number of evidence generation failures,
- number of evidence storage or access failures,
- number of repeated denial patterns,
- number of escalations by handoff category,
- time to identify evidence gaps,
- time to reconstruct selected actions, and
- number of unresolved review items.

Metrics should support operational visibility. They should not be presented as proof of compliance, certification, conformity, audit sufficiency, or production readiness by themselves.

## Non-goals

This document does not provide:

- SIEM queries,
- SOAR playbooks,
- alert thresholds,
- staffing models,
- on-call procedures,
- incident severity definitions,
- evidence retention schedules,
- legal advice,
- compliance advice,
- audit opinions,
- certification criteria,
- conformity assessment criteria,
- production readiness criteria,
- implementation conformance criteria, or
- equivalence mappings to external frameworks.

## Relationship to AAEF baseline

This document is intended to help operators apply AAEF concepts in operational review.

It does not update the control catalog, evidence schema, assessment artifacts, or testing procedures.

Where this document conflicts with a current active baseline artifact, the active baseline artifact takes precedence unless a later release explicitly changes that baseline.

## Summary

Operators should review agentic action systems by focusing on authority, enforcement, evidence, and reconstruction.

The basic review posture is:

- model output may explain or propose,
- authority must be separately established,
- execution must pass through enforceable boundaries,
- evidence must be available for review, and
- actions should be reconstructable after the fact.

This is the operational expression of the AAEF principle:

> Model output is not authority.
