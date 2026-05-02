# AAEF v0.6.0 Version Reference Audit

Status: Post-release reference audit  
Related roadmap: #241  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document audits release, baseline, and planning-material version references after the AAEF v0.6.0 Practical Adoption Readiness Planning Release.

The purpose is to distinguish:

- the latest public review planning release,
- the current control and assessment baseline,
- prior planning releases,
- historical release references,
- non-normative planning material,
- and potentially stale or ambiguous version wording.

This document is an audit and planning artifact. It does not change active controls, schemas, testing procedures, assessment artifacts, mappings, examples, or the current control and assessment baseline.

## Expected version semantics

| Concept | Expected value after v0.6.0 |
| --- | --- |
| Latest public review planning release | AAEF v0.6.0 Practical Adoption Readiness Planning Release |
| Current control and assessment baseline | AAEF v0.4.1 |
| Prior public review planning release | AAEF v0.5.0 |
| v0.5.0 planning material | Historical non-normative planning material unless explicitly incorporated |
| v0.6.0 planning material | Non-normative planning and adoption-readiness material unless explicitly promoted |
| Certification / compliance / audit posture | No certification, compliance, audit opinion, conformity, or equivalence claim |

## Scan method

The audit scanned text-like repository files with the following extensions:

- `.md`
- `.txt`
- `.csv`
- `.json`
- `.yaml`
- `.yml`
- `.cff`
- `.py`

The scan searched for version and status terms such as:

- `v0.4.1`
- `v0.5.0`
- `v0.6.0`
- `latest public review`
- `current control and assessment baseline`
- `current active control and assessment baseline`
- `current public review`
- `planning release`
- `public review draft`
- `public review baseline`
- `non-normative`
- `baseline`

## Scan summary

| Metric | Count |
| --- | ---: |
| Total matched lines | 1038 |
| Expected/reference lines | 573 |
| Review-needed lines | 465 |

## Classification summary

| Classification | Count |
| --- | ---: |
| ambiguous baseline wording | 160 |
| ambiguous or possibly stale latest wording | 1 |
| expected current-baseline reference | 4 |
| expected historical release reference | 13 |
| expected historical release-preparation reference | 22 |
| expected latest-release reference | 2 |
| expected prior-planning-release reference | 2 |
| expected v0.4.1 reference or manual review | 70 |
| expected v0.5.0 planning-material reference | 189 |
| expected v0.6.0 planning-release reference | 54 |
| expected v0.6.0 reference or manual review | 198 |
| expected v0.6.0 release reference | 19 |
| manual review status wording | 244 |
| manual review v0.5.0 reference | 55 |
| needs baseline review | 5 |

## Files with most version/status references

| File | Matched lines |
| --- | ---: |
| `docs/en/document-map.md` | 71 |
| `CHANGELOG.md` | 63 |
| `docs/en/status/v060-release-decision-record.md` | 48 |
| `docs/en/status/v060-release-preparation-planning.md` | 41 |
| `docs/en/34-v050-control-design-options.md` | 39 |
| `docs/en/status/v060-release-readiness-review.md` | 33 |
| `docs/en/53-v050-release-scope-decision.md` | 32 |
| `docs/en/54-v050-release-preparation-checklist.md` | 31 |
| `docs/en/status/v060-release-notes-draft.md` | 30 |
| `docs/en/33-v050-planning-overview.md` | 28 |
| `docs/en/status/v060-planning-input-synthesis.md` | 26 |
| `docs/en/status/README.md` | 23 |
| `docs/en/status/v060-planning-progress-summary.md` | 20 |
| `docs/en/14-evidence-event-schema.md` | 17 |
| `docs/en/status/v060-status-document-inventory-planning.md` | 17 |
| `docs/en/status/v060-status-document-triage-decision-register.md` | 17 |
| `docs/en/status/v060-status-document-triage-planning.md` | 16 |
| `docs/en/status/v060-review-follow-up-summary.md` | 15 |
| `docs/en/38-v050-evidence-schema-field-candidates.md` | 14 |
| `docs/en/55-researcher-overview.md` | 12 |
| `docs/en/release/v0.2.0-preparation-checklist.md` | 12 |
| `docs/en/status/v050x-incorporation-decision-register.md` | 12 |
| `docs/en/37-tamper-evident-evidence-storage.md` | 11 |
| `docs/en/status/v050x-follow-up-status.md` | 11 |
| `README.md` | 11 |
| `docs/en/36-risk-proportional-evidence-profile.md` | 10 |
| `docs/en/07-control-requirements.md` | 9 |
| `docs/en/status/v060-operational-responsibility-matrix-planning.md` | 9 |
| `docs/en/status/v060-research-positioning-review.md` | 9 |
| `docs/en/11-high-impact-action-taxonomy.md` | 8 |
| `docs/en/51-evidence-integrity-levels.md` | 8 |
| `docs/en/status/v060-authorization-decision-artifact-minimal-profile-planning.md` | 8 |
| `docs/en/30-principal-context-degradation.md` | 7 |
| `docs/en/31-cross-agent-cross-domain-authority.md` | 7 |
| `docs/en/32-authority-denial-reauthorization-flow.md` | 7 |
| `docs/en/39-approval-quality-approval-fatigue.md` | 7 |
| `docs/en/40-approval-evidence-examples.md` | 7 |
| `docs/en/43-risk-proportional-evidence-assessment-guidance.md` | 7 |
| `docs/en/release/v0.3.0-preparation-checklist.md` | 7 |
| `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md` | 7 |

## Review-needed candidates

These lines may require cleanup, clarification, or explicit confirmation.

| File | Line | Classification | Text |
| --- | ---: | --- | --- |
| `CHANGELOG.md` | 28 | manual review status wording | - Registered previously missing top-level numbered English documents in `docs/en/document-map.md`, including core framework, assessment, schema reference, non-normative planning, example, and guidance documents. |
| `CHANGELOG.md` | 34 | manual review status wording | - Added non-normative v0.5.x follow-up guidance covering evidence integrity, cross-agent budget propagation, cross-agent delegation, capability-scoped delegation, tamper-evident evidence requirements, principal context degradation testing, ... |
| `CHANGELOG.md` | 68 | needs baseline review | - v0.6.0 does not, by itself, change the current active control and assessment baseline. |
| `CHANGELOG.md` | 81 | manual review status wording | - Added `docs/en/18-implementation-guidance.md` to close the documentation numbering gap and provide non-normative implementation adoption guidance. |
| `CHANGELOG.md` | 92 | manual review status wording | This maintenance release refines the v0.4.0 Public Review Draft based on post-release review work. |
| `CHANGELOG.md` | 96 | manual review status wording | - Updated One-page Overview references from v0.2-specific wording to current public review support artifacts. |
| `CHANGELOG.md` | 106 | ambiguous baseline wording | - Refreshed OWASP Agentic Top 10 mapping for the v0.4.x baseline. |
| `CHANGELOG.md` | 113 | manual review status wording | - This release remains a Public Review Draft. |
| `CHANGELOG.md` | 118 | manual review status wording | ## v0.4.0 Public Review Draft - 2026-04-28 |
| `CHANGELOG.md` | 120 | ambiguous baseline wording | This release expands the v0.3.x public review baseline with enterprise assessment usability guidance for agentic AI action assurance. |
| `CHANGELOG.md` | 138 | manual review status wording | - Updated `CITATION.cff` for the v0.4.0 public review draft. |
| `CHANGELOG.md` | 143 | manual review status wording | - This release remains a public review draft. |
| `CHANGELOG.md` | 150 | manual review status wording | This maintenance release improves repository organization, version reference consistency, and automated validation after the v0.3.0 Public Review Draft. |
| `CHANGELOG.md` | 166 | ambiguous baseline wording | - This release does not change the v0.3.0 Public Review Draft baseline scope. |
| `CHANGELOG.md` | 167 | manual review status wording | - This release remains part of the public review draft series. |
| `CHANGELOG.md` | 170 | manual review status wording | ## v0.3.0 Public Review Draft - 2026-04-27 |
| `CHANGELOG.md` | 172 | ambiguous baseline wording | This release expands the v0.2.x public review baseline with implementation profiles, evidence quality assessment criteria, action sequence monitoring, assessment automation guidance, and infrastructure / SIEM evidence integration patterns. |
| `CHANGELOG.md` | 194 | manual review status wording | - This release remains a public review draft. |
| `CHANGELOG.md` | 196 | ambiguous baseline wording | - v0.2.1 remains available as the prior public review refinement baseline. |
| `CHANGELOG.md` | 231 | ambiguous baseline wording | - v0.2.0 remains available as the prior public review baseline. |
| `CHANGELOG.md` | 233 | manual review status wording | ## v0.2.0 Public Review Draft - 2026-04-26 |
| `CHANGELOG.md` | 249 | manual review status wording | - Updated README repository structure and document status for the v0.2.0 Public Review Draft. |
| `CHANGELOG.md` | 252 | manual review status wording | ## v0.1.5 Public Review Draft |
| `CHANGELOG.md` | 256 | manual review status wording | ## v0.1.4 Public Review Draft |
| `CHANGELOG.md` | 261 | manual review status wording | ## v0.1.3 Public Review Draft |
| `CHANGELOG.md` | 268 | manual review status wording | ## v0.1 Public Review Draft — revised pre-publication package |
| `CHANGELOG.md` | 284 | manual review status wording | ## v0.1 Public Review Draft |
| `CHANGELOG.md` | 286 | manual review status wording | Initial public review draft. |
| `CONTRIBUTING.md` | 3 | manual review status wording | AAEF is currently in **Public Review Draft** status. |
| `docs/en/03-definitions.md` | 93 | manual review v0.5.0 reference | See also: `docs/en/30-principal-context-degradation.md` for the v0.5.0 planning concept of Principal Context Degradation. |
| `docs/en/04-threat-model.md` | 104 | manual review v0.5.0 reference | For v0.5.0 planning, see `docs/en/31-cross-agent-cross-domain-authority.md` for the Cross-Agent and Cross-Domain Authority concept note. |
| `docs/en/05-trust-model.md` | 86 | manual review v0.5.0 reference | For v0.5.0 planning, AAEF tracks Cross-Agent and Cross-Domain Authority as a concept for verifying identity, authority, delegation constraints, evidence, and revocation semantics across trust boundaries. See `docs/en/31-cross-agent-cross-do... |
| `docs/en/05-trust-model.md` | 97 | manual review v0.5.0 reference | For v0.5.0 planning, AAEF also tracks Principal Context Degradation: cases where principal context is technically present but stale, ambiguous, semantically distant, or no longer sufficient for the requested high-impact action. See `docs/en... |
| `docs/en/07-control-requirements.md` | 113 | manual review v0.5.0 reference | For the related v0.5.0 planning concept, see `docs/en/30-principal-context-degradation.md`. |
| `docs/en/07-control-requirements.md` | 170 | manual review v0.5.0 reference | For the related v0.5.0 planning concept, see `docs/en/31-cross-agent-cross-domain-authority.md`. |
| `docs/en/07-control-requirements.md` | 209 | manual review v0.5.0 reference | For the related v0.5.0 planning concept, see `docs/en/39-approval-quality-approval-fatigue.md`. |
| `docs/en/07-control-requirements.md` | 286 | manual review v0.5.0 reference | For the related v0.5.0 planning concept, see `docs/en/32-authority-denial-reauthorization-flow.md`. |
| `docs/en/07-control-requirements.md` | 413 | manual review v0.5.0 reference | For the related v0.5.0 planning profile, see `docs/en/37-tamper-evident-evidence-storage.md`. |
| `docs/en/07-control-requirements.md` | 428 | manual review status wording | For non-normative examples, see `docs/en/41-non-execution-reauthorization-examples.md`. |
| `docs/en/07-control-requirements.md` | 443 | manual review status wording | For non-normative examples, see `docs/en/41-non-execution-reauthorization-examples.md`. |
| `docs/en/07-control-requirements.md` | 462 | manual review v0.5.0 reference | For the related v0.5.0 planning concept, see `docs/en/39-approval-quality-approval-fatigue.md`. |
| `docs/en/07-control-requirements.md` | 479 | manual review v0.5.0 reference | For the related v0.5.0 planning concept, see `docs/en/39-approval-quality-approval-fatigue.md`. |
| `docs/en/10-maintenance-and-validation.md` | 35 | manual review status wording | AAEF is intended to be a public review draft and, eventually, a practical control profile. |
| `docs/en/11-high-impact-action-taxonomy.md` | 26 | ambiguous baseline wording | - `Recommended Baseline` |
| `docs/en/11-high-impact-action-taxonomy.md` | 40 | ambiguous baseline wording | This taxonomy provides recommended baseline categories for actions that should normally be treated as high-impact by default. |
| `docs/en/11-high-impact-action-taxonomy.md` | 42 | ambiguous baseline wording | Organizations may define additional high-impact actions based on their context, but AAEF recommends treating the categories in this document as a starting baseline. |
| `docs/en/11-high-impact-action-taxonomy.md` | 76 | ambiguous baseline wording | ## Recommended Baseline Categories |
| `docs/en/11-high-impact-action-taxonomy.md` | 349 | manual review v0.5.0 reference | For v0.5.0 planning, see `docs/en/31-cross-agent-cross-domain-authority.md` for the Cross-Agent and Cross-Domain Authority concept note. |
| `docs/en/11-high-impact-action-taxonomy.md` | 406 | ambiguous baseline wording | 2. Does the definition include the recommended AAEF baseline categories? |
| `docs/en/11-high-impact-action-taxonomy.md` | 447 | ambiguous baseline wording | - whether the baseline is too broad or too narrow, |
| `docs/en/13-one-page-overview.md` | 57 | manual review status wording | AAEF also includes current public review support materials: |
| `docs/en/13-one-page-overview.md` | 141 | manual review status wording | Then read the current public review support artifacts: |
| `docs/en/13-one-page-overview.md` | 195 | manual review status wording | These materials remain public review drafts and are not a certification scheme, formal standard, implementation conformance claim, audit opinion, compliance equivalence, or claim of complete mitigation. |
| `docs/en/14-evidence-event-schema.md` | 183 | ambiguous baseline wording | The evidence event schema includes optional sections and objects introduced during earlier public review expansion and retained in the current baseline. |
| `docs/en/14-evidence-event-schema.md` | 260 | manual review v0.5.0 reference | For v0.5.0 planning, see `docs/en/32-authority-denial-reauthorization-flow.md` for denial, deferral, retry, reauthorization, and safe termination evidence considerations. |
| `docs/en/14-evidence-event-schema.md` | 548 | manual review v0.5.0 reference | ## v0.5.0 Planning Notes |
| `docs/en/14-evidence-event-schema.md` | 550 | manual review v0.5.0 reference | For v0.5.0 planning on evidence depth, assurance value, and operational overhead, see `docs/en/36-risk-proportional-evidence-profile.md`. |
| `docs/en/14-evidence-event-schema.md` | 552 | manual review v0.5.0 reference | For v0.5.0 planning on evidence integrity, tamper evidence, and independent verification, see `docs/en/37-tamper-evident-evidence-storage.md`. |
| `docs/en/14-evidence-event-schema.md` | 554 | manual review v0.5.0 reference | For v0.5.0 planning field candidates before changing the schema, see `docs/en/38-v050-evidence-schema-field-candidates.md`. |
| `docs/en/14-evidence-event-schema.md` | 556 | manual review v0.5.0 reference | For v0.5.0 approval evidence examples, see `docs/en/40-approval-evidence-examples.md`. |
| `docs/en/14-evidence-event-schema.md` | 558 | manual review v0.5.0 reference | For v0.5.0 non-execution and reauthorization examples, see `docs/en/41-non-execution-reauthorization-examples.md`. |
| `docs/en/14-evidence-event-schema.md` | 560 | manual review v0.5.0 reference | For v0.5.0 tamper-evident evidence examples, see `docs/en/42-tamper-evident-evidence-examples.md`. |
| `docs/en/14-evidence-event-schema.md` | 562 | manual review v0.5.0 reference | For v0.5.0 risk-proportional evidence assessment guidance, see `docs/en/43-risk-proportional-evidence-assessment-guidance.md`. |
| `docs/en/14-evidence-event-schema.md` | 564 | manual review v0.5.0 reference | For v0.5.0 evidence depth examples, see `docs/en/44-evidence-depth-examples.md`. |
| `docs/en/14-evidence-event-schema.md` | 566 | manual review v0.5.0 reference | For v0.5.0 Principal Context Degradation examples, see `docs/en/45-principal-context-degradation-examples.md`. |
| `docs/en/14-evidence-event-schema.md` | 568 | manual review v0.5.0 reference | For v0.5.0 cross-agent authority examples, see `docs/en/46-cross-agent-authority-examples.md`. |
| `docs/en/14-evidence-event-schema.md` | 570 | manual review v0.5.0 reference | For v0.5.0 approval quality assessment guidance, see `docs/en/47-approval-quality-assessment-guidance.md`. |
| `docs/en/14-evidence-event-schema.md` | 572 | manual review v0.5.0 reference | For v0.5.0 non-execution and reauthorization negative tests, see `docs/en/48-non-execution-reauthorization-negative-tests.md`. |
| `docs/en/14-evidence-event-schema.md` | 574 | manual review v0.5.0 reference | For v0.5.0 tamper-evident evidence negative tests, see `docs/en/49-tamper-evident-evidence-negative-tests.md`. |
| `docs/en/18-implementation-guidance.md` | 3 | manual review status wording | **Status:** Non-normative implementation guidance |
| `docs/en/18-implementation-guidance.md` | 81 | manual review status wording | - treating non-normative planning material as current control requirements. |
| `docs/en/18-implementation-guidance.md` | 99 | manual review v0.5.0 reference | v0.5.0 planning documents remain non-normative unless explicitly incorporated into control, schema, assessment, testing, or release artifacts. |
| `docs/en/18-implementation-guidance.md` | 101 | manual review v0.5.0 reference | This document may help implementers understand the direction of future planning work, but it does not make any v0.5.0 planning concept mandatory. |
| `docs/en/19-open-research-questions.md` | 45 | manual review v0.5.0 reference | ## v0.5.0 Planning Overview |
| `docs/en/19-open-research-questions.md` | 47 | manual review v0.5.0 reference | A v0.5.0 planning overview is maintained in `docs/en/33-v050-planning-overview.md`. |
| `docs/en/19-open-research-questions.md` | 53 | manual review v0.5.0 reference | A v0.5.0 planning concept note is maintained in `docs/en/30-principal-context-degradation.md`. |
| `docs/en/19-open-research-questions.md` | 171 | manual review v0.5.0 reference | A v0.5.0 planning concept note is maintained in `docs/en/31-cross-agent-cross-domain-authority.md`. |
| `docs/en/19-open-research-questions.md` | 230 | manual review v0.5.0 reference | A v0.5.0 planning concept note is maintained in `docs/en/32-authority-denial-reauthorization-flow.md`. |
| `docs/en/24-control-catalog-versioning.md` | 27 | manual review status wording | Unless superseded by a later catalog file, this file remains the source of truth for the current public review control set. |
| `docs/en/24-control-catalog-versioning.md` | 51 | manual review status wording | - `v0.3.0 Public Review Draft` |
| `docs/en/24-control-catalog-versioning.md` | 53 | manual review status wording | - future `v0.4.0 Public Review Draft` |
| `docs/en/24-control-catalog-versioning.md` | 67 | ambiguous baseline wording | The catalog file name should change only when there is a meaningful need to introduce a new catalog baseline or compatibility boundary. |
| `docs/en/27-trusted-control-boundary-integrity.md` | 234 | manual review v0.5.0 reference | For v0.5.0 planning, see `docs/en/32-authority-denial-reauthorization-flow.md` for the Authority Denial and Reauthorization Flow concept note. |
| `docs/en/28-external-framework-mapping-methodology.md` | 145 | ambiguous baseline wording | - a new catalog baseline is introduced, |
| `docs/en/28-external-framework-mapping-methodology.md` | 278 | manual review status wording | AAEF remains a Public Review Draft control profile and assessment aid. External mappings should help readers understand relationships, not claim that AAEF satisfies another framework. |
| `docs/en/29-iso-iec-42001-feasibility.md` | 3 | manual review status wording | Status: Public Review Draft supporting note |
| `docs/en/29-iso-iec-42001-feasibility.md` | 4 | ambiguous baseline wording | AAEF baseline: v0.4.x Public Review |
| `docs/en/29-iso-iec-42001-feasibility.md` | 13 | manual review status wording | AAEF remains a Public Review Draft control profile and assessment aid for agentic action assurance. |
| `docs/en/30-principal-context-degradation.md` | 21 | manual review status wording | That document defines non-normative negative test guidance for stale context, task drift, scope expansion, risk escalation, role or policy changes, revocation, delegation after context degradation, retry pressure, task splitting, and untrus... |
| `docs/en/31-cross-agent-cross-domain-authority.md` | 168 | manual review status wording | Future AAEF work may define a cross-domain authority assertion profile. A non-normative planning profile is maintained in `docs/en/35-authority-assertion-profile.md`. |
| `docs/en/32-authority-denial-reauthorization-flow.md` | 236 | manual review status wording | For non-normative non-execution and reauthorization examples, see `docs/en/41-non-execution-reauthorization-examples.md`. |
| `docs/en/33-v050-planning-overview.md` | 79 | manual review status wording | For the non-normative authority assertion planning profile, see `docs/en/35-authority-assertion-profile.md`. |
| `docs/en/33-v050-planning-overview.md` | 101 | manual review status wording | For the non-normative risk-proportional evidence planning profile, see `docs/en/36-risk-proportional-evidence-profile.md`. |
| `docs/en/33-v050-planning-overview.md` | 283 | manual review status wording | ### Non-Normative Examples |
| `docs/en/33-v050-planning-overview.md` | 297 | manual review status wording | These documents are non-normative planning materials unless otherwise stated. They are intended to support discussion before future schema, control, testing, or assessment changes are adopted. |
| `docs/en/34-v050-control-design-options.md` | 40 | manual review status wording | That document should be used when deciding whether each planning theme remains non-normative guidance, becomes a v0.5.x follow-up item, or is later incorporated into control, evidence, assessment, testing, mapping, or release artifacts. |
| `docs/en/34-v050-control-design-options.md` | 63 | manual review status wording | \| Planning only \| The concept remains design input for future work. \| Keep it marked as non-normative planning material. \| |
| `docs/en/34-v050-control-design-options.md` | 128 | manual review status wording | - remain marked as non-normative planning material; |
| `docs/en/34-v050-control-design-options.md` | 242 | manual review status wording | These considerations remain non-normative until incorporated into control, testing, evidence, assessment, or release artifacts. |
| `docs/en/34-v050-control-design-options.md` | 301 | manual review status wording | Do not add controls yet. First define a non-normative authority assertion profile. A planning profile is maintained in `docs/en/35-authority-assertion-profile.md`. |
| `docs/en/34-v050-control-design-options.md` | 339 | manual review status wording | 3. define a non-normative authority assertion profile; |
| `docs/en/34-v050-control-design-options.md` | 475 | manual review status wording | 3. Define non-normative evidence and authority assertion candidates. |
| `docs/en/35-authority-assertion-profile.md` | 5 | manual review status wording | **Scope:** Non-normative planning profile for cross-agent and cross-domain authority assertions |
| `docs/en/35-authority-assertion-profile.md` | 187 | manual review status wording | For non-normative cross-agent and cross-domain authority examples, see `docs/en/46-cross-agent-authority-examples.md`. |
| `docs/en/36-risk-proportional-evidence-profile.md` | 5 | manual review status wording | **Scope:** Non-normative planning profile for evidence depth, assurance value, and operational overhead |
| `docs/en/36-risk-proportional-evidence-profile.md` | 48 | manual review status wording | These levels are non-normative planning categories. |
| `docs/en/37-tamper-evident-evidence-storage.md` | 5 | manual review status wording | **Scope:** Non-normative planning profile for evidence integrity, tamper evidence, and independent verification |
| `docs/en/37-tamper-evident-evidence-storage.md` | 32 | manual review status wording | That document provides non-normative guidance for selected contexts where tamper-evident evidence may be required, strongly recommended, recommended, optional, or usually unnecessary. |
| `docs/en/37-tamper-evident-evidence-storage.md` | 94 | manual review status wording | These levels are non-normative planning categories. |
| `docs/en/37-tamper-evident-evidence-storage.md` | 323 | manual review status wording | For non-normative tamper-evident evidence examples, see `docs/en/42-tamper-evident-evidence-examples.md`. |
| `docs/en/37-tamper-evident-evidence-storage.md` | 358 | manual review status wording | For non-normative tamper-evident evidence negative tests, see `docs/en/49-tamper-evident-evidence-negative-tests.md`. |
| `docs/en/38-v050-evidence-schema-field-candidates.md` | 5 | manual review status wording | **Scope:** Non-normative field candidate inventory before changing the Evidence Event Schema |
| `docs/en/38-v050-evidence-schema-field-candidates.md` | 281 | manual review status wording | For non-normative assessment guidance on applying evidence depth levels, see `docs/en/43-risk-proportional-evidence-assessment-guidance.md`. |
| `docs/en/38-v050-evidence-schema-field-candidates.md` | 283 | manual review status wording | For non-normative evidence depth examples, see `docs/en/44-evidence-depth-examples.md`. |
| `docs/en/39-approval-quality-approval-fatigue.md` | 5 | manual review status wording | **Scope:** Non-normative planning note for approval quality, approval fatigue, and meaningful human authorization |
| `docs/en/39-approval-quality-approval-fatigue.md` | 181 | manual review status wording | For non-normative approval evidence examples, see `docs/en/40-approval-evidence-examples.md`. |
| `docs/en/39-approval-quality-approval-fatigue.md` | 213 | manual review status wording | For non-normative approval quality assessment guidance, see `docs/en/47-approval-quality-assessment-guidance.md`. |
| `docs/en/40-approval-evidence-examples.md` | 5 | manual review status wording | **Scope:** Non-normative examples for approval quality, approval evidence, and approval laundering review |
| `docs/en/40-approval-evidence-examples.md` | 28 | manual review status wording | That document provides non-normative negative tests and candidate evidence expectations for approval evidence quality. |
| `docs/en/40-approval-evidence-examples.md` | 430 | manual review status wording | For non-normative approval quality assessment guidance, see `docs/en/47-approval-quality-assessment-guidance.md`. |
| `docs/en/41-non-execution-reauthorization-examples.md` | 5 | manual review status wording | **Scope:** Non-normative examples for denial, deferral, safe termination, escalation, freeze, and reauthorization review |
| `docs/en/41-non-execution-reauthorization-examples.md` | 363 | manual review status wording | For non-normative non-execution and reauthorization negative tests, see `docs/en/48-non-execution-reauthorization-negative-tests.md`. |
| `docs/en/42-tamper-evident-evidence-examples.md` | 5 | manual review status wording | **Scope:** Non-normative examples for tamper-evident, independently corroborated, and integrity-verifiable evidence review |
| `docs/en/42-tamper-evident-evidence-examples.md` | 364 | manual review status wording | For non-normative tamper-evident evidence negative tests, see `docs/en/49-tamper-evident-evidence-negative-tests.md`. |
| `docs/en/43-risk-proportional-evidence-assessment-guidance.md` | 5 | manual review status wording | **Scope:** Non-normative assessment guidance for evidence depth, assurance value, and operational overhead |
| `docs/en/43-risk-proportional-evidence-assessment-guidance.md` | 30 | manual review status wording | That document provides non-normative guidance for relating evidence integrity expectations to high-impact and audit-grade assessment contexts. |
| `docs/en/43-risk-proportional-evidence-assessment-guidance.md` | 370 | manual review status wording | For non-normative evidence depth examples, see `docs/en/44-evidence-depth-examples.md`. |
| `docs/en/44-evidence-depth-examples.md` | 5 | manual review status wording | **Scope:** Non-normative examples for E3, E4, and E5 evidence depth assessment |
| `docs/en/45-principal-context-degradation-examples.md` | 5 | manual review status wording | **Scope:** Non-normative examples for principal context freshness, ambiguity, drift, reconfirmation, denial, and reauthorization review |
| `docs/en/45-principal-context-degradation-examples.md` | 32 | manual review status wording | That document extends these examples into non-normative test scenarios and candidate evidence expectations. |
| `docs/en/46-cross-agent-authority-examples.md` | 5 | manual review status wording | **Scope:** Non-normative examples for cross-agent authority, cross-domain authority assertions, delegation lineage, receiving-side validation, and evidence limitations |
| `docs/en/47-approval-quality-assessment-guidance.md` | 5 | manual review status wording | **Scope:** Non-normative assessment guidance for meaningful approval, blind approval, approval fatigue, approval laundering, retry pressure, and task-splitting review |
| `docs/en/47-approval-quality-assessment-guidance.md` | 21 | manual review status wording | That document extends this assessment guidance with non-normative negative tests and candidate evidence expectations. |
| `docs/en/48-non-execution-reauthorization-negative-tests.md` | 5 | manual review status wording | **Scope:** Non-normative negative tests for denial, deferral, freeze, safe termination, retry, task splitting, reauthorization, and non-execution evidence review |
| `docs/en/49-tamper-evident-evidence-negative-tests.md` | 5 | manual review status wording | **Scope:** Non-normative negative tests for evidence tampering, replay, deletion, truncation, reordering, selective omission, integrity verification, and evidence preservation review |
| `docs/en/49-tamper-evident-evidence-negative-tests.md` | 45 | manual review status wording | For non-normative examples, see `docs/en/42-tamper-evident-evidence-examples.md`. |
| `docs/en/51-evidence-integrity-levels.md` | 9 | manual review status wording | This document defines a non-normative planning model for evidence integrity levels in AAEF. |
| `docs/en/51-evidence-integrity-levels.md` | 100 | ambiguous baseline wording | EIL-2 is a practical baseline for many assessed actions because it reduces dependence on agent runtime self-reporting. |
| `docs/en/51-evidence-integrity-levels.md` | 146 | manual review status wording | This table is non-normative. It provides planning guidance only. |
| `docs/en/51-evidence-integrity-levels.md` | 192 | manual review status wording | A future AAEF release may decide that some profiles, actions, or assessment levels require EIL-3 properties. Until then, this document remains non-normative planning guidance. |
| `docs/en/52-approval-quality-model.md` | 9 | manual review status wording | This document defines a non-normative planning model for approval quality and approval fatigue in AAEF. |
| `docs/en/52-approval-quality-model.md` | 23 | manual review status wording | That document defines non-normative negative test guidance and candidate evidence expectations for approval quality, approval fatigue, approval laundering, batch approval, reauthorization, and approval-to-execution binding. |
| `docs/en/53-v050-release-scope-decision.md` | 15 | manual review status wording | - non-normative planning models; |
| `docs/en/53-v050-release-scope-decision.md` | 45 | manual review status wording | \| Principal Context Degradation \| Non-normative planning model \| Existing control refinement, guidance, and testing refinement candidate \| `docs/en/30-principal-context-degradation.md`, `docs/en/50-authority-lifecycle-model.md` \| |
| `docs/en/53-v050-release-scope-decision.md` | 46 | manual review status wording | \| Cross-Agent and Cross-Domain Authority \| Non-normative planning model \| Existing control refinement or new cross-agent control candidate if existing controls cannot express capability-scoped delegation, explicit acceptance/refusal, delega... |
| `docs/en/53-v050-release-scope-decision.md` | 47 | manual review status wording | \| Authority Denial and Reauthorization Flow \| Non-normative planning model \| Testing refinement, evidence refinement, and existing control refinement candidate \| `docs/en/32-authority-denial-reauthorization-flow.md`, `docs/en/50-authority-l... |
| `docs/en/53-v050-release-scope-decision.md` | 48 | manual review status wording | \| Risk-Proportional Evidence and Performance Overhead \| Non-normative planning model \| Guidance, evidence refinement, and assessment profile refinement candidate \| `docs/en/36-risk-proportional-evidence-profile.md`, `docs/en/51-evidence-int... |
| `docs/en/53-v050-release-scope-decision.md` | 49 | manual review status wording | \| Tamper-Evident Evidence Storage \| Non-normative planning model \| Evidence refinement and possible high-impact or audit-grade profile requirement candidate \| `docs/en/37-tamper-evident-evidence-storage.md`, `docs/en/51-evidence-integrity-l... |
| `docs/en/53-v050-release-scope-decision.md` | 50 | manual review status wording | \| Approval Quality and Approval Fatigue \| Non-normative planning model \| Existing HUM control refinement, guidance, testing refinement, or new HUM control candidate \| `docs/en/39-approval-quality-approval-fatigue.md`, `docs/en/52-approval-q... |
| `docs/en/53-v050-release-scope-decision.md` | 99 | manual review status wording | - close as addressed by non-normative planning guidance; |
| `docs/en/54-v050-release-preparation-checklist.md` | 3 | manual review status wording | **Status:** Non-normative release preparation checklist |
| `docs/en/54-v050-release-preparation-checklist.md` | 40 | manual review status wording | \| `docs/en/50-authority-lifecycle-model.md` \| Confirm authority lifecycle model remains non-normative. \| |
| `docs/en/54-v050-release-preparation-checklist.md` | 41 | manual review status wording | \| `docs/en/51-evidence-integrity-levels.md` \| Confirm evidence integrity model remains non-normative. \| |
| `docs/en/54-v050-release-preparation-checklist.md` | 42 | manual review status wording | \| `docs/en/52-approval-quality-model.md` \| Confirm approval quality model remains non-normative. \| |
| `docs/en/54-v050-release-preparation-checklist.md` | 130 | manual review status wording | ### Non-Normative Scope |
| `docs/en/55-researcher-overview.md` | 3 | manual review status wording | **Status:** Non-normative research-facing overview |
| `docs/en/55-researcher-overview.md` | 11 | ambiguous baseline wording | This document does not create new control requirements and does not change the current control and assessment baseline. |
| `docs/en/56-capability-scoped-cross-agent-delegation.md` | 3 | manual review status wording | **Status:** Non-normative v0.5.x follow-up guidance |
| `docs/en/56-capability-scoped-cross-agent-delegation.md` | 7 | manual review status wording | This document defines non-normative guidance for capability-scoped cross-agent delegation in AAEF. |
| `docs/en/56-capability-scoped-cross-agent-delegation.md` | 115 | manual review status wording | The following are non-normative candidate expectations for future control refinement. |
| `docs/en/57-cross-agent-delegation-negative-tests.md` | 3 | manual review status wording | **Status:** Non-normative v0.5.x follow-up testing guidance |
| `docs/en/57-cross-agent-delegation-negative-tests.md` | 7 | manual review status wording | This document defines non-normative negative test guidance for cross-agent delegation acceptance, refusal, chain accountability, and receiving-side authority validation. |
| `docs/en/57-cross-agent-delegation-negative-tests.md` | 80 | manual review status wording | Candidate severity is non-normative. |
| `docs/en/58-cross-agent-budget-propagation.md` | 3 | manual review status wording | **Status:** Non-normative v0.5.x follow-up guidance |
| `docs/en/58-cross-agent-budget-propagation.md` | 7 | manual review status wording | This document defines non-normative guidance for cross-agent budget and resource propagation in AAEF. |
| `docs/en/58-cross-agent-budget-propagation.md` | 146 | manual review status wording | The following are non-normative candidate expectations for future control refinement. |
| `docs/en/59-principal-context-degradation-testing.md` | 3 | manual review status wording | **Status:** Non-normative v0.5.x follow-up testing guidance |
| `docs/en/59-principal-context-degradation-testing.md` | 7 | manual review status wording | This document defines non-normative testing guidance for Principal Context Degradation in AAEF. |
| `docs/en/59-principal-context-degradation-testing.md` | 91 | manual review status wording | Candidate severity is non-normative. |
| `docs/en/60-evidence-integrity-profile-guidance.md` | 3 | manual review status wording | **Status:** Non-normative v0.5.x follow-up guidance |
| `docs/en/60-evidence-integrity-profile-guidance.md` | 7 | manual review status wording | This document defines non-normative guidance for relating Evidence Integrity Levels to high-impact and audit-grade assessment contexts in AAEF. |
| `docs/en/60-evidence-integrity-profile-guidance.md` | 9 | manual review v0.5.0 reference | It addresses follow-up work from the v0.5.0 Evidence Integrity Levels, Risk-Proportional Evidence, and Tamper-Evident Evidence planning material. |
| `docs/en/60-evidence-integrity-profile-guidance.md` | 40 | manual review status wording | The following bands are non-normative planning categories. |
| `docs/en/61-tamper-evident-evidence-requirements.md` | 3 | manual review status wording | **Status:** Non-normative v0.5.x follow-up guidance |
| `docs/en/61-tamper-evident-evidence-requirements.md` | 7 | manual review status wording | This document defines non-normative guidance for deciding when tamper-evident evidence should be required, strongly recommended, recommended, optional, or unnecessary for selected AAEF contexts. |
| `docs/en/61-tamper-evident-evidence-requirements.md` | 9 | manual review v0.5.0 reference | It addresses follow-up work from the v0.5.0 Tamper-Evident Evidence Storage and Evidence Integrity Levels planning material. |
| `docs/en/61-tamper-evident-evidence-requirements.md` | 42 | manual review status wording | The following categories are non-normative planning guidance. |
| `docs/en/62-approval-quality-testing-guidance.md` | 3 | manual review status wording | **Status:** Non-normative v0.5.x follow-up testing and evidence guidance |
| `docs/en/62-approval-quality-testing-guidance.md` | 7 | manual review status wording | This document defines non-normative testing and evidence guidance for Approval Quality and Approval Fatigue in AAEF. |
| `docs/en/62-approval-quality-testing-guidance.md` | 9 | manual review v0.5.0 reference | It addresses follow-up work from the v0.5.0 Approval Quality planning material. |
| `docs/en/62-approval-quality-testing-guidance.md` | 65 | manual review status wording | Candidate severity is non-normative. |
| `docs/en/document-map.md` | 3 | manual review status wording | **Status:** Non-normative navigation and classification aid |
| `docs/en/document-map.md` | 9 | ambiguous baseline wording | It does not move files, change document status, change the current control and assessment baseline, or make planning material normative. |
| `docs/en/document-map.md` | 19 | ambiguous baseline wording | - current baseline or assessment-relevant material; |
| `docs/en/document-map.md` | 22 | manual review status wording | - non-normative planning material; |
| `docs/en/document-map.md` | 23 | manual review status wording | - non-normative follow-up guidance or testing guidance; |
| `docs/en/document-map.md` | 29 | ambiguous baseline wording | The current baseline is determined by the release notes and explicit baseline statements in the repository. |
| `docs/en/document-map.md` | 31 | ambiguous baseline wording | ## Current Baseline and Assessment-Relevant Artifacts |
| `docs/en/document-map.md` | 37 | ambiguous baseline wording | \| `controls/aaef-controls-v0.1.csv` \| Control catalog artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 38 | ambiguous baseline wording | \| `assessment/aaef-assessment-profiles-v0.3-draft.csv` \| Assessment artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 39 | ambiguous baseline wording | \| `assessment/aaef-assessment-worksheet-v0.2-draft.csv` \| Assessment artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 40 | ambiguous baseline wording | \| `assessment/aaef-testing-procedures-v0.4-draft.csv` \| Assessment artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 41 | ambiguous baseline wording | \| `schemas/agentic-action-evidence-event.schema.json` \| Evidence schema artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 42 | ambiguous baseline wording | \| `examples/agentic-action-evidence-event.audit-grade.json` \| Evidence example artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 43 | ambiguous baseline wording | \| `examples/agentic-action-evidence-event.high-impact.json` \| Evidence example artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 44 | ambiguous baseline wording | \| `examples/agentic-action-evidence-event.invalid.json` \| Evidence example artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 45 | ambiguous baseline wording | \| `examples/agentic-action-evidence-event.json` \| Evidence example artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 46 | ambiguous baseline wording | \| `examples/agentic-action-evidence-event.minimal.json` \| Evidence example artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 47 | ambiguous baseline wording | \| `examples/agentic-action-evidence-event.valid.json` \| Evidence example artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 48 | ambiguous baseline wording | \| `mappings/aaef-external-framework-mapping-v0.4-draft.csv` \| External framework mapping artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 49 | ambiguous baseline wording | \| `mappings/threat-control-assurance-mapping-v0.2-draft.csv` \| External framework mapping artifact \| Baseline / assessment-relevant artifact \| |
| `docs/en/document-map.md` | 79 | manual review status wording | They are non-normative unless a later release explicitly incorporates them into control, evidence, assessment, testing, schema, mapping, or release artifacts. |
| `docs/en/document-map.md` | 83 | manual review status wording | \| `docs/en/30-principal-context-degradation.md` \| Principal context degradation concept \| Non-normative planning material \| |
| `docs/en/document-map.md` | 84 | manual review status wording | \| `docs/en/31-cross-agent-cross-domain-authority.md` \| Cross-agent and cross-domain authority planning \| Non-normative planning material \| |
| `docs/en/document-map.md` | 85 | manual review v0.5.0 reference | \| `docs/en/33-v050-planning-overview.md` \| v0.5.0 planning overview \| Non-normative planning material \| |
| `docs/en/document-map.md` | 86 | manual review v0.5.0 reference | \| `docs/en/34-v050-control-design-options.md` \| v0.5.0 control design options and incorporation notes \| Non-normative planning material \| |
| `docs/en/document-map.md` | 87 | manual review status wording | \| `docs/en/36-risk-proportional-evidence-profile.md` \| Risk-proportional evidence planning \| Non-normative planning material \| |
| `docs/en/document-map.md` | 88 | manual review status wording | \| `docs/en/37-tamper-evident-evidence-storage.md` \| Tamper-evident evidence storage planning \| Non-normative planning material \| |
| `docs/en/document-map.md` | 89 | manual review status wording | \| `docs/en/39-approval-quality-approval-fatigue.md` \| Approval quality and approval fatigue planning \| Non-normative planning material \| |
| `docs/en/document-map.md` | 90 | manual review status wording | \| `docs/en/50-authority-lifecycle-model.md` \| Authority Lifecycle Model \| Non-normative planning model \| |
| `docs/en/document-map.md` | 91 | manual review status wording | \| `docs/en/51-evidence-integrity-levels.md` \| Evidence Integrity Levels \| Non-normative planning model \| |
| `docs/en/document-map.md` | 92 | manual review status wording | \| `docs/en/52-approval-quality-model.md` \| Approval Quality Model \| Non-normative planning model \| |
| `docs/en/document-map.md` | 93 | manual review v0.5.0 reference | \| `docs/en/53-v050-release-scope-decision.md` \| v0.5.0 release scope decision \| Release planning / decision record \| |
| `docs/en/document-map.md` | 94 | manual review v0.5.0 reference | \| `docs/en/54-v050-release-preparation-checklist.md` \| v0.5.0 release preparation checklist \| Release planning / validation checklist \| |
| `docs/en/document-map.md` | 98 | manual review v0.5.0 reference | These documents capture the first follow-up guidance or testing pass after v0.5.0. |
| `docs/en/document-map.md` | 104 | manual review status wording | \| `docs/en/56-capability-scoped-cross-agent-delegation.md` \| Capability-scoped cross-agent delegation guidance \| Non-normative follow-up guidance \| |
| `docs/en/document-map.md` | 105 | manual review status wording | \| `docs/en/57-cross-agent-delegation-negative-tests.md` \| Cross-agent delegation negative tests \| Non-normative follow-up testing guidance \| |
| `docs/en/document-map.md` | 106 | manual review status wording | \| `docs/en/58-cross-agent-budget-propagation.md` \| Cross-agent budget propagation guidance \| Non-normative follow-up guidance \| |
| `docs/en/document-map.md` | 107 | manual review status wording | \| `docs/en/59-principal-context-degradation-testing.md` \| Principal context degradation testing guidance \| Non-normative follow-up testing guidance \| |
| `docs/en/document-map.md` | 108 | manual review status wording | \| `docs/en/60-evidence-integrity-profile-guidance.md` \| Evidence integrity profile guidance \| Non-normative follow-up guidance \| |
| `docs/en/document-map.md` | 109 | manual review status wording | \| `docs/en/61-tamper-evident-evidence-requirements.md` \| Tamper-evident evidence requirements guidance \| Non-normative follow-up guidance \| |
| `docs/en/document-map.md` | 110 | manual review status wording | \| `docs/en/62-approval-quality-testing-guidance.md` \| Approval quality testing guidance \| Non-normative follow-up testing and evidence guidance \| |
| `docs/en/document-map.md` | 123 | manual review status wording | \| `docs/en/48-non-execution-reauthorization-negative-tests.md` \| Non-execution and reauthorization negative tests \| Examples / non-normative negative test guidance \| |
| `docs/en/document-map.md` | 124 | manual review status wording | \| `docs/en/49-tamper-evident-evidence-negative-tests.md` \| Tamper-evident evidence negative tests \| Examples / non-normative negative test guidance \| |
| `docs/en/document-map.md` | 192 | ambiguous baseline wording | \| `docs/en/status/v060-release-readiness-review.md` \| v0.6.0 release readiness review \| Defines release-readiness checks, release-blocking decisions, validation commands, claim boundaries, and baseline-change review before any v0.6.0 releas... |
| `docs/en/document-map.md` | 223 | manual review status wording | \| `docs/en/32-authority-denial-reauthorization-flow.md` \| Authority Denial and Reauthorization Flow \| Non-normative planning concept \| |
| `docs/en/document-map.md` | 224 | manual review status wording | \| `docs/en/35-authority-assertion-profile.md` \| Authority Assertion Profile \| Non-normative planning profile \| |
| `docs/en/document-map.md` | 225 | manual review v0.5.0 reference | \| `docs/en/38-v050-evidence-schema-field-candidates.md` \| v0.5.0 Evidence Schema Field Candidates \| Non-normative planning note \| |
| `docs/en/document-map.md` | 226 | manual review status wording | \| `docs/en/41-non-execution-reauthorization-examples.md` \| Non-Execution and Reauthorization Examples \| Non-normative examples \| |
| `docs/en/document-map.md` | 227 | manual review status wording | \| `docs/en/43-risk-proportional-evidence-assessment-guidance.md` \| Risk-Proportional Evidence Assessment Guidance \| Non-normative guidance \| |
| `docs/en/document-map.md` | 228 | manual review status wording | \| `docs/en/47-approval-quality-assessment-guidance.md` \| Approval Quality Assessment Guidance \| Non-normative guidance \| |
| `docs/en/document-map.md` | 242 | ambiguous baseline wording | - change the current baseline; |
| `docs/en/status/README.md` | 3 | manual review status wording | **Status:** Non-normative status and coordination directory |
| `docs/en/status/README.md` | 34 | ambiguous baseline wording | - current baseline artifacts. |
| `docs/en/status/README.md` | 36 | ambiguous baseline wording | ## Baseline Statement |
| `docs/en/status/README.md` | 38 | ambiguous baseline wording | Documents in this directory do not change the current AAEF control and assessment baseline. |
| `docs/en/status/v050x-approval-quality-csv-refinement-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative CSV refinement proposal |
| `docs/en/status/v050x-approval-quality-csv-refinement-proposal.md` | 68 | ambiguous baseline wording | - changing the active baseline before reviewer agreement; |
| `docs/en/status/v050x-approval-quality-testing-candidate-appendix.md` | 3 | manual review status wording | **Status:** Temporary, non-normative testing candidate appendix |
| `docs/en/status/v050x-approval-quality-testing-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative testing proposal review document |
| `docs/en/status/v050x-approval-quality-testing-proposal.md` | 278 | ambiguous baseline wording | \| Option A \| Add these as a separate candidate appendix first. \| Safer, but delays active baseline incorporation. \| |
| `docs/en/status/v050x-cross-agent-delegation-csv-refinement-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative CSV refinement proposal |
| `docs/en/status/v050x-cross-agent-delegation-csv-refinement-proposal.md` | 66 | ambiguous baseline wording | - changing the active baseline before reviewer agreement; |
| `docs/en/status/v050x-cross-agent-delegation-testing-candidate-appendix.md` | 3 | manual review status wording | **Status:** Temporary, non-normative testing candidate appendix |
| `docs/en/status/v050x-cross-agent-delegation-testing-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative testing proposal review document |
| `docs/en/status/v050x-cross-agent-delegation-testing-proposal.md` | 273 | ambiguous baseline wording | \| Option A \| Add these as a separate candidate appendix first. \| Safer, but delays active baseline incorporation. \| |
| `docs/en/status/v050x-evd01-evidence-sufficiency-limitation-review-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative review proposal |
| `docs/en/status/v050x-evd01-evidence-sufficiency-limitation-review-proposal.md` | 120 | ambiguous baseline wording | - preserves current active baseline; |
| `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative decision proposal |
| `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md` | 65 | manual review status wording | E5 should be treated as non-normative evidence depth terminology for review, examples, and future guidance. |
| `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md` | 77 | manual review status wording | \| Example terminology \| Allow with explicit non-normative framing \| |
| `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md` | 163 | manual review status wording | The existing integrity-focused example may use E5-like framing as non-normative example terminology. |
| `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md` | 217 | manual review status wording | 1. Keep E5 as non-normative terminology. |
| `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md` | 275 | manual review status wording | - E5 is retained as non-normative evidence depth terminology. |
| `docs/en/status/v050x-evidence-example-design-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative example design proposal |
| `docs/en/status/v050x-evidence-example-design-proposal.md` | 46 | ambiguous baseline wording | ## Current Baseline Constraint |
| `docs/en/status/v050x-evidence-integrity-csv-refinement-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative CSV refinement proposal |
| `docs/en/status/v050x-evidence-integrity-csv-refinement-proposal.md` | 79 | ambiguous baseline wording | - changing the active baseline before reviewer agreement; |
| `docs/en/status/v050x-evidence-integrity-negative-tests-candidate-appendix.md` | 3 | manual review status wording | **Status:** Temporary, non-normative candidate appendix |
| `docs/en/status/v050x-evidence-integrity-negative-tests-csv-refinement-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative CSV refinement proposal |
| `docs/en/status/v050x-evidence-integrity-negative-tests-track-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative track proposal |
| `docs/en/status/v050x-evidence-integrity-negative-tests-track-proposal.md` | 60 | ambiguous baseline wording | ## Current Baseline |
| `docs/en/status/v050x-evidence-integrity-negative-tests-track-proposal.md` | 62 | ambiguous baseline wording | The current active baseline already includes: |
| `docs/en/status/v050x-evidence-schema-and-examples-track-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative track proposal |
| `docs/en/status/v050x-evidence-schema-and-examples-track-proposal.md` | 25 | ambiguous baseline wording | This document does not change the active baseline. |
| `docs/en/status/v050x-evidence-schema-and-examples-track-proposal.md` | 48 | ambiguous baseline wording | ## Current Baseline Constraint |
| `docs/en/status/v050x-evidence-schema-example-implementation-readiness.md` | 3 | manual review status wording | **Status:** Temporary, non-normative implementation readiness review |
| `docs/en/status/v050x-evidence-schema-field-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative schema field proposal |
| `docs/en/status/v050x-follow-up-completion-summary.md` | 40 | manual review status wording | - cross-agent budget and resource propagation remains non-normative guidance and an existing-control refinement candidate; |
| `docs/en/status/v050x-follow-up-status.md` | 26 | manual review status wording | **Status:** Temporary, non-normative follow-up status document |
| `docs/en/status/v050x-follow-up-status.md` | 42 | manual review status wording | These updates produced non-normative guidance and testing guidance documents. |
| `docs/en/status/v050x-follow-up-status.md` | 60 | manual review status wording | \| #162 \| Capability-scoped cross-agent delegation controls \| PR #171 \| `docs/en/56-capability-scoped-cross-agent-delegation.md` \| Decide whether guidance remains non-normative, refines existing controls, becomes testing/evidence/schema mate... |
| `docs/en/status/v050x-follow-up-status.md` | 77 | manual review status wording | - remain non-normative guidance; |
| `docs/en/status/v050x-follow-up-status.md` | 111 | manual review status wording | - where non-normative planning should become normative or assessment-relevant; |
| `docs/en/status/v050x-follow-up-status.md` | 135 | ambiguous baseline wording | - change the baseline; |
| `docs/en/status/v050x-follow-up-status.md` | 316 | manual review status wording | The proposal recommends treating E5 as non-normative evidence depth terminology for examples, review, and future guidance, not as a certification level, required schema value, or active testing procedure requirement. |
| `docs/en/status/v050x-follow-up-status.md` | 328 | manual review status wording | - E5 is treated as non-normative evidence depth terminology for examples, review, and future guidance. |
| `docs/en/status/v050x-follow-up-status.md` | 487 | manual review status wording | The checkpoint records that delegation acceptance/refusal and chain accountability negative tests are already defined in non-normative guidance, supported by proposal, candidate appendix, CSV refinement proposal, and active testing coverage... |
| `docs/en/status/v050x-follow-up-status.md` | 505 | manual review status wording | The checkpoint records that cross-agent budget propagation guidance is already defined in non-normative guidance and that the current v0.5.x cycle does not require immediate active artifact changes. |
| `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md` | 3 | manual review status wording | **Status:** Temporary, non-normative candidate appendix |
| `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md` | 66 | manual review status wording | This appendix uses four non-normative preservation levels. |
| `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative guidance proposal |
| `docs/en/status/v050x-incorporation-decision-register.md` | 26 | manual review status wording | **Status:** Temporary, non-normative incorporation decision register |
| `docs/en/status/v050x-incorporation-decision-register.md` | 54 | manual review status wording | \| Keep as guidance \| The material should remain non-normative guidance for now. \| |
| `docs/en/status/v050x-incorporation-decision-register.md` | 77 | manual review status wording | The following waves are non-normative planning guidance. |
| `docs/en/status/v050x-incorporation-decision-register.md` | 79 | ambiguous baseline wording | They are intended to reduce review risk and avoid premature baseline changes. |
| `docs/en/status/v050x-incorporation-decision-register.md` | 287 | ambiguous baseline wording | ### Do not update baseline artifacts in this phase |
| `docs/en/status/v050x-incorporation-decision-register.md` | 310 | manual review status wording | ### Preserve non-normative status until explicit incorporation |
| `docs/en/status/v050x-incorporation-decision-register.md` | 312 | manual review status wording | Planning documents and follow-up guidance remain non-normative unless a later PR explicitly updates the relevant normative or assessment artifact. |
| `docs/en/status/v050x-incorporation-decision-register.md` | 643 | manual review status wording | \| Example terminology \| Allowed with non-normative framing \| |
| `docs/en/status/v050x-incorporation-decision-register.md` | 660 | manual review status wording | \| Example terminology \| Allowed with non-normative framing \| |
| `docs/en/status/v050x-incorporation-decision-register.md` | 939 | manual review status wording | - keep delegation acceptance/refusal and chain accountability negative tests as non-normative guidance and candidate material for the current cycle; |
| `docs/en/status/v050x-incorporation-decision-register.md` | 951 | manual review status wording | - keep cross-agent budget propagation as non-normative guidance and an existing-control refinement candidate for the current cycle; |
| `docs/en/status/v050x-incorporation-review-checkpoint.md` | 6 | manual review status wording | **Status:** Temporary, non-normative incorporation checkpoint |
| `docs/en/status/v050x-incorporation-review-checkpoint.md` | 21 | ambiguous baseline wording | It does not change the active baseline. |
| `docs/en/status/v050x-issue-163-delegation-negative-tests-consolidation-checkpoint.md` | 34 | manual review status wording | The non-normative negative test guidance already covers the major #163 failure modes. |
| `docs/en/status/v050x-issue-163-delegation-negative-tests-consolidation-checkpoint.md` | 57 | manual review status wording | These tests are non-normative planning and review material. They do not create executable fixtures or independent active testing rows. |
| `docs/en/status/v050x-issue-164-budget-propagation-consolidation-checkpoint.md` | 180 | manual review status wording | Cross-agent budget propagation remains non-normative guidance and an existing-control refinement candidate for the current cycle. |
| `docs/en/status/v050x-issue-165-evidence-integrity-consolidation-checkpoint.md` | 3 | manual review status wording | **Status:** Temporary, non-normative consolidation checkpoint |
| `docs/en/status/v050x-issue-165-evidence-integrity-consolidation-checkpoint.md` | 39 | manual review status wording | - E5 / evidence depth was defined as non-normative review vocabulary, not a certification scale; |
| `docs/en/status/v050x-issue-165-evidence-integrity-consolidation-checkpoint.md` | 57 | manual review status wording | \| Evidence depth / E5 decision \| Completed for current cycle \| E5 retained as non-normative review vocabulary. \| |
| `docs/en/status/v050x-issue-166-tamper-evident-contexts-consolidation-checkpoint.md` | 3 | manual review status wording | **Status:** Temporary, non-normative consolidation checkpoint |
| `docs/en/status/v050x-issue-167-approval-quality-consolidation-checkpoint.md` | 3 | manual review status wording | **Status:** Temporary, non-normative consolidation checkpoint |
| `docs/en/status/v050x-negative-evidence-examples-fixtures-decision-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative decision proposal |
| `docs/en/status/v050x-negative-evidence-examples-fixtures-decision-proposal.md` | 187 | manual review status wording | The evidence depth decision proposal keeps E5 non-normative. |
| `docs/en/status/v050x-next-phase-track-plan.md` | 6 | manual review status wording | **Status:** Temporary, non-normative planning and coordination document |
| `docs/en/status/v050x-next-phase-track-plan.md` | 25 | ambiguous baseline wording | This document does not change the active baseline. |
| `docs/en/status/v050x-next-phase-track-plan.md` | 256 | ambiguous baseline wording | - Evidence integrity negative tests are concrete and can be developed without changing the baseline immediately. |
| `docs/en/status/v050x-principal-context-testing-candidate-appendix.md` | 3 | manual review status wording | **Status:** Temporary, non-normative testing candidate appendix |
| `docs/en/status/v050x-principal-context-testing-csv-refinement-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative CSV refinement proposal |
| `docs/en/status/v050x-principal-context-testing-csv-refinement-proposal.md` | 44 | ambiguous baseline wording | - changing the active baseline before reviewer agreement; |
| `docs/en/status/v050x-principal-context-testing-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative testing proposal review document |
| `docs/en/status/v050x-principal-context-testing-proposal.md` | 204 | ambiguous baseline wording | \| Option A \| Add these as a separate candidate appendix first. \| Safer, but delays active baseline incorporation. \| |
| `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-candidate-appendix.md` | 3 | manual review status wording | **Status:** Temporary, non-normative candidate appendix |
| `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-candidate-appendix.md` | 56 | manual review status wording | The expectation levels in this appendix are non-normative. |
| `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-candidate-appendix.md` | 828 | manual review status wording | - selected contexts remain non-normative guidance; |
| `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-incorporation-decision.md` | 3 | manual review status wording | **Status:** Temporary, non-normative incorporation decision |
| `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-incorporation-decision.md` | 140 | manual review status wording | The selected contexts should remain non-normative guidance for now. |
| `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-incorporation-decision.md` | 207 | manual review status wording | - selected contexts remain non-normative guidance; |
| `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-proposal.md` | 3 | manual review status wording | **Status:** Temporary, non-normative proposal |
| `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-proposal.md` | 43 | manual review status wording | - E5 is non-normative evidence depth vocabulary, not certification; |
| `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-proposal.md` | 55 | manual review status wording | This proposal uses three non-normative context tiers. |
| `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-proposal.md` | 163 | manual review status wording | E5 remains non-normative review vocabulary. |
| `docs/en/status/v050x-testing-candidate-mapping.md` | 3 | manual review status wording | **Status:** Temporary, non-normative testing candidate mapping document |
| `docs/en/status/v050x-testing-candidate-mapping.md` | 29 | ambiguous baseline wording | The goal is to prepare for future testing procedure review without prematurely modifying baseline artifacts. |
| `docs/en/status/v050x-testing-candidate-selection.md` | 3 | manual review status wording | **Status:** Temporary, non-normative testing candidate selection document |
| `docs/en/status/v050x-testing-candidate-selection.md` | 197 | ambiguous baseline wording | That PR should still avoid directly modifying the active testing procedure CSV unless the pass/fail language is ready for baseline review. |
| `docs/en/status/v050x-testing-draft-pass-fail-criteria.md` | 3 | manual review status wording | **Status:** Temporary, non-normative draft pass/fail criteria |
| `docs/en/status/v050x-testing-incorporation-readiness-review.md` | 3 | manual review status wording | **Status:** Temporary, non-normative testing incorporation readiness review |
| `docs/en/status/v050x-testing-incorporation-readiness-review.md` | 33 | manual review status wording | This readiness status is non-normative. |
| `docs/en/status/v050x-testing-incorporation-readiness-review.md` | 185 | manual review status wording | ### Maintain non-normative status |
| `docs/en/status/v050x-testing-procedure-candidate-matrix.md` | 3 | manual review status wording | **Status:** Temporary, non-normative testing procedure candidate matrix |
| `docs/en/status/v060-authorization-decision-artifact-minimal-profile-planning.md` | 17 | ambiguous baseline wording | This document is planning material. It does not change active controls, assessment criteria, schema requirements, or the current control and assessment baseline. |
| `docs/en/status/v060-authorization-decision-artifact-minimal-profile-planning.md` | 65 | ambiguous baseline wording | - change the current active AAEF baseline |
| `docs/en/status/v060-authorization-decision-artifact-minimal-profile-planning.md` | 257 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-external-framework-mapping-csv-enrichment-review.md` | 45 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md` | 16 | ambiguous baseline wording | This document is planning material. It does not change active controls, assessment criteria, or the current control and assessment baseline. |
| `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md` | 61 | ambiguous baseline wording | - change the current active AAEF baseline |
| `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md` | 385 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-implementer-quick-start-planning.md` | 20 | ambiguous baseline wording | This document is planning material. It does not change active controls, assessment criteria, schema requirements, or the current control and assessment baseline. |
| `docs/en/status/v060-implementer-quick-start-planning.md` | 335 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-legal-compliance-applicability-note-planning.md` | 21 | ambiguous baseline wording | This document is planning material. It does not change active controls, assessment criteria, legal obligations, schema requirements, or the current control and assessment baseline. |
| `docs/en/status/v060-legal-compliance-applicability-note-planning.md` | 312 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-operational-responsibility-matrix-planning.md` | 15 | ambiguous baseline wording | This document is planning material. It does not change active controls, assessment criteria, or the current control and assessment baseline. |
| `docs/en/status/v060-operational-responsibility-matrix-planning.md` | 60 | ambiguous baseline wording | - change the current active AAEF baseline |
| `docs/en/status/v060-operational-responsibility-matrix-planning.md` | 262 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-planning-input-synthesis.md` | 11 | manual review v0.5.0 reference | The purpose of v0.6.0 is to convert selected v0.5.0 and v0.5.x planning material into practical adoption packages that can be evaluated by implementers, operators, auditors, legal and compliance teams, security architects, and risk owners. |
| `docs/en/status/v060-planning-input-synthesis.md` | 13 | ambiguous baseline wording | v0.6.0 should not be treated as a direct expansion of the active control baseline by default. Instead, it should define the adoption-facing materials needed before selected planning concepts can be promoted into active artifacts in a future... |
| `docs/en/status/v060-planning-input-synthesis.md` | 29 | ambiguous baseline wording | ## Baseline position |
| `docs/en/status/v060-planning-input-synthesis.md` | 31 | needs baseline review | v0.6.0 planning does not automatically change the current control and assessment baseline. |
| `docs/en/status/v060-planning-input-synthesis.md` | 33 | ambiguous or possibly stale latest wording | The current active baseline remains the latest explicitly designated control and assessment baseline until active artifacts are updated. |
| `docs/en/status/v060-planning-input-synthesis.md` | 265 | manual review v0.5.0 reference | - automatically promote all v0.5.0 or v0.5.x planning material into active controls |
| `docs/en/status/v060-planning-input-synthesis.md` | 270 | ambiguous baseline wording | - imply that the current active baseline has changed unless active artifacts are explicitly updated |
| `docs/en/status/v060-planning-input-synthesis.md` | 295 | ambiguous baseline wording | 5. Avoid baseline changes until candidate artifacts are reviewed and intentionally promoted. |
| `docs/en/status/v060-planning-progress-summary.md` | 14 | ambiguous baseline wording | This document is planning and coordination material. It does not change active controls, assessment criteria, schema requirements, legal obligations, or the current control and assessment baseline. |
| `docs/en/status/v060-planning-progress-summary.md` | 30 | ambiguous baseline wording | v0.6.0 remains planning-oriented at this stage. The current active baseline is not changed unless active artifacts are explicitly updated in later PRs. |
| `docs/en/status/v060-planning-progress-summary.md` | 84 | manual review status wording | A repository review identified document-map coverage gaps affecting both core numbered documents and non-normative planning/guidance documents. |
| `docs/en/status/v060-planning-progress-summary.md` | 100 | manual review status wording | \| F-05 \| `document-map.md` missing non-normative planning / guidance docs \| Addressed by #254 and regression-protected by #255 \| |
| `docs/en/status/v060-planning-progress-summary.md` | 107 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-planning-progress-summary.md` | 150 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-release-decision-record.md` | 24 | ambiguous baseline wording | \| D-02 \| Active baseline \| Do not change the current active control and assessment baseline by implication. \| README, CHANGELOG, and release notes must preserve explicit baseline boundaries. \| |
| `docs/en/status/v060-release-decision-record.md` | 26 | ambiguous baseline wording | \| D-04 \| README status wording \| Review README status wording and update only if needed to describe v0.6.0 as a planning release without implying active baseline change. \| Release PR may update README files if current wording would be stale... |
| `docs/en/status/v060-release-decision-record.md` | 35 | manual review status wording | \| D-13 \| Child track issues \| Do not automatically close child track issues merely because a planning release is created. \| Close or keep child track issues only after issue-specific review. \| |
| `docs/en/status/v060-release-decision-record.md` | 52 | ambiguous baseline wording | ## D-02: active baseline |
| `docs/en/status/v060-release-decision-record.md` | 56 | needs baseline review | v0.6.0 should not change the current active control and assessment baseline by implication. |
| `docs/en/status/v060-release-decision-record.md` | 60 | ambiguous baseline wording | The v0.6.0 artifacts are currently planning and coordination materials. Any baseline change should require explicit changes to active artifacts through later PRs. |
| `docs/en/status/v060-release-decision-record.md` | 66 | ambiguous baseline wording | > Unless explicitly updated in active artifacts, the current control and assessment baseline remains unchanged. |
| `docs/en/status/v060-release-decision-record.md` | 83 | manual review status wording | - keep wording clear that this is a planning release |
| `docs/en/status/v060-release-decision-record.md` | 84 | ambiguous baseline wording | - avoid implying active baseline change |
| `docs/en/status/v060-release-decision-record.md` | 97 | manual review status wording | - current planning release |
| `docs/en/status/v060-release-decision-record.md` | 98 | ambiguous baseline wording | - current active control and assessment baseline |
| `docs/en/status/v060-release-decision-record.md` | 99 | manual review status wording | - non-normative planning material |
| `docs/en/status/v060-release-decision-record.md` | 110 | ambiguous baseline wording | - active baseline change by implication |
| `docs/en/status/v060-release-decision-record.md` | 124 | manual review status wording | Citation metadata should not be updated casually, but a tagged planning release may be citable depending on project policy. |
| `docs/en/status/v060-release-decision-record.md` | 131 | ambiguous baseline wording | - explicitly state that `CITATION.cff` is not updated because v0.6.0 is a planning release and citation metadata remains tied to the current citable baseline |
| `docs/en/status/v060-release-decision-record.md` | 141 | ambiguous baseline wording | The release notes draft already contains baseline and claim-boundary language. |
| `docs/en/status/v060-release-decision-record.md` | 147 | manual review status wording | - planning release status |
| `docs/en/status/v060-release-decision-record.md` | 148 | ambiguous baseline wording | - current baseline note |
| `docs/en/status/v060-release-decision-record.md` | 241 | manual review status wording | Do not automatically close child track issues solely because a planning release is created. |
| `docs/en/status/v060-release-decision-record.md` | 283 | ambiguous baseline wording | - assessment baseline changes |
| `docs/en/status/v060-release-decision-record.md` | 295 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-release-decision-record.md` | 311 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-release-decision-record.md` | 326 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-release-notes-draft.md` | 15 | ambiguous baseline wording | This document does not create a release, create a tag, change active controls, change the current control and assessment baseline, or promote planning material into active requirements. |
| `docs/en/status/v060-release-notes-draft.md` | 27 | ambiguous baseline wording | It does not, by itself, change the current active control and assessment baseline. |
| `docs/en/status/v060-release-notes-draft.md` | 52 | ambiguous baseline wording | - an automatic change to the current active control and assessment baseline |
| `docs/en/status/v060-release-notes-draft.md` | 55 | ambiguous baseline wording | ## Current baseline note |
| `docs/en/status/v060-release-notes-draft.md` | 57 | ambiguous baseline wording | Unless explicitly updated in active artifacts, the current control and assessment baseline remains unchanged. |
| `docs/en/status/v060-release-notes-draft.md` | 150 | manual review status wording | \| F-05 document-map missing non-normative planning / guidance docs \| Addressed and regression-protected. \| |
| `docs/en/status/v060-release-notes-draft.md` | 206 | ambiguous baseline wording | - README status language does not imply an active baseline change |
| `docs/en/status/v060-release-notes-draft.md` | 207 | ambiguous baseline wording | - release notes preserve baseline and claim boundaries |
| `docs/en/status/v060-release-notes-draft.md` | 222 | ambiguous baseline wording | - changing the current active control and assessment baseline |
| `docs/en/status/v060-release-notes-draft.md` | 243 | ambiguous baseline wording | It organizes implementer, operator, legal/compliance, security architecture, and risk owner planning artifacts for future adoption-facing refinement. It does not, by itself, change the current active control and assessment baseline. |
| `docs/en/status/v060-release-notes-draft.md` | 256 | ambiguous baseline wording | #### Baseline and claim boundary |
| `docs/en/status/v060-release-notes-draft.md` | 258 | ambiguous baseline wording | Unless explicitly updated in active artifacts, the current control and assessment baseline remains unchanged. |
| `docs/en/status/v060-release-notes-draft.md` | 271 | ambiguous baseline wording | - baseline-change boundaries are clear |
| `docs/en/status/v060-release-preparation-planning.md` | 16 | ambiguous baseline wording | This document is planning and coordination material. It does not create a release, create a tag, change active controls, change the current control and assessment baseline, or promote planning material into active requirements. |
| `docs/en/status/v060-release-preparation-planning.md` | 24 | manual review v0.5.0 reference | The release should be positioned as a planning and adoption-readiness release that organizes selected v0.5.0 and v0.5.x planning material into implementer, operational, legal/compliance, security architecture, and risk owner adoption packag... |
| `docs/en/status/v060-release-preparation-planning.md` | 26 | ambiguous baseline wording | It should not be positioned as a new active control baseline unless later PRs explicitly update active artifacts. |
| `docs/en/status/v060-release-preparation-planning.md` | 41 | ambiguous baseline wording | - No active baseline change has been made. |
| `docs/en/status/v060-release-preparation-planning.md` | 64 | ambiguous baseline wording | - change the current control and assessment baseline by implication |
| `docs/en/status/v060-release-preparation-planning.md` | 87 | ambiguous baseline wording | \| README status review \| Ensure README status wording does not imply an active baseline change. \| Required before release \| |
| `docs/en/status/v060-release-preparation-planning.md` | 136 | ambiguous baseline wording | 9. Current baseline note |
| `docs/en/status/v060-release-preparation-planning.md` | 151 | needs baseline review | > AAEF v0.6.0 is a planning and adoption-readiness release. It organizes implementer, operator, legal/compliance, security architecture, and risk owner planning artifacts for future adoption-facing refinement. It does not, by itself, change... |
| `docs/en/status/v060-release-preparation-planning.md` | 153 | ambiguous baseline wording | ## Candidate baseline language |
| `docs/en/status/v060-release-preparation-planning.md` | 155 | ambiguous baseline wording | Suggested baseline language: |
| `docs/en/status/v060-release-preparation-planning.md` | 157 | needs baseline review | > Unless explicitly updated in active artifacts, the current control and assessment baseline remains unchanged. v0.6.0 planning artifacts are non-normative planning material until later PRs promote selected material into active guidance, co... |
| `docs/en/status/v060-release-preparation-planning.md` | 201 | ambiguous baseline wording | - Treat v0.6.0 as a planning release, not an active baseline release. |
| `docs/en/status/v060-release-preparation-planning.md` | 216 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-release-preparation-planning.md` | 228 | ambiguous baseline wording | - baseline and claim-boundary language are proposed |
| `docs/en/status/v060-release-preparation-planning.md` | 231 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-release-readiness-review.md` | 24 | ambiguous baseline wording | The release should be treated as a planning and adoption-readiness release, not as an active control-baseline release. |
| `docs/en/status/v060-release-readiness-review.md` | 41 | ambiguous baseline wording | \| Active baseline change \| Not performed. \| |
| `docs/en/status/v060-release-readiness-review.md` | 52 | ambiguous baseline wording | \| README status wording reviewed \| Yes \| Must not imply active baseline change \| Decision needed \| |
| `docs/en/status/v060-release-readiness-review.md` | 59 | ambiguous baseline wording | \| Baseline-change review \| Yes \| Must confirm no active baseline change is implied \| Required \| |
| `docs/en/status/v060-release-readiness-review.md` | 71 | ambiguous baseline wording | \| Does v0.6.0 change the active control and assessment baseline? \| No \| No active artifacts have been explicitly promoted. \| |
| `docs/en/status/v060-release-readiness-review.md` | 76 | ambiguous baseline wording | \| Should README status wording be updated? \| Decision needed \| Must avoid implying a baseline change. \| |
| `docs/en/status/v060-release-readiness-review.md` | 130 | ambiguous baseline wording | - active baseline change by implication |
| `docs/en/status/v060-release-readiness-review.md` | 132 | ambiguous baseline wording | ## Baseline-change checklist |
| `docs/en/status/v060-release-readiness-review.md` | 137 | ambiguous baseline wording | - no assessment baseline is changed by implication |
| `docs/en/status/v060-release-readiness-review.md` | 138 | manual review status wording | - planning drafts remain non-normative unless explicitly promoted |
| `docs/en/status/v060-release-readiness-review.md` | 139 | ambiguous baseline wording | - current baseline language is included in release notes |
| `docs/en/status/v060-release-readiness-review.md` | 140 | ambiguous baseline wording | - README status wording remains consistent with the intended baseline posture |
| `docs/en/status/v060-release-readiness-review.md` | 167 | ambiguous baseline wording | - preserve explicit language that v0.6.0 is planning/adoption-readiness material, not an active baseline change |
| `docs/en/status/v060-release-readiness-review.md` | 182 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-release-readiness-review.md` | 194 | ambiguous baseline wording | - baseline-change checks are documented |
| `docs/en/status/v060-release-readiness-review.md` | 197 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-research-positioning-review.md` | 14 | ambiguous baseline wording | This document is research-positioning material. It does not change active controls, schemas, assessment procedures, testing procedures, mappings, examples, or the current control and assessment baseline. |
| `docs/en/status/v060-research-positioning-review.md` | 230 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-research-positioning-review.md` | 249 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-review-follow-up-summary.md` | 15 | ambiguous baseline wording | This document is planning and coordination material. It does not change active controls, assessment criteria, schema requirements, external mappings, legal claims, or the current control and assessment baseline. |
| `docs/en/status/v060-review-follow-up-summary.md` | 27 | manual review status wording | \| F-05 \| `document-map.md` missing non-normative planning / guidance documents \| Addressed and regression-protected \| |
| `docs/en/status/v060-review-follow-up-summary.md` | 158 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-review-follow-up-summary.md` | 194 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-risk-owner-guide-planning.md` | 23 | ambiguous baseline wording | This document is planning material. It does not change active controls, assessment criteria, legal obligations, schema requirements, or the current control and assessment baseline. |
| `docs/en/status/v060-risk-owner-guide-planning.md` | 313 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-status-document-archive-readiness-review.md` | 129 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-status-document-archive-readiness-review.md` | 140 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-status-document-inventory-planning.md` | 122 | manual review status wording | 7. Should it remain explicitly non-normative? |
| `docs/en/status/v060-status-document-inventory-planning.md` | 147 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-status-document-inventory-planning.md` | 158 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-status-document-triage-decision-register.md` | 140 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-status-document-triage-decision-register.md` | 152 | ambiguous baseline wording | - no active baseline change is implied |
| `docs/en/status/v060-status-document-triage-planning.md` | 58 | ambiguous baseline wording | - change the current control and assessment baseline |
| `docs/en/status/v060-status-document-triage-planning.md` | 166 | manual review status wording | 8. Should it remain non-normative? |
| `docs/en/status/v060-status-document-triage-planning.md` | 251 | ambiguous baseline wording | - no active baseline change is implied |
| `mappings/csa-agentic-trust-framework.md` | 4 | ambiguous baseline wording | **AAEF version baseline:** v0.4.0 Public Review Draft with v0.4.x refinements |
| `mappings/nist-ai-rmf-genai-profile.md` | 4 | ambiguous baseline wording | **AAEF version baseline:** v0.4.0 Public Review Draft with v0.4.x refinements |
| `mappings/owasp-agentic-top10-2026.md` | 4 | ambiguous baseline wording | **AAEF version baseline:** v0.4.0 Public Review Draft with v0.4.x refinements |
| `mappings/threat-control-assurance-mapping.md` | 5 | manual review status wording | This is an initial v0.2 public review draft. |
| `README.ko.md` | 84 | manual review v0.5.0 reference | **AAEF v0.5.0 Public Review Planning Release** 는 최신 공개 검토 planning release 입니다. |
| `README.ko.md` | 88 | ambiguous baseline wording | 이전 v0.3.x, v0.2.x, v0.1.x releases 는 prior public review baselines 로 계속 참조할 수 있습니다. |
| `README.ko.md` | 90 | manual review v0.5.0 reference | AAEF v0.5.0에 포함된 주요 요소: |
| `README.ko.md` | 103 | manual review v0.5.0 reference | AAEF v0.5.0은 공개 검토 planning release 입니다. 인증 체계, 공식 표준, implementation conformance claim, audit opinion, compliance equivalence 또는 완전한 완화 주장을 의미하지 않습니다. |
| `README.ko.md` | 123 | manual review v0.5.0 reference | > Kazuma Horishita, *Agentic Authority & Evidence Framework (AAEF): An Action Assurance Control Profile for Agentic AI Systems*, v0.5.0 Public Review Planning Release, 2026. |
| `README.md` | 65 | manual review status wording | - [AAEF v0.1.3 Public Review Draft announcement](https://www.linkedin.com/feed/update/urn:li:activity:7453853837167263744/) — LinkedIn |
| `README.md` | 96 | manual review status wording | The file name is retained for continuity, but the catalog contains the current public review control set. |
| `README.md` | 98 | manual review status wording | The v0.4.x Public Review Draft includes: |
| `README.md` | 133 | ambiguous baseline wording | 1. [`docs/en/13-one-page-overview.md`](docs/en/13-one-page-overview.md) — quick mental model and current public review baseline |
| `README.zh-CN.md` | 84 | manual review v0.5.0 reference | **AAEF v0.5.0 Public Review Planning Release** 是最新公开评审 planning release。 |
| `README.zh-CN.md` | 88 | ambiguous baseline wording | 此前的 v0.3.x、v0.2.x、v0.1.x releases 仍可作为 prior public review baselines 参考。 |
| `README.zh-CN.md` | 90 | manual review v0.5.0 reference | AAEF v0.5.0 包含的主要内容包括： |
| `README.zh-CN.md` | 103 | manual review v0.5.0 reference | AAEF v0.5.0 是公开评审 planning release。它不是认证机制、正式标准、implementation conformance claim、audit opinion、compliance equivalence，也不声称能够完全缓解所有风险。 |
| `README.zh-CN.md` | 123 | manual review v0.5.0 reference | > Kazuma Horishita, *Agentic Authority & Evidence Framework (AAEF): An Action Assurance Control Profile for Agentic AI Systems*, v0.5.0 Public Review Planning Release, 2026. |
| `taxonomies/high-impact-action-taxonomy-v0.2-draft.csv` | 1 | ambiguous baseline wording | Category ID,Category Name,Definition,Example Actions,Typical Impact,Recommended Baseline,Key AAEF Control Areas,Suggested Evidence |


## Expected-reference sample

These lines appear to be expected historical, baseline, or v0.6.0 release references. This is a sample only, not a complete inventory.

| File | Line | Classification | Text |
| --- | ---: | --- | --- |
| `CHANGELOG.md` | 7 | expected v0.6.0 release reference | ## v0.6.0 Practical Adoption Readiness Planning Release - 2026-05-02 |
| `CHANGELOG.md` | 9 | expected v0.6.0 release reference | ### v0.6.0 Planning and Adoption Readiness |
| `CHANGELOG.md` | 11 | expected v0.6.0 release reference | - Added the v0.6.0 planning input synthesis for the Practical Adoption Readiness planning cycle. |
| `CHANGELOG.md` | 12 | expected v0.6.0 release reference | - Added initial five-pillar v0.6.0 planning drafts for Implementer Readiness, Operational Readiness, Legal and Compliance Applicability, Security Architecture Hardening, and Risk Owner / Executive Adoption. |
| `CHANGELOG.md` | 19 | expected v0.6.0 release reference | - Added the v0.6.0 Planning Progress Summary to summarize the initial five-pillar planning set, cross-workstream integration, document-map review follow-up, and remaining planning candidates. |
| `CHANGELOG.md` | 20 | expected v0.6.0 release reference | - Added the v0.6.0 Review Follow-up Summary to summarize repository review follow-up across F-01 through F-05. |
| `CHANGELOG.md` | 21 | expected v0.6.0 release reference | - Added the v0.6.0 Release Preparation Planning document. |
| `CHANGELOG.md` | 22 | expected v0.6.0 release reference | - Added the v0.6.0 Release Notes Draft. |
| `CHANGELOG.md` | 23 | expected v0.6.0 release reference | - Added the v0.6.0 Release Readiness Review. |
| `CHANGELOG.md` | 24 | expected v0.6.0 release reference | - Added the v0.6.0 Release Decision Record. |
| `CHANGELOG.md` | 30 | expected v0.6.0 release reference | - Added and maintained status index entries for v0.6.0 planning documents. |
| `CHANGELOG.md` | 31 | expected historical release reference | - Updated Japanese README document status to align with the v0.5.0 Public Review Planning Release. |
| `CHANGELOG.md` | 45 | expected v0.6.0 release reference | - Added the v0.6.0 status document triage planning draft. |
| `CHANGELOG.md` | 46 | expected v0.6.0 release reference | - Added the v0.6.0 status document inventory planning draft, identifying 52 status documents. |
| `CHANGELOG.md` | 47 | expected v0.6.0 release reference | - Added the v0.6.0 status document triage decision register, with 36 archive-later candidates, 15 keep decisions, and 1 replace-later candidate. |
| `CHANGELOG.md` | 48 | expected v0.6.0 release reference | - Added the v0.6.0 status document archive readiness review, finding that all 36 archive-later documents still have status-document references. |
| `CHANGELOG.md` | 49 | expected v0.6.0 release reference | - Added the v0.6.0 external framework mapping CSV enrichment review, identifying 2 mapping CSV candidates and 9 mapping Markdown candidates. |
| `CHANGELOG.md` | 67 | expected v0.6.0 release reference | - v0.6.0 is a planning and adoption-readiness release. |
| `CHANGELOG.md` | 69 | expected v0.6.0 release reference | - v0.6.0 does not create a certification scheme, legal compliance claim, audit opinion, conformity assessment, or equivalence claim with external frameworks. |
| `CHANGELOG.md` | 70 | expected v0.6.0 release reference | - v0.6.0 planning artifacts remain non-normative unless later PRs explicitly promote selected material into active guidance, controls, schemas, assessment methods, testing procedures, examples, or release artifacts. |
| `CHANGELOG.md` | 72 | expected historical release reference | ## v0.5.0 Public Review Planning Release - 2026-04-29 |
| `CHANGELOG.md` | 76 | expected historical release reference | - Added a v0.5.0 release preparation checklist with validation steps, issue review guidance, follow-up issue candidates, and draft release notes. |
| `CHANGELOG.md` | 77 | expected historical release reference | - Added a v0.5.0 release scope decision record clarifying that current planning models remain non-normative unless explicitly incorporated into future normative or assessment artifacts. |
| `CHANGELOG.md` | 78 | expected historical release reference | - Added a non-normative v0.5.0 approval quality model for meaningful approval, approval context sufficiency, batch approval risk, approval fatigue, and approval evidence expectations. |
| `CHANGELOG.md` | 80 | expected historical release reference | - Added a non-normative v0.5.0 evidence integrity levels model for risk-proportional evidence, tamper-evident storage, and performance overhead tradeoffs. |
| `CHANGELOG.md` | 82 | expected historical release reference | - Added a non-normative v0.5.0 authority lifecycle model covering principal context degradation, cross-agent authority, denial, freeze, revocation, and reauthorization. |
| `CHANGELOG.md` | 83 | expected historical release reference | - Added a preliminary v0.5.0 incorporation outcome register for current planning themes. |
| `CHANGELOG.md` | 84 | expected historical release reference | - Added v0.5.0 planning incorporation rules to clarify when planning concepts become guidance, testing refinements, evidence refinements, existing control refinements, or new controls. |
| `CHANGELOG.md` | 85 | expected historical release reference | - Clarified that `docs/en/30-49` v0.5.0 planning materials are non-normative unless explicitly incorporated into catalog, schema, assessment, testing, or release artifacts. |
| `CHANGELOG.md` | 86 | expected historical release reference | - Clarified the v0.5.0 planning overview by grouping the six planning themes into authority lifecycle and supporting assurance themes. |
| `CHANGELOG.md` | 87 | expected historical release reference | - Added missing v0.5.0 planning document index entries for Principal Context Degradation and tamper-evident evidence negative tests. |
| `CHANGELOG.md` | 88 | expected v0.4.1 reference or manual review | - Clarified current-status wording for v0.2-originated documents that remain part of the v0.4.1 Public Review Draft baseline. |
| `CHANGELOG.md` | 90 | expected v0.4.1 reference or manual review | ## v0.4.1 Public Review Refinement Release - 2026-04-28 |
| `CHANGELOG.md` | 97 | expected v0.4.1 reference or manual review | - Updated Korean and Simplified Chinese README document status and citation text to v0.4.1. |
| `CHANGELOG.md` | 98 | expected historical release reference | - Updated README repository structure to include current v0.5.0 planning documents and mapping files. |
| `docs/en/11-high-impact-action-taxonomy.md` | 11 | expected v0.4.1 reference or manual review | This taxonomy originated during the AAEF v0.2.0 discussion and review cycle and remains part of the current v0.4.1 Public Review Draft baseline. It is not a certification scheme, legal standard, or exhaustive list of all high-risk agentic A... |
| `docs/en/12-assessment-quick-start.md` | 5 | expected v0.4.1 reference or manual review | This document originated as an initial assessment quick start during the AAEF v0.2 public review cycle and remains part of the current v0.4.1 Public Review Draft baseline. |
| `docs/en/13-one-page-overview.md` | 189 | expected v0.4.1 reference or manual review | AAEF v0.4.1 Public Review Draft is the current public review baseline. |
| `docs/en/13-one-page-overview.md` | 191 | expected v0.4.1 reference or manual review | AAEF v0.4.1 is a maintenance and refinement release over v0.4.0. It preserves the v0.4.0 enterprise assessment usability baseline and incorporates post-release refinements to testing criteria and external framework mappings. |
| `docs/en/14-evidence-event-schema.md` | 17 | expected v0.4.1 reference or manual review | This schema originated during the AAEF v0.2.0 discussion and review cycle and remains part of the current v0.4.1 Public Review Draft baseline. It is not a certification format and does not guarantee compliance by itself. |
| `docs/en/16-assurance-model.md` | 5 | expected v0.4.1 reference or manual review | This document originated as an initial AAEF assurance model during the v0.2 public review cycle and remains part of the current v0.4.1 Public Review Draft baseline. |
| `docs/en/17-reference-architecture.md` | 5 | expected v0.4.1 reference or manual review | This document originated as the AAEF reference architecture during the v0.2 public review cycle and remains part of the current v0.4.1 Public Review Draft baseline. |
| `docs/en/18-implementation-guidance.md` | 97 | expected v0.5.0 planning-material reference | ## Relationship to v0.5.0 Planning Material |
| `docs/en/30-principal-context-degradation.md` | 3 | expected v0.5.0 planning-material reference | **Status:** Non-normative v0.5.0 planning concept note |
| `docs/en/30-principal-context-degradation.md` | 4 | expected v0.4.1 reference or manual review | **AAEF baseline:** v0.4.1 Public Review Draft |
| `docs/en/30-principal-context-degradation.md` | 7 | expected v0.5.0 planning-material reference | > **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifac... |
| `docs/en/30-principal-context-degradation.md` | 11 | expected v0.5.0 planning-material reference | This note defines Principal Context Degradation as a v0.5.0 planning concept for AAEF. |
| `docs/en/30-principal-context-degradation.md` | 206 | expected v0.5.0 planning-material reference | Future v0.5.0 work may include: |
| `docs/en/30-principal-context-degradation.md` | 215 | expected v0.5.0 planning-material reference | For v0.5.0 Principal Context Degradation examples, see `docs/en/45-principal-context-degradation-examples.md`. |
| `docs/en/31-cross-agent-cross-domain-authority.md` | 3 | expected v0.5.0 planning-material reference | **Status:** Non-normative v0.5.0 planning concept note |
| `docs/en/31-cross-agent-cross-domain-authority.md` | 4 | expected v0.4.1 reference or manual review | **AAEF baseline:** v0.4.1 Public Review Draft |
| `docs/en/31-cross-agent-cross-domain-authority.md` | 7 | expected v0.5.0 planning-material reference | > **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifac... |
| `docs/en/31-cross-agent-cross-domain-authority.md` | 11 | expected v0.5.0 planning-material reference | This note defines Cross-Agent and Cross-Domain Authority as a v0.5.0 planning concept for AAEF. |
| `docs/en/31-cross-agent-cross-domain-authority.md` | 240 | expected v0.5.0 planning-material reference | Future v0.5.0 work may include: |
| `docs/en/31-cross-agent-cross-domain-authority.md` | 251 | expected v0.5.0 planning-material reference | For v0.5.0 cross-agent authority examples, see `docs/en/46-cross-agent-authority-examples.md`. |
| `docs/en/32-authority-denial-reauthorization-flow.md` | 3 | expected v0.5.0 planning-material reference | **Status:** Non-normative v0.5.0 planning concept note |
| `docs/en/32-authority-denial-reauthorization-flow.md` | 4 | expected v0.4.1 reference or manual review | **AAEF baseline:** v0.4.1 Public Review Draft |
| `docs/en/32-authority-denial-reauthorization-flow.md` | 7 | expected v0.5.0 planning-material reference | > **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifac... |
| `docs/en/32-authority-denial-reauthorization-flow.md` | 11 | expected v0.5.0 planning-material reference | This note defines Authority Denial and Reauthorization Flow as a v0.5.0 planning concept for AAEF. |
| `docs/en/32-authority-denial-reauthorization-flow.md` | 225 | expected v0.5.0 planning-material reference | Future v0.5.0 work may include: |


## Interpretation guidance

Use the following interpretation rules before changing any line:

1. A `v0.5.0` reference is not automatically stale.
   It may be correct when referring to historical v0.5.0 planning materials, prior planning release artifacts, or numbered v0.5.0 documents.
2. A `v0.4.1` reference is expected when it describes the current control and assessment baseline.
3. A `v0.6.0` reference is expected when it describes the latest public review planning release, Practical Adoption Readiness planning, release metadata, or post-release documentation.
4. A line is likely stale when it says v0.5.0 is the latest public review planning release.
5. A line is ambiguous when it mentions baseline or latest status without clearly separating latest planning release from current control and assessment baseline.
6. Planning material should remain non-normative unless explicitly incorporated into active controls, schemas, assessment methods, testing procedures, examples, or release artifacts.

## Recommended cleanup policy

Recommended policy:

- Correct stale latest-release wording from v0.5.0 to v0.6.0 where the line is describing the latest release.
- Preserve v0.5.0 references where the line describes v0.5.0 planning materials or historical release records.
- Preserve v0.4.1 baseline wording where the line describes the current control and assessment baseline.
- Add clarification rather than replacement when a line must mention both v0.6.0 and v0.4.1.
- Avoid changes that imply v0.6.0 changes active controls or the current assessment baseline.

## Recommended next steps

Recommended next steps:

1. Review the review-needed candidate table.
2. Decide which entries need cleanup.
3. Prepare a targeted cleanup PR for stale or ambiguous references only.
4. Re-run this audit after cleanup if needed.
5. Then request a fresh framework review using the clarified version semantics.

## Non-goals

This audit does not:

- change active controls
- change the current control and assessment baseline
- update schemas, examples, mappings, CSVs, or testing procedures
- move, delete, archive, replace, or promote status documents
- claim certification, compliance, audit sufficiency, conformity, or equivalence
- decide that all v0.5.0 references are stale

## Acceptance criteria

This audit is sufficient when:

- expected version semantics are documented
- matched version/status references are summarized
- review-needed candidates are listed
- expected historical and baseline references are distinguished from stale references
- no active baseline change is implied
