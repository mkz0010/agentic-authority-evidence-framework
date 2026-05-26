# Post-v1.0.0 Operational Action Validation Planning

Status: Planning artifact.

This document plans whether and how repository validation might later cover the static `examples/prototype/fixtures/operational-action/` fixture family.

It does not update validators.

It does not define AAEF conformance, implementation conformance, control conformance, certification, audit sufficiency, legal sufficiency, compliance sufficiency, evidence sufficiency, assessment sufficiency, production readiness, deployment guidance, customer PoC approval, or external-framework equivalence.

## Context

AAEF main now includes:

- generic prototype fixtures under `examples/prototype/fixtures/permitted/`
- generic prototype fixtures under `examples/prototype/fixtures/non-execution/`
- a separately scoped operational-action static fixture family under `examples/prototype/fixtures/operational-action/`

The current prototype fixture validator covers the existing generic `permitted/` and `non-execution/` fixture paths.

The `operational-action/` fixture family is currently static JSON example material and is not yet covered by operational-action-specific validation beyond general JSON syntax checks.

## Purpose

The purpose of future operational-action validation would be limited to static structural and consistency checks.

The purpose would not be to evaluate logistics policy correctness, RPA implementation design, production readiness, AAEF conformance, audit sufficiency, legal sufficiency, compliance sufficiency, evidence sufficiency, assessment sufficiency, or external-framework equivalence.

## Candidate validation checks

A future validator may check only static fixture structure and consistency, such as:

- required scenario directories are present
- required static JSON files are present in each scenario directory
- each file contains a JSON object
- `fixture_family` is `operational-action`
- `scenario_id` matches the scenario directory
- `correlation_id` is consistent across records in the same scenario
- `record_type` matches the fixture file role
- action request IDs are consistently referenced by downstream records
- authorization decision IDs are consistently referenced by dispatch and evidence records
- dispatch decision IDs are consistently referenced by backend verification and evidence records
- backend verification IDs are consistently referenced by evidence records
- allowed scenarios indicate dispatch and simulated backend invocation consistently
- denied scenarios indicate non-dispatch and simulated backend non-invocation consistently
- human-review-required scenarios indicate non-dispatch pending review and simulated backend non-invocation pending review consistently
- evidence outcome is consistent with authorization, dispatch, and backend records
- required claim-boundary markers are present
- records do not include obvious executable/runtime markers
- records do not include obvious production, customer-data, real credential, real backend, real RPA, scanner, vulnerability assessment, AAEF-AI-VA implementation, certification, compliance, audit, legal, conformance, sufficiency, or external-framework equivalence claims

## Non-goals for validation

A future validator must not check or imply:

- logistics policy correctness
- RPA implementation correctness
- backend implementation correctness
- production automation suitability
- deployment readiness
- customer PoC approval
- real backend authorization
- real shipment or address-change authorization
- audit evidence sufficiency
- legal sufficiency
- compliance sufficiency
- evidence sufficiency
- assessment sufficiency
- AAEF implementation conformance
- AAEF control conformance
- certification
- conformity
- external-framework equivalence
- scanner behavior
- vulnerability assessment behavior
- AAEF-AI-VA implementation correctness

## Suggested validation posture

Operational-action validation should be introduced, if at all, as a narrow repository hygiene check.

It should be described as a static fixture consistency validator.

It should not be described as an AAEF validator, conformance validator, assessment validator, audit validator, certification validator, compliance validator, legal validator, production readiness validator, or implementation validator.

## Relationship to reviewer walkthrough

Reviewer walkthrough work is separate.

A walkthrough may explain how to read one scenario and how the action request, authorization decision, dispatch decision, backend verification or non-invocation, evidence event, and reconstruction notes relate to one another.

A validator should not replace reviewer judgment.

## Recommended next step

The recommended next step is to keep the operational-action static fixture family stable while reviewing this validation planning boundary.

If validation is later implemented, it should be a separately scoped follow-up that updates validator code and documentation without changing the active baseline or making conformance, certification, audit, legal, compliance, evidence sufficiency, assessment sufficiency, production readiness, or external-framework equivalence claims.
