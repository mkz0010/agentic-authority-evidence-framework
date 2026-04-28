# Tamper-Evident Evidence Examples

**Status:** v0.5.0 planning examples
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative examples for tamper-evident, independently corroborated, and integrity-verifiable evidence review

## Purpose

This document provides non-normative examples for reviewing tamper-evident evidence in AAEF v0.5.0 planning.

It illustrates how reviewers can distinguish:

- strong tamper-evident evidence;
- weak mutable logs;
- append-only evidence;
- cryptographically linked evidence;
- signed or sealed evidence;
- externally timestamped evidence;
- independently corroborated evidence;
- trusted runtime or attestation-referenced evidence;
- evidence trust limitations;
- evidence deletion, replay, reordering, and selective omission risks.

This document does not change the Evidence Event Schema, control catalog, testing procedures, or assessment worksheet.

## Core Principle

Tamper-evident evidence does not necessarily prevent tampering.

It should make alteration, deletion, replay, reordering, truncation, selective omission, or inconsistency detectable during review or incident reconstruction.

Evidence is stronger when reviewers can verify integrity independently from the component being assessed.

## Related Controls

These examples support review of:

- `AAEF-EVD-04`: critical and audit-grade action evidence integrity;
- `AAEF-EVD-01`: action reconstruction;
- `AAEF-EVD-02`: standardized evidence fields;
- `AAEF-EVD-05`: non-execution evidence;
- `AAEF-EVD-06`: reauthorization evidence;
- `AAEF-RES-04`: evidence preservation during incident response.

For the related planning profile, see `docs/en/37-tamper-evident-evidence-storage.md`.

## Example 1: Weak Mutable Local Log

### Scenario

An agent runtime writes action evidence to a local JSON log file on the same host where the agent runs.

The agent runtime and local administrator can modify or delete the log.

### Evidence Characteristics

Weak evidence includes:

- local-only storage;
- mutable file;
- no append-only protection;
- no signing;
- no external timestamp;
- no independent corroboration;
- no deletion record;
- no integrity verification result.

### Assessment Interpretation

This evidence may be useful for debugging, but it should not be treated as strong assurance for critical or audit-grade actions.

A reviewer should record an evidence trust limitation if the same component being assessed can silently modify or delete the evidence.

## Example 2: Centralized Controlled Evidence Pipeline

### Scenario

Authorization, dispatch, backend execution, and evidence components send records to a centralized evidence pipeline.

The agent runtime cannot directly modify records after submission.

### Stronger Properties

Stronger evidence includes:

- centralized collection;
- controlled write path;
- separate access controls;
- correlation across authorization, dispatch, execution, and evidence records;
- retention policy;
- administrative access logging;
- integrity verification or monitoring.

### Assessment Interpretation

This is stronger than local self-reporting because evidence is not stored only inside the agent runtime.

However, centralized evidence is still limited if privileged administrators or the evidence pipeline can silently modify or delete records.

## Example 3: Append-Only or Write-Restricted Evidence Store

### Scenario

Critical action evidence is written to an append-only log or write-restricted evidence store.

Records cannot be modified through normal application paths.

### Stronger Properties

Strong evidence includes:

- append-only write path;
- restricted deletion capability;
- retention policy;
- administrative access monitoring;
- truncation detection;
- export or verification process;
- evidence store identifier.

### Assessment Interpretation

Append-only storage improves evidence reliability, especially for incident reconstruction.

A reviewer should still verify whether privileged operators can truncate, rotate, or delete logs without detection.

## Example 4: Hash-Chained Evidence

### Scenario

Each evidence record includes a hash of the previous record.

A later verifier can detect missing, reordered, or modified records.

### Stronger Properties

Strong evidence includes:

- record hash;
- previous record hash;
- chain sequence;
- batch identifier;
- root or checkpoint reference;
- verification result;
- verification timestamp.

### Assessment Interpretation

Hash chains help detect modification, deletion, insertion, or reordering.

They do not prove that the original evidence content was true. They prove consistency of the recorded sequence under the chosen integrity mechanism.

## Example 5: Signed Evidence Batch

### Scenario

Evidence records are batched every five minutes and signed by an evidence service key.

### Stronger Properties

Strong evidence includes:

- batch ID;
- signing key ID;
- signature reference;
- signature verification result;
- signing time;
- evidence store ID;
- key management reference;
- rotation or revocation handling.

### Assessment Interpretation

Signed evidence helps detect unauthorized modification after signing.

A reviewer should still evaluate whether the signing key is protected and whether the signing service signs complete and accurate evidence.

## Example 6: External Timestamp or Anchor

### Scenario

Evidence batch hashes are timestamped by an external timestamping service or anchored outside the assessed system.

### Stronger Properties

Strong evidence includes:

- evidence batch hash;
- external timestamp reference;
- external anchor ID;
- timestamp verification result;
- batch coverage period;
- retained local evidence records.

### Assessment Interpretation

External timestamping can help detect backdating, delayed insertion, or after-the-fact evidence creation.

It does not prove that the underlying action was authorized or correctly executed.

## Example 7: Independent Corroboration

### Scenario

A high-impact action has evidence from multiple sources:

- authorization decision log;
- tool dispatch log;
- backend API audit log;
- cloud audit trail;
- SIEM event;
- approval workflow record.

### Stronger Properties

Strong evidence includes:

- shared correlation ID;
- consistent timestamps;
- consistent action ID or digest;
- consistent principal and resource;
- evidence source identifiers;
- trust limitation for each source;
- inconsistency handling.

### Assessment Interpretation

Independent corroboration reduces reliance on a single component.

A reviewer should inspect inconsistencies rather than assuming all logs are equally trustworthy.

## Example 8: Evidence Replay Risk

### Scenario

A valid authorization evidence record from yesterday is reused to justify a new action today.

### Risk Indicators

Reviewers should look for:

- reused authorization decision ID;
- expired approval;
- stale timestamp;
- mismatched action digest;
- changed target resource;
- changed principal context;
- changed policy version;
- missing freshness check.

### Assessment Interpretation

Evidence integrity does not prevent misuse of old evidence by itself.

Replay controls require freshness, scope, expiration, and linkage to the actual action being dispatched or executed.

## Example 9: Selective Omission

### Scenario

Successful executions are logged, but denied, failed, escalated, or frozen actions are missing from the evidence store.

### Risk Indicators

Reviewers should look for:

- missing denial records;
- missing non-execution records;
- inconsistent counts between dispatcher and backend;
- absent failure events;
- unexplained gaps in sequence numbers;
- missing evidence for high-risk decision points.

### Assessment Interpretation

Selective omission can make a system appear safer than it is.

Tamper-evident evidence should help detect gaps, not only protect records that were successfully written.

## Example 10: Trusted Runtime or Attestation Reference

### Scenario

Evidence includes a reference to trusted runtime state, workload identity, secure boot, TPM, TEE, or remote attestation.

### Stronger Properties

Strong evidence includes:

- workload identity;
- code or image identity;
- policy version;
- runtime configuration reference;
- attestation reference;
- verification result;
- verification time;
- limitation of the attestation claim.

### Assessment Interpretation

Trusted runtime or attestation references can strengthen evidence that records were generated in an expected environment.

They do not prove policy correctness, approval quality, or action authorization by themselves.

## Review Questions

Assessors should ask:

1. Which component generated the evidence?
2. Can the assessed component modify or delete the evidence?
3. Can privileged administrators modify or delete the evidence without detection?
4. Is evidence append-only, write-restricted, signed, hash-linked, externally timestamped, independently corroborated, or otherwise integrity protected?
5. Can reviewers verify integrity after the fact?
6. Are verification results recorded?
7. Are deletion, redaction, retention, and rotation events recorded?
8. Are authorization, dispatch, execution, non-execution, reauthorization, approval, and override records correlated?
9. Can replay, reordering, truncation, or selective omission be detected?
10. Are evidence trust limitations documented?
11. Does the evidence prove integrity only, or does it also support action reconstruction?
12. Would incident responders be able to reconstruct the action lifecycle if one evidence source was compromised?

## Finding Patterns

Reviewers may record findings for:

- mutable local-only logs;
- agent self-reported evidence without corroboration;
- missing integrity verification;
- missing retention policy;
- missing deletion or redaction record;
- missing sequence, hash, signature, or timestamp reference for audit-grade evidence;
- evidence stored only in the component being assessed;
- unmonitored administrative modification capability;
- lack of independent corroboration for critical actions;
- replay of stale evidence;
- missing non-execution evidence;
- selective omission of failed or denied actions;
- inability to detect truncation or reordering;
- undocumented evidence trust limitations.

## Non-Goals

These examples do not require:

- blockchain;
- a specific SIEM;
- a specific cloud provider;
- a specific database;
- a specific cryptographic primitive;
- remote attestation for every action;
- tamper-evident storage for every action;
- raw prompt retention by default;
- full payload capture by default.

## Future Work

For non-normative tamper-evident evidence negative tests, see `docs/en/49-tamper-evident-evidence-negative-tests.md`.

Future AAEF work may decide whether to:

- add E5 JSON examples;
- add integrity fields to the Evidence Event Schema;
- define negative tests for evidence tampering;
- define minimum integrity expectations by evidence depth;
- define evidence replay tests;
- define selective omission tests;
- define incident-response evidence preservation guidance.
