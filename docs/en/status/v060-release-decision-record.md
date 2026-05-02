# AAEF v0.6.0 Release Decision Record

Status: Planning decision record  
Related roadmap: #241  
Milestone: v0.6.0 Planning  
Related release preparation: `docs/en/status/v060-release-preparation-planning.md`  
Related release notes draft: `docs/en/status/v060-release-notes-draft.md`  
Related release readiness review: `docs/en/status/v060-release-readiness-review.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document records release-scope decisions before preparing a possible AAEF v0.6.0 planning release PR.

The purpose is to clarify how `CHANGELOG.md`, README status wording, `CITATION.cff`, GitHub release notes, roadmap issue #241, umbrella issue #3, and post-release follow-up work should be handled.

This document is a planning decision record. It does not create a release, create a tag, update `CHANGELOG.md`, update README files, update `CITATION.cff`, close issues, or promote planning material into active requirements.

## Decision summary

| Decision ID | Topic | Decision | Release PR implication |
| --- | --- | --- | --- |
| D-01 | Release type | Prepare v0.6.0 as a planning and adoption-readiness release. | Release wording must say planning release, not active baseline release. |
| D-02 | Active baseline | Do not change the current active control and assessment baseline by implication. | README, CHANGELOG, and release notes must preserve explicit baseline boundaries. |
| D-03 | CHANGELOG | Convert the relevant Unreleased v0.6.0 planning entries into a v0.6.0 planning release section in the release PR. | Release PR should update `CHANGELOG.md`. |
| D-04 | README status wording | Review README status wording and update only if needed to describe v0.6.0 as a planning release without implying active baseline change. | Release PR may update README files if current wording would be stale or ambiguous after release. |
| D-05 | `CITATION.cff` | Review `CITATION.cff` during the release PR; update only if the project treats v0.6.0 as a citable released version. | Release PR must either update `CITATION.cff` or explicitly record no-update rationale. |
| D-06 | Release notes | Use `docs/en/status/v060-release-notes-draft.md` as the source for GitHub release body text. | Release PR may refine the draft before tag creation. |
| D-07 | Stable release notes path | Do not require a stable `docs/en/release/` release-notes file before v0.6.0. | Optional future improvement; not release-blocking. |
| D-08 | Status document movement | Do not move or archive status documents before v0.6.0 release. | Defer archive/historical-header work to post-release follow-up. |
| D-09 | External mapping CSV enrichment | Do not require external mapping CSV enrichment before v0.6.0 release. | Defer enrichment to post-release follow-up unless separately approved. |
| D-10 | Adoption-facing promotion | Do not promote all v0.6.0 planning drafts into active/adoption-facing artifacts in the release PR. | Promotion should happen through explicit v0.6.x follow-up PRs. |
| D-11 | Roadmap issue #241 | Keep #241 open unless release-scope completion is explicitly reviewed and accepted. | Release PR should not automatically close #241. |
| D-12 | Umbrella issue #3 | Keep #3 open. | Release PR should not close #3. |
| D-13 | Child track issues | Do not automatically close child track issues merely because a planning release is created. | Close or keep child track issues only after issue-specific review. |
| D-14 | Release tag | Create a tag only after the release PR is merged and final validation passes. | No tag should be created from this decision record PR. |

## D-01: release type

Decision:

AAEF v0.6.0 should be prepared as a planning and adoption-readiness release.

It should be titled along the lines of:

**AAEF v0.6.0 Practical Adoption Readiness Planning Release**

Rationale:

The v0.6.0 work has organized implementer, operational, legal/compliance, security architecture, and risk owner planning materials. It has not promoted those materials into active control requirements.

## D-02: active baseline

Decision:

v0.6.0 should not change the current active control and assessment baseline by implication.

Rationale:

The v0.6.0 artifacts are currently planning and coordination materials. Any baseline change should require explicit changes to active artifacts through later PRs.

Release PR requirement:

The release PR should preserve language such as:

> Unless explicitly updated in active artifacts, the current control and assessment baseline remains unchanged.

## D-03: CHANGELOG handling

Decision:

The release PR should convert the relevant v0.6.0 planning entries in `CHANGELOG.md` from Unreleased into a v0.6.0 planning release section.

Rationale:

A release tag should have a clear release boundary. Leaving all release content under Unreleased after the release would make the release boundary ambiguous.

Release PR requirement:

The release PR should:

- create a v0.6.0 release section or equivalent release-boundary entry
- keep wording clear that this is a planning release
- avoid implying active baseline change
- keep unrelated future work in Unreleased if applicable

## D-04: README status wording

Decision:

The release PR should review README status wording and update it only if needed to avoid stale or ambiguous release-status language.

Rationale:

After creating a v0.6.0 planning release, README status text may need to distinguish:

- current planning release
- current active control and assessment baseline
- non-normative planning material
- future adoption-facing follow-up

Release PR requirement:

README wording must not imply:

- certification
- legal compliance
- equivalence with external frameworks
- audit sufficiency
- active baseline change by implication

## D-05: `CITATION.cff` handling

Decision:

The release PR should review `CITATION.cff`.

If the repository treats v0.6.0 as a citable released version, update `CITATION.cff` in the release PR.

If not, leave `CITATION.cff` unchanged and record the no-update rationale in the release PR.

Rationale:

Citation metadata should not be updated casually, but a tagged planning release may be citable depending on project policy.

Release PR requirement:

Do one of the following:

- update `CITATION.cff` consistently with the release tag and date, or
- explicitly state that `CITATION.cff` is not updated because v0.6.0 is a planning release and citation metadata remains tied to the current citable baseline

## D-06: release notes source

Decision:

Use `docs/en/status/v060-release-notes-draft.md` as the source for the GitHub release body, with final edits allowed in the release PR.

Rationale:

The release notes draft already contains baseline and claim-boundary language.

Release PR requirement:

The final release text should preserve:

- planning release status
- current baseline note
- claim-boundary language
- non-goals
- deferred follow-up

## D-07: stable release notes path

Decision:

A stable `docs/en/release/` release-notes file is not required before v0.6.0.

Rationale:

The release notes draft can support GitHub release text. A stable release notes directory can be introduced later if desired.

Release PR implication:

Do not block v0.6.0 release on creating a new release-notes directory.

## D-08: status document movement

Decision:

Do not move or archive status documents before the v0.6.0 release.

Rationale:

The archive-readiness review found that all 36 `archive later` documents still have status-document references. Movement before release may create unnecessary reference churn.

Release PR implication:

Do not move, delete, archive, replace, or promote status documents in the release PR.

## D-09: external mapping CSV enrichment

Decision:

Do not require external mapping CSV enrichment before v0.6.0 release.

Rationale:

The external mapping enrichment review established a conservative basis, but actual enrichment requires additional structure, review, and claim-boundary controls.

Release PR implication:

Do not add mapping rows in the release PR unless separately approved.

## D-10: adoption-facing promotion

Decision:

Do not promote all v0.6.0 planning drafts into active or adoption-facing artifacts in the release PR.

Rationale:

Promotion should be intentional and artifact-specific.

Release PR implication:

Use v0.6.x follow-up PRs for selected promotion.

## D-11: roadmap issue #241

Decision:

Keep #241 open unless the release PR explicitly reviews and accepts release-scope completion.

Rationale:

#241 remains useful as the v0.6.0 coordination and roadmap issue.

Release PR implication:

Do not auto-close #241.

## D-12: umbrella issue #3

Decision:

Keep #3 open.

Rationale:

#3 is broader cross-agent and cross-domain authority roadmap context.

Release PR implication:

Do not close #3.

## D-13: child track issues

Decision:

Do not automatically close child track issues solely because a planning release is created.

Rationale:

Child track issues may still be useful for v0.6.x adoption-facing promotion and follow-up work.

Release PR implication:

Review each issue individually before closure.

## D-14: release tag

Decision:

Create a tag only after:

1. the release PR is merged
2. validation passes
3. README / CHANGELOG / CITATION handling is complete or explicitly deferred
4. release notes are final

Rationale:

The release tag should point to a reviewed release boundary.

## Recommended release PR scope

The next release PR should likely include:

- `CHANGELOG.md` release-boundary update
- README / README.ja status wording updates if needed
- `CITATION.cff` update or explicit no-update rationale
- final release notes refinement if needed
- validation result
- issue/milestone handling decision

The release PR should not include:

- status document movement
- external mapping CSV enrichment
- adoption-facing promotion of planning drafts
- active control changes
- assessment baseline changes

## Recommended release PR acceptance criteria

The release PR is sufficient when:

- v0.6.0 release boundary is clear
- release notes are final enough for GitHub release body
- README status wording is not stale or misleading
- `CITATION.cff` handling is decided
- `CHANGELOG.md` reflects the intended release boundary
- validation passes
- no active baseline change is implied
- no certification, compliance, equivalence, conformity, or audit-sufficiency claim is introduced

## Non-goals

This decision record does not:

- create a release
- create a tag
- update `CHANGELOG.md`
- update README files
- update `CITATION.cff`
- close issues
- move, delete, archive, replace, or promote status documents
- enrich external mapping CSVs
- change active controls
- change the current control and assessment baseline
- promote planning material into active requirements

## Acceptance criteria for this decision record

This decision record is sufficient when:

- release-scope decisions are listed
- CHANGELOG handling is decided
- README handling is decided
- `CITATION.cff` handling is decision-gated
- release notes source is identified
- #241 and #3 handling are clarified
- deferred work is identified
- no release action is performed
- no active baseline change is implied
