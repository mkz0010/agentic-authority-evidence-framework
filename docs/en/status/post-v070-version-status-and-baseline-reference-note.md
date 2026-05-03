# Post-v0.7.0 Version Status and Baseline Reference Note

## Purpose

This document clarifies how to read version, latest-status, and baseline references after completion of the v0.7.0 roadmap.

AAEF uses different "latest" references depending on the review purpose.

This note is intended to prevent stale or ambiguous version wording in entry-point documents while preserving historical planning artifacts, release preparation materials, and versioned file names.

This document is explanatory status material only. It does not change the active control and assessment baseline, update the control catalog, update the evidence schema, update assessment artifacts, update testing procedures, publish a release, or create a certification, compliance, audit, legal, implementation-conformance, or external-framework-equivalence claim.

## Summary

As of the completion of v0.7.0 roadmap work:

| Reference purpose | Current reference |
| --- | --- |
| Latest completed planning roadmap | v0.7.0 |
| Latest v0.7.0 roadmap wrap-up artifact | `docs/en/status/v070-roadmap-wrap-up-and-release-readiness-note.md` |
| Latest completed v0.7.0 child tracks | #319, #320, #321, #322, and #323 |
| Latest published planning release | Determined by GitHub Releases / tags; v0.7.0 roadmap completion does not by itself create a new published release. |
| Current active control and assessment baseline | Not changed by v0.7.0. It changes only when a later release explicitly updates the control catalog, evidence schema, assessment artifacts, testing procedures, or related baseline artifacts. |
| Future v1.0.0 path | Not current, not active, and not a baseline yet. It should be handled through separate roadmap or release-planning work. |

## Why "latest" must be qualified

AAEF has several kinds of versioned materials:

- public review baselines,
- planning releases,
- planning roadmaps,
- status and coordination artifacts,
- release preparation checklists,
- assessment artifacts,
- schema artifacts,
- examples,
- validators,
- mapping artifacts, and
- historical design notes.

A statement that something is "latest" should clarify what kind of latest status it means.

For example:

- "latest completed planning roadmap" is not the same as "latest published GitHub Release";
- "latest planning artifact" is not the same as "active control and assessment baseline";
- "latest reviewability material" is not the same as "normative control requirement";
- "future v1.0.0 path" is not the same as "current baseline."

## Current recommended wording

Use this wording when a document needs to summarize current state:

> The latest completed planning roadmap is v0.7.0.
>
> v0.7.0 completed the Evaluation Readiness, Implementation Reviewability, Research Positioning, Operational Reconstruction, and Risk-Owner Decision Support tracks.
>
> v0.7.0 does not automatically change the active control and assessment baseline.
>
> The active baseline changes only when a later release explicitly updates the control catalog, evidence schema, assessment artifacts, testing procedures, or related baseline artifacts.

Use this wording when distinguishing roadmap completion from release publication:

> v0.7.0 roadmap work has been completed, but roadmap completion is not the same as publishing a new release.
>
> Published-release status should be determined by GitHub Releases, tags, release notes, and explicit release artifacts.

Use this wording when discussing v1.0.0:

> Future v1.0.0 path planning should decide whether and how to update the active baseline, control catalog, evidence schema, assessment artifacts, examples, validators, adoption guidance, and public communication posture.
>
> v1.0.0 should not be described as current, active, or baseline until a later release explicitly makes that change.

## Historical artifact handling

Versioned historical artifact names should generally remain unchanged.

Examples include:

- `v050x-*` status files,
- `v060-*` planning files,
- `v070-*` planning and wrap-up files,
- release preparation checklists,
- older planning overview files,
- prior public review draft references, and
- historical release notes or citation examples.

These names describe when and why the artifact was created.

They should not be bulk-renamed merely because a later roadmap completed.

## When to update old wording

Old wording should be updated when it makes a current-state claim that is no longer accurate or is likely to confuse readers.

Examples of wording that should be reviewed:

- "latest public review planning release",
- "current planning milestone",
- "current roadmap",
- "active follow-up work",
- "current status",
- "current baseline",
- "remains current",
- "latest release",
- "current public review draft", and
- "latest planning release."

These phrases are safe only when their reference purpose is clear.

## Entry-point document expectations

Entry-point documents should point readers to this note or an equivalent current status reference when they mention version status.

Entry-point documents include:

- `README.md`,
- localized README files,
- `docs/en/document-map.md`,
- `docs/en/status/README.md`,
- `docs/en/55-researcher-overview.md`, and
- other overview or adoption entry points.

They do not need to repeat every historical version detail.

## Active baseline boundary

v0.7.0 does not change the active control and assessment baseline by itself.

Planning, reviewability, reconstruction, and decision-support artifacts may be newer than the active baseline, but they do not automatically replace it.

A baseline change should be explicit and should identify which artifacts are updated, such as:

- control catalog,
- evidence schema,
- assessment worksheet,
- assessment profiles,
- testing procedures,
- examples,
- validators,
- mappings, or
- release notes.

## Public communication posture

Public communication should avoid presenting v0.7.0 as:

- a new certification scheme,
- a compliance claim,
- a legal sufficiency claim,
- an audit sufficiency claim,
- an operational readiness claim,
- a production readiness claim,
- an implementation conformance claim,
- an empirical validation claim,
- an external-framework equivalence claim, or
- an active baseline replacement.

The safer public posture is:

- v0.7.0 completed major planning and reviewability roadmap work;
- v0.7.0 clarified evaluation readiness, implementation reviewability, research positioning, operational reconstruction, and risk-owner decision support;
- v0.7.0 preserved the active baseline boundary; and
- future v1.0.0 path planning should determine what, if anything, is promoted into a stable baseline.

## Review questions

Reviewers should be able to answer:

- Does the document distinguish latest completed roadmap from latest published release?
- Does the document distinguish planning material from active baseline?
- Does the document avoid implying that v0.7.0 updates the control catalog, schema, assessment artifacts, or testing procedures?
- Does the document avoid implying that v1.0.0 is already current or active?
- Does the document preserve historical versioned artifact names where they are descriptive?
- Does the document update or qualify current-state claims that could mislead readers?

## Scope reminder

This note is status and reference material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, or GitHub Releases.

It does not establish operational readiness, production readiness, implementation conformance, empirical validation, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, or external-framework equivalence.
