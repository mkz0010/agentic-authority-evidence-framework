# v0.5.x Principal Context Testing CSV Refinement Proposal

**Status:** Temporary, non-normative CSV refinement proposal

## Purpose

This document records the proposed path for incorporating principal context testing candidates into active testing artifacts.

It follows:

- `docs/en/status/v050x-principal-context-testing-candidate-appendix.md`
- `docs/en/status/v050x-principal-context-testing-proposal.md`
- `docs/en/status/v050x-testing-incorporation-readiness-review.md`
- `docs/en/status/v050x-testing-draft-pass-fail-criteria.md`
- `docs/en/status/v050x-testing-candidate-mapping.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

This document does not change the v0.4.1 control and assessment baseline.

It does not update the active testing procedure CSV.

It does not create executable fixtures.

## Current Testing CSV Constraint

The active testing procedure draft is:

- `assessment/aaef-testing-procedures-v0.4-draft.csv`

The current testing procedure validator expects testing procedure rows to match the control catalog one-to-one.

Therefore, temporary VTC candidate IDs should not be added directly to the active testing procedure CSV unless a later change explicitly updates the testing model, validator, and related documentation.

## Decision

Do not add `VTC-PCD-*` rows directly to the active testing procedure CSV at this stage.

Instead, treat the principal context candidates as refinement inputs for existing AUZ testing rows.

This avoids:

- breaking one-to-one validation with the control catalog;
- turning temporary VTC IDs into apparent active requirements;
- changing the active baseline before reviewer agreement;
- mixing candidate tests with current control-linked testing procedures.

## Candidate-to-Active-Row Mapping

| Candidate | Primary existing row | Secondary existing rows | Proposed incorporation path |
| --- | --- | --- | --- |
| VTC-PCD-02 Scope Expansion Accepted | AAEF-AUZ-02 | AAEF-AUZ-08, AAEF-AUZ-09, AAEF-TOOL-04 | Refine sampling, pass, partial, or fail language for requested-vs-authorized scope and scope expansion before execution. |
| VTC-PCD-03 Risk Escalation Ignored | AAEF-AUZ-07 | AAEF-AUZ-03, AAEF-AUZ-05, AAEF-AUZ-08 | Refine state/risk escalation testing language where risk changes before execution. |
| VTC-PCD-04 Revoked or Downscoped Principal Context Accepted | AAEF-AUZ-07 | AAEF-AUZ-08, AAEF-AUZ-09 | Refine runtime state and revocation/downscope testing language. |
| VTC-PCD-07 Untrusted Input Changes Principal Intent | AAEF-AUZ-05 | AAEF-AUZ-06, AAEF-AUZ-08, AAEF-TOOL-04, AAEF-EVD-05 | Refine untrusted input influence testing language and evidence expectations. |

## Minimal First CSV Refinement Candidate

The smallest active CSV refinement candidate should be limited to:

- VTC-PCD-02 mapped primarily to `AAEF-AUZ-02`
- VTC-PCD-04 mapped primarily to `AAEF-AUZ-07`

These two are the most concrete and least dependent on unresolved threshold definitions.

## Proposed AAEF-AUZ-02 Refinement Direction

### Current concern

`AAEF-AUZ-02` already covers requested purpose and target resource mismatch.

However, the principal context testing work indicates that scope expansion should be explicitly visible in testing language.

### Proposed refinement area

Potential future refinements may clarify that samples should include, where feasible:

- originally authorized scope;
- later requested or executed scope;
- target, tenant, resource, dataset, environment, or operation expansion;
- comparison between authorized and requested scope;
- denial, deferral, escalation, limitation, or reauthorization before execution.

### Candidate impact

This would incorporate the core of VTC-PCD-02 without adding a new testing row.

## Proposed AAEF-AUZ-07 Refinement Direction

### Current concern

`AAEF-AUZ-07` already covers material runtime state and includes revocation state.

However, the principal context testing work indicates that revoked, expired, or downscoped principal context should be explicit in testing language.

### Proposed refinement area

Potential future refinements may clarify that samples should include, where feasible:

- authority revocation;
- authority expiry;
- downscoped entitlement or authority;
- runtime state change affecting execution eligibility;
- state check timestamp or trusted state source;
- denial, freeze, escalation, limitation, or reauthorization before execution.

### Candidate impact

This would incorporate the core of VTC-PCD-04 without adding a new testing row.

## Candidates Not Recommended for Immediate CSV Refinement

### VTC-PCD-03 — Risk Escalation Ignored

This candidate should remain close, but may require clearer wording around:

- risk tier definitions;
- high-impact transition thresholds;
- relationship to `AAEF-AUZ-03`;
- relationship to assessment profiles.

### VTC-PCD-07 — Untrusted Input Changes Principal Intent

This candidate should remain close, but may require clearer wording around:

- material untrusted input influence;
- input source classification;
- trusted principal intent;
- relationship to `AAEF-AUZ-05`;
- relationship to `AAEF-TOOL-04` and evidence expectations.

## Proposed Next Active CSV PR

A later active CSV PR, if approved, should be narrow.

Recommended initial scope:

- refine only `AAEF-AUZ-02`;
- refine only `AAEF-AUZ-07`;
- do not add new rows;
- do not add VTC IDs to active CSV;
- update only testing language, not control requirements;
- validate the one-to-one testing procedure model remains intact.

## Review Questions Before Active CSV Change

Before editing the active testing procedure CSV, reviewers should answer:

- Should VTC-PCD-02 be incorporated into `AAEF-AUZ-02`, `AAEF-AUZ-08`, or both?
- Should VTC-PCD-04 be incorporated into `AAEF-AUZ-07`, `AAEF-AUZ-08`, or both?
- Should scope expansion and revocation/downscope be sample selection refinements, pass criteria refinements, fail condition refinements, or all three?
- Would the refinements materially change control expectations, or only clarify testing?
- Should the changelog describe the next change as testing refinement rather than a new testing requirement?
- Should #161 remain open after the first CSV refinement because task drift, retry, and task splitting remain unresolved?

## Relationship to #161

This document supports #161 by identifying a safe path from principal context testing candidates toward active testing procedure refinement.

It does not close #161.

Remaining #161 work includes:

- deciding whether to refine active testing CSV rows;
- deciding whether VTC-PCD-03 and VTC-PCD-07 are ready for later refinement;
- defining material task drift thresholds;
- defining retry-after-denial correlation;
- defining task splitting and aggregate-effect bypass criteria;
- deciding whether related evidence/schema candidates are needed.

## Non-Goals

This document does not:

- update testing procedure CSV;
- add active testing procedure rows;
- add VTC IDs to active CSV;
- create executable fixtures;
- add control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- close #161;
- change the one-to-one testing procedure model.

It is a temporary CSV refinement proposal for the v0.5.x incorporation phase.
