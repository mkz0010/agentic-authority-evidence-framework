# Control Catalog Versioning and Change Impact Model

## Status

This document is part of the AAEF v0.4.0 planning work.

It defines versioning and change impact guidance for the AAEF control catalog.

This document is informative and does not create a certification scheme, formal standard, implementation conformance claim, audit opinion, or claim of complete mitigation.

## Purpose

The AAEF control catalog is intended to provide a stable machine-readable source of truth for control identifiers, objectives, applicability, testing procedures, evidence examples, and assessment support.

As AAEF evolves, control requirements may be added, clarified, reorganized, deprecated, or superseded.

This document defines how such changes should be described so that readers, implementers, assessors, and mapping users can understand the impact of control catalog changes.

## Current Control Catalog Source of Truth

The current machine-readable control catalog file remains:

- `controls/aaef-controls-v0.1.csv`

The file name is retained for continuity.

Unless superseded by a later catalog file, this file remains the source of truth for the current public review control set.

The release version of AAEF and the file name of the control catalog are related but not identical.

For example, an AAEF public review release may update documentation, evidence guidance, assessment methodology, or release metadata without changing the catalog file name.

## Versioning Principles

AAEF should distinguish between:

- framework release versions,
- control catalog file versions,
- control identifiers,
- assessment artifacts,
- and external mapping artifacts.

These artifacts may evolve at different rates.

### Framework Release Version

Framework release versions describe the published state of the AAEF repository.

Examples:

- `v0.3.0 Public Review Draft`
- `v0.3.1 Maintenance Release`
- future `v0.4.0 Public Review Draft`

A framework release may include documentation, schema, examples, assessments, mappings, issue planning, or repository maintenance changes.

A framework release does not necessarily imply that the control catalog file name has changed.

### Control Catalog File Version

The control catalog file version refers to the machine-readable catalog file.

Example:

- `controls/aaef-controls-v0.1.csv`

The catalog file name should change only when there is a meaningful need to introduce a new catalog baseline or compatibility boundary.

Minor documentation clarification around the catalog does not require a new catalog file name.

### Control Identifier Stability

Control IDs should be treated as stable identifiers once published in a public review release.

Control IDs should not be reused for different control meanings.

If a control is removed, replaced, or materially redefined, the change should be documented using change impact categories.

## Change Impact Categories

AAEF should classify control catalog changes using the following categories.

### Editorial

Editorial changes do not change the control meaning.

Examples:

- grammar fixes,
- formatting fixes,
- wording improvements that do not change control intent,
- clarification of examples without changing requirements.

Expected impact:

- no assessment migration required,
- no mapping migration required,
- no control ID change required.

### Clarification

Clarification changes explain existing intent more clearly but do not materially expand or reduce the control requirement.

Examples:

- clarifying evidence expectations,
- clarifying applicability wording,
- clarifying terms already used elsewhere in AAEF.

Expected impact:

- assessment interpretation may improve,
- existing mappings may remain valid,
- review notes may be useful.

### Minor Requirement Change

Minor requirement changes adjust control wording or expectations without changing the core control objective.

Examples:

- adding a narrow evidence example,
- refining applicability conditions,
- tightening an assessment note.

Expected impact:

- assessment worksheets may need updates,
- testing procedures may need review,
- external mappings may need confirmation.

### Major Requirement Change

Major requirement changes materially change the control meaning, assessment expectations, or implementation implications.

Examples:

- changing the control objective,
- adding a new required control behavior,
- changing applicability in a way that affects assessed systems,
- substantially changing evidence expectations.

Expected impact:

- assessment worksheets should be updated,
- testing procedures should be updated,
- external mappings should be reviewed,
- migration notes should be provided.

### New Control

A new control introduces a new control ID and control requirement.

Expected impact:

- control catalog update required,
- Markdown control list update required,
- assessment worksheet update required,
- testing procedure update required,
- mapping review required.

### Deprecated Control

A deprecated control remains visible for historical continuity but is no longer recommended for future assessment use.

Expected impact:

- deprecation rationale should be documented,
- replacement control should be identified where possible,
- mappings should be updated,
- assessment guidance should indicate how to treat the deprecated control.

### Superseded Control

A superseded control has been replaced by another control or set of controls.

Expected impact:

- superseding control IDs should be listed,
- migration guidance should be provided,
- external mappings should be updated,
- historical references should remain traceable.

### Removed Control

A removed control is no longer part of the current catalog.

Removal should be rare.

Expected impact:

- removal rationale should be documented,
- historical releases should remain available,
- mappings and assessment artifacts should be updated.

## Control Catalog Change Record

For future catalog changes, AAEF should maintain a change record that includes:

- release version,
- catalog file version,
- control ID,
- change impact category,
- summary of change,
- migration note,
- affected artifacts,
- mapping impact,
- assessment impact.

A future machine-readable change log may use fields such as:

- `release_version`
- `catalog_file`
- `control_id`
- `change_type`
- `change_summary`
- `assessment_impact`
- `mapping_impact`
- `migration_note`
- `superseded_by`
- `notes`

## Relationship to Assessment Artifacts

Assessment artifacts depend on stable control identifiers.

Affected artifacts may include:

- assessment worksheet,
- assessment profile mapping,
- testing procedures,
- evidence quality criteria,
- external framework mappings,
- implementation examples.

When a control change is classified as a Minor Requirement Change, Major Requirement Change, New Control, Deprecated Control, Superseded Control, or Removed Control, dependent assessment artifacts should be reviewed.

## Relationship to External Mappings

External framework mappings depend on stable control meaning.

AAEF mappings should be treated as informative aids.

They must not claim:

- compliance equivalence,
- certification coverage,
- audit sufficiency,
- complete control coverage,
- or formal standard alignment.

When a control changes materially, mappings should be reviewed to determine whether the relationship remains valid.

Mapping impact may be classified as:

- no impact,
- review recommended,
- mapping update required,
- mapping deprecated,
- mapping superseded.

## Relationship to Testing Procedures

Testing procedures should be reviewed when a control requirement changes.

Potential impacts include:

- required evidence changes,
- sampling approach changes,
- pass criteria changes,
- partial or fail criteria changes,
- reviewer judgment boundaries change,
- automation suitability changes.

This document should be coordinated with future measurable testing procedure and pass criteria work.

## Recommended Change Workflow

For future control catalog changes, AAEF should follow a workflow similar to:

1. identify proposed control change,
2. classify change impact,
3. update the machine-readable control catalog,
4. update the Markdown control list,
5. update assessment worksheet or mapping artifacts if needed,
6. update testing procedures if needed,
7. update external mappings if needed,
8. update changelog or migration notes,
9. run validation scripts,
10. document the change in the release notes.

## Non-Goals

This document does not define a complete conformance program.

It does not define certification criteria.

It does not assert that any external framework requirement is satisfied by AAEF controls.

It does not require every documentation-only release to create a new control catalog file.

## Open Questions

Future work should determine:

- when the catalog file should move from `aaef-controls-v0.1.csv` to a later file name,
- whether a machine-readable control change log should be added,
- how external mappings should reference control catalog versions,
- how testing procedures should declare compatibility with catalog versions,
- how deprecated or superseded controls should appear in assessment worksheets.
