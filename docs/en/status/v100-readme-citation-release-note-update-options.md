# v1.0.0 README, Citation, and Release Note Update Options

## Purpose

This document records README, citation, and release-note update options for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #380, `[Track] v1.0.0: Release Readiness and Communication Planning`
- `docs/en/status/v100-release-readiness-review.md`
- `docs/en/status/v100-release-communication-boundary-note.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- completed track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`
- completed track #369, `[Track] v1.0.0: Assessment Artifact and Testing Procedure Readiness Review`
- completed track #374, `[Track] v1.0.0: Implementation and Adoption Guidance Readiness Review`

The goal is to make release-facing update options explicit before any final v1.0.0 release decision.

This document is release-readiness and decision-support material only. It does not update README files, citation material, release notes, GitHub Releases, release tags, the active baseline, control catalog, evidence schema, assessment artifacts, testing procedures, examples, fixtures, validators, implementation guidance, or adoption guidance.

## Current posture

As of this note:

- v1.0.0 path planning is active under roadmap #350.
- #380 has reviewed release readiness at the planning level.
- #380 has documented release communication boundaries at the planning level.
- README release posture has not been updated by #380.
- Citation status has not been updated by #380.
- Release notes have not been published by #380.
- No v1.0.0 release tag has been created by #380.
- No GitHub Release has been published by #380.
- The active control and assessment baseline has not been changed by completed v1.0.0 readiness tracks.
- Any future README, citation, release-note, GitHub Release, tag, or active baseline wording update must be explicit.

## Decision posture

The recommended posture is:

> Treat README, citation, and release-note updates as release-facing actions that require explicit final release decision context.
>
> Do not update README release posture, citation status, or release notes merely because readiness-review tracks completed.
>
> Defer release-facing wording changes until final release decision inputs are documented, active baseline wording is decided, and release notes can state clearly what did and did not change.

This posture keeps release communication useful without creating accidental release or baseline claims.

## Update options summary

| Option | Summary | Initial posture |
| --- | --- | --- |
| Option A | Preserve README, citation, and release notes unchanged for now. | Safest default while planning remains open. |
| Option B | Prepare README update options but do not apply them yet. | Useful before final release decision. |
| Option C | Prepare citation update options but do not apply them yet. | Useful if a final v1.0.0 release tag is likely. |
| Option D | Prepare release-note draft options but do not publish them yet. | Recommended before final release action. |
| Option E | Coordinate README, citation, and release notes only after final release decision inputs are complete. | Recommended near-term path. |
| Option F | Update README release posture before final release decision. | Not recommended by default. |
| Option G | Update citation status before final release tag/GitHub Release. | Not recommended by default. |
| Option H | Publish release notes before release tag/GitHub Release. | Not recommended by default. |
| Option I | Treat release-facing artifacts as certification, compliance, audit, legal, readiness, conformance, or equivalence claims. | Non-goal. |

## Option A: Preserve README, citation, and release notes unchanged for now

Meaning:

- README release posture remains unchanged.
- Localized README release posture remains unchanged.
- Citation status remains unchanged.
- Release notes remain unpublished.
- GitHub Release text remains unpublished.
- No release tag is created.
- Document map and status README registration continues normally.

Benefits:

- Lowest risk of accidental v1.0.0 publication claims.
- Avoids accidental active baseline wording changes.
- Avoids implying release before final release decision.
- Keeps #380 scoped to planning and decision support.

Risks:

- Public-facing entry points may not yet reflect final v1.0.0 readiness work.
- Final release communication remains outstanding.
- Readers may need issue and status documents to understand the v1.0.0 path.

Best fit when:

- v1.0.0 is still in planning;
- final release decision inputs are not complete;
- active baseline wording has not been finalized; and
- release notes have not been drafted and reviewed.

## Option B: Prepare README update options but do not apply them yet

Meaning:

- Draft possible README release-posture wording.
- Do not commit README changes yet.
- Compare wording for active-baseline-preserving and active-baseline-updating release paths.
- Identify localized README alignment needs if README changes later.

Benefits:

- Improves readiness for final release decision.
- Allows wording review before release action.
- Helps clarify active baseline, release status, planning artifacts, status artifacts, and stable guidance candidates.
- Reduces rushed release communication risk.

Risks:

- Draft wording may be mistaken as approved if not labeled clearly.
- May create scope creep if README updates expand into navigation redesign.
- Requires careful claim-boundary review.

Best fit when:

- final release decision is approaching;
- release-facing wording needs pre-review; and
- maintainers want to separate wording options from actual README updates.

## Option C: Prepare citation update options but do not apply them yet

Meaning:

- Draft possible citation wording for a later v1.0.0 release.
- Do not update citation files or citation status yet.
- Distinguish framework release citation from peer-reviewed publication, standardization, empirical validation, or external endorsement.

Benefits:

- Helps prepare release publication hygiene.
- Avoids last-minute citation wording decisions.
- Clarifies that citation does not imply peer-reviewed acceptance or empirical validation.

Risks:

- Citation wording can imply more maturity than intended.
- Citation status may be interpreted as publication if updated too early.
- Citation updates should align with actual tag and GitHub Release.

Best fit when:

- a v1.0.0 tag and GitHub Release are likely but not yet created;
- citation wording needs review; and
- peer-reviewed/empirical/standardization claims remain explicitly out of scope.

## Option D: Prepare release-note draft options but do not publish them yet

Meaning:

- Draft release-note structure and candidate wording.
- Do not publish release notes yet.
- Include sections for what changed, what did not change, validation, active baseline posture, claim boundaries, and follow-up work.
- Keep release-note draft separate from release publication.

Benefits:

- Strong release readiness support.
- Helps ensure final release notes preserve boundaries.
- Makes release artifact review easier.
- Reduces risk of overclaiming completed readiness tracks.

Risks:

- Draft release notes may be mistaken for published release notes.
- Requires alignment with final release decision.
- Must be updated if final release scope changes.

Best fit when:

- release communication boundary note exists;
- final release decision inputs are being prepared; and
- maintainers want a controlled release-note structure before tagging.

## Option E: Coordinate README, citation, and release notes only after final release decision inputs are complete

Meaning:

- README update options, citation update options, and release-note draft options remain decision-support material until final release decision inputs are documented.
- Actual updates wait for explicit final release action.
- GitHub Release and tag creation remain separate final steps.

Benefits:

- Best balance between readiness and caution.
- Preserves release discipline.
- Prevents accidental release communication before release scope is final.
- Aligns README, citation, release notes, tag, and GitHub Release.

Risks:

- Requires one more release decision step.
- Public-facing release artifacts remain unchanged until later.

Initial posture:

- Recommended near-term path.

## Option F: Update README release posture before final release decision

Meaning:

- README is changed before final release decision inputs are complete.

Benefits:

- README becomes more current earlier.
- Readers may find v1.0.0 planning status faster.

Risks:

- High risk of implying v1.0.0 is already released.
- High risk of implying active baseline change.
- High risk of inconsistent wording with final release notes.
- May require localized README updates.
- May create public communication confusion.

Initial posture:

- Not recommended by default.

## Option G: Update citation status before final release tag/GitHub Release

Meaning:

- Citation material is updated before tag and GitHub Release exist.

Benefits:

- Citation material is ready early.

Risks:

- May imply release publication before release.
- May imply peer-reviewed acceptance, empirical validation, standardization, or external endorsement if wording is not precise.
- May become inconsistent with final tag or release date.

Initial posture:

- Not recommended by default.

## Option H: Publish release notes before release tag/GitHub Release

Meaning:

- Release notes are published before final release action.

Benefits:

- Early visibility into planned release scope.

Risks:

- May be mistaken for a release.
- May conflict with final release scope.
- May imply publication before tag/GitHub Release.
- May create version and baseline confusion.

Initial posture:

- Not recommended by default.

## Option I: Treat release-facing artifacts as certification, compliance, audit, legal, readiness, conformance, or equivalence claims

Meaning:

- README, citation, release notes, or GitHub Release text claims that AAEF certifies, proves compliance, proves legal/audit sufficiency, proves production readiness, proves implementation conformance, or is equivalent to external frameworks.

Initial posture:

- Non-goal.
- Should not be selected.

Rationale:

- AAEF is not a certification scheme.
- AAEF does not provide legal advice or legal sufficiency.
- AAEF does not provide audit opinions or audit sufficiency.
- AAEF does not prove implementation conformance by release text alone.
- AAEF does not claim external-framework equivalence.

## Dependency impact matrix

| Update type | Active baseline impact | Release communication impact | Review need |
| --- | --- | --- | --- |
| Preserve unchanged | None | Low | Confirm later. |
| README update options only | None now | Medium | Wording review needed. |
| Citation update options only | None now | Medium | Citation/release alignment needed. |
| Release-note draft options only | None now | Medium | Final release scope alignment needed. |
| Coordinated post-decision update | Depends on final decision | Medium/high | Recommended controlled path. |
| Early README update | Possible implied impact | High | Not recommended by default. |
| Early citation update | Possible implied publication | High | Not recommended by default. |
| Early release notes | Possible implied publication | High | Not recommended by default. |
| Certification/compliance/equivalence positioning | Not acceptable | Very high | Non-goal. |

## README update option requirements

Any future README release-posture update should state:

- whether v1.0.0 has actually been released;
- whether a GitHub Release exists;
- whether a release tag exists;
- whether the active baseline changed;
- which artifacts are active baseline artifacts;
- which artifacts are planning/status artifacts;
- which artifacts are stable guidance candidates;
- which artifacts remain future work;
- what AAEF does not claim;
- where readers should go next.

Any future README update should avoid:

- implying readiness-track completion equals release;
- implying active baseline change unless explicitly decided;
- implying certification, compliance, audit, legal, readiness, conformance, or equivalence claims;
- presenting examples, validators, assessment artifacts, or testing procedures as sufficiency proof.

## Citation update option requirements

Any future citation update should state or preserve:

- actual release version;
- actual release date, if available;
- actual release tag, if available;
- repository location;
- distinction between framework release and peer-reviewed publication;
- no implication of empirical validation unless separately supported;
- no implication of standardization unless separately supported;
- no implication of certification or compliance.

Citation updates should wait until the final release version, tag, and publication status are explicit.

## Release-note option requirements

Any future release notes should include:

- release title;
- release scope;
- active baseline posture;
- completed readiness-track summary;
- artifacts added or updated;
- artifacts not changed;
- validation performed;
- claim boundaries;
- non-goals;
- follow-up work;
- links to relevant roadmap/issues where appropriate.

Release notes should explicitly say whether:

- the active baseline changed;
- control catalog changed;
- control IDs changed;
- evidence schema changed;
- assessment artifacts changed;
- testing procedures changed;
- validators changed;
- examples or fixtures changed;
- README release posture changed;
- citation status changed.

## Minimal safe release-note structure

A minimal safe release-note structure would include:

1. Summary
2. Release scope
3. Active baseline posture
4. Completed readiness-track inputs
5. Added or updated artifacts
6. Artifacts not changed
7. Validation
8. Claim boundaries
9. Non-goals
10. Follow-up work

This note does not publish release notes.

## Active baseline wording options

### Active baseline unchanged wording

Potential wording:

> This release does not change the active control and assessment baseline unless a separate release artifact explicitly states otherwise.

Potential stronger wording for a final release, if chosen:

> AAEF v1.0.0 preserves the existing active control and assessment baseline and publishes release-readiness documentation and communication boundaries for the stable release path.

This wording should only be used if the final release decision confirms that the active baseline remains unchanged.

### Active baseline updated wording

Potential wording:

> AAEF v1.0.0 updates the active control and assessment baseline through the explicitly listed artifacts below.

This wording should only be used if final release work explicitly updates baseline artifacts and lists them.

## Recommended near-term decision

The recommended near-term decision is:

> Preserve README release posture, citation status, and release notes unchanged during #380 until final release decision inputs are documented.
>
> Use this document to define update options.
>
> Proceed next to final release decision inputs.
>
> Treat actual README, citation, release-note, tag, and GitHub Release updates as later explicit release actions.

This keeps release-facing artifacts safe while allowing release planning to continue.

## Relationship to release communication boundary note

This document relies on `docs/en/status/v100-release-communication-boundary-note.md`.

README, citation, and release-note options should preserve that note's boundaries for:

- active baseline wording,
- release readiness versus release action,
- completed readiness-track summaries,
- examples and fixtures,
- validators,
- assessment artifacts,
- testing procedures,
- implementation/adoption guidance,
- external mappings,
- research positioning,
- public communication,
- unsupported claims.

## Relationship to final release decision inputs

This document should feed into final release decision inputs by identifying:

- which release-facing artifacts may need updates;
- which updates should wait;
- which wording boundaries apply;
- what release notes should include;
- whether active baseline wording is unchanged or changed;
- what must be explicit before tagging or publishing.

## Recommended follow-up work for #380

Recommended next #380 artifacts:

- final release decision inputs,
- release readiness close-readiness checklist.

Optional follow-up artifacts:

- public announcement draft planning,
- final roadmap close-readiness checklist,
- active baseline wording decision note.

## Claim boundaries

This update-options note does not claim:

- v1.0.0 release,
- release tag creation,
- GitHub Release publication,
- active baseline update,
- control catalog update,
- control ID update,
- evidence schema update,
- assessment artifact update,
- testing procedure update,
- validator update,
- example update,
- fixture update,
- README release posture update,
- navigation update,
- citation status update,
- release-note publication,
- public announcement approval,
- implementation readiness,
- adoption readiness,
- operational readiness,
- production readiness,
- implementation conformance,
- assessment sufficiency,
- testing sufficiency,
- evidence sufficiency,
- semantic correctness,
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

- Does this note distinguish update options from actual updates?
- Does it avoid implicitly updating README release posture?
- Does it avoid implicitly updating citation status?
- Does it avoid implicitly publishing release notes?
- Does it preserve active baseline wording boundaries?
- Does it preserve release communication boundaries?
- Does it identify safe release-note structure?
- Does it identify when README/citation/release-note updates should occur?
- Does it preserve claim boundaries?
- Does it provide enough direction for final release decision inputs?

## Scope reminder

This artifact is release-readiness and decision-support material only.

It does not publish v1.0.0, create a release tag, publish a GitHub Release, update README release posture, update navigation, update citation status, publish release notes, approve public announcement text, update the active control and assessment baseline, update the control catalog, update control IDs, update the evidence schema, update assessment artifacts, update testing procedures, add executable validators, add executable prototypes, add scenario fixtures, add JSON examples, or establish readiness, conformance, certification, compliance, audit, legal, control conformance, or external-framework equivalence claims.
