# AAEF v0.6.x Adoption Follow-up Split Planning

Status: Adoption follow-up split planning  
Related roadmap: #241  
Related adoption index: `docs/en/status/v060-adoption-package-index-planning.md`  
Related operator runbook: `docs/en/status/v060-operator-runbook-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document organizes candidate v0.6.x follow-up work after the initial v0.6.0 adoption-oriented planning set.

The purpose is to avoid uncontrolled document expansion by separating:

- planning artifacts that should remain planning material,
- candidates for active examples or fixtures,
- candidates for active assessment or operational guidance,
- candidates for external framework mapping enrichment,
- candidates for README or navigation integration,
- candidates for prototype or reference implementation scoping,
- and candidates for research/related-work development.

This document is planning material. It does not change active controls, schemas, examples, mappings, testing procedures, assessment artifacts, or the current control and assessment baseline.

## Why this split is needed

The v0.6.0 adoption-readiness cycle added a substantial set of role- and use-case-oriented planning artifacts.

Those artifacts improve adoption readiness, but the project now needs controlled follow-up splitting to decide what should happen next.

The key question is no longer only:

> What should be documented?

The key question is now:

> Which planning materials should remain planning aids, which should become active artifacts, and which should become separate follow-up work?

## Current v0.6.0 adoption-oriented materials

| Area | Artifact | Current status |
| --- | --- | --- |
| Adoption direction | `v060-external-review-reassessment-response.md` | Planning / response |
| Implementation bridge | `v060-implementation-reference-pattern-planning.md` | Planning |
| Permitted evidence example | `v060-permitted-action-evidence-example-planning.md` | Planning example |
| Non-execution evidence example | `v060-non-execution-evidence-example-planning.md` | Planning example |
| Auditor evidence request | `v060-auditor-evidence-request-checklist-planning.md` | Planning checklist |
| Consultant discovery | `v060-consultant-discovery-checklist-planning.md` | Planning checklist |
| Adoption navigation | `v060-adoption-package-index-planning.md` | Planning index |
| Operator runbook | `v060-operator-runbook-planning.md` | Planning runbook |
| Risk owner guide | `v060-risk-owner-guide-planning.md` | Planning guide |
| Legal/compliance note | `v060-legal-compliance-applicability-note-planning.md` | Planning note |
| Security architecture profile | `v060-high-impact-production-minimum-architecture-profile-planning.md` | Planning profile |
| Authorization artifact profile | `v060-authorization-decision-artifact-minimal-profile-planning.md` | Planning profile |
| Implementer quick start | `v060-implementer-quick-start-planning.md` | Planning guide |

## Split principles

Follow-up work should follow these principles:

1. Do not promote planning material into active requirements by implication.
2. Keep v0.4.1 as the current control and assessment baseline until explicitly changed.
3. Treat active-example promotion as separate from planning-example publication.
4. Treat external framework mapping as informative unless explicitly scoped otherwise.
5. Avoid certification, compliance, audit sufficiency, conformity, or equivalence claims.
6. Prefer small, reviewable follow-up issues over one broad adoption umbrella.
7. Preserve reader navigation as the number of artifacts grows.
8. Prioritize artifacts that reduce adoption friction for implementers, auditors, operators, consultants, and risk owners.

## Candidate follow-up tracks

| Priority | Track | Purpose |
| --- | --- | --- |
| P0 | Active Example Candidate Review | Decide whether planning examples can become active examples or fixtures. |
| P1 | External Framework Mapping Enrichment Plan | Define conservative mapping enrichment without equivalence claims. |
| P1 | Operator Runbook Review | Decide whether operator planning can later become active operational guidance. |
| P1 | Adoption Navigation Integration | Decide how adoption package navigation should connect to README or document-map entry points. |
| P1 | Risk Owner Adoption Package Refinement | Strengthen executive/risk-owner decision materials. |
| P2 | Prototype / Reference Implementation Scope | Decide whether a minimal prototype belongs in examples or a separate repository. |
| P2 | Research Related-Work Mapping | Prepare academic/research positioning against related work. |

## P0: Active Example Candidate Review

Purpose:

Review whether the permitted-action and non-execution evidence planning examples should later be promoted into active examples, fixtures, or schema-adjacent examples.

Candidate source artifacts:

- `v060-permitted-action-evidence-example-planning.md`
- `v060-non-execution-evidence-example-planning.md`
- `v060-implementation-reference-pattern-planning.md`

Candidate outputs:

- active example candidate review,
- example promotion criteria,
- active example scope decision,
- schema alignment review,
- fixture naming policy,
- validation implications.

Promotion questions:

- Are the examples aligned with the active evidence schema?
- Are fields illustrative or stable enough to become active examples?
- Would promotion imply schema changes?
- Are both permitted and non-execution cases needed?
- Should examples live in `docs/en/status/`, `examples/`, or another active example path?
- Should examples be machine-validated?
- What claim boundaries must remain attached?

Recommended issue title:

`[Follow-up] v0.6.x: Review active evidence example candidates`

Suggested labels:

- `documentation`
- `planning`
- `examples`
- `evidence`
- `v0.6.0`

## P1: External Framework Mapping Enrichment Plan

Purpose:

Define a conservative enrichment plan for external framework mapping without claiming equivalence, compliance, certification, or audit sufficiency.

Candidate source artifacts:

- `v060-external-framework-mapping-csv-enrichment-review.md`
- `v060-legal-compliance-applicability-note-planning.md`
- `v060-version-reference-audit.md`
- `v060-external-review-reassessment-response.md`

Candidate outputs:

- mapping enrichment plan,
- mapping confidence levels,
- mapping limitation language,
- candidate target frameworks,
- CSV field design,
- validation implications.

Candidate mapping targets:

- NIST AI RMF,
- ISO/IEC 42001,
- OWASP Agentic / LLM risk materials,
- CSA AI controls or guidance,
- MITRE ATLAS or related adversarial AI materials.

Recommended issue title:

`[Follow-up] v0.6.x: Define conservative external framework mapping enrichment`

Suggested labels:

- `documentation`
- `planning`
- `mapping`
- `legal`
- `v0.6.0`

## P1: Operator Runbook Review

Purpose:

Review whether the operator runbook planning artifact should remain planning-only or later support active operational guidance.

Candidate source artifact:

- `v060-operator-runbook-planning.md`

Candidate outputs:

- operator runbook review,
- active operational guidance candidate scope,
- operational metric review,
- alert category review,
- freeze/hold review,
- evidence retention and access review.

Promotion questions:

- Which parts are stable enough for active guidance?
- Which parts are organization-specific and should remain illustrative?
- Should daily/weekly/monthly checklists become active guidance?
- Should operational records become a recommended example?
- Should freeze/hold behavior become assessment-related?
- Are SIEM-specific queries out of scope?

Recommended issue title:

`[Follow-up] v0.6.x: Review operator runbook planning for active guidance candidates`

Suggested labels:

- `documentation`
- `planning`
- `operations`
- `evidence`
- `v0.6.0`

## P1: Adoption Navigation Integration

Purpose:

Decide whether the adoption package index should be linked from README, researcher overview, document map, or a short adoption README.

Candidate source artifact:

- `v060-adoption-package-index-planning.md`

Candidate outputs:

- navigation integration review,
- README integration decision,
- short adoption README candidate,
- role-based reading path update,
- document-map entry refinement.

Review questions:

- Should adoption package navigation be visible from top-level README?
- Should the Japanese README mention adoption packages?
- Should the researcher overview mention the adoption package index?
- Should a short non-status adoption guide be created?
- Should the status document remain the only index for now?

Recommended issue title:

`[Follow-up] v0.6.x: Integrate adoption package navigation`

Suggested labels:

- `documentation`
- `planning`
- `readme`
- `v0.6.0`

## P1: Risk Owner Adoption Package Refinement

Purpose:

Strengthen the risk-owner path so managers and executives can make enablement, remediation, exception, or deferral decisions.

Candidate source artifacts:

- `v060-risk-owner-guide-planning.md`
- `v060-consultant-discovery-checklist-planning.md`
- `v060-auditor-evidence-request-checklist-planning.md`
- `v060-adoption-package-index-planning.md`

Candidate outputs:

- risk-owner adoption package review,
- risk decision memo candidate,
- exception handling candidate,
- residual risk register candidate,
- board/executive reporting candidate.

Review questions:

- What should a risk owner decide?
- What evidence should support the decision?
- What residual risk should be recorded?
- What exceptions should be time-bounded?
- What should be escalated to executives?
- What should remain consultant/advisor guidance?

Recommended issue title:

`[Follow-up] v0.6.x: Refine risk-owner adoption package`

Suggested labels:

- `documentation`
- `planning`
- `risk`
- `governance`
- `v0.6.0`

## P2: Prototype / Reference Implementation Scope

Purpose:

Decide whether AAEF should include or link to a minimal reference implementation or prototype.

Candidate source artifacts:

- `v060-implementation-reference-pattern-planning.md`
- `v060-authorization-decision-artifact-minimal-profile-planning.md`
- `v060-permitted-action-evidence-example-planning.md`
- `v060-non-execution-evidence-example-planning.md`

Candidate outputs:

- prototype scope decision,
- repository placement decision,
- minimal components list,
- non-goals,
- validation approach,
- claim-boundary statement.

Review questions:

- Should prototype work live in this repository or a separate repository?
- Should it be SDK-neutral or target one stack?
- Should it include mock authorization and dispatcher components?
- Should it include generated evidence examples?
- Should it be explicitly non-production?
- What maintenance burden is acceptable?

Recommended issue title:

`[Follow-up] v0.6.x: Define prototype and reference implementation scope`

Suggested labels:

- `documentation`
- `planning`
- `implementation`
- `examples`
- `v0.6.0`

## P2: Research Related-Work Mapping

Purpose:

Prepare AAEF for research review, workshop submission, academic presentation, or related-work analysis.

Candidate source artifacts:

- `v060-research-positioning-review.md`
- `v060-external-review-reassessment-response.md`
- `v060-version-reference-audit.md`
- `v060-implementation-reference-pattern-planning.md`

Candidate outputs:

- related-work mapping plan,
- candidate contribution matrix,
- evaluation design options,
- research abstract refinement,
- research claim-boundary note.

Review questions:

- What research communities are most relevant?
- Which existing work overlaps with AAEF?
- What is AAEF's unique claim?
- What can be evaluated empirically?
- What remains conceptual or design-oriented?
- What should not be claimed before peer review?

Recommended issue title:

`[Follow-up] v0.6.x: Prepare research related-work mapping`

Suggested labels:

- `documentation`
- `planning`
- `research`
- `v0.6.0`

## Recommended issue split order

Recommended order:

1. Active Example Candidate Review
2. External Framework Mapping Enrichment Plan
3. Adoption Navigation Integration
4. Operator Runbook Review
5. Risk Owner Adoption Package Refinement
6. Prototype / Reference Implementation Scope
7. Research Related-Work Mapping

Rationale:

- Active examples are the closest bridge from planning material to reusable artifacts.
- External mapping supports enterprise adoption but requires conservative wording.
- Navigation integration reduces friction before more artifacts are added.
- Operator and risk-owner refinement can follow after the index and current planning materials settle.
- Prototype and research mapping are valuable but can wait until artifact boundaries are clearer.

## Recommended immediate next issue

The immediate next issue should be:

> `[Follow-up] v0.6.x: Review active evidence example candidates`

Reason:

The project now has paired permitted-action and non-execution planning examples. Reviewing whether they can become active examples is the most concrete next step toward implementer and auditor usability.

## Work that should remain explicitly out of scope for v0.6.x unless separately approved

The following should not be done accidentally:

- changing the current control and assessment baseline,
- updating the active evidence schema,
- claiming production readiness,
- claiming certification,
- claiming compliance,
- claiming audit sufficiency,
- claiming external framework equivalence,
- adding SDK-specific production code,
- turning all planning documents into active requirements,
- or closing the roadmap issue solely because planning artifacts exist.

## Suggested issue template text

Future follow-up issues should include:

- purpose,
- source artifacts,
- candidate output,
- non-goals,
- claim boundaries,
- validation expectations,
- expected impact,
- and promotion boundary.

## Relationship to roadmap issue #241

Roadmap issue #241 can remain the coordination point until child follow-up issues are created.

After child issues are created, #241 can track:

- which follow-ups were split,
- which are completed,
- which remain deferred,
- and whether any active artifact promotion is proposed.

## Non-goals

This document does not:

- create follow-up issues by itself,
- close roadmap issue #241,
- change active controls,
- change the current control and assessment baseline,
- update schemas, examples, mappings, CSVs, or testing procedures,
- promote v0.5.0 or v0.6.0 planning material into active requirements,
- assert audit sufficiency,
- claim compliance,
- claim certification,
- claim conformity,
- claim equivalence with external frameworks,
- assert production readiness,
- or require all listed follow-ups to be performed.

## Acceptance criteria

This planning document is sufficient when:

- current adoption-oriented planning artifacts are inventoried,
- follow-up tracks are separated,
- priorities are assigned,
- candidate issue titles are proposed,
- non-goals and claim boundaries are preserved,
- recommended issue split order is documented,
- and no active baseline change is implied.
