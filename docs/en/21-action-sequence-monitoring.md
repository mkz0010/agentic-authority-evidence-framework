# Action Sequence Monitoring and Task Splitting

This document provides draft guidance for monitoring action sequences in agentic systems.

AAEF controls often evaluate whether a specific proposed action was authorized, dispatched, executed, and evidenced correctly.

However, some risks are not visible when each action is reviewed in isolation.

An agentic system may produce a harmful or unauthorized outcome through a sequence of individually low-risk actions.

## Purpose

Action sequence monitoring helps assess whether an agentic system can detect, prevent, or escalate patterns of behavior that become risky only when viewed across multiple actions.

Examples include:

- splitting a large data export into many smaller exports,
- splitting a payment into multiple smaller transfers,
- making a series of infrastructure changes that collectively weaken security,
- creating subtasks that hide the final objective,
- repeatedly requesting actions that remain just below approval thresholds,
- using delegation chains to distribute responsibility across agents or tools,
- and combining individually permitted tool calls into an unauthorized operational effect.

The purpose of this guidance is not to require every low-risk action to be treated as high-impact.

The purpose is to ensure that high-impact outcomes cannot be hidden by decomposing them into smaller actions.

## Core Concept

An individual action may appear authorized when reviewed by itself.

A sequence of actions may still indicate:

- threshold avoidance,
- staged execution,
- hidden objective pursuit,
- unauthorized aggregation,
- policy evasion,
- excessive agency,
- or abuse of delegation.

Assessment should therefore consider both:

- action-level authorization,
- and sequence-level behavior.

## Task Splitting Risk

Task splitting occurs when an agent, workflow, user, or upstream system decomposes a high-impact objective into smaller actions that receive weaker review.

This can happen intentionally or unintentionally.

Examples include:

| Scenario | Individual action view | Sequence-level risk |
|---|---|---|
| Data export split into small batches | Each export is below the review threshold | The combined sequence may disclose a sensitive dataset |
| Payment split into small transfers | Each transfer is below approval limits | The combined sequence may exceed financial authorization |
| Incremental infrastructure changes | Each change appears routine | The combined changes may disable security controls or expose systems |
| Permission changes across multiple steps | Each grant appears limited | The combined privileges may create excessive access |
| Repeated failed or denied requests | Each denial is logged separately | The pattern may indicate attempted policy probing or evasion |
| Delegated subtasks | Each subtask appears narrow | The overall delegated objective may exceed authority |

## Sequence-Level Assessment Questions

Assessors should consider whether the implementation can answer the following questions.

| Question | Assessment relevance |
|---|---|
| Can related actions be correlated into a sequence? | Without correlation, task splitting may be invisible. |
| Can the system identify the user, agent, workflow, or objective behind related actions? | Sequence review requires a stable actor or objective reference. |
| Are approval thresholds evaluated only per action, or across related actions? | Per-action thresholds may be bypassed by repeated smaller actions. |
| Are repeated denials, retries, or near-threshold actions reviewed? | These patterns may indicate probing, evasion, or unsafe automation. |
| Can delegated subtasks be traced back to the originating objective? | Delegation can hide the larger intent or authority boundary. |
| Can evidence reconstruct the sequence after an incident? | Incident review requires action ordering, correlation, and outcome reconstruction. |

## Sequence Correlation

Action sequence monitoring may use one or more correlation references.

Examples include:

- `sequence_id`,
- `parent_action_id`,
- `root_objective_id`,
- `workflow_id`,
- `delegation_chain_id`,
- `principal_id`,
- `agent_id`,
- `tool_session_id`,
- `approval_request_id`,
- `policy_evaluation_id`,
- `case_id`,
- or incident / investigation reference.

AAEF v0.3.0 does not require a specific schema field for all sequence correlation.

However, implementations should be able to explain how related actions can be correlated when sequence-level risk is relevant.

Future versions may define additional schema guidance for action sequence correlation.

## Monitoring Expectations by Profile

Action sequence monitoring expectations should vary by assessment profile.

| Profile | Expected sequence monitoring depth |
|---|---|
| Lite | Basic awareness of whether the agent can initiate repeated or externally visible actions. |
| Standard | Ability to review related actions by user, agent, workflow, or tool session where operational risk exists. |
| High-Impact | Sequence-level review for threshold avoidance, staged execution, delegated subtasks, repeated attempts, and cumulative effects. |
| Audit-Grade | Strong correlation, retention, and reconstruction support for action sequences, including authorization, dispatch, execution, denial, override, and result events. |

Lite implementations may not need formal sequence monitoring if the agent cannot execute actions, call tools, or affect external systems.

High-Impact and Audit-Grade implementations should not rely only on isolated per-action review when cumulative effects may create material harm.

## Evidence Expectations

For action sequences, evidence should support reconstruction of:

- the initiating principal,
- the agent or workflow involved,
- the proposed actions,
- the order of actions,
- authorization decisions,
- dispatch events,
- execution results,
- denials or failed attempts,
- approvals or overrides,
- delegated subtasks,
- and the cumulative effect of the sequence.

Evidence does not need to prove intent by itself.

However, evidence should make it possible to review whether the sequence exceeded authority, bypassed thresholds, or produced a high-impact outcome.

## Relationship to Authorization

Action sequence monitoring does not replace action-level authorization.

Each high-impact action should still be authorized at the point of execution.

However, sequence-level review may determine that a later action requires stronger authorization because of earlier related actions.

For example:

- a fifth data export may require escalation because four related exports already occurred,
- a repeated infrastructure change may require review because earlier changes affected related controls,
- a delegated subtask may require review because it contributes to a high-impact objective,
- or a near-threshold financial action may require review because related transfers occurred in the same workflow.

## Relationship to Delegation

Delegation can make sequence-level risk harder to observe.

A root objective may be decomposed into subtasks across:

- agents,
- tools,
- workflows,
- systems,
- human approvers,
- or organizational domains.

Assessors should consider whether the implementation can trace delegated actions back to the original authority, principal, or objective.

If delegation breaks sequence visibility, the assessment should record a limitation or finding.

## Relationship to Evidence Quality Gate

Sequence-level evidence should be evaluated for quality.

For high-impact action sequences, assessors should consider whether the evidence is:

- action-bound,
- sequence-correlated,
- generated or corroborated by trusted components,
- protected against tampering or later modification,
- traceable across authorization, dispatch, execution, and result,
- and sufficient to reconstruct the cumulative effect.

Model-only summaries of a sequence should not be treated as sufficient evidence for high-impact or audit-grade assessment results.

## Non-Goals

This document does not:

- require a specific sequence identifier format,
- require immediate schema changes,
- require every low-risk repeated action to be escalated,
- define a fraud detection system,
- define behavioral analytics requirements,
- create a certification program,
- or require vendor-specific monitoring technology.

## Draft Status

This document is draft guidance for v0.3.0.

It is intended to support future work on evidence schema extensions, assessment worksheet updates, detection examples, and implementation patterns for sequence-level monitoring.
