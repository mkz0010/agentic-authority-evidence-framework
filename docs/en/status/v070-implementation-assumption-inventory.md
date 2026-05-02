# v0.7.0 Implementation Assumption Inventory

## Status

This is a v0.7.0 planning artifact for Implementation Reviewability.

This document is:

- a planning artifact for #320;
- a follow-up to the v0.7.0 Implementation Reviewability Planning artifact;
- a follow-up to the v0.7.0 Implementation Review Checklist artifact;
- a follow-up to the v0.7.0 Prototype and Reference Boundary Note artifact;
- an assumption inventory for implementation-facing AAEF artifacts;
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

The purpose of this document is to make implementation assumptions explicit before future implementation-facing work expands.

The central question is:

> Which assumptions must be visible before an implementation-facing artifact can be reviewed responsibly?

This inventory separates:

- documented assumptions from hidden assumptions;
- reviewable assumptions from implemented guarantees;
- local illustrative assumptions from deployable service assumptions;
- validator assumptions from conformance claims;
- prototype assumptions from production readiness.

## Relationship to v0.7.0 Implementation Reviewability

This artifact follows:

- `docs/en/status/v070-implementation-reviewability-planning.md`
- `docs/en/status/v070-implementation-review-checklist.md`
- `docs/en/status/v070-prototype-reference-boundary-note.md`

It contributes to:

- #317 — v0.7.0 roadmap
- #320 — Implementation Reviewability track

The implementation review checklist defines review questions. The prototype/reference boundary note defines artifact categories. This document inventories assumptions that should be explicit when those artifacts are reviewed.

## Assumption inventory posture

An assumption inventory may support:

- reviewability;
- implementation planning;
- boundary clarity;
- gap identification;
- future issue splitting;
- reviewer alignment.

An assumption inventory must not claim:

- implementation conformance;
- production readiness;
- empirical validation;
- runtime safety;
- audit sufficiency;
- legal sufficiency;
- certification;
- compliance;
- conformity;
- external framework equivalence;
- complete threat coverage;
- mitigation completeness.

## Assumption categories

Implementation-facing artifacts should identify assumptions in the following categories.

| Category | Purpose |
| --- | --- |
| Runtime boundary assumptions | Define where model planning ends and controlled execution begins. |
| Authorization assumptions | Define where authorization decisions are made and what they bind. |
| Dispatch assumptions | Define how tool invocation is gated. |
| Backend verification assumptions | Define how effectful systems verify authority before execution. |
| Evidence assumptions | Define how evidence is generated, correlated, stored, and reviewed. |
| Non-execution assumptions | Define how denial, block, expiry, mismatch, failure, and non-invocation are represented. |
| Human approval assumptions | Define how human approval is scoped, bound, and reviewed. |
| Validator assumptions | Define what validators check and what they do not check. |
| Prototype/reference assumptions | Define what future prototype or reference material would be allowed to show. |
| Deployment assumptions | Define what remains out of scope before deployable operation. |

## Runtime boundary assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Model output is not authority. | Is model output treated as request, proposal, or input only? | The implementation may silently treat model text as authorization. |
| Controlled execution begins outside the model. | Is the execution boundary separate from model reasoning? | Reviewers cannot locate enforcement responsibility. |
| Tool execution is mediated. | Is there a dispatcher or equivalent gate before tool invocation? | Tool calls may bypass independent review. |
| Runtime state is not automatically trusted. | Are memory, retrieved content, and runtime state treated according to trust level? | Prompt or memory influence may become unreviewed authority. |
| Agent-to-agent requests are not inherently trusted. | Are delegated or chained requests treated as requests requiring review? | Delegation may bypass authorization. |

Expected review result:

- The artifact identifies where model planning ends and controlled execution begins.

Must not claim:

- runtime safety;
- complete prompt-injection mitigation;
- production readiness;
- implementation conformance.

## Authorization assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Authorization decision is independent from model output. | Which component makes the decision? | The model may become the de facto authority. |
| Decision binds principal. | Which principal or actor is bound? | Actions may be authorized without accountable identity. |
| Decision binds action type. | What action is authorized? | Broad approval may cover unintended actions. |
| Decision binds target resource or scope. | What resource or scope is authorized? | Authorized action may be replayed against another target. |
| Decision binds parameters. | Which parameters are authorized? | Parameters may change after approval. |
| Decision has freshness or expiration. | When does authorization expire? | Stale authorization may be reused. |
| Decision references policy basis. | Which policy version or basis applies? | Reviewers cannot evaluate why the decision occurred. |

Expected review result:

- The artifact makes authorization binding assumptions visible.

Must not claim:

- complete authorization correctness;
- conformance;
- compliance;
- audit sufficiency.

## Dispatch assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Dispatch follows authorization. | Does dispatch depend on authorization rather than model output? | Tool calls may execute from model text alone. |
| Dispatch has explicit allow/deny/block outcomes. | Are outcomes reviewable? | Non-execution may be ambiguous. |
| Dispatch checks decision freshness. | Does dispatch reject expired decisions? | Stale decisions may be used. |
| Dispatch checks action binding. | Does dispatch compare requested and authorized action? | Parameter or target mismatch may execute. |
| Dispatch records decision context. | Is dispatch evidence available? | Reviewers cannot reconstruct the decision path. |
| Dispatch failure is represented. | Are errors and failures distinguishable from denial? | Failure may be misread as successful control behavior. |

Expected review result:

- The artifact makes dispatch expectations and limits explicit.

Must not claim:

- runtime enforcement unless implementation evidence exists;
- complete prevention coverage;
- production readiness.

## Backend verification assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Backend is a relying party, not a passive executor. | Does backend independently verify authority before effectful execution? | Dispatcher approval may become a single point of failure. |
| Backend verifies authorization context. | Does backend check decision, principal, action, target, parameters, and freshness where applicable? | Mismatched or replayed requests may execute. |
| Backend distinguishes non-invocation from missing evidence. | Is backend absent because dispatch blocked the action, or because evidence is missing? | Reviewers may invent backend behavior. |
| Backend records or contributes to evidence. | Is backend verification correlated to the action outcome? | Execution may not be reconstructable. |
| Backend failure is reviewable. | Can failed verification be distinguished from denied authorization? | Reviewers may overstate control behavior. |

Expected review result:

- The artifact identifies when backend verification is expected, invoked, not invoked, failed, or out of scope.

Must not claim:

- all backends implement relying-party verification;
- audit sufficiency;
- legal sufficiency;
- production readiness.

## Evidence assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Evidence is action-bound. | Can evidence be correlated to a specific action request? | Evidence may be generic or non-attributable. |
| Evidence is not merely model self-report. | Is evidence generated or corroborated outside the model? | Review may depend on untrusted self-report. |
| Evidence links request, authorization, dispatch, backend verification, and outcome. | Can the chain be reconstructed? | Reviewers cannot explain why execution did or did not occur. |
| Evidence gaps are visible. | Are missing identifiers treated as gaps or legitimate non-invocation? | Missing evidence may be mistaken for successful control behavior. |
| Evidence integrity assumptions are explicit. | Does the artifact state whether integrity, immutability, or tamper-evidence is assumed? | Reviewers may infer stronger trust than documented. |
| Evidence retention assumptions are explicit where relevant. | Is retention or availability assumed? | Reconstruction may fail after the fact. |

Expected review result:

- The artifact describes evidence correlation and evidence limits.

Must not claim:

- evidence sufficiency;
- audit sufficiency;
- legal sufficiency;
- compliance;
- certification.

## Non-execution assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Non-execution is a first-class outcome. | Does the artifact represent actions that did not execute? | Review may focus only on successful execution. |
| Denied, blocked, expired, failed, mismatched, and non-invoked outcomes are distinguishable. | Are non-execution reasons reviewable? | Reviewers may confuse control behavior with system failure. |
| Null identifiers are explained. | Does `null` mean legitimate non-invocation or missing evidence? | Reviewers may infer nonexistent backend behavior. |
| Non-execution evidence does not imply complete prevention. | Are prevention claims avoided? | A single blocked example may be overclaimed. |
| Non-execution is correlated to the request. | Can reviewers link the denied or blocked action to the original request? | Denials may not be attributable. |

Expected review result:

- The artifact explains how non-execution is represented and reviewed.

Must not claim:

- complete prevention coverage;
- complete mitigation;
- empirical validation;
- runtime safety.

## Human approval assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Human approval has scope. | What action, target, parameter, and time window does approval cover? | Approval may be reused too broadly. |
| Human approval is bound to the request. | Which request does approval apply to? | Approval may drift from the action actually executed. |
| Human approval has freshness. | Does approval expire? | Stale approval may authorize later actions. |
| Human approval is not a substitute for backend verification unless explicitly scoped. | Does backend still verify where needed? | Human approval may bypass technical enforcement. |
| Approval evidence is reviewable. | Can the approval be reconstructed? | Reviewers cannot determine what was approved. |

Expected review result:

- The artifact defines human approval assumptions when human approval is in scope.

Must not claim:

- human approval always satisfies authorization;
- audit sufficiency;
- legal sufficiency;
- compliance.

## Validator assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Validator scope is file-bound or artifact-bound. | What files does the validator inspect? | Passing validation may be overgeneralized. |
| Validator checks are explicit. | What conditions does the validator enforce? | Reviewers may infer checks that do not exist. |
| Validator non-goals are explicit. | What does the validator not check? | Hygiene validation may be mistaken for conformance. |
| Validator failures are actionable. | Are errors specific enough to fix? | Validation may not support maintenance. |
| Validator success is not conformance. | Is the passing result bounded? | CI success may be misrepresented as certification. |

Expected review result:

- The artifact explains validator scope, checks, limits, and non-goals.

Must not claim:

- certification;
- conformance;
- compliance;
- production readiness;
- audit sufficiency.

## Prototype assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Prototype scope is local and constrained unless explicitly stated otherwise. | What environment is assumed? | Prototype may be mistaken for deployable service. |
| Supported action classes are explicit. | What actions can the prototype illustrate? | Unsupported actions may be inferred. |
| Unsupported action classes are explicit. | What actions are excluded? | Dangerous or high-impact behavior may be assumed safe. |
| Prototype data is illustrative. | Are fixtures and examples non-production? | Test data may be mistaken for operational evidence. |
| Prototype teardown/reset is defined where relevant. | Can local state be reset? | Reviewers may misread prototype persistence or safety. |
| Prototype safety boundaries are explicit. | What must not be attempted? | Prototype may be misused. |

Expected review result:

- Prototype assumptions are explicit before executable work expands.

Must not claim:

- production readiness;
- customer deployment readiness;
- unrestricted operational safety;
- conformance.

## Reference implementation assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Reference scope is explicit. | What implementation pattern is being shown? | Reference material may be overgeneralized. |
| Non-target scope is explicit. | What does the reference not address? | Readers may infer complete coverage. |
| Operational assumptions are explicit. | What environment, identity, evidence, and policy assumptions apply? | Deployment assumptions may be hidden. |
| Residual risks are explicit. | What remains unresolved? | Reference material may imply completeness. |
| Validation scope is explicit. | What validation exists and what does it not prove? | Local tests may be mistaken for conformance. |

Expected review result:

- Reference implementation assumptions are reviewable before stronger claims are made.

Must not claim:

- certification;
- compliance;
- conformity;
- audit sufficiency;
- legal sufficiency;
- external framework equivalence;
- production readiness by default.

## Deployment assumptions

| Assumption | Review question | Risk if hidden |
| --- | --- | --- |
| Deployment is out of scope unless explicitly stated. | Does the artifact imply deployability? | Planning artifacts may be mistaken for deployment guidance. |
| Operating environment is unspecified unless documented. | Is there a target environment? | Reviewers may assume unsupported environments. |
| Security responsibility is unspecified unless documented. | Who operates and monitors the system? | Accountability may be unclear. |
| Data handling is unspecified unless documented. | What data is processed or retained? | Privacy and compliance implications may be hidden. |
| Incident response is unspecified unless documented. | What happens on control failure? | Operational readiness may be overclaimed. |

Expected review result:

- Deployment assumptions remain out of scope unless explicitly documented.

Must not claim:

- production readiness;
- customer deployment readiness;
- compliance;
- legal sufficiency;
- operational readiness.

## Assumption review matrix

Use the following matrix for future implementation-facing reviews.

| Assumption category | Should be explicit? | If absent, classify as |
| --- | --- | --- |
| Runtime boundary | Yes | Review gap |
| Authorization binding | Yes | Review gap |
| Dispatch enforcement | Yes | Review gap |
| Backend verification | Yes where effectful execution is in scope | Review gap or explicitly deferred |
| Evidence correlation | Yes | Review gap |
| Non-execution handling | Yes where denial/block/failure is in scope | Review gap or explicitly deferred |
| Human approval | Yes where human approval is in scope | Review gap or explicitly deferred |
| Validator scope | Yes where validation is referenced | Review gap |
| Prototype scope | Yes where prototype material is referenced | Review gap |
| Reference scope | Yes where reference material is referenced | Review gap |
| Deployment scope | Yes if deployment is discussed | Review gap |

## Result categories for assumption review

Use conservative result categories.

| Result | Meaning |
| --- | --- |
| Assumption documented | The assumption is explicitly stated. |
| Assumption documented with limits | The assumption is stated and bounded. |
| Assumption deferred | The assumption is relevant but explicitly out of scope. |
| Assumption gap | The assumption appears necessary but is not stated. |
| Not applicable | The assumption category does not apply to the artifact. |

Avoid result categories such as:

- assumption satisfied;
- conformance achieved;
- production-ready;
- validated;
- compliant;
- certified;
- audit-sufficient;
- legally sufficient.

## Relationship to #320 acceptance criteria

This artifact supports #320 acceptance criteria as follows.

| #320 acceptance criterion | Support from this artifact |
| --- | --- |
| Implementation reviewability scope is documented. | The inventory defines assumption categories needed for reviewability. |
| Prototype/reference boundaries are preserved. | Prototype and reference assumptions are separated from deployment and production claims. |
| Assumptions and non-goals are clearly separated. | Each category distinguishes expected review results from forbidden claims. |
| Claim boundaries are preserved. | Forbidden claims are listed for every assumption area. |
| Implementation-producing work is split into narrower follow-up issues. | Prototype, reference, deployment, and conformance work remain out of scope unless separately scoped. |

## Candidate future follow-ups

Recommended follow-up artifacts for #320:

| Candidate follow-up | Purpose |
| --- | --- |
| Validator scope matrix | Map validators to checks, limits, and forbidden claims. |
| Component responsibility review | Review model, runtime, dispatcher, backend, evidence, and reviewer responsibilities. |
| Fixture-to-prototype transition plan | Define what would be required before static fixtures become executable prototype material. |
| Implementation review record template | Turn checklist and assumption inventory into a concise PR review template. |

## Non-goals

This assumption inventory does not:

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

After this inventory, #320 should continue with a validator scope matrix or component responsibility review.

The next artifact should continue to separate reviewability from implementation conformance and production readiness.
