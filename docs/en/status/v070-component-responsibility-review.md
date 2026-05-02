# v0.7.0 Component Responsibility Review

## Status

This is a v0.7.0 planning artifact for Implementation Reviewability.

This document is:

- a planning artifact for #320;
- a follow-up to the v0.7.0 Implementation Reviewability Planning artifact;
- a follow-up to the v0.7.0 Implementation Review Checklist artifact;
- a follow-up to the v0.7.0 Prototype and Reference Boundary Note artifact;
- a follow-up to the v0.7.0 Implementation Assumption Inventory artifact;
- a follow-up to the v0.7.0 Validator Scope Matrix artifact;
- a component responsibility review for implementation-facing AAEF artifacts;
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

The purpose of this document is to make component responsibilities reviewable before future implementation-facing work expands.

The central question is:

> Which component is responsible for which decision, boundary, evidence, and review function?

This document separates:

- model proposal from authority;
- agent runtime orchestration from authorization;
- dispatch enforcement from backend relying-party verification;
- evidence generation from evidence interpretation;
- validator hygiene from implementation conformance;
- human approval from unrestricted execution authority;
- reviewer assessment from runtime enforcement.

The purpose is implementation reviewability, not implementation conformance.

## Relationship to v0.7.0 Implementation Reviewability

This artifact follows:

- `docs/en/status/v070-implementation-reviewability-planning.md`
- `docs/en/status/v070-implementation-review-checklist.md`
- `docs/en/status/v070-prototype-reference-boundary-note.md`
- `docs/en/status/v070-implementation-assumption-inventory.md`
- `docs/en/status/v070-validator-scope-matrix.md`

It contributes to:

- #317 — v0.7.0 roadmap
- #320 — Implementation Reviewability track

The prior artifacts define scope, review questions, boundaries, assumptions, and validator limits. This artifact maps those concerns to component responsibilities.

## Component set

For implementation reviewability planning, use the following component set.

| Component | Review role |
| --- | --- |
| Model | Produces output, recommendations, plans, or action requests. |
| Agent runtime | Orchestrates model interactions, state, context, and workflow. |
| Authorization decision point | Decides whether a requested action is authorized. |
| Tool dispatch enforcement point | Allows, denies, blocks, or constrains tool invocation. |
| Backend relying party | Verifies authority before effectful execution. |
| Evidence producer | Records action-bound evidence and correlation identifiers. |
| Evidence store | Stores evidence under defined integrity and retention assumptions. |
| Validator | Checks repository-level syntax, hygiene, consistency, and claim-boundary rules. |
| Human approver | Provides bounded approval where explicitly in scope. |
| Reviewer | Reviews artifacts, assumptions, boundaries, and evidence relationships. |
| Risk owner | Decides whether residual risk is acceptable outside this implementation-review scope. |

This set is conceptual and planning-oriented. It does not require a specific runtime architecture.

## Responsibility posture

A component responsibility review may support:

- reviewability;
- component boundary clarity;
- implementation assumption discovery;
- separation-of-authority analysis;
- evidence relationship review;
- future issue splitting.

A component responsibility review must not claim:

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
- mitigation completeness;
- peer review.

## Responsibility matrix

| Component | Responsible for | Not responsible for by default | Review concern |
| --- | --- | --- | --- |
| Model | Generating text, plans, recommendations, or action requests. | Granting authority, enforcing policy, proving execution safety, producing sufficient evidence by itself. | Model output must remain request/proposal, not authority. |
| Agent runtime | Orchestration, context handling, state mediation, request preparation. | Final authorization, backend relying-party verification, audit sufficiency. | Runtime must not silently promote model output into authority. |
| Authorization decision point | Making bounded authorization decisions. | Tool execution, backend execution, evidence sufficiency, legal sufficiency. | Decision must bind principal, action, target, parameters, freshness, and policy basis where applicable. |
| Tool dispatch enforcement point | Gating tool invocation based on authorization and dispatch rules. | Backend execution, final business action validity, compliance. | Dispatch must depend on authorization, not direct model output. |
| Backend relying party | Verifying authority before effectful execution where backend execution is in scope. | Trusting dispatcher blindly, creating audit sufficiency by default. | Backend should distinguish invoked, failed, denied, and legitimate non-invocation cases. |
| Evidence producer | Recording action-bound evidence and correlation identifiers. | Making compliance or audit conclusions. | Evidence should link request, decision, dispatch, verification, and outcome where applicable. |
| Evidence store | Preserving evidence according to stated integrity and retention assumptions. | Guaranteeing legal sufficiency unless separately scoped. | Integrity, retention, and access assumptions should be explicit. |
| Validator | Checking selected repository hygiene and consistency rules. | Proving conformance, production readiness, certification, or compliance. | Validator success must remain bounded. |
| Human approver | Providing bounded approval where in scope. | Replacing all technical authorization or backend verification by default. | Approval must be scoped, fresh, and bound to the requested action. |
| Reviewer | Inspecting artifacts, assumptions, boundaries, and relationships. | Enforcing runtime controls. | Review conclusions must be conservative. |
| Risk owner | Accepting or rejecting residual risk in an organizational context. | Performing technical enforcement by default. | Risk acceptance must not be implied by planning artifacts. |

## Model responsibility review

The model may:

- propose an action;
- describe a plan;
- summarize context;
- request a tool action;
- explain reasoning in a user-facing or operator-facing way;
- produce candidate evidence descriptions for review.

The model must not be treated as:

- authorization authority;
- policy enforcement point;
- backend relying party;
- evidence sufficiency source;
- audit authority;
- legal authority;
- compliance authority.

Review questions:

- Is model output clearly separated from authorization?
- Is model output treated as a request or proposal?
- Can downstream components reject or constrain model output?
- Is any model self-report treated as insufficient without corroboration?
- Does the artifact avoid saying the model “approved” or “authorized” an effectful action?

## Agent runtime responsibility review

The agent runtime may:

- manage conversation state;
- call the model;
- prepare action requests;
- apply context handling rules;
- route proposed actions to authorization or dispatch components;
- record runtime context under explicit assumptions.

The agent runtime must not be assumed to:

- authorize actions by itself unless explicitly designed as an authorization decision point;
- replace backend verification;
- provide audit sufficiency;
- prove control effectiveness;
- make production readiness claims.

Review questions:

- Does the runtime separate model output from controlled execution?
- Does it preserve context trust boundaries?
- Does it distinguish request preparation from authorization?
- Does it avoid direct tool execution without a dispatch boundary?
- Are runtime state assumptions explicit?

## Authorization decision point responsibility review

The authorization decision point may:

- evaluate whether an action is permitted;
- bind principal, action, target, parameters, scope, freshness, and policy basis;
- deny, allow, constrain, or require additional approval;
- produce an authorization decision identifier;
- record decision metadata.

The authorization decision point must not be assumed to:

- execute tools;
- perform backend business logic;
- create audit sufficiency by itself;
- guarantee downstream enforcement if dispatch and backend verification are absent.

Review questions:

- Which component makes the authorization decision?
- What is bound by the decision?
- Does the decision expire?
- Does the decision identify policy basis?
- Can dispatch and backend components verify the decision?
- Are deny and constrained outcomes represented?

## Tool dispatch enforcement responsibility review

The tool dispatch enforcement point may:

- allow, deny, block, or constrain tool invocation;
- check authorization decision identifiers;
- compare requested and authorized action context;
- reject expired or mismatched decisions;
- record dispatch evidence;
- preserve non-execution outcomes.

The tool dispatch enforcement point must not be assumed to:

- replace backend relying-party verification;
- guarantee final business action correctness;
- prove compliance;
- provide complete prevention coverage.

Review questions:

- Does dispatch depend on authorization rather than model output?
- Are dispatch outcomes explicit?
- Are expired, mismatched, denied, blocked, and failed outcomes distinguishable?
- Is non-execution reviewable?
- Does dispatch evidence link to the request and authorization decision?

## Backend relying-party responsibility review

The backend relying party may:

- verify authorization context before effectful execution;
- reject missing, expired, mismatched, or unauthorized requests;
- perform effectful action only after verification;
- record backend verification evidence;
- report execution or non-execution outcome.

The backend relying party must not be assumed to:

- trust dispatch blindly without verification unless explicitly scoped;
- generate audit sufficiency by default;
- cover all possible backends or integrations;
- prove production readiness.

Review questions:

- Is backend verification expected for effectful execution?
- What does the backend verify?
- Does backend verification bind to authorization and dispatch context?
- Is legitimate non-invocation distinguished from missing evidence?
- Is backend failure distinguishable from denial or block?

## Evidence producer responsibility review

The evidence producer may:

- record action request identifiers;
- record authorization decision identifiers;
- record dispatch decision identifiers;
- record backend verification identifiers where invoked;
- record outcome and non-execution reason;
- record timestamps and policy/version context where applicable.

The evidence producer must not be assumed to:

- decide authority;
- enforce controls;
- create compliance evidence by default;
- prove audit sufficiency or legal sufficiency.

Review questions:

- Which component produces which evidence?
- Is evidence generated outside model self-report where needed?
- Does evidence correlate request, decision, dispatch, backend verification, and outcome?
- Are evidence gaps explicit?
- Are integrity and retention assumptions documented?

## Evidence store responsibility review

The evidence store may:

- preserve evidence records;
- support retrieval for review;
- maintain integrity or tamper-evidence features if explicitly scoped;
- retain evidence under documented assumptions;
- support correlation across events.

The evidence store must not be assumed to:

- prove evidence correctness;
- prove evidence completeness;
- create legal sufficiency;
- create audit sufficiency;
- replace reviewer judgment.

Review questions:

- What integrity assumptions apply?
- What retention assumptions apply?
- Who can write, update, delete, or read evidence?
- Can evidence be correlated across components?
- What happens when evidence is missing or ambiguous?

## Validator responsibility review

The validator may:

- check syntax;
- check registration;
- check required fields;
- check selected identifier consistency;
- check selected controlled vocabulary;
- check selected claim-boundary language;
- run in CI as repository validation.

The validator must not be assumed to:

- certify an implementation;
- prove conformance;
- prove production readiness;
- prove audit sufficiency;
- prove legal sufficiency;
- validate runtime behavior;
- replace reviewer judgment.

Review questions:

- What files are in scope?
- What checks are performed?
- What checks are not performed?
- What does passing mean narrowly?
- What must passing not be interpreted as?

## Human approver responsibility review

The human approver may:

- approve, deny, or require change for a bounded action request;
- provide approval metadata;
- constrain time, target, action, parameters, or scope;
- participate in review where human approval is in scope.

The human approver must not be assumed to:

- authorize unrelated actions;
- provide indefinite approval;
- replace technical enforcement by default;
- create audit sufficiency automatically;
- accept residual risk unless explicitly acting as risk owner.

Review questions:

- What exactly did the human approve?
- Is approval bound to the action request?
- Does approval expire?
- Are approval conditions reviewable?
- Does backend verification remain in scope where required?

## Reviewer responsibility review

The reviewer may:

- inspect artifacts;
- evaluate assumptions;
- check component boundaries;
- compare claims against evidence;
- identify gaps;
- recommend follow-up work;
- confirm that claim boundaries are preserved.

The reviewer must not be assumed to:

- enforce runtime controls;
- certify the implementation;
- create compliance;
- produce an audit opinion;
- provide legal sufficiency;
- accept organizational risk by default.

Review questions:

- What artifact is under review?
- What conclusion is allowed?
- What conclusion is forbidden?
- What evidence supports the conclusion?
- What gaps remain?
- What follow-up issue should be created if stronger work is needed?

## Risk owner responsibility review

The risk owner may:

- accept or reject residual risk;
- request additional control work;
- set organizational risk appetite;
- decide whether implementation work can proceed in a defined environment.

The risk owner must not be assumed to:

- perform technical enforcement;
- replace authorization components;
- certify external framework alignment;
- accept risk silently through planning artifact approval.

Review questions:

- Is a risk decision in scope?
- Who is the accountable risk owner?
- What residual risk is being accepted?
- What evidence supports the risk decision?
- Is the decision separated from implementation reviewability?

## Cross-component responsibility checks

Use the following checks for future implementation-facing artifacts.

| Check | Expected result |
| --- | --- |
| Model output is separated from authority. | Model proposes or requests; independent component authorizes. |
| Authorization is separated from dispatch. | Authorization decision and dispatch decision are distinguishable. |
| Dispatch is separated from backend verification. | Dispatch gates invocation; backend verifies before effectful execution where in scope. |
| Evidence production is separated from evidence interpretation. | Evidence is recorded; reviewer interprets within limits. |
| Validator success is separated from conformance. | Validator passing result remains repository hygiene. |
| Human approval is bounded. | Approval is scoped, fresh, and action-bound where used. |
| Risk acceptance is explicit. | Risk owner decision is not implied by planning artifacts. |

## Responsibility gap categories

Use conservative categories.

| Gap category | Meaning |
| --- | --- |
| Responsibility documented | The component responsibility is explicit. |
| Responsibility documented with limits | Responsibility is explicit and bounded. |
| Responsibility deferred | Responsibility is relevant but explicitly out of scope. |
| Responsibility gap | Responsibility appears necessary but is not assigned. |
| Boundary conflict | Two components appear to own the same decision without clear separation. |
| Overclaim risk | Artifact wording could imply stronger responsibility or claims than supported. |

Avoid categories such as:

- responsibility satisfied;
- control effective;
- conformance achieved;
- production-ready;
- certified;
- compliant;
- audit-sufficient.

## Relationship to #320 acceptance criteria

This artifact supports #320 acceptance criteria as follows.

| #320 acceptance criterion | Support from this artifact |
| --- | --- |
| Implementation reviewability scope is documented. | Component responsibilities are mapped to review questions and gap categories. |
| Prototype/reference boundaries are preserved. | Prototype and reference work must map responsibilities before stronger implementation claims. |
| Assumptions and non-goals are clearly separated. | Each component has may-do and must-not-assume boundaries. |
| Claim boundaries are preserved. | Responsibility review explicitly excludes conformance, production, audit, compliance, certification, and equivalence claims. |
| Implementation-producing work is split into narrower follow-up issues. | Responsibility gaps and boundary conflicts are treated as follow-up triggers. |

## Candidate future follow-ups

Recommended follow-up artifacts after this review:

| Candidate follow-up | Purpose |
| --- | --- |
| Fixture-to-prototype transition plan | Define what would be required before static fixtures become executable prototype material. |
| Implementation review record template | Turn checklist, assumptions, validator scope, and responsibility review into a concise PR review template. |
| Component-boundary example review | Apply this responsibility review to one existing illustrative scenario without adding executable code. |

## Non-goals

This component responsibility review does not:

- add implementation code;
- add production service code;
- add executable prototype code;
- add validator code;
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

After this artifact, #320 should be reviewed for closure readiness.

If further implementation reviewability expansion is needed, it should be split into a narrower follow-up issue rather than broadening #320.
