# Post-v1.0.0 Framework Gap Statement Planning

Status: Non-normative planning and review artifact.

This document provides a conservative planning statement for how AAEF may be positioned relative to existing AI governance, security, identity, threat, and architecture frameworks.

This document does not update the active control and assessment baseline. The active baseline remains AAEF v0.4.1 unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

AAEF v1.0.0 remains a conservative release path planning release.

## Purpose

The purpose of this document is to clarify where AAEF begins without claiming that AAEF replaces, satisfies, certifies, implements, or is equivalent to external frameworks.

This planning statement is intended to support future communication, implementation guidance, reviewer guidance, and baseline-candidate planning.

It is not an external mapping, certification statement, compliance statement, conformity assessment, audit opinion, legal interpretation, or equivalence claim.

## Core thesis

AAEF's core thesis remains:

> Model output is not authority.

The practical gap AAEF focuses on is the boundary where model-generated or agent-generated intent may become actual action execution.

AAEF is most relevant when a system must answer:

1. Who or what requested the action?
2. On whose behalf was the action requested?
3. With what authority?
4. Was the action allowed at the point of execution?
5. What evidence proves what happened or did not happen?

## Planning-level gap statement

Many existing frameworks help organizations govern AI risk, define management systems, identify threats, manage identities, apply Zero Trust principles, or control privileged access.

AAEF is intended to complement those efforts by focusing on a narrower action-assurance boundary:

- model output as request, not authority
- action-bound authorization
- dispatch-time enforcement
- backend verification
- execution and non-execution evidence
- reviewer-visible traceability from request to decision to dispatch to result

This gap statement does not assert that existing frameworks lack value. It states that AAEF's distinctive focus is the execution-authority boundary for agentic AI systems.

## Relationship posture

AAEF should be positioned as:

- complementary to external frameworks
- narrower than broad AI governance frameworks
- more action-bound than general AI risk management language
- more evidence-bound than high-level architecture guidance
- more execution-bound than prompt, model, or policy-output review alone
- compatible with identity, access, and privileged-access control concepts
- not a replacement for external assurance, audit, legal, compliance, or certification processes

AAEF should not be positioned as:

- a certification scheme
- a compliance framework
- a legal sufficiency model
- an audit sufficiency model
- a complete AI governance program
- a complete secure development lifecycle
- a complete identity governance system
- a complete Zero Trust architecture
- a complete privileged access management system
- equivalent to NIST, ISO, OWASP, MITRE, IAM, Zero Trust, PAM, or any other external framework

## External framework categories

The following categories are useful for future planning.

The statements below are planning-level positioning notes. They are not authoritative summaries of external frameworks and should not be used as external mapping assertions without separate review against primary sources.

### AI risk and governance frameworks

Examples include broad AI risk management and AI management system frameworks.

These frameworks may help organizations structure governance, risk management, accountability, lifecycle controls, and management-system expectations.

AAEF's gap focus is narrower:

- whether model output is separated from execution authority
- whether authority is evaluated at the action boundary
- whether the enforcement point can deny or withhold action
- whether execution or non-execution is evidenced

AAEF should not claim that this focus satisfies broad AI governance requirements.

### AI security and threat frameworks

Examples include AI threat, adversarial technique, and application security guidance.

These frameworks may help identify threat patterns, attack paths, abuse cases, model/system risks, and testing considerations.

AAEF's gap focus is the execution boundary:

- whether a malicious, mistaken, or manipulated output can become action without authority
- whether tool dispatch is constrained by authorization decisions
- whether denied, held, expired, or revoked actions are evidenced
- whether reviewers can reconstruct the authority path

AAEF should not claim that it replaces threat modeling, application security testing, red teaming, or adversarial testing.

### LLM and agentic application security guidance

Examples include LLM application and agentic application security guidance.

These frameworks may help identify risks such as prompt injection, excessive agency, insecure tool use, sensitive information exposure, supply-chain risk, and unsafe plugin or tool interaction.

AAEF's gap focus is the point where those risks may result in actual action execution:

- model or tool request is not treated as authority
- untrusted content is not treated as authorization input by itself
- dispatch requires an authorization decision
- backend execution verifies the authority context
- evidence links the request, decision, dispatch, and result

AAEF should not claim that it fully addresses all LLM or agentic application security risks.

### Identity and access management

IAM helps identify principals, manage authentication, assign access, govern roles, and support authorization models.

AAEF's gap focus depends on identity and authorization context but is not identical to IAM.

AAEF asks whether a specific agentic action can be bound to:

- actor or principal context
- delegated authority
- action-specific authorization
- dispatch enforcement
- execution or non-execution evidence

AAEF should not claim that it replaces IAM, identity governance, access review, entitlement management, or authentication controls.

### Zero Trust architecture

Zero Trust concepts emphasize verification, least privilege, segmentation, continuous evaluation, and reduced implicit trust.

AAEF is compatible with this posture, but its focus is narrower and more evidence-specific.

AAEF asks whether a specific model-influenced or agent-requested action was authorized and enforced at the point of execution.

AAEF should not claim that it implements or satisfies Zero Trust architecture by itself.

### Privileged access management

PAM focuses on controlling, monitoring, and governing privileged access and privileged operations.

AAEF may be especially relevant where agentic systems request or influence privileged actions.

AAEF's gap focus is:

- whether the privileged action request is distinguishable from model output
- whether delegated authority is explicit
- whether dispatch is controlled
- whether backend execution verifies authority
- whether evidence records execution or non-execution

AAEF should not claim that it replaces PAM, session recording, credential vaulting, privileged workflow approval, or privileged access review.

### Audit, assurance, and compliance programs

External audit, assurance, and compliance programs depend on scope, criteria, evidence quality, professional judgment, legal context, and organizational obligations.

AAEF may support structured evidence and reviewer questions.

AAEF does not establish:

- audit sufficiency
- legal sufficiency
- compliance
- certification
- conformity
- control conformance
- evidence sufficiency
- assessment sufficiency

AAEF should be described as supporting review, not deciding assurance outcomes by itself.

## Where AAEF begins

AAEF begins where a system needs to determine whether a model-influenced or agent-requested action may execute.

AAEF is most relevant when:

- a model proposes an action
- an agent generates a tool request
- a workflow may mutate state
- an external system may be called
- a privileged or high-impact operation may occur
- retrieved or user-provided content may influence the action
- a human or automated reviewer later needs evidence of what happened
- a non-execution decision must be evidenced

AAEF's distinctive boundary is not the model's reasoning. It is the authority and evidence boundary around action.

## Where AAEF does not begin

AAEF does not begin as a complete replacement for:

- AI governance
- model evaluation
- model safety testing
- secure software development
- identity governance
- access review
- threat modeling
- red teaming
- vulnerability management
- privacy governance
- legal review
- audit planning
- compliance assessment
- certification

Those domains may remain necessary even if AAEF is used.

## Safe relationship language

Future AAEF communication should prefer wording such as:

- "AAEF complements existing AI governance and security frameworks."
- "AAEF focuses on the boundary where model output may become action."
- "AAEF helps make authority and evidence boundaries reviewable."
- "AAEF may support reviewer questions about action authorization and evidence traceability."
- "AAEF does not establish compliance, certification, audit sufficiency, legal sufficiency, or equivalence by itself."

Future AAEF communication should avoid wording such as:

- "AAEF satisfies NIST requirements."
- "AAEF implements ISO requirements."
- "AAEF is equivalent to OWASP guidance."
- "AAEF replaces IAM."
- "AAEF implements Zero Trust."
- "AAEF replaces PAM."
- "AAEF proves compliance."
- "AAEF certifies agentic AI systems."
- "AAEF establishes audit sufficiency."
- "AAEF establishes legal sufficiency."

## Future mapping boundary

A future external mapping may be useful, but it should remain conservative.

Any future mapping should distinguish:

- conceptual relationship
- partial support
- implementation dependency
- evidence support
- assessment support
- non-equivalence
- non-certification
- non-compliance
- non-conformity

Mapping rows should not imply that AAEF satisfies external framework requirements unless a future release explicitly scopes, supports, and qualifies such a claim.

## Baseline-candidate implications

This gap statement may inform future baseline-candidate planning by identifying where AAEF has independent value.

However, this document does not promote any material into the active baseline.

Future baseline-candidate work should avoid promoting external relationship language unless it has:

- clear scope
- primary-source review
- conservative mapping language
- explicit non-equivalence language
- reviewer limitation language
- no unsupported certification, compliance, conformity, audit, legal, readiness, conformance, sufficiency, or equivalence claims

## Non-goals

This planning statement does not:

- update the active baseline
- create a v1.1.0 roadmap
- update the control catalog
- update the evidence schema
- update assessment artifacts
- update testing procedures
- update validators
- update examples or fixtures
- create or update external mappings
- establish compliance with any external framework
- establish equivalence with any external framework
- establish certification, conformity, audit sufficiency, or legal sufficiency
- establish evidence sufficiency or assessment sufficiency
- establish implementation readiness, operational readiness, or production readiness
- establish implementation conformance or control conformance
- establish semantic correctness or empirical validation
- establish automated risk acceptance

## Recommended follow-up options

After this planning statement, possible follow-up work includes:

1. A public-facing gap statement suitable for README or overview material.
2. A reviewer-facing "AAEF can / cannot provide" reference.
3. A conservative external mapping review refresh.
4. A baseline-candidate close-readiness review for the current post-v1.0.0 track.
5. A decision on whether the next track should be stabilization, implementation guidance expansion, or baseline-candidate review.

Any follow-up should preserve the distinction between planning material, baseline-candidate material, and active baseline material.
