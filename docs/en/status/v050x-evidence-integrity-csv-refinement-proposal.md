# v0.5.x Evidence Integrity CSV Refinement Proposal

**Status:** Temporary, non-normative CSV refinement proposal

## Purpose

This document records the proposed path for evaluating whether evidence integrity and tamper-evident evidence work should be incorporated into active testing artifacts.

It follows the v0.5.x incorporation pattern used for principal context, cross-agent delegation, and approval quality work.

Related active control area:

- `AAEF-EVD-04` — Evidence Integrity / Tamper-Evident Evidence

Related evidence and auditability rows:

- `AAEF-EVD-01` — High-Impact Action Evidence
- `AAEF-EVD-02` — Evidence Fields
- `AAEF-EVD-03` — Approval Evidence Linkage
- `AAEF-EVD-05` — Non-Execution Evidence
- `AAEF-EVD-06` — Reauthorization Evidence

This document does not change the v0.4.1 control and assessment baseline.

It does not update the active testing procedure CSV.

It does not create executable fixtures.

## Current Testing CSV Constraint

The active testing procedure draft is:

- `assessment/aaef-testing-procedures-v0.4-draft.csv`

The current testing procedure validator expects testing procedure rows to match the control catalog one-to-one.

Therefore, temporary evidence integrity candidate IDs should not be added directly to the active testing procedure CSV unless a later change explicitly updates the testing model, validator, and related documentation.

## Existing Active Coverage

The current active testing procedure CSV already includes substantial evidence integrity coverage in `AAEF-EVD-04`.

`AAEF-EVD-04` already covers:

- critical and audit-grade action evidence;
- undetected alteration;
- deletion;
- replay;
- reordering;
- truncation;
- selective omission;
- integrity verification;
- append-only logs;
- write-restricted evidence stores;
- signed evidence records;
- hash chains;
- Merkle roots;
- external timestamps;
- immutable storage policies;
- independent corroborating logs;
- retention policy;
- deletion or redaction records;
- evidence trust limitations.

This means immediate new control IDs are not required for the first evidence integrity refinement batch.

## Decision

Do not add temporary evidence integrity candidate IDs directly to the active testing procedure CSV at this stage.

Do not create new control IDs at this stage.

Treat evidence integrity and tamper-evident evidence work as refinement input for `AAEF-EVD-04` first.

This avoids:

- breaking one-to-one validation with the control catalog;
- turning temporary candidate IDs into apparent active requirements;
- changing the active baseline before reviewer agreement;
- adding new evidence integrity controls before confirming that `AAEF-EVD-04` is insufficient;
- mixing candidate tests with current control-linked testing procedures.

## Candidate-to-Active-Row Mapping

| Candidate theme | Primary existing row | Secondary existing rows | Proposed incorporation path |
| --- | --- | --- | --- |
| Tamper-evident evidence storage | AAEF-EVD-04 | AAEF-EVD-01, AAEF-EVD-02 | Keep centered on EVD-04; only refine if more explicit verification expectations are needed. |
| Evidence deletion detection | AAEF-EVD-04 | AAEF-EVD-05, AAEF-EVD-06 | Keep centered on EVD-04; apply to non-execution and reauthorization evidence through sample selection. |
| Evidence replay detection | AAEF-EVD-04 | AAEF-EVD-01, AAEF-EVD-02 | Keep centered on EVD-04; clarify replay detection only if needed. |
| Evidence reordering detection | AAEF-EVD-04 | AAEF-EVD-01 | Keep centered on EVD-04; clarify sequence or timestamp verification only if needed. |
| Selective omission detection | AAEF-EVD-04 | AAEF-EVD-01, AAEF-EVD-05, AAEF-EVD-06 | Keep centered on EVD-04; clarify coverage and completeness only if needed. |
| Evidence trust limitations | AAEF-EVD-04 | AAEF-EVD-01, AAEF-EVD-02 | Keep centered on EVD-04; refine language around evidence trust limitation and verification result only if needed. |
| Self-reported evidence limitations | AAEF-EVD-01 | AAEF-EVD-02, AAEF-EVD-04 | Consider later refinement, but do not include in the first active CSV batch unless EVD-01 needs stronger language. |

## Minimal First CSV Refinement Candidate

The smallest active CSV refinement candidate, if any, should be limited to:

- `AAEF-EVD-04` only.

However, based on current active testing language, even this may not be necessary immediately.

The current `AAEF-EVD-04` row already includes:

- storage, integrity, retention, and verification mechanisms;
- sampled critical or audit-grade evidence;
- modification, deletion, replay, reordering, truncation, inconsistency, and selective omission detection;
- concrete evidence examples for tamper-evident and integrity mechanisms.

Therefore, the recommended next step is not immediate active CSV modification.

The recommended next step is to document review questions and decide whether `AAEF-EVD-04` requires only status closure, a minor wording refinement, or later evidence schema work.

## Proposed AAEF-EVD-04 Refinement Direction

### Current concern

`AAEF-EVD-04` is already strong and directly addresses tamper-evident evidence.

The remaining open question is not whether the concept exists in active testing procedures, but whether testing language should be more explicit about:

- integrity verification result;
- verification failure behavior;
- minimum evidence integrity coverage by action risk;
- whether evidence integrity applies only to critical and audit-grade evidence or broader high-impact evidence;
- whether evidence trust limitations are required for all protected evidence;
- whether independently corroborated evidence is an alternative or supplement to cryptographic tamper evidence;
- whether deletion and redaction records should be treated as evidence integrity records.

### Potential future refinement area

Potential future refinements may clarify that samples should include, where feasible:

- protected evidence class;
- integrity mechanism;
- verification method;
- verification result;
- verification timestamp;
- evidence chain or batch reference;
- deletion, redaction, or retention event where applicable;
- replay or reordering detection evidence;
- selective omission detection or completeness check;
- independent corroborating log or external anchor where applicable;
- evidence trust limitation.

### Candidate impact

This would refine `AAEF-EVD-04` without adding a new testing row.

## Proposed AAEF-EVD-01 Relationship

`AAEF-EVD-01` requires evidence sufficient to reconstruct what happened.

Evidence integrity supports that objective, but does not replace it.

A later refinement may clarify that reconstruction should not rely solely on mutable, self-reported, contradictory, or unverifiable evidence for critical or audit-grade actions.

However, this should be treated as secondary to `AAEF-EVD-04`.

## Proposed AAEF-EVD-02 Relationship

`AAEF-EVD-02` standardizes required evidence fields.

A later evidence schema or field-level refinement may be needed if AAEF decides to add structured integrity fields such as:

- evidence hash;
- evidence chain reference;
- signature reference;
- storage integrity mechanism;
- tamper-evidence indicator;
- retention class;
- integrity verification result.

This should not be added to the active testing procedure CSV until evidence schema direction is decided.

## Proposed AAEF-EVD-05 and AAEF-EVD-06 Relationship

`AAEF-EVD-05` and `AAEF-EVD-06` cover non-execution and reauthorization evidence.

Evidence integrity matters for these records, but the first active refinement should not spread across EVD-05 and EVD-06.

Instead, EVD-04 sample selection can already include non-execution, reauthorization, approval, and override evidence where available.

## Candidates Not Recommended for Immediate CSV Refinement

### New evidence integrity candidate rows

Do not add temporary candidate rows to active CSV.

The one-control-one-row model should remain intact.

### Broad EVD-01 rewrite

Do not broaden `AAEF-EVD-01` yet.

It is the general reconstruction control and should not absorb all evidence integrity expectations.

### EVD-02 field expansion

Do not expand active field expectations yet.

Any field-level change should be coordinated with evidence schema review.

### EVD-05 / EVD-06 integrity-specific edits

Do not refine EVD-05 or EVD-06 yet.

Integrity-specific expectations should remain centralized in EVD-04 unless a concrete gap appears.

## Proposed Next Active CSV PR

A later active CSV PR, if approved, should be narrow.

Recommended initial scope:

- refine only `AAEF-EVD-04`, or make no active CSV change;
- do not add new rows;
- do not add temporary candidate IDs to active CSV;
- update only testing language, not control requirements;
- validate that the one-to-one testing procedure model remains intact.

## Review Questions Before Active CSV Change

Before editing the active testing procedure CSV, reviewers should answer:

- Is `AAEF-EVD-04` already sufficient for the first evidence integrity incorporation step?
- Should any active CSV refinement be made now, or should this be recorded as already incorporated?
- Should EVD-04 explicitly require integrity verification result evidence?
- Should EVD-04 explicitly require verification failure handling?
- Should EVD-04 distinguish cryptographic tamper evidence, append-only storage, write restriction, and independent corroboration?
- Should evidence trust limitations be required whenever integrity protection is partial?
- Should evidence integrity fields be added to the Evidence Event Schema before further active testing refinement?
- Should #165 remain open because schema fields, examples, negative tests, and incident-response preservation guidance remain unresolved?

## Relationship to #165

This document supports #165 by identifying a safe path from evidence integrity and tamper-evident evidence planning toward active testing procedure refinement.

It does not close #165.

Remaining #165 work may include:

- deciding whether `AAEF-EVD-04` needs additional active CSV refinement;
- deciding whether evidence integrity fields should be added to the Evidence Event Schema;
- defining E5 or higher-depth examples using tamper-evident evidence;
- defining minimum integrity expectations by evidence depth or action risk;
- defining negative tests for evidence tampering, deletion, replay, reordering, truncation, and selective omission;
- defining evidence replay tests;
- defining selective omission tests;
- defining incident-response evidence preservation guidance.

## Non-Goals

This document does not:

- update testing procedure CSV;
- add active testing procedure rows;
- add temporary candidate IDs to active CSV;
- create executable fixtures;
- add control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- close #165;
- change the one-to-one testing procedure model.

It is a temporary CSV refinement proposal for the v0.5.x incorporation phase.
