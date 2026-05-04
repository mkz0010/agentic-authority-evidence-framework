# v1.0.0 Release Communication Boundary Note

## Purpose

This document records release communication boundaries for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #380, `[Track] v1.0.0: Release Readiness and Communication Planning`
- `docs/en/status/v100-release-readiness-review.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- completed track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`
- completed track #369, `[Track] v1.0.0: Assessment Artifact and Testing Procedure Readiness Review`
- completed track #374, `[Track] v1.0.0: Implementation and Adoption Guidance Readiness Review`

The goal is to define safe communication boundaries before any v1.0.0 release-facing update, including README release-posture updates, citation updates, release notes, GitHub Release text, public announcement text, or external summaries.

This document is release communication planning material only. It does not publish v1.0.0, create a release tag, publish a GitHub Release, update README release posture, update citation status, publish release notes, change the active baseline, update baseline artifacts, or authorize public announcement text.

## Current posture

As of this note:

- v1.0.0 path planning is active under roadmap #350.
- #380 is reviewing release readiness and communication planning.
- Release readiness has been reviewed at the planning level.
- The current active baseline has not been changed by the completed v1.0.0 readiness tracks.
- The current control catalog and control IDs are preserved by default unless later explicit release decision changes them.
- The current evidence schema, examples, fixtures, validators, assessment artifacts, and testing procedures are preserved by default unless later explicit updates are scoped.
- README release posture, citation status, release notes, GitHub Release text, and public announcement text have not been updated by #380.
- Any release-facing communication must remain explicit, scoped, and claim-boundary-first.

## Communication posture

The recommended posture is:

> Communicate v1.0.0 readiness work as release planning and decision support until a final release action is explicitly performed.
>
> Do not describe readiness-track completion as v1.0.0 publication, active baseline update, implementation readiness, adoption readiness, operational readiness, production readiness, implementation conformance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
>
> Treat release-facing wording as part of the control boundary for the framework itself.

This keeps public and repository-facing communication aligned with the conservative scope of the v1.0.0 path.

## Communication audiences

Release communication may eventually address:

- repository maintainers,
- implementers,
- operators,
- auditors and reviewers,
- evidence requesters,
- risk owners and executives,
- security architects,
- legal and compliance reviewers,
- researchers,
- standards and assurance readers,
- public readers,
- social media or article readers.

Each audience may need different emphasis, but the claim boundaries should remain consistent.

## Allowed high-level messages

The following messages are safe if phrased carefully:

- AAEF is reviewing readiness for a v1.0.0 release path.
- Completed v1.0.0 readiness tracks provide decision inputs.
- v1.0.0 planning has reviewed baseline scope, control catalog readiness, evidence schema readiness, examples and validator readiness, assessment/testing readiness, implementation/adoption guidance readiness, and release readiness.
- The framework continues to emphasize that model output is not authority.
- The framework focuses on action authority, execution boundaries, evidence, reviewability, and risk-owner decision support.
- Release readiness work does not automatically publish v1.0.0.
- Release readiness work does not automatically change the active baseline.
- Release-facing updates should be explicit and separately reviewed.
- AAEF is not a certification scheme, audit opinion, legal opinion, or external-framework equivalence claim.

## Messages requiring caution

The following messages may be used only with precise qualifiers:

| Message type | Required qualifier |
| --- | --- |
| "v1.0.0 is ready" | Specify whether this means planning-ready, release-decision-ready, or actually released. |
| "stable" | Specify whether it means stable guidance candidate, stable release, or stable active baseline. |
| "baseline" | Specify whether the active baseline changed or remains unchanged. |
| "assessment" | Clarify that assessment artifacts support review and do not prove assessment sufficiency by themselves. |
| "testing" | Clarify that testing procedures support review and do not prove testing sufficiency by themselves. |
| "validator" | Clarify that validators support repository hygiene and do not prove semantic correctness or assurance. |
| "example" | Clarify that examples are illustrative unless explicitly scoped otherwise. |
| "adoption" | Clarify adoption support versus adoption readiness. |
| "implementation" | Clarify implementation guidance versus implementation conformance. |
| "external mapping" | Clarify conservative relationship mapping versus compliance or equivalence. |
| "research" | Clarify research positioning versus empirical validation or peer-reviewed acceptance. |

## Prohibited or unsupported messages

Release-facing communication should not claim:

- v1.0.0 has been published unless a release tag and GitHub Release actually exist;
- the active baseline changed unless an explicit release decision changed it;
- AAEF certifies implementations;
- AAEF establishes compliance;
- AAEF establishes conformity;
- AAEF provides legal sufficiency;
- AAEF provides audit sufficiency;
- AAEF provides an audit opinion;
- AAEF proves implementation readiness;
- AAEF proves adoption readiness;
- AAEF proves operational readiness;
- AAEF proves production readiness;
- AAEF proves implementation conformance;
- AAEF proves assessment sufficiency;
- AAEF proves testing sufficiency;
- AAEF proves evidence sufficiency;
- AAEF proves semantic correctness;
- AAEF automates risk acceptance;
- AAEF proves control conformance;
- AAEF is equivalent to external frameworks;
- external mappings prove compliance;
- examples prove complete coverage;
- validators prove real-world correctness;
- planning artifacts are normative baseline changes by themselves;
- completed readiness tracks are release actions by themselves.

## Release readiness versus release action

Communication should distinguish:

| Concept | Meaning | Should not be described as |
| --- | --- | --- |
| Release readiness review | Planning-level review of release-facing decisions and blockers. | Release publication. |
| Release communication boundary note | Planning-level wording guardrails. | Approved release notes or announcement. |
| README/citation/release-note update options | Decision-support material. | Actual README/citation/release-note update. |
| Final release decision inputs | Inputs for maintainers. | Final release decision by itself. |
| Release tag | Explicit Git tag. | Planning document. |
| GitHub Release | Explicit release publication. | Roadmap closure alone. |
| Active baseline update | Explicit baseline-relevant artifact change. | Readiness-track completion. |

## README communication boundaries

README release-posture updates should:

- identify the current active baseline clearly;
- distinguish release artifacts from planning/status artifacts;
- state whether v1.0.0 is released only after actual release;
- state whether the active baseline changed or remains unchanged;
- avoid describing readiness tracks as baseline updates;
- avoid certification, compliance, conformity, audit, legal, readiness, conformance, and equivalence claims;
- route readers to relevant documents without overstating their status.

README release-posture updates should not occur implicitly through this note.

## Citation communication boundaries

Citation updates should:

- be aligned with actual release tag and GitHub Release status;
- distinguish framework release from peer-reviewed publication;
- avoid implying empirical validation;
- avoid implying standardization;
- avoid implying external endorsement;
- avoid implying legal, audit, compliance, or conformity status.

Citation status should not be updated implicitly through this note.

## Release-note communication boundaries

Release notes should:

- identify what was added or changed;
- identify what was not changed;
- state whether the active baseline changed;
- list relevant release artifacts;
- preserve claim boundaries;
- distinguish readiness-track outputs from assurance claims;
- distinguish repository validation from implementation assurance.

Release notes should not claim:

- certification,
- compliance,
- conformity,
- audit sufficiency,
- legal sufficiency,
- implementation readiness,
- adoption readiness,
- operational readiness,
- production readiness,
- implementation conformance,
- assessment sufficiency,
- testing sufficiency,
- evidence sufficiency,
- semantic correctness,
- automated risk acceptance,
- control conformance, or
- external-framework equivalence.

Release notes are not published by this note.

## GitHub Release communication boundaries

A GitHub Release should not be prepared or published until:

- release readiness review is complete;
- release communication boundaries are documented;
- README / citation / release-note update options are documented;
- final release decision inputs are documented;
- release readiness close-readiness is confirmed;
- maintainers explicitly decide whether to publish v1.0.0;
- release notes are drafted and reviewed;
- active baseline wording is decided.

A GitHub Release should not imply more than the repository artifacts support.

## Public announcement communication boundaries

Public announcement wording should:

- be conservative;
- state release status accurately;
- avoid unsupported assurance claims;
- distinguish planning/review work from validation;
- distinguish release from certification;
- distinguish guidance from conformance;
- distinguish external mappings from compliance or equivalence;
- avoid implying legal or audit sufficiency;
- avoid implying production readiness.

Public announcement wording should be handled in a later release-facing artifact or final release process, not through this note.

## Suggested safe wording patterns

Potential safe wording patterns:

- "AAEF v1.0.0 release readiness planning is in progress."
- "The v1.0.0 path has completed several readiness-review tracks."
- "These tracks provide decision inputs for a later release decision."
- "This work does not by itself publish v1.0.0 or change the active baseline."
- "AAEF focuses on action authority, execution boundaries, and evidence rather than treating model output as authority."
- "AAEF does not claim certification, compliance, audit sufficiency, legal sufficiency, or equivalence with external frameworks."
- "Examples and validators support review and repository hygiene; they do not prove implementation assurance by themselves."
- "Assessment and testing artifacts support reviewer judgment; they do not prove sufficiency by themselves."

## Wording to avoid

Avoid wording such as:

- "v1.0.0 certifies agentic AI systems."
- "v1.0.0 proves compliance."
- "v1.0.0 is audit-ready."
- "v1.0.0 guarantees safe operation."
- "v1.0.0 proves implementation conformance."
- "v1.0.0 validates evidence sufficiency."
- "AAEF is equivalent to NIST, ISO, OWASP, or other external frameworks."
- "Passing validators proves the implementation is correct."
- "Completing worksheets proves assessment sufficiency."
- "Following guidance proves production readiness."
- "The roadmap is closed, so the release is published."
- "Planning artifacts have become the active baseline automatically."

## Version and baseline wording boundaries

Release communication should always distinguish:

- version status,
- release status,
- active baseline status,
- planning artifact status,
- historical artifact status,
- stable guidance candidate status,
- future-work status.

Recommended pattern:

> The v1.0.0 path reviews release readiness and communication planning. It does not change the active baseline unless a later explicit release decision says so.

If a later final release decision updates the active baseline, the release communication should identify exactly which artifacts changed the baseline.

If a later final release decision preserves the active baseline, the release communication should state that clearly.

## Completed readiness-track communication boundaries

When summarizing completed readiness tracks, use phrases such as:

- "reviewed at the planning level";
- "provides release-decision input";
- "preserves current artifacts by default";
- "does not itself update the baseline";
- "does not itself establish sufficiency";
- "does not itself establish conformance."

Avoid phrases such as:

- "proved";
- "validated";
- "certified";
- "confirmed compliance";
- "approved for production";
- "audit-ready";
- "legally sufficient";
- "equivalent to external frameworks."

## Support-artifact communication boundaries

### Examples and fixtures

Safe description:

- examples and fixtures illustrate expected patterns or scenario structure.

Do not describe them as:

- complete coverage,
- required architecture,
- production implementation,
- proof of conformance,
- proof of semantic correctness.

### Validators

Safe description:

- validators support repository hygiene and consistency checks.

Do not describe them as:

- semantic correctness proof,
- implementation assurance,
- security validation,
- assessment sufficiency,
- evidence sufficiency.

### Assessment artifacts

Safe description:

- assessment artifacts support reviewer judgment.

Do not describe them as:

- certification tools,
- compliance checklists,
- audit opinions,
- assessment sufficiency proof.

### Testing procedures

Safe description:

- testing procedures support review of controls and evidence.

Do not describe them as:

- conformance tests by themselves,
- complete implementation tests,
- production readiness tests,
- testing sufficiency proof.

### Guidance materials

Safe description:

- guidance materials orient readers and support adoption planning.

Do not describe them as:

- implementation conformance proof,
- adoption readiness proof,
- operational readiness proof,
- production readiness proof.

## External mapping communication boundaries

External mappings should be described as:

- conservative relationship mappings,
- orientation aids,
- non-equivalence references,
- non-compliance claims.

External mappings should not be described as:

- compliance mappings that prove compliance;
- equivalence mappings;
- certification mappings;
- conformity assessments;
- audit procedures;
- legal opinions.

## Research communication boundaries

Research-facing communication should distinguish:

- candidate research contribution,
- research positioning,
- research questions,
- framework thesis,
- future empirical work,
- peer-reviewed publication status.

Research communication should not imply:

- peer-reviewed acceptance unless actually achieved;
- empirical validation unless actually performed;
- standardization unless actually achieved;
- external endorsement unless actually received.

## Release communication checklist

Before any release-facing communication, confirm:

- Is v1.0.0 actually released?
- Does a tag exist?
- Does a GitHub Release exist?
- Did the active baseline change?
- Did README release posture change?
- Did citation status change?
- Were release notes published?
- Were examples, validators, assessment artifacts, testing procedures, evidence schema, or control catalog updated?
- Are non-goals stated?
- Are unsupported claims avoided?
- Are completed readiness tracks described as decision inputs rather than proof?
- Are validators described as repository hygiene?
- Are examples described as illustrative?
- Are assessment/testing artifacts described as reviewer support?
- Are external mappings described conservatively?
- Is public wording aligned with repository artifacts?

## Recommended follow-up work for #380

Recommended next #380 artifacts:

- README / citation / release-note update options,
- final release decision inputs,
- release readiness close-readiness checklist.

Optional follow-up artifacts:

- public announcement draft planning,
- final roadmap close-readiness checklist,
- active baseline wording decision note.

## Claim boundaries

This communication boundary note does not claim:

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

- Does this note distinguish release communication from release action?
- Does it preserve active baseline wording boundaries?
- Does it preserve README, citation, release-note, and GitHub Release boundaries?
- Does it identify safe and unsafe wording patterns?
- Does it prevent readiness tracks from being described as proof?
- Does it preserve support-artifact boundaries?
- Does it preserve external mapping boundaries?
- Does it preserve research communication boundaries?
- Does it provide enough direction for README/citation/release-note update options?
- Does it preserve claim boundaries?

## Scope reminder

This artifact is release communication planning material only.

It does not publish v1.0.0, create a release tag, publish a GitHub Release, update the active control and assessment baseline, update the control catalog, update control IDs, update the evidence schema, update assessment artifacts, update testing procedures, add executable validators, add executable prototypes, add scenario fixtures, add JSON examples, update README release posture, update navigation, update citation status, publish release notes, approve public announcement text, or establish readiness, conformance, certification, compliance, audit, legal, control conformance, or external-framework equivalence claims.
