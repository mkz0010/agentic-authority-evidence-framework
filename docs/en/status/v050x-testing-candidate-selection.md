# v0.5.x Testing Candidate Selection

**Status:** Temporary, non-normative testing candidate selection document

## Purpose

This document selects an initial subset of v0.5.x follow-up negative tests that may later be considered for testing procedure refinement.

It is part of Wave 1 from `docs/en/status/v050x-incorporation-decision-register.md`.

This document does not change the v0.4.1 control and assessment baseline.

It does not update the testing procedure CSV.

It does not create executable fixtures.

## Scope

This selection covers testing-oriented follow-up work from:

- #161 — Principal context degradation testing criteria
- #163 — Delegation acceptance/refusal and chain accountability negative tests
- #167 — Approval quality testing and evidence expectations

Related guidance documents:

- `docs/en/59-principal-context-degradation-testing.md`
- `docs/en/57-cross-agent-delegation-negative-tests.md`
- `docs/en/62-approval-quality-testing-guidance.md`

## Selection Principles

The initial candidate set should be smaller than the full planning-level test catalog.

A negative test is a stronger candidate when it:

- targets a high-impact failure mode;
- is likely to appear in real agentic systems;
- can be evaluated without excessive implementation-specific assumptions;
- maps to AAEF's core authority and evidence principles;
- supports clear expected safe behavior;
- supports clear evidence expectations;
- helps distinguish model output, communication, or approval from actual authority;
- can later be converted into testing procedure criteria or executable fixtures.

The purpose is not to import every planning-level negative test into testing procedures.

## Candidate Status Legend

| Status | Meaning |
| --- | --- |
| Selected candidate | Strong candidate for future testing procedure or fixture refinement. |
| Secondary candidate | Useful, but likely later or dependent on another candidate. |
| Defer for now | Keep as guidance until a clearer implementation or assessment need exists. |

## Summary

| Area | Source issue | Candidate count | Initial priority |
| --- | --- | --- | --- |
| Principal context degradation | #161 | 7 selected candidates | High |
| Cross-agent delegation | #163 | 9 selected candidates | High |
| Approval quality | #167 | 9 selected candidates | High |

## Principal Context Degradation Candidates

Source document:

- `docs/en/59-principal-context-degradation-testing.md`

| Test ID | Title | Status | Rationale |
| --- | --- | --- | --- |
| NT-PCD-02 | Task Drift Accepted Without Reconfirmation | Selected candidate | Directly tests whether narrow authorization is reused for broader action. |
| NT-PCD-03 | Scope Expansion Accepted | Selected candidate | Tests whether resource, tenant, account, dataset, or environment expansion requires reauthorization. |
| NT-PCD-04 | Risk Escalation Ignored | Selected candidate | Tests escalation from low-risk to high-impact action. |
| NT-PCD-08 | Revoked or Downscoped Principal Context Accepted | Selected candidate | Tests whether revoked or narrowed authority remains usable. |
| NT-PCD-10 | Retry After Denial Without Context Refresh | Selected candidate | Tests retry pressure after authority denial. |
| NT-PCD-11 | Task Splitting After Context Denial | Selected candidate | Tests aggregate-effect bypass after denial. |
| NT-PCD-13 | Untrusted Input Changes Principal Intent | Selected candidate | Tests whether untrusted input can change principal intent without reconfirmation. |
| NT-PCD-01 | Stale Session Context Accepted | Secondary candidate | Important, but freshness thresholds may require profile-specific guidance. |
| NT-PCD-05 | Role or Entitlement Change Ignored | Secondary candidate | Important, but may depend on identity and entitlement integration details. |
| NT-PCD-06 | Policy Version Change Ignored | Secondary candidate | Important for policy-driven systems, but may require policy versioning assumptions. |
| NT-PCD-07 | Environment Boundary Change Ignored | Secondary candidate | Often covered by scope expansion or risk escalation, but may remain useful separately. |
| NT-PCD-09 | Delegation After Context Degradation | Secondary candidate | Useful cross-link with cross-agent testing; may be covered after #163 prioritization. |
| NT-PCD-12 | Model Explanation Accepted as Fresh Principal Context | Secondary candidate | Important model-output principle, but may overlap with evidence-source tests. |

## Cross-Agent Delegation Candidates

Source document:

- `docs/en/57-cross-agent-delegation-negative-tests.md`

| Test ID | Title | Status | Rationale |
| --- | --- | --- | --- |
| NT-A2A-01 | Communication Treated as Delegation Authority | Selected candidate | Directly tests the core principle that communication is not delegation authority. |
| NT-A2A-02 | Agent Identity Treated as All-Purpose Delegation Authority | Selected candidate | Tests capability-scoped authorization rather than broad agent trust. |
| NT-A2A-03 | Fire-and-Forget Delegation | Selected candidate | Tests missing explicit acceptance before workflow continuation. |
| NT-A2A-04 | Refusal Not Propagated | Selected candidate | Tests whether refusal affects workflow state and downstream actions. |
| NT-A2A-06 | Delegated Scope Mismatch Ignored | Selected candidate | Tests capability, operation, and scope mismatch. |
| NT-A2A-10 | Unauthorized Downstream Redelegation | Selected candidate | Tests redelegation without downstream authority. |
| NT-A2A-12 | Broken Delegation Chain Evidence | Selected candidate | Tests accountability and reconstruction across agents. |
| NT-A2A-13 | Budget or Resource Constraint Not Propagated | Selected candidate | Tests resource amplification through delegation. |
| NT-A2A-17 | Receiving-Side Validation Missing | Selected candidate | Tests whether receiving side independently validates delegated authority. |
| NT-A2A-05 | Ambiguous Response Treated as Acceptance | Secondary candidate | Useful, but may be covered by explicit acceptance testing. |
| NT-A2A-07 | Target or Resource Boundary Mismatch | Secondary candidate | Often covered by scope mismatch but may be kept for cross-tenant contexts. |
| NT-A2A-08 | Stale Delegation Accepted | Secondary candidate | Useful when authority lifetime is defined. |
| NT-A2A-09 | Revoked or Downscoped Authority Accepted | Secondary candidate | Important but may overlap with principal context revocation tests. |
| NT-A2A-11 | Delegation Chain Depth Exceeded | Secondary candidate | Useful when depth limits are explicitly defined. |
| NT-A2A-14 | Retry After Refusal Without Material Change | Secondary candidate | Useful but may be handled after refusal propagation criteria are stable. |
| NT-A2A-15 | Task Splitting After Refusal | Secondary candidate | Important aggregate-effect bypass, but may depend on correlation capability. |
| NT-A2A-16 | Model-Generated Delegation Rationale Accepted as Evidence | Secondary candidate | Important model-output principle, but may be handled under evidence-source testing. |
| NT-A2A-18 | Refusal Evidence Overwritten by Later Success | Secondary candidate | Useful for audit-grade evidence testing. |

## Approval Quality Candidates

Source document:

- `docs/en/62-approval-quality-testing-guidance.md`

| Test ID | Title | Status | Rationale |
| --- | --- | --- | --- |
| NT-APP-01 | Vague Approval Prompt for High-Impact Action | Selected candidate | Tests whether approval prompt content is sufficient for high-impact action. |
| NT-APP-02 | Approval to Draft Treated as Approval to Execute | Selected candidate | Tests operation-class mismatch between approval and execution. |
| NT-APP-03 | Canonical Action Mismatch | Selected candidate | Tests approval-to-execution binding. |
| NT-APP-04 | Approval Payload Modified After Approval | Selected candidate | Tests whether approval is invalidated when action material changes. |
| NT-APP-05 | Blind Approval | Selected candidate | Tests missing approval context. |
| NT-APP-07 | Batch Approval Hides High-Impact Item | Selected candidate | Tests high-impact item visibility inside batch approval. |
| NT-APP-09 | Approval Laundering After Denial | Selected candidate | Tests reformulation, retry, or routing around denial. |
| NT-APP-12 | Model-Generated Approval Summary Accepted as Evidence | Selected candidate | Tests rejection of model-only approval claims. |
| NT-APP-15 | Approval Without Independent Enforcement | Selected candidate | Tests whether execution boundary verifies approval state. |
| NT-APP-06 | Rubber-Stamp Approval Pattern | Secondary candidate | Important, but may require thresholds such as count, dwell time, or timing windows. |
| NT-APP-08 | Approval Fatigue from Repeated Prompts | Secondary candidate | Important, but may require fatigue threshold definitions. |
| NT-APP-10 | Approval After Scope Expansion | Secondary candidate | Often covered by canonical action mismatch or scope expansion tests. |
| NT-APP-11 | Approval After Risk Escalation | Secondary candidate | Often covered by high-impact prompt and risk clarity tests. |
| NT-APP-13 | Approval State Overwritten | Secondary candidate | Useful for audit-grade evidence testing. |
| NT-APP-14 | Expired Approval Reused | Secondary candidate | Useful when approval validity windows are defined. |
| NT-APP-16 | Reauthorization Prompt Omits Prior Denial Context | Secondary candidate | Important, but may be handled with approval laundering and reauthorization work. |

## Initial High-Priority Test Set

The following set is recommended as the first testing procedure candidate review set.

### Principal context degradation

- NT-PCD-02 — Task Drift Accepted Without Reconfirmation
- NT-PCD-03 — Scope Expansion Accepted
- NT-PCD-04 — Risk Escalation Ignored
- NT-PCD-08 — Revoked or Downscoped Principal Context Accepted
- NT-PCD-10 — Retry After Denial Without Context Refresh
- NT-PCD-11 — Task Splitting After Context Denial
- NT-PCD-13 — Untrusted Input Changes Principal Intent

### Cross-agent delegation

- NT-A2A-01 — Communication Treated as Delegation Authority
- NT-A2A-02 — Agent Identity Treated as All-Purpose Delegation Authority
- NT-A2A-03 — Fire-and-Forget Delegation
- NT-A2A-04 — Refusal Not Propagated
- NT-A2A-06 — Delegated Scope Mismatch Ignored
- NT-A2A-10 — Unauthorized Downstream Redelegation
- NT-A2A-12 — Broken Delegation Chain Evidence
- NT-A2A-13 — Budget or Resource Constraint Not Propagated
- NT-A2A-17 — Receiving-Side Validation Missing

### Approval quality

- NT-APP-01 — Vague Approval Prompt for High-Impact Action
- NT-APP-02 — Approval to Draft Treated as Approval to Execute
- NT-APP-03 — Canonical Action Mismatch
- NT-APP-04 — Approval Payload Modified After Approval
- NT-APP-05 — Blind Approval
- NT-APP-07 — Batch Approval Hides High-Impact Item
- NT-APP-09 — Approval Laundering After Denial
- NT-APP-12 — Model-Generated Approval Summary Accepted as Evidence
- NT-APP-15 — Approval Without Independent Enforcement

## Why This Is Still Not a Testing Procedure Update

This document selects candidates only.

Before updating testing procedure artifacts, future work should define:

- the control or guidance target for each test;
- the tested system boundary;
- test preconditions;
- expected evidence;
- pass criteria;
- fail criteria;
- not applicable criteria;
- profile applicability;
- whether the test is manual, review-based, or executable;
- whether the test belongs in existing testing procedure rows or new candidate testing material.

## Recommended Next Step

The next step should be a smaller PR that turns selected candidates into a draft testing procedure candidate matrix.

That PR should still avoid directly modifying the active testing procedure CSV unless the pass/fail language is ready for baseline review.

A possible next document is:

- a future testing procedure candidate matrix document

## Non-Goals

This document does not:

- update testing procedure CSV;
- create executable fixtures;
- add control IDs;
- change the evidence schema;
- change assessment profiles;
- close #161, #163, or #167;
- claim that all selected candidates must become normative tests.

It is a temporary selection document for the v0.5.x incorporation phase.
