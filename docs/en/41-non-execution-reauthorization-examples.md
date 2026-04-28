# Non-Execution and Reauthorization Examples

**Status:** v0.5.0 planning examples
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative examples for denial, deferral, safe termination, escalation, freeze, and reauthorization review

## Purpose

This document provides non-normative examples for reviewing non-executed high-impact actions and reauthorization flows in AAEF v0.5.0 planning.

It illustrates how reviewers can distinguish:

- safe denial;
- deferral;
- escalation;
- freeze;
- safe termination;
- reauthorization after denial;
- additional scope requests;
- retry behavior;
- reauthorization bypass patterns;
- non-execution evidence limitations.

This document does not change the Evidence Event Schema, control catalog, testing procedures, or assessment worksheet.

## Core Principle

A denied, deferred, escalated, frozen, or safely terminated action is still security-relevant.

Non-execution evidence helps prove that the system failed closed, preserved accountability, and did not silently convert denial into execution through retry, rephrasing, task splitting, or unreviewed reauthorization.

## Related Controls

These examples support review of:

- `AAEF-AUZ-04`: denial or escalation when authority, principal, or purpose cannot be determined;
- `AAEF-AUZ-09`: authority denial and reauthorization flow;
- `AAEF-EVD-05`: evidence for non-executed high-impact actions;
- `AAEF-EVD-06`: reauthorization evidence;
- `AAEF-RES-04`: evidence preservation during incident response;
- `AAEF-HUM-01`: meaningful human approval context;
- `AAEF-HUM-02`: approval fatigue and repeated prompt controls.

For the related planning concept, see `docs/en/32-authority-denial-reauthorization-flow.md`.

## Example 1: Safe Denial Due to Missing Authority

### Scenario

An agent attempts to modify a production firewall rule.

The requested action is high-impact, but the agent does not have delegated authority for production network changes.

### Strong Evidence

Strong non-execution evidence includes:

- attempted action ID;
- principal context;
- agent and agent instance;
- requested action;
- target resource;
- authority evaluation result;
- missing authority reason;
- denial decision;
- timestamp;
- policy reference;
- non-execution outcome;
- confirmation that dispatch and backend execution did not occur;
- correlation ID or trace ID.

### Assessment Interpretation

This is strong non-execution evidence if it shows that the action was denied before dispatch or backend execution and that the denial can be correlated to the attempted action.

## Example 2: Deferral Due to Ambiguous Principal Context

### Scenario

An agent attempts to approve a vendor payment using stale session context.

The system cannot determine whether the current principal still has authority.

### Expected Safe Behavior

The system should:

- defer execution;
- record the principal context issue;
- request principal reconfirmation or reauthentication;
- prevent dispatch until context is refreshed;
- record the final outcome.

### Assessment Interpretation

Deferral is acceptable if the system records why execution did not proceed and does not allow the action to execute while principal context remains degraded or ambiguous.

## Example 3: Escalation Due to Material Ambiguity

### Scenario

An agent receives a request to delete "old customer records."

The request lacks retention scope, jurisdiction, and affected dataset boundaries.

### Expected Safe Behavior

The system should:

- detect material ambiguity;
- escalate to an authorized reviewer or workflow;
- record ambiguity type;
- prevent execution until scope is clarified;
- preserve the original request context;
- record reviewer decision and final outcome.

### Assessment Interpretation

Escalation evidence should show that the system did not allow the model to resolve material ambiguity by itself.

## Example 4: Safe Termination After Tool Dispatch Mismatch

### Scenario

Authorization approves a read-only customer account review.

Before dispatch, the tool invocation attempts to update customer account status.

### Expected Safe Behavior

The system should:

- detect mismatch between approved action and dispatch request;
- safely terminate or deny the dispatch;
- record the mismatch;
- link the denial to the original authorization decision;
- preserve evidence for investigation.

### Assessment Interpretation

This is a strong example of model output not being authority. The dispatch layer should not execute a materially different action merely because a prior approval or authorization exists.

## Example 5: Freeze During Suspected Compromise

### Scenario

A workflow suddenly attempts multiple high-impact actions after ingesting external content.

The system suspects prompt injection or compromised workflow state.

### Expected Safe Behavior

The system may:

- freeze the workflow;
- block further tool dispatch;
- preserve current state;
- record freeze reason;
- notify an operator or incident workflow;
- require review before resumption.

### Assessment Interpretation

A freeze is stronger when it prevents further execution and preserves evidence rather than merely logging a warning.

## Example 6: Reauthorization After Denial

### Scenario

A high-impact action is denied because the requested scope exceeds the agent's delegated authority.

The agent requests additional scope.

### Strong Reauthorization Evidence

Strong evidence includes:

- original denied action ID;
- denial reason;
- requested additional scope;
- principal reconfirmation where required;
- approver or escalation target;
- reauthorization request ID;
- final decision;
- post-reauthorization effective scope;
- retry count;
- final dispatch or non-execution record.

### Weak Reauthorization Evidence

Weak evidence includes:

- informal approval without linkage;
- no original denial reference;
- no requested scope;
- no effective scope after approval;
- no retry count;
- no final outcome.

### Assessment Interpretation

Reauthorization should remain scoped, attributable, and linked to the prior denial. It should not become a bypass path.

## Example 7: Retry Loop After Denial

### Scenario

An agent repeatedly retries a denied action with slightly different wording.

### Risk Indicators

Reviewers should look for:

- repeated action attempts;
- same target resource;
- same principal or agent;
- similar purpose;
- different natural-language phrasing;
- same underlying tool action;
- missing retry correlation;
- eventual execution without new authority.

### Expected Safe Behavior

The system should:

- correlate retries;
- preserve original denial;
- enforce denial unless new authority is granted;
- escalate if repeated retries appear to bypass policy.

### Assessment Interpretation

A retry loop is risky if the system treats each attempt as unrelated and eventually executes the action without resolving the original authority gap.

## Example 8: Task Splitting to Avoid Approval

### Scenario

A high-impact action requires approval if the amount exceeds a threshold.

The agent splits one large transaction into smaller transactions that individually fall below the approval threshold.

### Expected Safe Behavior

The system should detect or flag:

- related actions;
- repeated target;
- cumulative impact;
- shared purpose;
- same principal;
- same agent or workflow;
- threshold avoidance pattern.

### Assessment Interpretation

Task splitting may indicate approval or authorization bypass. Reviewers should assess whether the evidence preserves enough correlation to reconstruct cumulative impact.

## Example 9: Non-Execution With Insufficient Evidence

### Scenario

The system says an action was blocked, but evidence only contains:

- "blocked";
- timestamp;
- agent ID.

### Evidence Limitation

This is insufficient for high-impact review if it omits:

- attempted action;
- target resource;
- principal context;
- denial reason;
- authority gap;
- policy reference;
- dispatch prevention evidence;
- final non-execution outcome.

### Assessment Interpretation

A reviewer may record partial implementation or evidence limitation. A block message alone is not enough to prove safe non-execution.

## Example 10: Reauthorization Approval Fatigue

### Scenario

A reviewer receives repeated reauthorization requests from the same agent in a short period.

The requests are similar and do not clearly show what changed since the prior denial.

### Expected Safe Behavior

The workflow should:

- show prior denial context;
- show requested additional scope;
- show reason for renewed request;
- show retry count;
- highlight repeated or task-split behavior;
- allow deny, defer, escalate, or freeze;
- avoid training reviewers to approve repetitive prompts blindly.

### Assessment Interpretation

Reauthorization workflows should be reviewed for approval fatigue, not only for the presence of approval records.

## Review Questions

Assessors should ask:

1. Why did execution not proceed?
2. Was non-execution recorded before dispatch or backend execution?
3. What authority, principal, purpose, state, input trust, policy, or evidence gap caused non-execution?
4. Was the attempted action linked to denial, deferral, escalation, freeze, or safe termination evidence?
5. Was the final non-execution outcome recorded?
6. Did the system preserve evidence for later review?
7. Did the agent retry the denied action?
8. Were retries correlated?
9. Did reauthorization request additional scope?
10. Was the additional scope approved explicitly and narrowly?
11. Did post-reauthorization execution stay within the approved scope?
12. Could task splitting or rephrasing bypass the original denial?

## Finding Patterns

Reviewers may record findings for:

- missing non-execution reason;
- denial not linked to attempted action;
- non-execution evidence generated only by the agent runtime;
- dispatch or execution occurring after denial;
- unclear authority gap;
- missing principal context issue;
- missing policy reference;
- retry attempts not correlated;
- reauthorization request not linked to original denial;
- reauthorization silently broadening authority;
- repeated prompts creating approval fatigue;
- task splitting to avoid approval or authorization thresholds;
- freeze without evidence preservation;
- safe termination that cannot be reconstructed.

## Non-Goals

These examples do not require:

- a specific workflow engine;
- a specific ticketing system;
- a specific incident response platform;
- a specific schema change;
- reauthorization for every denied action;
- human approval for every retry;
- raw prompt retention by default.

## Future Work

Future AAEF work may decide whether to:

- add non-execution JSON examples;
- add reauthorization JSON examples;
- add retry and task-splitting negative tests;
- strengthen `AAEF-EVD-05`;
- strengthen `AAEF-EVD-06`;
- define schema fields for non-execution and reauthorization;
- define assessment guidance for repeated denial and reauthorization fatigue.
