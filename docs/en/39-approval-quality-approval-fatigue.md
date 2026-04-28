# Approval Quality and Approval Fatigue

**Status:** v0.5.0 planning concept
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative planning note for approval quality, approval fatigue, and meaningful human authorization

## Purpose

This document defines Approval Quality and Approval Fatigue as a v0.5.0 planning concept for AAEF.

AAEF already recognizes that some high-risk and critical actions require explicit approval or additional verification.

The remaining design issue is that an approval event is not automatically meaningful. A human click, generic confirmation, or repeated approval prompt may create the appearance of control while failing to provide informed authorization.

This concept note explores how AAEF should distinguish meaningful approval from approval-shaped friction.

## Core Principle

Human approval is not authority unless the approver has enough context, capability, time, and independence to make a meaningful decision.

Approval controls should not rely on blind confirmation, alert fatigue, generic consent, or rubber-stamping as evidence of authorization.

## Problem Statement

Agentic AI systems may generate frequent, complex, or ambiguous approval prompts.

If approval is overused, poorly designed, or insufficiently contextualized, humans may approve high-impact actions without understanding:

- what action will occur;
- on whose behalf it will occur;
- what resource or system will be affected;
- what authority is being used;
- what risk or irreversible effect exists;
- what alternatives exist;
- what prior denials, retries, or reauthorization attempts occurred;
- whether the action was influenced by untrusted input;
- whether the model output is merely a proposal rather than authority.

This creates approval fatigue and weakens the assurance value of human oversight.

## Approval Quality

Approval quality refers to whether an approval decision is informed, contextual, attributable, timely, and appropriate for the risk of the action.

A high-quality approval should generally answer:

1. Who is approving?
2. What action is being approved?
3. On whose behalf will the action occur?
4. What authority basis applies?
5. What resource, account, system, or external party will be affected?
6. What risk, impact, reversibility, or external effect exists?
7. What policy or control condition triggered approval?
8. What evidence was shown to the approver?
9. What alternatives were available?
10. Was approval granted before execution?
11. Was the approval specific to the action, or broad and reusable?
12. Was the approval linked to the final dispatched or executed action?

## Approval Fatigue

Approval fatigue occurs when repeated, low-quality, poorly prioritized, or overly frequent approval prompts cause approvers to stop exercising meaningful judgment.

Approval fatigue may be caused by:

- too many prompts;
- generic prompts;
- prompts with insufficient action context;
- repeated prompts for similar actions;
- unclear risk severity;
- lack of meaningful deny or defer options;
- approval requests after the system has already progressed too far;
- prompts that hide material changes between request and execution;
- prompts that require expert judgment from non-expert users;
- prompts caused by retry loops or task splitting;
- alerts that do not distinguish routine actions from critical actions.

## Risk Factors

Approval quality concerns increase when actions are:

- high-impact;
- irreversible;
- externally impactful;
- cross-domain;
- delegated;
- reauthorization-required;
- influenced by untrusted input;
- associated with degraded principal context;
- repeated after denial;
- part of an incident or suspected compromise;
- capable of affecting production systems, funds, access rights, security controls, safety, legal obligations, or customer data.

## Candidate Approval Quality Requirements

Future AAEF work may refine approval-related controls to require that approval prompts include:

- action summary;
- principal context;
- authority basis;
- target resource;
- purpose;
- risk level;
- reversibility;
- external impact;
- delegated scope where applicable;
- prior denial or reauthorization context;
- input trust or untrusted influence warning where relevant;
- evidence limitations;
- final effective scope;
- execution timing;
- approver identity;
- approval decision;
- approval timestamp;
- linkage to final dispatch and execution evidence.

## Candidate Fatigue Controls

Future AAEF work may consider controls for:

- approval frequency monitoring;
- repeated approval prompt detection;
- retry-driven approval escalation;
- task-splitting detection;
- risk-based prompt prioritization;
- suppression or aggregation of low-risk prompts;
- stronger friction for critical actions;
- mandatory cooling-off or second approval for certain actions;
- approval quality review metrics;
- post-approval outcome sampling;
- approver workload and role suitability review.

## Approval Is Not a Substitute for Authorization

Human approval should not replace execution-time authorization.

A high-quality approval may support authorization, but the system should still evaluate whether the action is allowed at the point of execution.

The final dispatched action should remain within the approved scope.

If the action changes materially after approval, the system should deny, defer, escalate, or require reapproval.

## Relationship to AAEF Controls

This concept may inform future refinements to:

- `AAEF-AUZ-03`: explicit approval or additional verification for high-risk actions;
- `AAEF-AUZ-08`: safe handling of material ambiguity;
- `AAEF-AUZ-09`: denial and reauthorization flow;
- `AAEF-EVD-01`: evidence recording;
- `AAEF-EVD-05`: non-execution evidence;
- `AAEF-EVD-06`: reauthorization evidence;
- `AAEF-HUM-*` if future human oversight controls are added.

## Relationship to Evidence

Approval evidence should be action-bound.

Evidence should show:

- what the approver saw;
- what decision was made;
- when approval occurred;
- who approved;
- what scope was approved;
- whether the executed action matched the approved action;
- whether approval was reused;
- whether approval followed prior denial, retry, escalation, or reauthorization;
- whether any material context changed before execution.

Approval evidence should avoid storing unnecessary sensitive content. Structured summaries, identifiers, hashes, screenshots, or references may be preferable to raw prompt or full payload retention where appropriate.

For non-normative approval evidence examples, see `docs/en/40-approval-evidence-examples.md`.

## Negative Test Ideas

Assessments may test whether:

- a generic approval can authorize a materially different action;
- approval can be reused outside its intended scope;
- repeated denial can be bypassed by rephrasing or task splitting;
- an approver receives insufficient context;
- an approver receives too many prompts to review meaningfully;
- approval occurs after execution has already effectively happened;
- approval evidence cannot be linked to the final executed action;
- a model-generated recommendation hides material risk from the approver;
- untrusted input influences the approval request without warning;
- a low-risk approval path can be used for a high-risk action.

## Non-Goals

This concept does not require:

- human approval for every high-impact action;
- manual review for every tool call;
- a specific approval UI;
- a specific workflow engine;
- a specific ticketing system;
- raw prompt retention by default;
- replacing execution-time authorization with human approval;
- treating a click as sufficient authority.

## Future Work

Future AAEF work may decide whether to:

- strengthen `AAEF-AUZ-03`;
- add approval quality testing procedures;
- add approval fatigue assessment guidance;
- add approval evidence examples;
- define approval quality metrics;
- define a dedicated human oversight or approval quality control;
- connect approval quality to risk-proportional evidence levels.
