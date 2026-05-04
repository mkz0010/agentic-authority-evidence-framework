# v1.0.0 Role Guidance Readiness Review

## Purpose

This document reviews role guidance readiness for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #374, `[Track] v1.0.0: Implementation and Adoption Guidance Readiness Review`
- `docs/en/status/v100-implementation-adoption-guidance-readiness-review.md`
- `docs/en/status/v100-adoption-entrypoint-and-navigation-readiness-review.md`
- completed track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- completed track #357, `[Track] v1.0.0: Control Catalog and Baseline Artifact Readiness Review`
- completed track #363, `[Track] v1.0.0: Evidence Schema, Examples, and Validator Readiness Review`
- completed track #369, `[Track] v1.0.0: Assessment Artifact and Testing Procedure Readiness Review`

The goal is to review whether current role-specific guidance is ready for v1.0.0 planning, what appears stable enough to preserve, what may need later clarification, and what claim boundaries must be maintained.

This document is readiness-review material only. It does not update role guidance, README entry points, document navigation, implementation guidance, examples, validators, assessment artifacts, testing procedures, the active baseline, the control catalog, release tags, or GitHub Releases.

## Current posture

As of this review:

- v1.0.0 path planning is active under roadmap #350.
- #374 is reviewing implementation and adoption guidance readiness.
- Implementation/adoption guidance readiness has been reviewed at the planning level.
- Adoption entrypoint and navigation readiness has been reviewed at the planning level.
- The current control catalog and control IDs are preserved by default for v1.0.0 planning.
- The current evidence schema, examples, fixtures, and validators are preserved by default unless later explicit updates are scoped.
- Current assessment artifacts and testing procedures are preserved by default unless later explicit updates are scoped.
- README release posture, navigation, release notes, and citation status are preserved by default while v1.0.0 planning remains open.
- Role guidance is not updated by this document.
- Any future v1.0.0 role guidance update must be explicit.

## Review posture

The recommended posture is:

> Treat role guidance as practical orientation for different readers, not as a claim that AAEF proves readiness, conformance, certification, compliance, audit sufficiency, legal sufficiency, or external-framework equivalence.
>
> Preserve current role guidance by default while identifying where targeted clarification may improve adoption.
>
> Keep role guidance aligned with the current active baseline, current release posture, and scoped status of examples, validators, assessment artifacts, and testing procedures.

This posture supports adoption without turning role-specific guidance into assurance claims.

## Role guidance readiness summary

| Role | Initial readiness posture | Follow-up need |
| --- | --- | --- |
| Implementer | Review-readiness candidate | Clarify guidance vs implementation conformance. |
| Operator | Stable guidance candidate | Preserve operational support without operational-readiness claims. |
| Auditor / reviewer | Stable guidance candidate | Preserve evidence-request support without audit sufficiency claims. |
| Evidence requester | Stable guidance candidate | Preserve action-bound evidence request boundaries. |
| Risk owner / executive | Stable guidance candidate | Preserve decision support without automated risk acceptance. |
| Security architect | Stable guidance candidate | Preserve architecture interpretation without production-readiness claims. |
| Legal / compliance reviewer | Conservative guidance candidate | Preserve non-legal, non-compliance, non-equivalence posture. |
| Researcher | Review-readiness candidate | Preserve research positioning without empirical or peer-reviewed acceptance claims. |
| Maintainer | Review-readiness candidate | Preserve baseline, release, index, and validation discipline. |
| Public communicator | Later release-readiness work | Preserve claim-boundary and release-posture discipline. |

## Role guidance role

Role guidance should help each reader understand:

- which AAEF artifacts are relevant to their responsibilities;
- what questions they should ask;
- what evidence they should look for;
- what decisions remain theirs;
- what artifacts are planning or status material;
- what artifacts are current baseline material;
- what artifacts are illustrative or repository hygiene support;
- what AAEF does not claim; and
- where later v1.0.0 readiness work may continue.

Role guidance should not imply:

- a role can rely on AAEF as certification,
- a role can treat AAEF as legal advice,
- a role can treat AAEF as an audit opinion,
- a role can treat AAEF as implementation conformance proof,
- a role can treat validators as semantic assurance,
- a role can treat examples as complete coverage,
- a role can treat assessment/testing artifacts as sufficiency mechanisms, or
- a role can treat risk-owner support as automated risk acceptance.

## Implementer guidance readiness

Implementer guidance should help implementers understand:

- how to separate model output from authority;
- how action requests, authorization decisions, tool dispatch, backend verification, and evidence relate;
- how to reason about trusted and untrusted inputs;
- how to produce action-bound evidence;
- how to avoid using model output as an execution grant;
- how to avoid relying only on agent runtime self-report;
- how examples and fixtures may support understanding; and
- how assessment and testing materials may support review.

Implementer guidance should not imply:

- AAEF provides a reference implementation;
- AAEF guarantees implementation conformance;
- examples or fixtures are required architecture;
- validators prove implementation correctness;
- following guidance proves production readiness; or
- a specific runtime, policy engine, gateway, evidence store, or vendor is required.

Initial assessment:

- Implementer guidance is a review-readiness candidate.
- Current guidance should be preserved by default.
- Targeted clarification may be useful later to improve discoverability and implementation-path orientation.
- Any future update should avoid implementation conformance, production readiness, and complete security architecture claims.

## Operator guidance readiness

Operator guidance should help operators understand:

- what evidence to review during operation;
- how to recognize missing, conflicting, or insufficient evidence;
- how to handle exception, hold, blocked, denied, or freeze-like situations where applicable;
- when to escalate to reviewers, maintainers, approvers, or risk owners;
- how operational reconstruction support may be used;
- how residual uncertainty should be preserved; and
- how operational records should support later review.

Operator guidance should not imply:

- following AAEF guidance guarantees safe operation;
- AAEF establishes operational readiness;
- AAEF is an incident-response certification;
- operational reconstruction is complete root-cause analysis;
- evidence review eliminates residual uncertainty; or
- operator action replaces risk-owner accountability.

Initial assessment:

- Operator guidance is a strong stable guidance candidate.
- Current operator guidance should be preserved by default.
- Later targeted navigation or handoff clarification may be useful.
- Any future update should avoid operational-readiness and safe-operation guarantee claims.

## Auditor and reviewer guidance readiness

Auditor and reviewer guidance should help reviewers understand:

- what action-bound evidence to request;
- how to distinguish authority, authorization, dispatch, backend result, and outcome evidence;
- how to distinguish independently generated or corroborated evidence from self-report;
- how to evaluate evidence gaps and residual uncertainty;
- how to use assessment artifacts and testing procedures as support material;
- how to avoid equating repository validation with implementation assurance; and
- how to record scope limitations.

Auditor and reviewer guidance should not imply:

- AAEF provides audit sufficiency;
- AAEF produces an audit opinion;
- AAEF provides certification or compliance results;
- worksheet completion proves assessment sufficiency;
- testing procedure execution proves testing sufficiency;
- validator success proves semantic correctness; or
- examples prove implementation coverage.

Initial assessment:

- Auditor and reviewer guidance is a strong stable guidance candidate.
- Current guidance should remain review-support material.
- Future role guidance may clarify how auditors and reviewers navigate evidence schema, examples, assessment artifacts, and testing procedures.
- Audit sufficiency and compliance claims should remain out of scope.

## Evidence requester guidance readiness

Evidence requester guidance should help users request:

- action-bound evidence;
- principal, delegated authority, or relying-party context where applicable;
- authorization decision artifacts;
- dispatch or enforcement records;
- backend verification or relying-party result records;
- evidence events;
- evidence gap records;
- residual uncertainty notes; and
- risk-owner decision package inputs.

Evidence requester guidance should not imply:

- all evidence requests are universally required;
- requested evidence is automatically sufficient;
- absence of evidence always means confirmed control failure;
- evidence schema validity proves real-world truth;
- evidence event examples are complete scenario coverage; or
- evidence request guidance replaces reviewer judgment.

Initial assessment:

- Evidence requester guidance is a strong stable guidance candidate.
- Future role guidance may make evidence requester pathways easier to find.
- Evidence request boundaries from #363 and #369 should be preserved.

## Risk owner and executive guidance readiness

Risk owner and executive guidance should help decision-makers understand:

- what decision they are being asked to make;
- what evidence supports the decision;
- what evidence gaps remain;
- what residual uncertainty remains;
- whether to accept, reject, request evidence, defer, or escalate;
- what follow-up actions are required;
- who owns remaining risk; and
- how decisions should be recorded.

Risk owner and executive guidance should not imply:

- AAEF automates risk acceptance;
- a decision matrix makes the decision by itself;
- a decision package eliminates uncertainty;
- evidence presence eliminates risk;
- AAEF certifies that a system is safe;
- AAEF proves operational or production readiness; or
- AAEF replaces management accountability.

Initial assessment:

- Risk-owner decision support is a strong stable guidance candidate.
- Current materials should be preserved by default.
- Later role guidance may improve reader navigation for risk owners and executives.
- Automated risk acceptance claims should remain out of scope.

## Security architect guidance readiness

Security architect guidance should help architects understand:

- authority boundaries;
- authorization decision point expectations;
- tool dispatch enforcement point expectations;
- backend verification boundaries;
- evidence production boundaries;
- trusted and untrusted input separation;
- reference architecture patterns;
- how examples relate to architecture concepts; and
- where organization-specific design review is still required.

Security architect guidance should not imply:

- AAEF provides complete security design coverage;
- AAEF provides production-ready architecture;
- a single architecture is required;
- reference architecture material is a reference implementation;
- architecture guidance proves control conformance; or
- design patterns eliminate the need for threat modeling.

Initial assessment:

- Security architecture guidance is a stable guidance candidate.
- Current guidance should be preserved by default.
- Later targeted navigation may help architects find relevant materials.
- Production reference implementation claims should remain future work unless separately scoped.

## Legal and compliance reviewer guidance readiness

Legal and compliance guidance should help reviewers understand:

- the scope and limits of AAEF;
- what AAEF does not claim;
- how external mappings should be read conservatively;
- where legal advice is outside the framework;
- where regulatory compliance conclusions are outside the framework;
- how adoption may support internal review without asserting compliance; and
- what questions legal/compliance reviewers should ask.

Legal and compliance guidance should not imply:

- AAEF provides legal advice;
- AAEF establishes legal sufficiency;
- AAEF establishes regulatory compliance;
- AAEF provides conformity assessment;
- AAEF is equivalent to external frameworks;
- external mappings prove compliance; or
- public communication can claim more than scoped artifacts support.

Initial assessment:

- Legal/compliance guidance should remain conservative.
- External mapping posture should remain non-equivalence-oriented.
- Future role guidance may improve readability without changing claims.
- Legal sufficiency, compliance, conformity, and equivalence claims should remain out of scope.

## Researcher guidance readiness

Researcher guidance should help researchers understand:

- the framework thesis;
- research positioning;
- candidate contribution areas;
- research questions;
- claim boundaries;
- what has been planned versus validated;
- what remains empirical work; and
- what should not be overstated.

Researcher guidance should not imply:

- AAEF has peer-reviewed acceptance;
- AAEF has empirical validation unless separately supported;
- AAEF is an adopted standard;
- AAEF is a certification scheme;
- planning artifacts are research results by themselves; or
- future-work concepts are already mature claims.

Initial assessment:

- Researcher guidance is a review-readiness candidate.
- Current research positioning should remain conservative.
- Future updates may help researchers navigate v1.0.0 readiness material.
- Peer-reviewed acceptance and empirical validation claims should remain out of scope unless separately supported.

## Maintainer guidance readiness

Maintainer guidance should help maintainers preserve:

- active baseline boundaries;
- release tag and GitHub Release discipline;
- control catalog and control ID stability;
- document map and status README registration discipline;
- validator scope discipline;
- example and fixture claim boundaries;
- issue, PR, milestone, and label discipline;
- release communication boundaries; and
- historical artifact context.

Maintainer guidance should not imply:

- merging planning artifacts changes the active baseline;
- status documents are release artifacts by themselves;
- validator success proves assurance;
- examples prove coverage;
- release posture changes without explicit release artifacts; or
- roadmap closure equals publication.

Initial assessment:

- Maintainer guidance is a review-readiness candidate.
- Existing repo discipline appears strong.
- Future role guidance may explicitly describe maintainer responsibilities for v1.0.0 release readiness.

## Public communicator guidance readiness

Public communication guidance should help communicators explain:

- what AAEF is;
- what version or release is being discussed;
- what the current active baseline is;
- what v1.0.0 planning means;
- what AAEF does not claim;
- how to avoid certification, compliance, audit, legal, equivalence, readiness, and conformance overclaims;
- how to describe examples, validators, assessment artifacts, and testing procedures conservatively; and
- how to direct readers to release artifacts and documentation.

Public communication guidance should not imply:

- v1.0.0 is released before release artifacts exist;
- planning status equals publication;
- AAEF proves adoption readiness;
- AAEF proves production readiness;
- AAEF has regulatory approval;
- AAEF has external-framework equivalence; or
- AAEF has peer-reviewed acceptance unless separately supported.

Initial assessment:

- Public communication guidance should be handled in later release readiness and communication planning.
- #374 should preserve public communication boundaries without updating release messaging by default.

## Cross-role responsibility boundaries

Role guidance should preserve responsibility separation:

| Role | Owns or supports | Should not be assigned |
| --- | --- | --- |
| Implementer | Design and implementation choices | Certification, legal sufficiency, audit opinion |
| Operator | Operational review and escalation | Automated risk acceptance |
| Auditor / reviewer | Evidence request and review judgment | Product certification by AAEF alone |
| Evidence requester | Evidence request framing | Evidence sufficiency conclusion by request alone |
| Risk owner / executive | Risk decision and residual uncertainty ownership | Delegating risk acceptance to the framework |
| Security architect | Architecture interpretation and design review | Claiming production readiness from guidance alone |
| Legal/compliance reviewer | Legal/compliance question framing | Treating AAEF as legal advice or compliance proof |
| Researcher | Research framing and question development | Peer-reviewed or empirical claims without support |
| Maintainer | Repository, release, baseline, and validation discipline | Silent baseline or release posture changes |
| Public communicator | Accurate public explanation | Overclaiming readiness, conformance, compliance, or equivalence |

## Relationship to adoption entrypoints and navigation

Role guidance should build on adoption entrypoints and navigation by:

- making reader paths concrete;
- mapping reader roles to relevant artifacts;
- preserving current baseline and release posture;
- keeping role-specific claims conservative;
- separating planning/status material from baseline material;
- avoiding implicit README or release-note updates; and
- supporting later decision options.

This review does not update entrypoints or navigation.

## Relationship to implementation/adoption guidance

Role guidance should support implementation/adoption guidance by:

- identifying reader-specific guidance needs;
- clarifying stable guidance candidates;
- distinguishing adoption support from adoption readiness claims;
- preserving implementation flexibility;
- preserving reviewer judgment;
- preserving risk-owner accountability; and
- keeping claim boundaries visible.

This review does not update implementation or adoption guidance.

## Relationship to examples, validators, assessment artifacts, and testing procedures

Role guidance should preserve the following boundaries:

- examples are illustrative unless explicitly scoped otherwise;
- fixtures are scoped support material unless explicitly scoped otherwise;
- validators support repository hygiene, not semantic correctness or assurance;
- assessment artifacts support reviewer judgment, not assessment sufficiency by themselves;
- testing procedures support review, not testing sufficiency by themselves;
- evidence schema validity does not prove evidence sufficiency; and
- role guidance should not turn any support artifact into a conformance mechanism.

## Role guidance update options

This review leaves several options open.

### Option A: Preserve current role guidance unchanged

Meaning:

- Existing role guidance and navigation remain unchanged.

Benefits:

- Lowest churn.
- Avoids accidental readiness or conformance claims.
- Avoids release posture changes.

Risks:

- Reader-specific paths may remain less discoverable.

### Option B: Preserve guidance and add explanatory role navigation later

Meaning:

- Existing guidance remains unchanged.
- Later material maps reader roles to existing artifacts.

Benefits:

- Improves usability without changing baseline or release posture.
- Supports adoption while reducing overclaim risk.

Risks:

- Requires careful wording to avoid readiness claims.

### Option C: Apply targeted role guidance clarification later

Meaning:

- Specific role guidance is clarified after explicit review.

Benefits:

- Improves reader relevance.
- Can reduce ambiguity for implementers, operators, auditors, risk owners, legal/compliance reviewers, architects, and researchers.

Risks:

- May imply readiness, conformance, audit, legal, compliance, or production claims if overdescribed.

### Option D: Create a role-specific guidance gap register later

Meaning:

- A later artifact lists role guidance gaps and possible update candidates.

Benefits:

- Helps prioritize adoption work.
- Avoids changing guidance before gaps are reviewed.

Risks:

- Adds planning overhead.

### Option E: Broader role guidance redesign

Meaning:

- Role guidance is redesigned across major reader groups.

Benefits:

- Potentially clearer long-term adoption experience.

Risks:

- High scope creep.
- High release communication burden.
- High overclaim risk.
- Not recommended by default for near-term v1.0.0 readiness review.

## Initial recommendation

The initial recommendation is:

> Preserve current role guidance by default.
>
> Treat explanatory role navigation and targeted role guidance clarification as likely useful later options.
>
> Consider a role-specific guidance gap register if maintainers want to prioritize future guidance work.
>
> Defer broad role guidance redesign until release readiness and communication needs are clearer.
>
> Keep all role guidance separate from implementation conformance, adoption readiness, operational readiness, production readiness, certification, compliance, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, and external-framework equivalence claims.

This keeps v1.0.0 adoption guidance practical while preserving conservative claim boundaries.

## Recommended follow-up work for #374

Recommended #374 follow-up candidates:

- implementation/adoption guidance decision options,
- implementation/adoption guidance close-readiness checklist.

Optional follow-up candidates:

- README and document navigation update options,
- public communication boundary note,
- role-specific guidance gap register.

## Claim boundaries

This review does not claim:

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

- Does this review preserve role guidance stability?
- Does it avoid implicitly updating role guidance?
- Does it distinguish role guidance from readiness claims?
- Does it distinguish role guidance from implementation conformance?
- Does it preserve reviewer judgment and risk-owner accountability?
- Does it preserve audit, legal, compliance, and equivalence boundaries?
- Does it identify major reader roles clearly?
- Does it connect role guidance to adoption entrypoints and navigation?
- Does it preserve claim boundaries?
- Does it provide enough direction for later #374 artifacts?

## Scope reminder

This artifact is readiness-review material only.

It does not update the active control and assessment baseline, control catalog, control IDs, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, README release posture, navigation, citation status, release notes, role guidance, release tags, or GitHub Releases.

It does not establish implementation readiness, adoption readiness, operational readiness, production readiness, implementation conformance, assessment sufficiency, testing sufficiency, evidence sufficiency, semantic correctness, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, control conformance, or external-framework equivalence.
