# AAEF v0.6.0 Risk Owner Guide Planning Draft

Status: Planning input  
Related roadmap: #241  
Related track: #247  
Related implementer track: #243  
Related operational track: #244  
Related legal/compliance track: #245  
Related architecture track: #246  
Parent planning synthesis: `docs/en/status/v060-planning-input-synthesis.md`  
Related implementer planning: `docs/en/status/v060-implementer-quick-start-planning.md`  
Related operational planning: `docs/en/status/v060-operational-responsibility-matrix-planning.md`  
Related legal/compliance planning: `docs/en/status/v060-legal-compliance-applicability-note-planning.md`  
Related architecture planning: `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document defines an initial planning draft for an AAEF Risk Owner Guide.

The purpose is to help risk owners and executive decision-makers evaluate whether high-impact agentic actions should be enabled, restricted, deferred, or rejected.

This document is planning material. It does not change active controls, assessment criteria, legal obligations, schema requirements, or the current control and assessment baseline.

## Intended audience

This planning draft is intended for:

- risk owners
- executives
- business owners
- governance committees
- security and technology leaders
- compliance and legal stakeholders
- product and platform owners
- AI adoption review boards
- auditors and assessors reviewing risk acceptance decisions

## Core risk owner question

A risk owner does not need to understand every implementation detail first.

The core question is:

> Should this organization allow this agentic system to perform or influence this high-impact action under these authority, evidence, operational, architecture, legal, and residual risk conditions?

The Risk Owner Guide should help decision-makers answer that question consistently.

## What risk owners should decide

For high-impact agentic actions, risk owners should decide:

- whether the action is in scope for agentic execution
- whether the action is high-impact
- whether the organization has enough authority control to permit execution
- whether the implementation can prevent model output from becoming authority
- whether dispatch and backend execution are bound to authorization
- whether evidence is sufficient for reconstruction
- whether operational owners are assigned
- whether legal and compliance boundaries are understood
- whether third-party responsibility gaps are acceptable
- whether residual risk should be accepted, reduced, transferred, avoided, or escalated

## Decision outcomes

The guide should support at least the following decision outcomes.

| Outcome | Meaning |
| --- | --- |
| Approve for limited pilot | The action may be tested under constrained scope, monitoring, and review. |
| Approve for production with conditions | The action may proceed if specified conditions, controls, and evidence expectations are met. |
| Defer | The action should not proceed until gaps are resolved. |
| Reject | The action should not be enabled due to unacceptable risk. |
| Escalate | The decision requires higher-level governance, legal, security, or executive review. |
| Approve exception temporarily | A temporary exception is allowed with scope, rationale, owner, expiration, and compensating measures. |

## Minimum decision inputs

A risk owner should have enough information to review the following areas before approving high-impact agentic action use.

| Input area | Candidate decision question |
| --- | --- |
| Action scope | What action will the agentic system perform or influence? |
| Impact level | Why is the action high-impact? |
| Principal and authority | On whose behalf is the action requested or authorized? |
| Authorization policy | What policy determines whether the action is allowed? |
| Approval model | Is human or organizational approval required? |
| Dispatch enforcement | Where is tool or action dispatch mediated? |
| Backend verification | Does the backend verify authorization before execution? |
| Evidence and reconstruction | Can the action lifecycle be reconstructed later? |
| Operational ownership | Who owns policy, dispatch, backend execution, evidence, monitoring, and incidents? |
| Legal/compliance boundaries | What claims are supported and what claims are avoided? |
| Third-party dependencies | Which SaaS, vendor, tool, or external agent responsibilities are outside direct control? |
| Monitoring and response | Who is alerted when evidence, authorization, or execution behavior is missing or inconsistent? |
| Freeze or rollback | Can high-impact execution be disabled or reduced quickly? |
| Residual risk | What risk remains after controls and evidence expectations are applied? |

## Candidate high-impact action decision matrix

The following decision matrix is an initial planning candidate.

| Decision area | Low concern | Review required | High concern |
| --- | --- | --- | --- |
| Action impact | Low business, security, legal, or financial impact | Material operational or customer impact | Safety, legal, financial, security, or irreversible impact |
| Authority clarity | Principal, delegation, and policy are clear | Some authority ambiguity exists | Principal or delegation is unclear |
| Authorization control | Explicit authorization decision exists | Authorization exists but weak binding or expiration | Model output or agent runtime effectively authorizes |
| Dispatch enforcement | High-impact action is mediated and fail-closed | Partial mediation or unclear failure behavior | Direct model-to-tool execution |
| Backend verification | Backend verifies decision before execution | Verification is partial or not universal | Backend executes without authority verification |
| Evidence quality | Trusted components generate reconstructable evidence | Evidence exists but has gaps | Agent-only or self-reported evidence |
| Operational ownership | Owners are assigned and escalation is clear | Some ownership gaps remain | No clear owner for policy, evidence, incidents, or risk |
| Third-party boundary | Responsibilities and evidence access are documented | Some external dependencies unclear | Critical responsibilities are outside visibility |
| Freeze and rollback | Disablement path exists and owner is assigned | Manual or delayed containment exists | No practical containment path |
| Residual risk | Explicitly accepted within defined limits | Needs risk owner review | Not acceptable without escalation |

## Candidate approval conditions

A risk owner may approve high-impact agentic action use with conditions.

Candidate conditions include:

- limit to a pilot scope
- limit to specific actions or resources
- require approval for high-risk action types
- require backend relying-party verification
- require trusted evidence generation
- require monitoring for missing or mismatched evidence
- require emergency freeze capability
- require exception expiration
- require periodic review of evidence quality
- require legal/compliance review before expansion
- require third-party responsibility mapping
- require executive review for residual high risk

## Candidate risk acceptance memo structure

The Risk Owner Guide may include a risk acceptance memo template.

Suggested sections:

1. decision title
2. action or system in scope
3. business purpose
4. high-impact action classification
5. authority model
6. authorization and approval model
7. dispatch and backend verification model
8. evidence and reconstruction model
9. operational ownership
10. legal and compliance applicability boundaries
11. third-party responsibility boundaries
12. known gaps and compensating measures
13. residual risk statement
14. approval conditions
15. exception expiration date where applicable
16. review cadence
17. approving risk owner
18. escalation path

## Candidate residual risk register fields

A future Risk Owner Guide may define a residual risk register template.

| Field | Purpose |
| --- | --- |
| `risk_id` | Unique residual risk identifier. |
| `related_action` | High-impact action or action family affected. |
| `risk_owner` | Person or role accountable for the residual risk. |
| `risk_statement` | Clear statement of the remaining risk. |
| `impact_area` | Business, security, legal, operational, safety, financial, or other impact area. |
| `current_controls` | AAEF-aligned or external controls currently in place. |
| `evidence_available` | Evidence supporting the control or residual risk decision. |
| `known_gaps` | Remaining gaps or limitations. |
| `treatment_decision` | Accept, reduce, transfer, avoid, defer, or escalate. |
| `conditions` | Conditions attached to approval or acceptance. |
| `expiration_or_review_date` | Date when risk acceptance or exception must be reviewed. |
| `status` | Open, accepted, mitigated, escalated, expired, or closed. |

## Candidate executive one-pager structure

Risk owners and executives may need a compressed adoption summary.

A future Executive One-Pager may include:

- what agentic action is being proposed
- why the action is high-impact
- what business value is expected
- what authority model is used
- how model output is prevented from becoming authority
- where dispatch and backend verification occur
- what evidence supports reconstruction
- who owns operations and residual risk
- what legal/compliance claims are avoided
- what third-party gaps remain
- what conditions or exceptions are attached
- what decision is requested

## Candidate KRI and KPI examples

The guide may include risk and performance indicators.

| Indicator | Type | Purpose |
| --- | --- | --- |
| High-impact actions executed | KPI | Shows operating volume under scope. |
| High-impact actions blocked | KRI / KPI | Shows policy enforcement and rejection patterns. |
| Authorization-to-dispatch mismatch rate | KRI | Detects divergence between decision and dispatch. |
| Backend verification rejection rate | KRI | Shows backend detection of invalid or mismatched execution. |
| Missing evidence rate | KRI | Detects evidence pipeline failure. |
| Exception count and age | KRI | Detects unmanaged bypasses. |
| Expired exceptions still active | KRI | Detects governance failure. |
| Incident reconstruction time | KPI / KRI | Measures ability to explain disputed actions. |
| Evidence retrieval time | KPI | Measures audit and review readiness. |
| Third-party responsibility gaps | KRI | Tracks unresolved external dependency risks. |
| Stale owner count | KRI | Detects responsibility drift. |

## Exception management expectations

Risk owners should not treat exceptions as permanent policy alternatives.

A future guide should define expectations for:

- exception owner
- exception rationale
- affected action scope
- affected systems or agents
- compensating controls
- monitoring expectations
- expiration date
- review cadence
- escalation path
- evidence required during the exception
- closure or renewal decision

## Board or executive reporting considerations

For board or executive reporting, AAEF should support concise reporting on:

- high-impact agentic actions in scope
- actions approved, deferred, rejected, or escalated
- current residual risk posture
- major exceptions and expired exceptions
- incidents and disputed actions
- evidence quality and reconstruction readiness
- third-party responsibility gaps
- material control or architecture gaps
- upcoming risk acceptance renewals
- decisions needed from leadership

The guide should avoid over-technical reporting that obscures accountability.

## Relationship to other v0.6.0 planning artifacts

### Implementer Quick Start

The Risk Owner Guide should use implementer planning to understand what the system actually does from action request through evidence generation.

### Operational Responsibility Matrix

The Risk Owner Guide should use operational planning to determine who owns policy, dispatch, evidence, incident response, freeze, rollback, exceptions, and residual risk.

### Legal and Compliance Applicability Note

The Risk Owner Guide should use legal/compliance planning to avoid unsupported compliance claims and to frame evidence as supplementary support rather than legal proof or certification.

### High-Impact Production Minimum Architecture Profile

The Risk Owner Guide should use architecture planning to determine whether minimum production architecture expectations are met before approving high-impact action use.

### Authorization Decision Artifact Minimal Profile

The Risk Owner Guide should use authorization artifact planning to understand how action authorization is bound to dispatch, backend verification, and evidence.

## Candidate anti-patterns

| Anti-pattern | Risk |
| --- | --- |
| Executive approval without action-level evidence | Decision-makers cannot understand what is actually being authorized. |
| Treating business value as sufficient justification | Risk controls, evidence, and accountability may be bypassed. |
| No named risk owner | Residual risk is not accountable. |
| No exception expiration | Temporary bypasses become permanent operating modes. |
| No third-party responsibility review | External dependency gaps remain hidden. |
| No freeze or rollback owner | Unsafe behavior cannot be contained quickly. |
| Overstating compliance claims | Legal or compliance assurance may be misleading. |
| No evidence quality review | Large volumes of logs may be mistaken for meaningful evidence. |
| Approving production before pilot constraints are defined | High-impact deployment may proceed without controlled learning. |

## Open questions

The following questions should be resolved before promoting this planning draft into an adoption-facing guide:

- Should the guide include a formal risk acceptance memo template?
- Should the High-Impact Action Decision Matrix be a standalone artifact?
- What minimum decision inputs should be required before production approval?
- Should pilot approval and production approval use separate decision criteria?
- Which KRIs and KPIs should be included in the first adoption-facing version?
- Should board reporting be a separate template?
- How should risk owners handle SaaS deployments where backend verification is not available?
- Should exception expiration be mandatory for high-impact agentic actions?
- How should this guide align with future assessment and audit materials?

## Acceptance criteria for this planning draft

This planning draft is sufficient when:

- risk owner decision inputs are defined
- decision outcomes are described
- a candidate high-impact action decision matrix is included
- risk acceptance memo structure is outlined
- residual risk register fields are identified
- KRI and KPI examples are identified
- exception management expectations are described
- board or executive reporting considerations are included
- relationships to other v0.6.0 planning artifacts are documented
- no active baseline change is implied
- #247 can use this document as input for a future Risk Owner Guide

## Expected next steps

Recommended next steps:

1. Review whether the decision matrix is suitable for high-impact action approval.
2. Decide whether to split the risk acceptance memo into a standalone template.
3. Decide whether executive one-pager and board reporting should be separate artifacts.
4. Review how this guide should handle SaaS and external-agent responsibility gaps.
5. Decide whether the eventual adoption-facing guide should remain in status material first or move into a risk-owner-oriented document path.
