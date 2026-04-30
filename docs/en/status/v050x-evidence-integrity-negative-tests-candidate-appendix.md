# v0.5.x Evidence Integrity Negative Tests Candidate Appendix

**Status:** Temporary, non-normative candidate appendix

## Purpose

This appendix expands the v0.5.x evidence integrity negative tests track proposal into structured test candidates.

It follows:

- `docs/en/status/v050x-evidence-integrity-negative-tests-track-proposal.md`
- `docs/en/status/v050x-next-phase-track-plan.md`
- `docs/en/status/v050x-evidence-schema-example-implementation-readiness.md`
- `docs/en/status/v050x-evidence-schema-field-proposal.md`
- `docs/en/status/v050x-evidence-example-design-proposal.md`

Primary source issue:

- #165 — evidence integrity and tamper-evident evidence

Primary active row:

- `AAEF-EVD-04`

This appendix does not update active testing procedures.

It does not add executable tests.

It does not update the Evidence Event Schema.

It does not add or modify evidence examples.

It does not close #165 by itself.

## Candidate Summary

| Candidate ID | Category | Primary target | Candidate incorporation path |
| --- | --- | --- | --- |
| EINT-NEG-01 | Evidence tampering | Modified protected evidence | Candidate for `AAEF-EVD-04` refinement |
| EINT-NEG-02 | Evidence deletion | Missing required evidence | Candidate for `AAEF-EVD-04` refinement |
| EINT-NEG-03 | Evidence replay | Reused evidence for different action | Candidate for `AAEF-EVD-04` refinement |
| EINT-NEG-04 | Evidence reordering | Sequence-sensitive evidence order | Candidate for `AAEF-EVD-04` refinement |
| EINT-NEG-05 | Evidence truncation | Incomplete evidence chains | Candidate for `AAEF-EVD-04` refinement |
| EINT-NEG-06 | Selective omission | Omitted unfavorable or required records | Candidate for `AAEF-EVD-04` refinement |
| EINT-NEG-07 | Verification failure handling | Failed or unavailable integrity verification | Candidate for `AAEF-EVD-04` refinement |
| EINT-NEG-08 | Evidence trust limitation bypass | Weak or self-reported evidence overtrusted | Candidate for `AAEF-EVD-01` and `AAEF-EVD-04` review |

## Candidate Evaluation Criteria

Each candidate should be evaluated against the following questions before active incorporation:

- Does the test reveal a concrete gap in `AAEF-EVD-04`?
- Can the test be expressed within the existing one-control-one-row testing model?
- Is the test better represented as active testing language, example guidance, validator fixture, or incident-response guidance?
- Does the test require schema changes, or can current optional fields express the needed evidence state?
- Does the test avoid implying one required tamper-evidence mechanism?
- Does the test avoid treating model or agent self-report as independent evidence?

## EINT-NEG-01 — Evidence Tampering Detection

### Purpose

Confirm that modified evidence records or modified referenced evidence packages do not pass integrity review silently.

### Candidate setup

Use a high-impact or audit-grade action with evidence integrity metadata.

The evidence package should include one or more of:

- evidence hash;
- proof reference;
- external anchor reference;
- verification reference;
- append-only or write-restricted evidence storage;
- corroborating enforcement or backend logs.

### Mutation

Modify at least one protected item, such as:

- action identifier;
- authorization decision reference;
- approval record reference;
- execution result;
- evidence hash;
- proof target;
- evidence package content;
- timestamp or ordering metadata.

### Expected observation

The implementation or assessment process should identify that the evidence no longer verifies cleanly.

Acceptable outcomes include:

- integrity verification fails;
- verification becomes partial;
- trust limitation is recorded;
- reviewer is unable to treat evidence as complete audit-grade evidence.

### Candidate pass expectation

Tampered evidence is not treated as fully valid evidence.

### Candidate fail expectation

Tampered evidence is accepted as valid, complete, or audit-grade evidence without detection or limitation.

### Candidate incorporation note

Strong candidate for later `AAEF-EVD-04` wording refinement if current active row does not clearly require tampering tests.

## EINT-NEG-02 — Evidence Deletion Detection

### Purpose

Confirm that deletion of required evidence is detectable, disclosed, or reflected in assessment confidence.

### Candidate setup

Use an action where review requires multiple evidence records, such as:

- authorization decision;
- approval record;
- dispatch record;
- execution record;
- evidence integrity proof;
- verification record.

### Mutation

Remove one or more required records.

Candidate deletions include:

- authorization decision artifact;
- approval workflow record;
- execution log;
- proof reference;
- verification record;
- denial or non-execution record;
- override record.

### Expected observation

Review or reconstruction should identify the evidence gap.

Acceptable outcomes include:

- missing evidence is detected;
- reconstruction is marked incomplete;
- evidence limitation is recorded;
- assessment confidence is reduced;
- action cannot be treated as fully supported by evidence.

### Candidate pass expectation

Deleted evidence does not silently produce a complete evidence story.

### Candidate fail expectation

Deleted evidence is not noticed and the remaining evidence is treated as complete.

### Candidate incorporation note

Strong candidate for `AAEF-EVD-04`, with possible relationship to retention and incident preservation guidance.

## EINT-NEG-03 — Evidence Replay Detection

### Purpose

Confirm that evidence from one action cannot be reused to support a different action.

### Candidate setup

Use two distinct actions with different identifiers, scopes, or action digests.

Candidate binding fields include:

- `action_id`;
- action digest;
- authorization decision artifact;
- approval workflow record;
- proof reference;
- evidence hash;
- external anchor reference.

### Mutation

Reuse evidence from action A to support action B.

Candidate replay examples include:

- reusing an approval record for a different action;
- reusing a proof reference for a different evidence package;
- reusing an authorization decision artifact outside its original action scope;
- reusing evidence hash or evidence package content with a different action ID.

### Expected observation

Replay should be detected through binding mismatch, scope mismatch, expired evidence, or trust limitation.

### Candidate pass expectation

Replayed evidence cannot satisfy evidence requirements for a different action without detection.

### Candidate fail expectation

Evidence from one action is accepted for a different action as if it were action-bound evidence.

### Candidate incorporation note

Strong candidate for `AAEF-EVD-04`, with possible overlap with approval binding and authorization artifact binding.

## EINT-NEG-04 — Evidence Reordering Detection

### Purpose

Confirm that sequence-sensitive evidence cannot be reordered without detection or limitation.

### Candidate setup

Use a workflow where event order matters.

Sequence-sensitive records may include:

- authorization before dispatch;
- approval before execution;
- revocation check before execution;
- verification after evidence generation;
- non-execution before final result;
- override after denial.

### Mutation

Reorder evidence records or timestamps to create a misleading sequence.

Candidate reorderings include:

- execution before approval;
- dispatch before authorization;
- verification before evidence generation;
- override before denial;
- reauthorization after execution but represented as before execution.

### Expected observation

The system or reviewer should detect chronology, sequence, chain, or timestamp inconsistency.

### Candidate pass expectation

Misordered evidence cannot support a valid reconstruction where order matters.

### Candidate fail expectation

Reordered evidence creates a false but accepted action story.

### Candidate incorporation note

Candidate for `AAEF-EVD-04`; may need careful wording so it does not require a specific log-chain technology.

## EINT-NEG-05 — Evidence Truncation Detection

### Purpose

Confirm that shortened evidence chains or incomplete evidence packages are identified.

### Candidate setup

Use an evidence package with multiple related records.

Candidate chain elements include:

- prior hash reference;
- external anchor;
- execution logs;
- verification logs;
- approval or authorization references;
- retention or preservation records.

### Mutation

Remove tail, intermediate, or verification records.

Candidate truncations include:

- removing later failure records;
- removing verification failure;
- removing final execution result;
- removing post-action revocation evidence;
- removing intermediate hash-chain entries.

### Expected observation

The evidence package should be identified as incomplete, partial, or unverifiable.

### Candidate pass expectation

Truncated evidence is not treated as complete.

### Candidate fail expectation

A shortened evidence package still appears complete and valid.

### Candidate incorporation note

Candidate for `AAEF-EVD-04`; may overlap with deletion but focuses on chain or package completeness.

## EINT-NEG-06 — Selective Omission Detection

### Purpose

Confirm that evidence packages cannot omit unfavorable or required records while still appearing complete.

### Candidate setup

Use a workflow with both favorable and unfavorable records.

Potentially omitted records include:

- denied authorization decisions;
- failed approval checks;
- non-execution records;
- override records;
- failed verification records;
- revocation or freeze records;
- partial execution results.

### Mutation

Construct an evidence package that includes only favorable records.

### Expected observation

The review process should identify missing corroborating records, incomplete scope, or selective omission risk.

Acceptable outcomes include:

- independent corroborating logs reveal omitted records;
- completeness checks fail;
- evidence trust limitation records selective scope;
- assessment result is reduced or blocked.

### Candidate pass expectation

Cherry-picked evidence cannot create false assurance.

### Candidate fail expectation

Selective omission produces an accepted complete evidence story.

### Candidate incorporation note

Strong candidate for `AAEF-EVD-04`; may also connect to `AAEF-EVD-01` evidence sufficiency.

## EINT-NEG-07 — Verification Failure Handling

### Purpose

Confirm that failed or unavailable integrity verification is surfaced and not treated as pass.

### Candidate setup

Use evidence integrity metadata with a verification result.

Candidate verification states include:

- `fail`;
- `partial`;
- `unavailable`;
- `not_checked`;
- verification error;
- missing verification reference.

### Mutation

Set or produce a non-passing verification state.

### Expected observation

Reviewer-facing evidence should clearly show the verification result and limitation.

### Candidate pass expectation

Failed, partial, unavailable, or unchecked verification is not treated as full integrity assurance.

### Candidate fail expectation

Verification failure is ignored, hidden, or treated as equivalent to pass.

### Candidate incorporation note

Strong candidate for `AAEF-EVD-04`; likely expressible using existing optional schema fields.

## EINT-NEG-08 — Evidence Trust Limitation Bypass

### Purpose

Confirm that weak, self-reported, partial, or unverifiable evidence is not treated as equivalent to independently protected evidence.

### Candidate setup

Use evidence sources with different trust strength.

Candidate weak sources include:

- model-generated summaries;
- agent runtime self-report;
- implementation self-report;
- partial logs;
- unverifiable screenshots;
- logs without independent generation or corroboration.

### Mutation

Attempt to present weak evidence as if it were independent, complete, or tamper-evident.

### Expected observation

The system or reviewer should record evidence limitations or reduce confidence.

### Candidate pass expectation

Weak evidence is not overtrusted.

### Candidate fail expectation

Self-reported or unverifiable evidence is treated as equivalent to independently generated or tamper-evident evidence.

### Candidate incorporation note

Candidate for both `AAEF-EVD-01` and `AAEF-EVD-04` review.

## Incorporation Assessment

| Candidate ID | Active CSV readiness | Suggested next action |
| --- | --- | --- |
| EINT-NEG-01 | High | Consider for `AAEF-EVD-04` refinement proposal |
| EINT-NEG-02 | High | Consider for `AAEF-EVD-04` refinement proposal |
| EINT-NEG-03 | High | Consider for `AAEF-EVD-04` refinement proposal |
| EINT-NEG-04 | Medium | Clarify sequence and chronology expectations first |
| EINT-NEG-05 | Medium | Combine with deletion/truncation wording carefully |
| EINT-NEG-06 | High | Consider for `AAEF-EVD-04` or `AAEF-EVD-01` refinement proposal |
| EINT-NEG-07 | High | Consider for `AAEF-EVD-04` refinement proposal |
| EINT-NEG-08 | Medium | Consider as evidence sufficiency / limitation guidance |

## Recommended Minimal Active Refinement Candidate

If this appendix is later incorporated into active testing procedures, the minimal active refinement should focus on `AAEF-EVD-04`.

Recommended focus:

- tampering;
- deletion;
- replay;
- truncation;
- selective omission;
- failed or unavailable verification;
- evidence trust limitations.

Avoid adding temporary candidate IDs to active CSV.

Avoid creating new control IDs unless `AAEF-EVD-04` is proven insufficient.

## Recommended Next Step

The recommended next PR is a CSV refinement proposal, not immediate active CSV modification.

Suggested planned filename:

- `v050x-evidence-integrity-negative-tests-csv-refinement-proposal.md`

That proposal should decide whether `AAEF-EVD-04` already covers these negative tests or whether wording refinement is needed.

## Non-Goals

This appendix does not:

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

It records candidate negative tests before any active incorporation decision.

## CSV Refinement Proposal

The CSV refinement proposal is recorded in `docs/en/status/v050x-evidence-integrity-negative-tests-csv-refinement-proposal.md`.

The proposal recommends refining the existing `AAEF-EVD-04` active testing procedure row instead of adding new rows, new candidate IDs, new controls, schema fields, or examples.
