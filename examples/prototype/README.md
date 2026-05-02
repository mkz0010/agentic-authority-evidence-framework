# Prototype Examples

This directory is reserved for future AAEF prototype and reference implementation examples.

The initial purpose of this directory is to establish a safe, non-executable boundary for prototype-facing materials before fixtures, validators, or runnable code are introduced.

## Status and claim boundary

This directory currently contains documentation only.

It does not provide:

- executable prototype code,
- production service code,
- SDK-specific implementation,
- cloud-specific implementation,
- implementation conformance criteria,
- production readiness criteria,
- audit sufficiency evidence,
- legal or compliance conclusions,
- certification criteria,
- conformity criteria, or
- equivalence claims with external frameworks.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

Future prototype material should help explain the AAEF principle:

> Model output is not authority.

A prototype may later show how a model or agent can propose an action while execution depends on separately reviewable authority, enforcement, backend verification, evidence generation, and reconstruction.

This directory should remain illustrative and review-oriented unless a later PR explicitly changes its scope.

## Intended future scope

Future PRs may add small, static examples that illustrate:

- action request shape,
- authorization decision shape,
- dispatch enforcement decision,
- backend relying-party verification,
- permitted execution evidence,
- denied or non-executed action evidence,
- correlation identifiers,
- reconstruction path, and
- local validation expectations.

These materials should remain small enough to inspect manually.

## Planned directory shape

Candidate future layout:

~~~text
examples/prototype/
  README.md
  fixtures/
    action-request.example.json
    authorization-decision.example.json
    permitted-dispatch.example.json
    backend-verification.example.json
    permitted-evidence.example.json
    non-execution-evidence.example.json
~~~

This layout is a planning candidate only. Future PRs may adjust names, structure, or sequencing.

## Safe introduction sequence

A conservative sequence is:

1. keep this README as the non-executable boundary,
2. add static fixtures,
3. add fixture validation,
4. add reconstruction expectations,
5. consider narrow runnable examples only after static examples and validation are stable.

Executable prototype code should not be added before the boundary, fixture scope, validation expectations, and claim boundaries are clear.

## Relationship to existing examples

This directory should complement existing evidence examples.

It should not replace:

- existing evidence example files,
- evidence validation utilities,
- implementer guidance,
- operator guidance,
- risk-owner guidance,
- assessment methodology, or
- active baseline artifacts.

## Validation expectations

Future prototype examples should be locally validatable before they are treated as meaningful examples.

Candidate validation may include:

- JSON syntax validation,
- required field checks,
- correlation identifier consistency,
- action identifier consistency,
- authorization decision reference consistency,
- permitted-path consistency,
- non-execution-path consistency,
- absence of model-output-as-authority patterns,
- absence of production-readiness claims,
- absence of conformance claims, and
- absence of compliance or audit-sufficiency claims.

Validation should support learning and review. It should not imply production assurance.

## Non-goals

This directory does not currently provide:

- a runnable prototype,
- a reference implementation,
- a conformance test suite,
- a policy engine,
- an agent runtime,
- a dispatcher implementation,
- backend service code,
- SIEM or SOAR integration,
- production deployment guidance,
- security certification,
- compliance assurance,
- audit opinion support, or
- legal advice.

## Local fixture validation

Prototype fixtures can be checked locally with:

~~~bash
py tools/validate_prototype_examples.py
~~~

This validator is limited to static prototype fixtures under `examples/prototype/fixtures/`.

It checks:

- required fixture files,
- JSON object shape,
- required identifier fields,
- correlation consistency,
- permitted-path consistency,
- non-execution-path consistency, and
- static fixture claim-boundary markers.

The validator does not provide production assurance, implementation conformance, audit sufficiency, legal sufficiency, compliance sufficiency, certification, conformity, or equivalence with external frameworks.

## Current static fixtures

This directory now includes minimal static fixture examples for two illustrative paths:

- `fixtures/permitted/` — a permitted action path with request, authorization decision, dispatch decision, backend verification, evidence event, and reconstruction notes.
- `fixtures/non-execution/` — a non-execution path with request, authorization decision, dispatch refusal, backend non-execution, evidence event, and reconstruction notes.

These fixtures are static JSON examples only.

They do not provide:

- executable prototype behavior,
- runtime authorization,
- runtime dispatch enforcement,
- backend service behavior,
- validation-backed assurance,
- implementation conformance,
- production readiness,
- audit sufficiency,
- legal sufficiency,
- compliance sufficiency,
- certification, or
- conformity.

A later PR may add local validation for these fixtures.

## Next step

The next safe step is to add static fixtures for a permitted path and a non-execution path, or to define validation planning for such fixtures.

Any future executable code should be introduced only after the static fixture and validation boundaries are clear.
