# Post-v1.0.0 Implementation Guidance Priority Review

Status: Non-normative planning and review artifact.

This document identifies priority areas for practical AAEF implementation guidance after the completion of the post-v1.0.0 repository and roadmap review.

This document does not update the active control and assessment baseline. The active baseline remains AAEF v0.4.1 unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

AAEF v1.0.0 remains a conservative release path planning release.

## Purpose

The purpose of this review is to identify which implementation guidance areas should be addressed first without prematurely opening a major v1.1.0 roadmap or promoting planning material into the active baseline.

The immediate goal is to help future readers, especially security architects, understand where AAEF can be applied first and what material may later become an active-baseline candidate.

## Priority rationale

The next post-v1.0.0 work should prioritize implementation guidance because AAEF's central boundary is practical and architectural:

> Model output is not authority.

The highest-value implementation guidance should therefore focus on the point where model-generated intent, agent runtime behavior, authorization decisions, tool dispatch, backend execution, and evidence production meet.

This priority does not imply implementation readiness, operational readiness, implementation conformance, assessment sufficiency, audit sufficiency, legal sufficiency, certification, compliance, conformity, or equivalence with external frameworks.

## Primary audience order

The first implementation guidance path should be written for the following audiences in this order:

1. Security architects
2. Implementers and platform engineers
3. Reviewers, assessors, and risk owners
4. Operators and incident reviewers
5. Legal and compliance reviewers

Security architects should remain the first audience because AAEF is most useful when the system boundary is being designed or reviewed before high-impact agentic actions are delegated to automated systems.

## First guidance areas to consider

The first implementation guidance should focus on the following areas as non-normative candidate material.

### 1. Action boundary identification

Guidance should help readers identify where model output may become an attempted action.

This includes:

- tool calls
- workflow transitions
- approvals or approval requests
- data writes or mutations
- external API calls
- privileged operations
- irreversible or high-impact actions

The purpose is not to classify every action as high risk. The purpose is to make action boundaries visible and reviewable.

### 2. Authority separation

Guidance should explain how to separate model output from execution authority.

Candidate topics include:

- model output as request, not authority
- canonical action request boundaries
- authorization decision points
- tool dispatch enforcement points
- backend verification before execution
- human approval or freeze/hold handling for selected cases

This guidance should avoid claiming that any architecture automatically satisfies AAEF controls.

### 3. Trusted and untrusted input handling

Guidance should explain how systems can distinguish inputs used for authorization from inputs that may influence model behavior but should not be trusted as authority.

Candidate topics include:

- trusted inputs used
- untrusted inputs excluded
- user-provided or retrieved content that may influence the model
- prompt, retrieval, page, or document content that must not become authorization authority by itself

This is a priority because agentic systems often fail at the boundary between contextual influence and execution authority.

### 4. Evidence traceability

Guidance should explain what evidence should make review possible.

Candidate topics include:

- action request identity
- authorization decision identity
- dispatch decision identity
- backend verification result
- execution or non-execution result
- evidence event linkage
- policy or rule version linkage
- time and actor/principal context

This guidance should distinguish assessment support from evidence sufficiency, audit sufficiency, or legal sufficiency.

### 5. Non-execution cases

Guidance should cover denied, held, expired, revoked, and not-dispatched actions.

This is important because AAEF is not only about proving that an action happened. It is also about proving that a requested action was blocked, held, expired, or not executed when authority was absent or insufficient.

## Adoption planning view

The following planning view may be useful for future implementation guidance. It is not an implementation-readiness claim.

### Two-week orientation view

A short orientation path could help a security architect or reviewer:

- identify action boundaries
- identify where authorization decisions are made
- identify where tool dispatch is enforced
- identify where backend verification occurs
- identify where evidence is produced and retained
- identify obvious places where model output may be treated as authority

Expected output:

- initial action-boundary inventory
- initial authority-separation notes
- initial evidence-gap notes

This does not establish implementation readiness or conformance.

### Four-week guidance view

A four-week guidance path could help a team produce a more structured review package.

Candidate output:

- candidate architecture boundary diagram
- candidate action request model
- candidate authorization decision artifact shape
- candidate dispatch/evidence linkage notes
- denied and non-executed action examples
- reviewer questions and known gaps

This does not establish production readiness, operational readiness, evidence sufficiency, or assessment sufficiency.

### Twelve-week candidate view

A twelve-week planning path could help determine whether selected material is mature enough to become active-baseline candidate material.

Candidate output:

- implementation guidance draft
- reviewer guidance draft
- baseline candidate promotion notes
- known non-promotion criteria
- validation and example gaps
- external mapping gap statement

This does not promote material into the active baseline by itself.

## Candidate promotion considerations

Future promotion into active-baseline candidate material should require clear separation between:

- planning guidance
- examples and fixtures
- validator behavior
- normative control requirements
- assessment artifacts
- evidence schema requirements
- testing procedures

Material should not be promoted merely because it is useful, intuitive, or consistent with the AAEF thesis.

A future baseline candidate should be supported by:

- clear scope
- stable terminology
- reviewable examples
- explicit claim boundaries
- validator limitations where applicable
- no unsupported compliance, certification, conformity, audit, legal, or equivalence claims

## Non-goals

This review does not:

- update the active baseline
- create a v1.1.0 roadmap
- update the control catalog
- update the evidence schema
- update assessment artifacts
- update testing procedures
- update validators
- create implementation readiness
- create operational readiness
- create implementation conformance
- create control conformance
- create evidence sufficiency
- create assessment sufficiency
- create audit or legal sufficiency
- create certification, compliance, conformity, or external-framework equivalence
- establish semantic correctness or empirical validation

## Recommended next artifacts

Recommended next artifacts after this review are:

1. `post-v100-evidence-and-reviewer-guidance-review.md`
2. `post-v100-baseline-candidate-promotion-model.md`
3. `post-v100-framework-gap-statement-planning.md`

These should remain non-normative unless a later issue or release explicitly scopes baseline candidate promotion.
