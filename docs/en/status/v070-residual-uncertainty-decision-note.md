# v0.7.0 Residual Uncertainty Decision Note

## Purpose

This document defines a planning-level residual uncertainty decision note for the v0.7.0 Risk-Owner Decision Support track.

It builds on:

- `docs/en/status/v070-risk-owner-decision-support-planning.md`
- `docs/en/status/v070-risk-owner-decision-question-set.md`
- `docs/en/status/v070-operational-reconstruction-handoff-note.md`
- `docs/en/status/v070-evidence-gap-classification-note.md`

The goal is to help risk owners and supporting reviewers describe, classify, and decide what to do with residual uncertainty after operational reconstruction, evidence gap classification, and decision-support review.

This document is planning and review material only. It does not automate risk acceptance, replace management judgment, define legal advice, provide audit sufficiency, provide legal sufficiency, establish compliance, define a complete governance process, or claim production readiness.

## Relationship to Risk-Owner Decision Support

Risk-Owner Decision Support asks what decision should be made given the evidence, gaps, uncertainty, impact, and owner authority.

Residual uncertainty is the uncertainty that remains after available evidence has been reviewed, reconstruction has been scoped, evidence gaps have been identified, and unsupported conclusions have been excluded.

This note focuses on how that remaining uncertainty should be described and routed to a decision.

## Definition

Residual uncertainty is uncertainty that remains after review.

It may arise from:

- missing evidence,
- conflicting evidence,
- untrusted self-report,
- uncorrelated evidence,
- scope ambiguity,
- ownership ambiguity,
- incomplete reconstruction,
- possible side effects,
- incomplete impact analysis,
- unresolved authority context,
- unresolved approval context, or
- a decision request that exceeds the reviewed boundary.

Residual uncertainty is not the same as failure.

Residual uncertainty is also not the same as accepted risk until a risk owner explicitly accepts it within a defined boundary.

## Decision-support posture

Residual uncertainty should be made explicit.

A decision-support artifact should not:

- hide residual uncertainty,
- convert residual uncertainty into a supported conclusion,
- treat risk-owner acceptance as legal sufficiency,
- treat risk-owner acceptance as audit sufficiency,
- treat risk-owner acceptance as compliance,
- treat risk-owner acceptance as certification,
- treat risk-owner acceptance as production readiness,
- treat risk-owner acceptance as implementation conformance,
- treat model output as authority for acceptance, or
- treat runtime self-report as sufficient evidence for acceptance.

Risk owners may accept, reject, request evidence, defer, escalate, require remediation, or open follow-up work.

## Residual uncertainty classification summary

| Classification | Description | Typical decision path |
| --- | --- | --- |
| Evidence-missing uncertainty | Needed evidence is absent or incomplete. | Request evidence, defer, or reject uncertainty. |
| Evidence-conflict uncertainty | Evidence sources support incompatible conclusions. | Escalate, request clarification, or narrow conclusion. |
| Evidence-quality uncertainty | Evidence relies on model output, runtime self-report, or weak source quality. | Request corroboration or narrow conclusion. |
| Correlation uncertainty | Evidence exists but is not tied to the scoped action. | Request correlation evidence or narrow conclusion. |
| Scope uncertainty | The reviewed boundary is unclear or too broad. | Narrow scope, defer, or escalate. |
| Ownership uncertainty | The owner of the gap or decision is unclear. | Assign owner or escalate. |
| Authority uncertainty | Principal, delegation, authority source, or approval state is unresolved. | Request evidence, hold, or escalate. |
| Execution uncertainty | Execution, non-execution, partial execution, or side effects remain unclear. | Request evidence, hold, or operational escalation. |
| Impact uncertainty | Business, safety, security, or governance impact is unclear. | Risk-owner review, impact analysis, or escalation. |
| Claim-boundary uncertainty | The proposed conclusion may overstate what evidence supports. | Narrow wording or mark unsupported. |

## Decision result categories

Residual uncertainty may lead to one or more decision results.

| Decision result | Meaning |
| --- | --- |
| Accept uncertainty | The risk owner accepts the documented uncertainty within a defined boundary. |
| Reject uncertainty | The risk owner does not accept the uncertainty and requires further action. |
| Request evidence | Additional evidence is required before deciding. |
| Defer decision | The decision is delayed pending evidence, owner input, or scope clarification. |
| Escalate decision | The decision is routed to another owner or separate process. |
| Require remediation | A gap, control issue, documentation issue, or implementation issue must be addressed. |
| Open follow-up work | A separate issue, PR, review, investigation, or planning artifact is needed. |
| Narrow conclusion | A weaker or narrower conclusion is recorded instead of the proposed claim. |
| Mark unsupported | The proposed conclusion is not supported by available evidence. |

These categories do not establish legal sufficiency, audit sufficiency, compliance, certification, operational readiness, production readiness, implementation conformance, or external-framework equivalence.

## Accepting residual uncertainty

### When acceptance may be appropriate

A risk owner may accept residual uncertainty when:

- the uncertainty is clearly documented,
- the reviewed boundary is clear,
- the decision is within the risk owner's authority,
- the available evidence supports at least a scoped conclusion,
- unsupported claims are excluded,
- potential impact is understood enough for the decision,
- follow-up obligations are recorded, and
- a review point or monitoring expectation is defined where appropriate.

### Questions before acceptance

A risk owner should ask:

- What uncertainty is being accepted?
- What boundary does the acceptance apply to?
- What evidence supports the current conclusion?
- What evidence is missing or limited?
- What impact may remain?
- Is acceptance within my authority?
- Does acceptance require monitoring, remediation, or later review?
- What claims should not be made after acceptance?
- Where will the acceptance decision be recorded?
- Can the decision be correlated to the reconstruction and evidence package?

### Required caution

Acceptance of residual uncertainty does not prove that the action was safe, compliant, legally sufficient, audit sufficient, production-ready, or fully reconstructed.

Acceptance should be recorded as a scoped risk-owner decision, not as a universal assurance conclusion.

## Rejecting residual uncertainty

### When rejection may be appropriate

A risk owner may reject residual uncertainty when:

- the uncertainty affects a high-impact action,
- key evidence is missing,
- evidence conflicts,
- authority or approval is unresolved,
- execution or non-execution is unclear,
- possible side effects remain material,
- impact cannot be sufficiently understood,
- the requested decision exceeds the reviewed boundary, or
- acceptance is outside the risk owner's authority.

### Questions before rejection

A risk owner should ask:

- What uncertainty is unacceptable?
- Why is it unacceptable?
- What decision is blocked?
- What evidence is needed?
- Who owns the next step?
- Should the action be held, denied, paused, frozen, retried, rolled back, or escalated?
- Should remediation or follow-up work be opened?
- What safer conclusion can be recorded now?

### Required caution

Rejecting uncertainty does not prove that the action was unsafe, unauthorized, non-compliant, or incorrect.

It means the current evidence and uncertainty state are not acceptable for the requested decision.

## Requesting more evidence

### When evidence should be requested

A risk owner may request more evidence when:

- the current evidence package is incomplete,
- the reconstruction is partial,
- evidence conflicts,
- evidence is only model output or runtime self-report,
- evidence is not correlated to the action,
- approval evidence is missing,
- backend evidence is missing,
- execution or non-execution evidence is unclear, or
- impact cannot be assessed from current evidence.

### Questions for an evidence request

The request should answer:

- What evidence is needed?
- Which decision depends on it?
- Why does it matter?
- Who can provide it?
- Which component should have produced it?
- Is the evidence recoverable?
- Is the evidence unavailable by design?
- Is the evidence missing because of an implementation, process, or documentation gap?
- What should happen while evidence is collected?
- What conclusion should be avoided until the evidence is available?

### Required caution

A request for more evidence should be specific.

Vague evidence requests can leave uncertainty unowned and make the decision difficult to resume.

## Deferring a decision

### When deferral may be appropriate

A risk owner may defer a decision when:

- more evidence is expected,
- another owner must provide input,
- the reviewed boundary must be narrowed,
- impact analysis is incomplete,
- separate legal, audit, compliance, safety, incident-response, or operational review may be needed, or
- the risk owner cannot decide within the current information state.

### Questions for deferral

A deferral should record:

- why the decision is deferred,
- what uncertainty remains,
- what evidence or owner input is needed,
- who owns the next step,
- what condition will resume the decision,
- whether the action remains held, paused, monitored, or constrained,
- when the decision should be reviewed again, and
- what conclusion should not be made during deferral.

### Required caution

Deferral should not become silent acceptance.

A deferred decision should have an owner, condition, and review point where possible.

## Escalating a decision

### When escalation may be appropriate

A risk owner may escalate residual uncertainty when:

- the decision exceeds the risk owner's authority,
- impact may be high,
- authority or approval is disputed,
- evidence conflicts across components,
- legal, audit, compliance, safety, incident-response, or executive review may be needed,
- side effects may extend outside the reviewed boundary,
- ownership is ambiguous, or
- the decision cannot be narrowed safely.

### Questions for escalation

An escalation should answer:

- Why is escalation needed?
- Who should receive the escalation?
- What evidence supports the current state?
- What uncertainty remains?
- What decision is pending?
- What operational action is needed while escalation is pending?
- What claim should not be made while escalation is pending?
- Should a follow-up issue, PR, review, investigation, or external process be opened?

### Required caution

Escalation routes the unresolved decision to another owner or process.

Escalation itself does not establish legal, audit, compliance, certification, or incident-response sufficiency.

## Requiring remediation

### When remediation may be appropriate

A risk owner may require remediation when residual uncertainty reveals:

- missing evidence production,
- unclear authority handling,
- incomplete approval capture,
- insufficient dispatch enforcement evidence,
- incomplete backend evidence,
- unclear ownership,
- ambiguous documentation,
- weak correlation between events,
- an implementation assumption gap,
- a validator boundary gap, or
- a process handoff gap.

### Questions for remediation

A remediation decision should answer:

- What issue requires remediation?
- Is the issue evidence-related, control-related, documentation-related, implementation-related, ownership-related, or process-related?
- Which artifact, component, workflow, or owner is affected?
- What decision remains blocked or narrowed?
- What evidence would show that remediation is complete?
- Should remediation be tracked as an issue, PR, design note, checklist, implementation task, or external review?
- What claim should not be made until remediation is complete?

### Required caution

Remediation planning does not prove remediation effectiveness.

A future artifact or review may be needed to assess whether remediation was completed.

## Opening follow-up work

### When follow-up work may be appropriate

Residual uncertainty may be split into follow-up work when it should not block the current planning track but should remain visible.

Follow-up work may include:

- evidence package checklist,
- risk-owner handoff checklist,
- high-impact action decision support note,
- accept / reject / defer / escalate decision matrix,
- implementation assumption review,
- validator boundary clarification,
- documentation update,
- reconstruction walkthrough candidate,
- operational reviewer guidance, or
- separate legal, audit, compliance, safety, incident-response, or governance review.

### Questions for follow-up

A follow-up item should answer:

- What uncertainty or gap is being split out?
- Why is it not resolved in the current decision?
- Who owns the follow-up?
- What artifact or process should address it?
- What scope boundary should be preserved?
- What decision or claim remains limited until follow-up is complete?

## Decision record expectations

A residual uncertainty decision record should include:

- decision request,
- decision owner,
- decision date or review point,
- scoped action or non-action,
- reviewed boundary,
- evidence summary,
- evidence gaps,
- residual uncertainty statement,
- impact context,
- decision result,
- rationale,
- follow-up action,
- claims explicitly not made, and
- links or identifiers connecting the decision to reconstruction and evidence materials.

A decision record supports reviewability.

It does not by itself prove that the decision was correct, compliant, legally sufficient, audit sufficient, production-ready, or externally equivalent.

## Minimal residual uncertainty decision prompt

For a lightweight decision review, use:

1. What uncertainty remains?
2. What evidence supports the current conclusion?
3. What evidence is missing, conflicting, untrusted, uncorrelated, ambiguous, or unowned?
4. What conclusion is affected?
5. What impact may result?
6. Who owns the uncertainty?
7. Is the uncertainty within the risk owner's authority to accept?
8. Should the uncertainty be accepted, rejected, evidence-requested, deferred, escalated, remediated, or split to follow-up?
9. What claim should not be made?
10. What decision record is needed?

This prompt is a decision-support aid only. It does not automate the decision.

## Safe wording patterns

| Overbroad wording | Safer wording |
| --- | --- |
| The risk owner approved the system. | The risk owner accepted the documented residual uncertainty for the scoped decision. |
| The uncertainty was resolved. | The uncertainty was accepted, rejected, deferred, escalated, or assigned for follow-up. |
| The decision proves the action was safe. | The decision records a risk-owner judgment based on available evidence and residual uncertainty. |
| The decision establishes compliance. | The decision does not establish compliance, certification, audit sufficiency, or legal sufficiency. |
| The model said the risk is acceptable. | Risk acceptance must be made by an authorized risk owner, not by model output. |
| The gap can be ignored. | The gap should be documented, assigned, accepted, rejected, deferred, escalated, or split to follow-up. |

## Relationship to future #323 work

This note may support narrower follow-up artifacts such as:

- decision package checklist,
- accept / reject / defer / escalate decision matrix,
- risk-owner handoff checklist,
- high-impact action decision support note,
- claim-boundary checklist for risk-owner materials, and
- #323 close-readiness checklist.

These should remain planning or review artifacts unless a later issue explicitly scopes executable fixtures, examples, validators, or implementation work.

## Review questions

Reviewers should be able to answer:

- Does this note preserve the thesis that model output is not authority?
- Does this note distinguish residual uncertainty from accepted risk?
- Does this note distinguish decision support from automated decision-making?
- Does this note distinguish risk-owner judgment from model output, runtime self-report, or implementation self-report?
- Does this note preserve evidence gaps and residual uncertainty instead of hiding them?
- Does this note distinguish accepting uncertainty from proving safety, compliance, or correctness?
- Does this note avoid legal sufficiency, audit sufficiency, compliance, certification, operational readiness, production readiness, implementation conformance, and external-framework equivalence claims?
- Does this note create useful follow-up paths for #323?

## Scope reminder

This artifact is planning and review material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, or JSON examples.

It does not establish operational readiness, complete reconstruction, complete root-cause analysis, incident-response certification, audit sufficiency, legal sufficiency, empirical validation, implementation conformance, production readiness, certification, compliance, conformity, automated risk acceptance, or external-framework equivalence.
