# AAEF v0.6.0 Release Preparation Planning

Status: Planning input  
Related roadmap: #241  
Milestone: v0.6.0 Planning  
Related planning summary: `docs/en/status/v060-planning-progress-summary.md`  
Related review follow-up summary: `docs/en/status/v060-review-follow-up-summary.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document defines preparation criteria for a possible AAEF v0.6.0 planning release.

The purpose is to connect the completed v0.6.0 planning work, repository review follow-up, validation status, and remaining decisions to a release-readiness workflow.

This document is planning and coordination material. It does not create a release, create a tag, change active controls, change the current control and assessment baseline, or promote planning material into active requirements.

## Planned release positioning

AAEF v0.6.0 is planned as:

**AAEF v0.6.0: Practical Adoption Readiness**

The release should be positioned as a planning and adoption-readiness release that organizes selected v0.5.0 and v0.5.x planning material into implementer, operational, legal/compliance, security architecture, and risk owner adoption packages.

It should not be positioned as a new active control baseline unless later PRs explicitly update active artifacts.

## Current release posture

The current posture is:

- v0.6.0 planning foundations have been created.
- The initial five-pillar planning set exists.
- Repository review follow-up findings F-01 through F-05 have documented handling status.
- Document-map coverage has been repaired and regression-protected.
- CHANGELOG Unreleased has been consolidated for v0.6.0 planning.
- Status-document triage has planning, inventory, decision register, and archive-readiness review.
- External framework mapping CSV enrichment has a conservative review basis.
- No release tag has been created.
- No release notes have been finalized.
- No active baseline change has been made.

## Release candidate content

A v0.6.0 planning release candidate may include the following planning artifacts.

| Area | Candidate release content |
| --- | --- |
| Planning synthesis | `docs/en/status/v060-planning-input-synthesis.md` |
| Implementer Readiness | `docs/en/status/v060-authorization-decision-artifact-minimal-profile-planning.md` and `docs/en/status/v060-implementer-quick-start-planning.md` |
| Operational Readiness | `docs/en/status/v060-operational-responsibility-matrix-planning.md` |
| Legal and Compliance Applicability | `docs/en/status/v060-legal-compliance-applicability-note-planning.md` |
| Security Architecture Hardening | `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md` |
| Risk Owner and Executive Adoption | `docs/en/status/v060-risk-owner-guide-planning.md` |
| Planning progress | `docs/en/status/v060-planning-progress-summary.md` |
| Repository review follow-up | `docs/en/status/v060-review-follow-up-summary.md` |
| Status document triage | `docs/en/status/v060-status-document-triage-planning.md`, inventory, decision register, and archive-readiness review |
| External mapping follow-up | `docs/en/status/v060-external-framework-mapping-csv-enrichment-review.md` |

## Release non-goals

A v0.6.0 planning release should not:

- change the current control and assessment baseline by implication
- claim that v0.6.0 is a certification scheme
- claim legal or regulatory compliance
- claim equivalence with external frameworks
- claim audit sufficiency or conformity
- promote all planning documents into active requirements
- delete, archive, move, or replace status documents
- complete external framework mapping CSV enrichment unless handled by separate PRs
- close umbrella issue #3 unless explicitly decided
- close roadmap issue #241 unless the release scope is complete and documented

## Required pre-release checks

Before a v0.6.0 planning release, the following checks should be completed.

| Check | Purpose | Status |
| --- | --- | --- |
| Working tree clean | Ensure no local uncommitted changes are present. | Required before release |
| Branch synchronized | Ensure `main` is synchronized with `origin/main`. | Required before release |
| Artifact validation | Run repository validation. | Required before release |
| Markdown index validation | Ensure status README and document-map entries are valid. | Required before release |
| Numbered document coverage validation | Ensure top-level numbered docs are represented in document-map. | Required before release |
| CHANGELOG review | Ensure Unreleased accurately describes v0.6.0 planning scope. | Required before release |
| README status review | Ensure README status wording does not imply an active baseline change. | Required before release |
| CITATION review | Decide whether a v0.6.0 planning release requires citation update. | Decision needed |
| Release notes draft | Prepare conservative release notes. | Decision needed |
| Milestone review | Confirm open/closed issue status for `v0.6.0 Planning`. | Required before release |
| Label review | Confirm PRs and issues have expected labels. | Required before release |
| Claim-boundary review | Confirm no compliance, equivalence, audit sufficiency, or certification claims are introduced. | Required before release |

## Suggested validation commands

Recommended local validation commands:

    cd /e/AAEF/agentic-authority-evidence-framework

    git checkout main
    git pull --ff-only origin main
    git status
    py tools/validate_markdown_indexes.py

Recommended repository review commands:

    git log --oneline --decorate --graph -12
    sed -n '1,140p' CHANGELOG.md
    sed -n '1,140p' docs/en/status/README.md
    grep -n "v060-" docs/en/document-map.md

If additional validators exist, release preparation should run the same validation suite used by GitHub Actions.

## Suggested GitHub review commands

Recommended GitHub CLI checks:

    gh issue view 241 --json number,title,state,labels,milestone,url
    gh issue list --milestone "v0.6.0 Planning" --state open
    gh issue list --milestone "v0.6.0 Planning" --state closed
    gh pr list --state open --label "v0.6.0"
    gh release list --limit 10

## Candidate release notes structure

A future v0.6.0 planning release note may use the following structure.

1. Title
2. Release status
3. What this release is
4. What this release is not
5. Major planning additions
6. Five-pillar adoption readiness coverage
7. Repository review follow-up
8. Validation summary
9. Current baseline note
10. Remaining follow-up
11. Links to key artifacts
12. Disclaimer about certification, compliance, equivalence, and audit sufficiency

## Candidate release note title

Candidate title:

**AAEF v0.6.0 Practical Adoption Readiness Planning Release**

## Candidate release status language

Suggested status language:

> AAEF v0.6.0 is a planning and adoption-readiness release. It organizes implementer, operator, legal/compliance, security architecture, and risk owner planning artifacts for future adoption-facing refinement. It does not, by itself, change the current active control and assessment baseline.

## Candidate baseline language

Suggested baseline language:

> Unless explicitly updated in active artifacts, the current control and assessment baseline remains unchanged. v0.6.0 planning artifacts are non-normative planning material until later PRs promote selected material into active guidance, controls, schema, assessment, testing, or release artifacts.

## Candidate claim-boundary language

Suggested claim-boundary language:

> AAEF does not create a certification scheme, legal compliance claim, audit opinion, conformity assessment, or equivalence claim with external frameworks. External framework mapping materials are informative alignment aids only.

## Release readiness decision points

Before creating a release tag, decide:

1. Should v0.6.0 be released as a planning release now?
2. Should any README status text be updated first?
3. Should `CITATION.cff` be updated for v0.6.0?
4. Should release notes be drafted in `docs/en/release/` first?
5. Should `CHANGELOG.md` Unreleased be converted into a `v0.6.0 Planning Release` section?
6. Should #241 remain open after release as the v0.6.0 coordination issue?
7. Should any child track issues remain open after release?
8. Should status document archive movement be deferred until after release?
9. Should external framework mapping CSV enrichment be deferred to a post-release follow-up?
10. Should adoption-facing promotion work be split into v0.6.x follow-up issues?

## Recommended release preparation sequence

Recommended sequence:

1. Add this release preparation planning document.
2. Review current milestone and issue state.
3. Draft v0.6.0 release notes.
4. Decide whether README and CITATION updates are required.
5. Decide whether CHANGELOG should be converted from Unreleased to a release section.
6. Run validation locally.
7. Confirm GitHub Actions status.
8. Prepare release PR.
9. Merge release PR with extended description.
10. Create release tag only after final review.

## Current recommendation

The current recommended path is:

- Do not move status documents before release.
- Do not enrich external mapping CSVs before release unless a separate conservative CSV structure PR is added.
- Treat v0.6.0 as a planning release, not an active baseline release.
- Use v0.6.x follow-up work for adoption-facing promotion, mapping enrichment, and status archive execution.

## Non-goals for this preparation document

This document does not:

- create a release
- create a tag
- update `CITATION.cff`
- update README status wording
- update release notes
- change `CHANGELOG.md`
- close issues
- change active controls
- change the current control and assessment baseline
- promote planning material into active requirements

## Acceptance criteria for this preparation document

This preparation document is sufficient when:

- release positioning is defined
- release non-goals are documented
- pre-release checks are listed
- validation commands are documented
- release notes structure is proposed
- baseline and claim-boundary language are proposed
- release readiness decision points are listed
- no release action is performed
- no active baseline change is implied
