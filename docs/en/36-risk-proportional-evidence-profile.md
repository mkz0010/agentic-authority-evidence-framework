# Risk-Proportional Evidence Profile

**Status:** Non-normative v0.5.0 planning profile
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Non-normative planning profile for evidence depth, assurance value, and operational overhead

> **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifacts, testing procedures, or release notes.

## Purpose

This document defines a non-normative Risk-Proportional Evidence Profile for AAEF v0.5.0 planning.

The purpose is to avoid two undesirable extremes:

1. requiring audit-grade evidence for every agentic action, which may create excessive performance, storage, privacy, and operational burden;
2. collecting minimal evidence for high-impact or critical actions, which may make authorization, incident reconstruction, and accountability impossible.

AAEF should scale evidence depth according to risk, impact, reversibility, authority complexity, evidence trust gaps, and operational context.

This document does not change the Evidence Event Schema, control catalog, assessment worksheet, or testing procedures.

## Core Principle

Evidence depth should be proportional to action risk and assurance need.

High-impact actions require evidence that can support review, correlation, and reconstruction. Critical or externally impactful actions may require stronger evidence, stronger integrity protections, longer retention, or additional verification.

Lower-risk actions may require less evidence, shorter retention, aggregation, sampling, or reduced detail where appropriate.

## Design Goals

Risk-proportional evidence should support:

- authorization review;
- non-execution review;
- incident reconstruction;
- delegation and authority lineage;
- cross-agent and cross-domain verification;
- reauthorization review;
- tamper-evident evidence planning;
- performance and storage manageability;
- privacy and sensitive-data minimization.

## Evidence Depth Levels

AAEF v0.5.0 planning may use evidence depth levels to describe expected evidence burden.

These levels are non-normative planning categories.

| Level | Name | Intended Use |
| --- | --- | --- |
| E0 | No AAEF evidence expected | Actions outside AAEF scope or non-agentic internal operations. |
| E1 | Minimal operational evidence | Low-risk actions where basic operational traceability is sufficient. |
| E2 | Standard action evidence | Routine in-scope agentic actions requiring correlation and review. |
| E3 | High-impact evidence | High-impact actions requiring authorization, dispatch, execution, and outcome correlation. |
| E4 | Audit-grade evidence | Critical, irreversible, externally impactful, delegated, cross-domain, or incident-relevant actions requiring stronger reconstruction and review. |
| E5 | Tamper-evident or independently verifiable evidence | Highest-assurance cases where evidence integrity, independent verification, or external review is required. |

## Candidate Evidence Depth Criteria

Evidence depth may increase when one or more of the following conditions apply:

- action is high-impact;
- action is critical or irreversible;
- action affects production systems, funds, legal rights, safety, security controls, customer data, or third parties;
- action crosses organizational, tenant, vendor, or trust-domain boundaries;
- action uses delegated authority;
- action uses external agents or cross-agent workflows;
- principal context is degraded, stale, ambiguous, or requires reconfirmation;
- reauthorization is required;
- non-execution, denial, deferral, escalation, freeze, or safe termination occurs;
- evidence is not independently generated or cannot be corroborated;
- evidence has integrity, completeness, or trust limitations;
- action is part of an incident, suspected compromise, or post-event investigation;
- action falls under regulatory, contractual, audit, or governance requirements.

## Evidence Depth Expectations

### E0: No AAEF Evidence Expected

E0 applies when an action is outside the AAEF assessment scope.

Examples:

- non-agentic internal operations;
- actions with no meaningful external effect;
- local draft generation with no tool execution;
- actions that do not use delegated or high-impact authority.

E0 should not be used for high-impact agentic actions.

### E1: Minimal Operational Evidence

E1 evidence may include:

- timestamp;
- agent or workflow identifier;
- action category;
- operational outcome;
- correlation reference where available.

E1 is not intended to support high-impact authorization review.

### E2: Standard Action Evidence

E2 evidence may include:

- agent identity;
- agent instance;
- principal reference where applicable;
- requested action;
- tool or workflow reference;
- correlation ID;
- timestamp;
- outcome;
- basic policy or decision reference.

E2 may be appropriate for routine in-scope actions that are reversible and low to moderate impact.

### E3: High-Impact Evidence

E3 evidence should support reconstruction of high-impact execution.

It may include:

- principal context;
- authority basis;
- authorization decision;
- delegated scope where applicable;
- tool dispatch reference;
- backend execution reference;
- input influence or trust boundary information where relevant;
- execution result;
- non-execution result where relevant;
- correlation and trace identifiers;
- evidence source and limitations.

E3 should be the default minimum for high-impact actions.

### E4: Audit-Grade Evidence

E4 evidence should support stronger review, audit, and incident reconstruction.

It may include:

- all relevant E3 fields;
- approval or reauthorization evidence;
- principal reconfirmation evidence;
- authority lineage;
- cross-agent or cross-domain evidence references;
- retry and task-splitting correlation;
- non-execution and safe termination details;
- evidence source classification;
- confidence or limitation statements;
- retention and review metadata;
- stronger correlation across authorization, dispatch, execution, and evidence components.

E4 may be appropriate for critical, irreversible, delegated, cross-domain, or externally impactful actions.

### E5: Tamper-Evident or Independently Verifiable Evidence

E5 evidence should support stronger integrity or independent verification.

It may include:

- all relevant E4 fields;
- signed evidence references;
- hash chains or append-only log references;
- external timestamping;
- remote attestation or trusted runtime references where applicable;
- independent evidence source correlation;
- write-once or append-only storage references;
- evidence integrity verification results;
- auditor-accessible verification records.

E5 is a planning category. It does not require a specific technology.

## Risk-to-Evidence Mapping

The following mapping is a planning guide, not a normative requirement.

| Scenario | Suggested Minimum |
| --- | --- |
| Low-risk reversible action | E1 or E2 |
| Routine in-scope tool action | E2 |
| High-impact action | E3 |
| High-impact delegated action | E3 or E4 |
| High-impact action with degraded principal context | E4 |
| Reauthorization-required action | E4 |
| Cross-agent or cross-domain high-impact action | E4 |
| Critical irreversible action | E4 or E5 |
| Incident-relevant action | E4 or E5 |
| Externally audited or regulated action | E4 or E5 |
| Tamper-evident evidence requirement | E5 |

## Performance and Storage Considerations

Evidence depth affects:

- latency;
- storage volume;
- indexing cost;
- retention cost;
- privacy exposure;
- sensitive data handling;
- SIEM ingestion volume;
- operational complexity;
- investigation usability.

Implementations should avoid collecting unnecessary sensitive data. Evidence should capture references, hashes, identifiers, policy versions, decision IDs, or structured summaries where those are sufficient for review.

Full payload capture should not be the default if it creates privacy, confidentiality, or data minimization risks.

## Evidence Minimization Guidance

Risk-proportional evidence should prefer:

- structured fields over raw prompts or raw model outputs;
- references over full content where possible;
- hashes over sensitive payloads where appropriate;
- policy identifiers over copied policy text;
- decision IDs over duplicated decision records;
- redacted or minimized values where full values are unnecessary;
- retention periods based on risk and obligation;
- separation between evidence metadata and sensitive content stores.

## Relationship to Tamper-Evident Evidence

Risk-proportional evidence and tamper-evident evidence are related but distinct.

Risk-proportional evidence asks:

> How much evidence is needed for this action?

Tamper-evident evidence asks:

> How strongly can this evidence be trusted after the fact?

Not every action needs tamper-evident evidence. However, critical, irreversible, cross-domain, or incident-relevant actions may require stronger evidence integrity guarantees.

For v0.5.0 planning, tamper-evident evidence storage is tracked separately in `docs/en/37-tamper-evident-evidence-storage.md`.

## Relationship to Evidence Event Schema

This profile may inform future Evidence Event Schema refinements.

Candidate future schema concepts include:

- `evidence_depth_level`;
- `risk_basis`;
- `assurance_level`;
- `retention_class`;
- `integrity_requirement`;
- `evidence_minimization_method`;
- `sensitive_data_handling`;
- `sampling_or_aggregation_basis`;
- `verification_requirement`.

These are planning candidates only.

## Relationship to Controls

This profile may inform future refinements to:

- `AAEF-EVD-*` evidence controls;
- `AAEF-AUZ-*` authorization controls;
- `AAEF-DEL-*` delegation controls;
- `AAEF-RES-*` response and revocation controls;
- assessment profiles;
- testing procedures.

The first v0.5.0 design preference is to use guidance and assessment language before adding new controls.

## Assessment Considerations

Assessors may ask:

1. Are evidence requirements proportional to action risk?
2. Are high-impact actions evidenced at least at an appropriate high-impact level?
3. Are critical or irreversible actions captured with audit-grade evidence?
4. Are cross-agent or cross-domain actions evidenced with authority lineage and evidence limitations?
5. Are reauthorization and non-execution outcomes evidenced?
6. Are evidence records excessive, duplicative, or privacy-invasive?
7. Are evidence minimization techniques used where appropriate?
8. Are retention and integrity expectations defined?
9. Are SIEM and audit ingestion volumes manageable?
10. Can incident reconstruction still be performed when evidence is minimized?

## Non-Goals

This profile does not require:

- audit-grade evidence for every action;
- tamper-evident storage for every evidence event;
- raw prompt or raw model output retention by default;
- full payload capture by default;
- a specific SIEM, log store, database, or tracing system;
- a specific cryptographic mechanism;
- a specific retention period;
- certification or compliance equivalence.

## Future Work

Future AAEF work may decide whether to:

- add an evidence depth field to the Evidence Event Schema;
- add assessment profile guidance for evidence depth;
- add testing procedures for risk-proportional evidence;
- define examples for E3, E4, and E5 evidence;
- define tamper-evident evidence storage expectations;
- define privacy and data minimization guidance for evidence records.

For v0.5.0 risk-proportional evidence assessment guidance, see `docs/en/43-risk-proportional-evidence-assessment-guidance.md`.
