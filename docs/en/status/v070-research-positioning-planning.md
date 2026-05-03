# v0.7.0 Research Positioning Planning

## Purpose

This document defines the planning scope for the v0.7.0 research positioning track.

The goal is to make AAEF easier to describe, review, and discuss as a research-oriented framework without changing the active control and assessment baseline.

This document is planning guidance only. It does not introduce new controls, update the evidence schema, define assessment procedures, provide empirical validation, or claim peer-reviewed status.

## Relationship to the AAEF thesis

AAEF is organized around the thesis that model output is not authority.

For research positioning, this means AAEF should be described as a framework for analyzing and governing agentic action boundaries rather than as a framework for evaluating model text alone.

The research framing should keep attention on:

- who or what acted,
- on whose behalf the action was taken,
- what authority was used,
- whether execution was allowed at the point of action, and
- what evidence supports reconstruction of the action.

## Scope

This planning track may define:

- research problem framing,
- contribution boundaries,
- terminology useful for research discussion,
- relationships to assurance, governance, auditability, and AI safety discussions,
- candidate research questions,
- candidate future research artifacts, and
- claim-boundary language for research-facing materials.

This planning track may also identify where future work should be split into narrower issues.

## Non-goals

This document does not:

- change the current active control and assessment baseline,
- update the control catalog,
- update the evidence schema,
- update assessment artifacts,
- update testing procedures,
- introduce executable validators,
- introduce executable prototypes,
- introduce scenario fixtures,
- provide empirical validation,
- claim peer review,
- claim implementation conformance,
- claim production readiness,
- claim certification,
- claim legal compliance,
- claim conformity,
- claim audit sufficiency,
- claim legal sufficiency, or
- claim equivalence with external standards or frameworks.

## Research posture

AAEF should be positioned conservatively as a structured framework for reasoning about authority, execution boundaries, and evidence in agentic AI systems.

Research-facing descriptions should distinguish between:

- a conceptual framework,
- a control and evidence model,
- a review aid,
- a planning aid,
- a candidate basis for future empirical work, and
- a certification, compliance, or conformity scheme.

AAEF may support research discussion by making action authorization and evidence reconstruction explicit. It should not be presented as proving that a system is safe, compliant, auditable, or production-ready.

## Problem framing

Agentic AI systems can produce outputs that appear instruction-like, decision-like, or operationally useful. However, model output alone does not establish authority to act.

A research framing for AAEF should focus on the gap between:

- text generation and authorized action,
- intention and execution,
- delegated authority and runtime enforcement,
- system self-reporting and independently reviewable evidence, and
- post-incident explanation and action-bound reconstruction.

This framing helps separate model behavior questions from authority, governance, and evidence questions.

## Candidate research contribution areas

AAEF may contribute to research discussions in the following areas:

1. **Action authority separation**

   AAEF separates model output from authority to execute actions.

2. **Execution-boundary reviewability**

   AAEF emphasizes the point where an action is allowed, denied, held, or escalated.

3. **Action-bound evidence**

   AAEF emphasizes evidence that can be correlated to a specific action rather than relying only on general system claims.

4. **Delegation and principal context**

   AAEF supports analysis of who or what acted, on whose behalf, and with what authority.

5. **Reconstruction after execution or non-execution**

   AAEF supports discussion of how reviewers reconstruct allowed actions, denied actions, held actions, and evidence gaps.

6. **Conservative assurance language**

   AAEF can help distinguish useful assurance evidence from overclaims of compliance, certification, or safety.

## Relationship to existing discussions

AAEF may be discussed alongside existing work in:

- AI governance,
- AI safety,
- agentic AI risk management,
- access control,
- audit logging,
- security architecture,
- evidence-based assurance,
- incident reconstruction,
- model governance,
- software supply-chain security, and
- operational risk management.

Any such discussion should be framed as relationship or comparison, not equivalence.

AAEF should not claim to replace, satisfy, certify against, or be equivalent to external standards, frameworks, regulations, or audit methods.

## Research claim boundaries

Research-facing materials should be careful with terms such as:

- validated,
- proven,
- certified,
- compliant,
- equivalent,
- safe,
- secure,
- auditable,
- production-ready,
- legally sufficient,
- audit-sufficient, and
- peer-reviewed.

These terms should be avoided unless a later artifact explicitly defines the basis, evidence, review process, and claim scope.

Acceptable conservative wording includes:

- “AAEF proposes...”
- “AAEF frames...”
- “AAEF may help reviewers reason about...”
- “AAEF is intended to make the following boundary reviewable...”
- “This artifact does not establish compliance, conformity, certification, or audit sufficiency.”

## Candidate future research artifacts

Future #321 work may add narrower artifacts such as:

- research contribution inventory,
- research question inventory,
- terminology and concept boundary note,
- related-work positioning note,
- research claim-boundary checklist,
- paper-outline candidate,
- external-review readiness checklist, and
- public research communication guidance.

These should remain planning or positioning artifacts unless a later issue explicitly scopes empirical work, formal evaluation, or publication-oriented drafting.

## Review questions

Reviewers should be able to answer:

- Does this framing preserve the thesis that model output is not authority?
- Does this framing avoid implying certification, compliance, conformity, audit sufficiency, legal sufficiency, peer review, or empirical validation?
- Does this framing distinguish conceptual contribution from implemented system behavior?
- Does this framing distinguish evidence-supported reconstruction from general system self-reporting?
- Does this framing make future research artifacts easier to scope?
- Does this framing avoid external-framework equivalence claims?

## Relationship to v0.7.0 roadmap

This artifact supports the v0.7.0 Research Positioning track.

It is related to the v0.7.0 roadmap and should be treated as planning input for future research-facing artifacts.

It does not close the research positioning track by itself.
