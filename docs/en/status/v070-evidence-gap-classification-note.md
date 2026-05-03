# v0.7.0 Evidence Gap Classification Note

## Purpose

This document defines a planning-level evidence gap classification note for the v0.7.0 Operational Reconstruction track.

It builds on:

- `docs/en/status/v070-operational-reconstruction-planning.md`
- `docs/en/status/v070-operational-reconstruction-question-set.md`

The goal is to help reviewers classify missing, incomplete, conflicting, ambiguous, or unsupported evidence during operational reconstruction.

This document is planning and review material only. It does not update the evidence schema, define a forensic method, define an audit procedure, define an incident-response procedure, or establish audit sufficiency, legal sufficiency, operational readiness, complete reconstruction, complete root-cause analysis, certification, compliance, conformity, implementation conformance, production readiness, empirical validation, or external-framework equivalence.

## Relationship to operational reconstruction

Operational reconstruction asks what happened, who or what acted, what authority was used, what decision was made, what execution or non-execution occurred, and what evidence supports the conclusion.

Evidence gap classification helps reviewers avoid hiding uncertainty.

A gap classification should answer:

- what evidence is missing or limited,
- which reconstruction question is affected,
- which conclusion is blocked, weakened, or out of scope,
- which role or component may own the gap, and
- whether the gap should be accepted, documented, investigated, escalated, or split into follow-up work.

Classifying a gap does not resolve the gap.

## Intended users

This note may be used by:

- reviewers,
- operators,
- risk owners,
- maintainers,
- implementers,
- evidence reviewers,
- approvers,
- incident coordinators, and
- future operational reconstruction scenario authors.

Different roles may use different parts of the classification.

## Classification result categories

A classified evidence gap may lead to one of the following review outcomes.

| Result | Meaning |
| --- | --- |
| Record as limitation | The gap is documented and the conclusion is narrowed accordingly. |
| Request evidence | Additional evidence should be collected before reaching a conclusion. |
| Escalate to owner | A component owner, operator, approver, risk owner, or maintainer must resolve or accept the gap. |
| Mark conclusion unsupported | The proposed conclusion is not supported by available evidence. |
| Mark conclusion partial | The conclusion is partially supported but limited by the gap. |
| Mark out of scope | The gap cannot be resolved inside the reviewed boundary. |
| Split to follow-up | The gap requires a separate issue, PR, investigation, or review activity. |

These categories are review aids only. They do not establish audit sufficiency, legal sufficiency, operational readiness, incident-response certification, or complete root-cause analysis.

## Gap classification summary

| Gap class | Reconstruction area affected | Typical impact |
| --- | --- | --- |
| Missing request evidence | Action request | The action under review may not be identifiable or correlatable. |
| Missing principal evidence | Principal and authority context | Who acted or on whose behalf may be unclear. |
| Missing authority evidence | Authority chain | Authority source, scope, freshness, or delegation may be unsupported. |
| Missing decision evidence | Authorization decision | Allow, deny, hold, escalation, or non-dispatch decision may be unsupported. |
| Missing enforcement evidence | Dispatch enforcement | Whether the action was dispatched, blocked, held, or escalated may be unclear. |
| Missing backend evidence | Backend acceptance and result | Whether the backend accepted, rejected, failed, or executed may be unsupported. |
| Missing execution evidence | Execution outcome | Execution, partial execution, or failure may be unsupported. |
| Missing non-execution evidence | Denied, held, blocked, or not-dispatched action | Non-execution claims may be too broad or unsupported. |
| Missing approval evidence | Human approval or denial | Required approval state may be unsupported. |
| Missing timeline evidence | Event ordering | Sequence, delay, retry, or inconsistency may be unresolved. |
| Conflicting evidence | Any reconstruction area | Multiple evidence sources support incompatible conclusions. |
| Untrusted self-report | Evidence source quality | Evidence relies only on model output or runtime self-report. |
| Uncorrelated evidence | Evidence chain | Evidence exists but cannot be tied to the scoped action. |
| Scope ambiguity | Reconstruction boundary | The reviewed boundary may be too unclear for a stable conclusion. |
| Ownership ambiguity | Handoff and follow-up | No role or component owner is identified for the gap. |

## Gap class 1: Missing request evidence

### Description

Missing request evidence means the original action request, proposed action, command, tool call, workflow step, or equivalent request artifact cannot be found, identified, or correlated.

### Reconstruction questions affected

- What action or non-action is being reconstructed?
- Was the action proposed by a model, user, workflow, runtime, or external system?
- Was the action uniquely identifiable?
- Can the request be correlated to later authorization, dispatch, backend, and evidence events?

### Possible impacts

- The reconstruction object may be ambiguous.
- Authorization evidence may not be linkable to the request.
- Dispatch evidence may not be linkable to the request.
- Backend evidence may not be linkable to the request.
- The review may need to classify the conclusion as partial, unsupported, or out of scope.

### Possible owner

- Agent runtime owner
- Workflow owner
- Tool gateway owner
- Evidence pipeline owner
- Application owner
- Reviewer or maintainer

### Required caution

Do not infer the original request solely from model explanation or later runtime narrative unless the limitation is explicitly recorded.

## Gap class 2: Missing principal evidence

### Description

Missing principal evidence means the reconstruction cannot identify who or what initiated, requested, approved, or triggered the action, or on whose behalf the action was taken.

### Reconstruction questions affected

- Which principal initiated the action?
- Which component acted?
- On whose behalf was the action performed or attempted?
- Was the acting principal distinct from the represented principal?
- Was the principal context captured in evidence?

### Possible impacts

- Authority reconstruction may be incomplete.
- Responsibility assignment may be ambiguous.
- Risk-owner review may be required.
- Legal or organizational authorization must not be inferred from incomplete evidence.

### Possible owner

- Identity and access management owner
- Application owner
- Agent runtime owner
- Authorization component owner
- Risk owner
- Approver

### Required caution

AAEF does not resolve all identity, delegation, consent, or legal agency questions. Missing principal evidence should not be converted into an assumed authority chain.

## Gap class 3: Missing authority evidence

### Description

Missing authority evidence means the authority source, scope, freshness, delegation path, or reauthorization state cannot be confirmed.

### Reconstruction questions affected

- What authority source was asserted?
- Was the authority scoped to the action?
- Was the authority current at the time of decision?
- Was authority delegated, inherited, assumed, or ambiguous?
- Was reauthorization required?
- Was the authority chain preserved?

### Possible impacts

- The action may not be reconstructable as authorized.
- The decision may be only partially supported.
- Risk-owner review may be required.
- A stronger authorization conclusion may be unsupported.

### Possible owner

- Authorization decision component owner
- Policy owner
- IAM owner
- Approver
- Risk owner
- Backend relying party owner

### Required caution

Missing authority evidence should not be treated as proof of no authority or proof of authority. It means the authority conclusion is unsupported or partial within the reviewed boundary.

## Gap class 4: Missing decision evidence

### Description

Missing decision evidence means the authorization decision cannot be found, correlated, or interpreted.

### Reconstruction questions affected

- Was an authorization decision made?
- What decision was recorded?
- Was the action allowed, denied, held, escalated, or not dispatched?
- Which component made the decision?
- What policy or rule version was evaluated?
- Was the decision made before dispatch?

### Possible impacts

- Execution may not be linkable to authorization.
- Non-execution may not be linkable to denial or hold state.
- The review may need to classify the result as unsupported or conflicting.
- Validator or artifact success must not be substituted for runtime decision evidence.

### Possible owner

- Authorization decision point owner
- Policy engine owner
- Agent runtime owner
- Evidence producer
- Tool gateway owner
- Maintainer

### Required caution

A missing decision record does not prove the action was unauthorized. It means the authorization decision cannot be supported by available evidence.

## Gap class 5: Missing enforcement evidence

### Description

Missing enforcement evidence means the dispatch enforcement outcome is unavailable, incomplete, ambiguous, or not correlated to the decision.

### Reconstruction questions affected

- Was dispatch attempted?
- Was dispatch allowed?
- Was dispatch blocked?
- Was dispatch held or escalated?
- Was the dispatched action identical to the authorized action?
- Was enforcement consistent with the decision?
- Can dispatch evidence be correlated to backend evidence?

### Possible impacts

- The reconstruction may not distinguish allowed execution from bypass.
- Blocked-action claims may be unsupported.
- Non-dispatch claims may be unsupported.
- A conclusion about enforcement effectiveness may be out of scope.

### Possible owner

- Tool dispatch enforcement point owner
- Tool gateway owner
- Agent runtime owner
- Backend relying party owner
- Evidence pipeline owner

### Required caution

Do not claim enforcement effectiveness without evidence that links the decision to the dispatch or non-dispatch outcome.

## Gap class 6: Missing backend evidence

### Description

Missing backend evidence means the backend, tool, API, service, or downstream system result is unavailable, incomplete, ambiguous, or not correlated.

### Reconstruction questions affected

- Did the backend receive the action?
- Did the backend accept the action?
- Did the backend reject the action?
- Did the backend fail?
- Did the backend partially execute the action?
- Did the backend produce side effects?
- Was the backend result independently recorded?

### Possible impacts

- Execution status may be uncertain.
- Non-execution claims may be too broad.
- Backend rejection cannot be distinguished from non-dispatch.
- Side-effect conclusions may be unsupported.

### Possible owner

- Backend relying party owner
- Tool owner
- API owner
- Application owner
- Evidence producer
- Operator

### Required caution

Backend rejection does not prove absence of all side effects. Missing backend evidence should narrow the reconstruction conclusion.

## Gap class 7: Missing execution evidence

### Description

Missing execution evidence means available artifacts do not support whether the action executed, partially executed, failed, retried, cancelled, or produced side effects.

### Reconstruction questions affected

- Did the action execute?
- Did it partially execute?
- Did it fail before completion?
- Was execution retried?
- Was execution cancelled?
- Were side effects produced?
- Was execution consistent with the decision and dispatch evidence?

### Possible impacts

- The execution outcome may be unsupported.
- Root-cause conclusions may be premature.
- Operator action may be needed to inspect downstream state.
- Risk-owner review may be required if impact is uncertain.

### Possible owner

- Backend owner
- Operator
- Application owner
- Tool owner
- Evidence pipeline owner
- Risk owner

### Required caution

Do not claim execution, non-execution, or absence of side effects without scoped evidence.

## Gap class 8: Missing non-execution evidence

### Description

Missing non-execution evidence means the review cannot support that an action was denied, held, blocked, not dispatched, or not received by a backend.

### Reconstruction questions affected

- Was the action denied?
- Was it held?
- Was it escalated?
- Was it not dispatched?
- Was dispatch blocked?
- Did the backend not receive the action?
- Are there signs of retries, alternate paths, partial attempts, or side effects?

### Possible impacts

- Non-execution conclusions may be unsupported.
- The review may need to classify the result as ambiguous.
- Operator or backend owner review may be needed.
- A claim that "nothing happened" may be unsafe.

### Possible owner

- Tool gateway owner
- Backend owner
- Operator
- Authorization component owner
- Evidence pipeline owner
- Risk owner

### Required caution

Non-execution evidence must be scoped to the reviewed boundary. It does not prove absence of all side effects.

## Gap class 9: Missing approval evidence

### Description

Missing approval evidence means required human approval, denial, hold, escalation, or approver identity cannot be confirmed.

### Reconstruction questions affected

- Was human approval required?
- Was approval granted?
- Was approval denied?
- Was approval missing?
- Was approval stale or ambiguous?
- Was the approver authorized?
- Can approval be correlated to the action and decision?

### Possible impacts

- High-impact action reconstruction may be incomplete.
- Authorization conclusions may be partial or unsupported.
- Risk-owner review may be required.
- Human-in-the-loop claims may be unsupported.

### Possible owner

- Approver
- Human approval workflow owner
- Authorization component owner
- Evidence producer
- Risk owner

### Required caution

Do not infer approval from execution alone. Execution may have occurred without sufficient approval evidence.

## Gap class 10: Missing timeline evidence

### Description

Missing timeline evidence means timestamps, ordering, retries, delays, or sequence relationships cannot be reconstructed.

### Reconstruction questions affected

- When was the request created?
- When was authority evaluated?
- When was the decision made?
- When was dispatch attempted or blocked?
- When did the backend respond?
- When was evidence generated?
- Were events ordered correctly?
- Were there retries, holds, or escalations?

### Possible impacts

- Causality may be uncertain.
- Decision-before-dispatch may be unsupported.
- Retry or fallback behavior may be hidden.
- Conflicting evidence may be harder to resolve.

### Possible owner

- Evidence pipeline owner
- Agent runtime owner
- Authorization component owner
- Tool gateway owner
- Backend owner
- Operator

### Required caution

Timestamp presence supports reconstruction but does not prove authorization correctness, safety, compliance, or complete reconstruction.

## Gap class 11: Conflicting evidence

### Description

Conflicting evidence means two or more evidence sources support incompatible conclusions.

### Reconstruction questions affected

- Which evidence source is authoritative for this event?
- Do the sources cover the same boundary?
- Do timestamps disagree?
- Does one source describe a request while another describes dispatch or backend result?
- Does model output conflict with independently generated evidence?
- Does the backend result conflict with dispatch evidence?

### Possible impacts

- The reconstruction result may be conflicting.
- A stronger conclusion may require escalation.
- Component owners may need to explain discrepancies.
- Evidence trust assumptions may need review.

### Possible owner

- Evidence reviewer
- Evidence pipeline owner
- Component owners for conflicting sources
- Operator
- Maintainer
- Risk owner

### Required caution

Do not resolve conflicts by selecting the most convenient evidence source. Record the conflict and identify the basis for any preferred interpretation.

## Gap class 12: Untrusted self-report

### Description

Untrusted self-report means evidence relies only on model output, agent runtime narrative, or another source that is not independently generated or corroborated.

### Reconstruction questions affected

- Is the evidence independently generated?
- Is the evidence corroborated?
- Is the evidence merely a model explanation?
- Is the evidence merely a runtime self-report?
- Does the evidence prove action request, decision, dispatch, backend result, or execution outcome?

### Possible impacts

- The conclusion may be unsupported or partial.
- Evidence quality may be insufficient for the reconstruction question.
- Additional corroborating evidence may be required.
- Reviewer language should be narrowed.

### Possible owner

- Evidence pipeline owner
- Agent runtime owner
- Reviewer
- Maintainer
- Tool gateway owner
- Backend owner

### Required caution

Model output is not authority, and model explanation is not sufficient action-bound evidence by itself.

## Gap class 13: Uncorrelated evidence

### Description

Uncorrelated evidence means relevant-looking evidence exists but cannot be tied to the scoped action, decision, dispatch, backend result, or review object.

### Reconstruction questions affected

- Does the evidence refer to the same action?
- Does the evidence share a stable identifier?
- Does the evidence share a consistent timestamp or sequence?
- Does the evidence match the same principal, tool, backend, or decision?
- Can the evidence be linked across components?

### Possible impacts

- The review may have evidence but not action-bound evidence.
- Reconstruction may remain partial.
- Strong conclusions may be unsupported.
- Evidence pipeline improvements may be needed.

### Possible owner

- Evidence pipeline owner
- Agent runtime owner
- Authorization component owner
- Tool gateway owner
- Backend owner
- Maintainer

### Required caution

General logs or similar-looking records should not be treated as action-bound evidence unless correlation is supported.

## Gap class 14: Scope ambiguity

### Description

Scope ambiguity means the reconstruction boundary, included systems, excluded systems, time range, or review target is unclear.

### Reconstruction questions affected

- What is included in the reconstruction?
- What is excluded?
- Which system boundary is being reviewed?
- Which evidence sources are in scope?
- Which side effects are out of scope?
- Which conclusions are out of scope?

### Possible impacts

- Conclusions may be overbroad.
- Non-execution claims may exceed the reviewed boundary.
- Audit, legal, operational, or compliance implications may be overstated.
- The review may need to restart with a narrower boundary.

### Possible owner

- Reviewer
- Risk owner
- Operator
- System owner
- Maintainer
- Engagement or review lead

### Required caution

If the boundary is unclear, conclusions should be narrowed or marked out of scope.

## Gap class 15: Ownership ambiguity

### Description

Ownership ambiguity means no role, team, or component owner is identified for resolving, accepting, or escalating the evidence gap.

### Reconstruction questions affected

- Who owns the missing evidence?
- Who owns the affected component?
- Who can provide additional evidence?
- Who can accept residual uncertainty?
- Who can decide whether to pause, escalate, retry, or close the review?
- Who should open follow-up work?

### Possible impacts

- Gaps may remain unresolved.
- Risk acceptance may be unclear.
- Operational handoff may fail.
- Follow-up issues may not be opened.
- Reconstruction may stall.

### Possible owner

- Reviewer
- Operator
- Risk owner
- Component owner
- Maintainer
- Approver
- Project owner

### Required caution

An unowned gap should not be silently accepted. It should be assigned, escalated, or explicitly documented as residual uncertainty.

## Conclusion impact categories

Evidence gaps should be tied to their impact on conclusions.

| Impact | Meaning |
| --- | --- |
| Blocks conclusion | The conclusion should not be made without resolving the gap. |
| Narrows conclusion | A narrower conclusion may be supported. |
| Adds uncertainty | The conclusion may be supported, but residual uncertainty must be recorded. |
| Requires owner decision | A risk owner, operator, approver, or maintainer must decide whether the residual uncertainty is acceptable. |
| Requires follow-up evidence | Additional evidence should be collected. |
| Requires scope change | The reconstruction boundary should be narrowed or redefined. |
| Requires escalation | Separate operational, legal, audit, compliance, incident-response, or component-owner review may be needed. |

## Escalation and handoff criteria

A gap should be considered for escalation when:

- it blocks a high-impact action conclusion,
- it affects authorization or approval evidence,
- it affects whether execution or non-execution occurred,
- it affects possible side effects,
- it affects residual business or safety risk,
- evidence sources conflict,
- evidence relies only on model output or runtime self-report,
- the relevant component owner is unclear,
- legal, audit, compliance, or incident-response implications may exist, or
- the reviewer cannot safely narrow the conclusion.

Escalation does not establish legal, audit, compliance, or incident-response sufficiency. It routes the unresolved question to the appropriate owner.

## Minimal gap classification prompt

For a lightweight review, reviewers may ask:

1. What conclusion is being evaluated?
2. What evidence supports the conclusion?
3. What evidence is missing?
4. Is the missing evidence request, principal, authority, decision, enforcement, backend, execution, non-execution, approval, timeline, correlation, scope, or ownership evidence?
5. Does the gap block the conclusion, narrow the conclusion, add uncertainty, require owner decision, require follow-up evidence, require scope change, or require escalation?
6. Who owns the gap?
7. What safer conclusion can be stated now?
8. What follow-up action is needed?

This prompt is a review aid only and does not define a complete operational procedure.

## Safe wording patterns

When evidence gaps exist, prefer narrow wording.

| Overbroad wording | Safer wording |
| --- | --- |
| The action was authorized. | Available evidence supports an authorization decision within the reviewed boundary. |
| The action did not execute. | Available evidence supports non-dispatch within the reviewed enforcement boundary; absence of all side effects is not established. |
| The backend rejected the action, so nothing happened. | Backend rejection is recorded, but possible side effects or alternate paths require separate review. |
| The model explained what happened. | The model explanation is available, but action-bound evidence is still required. |
| The logs prove the reconstruction. | The available evidence supports a scoped reconstruction, with the following gaps recorded. |
| The issue is closed. | The current reconstruction conclusion is supported within scope; unresolved gaps are assigned or accepted as residual uncertainty. |

## Relationship to future #322 work

This note may support narrower follow-up artifacts such as:

- action timeline reconstruction checklist,
- authority chain reconstruction checklist,
- decision chain reconstruction checklist,
- execution and non-execution reconstruction checklist,
- reviewer/operator/risk-owner handoff note,
- reconstruction walkthrough candidates, and
- #322 close-readiness checklist.

These should remain planning or review artifacts unless a later issue explicitly scopes executable fixtures, examples, validators, or implementation work.

## Review questions

Reviewers should be able to answer:

- Does this note preserve the thesis that model output is not authority?
- Does this note distinguish model explanation from action-bound evidence?
- Does this note classify missing and limited evidence without converting gaps into conclusions?
- Does this note distinguish missing evidence, conflicting evidence, untrusted self-report, uncorrelated evidence, scope ambiguity, and ownership ambiguity?
- Does this note connect evidence gaps to conclusion impact?
- Does this note identify when escalation or handoff may be needed?
- Does this note avoid audit sufficiency, legal sufficiency, operational readiness, incident-response certification, complete reconstruction, and complete root-cause claims?
- Does this note create useful follow-up paths for #322?

## Scope reminder

This artifact is planning and review material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, or JSON examples.

It does not establish operational readiness, complete reconstruction, complete root-cause analysis, incident-response certification, audit sufficiency, legal sufficiency, empirical validation, implementation conformance, production readiness, certification, compliance, conformity, or external-framework equivalence.
