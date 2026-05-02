# v0.6.x Prototype Placement and File Inventory Planning

This document defines a conservative placement and file-inventory plan for future AAEF prototype or reference implementation work.

It is a planning artifact for #285. It does not add executable prototype code, production service code, implementation conformance criteria, or production readiness claims.

## Status

Planning artifact.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

The v0.6.0 and v0.6.x adoption materials remain non-normative unless explicitly promoted into active guidance or active examples.

## Purpose

The purpose of this planning document is to decide where future prototype material should live and what files may be introduced first.

This document follows the v0.6.x Prototype and Reference Implementation Scope Planning artifact.

It narrows the next step from general prototype scope to repository placement and file inventory.

## Placement decision

Initial recommendation:

- Use `examples/prototype/` for the first prototype-facing materials.
- Keep the first step educational and review-oriented.
- Avoid adding executable prototype code in the first placement PR.
- Avoid creating a separate repository until the maintenance burden is clearer.
- Avoid using `prototypes/` until a broader runnable multi-component prototype is justified.
- Use `tools/` only for validators or reconstruction helpers that are intended to be maintained as repository utilities.

Rationale:

- `examples/prototype/` keeps prototype material near existing examples.
- It signals that the material is illustrative.
- It reduces the risk of implying production readiness.
- It allows static fixtures and README guidance to be added incrementally.
- It preserves a path to later validation without requiring executable prototype code immediately.

## Candidate initial file inventory

A safe first file inventory may include:

- `examples/prototype/README.md`

This first file should be non-executable and should explain:

- prototype purpose,
- claim boundary,
- planned file layout,
- intended future fixtures,
- intended future validation,
- relationship to existing evidence examples,
- non-goals, and
- next steps.

No executable code should be added in the initial placement PR.

## Candidate later file inventory

Later PRs may consider adding files such as:

- `examples/prototype/fixtures/action-request.example.json`
- `examples/prototype/fixtures/authorization-decision.example.json`
- `examples/prototype/fixtures/permitted-dispatch.example.json`
- `examples/prototype/fixtures/backend-verification.example.json`
- `examples/prototype/fixtures/permitted-evidence.example.json`
- `examples/prototype/fixtures/non-execution-evidence.example.json`
- `examples/prototype/README.md`
- `tools/validate_prototype_examples.py`

These names are candidates only. A later PR should decide exact names and validation scope.

## Initial README scope

The initial `examples/prototype/README.md` should explain:

- the prototype is illustrative,
- model output is not authority,
- the prototype is not production-ready,
- the prototype is not a conformance suite,
- the prototype is not legal, compliance, audit, certification, or conformity evidence,
- the first version may use static examples,
- future runnable code is optional, and
- validation should be introduced before executable behavior is treated as meaningful.

## Static fixture sequence

If static fixtures are added later, a safe sequence is:

1. action request fixture,
2. authorization decision fixture,
3. dispatch decision fixture,
4. backend verification fixture,
5. permitted execution evidence fixture,
6. non-execution evidence fixture,
7. reconstruction notes or expected correlation paths,
8. local validation script.

This sequence preserves reviewability before adding executable behavior.

## Validation planning

Validation should be introduced before any prototype is treated as reliable.

Candidate validation checks may include:

- JSON syntax validation,
- required field presence,
- correlation identifier consistency,
- action identifier consistency,
- authorization decision reference consistency,
- permitted-path consistency,
- non-execution-path consistency,
- no model-output-as-authority pattern,
- no production-readiness claim,
- no conformance claim, and
- no compliance or audit-sufficiency claim.

Validation should support learning and review. It should not imply production assurance.

## Maintenance considerations

Before adding executable prototype code, the project should consider:

- maintenance burden,
- dependency management,
- security expectations,
- compatibility expectations,
- whether the prototype should remain SDK-neutral,
- whether implementation examples should live in this repository or a separate repository,
- whether tests are required for all prototype behavior,
- whether generated outputs should be committed,
- how to avoid stale examples, and
- how to preserve claim boundaries.

## Explicit exclusions

This planning document does not add:

- executable prototype code,
- production service code,
- SDK-specific implementation,
- cloud-specific implementation,
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

After this planning artifact is reviewed, add a minimal non-executable `examples/prototype/README.md`.

That README should establish the prototype directory boundary before any fixtures, validators, or executable prototype code are introduced.

The next PR should remain narrow and should preserve claim boundaries.
