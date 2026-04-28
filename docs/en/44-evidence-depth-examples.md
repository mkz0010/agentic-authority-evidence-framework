# Evidence Depth Examples

**Status:** v0.5.0 planning examples
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative examples for E3, E4, and E5 evidence depth assessment

## Purpose

This document provides non-normative examples for applying evidence depth levels in AAEF v0.5.0 planning.

It focuses on:

- E3: High-impact evidence;
- E4: Audit-grade evidence;
- E5: Tamper-evident or independently verifiable evidence.

This document does not change the Evidence Event Schema, control catalog, testing procedures, or assessment worksheet.

## Core Principle

Evidence depth should increase with action risk, review need, and consequence.

A high-impact action should not rely only on minimal operational logs.

An audit-grade action should support reconstruction by reviewers who were not involved in the original action.

An E5 action should include tamper-evident, independently corroborated, or independently verifiable evidence properties where appropriate.

## Related Planning Documents

These examples relate to:

- `docs/en/36-risk-proportional-evidence-profile.md`
- `docs/en/37-tamper-evident-evidence-storage.md`
- `docs/en/38-v050-evidence-schema-field-candidates.md`
- `docs/en/40-approval-evidence-examples.md`
- `docs/en/41-non-execution-reauthorization-examples.md`
- `docs/en/42-tamper-evident-evidence-examples.md`
- `docs/en/43-risk-proportional-evidence-assessment-guidance.md`

## Example 1: E3 High-Impact Evidence

### Scenario

An agent updates a production configuration setting that affects customer-facing behavior.

The action is high-impact but reversible and does not require external audit evidence.

### Expected Evidence

E3 evidence should usually include:

- canonical action ID or action digest;
- agent identity;
- agent instance or workflow identifier;
- principal context;
- authority basis;
- authorization decision;
- policy version;
- requested action;
- target resource;
- risk classification;
- dispatch record;
- backend execution result;
- timestamp;
- correlation ID;
- evidence source;
- evidence trust limitation.

### Weak Evidence

Weak evidence includes:

- generic model output saying the action was completed;
- screenshot of a chat response;
- local agent log without principal, authorization, or resource context;
- backend log without linkage to the agentic action;
- uncorrelated records across authorization, dispatch, and execution.

### Assessment Interpretation

This is E3 when the evidence supports high-impact action reconstruction and control review, but does not necessarily include formal audit-grade review coverage or tamper-evident properties.

### Finding Patterns

Findings may arise when:

- principal context is missing;
- authority basis is missing;
- action and resource are ambiguous;
- dispatch and backend execution are not correlated;
- evidence is only model self-reporting;
- the evidence source and limitations are not documented.

## Example 2: E3 Non-Execution Evidence

### Scenario

An agent attempts to perform a high-impact action but the system denies execution due to missing authority.

### Expected Evidence

E3 non-execution evidence should usually include:

- attempted action ID;
- principal context;
- requested action;
- target resource;
- denial reason;
- authority gap;
- policy reference;
- dispatch prevention record;
- final non-execution outcome;
- retry correlation where applicable.

### Weak Evidence

Weak evidence includes:

- "blocked" without action context;
- denial reason stored only in model memory;
- no record of whether dispatch was prevented;
- no correlation between retry attempts;
- no final outcome.

### Assessment Interpretation

High-impact non-execution is security-relevant. E3 evidence should show why execution did not proceed and whether the system failed closed.

## Example 3: E4 Audit-Grade Approval Evidence

### Scenario

An agent proposes a high-value vendor payment.

The action requires approval and may be reviewed later by finance, audit, or incident response teams.

### Expected Evidence

E4 evidence should usually include:

- canonical action ID or action digest;
- approval request ID;
- approver identity or role;
- approval timestamp;
- principal context;
- authority basis;
- target vendor;
- amount and currency;
- business purpose;
- risk classification;
- policy threshold;
- context shown to approver;
- approval decision;
- authorization decision;
- dispatch record;
- backend execution record;
- correlation across approval, authorization, dispatch, and execution;
- retention policy reference;
- evidence trust limitations.

### Weak Evidence

Weak evidence includes:

- generic "approved" record;
- approver click without action context;
- approval not linked to final execution;
- post-execution approval presented as pre-execution approval;
- approval summary that differs from the executed action.

### Assessment Interpretation

This is E4 when the evidence supports formal accountability review and allows a reviewer to understand what was approved, why approval was required, what was dispatched, and what executed.

### Finding Patterns

Findings may arise when:

- the approver did not see enough context;
- the executed action differs materially from the approved action;
- approval records are not linked to dispatch or backend execution;
- approval evidence cannot distinguish approval, denial, reauthorization, and final execution states.

## Example 4: E4 Reauthorization Evidence

### Scenario

An agent is denied because the requested scope exceeds delegated authority.

The agent requests additional scope through a reauthorization flow.

### Expected Evidence

E4 reauthorization evidence should usually include:

- original denied action ID;
- denial reason;
- requested additional scope;
- principal reconfirmation where required;
- approver or escalation target;
- reauthorization request ID;
- final decision;
- post-reauthorization effective scope;
- retry count;
- retry correlation;
- final dispatch or final non-execution record;
- approval fatigue or task-splitting indicator where applicable.

### Weak Evidence

Weak evidence includes:

- informal chat approval;
- no link to original denial;
- no requested scope;
- no effective scope after reauthorization;
- no retry count;
- no final outcome.

### Assessment Interpretation

This is E4 when the evidence allows reviewers to reconstruct why the first action was denied, what additional authority was requested, who approved or denied it, and whether the final action stayed within the approved scope.

## Example 5: E4 Human Override Evidence

### Scenario

A human operator overrides an agentic authorization flow during an incident.

### Expected Evidence

E4 override evidence should usually include:

- override event ID;
- linked action ID;
- original decision;
- changed decision;
- override actor;
- override authority basis;
- override reason;
- override scope;
- timestamp;
- affected control path;
- post-review requirement;
- incident or ticket reference;
- final action outcome.

### Weak Evidence

Weak evidence includes:

- manual change without linked action evidence;
- override reason stored only in chat;
- original evidence overwritten;
- no post-review requirement;
- no affected control context.

### Assessment Interpretation

Override evidence should supplement the original evidence trail, not erase it.

## Example 6: E5 Tamper-Evident Evidence

### Scenario

A critical action affects production access rights and may be reviewed during an incident.

The organization needs evidence integrity beyond normal operational logging.

### Expected Evidence

E5 evidence may include:

- E4 lifecycle evidence;
- append-only or write-restricted evidence store;
- signed evidence record;
- hash chain;
- Merkle root;
- external timestamp reference;
- immutable storage policy;
- integrity verification result;
- independent corroborating log;
- deletion or redaction record;
- evidence trust limitation.

### Weak Evidence

Weak evidence includes:

- mutable local log;
- evidence stored only in the agent runtime;
- no integrity verification;
- no independent corroboration;
- no detection of deletion, replay, truncation, or reordering;
- no documented evidence trust limitation.

### Assessment Interpretation

This is E5 when alteration, deletion, replay, reordering, truncation, selective omission, or inconsistency is detectable.

E5 does not prove that the action was correct. It strengthens confidence that the evidence record has not been silently manipulated.

## Example 7: E5 Independently Corroborated Evidence

### Scenario

A disputed high-impact action is reconstructed from several independent sources.

### Expected Evidence

E5 evidence may include:

- authorization decision log;
- tool dispatch log;
- backend API audit log;
- cloud audit trail;
- SIEM event;
- approval workflow record;
- shared correlation ID;
- consistent action ID or digest;
- consistent principal and resource;
- source trust limitations;
- inconsistency handling.

### Weak Evidence

Weak evidence includes:

- only one mutable source;
- inconsistent logs with no reconciliation;
- missing backend execution evidence;
- missing authorization decision evidence;
- no source trust limitations.

### Assessment Interpretation

Independent corroboration is valuable when one component may be compromised, incomplete, or unreliable.

Reviewers should inspect inconsistencies rather than assuming that all logs are equally trustworthy.

## Example 8: Evidence Depth Mismatch

### Scenario

A system classifies all agent actions as E1 to reduce logging cost.

Some actions include production access changes, payments, and customer data exports.

### Assessment Interpretation

This is an evidence depth mismatch.

E1 may be acceptable for low-risk operational activity, but not for high-impact or critical actions requiring reconstruction, approval review, non-execution review, or incident response.

### Finding Patterns

Findings may arise when:

- high-impact actions are assigned E1;
- evidence depth is selected for convenience rather than risk;
- evidence does not support reconstruction;
- evidence minimization is used as a reason for missing essential evidence.

## Example 9: Excessive Evidence Depth

### Scenario

A system records full prompts, full payloads, customer records, and raw intermediate reasoning for every low-risk action.

### Assessment Interpretation

Risk-proportional evidence should not mean collecting everything.

Evidence should be sufficient, action-bound, and reviewable, but also privacy-aware and minimized.

### Finding Patterns

Findings may arise when:

- sensitive data is retained without need;
- raw prompts are retained by default without justification;
- full payload retention replaces structured evidence design;
- retention policy is unclear;
- access controls are weak.

## Example 10: Candidate Field Representation

### Scenario

A future evidence event includes candidate evidence depth fields.

### Candidate Representation

A future schema or example-only representation may include:

- evidence depth level;
- evidence depth rationale;
- evidence depth source;
- evidence depth limitations.

### Assessment Interpretation

These candidate fields could help reviewers understand whether the evidence depth is expected, applied, policy-driven, risk-driven, or limited by implementation constraints.

The current Evidence Event Schema is not changed by this document.

## Review Questions

Assessors should ask:

1. What evidence depth was expected?
2. Why was that depth selected?
3. What action risk or impact justified the depth?
4. Does the evidence support reconstruction?
5. Does it support authorization review?
6. Does it support approval review where applicable?
7. Does it support non-execution or reauthorization review where applicable?
8. Does it support incident response?
9. Does it include evidence source and trust limitations?
10. Does it avoid unnecessary sensitive data?
11. Does it require tamper-evident or independently verifiable properties?
12. Would the evidence remain useful if one component were compromised?

## Finding Patterns

Reviewers may record findings for:

- high-impact actions with only E1 evidence;
- audit-grade claims based on mutable logs;
- missing principal or authority context;
- missing dispatch or execution linkage;
- missing approval linkage;
- missing non-execution evidence;
- missing reauthorization linkage;
- missing integrity verification for E5 claims;
- missing evidence trust limitations;
- excessive sensitive data retention;
- evidence depth selected without rationale.

## Non-Goals

These examples do not require:

- adding `evidence_depth_level` to the current schema;
- E5 evidence for every action;
- raw prompt retention;
- full payload retention;
- blockchain;
- remote attestation for every action;
- a specific SIEM or evidence store.

## Future Work

Future AAEF work may decide whether to:

- add E3, E4, and E5 JSON examples;
- add `evidence_depth_level` to the Evidence Event Schema;
- define minimum evidence depth by action class;
- add evidence depth to assessment profiles;
- define evidence minimization requirements by depth;
- define evidence depth negative tests.
