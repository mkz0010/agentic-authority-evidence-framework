# v0.6.x Prototype Fixture Validation Planning

This document defines conservative validation planning for future AAEF prototype static fixtures.

It is a planning artifact for #285. It does not add fixture JSON files, validation tools, executable prototype code, implementation conformance criteria, or production readiness claims.

## Status

Planning artifact.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

The v0.6.0 and v0.6.x adoption materials remain non-normative unless explicitly promoted into active guidance or active examples.

## Purpose

The purpose of this planning document is to define what a future prototype fixture validator should check before static fixtures are treated as meaningful examples.

This document follows:

- `docs/en/status/v060-prototype-reference-implementation-scope-planning.md`
- `docs/en/status/v060-prototype-placement-and-file-inventory-planning.md`
- `examples/prototype/README.md`
- `docs/en/status/v060-prototype-static-fixture-planning.md`

It narrows the next step from static fixture planning to validation boundaries.

## Validation principles

Future prototype fixture validation should be:

- local,
- deterministic,
- dependency-light,
- easy to run in CI,
- explicit about required files,
- explicit about correlation expectations,
- conservative about claims,
- separate from production assurance, and
- limited to repository examples unless explicitly expanded.

Validation should support reviewability. It should not imply production readiness, implementation conformance, audit sufficiency, legal sufficiency, compliance sufficiency, certification, conformity, or equivalence with external frameworks.

## Candidate validation target

A future validator may apply to:

- `examples/prototype/fixtures/permitted/`
- `examples/prototype/fixtures/non-execution/`

The first validation scope should remain narrow and should not attempt to validate a complete runtime system.

## Candidate required files

A future minimal validation pass may require the following files for each path.

### Permitted path

Candidate files:

- `examples/prototype/fixtures/permitted/action-request.example.json`
- `examples/prototype/fixtures/permitted/authorization-decision.example.json`
- `examples/prototype/fixtures/permitted/dispatch-decision.example.json`
- `examples/prototype/fixtures/permitted/backend-verification.example.json`
- `examples/prototype/fixtures/permitted/evidence-event.example.json`
- `examples/prototype/fixtures/permitted/reconstruction-notes.example.json`

### Non-execution path

Candidate files:

- `examples/prototype/fixtures/non-execution/action-request.example.json`
- `examples/prototype/fixtures/non-execution/authorization-decision.example.json`
- `examples/prototype/fixtures/non-execution/dispatch-decision.example.json`
- `examples/prototype/fixtures/non-execution/backend-verification.example.json`
- `examples/prototype/fixtures/non-execution/evidence-event.example.json`
- `examples/prototype/fixtures/non-execution/reconstruction-notes.example.json`

These filenames are candidates. A later PR may reduce or rename them before fixtures are added.

## JSON syntax checks

The validator should check that each fixture file is valid JSON.

This check should fail if:

- a fixture is missing,
- a fixture is not valid JSON,
- a fixture is not a JSON object where an object is expected, or
- a fixture contains ambiguous placeholder content that prevents review.

## Required field checks

A future validator may check for fields such as:

- `action_request_id`,
- `authorization_decision_id`,
- `dispatch_decision_id`,
- `backend_verification_id`,
- `evidence_event_id`,
- `correlation_id`,
- `action_type`,
- `outcome`,
- `policy_version`, and
- `reason`.

The exact field set should be decided when fixture JSON files are introduced.

Required fields should remain minimal. The purpose is reviewability, not schema replacement.

## Correlation consistency checks

A future validator should check that records can be correlated across the path.

Candidate checks:

- the same `correlation_id` appears across related files,
- the action request referenced by downstream records exists,
- the authorization decision referenced by dispatch exists,
- the dispatch decision referenced by backend verification exists where applicable,
- the evidence event references the relevant action, decision, and outcome records, and
- reconstruction notes reference the same correlation path.

Correlation checks should make it difficult for fixture examples to imply that uncorrelated model narrative is sufficient evidence.

## Permitted path consistency checks

The permitted path should show that execution proceeds only when required authority and enforcement conditions are satisfied.

Candidate checks:

- action request outcome expectation is permitted or executable,
- authorization decision outcome allows the requested action,
- authorization decision action type matches the requested action type,
- dispatch decision allows forwarding or execution,
- backend verification accepts the authority context where applicable,
- evidence event records execution or permitted outcome, and
- reconstruction notes describe the permitted path.

The validator should reject examples that imply model output alone authorized the action.

## Non-execution path consistency checks

The non-execution path should show fail-closed behavior.

Candidate checks:

- action request is not executed,
- dispatch or backend verification denies or refuses execution,
- evidence event records non-execution,
- non-execution reason is present,
- the reason is clear and reviewable, and
- reconstruction notes describe why execution did not occur.

The first validator should support a simple non-execution reason rather than trying to validate every failure mode.

## Claim-boundary checks

A future validator or supporting documentation should prevent prototype fixtures from making overclaims.

Candidate checks may flag forbidden phrases or require boundary text in README files.

Examples of claims to avoid:

- production-ready,
- production assurance,
- implementation conformance,
- audit sufficient,
- legally sufficient,
- compliance sufficient,
- certified,
- conformant,
- equivalent to an external framework, and
- complete reference implementation.

Claim-boundary checks should support conservative repository hygiene, not replace human review.

## Relationship to existing validators

The future prototype fixture validator should coexist with existing validation tools.

It should not replace:

- `tools/validate_json_examples.py`
- `tools/validate_external_mappings.py`
- `tools/validate_markdown_indexes.py`

A later PR may decide whether prototype fixtures are covered by the existing JSON validation tool or by a new dedicated tool such as `tools/validate_prototype_examples.py`.

## CI integration planning

A future validator may be added to the artifact validation workflow after it is stable.

Candidate CI sequence:

1. validate Markdown indexes,
2. validate general JSON examples,
3. validate external mappings,
4. validate prototype examples.

CI integration should not be added before the validator behavior is clear enough to avoid noisy failures.

## Sequencing recommendation

Recommended sequence:

1. finalize this validation planning artifact,
2. add minimal static fixtures,
3. add a dedicated validator or extend the existing JSON validator,
4. add CI integration after local validation behavior is stable,
5. only then consider narrow executable prototype behavior.

This keeps fixture content, validation expectations, and executable behavior separated.

## Explicit exclusions

This planning document does not add:

- fixture JSON files,
- validators,
- CI workflow changes,
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

After this planning artifact is reviewed, the next PR may add minimal static fixtures for one permitted path and one non-execution path.

If fixtures are added before a validator, the fixture README should clearly state that the fixtures are illustrative and not yet validation-backed.

If validation is added first, the validator should use small placeholder-aware checks that do not require production-grade schema completeness.
