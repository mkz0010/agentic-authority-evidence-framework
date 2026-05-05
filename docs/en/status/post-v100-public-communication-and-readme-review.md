# post-v1.0.0 Public Communication and README Review

## Purpose

This document reviews public-facing communication and README wording risks after publication of AAEF v1.0.0.

It supports issue #388, `[Track] post-v1.0.0: Repository and Roadmap Review`.

The goal is not to update README or publish an announcement directly. The goal is to identify whether the current public-facing posture could cause readers to misunderstand the AAEF v1.0.0 release as an active baseline update, certification claim, compliance claim, audit/legal claim, production-readiness claim, implementation-conformance claim, or external-framework-equivalence claim.

This document is review material only. It does not publish a new release, change the active baseline, update README release posture directly, update citation status, approve public announcement text, update the control catalog, update control IDs, update the evidence schema, update assessment artifacts, update testing procedures, add validators, add prototypes, add fixtures, or add JSON examples.

## Current context

AAEF v1.0.0 has been published as:

- Release: `AAEF v1.0.0 Stable Release Path Planning Release`
- Tag: `v1.0.0`
- Release URL: `https://github.com/mkz0010/agentic-authority-evidence-framework/releases/tag/v1.0.0`
- Release commit: `885dd56`

The release posture remains conservative:

- active control and assessment baseline remains unchanged;
- no control catalog update;
- no control ID update;
- no evidence schema update;
- no assessment artifact update;
- no testing procedure update;
- no executable validator update;
- no prototype, fixture, or JSON example update;
- no implementation readiness claim;
- no adoption readiness claim;
- no operational readiness claim;
- no production readiness claim;
- no implementation conformance claim;
- no certification, compliance, or conformity claim;
- no audit or legal sufficiency claim;
- no external-framework equivalence claim.

## Review question

The core review question is:

> Does the public-facing project entrypoint and release communication posture make it clear that AAEF v1.0.0 is a conservative release path planning release, not an active baseline update or assurance claim?

This review treats that question as more important than adding new material.

## Public-facing risk model

The main risk is reader compression.

Readers may compress:

- `v1.0.0` into "new active baseline";
- "stable release path" into "stable standard";
- "readiness review" into "ready";
- "assessment artifact" into "audit sufficiency";
- "testing procedure" into "conformance test";
- "validator" into "semantic correctness";
- "external mapping" into "compliance or equivalence";
- "adoption guidance" into "implementation readiness";
- "release" into "certification-quality maturity."

The repository should avoid wording that increases these compression risks.

## README review posture

README should remain clear on the following distinctions:

| Distinction | Desired public-facing posture |
| --- | --- |
| Latest release vs active baseline | The latest release may be v1.0.0, but the active baseline is unchanged unless explicitly updated. |
| Planning/status artifacts vs baseline artifacts | Planning/status artifacts support review and traceability; they do not automatically update the baseline. |
| Validators vs assurance | Validators support repository hygiene and structural checks; they do not prove semantic correctness or implementation conformance. |
| Assessment/testing artifacts vs sufficiency | Assessment/testing artifacts support review; they do not prove audit sufficiency, legal sufficiency, or conformance. |
| External mappings vs equivalence | External mappings are conservative orientation aids; they are not compliance or equivalence claims. |
| Guidance vs readiness | Implementation/adoption guidance does not establish implementation readiness, adoption readiness, operational readiness, or production readiness. |

## README update decision options

### Option A: Preserve README unchanged for now

Meaning:

- No README wording change is made immediately.
- v1.0.0 release notes and status documents continue to carry the conservative release posture.
- #388 continues reviewing communication risk before deciding whether README changes are needed.

Benefits:

- Avoids unnecessary churn immediately after release.
- Preserves current repository entrypoint until a specific wording gap is identified.
- Keeps #388 focused on review before editing.

Risks:

- Readers who only read README may not see the v1.0.0 active-baseline-unchanged posture quickly enough.
- Release posture may require clicking into release notes or status documents.

Initial assessment:

- Acceptable if README already contains clear baseline and non-claim language.
- If README lacks a concise version/baseline status note, Option B may be safer.

### Option B: Add a narrow version and baseline status note

Meaning:

- Add a short README note stating the latest release and active-baseline posture.
- Keep the change narrow.
- Avoid broad README restructuring.

Possible safe wording:

> Latest release: AAEF v1.0.0.
>
> AAEF v1.0.0 is a conservative release path planning release. It does not change the active control and assessment baseline, and it does not establish certification, compliance, conformity, audit sufficiency, legal sufficiency, implementation conformance, production readiness, or external-framework equivalence.

Benefits:

- Reduces reader confusion at the public entrypoint.
- Separates release version from active baseline.
- Keeps the update small and low risk.

Risks:

- Adds another status statement that must be maintained.
- If too prominent, may distract from the core framework explanation.

Initial assessment:

- Strong candidate if public communication is expected soon.

### Option C: Add a larger post-v1.0.0 README restructuring

Meaning:

- Reorganize README around release status, active baseline, entrypoints, adoption guidance, and research positioning.

Benefits:

- Could make the repository easier for new readers.

Risks:

- Higher churn.
- Higher claim-boundary risk.
- Could unintentionally elevate planning/status material into perceived baseline material.
- Should not be done without a dedicated README/navigation update plan.

Initial assessment:

- Not recommended as the immediate post-v1.0.0 action.

### Option D: Publish external announcement before README review

Meaning:

- Publish Zenn, Qiita, LinkedIn, or similar public communication before README/public-entrypoint wording is reviewed.

Benefits:

- Uses release momentum.

Risks:

- Higher chance of overclaiming or inconsistent wording.
- Public readers may arrive at README without clear active-baseline guidance.

Initial assessment:

- Not recommended before public-facing README wording risk is resolved or explicitly accepted.

## Recommended communication posture

Recommended posture:

> Keep public-facing wording conservative and claim-boundary-first.
>
> Prefer a narrow README status clarification if the current README does not clearly distinguish latest release from active baseline.
>
> Do not publish broad external announcement text until README/public-entrypoint wording risk has been reviewed or accepted.

## Safe wording patterns

Safe patterns:

- "AAEF v1.0.0 is a conservative release path planning release."
- "The active control and assessment baseline remains unchanged."
- "Planning and readiness-review artifacts do not automatically update the active baseline."
- "AAEF does not provide certification, compliance, conformity, audit, or legal sufficiency claims."
- "AAEF does not claim external-framework equivalence."
- "Validators support repository hygiene and structural checks, not semantic correctness or implementation conformance."
- "Examples and fixtures are illustrative unless explicitly stated otherwise."

## Wording to avoid

Avoid wording that implies:

- "v1.0.0 is the new active baseline" unless a later baseline update explicitly says so;
- "AAEF is production-ready";
- "AAEF is certified";
- "AAEF provides compliance";
- "AAEF proves implementation conformance";
- "AAEF is audit-ready";
- "AAEF is legally sufficient";
- "AAEF is equivalent to NIST / ISO / OWASP / MITRE frameworks";
- "validators prove correctness";
- "assessment artifacts prove sufficiency";
- "readiness-review tracks make implementations ready."

## Public announcement review posture

Before any public announcement, confirm:

- release URL is correct;
- release scope is conservative;
- active baseline unchanged wording is included;
- non-claim boundaries are included;
- "Model output is not authority" remains central;
- no certification/compliance/audit/legal/equivalence claim is implied;
- no implementation/adoption/operational/production readiness claim is implied;
- no active baseline update is implied;
- announcement links to release notes or repository status material.

## Public announcement candidate framing

If a public announcement is prepared later, a safe high-level framing is:

> AAEF v1.0.0 has been published as a conservative release path planning release.
>
> The release completes a series of readiness-review and release-planning tracks while preserving the active control and assessment baseline unchanged.
>
> AAEF continues to focus on action authority, execution boundaries, evidence, reviewability, and risk-owner decision support under the principle that model output is not authority.

This is not approved announcement text. It is a safe framing candidate for later review.

## Review findings

Initial finding:

- The most important communication risk is active-baseline confusion.
- The second most important communication risk is overclaiming readiness or conformance.
- The third most important communication risk is treating external mappings as equivalence.
- A narrow README status clarification may be useful if external communication is planned.
- A broad README restructuring is not recommended as the immediate next step.
- External announcement should wait until README/public-entrypoint wording risk is accepted or addressed.

## Recommended next decision

Recommended decision for maintainers:

> Decide whether to preserve README unchanged for now or prepare a narrow README version/baseline status note.

If the answer is "preserve README unchanged," then #388 can proceed to next-roadmap options or close-readiness.

If the answer is "add a narrow README note," that should be handled as a separate explicitly scoped PR that does not update the active baseline or make new claims.

## Potential follow-up issues or PRs

Potential follow-ups:

- narrow README version/baseline status note;
- README/public entrypoint wording cleanup;
- post-v1.0.0 public announcement draft review;
- next-roadmap options note;
- post-v1.0.0 close-readiness checklist.

## Non-goals

This review does not:

- publish a new release;
- change the active baseline;
- update README directly;
- update citation status;
- approve public announcement text;
- update the control catalog;
- update control IDs;
- update the evidence schema;
- update assessment artifacts;
- update testing procedures;
- add executable validators;
- add executable prototypes;
- add scenario fixtures;
- add JSON examples;
- claim implementation readiness;
- claim adoption readiness;
- claim operational readiness;
- claim production readiness;
- claim implementation conformance;
- claim certification, compliance, or conformity;
- claim audit or legal sufficiency;
- claim automated risk acceptance;
- claim control conformance;
- claim external-framework equivalence.

## Close-readiness contribution

This artifact supports #388 by reviewing:

- README release posture risk;
- public-facing wording risk;
- active-baseline-unchanged communication risk;
- public announcement timing risk;
- safe and unsafe wording patterns;
- whether README should remain unchanged or receive a narrow status note.

#388 should remain open until maintainers decide whether to add a narrow README note, proceed to next-roadmap options, or move directly to a close-readiness checklist.
