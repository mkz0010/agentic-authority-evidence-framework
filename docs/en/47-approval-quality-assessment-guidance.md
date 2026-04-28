# Approval Quality Assessment Guidance

**Status:** v0.5.0 planning guidance
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative assessment guidance for meaningful approval, blind approval, approval fatigue, approval laundering, retry pressure, and task-splitting review

## Purpose

This document provides non-normative assessment guidance for reviewing approval quality in AAEF v0.5.0 planning.

It helps assessors reason about whether a human approval was meaningful, informed, action-bound, and resistant to approval fatigue or approval laundering.

This document does not change the Evidence Event Schema, control catalog, testing procedures, or assessment worksheet.

## Core Principle

Human approval is not automatically authority.

An approval should only strengthen assurance when the approver was shown sufficient, accurate, action-bound context and had a reasonable opportunity to understand what would be executed.

Approval evidence is weak when it shows only that a user clicked "approve" without showing what was presented, what was approved, what changed afterward, and what finally executed.

## Related Controls

This guidance supports review of:

- `AAEF-AUZ-03`: human approval for high-impact actions;
- `AAEF-HUM-01`: meaningful human approval context;
- `AAEF-HUM-02`: approval fatigue controls;
- `AAEF-HUM-03`: human override evidence;
- `AAEF-EVD-03`: approval evidence linked to action evidence;
- `AAEF-EVD-05`: non-execution evidence;
- `AAEF-EVD-06`: reauthorization evidence;
- `AAEF-PRN-02`: principal context validity.

For the related planning concept, see `docs/en/39-approval-quality-approval-fatigue.md`.

For approval evidence examples, see `docs/en/40-approval-evidence-examples.md`.

## Approval Quality Dimensions

Assessors should consider approval quality across the following dimensions.

| Dimension | Review Question |
| --- | --- |
| Action binding | Was the approval linked to the specific action that executed? |
| Context sufficiency | Did the approver see enough information to make a meaningful decision? |
| Material accuracy | Did the displayed approval context match the final dispatched action? |
| Scope clarity | Was the action scope, resource, tenant, principal, and impact clear? |
| Risk visibility | Was the risk, criticality, reversibility, or policy reason visible? |
| Timing | Was approval obtained before execution and still fresh at dispatch time? |
| Change handling | Were material changes after approval reapproved or denied? |
| Fatigue resistance | Was the approval flow resistant to repeated prompts or habituation? |
| Laundering resistance | Could an approval of one action be reused to justify a different action? |
| Evidence linkage | Can reviewers correlate approval, authorization, dispatch, execution, and final outcome? |

## Meaningful Approval

### Assessment Expectation

A meaningful approval should generally show:

- what action will be executed;
- who or what will execute it;
- on whose behalf it will be executed;
- target resource or tenant;
- expected impact;
- risk level or policy reason;
- requested scope;
- relevant constraints;
- whether the action is reversible;
- whether the action is delegated, cross-domain, or reauthorization-related;
- what will happen after approval.

### Strong Evidence

Strong evidence may include:

- approval request ID;
- approver identity or role;
- approval timestamp;
- displayed approval context;
- canonical action ID or action digest;
- target resource;
- amount, scope, or change details where applicable;
- risk classification;
- authorization decision linkage;
- dispatch linkage;
- execution or non-execution outcome;
- evidence source and trust limitations.

### Weak Evidence

Weak evidence includes:

- generic "approved" record;
- approval click without displayed context;
- approval not linked to the executed action;
- approval after execution;
- approval summary that differs from the action dispatched;
- approval stored only in an agent runtime log;
- missing approver identity or role.

## Blind Approval

### Scenario

A user is shown a prompt such as "Approve this action?" without details about the action, resource, principal context, or impact.

### Assessment Interpretation

This should be treated as weak approval evidence.

The approval may show that a user interacted with the system, but it does not show that the user made an informed decision.

### Finding Patterns

Findings may arise when:

- approval prompts omit resource or scope;
- high-impact actions are approved using generic prompts;
- approvers cannot inspect the final action payload or digest;
- approval prompts hide principal or tenant context;
- approval prompts omit risk or policy reason.

## Approval Laundering

### Scenario

An agent obtains approval for a benign or vague action, then uses that approval to justify a broader, riskier, or materially different action.

### Risk Indicators

Reviewers should look for:

- approved action differs from executed action;
- approved scope differs from final scope;
- action digest mismatch;
- target resource changed after approval;
- approval reused across multiple actions;
- vague approval context;
- no material-change reapproval;
- no final execution linkage.

### Expected Safe Behavior

The system should require renewed approval or reauthorization when the final action materially differs from the approved action.

### Assessment Interpretation

Approval should not be transferable across materially different actions unless the approved scope explicitly permits it.

## Approval Fatigue

### Scenario

An approver receives repeated approval prompts from an agent.

Over time, the approver begins clicking approve without reviewing the details.

### Risk Indicators

Reviewers should look for:

- high approval frequency;
- repeated prompts for similar actions;
- repeated denial followed by reworded approval requests;
- short time between prompt and approval;
- identical or near-identical approval text;
- many approvals by the same approver in a short window;
- approval prompts after previous denial;
- task splitting across many low-risk approvals.

### Assessment Interpretation

Approval fatigue can reduce the assurance value of human approval.

Assessment should consider whether the approval workflow supports attention, reviewability, and escalation rather than habituation.

## Retry Pressure After Denial

### Scenario

An agent receives a denial, modifies the wording, and asks again.

The action is eventually approved without resolving the original reason for denial.

### Risk Indicators

Reviewers should look for:

- denial followed by similar approval requests;
- no change in underlying authority or risk;
- no linkage between denial and retry;
- no escalation or reauthorization record;
- approval prompt hides prior denial;
- retry count missing.

### Expected Safe Behavior

The system should correlate retries to the original denial and show prior denial context to the approver where appropriate.

### Assessment Interpretation

Repeated approval requests should not become a bypass path around denial.

## Task Splitting

### Scenario

An agent splits a high-impact action into several smaller actions, each of which individually appears approval-safe.

### Risk Indicators

Reviewers should look for:

- multiple related approvals;
- shared target resource;
- shared business purpose;
- same principal or agent;
- small actions executed in sequence;
- combined effect exceeds approval threshold;
- missing aggregate risk review.

### Expected Safe Behavior

The system should detect aggregation risk where multiple actions combine into a high-impact outcome.

### Assessment Interpretation

Approval quality should consider the cumulative effect of related approvals, not only each approval in isolation.

## Approval Under Degraded Principal Context

### Scenario

The approver is not shown which principal, role, tenant, workspace, delegation, or authority basis the agent will use.

### Assessment Interpretation

Approval quality is weaker when principal context is hidden or degraded.

This may affect review of both approval quality and Principal Context Degradation.

### Expected Safe Behavior

The approval prompt should expose principal context when it is material to the action.

## Reauthorization Approval

### Scenario

An action is denied because the requested scope exceeds delegated authority.

The agent requests reauthorization.

### Strong Evidence

Strong reauthorization approval evidence includes:

- original denied action ID;
- denial reason;
- requested additional scope;
- principal reconfirmation where required;
- approver or escalation target;
- reauthorization decision;
- post-reauthorization effective scope;
- retry count;
- final dispatch or non-execution record.

### Assessment Interpretation

Reauthorization approval should be linked to the original denial and should not silently broaden authority beyond the approved scope.

## Approval Evidence Checklist

Assessors may review whether approval evidence includes:

- approval request ID;
- approver identity;
- approver role or authority basis;
- approval timestamp;
- displayed approval context;
- action ID or digest;
- target resource;
- principal context;
- requested scope;
- risk classification;
- policy reason;
- approval decision;
- denial or escalation history where applicable;
- reauthorization linkage where applicable;
- final dispatch linkage;
- final execution or non-execution outcome;
- evidence trust limitation.

## Review Questions

Assessors should ask:

1. What exactly did the approver approve?
2. Was the approval linked to the final executed action?
3. Was the approval context sufficient and accurate?
4. Did the approver see principal, tenant, resource, and scope information?
5. Was the action risk or policy reason visible?
6. Did the action change after approval?
7. Was reapproval required for material changes?
8. Was approval obtained before execution?
9. Was the approval still fresh at execution time?
10. Were retries after denial correlated and visible?
11. Could repeated prompts create approval fatigue?
12. Could task splitting reduce the apparent risk of a high-impact action?
13. Was the approval generated or summarized by the same agent requesting approval?
14. Can reviewers correlate approval, authorization, dispatch, execution, and final outcome?
15. Are evidence limitations documented?

## Negative Test Candidates

Future assessments may include tests for:

- blind approval prompts;
- approval prompt missing target resource;
- approval prompt missing principal context;
- approval prompt missing risk or policy reason;
- action changed after approval;
- approval reused for a different action;
- approval obtained after execution;
- approval retry after denial without linkage;
- repeated prompts causing fatigue;
- task splitting around approval thresholds;
- approval stored only in mutable agent logs;
- approval evidence not linked to dispatch or execution.

## Finding Patterns

Reviewers may record findings for:

- approval not action-bound;
- approval not linked to dispatch or execution;
- generic approval prompts for high-impact actions;
- missing approver identity or role;
- missing displayed approval context;
- material action change after approval;
- repeated approval requests without retry correlation;
- approval fatigue indicators;
- approval laundering indicators;
- task splitting indicators;
- missing reauthorization linkage;
- missing evidence limitations.

## Non-Goals

This guidance does not require:

- human approval for every action;
- raw prompt retention by default;
- full payload retention by default;
- a specific approval UI;
- a specific ticketing or workflow system;
- a dedicated approval quality control in the current version;
- schema changes in the current Evidence Event Schema.

## Future Work

Future AAEF work may decide whether to:

- define approval quality metrics;
- define approval fatigue thresholds;
- define approval laundering negative tests;
- add approval quality fields to the Evidence Event Schema;
- add assessment profile guidance for approval quality;
- define stronger approval requirements for critical actions;
- add a dedicated approval quality control.
