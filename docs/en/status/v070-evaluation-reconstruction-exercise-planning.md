# v0.7.0 Evaluation Reconstruction Exercise Planning

## Status

This is a v0.7.0 planning artifact for evaluation reconstruction exercises.

This document is:

- a planning artifact for #319;
- a follow-up to the v0.7.0 Evaluation Readiness, Scenario Walkthrough, Scenario Candidate, and Artifact Inventory artifacts;
- a reconstruction exercise design aid for reviewer-facing evaluation planning;
- non-normative unless a later release explicitly promotes content into active guidance.

This document is not:

- an empirical evaluation result;
- an implementation test result;
- a production-readiness claim;
- an implementation conformance claim;
- a certification scheme;
- a compliance claim;
- a conformity claim;
- an audit sufficiency claim;
- a legal sufficiency claim;
- an external framework equivalence claim;
- a peer-review claim;
- a change to the current AAEF control and assessment baseline.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

The purpose of this document is to define how future reconstruction exercises should be planned for the v0.7.0 Evaluation Readiness track.

The exercise should help reviewers ask whether they can reconstruct:

- what action was requested;
- what authority was required;
- what authorization decision applied;
- what dispatch decision occurred;
- whether backend verification was expected or invoked;
- whether the action executed or did not execute;
- what evidence relationships support the explanation;
- which gaps or uncertainties remain;
- what must not be concluded from the exercise.

The purpose is reviewability, not proof.

## Relationship to prior v0.7.0 artifacts

This artifact follows:

- `docs/en/status/v070-planning-entrypoint.md`
- `docs/en/status/v070-evaluation-readiness-planning.md`
- `docs/en/status/v070-evaluation-scenario-walkthrough-planning.md`
- `docs/en/status/v070-evaluation-scenario-walkthrough-candidates.md`
- `docs/en/status/v070-evaluation-artifact-inventory.md`

It contributes to:

- #317 — v0.7.0 roadmap
- #319 — Evaluation Readiness track

The prior artifacts defined evaluation scope, walkthrough structure, candidate scenarios, and an inventory of artifacts that may support future evaluation-readiness review. This document defines a reconstruction exercise planning pattern.

## Reconstruction exercise posture

A reconstruction exercise is a reviewer-facing structured exercise.

It may support:

- conceptual action traceability;
- review of evidence relationships;
- review of non-execution handling;
- identification of evidence gaps;
- role and boundary clarity;
- evaluation-readiness planning.

It must not claim:

- empirical validation;
- implementation conformance;
- production readiness;
- real-world safety;
- control effectiveness;
- audit sufficiency;
- legal sufficiency;
- compliance;
- certification;
- conformity;
- external framework equivalence;
- complete threat coverage;
- mitigation completeness.

## Candidate reconstruction objects

The initial reconstruction exercise should use the two scenario candidates from:

- `docs/en/status/v070-evaluation-scenario-walkthrough-candidates.md`

Candidate reconstruction objects:

| Candidate | Reconstruction focus |
| --- | --- |
| Candidate A: Permitted action with reviewable authority chain | Reconstruct why the action executed and whether the authority chain is reviewable. |
| Candidate B: Non-execution with reviewable denial or block reason | Reconstruct why the action did not execute and whether non-execution is reviewable. |

These candidates are illustrative. They are not executable fixtures and do not prove implementation behavior.

## Reconstruction exercise structure

Each future reconstruction exercise should use a consistent structure.

| Section | Purpose |
| --- | --- |
| Exercise objective | State what the reviewer is trying to reconstruct. |
| Reconstruction inputs | Identify the artifacts or fields used as input. |
| Expected relationship chain | Describe expected relationships across request, decision, dispatch, verification, evidence, and outcome. |
| Reviewer questions | List questions the reviewer must answer. |
| Reconstruction notes | Capture what can be explained and what remains unclear. |
| Gap classification | Distinguish legitimate non-invocation, missing evidence, ambiguity, and claim-boundary limitations. |
| Allowed conclusion | State the narrow conclusion the exercise may support. |
| Forbidden conclusions | State what the exercise must not claim. |

## Candidate input inventory

A reconstruction exercise may use the following current artifacts as input.

| Input artifact | Use in reconstruction | Limit |
| --- | --- | --- |
| `docs/en/status/v070-evaluation-scenario-walkthrough-candidates.md` | Source of Candidate A and Candidate B walkthrough fields. | Planning artifact only; not execution evidence. |
| `examples/evidence/permitted-action-evidence.example.json` | Illustrative permitted-action evidence relationship reference. | Does not prove evidence sufficiency. |
| `examples/evidence/non-execution-evidence.example.json` | Illustrative non-execution evidence relationship reference. | Does not prove complete prevention coverage. |
| `examples/prototype/fixtures/permitted/` | Static permitted-action fixture relationship reference. | Does not prove runtime behavior. |
| `examples/prototype/fixtures/non-execution/` | Static non-execution fixture relationship reference. | Does not prove operational enforcement. |
| `tools/validate_evidence_examples.py` | Hygiene validation reference for evidence examples. | Passing validation does not prove conformance. |
| `tools/validate_prototype_examples.py` | Hygiene validation reference for static prototype fixtures. | Passing validation does not prove production readiness. |

## Candidate A reconstruction plan

### Exercise objective

Reconstruct why Candidate A executed.

The reviewer should determine whether the candidate provides a reviewable chain from action request to execution outcome.

### Reconstruction inputs

Candidate inputs:

| Input | Candidate value |
| --- | --- |
| `action_request_id` | `arq-v070-candidate-a-0001` |
| `authorization_decision_id` | `auz-v070-candidate-a-0001` |
| `dispatch_decision_id` | `dsp-v070-candidate-a-0001` |
| `backend_verification_id` | `bev-v070-candidate-a-0001` |
| `evidence_event_id` | `evd-v070-candidate-a-0001` |
| `execution_outcome` | `executed` |

### Expected relationship chain

Expected chain:

1. The action request identifies the principal, action type, target resource, requested change, and high-impact status.
2. The authorization decision binds the same action request.
3. The dispatch decision binds the same authorization decision and action request.
4. Backend verification confirms the authorization and dispatch binding before effectful execution.
5. Evidence links the request, decision, dispatch, backend verification, and execution outcome.
6. The reviewer can reconstruct why execution occurred.

### Reviewer questions

The reviewer should answer:

- What action was requested?
- Why was authority required?
- Did the authorization decision bind the same requested action?
- Did dispatch follow the authorization decision?
- Did backend verification occur before effectful execution?
- Does the evidence relationship chain support reconstruction?
- Can the reviewer explain execution without relying on model self-report?
- What evidence would be missing in a real system before making a stronger claim?
- What does this exercise not prove?

### Reconstruction notes

The exercise may record:

- whether all illustrative identifiers are present;
- whether action binding appears internally consistent;
- whether the reviewer can explain execution;
- whether any evidence relationships are ambiguous;
- whether stronger claims would require implementation or runtime evidence.

### Gap classification

Candidate gap classes:

| Gap class | Meaning |
| --- | --- |
| No apparent illustrative gap | The illustrative relationship chain is complete for planning review. |
| Ambiguous binding | A relationship exists but is not specific enough to reconstruct confidently. |
| Missing evidence | Expected evidence is absent. |
| Unsupported stronger claim | The walkthrough is clear but does not support empirical, audit, compliance, or production claims. |

### Allowed conclusion

This exercise may support the following limited conclusion:

> Candidate A can be used as an illustrative reconstruction exercise for a permitted high-impact action with a reviewable authority, dispatch, backend verification, and evidence chain.

### Forbidden conclusions

This exercise must not claim:

- Candidate A proves implementation conformance;
- Candidate A proves production readiness;
- Candidate A proves real-world safety;
- Candidate A proves audit sufficiency;
- Candidate A proves compliance;
- Candidate A proves certification;
- Candidate A proves conformity;
- Candidate A proves legal sufficiency;
- Candidate A proves external framework equivalence;
- Candidate A proves complete threat coverage or mitigation completeness.

## Candidate B reconstruction plan

### Exercise objective

Reconstruct why Candidate B did not execute.

The reviewer should determine whether the candidate provides a reviewable non-execution chain from action request to denial or block outcome.

### Reconstruction inputs

Candidate inputs:

| Input | Candidate value |
| --- | --- |
| `action_request_id` | `arq-v070-candidate-b-0001` |
| `authorization_decision_id` | `auz-v070-candidate-b-0001` |
| `dispatch_decision_id` | `dsp-v070-candidate-b-0001` |
| `backend_verification_id` | `null` |
| `evidence_event_id` | `evd-v070-candidate-b-0001` |
| `execution_outcome` | `not_executed` |
| `non_execution_reason` | `authorization_denied_and_dispatch_blocked` |

### Expected relationship chain

Expected chain:

1. The action request identifies the principal, action type, target resource, requested change, and high-impact status.
2. The authorization decision binds the same action request and denies the action.
3. The dispatch decision binds the authorization decision and blocks dispatch.
4. Backend verification is not invoked because dispatch is denied.
5. Evidence links the request, denial, dispatch block, null backend verification context, and non-execution outcome.
6. The reviewer can reconstruct why execution did not occur.

### Reviewer questions

The reviewer should answer:

- What action was requested?
- Why was authority required?
- Why was authorization denied?
- Did dispatch block the action because authorization was denied?
- Is backend verification absent because the backend was not invoked?
- Is `null` backend verification a legitimate non-invocation marker or an evidence gap?
- Does the evidence relationship chain support non-execution reconstruction?
- Can the reviewer explain non-execution without inventing backend evidence?
- What evidence would be missing in a real system before making a stronger claim?
- What does this exercise not prove?

### Reconstruction notes

The exercise may record:

- whether denial or block reason is explicit;
- whether non-execution is distinguishable from missing evidence;
- whether backend non-invocation is explained;
- whether evidence supports review without implying execution;
- whether stronger prevention or safety claims would require additional evidence.

### Gap classification

Candidate gap classes:

| Gap class | Meaning |
| --- | --- |
| Legitimate non-invocation | A component was not invoked because an earlier boundary denied or blocked the action. |
| Missing evidence | A component should have recorded evidence but did not. |
| Ambiguous non-execution reason | The action did not execute, but the reason is unclear. |
| Unsupported prevention claim | The non-execution example is reviewable but does not prove complete prevention coverage. |

### Allowed conclusion

This exercise may support the following limited conclusion:

> Candidate B can be used as an illustrative reconstruction exercise for a denied or blocked high-impact action where non-execution remains reviewable.

### Forbidden conclusions

This exercise must not claim:

- Candidate B proves complete prevention coverage;
- Candidate B proves complete threat mitigation;
- Candidate B proves implementation conformance;
- Candidate B proves production readiness;
- Candidate B proves real-world safety;
- Candidate B proves audit sufficiency;
- Candidate B proves compliance;
- Candidate B proves certification;
- Candidate B proves conformity;
- Candidate B proves legal sufficiency;
- Candidate B proves external framework equivalence.

## Cross-candidate reconstruction review

The reviewer should compare Candidate A and Candidate B.

| Review dimension | Candidate A | Candidate B |
| --- | --- | --- |
| Requested action identified | Expected yes. | Expected yes. |
| Authority required | Expected yes. | Expected yes. |
| Model output treated as request only | Expected yes. | Expected yes. |
| Authorization decision reviewable | Expected yes. | Expected yes. |
| Dispatch decision reviewable | Expected yes. | Expected yes. |
| Backend verification context reviewable | Expected yes, invoked and verified. | Expected yes, not invoked because dispatch denied. |
| Outcome reviewable | Expected executed. | Expected not executed. |
| Evidence relationship reviewable | Expected yes. | Expected yes. |
| Stronger claims excluded | Expected yes. | Expected yes. |

## Reconstruction exercise acceptance checklist

A future reconstruction exercise should be accepted only if:

- the exercise objective is clearly stated;
- candidate inputs are listed;
- relationship chains are explicit;
- reviewer questions are included;
- legitimate non-invocation is distinguished from missing evidence;
- permitted action and non-execution outcomes are both reviewable;
- reconstruction notes can record uncertainty;
- allowed conclusions are narrow;
- forbidden conclusions are explicit;
- current baseline impact is excluded.

## Relationship to #319 acceptance criteria

This artifact supports #319 acceptance criteria as follows.

| #319 acceptance criterion | Support from this artifact |
| --- | --- |
| Evaluation readiness scope is documented. | Reconstruction exercise scope is defined as a narrow evaluation-readiness method. |
| Candidate evaluation methods are separated from empirical validation claims. | Reconstruction exercise is explicitly separated from empirical validation, conformance, production, audit, compliance, and equivalence claims. |
| Negative test and scenario walkthrough options are identified or explicitly deferred. | Candidate A and B are used as walkthrough/reconstruction inputs; further negative tests remain future work. |
| Claim boundaries are preserved. | Allowed and forbidden conclusions are explicitly listed. |
| Future implementation work is split into narrower follow-up issues. | Executable tests, fixtures, and runtime validation remain non-goals. |

## Candidate future follow-ups

If additional evaluation-readiness work is needed after #319, it should be split into narrower issues.

Potential future follow-ups:

| Follow-up | Purpose |
| --- | --- |
| Negative test candidate set | Define selected failure modes and expected review outcomes. |
| Fixture-to-scenario mapping | Relate static evidence/prototype examples to Candidate A and B without adding executable tests. |
| Reconstruction exercise checklist | Extract the acceptance checklist into a reusable reviewer checklist. |
| Evaluation method matrix | Compare artifact review, scenario walkthrough, reconstruction, negative test planning, and persona review. |

## Non-goals

This planning artifact does not:

- perform a reconstruction exercise;
- add executable tests;
- add scenario fixtures;
- add JSON examples;
- add empirical results;
- validate a deployed system;
- update active controls;
- update the evidence schema;
- update assessment artifacts;
- update testing procedures;
- create a conformance test suite;
- claim implementation conformance;
- claim production readiness;
- claim certification;
- claim compliance;
- claim conformity;
- claim audit sufficiency;
- claim legal sufficiency;
- claim external-framework equivalence;
- claim peer review;
- claim complete threat coverage;
- claim mitigation completeness.

## Recommended next step

After this artifact, #319 should be reviewed for closure readiness.

If #319 is closed, any future evaluation-readiness expansion should be split into a narrower follow-up issue rather than broadening #319.
