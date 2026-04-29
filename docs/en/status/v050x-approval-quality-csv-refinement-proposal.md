# v0.5.x Approval Quality Testing CSV Refinement Proposal

**Status:** Temporary, non-normative CSV refinement proposal

## Purpose

This document records the proposed path for incorporating approval quality testing candidates into active testing artifacts.

It follows:

- `docs/en/status/v050x-approval-quality-testing-candidate-appendix.md`
- `docs/en/status/v050x-approval-quality-testing-proposal.md`
- `docs/en/status/v050x-testing-incorporation-readiness-review.md`
- `docs/en/status/v050x-testing-draft-pass-fail-criteria.md`
- `docs/en/status/v050x-testing-candidate-mapping.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Related guidance documents:

- `docs/en/39-approval-quality-approval-fatigue.md`
- `docs/en/40-approval-evidence-examples.md`
- `docs/en/47-approval-quality-assessment-guidance.md`
- `docs/en/52-approval-quality-model.md`
- `docs/en/62-approval-quality-testing-guidance.md`

This document does not change the v0.4.1 control and assessment baseline.

It does not update the active testing procedure CSV.

It does not create executable fixtures.

## Current Testing CSV Constraint

The active testing procedure draft is:

- `assessment/aaef-testing-procedures-v0.4-draft.csv`

The current testing procedure validator expects testing procedure rows to match the control catalog one-to-one.

Therefore, temporary `VTC-APP-*` candidate IDs should not be added directly to the active testing procedure CSV unless a later change explicitly updates the testing model, validator, and related documentation.

## Existing Active Coverage

The current active control catalog and testing procedure CSV already include several approval-oriented rows.

The most relevant active rows are:

- `AAEF-HUM-01` — human approval requests shall present sufficient action-bound context for meaningful review;
- `AAEF-HUM-02` — approval workflows shall reduce blind approval, rubber-stamping, excessive prompting, and approval fatigue;
- `AAEF-AUZ-03` — high-risk and critical actions require meaningful, risk-proportional explicit approval or additional verification before execution;
- `AAEF-EVD-03` — approval evidence shall be linked to the action evidence;
- `AAEF-AUZ-01` — high-impact actions shall be authorized at the point of execution;
- `AAEF-TOOL-02` — tool invocation shall be governed by explicit policy rather than model output alone;
- `AAEF-TOOL-04` — tool invocation requests derived from untrusted or external content shall be subject to intent validation and policy checks before execution.

This means immediate new control IDs are not required for the first approval quality testing refinement batch.

## Decision

Do not add `VTC-APP-*` rows directly to the active testing procedure CSV at this stage.

Instead, treat approval quality candidates as refinement inputs for existing HUM, AUZ, EVD, and TOOL testing rows.

This avoids:

- breaking one-to-one validation with the control catalog;
- turning temporary VTC IDs into apparent active requirements;
- changing the active baseline before reviewer agreement;
- adding new approval quality control IDs before confirming that existing rows are insufficient;
- mixing candidate tests with current control-linked testing procedures.

## Candidate-to-Active-Row Mapping

| Candidate | Primary existing row | Secondary existing rows | Proposed incorporation path |
| --- | --- | --- | --- |
| VTC-APP-01 Vague Approval Prompt for High-Impact Action | AAEF-HUM-01 | AAEF-AUZ-03, AAEF-EVD-03 | Refine approval context language and evidence linkage where needed. |
| VTC-APP-02 Approval to Draft Treated as Approval to Execute | AAEF-AUZ-03 | AAEF-HUM-01, AAEF-EVD-03 | Refine operation-class and execution-specific approval language. |
| VTC-APP-03 Canonical Action Mismatch | AAEF-AUZ-03 | AAEF-EVD-03, AAEF-HUM-01 | Refine canonical action / action digest / final dispatched action matching language. |
| VTC-APP-04 Approval Payload Modified After Approval | AAEF-AUZ-03 | AAEF-EVD-03, AAEF-HUM-01 | Refine material post-approval change and reapproval language. |
| VTC-APP-08 Model-Generated Approval Summary Accepted as Evidence | AAEF-EVD-03 | AAEF-EVD-01, AAEF-EVD-02, AAEF-HUM-01 | Refine trusted approval evidence source expectations. |
| VTC-APP-09 Approval Without Independent Enforcement | AAEF-AUZ-03 | AAEF-AUZ-01, AAEF-TOOL-02, AAEF-EVD-03 | Refine execution-bound approval enforcement language. |

## Minimal First CSV Refinement Candidate

The smallest active CSV refinement candidate should be limited to:

- VTC-APP-01 mapped primarily to `AAEF-HUM-01`;
- VTC-APP-03 mapped primarily to `AAEF-AUZ-03`;
- VTC-APP-09 mapped primarily to `AAEF-AUZ-03`.

These three are the most directly tied to meaningful approval and execution-bound enforcement.

## Proposed AAEF-HUM-01 Refinement Direction

### Current concern

`AAEF-HUM-01` already covers approval context and meaningful review.

However, the approval quality testing work indicates that vague approval prompts should be explicitly visible in testing language.

### Proposed refinement area

Potential future refinements may clarify that samples should include, where feasible:

- approval prompt or review surface;
- exact context presented to the approver;
- agent and principal context;
- requested action;
- target, resource, purpose, and scope;
- authority basis;
- risk level;
- expected effect;
- material limitations and consequence;
- linkage to final dispatched or executed action.

### Candidate impact

This would incorporate the core of VTC-APP-01 without adding a new testing row.

## Proposed AAEF-AUZ-03 Refinement Direction

### Current concern

`AAEF-AUZ-03` already covers meaningful, risk-proportional approval or additional verification before execution, including canonical action ID or action digest and final dispatch linkage.

However, the approval quality testing work indicates that the row should more explicitly test two issues:

- approved canonical action must match the dispatched or executed action;
- approval state must be independently enforced before execution.

### Proposed refinement area

Potential future refinements may clarify that samples should include, where feasible:

- approved canonical action;
- action digest or canonical action ID;
- approved operation class;
- final dispatched or executed action;
- approval scope;
- approval state source;
- enforcement check before execution;
- material mismatch check;
- denial, escalation, reapproval, or execution outcome.

### Candidate impact

This would incorporate the core of VTC-APP-03 and VTC-APP-09 without adding a new testing row.

## Proposed AAEF-EVD-03 Refinement Direction

### Current concern

`AAEF-EVD-03` already covers linking approval evidence to action evidence.

However, approval quality testing indicates that the row may later need more explicit trusted-source language.

### Proposed refinement area

Potential future refinements may clarify that approval evidence should distinguish:

- trusted approval workflow records;
- approval UI or workflow state;
- model-generated approval summaries;
- approval claims or rationales;
- approval ID or workflow record;
- linkage to authorization, dispatch, and execution evidence;
- evidence source trust status.

### Candidate impact

This would incorporate the core of VTC-APP-08 later, but it is not recommended for the first active CSV refinement batch.

## Candidates Not Recommended for Immediate CSV Refinement

### VTC-APP-02 — Approval to Draft Treated as Approval to Execute

This candidate should remain close, but may require clearer operation-class vocabulary before active CSV refinement.

It may be incorporated through `AAEF-AUZ-03` after confirming draft, preview, recommendation, execution, publish, send, delete, spend, and externally effective action categories.

### VTC-APP-04 — Approval Payload Modified After Approval

This candidate should remain close, but may require clearer materiality thresholds.

Questions include:

- which payload changes are material;
- whether target, recipient, amount, environment, or tool changes always require reapproval;
- how post-approval change checks should be evidenced.

### VTC-APP-08 — Model-Generated Approval Summary Accepted as Evidence

This candidate should remain close, but may map more cleanly to evidence quality refinement than human approval refinement.

It should likely be handled through `AAEF-EVD-03`, and possibly `AAEF-EVD-01` or `AAEF-EVD-02`, after deciding how AAEF wants to phrase trusted approval evidence source expectations.

## Proposed Next Active CSV PR

A later active CSV PR, if approved, should be narrow.

Recommended initial scope:

- refine only `AAEF-HUM-01`;
- refine only `AAEF-AUZ-03`;
- do not add new rows;
- do not add `VTC-APP-*` IDs to active CSV;
- update only testing language, not control requirements;
- validate that the one-to-one testing procedure model remains intact.

## Review Questions Before Active CSV Change

Before editing the active testing procedure CSV, reviewers should answer:

- Should VTC-APP-01 be incorporated into `AAEF-HUM-01`, `AAEF-AUZ-03`, or both?
- Should VTC-APP-03 be incorporated into `AAEF-AUZ-03`, `AAEF-EVD-03`, or both?
- Should VTC-APP-09 be incorporated into `AAEF-AUZ-03`, `AAEF-AUZ-01`, `AAEF-TOOL-02`, or multiple rows?
- Should approval enforcement be tested as authorization behavior, tool-dispatch behavior, evidence behavior, or all three?
- Should vague approval prompt language appear in sample selection, pass criteria, fail conditions, notes, or all four?
- Should canonical action mismatch be handled as approval quality, authorization binding, evidence linkage, or all three?
- Would these refinements materially change control expectations, or only clarify testing?
- Should #167 remain open after the first CSV refinement because draft-vs-execute, post-approval modification, approval evidence trust, and approval fatigue remain unresolved?

## Relationship to #167

This document supports #167 by identifying a safe path from approval quality testing candidates toward active testing procedure refinement.

It does not close #167.

Remaining #167 work includes:

- deciding whether to refine active testing CSV rows;
- deciding whether VTC-APP-02, VTC-APP-04, and VTC-APP-08 are ready for later refinement;
- defining minimum approval context fields;
- defining approval-to-execution binding evidence expectations;
- defining post-approval modification materiality;
- defining model-generated approval summary evidence treatment;
- deciding whether related evidence/schema or assessment profile changes are needed.

## Non-Goals

This document does not:

- update testing procedure CSV;
- add active testing procedure rows;
- add `VTC-APP-*` IDs to active CSV;
- create executable fixtures;
- add control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- close #167;
- change the one-to-one testing procedure model.

It is a temporary CSV refinement proposal for the v0.5.x incorporation phase.
