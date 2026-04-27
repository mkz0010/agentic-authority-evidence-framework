# Assessment Profiles and Tiered Applicability

This document defines draft assessment profiles for applying AAEF controls with different levels of depth.

Assessment profiles are intended to help implementers and assessors decide how deeply AAEF should be applied to a given agentic system, action class, or deployment context.

They do not replace the Control Catalog.

They also do not change whether a control exists. Instead, they describe how control applicability, evidence expectations, and assessment depth may vary based on action risk and agent autonomy.

## Purpose

AAEF is not intended to require the same assessment depth for every agent, every action, or every organization.

A low-risk assistant that drafts text should not require the same evidence depth as an autonomous agent that can move funds, change production infrastructure, disclose sensitive data, or execute externally visible actions.

Assessment profiles provide a structured way to distinguish these cases.

The primary drivers for profile selection are:

- action risk,
- agent autonomy,
- external system impact,
- data sensitivity,
- reversibility of the action,
- human review and approval depth,
- and the degree to which the action may affect safety, security, compliance, finance, privacy, or operational continuity.

Organization size alone should not determine the profile.

A small organization running a high-impact autonomous agent may require stronger controls than a large organization running a low-risk internal drafting assistant.

## Profile Overview

AAEF defines the following draft assessment profiles.

| Profile | Intended use | Typical evidence expectation |
|---|---|---|
| Lite | Low-risk, low-autonomy agentic use cases with limited external impact. | Basic documentation and lightweight evidence that controls are understood and applied where relevant. |
| Standard | Common production agentic systems with bounded tool use, moderate autonomy, or meaningful business impact. | Consistent control implementation evidence, authorization records, tool dispatch records, and reviewable evidence events. |
| High-Impact | Agentic actions involving sensitive data, financial effects, infrastructure changes, security-relevant operations, or other high-impact action classes. | Action-bound evidence, trusted enforcement records, authorization evidence, dispatch and execution correlation, and evidence quality review. |
| Audit-Grade | Systems requiring strong independent assurance, regulated review, incident reconstruction, or formal audit support. | Independently generated or corroborated evidence, tamper-evident records, traceable authorization and execution artifacts, and stronger evidence retention and review procedures. |

These profiles are draft guidance for assessment planning.

A future profile mapping may define how individual controls are assessed under each profile without changing the Control Catalog itself.

## Lite Profile

The Lite profile is intended for low-risk systems where the agent has little or no ability to directly cause external effects.

Examples may include:

- summarization assistants,
- drafting assistants,
- internal knowledge retrieval assistants,
- recommendation assistants without direct execution authority,
- agents whose outputs are always reviewed and manually executed by a human.

Lite does not mean no governance.

Even under Lite, implementers should be able to explain:

- what the agent can and cannot do,
- what tools or data sources it can access,
- whether any user, system, or third-party inputs may influence outputs,
- whether the agent can trigger actions directly,
- and what human review or operational checks exist before meaningful action is taken.

Lite is generally not appropriate for high-impact agentic actions.

## Standard Profile

The Standard profile is intended for production systems where agentic behavior is meaningful but bounded.

Examples may include:

- agents that prepare operational changes for human approval,
- agents that call internal APIs with limited privileges,
- agents that update non-critical records,
- agents that perform workflow automation with constrained business impact,
- agents that use tools but remain within clearly defined authorization boundaries.

Under Standard, assessment should focus on whether:

- authority boundaries are documented,
- tool use is mediated by enforceable controls,
- authorization decisions are recorded,
- evidence events are generated consistently,
- users and reviewers can understand what action was proposed or taken,
- and failures, denials, or non-execution events can be reviewed.

Standard should not be used to downscope high-impact actions solely because the organization is small or the system is early-stage.

## High-Impact Profile

The High-Impact profile is intended for actions where incorrect, unauthorized, or manipulated execution could produce material harm.

Examples may include actions that affect:

- financial movement or payment execution,
- production infrastructure or security configuration,
- access control or identity privileges,
- sensitive or regulated data,
- legal, compliance, or contractual commitments,
- safety-critical or operationally critical systems,
- irreversible or difficult-to-reverse external effects.

Under High-Impact, assessment should require more than structurally valid logs.

Evidence should be action-bound, correlated across authorization and execution, and strong enough to support reconstruction of:

- the proposed action,
- the authorization decision,
- the enforcement point,
- the dispatch event,
- the execution result,
- relevant human approvals or overrides,
- and any denial, revocation, or non-execution outcome.

Model-only explanations, agent runtime self-reports, or uncorroborated implementation logs should not be treated as sufficient evidence for a strong Pass result.

## Audit-Grade Profile

The Audit-Grade profile is intended for systems that require stronger independent assurance.

This may include systems subject to formal audit, regulated review, external assurance, post-incident reconstruction, or high-confidence internal governance.

Audit-Grade does not mean AAEF is a certification scheme.

It means the implementation and assessment should support stronger evidence quality expectations, such as:

- independently generated or corroborated evidence,
- tamper-evident evidence storage,
- traceability between policy, authorization, dispatch, execution, and result,
- retention procedures appropriate to the action impact,
- separation between model output and trusted enforcement,
- and review procedures that can be understood by assessors who were not involved in the original implementation.

Audit-Grade assessment should pay particular attention to whether evidence is generated by trusted enforcement, policy, backend, infrastructure, SIEM, or evidence pipeline components rather than by the model itself.

## Profile Selection Guidance

Profile selection should be based on the highest-impact action that the agentic system can initiate, recommend, authorize, dispatch, or materially influence.

Assessors should consider:

| Question | Assessment implication |
|---|---|
| Can the agent directly execute an external action? | Higher autonomy may require Standard or above. |
| Can the action affect money, infrastructure, access, sensitive data, safety, or compliance? | High-Impact or Audit-Grade may be appropriate. |
| Can a human meaningfully review the action before execution? | Strong human review may reduce autonomy risk, but does not eliminate evidence requirements. |
| Is the action reversible? | Irreversible or difficult-to-reverse actions may require stronger profiles. |
| Is the evidence generated by trusted components or only by the model/runtime? | Weak assertion sources may limit the achievable assessment result. |
| Would incident reconstruction be required after failure or misuse? | Audit-Grade evidence expectations may be appropriate. |

When multiple profiles could apply, assessors should select the stronger profile for the relevant action class.

A system may use different profiles for different action classes.

For example, the same agent may be assessed as:

- Lite for drafting internal summaries,
- Standard for updating low-risk workflow records,
- High-Impact for modifying access permissions,
- and Audit-Grade for actions requiring formal auditability or regulated evidence retention.

## Relationship to the Control Catalog

Assessment profiles do not modify the Control Catalog.

The Control Catalog remains the source of truth for AAEF controls.

Profiles should be treated as assessment planning guidance until a separate profile mapping is defined.

A future sidecar mapping may specify how each control is expected to apply under each profile.

That mapping should be maintained separately from the Control Catalog so that:

- control definitions remain stable,
- profile applicability can evolve independently,
- assessment tooling can use profile-specific views,
- and implementers can adopt profiles without changing the control source of truth.

## Draft Profile Mapping

The draft sidecar mapping is maintained at:

- `assessment/aaef-assessment-profiles-v0.3-draft.csv`

This mapping provides draft applicability guidance for each control across the following profiles:

- Lite
- Standard
- High-Impact
- Audit-Grade

The mapping is assessment guidance, not a change to the Control Catalog.

The Control Catalog remains the control source of truth. The sidecar mapping provides a profile-specific assessment view that can evolve independently.

## Relationship to Evidence Quality Gate

Assessment profiles and Evidence Quality Gate results are related but distinct.

The profile describes the expected depth of assessment.

The Evidence Quality Gate evaluates whether the available evidence is strong enough to support the assessment result for a specific action and risk level.

For high-impact and audit-grade assessments, evidence quality should consider:

- whether evidence is action-bound,
- whether evidence was independently generated or corroborated,
- whether evidence is protected against tampering or later modification,
- whether evidence can be correlated to authorization, dispatch, execution, and result,
- and whether the assertion source is strong enough for the claimed assurance level.

A schema-valid evidence event is not automatically meaningful assurance evidence.

## Non-Goals

This document does not:

- define a certification program,
- create organization-size based tiers,
- replace the Control Catalog,
- define final control-by-profile applicability,
- require every implementation to adopt every profile,
- or define vendor-specific implementation requirements.

## Draft Status

These assessment profiles are draft guidance for v0.3.0 planning and implementation.

They are expected to be refined through implementation feedback, assessment examples, and future profile mapping work.
