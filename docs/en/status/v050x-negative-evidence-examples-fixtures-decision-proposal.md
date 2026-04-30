# v0.5.x Negative Evidence Examples and Validator Fixtures Decision Proposal

**Status:** Temporary, non-normative decision proposal

## Purpose

This document evaluates whether AAEF should add negative evidence examples or validator fixtures for evidence integrity failure scenarios in the current v0.5.x follow-up cycle.

It follows:

- `docs/en/status/v050x-evidence-integrity-negative-tests-track-proposal.md`
- `docs/en/status/v050x-evidence-integrity-negative-tests-candidate-appendix.md`
- `docs/en/status/v050x-evidence-integrity-negative-tests-csv-refinement-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md`
- `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md`
- `docs/en/status/v050x-follow-up-status.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Primary source issue:

- #165 — evidence integrity and tamper-evident evidence

Related active row:

- `AAEF-EVD-04`

This proposal does not add negative examples.

It does not add validator fixtures.

It does not update the Evidence Event Schema.

It does not update active testing procedures.

It does not close #165 by itself.

## Decision Context

Recent v0.5.x work has already added:

- optional evidence integrity schema fields;
- an integrity-focused positive example;
- evidence integrity negative test candidates;
- incident-response evidence preservation guidance;
- incident-response evidence preservation scenario appendix;
- evidence depth / E5 decision proposal.

The remaining question is whether negative evidence conditions should now be represented as:

1. intentionally schema-invalid validator fixtures;
2. schema-valid negative examples showing failed, partial, missing, or unavailable evidence states;
3. documentation-only negative scenarios;
4. later reviewer-facing guidance.

## Key Distinction

Evidence integrity failure is usually not the same as JSON Schema invalidity.

A schema-valid evidence event can still describe weak, failed, partial, unavailable, incomplete, or untrusted evidence.

Examples:

| Scenario | Schema-invalid? | Better representation |
| --- | --- | --- |
| Verification result is fail | Usually no | Schema-valid negative evidence example |
| Proof reference is unavailable | Usually no | Schema-valid negative evidence example or trust limitation |
| Evidence was selectively omitted | Usually no | Documentation, review guidance, or scenario example |
| Action evidence is replayed for another action | Usually no | Review guidance or semantic test scenario |
| Required JSON field is missing | Yes | Validator invalid fixture |
| Field has wrong data type | Yes | Validator invalid fixture |

Because most evidence integrity failures are semantic or assurance failures rather than structural JSON failures, validator fixtures should be used carefully.

## Proposed Decision

Do not add new validator fixtures for evidence integrity negative scenarios in the current v0.5.x cycle.

Do not add negative evidence examples immediately in the same decision step.

Instead:

- retain current schema validation behavior;
- keep `tools/validate_evidence_schema.py` focused on structural schema validation;
- treat semantic evidence failures as reviewer-facing examples or guidance candidates;
- consider future schema-valid negative examples only if they improve human reviewability;
- avoid implying that JSON Schema validation can prove evidence integrity.

Recommended decision:

| Area | Recommendation |
| --- | --- |
| Add schema-invalid fixtures now | No |
| Add schema-valid negative examples now | Defer |
| Update validator behavior now | No |
| Update Evidence Event Schema now | No |
| Update active CSV now | No |
| Create reviewer-facing negative examples later | Candidate future work |
| Treat semantic evidence failures as schema failures | No |

## Why Not Add Validator Fixtures Now

Validator fixtures are useful when testing structural schema rules.

They are less useful for evidence integrity failure semantics.

Adding validator fixtures for semantic failures could create confusion:

- a tampered evidence package may still be schema-valid JSON;
- a failed verification result may be valid evidence of a failed verification;
- a partial evidence package may be valid to record, even if insufficient for assurance;
- a model self-report may be valid to retain as context, even if not trusted evidence;
- JSON Schema cannot determine whether an external proof reference is true, complete, fresh, or action-bound.

The validator should not imply that a schema-valid event is sufficient evidence.

## Negative Example Types

Future negative examples could be useful if clearly framed.

Candidate types:

| Type | Description | Recommended status |
| --- | --- | --- |
| Failed verification example | Schema-valid event with failed integrity verification | Candidate future example |
| Partial verification example | Schema-valid event with partial or unavailable verification | Candidate future example |
| Missing evidence limitation example | Schema-valid event recording missing evidence and trust limitation | Candidate future example |
| Model-summary-only example | Example showing weak evidence source and limitation | Candidate future guidance |
| Replay scenario example | Documentation scenario showing action-binding mismatch | Candidate future guidance |
| Selective omission scenario | Documentation scenario showing incomplete evidence package | Candidate future guidance |
| Schema-invalid fixture | Invalid JSON used to test schema structure | Not needed now |

## Recommended Future Negative Example Pattern

If negative examples are added later, they should be schema-valid examples that demonstrate reduced assurance, not invalid examples that fail schema validation.

A future negative example could show:

- `verification_result` as failed, partial, unavailable, or not checked;
- missing proof reference;
- explicit evidence trust limitation;
- model-generated summary retained only as untrusted context;
- evidence package that cannot be treated as complete tamper-evident evidence.

This would help reviewers understand that:

- recording a failure is valid;
- treating that failure as full assurance is not valid;
- model output is not authority;
- schema validity is not evidence sufficiency.

## Recommended Future Validator Boundary

The validator should continue to answer:

> Is this evidence event structurally valid according to the schema?

The validator should not answer:

> Is this evidence sufficient?
> Is this evidence tamper-evident?
> Is this evidence complete?
> Is this evidence independently corroborated?
> Is this action authorized?
> Is this action safe?

Those questions belong to assessment, review, policy, evidence integrity verification, and audit procedures.

## Relationship to Existing Invalid Example

The existing invalid example should continue to serve structural validation purposes.

Do not overload it with semantic evidence-integrity failure cases.

Structural invalid examples should remain focused on schema expectations such as missing required fields, wrong types, or invalid enum-like values where applicable.

## Relationship to AAEF-EVD-04

`AAEF-EVD-04` already covers evidence integrity and tamper-evident evidence.

Negative examples may later help illustrate how evidence integrity failures are reviewed, but they do not need to be required by the active testing procedure row.

No active CSV change is recommended in this proposal.

## Relationship to E5 / Evidence Depth

The evidence depth decision proposal keeps E5 non-normative.

Negative examples should not introduce an implicit E5 certification test.

If future examples use evidence depth vocabulary, they should clearly state that the vocabulary is explanatory and not a required schema value or certification scale.

## Relationship to #165

This proposal advances #165 by deciding not to add negative examples or validator fixtures immediately.

It does not close #165.

Remaining #165 work may include:

- possible future reviewer-facing negative examples;
- possible `AAEF-EVD-01` evidence sufficiency / limitation review;
- possible evidence depth guidance consolidation;
- temporary-document consolidation after the current follow-up cycle.

## Recommended Next Step

The recommended next step is a status update recording this decision.

After that, the next substantive #165 decision should be whether to review `AAEF-EVD-01` for evidence sufficiency and limitation language.

## Non-Goals

This proposal does not:

- add negative examples;
- add validator fixtures;
- update `tools/validate_evidence_schema.py`;
- update active testing procedure CSV;
- add testing procedure rows;
- add candidate IDs to active CSV;
- update the Evidence Event Schema;
- change control catalog CSV;
- change human-readable control requirements;
- change assessment worksheet;
- change assessment profiles;
- change external framework mapping CSV;
- create GitHub issues;
- create a certification scale;
- close #161, #163, #165, or #167.

It records the negative evidence examples and validator fixtures decision proposal before any active incorporation decision.

## Status after Initial Decision

This proposal records the current v0.5.x decision for negative evidence examples and validator fixtures.

Current incorporation status:

- schema-invalid validator fixtures are not added in this cycle;
- schema-valid negative evidence examples are deferred;
- validator behavior remains unchanged;
- the Evidence Event Schema remains unchanged;
- active testing procedures remain unchanged;
- reviewer-facing negative examples remain candidate future work.

The remaining question is whether evidence sufficiency and evidence limitation language should later be reviewed under `AAEF-EVD-01`.
