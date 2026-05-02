# v0.6.x Prototype Static Fixture Planning

This document defines a conservative static fixture plan for future AAEF prototype examples.

It is a planning artifact for #285. It does not add fixture JSON files, validation tools, executable prototype code, implementation conformance criteria, or production readiness claims.

## Status

Planning artifact.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

The v0.6.0 and v0.6.x adoption materials remain non-normative unless explicitly promoted into active guidance or active examples.

## Purpose

The purpose of this planning document is to define the minimum static fixture set that may be added later under `examples/prototype/`.

This document follows:

- `docs/en/status/v060-prototype-reference-implementation-scope-planning.md`
- `docs/en/status/v060-prototype-placement-and-file-inventory-planning.md`
- `examples/prototype/README.md`

It narrows the next step from directory placement to static fixture content and validation boundaries.

## Fixture planning principles

Future static fixtures should be:

- small,
- manually reviewable,
- tool-neutral,
- SDK-neutral,
- cloud-neutral,
- action-bound,
- correlated across components,
- distinguishable from model narrative,
- useful for reconstruction, and
- explicit about non-execution outcomes.

Fixtures should not imply:

- production readiness,
- implementation conformance,
- audit sufficiency,
- legal sufficiency,
- compliance sufficiency,
- certification,
- conformity, or
- equivalence with external frameworks.

## Minimum fixture set

A conservative first fixture set may include two paths:

1. permitted path,
2. non-execution path.

The permitted path should show an action that is allowed to proceed because the required authority and enforcement conditions are present.

The non-execution path should show an action that does not execute because required authority, scope, validity, backend verification, or evidence conditions are not satisfied.

## Candidate directory layout

A later PR may add:

~~~text
examples/prototype/
  fixtures/
    permitted/
      action-request.example.json
      authorization-decision.example.json
      dispatch-decision.example.json
      backend-verification.example.json
      evidence-event.example.json
      reconstruction-notes.example.json
    non-execution/
      action-request.example.json
      authorization-decision.example.json
      dispatch-decision.example.json
      backend-verification.example.json
      evidence-event.example.json
      reconstruction-notes.example.json
~~~

This layout is a planning candidate only. Future PRs may reduce, rename, or split files if doing so improves reviewability.

## Permitted path fixture expectations

A permitted path should demonstrate:

- the requested action is identifiable,
- the acting or initiating context is identifiable,
- the authorization decision is action-bound,
- the authorization decision is valid for the requested action,
- dispatch enforcement checks the authorization decision,
- backend verification does not rely only on caller intent or model output,
- execution outcome is recorded,
- evidence is generated, and
- records can be correlated for reconstruction.

The permitted path should not imply that all real systems must use the same structure.

## Non-execution path fixture expectations

A non-execution path should demonstrate fail-closed behavior.

A minimal non-execution path may show one of the following:

- missing authorization,
- expired authorization,
- authorization scoped to a different action,
- malformed authorization,
- failed dispatch enforcement,
- failed backend verification, or
- required evidence unavailable.

The first non-execution fixture should use only one primary failure reason so that reviewers can understand the path clearly.

## Correlation expectations

Future fixtures should allow a reviewer to connect:

1. action request,
2. authorization decision,
3. dispatch decision,
4. backend verification,
5. execution or non-execution outcome,
6. evidence event, and
7. reconstruction notes.

Candidate correlation fields may include:

- `action_request_id`,
- `authorization_decision_id`,
- `dispatch_decision_id`,
- `backend_verification_id`,
- `evidence_event_id`,
- `correlation_id`,
- `policy_version`,
- `action_type`, and
- `outcome`.

Exact fields should align with existing examples and schema expectations where applicable.

## Validation planning

Validation should be introduced before fixtures are treated as meaningful examples.

A future validation script may check:

- JSON syntax,
- required file presence,
- required field presence,
- identifier consistency,
- action type consistency,
- authorization decision reference consistency,
- permitted path outcome consistency,
- non-execution path outcome consistency,
- absence of model-output-as-authority patterns,
- absence of production-readiness claims,
- absence of conformance claims, and
- absence of compliance or audit-sufficiency claims.

Validation should support learning and review. It should not imply production assurance.

## Relationship to existing evidence examples

Prototype fixtures should complement existing evidence examples.

They may reuse concepts from:

- `examples/evidence/permitted-action-evidence.example.json`
- `examples/evidence/non-execution-evidence.example.json`

Prototype fixtures should not replace those examples or redefine the active evidence schema.

If a prototype fixture intentionally differs from existing examples, the difference should be explained in the prototype README or fixture notes.

## Maintenance considerations

Before adding fixtures, the project should consider:

- whether fixture names are stable enough,
- whether correlation fields are sufficiently clear,
- whether fixtures duplicate existing examples unnecessarily,
- whether validation rules are too strict or too loose,
- whether fixtures imply implementation conformance,
- whether examples can become stale as planning materials evolve, and
- whether fixture updates should be required when evidence examples change.

## Explicit exclusions

This planning document does not add:

- fixture JSON files,
- validators,
- executable prototype code,
- SDK-specific implementation,
- cloud-specific implementation,
- production service code,
- reference architecture mandate,
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

After this planning artifact is reviewed, a later PR may add the first minimal static fixtures.

The recommended first fixture PR should include:

- one permitted path,
- one non-execution path,
- clear reconstruction notes, and
- either validation planning notes or a minimal validation script.

If validation cannot be added in the same PR, the fixture README should clearly mark the fixtures as illustrative and not yet validation-backed.
