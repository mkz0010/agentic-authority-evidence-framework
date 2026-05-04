# v1.0.0 Control ID Stability Note

## Purpose

This document records the control ID stability posture for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- `docs/en/status/v100-control-catalog-readiness-review.md`
- `docs/en/status/v100-baseline-artifact-readiness-review.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`

The goal is to make control ID stability reviewable before any future v1.0.0 baseline or control catalog decision.

This document is readiness-review material only. It does not update the active baseline, control catalog, evidence schema, assessment artifacts, testing procedures, examples, fixtures, validators, release tags, or GitHub Releases.

## Stability posture

The recommended posture is:

> Preserve existing control IDs by default for the v1.0.0 path.
>
> Do not renumber, rename, split, merge, or repurpose control IDs unless a later dedicated control catalog update explicitly decides to do so.
>
> Treat control ID stability as a traceability and reviewability safeguard.

This posture supports v1.0.0 planning without creating unnecessary baseline churn.

## Why control ID stability matters

Control IDs are not just labels.

They may be referenced by:

- control catalog rows,
- control requirement documentation,
- evidence schema discussion,
- assessment quick start material,
- assessment worksheets,
- assessment profiles,
- testing procedures,
- examples and fixtures,
- validators,
- external mappings,
- document map entries,
- README or overview documents,
- status artifacts,
- release notes,
- historical issue and PR discussions, and
- users' local notes or implementation plans.

Changing control IDs can therefore affect traceability even when the underlying control concept is unchanged.

## Stability principles

Control ID decisions should follow these principles:

1. Preserve existing IDs unless there is a strong reviewable reason to change them.
2. Do not use renumbering as a cosmetic cleanup step.
3. Do not repurpose an existing ID to mean something materially different.
4. Prefer wording clarification over ID change when the control concept remains stable.
5. Prefer append-only additions over insertion-based renumbering if new controls are later required.
6. Prefer guidance or examples over new controls when the concept is not mature enough for baseline inclusion.
7. Preserve historical references even when newer guidance supersedes older wording.
8. Treat deleted, merged, or split controls as baseline-impacting changes requiring separate review.

## Current recommendation

For the current #357 stage, the recommendation is:

- keep existing control IDs stable;
- do not introduce new control IDs in this track;
- do not renumber existing controls;
- do not merge or split controls;
- do not repurpose control IDs;
- document any future control ID change proposal separately; and
- handle mature v0.7.0 materials first as stable guidance candidates rather than automatic control additions.

This recommendation is consistent with `docs/en/status/v100-control-catalog-readiness-review.md`, which recommends preserving the current control catalog by default while reviewing targeted wording changes or later control additions separately.

## Control ID change categories

| Change category | Description | v1.0.0 readiness posture |
| --- | --- | --- |
| No ID change | Existing IDs remain unchanged. | Preferred default. |
| Wording clarification only | Control wording changes but ID and control meaning remain stable. | Possible later, but requires targeted review. |
| New appended control | New control is added without changing existing IDs. | Possible later if mature and separately scoped. |
| Renumbering | Existing IDs are changed for ordering or structure. | Avoid unless strongly justified. |
| Repurposing | Existing ID is reused for a materially different requirement. | Avoid. |
| Splitting | One control becomes multiple controls. | Baseline-impacting; requires separate review. |
| Merging | Multiple controls become one control. | Baseline-impacting; requires separate review. |
| Deprecation | A control is marked historical or no longer active. | Baseline-impacting; requires explicit decision. |

## Preferred approach for new concepts

Mature v0.7.0 concepts should not automatically become new controls.

Recommended ordering:

1. Preserve as planning material.
2. Review as stable guidance candidate.
3. Review relationship to existing controls.
4. Decide whether wording clarification is enough.
5. Decide whether examples, assessment guidance, or testing procedures are more appropriate.
6. Only then consider new control additions.

This is especially relevant for:

- evidence gap classification,
- operational reconstruction,
- risk-owner decision support,
- residual uncertainty handling,
- decision package checklist,
- decision matrix,
- component responsibility review,
- validator scope boundaries, and
- prototype/reference boundary guidance.

## Append vs insertion

If new controls are later required, append-only additions should be preferred over insertion-based renumbering.

Rationale:

- appending preserves historical references;
- appending reduces document-map churn;
- appending reduces assessment worksheet churn;
- appending reduces external mapping churn;
- appending reduces validator and example update burden;
- appending makes the change easier to review; and
- appending avoids implying that older references were invalid.

Insertion-based renumbering should be avoided unless the repository deliberately accepts the cost of updating all dependent artifacts.

## Repurposing warning

An existing control ID should not be reused to mean something materially different.

Repurposing creates a traceability risk because older references may appear to point to the same control while actually pointing to a changed requirement.

If a control concept changes materially, prefer:

- a wording change with explicit migration note,
- a new appended control,
- a deprecation note,
- a historical reference note, or
- a dedicated baseline update decision.

## Dependency impact of control ID changes

| Dependent artifact family | Impact of control ID change |
| --- | --- |
| Control catalog | Requires row update, historical traceability, and validation. |
| Control requirement docs | Requires link and reference updates. |
| Evidence schema docs | May require mapping or expectation updates. |
| Assessment worksheets | Requires control reference updates. |
| Assessment profiles | May require profile coverage updates. |
| Testing procedures | Requires procedure mapping updates. |
| Examples and fixtures | May require control reference updates. |
| Validators | May require expected ID list or mapping updates. |
| External mappings | Requires mapping row review and claim-boundary review. |
| Document map | May require navigation and description updates. |
| README / overview | May require baseline wording updates. |
| Release notes | Must disclose ID changes clearly. |
| Historical artifacts | Should remain historically accurate and not be rewritten to hide the change. |

## Control ID stability checklist

Before any future control ID change, reviewers should ask:

- What problem does the ID change solve?
- Can the problem be solved by wording clarification instead?
- Can the concept be handled as guidance instead of a new control?
- Can the concept be handled as an example, assessment note, or testing procedure?
- Does the change alter the active baseline?
- Which artifacts reference the affected ID?
- Which validators or examples depend on the ID?
- Which mappings depend on the ID?
- How will historical references remain understandable?
- How will release notes explain the change?
- Does the change preserve conservative claim boundaries?
- Does the change avoid certification, compliance, audit, legal, conformance, and equivalence claims?

## Baseline update relationship

Control ID changes are baseline-relevant.

A future v1.0.0 baseline decision should explicitly state whether:

- the control catalog is unchanged;
- control wording is clarified without ID changes;
- new controls are appended;
- controls are split, merged, deprecated, or renumbered; or
- control catalog changes are deferred beyond v1.0.0.

Until that explicit decision exists, the safe posture is to preserve current control IDs.

## Release communication relationship

If a future v1.0.0 release changes control IDs, release communication should include:

- what changed,
- why it changed,
- whether the active baseline changed,
- whether old IDs remain historical references,
- whether mappings changed,
- whether assessment artifacts changed,
- whether validators changed,
- whether examples changed, and
- what claims are not being made.

If v1.0.0 preserves control IDs, release communication should still say so if the release discusses baseline stability.

## Claim boundaries

This note does not claim:

- v1.0.0 release,
- active baseline update,
- control catalog update,
- control ID update,
- control wording update,
- evidence schema update,
- assessment artifact update,
- testing procedure update,
- example or fixture coverage,
- validator sufficiency,
- operational readiness,
- production readiness,
- implementation conformance,
- empirical validation,
- peer-reviewed acceptance,
- certification,
- compliance,
- conformity,
- audit sufficiency,
- legal sufficiency,
- automated risk acceptance,
- control conformance, or
- external-framework equivalence.

## Initial decision

The initial decision for #357 is:

> Preserve current control IDs by default for v1.0.0 planning.
>
> Treat any future control ID change as a baseline-relevant change requiring separate review.
>
> Prefer guidance, examples, assessment support, or appended controls over renumbering or repurposing.
>
> Do not treat this note as a control catalog update.

## Recommended follow-up work

Recommended #357 follow-up candidates after this note:

- baseline update decision options,
- control catalog and baseline artifact close-readiness checklist.

Recommended later roadmap #350 tracks:

- evidence schema, examples, and validator readiness review,
- assessment artifact and testing procedure readiness review,
- implementation and adoption guidance readiness review,
- release readiness and communication planning,
- final v1.0.0 release decision.

## Review questions

Reviewers should be able to answer:

- Does this note preserve control ID stability?
- Does it avoid implicitly updating the active baseline?
- Does it clarify why control ID changes are baseline-relevant?
- Does it identify dependencies affected by ID changes?
- Does it prefer guidance or append-only additions over renumbering?
- Does it prevent repurposing existing IDs?
- Does it preserve historical traceability?
- Does it preserve claim boundaries?
- Does it provide enough direction for future baseline update options?

## Scope reminder

This artifact is readiness-review material only.

It does not update the active control and assessment baseline, control catalog, control IDs, control wording, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, GitHub Releases, README release posture, or citation status.

It does not establish operational readiness, production readiness, implementation conformance, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
