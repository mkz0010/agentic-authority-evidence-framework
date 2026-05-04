# v1.0.0 Claim-Boundary and Non-Goal Checklist

## Purpose

This document provides a claim-boundary and non-goal checklist for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- `docs/en/status/v100-baseline-scope-and-promotion-decision.md`
- `docs/en/status/v100-promoted-artifact-candidate-inventory.md`
- `docs/en/status/v100-planning-only-and-future-work-register.md`
- `docs/en/status/post-v070-version-status-and-baseline-reference-note.md`

The goal is to preserve conservative wording while planning v1.0.0 as a usable stable public baseline candidate.

This document is planning and checklist material only. It does not publish v1.0.0, create a release tag, update the active baseline, update the control catalog, update the evidence schema, update assessment artifacts, update testing procedures, add examples, add fixtures, or add executable validators.

## Checklist posture

This checklist separates usable baseline language from overclaims.

AAEF v1.0.0 may be planned as a usable stable public baseline candidate.

That does not mean that v1.0.0 should claim:

- certification,
- compliance,
- conformity,
- audit sufficiency,
- legal sufficiency,
- external-framework equivalence,
- production readiness,
- implementation conformance,
- empirical validation,
- peer-reviewed acceptance,
- complete risk mitigation,
- complete operational reconstruction, or
- automated risk acceptance.

The checklist should be used when drafting:

- baseline scope documents,
- promotion decisions,
- README updates,
- release notes,
- public announcements,
- assessment guidance,
- implementation guidance,
- operator guidance,
- risk-owner guidance,
- external mapping language, and
- future v1.0.0 release communication.

## Core safe framing

The preferred v1.0.0 framing is:

> AAEF v1.0.0 is being planned as a usable stable public baseline candidate for reviewing AI-agent action authority, execution boundaries, evidence expectations, operational reconstruction, and risk-owner decision support.

This should be paired with:

> AAEF v1.0.0 should not be presented as certification, compliance, audit sufficiency, legal sufficiency, implementation conformance, production readiness, empirical validation, or external-framework equivalence unless separate future work explicitly establishes such a claim.

## Claim-boundary checklist

| Claim area | Allowed posture | Prohibited or unsafe posture |
| --- | --- | --- |
| Stable baseline | May describe v1.0.0 as a planned stable public baseline candidate. | Do not imply the active baseline has changed before an explicit release decision. |
| Usability | May say v1.0.0 should be usable for implementers, reviewers, operators, and risk owners. | Do not imply all implementations are safe or production-ready. |
| Controls | May discuss control catalog readiness or baseline candidates. | Do not imply controls are updated unless the control catalog is explicitly updated. |
| Evidence | May describe evidence expectations, evidence gaps, and evidence review. | Do not imply evidence existence proves sufficiency. |
| Assessment | May describe assessment-support material. | Do not claim certification, compliance, audit sufficiency, or legal sufficiency. |
| Validators | May describe structural validation and validator scope. | Do not imply semantic correctness, implementation conformance, or operational assurance. |
| Examples | May use examples as illustrative or test fixtures. | Do not imply examples prove production readiness. |
| Operational reconstruction | May support reconstruction questions and evidence gap review. | Do not claim complete reconstruction or complete root-cause analysis. |
| Risk-owner decision support | May support accept, reject, request-evidence, defer, and escalate decisions. | Do not automate or replace management judgment. |
| External mappings | May provide conservative contextual mappings. | Do not claim equivalence, substitution, certification, or compliance. |
| Research positioning | May describe candidate research questions or contribution areas. | Do not claim empirical validation or peer-reviewed acceptance without separate support. |
| Implementation guidance | May describe patterns, boundaries, and assumptions. | Do not claim implementation conformance or production readiness. |

## Certification boundary

Checklist:

- Does the text avoid calling AAEF a certification scheme?
- Does it avoid implying that an implementation can be certified under AAEF?
- Does it avoid implying third-party certification, conformity assessment, or accreditation?
- Does it avoid certification-like words unless explicitly negating them?

Safe wording:

> AAEF is not a certification scheme.

Unsafe wording:

> Systems can be certified as AAEF-compliant.

Required posture:

- Certification remains a non-goal for v1.0.0 unless a separate governance and conformity-assessment structure is created later.

## Compliance boundary

Checklist:

- Does the text avoid claiming legal, regulatory, contractual, or industry compliance?
- Does it avoid saying AAEF satisfies external requirements?
- Does it avoid presenting mappings as compliance evidence?
- Does it distinguish framework use from compliance determination?

Safe wording:

> AAEF may help organize action-authority and evidence review, but it does not establish compliance.

Unsafe wording:

> Using AAEF makes an AI-agent system compliant.

Required posture:

- Compliance remains a non-goal for v1.0.0.

## Audit sufficiency boundary

Checklist:

- Does the text avoid claiming audit sufficiency?
- Does it avoid implying that AAEF evidence automatically satisfies an auditor?
- Does it preserve auditor judgment, scope, criteria, and evidence quality?
- Does it distinguish evidence-support material from audit opinion?

Safe wording:

> AAEF can support evidence organization and review questions, but audit sufficiency depends on the audit scope, criteria, evidence quality, and reviewer judgment.

Unsafe wording:

> AAEF evidence is sufficient for audit.

Required posture:

- Audit sufficiency remains a non-goal for v1.0.0.

## Legal sufficiency boundary

Checklist:

- Does the text avoid legal advice?
- Does it avoid determining liability, authorization, or enforceability?
- Does it avoid saying AAEF proves legal authorization?
- Does it preserve the distinction between technical authority evidence and legal authority conclusions?

Safe wording:

> AAEF is not legal advice and does not determine legal sufficiency.

Unsafe wording:

> AAEF proves the action was legally authorized.

Required posture:

- Legal sufficiency remains a non-goal for v1.0.0.

## External-framework equivalence boundary

Checklist:

- Does the text avoid claiming equivalence with NIST, ISO, OWASP, MITRE, CSA, or other frameworks?
- Does it avoid saying AAEF substitutes for another framework?
- Does it avoid presenting mappings as conformance?
- Does it preserve conservative mapping language?

Safe wording:

> External mappings are contextual and conservative; they do not establish equivalence, substitution, or compliance.

Unsafe wording:

> AAEF is equivalent to ISO/IEC 42001 or NIST AI RMF.

Required posture:

- External-framework equivalence remains a non-goal for v1.0.0.

## Production readiness boundary

Checklist:

- Does the text avoid claiming production readiness?
- Does it avoid implying that documentation alone proves deployability?
- Does it preserve implementation assumptions and environment-specific validation?
- Does it distinguish usable public baseline from production system readiness?

Safe wording:

> AAEF v1.0.0 may be usable as a stable public reference, but that does not prove any implementation is production-ready.

Unsafe wording:

> AAEF v1.0.0 makes AI-agent systems production-ready.

Required posture:

- Production readiness remains a non-goal unless separately scoped and validated.

## Implementation conformance boundary

Checklist:

- Does the text avoid claiming implementation conformance?
- Does it avoid saying validators prove conformance?
- Does it distinguish implementation reviewability from implementation correctness?
- Does it preserve the need for implementation-specific review?

Safe wording:

> Implementation reviewability is not implementation conformance.

Unsafe wording:

> Passing repository validators means the implementation conforms to AAEF.

Required posture:

- Implementation conformance remains a non-goal unless a separate conformance model is created.

## Empirical validation boundary

Checklist:

- Does the text avoid claiming empirical validation?
- Does it avoid treating planning artifacts as study results?
- Does it avoid treating repository validation as empirical effectiveness evidence?
- Does it preserve candidate research questions as questions rather than conclusions?

Safe wording:

> AAEF contains candidate research questions and planning material; it does not claim empirical validation unless separate empirical work is performed.

Unsafe wording:

> AAEF has been empirically proven effective.

Required posture:

- Empirical validation remains future work unless separately performed and documented.

## Peer-review boundary

Checklist:

- Does the text avoid claiming peer-reviewed acceptance?
- Does it distinguish research positioning from accepted research contribution?
- Does it avoid implying academic consensus?
- Does it preserve future research posture?

Safe wording:

> AAEF may support future research positioning, but it does not claim peer-reviewed acceptance.

Unsafe wording:

> AAEF is a peer-reviewed standard.

Required posture:

- Peer-reviewed acceptance remains unclaimed unless separately established.

## Validator claim boundary

Checklist:

- Does the text state what validators check?
- Does it state what validators do not check?
- Does it avoid semantic sufficiency claims?
- Does it avoid implementation conformance claims?
- Does it avoid operational assurance claims?

Safe wording:

> Validators check repository artifact structure and scoped consistency. Passing validation does not prove operational effectiveness, implementation conformance, evidence sufficiency, or semantic correctness.

Unsafe wording:

> The validators prove the framework is implemented correctly.

Required posture:

- Validator claims must remain scope-bounded.

## Example and fixture boundary

Checklist:

- Does the text describe examples as illustrative unless explicitly scoped otherwise?
- Does it avoid saying examples prove implementation readiness?
- Does it avoid implying complete scenario coverage?
- Does it preserve negative-example and non-execution boundaries where relevant?

Safe wording:

> Examples and fixtures illustrate scoped artifact expectations; they do not prove production readiness or complete coverage.

Unsafe wording:

> The examples demonstrate full operational readiness.

Required posture:

- Examples support explanation and validation, not production assurance.

## Operational reconstruction boundary

Checklist:

- Does the text avoid claiming complete reconstruction?
- Does it preserve evidence gaps and residual uncertainty?
- Does it avoid claiming complete root-cause analysis?
- Does it avoid claiming absence of all side effects?
- Does it distinguish reconstruction support from incident-response certification?

Safe wording:

> Operational reconstruction material supports review of scoped actions, evidence, gaps, uncertainty, and handoffs. It does not guarantee complete reconstruction or complete root-cause analysis.

Unsafe wording:

> AAEF reconstructs every action completely.

Required posture:

- Reconstruction remains support material, not complete incident analysis.

## Risk-owner decision boundary

Checklist:

- Does the text preserve human risk-owner judgment?
- Does it avoid automating risk acceptance?
- Does it record residual uncertainty?
- Does it distinguish decision support from decision authority?
- Does it avoid replacing management accountability?

Safe wording:

> Risk-owner materials support human decision-making under documented residual uncertainty; they do not automate risk acceptance or replace management judgment.

Unsafe wording:

> The decision matrix decides whether the risk is accepted.

Required posture:

- Risk-owner decision support remains advisory and review-oriented.

## Memory and Retrieval boundary

Checklist:

- Does the text avoid implying full memory/retrieval coverage?
- Does it treat Memory and Retrieval as future work unless separately scoped?
- Does it avoid claiming protection against retrieval poisoning, stale memory, or cross-session contamination?
- Does it preserve the need for separate controls, evidence, examples, and testing?

Safe wording:

> Memory and Retrieval is an important future-work domain and is not fully covered by v1.0.0 unless separately scoped.

Unsafe wording:

> v1.0.0 fully addresses memory and retrieval risks.

Required posture:

- Memory and Retrieval remains future work unless separately scoped.

## Cross-agent delegation boundary

Checklist:

- Does the text avoid claiming full cross-agent governance coverage?
- Does it distinguish narrow existing delegation concepts from broad cross-agent authority management?
- Does it avoid claiming complete downstream authority propagation control?
- Does it preserve future-work boundaries?

Safe wording:

> v1.0.0 may preserve narrow cross-agent authority concepts, but broad cross-agent and cross-domain delegation remains future work unless separately scoped.

Unsafe wording:

> AAEF v1.0.0 fully governs cross-agent systems.

Required posture:

- Advanced cross-agent delegation remains future work or narrow-scope material.

## Approval-quality boundary

Checklist:

- Does the text avoid claiming formal approval-laundering or approval-fatigue testing coverage?
- Does it preserve human approval evidence and accountability concerns?
- Does it avoid saying human approval is sufficient by itself?
- Does it avoid treating approval as authority without context?

Safe wording:

> Approval-quality concerns are important, but formal approval laundering and approval fatigue testing remain future work unless separately scoped.

Unsafe wording:

> Human approval automatically validates the action.

Required posture:

- Approval quality should remain carefully scoped.

## Public communication checklist

Before public release or announcement language is used, verify:

- Does it identify what v1.0.0 means?
- Does it identify what v1.0.0 does not mean?
- Does it avoid certification, compliance, audit, and legal claims?
- Does it avoid production-readiness and implementation-conformance claims?
- Does it avoid empirical validation and peer-review claims?
- Does it avoid external-framework equivalence claims?
- Does it explain that model output is not authority?
- Does it distinguish action authority, execution boundary, evidence, reconstruction, and risk-owner decision support?
- Does it avoid suggesting that AAEF eliminates all AI-agent risk?

## README and entry-point checklist

Before README or entry-point updates, verify:

- Does the entry point distinguish latest completed roadmap from published release status?
- Does it distinguish active baseline from planning artifacts?
- Does it link to current status and baseline reference material?
- Does it avoid stale latest/current wording?
- Does it avoid presenting planning-only artifacts as baseline?
- Does it preserve non-goals?
- Does it avoid overloading readers with every historical artifact?
- Does it provide a usable reading path?

## Release-note checklist

Before v1.0.0 release notes are drafted, verify:

- Does the release note say whether the active baseline changes?
- If the baseline changes, does it identify exactly which artifacts changed?
- If the baseline does not change, does it explain what v1.0.0 stabilizes?
- Does it describe promoted artifacts without overclaiming?
- Does it describe deferred domains?
- Does it preserve non-goals?
- Does it identify validation performed and validation limits?
- Does it avoid certification, compliance, audit, legal, production, implementation, empirical, and equivalence claims?

## Safe wording patterns

| Overbroad wording | Safer wording |
| --- | --- |
| AAEF v1.0.0 certifies AI agents. | AAEF v1.0.0 is planned as a stable public baseline candidate; it is not a certification scheme. |
| AAEF makes systems compliant. | AAEF may support action-authority and evidence review; it does not establish compliance. |
| AAEF evidence is audit sufficient. | AAEF can help organize evidence expectations; audit sufficiency depends on scope, criteria, evidence quality, and reviewer judgment. |
| AAEF proves legal authorization. | AAEF is not legal advice and does not determine legal sufficiency. |
| AAEF is equivalent to external frameworks. | External mappings are contextual and conservative; they do not establish equivalence. |
| Passing validators proves conformance. | Passing validators means scoped repository checks passed; it does not prove implementation conformance. |
| v1.0.0 is production-ready. | v1.0.0 may be usable as a stable public reference; it does not prove production readiness. |
| The decision matrix accepts risk. | The decision matrix supports human risk-owner decisions; it does not automate risk acceptance. |
| Operational reconstruction is complete. | Reconstruction materials support scoped review and preserve evidence gaps and residual uncertainty. |
| Memory and Retrieval is covered. | Memory and Retrieval remains future work unless separately scoped. |

## Relationship to #351 acceptance criteria

This checklist supports #351 by documenting:

- claim boundaries,
- non-goals,
- public communication cautions,
- entry-point wording cautions,
- release-note wording cautions,
- baseline and promotion guardrails,
- future-work guardrails, and
- close-readiness criteria for conservative v1.0.0 planning.

It complements:

- `docs/en/status/v100-baseline-scope-and-promotion-decision.md`
- `docs/en/status/v100-promoted-artifact-candidate-inventory.md`
- `docs/en/status/v100-planning-only-and-future-work-register.md`

## Review questions

Reviewers should be able to answer:

- Does this checklist protect v1.0.0 from overclaiming?
- Does it separate usability from certification, compliance, audit, legal, production, and conformance claims?
- Does it preserve validator, example, reconstruction, and risk-owner decision boundaries?
- Does it preserve future-work boundaries for Memory and Retrieval, cross-agent delegation, approval quality, semantic validators, and production implementation?
- Does it provide safe wording for public and release communication?
- Does it support closing #351 without losing claim-boundary discipline?

## Scope reminder

This artifact is planning and checklist material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, or GitHub Releases.

It does not establish operational readiness, production readiness, implementation conformance, empirical validation, peer-reviewed acceptance, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, or external-framework equivalence.
