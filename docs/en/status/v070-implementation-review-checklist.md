# v0.7.0 Implementation Review Checklist

## Status

This is a v0.7.0 planning artifact for implementation reviewability.

This document is:

- a planning artifact for #320;
- a follow-up to the v0.7.0 Implementation Reviewability Planning artifact;
- a review checklist for implementation-facing artifacts;
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

The purpose of this document is to define a reusable checklist for reviewing implementation-facing AAEF artifacts.

The checklist helps reviewers ask:

- what kind of artifact is being reviewed;
- what assumptions it makes;
- what component boundaries it describes;
- whether model output is kept separate from execution authority;
- whether authorization, dispatch, backend verification, evidence, and non-execution expectations are reviewable;
- what the artifact may support;
- what the artifact must not claim.

The purpose is reviewability, not proof of correctness.

## Relationship to v0.7.0 Implementation Reviewability

This artifact follows:

- `docs/en/status/v070-planning-entrypoint.md`
- `docs/en/status/v070-evaluation-readiness-planning.md`
- `docs/en/status/v070-evaluation-artifact-inventory.md`
- `docs/en/status/v070-evaluation-reconstruction-exercise-planning.md`
- `docs/en/status/v070-implementation-reviewability-planning.md`

It contributes to:

- #317 — v0.7.0 roadmap
- #320 — Implementation Reviewability track

The prior implementation-reviewability planning artifact defined review objects, categories, dimensions, assumptions, and boundaries. This checklist turns those dimensions into review questions.

## Checklist use

Use this checklist when reviewing implementation-facing material such as:

- static examples;
- static prototype fixtures;
- validator scripts;
- reference architecture descriptions;
- implementation assumption notes;
- prototype boundary notes;
- future prototype or reference implementation proposals.

The checklist should be used conservatively.

A checklist pass may support:

- reviewability;
- artifact consistency;
- assumption clarity;
- boundary clarity;
- claim-boundary hygiene.

A checklist pass must not claim:

- implementation conformance;
- production readiness;
- empirical validation;
- runtime safety;
- audit sufficiency;
- legal sufficiency;
- compliance;
- certification;
- conformity;
- external framework equivalence;
- complete threat coverage;
- mitigation completeness.

## Review section 1: Artifact identity

| Question | Expected review result |
| --- | --- |
| What artifact is being reviewed? | The artifact path and title are identified. |
| What artifact category applies? | Planning-only artifact, static example, static fixture, validator, prototype code, or reference implementation material. |
| Is the artifact normative? | Expected no unless explicitly promoted by a later release. |
| Does the artifact claim to update the active baseline? | Expected no unless a later release explicitly changes the baseline. |
| Does the artifact define its own non-goals? | Expected yes for implementation-facing material. |
| Does the artifact identify related issues or PRs? | Expected yes where relevant. |

Reviewer note:

- If the artifact category is unclear, the artifact should not be used for stronger review conclusions.

## Review section 2: Scope and baseline boundary

| Question | Expected review result |
| --- | --- |
| Does the artifact preserve AAEF v0.4.1 as the current control and assessment baseline? | Expected yes unless explicitly changed by a later release. |
| Does the artifact avoid changing active controls? | Expected yes. |
| Does the artifact avoid changing the evidence schema? | Expected yes. |
| Does the artifact avoid changing assessment artifacts? | Expected yes. |
| Does the artifact avoid changing testing procedures? | Expected yes. |
| Does the artifact avoid silent normative promotion? | Expected yes. |

Reviewer note:

- Any active baseline change should be handled through an explicit release and should not be implied by planning or reviewability artifacts.

## Review section 3: Model output and authority separation

| Question | Expected review result |
| --- | --- |
| Does the artifact keep model output separate from execution authority? | Expected yes. |
| Does the artifact treat model output as request, proposal, or input rather than authorization? | Expected yes. |
| Does the artifact identify where authorization is made? | Expected yes, or explicitly deferred. |
| Does the artifact avoid relying on prompt text as an authority boundary? | Expected yes. |
| Does the artifact avoid treating model self-report as enforcement evidence? | Expected yes. |

Reviewer note:

- AAEF reviewability depends on preserving the distinction between model-generated requests and independently authorized execution.

## Review section 4: Authorization binding

| Question | Expected review result |
| --- | --- |
| Does the artifact describe what principal is bound? | Expected yes where applicable. |
| Does the artifact describe what action is bound? | Expected yes where applicable. |
| Does the artifact describe target resource or scope? | Expected yes where applicable. |
| Does the artifact describe parameter binding? | Expected yes where applicable. |
| Does the artifact describe decision freshness or expiration? | Expected yes or explicitly deferred. |
| Does the artifact describe policy version or decision basis? | Expected yes or explicitly deferred. |
| Does the artifact distinguish authorization decision from dispatch decision? | Expected yes. |

Reviewer note:

- If authorization binding is absent, the artifact may still be illustrative, but it should not be used to support implementation-review conclusions beyond that limit.

## Review section 5: Dispatch enforcement expectation

| Question | Expected review result |
| --- | --- |
| Does the artifact identify the dispatch decision point? | Expected yes where dispatch is in scope. |
| Does dispatch depend on authorization rather than model output? | Expected yes. |
| Does the artifact describe allow, deny, block, expired, or constrained outcomes where relevant? | Expected yes. |
| Does the artifact preserve non-execution as a reviewable outcome? | Expected yes. |
| Does the artifact avoid implying that dispatch enforcement is implemented unless code exists? | Expected yes. |

Reviewer note:

- A planning or fixture artifact can describe expected dispatch behavior, but it does not prove runtime enforcement.

## Review section 6: Backend verification expectation

| Question | Expected review result |
| --- | --- |
| Does the artifact identify whether backend relying-party verification is expected? | Expected yes where effectful execution is in scope. |
| Does backend verification bind to authorization and dispatch context? | Expected yes where applicable. |
| Does the artifact distinguish invoked backend verification from legitimate non-invocation? | Expected yes. |
| Does the artifact explain null or absent backend identifiers where appropriate? | Expected yes. |
| Does the artifact avoid claiming backend enforcement without implementation evidence? | Expected yes. |

Reviewer note:

- Backend verification is a key review boundary, but planning material should not imply deployed enforcement.

## Review section 7: Evidence and correlation

| Question | Expected review result |
| --- | --- |
| Does the artifact identify evidence relationships? | Expected yes where evidence is in scope. |
| Can action request, authorization, dispatch, backend verification, and outcome be correlated? | Expected yes or explicitly identified as a gap. |
| Does the artifact distinguish illustrative evidence from evidence sufficiency? | Expected yes. |
| Does the artifact avoid treating model self-report as sufficient evidence? | Expected yes. |
| Does the artifact identify evidence gaps or ambiguity where present? | Expected yes. |
| Does the artifact avoid audit sufficiency claims? | Expected yes. |

Reviewer note:

- Evidence correlation can support reviewability, but does not establish audit sufficiency or legal sufficiency by itself.

## Review section 8: Non-execution handling

| Question | Expected review result |
| --- | --- |
| Does the artifact treat non-execution as a first-class review outcome? | Expected yes where relevant. |
| Does it distinguish denied, blocked, expired, failed, mismatched, and non-invoked outcomes? | Expected yes or explicitly deferred. |
| Does it explain why backend verification may be absent in a non-execution path? | Expected yes where relevant. |
| Does it avoid inventing backend evidence when backend was not invoked? | Expected yes. |
| Does it avoid claiming complete prevention coverage from a non-execution example? | Expected yes. |

Reviewer note:

- Non-execution reviewability is not the same as complete prevention or complete mitigation.

## Review section 9: Validator scope

| Question | Expected review result |
| --- | --- |
| Does the artifact identify which validators apply? | Expected yes where applicable. |
| Does it explain what validators check? | Expected yes. |
| Does it explain what validators do not check? | Expected yes. |
| Does it avoid treating validator success as conformance? | Expected yes. |
| Does it avoid treating validator success as production readiness? | Expected yes. |
| Does it avoid treating validator success as compliance, certification, or audit sufficiency? | Expected yes. |

Reviewer note:

- Validators support repository discipline and hygiene. They do not prove implementation correctness.

## Review section 10: Prototype and reference boundary

| Question | Expected review result |
| --- | --- |
| Does the artifact identify whether it is static fixture, prototype, reference material, or production code? | Expected yes. |
| Does it avoid calling static fixtures executable? | Expected yes. |
| Does it avoid calling prototype material production-ready? | Expected yes. |
| Does it define local-only or illustrative boundaries where applicable? | Expected yes. |
| Does it identify unsupported action classes or deployment assumptions where relevant? | Expected yes or explicitly deferred. |
| Does it avoid customer deployment readiness claims? | Expected yes. |

Reviewer note:

- Future prototype or reference work should be reviewable without becoming a production or commercial deployment claim.

## Review section 11: Implementation assumptions

| Question | Expected review result |
| --- | --- |
| Are runtime boundary assumptions explicit? | Expected yes or explicitly deferred. |
| Are authorization component assumptions explicit? | Expected yes or explicitly deferred. |
| Are dispatch component assumptions explicit? | Expected yes or explicitly deferred. |
| Are backend verification assumptions explicit? | Expected yes or explicitly deferred. |
| Are evidence generation assumptions explicit? | Expected yes or explicitly deferred. |
| Are human approval assumptions explicit where applicable? | Expected yes or explicitly deferred. |
| Are storage, integrity, or tamper-evidence assumptions explicit where applicable? | Expected yes or explicitly deferred. |
| Are deployment assumptions explicit? | Expected yes or explicitly deferred. |

Reviewer note:

- Hidden assumptions should be treated as review gaps, not as satisfied requirements.

## Review section 12: Forbidden claims

The reviewed artifact should not claim any of the following unless a later explicit release, evidence package, or scoped process supports it.

| Forbidden claim | Expected result |
| --- | --- |
| Implementation conformance | Not claimed. |
| Production readiness | Not claimed. |
| Empirical validation | Not claimed. |
| Runtime safety | Not claimed. |
| Certification | Not claimed. |
| Compliance | Not claimed. |
| Conformity | Not claimed. |
| Audit sufficiency | Not claimed. |
| Legal sufficiency | Not claimed. |
| External framework equivalence | Not claimed. |
| Complete external framework coverage | Not claimed. |
| Complete threat coverage | Not claimed. |
| Mitigation completeness | Not claimed. |
| Peer review | Not claimed. |

Reviewer note:

- Claim-boundary violations should be corrected before merge or split into a clearly scoped future issue.

## Review result categories

Use conservative result categories.

| Result | Meaning |
| --- | --- |
| Reviewable | The artifact is clear enough for its stated planning or review purpose. |
| Reviewable with gaps | The artifact can be used, but assumptions or relationships need follow-up. |
| Planning-only | The artifact is intentionally non-normative and should not be used as implementation evidence. |
| Deferred | The review question is relevant but out of scope for the current artifact. |
| Not supported | The artifact does not support the requested conclusion. |

Avoid result categories such as:

- compliant;
- certified;
- conformant;
- production-ready;
- validated;
- audit-sufficient;
- legally sufficient;
- equivalent.

## Minimal review record template

Future implementation-review PRs may include a short review record.

Suggested template:

| Field | Review note |
| --- | --- |
| Artifact reviewed | Path or document title. |
| Artifact category | Planning, static example, fixture, validator, prototype, or reference material. |
| Review purpose | What the review attempted to determine. |
| Reviewable aspects | What can be reviewed. |
| Gaps or deferred items | What is missing or out of scope. |
| Claim boundaries | What must not be claimed. |
| Follow-up needed | Narrow future issue or PR if needed. |

## Relationship to #320 acceptance criteria

This artifact supports #320 acceptance criteria as follows.

| #320 acceptance criterion | Support from this artifact |
| --- | --- |
| Implementation reviewability scope is documented. | The checklist defines artifact identity, scope, review dimensions, and result categories. |
| Prototype/reference boundaries are preserved. | Dedicated prototype/reference boundary questions are included. |
| Assumptions and non-goals are clearly separated. | Assumption review and forbidden-claim sections are included. |
| Claim boundaries are preserved. | Forbidden claims and conservative result categories are explicit. |
| Implementation-producing work is split into narrower follow-up issues. | Code, fixtures, prototypes, and conformance work remain non-goals. |

## Candidate next follow-ups

Recommended follow-up artifacts for #320:

| Candidate follow-up | Purpose |
| --- | --- |
| Prototype/reference boundary note | Clarify boundaries for static fixtures, prototype material, and future reference work. |
| Implementation assumption inventory | Expand the assumptions section into a dedicated inventory. |
| Validator scope matrix | Map validators to checks, limits, and forbidden claims. |
| Component responsibility review | Review model, runtime, dispatcher, backend, evidence, and reviewer responsibilities. |

## Non-goals

This checklist does not:

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

The recommended next step for #320 is a prototype/reference boundary note or implementation assumption inventory.

The next artifact should continue to separate implementation reviewability from implementation conformance and production readiness.
