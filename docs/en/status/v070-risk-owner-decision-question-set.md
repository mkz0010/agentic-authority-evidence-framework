# v0.7.0 Risk-Owner Decision Question Set

## Purpose

This document provides a decision question set for the v0.7.0 Risk-Owner Decision Support track.

It builds on `docs/en/status/v070-risk-owner-decision-support-planning.md` by turning the initial decision-support planning scope into role-appropriate questions for risk owners and supporting reviewers.

The goal is to help risk owners make scoped decisions about AI-assisted actions, denied actions, held actions, escalations, operational reconstruction results, evidence gaps, residual uncertainty, and follow-up actions.

This document is planning and review material only. It does not automate risk acceptance, replace management judgment, define legal advice, provide audit sufficiency, provide legal sufficiency, establish compliance, define a complete governance process, or claim production readiness.

## Relationship to risk-owner decision support planning

The risk-owner decision support planning artifact defines the initial posture, decision objects, inputs, evidence package expectations, residual uncertainty handling, decision result categories, and relationships to #319 through #322.

This question set makes those concepts easier to apply during review.

The questions are intended to support a human risk owner. They do not make the decision automatically, prove that a decision is correct, or establish that a decision is legally sufficient, audit sufficient, compliant, certified, production-ready, or externally equivalent.

## Intended users

This question set may be used by:

- risk owners,
- reviewers,
- operators,
- maintainers,
- implementers,
- approvers,
- evidence owners,
- backend owners,
- governance reviewers, and
- future decision-support artifact authors.

Different roles may use different subsets of the questions, but the risk owner remains responsible for scoped risk decisions within their authority.

## Decision-support result categories

A risk-owner decision review may result in:

| Result | Meaning |
| --- | --- |
| Accept residual uncertainty | The risk owner accepts documented uncertainty within a defined boundary. |
| Reject residual uncertainty | The risk owner does not accept the uncertainty and requires further action. |
| Request more evidence | Additional evidence is needed before deciding. |
| Defer decision | The decision is delayed pending evidence, owner input, or scope clarification. |
| Escalate decision | The decision is routed to a different owner or separate process. |
| Approve action | The action may proceed within the defined boundary. |
| Deny action | The action should not proceed. |
| Hold action | The action remains paused pending review. |
| Require remediation | A gap, control issue, evidence issue, documentation issue, or implementation issue must be addressed. |
| Open follow-up work | A separate issue, PR, review, investigation, or planning artifact is needed. |

These categories are decision-support aids only. They do not establish legal sufficiency, audit sufficiency, compliance, certification, operational readiness, production readiness, implementation conformance, or external-framework equivalence.

## Question group 1: Decision boundary

### Purpose

Risk owners should first understand the boundary of the decision they are being asked to make.

### Questions

- What decision am I being asked to make?
- What action, non-action, held action, denied action, escalation, backend rejection, or evidence gap is in scope?
- What system, workflow, component, principal, tool, backend, or evidence source is in scope?
- What is explicitly out of scope?
- What time period is being reviewed?
- Which business, safety, operational, security, or governance concern is affected?
- Is this decision within my authority?
- Does this decision require another owner?
- Does this decision require legal, audit, compliance, incident-response, safety, executive, or operational review outside AAEF?
- What conclusion should not be made from this decision?

### Cautions

A risk-owner decision should be scoped to the reviewed boundary.

Accepting uncertainty within one boundary should not be treated as accepting all related risk outside that boundary.

## Question group 2: Decision request

### Purpose

Risk owners should confirm the requested decision before evaluating evidence or uncertainty.

### Questions

- Am I being asked to accept residual uncertainty?
- Am I being asked to reject residual uncertainty?
- Am I being asked to request more evidence?
- Am I being asked to defer the decision?
- Am I being asked to escalate the decision?
- Am I being asked to approve an action?
- Am I being asked to deny an action?
- Am I being asked to hold an action?
- Am I being asked to require remediation?
- Am I being asked to open follow-up work?
- Is the requested decision clearly stated?
- Is the requested decision too broad?
- Can the requested decision be safely narrowed?

### Cautions

The decision request should not be inferred from model output, model explanation, or runtime narrative.

If the requested decision is ambiguous, clarify it before accepting or rejecting uncertainty.

## Question group 3: Evidence package review

### Purpose

Risk owners should determine whether the evidence package is sufficient for the decision being requested.

### Questions

- What evidence supports the current reconstruction?
- What evidence supports the action request?
- What evidence supports principal and authority context?
- What evidence supports the authorization decision?
- What evidence supports dispatch or non-dispatch?
- What evidence supports backend acceptance, rejection, failure, partial execution, or side effects?
- What evidence supports execution or non-execution?
- What evidence supports approval, denial, hold, or escalation?
- Which evidence is independently generated?
- Which evidence is corroborated?
- Which evidence is only model output?
- Which evidence is only runtime self-report?
- Which evidence is missing?
- Which evidence conflicts?
- Which evidence is uncorrelated?
- Which evidence is outside scope?
- Which evidence source is authoritative for the decision?
- Is the evidence package sufficient for this decision, or only for a narrower decision?

### Cautions

Evidence existence does not equal evidence sufficiency.

Evidence sufficiency must be assessed against the specific decision request.

## Question group 4: Operational reconstruction result

### Purpose

Risk owners should understand what the operational reconstruction supports before deciding.

### Questions

- Is the reconstruction result supported?
- Is the reconstruction result partially supported?
- Is the reconstruction result unsupported?
- Is the reconstruction result conflicting?
- Is the reconstruction result out of scope?
- Does the reconstruction require escalation?
- What action or non-action was reconstructed?
- What evidence supports the reconstruction?
- What evidence limits the reconstruction?
- What execution or non-execution outcome is supported?
- Is there possible partial execution, retry, fallback, alternate path, or side effect?
- What conclusion is explicitly not supported?
- Does the reconstruction support the decision being requested, or only a narrower decision?

### Cautions

Operational reconstruction support does not establish legal sufficiency, audit sufficiency, compliance, certification, operational readiness, production readiness, or complete root-cause analysis.

## Question group 5: Residual uncertainty

### Purpose

Risk owners should make residual uncertainty explicit before accepting, rejecting, deferring, or escalating a decision.

### Questions

- What remains unknown?
- Why does it remain unknown?
- What evidence is missing or limited?
- What conclusion is affected by the uncertainty?
- What impact may result from the uncertainty?
- Who owns the uncertainty?
- Can the uncertainty be reduced by collecting more evidence?
- Can the uncertainty be reduced by narrowing the decision boundary?
- Can the uncertainty be accepted within my authority?
- Should the uncertainty be rejected?
- Should the uncertainty be deferred?
- Should the uncertainty be escalated?
- What follow-up action is required?
- What monitoring or review point is needed if uncertainty is accepted?

### Cautions

Residual uncertainty should not be silently accepted.

Accepting uncertainty is not the same as proving that the system is safe, compliant, correct, or production-ready.

## Question group 6: Impact context

### Purpose

Risk owners should connect the decision to business, safety, operational, security, or governance impact.

### Questions

- What impact may have occurred?
- What impact may occur if the action proceeds?
- What impact may occur if the action remains held?
- What impact may occur if the action is denied?
- What impact may occur if the decision is deferred?
- What impact may occur if more evidence is requested?
- What impact may occur if the issue is escalated?
- Is the action high-impact, sensitive, privileged, irreversible, or business-critical?
- Does the decision affect users, customers, assets, regulated processes, production systems, or security boundaries?
- Does residual uncertainty affect safety, security, compliance, operations, reputation, or business continuity?
- Which impact is supported by evidence?
- Which impact is hypothetical?
- Which impact is outside scope?

### Cautions

Impact context should be distinguished from legal, audit, or compliance conclusions.

A business-impact decision does not by itself establish legal sufficiency or audit sufficiency.

## Question group 7: Accept residual uncertainty

### Purpose

Risk owners may accept residual uncertainty only when it is documented, scoped, and within their authority.

### Questions

- What uncertainty am I accepting?
- Is the uncertainty clearly documented?
- Is the acceptance boundary clear?
- Is the acceptance within my authority?
- What evidence supports accepting the uncertainty?
- What evidence is missing?
- What risk treatment accompanies acceptance?
- Is monitoring required?
- Is a later review point required?
- Is remediation required even if uncertainty is accepted?
- What claim should not be made after acceptance?
- Should the decision record state that acceptance does not establish legal sufficiency, audit sufficiency, compliance, certification, operational readiness, or production readiness?

### Cautions

Accepting residual uncertainty does not mean the action was safe, compliant, legally sufficient, audit sufficient, or fully reconstructed.

Acceptance should be scoped, recorded, and reviewable.

## Question group 8: Reject residual uncertainty

### Purpose

Risk owners may reject residual uncertainty when the current evidence is insufficient for the decision.

### Questions

- What uncertainty am I rejecting?
- Why is the uncertainty unacceptable?
- What evidence is missing?
- What evidence conflicts?
- What impact does the uncertainty create?
- Who owns the next step?
- Should the action be denied, held, paused, frozen, retried, rolled back, or escalated?
- Should remediation be required?
- Should a follow-up issue or PR be opened?
- Should the decision be routed to another owner?
- What safer conclusion should be recorded now?

### Cautions

Rejecting uncertainty is not the same as proving that the action was unauthorized, unsafe, non-compliant, or incorrect.

It means the current evidence is not enough for the requested decision.

## Question group 9: Request more evidence

### Purpose

Risk owners may request more evidence when the current package is partial, conflicting, unsupported, or out of scope.

### Questions

- What evidence is needed?
- Why is the evidence needed?
- Which decision depends on the evidence?
- Who can provide the evidence?
- Which component should have produced the evidence?
- Is the evidence recoverable?
- Is the evidence unavailable by design?
- Is the evidence unavailable because of an implementation gap?
- Is the evidence unavailable because of a documentation gap?
- What timeframe or follow-up path applies?
- Should operations remain paused, held, monitored, or constrained while evidence is collected?
- What conclusion should be avoided until the evidence is available?

### Cautions

A request for more evidence should be specific enough to guide action.

Vague requests can leave uncertainty unowned.

## Question group 10: Defer decision

### Purpose

Risk owners may defer a decision when more evidence, owner input, scope clarification, or separate review is needed.

### Questions

- Why is the decision being deferred?
- What evidence, owner input, or scope clarification is needed?
- Who owns the next step?
- What condition will allow the decision to resume?
- Is there an operational hold, pause, monitoring requirement, or escalation while deferred?
- What impact does deferral have?
- What is the next review point?
- What decision remains pending?
- What conclusion should not be made during deferral?

### Cautions

Deferral should not become silent acceptance.

A deferred decision should have an owner, condition, and review point where possible.

## Question group 11: Escalate decision

### Purpose

Risk owners may escalate a decision when it exceeds their authority or requires separate review.

### Questions

- Why does this decision need escalation?
- Who should receive the escalation?
- Is the target a risk owner, operator, approver, executive, legal, audit, compliance, safety, incident-response, or component owner?
- What evidence should be included in the escalation?
- What residual uncertainty should be highlighted?
- What decision remains pending?
- What operational action is needed while escalation is pending?
- What claim should not be made while escalation is pending?
- Should a follow-up issue, PR, review, or investigation be opened?

### Cautions

Escalation routes the unresolved question to another owner or process.

Escalation itself does not establish legal sufficiency, audit sufficiency, compliance, certification, or incident-response sufficiency.

## Question group 12: Approve, deny, or hold action

### Purpose

Risk owners may be asked to approve, deny, or hold a scoped action.

### Questions

- What action is being approved, denied, or held?
- Is the action request clearly identified?
- Is the principal and authority context clear?
- Is required approval evidence available?
- Is execution or non-execution evidence relevant?
- What impact may occur if the action proceeds?
- What impact may occur if the action is denied?
- What impact may occur if the action remains held?
- What evidence gaps affect the decision?
- Is the decision within my authority?
- Should the action be narrowed, constrained, monitored, or escalated?
- What decision record is needed?
- What claim should not be made after the decision?

### Cautions

Approval should not be inferred from execution.

A risk-owner approval is scoped to the reviewed boundary and does not establish legal, audit, compliance, certification, or production-readiness conclusions.

## Question group 13: Require remediation or follow-up work

### Purpose

Risk owners may require remediation or follow-up work when a gap affects decision quality.

### Questions

- What gap or issue requires remediation?
- Is the issue an evidence gap, policy gap, control gap, documentation gap, implementation assumption, validator boundary issue, or ownership issue?
- Which artifact, component, process, or owner is affected?
- Should the follow-up be an issue, PR, design note, checklist, validator clarification, implementation task, or external review?
- What decision is blocked or narrowed until remediation is complete?
- What evidence would demonstrate that the follow-up is complete?
- Who owns follow-up?
- What scope boundary should be preserved?

### Cautions

Opening follow-up work does not mean the original risk is resolved.

Remediation planning should not be treated as operational effectiveness evidence.

## Question group 14: Claim-boundary review

### Purpose

Risk owners and reviewers should avoid overstating what a decision establishes.

### Questions

- Does the decision imply automated risk acceptance?
- Does the decision imply that management judgment was replaced?
- Does the decision imply legal sufficiency?
- Does the decision imply audit sufficiency?
- Does the decision imply compliance, certification, conformity, or external-framework equivalence?
- Does the decision imply operational readiness?
- Does the decision imply production readiness?
- Does the decision imply implementation conformance?
- Does the decision imply complete reconstruction or complete root-cause analysis?
- Does the decision imply that all side effects are absent?
- Does the decision imply that model output was authority?
- What narrower wording should be used?
- What should be documented as residual uncertainty?

### Cautions

A risk-owner decision may be useful and necessary without being a legal, audit, compliance, or certification conclusion.

## Question group 15: Decision record

### Purpose

A risk-owner decision should be recorded clearly enough for later review.

### Questions

- What decision was made?
- Who made the decision?
- When was the decision made?
- What authority did the decision owner have?
- What action, non-action, or gap was in scope?
- What evidence supported the decision?
- What evidence was missing or conflicting?
- What residual uncertainty was accepted, rejected, deferred, or escalated?
- What impact context was considered?
- What follow-up action was required?
- What monitoring or review point was set?
- What claims were explicitly not made?
- Where is the decision record stored?
- Can the decision record be correlated to the reconstruction, evidence package, and follow-up work?

### Cautions

A decision record supports reviewability.

It does not by itself prove that the decision was correct, compliant, legally sufficient, audit sufficient, or production-ready.

## Minimal risk-owner decision prompt

For a lightweight decision review, a risk owner may start with:

1. What decision am I being asked to make?
2. What action, non-action, or evidence gap is in scope?
3. What evidence supports the current reconstruction?
4. What evidence is missing, conflicting, untrusted, uncorrelated, ambiguous, or unowned?
5. What residual uncertainty remains?
6. What impact may result from accepting or rejecting the uncertainty?
7. Is this decision within my authority?
8. Should I accept, reject, request evidence, defer, escalate, approve, deny, hold, require remediation, or open follow-up work?
9. What claim should not be made from this decision?
10. What decision record is needed?

This prompt is a decision-support aid only. It does not automate the decision.

## Relationship to future #323 work

This question set may support narrower follow-up artifacts such as:

- residual uncertainty decision note,
- decision package checklist,
- accept / reject / defer / escalate decision matrix,
- risk-owner handoff checklist,
- high-impact action decision support note,
- claim-boundary checklist for risk-owner materials, and
- #323 close-readiness checklist.

These should remain planning or review artifacts unless a later issue explicitly scopes executable fixtures, examples, validators, or implementation work.

## Review questions

Reviewers should be able to answer:

- Does this question set preserve the thesis that model output is not authority?
- Does this question set distinguish decision support from automated decision-making?
- Does this question set distinguish risk-owner judgment from model output, runtime self-report, or implementation self-report?
- Does this question set preserve evidence gaps and residual uncertainty?
- Does this question set distinguish accepting uncertainty from proving safety, compliance, or correctness?
- Does this question set avoid legal sufficiency, audit sufficiency, compliance, certification, operational readiness, production readiness, implementation conformance, and external-framework equivalence claims?
- Does this question set create useful follow-up paths for #323?

## Scope reminder

This artifact is planning and review material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, or JSON examples.

It does not establish operational readiness, complete reconstruction, complete root-cause analysis, incident-response certification, audit sufficiency, legal sufficiency, empirical validation, implementation conformance, production readiness, certification, compliance, conformity, automated risk acceptance, or external-framework equivalence.
