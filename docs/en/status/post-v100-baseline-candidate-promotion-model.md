# Post-v1.0.0 Baseline Candidate Promotion Model

Status: Non-normative planning and review artifact.

This document defines a conservative model for how post-v1.0.0 planning, guidance, example, and review material may later be considered for active-baseline candidate promotion.

This document does not update the active control and assessment baseline. The active baseline remains AAEF v0.4.1 unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

AAEF v1.0.0 remains a conservative release path planning release.

## Purpose

The purpose of this document is to prevent accidental baseline drift.

AAEF has accumulated planning, readiness, review, example, validation, and adoption-oriented material across multiple release cycles. Some of that material may become useful for a future active-baseline update. However, useful material should not be treated as baseline material merely because it exists, is well written, is validated structurally, or is consistent with the AAEF thesis.

This document provides a conservative promotion model for distinguishing:

- planning material
- guidance material
- examples and fixtures
- validators
- reviewer aids
- baseline-candidate material
- active baseline material

## Core premise

AAEF's core thesis remains:

> Model output is not authority.

The same principle should apply to AAEF's own development process:

- planning output is not baseline authority
- example output is not normative authority
- validator output is not semantic authority
- reviewer guidance is not audit or legal authority
- external mapping is not equivalence authority

A later release must explicitly identify any baseline update.

## Current baseline boundary

The active control and assessment baseline remains AAEF v0.4.1 unless a later release explicitly updates one or more baseline artifacts, such as:

- control catalog
- evidence schema
- assessment artifacts
- testing procedures

Post-v1.0.0 planning artifacts do not update the active baseline by themselves.

This includes this document.

## Promotion stages

Future work should use the following conservative stages.

### Stage 0: Planning material

Planning material identifies ideas, risks, candidate directions, open questions, review findings, or future work.

Examples include:

- roadmap notes
- readiness reviews
- implementation guidance priority reviews
- evidence and reviewer guidance reviews
- gap statements
- adoption planning notes
- public communication review notes

Stage 0 material is not baseline material.

### Stage 1: Guidance material

Guidance material helps readers interpret, apply, or review AAEF concepts.

Examples include:

- implementation guidance
- reviewer guidance
- operator guidance
- risk-owner guidance
- safe wording guidance
- non-execution review guidance

Stage 1 material may be useful for adoption, but it is not automatically baseline-candidate material.

### Stage 2: Example or fixture material

Example or fixture material illustrates possible AAEF-shaped records, scenarios, decisions, events, or flows.

Examples include:

- evidence event examples
- prototype fixtures
- denied-action examples
- non-executed-action examples
- permitted-action examples
- static validation examples

Stage 2 material must remain clearly distinguishable from normative requirements.

Examples and fixtures may support understanding. They do not establish required implementation behavior by themselves.

### Stage 3: Validator-supported material

Validator-supported material is structurally checked by repository tooling.

Validators may check:

- schema conformance
- index registration
- JSON example validity
- fixture consistency
- documentation coverage
- example hygiene

Validator support may improve maintenance quality. It does not establish semantic correctness, implementation correctness, evidence sufficiency, assessment sufficiency, control conformance, audit sufficiency, legal sufficiency, or external-framework equivalence.

### Stage 4: Baseline-candidate material

Baseline-candidate material is material that has been explicitly identified for possible future incorporation into the active baseline.

Baseline-candidate material should have:

- a clearly scoped issue or PR
- explicit relationship to existing baseline artifacts
- stable terminology
- clear normative vs non-normative boundaries
- clear evidence and assessment implications
- explicit non-goals
- validator limitation language where applicable
- reviewer limitation language where applicable
- claim-boundary review
- migration or compatibility notes where needed

Stage 4 material is still not active baseline material.

### Stage 5: Active baseline material

Material becomes active baseline material only when a later release explicitly updates the relevant active baseline artifacts.

This should require explicit release notes and repository changes identifying what changed.

A future active baseline update should clearly state whether it updates:

- control requirements
- evidence schema requirements
- assessment artifacts
- testing procedures
- required examples or fixtures, if any
- validator expectations, if any
- document map and status references

## Promotion criteria

Planning, guidance, example, reviewer, or validator material should not become baseline-candidate material unless it satisfies the following criteria.

### 1. Clear scope

The material must define what it covers and what it does not cover.

It should identify whether it concerns:

- action requests
- authorization decisions
- dispatch enforcement
- backend verification
- evidence events
- non-execution records
- reviewer guidance
- assessment preparation
- implementation guidance
- external mapping
- public communication

### 2. Clear relationship to existing baseline

The material must explain whether it relates to existing baseline artifacts and how.

It should not silently change the meaning of existing controls, evidence schema fields, assessment procedures, or testing expectations.

### 3. Stable terminology

The material should use terminology consistently with existing AAEF documents or explicitly define any new terms.

New terms should not be promoted if they are still exploratory, ambiguous, or likely to change.

### 4. Normative boundary

The material must make clear whether it is:

- normative
- non-normative
- illustrative
- planning-only
- reviewer guidance
- implementation guidance
- candidate material

A future baseline-candidate PR should not rely on ambiguous wording.

### 5. Evidence and assessment boundary

The material must distinguish between:

- evidence structure
- evidence traceability
- evidence sufficiency
- assessment support
- assessment sufficiency
- audit sufficiency
- legal sufficiency

AAEF may support structure and traceability, but should not imply sufficiency without explicit scope-specific criteria.

### 6. Validator boundary

If validators are relevant, the material must state what validators can and cannot establish.

Validator success must not be described as proof of semantic correctness, control conformance, implementation correctness, audit sufficiency, legal sufficiency, or production readiness.

### 7. Example boundary

If examples or fixtures are relevant, the material must state that examples are illustrative unless a later release explicitly promotes them into a normative role.

Examples should not be treated as required behavior merely because they appear in the repository.

### 8. Claim-boundary review

The material must avoid unsupported claims of:

- certification
- compliance
- conformity
- audit sufficiency
- legal sufficiency
- production readiness
- operational readiness
- implementation readiness
- implementation conformance
- assessment sufficiency
- testing sufficiency
- evidence sufficiency
- semantic correctness
- empirical validation
- automated risk acceptance
- control conformance
- external-framework equivalence

### 9. Reviewability

The material should be reviewable by a human reader.

It should be possible to identify:

- what changed
- why it matters
- what it affects
- what it does not affect
- what evidence supports the change
- what risks remain

### 10. Promotion path

The material should identify what additional work would be needed before active-baseline promotion.

This may include:

- control wording updates
- evidence schema updates
- testing procedure updates
- assessment artifact updates
- example updates
- validator updates
- migration notes
- compatibility review
- reviewer guidance updates

## Non-promotion criteria

Material should not become baseline-candidate material if any of the following apply.

### 1. The material is only useful, not stable

A useful idea is not enough for baseline-candidate promotion.

The material should be stable enough to review against the active baseline and future maintenance expectations.

### 2. The material relies on ambiguous authority language

Material should not be promoted if it blurs the distinction between:

- model output and authority
- request and authorization
- authorization and dispatch
- dispatch and execution
- evidence existence and evidence sufficiency
- validator success and semantic correctness
- assessment support and audit/legal sufficiency

### 3. The material creates unsupported readiness claims

Material should not be promoted if it implies implementation readiness, operational readiness, production readiness, conformance, compliance, certification, audit sufficiency, or legal sufficiency without explicit scope and support.

### 4. The material depends on examples as normative requirements

Examples may be used to explain behavior, but example presence should not silently create normative requirements.

### 5. The material depends on validators as assurance conclusions

Validator success may support maintenance and structural checks. It should not become an assurance conclusion by itself.

### 6. The material changes baseline behavior indirectly

Material should not be promoted if it changes the expected meaning of controls, evidence schema, assessment artifacts, or testing procedures without explicitly updating those artifacts.

### 7. The material creates external-framework equivalence risk

External mappings may support comparison and communication. They should not imply equivalence with NIST, ISO, OWASP, MITRE, IAM, Zero Trust, PAM, or any other external framework unless a future release explicitly scopes and supports such a claim.

## Baseline-candidate issue requirements

A future issue that proposes baseline-candidate promotion should include:

- target artifact or material
- reason for candidate consideration
- affected baseline artifacts, if any
- expected non-normative vs normative status
- relationship to active baseline
- relationship to examples, validators, or reviewer guidance
- known claim-boundary risks
- non-goals
- validation plan
- expected reviewer audience

## Baseline-candidate PR requirements

A future PR that proposes baseline-candidate material should include:

- explicit statement that the material is baseline-candidate, not active baseline, unless the PR is part of a release explicitly updating the active baseline
- affected files
- claim-boundary impact
- validation results
- reviewer guidance impact
- example or validator impact, if applicable
- migration or compatibility notes, if applicable
- related issue references

## Active baseline update requirements

A future active baseline update should be explicit.

It should identify:

- release version
- updated baseline artifacts
- unchanged baseline artifacts
- whether controls changed
- whether evidence schema changed
- whether assessment artifacts changed
- whether testing procedures changed
- whether examples or validators changed
- transition notes from the previous active baseline
- claim boundaries that remain unchanged

An active baseline update should not be inferred from planning documents, status notes, examples, validation tooling, external mappings, or public communication material.

## Relationship to current post-v1.0.0 track

This model supports the post-v1.0.0 implementation guidance and baseline candidate planning track.

It follows:

- `post-v100-implementation-guidance-priority-review.md`
- `post-v100-evidence-and-reviewer-guidance-review.md`

Together, these documents establish:

- which implementation guidance areas should be considered first
- how evidence and reviewer guidance should avoid overclaiming
- how planning material may later be considered for baseline-candidate status

## Recommended next artifact

The recommended next artifact is:

- `post-v100-framework-gap-statement-planning.md`

That artifact should clarify where AAEF fits relative to existing frameworks without asserting equivalence.
