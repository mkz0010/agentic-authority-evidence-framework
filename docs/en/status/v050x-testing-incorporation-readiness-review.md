# v0.5.x Testing Incorporation Readiness Review

**Status:** Temporary, non-normative testing incorporation readiness review

## Purpose

This document reviews selected v0.5.x testing candidates and classifies their readiness for possible future active testing procedure proposal.

It builds on:

- `docs/en/status/v050x-testing-candidate-selection.md`
- `docs/en/status/v050x-testing-procedure-candidate-matrix.md`
- `docs/en/status/v050x-testing-candidate-mapping.md`
- `docs/en/status/v050x-testing-draft-pass-fail-criteria.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

This document does not change the v0.4.1 control and assessment baseline.

It does not update the active testing procedure CSV.

It does not create executable fixtures.

It is intended to identify which selected candidates are closest to testing procedure incorporation and which still need refinement.

## Readiness Legend

| Readiness | Meaning |
| --- | --- |
| Ready for proposal | The candidate is sufficiently clear to be considered in a future active testing procedure proposal. |
| Needs refinement | The candidate is useful, but requires clearer thresholds, scope, evidence expectations, or profile applicability before active testing proposal. |
| Defer for now | The candidate should remain in guidance or status material for now. |

This readiness status is non-normative.

It does not make any candidate an active AAEF testing requirement.

## Readiness Review Criteria

A candidate is closer to active testing proposal when:

- the tested boundary is clear;
- the unsafe behavior is concrete;
- the expected safe behavior is reviewable;
- pass, fail, and N/A criteria are reasonably narrow;
- expected evidence can be produced by trusted components;
- the likely control area is clear;
- profile applicability is understandable;
- the candidate does not require broad unresolved design decisions.

A candidate needs refinement when:

- materiality thresholds are unclear;
- evidence expectations are too broad;
- implementation assumptions are too strong;
- the test may overlap with another candidate;
- profile applicability is not yet clear;
- the test requires correlation, aggregation, or timing rules that are not yet defined.

## Overall Readiness Summary

| Area | Ready for proposal | Needs refinement | Defer for now |
| --- | --- | --- | --- |
| Principal context degradation | 4 | 3 | 0 |
| Cross-agent delegation | 6 | 3 | 0 |
| Approval quality | 6 | 3 | 0 |
| Total | 16 | 9 | 0 |

No selected candidate is rejected at this stage.

Secondary candidates from the earlier selection document remain outside this readiness review.

## Principal Context Degradation Readiness

| Candidate ID | Readiness | Rationale | Recommended next action |
| --- | --- | --- | --- |
| VTC-PCD-01 | Needs refinement | Task drift is important, but material drift thresholds may vary by workflow and action class. | Define drift materiality examples before active testing proposal. |
| VTC-PCD-02 | Ready for proposal | Scope expansion is concrete, reviewable, and strongly tied to authorization and execution boundaries. | Consider for first active testing proposal batch. |
| VTC-PCD-03 | Ready for proposal | Risk escalation from low-risk to high-impact action is clear and profile-relevant. | Consider for first active testing proposal batch. |
| VTC-PCD-04 | Ready for proposal | Revocation, expiry, and downscope handling are clear authority lifecycle behaviors. | Consider for first active testing proposal batch. |
| VTC-PCD-05 | Needs refinement | Retry-after-denial is important, but correlation and material-change criteria need tighter definition. | Define retry correlation and material-change expectations. |
| VTC-PCD-06 | Needs refinement | Task splitting and aggregate-effect bypass are high value but require aggregate-effect correlation rules. | Define aggregate-effect and split-action correlation criteria. |
| VTC-PCD-07 | Ready for proposal | Untrusted input changing principal intent is central to AAEF and maps clearly to authorization and evidence review. | Consider for first active testing proposal batch. |

## Cross-Agent Delegation Readiness

| Candidate ID | Readiness | Rationale | Recommended next action |
| --- | --- | --- | --- |
| VTC-A2A-01 | Ready for proposal | Communication not implying delegation authority is a core cross-agent authority boundary. | Consider for first active testing proposal batch. |
| VTC-A2A-02 | Ready for proposal | Capability-scoped delegation is concrete and directly supported by current follow-up guidance. | Consider for first active testing proposal batch. |
| VTC-A2A-03 | Ready for proposal | Explicit acceptance before workflow continuation is reviewable and has clear failure behavior. | Consider for first active testing proposal batch. |
| VTC-A2A-04 | Ready for proposal | Refusal propagation is concrete and directly observable in workflow state. | Consider for first active testing proposal batch. |
| VTC-A2A-05 | Ready for proposal | Delegated scope mismatch maps cleanly to authorization and receiving-side validation. | Consider for first active testing proposal batch. |
| VTC-A2A-06 | Needs refinement | Unauthorized downstream redelegation is important, but redelegation authority semantics may need clearer scoping. | Define downstream redelegation authority and N/A criteria. |
| VTC-A2A-07 | Needs refinement | Delegation chain evidence is important for auditability, but required chain depth and evidence depth need clarification. | Define minimum reconstructable chain evidence expectations. |
| VTC-A2A-08 | Needs refinement | Budget/resource propagation is important, but resource types and thresholds need selected-context scoping. | Define high-impact or resource-consuming contexts first. |
| VTC-A2A-09 | Ready for proposal | Receiving-side validation is a clear, testable authority boundary. | Consider for first active testing proposal batch. |

## Approval Quality Readiness

| Candidate ID | Readiness | Rationale | Recommended next action |
| --- | --- | --- | --- |
| VTC-APP-01 | Ready for proposal | Vague approval prompt for high-impact action is concrete, reviewable, and central to meaningful approval. | Consider for first active testing proposal batch. |
| VTC-APP-02 | Ready for proposal | Draft-vs-execute mismatch is a clear operation-class binding failure. | Consider for first active testing proposal batch. |
| VTC-APP-03 | Ready for proposal | Canonical action mismatch is a clear approval-to-execution binding failure. | Consider for first active testing proposal batch. |
| VTC-APP-04 | Ready for proposal | Post-approval material modification is concrete and maps to approval invalidation. | Consider for first active testing proposal batch. |
| VTC-APP-05 | Needs refinement | Blind approval is important, but sufficient approval context may need profile-specific minimum fields. | Define minimum context fields for selected high-impact contexts. |
| VTC-APP-06 | Needs refinement | Batch approval hiding high-impact items is important, but itemization thresholds need clearer scope. | Define when item-level approval is required or recommended. |
| VTC-APP-07 | Needs refinement | Approval laundering after denial is important, but similarity/correlation thresholds need refinement. | Define denial-correlation and material-change expectations. |
| VTC-APP-08 | Ready for proposal | Rejecting model-only approval claims is core to “Model output is not authority.” | Consider for first active testing proposal batch. |
| VTC-APP-09 | Ready for proposal | Independent approval enforcement at execution boundary is concrete and testable. | Consider for first active testing proposal batch. |

## First Active Testing Proposal Candidate Set

The following candidates are closest to future active testing procedure proposal.

### Principal context degradation

- VTC-PCD-02 — Scope Expansion Accepted
- VTC-PCD-03 — Risk Escalation Ignored
- VTC-PCD-04 — Revoked or Downscoped Principal Context Accepted
- VTC-PCD-07 — Untrusted Input Changes Principal Intent

### Cross-agent delegation

- VTC-A2A-01 — Communication Treated as Delegation Authority
- VTC-A2A-02 — Agent Identity Treated as All-Purpose Delegation Authority
- VTC-A2A-03 — Fire-and-Forget Delegation
- VTC-A2A-04 — Refusal Not Propagated
- VTC-A2A-05 — Delegated Scope Mismatch Ignored
- VTC-A2A-09 — Receiving-Side Validation Missing

### Approval quality

- VTC-APP-01 — Vague Approval Prompt for High-Impact Action
- VTC-APP-02 — Approval to Draft Treated as Approval to Execute
- VTC-APP-03 — Canonical Action Mismatch
- VTC-APP-04 — Approval Payload Modified After Approval
- VTC-APP-08 — Model-Generated Approval Summary Accepted as Evidence
- VTC-APP-09 — Approval Without Independent Enforcement

## Candidates Requiring Refinement

The following candidates should remain in status material until refined.

| Candidate ID | Refinement needed |
| --- | --- |
| VTC-PCD-01 | Define material task drift thresholds and examples. |
| VTC-PCD-05 | Define retry correlation and material-change criteria. |
| VTC-PCD-06 | Define aggregate-effect and split-action correlation criteria. |
| VTC-A2A-06 | Define downstream redelegation authority scope. |
| VTC-A2A-07 | Define minimum reconstructable delegation chain evidence. |
| VTC-A2A-08 | Define selected contexts for budget/resource propagation testing. |
| VTC-APP-05 | Define minimum approval context fields for selected contexts. |
| VTC-APP-06 | Define batch itemization and high-impact item visibility thresholds. |
| VTC-APP-07 | Define approval laundering correlation and material-change criteria. |

## Incorporation Risk Notes

### Avoid importing all candidates at once

The ready set is still large.

Future work should consider smaller batches by theme, such as:

- principal context and authorization freshness;
- cross-agent delegation authority;
- approval quality and approval-to-execution binding.

### Avoid premature CSV changes

Even ready candidates should not be added to active testing procedure CSV until:

- target control area is accepted;
- row wording is concise enough for CSV use;
- pass/fail/N/A language is stable;
- evidence expectations are not overly broad;
- profile applicability is clear.

### Keep candidate IDs temporary

VTC IDs are temporary planning IDs.

They should not be treated as permanent test IDs unless a later release explicitly adopts them.

### Maintain non-normative status

This readiness review does not create active requirements.

It only identifies candidates that are closer to future proposal.

## Recommended Next Step

The next step should be to choose one small batch for active testing procedure proposal review.

Recommended first batch:

- VTC-PCD-02
- VTC-PCD-03
- VTC-PCD-04
- VTC-PCD-07

This batch is narrow enough to focus on principal context and authorization freshness before introducing cross-agent and approval quality changes.

A second possible batch would focus on cross-agent delegation authority.

A third possible batch would focus on approval quality and approval-to-execution binding.

## Non-Goals

This document does not:

- update testing procedure CSV;
- add testing procedure rows;
- create executable fixtures;
- add control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- close #161, #163, or #167;
- claim that ready candidates are already active AAEF requirements.

It is a temporary readiness review for the v0.5.x incorporation phase.
