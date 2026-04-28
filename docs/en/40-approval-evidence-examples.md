# Approval Evidence Examples

**Status:** v0.5.0 planning examples
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative examples for approval quality, approval evidence, and approval laundering review

## Purpose

This document provides non-normative approval evidence examples for AAEF v0.5.0 planning.

It illustrates how reviewers can distinguish:

- meaningful approval evidence;
- weak approval evidence;
- approval laundering;
- approval fatigue indicators;
- approval-to-execution mismatch;
- approval evidence that should trigger a finding or limitation.

This document does not change the Evidence Event Schema, control catalog, testing procedures, or assessment worksheet.

## Core Principle

A human approval record is not automatically meaningful evidence.

Approval evidence is stronger when it is:

- action-bound;
- specific to the requested action;
- captured before execution;
- attributable to an approver;
- linked to principal context;
- linked to authority basis;
- linked to the canonical action request;
- linked to dispatch and execution evidence;
- scoped to the approved resource, purpose, and effect;
- clear about limitations and material changes.

Approval evidence is weak when it is only a click, generic confirmation, unlinked screenshot, broad reusable consent, post-execution acknowledgement, or model-generated summary without action binding.

## Related Controls

These examples support review of:

- `AAEF-AUZ-03`: meaningful approval or additional verification for high-risk and critical actions;
- `AAEF-HUM-01`: action-bound context for meaningful human approval;
- `AAEF-HUM-02`: blind approval and approval fatigue reduction;
- `AAEF-EVD-03`: approval evidence linked to action evidence;
- `AAEF-EVD-06`: reauthorization evidence;
- `AAEF-TOOL-04`: tool invocation requests derived from untrusted or external content.

For the related planning concept, see `docs/en/39-approval-quality-approval-fatigue.md`.

## Example 1: Strong Approval Evidence

### Scenario

An agent proposes a high-impact vendor payment.

The payment requires approval because it exceeds a defined financial threshold.

### Evidence Characteristics

Strong evidence includes:

- approval request ID;
- approver identity or role;
- approval timestamp;
- principal on whose behalf the action occurs;
- agent and agent instance;
- canonical action ID or action digest;
- target vendor;
- payment amount;
- destination account or verified payment route reference;
- business purpose;
- risk classification;
- policy or threshold that required approval;
- context shown to the approver;
- approval decision;
- final dispatch record;
- backend execution result;
- correlation ID or trace ID.

### Example Evidence Summary

~~~json
{
  "approval_required": true,
  "approval_id": "approval_2026_000123",
  "approver_id": "finance_manager_456",
  "approval_decision": "approved",
  "approval_timestamp": "2026-04-28T10:15:00Z",
  "canonical_action_id": "action_payment_000789",
  "approved_scope": {
    "action": "submit_vendor_payment",
    "vendor_id": "vendor_123",
    "amount": "25000",
    "currency": "USD",
    "purpose": "approved_invoice_payment"
  },
  "approval_context_presented": [
    "principal",
    "agent_id",
    "vendor_id",
    "amount",
    "currency",
    "purpose",
    "risk_level",
    "policy_threshold",
    "expected_effect"
  ],
  "linked_dispatch_id": "dispatch_000789",
  "linked_execution_id": "backend_payment_000789"
}
~~~

### Assessment Interpretation

This is strong approval evidence because the approval is specific, contextual, pre-execution, attributable, and linked to final dispatch and execution.

## Example 2: Weak Generic Approval

### Scenario

An agent asks a user:

> Do you approve this action?

The user clicks "Approve."

The record contains no canonical action ID, resource, scope, risk, or final execution linkage.

### Evidence Characteristics

Weak evidence includes:

- generic approval text;
- no clear target resource;
- no action digest;
- no link to final dispatch;
- no policy threshold;
- no proof of what the approver saw;
- no material risk or effect summary.

### Example Evidence Summary

~~~json
{
  "approval_required": true,
  "approval_id": "approval_001",
  "approver_id": "user_123",
  "approval_decision": "approved",
  "approval_context_presented": [
    "Do you approve this action?"
  ]
}
~~~

### Assessment Interpretation

This should not be treated as strong approval evidence for a high-impact action.

A reviewer should record a finding or limitation if the approval cannot be tied to the actual action, resource, authority scope, and execution result.

## Example 3: Approval Laundering

### Scenario

An approver reviews and approves:

> Send a notification to the customer.

The executed action is:

> Send a legally binding cancellation notice to the customer and update account status.

### Evidence Issue

The approval was used to legitimize a materially different action.

### Indicators

- approved summary differs from dispatched operation;
- final payload includes material effects not shown to approver;
- resource or recipient changed after approval;
- action digest changed after approval;
- dispatch layer did not require reapproval;
- evidence links approval to execution but not to the same canonical action.

### Assessment Interpretation

This is approval laundering.

The approval should be treated as insufficient because the approver did not approve the canonical action that was actually dispatched or executed.

## Example 4: Payload Substitution After Approval

### Scenario

A human approves a database maintenance action against a staging environment.

After approval, the agent or workflow changes the target environment to production.

### Expected Safe Behavior

The system should:

- detect material change;
- invalidate prior approval;
- deny, defer, escalate, or require reapproval;
- record the non-execution or reauthorization path.

### Finding Condition

A finding should be recorded if the system allows execution using the old approval after material action, resource, environment, scope, or payload changes.

## Example 5: Approval Fatigue Indicator

### Scenario

An approver receives 200 approval prompts in one hour.

Most prompts use similar wording and do not distinguish routine actions from critical actions.

### Evidence Indicators

Reviewers should examine:

- approval volume per approver;
- approval frequency over time;
- repeated prompts for similar actions;
- approval latency;
- denial rate;
- escalation rate;
- batching behavior;
- role suitability;
- critical-action separation;
- whether prompts include risk and consequence.

### Assessment Interpretation

High approval volume does not automatically prove approval fatigue, but it is a risk indicator.

If approval volume, prompt design, and lack of context make meaningful review unlikely, reviewers should treat approval quality as limited even if every action has an approval record.

## Example 6: Reauthorization After Denial

### Scenario

A high-impact action is denied because the requested scope exceeds delegated authority.

The agent requests additional approval.

### Strong Evidence

Strong reauthorization evidence includes:

- original denied action ID;
- denial reason;
- requested additional scope;
- approver or escalation target;
- principal reconfirmation where required;
- reauthorization request ID;
- final reauthorization decision;
- post-reauthorization effective scope;
- retry count;
- link to final dispatch or non-execution.

### Weak Evidence

Weak evidence includes:

- informal chat approval;
- no link to original denial;
- no requested scope;
- no post-reauthorization scope;
- no retry tracking;
- no final outcome.

### Assessment Interpretation

Reauthorization should not become an unevidenced bypass path.

## Example 7: Approval Influenced by Untrusted Input

### Scenario

An external email contains instructions telling the agent to mark an action as urgent and request approval immediately.

The approval prompt repeats the external email's urgency language without warning the approver that the urgency came from untrusted content.

### Evidence Issue

The approval request may be influenced by untrusted input.

### Stronger Evidence

Stronger evidence would show:

- source of urgency claim;
- trust classification of the input;
- warning that urgency came from external content;
- policy-based risk classification;
- authorization decision based on trusted inputs;
- approval context separating trusted facts from untrusted claims.

### Assessment Interpretation

Approval evidence is weaker when untrusted content shapes the approval request without clear source and trust context.

## Example 8: Post-Execution Approval

### Scenario

The system performs a high-impact action and then asks a human to confirm that the action was acceptable.

### Assessment Interpretation

This is not pre-execution approval.

It may be useful as review or acknowledgement evidence, but it should not satisfy an approval requirement for high-risk or critical action authorization.

## Example 9: Broad Reusable Approval

### Scenario

A user approves:

> Allow this agent to handle all procurement requests this week.

The agent later executes several high-impact purchases with different vendors, amounts, and business purposes.

### Evidence Issue

The approval is broad and reusable.

### Assessment Interpretation

Broad approval may be acceptable only if bounded by clear policy, scope, thresholds, time limits, resource constraints, and evidence requirements.

For high-impact actions, reviewers should verify whether each resulting action remained within the approved scope and whether additional approval was required for material risk changes.

## Example 10: Approval Evidence Minimization

### Scenario

A system avoids storing full customer records in approval evidence.

Instead, it records identifiers, hashes, structured summaries, and references.

### Strong Evidence

Evidence may include:

- customer record reference;
- action digest;
- policy version;
- approval ID;
- approver ID;
- approval timestamp;
- redacted summary;
- evidence minimization method;
- secure reference to full record where authorized.

### Assessment Interpretation

This can be strong evidence if reviewers can reconstruct the action and verify approval linkage without unnecessary sensitive data exposure.

Approval quality does not require raw prompt or full payload retention by default.

## Review Questions

Assessors should ask:

1. What did the approver actually see?
2. Was the approval captured before execution?
3. Was the approval specific to the canonical action?
4. Was the approval linked to principal context and authority basis?
5. Was the approval linked to the final dispatch and execution record?
6. Did the action change after approval?
7. Was reapproval required after material change?
8. Was the approval influenced by untrusted input?
9. Was the approval reusable, broad, or scope-limited?
10. Could approval fatigue make the approval less meaningful?
11. Was sensitive data minimized without losing reviewability?
12. Would an incident reviewer understand what was approved and what happened?

## Finding Patterns

Reviewers may record findings for:

- generic approval prompts;
- missing action context;
- missing principal context;
- missing authority basis;
- missing risk or consequence summary;
- approval not linked to canonical action;
- approval not linked to dispatch or execution;
- approval after execution;
- broad reusable approval without constraints;
- material changes after approval without reapproval;
- approval laundering;
- payload substitution;
- untrusted input shaping approval without warning;
- excessive approval volume without fatigue controls;
- approval records that cannot support incident reconstruction.

## Non-Goals

These examples do not require:

- a specific approval UI;
- a specific workflow system;
- raw prompt retention;
- full payload capture by default;
- human approval for every action;
- multi-party approval for every high-impact action;
- a specific evidence schema change.

## Future Work

Future AAEF work may decide whether to:

- add approval evidence examples to JSON examples;
- add approval quality fields to the Evidence Event Schema;
- define approval fatigue metrics;
- define approval laundering negative tests;
- strengthen `AAEF-EVD-03`;
- add profile-specific approval evidence requirements for audit-grade actions.
