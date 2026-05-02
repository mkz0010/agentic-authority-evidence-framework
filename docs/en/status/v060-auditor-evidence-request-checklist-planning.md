# AAEF v0.6.0 Auditor Evidence Request Checklist Planning

Status: Auditor evidence request checklist planning  
Related roadmap: #241  
Related implementation reference: `docs/en/status/v060-implementation-reference-pattern-planning.md`  
Related permitted-action example: `docs/en/status/v060-permitted-action-evidence-example-planning.md`  
Related non-execution example: `docs/en/status/v060-non-execution-evidence-example-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document provides a non-normative planning checklist for evidence requests an auditor, assessor, reviewer, or consultant may use when evaluating an AAEF-style agentic action implementation.

The checklist translates the v0.6.0 implementation reference pattern and paired evidence examples into practical evidence-request categories.

This document is planning material. It does not create an audit standard, certification requirement, compliance requirement, conformity assessment, audit opinion, or implementation conformance profile.

## Intended users

This checklist is intended for:

- auditors,
- assessors,
- security reviewers,
- GRC reviewers,
- consultants,
- risk owners,
- incident responders,
- security architects,
- and implementers preparing evidence for review.

## Non-normative status

This document is not an active assessment artifact.

It does not update:

- active controls,
- active evidence schema,
- active assessment worksheet,
- active testing procedures,
- active examples,
- mappings,
- CSVs,
- or the current control and assessment baseline.

Any future promotion into active assessment artifacts must be handled through explicit review and PRs.

## Review objective

An evidence reviewer should be able to determine whether a sampled agentic action was:

1. requested in a structured way,
2. bound to an identifiable principal,
3. evaluated by an authorization decision process,
4. enforced at the dispatch or execution boundary,
5. verified by the backend relying party where applicable,
6. executed or not executed according to the authorization outcome,
7. evidenced with sufficient linkage,
8. reconstructable after the fact,
9. protected from obvious replay, scope expansion, or approval laundering,
10. and documented with evidence limitations.

## Evidence request package overview

A reviewer should request evidence in packages rather than isolated logs.

| Package | Purpose |
| --- | --- |
| Action request evidence | Shows what the agent attempted to do and on whose behalf. |
| Principal and authority evidence | Shows who or what had authority and under what scope. |
| Authorization decision evidence | Shows the explicit decision outside model output. |
| Approval evidence | Shows meaningful approval where required. |
| Dispatch enforcement evidence | Shows the execution boundary enforced the decision. |
| Backend verification evidence | Shows the backend did not rely solely on agent runtime claims. |
| Execution evidence | Shows whether the action actually occurred. |
| Non-execution evidence | Shows fail-closed, denied, held, frozen, or reauthorization outcomes. |
| Evidence integrity evidence | Shows how records are protected, retained, and correlated. |
| Reconstruction evidence | Shows that the action chain can be reconstructed. |
| Limitation evidence | Shows evidence trust assumptions and gaps. |

## Checklist summary

| Area | Evidence request | Reviewer question |
| --- | --- | --- |
| Action request | Structured action request record | What was requested? |
| Principal | Principal binding record | On whose behalf was the action requested? |
| Agent | Agent instance/session record | Which agent proposed the action? |
| Authorization | Authorization decision artifact | What authority permitted or denied the action? |
| Policy | Policy version and rule reference | Which policy was used? |
| Approval | Approval record and binding | Was approval meaningful and action-bound? |
| Dispatch | Dispatcher enforcement result | Was the decision enforced before execution? |
| Backend | Backend verification result | Did the backend independently verify authority? |
| Execution | Execution or non-execution result | Did the action occur? |
| Evidence | Evidence event record | Can the chain be reconstructed? |
| Integrity | Evidence storage and protection record | Can evidence be trusted? |
| Limitations | Evidence limitation statement | What assurance limits remain? |

## Action request evidence

Request:

- sampled action request records,
- request identifiers,
- requested action names,
- target resources,
- principal identifiers,
- agent instance identifiers,
- input source records,
- untrusted input indicators,
- impact classification,
- requested scope,
- requested time window,
- and request hash or canonical digest where available.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| What action was requested? | `action_request_id`, `requested_action` |
| What resource was affected? | `target_resource` |
| Who was the principal? | `principal_id` |
| Which agent proposed the action? | `agent_instance_id`, `session_id` |
| Was untrusted input present? | `input_sources`, `untrusted_input_present` |
| Was requested scope bounded? | `requested_scope`, `requested_time_window` |
| Can the request be uniquely identified? | request identifier and request hash |

Red flags:

- only free-text prompt logs are available,
- principal cannot be identified,
- action scope is ambiguous,
- no stable request identifier exists,
- untrusted input is not recorded,
- request records can be edited without trace.

## Principal and authority evidence

Request:

- principal directory records,
- role or group membership evidence,
- delegated authority records,
- session binding records,
- authority scope records,
- authority expiry records,
- and authority lineage records where delegation is involved.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| Who or what is the principal? | principal directory or identity record |
| What authority did the principal have? | role, policy, delegation, or approval record |
| Was authority time-bounded? | expiry or validity window |
| Was authority scope-bounded? | authorized action/resource/scope |
| Was delegation attenuated? | delegated scope narrower than source authority |
| Can authority lineage be reconstructed? | authority lineage or delegation chain |

Red flags:

- authority is inferred from a model response,
- broad role membership is used without action-specific constraints,
- delegation chain is missing,
- authority has no expiry,
- authority scope is wider than the action requires.

## Authorization decision evidence

Request:

- authorization decision artifacts,
- policy decision logs,
- policy version identifiers,
- decision timestamps,
- decision expiry,
- decision scope,
- trusted inputs used,
- untrusted inputs excluded,
- decision hash or signature where available,
- and deny / hold / require-approval outcomes.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| Was there an explicit authorization decision? | `authorization_decision_id` |
| Was the decision separate from model output? | policy service or authorization service record |
| What policy version was used? | `policy_version` |
| What did the decision permit or deny? | decision, action, resource, scope |
| Was the decision time-bounded? | `decision_time`, `expires_at` |
| Were trusted inputs identified? | `trusted_inputs_used` |
| Were untrusted inputs excluded from authority? | `untrusted_inputs_excluded` |
| Can the decision be bound to the request? | `action_request_id`, request hash, decision hash |

Red flags:

- model self-assessment is the only decision record,
- natural-language approval is the only authority source,
- decision scope is broader than requested scope,
- decision is reusable across unrelated requests,
- policy version is missing,
- expiry is missing.

## Approval evidence

Request:

- approval records,
- approver identity,
- approval time,
- approved action,
- approved resource,
- approved scope,
- approval reason,
- approval evidence reference,
- and linkage to authorization decision and action request.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| Was approval required? | policy or decision result |
| Who approved? | `approver_id` |
| What exactly was approved? | approved action/resource/scope |
| Was approval specific to the action? | action request and decision linkage |
| Was approval valid at execution time? | approval timestamp and expiry |
| Was approval reused? | reuse detection or decision binding |
| Was approval meaningful? | approver authority and sufficient context |

Red flags:

- generic "approved" text with no scope,
- approval is not bound to the action,
- approval is copied across actions,
- approver identity is missing,
- approval occurred after execution,
- broad approval is used for different resources.

## Dispatch enforcement evidence

Request:

- dispatcher logs,
- dispatch event records,
- tool gateway records,
- enforcement check results,
- request/decision binding checks,
- principal/action/resource/scope matching results,
- expiry checks,
- policy version checks,
- and allow / deny / hold results.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| Did dispatch occur only after authorization? | dispatch event linked to decision |
| Did the dispatcher validate the decision? | check results |
| Did requested action match authorized action? | action match check |
| Did requested resource match authorized resource? | resource match check |
| Did scope constraints match? | scope check |
| Did the dispatcher fail closed when checks failed? | denied or non-execution event |
| Was evidence required and generated? | evidence-required check and evidence event |

Red flags:

- dispatcher only logs tool calls after execution,
- dispatcher does not check authorization decisions,
- dispatcher trusts agent runtime assertions,
- failed checks still result in backend invocation,
- denial events are not recorded,
- request and decision cannot be correlated.

## Backend relying-party verification evidence

Request:

- backend verification records,
- authorization introspection logs,
- signed decision validation logs where applicable,
- backend policy lookup logs,
- mTLS or internal service identity evidence where applicable,
- replay protection checks,
- and backend execution / rejection result.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| Did the backend independently verify authority? | backend verification record |
| Did the backend verify decision identity? | decision ID or token introspection |
| Did it verify action and resource scope? | verified fields |
| Did it verify expiry and policy version? | expiry and policy checks |
| Did it prevent replay? | nonce, request hash, or one-time decision binding |
| Did it reject mismatches? | backend denial record |
| Did execution occur only after verification? | verification timestamp before execution timestamp |

Red flags:

- backend trusts only a header set by the agent runtime,
- backend has no authorization verification record,
- backend accepts broad runtime credentials,
- backend cannot link execution to decision,
- backend verification occurs after execution,
- replay protection is absent for high-impact actions.

## Execution evidence

Request:

- backend execution logs,
- target system event logs,
- execution reference identifiers,
- resource change logs,
- timestamps,
- action result,
- actor/service identity,
- and correlation to action request, decision, dispatch, and backend verification records.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| Did the action occur? | execution result and backend event |
| What resource changed? | target system event |
| When did it occur? | execution timestamp |
| Which backend performed it? | backend ID |
| Can execution be linked to authorization? | decision ID and request ID |
| Was execution within scope? | resource/action/scope comparison |
| Is evidence complete enough for reconstruction? | correlated evidence event |

Red flags:

- execution logs are not correlated to authorization,
- resource changes have no request linkage,
- action result is only reported by the agent,
- execution timestamp predates authorization,
- target system logs contradict evidence event.

## Non-execution evidence

Request:

- denied dispatch records,
- hold / freeze records,
- expired decision records,
- missing approval records,
- backend rejection records,
- evidence-required-unavailable records,
- non-execution evidence events,
- and non-invocation records for the backend.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| Was the action not executed? | non-execution event |
| Why was it not executed? | non-execution reason |
| Which boundary rejected it? | dispatcher or backend record |
| Was the backend invoked? | backend invocation flag |
| Was this a fail-closed outcome? | denial before execution |
| Was the attempted action out of scope? | expected vs requested scope |
| Can the rejected action be reconstructed? | linked request/decision/dispatch/evidence records |

Red flags:

- rejected tool calls are not logged,
- backend was invoked despite dispatch denial,
- non-execution reason is missing,
- failed checks are overwritten by later success logs,
- no evidence exists for denied high-impact actions.

## Evidence integrity and storage evidence

Request:

- evidence storage design,
- retention policy,
- access control records,
- immutability or tamper-evidence controls where available,
- evidence writer identity,
- evidence writer placement,
- time source or timestamping mechanism,
- evidence correlation identifiers,
- and evidence deletion or modification logs.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| Where is evidence stored? | evidence store design or configuration |
| Who can write evidence? | evidence writer identity and access control |
| Who can modify or delete evidence? | access policy and audit logs |
| Is evidence protected from tampering? | immutability, signatures, append-only logs, or compensating controls |
| Is evidence retained long enough? | retention policy |
| Is timestamping reliable? | time source or synchronization evidence |
| Are limitations documented? | evidence trust limitations |

Red flags:

- evidence writer runs entirely inside the model-controlled path,
- evidence can be edited by the agent runtime,
- evidence retention is undefined,
- evidence store lacks access controls,
- timestamps are unreliable,
- evidence integrity limitations are not recorded.

## Reconstruction evidence

Request:

- sample reconstruction records,
- correlation queries,
- evidence bundle exports,
- incident review records,
- action request to evidence trace,
- decision to execution trace,
- and non-execution reconstruction examples.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| Can the full chain be reconstructed? | request, decision, dispatch, backend, evidence chain |
| Can reviewers identify the principal? | principal binding across records |
| Can reviewers identify the agent? | agent instance/session records |
| Can reviewers distinguish execution from non-execution? | outcome and non-execution reason |
| Can reviewers identify evidence limitations? | limitation fields or notes |
| Can reviewers detect mismatches? | request/decision/dispatch/backend comparison |

Red flags:

- evidence exists but cannot be correlated,
- identifiers differ across systems,
- reconstruction requires manual guesswork,
- missing evidence is not recorded,
- limitations are absent.

## Evidence limitation request

Request:

- evidence limitation statements,
- known trust boundary limitations,
- evidence writer placement notes,
- reliance on agent runtime logs,
- backend verification limitations,
- known missing evidence,
- and compensating controls.

Reviewer questions:

| Question | Expected evidence |
| --- | --- |
| What does the evidence prove? | explicit evidence purpose |
| What does it not prove? | limitation statement |
| Is the evidence self-referential? | evidence writer placement |
| Is backend verification independent? | backend verification architecture |
| Are there missing links? | known evidence gaps |
| Are compensating controls documented? | compensating control notes |

Red flags:

- no limitation statement exists,
- evidence is treated as self-proving,
- agent runtime logs are treated as authoritative,
- backend verification limitations are hidden,
- missing evidence is ignored.

## Sample request list for a permitted action

For a sampled permitted action, request:

1. structured action request,
2. principal and authority record,
3. authorization decision artifact,
4. approval record where applicable,
5. dispatcher enforcement result,
6. backend verification result,
7. backend execution result,
8. evidence event,
9. evidence storage record,
10. reconstruction trace,
11. evidence limitation statement.

## Sample request list for a non-executed action

For a sampled non-executed action, request:

1. structured action request,
2. available or missing authorization decision record,
3. dispatcher denial / hold / freeze record,
4. backend non-invocation or backend rejection record,
5. non-execution evidence event,
6. non-execution reason,
7. expected vs requested scope comparison,
8. evidence storage record,
9. reconstruction trace,
10. evidence limitation statement.

## Sampling guidance

Reviewers may sample:

- high-impact permitted actions,
- high-impact denied actions,
- actions requiring human approval,
- actions influenced by untrusted input,
- actions involving delegated authority,
- actions involving backend verification,
- failed or frozen actions,
- and actions with evidence limitations.

Sampling should include both successful execution and non-execution outcomes.

## Reviewer judgment guidance

This checklist helps reviewers ask for evidence.

It does not determine pass/fail by itself.

A reviewer should consider:

- completeness,
- correlation,
- independence,
- scope binding,
- timeliness,
- tamper resistance,
- limitation disclosure,
- and reconstruction quality.

## Consultant use

A consultant may use this checklist to prepare client discovery questions.

Examples:

- Which agentic actions are high-impact?
- Where are action requests recorded?
- Where are authorization decisions made?
- How are decisions bound to requests?
- Where is dispatch enforcement performed?
- Does the backend verify authority independently?
- What evidence is stored?
- Can denied actions be reconstructed?
- What evidence limitations remain?

## Operator use

An operator may use this checklist to prepare:

- monitoring requirements,
- alerting requirements,
- retention requirements,
- denied-action review workflows,
- freeze/hold procedures,
- escalation procedures,
- and evidence export processes.

## Manager / risk owner use

A manager or risk owner may use this checklist to understand:

- what evidence exists for high-impact actions,
- which actions are enforceable,
- where residual risk remains,
- which gaps require remediation,
- and whether evidence supports risk acceptance.

## Claim boundaries

This checklist does not claim:

- certification,
- compliance,
- audit sufficiency,
- conformity,
- equivalence with external frameworks,
- production readiness,
- or complete mitigation.

It may support:

- planning,
- evidence request preparation,
- implementation review,
- assessment discussion,
- consultant discovery,
- incident reconstruction,
- and risk decision support.

## Relationship to active artifacts

This document does not update active assessment procedures.

A future PR may choose to convert selected checklist items into an active assessment checklist or worksheet. That would require explicit review.

## Non-goals

This document does not:

- change active controls,
- change the current control and assessment baseline,
- update schemas, examples, mappings, CSVs, or testing procedures,
- promote v0.5.0 or v0.6.0 planning material into active requirements,
- assert audit sufficiency,
- claim compliance,
- claim certification,
- claim conformity,
- claim equivalence with external frameworks,
- or assert production readiness.

## Acceptance criteria

This planning checklist is sufficient when:

- evidence request packages are defined,
- permitted-action and non-execution evidence requests are included,
- reviewer questions are documented,
- red flags are identified,
- evidence limitations are requested,
- sampling guidance is provided,
- persona-specific use is described,
- claim boundaries are preserved,
- and no active baseline change is implied.
