# v0.7.0 Research Claim-Boundary Checklist

## Purpose

This document provides a research claim-boundary checklist for the v0.7.0 Research Positioning track.

It builds on:

- `docs/en/status/v070-research-positioning-planning.md`
- `docs/en/status/v070-research-contribution-inventory.md`
- `docs/en/status/v070-research-question-inventory.md`

The purpose is to help reviewers, authors, maintainers, and external-facing contributors avoid overstating what AAEF currently establishes.

This document is planning and positioning material only. It does not claim empirical validation, peer review, implementation conformance, production readiness, certification, compliance, conformity, audit sufficiency, legal sufficiency, or equivalence with external standards or frameworks.

## Why this checklist exists

AAEF is intended to make authority, execution boundaries, and evidence more reviewable for agentic AI systems.

That does not mean every AAEF artifact proves that a system is safe, compliant, auditable, production-ready, legally sufficient, or equivalent to an external framework.

Research-facing materials need explicit claim boundaries so that useful conceptual contributions are not accidentally turned into unsupported assurance claims.

This checklist helps preserve the thesis that model output is not authority while also preserving the distinction between:

- conceptual framing,
- planning support,
- review support,
- implementation guidance,
- evidence modeling,
- future evaluation,
- empirical validation,
- peer review,
- compliance,
- certification,
- audit sufficiency,
- legal sufficiency, and
- external-framework equivalence.

## Intended use

Use this checklist before publishing, merging, or circulating research-facing AAEF material such as:

- research positioning notes,
- contribution inventories,
- research question inventories,
- related-work comparisons,
- paper outlines,
- presentation drafts,
- public communication drafts,
- external-review materials,
- framework mappings,
- evaluation planning artifacts, and
- README or release text that discusses research value.

This checklist may also be used during PR review when a document makes claims about what AAEF contributes, supports, enables, or demonstrates.

## Checklist result categories

A reviewer may classify a claim or artifact as:

| Result | Meaning |
| --- | --- |
| Acceptable | The claim is conservative and supported by the current artifact scope. |
| Needs wording change | The claim may be acceptable after narrower wording. |
| Needs evidence | The claim requires evidence, evaluation, review, or external basis not present in the current artifact. |
| Out of scope | The claim should not be made in the current planning or positioning artifact. |
| Split to future work | The claim may become a future research or validation topic, but should not be asserted now. |

## Checklist 1: Artifact type is clear

Before making a research-facing claim, confirm that the artifact type is clear.

Review questions:

- Is this artifact a planning artifact?
- Is this artifact a positioning artifact?
- Is this artifact a review aid?
- Is this artifact an implementation guide?
- Is this artifact an evaluation design?
- Is this artifact an empirical study?
- Is this artifact a peer-reviewed publication?
- Is this artifact a certification, compliance, conformity, audit, or legal artifact?

Acceptable wording:

- "This artifact provides planning guidance."
- "This document inventories candidate research questions."
- "This document supports research positioning."
- "This artifact does not establish compliance, conformity, certification, audit sufficiency, legal sufficiency, or empirical validation."

Avoid unless separately supported:

- "This validates AAEF."
- "This proves AAEF works."
- "This establishes auditability."
- "This demonstrates compliance."
- "This confirms production readiness."

Required action:

If the artifact type is unclear, narrow the wording before publication or merge.

## Checklist 2: Research contribution claims are framed as candidates unless validated

Research contribution language should distinguish candidate contribution from proven result.

Review questions:

- Is the claim describing what AAEF may contribute?
- Is the claim describing what AAEF has empirically demonstrated?
- Is there evidence for the stronger interpretation?
- Does the claim imply novelty, superiority, replacement, or completeness?
- Does the claim distinguish framework proposal from validated method?

Acceptable wording:

- "AAEF may contribute to research discussion by..."
- "AAEF frames..."
- "AAEF proposes..."
- "AAEF makes the following boundary more reviewable..."
- "This candidate contribution requires future evaluation before stronger claims can be made."

Avoid unless separately supported:

- "AAEF proves..."
- "AAEF solves..."
- "AAEF is the first..."
- "AAEF is superior to..."
- "AAEF establishes a validated method for..."
- "AAEF fully addresses..."

Required action:

If the contribution has not been evaluated, keep the claim in candidate or proposal language.

## Checklist 3: Empirical validation is not implied

Research positioning material must not imply empirical validation unless an artifact explicitly provides it.

Review questions:

- Does the claim say or imply that AAEF has been empirically tested?
- Does the claim imply user study results, benchmark results, field results, or deployed-system validation?
- Does the claim treat repository validators as empirical validation?
- Does the claim treat example artifacts as empirical evidence?
- Does the claim treat planning completeness as proof of effectiveness?

Acceptable wording:

- "Future work may evaluate..."
- "This artifact identifies candidate evaluation questions."
- "Repository validation checks artifact consistency within their defined scope."
- "This does not establish empirical validation."

Avoid unless separately supported:

- "AAEF has been empirically validated."
- "AAEF has been proven effective."
- "AAEF improves outcomes."
- "AAEF reduces risk in production."
- "Validator success demonstrates operational effectiveness."

Required action:

If empirical language appears, either remove it or link it to an explicit future work path.

## Checklist 4: Peer-review status is not overstated

AAEF research positioning should not imply peer review unless peer review has actually occurred.

Review questions:

- Does the artifact imply academic acceptance?
- Does the artifact imply peer-reviewed status?
- Does the artifact cite publication plans as if they were completed?
- Does the artifact use language that suggests external academic validation?
- Does the artifact distinguish research direction from published research?

Acceptable wording:

- "This may support future publication-oriented work."
- "This may support future peer-review preparation."
- "This artifact is not peer-reviewed."
- "This is a research positioning artifact, not a peer-reviewed result."

Avoid unless separately supported:

- "Peer-reviewed framework."
- "Academically validated."
- "Accepted research result."
- "Published method."
- "Proven in the literature."

Required action:

If peer-review status is implied, revise the wording to distinguish future research preparation from completed peer review.

## Checklist 5: External-framework comparisons do not imply equivalence

AAEF may be compared with adjacent frameworks, but comparison must not become equivalence.

Review questions:

- Does the claim compare AAEF with an external framework?
- Does the claim imply that AAEF satisfies, replaces, maps completely to, or certifies against that framework?
- Does a mapping row imply compliance?
- Does the comparison distinguish relationship from equivalence?
- Does the comparison preserve the external framework's own scope and authority?

Acceptable wording:

- "AAEF may be discussed alongside..."
- "AAEF relates to..."
- "This comparison is not an equivalence claim."
- "This mapping is illustrative and does not establish compliance, conformity, certification, or coverage."

Avoid unless separately supported:

- "AAEF is equivalent to..."
- "AAEF satisfies..."
- "AAEF certifies..."
- "AAEF replaces..."
- "AAEF provides complete coverage of..."
- "AAEF ensures compliance with..."

Required action:

If external-framework language appears, add explicit non-equivalence wording or move the stronger claim to future work.

## Checklist 6: Audit and legal claims are not implied

AAEF evidence and review language must not imply audit or legal sufficiency unless separately established.

Review questions:

- Does the claim imply audit opinion, audit sufficiency, or audit readiness?
- Does the claim imply legal sufficiency or legal compliance?
- Does the claim imply admissibility, regulatory acceptance, or legal defensibility?
- Does the claim distinguish review support from audit or legal conclusion?
- Does the artifact avoid using audit language as a substitute for evidence scope?

Acceptable wording:

- "AAEF may support review."
- "AAEF may help structure evidence for a scoped action."
- "This does not establish audit sufficiency."
- "This does not establish legal sufficiency."
- "Legal, regulatory, and audit conclusions require separate review."

Avoid unless separately supported:

- "Audit-ready."
- "Legally sufficient."
- "Regulator-approved."
- "Compliant evidence."
- "Forensic proof."
- "Audit-grade" unless explicitly scoped and already established by the relevant artifact context.

Required action:

If audit or legal language appears, either remove it or narrow it to review support with explicit non-sufficiency wording.

## Checklist 7: Implementation and production claims are not implied

Research positioning does not establish implementation conformance or production readiness.

Review questions:

- Does the claim imply that AAEF has been implemented correctly?
- Does the claim imply that an implementation conforms to AAEF?
- Does the claim imply deployment readiness?
- Does the claim treat prototype references as production systems?
- Does the claim treat example artifacts as deployed-system evidence?
- Does the claim treat validators as runtime correctness checks?

Acceptable wording:

- "This is planning material."
- "This does not establish implementation conformance."
- "This does not establish production readiness."
- "Prototype or example material is illustrative unless explicitly scoped otherwise."
- "Validator success is limited to the validator's defined artifact scope."

Avoid unless separately supported:

- "Production-ready."
- "Implementation-conformant."
- "Runtime-enforced."
- "Deployment-validated."
- "Operationally proven."
- "Validator-passed, therefore compliant."

Required action:

If implementation language appears, distinguish design intent, example material, prototype scope, validator scope, and deployed-system evidence.

## Checklist 8: Safety and security claims are not overstated

AAEF addresses authority and evidence boundaries, but should not claim complete AI safety or security.

Review questions:

- Does the claim imply that AAEF makes an AI system safe?
- Does the claim imply complete security coverage?
- Does the claim imply complete threat mitigation?
- Does the claim distinguish action assurance from model safety?
- Does the claim distinguish control design from operational effectiveness?
- Does the claim avoid promising prevention of all incidents?

Acceptable wording:

- "AAEF focuses on action authority and evidence boundaries."
- "AAEF may help reviewers reason about..."
- "AAEF does not claim complete AI safety or security coverage."
- "Threat coverage and mitigation effectiveness require separate analysis."

Avoid unless separately supported:

- "AAEF makes AI safe."
- "AAEF prevents AI incidents."
- "AAEF fully secures agentic systems."
- "AAEF eliminates unauthorized actions."
- "AAEF guarantees accountability."

Required action:

If safety or security language appears, narrow it to the specific boundary or review function being discussed.

## Checklist 9: Evidence language remains action-bound and scoped

Evidence claims should remain tied to a specific action, decision, and review scope.

Review questions:

- Does the claim identify what action or non-action the evidence supports?
- Does the claim distinguish action-bound evidence from model explanation?
- Does the claim distinguish evidence existence from evidence sufficiency?
- Does the claim identify evidence gaps?
- Does the claim imply complete reconstruction without basis?
- Does the claim imply tamper-proof evidence without basis?

Acceptable wording:

- "Evidence may support reconstruction of a scoped action."
- "Evidence should be correlated to the action request, decision, dispatch outcome, backend response, and review event where applicable."
- "Evidence gaps should be visible."
- "This does not establish complete reconstruction or tamper-proof evidence."

Avoid unless separately supported:

- "The evidence proves everything."
- "The evidence is complete."
- "The evidence is tamper-proof."
- "The evidence is legally sufficient."
- "The evidence establishes audit sufficiency."

Required action:

If evidence language is broad, narrow it to a scoped action and state what the evidence does and does not support.

## Checklist 10: Non-execution claims avoid proving absence too broadly

Non-execution evidence can support review, but should not overclaim absence of all side effects.

Review questions:

- Does the claim distinguish denied, held, not-dispatched, failed, and partially attempted actions?
- Does the claim identify what evidence supports non-execution?
- Does the claim account for possible partial attempts or side effects?
- Does the claim imply absence of all effects?
- Does the claim identify evidence gaps or ambiguity?

Acceptable wording:

- "Evidence may support that the action was denied, held, or not dispatched within the reviewed boundary."
- "This does not prove absence of all side effects."
- "Partial attempts and ambiguous side effects require separate review."
- "Non-execution evidence should be scoped to the relevant control boundary."

Avoid unless separately supported:

- "No action occurred anywhere."
- "There were no side effects."
- "The system was completely safe because execution was denied."
- "Non-execution was fully proven."

Required action:

If non-execution language appears, scope it to the reviewed boundary and avoid universal absence claims.

## Checklist 11: Research questions are not treated as answered results

Research question inventories identify inquiry paths, not completed findings.

Review questions:

- Does the artifact present a research question as already answered?
- Does it distinguish possible future evaluation from current evidence?
- Does it avoid turning "may evaluate" into "has demonstrated"?
- Does it avoid using question lists as proof of maturity?
- Does it preserve uncertainty where appropriate?

Acceptable wording:

- "Candidate research question."
- "Future work may examine..."
- "This question remains open."
- "This artifact does not answer the question empirically."

Avoid unless separately supported:

- "This question has been resolved."
- "AAEF demonstrates..."
- "AAEF proves..."
- "The research confirms..."

Required action:

If a question is written like a conclusion, rewrite it as an inquiry or move it to a future evaluated artifact.

## Checklist 12: Public communication preserves conservative posture

Public-facing materials should remain understandable without overstating the maturity of AAEF.

Review questions:

- Does the material explain AAEF's value without claiming certification or compliance?
- Does the material distinguish framework proposal from adopted standard?
- Does the material avoid implying official recognition unless it exists?
- Does the material avoid implying peer review unless completed?
- Does the material avoid claiming production readiness?
- Does the material include appropriate non-goals or claim boundaries?

Acceptable wording:

- "AAEF is a framework for reasoning about action authority and evidence boundaries."
- "AAEF is not a certification scheme."
- "AAEF does not provide legal, audit, compliance, or conformity conclusions by itself."
- "AAEF's current artifacts support planning, review, and research positioning within their stated scope."

Avoid unless separately supported:

- "AAEF standard."
- "AAEF-certified."
- "AAEF-compliant."
- "Regulator-ready."
- "Peer-reviewed."
- "Production-proven."

Required action:

If public communication uses stronger claims, revise it before publication.

## Checklist 13: Future work is not confused with current scope

Future work can be valuable, but must remain separate from current claims.

Review questions:

- Does the artifact clearly mark future work as future work?
- Does it avoid implying that future artifacts already exist?
- Does it avoid treating future validation as current validation?
- Does it distinguish planned evaluation from completed evaluation?
- Does it preserve current baseline boundaries?

Acceptable wording:

- "Future work may..."
- "A later artifact may..."
- "This would require separate evaluation."
- "This is out of scope for the current planning artifact."

Avoid unless separately supported:

- "AAEF will prove..."
- "AAEF already supports..."
- "This confirms..."
- "This establishes..."

Required action:

If a future work item is written as a current claim, revise it.

## Checklist 14: Baseline impact is explicit

Research positioning material should not accidentally change the active baseline.

Review questions:

- Does the artifact update the active control and assessment baseline?
- Does it update the control catalog?
- Does it update the evidence schema?
- Does it update assessment artifacts?
- Does it update testing procedures?
- Does it add executable validators?
- Does it add executable prototypes, fixtures, or JSON examples?
- If not, does it explicitly say so when needed?

Acceptable wording:

- "This artifact does not update the active control and assessment baseline."
- "This artifact does not update the control catalog, evidence schema, assessment artifacts, or testing procedures."
- "This artifact does not add executable validators, executable prototypes, scenario fixtures, or JSON examples."

Avoid unless intentionally scoped in a separate PR:

- "This updates the baseline."
- "This establishes a new testing requirement."
- "This changes the evidence schema."
- "This creates a conformance expectation."

Required action:

If baseline impact is ambiguous, add an explicit scope reminder.

## Checklist 15: Close-readiness for research positioning

Before closing the v0.7.0 Research Positioning track, reviewers should confirm whether the track has enough artifacts to support the intended milestone scope.

Review questions:

- Is the overall research posture documented?
- Are candidate contribution areas documented?
- Are candidate research questions documented?
- Are research claim boundaries documented?
- Are non-goals and prohibited interpretations clear?
- Are follow-up candidates documented for work that should not block closure?
- Are scope boundaries preserved across the research positioning artifacts?
- Are the relevant status README and document map entries updated?
- Have local and CI validations passed?

Possible close-ready conclusion:

The track may be close-ready if the current artifacts provide enough research positioning structure for v0.7.0 and remaining items can be handled as future follow-up issues.

Possible keep-open conclusion:

The track should remain open if maintainers still want a related-work positioning note, terminology/concept boundary note, paper-outline candidate, or external-review readiness checklist before closing #321.

## Claim examples

### Acceptable conservative examples

- "AAEF proposes a way to separate model output from execution authority."
- "AAEF may help reviewers reason about action-bound evidence."
- "AAEF frames denied and held actions as reviewable outcomes."
- "AAEF's research positioning artifacts identify candidate research questions."
- "This artifact does not establish empirical validation, peer review, certification, compliance, conformity, audit sufficiency, legal sufficiency, implementation conformance, production readiness, or external-framework equivalence."

### Claims that need narrowing

- "AAEF validates agentic AI systems."
- "AAEF proves an AI agent acted correctly."
- "AAEF makes systems auditable."
- "AAEF ensures compliance."
- "AAEF is equivalent to external governance frameworks."
- "AAEF's validators prove conformance."
- "AAEF prevents unsafe actions."
- "AAEF is ready for production use."

### Safer rewrites

| Overbroad wording | Safer wording |
| --- | --- |
| AAEF validates agentic AI systems. | AAEF provides planning and review artifacts for reasoning about action authority and evidence boundaries. |
| AAEF proves an AI agent acted correctly. | AAEF may help reviewers correlate evidence for a scoped action, decision, and execution outcome. |
| AAEF makes systems auditable. | AAEF may support review preparation, but does not establish audit sufficiency. |
| AAEF ensures compliance. | AAEF does not establish compliance, conformity, certification, or legal sufficiency. |
| AAEF is equivalent to an external framework. | AAEF may be compared with external frameworks, but comparison does not establish equivalence. |
| Validator success proves implementation conformance. | Validator success is limited to the validator's defined artifact scope. |
| AAEF prevents unsafe actions. | AAEF focuses on making action authority and enforcement boundaries reviewable. |
| AAEF is production-ready. | This artifact does not establish production readiness or deployed-system validation. |

## Relationship to #321 closure

This checklist is intended to make #321 easier to close when maintainers decide that the Research Positioning track has enough planning structure for v0.7.0.

It does not close #321 by itself.

The checklist may also identify future follow-up candidates that should not necessarily block #321 closure, such as:

- related-work positioning note,
- terminology and concept boundary note,
- paper-outline candidate,
- external-review readiness checklist,
- public research communication guidance, and
- evaluation design planning.

## Review questions

Reviewers should be able to answer:

- Does this checklist preserve the thesis that model output is not authority?
- Does this checklist prevent research positioning from becoming unsupported validation language?
- Does this checklist distinguish candidate contribution from proven result?
- Does this checklist distinguish comparison from equivalence?
- Does this checklist distinguish review support from audit or legal sufficiency?
- Does this checklist distinguish validators from implementation conformance?
- Does this checklist preserve active baseline boundaries?
- Does this checklist support a #321 close-readiness decision without forcing unrelated follow-up work into the current track?

## Scope reminder

This artifact is planning and positioning material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, or JSON examples.

It does not establish empirical validation, peer review, implementation conformance, production readiness, certification, compliance, conformity, audit sufficiency, legal sufficiency, or equivalence with external standards or frameworks.
