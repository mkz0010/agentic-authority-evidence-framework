# Tamper-Evident Evidence Storage

**Status:** v0.5.0 planning profile
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative planning profile for evidence integrity, tamper evidence, and independent verification

## Purpose

This document defines a non-normative Tamper-Evident Evidence Storage profile for AAEF v0.5.0 planning.

The purpose is to describe how evidence records for high-impact agentic actions can remain reviewable and trustworthy after the fact, especially when the system being reviewed may be compromised, misconfigured, disputed, or operated across trust boundaries.

This document does not require a specific storage product, SIEM, database, cryptographic scheme, trusted execution environment, hardware root of trust, or remote attestation technology.

It is intended to support future design work for:

- evidence integrity;
- post-incident reconstruction;
- audit-grade evidence;
- independently verifiable evidence;
- cross-domain evidence exchange;
- authorization and execution correlation;
- non-execution and reauthorization evidence;
- evidence storage threat modeling.

## Core Principle

Evidence is useful only if reviewers can understand how much it can be trusted.

An evidence record that can be silently created, modified, replayed, suppressed, or deleted by the same component being assessed should not be treated as strong assurance by itself.

Tamper-evident evidence does not necessarily prevent tampering. It should make tampering, deletion, replay, reordering, or inconsistency detectable during review.

## Relationship to Risk-Proportional Evidence

Risk-proportional evidence asks:

> How much evidence is needed for this action?

Tamper-evident evidence asks:

> How strongly can this evidence be trusted after the fact?

Not every action requires tamper-evident storage.

Tamper-evident or independently verifiable evidence may be appropriate for:

- E4 audit-grade evidence;
- E5 tamper-evident or independently verifiable evidence;
- critical high-impact actions;
- irreversible actions;
- externally impactful actions;
- cross-agent or cross-domain actions;
- reauthorization-required actions;
- incident-relevant actions;
- actions subject to external audit, legal, regulatory, or contractual review.

For risk-proportional evidence planning, see `docs/en/36-risk-proportional-evidence-profile.md`.

## Evidence Integrity Threats

Tamper-evident evidence storage should consider threats such as:

- evidence deletion;
- evidence modification;
- evidence insertion after the fact;
- evidence replay;
- evidence reordering;
- timestamp manipulation;
- correlation ID manipulation;
- selective logging;
- local-only logging controlled by the component being assessed;
- model-generated or agent-generated self-reporting;
- administrator tampering;
- compromised evidence pipeline;
- inconsistent records across authorization, dispatch, execution, and evidence components;
- disputed cross-domain evidence;
- loss of evidence during incident response;
- retention gaps;
- clock drift or unsynchronized time sources.

## Candidate Integrity Levels

AAEF v0.5.0 planning may use integrity levels to describe evidence trust strength.

These levels are non-normative planning categories.

| Level | Name | Intended Use |
| --- | --- | --- |
| I0 | No integrity expectation | Evidence is outside AAEF scope or not relied upon. |
| I1 | Local operational log | Evidence is useful for debugging but not strong assurance. |
| I2 | Centralized controlled log | Evidence is collected by a controlled logging or evidence component. |
| I3 | Append-only or write-restricted evidence | Evidence is difficult to modify or delete without privileged access or trace. |
| I4 | Cryptographically linked or externally timestamped evidence | Evidence has hash chaining, signatures, external timestamping, or equivalent integrity references. |
| I5 | Independently verifiable or attested evidence | Evidence can be verified using independent systems, attestations, trusted runtime claims, or external review mechanisms. |

## Integrity Expectations by Evidence Depth

The following mapping is a planning guide, not a normative requirement.

| Evidence Depth | Suggested Integrity Expectation |
| --- | --- |
| E1 Minimal operational evidence | I1 or I2 |
| E2 Standard action evidence | I2 |
| E3 High-impact evidence | I2 or I3 |
| E4 Audit-grade evidence | I3 or I4 |
| E5 Tamper-evident or independently verifiable evidence | I4 or I5 |

## Candidate Storage Patterns

### Pattern 1: Centralized Evidence Pipeline

Evidence is emitted by authorization, dispatch, backend execution, and evidence components into a centralized evidence pipeline.

Useful properties:

- evidence is not stored only inside the agent runtime;
- evidence is correlated across components;
- evidence access can be controlled separately from the agent;
- deletion or modification can be monitored.

Limitations:

- centralized stores can still be modified by privileged operators;
- pipeline compromise can affect multiple evidence streams;
- centralized logs may not prove runtime integrity.

### Pattern 2: Append-Only Log

Evidence is written to an append-only or write-restricted log.

Useful properties:

- modification is more difficult than normal database updates;
- deletion or truncation may be detectable;
- useful for incident reconstruction.

Limitations:

- append-only behavior depends on storage and access controls;
- privileged administrators may still alter storage unless independently monitored;
- append-only does not automatically prove evidence correctness.

### Pattern 3: Hash Chain or Merkle Structure

Evidence records are linked using hashes, hash chains, Merkle roots, or similar structures.

Useful properties:

- record deletion, insertion, or reordering may be detectable;
- compact integrity proofs may be possible;
- supports later verification.

Limitations:

- hash chains prove consistency, not truth;
- key and root management are critical;
- weak timestamping or root storage can reduce assurance.

### Pattern 4: Digital Signature or Sealed Evidence

Evidence records or batches are signed or sealed by a trusted component.

Useful properties:

- supports attribution of evidence creation;
- helps detect modification;
- can support cross-domain evidence exchange.

Limitations:

- signing key protection is critical;
- signing a false or incomplete record does not make it true;
- key compromise or misuse must be handled.

### Pattern 5: External Timestamping or Anchoring

Evidence batches, hashes, or roots are timestamped or anchored outside the system being assessed.

Useful properties:

- helps detect backdating or after-the-fact insertion;
- supports external review;
- reduces reliance on local clocks.

Limitations:

- does not prove the underlying event was correct;
- introduces external dependency and cost;
- privacy-sensitive evidence should not be exposed directly.

### Pattern 6: Independent Evidence Source Correlation

Evidence is corroborated across independent or semi-independent sources.

Examples:

- authorization decision records;
- tool dispatch records;
- backend execution logs;
- cloud audit logs;
- SIEM events;
- workflow engine traces;
- database audit logs;
- ticketing or approval records;
- network or API gateway logs.

Useful properties:

- reduces reliance on a single component;
- supports inconsistency detection;
- improves incident reconstruction.

Limitations:

- correlation can be incomplete;
- independent systems may use different clocks or identifiers;
- sensitive data minimization remains necessary.

### Pattern 7: Trusted Runtime or Attestation Reference

Evidence includes references to trusted runtime state, secure boot, TPM, TEE, remote attestation, workload identity, or similar mechanisms where applicable.

Useful properties:

- may support claims that evidence was generated in an expected environment;
- may link evidence to runtime configuration;
- can strengthen cross-domain trust decisions.

Limitations:

- attestation is complex and environment-specific;
- attestation does not prove policy correctness by itself;
- trusted runtime claims should be tied to policy version, code identity, and evidence generation behavior.

## Candidate Evidence Integrity Metadata

Future evidence records may reference metadata such as:

- `evidence_integrity_level`;
- `evidence_store_id`;
- `append_only_reference`;
- `hash_chain_reference`;
- `merkle_root_reference`;
- `signature_reference`;
- `signing_key_id`;
- `external_timestamp_reference`;
- `attestation_reference`;
- `trusted_runtime_reference`;
- `integrity_verification_result`;
- `integrity_verification_time`;
- `retention_policy_reference`;
- `deletion_or_redaction_record`;
- `evidence_corroboration_reference`;
- `evidence_trust_limitation`.

These are planning candidates only.

## Evidence Trust Limitations

Tamper-evident evidence should disclose relevant limitations.

Examples:

- evidence generated by the same component being assessed;
- evidence not independently corroborated;
- evidence stored locally before upload;
- missing authorization correlation;
- missing dispatch correlation;
- missing backend execution correlation;
- missing non-execution evidence;
- incomplete timestamp synchronization;
- missing retention guarantee;
- missing integrity verification;
- administrative access to evidence store;
- cross-domain evidence not independently verifiable.

## Minimum Review Questions

Reviewers should be able to ask:

1. Which component generated the evidence?
2. Was the evidence generated by a trusted enforcement, authorization, backend, or evidence component?
3. Can the evidence be modified or deleted by the agent runtime?
4. Can the evidence be modified or deleted by the tool dispatcher?
5. Can the evidence be modified or deleted by the backend system?
6. Can privileged administrators modify or delete evidence without detection?
7. Are authorization, dispatch, execution, non-execution, and reauthorization records correlated?
8. Are timestamps reliable enough for reconstruction?
9. Is evidence stored in an append-only, write-restricted, signed, or externally anchored form?
10. Is evidence independently corroborated?
11. Are integrity verification results recorded?
12. Are retention, deletion, and redaction policies defined?
13. Are evidence trust limitations disclosed?
14. Can reviewers detect missing, reordered, replayed, or modified evidence?
15. Can incident reconstruction still proceed if one evidence source is compromised?

## Relationship to Controls

This profile may inform future refinements to:

- `AAEF-EVD-01`: evidence recording;
- `AAEF-EVD-02`: evidence correlation;
- `AAEF-EVD-03`: evidence independence and trust limitations;
- `AAEF-EVD-04`: evidence retention;
- `AAEF-EVD-05`: non-execution evidence;
- `AAEF-EVD-06`: reauthorization evidence;
- `AAEF-RES-03`: investigation and accountability;
- `AAEF-RES-04`: evidence preservation during incident response.

The first v0.5.0 design preference is to use planning guidance before adding new controls or schema fields.

## Relationship to Evidence Event Schema

For non-normative tamper-evident evidence examples, see `docs/en/42-tamper-evident-evidence-examples.md`.

This profile may inform future Evidence Event Schema refinements.

Candidate future schema concepts include:

- integrity level;
- storage reference;
- hash or signature reference;
- external timestamp reference;
- attestation reference;
- retention class;
- corroboration reference;
- integrity verification result;
- evidence trust limitation.

These are planning candidates only.

## Non-Goals

This profile does not require:

- blockchain;
- a specific SIEM;
- a specific cloud provider;
- a specific database;
- a specific cryptographic primitive;
- a specific remote attestation mechanism;
- a specific hardware root of trust;
- tamper-evident storage for every action;
- raw prompt or full payload retention;
- certification or compliance equivalence.

## Future Work

For non-normative tamper-evident evidence negative tests, see `docs/en/49-tamper-evident-evidence-negative-tests.md`.

Future AAEF work may decide whether to:

- add evidence integrity fields to the Evidence Event Schema;
- define E5 examples using tamper-evident evidence;
- strengthen evidence storage controls;
- define minimum integrity expectations for high-impact and critical actions;
- define negative tests for evidence tampering, deletion, replay, and reordering;
- define guidance for evidence preservation during incident response;
- map evidence integrity expectations to SIEM, WORM, append-only, signing, timestamping, or attestation technologies.
