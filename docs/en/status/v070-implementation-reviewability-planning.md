# v0.7.0 Implementation Reviewability Planning

## Status

This is a v0.7.0 planning artifact for Implementation Reviewability.

This document is:

- a planning artifact for #320;
- a child-track artifact under the v0.7.0 roadmap;
- a bridge from evaluation-readiness planning to future implementation review work;
- non-normative unless a later release explicitly promotes content into active guidance.

This document is not:

- an implementation specification;
- a reference implementation;
- production service code;
- executable prototype code;
- a conformance test suite;
- an implementation conformance claim;
- a production-readiness claim;
- a certification scheme;
- a compliance claim;
- a conformity claim;
- an audit sufficiency claim;
- a legal sufficiency claim;
- an external framework equivalence claim;
- a change to the current AAEF control and assessment baseline.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

The purpose of this document is to define the initial implementation-reviewability scope for v0.7.0.

The central question is:

> What should reviewers be able to inspect before future implementation work is treated as reviewable?

This planning artifact separates:

- implementation reviewability from production readiness;
- static examples from runtime behavior;
- validator hygiene from conformance;
- architectural assumptions from implemented enforcement;
- reference boundaries from certification or audit sufficiency.

## Relationship to v0.7.0 planning

This artifact follows:

- `docs/en/status/v060-practical-adoption-readiness-completion-checkpoint.md`
- `docs/en/status/v070-planning-entrypoint.md`
- `docs/en/status/v070-evaluation-readiness-planning.md`
- `docs/en/status/v070-evaluation-artifact-inventory.md`

It contributes to:

- #317 — v0.7.0 roadmap
- #320 — Implementation Reviewability track

The Evaluation Readiness track (#319) defined how selected artifacts may be reviewed without claiming empirical validation. This document starts the next track by defining how implementation-facing material should be reviewed without claiming production readiness or conformance.

## Implementation reviewability goals

The v0.7.0 Implementation Reviewability track should make future implementation work easier to inspect without overclaiming.

Candidate goals:

| Goal | Meaning |
| --- | --- |
| Define review objects | Identify which implementation-facing materials can be reviewed. |
| Define assumptions | Make implementation assumptions explicit before code or fixtures are expanded. |
| Define boundaries | Separate illustrative examples, static fixtures, validators, and future runtime behavior. |
| Define non-goals | Prevent implementation-facing artifacts from implying conformance, production readiness, audit sufficiency, or compliance. |
| Create follow-up paths | Split future implementation work into narrow reviewable issues and PRs. |

## Candidate review objects

Future implementation-reviewability work may examine the following objects.

| Review object | Candidate review question | Boundary |
| --- | --- | --- |
| Static prototype fixtures | Are fixture relationships internally consistent and reviewable? | Does not prove runtime behavior. |
| Evidence examples | Are action and non-execution examples hygienic and claim-boundary safe? | Does not prove evidence sufficiency. |
| Validator scripts | Do validators check intended repository-level hygiene rules? | Does not prove conformance or production readiness. |
| Reference architecture descriptions | Are component responsibilities and trust boundaries reviewable? | Does not implement enforcement. |
| Scenario walkthrough candidates | Can implementation assumptions be traced through illustrative action flows? | Does not validate a deployed system. |
| Future reference implementation notes | Can implementation scope be reviewed before code is added? | Does not create production service code by itself. |

## Implementation-facing artifact categories

Implementation-facing material should be categorized before review.

| Category | Description | Review boundary |
| --- | --- | --- |
| Planning-only artifact | Defines scope, assumptions, or follow-up structure. | Does not implement behavior. |
| Static example | Illustrates data or evidence relationships. | Does not prove runtime behavior. |
| Static fixture | Represents a non-executable example set. | Does not prove enforcement. |
| Validator | Checks repository hygiene or consistency rules. | Does not prove conformance. |
| Prototype code | Future executable prototype code, if added under explicit scope. | Must not imply production readiness. |
| Reference implementation | Future reviewable implementation material, if explicitly scoped. | Must not imply certification or audit sufficiency. |

## Review dimensions

Implementation review should focus on reviewability rather than production claims.

| Dimension | Review question | Must not become |
| --- | --- | --- |
| Authority separation | Is model output kept separate from execution authority? | A claim that all implementations are safe. |
| Authorization binding | Are principal, action, scope, parameters, and expiration assumptions reviewable? | A conformance claim. |
| Dispatch enforcement | Is dispatch expected to follow authorization rather than model output? | Proof of runtime enforcement. |
| Backend verification | Is relying-party verification expectation clear? | Proof that every backend implements it. |
| Evidence correlation | Can request, decision, dispatch, verification, and outcome be reviewed? | Audit sufficiency. |
| Non-execution handling | Is denied, blocked, expired, or non-invoked behavior reviewable? | Complete prevention coverage. |
| Validator scope | Are validator checks and limits explicit? | Certification or compliance. |
| Baseline impact | Is active baseline impact excluded unless explicitly changed? | Silent baseline update. |

## Implementation assumption inventory

Future implementation-facing work should state assumptions explicitly.

Candidate assumption areas:

| Assumption area | Example question |
| --- | --- |
| Runtime boundary | Where does model planning end and controlled execution begin? |
| Authorization decision point | Which component makes authorization decisions? |
| Tool dispatch enforcement | Which component gates tool invocation? |
| Backend relying-party verification | Which backend checks authorization before effectful action? |
| Evidence generation | Which component records evidence and correlation identifiers? |
| Evidence immutability or integrity | What integrity assumption is made, if any? |
| Human approval | What is the scope, binding, and freshness of human approval? |
| Non-execution | How are denied, blocked, expired, or non-invoked actions represented? |
| Validator role | What does each validator check, and what does it not check? |
| Deployment scope | Is the artifact local, illustrative, prototype, reference, or production? |

## Candidate implementation review checklist

A future checklist should help reviewers answer:

- What artifact is being reviewed?
- Is the artifact planning-only, example, fixture, validator, prototype, or reference material?
- What component boundary does it describe?
- Does it preserve the separation between model output and authority?
- Does it describe authorization binding?
- Does it describe dispatch enforcement expectations?
- Does it describe backend verification expectations?
- Does it describe evidence generation or correlation expectations?
- Does it handle non-execution explicitly?
- Does it identify assumptions and non-goals?
- Does it avoid conformance, production, compliance, certification, audit, legal, and equivalence claims?
- Does it preserve the current baseline?

## Validator review posture

Validators are important for repository discipline, but their claim boundary must remain explicit.

A validator may support:

- syntax validation;
- example hygiene validation;
- identifier consistency validation;
- index registration validation;
- mapping language guardrails;
- suspicious overclaiming phrase detection.

A validator must not claim:

- implementation conformance;
- production readiness;
- empirical validation;
- audit sufficiency;
- legal sufficiency;
- certification;
- compliance;
- conformity;
- external framework equivalence;
- complete threat coverage;
- mitigation completeness.

## Prototype and reference boundary posture

Future prototype or reference implementation work should be reviewed under strict boundaries.

Prototype work may support:

- illustration of component separation;
- local-only review;
- controlled fixture walkthroughs;
- validation of example shape;
- implementation assumption discovery.

Prototype work must not claim:

- production service readiness;
- customer deployment readiness;
- runtime safety for arbitrary targets;
- conformance;
- certification;
- compliance;
- audit sufficiency;
- legal sufficiency;
- equivalence to external frameworks.

Reference implementation work, if later scoped, should separately define:

- target environment;
- explicit non-goals;
- safety boundaries;
- runtime assumptions;
- supported action classes;
- unsupported action classes;
- evidence boundaries;
- validation scope;
- operational limits.

## Candidate first follow-ups for #320

Recommended follow-up issues or PRs after this planning artifact:

| Candidate follow-up | Purpose |
| --- | --- |
| Implementation review checklist | Create a reusable checklist for implementation-facing artifacts. |
| Prototype/reference boundary note | Clarify static fixture, prototype, and reference implementation boundaries. |
| Implementation assumption inventory | Enumerate assumptions required before implementation expansion. |
| Validator scope matrix | Map validators to what they check and what they do not claim. |
| Component responsibility review | Review model, runtime, dispatcher, backend, evidence, and reviewer responsibilities. |

## Relationship to #319

#319 Evaluation Readiness established review methods and candidate scenario/reconstruction planning.

#320 Implementation Reviewability should build on that by asking:

- What would an implementer need to expose for review?
- Which implementation assumptions are required for the scenario candidates to become executable later?
- What artifacts must remain planning-only?
- Which review steps can be supported by validators?
- Which claims remain explicitly out of scope?

This track should not reopen #319. Evaluation-specific expansion should be split into later follow-up issues if needed.

## Non-goals

This planning artifact does not:

- add implementation code;
- add production service code;
- add executable prototype code;
- add scenario fixtures;
- add JSON examples;
- update active controls;
- update the evidence schema;
- update assessment artifacts;
- update testing procedures;
- create a conformance test suite;
- claim implementation conformance;
- claim production readiness;
- claim empirical validation;
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

The recommended next step for #320 is a narrow implementation review checklist or prototype/reference boundary note.

The next artifact should remain documentation-only and should preserve the distinction between reviewability and implementation conformance.
