# v0.5.x Evidence Integrity Negative Tests CSV Refinement Proposal

**Status:** Temporary, non-normative CSV refinement proposal

## Purpose

This document evaluates whether evidence integrity negative test candidates should be incorporated into the active testing procedure CSV.

It follows:

- `docs/en/status/v050x-evidence-integrity-negative-tests-track-proposal.md`
- `docs/en/status/v050x-evidence-integrity-negative-tests-candidate-appendix.md`
- `docs/en/status/v050x-next-phase-track-plan.md`
- `docs/en/status/v050x-incorporation-decision-register.md`
- `docs/en/status/v050x-follow-up-status.md`

Primary source issue:

- #165 — evidence integrity and tamper-evident evidence

Primary active row:

- `AAEF-EVD-04`

This proposal does not update the active testing procedure CSV.

It does not add testing procedure rows.

It does not add candidate IDs to active CSV.

It does not update the Evidence Event Schema.

It does not add or modify evidence examples.

It does not close #165 by itself.

## Decision Summary

The candidate appendix identifies eight negative test candidates.

This proposal recommends a narrow active CSV refinement focused on `AAEF-EVD-04`.

Recommended incorporation decision:

| Decision | Recommendation |
| --- | --- |
| Add new testing rows | No |
| Add temporary candidate IDs to active CSV | No |
| Add new controls | No |
| Refine `AAEF-EVD-04` testing language | Yes |
| Refine `AAEF-EVD-01` in the same PR | No |
| Update schema or examples in the same PR | No |

The active testing procedure model should remain one row per control.

## Candidate Incorporation Assessment

| Candidate ID | Category | Recommended incorporation |
| --- | --- | --- |
| EINT-NEG-01 | Evidence tampering | Include in `AAEF-EVD-04` refinement |
| EINT-NEG-02 | Evidence deletion | Include in `AAEF-EVD-04` refinement |
| EINT-NEG-03 | Evidence replay | Include in `AAEF-EVD-04` refinement |
| EINT-NEG-04 | Evidence reordering | Include indirectly through sequencing and reconstruction wording |
| EINT-NEG-05 | Evidence truncation | Include in `AAEF-EVD-04` refinement |
| EINT-NEG-06 | Selective omission | Include in `AAEF-EVD-04` refinement |
| EINT-NEG-07 | Verification failure handling | Include in `AAEF-EVD-04` refinement |
| EINT-NEG-08 | Evidence trust limitation bypass | Defer detailed treatment; reference through limitation / unverifiable evidence wording |

## Proposed Active Refinement Scope

The active `AAEF-EVD-04` row should be refined to require testing that evidence integrity protections can identify or prevent false assurance from:

- tampering;
- deletion;
- replay;
- truncation;
- selective omission;
- failed or unavailable verification;
- unverifiable or limitation-bearing evidence.

The refinement should avoid:

- requiring a specific cryptographic mechanism;
- requiring Merkle trees or hash chains for all implementations;
- requiring all evidence to be high-assurance evidence;
- implying that all evidence integrity concerns must be solved through schema fields;
- adding temporary candidate IDs to the active CSV.

## Proposed Testing Procedure Direction

A later active CSV PR should refine the `testing_procedure` or equivalent testing criteria for `AAEF-EVD-04` along these lines:

> Verify that evidence integrity protections and review procedures detect or disclose tampering, deletion, replay, truncation, selective omission, and failed or unavailable verification for action-bound evidence. Confirm that evidence with integrity failures, missing records, unverifiable proof references, or explicit trust limitations is not treated as complete tamper-evident evidence.

This wording is a proposal only.

It is not active testing procedure language until incorporated into the CSV.

## Proposed Pass Criteria Direction

If the active testing procedure CSV has pass criteria or assessment notes for `AAEF-EVD-04`, a later PR should align them with the following direction:

A pass result should require evidence that:

- action-bound evidence integrity mechanisms or review procedures are implemented;
- tampered or modified evidence is not accepted silently;
- deleted, truncated, or missing evidence is detected or disclosed;
- replayed evidence cannot satisfy a different action without detection;
- selective omission does not create false completeness;
- failed, partial, unavailable, or unchecked verification is visible to reviewers;
- evidence trust limitations reduce assurance where appropriate.

This wording is a proposal only.

## Proposed Fail Criteria Direction

A fail result should be considered where:

- tampered evidence is accepted as valid without limitation;
- required evidence can be deleted or omitted without detection;
- evidence from one action can be replayed for another action;
- incomplete evidence chains are treated as complete;
- failed or unavailable verification is hidden or treated as pass;
- weak or self-reported evidence is treated as tamper-evident without limitation.

This wording is a proposal only.

## Why `AAEF-EVD-04` Is the Right First Target

`AAEF-EVD-04` is the best first active CSV target because:

- it already represents evidence integrity and tamper-evident evidence;
- the negative tests mostly concern integrity failure modes;
- it avoids spreading related wording across too many EVD rows too early;
- it preserves the active one-control-one-row model;
- it keeps #165 focused on evidence integrity instead of reopening the full evidence model.

## Why `AAEF-EVD-01` Is Deferred

`AAEF-EVD-01` may later need evidence sufficiency or evidence limitation refinement.

However, it should not be changed in the first active CSV refinement for this track because:

- #165 is centered on integrity and tamper-evidence;
- `AAEF-EVD-04` is the more direct control row;
- broadening to sufficiency too early risks scope creep;
- `EINT-NEG-08` can be revisited after the initial `AAEF-EVD-04` refinement.

## Why Schema and Examples Are Not Changed Here

Recent PRs already added optional schema and examples:

- #209 added optional evidence integrity and approval evidence schema fields.
- #210 added the integrity-focused evidence example.
- #211 added the approval-to-execution binding evidence example.

This proposal does not identify a concrete new schema or example gap.

The next active step should be testing procedure refinement, not another schema or example expansion.

## Recommended Next PR

The next PR should update only:

- `assessment/aaef-testing-procedures-v0.4-draft.csv`
- `CHANGELOG.md`

Expected scope:

- refine the existing `AAEF-EVD-04` testing procedure row;
- incorporate the negative test concepts without adding candidate IDs;
- do not change schema, examples, controls, profiles, worksheet, or mappings.

Suggested branch name:

- `feature/refine-evidence-integrity-testing-procedures`

Suggested commit message:

- `Refine evidence integrity testing procedures`

## Validation Expectations for Next PR

The active CSV refinement PR should run:

- `python tools/validate_testing_procedures.py`
- `python tools/validate_control_catalog.py`
- `python tools/validate_evidence_schema.py`
- `python tools/validate_assessment_profiles.py`
- `python tools/validate_assessment_worksheet.py`
- `python tools/validate_external_mappings.py`
- `git diff --check`

## Relationship to #165

This proposal advances #165 by selecting the active CSV incorporation path for evidence integrity negative tests.

It does not close #165.

Remaining #165 work after this proposal may include:

- active `AAEF-EVD-04` refinement;
- status update after active refinement;
- decision on whether evidence integrity negative examples or validator fixtures are useful;
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

It records the incorporation decision before any active CSV modification.

## Active Row Review Outcome

After this proposal, the active `AAEF-EVD-04` row was reviewed against the proposed evidence integrity negative testing concepts.

Outcome:

- no immediate active CSV refinement is required;
- the existing row already covers the core negative test concepts;
- no testing procedure rows were added;
- no candidate IDs were added to the active CSV;
- no schema, examples, controls, profiles, worksheet, or mapping changes were needed.

This changes the next step from active CSV modification to status tracking and remaining-work planning for #165.
