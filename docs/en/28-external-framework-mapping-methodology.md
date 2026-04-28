# External Framework Mapping Methodology

## Status

This document is part of the AAEF v0.4.0 planning work.

It defines an informative mapping methodology for relating AAEF controls and assessment artifacts to external frameworks.

This document is informative and does not create a certification scheme, formal standard, implementation conformance claim, audit opinion, compliance equivalence, or claim of complete mitigation.

## Purpose

AAEF focuses on agentic AI action assurance: authority, enforcement, evidence, and auditability around agentic actions.

Enterprise users, assessors, and reviewers may need to understand how AAEF relates to existing governance, security, risk, and audit frameworks.

This document defines how AAEF should express such relationships without overstating equivalence or compliance coverage.

## Mapping Principles

AAEF external mappings should be:

- informative,
- transparent,
- scoped,
- version-aware,
- evidence-aware,
- and conservative.

Mappings must not claim:

- compliance equivalence,
- certification coverage,
- audit sufficiency,
- complete control coverage,
- formal standard alignment,
- or that implementing AAEF satisfies an external framework.

## Mapping Is Not Equivalence

A mapping indicates that an AAEF control, evidence concept, assessment artifact, or architectural pattern may support analysis of an external framework topic.

It does not mean:

- the external requirement is fully satisfied,
- all test procedures are covered,
- all implementation details are present,
- the mapped item is sufficient for audit,
- or that an assessor should treat AAEF as a replacement for the external framework.

## Mapping Relationship Types

AAEF mappings should use explicit relationship types.

### Supports

AAEF provides supporting control or evidence concepts that may help address the external topic.

### Partially Supports

AAEF addresses part of the external topic, but additional controls, processes, or evidence are required.

### Related

AAEF is conceptually related to the external topic but does not directly provide assessment support.

### Contextual

AAEF provides useful context, terminology, or architectural framing for the external topic.

### Not Equivalent

AAEF may look similar to the external topic, but the relationship should not be treated as equivalent.

### Out of Scope

The external topic is outside AAEF's intended scope.

## Mapping Confidence

Mappings may include confidence values.

Suggested values:

- `High`
- `Medium`
- `Low`
- `Needs Review`

Confidence should reflect the maturity of the mapping, not the quality of the external framework.

## Mapping Status

Mappings may use the following status values:

- `Draft`
- `Review Needed`
- `Reviewed`
- `Deprecated`
- `Superseded`

Initial mappings should generally be marked `Draft` or `Review Needed`.

## Required Mapping Fields

Machine-readable mapping artifacts should include:

- `Mapping ID`
- `External Framework`
- `External Version`
- `External Reference ID`
- `External Reference Title`
- `AAEF References`
- `AAEF Control IDs`
- `Relationship Type`
- `Mapping Confidence`
- `Mapping Status`
- `Mapping Rationale`
- `Limitations`
- `Notes`

## AAEF References

AAEF references may include:

- control IDs,
- document paths,
- schema fields,
- assessment profiles,
- testing procedures,
- evidence concepts,
- architecture components.

When possible, mappings should include stable AAEF control IDs.

## Control ID Handling

AAEF control IDs should be treated as stable identifiers.

Mappings should be reviewed when:

- a control requirement changes materially,
- a control is deprecated,
- a control is superseded,
- a new catalog baseline is introduced,
- or a mapping target changes.

This should be coordinated with:

- `docs/en/24-control-catalog-versioning.md`

## Evidence and Assessment Considerations

Mappings should distinguish between:

- conceptual support,
- control support,
- evidence support,
- testing procedure support,
- and audit support.

A mapping to an external framework topic is stronger when AAEF provides:

- relevant control requirements,
- testing procedures,
- evidence expectations,
- pass / partial / fail criteria,
- and traceable assessment artifacts.

## External Framework Versioning

Each mapping should identify the external framework version or publication context where possible.

If the external framework changes, the mapping should be reviewed.

Mappings should not silently carry forward across external framework versions.

## External Reference Identifiers

External Reference ID should use an official external framework identifier where a stable identifier is available.

If a mapping row uses a topic-level, profile-level, or AAEF-defined reference because a stable external identifier is not being used, the mapping should make this clear in the Mapping Rationale, Limitations, or Notes fields.

Such identifiers are mapping aids only.

They must not be presented as official external control IDs unless they are defined by the external framework.


## Initial Mapping Pack

The initial machine-readable mapping draft is:

- `mappings/aaef-external-framework-mapping-v0.4-draft.csv`

This initial pack is intentionally conservative.

It is intended to demonstrate mapping structure and provide a starting point for review, not to claim full alignment or compliance coverage.

## Non-Goals

This methodology does not define a compliance program.

It does not define a certification scheme.

It does not provide legal, audit, or regulatory advice.

It does not claim that AAEF satisfies any external framework.

It does not require every AAEF control to map to an external framework.

It does not require every external framework topic to be covered by AAEF.

## Open Questions

Future work should determine:

- which external frameworks should be prioritized,
- whether mappings should become more granular,
- whether external framework references should be mirrored in Markdown and CSV,
- whether mapping validation should require known framework identifiers,
- how to handle external framework copyright and quotation limits,
- how to represent mapping confidence changes over time,
- and how external mappings should be reviewed before release.
