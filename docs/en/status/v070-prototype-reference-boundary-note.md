# v0.7.0 Prototype and Reference Boundary Note

## Status

This is a v0.7.0 planning artifact for Implementation Reviewability.

This document is:

- a planning artifact for #320;
- a follow-up to the v0.7.0 Implementation Reviewability Planning artifact;
- a follow-up to the v0.7.0 Implementation Review Checklist artifact;
- a boundary note for static examples, fixtures, validators, prototypes, reference implementation material, and production service code;
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

The purpose of this document is to preserve clear boundaries between different implementation-facing artifact types.

The central question is:

> What kind of implementation-facing material is this, and what must it not be mistaken for?

This boundary note separates:

- static examples from executable behavior;
- static fixtures from prototypes;
- validators from conformance tests;
- prototypes from reference implementations;
- reference implementation material from production service code;
- reviewability from implementation conformance;
- local illustrative material from deployable systems.

## Relationship to v0.7.0 Implementation Reviewability

This artifact follows:

- `docs/en/status/v070-implementation-reviewability-planning.md`
- `docs/en/status/v070-implementation-review-checklist.md`

It contributes to:

- #317 — v0.7.0 roadmap
- #320 — Implementation Reviewability track

The implementation review checklist provides review questions. This boundary note defines the artifact categories those questions should be applied to.

## Boundary vocabulary

Use the following vocabulary consistently.

| Term | Meaning |
| --- | --- |
| Static example | A non-executable illustrative file or document. |
| Static fixture | A non-executable structured example intended for local validation or review. |
| Validator | A script or workflow that checks repository hygiene or consistency rules. |
| Prototype | Future executable material intended to illustrate behavior under constrained local scope. |
| Reference implementation | Future implementation material intended to show a reviewable implementation pattern under explicit scope. |
| Production service code | Code intended to be operated as a deployed production service. |
| Reviewability | The ability to inspect assumptions, relationships, and boundaries. |
| Conformance | A stronger claim that an implementation satisfies defined requirements. |

## Artifact category boundaries

| Category | May support | Must not claim |
| --- | --- | --- |
| Static example | Illustrative structure, terminology, and review discussion. | Runtime behavior, implementation conformance, production readiness, audit sufficiency, or compliance. |
| Static fixture | Reviewable relationships and local consistency checks. | Executable enforcement, runtime correctness, production readiness, or conformance. |
| Validator | Repository hygiene, syntax, consistency, identifier checks, and claim-boundary guardrails. | Certification, compliance, conformance, production readiness, audit sufficiency, or legal sufficiency. |
| Prototype | Future constrained local demonstration under explicit scope. | Production service readiness, customer deployment readiness, certification, compliance, or unrestricted operational safety. |
| Reference implementation | Future reviewable implementation pattern under explicit assumptions. | Certification, audit sufficiency, legal sufficiency, external framework equivalence, or production readiness by default. |
| Production service code | Future deployable service code if explicitly scoped in a later release. | Should not be implied by planning, example, fixture, validator, prototype, or reference material. |

## Current repository boundary classification

The following current artifacts should be interpreted conservatively.

| Artifact or path | Boundary classification | Notes |
| --- | --- | --- |
| `examples/evidence/README.md` | Static example documentation | Explains evidence examples and boundaries. |
| `examples/evidence/*.example.json` | Static examples | Illustrative evidence examples; not proof of evidence sufficiency. |
| `examples/prototype/README.md` | Static fixture documentation | Explains prototype fixture boundaries. |
| `examples/prototype/fixtures/permitted/` | Static fixtures | Non-executable permitted-action fixture examples. |
| `examples/prototype/fixtures/non-execution/` | Static fixtures | Non-executable non-execution fixture examples. |
| `tools/validate_json_examples.py` | Validator | JSON syntax/example validation; not conformance. |
| `tools/validate_evidence_examples.py` | Validator | Evidence example hygiene validation; not evidence sufficiency. |
| `tools/validate_prototype_examples.py` | Validator | Static prototype fixture validation; not runtime enforcement. |
| `tools/validate_external_mappings.py` | Validator | Mapping hygiene and claim-boundary validation; not external alignment proof. |
| `.github/workflows/validate-aaef-artifacts.yml` | CI validation workflow | Runs repository validators; not a certification workflow. |
| `docs/en/status/v070-implementation-review-checklist.md` | Planning artifact | Review checklist; not an implementation specification. |

## Static example boundary

A static example may:

- illustrate expected fields or relationships;
- support discussion of evidence relationships;
- support walkthrough planning;
- support hygiene validation;
- support review of claim-boundary language.

A static example must not:

- be treated as runtime evidence;
- be treated as schema conformance unless explicitly validated by a scoped schema process;
- be treated as audit evidence;
- be treated as proof of production readiness;
- imply that a deployed system exists;
- imply that enforcement occurred.

Review questions:

- Is the example clearly labeled as illustrative?
- Does the example avoid conformance, production, compliance, or audit claims?
- Does the example identify non-goals or limitations?
- Does the example distinguish model output from authority where relevant?
- Does the example preserve non-execution as reviewable where relevant?

## Static fixture boundary

A static fixture may:

- represent an illustrative relationship chain;
- support local consistency validation;
- support scenario planning;
- support reconstruction exercise planning;
- support future prototype design discussion.

A static fixture must not:

- be treated as executable prototype code;
- be treated as runtime behavior;
- be treated as proof of enforcement;
- be treated as production service code;
- be treated as conformance evidence;
- be treated as complete test coverage.

Review questions:

- Is the fixture explicitly non-executable?
- Are identifiers internally consistent where required?
- Are non-invoked components represented without inventing execution?
- Are fixture limits clear?
- Are stronger claims explicitly excluded?

## Validator boundary

A validator may:

- check syntax;
- check required example metadata;
- check identifier consistency;
- check index registration;
- check conservative mapping fields;
- check claim-boundary phrases;
- detect selected suspicious overclaiming language.

A validator must not:

- certify an implementation;
- prove compliance;
- prove conformance;
- prove production readiness;
- prove audit sufficiency;
- prove legal sufficiency;
- prove complete threat coverage;
- prove mitigation completeness;
- replace reviewer judgment.

Review questions:

- What exact checks does the validator perform?
- What files or directories are in scope?
- What is explicitly out of scope?
- Does a passing result avoid stronger claims?
- Are validator errors actionable and bounded?

## Prototype boundary

A future prototype may:

- demonstrate a constrained local action flow;
- make component responsibilities easier to inspect;
- connect static examples to executable behavior under controlled scope;
- support local review of assumptions;
- expose implementation gaps for follow-up.

A future prototype must not:

- be presented as production service code;
- be presented as customer deployment-ready;
- be presented as safe for arbitrary targets;
- imply unrestricted tool execution safety;
- claim conformance;
- claim certification;
- claim compliance;
- claim audit sufficiency;
- claim legal sufficiency;
- claim external framework equivalence.

Prototype work should define:

- local environment assumptions;
- supported action classes;
- unsupported action classes;
- authorization boundary;
- dispatch boundary;
- backend verification boundary;
- evidence boundary;
- safety non-goals;
- teardown/reset expectations;
- reviewer expectations.

## Reference implementation boundary

A future reference implementation may:

- provide a reviewable implementation pattern;
- demonstrate how AAEF concepts can be composed;
- expose implementation assumptions;
- support implementer education;
- support future evaluation planning.

A future reference implementation must not automatically claim:

- production readiness;
- implementation conformance;
- certification;
- compliance;
- conformity;
- audit sufficiency;
- legal sufficiency;
- external framework equivalence;
- real-world safety;
- complete threat mitigation.

Reference implementation material should define:

- target scope;
- non-target scope;
- required assumptions;
- supported deployment mode, if any;
- unsupported deployment modes;
- evidence generation assumptions;
- validation scope;
- residual risks;
- known limitations.

## Production service code boundary

Production service code is out of scope for this planning artifact.

No current planning, example, fixture, validator, prototype, or reference material should be described as production service code unless a later issue and release explicitly scope that work.

Before any production service code is considered, future work should separately define:

- operating environment;
- target users;
- deployment assumptions;
- security responsibilities;
- operational monitoring expectations;
- data handling expectations;
- authorization and enforcement guarantees;
- evidence integrity expectations;
- rollback and incident response expectations;
- maintenance expectations;
- support expectations;
- legal and compliance review boundaries.

## Boundary escalation rules

Do not silently promote artifacts.

| From | To | Required action |
| --- | --- | --- |
| Static example | Static fixture | Explicit scope note and validation expectations. |
| Static fixture | Prototype | New issue, explicit non-goals, local safety boundaries, and review plan. |
| Prototype | Reference implementation | New issue, implementation assumptions, supported/unsupported scope, and claim boundaries. |
| Reference implementation | Production service code | Separate issue, security review, operational scope, legal/compliance review, and explicit production readiness process. |
| Validator | Conformance test | Separate issue, requirements definition, conformance criteria, and explicit claim boundary review. |

## Allowed wording

Preferred wording:

- illustrative example;
- static fixture;
- local validation;
- hygiene validation;
- reviewable assumption;
- candidate boundary;
- planning artifact;
- non-normative;
- may support review;
- does not prove conformance;
- does not imply production readiness.

Avoid wording:

- production-ready;
- certified;
- compliant;
- conformant;
- audit-sufficient;
- legally sufficient;
- equivalent to an external framework;
- validated implementation;
- complete mitigation;
- complete coverage;
- safe for deployment.

## Relationship to #320 acceptance criteria

This artifact supports #320 acceptance criteria as follows.

| #320 acceptance criterion | Support from this artifact |
| --- | --- |
| Implementation reviewability scope is documented. | Defines artifact categories and review boundaries. |
| Prototype/reference boundaries are preserved. | Explicitly separates static examples, static fixtures, validators, prototypes, reference implementation material, and production service code. |
| Assumptions and non-goals are clearly separated. | Each category includes may-support and must-not-claim boundaries. |
| Claim boundaries are preserved. | Forbidden promotions and avoided wording are explicit. |
| Implementation-producing work is split into narrower follow-up issues. | Boundary escalation rules require separate issues for prototype, reference, production, and conformance work. |

## Candidate future follow-ups

Recommended follow-up artifacts for #320:

| Candidate follow-up | Purpose |
| --- | --- |
| Implementation assumption inventory | Enumerate implementation assumptions that must be reviewed before executable work expands. |
| Validator scope matrix | Map validators to checks, limits, and forbidden claims. |
| Component responsibility review | Review model, runtime, dispatcher, backend, evidence, and reviewer responsibilities. |
| Fixture-to-prototype transition plan | Define what would be required before static fixtures become executable prototype material. |

## Non-goals

This boundary note does not:

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

After this boundary note, #320 should continue with an implementation assumption inventory or validator scope matrix.

The next artifact should continue to preserve the distinction between implementation reviewability and implementation conformance.
