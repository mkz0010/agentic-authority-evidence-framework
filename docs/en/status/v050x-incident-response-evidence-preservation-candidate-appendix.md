# v0.5.x Incident-Response Evidence Preservation Candidate Appendix

**Status:** Temporary, non-normative candidate appendix

## Purpose

This appendix expands the incident-response evidence preservation guidance proposal into concrete preservation candidates, incident scenarios, evidence packages, and review expectations.

It follows:

- `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md`
- `docs/en/status/v050x-evidence-integrity-negative-tests-track-proposal.md`
- `docs/en/status/v050x-evidence-integrity-negative-tests-candidate-appendix.md`
- `docs/en/status/v050x-evidence-integrity-negative-tests-csv-refinement-proposal.md`
- `docs/en/status/v050x-follow-up-status.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Primary source issue:

- #165 — evidence integrity and tamper-evident evidence

Related active row:

- `AAEF-EVD-04`

This appendix does not update active testing procedures.

It does not update the Evidence Event Schema.

It does not add evidence examples.

It does not add validator fixtures.

It does not close #165 by itself.

## Executive Summary

Agentic AI incidents often become difficult to investigate when evidence is overwritten, normalized too early, summarized by the model, or retained only inside the agent runtime.

This appendix proposes concrete preservation candidates for incident-response scenarios involving high-impact agentic actions.

The core preservation principle is:

> Preserve the evidence chain that proves what was authorized, what was approved, what was dispatched, what was executed, what was blocked, and what evidence limitations remain.

The purpose is not to require one storage mechanism for every implementation.

The purpose is to make sure incident responders can reconstruct the action story without relying on model output as authority.

## Preservation Objectives

Incident-response evidence preservation should support the following objectives:

| Objective | Explanation |
| --- | --- |
| Action reconstruction | Reconstruct what the agent attempted, dispatched, executed, blocked, or partially executed. |
| Authority reconstruction | Determine whether authority existed at the point of execution. |
| Approval reconstruction | Determine whether approval existed, what was approved, and whether the final action matched it. |
| Evidence integrity review | Determine whether evidence was altered, deleted, replayed, truncated, or selectively omitted. |
| Timeline reconstruction | Reconstruct relevant ordering across authorization, approval, dispatch, execution, verification, and incident handling. |
| Trust limitation preservation | Preserve uncertainty, missing records, failed verification, and source limitations rather than overwriting them. |
| Accountability triage | Help distinguish model behavior, agent runtime behavior, tool dispatcher behavior, backend execution, and human approval or override decisions. |

## Preservation Levels

This appendix uses four non-normative preservation levels.

| Level | Name | Description |
| --- | --- | --- |
| IR-P0 | Minimal preservation | Preserve enough evidence to identify the action, system, timestamp, and apparent outcome. |
| IR-P1 | Action-bound preservation | Preserve authorization, approval, dispatch, execution, and evidence references for the action. |
| IR-P2 | Reconstruction-grade preservation | Preserve correlated evidence across enforcement, backend, evidence store, approval workflow, and relevant system logs. |
| IR-P3 | Dispute-grade preservation | Preserve original records, proof references, integrity checks, failed checks, reviewer access, exports, and chain-of-custody context. |

These levels are planning guidance only.

They do not change the Evidence Event Schema.

They do not create a certification scale.

## Candidate Scenario Summary

| Candidate ID | Scenario | Recommended preservation level |
| --- | --- | --- |
| IR-EVD-PRES-01 | Suspected unauthorized high-impact action | IR-P2 or IR-P3 |
| IR-EVD-PRES-02 | Approval-to-execution mismatch | IR-P2 or IR-P3 |
| IR-EVD-PRES-03 | Failed or unavailable evidence integrity verification | IR-P2 or IR-P3 |
| IR-EVD-PRES-04 | Missing or inconsistent authorization evidence | IR-P2 |
| IR-EVD-PRES-05 | Suspicious override or reauthorization | IR-P2 or IR-P3 |
| IR-EVD-PRES-06 | Blocked or non-executed action under dispute | IR-P1 or IR-P2 |
| IR-EVD-PRES-07 | Suspected evidence deletion, truncation, or selective omission | IR-P3 |
| IR-EVD-PRES-08 | Model-generated incident summary conflicts with system evidence | IR-P2 |
| IR-EVD-PRES-09 | Cross-domain or delegated action incident | IR-P2 or IR-P3 |
| IR-EVD-PRES-10 | Retention, redaction, or privacy-sensitive incident evidence | IR-P2 or IR-P3 |

## Common Evidence Package

For most scenarios, responders should preserve an action-bound evidence package.

Candidate package contents:

| Evidence item | Purpose |
| --- | --- |
| Action ID or canonical action ID | Identifies the action being investigated. |
| Action digest or canonical representation | Supports comparison between proposed, approved, dispatched, and executed action. |
| Principal context | Shows user, service, agent, delegated principal, session, and authority context where available. |
| Authorization decision artifact | Shows decision, policy version, scope, constraints, expiry, and decision source. |
| Approval workflow record | Shows approval source, approver, approved scope, approver view, and approval timing. |
| Tool dispatch record | Shows what the agent runtime or tool dispatcher attempted to invoke. |
| Enforcement decision record | Shows allow, deny, defer, escalation, or block result at the enforcement point. |
| Backend execution record | Shows what the system of record actually executed. |
| Non-execution record | Shows denial, block, revocation, freeze, or non-execution where applicable. |
| Evidence integrity metadata | Shows mechanism, proof reference, verification result, and external anchors. |
| Evidence trust limitation | Shows missing, partial, unverifiable, weak, or self-reported evidence limitations. |
| Corroborating logs | Supports cross-checking across independent systems. |
| Incident handling record | Shows preservation trigger, responder actions, exports, access, and handoff. |

## IR-EVD-PRES-01 — Suspected Unauthorized High-Impact Action

### Scenario

A high-impact action appears to have been executed without clear user, service, policy, or delegated authority.

Examples include:

- sending external customer communication;
- modifying production configuration;
- deleting records;
- initiating payment or refund;
- changing access control state;
- triggering operational workflow with external impact.

### Preservation trigger

Preserve evidence when any of the following are observed:

- action outcome is disputed;
- authorization artifact is missing or inconsistent;
- tool execution occurred outside expected policy scope;
- user claims the action was not authorized;
- backend execution happened without clear dispatch or approval linkage.

### Evidence to preserve

Preserve:

- action ID and canonical action representation;
- authorization decision artifact;
- policy version;
- principal context;
- tool dispatch event;
- enforcement point decision;
- backend execution record;
- evidence integrity proof or verification result;
- relevant agent runtime transcript or trace as untrusted context;
- evidence trust limitations.

### Review expectation

A reviewer should be able to determine:

- whether authority existed;
- whether the action was within scope;
- whether the dispatched action matched the authorized action;
- whether backend execution matched the dispatch;
- whether missing evidence prevents a full conclusion.

### Anti-patterns

Do not rely only on:

- model explanation of why the action was allowed;
- agent runtime self-report;
- post-incident summary created after the fact;
- screenshot without corroborating logs.

## IR-EVD-PRES-02 — Approval-to-Execution Mismatch

### Scenario

The approved action differs from the executed action.

Examples include:

- approver approved draft or preview, but execution occurred;
- approver approved one recipient list, but a different list was used;
- approver approved a limited amount, but a larger amount was executed;
- approval expired before execution;
- approval covered a different action digest.

### Preservation trigger

Preserve evidence when:

- approval record and executed action differ;
- approval scope is ambiguous;
- approval was granted through a workflow but not checked at execution boundary;
- post-approval modification occurred;
- approval source is model-generated or agent-reported rather than workflow-generated.

### Evidence to preserve

Preserve:

- approval workflow record;
- approver identity or role reference;
- approver view reference;
- context presented to approver;
- approved canonical action ID;
- approved action digest;
- approved scope and operation class;
- final dispatched action;
- final backend execution record;
- approval enforcement check result;
- model-generated approval summaries as untrusted context only.

### Review expectation

A reviewer should be able to compare:

- what was presented;
- what was approved;
- what was dispatched;
- what was executed;
- whether approval was checked at the execution boundary.

### Anti-patterns

Do not treat the following as sufficient:

- “the model said it was approved”;
- approval UI state without workflow record;
- approval summary without action digest or scope;
- approval for a broader task used to justify a specific high-impact action.

## IR-EVD-PRES-03 — Failed or Unavailable Evidence Integrity Verification

### Scenario

Evidence integrity verification fails, is unavailable, or produces only partial results.

Examples include:

- hash chain mismatch;
- missing proof reference;
- external anchor unavailable;
- signature verification failure;
- immutable storage proof unavailable;
- verification job failed or was not run.

### Preservation trigger

Preserve evidence when:

- `verification_result` is fail, partial, unavailable, or not_checked;
- verification reference is missing;
- proof reference does not match the evidence package;
- verification system is unavailable;
- evidence store shows inconsistent integrity state.

### Evidence to preserve

Preserve:

- original evidence package;
- failed verification result;
- verification error;
- verification job reference;
- proof reference;
- external anchor reference;
- evidence store metadata;
- relevant system logs around verification;
- evidence trust limitation.

### Review expectation

A reviewer should see the failure state, not just the later corrected or reprocessed state.

### Anti-patterns

Avoid:

- rerunning verification and overwriting the original failure;
- replacing failed proof with a new proof without recording the transition;
- hiding failed verification behind an aggregated “audit status” field;
- treating unavailable verification as pass.

## IR-EVD-PRES-04 — Missing or Inconsistent Authorization Evidence

### Scenario

The system executed or attempted an action, but authorization evidence is missing, incomplete, expired, or inconsistent.

Examples include:

- authorization decision ID missing;
- policy version missing;
- action scope mismatch;
- expired authorization;
- principal context mismatch;
- enforcement decision missing.

### Preservation trigger

Preserve evidence when:

- backend execution exists without corresponding authorization decision;
- authorization decision does not match action digest;
- authorization expiry precedes execution;
- policy version differs between decision and execution;
- principal context changed before execution.

### Evidence to preserve

Preserve:

- authorization decision artifact;
- policy version and policy source;
- decision timestamp and expiry;
- principal context;
- action digest;
- enforcement point log;
- dispatch and execution records;
- evidence limitations if authorization evidence is incomplete.

### Review expectation

A reviewer should be able to determine whether the action was allowed at the point of execution.

### Anti-patterns

Do not infer authorization solely from:

- successful backend execution;
- presence of a tool call;
- model-generated reasoning;
- absence of denial logs.

## IR-EVD-PRES-05 — Suspicious Override or Reauthorization

### Scenario

An action was denied, blocked, expired, or revoked, but later executed after override or reauthorization.

Examples include:

- human override after policy denial;
- emergency override;
- reauthorization after expiry;
- revocation followed by execution;
- freeze lifted before action.

### Preservation trigger

Preserve evidence when:

- override follows denial;
- reauthorization occurs close to execution;
- emergency path is used;
- override actor differs from original approver;
- revoked or frozen authority is later restored.

### Evidence to preserve

Preserve:

- original denial or block record;
- override request and approval;
- reauthorization decision;
- actor identity and role;
- justification or ticket reference;
- dispatch and execution record;
- evidence integrity and trust limitation metadata;
- timeline of denial, override, reauthorization, dispatch, and execution.

### Review expectation

A reviewer should be able to distinguish normal authorization from override-based authority.

### Anti-patterns

Avoid:

- overwriting the original denial with the final allow decision;
- preserving only the final successful action;
- treating override as equivalent to routine approval without context;
- omitting emergency justification.

## IR-EVD-PRES-06 — Blocked or Non-Executed Action Under Dispute

### Scenario

An action was allegedly blocked or not executed, but a user, customer, operator, or auditor disputes the result.

Examples include:

- agent attempted a destructive action but tool dispatcher blocked it;
- backend rejected the request;
- action partially executed;
- user claims the system still performed the action;
- UI indicated success but backend did not execute.

### Preservation trigger

Preserve evidence when:

- outcome is disputed;
- non-execution record exists;
- dispatch was attempted but execution did not occur;
- frontend, agent runtime, dispatcher, and backend disagree;
- partial execution occurred.

### Evidence to preserve

Preserve:

- attempted action;
- tool dispatch request;
- enforcement decision;
- non-execution or block record;
- backend response;
- user-visible result;
- agent runtime context as untrusted context;
- evidence trust limitation.

### Review expectation

A reviewer should distinguish:

- attempted action;
- dispatched action;
- blocked action;
- partially executed action;
- fully executed action.

### Anti-patterns

Avoid:

- treating a tool call attempt as execution;
- treating a model statement of success as backend execution;
- dropping non-execution records during log cleanup;
- preserving only successful action records.

## IR-EVD-PRES-07 — Suspected Evidence Deletion, Truncation, or Selective Omission

### Scenario

Evidence appears incomplete or selectively favorable.

Examples include:

- denial records missing;
- failed verification missing;
- only successful records preserved;
- hash-chain tail missing;
- post-action failure record omitted;
- logs are shorter than expected.

### Preservation trigger

Preserve evidence when:

- evidence chain length changes;
- expected records are absent;
- corroborating logs disagree;
- proof references do not cover all expected records;
- evidence package appears cherry-picked.

### Evidence to preserve

Preserve:

- current evidence package;
- expected evidence inventory;
- evidence store metadata;
- retention and deletion records;
- redaction records;
- corroborating logs;
- proof references;
- trust limitation records.

### Review expectation

A reviewer should be able to determine whether evidence is complete enough to support the assessment result.

### Anti-patterns

Avoid:

- presenting partial evidence as complete;
- deleting unfavorable records after incident declaration;
- relying on a single evidence store without corroboration;
- omitting records that show denial, revocation, override, failure, or non-execution.

## IR-EVD-PRES-08 — Model Summary Conflicts With System Evidence

### Scenario

A model-generated incident summary conflicts with backend, enforcement, approval, or evidence store records.

Examples include:

- model claims action was approved but workflow has no approval;
- model claims execution failed but backend shows success;
- model claims user authorized action but authorization artifact is missing;
- model summarizes wrong recipient, amount, resource, or operation.

### Preservation trigger

Preserve evidence when:

- model summary conflicts with system evidence;
- responder relies on model summary for triage;
- model-generated incident report is used in review;
- model summary omits unfavorable records.

### Evidence to preserve

Preserve:

- model-generated summary;
- prompt and context used to generate summary where appropriate;
- source evidence references used by the model;
- backend execution record;
- authorization and approval records;
- evidence store records;
- explicit note that model summary is not authority.

### Review expectation

A reviewer should be able to separate model-generated narrative from trusted evidence.

### Anti-patterns

Avoid:

- replacing source evidence with model summary;
- treating model summary as a trusted audit record;
- allowing model summary to overwrite failed verification or missing evidence;
- citing model explanation as authorization.

## IR-EVD-PRES-09 — Cross-Domain or Delegated Action Incident

### Scenario

An agent acts across domains, tenants, tools, services, or delegated authority boundaries.

Examples include:

- one agent delegates to another;
- service account acts on behalf of a user;
- cross-tenant operation occurs;
- toolchain crosses internal and external systems;
- delegated authority is stale, revoked, or unclear.

### Preservation trigger

Preserve evidence when:

- authority lineage is unclear;
- receiving system accepted delegated context;
- action crosses trust domains;
- principal context changed;
- delegated authority was revoked, expired, or narrowed.

### Evidence to preserve

Preserve:

- originating principal context;
- delegated principal context;
- delegation or handoff record;
- receiving-side validation record;
- authorization decisions at each boundary;
- dispatch and execution records per domain;
- trust limitations around delegation evidence.

### Review expectation

A reviewer should be able to reconstruct authority across boundaries.

### Anti-patterns

Avoid:

- preserving only the final system’s execution record;
- assuming delegated context was valid without receiving-side validation;
- dropping the original principal context;
- treating agent-to-agent messages as authority.

## IR-EVD-PRES-10 — Retention, Redaction, or Privacy-Sensitive Incident Evidence

### Scenario

Incident evidence contains sensitive data or is subject to retention, deletion, or redaction constraints.

Examples include:

- personal data in prompts or tool inputs;
- customer data in execution logs;
- secrets or credentials in traces;
- regulated data in evidence packages;
- legal hold or retention conflict.

### Preservation trigger

Preserve evidence carefully when:

- incident review requires sensitive records;
- standard retention would delete relevant evidence;
- redaction may remove action-critical context;
- privacy or legal constraints limit evidence sharing.

### Evidence to preserve

Preserve:

- original evidence under restricted access;
- redacted review copy where appropriate;
- redaction record;
- retention hold record;
- access log;
- evidence trust limitation describing redaction impact;
- proof reference for original evidence where available.

### Review expectation

A reviewer should be able to understand whether redaction or retention constraints affect confidence.

### Anti-patterns

Avoid:

- redacting without recording what class of information was removed;
- deleting original evidence before review;
- copying secrets into uncontrolled investigation notes;
- treating redacted evidence as complete when redaction affects reconstruction.

## Preservation Timeline Candidate

A typical preservation sequence may be:

1. Identify preservation trigger.
2. Assign incident or review identifier.
3. Freeze or snapshot relevant evidence.
4. Preserve original records before transformation.
5. Preserve proof references and verification states.
6. Preserve failed, partial, unavailable, or not-checked verification states.
7. Preserve authorization, approval, dispatch, execution, and non-execution linkage.
8. Preserve trust limitations and missing-record indicators.
9. Record responder access, export, handoff, and chain-of-custody context where available.
10. Produce a review package that distinguishes trusted evidence from model summaries and analysis notes.

## Reviewer Checklist Candidate

A reviewer should ask:

- What action is being investigated?
- What was authorized?
- What was approved?
- What was dispatched?
- What was executed?
- What was blocked or not executed?
- What evidence was preserved?
- What evidence is missing?
- What evidence integrity checks passed, failed, or were unavailable?
- What evidence trust limitations exist?
- Which records are model-generated summaries or agent self-reports?
- Which records are generated by trusted enforcement, backend, approval, or evidence systems?
- Does the evidence package support reconstruction without relying on model output as authority?

## Minimal Preservation Package Candidate

For a high-impact action incident, a minimal useful package should include:

- action identifier;
- incident or review identifier;
- authorization decision artifact or missing-authorization limitation;
- approval record or approval-not-required rationale;
- dispatch record;
- execution or non-execution record;
- evidence integrity metadata or limitation;
- evidence trust limitation;
- relevant timestamps;
- responder preservation note.

## Dispute-Grade Preservation Package Candidate

For disputed, high-impact, externally consequential, or legally sensitive incidents, a stronger package should include:

- all minimal package items;
- canonical action representation;
- action digest;
- policy version;
- principal and delegated context;
- approver view reference;
- approval scope;
- enforcement check result;
- backend system-of-record response;
- failed verification results;
- proof references;
- external anchors;
- retention hold or preservation record;
- redaction record if applicable;
- reviewer access and export record;
- chain-of-custody or handoff notes where available.

## Incorporation Assessment

| Candidate area | Active incorporation readiness | Suggested next action |
| --- | --- | --- |
| Preservation trigger conditions | Medium | Keep as guidance for now |
| Evidence to preserve | Medium | Keep as guidance; consider later assessment aid |
| Trust boundary considerations | High | Candidate for future evidence guidance |
| Anti-patterns | High | Candidate for implementer-facing guidance |
| Scenario candidates | Medium | Keep in appendix; avoid active CSV for now |
| Reviewer checklist | High | Candidate for future assessment worksheet or quick-start guidance |
| Minimal preservation package | Medium | Candidate for future evidence guidance |
| Dispute-grade package | Medium | Candidate for future evidence guidance |

## Relationship to AAEF-EVD-04

This appendix complements `AAEF-EVD-04`.

`AAEF-EVD-04` covers tamper-evident evidence and evidence integrity.

This appendix focuses on what responders should preserve when there is an incident or evidence-integrity concern.

No active CSV change is recommended in this appendix.

## Relationship to #165

This appendix advances #165 by giving incident-response evidence preservation concrete scenario coverage.

It does not close #165.

Remaining #165 work may include:

- deciding whether this guidance is sufficient for the current cycle;
- deciding whether evidence depth or E5 terminology should become profile guidance;
- deciding whether negative evidence examples or validator fixtures would help;
- deciding whether `AAEF-EVD-01` needs later evidence sufficiency or limitation refinement;
- consolidating temporary planning documents after the current follow-up cycle.

## Non-Goals

This appendix does not:

- update active testing procedure CSV;
- add testing procedure rows;
- add candidate IDs to active CSV;
- update the Evidence Event Schema;
- add evidence examples;
- add validator fixtures;
- change control catalog CSV;
- change human-readable control requirements;
- change assessment worksheet;
- change assessment profiles;
- change external framework mapping CSV;
- create GitHub issues;
- close #161, #163, #165, or #167.

It records candidate incident-response preservation scenarios before any active incorporation decision.

## Status after Initial Appendix Completion

This appendix completes the current incident-response evidence preservation candidate coverage for #165.

Current result:

- ten preservation scenarios are documented;
- preservation levels are documented;
- common evidence package guidance is documented;
- minimal and dispute-grade preservation package candidates are documented;
- reviewer checklist candidates and anti-patterns are documented.

No active CSV, schema, example, validator fixture, control catalog, assessment worksheet, assessment profile, or external mapping change is required by this appendix.
