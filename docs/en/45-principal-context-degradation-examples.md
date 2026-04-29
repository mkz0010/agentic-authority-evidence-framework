# Principal Context Degradation Examples

**Status:** Non-normative v0.5.0 planning examples
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative examples for principal context freshness, ambiguity, drift, reconfirmation, denial, and reauthorization review

> **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifacts, testing procedures, or release notes.

## Purpose

This document provides non-normative examples for reviewing Principal Context Degradation in AAEF v0.5.0 planning.

It illustrates how reviewers can distinguish:

- fresh principal context;
- stale principal context;
- ambiguous principal context;
- role or authority drift;
- delegated authority expiration;
- cross-domain principal mismatch;
- approval under degraded principal context;
- reauthorization after principal reconfirmation;
- safe non-execution when principal context cannot be trusted;
- evidence expectations for principal context review.

This document does not change the Evidence Event Schema, control catalog, testing procedures, or assessment worksheet.

## Testing Guidance Follow-up

Principal context degradation testing guidance is maintained in `docs/en/59-principal-context-degradation-testing.md`.

That document extends these examples into non-normative test scenarios and candidate evidence expectations.

## Core Principle

Principal context is not valid merely because some principal identifier exists.

For high-impact actions, principal context should remain sufficiently current, specific, bounded, and semantically connected to the requested action.

When principal context is stale, ambiguous, degraded, or semantically distant from the requested action, the system should deny, defer, escalate, freeze, require reconfirmation, or require scoped reauthorization.

## Related Controls

These examples support review of:

- `AAEF-PRN-01`: principal binding for high-impact actions;
- `AAEF-PRN-02`: principal context validity;
- `AAEF-AUZ-04`: denial or escalation when authority, principal, or purpose cannot be determined;
- `AAEF-AUZ-09`: authority denial and reauthorization flow;
- `AAEF-EVD-05`: non-execution evidence;
- `AAEF-EVD-06`: reauthorization evidence;
- `AAEF-HUM-01`: meaningful human approval context.

For the related planning concept, see `docs/en/30-principal-context-degradation.md`.

## Example 1: Fresh Principal Context

### Scenario

A user signs in, selects a workspace, confirms the relevant role, and immediately instructs an agent to perform a high-impact but authorized action in that workspace.

### Strong Evidence

Strong evidence includes:

- principal ID;
- authenticated session reference;
- workspace or tenant context;
- role or authority basis;
- timestamp of context establishment;
- requested action;
- target resource;
- authorization decision;
- dispatch and execution linkage.

### Assessment Interpretation

This is a strong principal context example if the action is clearly tied to the current principal, role, workspace, purpose, and authorization decision.

## Example 2: Stale Session Context

### Scenario

A user authenticated in the morning.

Several hours later, the agent attempts a high-impact production change using the earlier principal context.

The user's role or active workspace may have changed.

### Risk Indicators

Reviewers should look for:

- old authentication timestamp;
- long-running agent session;
- missing reconfirmation;
- missing current role check;
- missing workspace or tenant reconfirmation;
- high-impact action attempted after context aging.

### Expected Safe Behavior

The system should:

- detect stale context;
- defer the action;
- require reauthentication or reconfirmation;
- record the reason for deferral;
- prevent dispatch until context is refreshed.

### Assessment Interpretation

Stale principal context should not silently authorize high-impact actions.

## Example 3: Role Change After Approval

### Scenario

A human approves an action while holding a privileged role.

Before execution, the approver's role is removed or the user's authority changes.

The agent later attempts to execute the action using the earlier approval.

### Expected Safe Behavior

The system should:

- detect material authority change;
- invalidate or limit the earlier approval where required;
- require reauthorization or reconfirmation;
- record the authority change;
- prevent execution if the approval is no longer valid.

### Assessment Interpretation

Approval should not remain valid when the principal or approver authority context materially changes before execution.

## Example 4: Delegated Authority Expiration

### Scenario

A user delegates limited authority to an agent for a one-hour maintenance window.

The agent attempts the action after the delegation expires.

### Strong Evidence

Strong evidence includes:

- delegation ID;
- delegating principal;
- delegated scope;
- effective time;
- expiration time;
- attempted action time;
- denial reason;
- final non-execution outcome.

### Assessment Interpretation

Expired delegated authority should trigger denial, deferral, or reauthorization.

A finding may be recorded if the agent can execute after delegation expiration without renewed authority.

## Example 5: Cross-Domain Principal Mismatch

### Scenario

An agent receives authority in one SaaS tenant but attempts to use that principal context to perform an action in a different tenant or domain.

### Risk Indicators

Reviewers should look for:

- principal bound to tenant A;
- action attempted in tenant B;
- missing cross-domain authority assertion;
- missing receiving-domain validation;
- ambiguous resource ownership;
- mismatch between delegation scope and target domain.

### Expected Safe Behavior

The receiving domain should not accept the principal context without validation.

The system should require a valid authority assertion, reauthorization, or denial.

### Assessment Interpretation

A principal identifier is not enough when the target domain, tenant, resource owner, or authority root differs.

## Example 6: Semantic Drift Between Request and Action

### Scenario

A user asks an agent to "clean up old reports."

The agent interprets this as permission to delete production records that include regulated customer data.

### Risk Indicators

Reviewers should look for:

- vague user request;
- high-impact action inferred from broad language;
- missing purpose confirmation;
- missing resource scope;
- missing data classification review;
- no reconfirmation before destructive action.

### Expected Safe Behavior

The system should:

- treat the principal context as semantically insufficient;
- ask for clarification or approval;
- narrow the requested scope;
- deny or defer destructive action until authority is explicit.

### Assessment Interpretation

Principal context can degrade through semantic distance, not only time.

## Example 7: Approval Under Degraded Principal Context

### Scenario

An approval prompt asks a user to approve an action but does not show which principal, tenant, role, workspace, or delegated authority basis will be used.

The user clicks approve.

### Evidence Issue

The approval exists, but the approval may not be meaningful because the principal context was not visible.

### Assessment Interpretation

Approval evidence is weaker when the approver cannot see the principal context under which the action will execute.

This may affect review of `AAEF-HUM-01`, `AAEF-PRN-02`, and `AAEF-EVD-03`.

## Example 8: Reauthorization After Principal Reconfirmation

### Scenario

An agent attempts a high-impact action under degraded context.

The system denies execution and requests principal reconfirmation.

The user reauthenticates, confirms the active workspace, and authorizes a narrower action scope.

### Strong Evidence

Strong evidence includes:

- original attempted action ID;
- degradation reason;
- denial or deferral decision;
- reconfirmation request ID;
- reauthenticated principal;
- confirmed workspace or tenant;
- confirmed role or authority basis;
- narrowed scope;
- reauthorization decision;
- final dispatch or final non-execution record.

### Assessment Interpretation

This is a strong reauthorization path if it links the original degraded context, reconfirmation, scope reduction, and final outcome.

## Example 9: Safe Non-Execution Due to Untrusted Principal Context

### Scenario

An agent receives instructions from an external email claiming to be from an executive.

The instruction asks the agent to approve a payment.

The system cannot bind the request to an authenticated principal.

### Expected Safe Behavior

The system should:

- classify the principal context as untrusted or unbound;
- deny or escalate the action;
- record the reason;
- prevent dispatch;
- preserve evidence for review.

### Assessment Interpretation

External content should not establish principal authority by itself.

This is a strong non-execution case if the system records the attempted action, untrusted source, missing binding, denial reason, and final outcome.

## Example 10: Principal Context Evidence Limitation

### Scenario

The system records a principal ID and action result, but does not record how the principal context was established, whether it was current, or which authority basis applied.

### Evidence Limitation

Missing evidence may include:

- authentication freshness;
- role or authority basis;
- tenant or workspace context;
- delegation scope;
- expiration;
- reconfirmation status;
- trust source;
- limitations.

### Assessment Interpretation

A reviewer may record a limitation even if the action appears to have a principal ID.

Principal context evidence should support review of why that principal was valid for that action at that time.

## Review Questions

Assessors should ask:

1. Was the principal context current at the time of authorization and execution?
2. Was the principal context specific to the target resource, tenant, workspace, or domain?
3. Was the principal context semantically connected to the requested action?
4. Was the principal's role or authority basis recorded?
5. Was delegation scope recorded where applicable?
6. Was delegation expiration checked?
7. Was reconfirmation required after material context change?
8. Was the approval prompt clear about the principal context?
9. Was external or untrusted content used as a source of principal authority?
10. Was degraded context handled through denial, deferral, escalation, freeze, or reauthorization?
11. Was the final outcome recorded?
12. Could an incident reviewer reconstruct why the system believed the principal context was valid or invalid?

## Finding Patterns

Reviewers may record findings for:

- stale principal context used for high-impact actions;
- missing role or authority basis;
- missing tenant, workspace, or domain binding;
- expired delegation accepted as valid;
- broad user intent converted into destructive action without reconfirmation;
- approval prompts that hide principal context;
- external content treated as principal authority;
- cross-domain principal mismatch;
- reauthorization not linked to the original degraded context;
- missing non-execution evidence for degraded context;
- missing evidence limitations.

## Non-Goals

These examples do not require:

- a specific identity provider;
- a specific session management system;
- a specific delegation protocol;
- reauthentication for every action;
- raw prompt retention;
- full payload retention;
- schema changes in the current Evidence Event Schema.

## Future Work

Future AAEF work may decide whether to:

- add principal context degradation JSON examples;
- add principal context degradation fields to the Evidence Event Schema;
- define freshness thresholds by action class;
- define negative tests for stale context, role drift, delegation expiration, and cross-domain mismatch;
- define assessment guidance for principal context reconfirmation;
- strengthen `AAEF-PRN-02` further.
