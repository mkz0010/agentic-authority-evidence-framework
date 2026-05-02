# v0.7.0 Evaluation Scenario Walkthrough Planning

## Status

This is a v0.7.0 planning artifact for evaluation scenario walkthroughs.

This document is:

- a planning artifact for #319;
- a follow-up to the v0.7.0 Evaluation Readiness planning artifact;
- a scenario-walkthrough design aid;
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

The purpose of this document is to define how future evaluation scenario walkthroughs should be structured before any scenario-specific artifacts are added.

The walkthrough pattern should help reviewers ask:

- What action was requested?
- What model output or agent planning step influenced the request?
- What authority was required?
- What authorization decision was produced?
- What dispatch decision occurred?
- What backend verification was expected?
- Did the action execute, fail, or not execute?
- What evidence would allow reconstruction?
- What claim boundaries apply to the walkthrough?

The purpose is reviewability, not proof.

## Relationship to v0.7.0 Evaluation Readiness

This artifact follows:

- `docs/en/status/v070-planning-entrypoint.md`
- `docs/en/status/v070-evaluation-readiness-planning.md`

It contributes to:

- #317 — v0.7.0 roadmap
- #319 — Evaluation Readiness track

The Evaluation Readiness planning artifact defined evaluation objects, evaluation methods, and claim boundaries. This document narrows the next step to scenario walkthrough planning.

## Scenario walkthrough posture

A scenario walkthrough is a structured review exercise.

It may support:

- conceptual traceability;
- role and boundary clarity;
- action-authority review;
- evidence relationship review;
- non-execution review;
- claim-boundary discipline.

It must not claim:

- empirical validation;
- implementation conformance;
- production readiness;
- control effectiveness;
- audit sufficiency;
- legal sufficiency;
- compliance;
- certification;
- conformity;
- external framework equivalence;
- complete threat coverage;
- mitigation completeness.

## Candidate walkthrough structure

Each future scenario walkthrough should use a consistent structure.

| Section | Purpose |
| --- | --- |
| Scenario summary | Describe the illustrative action flow in plain language. |
| Actor and role context | Identify the model, agent runtime, tool dispatcher, backend service, operator, and risk owner roles where relevant. |
| Action request | Describe the requested action and any model or prompt influence. |
| Authority requirement | Identify what authority would be required before execution. |
| Authorization decision | Describe what decision should exist and what it should bind. |
| Dispatch decision | Describe whether the tool dispatch should be allowed, denied, blocked, expired, or constrained. |
| Backend verification | Describe what relying-party verification should happen before effectful execution. |
| Execution outcome | Describe whether the action executed, failed, or did not execute. |
| Evidence and reconstruction | Identify the evidence relationships needed to reconstruct the action. |
| Review questions | List questions a reviewer should answer. |
| Claim boundaries | State what the walkthrough does not prove. |

## Candidate scenario types

The first scenario set should remain intentionally small.

Recommended initial scenario types:

| Scenario type | Purpose | Boundary |
| --- | --- | --- |
| Permitted high-impact action | Walk through a case where authority, dispatch, backend verification, and evidence align. | Does not prove production readiness or implementation conformance. |
| Blocked or denied action | Walk through a case where action does not execute and non-execution is reviewable. | Does not prove complete prevention coverage. |
| Stale authorization decision | Walk through a case where a decision should not authorize execution because freshness or binding has failed. | Does not prove all replay or stale-decision risks are mitigated. |
| Action hash or parameter mismatch | Walk through a case where the requested action differs from the authorized action. | Does not prove all tampering risks are mitigated. |
| Missing evidence event | Walk through a case where the reviewer cannot reconstruct the outcome. | Does not prove audit sufficiency; it demonstrates review limitation. |

## Recommended first two walkthroughs

The first implementation should use only one or two walkthroughs.

Recommended first pair:

### Walkthrough A: Permitted action with reviewable authority chain

Purpose:

- demonstrate the intended review path from action request to authorization, dispatch, backend verification, execution, and evidence.

Candidate review focus:

- action request identity;
- authorization decision identity;
- policy version;
- decision expiration;
- action binding;
- dispatch decision;
- backend relying-party verification;
- evidence event correlation;
- reviewer reconstruction.

Allowed conclusion:

- The walkthrough illustrates how a permitted action could be reviewed.

Forbidden conclusion:

- The walkthrough proves implementation conformance, production readiness, audit sufficiency, or real-world safety.

### Walkthrough B: Non-execution with reviewable denial or block reason

Purpose:

- demonstrate that denied, blocked, expired, mismatched, or non-invoked actions should be reviewable outcomes.

Candidate review focus:

- action request identity;
- denial, block, expiry, or mismatch reason;
- absence of backend execution where appropriate;
- null identifiers for non-invoked components where appropriate;
- evidence event correlation;
- reviewer reconstruction.

Allowed conclusion:

- The walkthrough illustrates how non-execution can remain reviewable.

Forbidden conclusion:

- The walkthrough proves complete prevention coverage, threat mitigation, audit sufficiency, or compliance.

## Walkthrough review questions

A reviewer should be able to answer the following questions.

### Action and request questions

- What action was requested?
- Who or what initiated the request?
- Was the request influenced by model output, prompt content, retrieved content, memory, or another agent?
- Is the requested action high impact?
- Is the requested action within an allowed scope?

### Authority questions

- What authority was required?
- Was model output treated as authority, or merely as a request?
- Which authorization decision applies?
- What policy version applies?
- What principal, scope, action, parameters, and expiration were bound?

### Dispatch and backend questions

- Did the dispatcher allow, deny, block, or refuse the action?
- Did the dispatch decision match the authorization decision?
- Was backend verification required?
- Did backend verification occur?
- Was execution prevented when backend verification was absent or failed?

### Evidence and reconstruction questions

- Which evidence events exist?
- Can the action request be correlated to authorization, dispatch, backend verification, and outcome?
- Can non-execution be explained without inventing evidence?
- Are missing identifiers meaningful because components were not invoked, or are they evidence gaps?
- Can a reviewer reconstruct the outcome without trusting the model's self-report?

### Claim-boundary questions

- What does this walkthrough illustrate?
- What does this walkthrough not prove?
- Which claims remain explicitly out of scope?
- What additional evidence would be needed before making a stronger claim?

## Evidence relationship model for walkthroughs

Future walkthrough artifacts should describe relationships without requiring a schema update.

Candidate relationship chain:

1. `action_request_id`
2. `authorization_decision_id`
3. `dispatch_decision_id`
4. `backend_verification_id`
5. `evidence_event_id`
6. outcome or non-execution reason

The chain should be interpreted conservatively.

- Present identifiers can support reconstruction.
- Missing identifiers may be legitimate when a component was not invoked.
- Missing identifiers may also indicate a review gap.
- The walkthrough must distinguish legitimate non-invocation from missing evidence.

## Non-execution handling

Non-execution must remain a first-class review outcome.

A walkthrough may include non-execution cases such as:

- authorization denied;
- authorization expired;
- action hash mismatch;
- parameter mismatch;
- dispatch blocked;
- backend verification failed;
- backend was not invoked;
- evidence event missing or incomplete.

For non-execution walkthroughs:

- `null` or absent identifiers may be appropriate for non-invoked components;
- the reason for non-execution should be reviewable;
- the walkthrough should not imply execution occurred;
- the walkthrough should not invent backend verification where none occurred;
- the walkthrough should not claim complete prevention.

## Walkthrough acceptance checklist

A future walkthrough artifact should be accepted only if:

- the scenario is clearly illustrative;
- the action request is described;
- the authority requirement is described;
- the authorization decision expectation is described;
- the dispatch decision expectation is described;
- backend verification expectations are described where relevant;
- execution or non-execution outcome is described;
- evidence relationships are described;
- reconstruction questions are listed;
- claim boundaries are explicit;
- current baseline impact is excluded.

## Candidate future artifacts

Recommended future artifacts after this planning document:

| Candidate artifact | Purpose |
| --- | --- |
| `v070-evaluation-scenario-walkthrough-candidates.md` | Define one or two walkthrough candidates. |
| `v070-evaluation-negative-test-candidate-set.md` | Define selected failure modes without claiming coverage completeness. |
| `v070-evaluation-reconstruction-exercise-planning.md` | Define how reviewers reconstruct permitted and non-executed outcomes. |
| `v070-evaluation-artifact-inventory.md` | Identify which current files can be reviewed and under what limits. |
| `v070-evaluation-claim-boundary-checklist.md` | Provide a reusable checklist for future evaluation artifacts. |

## Non-goals

This planning artifact does not:

- add executable tests;
- add scenario fixtures;
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

The recommended next step for #319 is to add one small scenario walkthrough candidate artifact.

The first candidate should include:

- one permitted action walkthrough;
- one non-execution walkthrough;
- explicit claim boundaries;
- no empirical validation claim;
- no implementation conformance claim;
- no production-readiness claim;
- no audit sufficiency, compliance, certification, conformity, legal sufficiency, peer-review, or external-framework equivalence claim.

The walkthrough candidate should remain illustrative and review-oriented.
