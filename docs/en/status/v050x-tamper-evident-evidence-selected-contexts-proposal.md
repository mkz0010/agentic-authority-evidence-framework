# v0.5.x Tamper-Evident Evidence Selected Contexts Proposal

**Status:** Temporary, non-normative proposal

## Purpose

This document proposes selected contexts where tamper-evident evidence should be required, recommended, or optional in AAEF.

It follows the evidence integrity work completed for #165, including:

- `docs/en/status/v050x-issue-165-evidence-integrity-consolidation-checkpoint.md`
- `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md`
- `docs/en/status/v050x-negative-evidence-examples-fixtures-decision-proposal.md`
- `docs/en/status/v050x-evd01-evidence-sufficiency-limitation-review-proposal.md`

Primary source issue:

- #166 — define tamper-evident evidence requirements for selected contexts

Related rows:

- `AAEF-EVD-04`
- `AAEF-EVD-01`

This proposal does not update active testing procedures.

It does not update the Evidence Event Schema.

It does not add evidence examples.

It does not add validator fixtures.

It does not close #166 by itself.

## Background

The #165 workstream clarified that evidence integrity and tamper-evident evidence are important, but should remain mechanism-neutral.

It also clarified that:

- E5 is non-normative evidence depth vocabulary, not certification;
- evidence integrity failures are often semantic or assurance failures, not JSON Schema failures;
- `AAEF-EVD-04` already covers evidence integrity and tamper-evident evidence;
- `AAEF-EVD-01` already covers evidence sufficiency and reconstruction;
- incident-response evidence preservation can be described as guidance rather than active CSV requirements.

The next question is narrower:

> In which selected contexts should tamper-evident evidence be required, recommended, or optional?

## Proposed Context Tiers

This proposal uses three non-normative context tiers.

| Tier | Meaning |
| --- | --- |
| Required context | Tamper-evident evidence should normally be expected for this context. |
| Recommended context | Tamper-evident evidence is strongly recommended, but may depend on system risk, feasibility, and implementation maturity. |
| Optional context | Tamper-evident evidence may be useful, but should not be expected by default. |

These tiers are proposal language only.

They do not create certification levels.

They do not create schema values.

They do not create active CSV requirements until incorporated separately.

## Candidate Required Contexts

Tamper-evident evidence should be treated as required or near-required for contexts where action reconstruction, dispute handling, or post-incident accountability would otherwise be unreliable.

| Context | Rationale |
| --- | --- |
| High-impact external actions | External effects may be difficult to reverse and may create customer, legal, financial, or operational impact. |
| Financial transactions or refund actions | Amount, recipient, approval, authority, and execution records need strong reconstruction. |
| Access control changes | Privilege grants, revocations, role changes, and permission updates require trustworthy after-the-fact review. |
| Production configuration changes | Misconfiguration can cause security, availability, compliance, or customer impact. |
| Destructive data actions | Deletion, overwrite, purge, or irreversible mutation requires strong evidence of authority and execution. |
| Security control changes | Disabling monitoring, changing policy, modifying allowlists, or weakening enforcement requires strong evidence. |
| Cross-domain or delegated authority actions | Authority lineage and boundary validation need reconstruction across components. |
| Incident-response evidence packages | Preservation, review, and dispute handling require evidence integrity and explicit trust limitations. |
| Override, reauthorization, or emergency-path actions | Exceptional authority paths need reviewable justification and sequence evidence. |

## Candidate Recommended Contexts

Tamper-evident evidence should be recommended where action impact may be moderate or where evidence integrity materially improves review quality.

| Context | Rationale |
| --- | --- |
| High-volume automated operational changes | Volume increases the likelihood that selective omission or replay could hide issues. |
| Customer-visible content changes | External communications and published content may create reputational or contractual impact. |
| Data export or sharing actions | Evidence should support who authorized, what was exported, and where it was sent. |
| Toolchain actions involving multiple systems | Correlation across dispatcher, backend, and evidence systems reduces ambiguity. |
| Agent-to-agent delegation workflows | Delegation acceptance, refusal, scope, and chain accountability benefit from integrity evidence. |
| Approval-gated actions | Approval-to-execution binding benefits from tamper-evident records. |
| Audit-grade sample sets | Audit samples should preserve evidence depth and limitations for reviewer confidence. |

## Candidate Optional Contexts

Tamper-evident evidence may be optional where action impact is low or where ordinary operational logging is sufficient.

| Context | Rationale |
| --- | --- |
| Low-impact read-only actions | Tamper-evidence may not be proportionate unless privacy, regulated data, or dispute risk exists. |
| Local debugging traces | Useful for development, but not necessarily audit-grade evidence. |
| Non-production experiments | Tamper-evidence may be unnecessary unless experiments affect shared resources or security posture. |
| Ephemeral model reasoning artifacts | These may be retained as context, but should not be treated as authoritative evidence. |
| Low-risk recommendations without execution | Advice-only outputs generally do not need tamper-evident action evidence unless used to trigger action. |

## Proposed Requirement Factors

Whether tamper-evident evidence should be required should depend on the following factors.

| Factor | Higher need when... |
| --- | --- |
| Action impact | The action affects money, access, production, customers, safety, compliance, or external systems. |
| Reversibility | The action is hard to undo, destructive, or externally propagated. |
| Dispute likelihood | The action may be challenged by users, customers, operators, auditors, or regulators. |
| Delegation complexity | Authority crosses users, agents, services, tenants, or domains. |
| Approval dependency | Human or policy approval is required before execution. |
| Evidence fragility | Logs can be overwritten, truncated, selectively omitted, or generated only by the agent runtime. |
| Incident relevance | The action may be subject to incident response, legal hold, or forensic review. |
| Model-output risk | Model-generated summaries or agent self-reports may otherwise be overtrusted. |

## Candidate Decision Matrix

| Context | Suggested expectation | Notes |
| --- | --- | --- |
| High-impact external action | Required | Strong action-bound evidence should be expected. |
| Financial action | Required | Approval, authority, amount, recipient, and execution should be reconstructable. |
| Access control change | Required | Privilege changes require strong reviewability. |
| Production configuration change | Required | Requires correlation between authorization, dispatch, and backend change. |
| Destructive data mutation | Required | Deletion and overwrite actions require strong evidence. |
| Security control weakening | Required | Changes that reduce security posture require tamper-evident review. |
| Cross-domain delegated action | Required or Recommended | Depends on action impact and delegation boundary. |
| Approval-gated action | Recommended or Required | Required when high-impact or disputed. |
| Customer-visible communication | Recommended | May become required for regulated, contractual, or high-impact communications. |
| Data export action | Recommended or Required | Required when sensitive, regulated, or externally shared. |
| Low-impact read-only action | Optional | Escalate if privacy, regulated data, or incident context exists. |
| Non-production experiment | Optional | Escalate if it affects shared systems or security posture. |

## Relationship to `AAEF-EVD-04`

`AAEF-EVD-04` remains the primary active row for evidence integrity and tamper-evident evidence.

This proposal does not require active CSV modification.

A later review may decide whether `AAEF-EVD-04` should reference selected contexts more explicitly.

## Relationship to `AAEF-EVD-01`

`AAEF-EVD-01` remains the primary active row for evidence sufficiency and reconstruction.

Tamper-evident evidence is not automatically sufficient evidence.

Evidence must still support reconstruction of the assessed action, authority basis, decision path, dispatch or execution result, timing, and correlation identifiers.

## Relationship to E5 / Evidence Depth

E5 remains non-normative review vocabulary.

Selected contexts may describe where E5-style evidence is useful, but should not claim:

- E5 compliance;
- E5 certification;
- a required evidence-depth schema field;
- a universal audit score.

## Relationship to Incident Response

Incident-response contexts often increase the need for tamper-evident evidence.

When an incident or dispute occurs, preservation should include:

- original evidence records;
- verification results;
- failed or unavailable verification states;
- approval, authorization, dispatch, execution, and non-execution linkage;
- trust limitations;
- retention, redaction, or preservation records where relevant.

## Proposed Next Step

The recommended next step is a candidate appendix that expands these selected contexts into concrete scenarios.

Suggested planned filename:

- `v050x-tamper-evident-evidence-selected-contexts-candidate-appendix.md`

That appendix should define scenario-level expectations before any active CSV, schema, example, or validator change is considered.

## Non-Goals

This proposal does not:

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

It records selected-context proposal guidance before any active incorporation decision.

## Candidate Appendix

The tamper-evident evidence selected contexts candidate appendix is recorded in `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-candidate-appendix.md`.

The appendix expands the proposal into concrete selected-context candidates, expectation tiers, evidence package candidates, escalation rules, and incorporation considerations.
