# v0.7.0 Risk-Owner Decision Matrix

## Purpose

This document provides a planning-level accept / reject / defer / escalate decision matrix for the v0.7.0 Risk-Owner Decision Support track.

It builds on:

- `docs/en/status/v070-risk-owner-decision-support-planning.md`
- `docs/en/status/v070-risk-owner-decision-question-set.md`
- `docs/en/status/v070-residual-uncertainty-decision-note.md`
- `docs/en/status/v070-risk-owner-decision-package-checklist.md`
- `docs/en/status/v070-operational-reconstruction-handoff-note.md`
- `docs/en/status/v070-evidence-gap-classification-note.md`

The goal is to help risk owners and supporting reviewers choose a conservative decision path when a scoped action, non-action, reconstruction result, evidence gap, or residual uncertainty requires a decision.

This document is planning and review material only. It does not automate risk acceptance, replace management judgment, define legal advice, provide audit sufficiency, provide legal sufficiency, establish compliance, define a complete governance process, or claim production readiness.

## Decision matrix posture

The matrix is intended to support human decision-making, not replace it.

A risk owner remains responsible for deciding within their authority.

The matrix should help reviewers preserve:

- the scoped decision boundary,
- the evidence supporting the decision,
- the evidence gaps limiting the decision,
- residual uncertainty,
- impact context,
- owner accountability,
- follow-up requirements, and
- claim boundaries.

The matrix should not convert an evidence gap into a supported conclusion.

The matrix should not imply that a decision establishes legal sufficiency, audit sufficiency, compliance, certification, conformity, operational readiness, production readiness, implementation conformance, automated risk acceptance, or external-framework equivalence.

## Intended users

This matrix may be used by:

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

The matrix is a review aid only. It does not define a complete organizational governance process.

## Decision result categories

This matrix focuses on five primary decision results.

| Decision result | Meaning |
| --- | --- |
| Accept | The risk owner accepts documented residual uncertainty within a defined boundary. |
| Reject | The risk owner does not accept the uncertainty or decision request and requires further action. |
| Request evidence | The risk owner requires additional evidence before deciding. |
| Defer | The risk owner delays the decision pending evidence, owner input, scope clarification, or separate review. |
| Escalate | The risk owner routes the decision to another owner or separate process. |

Related outcomes such as approve, deny, hold, require remediation, narrow conclusion, or open follow-up work may be attached to one of these decision results.

## Primary decision matrix

| Condition | Prefer this decision path | Why |
| --- | --- | --- |
| Evidence supports the scoped conclusion, gaps are documented, impact is understood enough, and the decision is within the risk owner's authority. | Accept | The residual uncertainty can be accepted within a defined boundary. |
| Evidence is insufficient for the requested decision, the uncertainty is unacceptable, or acceptance is outside the risk owner's authority. | Reject | The requested decision should not be made from the current package. |
| Specific evidence is missing but plausibly obtainable and material to the decision. | Request evidence | The decision may become clearer after targeted evidence collection. |
| The decision cannot be made now because evidence, owner input, scope clarification, or impact analysis is pending. | Defer | The decision should remain open with an owner, condition, and review point. |
| The issue exceeds the risk owner's authority, has high-impact uncertainty, or may require legal, audit, compliance, incident-response, safety, executive, or external review. | Escalate | The decision should move to a different owner or process. |

## Evidence state matrix

| Evidence state | Accept | Reject | Request evidence | Defer | Escalate |
| --- | --- | --- | --- | --- | --- |
| Evidence supports the scoped conclusion and gaps are non-blocking. | Possible if impact and authority are clear. | Usually not needed. | Optional for future improvement. | Optional if timing requires later review. | Usually not needed. |
| Evidence supports only a narrower conclusion. | Possible only for the narrower boundary. | Possible for the broader request. | Possible if broader decision requires more evidence. | Possible if broader decision may resume later. | Possible if broader request exceeds authority. |
| Evidence is missing but recoverable. | Avoid unless the missing evidence is non-blocking. | Possible if the gap is unacceptable. | Preferred when evidence is material and obtainable. | Possible while evidence is collected. | Possible if the gap affects high-impact or external review. |
| Evidence conflicts. | Avoid unless conflict is resolved or narrowed. | Possible if conflict blocks the request. | Possible if clarification is available. | Possible while conflict is investigated. | Preferred if conflict affects high-impact, authority, or side effects. |
| Evidence is only model output or runtime self-report. | Avoid for material decisions. | Possible if no corroboration can be provided. | Preferred when corroboration is needed. | Possible while corroboration is sought. | Possible if unsupported reliance would be high-impact. |
| Evidence is uncorrelated to the scoped action. | Avoid unless decision is narrowed. | Possible for the requested decision. | Preferred when correlation evidence is needed. | Possible while correlation is investigated. | Possible if correlation gap affects high-impact action. |
| Evidence is outside the reviewed boundary. | Avoid for the current boundary. | Possible for the requested decision. | Possible if in-scope evidence can be gathered. | Possible while boundary is clarified. | Possible if boundary ownership is unclear. |

## Residual uncertainty matrix

| Residual uncertainty type | Accept | Reject | Request evidence | Defer | Escalate |
| --- | --- | --- | --- | --- | --- |
| Low residual uncertainty, documented, scoped, and owned. | Possible. | Usually not needed. | Optional. | Optional. | Usually not needed. |
| Evidence-missing uncertainty. | Possible only if non-blocking and accepted within authority. | Possible if material. | Preferred if evidence is obtainable. | Possible while evidence is collected. | Possible if evidence affects high-impact or external process. |
| Evidence-conflict uncertainty. | Avoid unless conflict is resolved or decision is narrowed. | Possible if conflict blocks decision. | Possible if clarification is available. | Possible while conflict is reviewed. | Preferred when conflict is material or high-impact. |
| Authority uncertainty. | Avoid unless narrowed and within authority. | Possible if authority evidence is insufficient. | Preferred if authority evidence can be obtained. | Possible while authority is clarified. | Preferred if authority is disputed or outside owner authority. |
| Execution uncertainty. | Avoid unless impact is low and boundary is clear. | Possible if unacceptable. | Preferred if execution evidence is obtainable. | Possible while operational review proceeds. | Preferred if side effects may be material. |
| Impact uncertainty. | Avoid unless impact is bounded and accepted. | Possible if impact cannot be accepted. | Possible if impact evidence is available. | Preferred while impact analysis is pending. | Preferred if impact may be high or external. |
| Ownership uncertainty. | Avoid until owner is assigned. | Possible for requested decision. | Possible if owner can provide evidence. | Possible while ownership is clarified. | Preferred if no owner can be assigned locally. |
| Scope uncertainty. | Avoid unless scope is narrowed. | Possible for overbroad request. | Possible if boundary evidence is needed. | Preferred while scope is clarified. | Possible if scope crosses ownership boundaries. |

## Impact and authority matrix

| Impact / authority condition | Preferred decision path |
| --- | --- |
| Low impact, evidence-supported, within authority, gaps documented. | Accept or narrow conclusion. |
| High impact, evidence-supported, within authority, monitoring or follow-up required. | Accept with explicit boundary, review point, and follow-up. |
| High impact, material evidence missing. | Request evidence, defer, or escalate. |
| High impact, authority or approval unclear. | Request evidence, hold, or escalate. |
| Possible side effects outside reviewed boundary. | Defer or escalate; avoid broad acceptance. |
| Decision exceeds risk owner's authority. | Escalate. |
| Decision requires legal, audit, compliance, safety, incident-response, or executive process. | Escalate. |
| Decision request is too broad for the evidence. | Reject broader request, narrow conclusion, request evidence, or defer. |
| Decision request is ambiguous. | Defer until clarified or reject if clarity cannot be obtained. |

## Accept path

### Use when

Use the accept path when:

- the decision request is clear,
- the reviewed boundary is clear,
- evidence supports the scoped conclusion,
- residual uncertainty is documented,
- material gaps are non-blocking or accepted,
- impact is understood enough for the decision,
- ownership is clear,
- the decision is within the risk owner's authority, and
- follow-up or monitoring is recorded where needed.

### Required decision record

An accept decision should record:

- accepted uncertainty,
- acceptance boundary,
- evidence summary,
- evidence gaps,
- residual uncertainty,
- impact context,
- owner authority,
- follow-up action,
- monitoring or review point where applicable, and
- claims explicitly not made.

### Claims to avoid

An accept decision should not claim:

- legal sufficiency,
- audit sufficiency,
- compliance,
- certification,
- conformity,
- operational readiness,
- production readiness,
- implementation conformance,
- complete reconstruction,
- complete root-cause analysis,
- absence of all side effects, or
- model output as authority.

## Reject path

### Use when

Use the reject path when:

- evidence does not support the requested decision,
- residual uncertainty is unacceptable,
- material gaps block the decision,
- the decision request is too broad,
- the decision exceeds the risk owner's authority,
- possible impact cannot be accepted,
- authority or approval is unresolved, or
- the request would require unsupported claims.

### Required decision record

A reject decision should record:

- rejected uncertainty or decision request,
- reason for rejection,
- evidence gaps,
- impact concern,
- owner of next step,
- requested remediation or evidence,
- whether the action should remain denied, held, paused, frozen, or escalated, and
- safer conclusion currently supported.

### Claims to avoid

A reject decision should not claim that the action was unsafe, unauthorized, illegal, non-compliant, or incorrect unless separately supported.

Rejecting uncertainty means the current package is not sufficient for the requested decision.

## Request-evidence path

### Use when

Use the request-evidence path when:

- specific evidence is missing,
- the missing evidence is material to the decision,
- the evidence is plausibly obtainable,
- the evidence owner can be identified,
- the decision could change after evidence is collected, and
- the action can remain held, paused, monitored, or otherwise constrained while evidence is collected if needed.

### Required decision record

A request-evidence decision should record:

- evidence requested,
- why the evidence matters,
- which decision depends on it,
- evidence owner,
- expected source or component,
- whether evidence is recoverable,
- operational state while evidence is collected,
- review point, and
- conclusions to avoid until evidence is available.

### Claims to avoid

A request for evidence should not be treated as acceptance, rejection, or proof of failure.

It means the current package is incomplete for the requested decision.

## Defer path

### Use when

Use the defer path when:

- more evidence is expected,
- another owner must provide input,
- scope must be clarified,
- impact analysis is pending,
- separate review may be needed,
- the decision is time-dependent,
- the action should remain held or monitored, or
- the risk owner cannot make the decision from the current package but does not reject it outright.

### Required decision record

A defer decision should record:

- reason for deferral,
- unresolved uncertainty,
- owner of next step,
- condition for resuming the decision,
- review point,
- operational state during deferral,
- pending decision, and
- conclusions to avoid during deferral.

### Claims to avoid

Deferral should not become silent acceptance.

A deferred decision remains unresolved until the condition for review is met or the decision is revisited.

## Escalate path

### Use when

Use the escalate path when:

- the decision exceeds the risk owner's authority,
- impact may be high,
- authority or approval is disputed,
- evidence conflicts across components,
- side effects may extend outside the reviewed boundary,
- ownership cannot be assigned,
- legal, audit, compliance, incident-response, safety, executive, or external review may be needed, or
- the decision cannot be safely narrowed.

### Required decision record

An escalation should record:

- reason for escalation,
- escalation target,
- current evidence,
- residual uncertainty,
- pending decision,
- operational action while escalation is pending,
- follow-up owner,
- claims to avoid, and
- links to the decision package and reconstruction materials.

### Claims to avoid

Escalation does not establish legal sufficiency, audit sufficiency, compliance, certification, incident-response sufficiency, operational readiness, production readiness, or external-framework equivalence.

It routes the decision to another owner or process.

## Related action outcomes

The decision matrix can be combined with action outcomes.

| Action outcome | Matrix use |
| --- | --- |
| Approve action | Usually requires an accept path for scoped uncertainty and evidence sufficient for approval. |
| Deny action | May follow reject, defer, or escalate depending on whether denial is final, temporary, or externally required. |
| Hold action | Often pairs with request-evidence, defer, or escalate. |
| Require remediation | Often follows reject, request-evidence, defer, or accept-with-follow-up. |
| Open follow-up work | May attach to any path when a gap should remain visible. |
| Narrow conclusion | May attach to accept, reject, request-evidence, or defer when the original request is too broad. |

These outcomes should be recorded separately from the matrix path where useful.

## Anti-patterns

Avoid these decision patterns:

- accepting uncertainty without recording the boundary,
- rejecting uncertainty while implying unsupported wrongdoing,
- deferring without owner, condition, or review point,
- escalating without a target owner or process,
- requesting vague evidence without an evidence owner,
- accepting model output as risk-owner authority,
- treating runtime self-report as sufficient evidence,
- treating risk-owner acceptance as legal or audit sufficiency,
- treating a decision package as compliance proof,
- treating operational reconstruction as complete root-cause analysis,
- treating backend rejection as proof of no side effects,
- treating non-dispatch as proof of absence of all side effects, and
- closing follow-up work while material gaps remain unowned.

## Minimal decision matrix prompt

For lightweight use, ask:

1. What decision is requested?
2. What evidence supports the requested decision?
3. What evidence is missing, conflicting, untrusted, uncorrelated, ambiguous, or unowned?
4. What residual uncertainty remains?
5. What impact may result?
6. Is the decision within the risk owner's authority?
7. Is the uncertainty acceptable within the reviewed boundary?
8. Should the decision path be accept, reject, request evidence, defer, or escalate?
9. What owner, next action, review point, or follow-up is required?
10. What claims should not be made from this decision?

This prompt is a decision-support aid only and does not automate the decision.

## Safe wording patterns

| Overbroad wording | Safer wording |
| --- | --- |
| The risk was accepted, so the system is safe. | The risk owner accepted documented residual uncertainty for a scoped decision. |
| The decision matrix says approve. | The matrix supports a human risk-owner decision path; it does not make the decision automatically. |
| The risk owner rejected the decision, so the action was wrong. | The risk owner rejected the current decision request because the available package was insufficient or unacceptable. |
| The decision is deferred, so it is accepted for now. | The decision is deferred and remains unresolved until the recorded condition or review point. |
| The issue was escalated, so AAEF has resolved it. | The issue was escalated to another owner or process; the unresolved decision remains tracked. |
| Evidence was requested, so the package failed. | Additional evidence was requested because the current package was incomplete for the requested decision. |

## Relationship to future #323 work

This matrix may support narrower follow-up artifacts such as:

- risk-owner handoff checklist,
- high-impact action decision support note,
- claim-boundary checklist for risk-owner materials, and
- #323 close-readiness checklist.

These should remain planning or review artifacts unless a later issue explicitly scopes executable fixtures, examples, validators, or implementation work.

## Review questions

Reviewers should be able to answer:

- Does this matrix preserve the thesis that model output is not authority?
- Does this matrix distinguish decision support from automated decision-making?
- Does this matrix distinguish risk-owner judgment from model output, runtime self-report, or implementation self-report?
- Does this matrix preserve evidence gaps and residual uncertainty instead of hiding them?
- Does this matrix distinguish acceptance from legal, audit, compliance, certification, operational, or production conclusions?
- Does this matrix give conservative paths for accept, reject, request evidence, defer, and escalate decisions?
- Does this matrix preserve owner, next-action, review-point, and claim-boundary expectations?
- Does this matrix create useful follow-up paths for #323 closure?

## Scope reminder

This artifact is planning and review material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, or JSON examples.

It does not establish operational readiness, complete reconstruction, complete root-cause analysis, incident-response certification, audit sufficiency, legal sufficiency, empirical validation, implementation conformance, production readiness, certification, compliance, conformity, automated risk acceptance, or external-framework equivalence.
