# v0.5.x Next Phase Track Plan

**Status:** Temporary, non-normative planning and coordination document

## Purpose

This document splits the remaining v0.5.x follow-up work into smaller tracks after the first incorporation review checkpoint.

It follows:

- `docs/en/status/v050x-incorporation-review-checkpoint.md`
- `docs/en/status/v050x-follow-up-status.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

This document covers remaining work related to:

- #161 — principal context testing refinement;
- #163 — cross-agent delegation testing refinement;
- #165 — evidence integrity and tamper-evident evidence;
- #167 — approval quality testing refinement.

This document does not change the active baseline.

It does not update active testing procedures.

It does not update the control catalog.

It does not update the evidence schema.

It does not close any follow-up issue by itself.

## Planning Summary

The first incorporation review cycle established that:

- #161 has an initial active testing procedure refinement incorporated;
- #163 has an initial active testing procedure refinement incorporated;
- #165 is substantially represented by existing `AAEF-EVD-04` for the first incorporation step;
- #167 has an initial active testing procedure refinement incorporated.

The remaining work should now be split into smaller, reviewable follow-up tracks.

## Track Overview

| Track ID | Track | Primary source issues | Priority | Expected output type |
| --- | --- | --- | --- | --- |
| T1 | Evidence schema and examples | #165, #167, #161, #163 | High | Schema proposal, examples, evidence guidance |
| T2 | Evidence integrity negative tests | #165 | High | Negative test proposal, candidate appendix, possible testing refinement |
| T3 | Delegation semantics | #163, #161 | High | Delegation semantics proposal, candidate tests, possible DEL refinements |
| T4 | Approval semantics | #167 | High | Approval semantics proposal, candidate tests, possible HUM/AUZ/EVD refinements |
| T5 | Cleanup and publication readiness | #161, #163, #165, #167 | Medium | Status cleanup, issue triage, release readiness material |

## T1 — Evidence Schema and Examples

### Purpose

Define whether additional evidence fields, examples, or evidence-depth guidance are needed after the first incorporation cycle.

### Source issues

- #165 — evidence integrity and tamper-evident evidence
- #167 — approval quality evidence
- #161 — principal context evidence
- #163 — delegation and authority lineage evidence

### Candidate work

- Decide whether evidence integrity fields belong in the Evidence Event Schema.
- Define whether E5 or higher-depth examples should be added.
- Define tamper-evident evidence examples.
- Define trusted approval evidence source expectations.
- Define model-generated approval summary handling.
- Define evidence trust limitation examples.
- Decide whether principal context freshness or delegation lineage fields require schema treatment.

### Possible outputs

- Evidence schema field proposal.
- E5 or higher-depth evidence example proposal.
- New or updated evidence examples.
- Guidance for trusted approval evidence source handling.
- Guidance for evidence trust limitations.

### Non-goals

This track should not immediately modify active testing procedures unless a schema or example decision requires a coordinated testing update.

## T2 — Evidence Integrity Negative Tests

### Purpose

Define negative tests for evidence tampering, deletion, replay, reordering, truncation, and selective omission.

### Source issues

- #165 — evidence integrity and tamper-evident evidence

### Candidate work

- Evidence tampering negative tests.
- Evidence deletion negative tests.
- Evidence replay negative tests.
- Evidence reordering negative tests.
- Evidence truncation negative tests.
- Selective omission negative tests.
- Verification failure behavior tests.
- Incident-response evidence preservation tests.

### Possible outputs

- Evidence integrity negative test proposal.
- Evidence integrity testing candidate appendix.
- Possible later `AAEF-EVD-04` refinement if a concrete active testing gap is found.
- Possible incident-response evidence preservation guidance.

### Non-goals

This track should not add temporary candidate IDs to the active testing procedure CSV.

This track should not duplicate `AAEF-EVD-04` unless a specific gap is identified.

## T3 — Delegation Semantics

### Purpose

Resolve remaining cross-agent delegation semantics that were intentionally left out of the first active CSV refinement.

### Source issues

- #163 — cross-agent delegation testing refinement
- #161 — principal context edge cases across delegation and long-running workflows

### Candidate work

- Capability-scoped delegation refinement.
- Downstream redelegation authority.
- Fire-and-forget delegation.
- Refusal propagation.
- Acceptance, refusal, pending, and timeout state evidence.
- Minimum delegation chain evidence expectations.
- Delegation behavior under principal context degradation.
- Delegation behavior under revocation, freeze, or reauthorization.

### Possible outputs

- Delegation semantics proposal.
- Delegation candidate appendix.
- Possible `AAEF-DEL-02` testing refinement.
- Possible additional `AAEF-DEL-05` refinement.
- Possible schema or evidence example follow-up if chain evidence fields are required.

### Non-goals

This track should not create new delegation controls until existing DEL rows are confirmed insufficient.

## T4 — Approval Semantics

### Purpose

Resolve remaining approval quality semantics that were intentionally left out of the first active CSV refinement.

### Source issues

- #167 — approval quality testing refinement

### Candidate work

- Draft-vs-execute approval operation-class semantics.
- Post-approval payload modification and materiality criteria.
- Model-generated approval summary treatment as evidence.
- Trusted approval evidence source expectations.
- Approval fatigue and repeated approval behavior.
- Approval batching and task-splitting interaction.
- Approval behavior under reauthorization.

### Possible outputs

- Approval semantics proposal.
- Approval candidate appendix.
- Possible `AAEF-EVD-03` refinement for trusted approval evidence linkage.
- Possible `AAEF-HUM-02` refinement for approval fatigue and repeated approval.
- Possible additional `AAEF-AUZ-03` refinement if operation-class or materiality semantics require it.

### Non-goals

This track should not create new approval quality controls until existing HUM, AUZ, and EVD rows are confirmed insufficient.

## T5 — Cleanup and Publication Readiness

### Purpose

Keep temporary status material manageable while v0.5.x follow-up work continues.

### Source issues

- #161
- #163
- #165
- #167

### Candidate work

- Review temporary status documents for duplication.
- Decide which status documents should remain active.
- Decide which status documents should be archived, consolidated, or removed later.
- Review `docs/en/document-map.md`.
- Review README repository tree.
- Review researcher overview links.
- Prepare v0.5.x release note material when appropriate.
- Triage whether large follow-up issues should remain open or be split into smaller issues.

### Possible outputs

- Status cleanup proposal.
- Follow-up issue split plan.
- Release readiness checklist.
- Documentation map cleanup PR.
- Publication-readiness notes.

### Non-goals

This track should not remove temporary documents until the related follow-up work has either been incorporated, explicitly deferred, or moved to replacement documents.

## Suggested Follow-Up Issue Split

The following issue split is recommended after this plan is accepted.

| Candidate issue title | Source issues | Track |
| --- | --- | --- |
| `[Follow-up] v0.5.x: Define evidence schema and examples for integrity and approval evidence` | #165, #167 | T1 |
| `[Follow-up] v0.5.x: Define evidence integrity negative tests` | #165 | T2 |
| `[Follow-up] v0.5.x: Refine delegation semantics after first incorporation cycle` | #163, #161 | T3 |
| `[Follow-up] v0.5.x: Refine approval semantics after first incorporation cycle` | #167 | T4 |
| `[Follow-up] v0.5.x: Consolidate temporary status documents and prepare publication readiness` | #161, #163, #165, #167 | T5 |

These issue titles are planning candidates only.

They do not create issues by themselves.

## Recommended Execution Order

Recommended order:

1. T1 — Evidence schema and examples
2. T2 — Evidence integrity negative tests
3. T3 — Delegation semantics
4. T4 — Approval semantics
5. T5 — Cleanup and publication readiness

Rationale:

- Evidence schema and examples may influence several later testing and evidence decisions.
- Evidence integrity negative tests are concrete and can be developed without changing the baseline immediately.
- Delegation and approval semantics are larger and may benefit from schema/example decisions first.
- Cleanup should happen after the next wave of track-specific planning stabilizes.

## Decision Boundaries

The following decisions should be made explicitly in later PRs:

- whether to update active testing procedure CSV;
- whether to update evidence schema;
- whether to add examples;
- whether to refine assessment profiles;
- whether to add new control IDs;
- whether to close, split, or keep open #161, #163, #165, or #167.

## Non-Goals

This plan does not:

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
- create GitHub issues;
- close #161, #163, #165, or #167.

It records the intended next-phase work split after the first v0.5.x incorporation review cycle.

## T1 Track Proposal

Track T1 is started in `docs/en/status/v050x-evidence-schema-and-examples-track-proposal.md`.

The proposal evaluates whether schema fields or examples are needed for:

- evidence integrity and tamper-evident evidence;
- trusted approval evidence source handling;
- model-generated approval summary limitations;
- principal context freshness and degradation evidence;
- delegation and authority lineage evidence.
