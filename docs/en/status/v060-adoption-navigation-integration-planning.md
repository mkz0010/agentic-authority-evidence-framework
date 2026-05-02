# AAEF v0.6.x Adoption Navigation Integration Planning

Status: Adoption navigation integration planning  
Related issue: #282  
Related roadmap: #241  
Related split plan: `docs/en/status/v060-adoption-follow-up-split-planning.md`  
Related adoption index: `docs/en/status/v060-adoption-package-index-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document plans how the v0.6.0 adoption-oriented materials should be discoverable from AAEF entry points.

The goal is to reduce navigation friction for:

- implementers,
- auditors,
- consultants,
- operators,
- risk owners,
- legal/compliance reviewers,
- security architects,
- and researchers.

This document is planning material. It does not change active controls, evidence schema, assessment artifacts, testing procedures, mappings, examples, or the current control and assessment baseline.

## Why navigation integration matters

The v0.6.0 and v0.6.x adoption work added useful materials, including:

- implementation reference pattern,
- evidence examples,
- auditor evidence request checklist,
- consultant discovery checklist,
- operator runbook planning,
- adoption package index,
- active evidence example candidates,
- conservative external mapping pilot.

Those materials are useful only if readers can find the right entry point.

The issue is not whether the materials exist.

The issue is whether a reader can quickly answer:

> Which document should I read first for my role?

## Source artifacts

| Artifact | Role |
| --- | --- |
| `docs/en/status/v060-adoption-package-index-planning.md` | Current role/use-case index for adoption-oriented materials |
| `docs/en/status/v060-implementation-reference-pattern-planning.md` | Implementer bridge |
| `docs/en/status/v060-auditor-evidence-request-checklist-planning.md` | Auditor/reviewer bridge |
| `docs/en/status/v060-consultant-discovery-checklist-planning.md` | Consultant discovery bridge |
| `docs/en/status/v060-operator-runbook-planning.md` | Operator bridge |
| `docs/en/status/v060-risk-owner-guide-planning.md` | Risk-owner bridge |
| `docs/en/status/v060-legal-compliance-applicability-note-planning.md` | Legal/compliance bridge |
| `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md` | Security architecture bridge |
| `docs/en/status/v060-research-positioning-review.md` | Research bridge |
| `examples/evidence/README.md` | Active evidence example candidate entry point |
| `mappings/README.md` | Conservative external mapping entry point |

## Candidate navigation entry points

Potential entry points:

| Entry point | Candidate use | Risk |
| --- | --- | --- |
| `README.md` | Primary external project entry point | Must stay concise and avoid over-promising |
| `README.ja.md` | Japanese external project entry point | Must remain aligned with English positioning |
| `docs/en/document-map.md` | Detailed document inventory | Already comprehensive but may be too broad |
| `docs/en/55-researcher-overview.md` | Research-facing entry point | Should not become adoption-only |
| `docs/en/status/README.md` | Status/planning inventory | Good for maintainers, less ideal for first-time readers |
| Future `docs/en/adoption/README.md` | Dedicated adoption entry point | Requires new document area and maintenance |
| Future `docs/en/examples/README.md` | Example-oriented entry point | Useful if examples expand |
| Future `mappings/README.md` integration | Mapping-specific entry point | Already exists, but should not be over-promoted |

## Recommended integration posture

Initial recommendation:

1. Keep the top-level README concise.
2. Add a short adoption-readiness pointer rather than a large adoption section.
3. Link to the adoption package index as the role-based navigation hub.
4. Mention that adoption materials are planning/adoption-readiness materials unless explicitly promoted.
5. Add a Japanese README pointer with equivalent claim-boundary wording.
6. Do not imply that v0.6.0 changes the current control and assessment baseline.
7. Keep `docs/en/status/v060-adoption-package-index-planning.md` as the current role-based adoption hub.
8. Defer creation of `docs/en/adoption/README.md` unless navigation grows further.

## Candidate README wording

Candidate English README wording:

> For role-based adoption guidance, see the v0.6.0 adoption package index. It provides entry points for implementers, auditors, consultants, operators, risk owners, legal/compliance reviewers, security architects, and researchers. These materials are adoption-readiness planning materials and do not, by themselves, change the current control and assessment baseline.

Candidate Japanese README wording:

> 役割別の採用・検討ガイドとして、v0.6.0 adoption package index を参照してください。実装者、監査人、コンサルタント、運用担当者、リスクオーナー、法務・コンプライアンス担当者、セキュリティアーキテクト、研究者向けの入口を整理しています。これらは採用準備のための planning material であり、それ自体では current control and assessment baseline を変更しません。

## Candidate link targets

Recommended initial link target:

- `docs/en/status/v060-adoption-package-index-planning.md`

Secondary link targets:

- `examples/README.md`
- `examples/evidence/README.md`
- `mappings/README.md`

Do not overload README with every individual v0.6.x artifact.

## Navigation decision questions

Before implementation, decide:

- Should top-level README link directly to the adoption package index?
- Should README.ja mirror that link?
- Should researcher overview mention the adoption package index?
- Should `docs/en/document-map.md` add a short adoption route note beyond existing entries?
- Should a dedicated `docs/en/adoption/README.md` be created now or deferred?
- Should `examples/` and `mappings/` be linked from the adoption package index in a later update?
- How much planning/non-normative warning is needed near the navigation links?

## Initial decision

Initial decision:

> Add a concise README / README.ja adoption-readiness pointer in a later PR, linking to the adoption package index and preserving the v0.4.1 baseline boundary.

Defer:

- dedicated `docs/en/adoption/README.md`,
- large README restructuring,
- promotion of planning material into active requirements,
- and broad role-specific document reorganization.

## Claim boundaries

Navigation updates must not imply:

- production readiness,
- implementation conformance,
- audit sufficiency,
- certification,
- compliance,
- conformity,
- equivalence with external frameworks,
- or baseline change.

Any navigation text should preserve:

- v0.6.0 is a planning and adoption-readiness release,
- v0.4.1 remains the current control and assessment baseline unless explicitly changed,
- and planning materials are non-normative unless explicitly promoted.

## Recommended next implementation PR

Recommended next PR:

> Add adoption package navigation pointers to README and README.ja.

Candidate changes:

- Add a short English README pointer to `docs/en/status/v060-adoption-package-index-planning.md`.
- Add a short Japanese README pointer with equivalent boundary language.
- Optionally add a short note to `docs/en/55-researcher-overview.md` if the research entry point needs adoption context.
- Run Markdown, JSON example, and external mapping validation.

## Relationship to #282

This document partially addresses #282 by defining the navigation integration posture and recommended implementation path.

#282 should remain open until one of the following occurs:

- README / README.ja navigation pointers are implemented,
- a dedicated adoption entry point is created,
- or navigation integration is explicitly deferred.

## Non-goals

This document does not:

- update README navigation by itself,
- create a dedicated adoption directory,
- promote planning material into active requirements,
- change active controls,
- change the current control and assessment baseline,
- update evidence schema,
- update assessment artifacts,
- update testing procedures,
- assert production readiness,
- assert implementation conformance,
- assert audit sufficiency,
- claim compliance,
- claim certification,
- claim conformity,
- or claim equivalence with external frameworks.

## Acceptance criteria

This planning document is sufficient when:

- candidate navigation entry points are identified,
- recommended navigation posture is documented,
- candidate README wording is drafted,
- link targets are identified,
- claim boundaries are preserved,
- next implementation PR is defined,
- and no active baseline change is implied.
