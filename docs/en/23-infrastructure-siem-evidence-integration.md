# Infrastructure and SIEM Evidence Integration

This document provides draft guidance for integrating AAEF evidence with infrastructure logs, backend logs, IAM logs, cloud audit logs, and SIEM or security analytics systems.

AAEF Evidence Events describe agentic action governance, authorization, dispatch, execution, and review context.

However, AAEF evidence should not be treated as the only source of truth for real-world system effects.

For high-impact and audit-grade actions, AAEF evidence should be correlated with independently generated or corroborating records where feasible.

## Purpose

The purpose of infrastructure and SIEM evidence integration is to help assessors and implementers determine whether agentic action evidence can be connected to actual system behavior.

This is especially important when an agentic system can:

- modify production infrastructure,
- change access controls,
- move funds or trigger financial operations,
- disclose or transform sensitive data,
- invoke backend APIs,
- call administrative tools,
- create externally visible effects,
- or perform security-relevant operations.

AAEF Evidence Events can explain what the agentic system proposed, authorized, dispatched, and recorded.

Infrastructure, backend, IAM, and SIEM evidence can help corroborate what actually happened.

## Core Principle

AAEF evidence and infrastructure evidence serve different roles.

| Evidence source | Primary role |
|---|---|
| AAEF Evidence Event | Records the agentic action context, authorization, dispatch, execution result, and governance metadata. |
| Backend application log | Records application-level request handling and business or system effect. |
| IAM / identity log | Records identity, authentication, authorization, credential use, or role assumption. |
| Infrastructure audit log | Records platform, cloud, operating system, network, or administrative events. |
| SIEM / detection system | Correlates events, raises alerts, supports investigation, and preserves security analytics context. |
| Human review record | Records approvals, overrides, break-glass use, findings, and reviewer judgment. |

A schema-valid AAEF Evidence Event is not automatically proof that the external system effect occurred as claimed.

For high-impact actions, the assessment should consider whether the AAEF evidence can be correlated with independently generated or corroborating records.

## Evidence Correlation References

Implementations should preserve enough identifiers to correlate agentic action evidence with infrastructure and backend records.

Examples include:

- `action_id`,
- `authorization_decision_id`,
- `dispatch_id`,
- `execution_id`,
- `principal_id`,
- `agent_id`,
- `tool_id`,
- `workflow_id`,
- `sequence_id`,
- `delegation_chain_id`,
- `resource_id`,
- `request_id`,
- `trace_id`,
- `span_id`,
- `session_id`,
- `approval_request_id`,
- `policy_version`,
- `backend_transaction_id`,
- `cloud_audit_event_id`,
- `siem_correlation_id`,
- or incident / case reference.

AAEF does not require a specific correlation identifier format in v0.3.0.

However, implementations should be able to explain how evidence records can be linked during review or incident reconstruction.

## Common Integration Patterns

### Pattern 1: AAEF Evidence Event with Backend Corroboration

In this pattern, the AAEF Evidence Event records the proposed action, authorization decision, dispatch event, and execution result.

The backend system also records the actual system effect.

Examples include:

- a user permission change recorded in an identity system,
- a payment initiation recorded in a financial backend,
- a production configuration change recorded by an infrastructure control plane,
- a data export recorded by a data platform or application service.

Assessment focus:

- whether the backend record can be correlated to the AAEF action,
- whether the backend record was generated independently of the model,
- whether the backend effect matches the authorized action,
- and whether mismatches are detected or reviewable.

### Pattern 2: IAM or Workload Identity Correlation

In this pattern, infrastructure or IAM logs record which identity performed the action.

The identity may be:

- a user,
- a service account,
- a workload identity,
- an agent identity,
- a dispatch gateway identity,
- a backend service identity,
- or a temporary credential issued to a trusted enforcement component.

Assessment focus:

- whether high-impact credentials are unavailable to the Agent Runtime where required,
- whether credential use can be linked to an authorized action,
- whether role assumption or token issuance is logged,
- whether privilege use is consistent with the authorization decision,
- and whether direct bypass paths are visible.

### Pattern 3: SIEM Correlation and Detection

In this pattern, AAEF Evidence Events and related backend or infrastructure logs are sent to a SIEM, data lake, or security analytics system.

The SIEM may be used to:

- correlate authorization, dispatch, execution, and backend effect records,
- detect missing or inconsistent evidence chains,
- flag repeated near-threshold actions,
- detect task splitting or staged execution,
- identify high-impact actions without matching authorization,
- alert on direct backend access that bypasses the Tool Dispatch Enforcement Point,
- and support incident reconstruction.

Assessment focus:

- whether the SIEM receives sufficient fields for correlation,
- whether event timestamps and identifiers are reliable enough for reconstruction,
- whether missing evidence is detectable,
- whether high-impact actions can be searched and reviewed,
- and whether retention is appropriate for the action impact.

### Pattern 4: Infrastructure Audit Log as Corroborating Evidence

In this pattern, infrastructure audit logs provide corroborating evidence for the system effect.

Examples may include cloud control plane logs, operating system audit logs, network device logs, database audit logs, container platform logs, or CI/CD pipeline records.

Cloud provider audit logs, such as AWS CloudTrail, may be useful examples, but AAEF does not require a specific cloud provider or logging product.

Assessment focus:

- whether the infrastructure audit log is generated outside the model-controlled path,
- whether it records the relevant resource, identity, action, and timestamp,
- whether it can be linked to the AAEF action or dispatch record,
- whether it is protected against unauthorized modification,
- and whether retention supports investigation and review.

## Minimum Correlation Expectations

For high-impact and audit-grade actions, implementations should aim to correlate at least the following:

| AAEF concept | Corroborating record examples |
|---|---|
| Proposed action | Canonical action request, workflow record, ticket, approval request. |
| Authorization decision | Policy decision log, approval record, authorization artifact. |
| Dispatch event | Tool dispatch log, gateway log, backend request record. |
| Principal / actor | IAM log, session record, workload identity, service account, approval identity. |
| Tool or backend target | API log, tool invocation log, resource identifier, infrastructure audit log. |
| Execution result | Backend transaction, infrastructure state change, application event, error or denial record. |
| Evidence storage | Evidence pipeline log, SIEM ingestion record, immutable or tamper-evident storage reference. |

The exact fields may vary by implementation.

The key expectation is that assessors can reconstruct the chain from proposed action to actual effect where the action impact requires it.

## Evidence Quality Considerations

Infrastructure and SIEM integration can strengthen Evidence Quality Gate results when the evidence is:

- generated outside the model-controlled path,
- correlated to the specific action,
- tied to a stable principal or workload identity,
- traceable to authorization and dispatch,
- consistent with backend or infrastructure effects,
- protected against unauthorized modification,
- retained for an appropriate period,
- and understandable to reviewers.

However, infrastructure logs are not automatically sufficient.

Assessors should consider:

- whether logs are complete enough,
- whether identifiers are stable and meaningful,
- whether timestamps are reliable,
- whether logs can be altered by the same component being assessed,
- whether correlation depends on fragile string matching,
- whether sensitive data is over-collected,
- and whether the evidence actually supports the assessment result.

## Detecting Evidence Gaps

Infrastructure and SIEM integration should help identify gaps such as:

- backend effects without matching AAEF authorization,
- AAEF dispatch events without backend execution records,
- backend execution records that contradict AAEF result status,
- high-impact actions performed by unexpected identities,
- tool calls using broad credentials held by the Agent Runtime,
- missing approval records for high-impact actions,
- missing revocation or freeze checks,
- repeated near-threshold actions,
- and sequences of actions that produce cumulative high-impact effects.

These gaps may indicate findings, limitations, false positives, or integration issues.

A human reviewer may still need to determine the assessment significance.

## Incident Reconstruction

For high-impact incidents, evidence should support reconstruction of:

- who or what initiated the action,
- what the agent proposed,
- what authority or approval was used,
- what policy decision was made,
- what tool or backend was invoked,
- what credentials or identity were used,
- what system effect occurred,
- whether related actions formed a sequence,
- whether any denial, override, revocation, or break-glass event occurred,
- and what evidence was available at the time.

AAEF Evidence Events should help organize this reconstruction.

Infrastructure and SIEM evidence should help corroborate the actual system behavior.

## Relationship to Assessment Profiles

Infrastructure and SIEM evidence expectations should vary by profile.

| Profile | Integration expectation |
|---|---|
| Lite | Infrastructure correlation may be minimal where the agent cannot execute actions or affect external systems. |
| Standard | Basic backend, tool, or workflow log correlation is expected for production tool use. |
| High-Impact | Correlation across authorization, dispatch, backend effect, identity, and evidence records is expected where feasible. |
| Audit-Grade | Stronger independent or corroborating evidence, retention, tamper resistance, and incident reconstruction support are expected. |

Higher profiles should not rely only on agent runtime logs or model-generated explanations.

## Relationship to Action Sequence Monitoring

Infrastructure and SIEM integration can support action sequence monitoring.

SIEM or analytics systems may help correlate:

- repeated exports,
- repeated payments,
- repeated denied attempts,
- staged infrastructure changes,
- delegated subtasks,
- related workflow actions,
- and cumulative high-impact outcomes.

However, sequence detection should not be treated as purely mechanical.

A human reviewer may need to determine whether the sequence indicates legitimate activity, policy evasion, excessive agency, or misuse.

## Relationship to Assessment Automation and Human Review

Infrastructure and SIEM evidence integration is usually hybrid.

Automation can:

- ingest events,
- check required fields,
- correlate identifiers,
- flag missing links,
- detect suspicious sequences,
- and surface mismatches.

Human review is often required to determine:

- whether the evidence is sufficient,
- whether the action was authorized,
- whether the system effect matched the approved action,
- whether compensating controls are credible,
- and whether residual risk is acceptable.

## Data Minimization and Sensitive Evidence

Evidence integration should avoid unnecessary collection of sensitive content.

Implementations should consider:

- storing references instead of raw sensitive payloads,
- hashing or redacting sensitive values,
- separating evidence metadata from protected content,
- applying retention appropriate to the action impact,
- controlling access to evidence stores and SIEM views,
- and documenting evidence limitations.

For sensitive or regulated data, evidence should support review without becoming an avoidable data exposure risk.

## Non-Goals

This document does not:

- require a specific SIEM product,
- require a specific cloud provider,
- require AWS, CloudTrail, or any vendor-specific logging service,
- define a complete detection engineering program,
- require all logs to be centralized,
- define final schema fields for infrastructure correlation,
- replace incident response procedures,
- or create a certification program.

## Draft Status

This document is draft guidance for v0.3.0.

It is intended to support future evidence schema refinements, SIEM mapping examples, infrastructure integration examples, and audit-oriented assessment workflows.
