# AAEF v0.6.0 External Framework Mapping CSV Enrichment Review

Status: Planning review  
Related roadmap: #241  
Milestone: v0.6.0 Planning  
Related planning summary: `docs/en/status/v060-planning-progress-summary.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document reviews current external framework mapping CSV and Markdown materials before any future mapping enrichment work.

The purpose is to prepare a conservative enrichment plan for machine-readable external framework mappings without overstating compliance, equivalence, audit sufficiency, or certification readiness.

This document is planning and review material. It does not modify mapping CSVs, external framework mappings, controls, schemas, examples, or assessment artifacts.

## Background

Repository review feedback identified that AAEF contains useful external-framework mapping discussion, but machine-readable CSV mapping coverage may be thinner than the surrounding Markdown discussion.

This review supports follow-up for that finding by identifying current mapping CSV candidates, related Markdown candidates, and safe enrichment directions.

## Scope

This review covers repository files whose paths indicate likely relationship to external framework mapping, including filename or path terms such as:

- `mapping`
- `framework`
- `OWASP`
- `NIST`
- `ISO`
- `CSA`
- `AI RMF`
- `external`

## Non-goals

This review does not:

- add or change mapping CSV rows
- claim compliance with external frameworks
- claim equivalence with external controls
- replace legal, compliance, audit, or standards analysis
- change active controls
- change the current control and assessment baseline
- change schemas, examples, or assessment artifacts
- create certification or conformity claims

## Mapping CSV candidates

| CSV file | Data rows | Columns | Review notes |
| --- | ---: | --- | --- |
| `mappings/aaef-external-framework-mapping-v0.4-draft.csv` | 10 | Mapping ID, External Framework, External Version, External Reference ID, External Reference Title, AAEF References, AAEF Control IDs, Relationship Type, Mapping Confidence, Mapping Status, Mapping Rationale, Limitations, Notes | limited mapping metadata columns |
| `mappings/threat-control-assurance-mapping-v0.2-draft.csv` | 44 | Control ID, Related Threats, Assurance Type, Primary Effect, Residual Risk, Implementation Assumptions | limited mapping metadata columns |

## Mapping Markdown candidates

| Markdown file | Title | Candidate role |
| --- | --- | --- |
| `docs/en/09-relationship-to-existing-frameworks.md` | 09. Relationship to Existing Frameworks | mapping or external-framework related Markdown candidate |
| `docs/en/28-external-framework-mapping-methodology.md` | External Framework Mapping Methodology | mapping or external-framework related Markdown candidate |
| `docs/en/29-iso-iec-42001-feasibility.md` | ISO/IEC 42001 Feasibility and Initial Alignment Note | mapping or external-framework related Markdown candidate |
| `docs/en/status/v050x-testing-candidate-mapping.md` | v0.5.x Testing Candidate Mapping | mapping or external-framework related Markdown candidate |
| `examples/attack-control-mapping.md` | Attack-Control Mapping Example | mapping or external-framework related Markdown candidate |
| `mappings/csa-agentic-trust-framework.md` | CSA Agentic Trust Framework Mapping | mapping or external-framework related Markdown candidate |
| `mappings/nist-ai-rmf-genai-profile.md` | NIST AI RMF and Generative AI Profile Mapping | mapping or external-framework related Markdown candidate |
| `mappings/owasp-agentic-top10-2026.md` | OWASP Agentic Top 10 2026 Mapping | mapping or external-framework related Markdown candidate |
| `mappings/threat-control-assurance-mapping.md` | Threat-Control Assurance Mapping | mapping or external-framework related Markdown candidate |

## Conservative enrichment principles

Any future mapping CSV enrichment should follow these principles:

1. Treat mappings as informative alignment aids only.
2. Avoid equivalence claims unless explicitly justified and reviewed.
3. Prefer relationship labels such as `supports`, `related`, `partial`, `informative`, or `not equivalent`.
4. Include rationale and limitations for each mapping row.
5. Preserve source references in a copyright-safe way.
6. Distinguish control intent, evidence support, assessment support, and governance support.
7. Avoid claiming that AAEF satisfies, certifies, or guarantees compliance with external frameworks.
8. Keep external framework mappings separate from active AAEF control requirements unless explicitly incorporated.

## Candidate enrichment columns

Future machine-readable mapping CSVs may benefit from fields such as:

| Candidate column | Purpose |
| --- | --- |
| `aaef_artifact` | AAEF control, principle, evidence field, assessment method, guidance document, or planning artifact being mapped. |
| `aaef_artifact_type` | Control, schema field, guidance, assessment method, architecture pattern, planning note, or example. |
| `external_framework` | External framework name. |
| `external_reference_id` | External framework section, control, category, or reference identifier where copyright-safe. |
| `external_reference_title` | Short copyright-safe reference title or summary. |
| `relationship_type` | `supports`, `related`, `partial`, `informative`, `gap`, or `not_equivalent`. |
| `mapping_rationale` | Short reason for the relationship. |
| `claim_boundary` | Explicit statement of what the mapping does not claim. |
| `evidence_relevance` | Whether AAEF evidence may support review of the external reference. |
| `assessment_relevance` | Whether AAEF assessment material may support review. |
| `limitations` | Known limitations, gaps, or context dependencies. |
| `review_status` | Draft, reviewed, deferred, needs legal review, or needs standards review. |

## Candidate enrichment targets

Future enrichment may prioritize:

| Target | Rationale |
| --- | --- |
| NIST AI RMF / Generative AI Profile | Useful for governance and risk framing. |
| OWASP LLM / GenAI / Agentic guidance | Useful for security and threat-model alignment. |
| CSA Agentic Trust or related cloud/security guidance | Useful for enterprise cloud and SaaS adoption. |
| ISO/IEC 42001 feasibility-level mapping | Useful only at conservative, copyright-safe, non-equivalence level. |
| EU AI Act support discussion | Should remain high-level and legal-review dependent. |

## Recommended next steps

Recommended next steps:

1. Review the detected CSV candidates and confirm which file should be enriched first.
2. Decide whether to create a dedicated mapping enrichment CSV or extend an existing one.
3. Define conservative relationship labels.
4. Add mapping rationale and limitations columns before adding many rows.
5. Add validation for required mapping columns if enrichment becomes structural.
6. Keep external framework mapping claims aligned with the Legal and Compliance Applicability Note.
7. Avoid mapping expansion that implies certification, legal compliance, or audit sufficiency.

## Acceptance criteria for this review

This review is sufficient when:

- current mapping CSV candidates are listed
- related mapping Markdown candidates are listed
- conservative enrichment principles are documented
- candidate enrichment columns are identified
- likely enrichment targets are identified
- no mapping CSV is modified
- no external compliance or equivalence claim is introduced
