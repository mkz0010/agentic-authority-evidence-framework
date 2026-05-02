# AAEF v0.6.x Conservative External Framework Mapping Enrichment Planning

Status: Conservative external framework mapping enrichment planning  
Related issue: #281  
Related roadmap: #241  
Related split plan: `docs/en/status/v060-adoption-follow-up-split-planning.md`  
Related mapping review: `docs/en/status/v060-external-framework-mapping-csv-enrichment-review.md`  
Related legal/compliance note: `docs/en/status/v060-legal-compliance-applicability-note-planning.md`  
Related version audit: `docs/en/status/v060-version-reference-audit.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document defines a conservative enrichment plan for AAEF external framework mapping.

The goal is to make AAEF easier to explain to enterprise, audit, compliance, risk, legal, security architecture, and research audiences without overstating what AAEF claims.

This document plans how mapping artifacts may be enriched while preserving clear claim boundaries.

It does not create equivalence, certification, compliance, audit sufficiency, conformity, or legal/regulatory claims.

## Why this matters

External framework mapping helps readers understand how AAEF relates to familiar materials.

However, mapping can create risk if readers interpret relationship rows as proof that AAEF:

- satisfies another framework,
- replaces another framework,
- certifies compliance,
- provides an audit opinion,
- creates conformity assessment,
- or establishes equivalence.

AAEF should avoid those claims.

The intended outcome is an informative relationship map, not a compliance crosswalk.

## Candidate external frameworks

Candidate mapping targets include:

| Framework / source family | Candidate mapping role |
| --- | --- |
| NIST AI RMF | Risk management, governance, measurement, and management context |
| ISO/IEC 42001 | AI management system and organizational governance context |
| OWASP Agentic / LLM risk materials | Agentic AI and LLM security risk context |
| MITRE ATLAS | Adversarial AI tactics, techniques, and threat modeling context |
| CSA AI Controls Matrix | Cloud AI security and governance control context |

The list is not exhaustive.

Each framework should be reviewed from official or primary sources where possible.

## Non-normative status

This document does not update:

- active controls,
- active evidence schema,
- active assessment artifacts,
- active mappings,
- mapping CSVs,
- testing procedures,
- examples,
- or the current control and assessment baseline.

Any future mapping enrichment must be implemented through a separate PR.

## Mapping claim boundaries

AAEF mapping language should not use the following meanings unless a future governance decision explicitly allows it:

- equivalent to,
- compliant with,
- certified against,
- satisfies,
- meets,
- conforms to,
- replaces,
- provides audit sufficiency for,
- proves legal compliance with,
- or provides conformity assessment for.

Preferred language:

- relates to,
- supports analysis of,
- may inform,
- provides evidence-relevant structure for,
- provides action-bound control context for,
- complements,
- can be compared with,
- is adjacent to,
- partially overlaps with,
- or is out of scope.

## Mapping relationship vocabulary

Recommended relationship vocabulary:

| Relationship | Meaning |
| --- | --- |
| `supports_analysis_of` | AAEF can help analyze the external topic. |
| `provides_action_boundary_context_for` | AAEF adds action-bound authorization/execution/evidence context. |
| `provides_evidence_context_for` | AAEF adds structured evidence or reconstruction context. |
| `partially_overlaps_with` | AAEF and the external source address related concerns but from different scopes. |
| `complements` | AAEF may be used alongside the external source. |
| `informs` | The external source informs AAEF review or positioning. |
| `not_equivalent` | Explicitly avoids equivalence. |
| `out_of_scope` | The external source topic is outside AAEF's current scope. |
| `deferred` | Mapping requires later review. |

Avoid relationship values such as:

- `meets`,
- `satisfies`,
- `complies_with`,
- `certifies`,
- `equivalent_to`,
- `conforms_to`.

## Mapping confidence levels

Recommended confidence levels:

| Level | Meaning |
| --- | --- |
| `high` | Strong textual and structural relationship, but still not equivalence. |
| `medium` | Clear conceptual relationship with scope limitations. |
| `low` | Weak or exploratory relationship. |
| `deferred` | Needs more review before mapping. |
| `not_applicable` | No useful relationship for current AAEF scope. |

Confidence is not compliance strength.

Confidence means confidence in the relationship explanation.

## Candidate mapping fields

A future enriched mapping CSV or table may use fields like:

| Field | Purpose |
| --- | --- |
| `mapping_id` | Stable mapping row identifier. |
| `external_framework` | Framework or source family name. |
| `external_version_or_date` | Version/date when available. |
| `external_reference_id` | Section, control, risk, category, tactic, technique, or item identifier. |
| `external_reference_title` | Human-readable title. |
| `aaef_reference_type` | Control, principle, threat, evidence schema, assessment artifact, planning artifact, or concept. |
| `aaef_reference_id` | AAEF reference identifier or path. |
| `relationship_type` | Conservative relationship vocabulary. |
| `relationship_confidence` | High, medium, low, deferred, or not_applicable. |
| `mapping_rationale` | Short explanation of relationship. |
| `scope_limitations` | What the mapping does not cover. |
| `claim_boundary` | Explicit non-equivalence / non-compliance boundary. |
| `review_status` | Draft, reviewed, deferred, or rejected. |
| `reviewer` | Reviewer or role. |
| `last_reviewed` | Review date. |
| `notes` | Additional notes. |

## Candidate mapping artifact options

Potential outputs:

| Option | Description | Initial disposition |
| --- | --- | --- |
| Enriched CSV | Machine-readable relationship rows | Preferred for future implementation |
| Narrative mapping note | Human-readable explanation | Useful companion |
| Mapping README | Explains claim boundaries and vocabulary | Recommended if CSV is added |
| Mapping validator | Validates required fields and forbidden claim terms | Recommended later |
| Framework-specific mapping docs | One document per framework | Defer until CSV structure stabilizes |

## Recommended initial enrichment strategy

Recommended first implementation approach:

1. Define mapping CSV field model.
2. Add mapping README with claim boundaries.
3. Add a small pilot mapping set.
4. Validate required fields.
5. Validate forbidden relationship terms.
6. Avoid framework equivalence or compliance language.
7. Keep mapping rows informative and reviewable.

Do not attempt a complete mapping in the first enrichment PR.

## Candidate target order

Recommended order:

1. NIST AI RMF
2. OWASP Agentic / LLM risk materials
3. MITRE ATLAS
4. ISO/IEC 42001
5. CSA AI Controls Matrix

Rationale:

- NIST AI RMF provides broad AI risk management context.
- OWASP Agentic / LLM materials connect directly to agentic AI risk language.
- MITRE ATLAS supports threat modeling and adversarial technique context.
- ISO/IEC 42001 supports management-system and governance context but should be handled carefully because certification/compliance misunderstanding risk is higher.
- CSA AI Controls Matrix may support cloud AI governance and control context but should be treated conservatively.

## Mapping review questions

Before adding enriched mappings, reviewers should ask:

- Is the external source official or primary?
- Is the referenced external version/date recorded?
- Is the AAEF reference active, planning, historical, or non-normative?
- Does the row imply equivalence?
- Does the row imply compliance?
- Does the row imply certification or audit sufficiency?
- Is the relationship type conservative?
- Are scope limitations explicit?
- Is claim-boundary language present?
- Is the mapping maintainable?

## Relationship to AAEF baseline

Mapping enrichment must preserve the version boundary:

- v0.6.0 is a planning and adoption-readiness release.
- v0.4.1 remains the current control and assessment baseline unless explicitly changed.
- v0.5.0 and v0.6.0 planning artifacts are non-normative unless explicitly promoted.
- Mapping rows may reference planning artifacts, but they must identify them as planning/non-normative where applicable.

## Suggested validation checks

A future mapping validator may check:

- required fields are present,
- forbidden relationship values are absent,
- claim-boundary field is populated,
- external framework name is from an allowed list,
- relationship confidence is from an allowed list,
- review status is from an allowed list,
- AAEF reference paths exist where applicable,
- active/planning/historical status is explicitly stated,
- no row uses forbidden terms such as `equivalent`, `compliant`, `certified`, or `satisfies`.

## Initial implementation recommendation

Recommended next PR after this planning document:

> Add an external mapping enrichment field model and a small pilot CSV with conservative relationship vocabulary and validation of required fields / forbidden terms.

Candidate future artifact names:

- `mappings/README.md`
- `mappings/external-framework-mapping.example.csv`
- `tools/validate_external_mappings.py`

Alternative future artifact names:

- `docs/en/mappings/README.md`
- `docs/en/mappings/external-framework-mapping.md`
- `mappings/external-framework-mapping.csv`

## Risks of premature mapping

| Risk | Why it matters |
| --- | --- |
| Equivalence confusion | Readers may treat mapping as proof that AAEF equals another framework. |
| Compliance overclaim | Legal/compliance reviewers may read mappings as compliance assertions. |
| Certification confusion | ISO/IEC 42001 or CSA-related rows may be misread as certification positioning. |
| Scope drift | AAEF may appear to cover topics outside action authority and evidence. |
| Version drift | External frameworks and AAEF releases may change over time. |
| Planning-active confusion | Rows may mix active and planning artifacts without clear status. |

## Claim-boundary text for future mapping artifacts

Future mapping artifacts should include language such as:

> AAEF external framework mappings are informative relationship mappings. They do not assert compliance, certification, audit sufficiency, conformity, or equivalence with external frameworks. Mapping rows describe conservative relationships between AAEF concepts/artifacts and external framework topics. They do not replace independent assessment against those external frameworks.

## Relationship to #281

This document addresses #281 by defining the conservative mapping enrichment approach.

#281 should remain open until one of the following occurs:

- a mapping enrichment field model is implemented,
- a pilot mapping artifact is added,
- or enrichment is explicitly deferred.

## Non-goals

This document does not:

- create enriched mapping rows,
- update existing mapping CSVs,
- add a mapping validator,
- claim compliance,
- claim certification,
- claim audit sufficiency,
- claim conformity,
- claim equivalence with external frameworks,
- update active controls,
- update the current control and assessment baseline,
- update evidence schema,
- update assessment artifacts,
- or update testing procedures.

## Acceptance criteria

This planning document is sufficient when:

- conservative mapping principles are documented,
- claim boundaries are explicit,
- candidate target frameworks are identified,
- mapping relationship vocabulary is proposed,
- confidence levels are defined,
- candidate mapping fields are documented,
- validation expectations are identified,
- implementation recommendation is provided,
- and no active baseline change is implied.
