# v0.5.x Tamper-Evident Evidence Selected Contexts Candidate Appendix

**Status:** Temporary, non-normative candidate appendix

## Purpose

This appendix expands the tamper-evident evidence selected contexts proposal into concrete candidate contexts, scenario expectations, evidence packages, and incorporation considerations.

It follows:

- `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-proposal.md`
- `docs/en/status/v050x-issue-165-evidence-integrity-consolidation-checkpoint.md`
- `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md`
- `docs/en/status/v050x-evd01-evidence-sufficiency-limitation-review-proposal.md`
- `docs/en/status/v050x-follow-up-status.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Primary source issue:

- #166 — define tamper-evident evidence requirements for selected contexts

Related active rows:

- `AAEF-EVD-04`
- `AAEF-EVD-01`

This appendix does not update active testing procedures.

It does not update the Evidence Event Schema.

It does not add evidence examples.

It does not add validator fixtures.

It does not close #166 by itself.

## Executive Summary

Tamper-evident evidence should not be required uniformly for every agentic action.

Instead, it should be expected where the cost of unclear, altered, omitted, replayed, or unverifiable evidence is high.

This appendix proposes candidate selected contexts where tamper-evident evidence should be:

- required;
- recommended;
- optional;
- escalated based on risk factors.

The goal is to make the selected-context decision reviewable without turning AAEF into a certification scale or requiring a single technical mechanism.

## Interpretation Rules

The expectation levels in this appendix are non-normative.

| Expectation | Meaning |
| --- | --- |
| Required | Tamper-evident evidence should normally be expected unless a documented exception exists. |
| Recommended | Tamper-evident evidence should be strongly considered and may become required based on impact, dispute risk, or implementation maturity. |
| Optional | Tamper-evident evidence may be useful, but ordinary evidence may be acceptable unless escalation factors apply. |
| Escalate | The context starts lower, but becomes recommended or required when additional risk factors apply. |

These are candidate terms only.

They do not create active CSV requirements until incorporated separately.

## Common Tamper-Evident Evidence Package

Where tamper-evident evidence is required or recommended, the evidence package should generally support reconstruction across the action lifecycle.

Candidate package contents:

| Evidence item | Purpose |
| --- | --- |
| Canonical action identifier | Identifies the action under review. |
| Canonical action representation or digest | Supports comparison between requested, approved, dispatched, and executed action. |
| Principal context | Shows user, agent, service, session, delegated principal, or authority context. |
| Authorization decision artifact | Shows authority basis, policy, constraints, decision, and expiry. |
| Approval workflow record | Shows approver, approved scope, approver view, and approval timing where applicable. |
| Tool dispatch record | Shows what the agent or runtime attempted to invoke. |
| Enforcement decision record | Shows allow, deny, block, defer, escalation, or override decision. |
| Backend execution or non-execution record | Shows what the system of record actually did or refused to do. |
| Integrity proof or verification state | Shows proof reference, verification result, failure, partial result, or unavailability. |
| Evidence trust limitation | Records missing, partial, unverifiable, self-reported, or weak evidence. |
| Correlation identifiers | Connects authorization, approval, dispatch, execution, and evidence records. |
| Preservation context | Supports incident review, retention hold, export, redaction, or handoff where relevant. |

## Candidate Context Summary

| Candidate ID | Context | Suggested expectation |
| --- | --- | --- |
| TE-CXT-01 | High-impact external action | Required |
| TE-CXT-02 | Financial transaction, refund, credit, or billing action | Required |
| TE-CXT-03 | Access control or privilege change | Required |
| TE-CXT-04 | Production configuration or infrastructure change | Required |
| TE-CXT-05 | Destructive or irreversible data action | Required |
| TE-CXT-06 | Security control weakening or enforcement bypass | Required |
| TE-CXT-07 | Cross-domain or delegated authority action | Required or Recommended |
| TE-CXT-08 | Approval-gated action | Recommended or Required |
| TE-CXT-09 | Incident-response evidence package | Required |
| TE-CXT-10 | Override, reauthorization, emergency, or break-glass path | Required |
| TE-CXT-11 | Customer-visible communication or publication | Recommended |
| TE-CXT-12 | Data export, disclosure, or sharing action | Recommended or Required |
| TE-CXT-13 | High-volume automated operational changes | Recommended |
| TE-CXT-14 | Low-impact read-only or advice-only action | Optional, with escalation |
| TE-CXT-15 | Non-production experiment or debugging trace | Optional, with escalation |

## TE-CXT-01 — High-Impact External Action

### Context

An agentic system performs or initiates an externally visible action that may affect customers, partners, operators, regulators, financial systems, public content, or production operations.

### Suggested expectation

Required.

### Rationale

External effects may be difficult to reverse and may be disputed by parties outside the system boundary.

Tamper-evident evidence should support reconstruction of what was authorized, dispatched, executed, and observed.

### Candidate evidence expectations

Preserve:

- action identifier;
- principal context;
- authorization decision;
- approval record if applicable;
- dispatch record;
- backend execution record;
- external target or recipient reference;
- timestamp and correlation identifiers;
- integrity verification state;
- evidence trust limitations.

### Escalation factors

Treat as strongly required when:

- the action is irreversible;
- the action affects money, access, legal commitments, regulated data, or security posture;
- the action may be challenged by an external party;
- the action was produced from model-generated content or agent-selected parameters.

### Anti-patterns

Do not rely only on:

- model explanation;
- UI success message;
- agent runtime trace;
- post-hoc summary without backend corroboration.

## TE-CXT-02 — Financial Transaction, Refund, Credit, or Billing Action

### Context

An agentic system initiates, approves, modifies, or cancels a financial action.

Examples:

- payment initiation;
- refund issuance;
- account credit;
- invoice modification;
- subscription cancellation;
- billing configuration change.

### Suggested expectation

Required.

### Rationale

Financial actions require strong reconstruction of amount, recipient, account, approval, authority, and execution outcome.

### Candidate evidence expectations

Preserve:

- amount and currency;
- recipient or account reference;
- authorization decision artifact;
- approval workflow record;
- approved and executed action digest;
- payment, refund, billing, or ledger backend response;
- non-execution or reversal record if applicable;
- integrity proof or verification state;
- evidence limitation if any part of the transaction chain is missing.

### Review questions

A reviewer should be able to answer:

- Who or what initiated the financial action?
- What amount and recipient were authorized?
- Was approval required and obtained?
- Did execution match approval?
- Was the backend system of record updated?
- Are failed, reversed, or partial states visible?

## TE-CXT-03 — Access Control or Privilege Change

### Context

An agentic system grants, revokes, modifies, or requests access.

Examples:

- role assignment;
- privilege escalation;
- access revocation;
- group membership change;
- API key or token permission update;
- service account permission change.

### Suggested expectation

Required.

### Rationale

Access changes directly affect authority boundaries and future action capability.

### Candidate evidence expectations

Preserve:

- target subject;
- target resource;
- permission or role before and after;
- authority basis;
- authorization decision;
- approval if required;
- backend identity or access management record;
- dispatch and execution record;
- revocation or rollback record if applicable;
- integrity verification and evidence limitations.

### Anti-patterns

Avoid accepting:

- “access was granted” model summary without IAM backend evidence;
- agent self-report as proof of revocation;
- missing before/after state;
- approval for a different privilege or resource.

## TE-CXT-04 — Production Configuration or Infrastructure Change

### Context

An agentic system modifies production configuration, infrastructure, deployment, routing, scaling, firewall, feature flag, or runtime parameters.

### Suggested expectation

Required.

### Rationale

Production changes may affect availability, security, compliance, and customer impact.

### Candidate evidence expectations

Preserve:

- change request or action digest;
- environment identifier;
- production target;
- authorization and approval records;
- dispatch record;
- backend configuration management or deployment record;
- pre-change and post-change state where feasible;
- rollback, failure, or partial deployment record;
- integrity verification and correlation identifiers.

### Escalation factors

Always require tamper-evident evidence when the change affects:

- authentication;
- authorization;
- network exposure;
- customer traffic;
- logging or monitoring;
- encryption;
- production data access;
- safety or compliance controls.

## TE-CXT-05 — Destructive or Irreversible Data Action

### Context

An agentic system deletes, purges, overwrites, anonymizes, archives, or irreversibly mutates data.

### Suggested expectation

Required.

### Rationale

Destructive actions are often hard to reconstruct after the fact unless evidence is preserved before or during execution.

### Candidate evidence expectations

Preserve:

- target dataset, object, table, file, or record set;
- operation type;
- authorization decision;
- approval or change ticket if applicable;
- dispatch and backend execution record;
- affected object count or scope;
- backup, snapshot, recovery, or non-recovery context;
- deletion, purge, overwrite, or redaction record;
- evidence integrity verification state.

### Review questions

A reviewer should be able to answer:

- What was deleted or changed?
- Was the target scope authorized?
- Was execution complete, partial, blocked, or failed?
- Can the system distinguish deletion from non-execution?
- Was evidence retained despite data deletion?

## TE-CXT-06 — Security Control Weakening or Enforcement Bypass

### Context

An agentic system disables, weakens, bypasses, or modifies a security control.

Examples:

- disable monitoring;
- suppress alerts;
- change policy mode from enforce to monitor;
- add allowlist entry;
- reduce authentication requirement;
- disable evidence collection;
- bypass approval or enforcement path.

### Suggested expectation

Required.

### Rationale

Security control weakening may hide subsequent unauthorized or unsafe behavior.

### Candidate evidence expectations

Preserve:

- control name or enforcement point;
- before and after state;
- authorization decision;
- approval or emergency justification;
- dispatch and backend change record;
- duration or expiry;
- rollback or re-enable record;
- affected scope;
- integrity verification state;
- evidence limitation if logging or monitoring was reduced.

### Anti-patterns

Avoid:

- treating missing logs after logging was disabled as neutral;
- preserving only the final allowed action;
- overwriting denial records with later override records;
- accepting model-generated justification as approval.

## TE-CXT-07 — Cross-Domain or Delegated Authority Action

### Context

An action crosses users, agents, services, tenants, organizations, tools, or administrative domains.

Examples:

- agent-to-agent delegation;
- service account on behalf of a user;
- cross-tenant operation;
- external tool invocation;
- delegated authority chain.

### Suggested expectation

Required or Recommended.

Required when high-impact or externally consequential.

Recommended for lower-impact delegated actions.

### Rationale

Authority lineage and validation can become ambiguous across boundaries.

### Candidate evidence expectations

Preserve:

- originating principal context;
- delegated principal context;
- delegation request and acceptance or refusal;
- delegated scope and expiry;
- receiving-side validation;
- authorization decision at each boundary;
- dispatch and execution records;
- evidence limitations around delegation chain.

### Review questions

A reviewer should be able to reconstruct:

- who originated the authority;
- what was delegated;
- who accepted it;
- what boundary validated it;
- whether the final action stayed within scope.

## TE-CXT-08 — Approval-Gated Action

### Context

An action requires human, policy, workflow, or risk-based approval before execution.

### Suggested expectation

Recommended or Required.

Required when the approved action is high-impact, financial, destructive, externally visible, or disputed.

### Rationale

Approval is meaningful only if the approved action can be bound to the executed action.

### Candidate evidence expectations

Preserve:

- approval request;
- approver identity or role;
- approver view;
- approved action digest;
- approved scope and constraints;
- approval timestamp and expiry;
- execution boundary approval check;
- final dispatch and backend execution record;
- mismatch, denial, or non-execution record.

### Anti-patterns

Avoid:

- approval for a broad task being reused for a specific high-impact action;
- approval summary without approved action digest;
- model statement that approval occurred;
- approval state stored only inside agent runtime.

## TE-CXT-09 — Incident-Response Evidence Package

### Context

Evidence is collected, preserved, exported, or reviewed during an incident, suspected misuse, unauthorized action, or dispute.

### Suggested expectation

Required.

### Rationale

Incident response depends on evidence that has not been silently altered, omitted, or overwritten.

### Candidate evidence expectations

Preserve:

- incident or review identifier;
- original evidence package;
- verification results;
- failed, partial, unavailable, or not-checked verification states;
- authorization, approval, dispatch, execution, and non-execution records;
- trust limitations;
- retention hold or preservation record;
- redaction and export records where applicable;
- reviewer access or handoff record where appropriate.

### Review questions

A reviewer should be able to distinguish:

- original evidence;
- enriched evidence;
- model-generated summary;
- reviewer notes;
- redacted copy;
- missing or unverifiable evidence.

## TE-CXT-10 — Override, Reauthorization, Emergency, or Break-Glass Path

### Context

An action proceeds after denial, expiry, revocation, emergency override, or exceptional reauthorization.

### Suggested expectation

Required.

### Rationale

Exceptional authority paths are more likely to be disputed or abused.

### Candidate evidence expectations

Preserve:

- original denial, expiry, revocation, or block record;
- override or reauthorization request;
- actor identity and role;
- justification;
- scope and duration;
- approval or policy basis;
- final dispatch and backend execution record;
- rollback, re-freeze, or revocation record if applicable.

### Anti-patterns

Avoid:

- preserving only the final allowed action;
- overwriting original denial with override;
- omitting emergency justification;
- treating emergency override as routine approval.

## TE-CXT-11 — Customer-Visible Communication or Publication

### Context

An agentic system sends, publishes, modifies, or schedules customer-visible content.

Examples:

- external email;
- customer support response;
- public webpage update;
- status page update;
- contractual notification;
- marketing or legal communication.

### Suggested expectation

Recommended.

Required when regulated, legally significant, contractual, high-impact, or dispute-prone.

### Candidate evidence expectations

Preserve:

- message or content digest;
- recipient or audience;
- approval if required;
- source content or generation context where relevant;
- dispatch or publication record;
- delivery or publication confirmation;
- modification or retraction record;
- evidence limitation for model-generated text.

### Review questions

A reviewer should know:

- what content was sent or published;
- who or what approved it;
- who received or saw it;
- whether the final version matched the approved version.

## TE-CXT-12 — Data Export, Disclosure, or Sharing Action

### Context

An agentic system exports, shares, transmits, or discloses data outside its original boundary.

### Suggested expectation

Recommended or Required.

Required when data is sensitive, regulated, customer-owned, confidential, or externally shared.

### Candidate evidence expectations

Preserve:

- dataset or object reference;
- data classification;
- recipient or destination;
- export scope;
- authorization decision;
- approval or data access review if required;
- dispatch and backend export record;
- transfer confirmation;
- redaction or filtering record;
- integrity verification and trust limitation.

### Anti-patterns

Avoid:

- model summary of exported data without export record;
- missing recipient;
- missing data classification;
- no record of filters or redactions;
- treating a query preview as equivalent to export execution.

## TE-CXT-13 — High-Volume Automated Operational Changes

### Context

An agentic system performs many operational changes automatically.

Examples:

- bulk ticket updates;
- batch configuration changes;
- automated remediation;
- large-scale workflow transitions;
- repeated tool dispatches.

### Suggested expectation

Recommended.

May become required if high-impact, irreversible, or externally visible.

### Rationale

High volume increases the risk that selective omission, replay, truncation, or aggregate-only summaries hide issues.

### Candidate evidence expectations

Preserve:

- batch identifier;
- per-action identifiers or sampled action set;
- authorization scope;
- dispatch and execution summaries;
- failure and non-execution records;
- aggregate counts;
- representative per-action evidence;
- evidence completeness and limitation records.

### Review questions

A reviewer should be able to determine:

- whether the batch scope was authorized;
- what subset executed;
- what failed;
- what was omitted;
- whether aggregate counts match per-action records.

## TE-CXT-14 — Low-Impact Read-Only or Advice-Only Action

### Context

An agentic system reads data, generates recommendations, or provides advice without executing an external action.

### Suggested expectation

Optional, with escalation.

### Escalation factors

Escalate to recommended or required when:

- the read involves sensitive, regulated, or confidential data;
- the recommendation is automatically used to trigger execution;
- the advice is used in a high-impact decision;
- there is a privacy, legal, or incident-response context;
- the action crosses tenant or domain boundaries.

### Candidate evidence expectations

When optional, ordinary logs may be enough.

When escalated, preserve:

- data source reference;
- query or read action;
- principal context;
- authorization basis;
- output or recommendation reference;
- downstream action linkage if advice triggered execution;
- trust limitation for model-generated recommendation.

### Anti-patterns

Avoid treating advice-only output as safe if it is automatically converted into execution elsewhere.

## TE-CXT-15 — Non-Production Experiment or Debugging Trace

### Context

An agentic system operates in non-production, test, lab, or debugging contexts.

### Suggested expectation

Optional, with escalation.

### Escalation factors

Escalate when:

- shared resources are affected;
- production data is used;
- credentials or secrets appear in traces;
- the test changes security posture;
- the experiment produces externally visible effects;
- results are used as audit or assurance evidence.

### Candidate evidence expectations

Preserve:

- environment identifier;
- experiment scope;
- data classification;
- tool permissions;
- execution records for actions affecting shared resources;
- redaction or secret-handling notes;
- evidence limitation if traces are used outside debugging.

## Cross-Cutting Escalation Rules

A context should move toward required tamper-evident evidence when any of the following apply:

| Escalation factor | Effect |
| --- | --- |
| High-impact action | Escalate to required. |
| External effect | Escalate to recommended or required. |
| Financial, access, production, security, or destructive impact | Escalate to required. |
| Human approval dependency | Escalate to recommended or required. |
| Cross-domain or delegated authority | Escalate based on impact and ambiguity. |
| Incident, dispute, legal hold, or audit review | Escalate to required. |
| Evidence generated only by model or agent runtime | Escalate evidence limitation review. |
| Missing, partial, failed, or unavailable verification | Escalate preservation and limitation handling. |
| Retention, deletion, redaction, or privacy constraints | Escalate preservation planning. |

## Candidate Incorporation Assessment

| Candidate area | Readiness | Suggested next action |
| --- | --- | --- |
| Required contexts | Medium | Keep in appendix; consider later guidance extraction. |
| Recommended contexts | Medium | Keep in appendix; refine with implementer feedback. |
| Optional contexts | Medium | Keep in appendix; define escalation factors. |
| Escalation rules | High | Candidate for future reviewer guidance. |
| Common evidence package | High | Candidate for stable evidence guidance. |
| Active CSV change | Low | Do not change active CSV yet. |
| Schema change | Low | Do not add context tier fields yet. |
| Examples | Medium | Candidate future work after context decisions stabilize. |

## Relationship to `AAEF-EVD-04`

`AAEF-EVD-04` remains the primary active testing row for evidence integrity and tamper-evident evidence.

This appendix does not recommend immediate active CSV modification.

A later proposal may decide whether `AAEF-EVD-04` should reference selected contexts or whether context guidance should remain separate.

## Relationship to `AAEF-EVD-01`

`AAEF-EVD-01` remains the primary active testing row for evidence sufficiency and action reconstruction.

Tamper-evident evidence improves reviewability, but it does not automatically make evidence sufficient.

Reviewers should still assess whether evidence supports the assessed action and risk level.

## Relationship to #166

This appendix advances #166 by defining concrete selected-context candidates.

It does not close #166.

Remaining #166 work may include:

- deciding whether selected contexts should remain guidance-only;
- deciding whether any active CSV refinement is needed;
- deciding whether examples should be added for selected contexts;
- deciding whether stable guidance should be extracted after the current follow-up cycle.

## Non-Goals

This appendix does not:

- update active testing procedure CSV;
- add testing procedure rows;
- add candidate IDs to active CSV;
- update the Evidence Event Schema;
- add evidence examples;
- add validator fixtures;
- update `tools/validate_evidence_schema.py`;
- create an evidence depth certification scale;
- change control catalog CSV;
- change human-readable control requirements;
- change assessment worksheet;
- change assessment profiles;
- change external framework mapping CSV;
- create GitHub issues;
- close #161, #163, #165, #166, or #167.

It records selected-context candidates before any active incorporation decision.

## Incorporation Decision

The selected-context incorporation decision is recorded in `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-incorporation-decision.md`.

Current result:

- selected contexts remain non-normative guidance;
- no active CSV change is required at this time;
- no Evidence Event Schema change is required at this time;
- no evidence example change is required at this time;
- no validator change is required at this time.
