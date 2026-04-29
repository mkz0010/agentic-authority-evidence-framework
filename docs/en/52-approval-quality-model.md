# Approval Quality Model

**Status:** Non-normative v0.5.0 planning model

> **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifacts, testing procedures, or release notes.

## Purpose

This document defines a non-normative planning model for approval quality and approval fatigue in AAEF.

It connects the current v0.5.0 planning theme:

- Approval Quality and Approval Fatigue

The purpose is to distinguish meaningful human approval from superficial approval UI, rubber-stamping, bulk confirmation, or approval flows that do not provide enough context for the approver to make an informed decision.

This model does not introduce new control requirements by itself.

## Design Rationale

Human approval is often used as a safety boundary for agentic actions.

However, a human approval step does not automatically create assurance.

Approval quality depends on whether the approver receives enough information, has appropriate authority, understands the action and its consequences, and approves a specific action within a clear scope.

AAEF planning should avoid treating the presence of an approval button as equivalent to meaningful authorization.

## Approval Quality Dimensions

| Dimension | Description | Primary risk |
| --- | --- | --- |
| Approver identity | The system records who approved the action and whether that approver was eligible. | Approval is anonymous, spoofed, delegated incorrectly, or performed by an unauthorized actor. |
| Action specificity | The approval is tied to a specific action, target, scope, and expected effect. | Approval is reused for actions the approver did not review. |
| Context sufficiency | The approver receives enough risk, policy, evidence, and consequence information. | The approver cannot make an informed decision. |
| Scope clarity | The approval has clear limits, validity window, target, and constraints. | Approval is interpreted more broadly than intended. |
| Risk visibility | The approver can see whether the action is high-impact, irreversible, privileged, sensitive, or unusual. | High-risk actions are approved as if they were routine. |
| Alternatives and denial path | The approver can deny, defer, escalate, or request changes. | Approval becomes a forced confirmation step. |
| Fatigue resistance | The workflow limits repetitive, low-information, or excessive approval prompts. | Approvers rubber-stamp actions due to volume or poor UI design. |
| Evidence capture | The approval event is recorded with enough detail for later assessment or incident review. | Auditors cannot determine what was approved, by whom, and under what context. |

## Meaningful Approval

Meaningful approval requires more than a user click.

A meaningful approval should be:

- tied to a specific action or bounded action set;
- tied to an identified approver;
- based on sufficient context;
- limited by scope and validity period where appropriate;
- recorded as action-bound evidence;
- enforceable by a trusted component;
- revocable, deniable, or rejectable where the workflow requires it.

The approver should not need to infer critical details solely from model-generated summaries.

## Approval Context Sufficiency

Approval context is sufficient when it allows the approver to understand what is being authorized.

Depending on the action risk, approval context may include:

- action type;
- target system, object, user, tenant, or resource;
- expected effect;
- risk tier or impact category;
- whether the action is reversible;
- whether the action involves external communication, data modification, privilege change, financial impact, or destructive operation;
- requesting agent or workflow;
- relevant policy decision or recommendation;
- evidence summary or supporting context;
- expiry or validity window;
- known constraints, exclusions, or assumptions.

For high-impact actions, approval context should be specific enough that a later reviewer can determine whether the approver authorized the executed action, not merely a vague category of activity.

## Approval Fatigue

Approval fatigue occurs when approvers are asked to approve too many actions, too frequently, with too little context, or with poor differentiation between routine and high-risk actions.

Approval fatigue can cause:

- rubber-stamping;
- missed high-risk actions;
- overreliance on defaults;
- approval of unclear or bundled actions;
- reduced attention to exception conditions;
- loss of trust in the approval workflow.

Approval fatigue is an assurance risk because it weakens the reliability of human approval as a control.

## Batch Approval and Bundling Risk

Batch approvals can be useful, but they create additional risk.

A batch approval should make clear:

- which actions are included;
- which actions are excluded;
- whether the approval applies to each action individually or to the batch as a whole;
- whether the batch contains mixed-risk actions;
- whether any action in the batch requires separate approval;
- how denied or partially approved items are handled;
- how the approval evidence links to each executed action.

High-impact or irreversible actions should not be hidden inside broad, low-information batches.

## Approval State Model

The following state model is a planning aid.

| Approval state | Meaning | Expected behavior |
| --- | --- | --- |
| Not required | The action does not require human approval under the applicable policy. | Proceed according to non-human authorization controls. |
| Required | The action requires approval before execution. | Block execution until valid approval is recorded. |
| Requested | Approval has been requested but not yet granted or denied. | Do not execute the approval-gated action. |
| Approved | An eligible approver approved the action within scope. | Execute only within the approved scope and validity window. |
| Denied | The approver rejected the action. | Do not execute; record denial evidence. |
| Expired | The approval is no longer valid. | Require renewed approval before execution. |
| Revoked | Previously granted approval has been withdrawn. | Stop dependent execution and invalidate cached approval. |
| Escalated | The action requires additional review or higher authority. | Do not execute until escalation is resolved. |
| Partial | Only part of a requested action set was approved. | Execute only the approved portion, if safe and supported. |
| Ambiguous | Approval context, scope, approver, or target is unclear. | Treat as insufficient approval and require clarification or reauthorization. |

## Evidence Expectations

Approval evidence should allow a reviewer to reconstruct:

- who requested approval;
- which action or action set was approved;
- who approved, denied, escalated, or revoked approval;
- whether the approver was eligible;
- what context was shown to the approver;
- what risk level or impact category was presented;
- when approval was requested and granted;
- whether the approval had an expiry, scope, or validity window;
- whether the executed action matched the approved scope;
- whether approval was denied, expired, revoked, partial, or ambiguous.

Approval evidence should not rely solely on model-generated explanations, screenshots without structured context, or agent runtime self-reporting.

## Approval Anti-Patterns

Implementers should avoid:

- generic “approve all” prompts for mixed-risk actions;
- approval prompts that omit target, effect, or risk context;
- approvals that are not tied to specific executed actions;
- approval records without approver identity;
- approvals generated or modified by the agent being approved;
- approval reuse outside the original scope;
- approval after execution when pre-execution approval was required;
- approval flows where denial or escalation is unavailable;
- treating conversation text as durable approval for later actions;
- hiding high-impact actions inside low-risk batches.

## Relationship to Existing AAEF Artifacts

This planning model may inform future refinements to:

- human approval controls;
- authorization controls;
- delegation controls;
- testing procedures for approval-gated actions;
- evidence expectations for approval records;
- high-impact and audit-grade prequalification guidance.

The model does not itself change the v0.4.1 control catalog, assessment worksheet, testing procedures, evidence schema, or external framework mappings.

## Relationship to HUM Controls

This model is especially relevant to human approval and human oversight controls.

Future incorporation may refine existing HUM controls or introduce additional control language if approval quality and approval fatigue cannot be adequately represented by existing controls.

Any such incorporation should preserve the distinction between:

- approval UI presence;
- approval evidence;
- approval authority;
- approval context quality;
- approval effectiveness under realistic workload.

## Preliminary Incorporation Outcome

The expected incorporation path is:

| Planning theme | Likely incorporation path |
| --- | --- |
| Approval Quality and Approval Fatigue | Existing HUM control refinement, guidance, testing refinement, and possible new HUM control candidate if approval quality cannot be adequately represented by existing controls |

Any future normative incorporation should follow the incorporation rules and outcome register in `docs/en/34-v050-control-design-options.md`.
