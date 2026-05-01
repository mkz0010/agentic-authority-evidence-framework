# v0.5.x Incorporation Review Checkpoint

> **Historical note:** This document records an earlier v0.5.x planning or incorporation state. The current completion state for #161 through #167 is summarized in `docs/en/status/v050x-follow-up-completion-summary.md`.


**Status:** Temporary, non-normative incorporation checkpoint

## Purpose

This document summarizes the v0.5.x incorporation review status after the first review cycle for selected follow-up issues.

It consolidates the current state after review and incorporation decisions for:

- #161 — principal context testing refinement;
- #163 — cross-agent delegation testing refinement;
- #165 — evidence integrity and tamper-evident evidence;
- #167 — approval quality testing refinement.

This document is a temporary coordination artifact.

It does not change the active baseline.

It does not update the control catalog.

It does not update testing procedures.

It does not update the evidence schema.

It does not close any follow-up issue by itself.

## Checkpoint Summary

| Issue | Topic | First incorporation result | Active artifact impact | Current status |
| --- | --- | --- | --- | --- |
| #161 | Principal context degradation / principal context testing | Partially incorporated | Active testing procedure CSV refined | Open, remaining edge cases |
| #163 | Cross-agent delegation testing | Partially incorporated | Active testing procedure CSV refined | Open, remaining delegation semantics |
| #165 | Evidence integrity / tamper-evident evidence | Substantially represented by existing active row | No immediate active CSV change required | Open, schema/examples/tests remain |
| #167 | Approval quality testing | Partially incorporated | Active testing procedure CSV refined | Open, remaining approval semantics |

## Completed Incorporation Work

### #161 — Principal Context

The first principal context testing refinement cycle has been completed.

Completed work includes:

- proposal and candidate review;
- active CSV refinement;
- status reflection;
- incorporation decision register update.

The first active refinement focused on existing principal context testing language rather than adding temporary candidate IDs or new controls.

Current state:

- first active incorporation completed;
- issue remains open;
- future work remains around long-running workflows, reauthorization, delegation edge cases, schema/profile implications, and additional testing depth.

### #163 — Cross-Agent Delegation

The first cross-agent delegation testing refinement cycle has been completed.

Completed work includes:

- proposal and candidate appendix;
- CSV refinement proposal;
- active CSV refinement for selected DEL rows;
- status reflection;
- incorporation decision register update.

The first active refinement preserved the one-control-one-row testing model.

Current state:

- first active incorporation completed;
- issue remains open;
- future work remains around capability-scoped delegation, fire-and-forget delegation, refusal propagation, downstream redelegation, minimum chain evidence, and possible schema/profile/control implications.

### #165 — Evidence Integrity

The first evidence integrity review cycle has been completed.

Completed work includes:

- CSV refinement proposal;
- determination that no immediate active testing procedure CSV change is required for the first incorporation step;
- status reflection;
- incorporation decision register update.

The review concluded that `AAEF-EVD-04` already substantially represents the core evidence integrity and tamper-evident evidence expectations.

Current state:

- first incorporation review completed;
- no immediate active CSV change required;
- issue remains open;
- future work remains around evidence schema fields, E5 or higher-depth examples, negative tests, evidence replay tests, selective omission tests, and incident-response evidence preservation guidance.

### #167 — Approval Quality

The first approval quality testing refinement cycle has been completed.

Completed work includes:

- proposal and candidate appendix;
- CSV refinement proposal;
- active CSV refinement for selected HUM and AUZ rows;
- status reflection;
- incorporation decision register update.

The first active refinement focused on meaningful approval context, what the approver actually saw, canonical action matching, approval scope, approval state source, and independent approval enforcement.

Current state:

- first active incorporation completed;
- issue remains open;
- future work remains around draft-vs-execute approval, post-approval payload modification, model-generated approval summary evidence, trusted approval evidence source expectations, approval fatigue, and possible schema/profile/control implications.

## Active Testing Procedure Impact So Far

The first incorporation cycle changed active testing procedures for selected topics only.

Active CSV refinements have been made for:

- principal context-related testing rows;
- cross-agent delegation-related testing rows;
- approval quality-related testing rows.

No active CSV refinement was made for #165 because `AAEF-EVD-04` already provides substantial coverage for the first evidence integrity incorporation step.

Temporary VTC-style candidate IDs were not added to the active testing procedure CSV.

The one-control-one-row testing procedure model remains intact.

## Remaining Work by Category

### Testing Procedure Refinement

Remaining testing-related work includes:

- capability-scoped delegation refinement;
- downstream redelegation tests;
- fire-and-forget delegation tests;
- refusal propagation tests;
- draft-vs-execute approval tests;
- post-approval payload modification tests;
- approval fatigue and repeated approval behavior;
- evidence replay, reordering, truncation, deletion, and selective omission negative tests.

### Evidence Schema and Examples

Remaining evidence-related work includes:

- deciding whether evidence integrity fields belong in the Evidence Event Schema;
- defining E5 or higher-depth tamper-evident evidence examples;
- defining trusted approval evidence source expectations;
- defining model-generated approval summary handling;
- defining evidence trust limitations more precisely where needed.

### Control Catalog and Profile Decisions

No new control IDs were added in the first incorporation cycle.

Remaining design questions include:

- whether approval quality needs new dedicated control entries later;
- whether cross-agent delegation needs additional controls for downstream redelegation or refusal propagation;
- whether evidence integrity should be tied to assessment profiles or evidence depth levels;
- whether principal context degradation requires profile-specific handling.

### Status and Maintenance

Temporary status documents remain useful while v0.5.x follow-up work is active.

They may later be:

- archived;
- removed;
- consolidated into stable documentation;
- converted into active testing, schema, profile, or guidance changes;
- replaced by issue-specific follow-up documents.

## Recommended Next Phase

The next phase should split remaining work into smaller follow-up tracks.

Recommended tracks:

1. Evidence schema and examples track
   - evidence integrity fields;
   - E5 evidence examples;
   - tamper-evident evidence examples;
   - trusted approval evidence source examples.

2. Negative testing track
   - evidence tampering;
   - evidence deletion;
   - evidence replay;
   - evidence reordering;
   - selective omission;
   - approval bypass;
   - delegation refusal propagation.

3. Delegation semantics track
   - capability-scoped delegation;
   - downstream redelegation;
   - fire-and-forget delegation;
   - refusal propagation;
   - minimum delegation chain evidence.

4. Approval semantics track
   - draft-vs-execute approval;
   - post-approval modification;
   - model-generated approval summaries;
   - approval fatigue and repeated approval.

5. Cleanup and publication-readiness track
   - status document consolidation;
   - document map review;
   - follow-up issue triage;
   - release note preparation.

## Non-Goals

This checkpoint does not:

- update active testing procedure CSV;
- add testing procedure rows;
- add candidate IDs to active CSV;
- change control catalog CSV;
- change human-readable control requirements;
- change assessment worksheet;
- change assessment profiles;
- change external framework mapping CSV;
- change evidence schema;
- change evidence examples;
- close #161, #163, #165, or #167.

It records the current incorporation review state after the first v0.5.x review cycle.

## Next Phase Track Plan

The next phase work split is recorded in `docs/en/status/v050x-next-phase-track-plan.md`.

The plan separates remaining work into:

- evidence schema and examples;
- evidence integrity negative tests;
- delegation semantics;
- approval semantics;
- cleanup and publication readiness.
