# v0.7.0 Operational Reconstruction Planning

## Purpose

This document defines the initial planning scope for the v0.7.0 Operational Reconstruction track.

The goal is to make AI-assisted actions, denied actions, held actions, escalations, and evidence gaps easier to reconstruct after the fact.

This document is planning material only. It does not introduce new controls, update the evidence schema, update assessment artifacts, define testing procedures, add executable validators, add executable prototypes, provide incident-response certification, provide audit sufficiency, provide legal sufficiency, or claim operational readiness.

## Relationship to the AAEF thesis

AAEF is organized around the thesis that model output is not authority.

For operational reconstruction, this means a reviewer should not rely only on model output, model explanations, or agent runtime self-reports when determining what happened.

A reconstruction should instead ask:

- what action was proposed,
- who or what requested it,
- on whose behalf it was requested,
- what authority was asserted,
- what authorization decision was made,
- what dispatch or non-dispatch outcome occurred,
- what backend accepted or rejected,
- what evidence was generated,
- what evidence is missing, and
- which component or role owns the gap.

## Scope

This planning track may define:

- operational reconstruction goals,
- action timeline reconstruction concepts,
- authority chain reconstruction concepts,
- decision chain reconstruction concepts,
- execution and non-execution reconstruction concepts,
- evidence gap classification concepts,
- reviewer, operator, and risk-owner questions,
- relationship to v0.7.0 evaluation reconstruction work, and
- future operational reconstruction artifacts.

This track may also identify follow-up artifacts that should be split into narrower issues or PRs.

## Non-goals

This document does not:

- change the current active control and assessment baseline,
- update the control catalog,
- update the evidence schema,
- update assessment artifacts,
- update testing procedures,
- add executable validators,
- add executable prototypes,
- add scenario fixtures,
- add JSON examples,
- define a complete incident-response methodology,
- define a forensic investigation methodology,
- provide legal sufficiency,
- provide audit sufficiency,
- provide incident-response certification,
- provide operational readiness,
- claim complete reconstruction,
- claim complete root-cause analysis,
- claim complete threat coverage,
- claim empirical validation,
- claim implementation conformance,
- claim production readiness, or
- claim certification, compliance, conformity, or external-framework equivalence.

## Reconstruction posture

Operational reconstruction should be treated as a structured review activity, not as a guarantee that every event can be fully recovered.

AAEF may help reviewers ask clearer questions about action authority, execution boundaries, evidence, and responsibility handoff.

However, AAEF does not guarantee that evidence exists, that evidence is complete, that evidence is tamper-proof, that root cause is fully determined, or that legal or audit conclusions can be reached from AAEF artifacts alone.

## Reconstruction object

The primary reconstruction object is an AI-assisted action or non-action.

A reconstruction object may include:

- an allowed and executed action,
- an allowed but failed action,
- a denied action,
- a held action,
- an escalated action,
- a not-dispatched action,
- a partially attempted action,
- a backend-rejected action,
- an action with incomplete evidence, or
- an action where the execution status is ambiguous.

## Reconstruction dimensions

Operational reconstruction should consider at least six dimensions.

| Dimension | Core question | Example reconstruction concern |
| --- | --- | --- |
| Action timeline | What happened and when? | Request, decision, dispatch, backend response, evidence generation |
| Authority chain | Who or what had authority? | Acting principal, represented principal, delegated authority, authority freshness |
| Decision chain | What decision was made? | Allowed, denied, held, escalated, not dispatched |
| Execution chain | What execution or non-execution occurred? | Tool dispatch, backend acceptance, backend rejection, side effects |
| Evidence chain | What evidence exists? | Evidence correlation, evidence source, evidence gaps |
| Responsibility chain | Who owns the next review step? | Operator, reviewer, risk owner, implementer, approver |

These dimensions are planning concepts. They do not define a complete operational procedure by themselves.

## Action timeline reconstruction

### Planning goal

Action timeline reconstruction should help reviewers understand the sequence of events around a scoped action or non-action.

### Candidate timeline questions

Reviewers may ask:

- When was the action proposed?
- When was the action request created?
- When was authorization evaluated?
- When was the action allowed, denied, held, escalated, or not dispatched?
- When was tool dispatch attempted or blocked?
- When did the backend accept, reject, or fail the action?
- When was evidence generated?
- Were timestamps consistent across components?
- Are there missing or conflicting timestamps?

### Required caution

A timeline does not prove correctness by itself.

Timestamp presence does not prove that the action was authorized, safe, compliant, or fully reconstructed.

### Future work

Potential follow-up artifacts include:

- action timeline reconstruction checklist,
- reconstruction walkthrough candidate,
- evidence gap classification for timestamp inconsistencies, and
- relationship note to evaluation reconstruction exercises.

## Authority chain reconstruction

### Planning goal

Authority chain reconstruction should help reviewers understand who or what acted, on whose behalf, and under what authority.

### Candidate authority questions

Reviewers may ask:

- Which principal initiated or requested the action?
- Which system component acted?
- On whose behalf was the action performed or attempted?
- What authority source was used?
- Was the authority scoped to the action?
- Was the authority current at the time of decision?
- Was authority delegated, inherited, assumed, or ambiguous?
- Was reauthorization required?
- Was the authority chain preserved in evidence?

### Required caution

Authority chain reconstruction does not resolve every identity, delegation, consent, or legal agency question.

It also does not prove legal authorization or organizational approval unless those conclusions are separately established.

### Future work

Potential follow-up artifacts include:

- authority chain reconstruction checklist,
- principal-context reconstruction questions,
- stale or degraded authority scenarios,
- risk-owner review questions, and
- relationship note to Research Positioning artifacts.

## Decision chain reconstruction

### Planning goal

Decision chain reconstruction should help reviewers understand how an action moved from request to allow, deny, hold, escalation, or non-dispatch.

### Candidate decision questions

Reviewers may ask:

- What action was requested?
- Which policy, authority source, or review rule was evaluated?
- What decision was made?
- Was the decision allow, deny, hold, escalate, or not dispatch?
- Which component made the decision?
- Which component enforced the decision?
- Was human approval required?
- Was human approval obtained, denied, or missing?
- Was the decision recorded with enough context for later review?
- Did any component act contrary to the decision?

### Required caution

Decision reconstruction does not prove that the policy was complete, correct, or legally sufficient.

It also does not prove that enforcement was effective unless the execution and evidence chains support that conclusion.

### Future work

Potential follow-up artifacts include:

- decision chain reconstruction checklist,
- allow/deny/hold/escalation review questions,
- human approval reconstruction checklist,
- relationship note to implementation reviewability artifacts, and
- evaluation scenario candidates.

## Execution and non-execution reconstruction

### Planning goal

Execution and non-execution reconstruction should help reviewers distinguish what actually executed, what did not execute, and what remains ambiguous.

### Candidate execution questions

Reviewers may ask:

- Was tool dispatch attempted?
- Was tool dispatch blocked?
- Was the action sent to a backend?
- Did the backend accept, reject, or fail the action?
- Did the action produce side effects?
- Was execution partial?
- Was execution retried?
- Was execution cancelled?
- Was the action denied before dispatch?
- Was the action held before dispatch?
- Is there evidence of non-execution within the reviewed boundary?
- Are there possible side effects outside the reviewed boundary?

### Required caution

Evidence of denial, hold, or non-dispatch does not prove absence of all side effects.

Non-execution claims must be scoped to the reviewed control boundary.

### Future work

Potential follow-up artifacts include:

- non-execution reconstruction checklist,
- blocked-action reconstruction scenario candidates,
- partial execution classification,
- side-effect ambiguity questions, and
- relationship note to high-impact action review.

## Evidence gap classification

### Planning goal

Evidence gap classification should help reviewers describe what is missing without overclaiming what can be concluded.

### Candidate evidence gap categories

Evidence gaps may include:

| Gap category | Description | Example review question |
| --- | --- | --- |
| Missing request evidence | The action request cannot be found or correlated | What initiated the action? |
| Missing authority evidence | Authority source or principal context is missing | On whose behalf was the action taken? |
| Missing decision evidence | Authorization decision is missing or incomplete | Was the action allowed, denied, or held? |
| Missing enforcement evidence | Dispatch enforcement outcome is missing | Was the action dispatched or blocked? |
| Missing backend evidence | Backend acceptance, rejection, or result is missing | Did the backend execute the action? |
| Missing non-execution evidence | Denial, hold, or non-dispatch cannot be proven | What supports the non-execution claim? |
| Conflicting evidence | Sources disagree | Which component is authoritative for this event? |
| Untrusted self-report | Evidence relies only on model or runtime self-report | Is there independent or corroborating evidence? |
| Scope ambiguity | The reviewed boundary is unclear | What system or component boundary is being reconstructed? |
| Ownership ambiguity | No owner is identified for the gap | Who must resolve or accept the gap? |

### Required caution

Classifying evidence gaps does not fill the gaps.

It also does not determine legal, audit, or compliance conclusions.

### Future work

Potential follow-up artifacts include:

- evidence gap taxonomy,
- evidence gap severity planning,
- reviewer handoff questions,
- gap-to-owner mapping, and
- operational reconstruction walkthroughs.

## Reviewer, operator, and risk-owner questions

Operational reconstruction may involve different roles.

### Reviewer questions

A reviewer may ask:

- What happened?
- What evidence supports that conclusion?
- What evidence is missing?
- Which claims are supported?
- Which claims are not supported?
- Which component or role owns the gap?

### Operator questions

An operator may ask:

- Is the system still in a safe operating state?
- Does an action need to be paused, frozen, reversed, or escalated?
- Is more evidence needed before continuing?
- Is the issue a policy failure, enforcement failure, evidence failure, or backend failure?
- Who should be notified?

### Risk-owner questions

A risk owner may ask:

- What business or safety impact may have occurred?
- Was the action within delegated authority?
- Was the action blocked, held, executed, or partially executed?
- What residual uncertainty remains?
- Is the residual uncertainty acceptable?
- What follow-up decision is needed?

### Required caution

These are planning questions only.

They do not define a complete role model, incident-response process, legal process, or audit procedure.

## Relationship to #319 Evaluation Readiness

The v0.7.0 Evaluation Readiness track included evaluation reconstruction exercise planning.

Operational Reconstruction should reuse that foundation while remaining distinct.

Evaluation reconstruction focuses on how reconstruction can be practiced or reviewed as part of evaluation planning.

Operational reconstruction focuses on how action timelines, authority chains, decision chains, execution outcomes, and evidence gaps should be described for operational review.

This document does not add executable scenarios or fixtures.

## Relationship to #320 Implementation Reviewability

The v0.7.0 Implementation Reviewability track documented assumptions, validator boundaries, and component responsibilities.

Operational Reconstruction should use those boundaries when asking which component produced, enforced, accepted, rejected, or failed to produce evidence.

This document does not add implementation code, validator code, or conformance tests.

## Relationship to #321 Research Positioning

The v0.7.0 Research Positioning track identified operational reconstruction as a candidate research contribution and research question area.

Operational Reconstruction develops that idea as a planning track.

This document does not claim empirical validation, peer review, or research conclusion.

## Candidate future #322 artifacts

Future #322 work may add narrower artifacts such as:

- operational reconstruction question set,
- action timeline reconstruction checklist,
- authority chain reconstruction checklist,
- decision chain reconstruction checklist,
- execution and non-execution reconstruction checklist,
- evidence gap classification note,
- reviewer/operator/risk-owner reconstruction handoff note,
- reconstruction walkthrough candidates, and
- #322 close-readiness checklist.

These should remain planning or review artifacts unless a later issue explicitly scopes executable fixtures, examples, validators, or implementation work.

## Review questions

Reviewers should be able to answer:

- Does this artifact preserve the thesis that model output is not authority?
- Does this artifact distinguish model explanation from action-bound evidence?
- Does this artifact distinguish execution from non-execution?
- Does this artifact avoid proving absence of all side effects?
- Does this artifact distinguish reconstruction support from incident-response certification?
- Does this artifact avoid audit sufficiency and legal sufficiency claims?
- Does this artifact preserve active baseline boundaries?
- Does this artifact create useful follow-up paths for #322?

## Scope reminder

This artifact is planning material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, or JSON examples.

It does not establish operational readiness, complete reconstruction, complete root-cause analysis, incident-response certification, audit sufficiency, legal sufficiency, empirical validation, implementation conformance, production readiness, certification, compliance, conformity, or external-framework equivalence.
