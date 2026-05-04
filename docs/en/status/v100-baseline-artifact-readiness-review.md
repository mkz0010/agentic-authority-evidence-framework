# v1.0.0 Baseline Artifact Readiness Review

## Purpose

This document reviews baseline-related artifact readiness for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- `docs/en/status/v100-control-catalog-readiness-review.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- `docs/en/status/post-v070-version-status-and-baseline-reference-note.md`

The goal is to review which artifact families are baseline-relevant, which are ready for v1.0.0 planning, which require separate readiness tracks, and which must remain planning-only, historical, or future work.

This document is readiness-review material only. It does not update the active baseline, control catalog, evidence schema, assessment artifacts, testing procedures, examples, fixtures, validators, release tags, or GitHub Releases.

## Current posture

As of this review:

- v1.0.0 path planning is active under roadmap #350.
- #351 completed baseline-scope and promotion-decision planning.
- #357 is reviewing control catalog and baseline artifact readiness.
- `docs/en/status/v100-control-catalog-readiness-review.md` recommends preserving the current control catalog by default while reviewing targeted wording changes or later control additions separately.
- The active control and assessment baseline has not been changed by #351, #357, or this artifact.
- Any future v1.0.0 baseline change must be explicit.

## Review posture

The recommended posture is:

> Treat baseline artifacts as a coordinated set.
>
> Do not update one baseline-relevant artifact implicitly without reviewing its relationship to the control catalog, evidence schema, assessment artifacts, testing procedures, examples, validators, and release communication.
>
> Keep v1.0.0 usable by clarifying artifact relationships before changing baseline content.

This supports v1.0.0 readiness while avoiding uncontrolled baseline drift.

## Baseline artifact families

For v1.0.0 planning, baseline-relevant artifact families include:

- control catalog,
- evidence schema,
- assessment quick start,
- assessment worksheets,
- assessment profiles,
- testing procedures,
- examples and fixtures,
- validators,
- external mappings,
- README and overview entry points,
- document map,
- status reference notes,
- release notes and citation material.

Not every artifact family must become part of the active baseline.

Some may remain stable guidance, review support, planning material, historical material, or future work.

## Readiness summary

| Artifact family | Current readiness posture | v1.0.0 implication |
| --- | --- | --- |
| Control catalog | Reviewed in `v100-control-catalog-readiness-review.md`; preserve by default. | Baseline-relevant; any update must be explicit. |
| Evidence schema | Review-readiness candidate. | Requires separate evidence schema readiness review before baseline update. |
| Assessment quick start | Review-readiness candidate. | Requires alignment review against baseline posture. |
| Assessment worksheets | Review-readiness candidate. | Requires consistency review if controls or schema change. |
| Assessment profiles | Review-readiness candidate. | Requires alignment review with v1.0.0 scope. |
| Testing procedures | Review-readiness candidate. | Requires specificity and claim-boundary review. |
| Examples and fixtures | Review-readiness candidate. | Requires minimum example set decision if used for v1.0.0 usability. |
| Validators | Scope-bounded readiness candidate. | Require validator scope review; passing validators must not imply conformance. |
| External mappings | Contextual reference only. | May support orientation but not equivalence or compliance. |
| README and overview entry points | Readiness candidate. | Should be updated later only after release posture is defined. |
| Document map | Current navigation support. | Should remain consistent with artifact additions. |
| Status reference notes | Useful current-state references. | Support planning traceability but do not replace baseline artifacts. |
| Release notes and citation material | Not ready until release decision. | Requires later release-readiness track. |

## Control catalog relationship

The control catalog is baseline-relevant and should be treated as the central control artifact.

Readiness posture:

- Preserve the current control catalog by default.
- Do not change control IDs implicitly.
- Do not change control wording without targeted review.
- Do not convert planning concepts into controls automatically.
- Treat mature v0.7.0 reconstruction and risk-owner decision materials as stable guidance candidates before considering control-level promotion.

Dependency considerations:

- Any control catalog update may require review of evidence schema, assessment artifacts, testing procedures, examples, validators, mappings, README, and release notes.
- If the control catalog is unchanged, v1.0.0 may still improve guidance, navigation, and release communication without changing the active baseline.

## Evidence schema relationship

The evidence schema is baseline-relevant if v1.0.0 claims a stable action-evidence structure.

Readiness questions:

- Does the current schema represent action, authority, execution, evidence, and review context sufficiently?
- Does it support non-execution, denial, hold, and blocked-action cases?
- Does it support evidence gap classification and operational reconstruction expectations?
- Does it support risk-owner decision package needs?
- Are schema fields stable enough for v1.0.0?
- Are examples aligned with schema expectations?
- Are validators clearly bounded to structural and scoped consistency checks?

Initial readiness posture:

- Evidence schema requires a separate readiness review.
- This artifact does not update the schema.
- Schema validity must not be presented as evidence sufficiency, implementation conformance, or operational assurance.

## Assessment artifact relationship

Assessment artifacts are baseline-relevant if v1.0.0 claims usable assessment support.

Assessment artifact families include:

- assessment quick start,
- assessment worksheet,
- assessment profiles,
- testing procedures,
- pass/fail criteria,
- reviewer evidence request guidance.

Readiness questions:

- Are assessment artifacts aligned with the control catalog?
- Are assessment artifacts aligned with evidence schema expectations?
- Do pass/fail criteria distinguish evidence presence from evidence sufficiency?
- Do testing procedures cover non-execution and blocked-action cases where relevant?
- Do assessment artifacts avoid certification, compliance, audit sufficiency, and legal sufficiency claims?
- Do assessment artifacts preserve reviewer judgment?

Initial readiness posture:

- Assessment artifacts require a separate readiness review.
- This artifact does not update assessment artifacts.
- Assessment support must remain distinct from certification, compliance, audit sufficiency, or legal sufficiency.

## Testing procedure relationship

Testing procedures connect control expectations to reviewable evidence.

Readiness questions:

- Are testing procedures specific enough for v1.0.0 use?
- Are they traceable to controls?
- Do they preserve action-bound evidence expectations?
- Do they avoid implying production readiness?
- Do they avoid implementation conformance claims?
- Do they align with validators and examples without overclaiming either?

Initial readiness posture:

- Testing procedures require a separate readiness review.
- This artifact does not update testing procedures.
- Testing support must remain scope-bounded.

## Examples and fixture relationship

Examples and fixtures can make v1.0.0 more usable.

They should not be mistaken for complete coverage or production readiness.

Readiness questions:

- What is the minimum example set needed for v1.0.0 usability?
- Are permitted, denied, non-executed, and held actions represented clearly enough?
- Are high-impact examples represented carefully?
- Are evidence gap examples needed?
- Are reconstruction examples needed?
- Are risk-owner decision package examples needed?
- Are examples clearly marked as illustrative or scoped fixtures?
- Do examples avoid implying production readiness or complete scenario coverage?

Initial readiness posture:

- Examples and fixtures require a separate readiness review.
- This artifact does not add examples or fixtures.
- Examples should support explanation and validation, not production assurance.

## Validator relationship

Validators support repository artifact consistency.

They do not prove operational correctness.

Readiness questions:

- What do current validators check?
- What do current validators intentionally not check?
- Are validator outputs clearly described in release or README language?
- Are validator failures actionable?
- Are validator successes bounded?
- Should v1.0.0 introduce additional validators?
- Would any new validator create false assurance?

Initial readiness posture:

- Validator readiness requires a separate review.
- Passing validators must not imply implementation conformance, operational readiness, evidence sufficiency, semantic correctness, or control conformance.
- Semantic validators should remain future work unless narrowly scoped.

## External mapping relationship

External mappings can provide orientation but must remain conservative.

Readiness questions:

- Are mappings clearly contextual?
- Do mappings avoid equivalence claims?
- Do mappings avoid compliance claims?
- Do mappings avoid substitution claims?
- Are mapping claims traceable and cautious?
- Do mappings require update if baseline artifacts change?

Initial readiness posture:

- External mappings are contextual references only.
- They do not establish compliance, equivalence, conformity, or certification.
- Mapping readiness may require later wording review.

## README and entry-point relationship

README and overview documents are not baseline artifacts by themselves, but they strongly shape reader interpretation.

Readiness questions:

- Do entry points distinguish latest completed roadmap from published release status?
- Do they distinguish active baseline from planning artifacts?
- Do they point to current baseline/status reference material?
- Do they avoid stale latest/current wording?
- Do they avoid presenting planning-only artifacts as baseline?
- Do they present a usable reading path?
- Do they preserve non-goals?

Initial readiness posture:

- README and entry-point updates should come later, after v1.0.0 release posture is clearer.
- This artifact does not update entry-point wording.

## Document map and status reference relationship

The document map and status README support discoverability.

Readiness questions:

- Are newly added status artifacts registered?
- Are historical and planning artifacts clearly positioned?
- Are v1.0.0 planning artifacts discoverable?
- Are baseline-relevant artifacts easy to find?
- Does navigation avoid implying that all status artifacts are active baseline?

Initial readiness posture:

- Document map and status README should continue to be updated as artifacts are added.
- They support navigation and traceability but do not define the active baseline by themselves.

## Release notes and citation relationship

Release notes and citation materials should not be updated prematurely.

Readiness questions:

- Does v1.0.0 publish a release?
- Does it update the active baseline?
- Which artifacts are promoted?
- Which artifacts remain planning-only?
- Which artifacts remain historical?
- Which domains are deferred?
- What validation was performed?
- What validation limits must be stated?
- What claims are explicitly not made?

Initial readiness posture:

- Release notes and citation updates should wait for a later release-readiness track.
- This artifact does not publish, tag, or cite v1.0.0 as released.

## Baseline artifact dependency matrix

| Change type | Likely dependent reviews |
| --- | --- |
| Control catalog wording change | Evidence schema, assessment artifacts, testing procedures, mappings, README, release notes. |
| Control ID change | Document map, worksheets, mappings, examples, validators, citations, historical references. |
| Evidence schema change | Examples, validators, assessment artifacts, testing procedures, README, release notes. |
| Assessment artifact change | Control catalog alignment, evidence schema alignment, testing procedures, examples. |
| Testing procedure change | Control wording, assessment criteria, evidence expectations, examples. |
| Example or fixture change | Schema validation, example validation, README guidance, validator wording. |
| Validator change | Release gate wording, README wording, claim-boundary review. |
| External mapping change | Claim-boundary review, mapping validation, README/release wording. |
| Release note change | Baseline status, version status, public communication, citation wording. |

## Baseline update options

This review leaves multiple options open.

### Option A: No baseline artifact update for v1.0.0

Meaning:

- v1.0.0 may focus on stable guidance, navigation, and release communication.
- Active baseline artifacts remain unchanged.

Benefits:

- Low risk of baseline drift.
- Easier release path.
- Preserves existing control and schema stability.

Risks:

- v1.0.0 may appear less substantive as a baseline release.

### Option B: Control catalog preserved, guidance promoted

Meaning:

- Control catalog remains unchanged.
- Mature v0.7.0 reconstruction and risk-owner decision materials are promoted as stable guidance.

Benefits:

- Improves usability without changing control baseline.
- Preserves control ID stability.

Risks:

- Requires careful wording to distinguish guidance from baseline.

### Option C: Targeted baseline artifact wording updates

Meaning:

- Select baseline-relevant artifacts receive wording clarifications.
- Control IDs and major structures remain stable.

Benefits:

- Improves clarity.
- Can align baseline wording with v1.0.0 posture.

Risks:

- Requires careful coordination across artifacts.

### Option D: Broader baseline update

Meaning:

- Control catalog, evidence schema, assessment artifacts, or testing procedures are updated.

Benefits:

- More ambitious v1.0.0 baseline.

Risks:

- High coordination cost.
- Requires additional validators, examples, mappings, release notes, and claim-boundary review.
- May delay v1.0.0.

## Initial recommendation

The initial recommendation is:

> Treat baseline artifact readiness as coordinated release planning.
>
> Preserve the current control catalog by default.
>
> Review evidence schema, examples, validators, assessment artifacts, and testing procedures in separate follow-up tracks before any baseline update.
>
> Use mature v0.7.0 materials as stable guidance candidates rather than automatically promoting them into baseline artifacts.
>
> Delay README, citation, and release-note updates until v1.0.0 release posture is clearer.

This keeps v1.0.0 planning useful without creating implicit baseline changes.

## Follow-up candidates for #357

Recommended #357 follow-up candidates:

- control ID stability note,
- baseline update decision options,
- control catalog and baseline artifact close-readiness checklist.

Optional follow-up candidates:

- baseline artifact dependency register,
- baseline wording review checklist,
- current baseline statement audit.

## Follow-up candidates for roadmap #350

Recommended later roadmap tracks:

- evidence schema, examples, and validator readiness review,
- assessment artifact and testing procedure readiness review,
- implementation and adoption guidance readiness review,
- release readiness and communication planning,
- final v1.0.0 release decision.

## Claim boundaries

This review does not claim:

- v1.0.0 release,
- active baseline update,
- control catalog update,
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

## Review questions

Reviewers should be able to answer:

- Does this review identify baseline-relevant artifact families?
- Does it avoid changing the active baseline implicitly?
- Does it clarify relationships among controls, schema, assessment, testing, examples, and validators?
- Does it identify which artifacts need separate readiness tracks?
- Does it preserve v1.0.0 claim boundaries?
- Does it avoid premature README, citation, or release-note updates?
- Does it provide enough direction for later #357 artifacts?

## Scope reminder

This artifact is readiness-review material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, GitHub Releases, README release posture, or citation status.

It does not establish operational readiness, production readiness, implementation conformance, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
