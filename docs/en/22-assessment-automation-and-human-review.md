# Assessment Automation and Human Review Classification

This document provides draft guidance for classifying AAEF assessment activities by the degree to which they can be automated.

AAEF assessment includes both mechanical checks and judgment-based review.

Automated checks can improve consistency, completeness, and maintainability.

However, automated validation does not by itself establish security assurance, audit assurance, or implementation conformance.

## Purpose

The purpose of this guidance is to help implementers and assessors distinguish between:

- checks that can be automated,
- checks that can be partially automated but require human interpretation,
- checks that require human review,
- and checks that are manual or context-dependent.

This distinction helps prevent overclaiming.

A system may pass repository validation, schema validation, or mapping consistency checks while still lacking meaningful assurance for a high-impact action.

## Review Mode Classification

AAEF uses the following draft review mode categories.

| Review mode | Meaning | Typical examples |
|---|---|---|
| Automatable | The check can be performed mechanically with low interpretation burden. | Required fields, allowed values, duplicate IDs, schema validation, referential consistency. |
| Hybrid | Automation can collect, correlate, or flag evidence, but a human must interpret significance. | Evidence correlation, anomaly flags, threshold review, missing linkage warnings. |
| Human-reviewed | A human reviewer must evaluate meaning, context, or sufficiency. | Business authority, residual risk, compensating controls, evidence sufficiency. |
| Manual-only / Context-dependent | The review depends heavily on organizational context, interviews, architecture understanding, or judgment. | Governance maturity, accountability effectiveness, exception justification, operational reasonableness. |

These categories describe assessment method, not control importance.

A control can be highly important even if its assessment is manual or human-reviewed.

## What Can Be Automated

The following checks are generally suitable for automation.

| Area | Automatable checks |
|---|---|
| Control Catalog | Required columns, unique Control IDs, allowed maturity values, missing domains. |
| Assessment Worksheet | Required columns, row count consistency, allowed assessment result values, missing requirement references. |
| Assessment Profile Mapping | Control coverage, unknown Control IDs, domain mismatch, allowed applicability values. |
| Evidence Event Schema | JSON schema validation, required fields, allowed enum values, valid and invalid example behavior. |
| Documentation maintenance | Broken internal links, duplicate document numbers, line ending consistency, markdown formatting checks. |
| Evidence completeness | Presence of authorization IDs, action IDs, timestamps, principal identifiers, dispatch records, and result references. |

Automated checks are useful for detecting structural problems.

They are not sufficient to determine whether the evidence is meaningful for assurance.

## What Requires Hybrid Review

Hybrid review combines automated collection or detection with human interpretation.

Examples include:

- detecting that a high-impact action lacks a correlated authorization decision,
- flagging repeated near-threshold actions,
- identifying missing delegation chain references,
- detecting evidence events that are schema-valid but self-reported only,
- correlating tool dispatch records with backend execution logs,
- identifying inconsistent timestamps or missing result records,
- and highlighting actions that may require Evidence Quality Gate review.

Automation can surface these issues.

A human reviewer may still need to decide whether the issue is a finding, limitation, false positive, compensating control case, or acceptable residual risk.

## What Requires Human Review

The following assessment areas generally require human review.

| Area | Why human review is needed |
|---|---|
| Business authority | The reviewer must understand whether the principal had real authority for the action. |
| Intent-authority alignment | The reviewer may need workflow, business, or policy context. |
| Evidence sufficiency | The reviewer must judge whether evidence supports the assessment result. |
| Evidence Quality Gate outcome | The reviewer must assess assertion source, independence, tamper resistance, and reconstruction value. |
| Residual risk | The reviewer must evaluate risk in organizational and operational context. |
| Compensating controls | The reviewer must judge whether alternate controls actually reduce risk. |
| Human approval quality | The reviewer must assess whether approval was meaningful, informed, and action-bound. |
| Governance accountability | The reviewer must determine whether ownership and escalation paths are effective. |

Human review should be documented.

Where possible, the assessment should record:

- what was reviewed,
- who reviewed it,
- what evidence was used,
- what limitations were identified,
- what judgment was made,
- and what residual risk remains.

## Validation Is Not Assurance

Repository validation and schema validation are maintenance aids.

They do not constitute:

- a security assessment,
- an audit opinion,
- implementation conformance,
- certification,
- or proof that controls are operating effectively.

For example:

- a schema-valid evidence event may still be model-only self-reporting,
- a complete profile mapping may still contain draft applicability judgments,
- a valid assessment worksheet may still contain unsupported assessment results,
- and a repository with passing validators may still contain incomplete or incorrect guidance.

Automated validation should therefore be described as structural validation, not assurance.

## Relationship to Evidence Quality Gate

Evidence Quality Gate assessment is usually hybrid or human-reviewed.

Automation can help identify:

- missing evidence,
- missing correlation fields,
- missing authorization references,
- missing dispatch records,
- missing execution results,
- evidence generated only by the model or agent runtime,
- evidence that lacks source, method, confidence, or limitation metadata,
- and evidence events that do not match the expected schema.

However, a reviewer may still need to determine whether the evidence is strong enough to support a Pass, Partial, Fail, or Not Assessed result.

For high-impact actions, evidence quality depends on more than field presence.

It depends on whether evidence is action-bound, independently generated or corroborated, traceable to authorization and execution, protected against tampering, and appropriate for the action impact.

## Relationship to Assessment Profiles

Assessment profiles influence the expected review depth.

| Profile | Automation and review expectation |
|---|---|
| Lite | Basic automated checks and lightweight human review may be sufficient for low-risk, low-autonomy use cases. |
| Standard | Structural validation, evidence completeness checks, and human review of key control areas are expected. |
| High-Impact | Hybrid review is expected for authorization, dispatch, evidence quality, delegation, and sequence-level risks. |
| Audit-Grade | Stronger evidence correlation, retention checks, tamper-evidence review, and independent human review are expected. |

Higher profiles should not rely only on automated validation.

Audit-Grade review should be understandable to reviewers who were not involved in the implementation.

## Relationship to Action Sequence Monitoring

Action sequence monitoring is usually hybrid.

Automation can help correlate related actions and flag patterns such as:

- repeated near-threshold actions,
- repeated denied attempts,
- cumulative exports,
- staged infrastructure changes,
- delegated subtasks,
- and sequences that produce high-impact outcomes.

However, human review may be required to determine whether the sequence indicates policy evasion, excessive agency, legitimate workflow behavior, or acceptable operational activity.

## Suggested Assessment Recording

When recording assessment results, assessors may identify the review mode used.

Example values include:

- `Automatable`
- `Hybrid`
- `Human-reviewed`
- `Manual-only / Context-dependent`

For each assessed item, the reviewer may record:

- review mode,
- automated checks performed,
- human review performed,
- evidence reviewed,
- limitations,
- finding summary,
- and residual risk.

Future versions may add explicit worksheet fields for review mode classification.

## Non-Goals

This document does not:

- require full automation of AAEF assessments,
- define a certification program,
- replace human audit judgment,
- claim that passing validators proves security,
- require a specific GRC platform,
- require a specific SIEM or evidence pipeline,
- or define final worksheet fields for review mode classification.

## Draft Status

This document is draft guidance for v0.3.0.

It is intended to support future worksheet refinements, assessment tooling, evidence review workflows, and audit-oriented implementation guidance.
