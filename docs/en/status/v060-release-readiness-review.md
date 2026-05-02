# AAEF v0.6.0 Release Readiness Review

Status: Release readiness review  
Related roadmap: #241  
Milestone: v0.6.0 Planning  
Related release preparation: `docs/en/status/v060-release-preparation-planning.md`  
Related release notes draft: `docs/en/status/v060-release-notes-draft.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document defines the readiness checks and decision points that should be reviewed before creating a possible AAEF v0.6.0 planning release.

The purpose is to clarify what must be checked before any release tag, GitHub release, changelog release-section conversion, README update, or citation update.

This document is a release-readiness review. It does not create a release, create a tag, close issues, update `CHANGELOG.md`, update README files, update `CITATION.cff`, or promote planning material into active requirements.

## Release readiness position

AAEF v0.6.0 may be prepared as:

**AAEF v0.6.0 Practical Adoption Readiness Planning Release**

The release should be treated as a planning and adoption-readiness release, not as an active control-baseline release.

## Current release preparation state

| Area | Current state |
| --- | --- |
| Release preparation planning | Added in `docs/en/status/v060-release-preparation-planning.md`. |
| Release notes draft | Added in `docs/en/status/v060-release-notes-draft.md`. |
| Review follow-up summary | Added in `docs/en/status/v060-review-follow-up-summary.md`. |
| Document-map coverage | Addressed and regression-protected. |
| Status document triage | Planning, inventory, decision register, and archive-readiness review exist. |
| External mapping enrichment | Conservative review basis exists; CSV enrichment is not yet performed. |
| Release tag | Not created. |
| GitHub release | Not created. |
| README status update | Not performed. |
| `CITATION.cff` update | Not performed. |
| `CHANGELOG.md` release-section conversion | Not performed. |
| Active baseline change | Not performed. |

## Readiness review checklist

| Check | Required before release? | Current expected status | Readiness decision |
| --- | --- | --- | --- |
| `main` synchronized with `origin/main` | Yes | Must be checked immediately before release | Pending final release check |
| Working tree clean | Yes | Must be checked immediately before release | Pending final release check |
| GitHub Actions passing | Yes | Must be checked on the final release PR or release commit | Pending final release check |
| `py tools/validate_markdown_indexes.py` passes | Yes | Required before release | Pending final release check |
| `CHANGELOG.md` reviewed | Yes | Unreleased has been consolidated, but release-section conversion is not yet done | Decision needed |
| README status wording reviewed | Yes | Must not imply active baseline change | Decision needed |
| `CITATION.cff` reviewed | Yes | Decide whether v0.6.0 planning release requires citation update | Decision needed |
| Release notes reviewed | Yes | Draft exists in `v060-release-notes-draft.md` | Needs final review |
| Milestone reviewed | Yes | Confirm open/closed issue status for `v0.6.0 Planning` | Pending final release check |
| Labels reviewed | Yes | Confirm release-related PRs/issues have expected labels | Pending final release check |
| Open PRs reviewed | Yes | Confirm no release-blocking PRs remain open | Pending final release check |
| Claim-boundary review | Yes | Must avoid compliance, equivalence, audit sufficiency, certification, conformity, or legal claims | Required |
| Baseline-change review | Yes | Must confirm no active baseline change is implied | Required |
| Status-document movement decision | No | Movement should be deferred | Defer |
| External mapping CSV enrichment | No | Enrichment should be deferred unless handled by separate PR | Defer |
| v0.6.x follow-up issue planning | No | Useful after release decision | Optional follow-up |

## Release-blocking decisions

The following decisions should be made before any release tag is created.

| Decision | Recommended answer | Rationale |
| --- | --- | --- |
| Is v0.6.0 a planning release? | Yes | Current artifacts are planning and adoption-readiness materials. |
| Does v0.6.0 change the active control and assessment baseline? | No | No active artifacts have been explicitly promoted. |
| Should all v0.6.0 planning drafts become active requirements? | No | Promotion should occur through later explicit PRs. |
| Should status documents be moved before release? | No | Archive-readiness review found status-document references for all archive-later documents. |
| Should external mapping CSV enrichment be completed before release? | No, unless handled by a separate conservative PR | Current work only establishes the enrichment review basis. |
| Should `CHANGELOG.md` be converted from Unreleased to a v0.6.0 release section? | Decision needed | Required if creating an actual release. |
| Should README status wording be updated? | Decision needed | Must avoid implying a baseline change. |
| Should `CITATION.cff` be updated? | Decision needed | Depends on whether v0.6.0 is treated as a citable planning release. |
| Should #241 close at release? | Probably no | It can remain as v0.6.0 coordination unless explicitly completed. |
| Should #3 close at release? | No | #3 remains broader umbrella / roadmap context. |

## Required local validation commands

Run immediately before a release PR or release tag decision:

    cd /e/AAEF/agentic-authority-evidence-framework

    git checkout main
    git pull --ff-only origin main
    git status
    py tools/validate_markdown_indexes.py
    git log --oneline --decorate --graph -12

## Required content review commands

Recommended review commands:

    sed -n '1,180p' CHANGELOG.md
    sed -n '1,180p' README.md
    sed -n '1,180p' README.ja.md
    sed -n '1,180p' CITATION.cff
    sed -n '1,220p' docs/en/status/v060-release-notes-draft.md
    grep -n "v060-" docs/en/document-map.md
    grep -n "v060-" docs/en/status/README.md

If `CITATION.cff` does not exist or does not need updating, record that decision in the release PR or release issue comment.

## Required GitHub review commands

Recommended GitHub CLI review commands:

    gh issue view 241 --json number,title,state,labels,milestone,url
    gh issue view 3 --json number,title,state,labels,milestone,url
    gh issue list --milestone "v0.6.0 Planning" --state open
    gh issue list --milestone "v0.6.0 Planning" --state closed
    gh pr list --state open --label "v0.6.0"
    gh release list --limit 10

## Claim-boundary checklist

Before release, confirm that release notes, README updates, CHANGELOG updates, and GitHub release text do not claim:

- certification
- legal compliance
- regulatory compliance
- audit sufficiency
- conformity assessment
- equivalence with external frameworks
- replacement of external standards
- replacement of legal, compliance, risk, or audit judgment
- active baseline change by implication

## Baseline-change checklist

Before release, confirm that:

- no active controls are changed by the release PR unless explicitly stated
- no assessment baseline is changed by implication
- planning drafts remain non-normative unless explicitly promoted
- current baseline language is included in release notes
- README status wording remains consistent with the intended baseline posture
- CHANGELOG wording does not imply that planning material is now active control material

## Recommended release path

Recommended path from here:

1. Complete this release readiness review.
2. Decide README / CHANGELOG / CITATION handling.
3. If release is still desired, create a release PR that:
   - finalizes `CHANGELOG.md`
   - updates README status wording if needed
   - updates `CITATION.cff` if needed
   - optionally adds a stable release notes file
4. Run validation locally.
5. Confirm GitHub Actions.
6. Merge release PR with extended description.
7. Create the GitHub release and tag only after final review.

## Current recommendation

The current recommendation is:

- proceed toward a v0.6.0 planning release only after README / CHANGELOG / CITATION decisions are made
- keep status document movement deferred
- keep external mapping CSV enrichment deferred
- keep adoption-facing promotion deferred to v0.6.x follow-up work
- preserve explicit language that v0.6.0 is planning/adoption-readiness material, not an active baseline change

## Non-goals

This review does not:

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

## Acceptance criteria for this review

This review is sufficient when:

- release readiness checks are listed
- release-blocking decisions are identified
- local validation commands are documented
- GitHub review commands are documented
- claim-boundary checks are documented
- baseline-change checks are documented
- recommended release path is documented
- no release action is performed
- no active baseline change is implied
