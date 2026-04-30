# v0.5.x Evidence Integrity Negative Tests Track Proposal

**Status:** Temporary, non-normative track proposal

## Purpose

This document starts Track T2 from the v0.5.x next phase plan.

Track T2 covers negative tests for evidence integrity and tamper-evident evidence.

It follows:

- `docs/en/status/v050x-next-phase-track-plan.md`
- `docs/en/status/v050x-evidence-schema-example-implementation-readiness.md`
- `docs/en/status/v050x-evidence-schema-field-proposal.md`
- `docs/en/status/v050x-evidence-example-design-proposal.md`
- `docs/en/status/v050x-incorporation-decision-register.md`
- `docs/en/status/v050x-follow-up-status.md`

Primary source issue:

- #165 — evidence integrity and tamper-evident evidence

Related active control area:

- `AAEF-EVD-04` — Evidence Integrity / Tamper-Evident Evidence

Related evidence rows:

- `AAEF-EVD-01`
- `AAEF-EVD-02`
- `AAEF-EVD-05`
- `AAEF-EVD-06`

This document does not update active testing procedures.

It does not add executable tests.

It does not update the Evidence Event Schema.

It does not add or modify evidence examples.

It does not close #165 by itself.

## Track Objective

The objective of this track is to define negative tests that demonstrate whether evidence integrity controls can detect or resist:

- evidence tampering;
- evidence deletion;
- evidence replay;
- evidence reordering;
- evidence truncation;
- selective omission;
- verification failure;
- incomplete or misleading evidence trust claims.

The goal is to convert the evidence integrity concept from positive evidence examples into adversarial validation expectations.

## Current Baseline

The current active baseline already includes:

- optional schema support for evidence integrity and evidence trust limitations;
- an integrity-focused positive example;
- `AAEF-EVD-04` active testing language covering tamper-evident evidence and integrity concerns.

Relevant recent PRs:

| PR | Result |
| --- | --- |
| #209 | Added optional evidence integrity and approval evidence schema fields. |
| #210 | Added `examples/agentic-action-evidence-event.integrity-e5.json`. |
| #211 | Added `examples/agentic-action-evidence-event.approval-binding.json`. |
| #212 | Updated v0.5.x status after the first schema/example implementation wave. |

## Negative Test Categories

| Category | Purpose | Primary row |
| --- | --- | --- |
| Tampering | Verify altered evidence is detected or identified as untrusted. | AAEF-EVD-04 |
| Deletion | Verify missing required evidence is detected or disclosed. | AAEF-EVD-04 |
| Replay | Verify stale or reused evidence cannot satisfy a new action. | AAEF-EVD-04 |
| Reordering | Verify sequence-sensitive evidence cannot be reordered silently. | AAEF-EVD-04 |
| Truncation | Verify shortened evidence chains or incomplete logs are detected. | AAEF-EVD-04 |
| Selective omission | Verify cherry-picked evidence does not create false assurance. | AAEF-EVD-04 |
| Verification failure | Verify failed integrity checks are visible and not treated as pass. | AAEF-EVD-04 |
| Trust limitation bypass | Verify weak, self-reported, or partial evidence is not overtrusted. | AAEF-EVD-01, AAEF-EVD-04 |

## Candidate Negative Tests

### EINT-NEG-01 — Evidence tampering detection

Purpose:

- Confirm that modified evidence records or modified referenced evidence packages do not pass integrity review silently.

Expected test idea:

- Start with an integrity-protected evidence package.
- Modify a protected field, referenced artifact, or proof target.
- Verify that integrity verification fails, becomes partial, or records a trust limitation.

Expected result:

- The system should not treat tampered evidence as fully valid audit-grade evidence.

### EINT-NEG-02 — Evidence deletion detection

Purpose:

- Confirm that deletion of required evidence is detectable or explicitly visible.

Expected test idea:

- Remove an evidence record, proof reference, approval record, dispatch record, or execution record.
- Verify that reconstruction or review identifies the missing evidence.

Expected result:

- Missing evidence should not be silently treated as complete evidence.

### EINT-NEG-03 — Evidence replay detection

Purpose:

- Confirm that evidence from one action cannot be reused to support a different action.

Expected test idea:

- Reuse an evidence hash, proof reference, approval record, or authorization artifact from a prior action.
- Attempt to bind it to a different action ID or action digest.

Expected result:

- Replayed evidence should fail binding checks or be treated as untrusted.

### EINT-NEG-04 — Evidence reordering detection

Purpose:

- Confirm that sequence-sensitive evidence cannot be reordered without detection.

Expected test idea:

- Reorder authorization, approval, dispatch, execution, verification, or log-chain records.
- Verify that chronology, chain, sequence, or timestamp inconsistencies are detected.

Expected result:

- Reordered evidence should not support a valid reconstruction if order matters.

### EINT-NEG-05 — Evidence truncation detection

Purpose:

- Confirm that shortened evidence chains or incomplete evidence packages are identified.

Expected test idea:

- Remove tail records, intermediate records, or verification records from an evidence chain.
- Verify that the chain or reconstruction is incomplete.

Expected result:

- Truncated evidence should be visible as partial, incomplete, or unverifiable.

### EINT-NEG-06 — Selective omission detection

Purpose:

- Confirm that evidence packages cannot omit unfavorable or required records while still appearing complete.

Expected test idea:

- Omit denial records, reauthorization records, override records, non-execution records, or failed verification records.
- Verify that completeness checks, corroborating logs, or trust limitations expose the omission.

Expected result:

- Selective omission should not create false audit assurance.

### EINT-NEG-07 — Verification failure handling

Purpose:

- Confirm that failed integrity verification is surfaced and not treated as pass.

Expected test idea:

- Set or produce `verification_result` as `fail`, `partial`, `unavailable`, or equivalent.
- Verify that the review result does not treat the evidence as fully trusted.

Expected result:

- Failure, partial verification, or unavailable verification should be visible to reviewers.

### EINT-NEG-08 — Evidence trust limitation bypass

Purpose:

- Confirm that self-reported, partial, or unverifiable evidence cannot be treated as equivalent to independently protected evidence.

Expected test idea:

- Provide only model-generated, agent-reported, or implementation self-reported evidence.
- Verify that evidence limitations are recorded or assessment confidence is reduced.

Expected result:

- Weak or self-reported evidence should not be treated as fully independent or tamper-evident.

## Candidate Output Types

This track may later produce:

1. a negative test candidate appendix;
2. example negative evidence events;
3. active testing procedure refinement for `AAEF-EVD-04`;
4. incident-response evidence preservation guidance;
5. evidence integrity review guidance;
6. validator fixtures, only if schema-level invalid examples are needed.

## Recommended Next Step

The recommended next step is a candidate appendix, not immediate active CSV modification.

Recommended file:

- planned filename: `v050x-evidence-integrity-negative-tests-candidate-appendix.md`

The appendix should define test candidates in a structured table before deciding whether any candidates should be incorporated into active testing procedure language.

## Active CSV Incorporation Boundary

Do not add temporary negative test IDs directly to the active testing procedure CSV.

The active testing procedure CSV remains one row per control.

If active incorporation is needed later, it should refine `AAEF-EVD-04` language rather than add temporary candidate rows.

## Evidence Schema Boundary

This track should not add new schema fields unless negative tests reveal a concrete field gap.

Current optional fields may already support many negative test descriptions:

- `evidence.evidence_integrity.protected`
- `evidence.evidence_integrity.mechanism`
- `evidence.evidence_integrity.verification_result`
- `evidence.evidence_integrity.verification_ref`
- `evidence.evidence_integrity.proof_ref`
- `evidence.evidence_integrity.external_anchor_ref`
- `evidence.evidence_trust_limitation`

## Example Boundary

Positive examples already exist for:

- integrity-focused evidence;
- approval-to-execution binding evidence.

Negative examples should be added only if they are useful for reviewer understanding or schema validation.

Do not mix negative test planning with broad example expansion in the same PR.

## Open Questions

Before implementing negative tests, reviewers should answer:

- Should negative tests be represented as documentation-only test procedures, JSON examples, validator fixtures, or assessment guidance?
- Should evidence tampering negative tests use intentionally invalid schema examples or schema-valid evidence events with failed verification results?
- Should replay tests be tied to `action_id`, `action_digest`, `authorization_decision_artifact`, or evidence proof references?
- Should selective omission tests require independent corroborating logs?
- Should failed verification be an assessment failure, an evidence limitation, or a conditional result depending on action risk?
- Should incident-response preservation be a separate guidance document or part of negative testing?

## Relationship to #165

This proposal advances #165 by moving from positive evidence integrity examples into adversarial evidence integrity testing.

It does not close #165.

Remaining #165 work includes:

- candidate appendix;
- possible active `AAEF-EVD-04` refinement;
- replay, reordering, truncation, deletion, and selective omission test design;
- incident-response evidence preservation guidance;
- evidence depth/profile decisions.

## Non-Goals

This proposal does not:

- update active testing procedure CSV;
- add testing procedure rows;
- add candidate IDs to active CSV;
- update the Evidence Event Schema;
- add evidence examples;
- add validator fixtures;
- change control catalog CSV;
- change human-readable control requirements;
- change assessment worksheet;
- change assessment profiles;
- change external framework mapping CSV;
- create GitHub issues;
- close #161, #163, #165, or #167.

It records the starting proposal for the v0.5.x evidence integrity negative tests track.
