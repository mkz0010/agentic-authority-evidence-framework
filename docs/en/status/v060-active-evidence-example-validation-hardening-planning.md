# v0.6.x Active Evidence Example Validation Hardening Planning

## Status

This is a v0.6.x deferred hardening planning artifact for active evidence example validation.

This document is:

- a planning artifact for #290;
- a validation-hardening scope definition for active evidence example candidates;
- a bridge from JSON syntax validation toward stronger example hygiene checks;
- non-normative unless a later release explicitly promotes requirements into active schema, control, assessment, or testing artifacts.

This document is not:

- an active evidence schema update;
- a conformance test suite;
- an implementation certification mechanism;
- an audit sufficiency claim;
- a compliance claim;
- a production-readiness claim;
- a complete validation implementation;
- a change to the current AAEF control and assessment baseline.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

PR #289 added active evidence example candidates under `examples/evidence/` and introduced JSON syntax validation.

#290 exists because JSON syntax validation alone is not enough to protect the long-term usefulness of active evidence examples.

This planning artifact defines the next validation-hardening layers before modifying validators or treating example files as stronger than illustrative candidates.

The intended outcome is a durable, reviewable path for hardening example validation without accidentally implying:

- schema conformance;
- implementation conformance;
- production readiness;
- audit sufficiency;
- regulatory compliance;
- external framework equivalence;
- evidence sufficiency in real deployments.

## Source context

The current active evidence example candidates are expected to be illustrative and reviewable examples for:

- permitted action evidence;
- non-execution evidence.

Existing validation is expected to confirm that example files are valid JSON.

Future validation may check additional structure and consistency, but those checks should remain conservative unless the active evidence schema is explicitly updated.

## Validation hardening layers

The following layers are candidate hardening targets.

| Layer | Candidate purpose | Current posture | Future validation direction |
| --- | --- | --- | --- |
| JSON syntax validation | Ensure examples are parseable JSON. | Already introduced for active evidence examples. | Preserve as the minimum validation layer. |
| Required top-level field validation | Ensure each example contains expected major sections. | Candidate hardening. | Validate presence of required illustrative sections without claiming schema conformance. |
| Scenario-type validation | Ensure permitted and non-execution examples identify their scenario type. | Candidate hardening. | Validate controlled scenario labels for examples. |
| Cross-reference validation | Ensure related identifiers are internally consistent within each example. | Candidate hardening. | Validate internal correlation fields such as action request, authorization decision, dispatch decision, and evidence event references where present. |
| Controlled vocabulary validation | Reduce drift in example status, outcome, and claim-boundary terms. | Candidate hardening. | Validate a small controlled vocabulary for example metadata and scenario outcomes. |
| Claim-boundary metadata validation | Ensure examples state what they do and do not imply. | Candidate hardening. | Require explicit non-conformance and non-production claim-boundary fields or README coverage. |
| Version and freshness validation | Keep examples aligned with current public release/baseline language. | Candidate hardening. | Validate known release/baseline strings or require explicit review markers where appropriate. |
| README coverage validation | Ensure the examples directory documents scope and limitations. | Candidate hardening. | Validate that `examples/evidence/README.md` exists and contains required boundary language. |

## Candidate required checks

A future validator update may check the following.

### Directory and file presence

Candidate checks:

- `examples/evidence/README.md` exists.
- At least one permitted-action example exists.
- At least one non-execution example exists.
- Example files use `.example.json` naming.
- Example files are valid JSON.

These checks help keep examples discoverable and parseable. They do not prove evidence sufficiency.

### Example metadata

Candidate checks:

- example status is explicitly illustrative or candidate-oriented;
- example scenario type is present;
- example is marked non-normative or non-conformance-oriented;
- example does not claim production readiness;
- example does not claim audit sufficiency;
- example does not claim compliance or certification;
- example does not claim external framework equivalence.

These checks help reduce accidental overclaiming.

### Internal reference consistency

Candidate checks:

- action request identifiers, if present, are consistently reused;
- authorization decision identifiers, if present, are consistently reused;
- dispatch decision identifiers, if present, are consistently reused;
- backend verification identifiers, if present, are consistently reused;
- evidence event identifiers, if present, are consistently reused;
- non-execution examples do not imply backend execution when dispatch denial is the intended outcome.

These checks improve reconstruction quality without claiming that the example is complete evidence.

### Scenario outcome consistency

Candidate checks:

- permitted-action examples should represent execution only when dispatch and backend verification are consistent with execution;
- non-execution examples should represent denied, blocked, expired, mismatched, or otherwise non-executed outcomes;
- non-execution examples should include a reviewable reason or failure point;
- denied examples should not simultaneously claim successful execution unless the scenario explicitly describes partial or failed execution.

These checks help reviewers interpret example intent.

### Claim-boundary terms

Candidate forbidden or suspicious phrases may include:

- production-ready;
- certified;
- compliant;
- audit sufficient;
- legally sufficient;
- equivalent to;
- guarantees;
- proves safety;
- conforms to;
- validated implementation.

The validator should avoid overreach. It can flag these terms in example metadata or README files, but human review remains necessary for full claim-boundary assessment.

## Candidate validator design

The future validator should remain small and transparent.

Recommended design:

- implement as `tools/validate_evidence_examples.py` or extend `tools/validate_json_examples.py` only if the resulting behavior remains clear;
- prefer deterministic local checks;
- produce actionable error messages;
- validate current examples before expanding example count;
- avoid network access;
- avoid dependency-heavy validation unless needed;
- avoid claiming JSON Schema conformance unless a schema is explicitly introduced and maintained;
- distinguish syntax validation from semantic hygiene validation.

## Candidate implementation sequence

Recommended sequence for #290:

1. Add this planning artifact.
2. Inspect current `examples/evidence/` structure and example fields.
3. Add a dedicated evidence example validator or extend the current JSON example validator with explicit evidence-example mode.
4. Add positive validation for current examples.
5. Add at least one local negative smoke test during development.
6. Add validator invocation to the existing artifact validation workflow only after local behavior is stable.
7. Update `examples/evidence/README.md` with validator instructions and claim boundaries.
8. Close #290 only after validation hardening is implemented or explicitly deferred into narrower follow-ups.

## Non-goals

This hardening track does not:

- define a final active evidence schema;
- update the active evidence schema;
- require all evidence examples to be complete operational evidence;
- certify implementations;
- prove production readiness;
- prove audit sufficiency;
- assert legal or regulatory compliance;
- assert external framework equivalence;
- replace human review of evidence examples;
- replace future schema validation if a schema is later promoted.

## Acceptance criteria for this planning artifact

This planning artifact is complete when:

- validation hardening layers are listed;
- candidate checks are separated from current validation behavior;
- claim boundaries are explicit;
- implementation sequence is documented;
- active baseline impact is explicitly excluded.

## Recommended next step for #290

After this planning artifact, the recommended next step is to implement a small dedicated evidence example validator that checks:

- file presence and naming;
- valid JSON;
- required illustrative metadata;
- scenario type;
- basic internal identifier consistency;
- forbidden overclaiming terms;
- README claim-boundary coverage.

The validator should be described as example hygiene validation, not as implementation conformance or evidence sufficiency validation.
