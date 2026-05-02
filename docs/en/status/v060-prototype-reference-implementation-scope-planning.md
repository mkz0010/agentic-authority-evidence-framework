# v0.6.x Prototype and Reference Implementation Scope Planning

This document defines the planning scope for a future AAEF prototype or reference implementation.

It is a planning artifact for #285. It does not create a prototype, define implementation conformance, assert production readiness, update the evidence schema, update assessment artifacts, or change the current control and assessment baseline.

## Status

Planning artifact.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

The v0.6.0 and v0.6.x adoption materials remain non-normative unless explicitly promoted into active guidance or active examples.

## Purpose

The purpose of this planning document is to define what a future AAEF prototype or reference implementation should and should not demonstrate.

The prototype should help implementers understand the minimum practical shape of AAEF-style action assurance without implying that one reference implementation is the only valid implementation pattern.

The planning focus is:

- implementation scope,
- reference architecture boundaries,
- candidate components,
- evidence flow,
- permitted and non-execution paths,
- validation expectations,
- explicit non-goals,
- claim boundaries, and
- recommended next implementation steps.

## Prototype purpose

A future prototype should demonstrate the AAEF principle:

> Model output is not authority.

The prototype should show that a model or agent can propose an action, but execution requires separately reviewable authority, enforcement, evidence, and reconstruction.

A prototype should help answer:

- What is the minimum action request shape?
- Where is authorization represented?
- Where is dispatch enforcement applied?
- What does the backend verify?
- What evidence is generated for permitted execution?
- What evidence is generated for denied or non-executed actions?
- How can a reviewer reconstruct the action path?
- What failures should result in non-execution?

## Reference implementation positioning

A reference implementation should be illustrative.

It should not be presented as:

- production-ready,
- security-complete,
- legally sufficient,
- compliance sufficient,
- audit sufficient,
- certification criteria,
- conformity criteria,
- the only valid architecture,
- a complete agent platform, or
- an equivalence mapping to external frameworks.

The reference implementation should be a learning and validation aid.

## Candidate scope

A narrow initial prototype may include:

- a sample action request,
- a sample authorization decision artifact,
- a dispatch enforcement check,
- a backend relying-party verification check,
- a permitted execution path,
- a denied or non-execution path,
- evidence event generation,
- evidence correlation identifiers,
- simple reconstruction output, and
- local validation scripts.

The prototype should remain small enough to review, run locally, and reason about.

## Candidate components

A minimal prototype may include the following components.

### Action requester

Represents the component that submits an action request.

This may be a small script or fixture. It does not need to include a real LLM integration in the first prototype.

### Authorization decision producer

Represents the component that creates or provides an authorization decision artifact.

The first prototype may use static fixtures rather than a full policy engine.

### Dispatch enforcement point

Represents the component that decides whether a requested action may be dispatched.

It should check that required authority is present, valid for the requested action, and not expired or otherwise invalid.

### Backend relying party

Represents the backend component that refuses to rely only on caller intent or model output.

It should verify the relevant authorization context before accepting execution.

### Evidence generator

Represents the component that writes action-bound evidence for execution and non-execution outcomes.

It should produce evidence suitable for reconstruction.

### Reconstruction helper

Represents a small review utility that correlates request, authorization, dispatch, backend, and outcome records.

It should be illustrative, not a full audit tool.

## Candidate action flow

A future prototype may demonstrate the following flow:

1. An action request is created.
2. An authorization decision artifact is created or selected.
3. The dispatch enforcement point validates the decision against the requested action.
4. The backend relying party verifies the authority context where applicable.
5. The action is executed or refused.
6. Evidence is generated.
7. A reviewer reconstructs the action path from records.

The prototype should include both a permitted path and a non-execution path.

## Non-execution path

The non-execution path is important.

A prototype should show fail-closed behavior when:

- authorization is missing,
- authorization is expired,
- authorization is scoped to a different action,
- authorization is malformed,
- backend verification fails,
- dispatch enforcement refuses the request, or
- required evidence cannot be produced.

The exact cases should remain minimal in the first prototype, but at least one denied or non-executed action should be represented.

## Evidence expectations

A future prototype should show evidence records that are:

- action-bound,
- correlated across components,
- distinguishable from model narrative,
- sufficient to explain execution or non-execution,
- useful for reconstruction, and
- locally validatable.

Evidence should not imply audit sufficiency, certification, legal compliance, or production assurance.

## Validation expectations

A future prototype should include local validation commands.

Candidate validation may include:

- JSON syntax validation,
- required field checks,
- fixture consistency checks,
- correlation identifier checks,
- permitted-path checks,
- non-execution-path checks, and
- reconstruction-path checks.

Validation should support reviewability. It should not imply production readiness or implementation conformance.

## Candidate repository placement

Candidate locations:

- `examples/prototype/`
- `examples/reference-implementation/`
- `prototypes/`
- `tools/`

Initial recommendation:

- Use `examples/prototype/` for small runnable examples if the artifact is primarily educational.
- Use `prototypes/` only if a broader multi-component prototype is needed.
- Use `tools/` for validators or reconstruction helpers only when they are intended to be maintained as repository utilities.

A later PR should decide placement before adding executable prototype files.

## Relationship to existing examples

The prototype should relate to existing evidence examples without replacing them.

Existing evidence examples can inform:

- permitted action evidence,
- non-execution evidence,
- evidence field expectations,
- validation style, and
- reconstruction expectations.

The prototype should avoid duplicating example files unless duplication improves clarity.

## Relationship to implementer guidance

The prototype should support implementer understanding.

It should not replace implementer guidance, architecture guidance, operator guidance, risk-owner guidance, or assessment methodology.

The prototype should demonstrate concepts with minimal moving parts.

## Explicit exclusions

This planning document does not create:

- executable prototype code,
- production service code,
- a reference architecture mandate,
- new controls,
- new evidence schema fields,
- new assessment procedures,
- new testing procedures,
- implementation conformance criteria,
- production readiness criteria,
- certification criteria,
- conformity criteria,
- legal conclusions,
- compliance conclusions,
- audit sufficiency claims, or
- equivalence claims with external frameworks.

## Recommended next step

After this planning artifact is reviewed, create a small prototype scope decision or initial prototype skeleton.

A safe next implementation step would be one of:

- define prototype placement and file inventory,
- add a minimal non-executable prototype README,
- add static fixtures for permitted and non-execution paths, or
- add local validation for prototype fixtures.

The next PR should remain narrow and should preserve claim boundaries.
