# v0.6.x External Framework Mapping Coverage Expansion Planning

## Status

This is a v0.6.x deferred expansion planning artifact for conservative external framework mapping coverage.

This document is:

- a planning artifact for #293;
- a scope definition for future conservative mapping coverage expansion;
- a bridge from the existing conservative mapping pilot toward additional carefully reviewed mapping rows;
- non-normative unless a later release explicitly promotes requirements into active schema, control, assessment, or testing artifacts.

This document is not:

- a completed external framework mapping;
- a compliance crosswalk;
- a conformity assessment;
- a certification mapping;
- an audit sufficiency mapping;
- a legal sufficiency mapping;
- an equivalence claim with any external framework;
- a change to the current AAEF control and assessment baseline.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

#293 exists to expand the conservative external framework mapping coverage after the pilot mapping structure and validation were introduced.

The purpose of this document is to prevent mapping expansion from turning into unsupported compliance, certification, conformity, audit sufficiency, or equivalence claims.

Future mapping work should remain informative and conservative.

## Source context

Current relevant artifacts include:

- `docs/en/status/v060-conservative-external-framework-mapping-enrichment-planning.md`
- `mappings/README.md`
- `mappings/external-framework-mapping.example.csv`
- `tools/validate_external_mappings.py`

The existing mapping pilot established a conservative pattern for informative relationship mapping. This planning artifact defines how to expand coverage without weakening claim boundaries.

## Mapping expansion principles

Future mapping expansion should follow these principles.

| Principle | Requirement |
| --- | --- |
| Informative only | Mapping rows describe relationship candidates, not compliance status. |
| Non-equivalence | No row should imply that AAEF is equivalent to an external framework, standard, law, or certification scheme. |
| Source traceability | Each row should identify the external source area, framework name, version or publication marker where known, and review status. |
| Relationship clarity | Each row should use conservative relationship vocabulary such as supports, informs, complements, or relates to. |
| Claim boundary | Each row should preserve non-compliance, non-certification, non-audit-sufficiency, non-conformity, and non-equivalence boundaries. |
| Reviewability | Mapping rows should be small enough to review individually. |
| Validator coverage | New rows should pass external mapping validation before merge. |

## Candidate expansion dimensions

Future mapping rows may be expanded along the following dimensions.

| Dimension | Candidate expansion direction | Boundary |
| --- | --- | --- |
| External framework area | Add narrowly selected source areas relevant to AI governance, AI security, authorization, logging, auditability, or assurance. | Do not imply broad coverage of the external framework. |
| AAEF concept | Relate external source areas to specific AAEF concepts such as authority separation, evidence, non-execution, backend verification, or claim boundaries. | Do not imply AAEF satisfies the external source requirement. |
| Relationship type | Use conservative terms such as supports, informs, complements, contextualizes, or partially relates to. | Do not use equivalent, compliant, certified, conforms, satisfies, guarantees, or audit sufficient. |
| Confidence level | Use conservative confidence markers based on review maturity. | Do not treat confidence as validation or compliance. |
| Review status | Mark rows as candidate, reviewed-draft, or deferred-review depending on maturity. | Do not imply completion unless independently reviewed. |
| Limitation note | Add explicit limitation language for each row. | Do not omit limitation language for convenience. |

## Candidate relationship vocabulary

Preferred relationship terms:

- relates to
- may support
- may inform
- may complement
- provides context for
- partially overlaps with
- can help structure review of
- can be considered alongside

Terms to avoid unless independently justified and reviewed:

- complies with
- satisfies
- certifies
- conforms to
- equivalent to
- guarantees
- proves
- validates
- audit sufficient
- legally sufficient
- production-ready

## Candidate coverage targets

The next mapping expansion should be intentionally small.

Recommended first expansion target:

- add a small number of rows that cover the strongest AAEF relationship areas;
- prioritize rows that are easy to review and clearly non-equivalent;
- avoid broad external-framework coverage claims;
- preserve the pilot mapping structure;
- keep validation deterministic.

Candidate AAEF relationship areas:

| AAEF relationship area | Reason for possible mapping |
| --- | --- |
| Model output is not authority | Central AAEF claim boundary and action-assurance premise. |
| Authorization decision separation | Connects action request, policy decision, dispatch, and backend verification. |
| Action-bound evidence | Supports reconstruction and review of agentic actions. |
| Non-execution evidence | Makes blocked, denied, expired, or non-invoked outcomes reviewable. |
| Conservative external mapping discipline | Prevents unsupported compliance, conformity, or equivalence claims. |

## Candidate row review checklist

Before adding or merging a mapping row, review whether:

- the external source area is named conservatively;
- the row does not claim compliance;
- the row does not claim certification;
- the row does not claim conformity;
- the row does not claim audit sufficiency;
- the row does not claim legal sufficiency;
- the row does not claim external-framework equivalence;
- the row does not overstate coverage;
- the row includes limitation language;
- the row uses allowed relationship vocabulary;
- the row is within current validation rules;
- the row remains informative and non-normative.

## Candidate validator expectations

The existing external mapping validator should remain the primary guardrail for mapping hygiene.

Future validation may check:

- required conservative columns;
- allowed relationship vocabulary;
- forbidden claim terms;
- non-empty limitation notes;
- recognized review status values;
- confidence markers;
- non-external mapping CSV exclusion behavior;
- legacy mapping behavior preservation where applicable.

Validator updates should not imply that a passing mapping row is correct, complete, compliant, or equivalent. Passing validation should mean only that the row meets repository hygiene and claim-boundary requirements.

## Recommended implementation sequence for #293

Recommended sequence:

1. Add this coverage expansion planning artifact.
2. Review the existing pilot mapping CSV and validator rules.
3. Add a small conservative mapping coverage expansion set.
4. Run `tools/validate_external_mappings.py` locally.
5. Confirm GitHub Actions validation passes.
6. Comment on #293 and #311.
7. Decide whether #293 is complete or whether additional coverage should be split into a later narrower issue.

## Non-goals

This expansion track does not:

- create a complete external mapping catalog;
- create a compliance crosswalk;
- create a certification path;
- create a conformity assessment;
- create a legal or audit sufficiency mapping;
- assert that AAEF satisfies any external framework;
- assert external-framework equivalence;
- change active controls;
- change the evidence schema;
- change assessment artifacts;
- change testing procedures;
- change the current control and assessment baseline.

## Acceptance criteria for this planning artifact

This planning artifact is complete when:

- mapping expansion principles are defined;
- candidate relationship vocabulary is documented;
- candidate coverage targets are listed;
- row-level review expectations are documented;
- validator expectations are documented;
- non-goals and claim boundaries are explicit;
- active baseline impact is explicitly excluded.

## Recommended next step for #293

After this planning artifact, the recommended next step is a small mapping coverage expansion PR that adds a limited number of conservative rows to the existing pilot mapping artifact and validates them with `tools/validate_external_mappings.py`.

The expansion should remain narrow enough to review manually.
