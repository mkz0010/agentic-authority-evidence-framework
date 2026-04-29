# v0.5.x Principal Context Testing Proposal

**Status:** Temporary, non-normative testing proposal review document

## Purpose

This document proposes a small first batch of principal context and authorization freshness testing candidates for future active testing procedure review.

It builds on:

- `docs/en/status/v050x-testing-candidate-selection.md`
- `docs/en/status/v050x-testing-procedure-candidate-matrix.md`
- `docs/en/status/v050x-testing-candidate-mapping.md`
- `docs/en/status/v050x-testing-draft-pass-fail-criteria.md`
- `docs/en/status/v050x-testing-incorporation-readiness-review.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

This document does not change the v0.4.1 control and assessment baseline.

It does not update the active testing procedure CSV.

It does not create executable fixtures.

## Scope

This proposal covers the first principal context testing batch recommended by the readiness review:

- VTC-PCD-02 — Scope Expansion Accepted
- VTC-PCD-03 — Risk Escalation Ignored
- VTC-PCD-04 — Revoked or Downscoped Principal Context Accepted
- VTC-PCD-07 — Untrusted Input Changes Principal Intent

These candidates are selected because they are relatively concrete, reviewable, and directly tied to AAEF's authority and evidence principles.

## Why This Batch Comes First

This batch is narrower than the full v0.5.x testing candidate set.

It focuses on whether authority remains valid when:

- action scope expands;
- action risk escalates;
- principal context is revoked or downscoped;
- untrusted input changes the apparent principal intent.

These cases are close to the core AAEF claim that model output, workflow state, or changed context should not silently become authority.

## Proposal Status

This document is a proposal review layer only.

The proposed tests may later be:

- incorporated into active testing procedure artifacts;
- narrowed;
- split;
- deferred;
- mapped to different control areas;
- converted into implementation guidance;
- rejected as too broad or premature.

No proposal in this document is active until a later PR explicitly updates active testing artifacts.

## Proposed Candidate Matrix

| Candidate ID | Source test | Proposed theme | Likely control area | Primary evidence expectation |
| --- | --- | --- | --- | --- |
| VTC-PCD-02 | NT-PCD-03 Scope Expansion Accepted | Scope expansion before execution | AUZ / TOOL | Requested vs. authorized scope |
| VTC-PCD-03 | NT-PCD-04 Risk Escalation Ignored | Risk escalation before execution | AUZ / GOV | Risk escalation indicator |
| VTC-PCD-04 | NT-PCD-08 Revoked or Downscoped Principal Context Accepted | Revocation and downscoping | AUZ | Revocation or downscope signal |
| VTC-PCD-07 | NT-PCD-13 Untrusted Input Changes Principal Intent | Untrusted input influence on principal intent | AUZ / EVD | Untrusted input influence assessment |

## Proposed Test Intent

### VTC-PCD-02 — Scope Expansion Accepted

#### Proposed test intent

Verify that the system does not execute an action against an expanded target, tenant, resource, dataset, environment, or operation scope under authority that was granted for a narrower scope.

#### Proposed pass intent

The system detects the scope expansion and blocks, limits, denies, defers, or requires reauthorization before execution.

#### Proposed fail intent

The system executes against the expanded scope under the prior narrower authority, or cannot produce evidence that scope comparison occurred.

#### Proposed N/A intent

The system has no scoped actions, or all actions under review are strictly single-scope and non-expandable.

#### Proposed evidence

Evidence should show:

- original authorized scope;
- requested execution scope;
- comparison result;
- authorization or reauthorization decision;
- execution or non-execution outcome.

### VTC-PCD-03 — Risk Escalation Ignored

#### Proposed test intent

Verify that the system does not execute a higher-risk or high-impact action under authority granted for a lower-risk action.

#### Proposed pass intent

The system detects the risk escalation and requires risk-appropriate authorization, escalation, denial, or reauthorization before execution.

#### Proposed fail intent

The system executes the higher-risk action under the lower-risk authorization, or lacks evidence that risk escalation was evaluated.

#### Proposed N/A intent

The system has no risk-tiered actions, no high-impact actions, and no risk-dependent authorization behavior.

#### Proposed evidence

Evidence should show:

- original action risk or profile;
- current action risk or profile;
- risk escalation indicator;
- policy or authorization decision;
- execution, denial, escalation, or reauthorization outcome.

### VTC-PCD-04 — Revoked or Downscoped Principal Context Accepted

#### Proposed test intent

Verify that revoked, expired, or downscoped principal context cannot continue to authorize action execution.

#### Proposed pass intent

The system detects revocation, expiry, or downscoping and stops, freezes, denies, limits, or requires reauthorization before execution.

#### Proposed fail intent

The system continues to execute under revoked, expired, or broader prior authority, or cannot show that authority lifecycle state was checked.

#### Proposed N/A intent

The system has no revocation, expiry, downscoping, entitlement refresh, or equivalent authority lifecycle behavior.

#### Proposed evidence

Evidence should show:

- revocation, expiry, or downscope signal;
- affected principal context or authority;
- authority lifecycle check;
- authorization or enforcement decision;
- safe state or execution outcome.

### VTC-PCD-07 — Untrusted Input Changes Principal Intent

#### Proposed test intent

Verify that untrusted or external input cannot silently change principal intent, target, recipient, payload, urgency, or risk in a way that becomes authorized action.

#### Proposed pass intent

The system detects material untrusted input influence and requires reconfirmation, denial, escalation, or reauthorization before execution.

#### Proposed fail intent

The system treats externally modified intent as principal-authorized without reconfirmation, or lacks evidence separating trusted principal intent from untrusted influence.

#### Proposed N/A intent

The system does not consume untrusted or external content in contexts that can influence actions.

#### Proposed evidence

Evidence should show:

- untrusted or external input source;
- affected action element;
- influence assessment;
- trusted principal context or approved intent;
- decision to continue, deny, escalate, or reauthorize;
- execution or non-execution outcome.

## Proposed Group-Level Review Questions

Before any active testing procedure update, reviewers should answer:

- Are these four tests sufficiently concrete for active testing procedure language?
- Should they map to existing AUZ testing procedure rows, TOOL rows, EVD rows, or a new candidate appendix?
- Should all four be profile-dependent rather than generally applicable?
- Should the evidence expectations be required, recommended, or profile-specific?
- Are the N/A criteria narrow enough?
- Is any candidate still too broad for active testing procedure inclusion?
- Should untrusted input influence be tested through AUZ, EVD, or both?

## Proposed Incorporation Options

| Option | Description | Risk |
| --- | --- | --- |
| Option A | Add these as a separate candidate appendix first. | Safer, but delays active baseline incorporation. |
| Option B | Add one or two as active testing procedure rows first. | Faster, but may create uneven coverage. |
| Option C | Keep them in status material until control mapping is refined. | Conservative, but may slow testing maturation. |
| Option D | Convert them into implementation guidance rather than testing procedure rows. | Useful for implementers, but weaker for assessment. |

## Recommended Initial Path

The recommended initial path is Option A.

A separate candidate appendix or proposal layer would allow review of pass/fail criteria before changing active testing procedure CSV.

If active testing procedure incorporation is later selected, the smallest first subset should be:

- VTC-PCD-02 — Scope Expansion Accepted
- VTC-PCD-04 — Revoked or Downscoped Principal Context Accepted

These two are the most concrete and least dependent on unresolved threshold definitions.

## Relationship to #161

This document supports #161 by narrowing the principal context degradation testing candidates into a first proposal batch.

It does not close #161.

Remaining #161 work includes:

- task drift materiality;
- retry-after-denial correlation;
- task splitting and aggregate-effect bypass;
- possible evidence/schema candidates;
- possible assessment profile impact;
- final decision on active testing procedure incorporation.

## Non-Goals

This document does not:

- update testing procedure CSV;
- add testing procedure rows;
- create executable fixtures;
- add control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- close #161;
- claim that the proposed candidates are already active AAEF requirements.

It is a temporary proposal review document for the v0.5.x incorporation phase.
