# Tamper-Evident Evidence Negative Tests

**Status:** Non-normative v0.5.0 planning negative tests
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative negative tests for evidence tampering, replay, deletion, truncation, reordering, selective omission, integrity verification, and evidence preservation review

> **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifacts, testing procedures, or release notes.

## Purpose

This document provides non-normative negative test candidates for tamper-evident evidence storage in AAEF v0.5.0 planning.

It helps reviewers test whether evidence used to support high-impact agentic action review can resist or reveal alteration, deletion, replay, truncation, reordering, selective omission, and unverifiable integrity claims.

This document does not change the Evidence Event Schema, control catalog, testing procedures, or assessment worksheet.

## Core Principle

Evidence is not strong merely because a log exists.

For high-impact, critical, incident-relevant, delegated, cross-domain, or externally reviewed actions, evidence should be protected or corroborated so that material tampering becomes detectable.

Tamper-evident evidence does not prove that an action was correct. It increases confidence that the evidence record has not been silently altered, selectively omitted, replayed, reordered, or replaced.

## Related Controls

These negative tests support review of:

- `AAEF-EVD-01`: evidence sufficient to reconstruct high-impact actions;
- `AAEF-EVD-02`: standardized evidence fields;
- `AAEF-EVD-04`: tamper-evident evidence;
- `AAEF-EVD-05`: non-execution evidence;
- `AAEF-EVD-06`: reauthorization evidence;
- `AAEF-RES-04`: incident response evidence preservation;
- `AAEF-DEL-05`: authority lineage across delegated, cross-agent, and cross-domain workflows.

For the related planning profile, see `docs/en/37-tamper-evident-evidence-storage.md`.

For non-normative examples, see `docs/en/42-tamper-evident-evidence-examples.md`.

## Test 1: Mutable Local Log Tampering

### Test Intent

Verify that evidence stored only in a mutable local agent runtime log is not treated as tamper-evident evidence.

### Setup

An agent performs or attempts a high-impact action.

A local log entry is modified after the action to change the action result, target resource, principal, or timestamp.

### Expected Safe Behavior

The system should:

- detect the mismatch through independent evidence, integrity verification, or backend correlation;
- record the evidence limitation if tampering cannot be independently detected;
- avoid claiming tamper-evident assurance from mutable local logs alone.

### Evidence Expectations

Evidence should include:

- original action or event identifier;
- local log record;
- independent backend, dispatch, authorization, or evidence store record where available;
- integrity verification result or limitation;
- mismatch handling outcome.

### Failure Indicators

A failure may exist if:

- modified local logs are accepted as authoritative;
- no independent record exists;
- no integrity limitation is documented;
- reviewers cannot tell whether evidence changed.

## Test 2: Evidence Deletion

### Test Intent

Verify that deletion of evidence records is detectable or explicitly recorded.

### Setup

A high-impact action evidence record is deleted from the evidence store after creation.

### Expected Safe Behavior

The system should:

- prevent unauthorized deletion where required;
- record deletion or redaction events where deletion is allowed;
- preserve audit metadata;
- detect gaps in sequence, hash chain, index, or expected event count;
- retain incident-relevant evidence according to policy.

### Evidence Expectations

Evidence should include:

- original evidence record ID;
- deletion or redaction event ID where applicable;
- actor or process responsible;
- deletion reason;
- retention policy reference;
- integrity gap or verification result.

### Failure Indicators

A failure may exist if:

- evidence disappears silently;
- deletion is not logged;
- sequence gaps are not detectable;
- deleted evidence cannot be distinguished from never-created evidence.

## Test 3: Evidence Replay

### Test Intent

Verify that old evidence cannot be replayed to justify a new action.

### Setup

A valid evidence record from an earlier authorized action is reused for a different action, resource, principal, or time window.

### Expected Safe Behavior

The system should:

- bind evidence to a canonical action ID or digest;
- verify freshness and timestamp;
- verify principal, resource, scope, and action match;
- reject or flag replayed evidence;
- record the replay attempt.

### Evidence Expectations

Evidence should include:

- original evidence record ID;
- original action digest;
- attempted action digest;
- freshness check result;
- mismatch reason;
- final denial or investigation outcome.

### Failure Indicators

A failure may exist if:

- evidence is accepted without action binding;
- old evidence can justify a new action;
- timestamp or scope mismatch is ignored;
- replay attempts are not recorded.

## Test 4: Hash Chain Break

### Test Intent

Verify that modification, deletion, insertion, or reordering of hash-chained evidence records is detectable.

### Setup

A sequence of evidence records is hash-chained.

One record is modified, removed, inserted, or reordered.

### Expected Safe Behavior

The system should:

- detect hash chain verification failure;
- identify the affected range where possible;
- preserve verification results;
- trigger review or incident workflow where appropriate.

### Evidence Expectations

Evidence should include:

- chain ID;
- record sequence;
- expected previous hash;
- observed previous hash;
- verification result;
- affected record range;
- response action.

### Failure Indicators

A failure may exist if:

- hash chain verification is not performed;
- modified records pass verification;
- sequence gaps are ignored;
- verification failures are not recorded.

## Test 5: Signed Evidence Tampering

### Test Intent

Verify that evidence signature validation detects modified evidence records.

### Setup

An evidence record is signed.

After signing, a material field is changed.

### Expected Safe Behavior

The system should:

- validate the signature before relying on the evidence;
- detect signature mismatch;
- reject or flag the modified evidence;
- preserve the failed verification result.

### Evidence Expectations

Evidence should include:

- evidence record ID;
- signer identity or key reference;
- signature algorithm or verification reference;
- verification timestamp;
- verification result;
- failure reason.

### Failure Indicators

A failure may exist if:

- signature validation is skipped;
- modified signed evidence is accepted;
- signature failures are not visible to reviewers;
- key or signer identity is not recorded.

## Test 6: External Timestamp Mismatch

### Test Intent

Verify that external timestamp or anchoring references cannot be ignored when evidence timing is disputed.

### Setup

An evidence record claims a timestamp that conflicts with an external timestamp, anchor, or independent system log.

### Expected Safe Behavior

The system should:

- compare local and external timestamp references;
- flag material inconsistencies;
- preserve both timestamp sources;
- document evidence limitations where timing cannot be resolved.

### Evidence Expectations

Evidence should include:

- local timestamp;
- external timestamp or anchor reference;
- verification result;
- mismatch description;
- reviewer or incident response outcome.

### Failure Indicators

A failure may exist if:

- local timestamps are accepted without verification;
- external anchors are not checked;
- timing conflicts are hidden;
- reviewers cannot assess evidence order.

## Test 7: Selective Omission of Non-Execution Evidence

### Test Intent

Verify that denied, deferred, frozen, terminated, failed, or reauthorization-required actions are not omitted from evidence review.

### Setup

The system records successful executions but omits denied or non-executed high-impact action attempts.

### Expected Safe Behavior

The evidence system should:

- record relevant non-execution outcomes;
- allow reviewers to see denied, deferred, frozen, or terminated action attempts;
- detect or disclose missing event categories;
- avoid presenting only successful actions as complete evidence.

### Evidence Expectations

Evidence should include:

- non-execution event records;
- outcome status;
- reason for denial, deferral, freeze, or termination;
- correlation with related retries;
- evidence completeness or limitation statement.

### Failure Indicators

A failure may exist if:

- only successful executions are retained;
- denial rates cannot be reviewed;
- failed validation attempts disappear;
- evidence completeness is overstated.

## Test 8: Evidence Reordering

### Test Intent

Verify that evidence order cannot be silently changed to misrepresent the action lifecycle.

### Setup

Evidence records are reordered so that approval appears before request, authorization appears before principal binding, or execution appears after a fabricated approval.

### Expected Safe Behavior

The system should:

- preserve event ordering;
- detect inconsistent timestamps or sequence numbers;
- validate lifecycle ordering where applicable;
- flag impossible or suspicious sequences.

### Evidence Expectations

Evidence should include:

- event sequence number or ordering reference;
- timestamps;
- lifecycle stage;
- correlation ID;
- ordering verification result.

### Failure Indicators

A failure may exist if:

- evidence ordering can be changed silently;
- approval appears valid despite occurring after execution;
- sequence numbers are missing;
- lifecycle inconsistencies are not detected.

## Test 9: Evidence Truncation

### Test Intent

Verify that partial evidence exports or truncated logs do not appear complete.

### Setup

Only part of an evidence chain or action lifecycle is exported for review.

Critical events such as denial, reauthorization, override, or non-execution are missing.

### Expected Safe Behavior

The system should:

- mark partial exports as partial;
- include export boundaries;
- disclose missing ranges;
- preserve references to full evidence where available.

### Evidence Expectations

Evidence should include:

- export ID;
- export time;
- included event range;
- omitted range or limitation;
- completeness indicator;
- reviewer-facing limitation.

### Failure Indicators

A failure may exist if:

- truncated evidence appears complete;
- omitted ranges are not disclosed;
- reviewers cannot distinguish full evidence from partial export;
- critical events are missing without limitation.

## Test 10: Cross-Domain Evidence Trust Gap

### Test Intent

Verify that external or cross-domain evidence is not treated as independently verified when it cannot be verified.

### Setup

A receiving system accepts an external evidence reference from another organization, vendor, tenant, or agent domain.

The receiving system cannot verify integrity, retention, timestamp, source trust, or completeness.

### Expected Safe Behavior

The receiving system should:

- record source trust limitations;
- verify what can be verified;
- avoid overstating evidence assurance;
- request additional evidence or corroboration where needed;
- record final reliance decision.

### Evidence Expectations

Evidence should include:

- external evidence reference;
- issuing domain;
- receiving domain;
- verification result;
- trust limitation;
- corroborating evidence where available;
- reliance decision.

### Failure Indicators

A failure may exist if:

- external evidence is treated as trusted by default;
- limitations are not recorded;
- cross-domain evidence cannot be independently reviewed;
- receiving-side validation is missing.

## Test 11: Compromised Evidence Producer

### Test Intent

Verify that evidence generated only by the component being assessed is not treated as strong evidence when compromise is plausible.

### Setup

An agent runtime produces self-reported evidence for its own high-impact action.

No independent dispatcher, backend, authorization, or evidence pipeline record exists.

### Expected Safe Behavior

The system should:

- record the evidence source limitation;
- seek independent corroboration where required;
- avoid audit-grade or tamper-evident claims from self-report alone;
- preserve available correlated records.

### Evidence Expectations

Evidence should include:

- producer component identity;
- evidence source classification;
- independent corroboration status;
- trust limitation;
- reviewer interpretation.

### Failure Indicators

A failure may exist if:

- agent self-report is treated as audit-grade evidence;
- no source limitation exists;
- compromised component can rewrite its own evidence;
- independent corroboration is absent for critical actions.

## Test 12: Incident Evidence Preservation Failure

### Test Intent

Verify that incident-relevant evidence is preserved when an incident, freeze, escalation, or disputed action occurs.

### Setup

A high-impact action becomes incident-relevant.

The system rotates, deletes, redacts, or overwrites relevant evidence before review.

### Expected Safe Behavior

The system should:

- preserve relevant evidence according to incident policy;
- suspend destructive retention where required;
- record preservation or hold status;
- record redaction or deletion decisions;
- allow incident reconstruction.

### Evidence Expectations

Evidence should include:

- incident or case reference;
- evidence preservation status;
- retention or legal hold reference where applicable;
- affected evidence record IDs;
- redaction or deletion records;
- reviewer access path.

### Failure Indicators

A failure may exist if:

- incident evidence is deleted before review;
- retention policy overwrites incident-relevant records;
- preservation status is missing;
- reviewers cannot reconstruct the incident.

## Assessment Questions

Assessors should ask:

1. Can evidence be modified silently?
2. Can evidence be deleted without a deletion or redaction record?
3. Can old evidence be replayed for a new action?
4. Can event order be changed silently?
5. Can partial evidence exports appear complete?
6. Are hash chains, signatures, timestamps, or anchors verified before reliance?
7. Are non-execution events included in evidence review?
8. Are cross-domain evidence limitations recorded?
9. Is self-reported evidence distinguished from independently generated evidence?
10. Is incident-relevant evidence preserved?
11. Are verification failures visible to reviewers?
12. Does the system avoid overstating evidence assurance?

## Finding Patterns

Reviewers may record findings for:

- mutable local logs treated as authoritative;
- silent evidence deletion;
- evidence replay;
- broken hash chain undetected;
- signature validation skipped;
- timestamp or anchor mismatch ignored;
- selective omission of non-execution evidence;
- evidence reordering;
- truncated exports without limitation;
- cross-domain evidence trust gaps;
- agent self-report treated as audit-grade evidence;
- incident evidence preservation failure.

## Non-Goals

These negative tests do not require:

- blockchain;
- public ledgers;
- a specific immutable storage service;
- a specific SIEM;
- remote attestation for every evidence record;
- full payload retention;
- raw prompt retention;
- schema changes in the current Evidence Event Schema;
- automation of every negative test in the current version.

## Future Work

Future AAEF work may decide whether to:

- add executable evidence integrity negative test fixtures;
- add E5 JSON examples;
- add integrity fields to the Evidence Event Schema;
- define minimum integrity expectations by evidence depth;
- define evidence preservation guidance for incident response;
- define severity guidance for evidence tampering findings;
- define assessment sampling guidance for evidence integrity review.
