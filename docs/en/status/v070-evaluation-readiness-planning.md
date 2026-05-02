# v0.7.0 Evaluation Readiness Planning

## Status

This is a v0.7.0 planning artifact for Evaluation Readiness.

This document is:

- a planning artifact for #319;
- a first child-track artifact under the v0.7.0 roadmap;
- a bridge from the v0.7.0 planning entrypoint to future evaluation design work;
- non-normative unless a later release explicitly promotes content into active guidance.

This document is not:

- an empirical evaluation result;
- a validation result for real-world systems;
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

The purpose of this document is to define the evaluation-readiness scope for v0.7.0 before adding scenario exercises, negative tests, reconstruction exercises, or evaluation-specific artifacts.

The central question is:

> What can AAEF be evaluated for, and what must not be claimed from those evaluations?

This planning artifact separates:

- evaluation design from empirical validation;
- example hygiene validation from evidence sufficiency;
- scenario walkthroughs from production testing;
- document review from implementation conformance;
- reconstruction exercises from audit sufficiency.

## Relationship to v0.7.0 planning

This artifact follows:

- `docs/en/status/v060-practical-adoption-readiness-completion-checkpoint.md`
- `docs/en/status/v070-planning-entrypoint.md`

It contributes to:

- #317 — v0.7.0 roadmap
- #319 — Evaluation Readiness track

The v0.7.0 planning entrypoint identified Evaluation Readiness as the first recommended track. This document defines the initial scope for that track.

## Evaluation readiness goals

The v0.7.0 Evaluation Readiness track should make AAEF easier to review and exercise without overclaiming.

Candidate goals:

| Goal | Meaning |
| --- | --- |
| Define evaluation objects | Identify which artifacts, examples, scenarios, or workflows can be evaluated. |
| Define evaluation methods | Separate artifact review, scenario walkthrough, negative testing, reconstruction exercises, and persona review. |
| Define evaluation limits | Make clear what each evaluation method cannot prove. |
| Preserve claim boundaries | Prevent evaluation artifacts from becoming compliance, certification, audit, production, or equivalence claims. |
| Create follow-up paths | Split future evaluation work into narrow reviewable issues and PRs. |

## Candidate evaluation objects

Future evaluation work may examine the following objects.

| Evaluation object | Candidate evaluation question | Boundary |
| --- | --- | --- |
| Control and assessment baseline | Are active baseline boundaries clearly preserved? | Does not update or validate the baseline. |
| Evidence examples | Are examples structurally hygienic and reviewable? | Does not prove evidence sufficiency. |
| Prototype fixtures | Are static fixtures internally consistent and reviewable? | Does not prove implementation correctness. |
| Conservative external mappings | Do mapping rows preserve non-equivalence and non-compliance boundaries? | Does not prove external framework alignment. |
| Adoption guidance | Can role-specific readers identify decisions, evidence, and limitations? | Does not prove operational readiness. |
| Scenario narratives | Can action authority separation be traced in a scenario? | Does not prove real-world safety. |
| Negative test cases | Are selected failure modes detectable or reviewable in the artifact model? | Does not prove complete threat coverage. |

## Candidate evaluation methods

### Artifact review

Artifact review examines whether repository artifacts are internally consistent, discoverable, and claim-boundary safe.

Candidate review questions:

- Are status documents registered in the status README and document map?
- Are examples validated by local tools and CI where appropriate?
- Are claim boundaries explicit?
- Are current baseline statements preserved?
- Are non-goals stated where confusion risk is high?

Boundary:

- Artifact review can support maintainability and clarity.
- Artifact review does not prove real-world control effectiveness.

### Scenario walkthrough

Scenario walkthroughs apply AAEF concepts to a representative agentic action flow.

Candidate review questions:

- What action was requested?
- What authority was required?
- What authorization decision was produced?
- What dispatch decision occurred?
- Was backend relying-party verification present?
- Did execution occur, fail, or get blocked?
- What evidence would allow reconstruction?

Boundary:

- Scenario walkthroughs can test conceptual traceability.
- Scenario walkthroughs do not prove production readiness or empirical effectiveness.

### Negative test planning

Negative test planning defines failure or abuse conditions that should be detectable or reviewable.

Candidate negative test areas:

- model output treated as authority;
- prompt-influenced tool call without independent authorization;
- stale authorization decision;
- action hash mismatch;
- missing dispatch decision;
- missing backend verification;
- missing evidence event;
- denied action without reviewable reason;
- ambiguous human approval scope;
- external mapping row with overclaiming language.

Boundary:

- Negative tests can help evaluate whether failure modes are visible in artifacts or examples.
- Negative tests do not prove complete threat coverage.

### Reconstruction exercise

A reconstruction exercise asks whether a reviewer can explain why an action executed or did not execute.

Candidate reconstruction questions:

- Can the reviewer link the action request to the authorization decision?
- Can the reviewer link the authorization decision to dispatch?
- Can the reviewer explain non-execution?
- Can the reviewer identify missing or ambiguous evidence?
- Can the reviewer identify which claim boundaries apply?

Boundary:

- Reconstruction exercises can support reviewability.
- Reconstruction exercises do not provide audit sufficiency by themselves.

### Persona review

Persona review asks whether different readers can understand what they own.

Candidate personas:

- implementer;
- operator;
- auditor or assessor;
- legal or compliance reviewer;
- risk owner;
- executive reviewer;
- researcher.

Candidate review questions:

- Can the persona identify their decision boundary?
- Can the persona identify what evidence they need?
- Can the persona identify what AAEF does not claim?
- Can the persona identify remaining residual risk?

Boundary:

- Persona review can improve adoption readiness.
- Persona review does not prove organizational deployment readiness.

## Evaluation claim boundaries

The following table defines what future evaluation artifacts may and may not support.

| Evaluation output | May support | Must not claim |
| --- | --- | --- |
| Artifact review | Internal consistency, registration, traceability, and claim-boundary hygiene. | Empirical validation, production readiness, compliance, certification, conformity, or audit sufficiency. |
| Scenario walkthrough | Conceptual traceability of authority, dispatch, backend verification, execution, and evidence. | Real-world safety, complete threat mitigation, or implementation conformance. |
| Negative test plan | Reviewable failure-mode coverage for selected examples. | Exhaustive security coverage or proof of risk elimination. |
| Reconstruction exercise | Ability to explain an illustrative action or non-execution flow. | Audit sufficiency or legal sufficiency. |
| Persona review | Reader comprehension and decision-boundary clarity. | Organizational readiness or governance effectiveness. |
| Mapping hygiene review | Non-equivalence and non-compliance language discipline. | External framework alignment, equivalence, conformity, or compliance. |

## Evaluation readiness acceptance model

Future evaluation-readiness artifacts should be assessed against the following questions.

| Acceptance question | Expected answer |
| --- | --- |
| Is the evaluation object clearly identified? | Yes. |
| Is the evaluation method clearly identified? | Yes. |
| Is the evaluation result limited to what the method can support? | Yes. |
| Are non-goals explicit? | Yes. |
| Is the current baseline preserved? | Yes. |
| Are stronger claims deferred unless evidence exists? | Yes. |
| Is future implementation or empirical work split into narrower issues? | Yes. |

## Candidate first evaluation follow-ups

Recommended follow-up issues or PRs after this planning artifact:

| Candidate follow-up | Purpose |
| --- | --- |
| Scenario walkthrough planning | Define one or two representative action scenarios for review. |
| Negative test candidate set | Define selected failure modes without claiming coverage completeness. |
| Reconstruction exercise planning | Define how reviewers would reconstruct permitted and non-executed actions. |
| Evaluation claim-boundary checklist | Create a reusable checklist for future evaluation artifacts. |
| Evaluation artifact inventory | Identify which current files can be evaluated and under what limits. |

## Non-goals

This planning artifact does not:

- perform an evaluation;
- report empirical results;
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

The recommended next step for #319 is a narrow evaluation artifact inventory or scenario walkthrough planning artifact.

The artifact should start with one or two representative agentic action scenarios and explicitly state what can and cannot be concluded from the walkthrough.

This keeps v0.7.0 evaluation work reviewable, conservative, and resistant to claim drift.
