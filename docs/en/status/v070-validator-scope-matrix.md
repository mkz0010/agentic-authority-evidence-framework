# v0.7.0 Validator Scope Matrix

## Status

This is a v0.7.0 planning artifact for Implementation Reviewability.

This document is:

- a planning artifact for #320;
- a follow-up to the v0.7.0 Implementation Reviewability Planning artifact;
- a follow-up to the v0.7.0 Implementation Review Checklist artifact;
- a follow-up to the v0.7.0 Prototype and Reference Boundary Note artifact;
- a follow-up to the v0.7.0 Implementation Assumption Inventory artifact;
- a validator scope matrix for repository validation scripts and workflow usage;
- non-normative unless a later release explicitly promotes content into active guidance.

This document is not:

- an implementation specification;
- a reference implementation;
- production service code;
- executable prototype code;
- a conformance test suite;
- an implementation conformance claim;
- a production-readiness claim;
- a certification scheme;
- a compliance claim;
- a conformity claim;
- an audit sufficiency claim;
- a legal sufficiency claim;
- an external framework equivalence claim;
- a change to the current AAEF control and assessment baseline.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

The purpose of this document is to define a conservative matrix for validator scope.

The central question is:

> What does each validator check, and what must a passing validator result not be mistaken for?

This matrix separates:

- syntax validation from schema conformance;
- hygiene validation from evidence sufficiency;
- index validation from content correctness;
- mapping guardrails from external framework equivalence;
- fixture validation from executable prototype behavior;
- CI success from certification or production readiness.

## Relationship to v0.7.0 Implementation Reviewability

This artifact follows:

- `docs/en/status/v070-implementation-reviewability-planning.md`
- `docs/en/status/v070-implementation-review-checklist.md`
- `docs/en/status/v070-prototype-reference-boundary-note.md`
- `docs/en/status/v070-implementation-assumption-inventory.md`

It contributes to:

- #317 — v0.7.0 roadmap
- #320 — Implementation Reviewability track

The implementation review checklist defines review questions. The implementation assumption inventory defines assumptions that should be explicit. This matrix defines validator limits so validator success is not overclaimed.

## Validator result posture

A validator may support:

- repository hygiene;
- file registration consistency;
- syntax checks;
- selected structural checks;
- selected identifier consistency checks;
- selected claim-boundary guardrails;
- maintenance confidence.

A validator must not claim:

- implementation conformance;
- production readiness;
- empirical validation;
- runtime safety;
- audit sufficiency;
- legal sufficiency;
- certification;
- compliance;
- conformity;
- external framework equivalence;
- complete external framework coverage;
- complete threat coverage;
- mitigation completeness;
- peer review.

## Current validator matrix

| Validator | Current scope | Passing result may support | Passing result must not claim |
| --- | --- | --- | --- |
| `tools/validate_markdown_indexes.py` | Checks selected Markdown index and document-map registration expectations. | Navigation consistency and discoverability hygiene. | Content correctness, normative completeness, implementation conformance, or production readiness. |
| `tools/validate_json_examples.py` | Checks JSON example parsing and syntax for selected `.json` / `.example.json` files. | JSON syntax validity for examples in scope. | Active evidence schema conformance, evidence sufficiency, runtime behavior, or audit sufficiency. |
| `tools/validate_evidence_examples.py` | Checks selected evidence example hygiene, metadata, identifiers, non-normative status, claim-boundary fields, and suspicious overclaiming phrases. | Evidence example hygiene and conservative claim-boundary maintenance. | Evidence sufficiency, implementation conformance, compliance, certification, audit sufficiency, legal sufficiency, or production readiness. |
| `tools/validate_prototype_examples.py` | Checks selected static prototype fixture shape and internal consistency where present. | Static fixture hygiene and reviewability. | Executable prototype behavior, runtime enforcement, conformance, production readiness, or safety for deployment. |
| `tools/validate_external_mappings.py` | Checks conservative external mapping rows, required fields, review metadata, and claim-boundary language. | Mapping artifact hygiene and overclaiming guardrails. | Compliance, certification, conformity, external framework equivalence, complete coverage, or mitigation completeness. |
| `tools/validate_evidence_schema.py` | Checks evidence schema and related example compatibility where in scope. | Schema file integrity and selected schema/example consistency. | Audit sufficiency, legal sufficiency, implementation conformance, or evidence generated by a deployed system. |
| `tools/validate_control_catalog.py` | Checks control catalog consistency and related documentation expectations where in scope. | Control catalog maintenance hygiene. | Control effectiveness, implementation conformance, compliance, or certification. |
| `tools/validate_testing_procedures.py` | Checks testing procedure documentation consistency where in scope. | Testing procedure artifact maintenance hygiene. | Test execution results, conformance, production readiness, or audit sufficiency. |
| `tools/validate_assessment_profiles.py` | Checks assessment profile mapping consistency where in scope. | Assessment profile artifact consistency. | Assessment correctness, audit opinion, certification, or compliance. |
| `tools/validate_assessment_worksheet.py` | Checks assessment worksheet structure or consistency where in scope. | Worksheet maintainability and selected structure checks. | Audit sufficiency, assessment conclusion correctness, legal sufficiency, or compliance. |
| `.github/workflows/validate-aaef-artifacts.yml` | Runs selected validators in CI. | Repeatable repository validation workflow. | Certification workflow, conformance test suite, production-readiness gate, or legal/audit approval process. |

## Validator scope dimensions

Each validator should be reviewed across the following dimensions.

| Dimension | Review question |
| --- | --- |
| Files in scope | Which files, directories, or patterns are inspected? |
| Checks performed | What exact rules are enforced? |
| Checks not performed | What important checks are intentionally out of scope? |
| Failure meaning | What does a failure mean? |
| Passing meaning | What does success mean narrowly? |
| Forbidden meaning | What must success not be interpreted as? |
| Maintenance risk | What future change could make the validator misleading? |
| Follow-up trigger | When should validator scope be expanded or split? |

## File-scope expectations

Validators should document or make reviewable:

- target file patterns;
- explicit exclusions;
- generated or static artifact assumptions;
- whether the validator is local-only or CI-integrated;
- whether the validator depends on active baseline artifacts;
- whether the validator is intended for examples, mappings, status docs, schemas, controls, assessments, or workflow hygiene.

If a validator's file scope is unclear, reviewers should treat the validator as limited to observed behavior and avoid stronger claims.

## Check-scope expectations

Validators should distinguish:

- syntax checks;
- required field checks;
- controlled vocabulary checks;
- cross-reference checks;
- index registration checks;
- suspicious phrase checks;
- claim-boundary checks;
- schema compatibility checks;
- documentation consistency checks.

A validator should not imply checks it does not perform.

## Failure interpretation

A validator failure may indicate:

- invalid syntax;
- missing required field;
- inconsistent identifier;
- missing index registration;
- unsupported vocabulary;
- suspicious overclaiming phrase;
- missing claim-boundary language;
- changed artifact shape that requires validator update.

A validator failure should not automatically indicate:

- real-world system failure;
- failed compliance;
- failed audit;
- unsafe deployed implementation;
- legal non-sufficiency;
- external framework non-equivalence.

## Passing interpretation

A validator pass may indicate:

- checked files satisfy the validator's current rules;
- selected hygiene expectations are met;
- selected repository consistency checks passed;
- selected claim-boundary language is present;
- selected examples remain parseable and internally reviewable.

A validator pass must not indicate:

- implementation conformance;
- production readiness;
- certification;
- compliance;
- conformity;
- audit sufficiency;
- legal sufficiency;
- empirical validation;
- runtime safety;
- external framework equivalence;
- complete coverage;
- mitigation completeness;
- peer review.

## Validator-by-validator notes

### `validate_markdown_indexes.py`

May support:

- ensuring new status artifacts are discoverable;
- maintaining document-map consistency;
- preventing orphaned planning documents where index rules apply.

Must not claim:

- the indexed content is correct;
- the indexed content is complete;
- the indexed content is normative;
- the repository is implementation-ready.

### `validate_json_examples.py`

May support:

- JSON syntax sanity;
- avoiding broken example files;
- maintaining parseable illustrative examples.

Must not claim:

- schema conformance unless explicitly scoped;
- evidence sufficiency;
- runtime generation correctness;
- deployed system behavior.

### `validate_evidence_examples.py`

May support:

- evidence example hygiene;
- metadata and non-normative marker checks;
- selected identifier consistency;
- selected claim-boundary and overclaiming checks.

Must not claim:

- evidence is sufficient for audit;
- evidence came from an implemented enforcement path;
- examples demonstrate production readiness;
- examples prove legal sufficiency or compliance.

### `validate_prototype_examples.py`

May support:

- static fixture consistency;
- local fixture reviewability;
- distinction between permitted and non-execution fixture examples.

Must not claim:

- executable prototype behavior;
- runtime enforcement;
- safe execution;
- reference implementation readiness;
- production readiness.

### `validate_external_mappings.py`

May support:

- conservative mapping row hygiene;
- required non-assertion language;
- review metadata consistency;
- detection of selected overclaiming patterns.

Must not claim:

- external framework equivalence;
- compliance;
- certification;
- conformity;
- legal sufficiency;
- audit sufficiency;
- complete coverage of any external framework.

### `validate_evidence_schema.py`

May support:

- schema artifact integrity;
- selected compatibility between schema and examples where scoped;
- maintenance confidence around evidence schema files.

Must not claim:

- evidence generated by a real system is sufficient;
- implementation conforms to the schema;
- audit evidence is sufficient;
- legal sufficiency.

### `validate_control_catalog.py`

May support:

- control catalog consistency;
- expected control metadata structure;
- relationship between catalog and documentation where scoped.

Must not claim:

- controls are implemented;
- controls are effective;
- controls satisfy external frameworks;
- compliance, certification, or conformity.

### `validate_testing_procedures.py`

May support:

- testing procedure documentation consistency;
- expected procedure structure;
- maintenance of testing-procedure artifacts.

Must not claim:

- tests have been executed;
- controls passed testing;
- implementation conformance;
- audit sufficiency.

### `validate_assessment_profiles.py`

May support:

- assessment profile mapping consistency;
- selected field and relationship checks.

Must not claim:

- assessment conclusions are correct;
- an audit opinion exists;
- compliance or certification.

### `validate_assessment_worksheet.py`

May support:

- assessment worksheet structure;
- worksheet maintainability;
- selected consistency checks.

Must not claim:

- assessment results are correct;
- evidence is sufficient;
- audit sufficiency;
- legal sufficiency.

### GitHub Actions validation workflow

May support:

- repeatable execution of selected validators;
- pull request hygiene;
- repository consistency checks before merge.

Must not claim:

- CI is a certification process;
- CI is a conformance test suite;
- CI proves production readiness;
- CI proves implementation safety;
- CI proves external framework equivalence.

## Validator expansion rules

Future validator expansion should follow these rules.

| Expansion type | Required boundary |
| --- | --- |
| Add new files to validator scope | Document file scope and expected checks. |
| Add stronger structural checks | Document what new checks mean and what they do not mean. |
| Add schema validation | Separate schema compatibility from implementation conformance. |
| Add cross-reference checks | Separate identifier consistency from runtime evidence sufficiency. |
| Add CI workflow step | Preserve CI as repository validation, not certification. |
| Add conformance-like checks | Split into a separate issue and explicitly define claim boundaries before implementation. |

## Validator review checklist

Before merging validator-related work, reviewers should ask:

- Which files are in scope?
- Which checks are performed?
- Which checks are explicitly out of scope?
- What does failure mean?
- What does success mean?
- What must success not be interpreted as?
- Is the validator local-only or CI-integrated?
- Does the PR body preserve claim boundaries?
- Does the merge description preserve claim boundaries?
- Is future stronger work split into a narrower follow-up issue?

## Relationship to #320 acceptance criteria

This artifact supports #320 acceptance criteria as follows.

| #320 acceptance criterion | Support from this artifact |
| --- | --- |
| Implementation reviewability scope is documented. | Defines validator scope as a reviewability support mechanism. |
| Prototype/reference boundaries are preserved. | Distinguishes fixture/prototype validation from executable behavior and production readiness. |
| Assumptions and non-goals are clearly separated. | Passing and failing results are separated from forbidden interpretations. |
| Claim boundaries are preserved. | Each validator includes must-not-claim boundaries. |
| Implementation-producing work is split into narrower follow-up issues. | Validator expansion rules require separate scoping for stronger or conformance-like checks. |

## Candidate future follow-ups

Recommended follow-up artifacts for #320:

| Candidate follow-up | Purpose |
| --- | --- |
| Component responsibility review | Review model, runtime, dispatcher, backend, evidence, and reviewer responsibilities. |
| Fixture-to-prototype transition plan | Define what would be required before static fixtures become executable prototype material. |
| Implementation review record template | Turn checklist, assumptions, and validator scope into a concise PR review template. |
| Validator hardening follow-up | Add scoped validator checks only when claim boundaries are explicit. |

## Non-goals

This validator scope matrix does not:

- add validator code;
- add implementation code;
- add production service code;
- add executable prototype code;
- add scenario fixtures;
- add JSON examples;
- update active controls;
- update the evidence schema;
- update assessment artifacts;
- update testing procedures;
- create a conformance test suite;
- claim implementation conformance;
- claim production readiness;
- claim empirical validation;
- claim certification;
- claim compliance;
- claim conformity;
- claim audit sufficiency;
- claim legal sufficiency;
- claim external-framework equivalence;
- claim peer review;
- claim complete threat coverage;
- claim mitigation completeness.

## Recommended next step

After this matrix, #320 may continue with a component responsibility review.

If #320 is closed later, future validator hardening should be split into narrower follow-up issues with explicit validator scope and claim boundaries.
