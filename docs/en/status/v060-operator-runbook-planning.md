# AAEF v0.6.0 Operator Runbook Planning

Status: Operator runbook planning  
Related roadmap: #241  
Related adoption index: `docs/en/status/v060-adoption-package-index-planning.md`  
Related implementation reference: `docs/en/status/v060-implementation-reference-pattern-planning.md`  
Related auditor checklist: `docs/en/status/v060-auditor-evidence-request-checklist-planning.md`  
Related consultant checklist: `docs/en/status/v060-consultant-discovery-checklist-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document provides a non-normative operator runbook planning guide for day-to-day operation of an AAEF-style agentic action assurance environment.

The purpose is to translate AAEF adoption materials into operational routines that help operators, administrators, incident responders, security operations teams, engineering teams, consultants, auditors, and risk owners understand who monitors what, when to intervene, how to preserve evidence, and when to escalate.

This document is planning material. It does not create an operational requirement, audit standard, certification requirement, compliance requirement, conformity assessment, audit opinion, or implementation conformance profile.

## Intended users

This runbook planning guide is intended for:

- agent platform operators,
- tool gateway administrators,
- backend service owners,
- security operations teams,
- incident responders,
- evidence store administrators,
- engineering managers,
- risk owners,
- consultants preparing operational handoff,
- and auditors reviewing operational readiness.

## Non-normative status

This document is not an active runbook requirement.

It does not update:

- active controls,
- active evidence schema,
- active assessment worksheet,
- active testing procedures,
- active examples,
- mappings,
- CSVs,
- or the current control and assessment baseline.

Any future promotion into active operational guidance must be handled through explicit review and PRs.

## Operating objective

An AAEF-style operating model should help an organization answer:

1. Which agentic actions are currently enabled?
2. Which high-impact actions require approval, reauthorization, or fail-closed behavior?
3. Which denied, held, frozen, or failed actions require review?
4. Which evidence gaps require operational response?
5. Who can freeze or resume agentic execution?
6. Who owns authorization policy changes?
7. Who owns evidence retention and export?
8. Who reviews backend verification failures?
9. Who decides whether residual risk is acceptable?
10. Can the organization reconstruct recent permitted and non-executed actions?

## Operating roles

| Role | Responsibilities |
| --- | --- |
| Agent system owner | Owns the agentic system, action inventory, and business purpose. |
| Agent platform operator | Operates agent runtime and agent configuration. |
| Tool gateway / dispatcher owner | Operates dispatch enforcement, tool access, and deny/hold behavior. |
| Authorization policy owner | Owns policies, policy versions, decision behavior, and approval rules. |
| Backend relying-party owner | Owns backend verification and execution behavior. |
| Evidence owner | Owns evidence writer, evidence store, retention, access, and export. |
| Security operations | Monitors alerts, anomalies, denied actions, and incident signals. |
| Incident responder | Coordinates response, reconstruction, containment, and lessons learned. |
| Change approver | Approves bounded high-impact actions where required. |
| Risk owner | Accepts, rejects, or escalates residual risk. |
| Consultant / advisor | Helps scope operational gaps, pilot readiness, and remediation. |
| Auditor / assessor | Requests evidence and reviews operational records where applicable. |

## Operating cadence

| Cadence | Activity |
| --- | --- |
| Daily | Review high-impact executions, denied actions, evidence failures, and freeze/hold events. |
| Weekly | Review action inventory changes, policy changes, approval exceptions, and evidence gaps. |
| Monthly | Review metrics, retention, access, sampling, reconstruction tests, and risk-owner reporting. |
| Event-driven | Respond to backend verification failures, evidence gaps, high-risk denials, scope mismatches, incidents, or emergency changes. |
| Release/change-driven | Review action enablement, policy versions, dispatcher changes, backend verification changes, and evidence schema/field changes. |

## Daily operator checklist

Daily review should include:

- high-impact permitted actions executed in the last review window,
- high-impact denied or non-executed actions,
- actions requiring approval,
- actions executed under exception or break-glass paths,
- failed dispatch checks,
- backend verification failures,
- missing evidence events,
- evidence writer failures,
- evidence store write failures,
- expired authorization decisions used or attempted,
- unusual increases in denied actions,
- unusual increases in untrusted-input-influenced actions,
- frozen or held actions,
- and unresolved incidents involving agentic actions.

Suggested daily questions:

| Question | Expected operational evidence |
| --- | --- |
| Were any high-impact actions executed? | execution evidence and action list |
| Were any high-impact actions denied? | non-execution evidence |
| Did any action execute without required evidence? | evidence-required check and gap record |
| Did any backend verification fail? | backend verification failure record |
| Did any dispatcher check fail? | dispatch denial / hold records |
| Were any actions frozen or held? | freeze/hold record |
| Were any approvals reused or ambiguous? | approval linkage and review notes |
| Are there open operational exceptions? | exception register |
| Are evidence limitations recorded? | limitation statements |

## Weekly operator checklist

Weekly review should include:

- newly enabled agentic actions,
- newly disabled agentic actions,
- changes to tool permissions,
- changes to dispatcher rules,
- changes to backend verification behavior,
- changes to authorization policy versions,
- approval workflow changes,
- evidence retention issues,
- access changes to evidence stores,
- unresolved evidence gaps,
- repeated denial patterns,
- repeated approval exceptions,
- open risk-owner decisions,
- and consultant/auditor follow-up items.

Suggested weekly questions:

| Question | Expected operational evidence |
| --- | --- |
| Did the action inventory change? | change record and action inventory |
| Did any policy version change? | policy change record |
| Did dispatcher behavior change? | gateway config change record |
| Did backend verification change? | backend change record |
| Did evidence writer/store access change? | access review record |
| Are denied-action patterns increasing? | trend report |
| Are any gaps recurring? | gap register |
| Are risk-owner decisions pending? | risk decision tracker |

## Monthly operator checklist

Monthly review should include:

- sampling of permitted high-impact actions,
- sampling of non-executed high-impact actions,
- reconstruction exercise results,
- evidence retention status,
- evidence access review,
- action inventory review,
- stale authority and delegation review,
- policy version review,
- approval quality review,
- denied-action trend review,
- freeze/hold readiness review,
- incident response readiness review,
- and risk-owner reporting.

Suggested monthly questions:

| Question | Expected operational evidence |
| --- | --- |
| Can sampled actions be reconstructed? | reconstruction trace |
| Are evidence records retained as expected? | retention report |
| Are evidence access rights appropriate? | access review |
| Are old decisions or delegated authority still active? | expiry / revocation report |
| Are approvals meaningful and action-bound? | approval quality review |
| Are non-execution events visible? | denied/held/frozen event sample |
| Are metrics reviewed by owners? | monthly metrics report |
| Are risk decisions current? | risk-owner review record |

## Event-driven procedures

### Procedure: high-impact permitted action review

Trigger:

- high-impact action executed,
- action executed under approval,
- action executed under delegated authority,
- action executed after reauthorization,
- or action executed with evidence limitations.

Review:

1. Confirm action request exists.
2. Confirm principal binding exists.
3. Confirm authorization decision exists.
4. Confirm decision was valid at execution time.
5. Confirm dispatcher enforcement passed.
6. Confirm backend verification passed.
7. Confirm evidence event exists.
8. Confirm evidence limitations are recorded.
9. Escalate if evidence is incomplete or inconsistent.

### Procedure: denied or non-executed action review

Trigger:

- dispatch denied,
- backend rejected,
- action held,
- action frozen,
- approval missing,
- authorization expired,
- scope mismatch,
- evidence-required-unavailable event.

Review:

1. Confirm action request exists.
2. Confirm denial or hold reason.
3. Confirm failed boundary.
4. Confirm backend was not invoked if dispatch failed.
5. Confirm non-execution evidence exists.
6. Confirm no later execution bypassed the denial.
7. Determine whether escalation, reauthorization, remediation, or risk-owner review is needed.

### Procedure: backend verification failure

Trigger:

- backend rejects authorization,
- backend cannot verify decision,
- backend detects mismatch,
- replay protection fails,
- policy version unacceptable,
- or backend verification record is missing.

Review:

1. Confirm whether execution occurred.
2. Confirm whether failure happened before execution.
3. Compare request, decision, dispatch, and backend records.
4. Identify whether failure indicates policy drift, malformed decision, replay attempt, backend misconfiguration, or integration failure.
5. Escalate to backend owner and security operations.
6. Record evidence limitation or incident if needed.

### Procedure: missing evidence event

Trigger:

- evidence-required check passes but no evidence event exists,
- evidence writer fails,
- evidence store write fails,
- event cannot be correlated,
- or evidence export is incomplete.

Review:

1. Identify affected action.
2. Determine whether action executed.
3. Determine whether evidence is missing, delayed, corrupted, or inaccessible.
4. Freeze or hold affected high-impact action class if evidence is required and unavailable.
5. Escalate to evidence owner.
6. Record limitation and remediation.
7. Notify risk owner where residual risk changes.

### Procedure: freeze or hold agentic execution

Trigger:

- repeated denied high-impact actions,
- evidence generation failure,
- backend verification failure,
- suspected prompt injection leading to action attempts,
- authorization policy error,
- approval laundering concern,
- evidence tampering concern,
- incident response containment.

Review:

1. Identify action class, agent, tool, backend, or principal scope to freeze.
2. Apply freeze or hold at the dispatcher or backend boundary.
3. Record freeze reason, owner, timestamp, and scope.
4. Notify system owner, security operations, and risk owner.
5. Define conditions for resumption.
6. Review pending actions before resuming.
7. Record resumption decision and evidence.

## Operational alert candidates

| Alert | Meaning | Suggested owner |
| --- | --- | --- |
| High-impact action executed | A high-impact action occurred and should be reviewed. | Operator / risk owner |
| High-impact action denied | Boundary enforcement prevented a high-impact action. | Operator / security operations |
| Dispatch check failed | Dispatcher rejected action due to mismatch or missing decision. | Tool gateway owner |
| Backend verification failed | Backend could not verify authority. | Backend owner |
| Evidence writer failed | Required evidence could not be generated. | Evidence owner |
| Evidence store write failed | Evidence could not be persisted. | Evidence owner |
| Expired decision attempted | Old decision was reused or attempted. | Authorization owner |
| Scope mismatch detected | Requested action/resource exceeded authorization. | Tool gateway owner |
| Approval reuse detected | Approval may have been reused beyond scope. | Authorization owner / risk owner |
| Agent bypass path used | Action may have bypassed dispatcher. | Security operations |
| Freeze/hold activated | Execution was suspended. | Operator / risk owner |
| Evidence access anomaly | Evidence was accessed or modified unexpectedly. | Evidence owner / security operations |

## Operational metrics

Candidate metrics:

| Metric | Purpose |
| --- | --- |
| Number of enabled agentic actions | Understand operating scope. |
| Number of high-impact actions | Understand high-risk scope. |
| High-impact executions per period | Monitor sensitive execution volume. |
| High-impact denials per period | Monitor attempted boundary violations or policy friction. |
| Backend verification failure rate | Detect integration or authority problems. |
| Evidence generation failure rate | Detect assurance degradation. |
| Non-execution evidence coverage | Confirm fail-closed visibility. |
| Reconstruction success rate | Measure evidence usability. |
| Mean time to reconstruct | Measure review readiness. |
| Number of open evidence gaps | Track operational debt. |
| Number of active exceptions | Track accepted deviations. |
| Number of stale delegations | Track authority hygiene. |
| Number of freeze/hold events | Track containment activity. |

Metrics should be used for operational awareness, not as certification or compliance proof.

## Evidence retention and access operations

Operators should define:

- evidence retention period,
- evidence storage location,
- evidence export process,
- evidence access roles,
- evidence deletion process,
- legal hold interaction,
- privacy/data-minimization expectations,
- evidence integrity controls,
- and evidence limitation documentation.

Operational questions:

- Who can write evidence?
- Who can read evidence?
- Who can export evidence?
- Who can delete evidence?
- Are deletion events logged?
- Are evidence access events logged?
- Is evidence retained long enough for review?
- Is evidence over-retained relative to privacy obligations?

## Escalation matrix

| Trigger | First owner | Escalate to |
| --- | --- | --- |
| Missing authorization decision | Authorization owner | Security architect / risk owner |
| Dispatch denial spike | Tool gateway owner | Security operations |
| Backend verification failure | Backend owner | Security operations / risk owner |
| Missing evidence | Evidence owner | Risk owner |
| Evidence integrity concern | Evidence owner | Security operations / incident response |
| High-impact action executed outside scope | Security operations | Incident response / risk owner |
| Approval laundering concern | Authorization owner | Risk owner / compliance reviewer |
| Agent bypass path detected | Security operations | Incident response |
| Claim-boundary concern | Legal/compliance reviewer | Project owner / risk owner |
| Production incident | Incident responder | Risk owner / executive owner |

## Operational records

A minimal operational record for an event-driven review may include:

| Field | Purpose |
| --- | --- |
| `review_record_id` | Unique operational review identifier. |
| `review_type` | Daily, weekly, monthly, event-driven, incident, or exception. |
| `action_request_id` | Linked action request. |
| `authorization_decision_id` | Linked decision. |
| `dispatch_event_id` | Linked dispatch event. |
| `backend_verification_id` | Linked backend verification. |
| `evidence_event_id` | Linked evidence event. |
| `owner` | Operational owner. |
| `reviewer` | Person/team performing review. |
| `outcome` | No issue, gap, escalation, incident, exception, freeze, remediation. |
| `limitations` | Known evidence or assurance limitations. |
| `next_action` | Follow-up action. |
| `risk_owner_notified` | Whether risk owner was notified. |
| `closed_at` | Closure timestamp. |

This is an illustrative planning shape, not an active schema.

## Operator handoff checklist

Before moving from pilot to ongoing operation, confirm:

- action inventory exists,
- high-impact actions are identified,
- owners are assigned,
- authorization policies are versioned,
- dispatcher checks are documented,
- backend verification is documented,
- evidence writer and store are owned,
- denied-action review process exists,
- freeze/hold process exists,
- evidence gap process exists,
- reconstruction process is tested,
- risk-owner escalation path exists,
- claim boundaries are documented.

## Relationship to auditor checklist

The operator runbook helps produce and maintain the evidence that auditors or reviewers may request.

The auditor evidence request checklist asks:

> What evidence should be requested and reviewed?

The operator runbook asks:

> Who produces, monitors, preserves, reviews, and escalates that evidence day to day?

## Relationship to consultant checklist

The consultant discovery checklist helps determine whether an organization is ready for operational adoption.

The operator runbook planning guide helps define what the organization should operate after discovery or pilot planning.

## Relationship to adoption package index

The adoption package index identifies the operator package as an adoption area with follow-up need.

This document fills that follow-up need at the planning level.

## Claim boundaries

This runbook planning guide does not claim:

- certification,
- compliance,
- audit sufficiency,
- conformity,
- equivalence with external frameworks,
- production readiness,
- implementation conformance,
- operational maturity,
- or complete mitigation.

It may support:

- operational planning,
- monitoring design,
- incident response planning,
- evidence handling,
- consultant discovery,
- auditor preparation,
- risk-owner decision support,
- and public review.

## Non-goals

This document does not:

- change active controls,
- change the current control and assessment baseline,
- update schemas, examples, mappings, CSVs, or testing procedures,
- promote v0.5.0 or v0.6.0 planning material into active requirements,
- define product-specific monitoring rules,
- define SIEM-specific queries,
- define binding incident response requirements,
- assert audit sufficiency,
- claim compliance,
- claim certification,
- claim conformity,
- claim equivalence with external frameworks,
- or assert production readiness.

## Acceptance criteria

This planning guide is sufficient when:

- operating roles are identified,
- daily, weekly, monthly, and event-driven routines are described,
- permitted-action and non-execution review procedures are included,
- backend verification failure and missing evidence procedures are included,
- freeze/hold behavior is described,
- alert candidates and metrics are listed,
- evidence retention and access operations are identified,
- escalation paths are described,
- relationship to auditor, consultant, and adoption index artifacts is explained,
- claim boundaries are preserved,
- and no active baseline change is implied.
