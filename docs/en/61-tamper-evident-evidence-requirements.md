# Tamper-Evident Evidence Requirements Guidance

**Status:** Non-normative v0.5.x follow-up guidance

## Purpose

This document defines non-normative guidance for deciding when tamper-evident evidence should be required, strongly recommended, recommended, optional, or unnecessary for selected AAEF contexts.

It addresses follow-up work from the v0.5.0 Tamper-Evident Evidence Storage and Evidence Integrity Levels planning material.

The purpose is to clarify how tamper-evident evidence relates to high-impact actions, audit-grade review, cross-agent delegation, authority denial, incident reconstruction, and evidence integrity.

This document does not add new control IDs, change the evidence schema, change testing procedures, or change the v0.4.1 control and assessment baseline.

## Core Principle

Tamper-evident evidence should be used where later alteration, deletion, omission, replay, or selective preservation of evidence would materially impair authority review, incident reconstruction, auditability, or accountability.

Tamper-evident evidence is not required for every action.

AAEF should prefer risk-proportional evidence integrity rather than universal heavyweight logging.

## Tamper-Evident Evidence Is Not Complete Evidence

Tamper-evident evidence helps show that a record has not been altered without detection.

It does not by itself prove that:

- the record is complete;
- the record is relevant;
- the original action was authorized;
- the executed action matched the authorized action;
- all related events were captured;
- the evidence was independently generated;
- the evidence is sufficient for assessment;
- the system behaved safely.

Evidence integrity and evidence completeness should be assessed separately.

## Requirement Posture Categories

The following categories are non-normative planning guidance.

| Posture | Meaning |
| --- | --- |
| Required candidate | Future work should consider whether tamper-evident evidence should become a required expectation for this context. |
| Strongly recommended | Tamper-evident evidence is usually appropriate, but future normative incorporation is still needed. |
| Recommended | Tamper-evident evidence may improve assurance but may be balanced against cost, privacy, or operational burden. |
| Optional | Basic attributable evidence may be sufficient for many implementations. |
| Usually unnecessary | Tamper-evident evidence is unlikely to add proportionate value for low-risk contexts. |

These categories do not create current AAEF requirements.

## Selected Context Guidance

The following table provides planning-level guidance for selected contexts.

| Context | Suggested posture | Rationale |
| --- | --- | --- |
| Low-risk local action | Usually unnecessary | Heavyweight integrity may exceed assurance value. |
| Internal reversible action | Optional | Basic attributable evidence may be sufficient. |
| Sensitive data access | Recommended | Later alteration may impair privacy or access review. |
| Privileged tool use | Recommended or strongly recommended | Enforcement evidence may need protection from alteration. |
| Production change | Strongly recommended | Incident reconstruction and rollback analysis often depend on preserved evidence. |
| Financial or resource-consuming action | Strongly recommended | Budget, approval, and execution evidence may be disputed later. |
| Destructive or irreversible action | Strongly recommended | Review depends on reliable action and authorization evidence. |
| Externally effective communication | Recommended or strongly recommended | External effects may require reconstruction of authorization and payload. |
| Cross-agent delegation | Strongly recommended | Delegation chains may otherwise become difficult to reconstruct. |
| Cross-domain or cross-tenant action | Strongly recommended | Boundary-crossing actions need stronger evidence integrity. |
| High-impact action | Strongly recommended, required candidate in selected cases | Evidence alteration could materially impair accountability. |
| Audit-grade assessment context | Required candidate or strongly recommended | Independent review may require stronger evidence integrity. |
| Incident response preservation | Required candidate | Evidence should be preserved after suspected failure, abuse, or security event. |
| Denial, refusal, or reauthorization path | Recommended or strongly recommended | Failed or blocked attempts may be as important as successful actions. |

This table is guidance only.

Future work should decide which contexts become normative requirements, testing criteria, assessment profile inputs, or evidence schema candidates.

## Candidate Required Contexts

Future AAEF work may consider required tamper-evident evidence for selected contexts such as:

- high-impact action execution;
- privileged production changes;
- destructive or irreversible actions;
- cross-agent delegation chains for high-impact actions;
- cross-domain or cross-tenant authority transfer;
- externally effective actions with legal, financial, operational, or safety impact;
- post-denial execution attempts;
- reauthorization after denial, refusal, expiry, or revocation;
- incident response evidence preservation;
- audit-grade assessment profiles.

These are candidate contexts only.

## Candidate Evidence Properties

Tamper-evident evidence may include one or more of the following properties:

- append-only recording;
- write-restricted evidence store;
- signed evidence records;
- hash-linked event chains;
- sequence numbers;
- external timestamping;
- retention lock;
- immutable or WORM storage;
- independent corroborating logs;
- deletion or redaction records;
- access-controlled evidence modification path;
- audit trail for evidence access;
- evidence export integrity checks;
- linkage to authorization, dispatch, execution, and outcome records.

AAEF should define evidence properties before mandating specific technologies.

## Candidate Evidence Fields

Future schema or guidance work may consider fields such as:

- evidence integrity level;
- tamper-evident mechanism type;
- evidence record hash;
- previous record hash;
- signature identifier;
- signing component;
- timestamp source;
- sequence number;
- retention policy;
- retention lock indicator;
- evidence store identifier;
- evidence writer identity;
- evidence access log reference;
- deletion or redaction record reference;
- external corroboration reference;
- incident preservation flag;
- chain verification result;
- evidence completeness limitation.

These fields are candidates only.

They are not required evidence schema fields in this document.

## Evidence Preservation for Denial and Refusal

Tamper-evident evidence should not be limited to successful actions.

Denied, refused, deferred, escalated, expired, revoked, or reauthorization-required actions may be important evidence.

This is especially true when:

- an agent retries after denial;
- an agent splits a denied action into smaller actions;
- an agent routes around a refusing component;
- a later successful action overwrites earlier failure evidence;
- an incident investigation depends on understanding blocked attempts.

Future work should consider whether selected denial and refusal paths require tamper-evident preservation.

## Evidence Preservation for Incident Response

Incident response contexts may require stronger preservation than ordinary operations.

Tamper-evident evidence may be especially important when:

- authority misuse is suspected;
- prompt injection or indirect prompt injection is suspected;
- cross-agent delegation abuse is suspected;
- high-impact action execution is disputed;
- evidence omission or replay is suspected;
- a workflow crossed tenant, domain, environment, or production boundaries;
- human approval may have been spoofed, fatigued, or laundered;
- the agent retried after denial or refusal.

In these cases, evidence should support reconstruction of the action chain, not just final outcome reporting.

## Relationship to Evidence Integrity Levels

Tamper-evident evidence corresponds most closely to stronger evidence integrity bands such as EI-4 or EI-5 in `docs/en/60-evidence-integrity-profile-guidance.md`.

However:

- EI-4 or EI-5 evidence may require more than tamper-evident storage;
- tamper-evident storage does not guarantee completeness;
- audit-grade evidence also requires reviewability, attribution, retention, and action linkage;
- high-integrity evidence should still be risk-proportional.

## Relationship to Evidence Depth

Evidence depth and tamper-evidence are different.

A system can have many evidence records that are mutable and weak.

A system can have tamper-evident records that omit important context.

For high-impact or audit-grade contexts, future work should consider both:

- whether enough evidence exists;
- whether the evidence is sufficiently protected.

## Implementation-Neutral Mechanisms

AAEF does not require a specific tamper-evident evidence technology.

Possible mechanisms may include:

- append-only logs;
- WORM storage;
- cloud retention lock;
- signed event records;
- hash chains;
- Merkle trees;
- external timestamping;
- transparency logs;
- independent SIEM ingestion;
- write-restricted evidence pipelines;
- separate evidence accounts or tenants;
- database audit logs;
- immutable object storage;
- hardware-backed signing;
- notarized exports.

These mechanisms are examples only.

AAEF should define the evidence integrity and reviewability properties required rather than mandate a specific implementation.

## Privacy and Retention Tradeoffs

Tamper-evident evidence may increase privacy, retention, and operational risk.

Potential tradeoffs include:

- retention of sensitive data;
- difficulty correcting or deleting erroneous records;
- conflict with data minimization goals;
- increased storage cost;
- increased review burden;
- long-term exposure if evidence stores are compromised;
- complexity around redaction and legal hold;
- cross-border or tenant-specific retention constraints.

Future guidance should distinguish between:

- preserving evidence metadata;
- preserving sensitive payloads;
- preserving hashes or references;
- preserving redaction records;
- preserving derived or minimized evidence.

Tamper-evident evidence should be designed with data minimization and retention limits in mind.

## Anti-Patterns

| Anti-pattern | Risk |
| --- | --- |
| Requiring tamper-evident evidence for every action | Creates unnecessary cost, privacy, and review burden. |
| Treating ordinary mutable logs as tamper-evident | Evidence may be changed or deleted without detection. |
| Treating tamper-evident storage as proof of authorization | Integrity does not prove authority. |
| Preserving only successful actions | Denials, refusals, retries, and bypass attempts may be lost. |
| Preserving evidence without action linkage | Evidence may not support reconstruction. |
| Preserving evidence without authorization linkage | Reviewers may not know why action was allowed. |
| Preserving payloads unnecessarily | Privacy and retention burden may exceed assurance value. |
| Allowing evidence deletion without redaction record | Selective omission may become undetectable. |
| Relying on model-generated summaries as tamper-evident evidence | Model output is not independently generated evidence. |

## Candidate Testing Themes

Future testing work may include:

- evidence modification after action execution;
- deletion of denial or refusal records;
- replay of earlier authorization evidence;
- selective omission of failed validation events;
- reordering of action evidence;
- truncation of delegation chain evidence;
- overwrite of earlier refusal by later success;
- missing evidence for reauthorization;
- missing evidence for budget expansion;
- tamper-evident record without authorization linkage;
- tamper-evident record without execution linkage.

These are candidate testing themes only.

## Relationship to Existing AAEF Materials

This document relates to:

- `docs/en/37-tamper-evident-evidence-storage.md`
- `docs/en/42-tamper-evident-evidence-examples.md`
- `docs/en/49-tamper-evident-evidence-negative-tests.md`
- `docs/en/51-evidence-integrity-levels.md`
- `docs/en/60-evidence-integrity-profile-guidance.md`

It also supports the v0.5.x follow-up issue for tamper-evident evidence requirements in selected contexts.

## Future Incorporation Questions

Future work should decide:

- which selected contexts should require tamper-evident evidence;
- which contexts should only recommend it;
- whether evidence integrity fields should become schema candidates;
- whether E5 examples should be added;
- whether tamper-evident evidence should affect assessment profiles;
- which negative tests should become testing procedure candidates;
- how incident-response evidence preservation should be represented;
- how tamper-evident evidence should interact with privacy, minimization, redaction, and retention requirements;
- whether audit-grade evidence profiles should include tamper-evident evidence expectations.

## Non-Goals

This document does not:

- add new control IDs;
- change the control catalog;
- change the evidence schema;
- change evidence examples;
- change testing procedures;
- require tamper-evident evidence for all actions;
- mandate a specific SIEM, storage, cryptographic, cloud, or logging technology;
- claim that tamper-evident evidence proves authorization, completeness, or correctness;
- require retention of sensitive payloads where minimized evidence would be sufficient.

Any normative incorporation must be handled through a later PR that explicitly updates the relevant control, testing, evidence, assessment, schema, mapping, or release artifacts.
