# v1.0.0 Implementation and Adoption Guidance Decision Options

## Purpose

This document records decision options for implementation and adoption guidance on the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #374, `[Track] v1.0.0: Implementation and Adoption Guidance Readiness Review`
- `docs/en/status/v100-implementation-adoption-guidance-readiness-review.md`
- `docs/en/status/v100-adoption-entrypoint-and-navigation-readiness-review.md`
- `docs/en/status/v100-role-guidance-readiness-review.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- completed track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`
- completed track #369, `[Track] v1.0.0: Assessment Artifact and Testing Procedure Readiness Review`

The goal is to make implementation/adoption guidance update or non-update choices explicit before any v1.0.0 release-readiness decision.

This document is readiness-review and decision-support material only. It does not update implementation guidance, adoption guidance, README entry points, navigation, role guidance, examples, validators, assessment artifacts, testing procedures, the active baseline, the control catalog, release tags, or GitHub Releases.

## Current posture

As of this review:

- v1.0.0 path planning is active under roadmap #350.
- #374 has reviewed implementation/adoption guidance readiness at the planning level.
- #374 has reviewed adoption entrypoint/navigation readiness at the planning level.
- #374 has reviewed role guidance readiness at the planning level.
- The current control catalog and control IDs are preserved by default for v1.0.0 planning.
- The current evidence schema, examples, fixtures, and validators are preserved by default unless later explicit updates are scoped.
- Current assessment artifacts and testing procedures are preserved by default unless later explicit updates are scoped.
- README release posture, navigation, release notes, citation status, and role guidance are preserved by default unless later explicit updates are scoped.
- The active control and assessment baseline has not been changed by #374.
- Any future implementation/adoption guidance, README, navigation, role guidance, release-note, or citation update must be explicit.

## Decision posture

The recommended posture is:

> Keep implementation and adoption guidance decisions explicit.
>
> Do not allow guidance availability, README visibility, navigation clarity, role guidance, examples, validators, assessment artifacts, or testing procedures to imply implementation readiness, adoption readiness, operational readiness, production readiness, implementation conformance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
>
> Prefer stability, explanatory navigation, and targeted clarification before broader guidance redesign or release-posture updates.

This keeps the v1.0.0 path usable without converting adoption guidance into a readiness or assurance claim.

## Decision options summary

| Option | Summary | Initial posture |
| --- | --- | --- |
| Option A | Preserve current implementation/adoption guidance unchanged. | Safest stability option. |
| Option B | Preserve guidance and add explanatory navigation later. | Strong low-churn usability option. |
| Option C | Apply targeted adoption entrypoint or navigation updates later. | Possible if discoverability gaps are identified. |
| Option D | Apply targeted role guidance clarification later. | Possible if role-specific ambiguity is identified. |
| Option E | Defer README release posture, citation, and release-note updates to release readiness. | Recommended default while v1.0.0 planning remains open. |
| Option F | Create a role-specific guidance gap register later. | Useful prioritization option if guidance gaps grow. |
| Option G | Add a public communication boundary note later. | Useful before external release communication. |
| Option H | Broader implementation/adoption guidance redesign. | Not recommended by default for v1.0.0. |
| Option I | Treat guidance as readiness, conformance, certification, compliance, audit, legal, or equivalence proof. | Non-goal. |

## Option A: Preserve current implementation/adoption guidance unchanged

Meaning:

- Current implementation guidance remains unchanged.
- Current adoption guidance remains unchanged.
- README release posture remains unchanged.
- Navigation remains unchanged except for normal index registration.
- Role guidance remains unchanged.
- Release notes and citation material remain unchanged.

Benefits:

- Lowest churn.
- Avoids accidental release posture changes.
- Avoids implying v1.0.0 publication.
- Avoids implying active baseline changes.
- Keeps v1.0.0 planning scope controlled.

Risks:

- New readers may still need clearer reader paths.
- Role-specific adoption paths may remain less discoverable.
- Later release communication work remains necessary.

Best fit when:

- maintainers prioritize stability;
- v1.0.0 release posture is not final; and
- guidance changes can wait for later release-readiness review.

## Option B: Preserve guidance and add explanatory navigation later

Meaning:

- Existing guidance remains unchanged.
- Later explanatory navigation helps readers find relevant artifacts by role or use case.
- Navigation clarifies current baseline, planning material, stable guidance candidates, and future-work areas without changing release posture.

Benefits:

- Improves usability without changing baseline artifacts.
- Helps separate role guidance from release declarations.
- Supports implementers, operators, auditors, risk owners, legal/compliance reviewers, security architects, and researchers.
- Lower risk than README release posture updates.

Risks:

- Requires careful wording to avoid adoption-readiness claims.
- Does not mechanically update README or role guidance.
- May still require later release communication work.

Best fit when:

- current artifacts are useful but harder to navigate;
- role-specific discovery should improve; and
- maintainers want to avoid premature release claims.

## Option C: Apply targeted adoption entrypoint or navigation updates later

Meaning:

- README, document map, status README, or top-level entrypoints may be updated after explicit review.
- Updates are narrow and focused on discoverability or baseline/release-posture clarity.

Benefits:

- Improves first-reader experience.
- Can make current baseline and v1.0.0 planning status clearer.
- Can reduce confusion between active baseline, planning material, historical material, and release artifacts.

Risks:

- May imply v1.0.0 release if not carefully scoped.
- May imply baseline change if wording is unclear.
- Requires release communication review.
- Requires localized entrypoint alignment if localized README files are updated.

Best fit when:

- specific entrypoint gaps are identified;
- updates are narrow and non-normative; and
- release posture boundaries are explicit.

## Option D: Apply targeted role guidance clarification later

Meaning:

- Specific role guidance is clarified after explicit review.
- Candidate reader groups include implementers, operators, auditors/reviewers, evidence requesters, risk owners/executives, security architects, legal/compliance reviewers, researchers, maintainers, and public communicators.

Benefits:

- Improves adoption for specific audiences.
- Helps each role understand relevant artifacts and boundaries.
- Can reduce misuse of examples, validators, assessment artifacts, and testing procedures.
- Can preserve responsibility boundaries more clearly.

Risks:

- May imply implementation readiness or adoption readiness if overdescribed.
- May imply operational readiness for operators.
- May imply audit sufficiency for auditors.
- May imply legal or compliance sufficiency for legal/compliance readers.
- May imply production readiness for security architects.

Best fit when:

- a specific role has a known navigation or interpretation gap;
- the clarification is narrow; and
- conservative claim boundaries are preserved.

## Option E: Defer README release posture, citation, and release-note updates to release readiness

Meaning:

- README release posture remains unchanged during #374.
- Citation status remains unchanged during #374.
- Release notes remain unchanged during #374.
- Final communication updates wait until release readiness and final v1.0.0 decision work.

Benefits:

- Avoids premature v1.0.0 publication claims.
- Avoids accidental active baseline changes.
- Keeps #374 focused on readiness review rather than publication.
- Preserves release discipline around tags, GitHub Releases, release notes, and citation status.

Risks:

- Release communication work remains outstanding.
- Some readers may not yet see a fully optimized v1.0.0 entrypoint.

Best fit when:

- v1.0.0 is still planning;
- final release posture is not yet decided; and
- maintainers want release communication handled in a dedicated later track.

## Option F: Create a role-specific guidance gap register later

Meaning:

- A later planning artifact lists role-specific guidance gaps and candidate improvements.
- It does not update role guidance itself.

Benefits:

- Helps prioritize guidance work.
- Separates gap identification from guidance changes.
- Supports future roadmap planning.
- Reduces risk of broad unscheduled guidance redesign.

Risks:

- Adds planning overhead.
- May defer concrete guidance improvements.

Best fit when:

- maintainers want clearer prioritization before changing guidance; and
- role-specific needs are expected to expand after v1.0.0.

## Option G: Add a public communication boundary note later

Meaning:

- A later artifact records safe public communication wording for v1.0.0.
- It clarifies how to describe baseline status, release status, planning artifacts, examples, validators, assessment/testing material, adoption guidance, and non-goals.

Benefits:

- Reduces external overclaim risk.
- Helps prepare release notes, announcements, README updates, and social/public messaging.
- Preserves distinction between useful framework guidance and certification/compliance/equivalence claims.

Risks:

- May overlap with release readiness and communication planning.
- Should not be treated as release notes by itself.

Best fit when:

- public release or announcement planning is approaching; and
- maintainers want wording guardrails before external communication.

## Option H: Broader implementation/adoption guidance redesign

Meaning:

- Implementation guidance, adoption guidance, README entrypoints, role guidance, navigation, release communication, and possibly examples are redesigned together.

Benefits:

- Potentially clearer long-term adoption experience.
- Can create a more polished role-based adoption package.

Risks:

- High scope creep.
- High risk of implied release posture changes.
- High risk of readiness, conformance, compliance, audit, legal, or equivalence overclaims.
- May delay v1.0.0 if treated as required.
- Requires broad review across baseline, schema, examples, validators, assessment, testing, release communication, citation, and public messaging.

Initial posture:

- Future work by default.
- Not recommended as the default #374 or near-term v1.0.0 path.

## Option I: Treat implementation/adoption guidance as readiness, conformance, certification, compliance, audit, legal, or equivalence proof

Meaning:

- Guidance is positioned as proving implementation readiness, adoption readiness, operational readiness, production readiness, implementation conformance, certification, compliance, conformity, audit sufficiency, legal sufficiency, control conformance, or external-framework equivalence.

Initial posture:

- Non-goal.
- Should not be selected.

Rationale:

- AAEF does not claim to be a certification scheme.
- AAEF does not claim legal sufficiency.
- AAEF does not claim audit sufficiency.
- AAEF does not claim external-framework equivalence.
- Implementation/adoption guidance supports review and orientation, not final assurance by itself.

## Dependency impact matrix

| Change type | README impact | Navigation impact | Role guidance impact | Release communication impact |
| --- | --- | --- | --- | --- |
| Preserve unchanged | None | Normal index registration only | None | Clarify later if needed. |
| Explanatory navigation | Low | Medium | Low | Must avoid readiness claims. |
| Targeted entrypoint/navigation update | Medium | Medium | Possible role-path impact | Must disclose planning/release posture. |
| Targeted role guidance clarification | Low/medium | Medium | Medium | Must avoid role-specific overclaims. |
| Defer release posture/citation/release notes | None now | None now | None now | Required later. |
| Role guidance gap register | Low | Low | Low | Planning only. |
| Public communication boundary note | Low | Low | Possible wording alignment | Useful before release communication. |
| Broader guidance redesign | High | High | High | High. |
| Readiness/conformance/certification positioning | Not acceptable | Not acceptable | Not acceptable | Non-goal. |

## Option comparison

| Criterion | A | B | C | D | E | F | G | H | I |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Churn | Very low | Low | Medium | Medium | Very low now | Low | Low | Very high | Not acceptable |
| Usability gain | Low | Medium | Medium/high | Medium/high | Low now | Medium later | Medium later | High | Not acceptable |
| Release-posture risk | Low | Low | Medium | Medium | Low | Low | Low/medium | High | Very high |
| False-assurance risk | Low | Low | Medium | Medium | Low | Low | Low/medium | High | Very high |
| Fit for near-term v1.0.0 | Strong | Strong | Possible | Possible | Strong | Optional | Optional | Weak | Non-goal |

## Initial recommendation

The initial recommendation for #374 is:

> Prefer Option B plus Option E as the near-term v1.0.0 posture:
>
> preserve current implementation/adoption guidance while allowing later explanatory navigation, and defer README release posture, citation, and release-note updates to release readiness and final v1.0.0 decision work.
>
> Keep targeted entrypoint/navigation updates, targeted role guidance clarification, a role-specific guidance gap register, and a public communication boundary note available as later scoped options.
>
> Do not pursue broader implementation/adoption guidance redesign by default for v1.0.0.
>
> Do not position implementation/adoption guidance as implementation readiness, adoption readiness, operational readiness, production readiness, implementation conformance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.

This recommendation keeps #374 useful and bounded while preserving release and claim boundaries.

## Entrypoint and navigation decision posture

Implementation/adoption guidance decision options should preserve the following entrypoint/navigation posture:

- README release posture remains unchanged unless explicitly updated later.
- Citation status remains unchanged unless explicitly updated later.
- Release notes remain unchanged unless explicitly updated later.
- Document map and status README registration discipline continues.
- Navigation should distinguish active baseline, planning material, historical material, stable guidance candidates, and future work.
- Navigation should not imply v1.0.0 has been released.
- Navigation should not imply active baseline changes.

This document does not update README, navigation, citation status, or release notes.

## Role guidance decision posture

Implementation/adoption guidance decision options should preserve the following role guidance posture:

- Role guidance helps readers find relevant artifacts.
- Role guidance does not prove readiness or conformance.
- Implementer guidance does not prove implementation correctness.
- Operator guidance does not prove operational readiness.
- Auditor/reviewer guidance does not prove audit sufficiency.
- Legal/compliance guidance does not prove legal sufficiency or regulatory compliance.
- Risk-owner guidance does not automate risk acceptance.
- Researcher guidance does not prove peer-reviewed acceptance or empirical validation.
- Public communication guidance should remain conservative.

This document does not update role guidance.

## Supporting artifact decision posture

Implementation/adoption guidance decision options should preserve the following support-artifact posture:

- Examples are illustrative.
- Fixtures are scoped support material.
- Validators are repository hygiene checks.
- Assessment artifacts support reviewer judgment.
- Testing procedures support reviewer judgment.
- Evidence schema validity does not prove evidence sufficiency.
- Support artifacts should not be described as conformance mechanisms.

This document does not update examples, fixtures, validators, assessment artifacts, testing procedures, or the evidence schema.

## Candidate near-term path

A reasonable near-term path is:

1. Complete implementation/adoption guidance readiness review.
2. Complete adoption entrypoint/navigation readiness review.
3. Complete role guidance readiness review.
4. Document implementation/adoption guidance decision options in this note.
5. Complete implementation/adoption guidance close-readiness checklist.
6. Close #374 if maintainers agree the track is complete.
7. Continue roadmap #350 with release readiness and communication planning.

## Release communication implications

Any future v1.0.0 release communication should state:

- whether the active baseline changed;
- whether README release posture changed;
- whether citation status changed;
- whether release notes were published;
- whether implementation/adoption guidance changed;
- whether role guidance changed;
- whether examples, fixtures, validators, assessment artifacts, or testing procedures changed;
- whether guidance is review-support material rather than readiness proof;
- what claims are not made; and
- what later work remains.

## Recommended decision language

Recommended near-term wording:

> For v1.0.0 planning, preserve current implementation/adoption guidance, README release posture, citation status, release notes, and role guidance by default.
>
> Continue document map and status README registration discipline.
>
> Treat explanatory navigation and targeted role guidance clarification as possible later scoped options.
>
> Defer README release posture, citation, and release-note updates until release readiness and final v1.0.0 decision work is clearer.
>
> Do not treat implementation/adoption guidance, README navigation, role guidance, examples, validators, assessment artifacts, or testing procedures as implementation readiness, adoption readiness, operational readiness, production readiness, implementation conformance, certification, compliance, conformity, audit sufficiency, legal sufficiency, control conformance, automated risk acceptance, or external-framework equivalence proof.

## Follow-up candidates for #374

Recommended #374 follow-up:

- implementation/adoption guidance close-readiness checklist.

Optional follow-up candidates:

- README and document navigation update options,
- public communication boundary note,
- role-specific guidance gap register,
- targeted entrypoint/navigation update proposal,
- targeted role guidance clarification proposal.

## Follow-up candidates for roadmap #350

Recommended later roadmap tracks:

- release readiness and communication planning,
- README / citation / release-note update decision,
- final v1.0.0 release decision.

## Claim boundaries

This decision-options note does not claim:

- v1.0.0 release,
- release tag creation,
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
- release-note update,
- role guidance update,
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

- Does this note make implementation/adoption guidance options explicit?
- Does it avoid implicitly updating implementation guidance?
- Does it avoid implicitly updating adoption guidance?
- Does it avoid implicitly updating README, navigation, citation, release notes, or role guidance?
- Does it preserve release posture and active baseline boundaries?
- Does it preserve role guidance boundaries?
- Does it distinguish guidance from readiness or conformance claims?
- Does it identify false-assurance and release-communication tradeoffs?
- Does it preserve claim boundaries?
- Does it provide enough direction for #374 close-readiness?

## Scope reminder

This artifact is readiness-review and decision-support material only.

It does not update the active control and assessment baseline, control catalog, control IDs, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, README release posture, navigation, citation status, release notes, role guidance, release tags, or GitHub Releases.

It does not establish implementation readiness, adoption readiness, operational readiness, production readiness, implementation conformance, assessment sufficiency, testing sufficiency, evidence sufficiency, semantic correctness, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
