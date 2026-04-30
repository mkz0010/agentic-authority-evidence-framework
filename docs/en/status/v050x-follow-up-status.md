# v0.5.x Follow-up Status

**Status:** Temporary, non-normative follow-up status document

## Purpose

This document summarizes the current status of the v0.5.x follow-up issues after the initial guidance and testing pass.

It is a temporary coordination document.

It may be removed, replaced, or archived when the v0.5.x follow-up incorporation decisions are complete.

This document does not change the v0.4.1 control and assessment baseline.

## Current Summary

The initial v0.5.x follow-up guidance/testing pass has been completed for the currently tracked follow-up issues #161 through #167.

These updates produced non-normative guidance and testing guidance documents.

They do not update:

- control catalog CSV;
- human-readable control requirements;
- assessment worksheet;
- assessment profiles;
- testing procedure CSV;
- external framework mapping CSV;
- evidence schema;
- evidence examples.

## Follow-up Issue Status

| Issue | Topic | Initial pass | Document | Remaining decision |
| --- | --- | --- | --- | --- |
| #161 | Principal context degradation testing criteria | PR #174 | `docs/en/59-principal-context-degradation-testing.md` | Decide whether degradation signals become testing procedure candidates, assessment profile inputs, evidence/schema candidates, or control refinements. |
| #162 | Capability-scoped cross-agent delegation controls | PR #171 | `docs/en/56-capability-scoped-cross-agent-delegation.md` | Decide whether guidance remains non-normative, refines existing controls, becomes testing/evidence/schema material, or becomes a future control requirement. |
| #163 | Delegation acceptance/refusal and chain accountability negative tests | PR #172 | `docs/en/57-cross-agent-delegation-negative-tests.md` | Decide which negative tests become testing procedure candidates, executable fixtures, evidence expectations, schema candidates, or control refinement criteria. |
| #164 | Cross-agent budget propagation guidance | PR #173 | `docs/en/58-cross-agent-budget-propagation.md` | Decide whether budget propagation remains guidance or becomes authority, governance, evidence, assessment, schema, testing, or control material. |
| #165 | Evidence integrity levels for high-impact and audit-grade profiles | PR #175 | `docs/en/60-evidence-integrity-profile-guidance.md` | Decide whether evidence integrity bands remain guidance or become assessment profile inputs, schema candidates, testing expectations, or control refinements. |
| #166 | Tamper-evident evidence requirements for selected contexts | PR #176 | `docs/en/61-tamper-evident-evidence-requirements.md` | Decide which contexts should require tamper-evident evidence and whether evidence fields, E5 examples, or testing candidates should be added. |
| #167 | Approval quality testing and evidence expectations | PR #177 | `docs/en/62-approval-quality-testing-guidance.md` | Decide which approval quality tests become testing procedure candidates, assessment profile inputs, evidence/schema candidates, or HUM control refinements. |

## Why the Issues Remain Open

The initial guidance/testing pass is complete.

The issues remain open because incorporation decisions are still pending.

The next step is not only to ask whether the concepts are useful, but to decide where each concept belongs.

Possible outcomes include:

- remain non-normative guidance;
- refine existing controls;
- become testing procedure candidates;
- become evidence expectations;
- become evidence schema candidates;
- become assessment profile guidance;
- become implementation guidance;
- become future control requirements;
- be deferred or split into later work.

## Incorporation Decision Axes

Future review should consider:

| Axis | Question |
| --- | --- |
| Control refinement | Should this concept modify existing control wording or add a future control requirement? |
| Testing procedure | Should this concept become a test case, pass/fail criterion, or executable fixture? |
| Evidence expectation | Should this concept define required, recommended, or optional evidence? |
| Schema candidate | Should new evidence fields be proposed? |
| Assessment profile | Should this concept affect profile selection, assurance level, or assessment depth? |
| Implementation guidance | Should this concept be implementation guidance rather than a control requirement? |
| Research question | Should this remain an open research topic? |
| Deferral | Should the concept remain out of scope for the next incorporation pass? |

## Review Priorities

Review is especially useful on:

- implementation feasibility;
- missing abuse cases;
- evidence and auditability gaps;
- whether negative tests represent realistic failure modes;
- whether proposed expectations are too strict, too vague, or too easy to bypass;
- where non-normative planning should become normative or assessment-relevant;
- where AAEF should avoid premature control, schema, or testing commitments.

## Relationship to Discussions

The public release and reviewer discussions have been updated to reflect the completion of the initial v0.5.x follow-up pass.

This document exists to keep the same status visible inside the repository.

## Removal or Archive Condition

This document should be removed, replaced, or archived when:

- all #161 through #167 incorporation decisions are resolved;
- the relevant follow-up issues are closed, split, or superseded;
- a later release incorporates the selected guidance into stable artifacts;
- or a new status document replaces this one.

## Non-Goals

This document does not:

- close any issue;
- promote any guidance to normative status;
- change the baseline;
- replace the changelog;
- replace release notes;
- replace the document map;
- define new control, testing, evidence, assessment, or schema requirements.

## Update after #189

PR #189 partially incorporated the principal context degradation testing work into active testing procedures.

The active testing procedure CSV was refined for:

- `AAEF-AUZ-02` — requested purpose, target resource, and applicable scope, including material scope expansion;
- `AAEF-AUZ-07` — material runtime state, including revocation, expiry, downscoping, and authority lifecycle state changes.

This update partially addresses #161.

#161 remains open because additional principal context degradation work is still pending, including:

- material task drift thresholds;
- retry-after-denial correlation;
- task splitting and aggregate-effect bypass criteria;
- whether VTC-PCD-03 and VTC-PCD-07 require additional active testing refinement;
- whether related evidence, schema, or assessment profile changes are needed.

## Update after #194

PR #194 partially incorporated the cross-agent delegation testing work into active testing procedures.

The active testing procedure CSV was refined for:

- `AAEF-DEL-01` — delegated scope mismatch, delegated capability, operation, target, resource, and downstream action comparison;
- `AAEF-DEL-05` — cross-agent authority lineage, communication-not-authority handling, and receiving-side validation evidence.

This update partially addresses #163.

#163 remains open because additional cross-agent delegation work is still pending, including:

- capability-scoped delegation refinement for `AAEF-DEL-02`;
- fire-and-forget delegation and explicit acceptance behavior;
- refusal propagation and resulting workflow state evidence;
- downstream redelegation authority;
- minimum delegation chain evidence expectations;
- whether related evidence, schema, control, or assessment profile changes are needed.

## Update after #199

PR #199 partially incorporated the approval quality testing work into active testing procedures.

The active testing procedure CSV was refined for:

- `AAEF-HUM-01` — what the approver actually saw, vague approval prompt handling, and action-bound approval context;
- `AAEF-AUZ-03` — canonical action matching, approval scope, approval state source, and independent approval enforcement before execution.

This update partially addresses #167.

#167 remains open because additional approval quality work is still pending, including:

- draft-vs-execute approval operation-class refinement;
- post-approval payload modification and materiality criteria;
- model-generated approval summary treatment as evidence;
- trusted approval evidence source expectations;
- approval fatigue and repeated approval interaction with HUM-02;
- whether related evidence, schema, control, or assessment profile changes are needed.

## Update after #201

PR #201 added the evidence integrity CSV refinement proposal.

The review determined that the first evidence integrity incorporation step does not require an immediate active testing procedure CSV change.

The existing active testing procedure row already provides substantial coverage:

- `AAEF-EVD-04` — critical and audit-grade evidence integrity, tamper-evident protection, append-only or write-restricted storage, cryptographic linkage, independent corroboration, deletion/redaction handling, replay, reordering, truncation, selective omission, and evidence trust limitations.

This update records #165 as already substantially represented in the current active testing procedure model through `AAEF-EVD-04`.

#165 remains open because additional evidence integrity work is still pending, including:

- deciding whether evidence integrity fields should be added to the Evidence Event Schema;
- defining E5 or higher-depth examples using tamper-evident evidence;
- defining minimum integrity expectations by evidence depth or action risk;
- defining negative tests for evidence tampering, deletion, replay, reordering, truncation, and selective omission;
- defining evidence replay tests;
- defining selective omission tests;
- defining incident-response evidence preservation guidance;
- deciding whether a later minor `AAEF-EVD-04` wording refinement is needed.

## Checkpoint after #202

After #202, the first incorporation review cycle for #161, #163, #165, and #167 is complete.

Current checkpoint:

- #161 principal context — first active CSV refinement incorporated; issue remains open.
- #163 cross-agent delegation — first active CSV refinement incorporated; issue remains open.
- #165 evidence integrity — substantially represented by existing `AAEF-EVD-04`; no immediate active CSV change required; issue remains open.
- #167 approval quality — first active CSV refinement incorporated; issue remains open.

For the consolidated checkpoint, see `docs/en/status/v050x-incorporation-review-checkpoint.md`.

The next phase should split remaining work into smaller tracks for evidence schema and examples, negative tests, delegation semantics, approval semantics, and cleanup/publication readiness.

## Update after #209, #210, and #211

PRs #209, #210, and #211 completed the first implementation wave for the v0.5.x evidence schema and examples track.

Implemented work:

- #209 added optional Evidence Event Schema fields for evidence integrity, evidence trust limitations, approval evidence source, approval-to-action binding, and execution-bound approval enforcement references.
- #210 added `examples/agentic-action-evidence-event.integrity-e5.json`.
- #211 added `examples/agentic-action-evidence-event.approval-binding.json`.

This completes the first schema-first, example-follow-up implementation sequence described in:

- `docs/en/status/v050x-evidence-schema-example-implementation-readiness.md`
- `docs/en/status/v050x-evidence-schema-field-proposal.md`
- `docs/en/status/v050x-evidence-example-design-proposal.md`

Current issue status:

- #165 remains open because evidence integrity negative tests, replay/reordering/selective omission tests, incident-response evidence preservation guidance, and any evidence-depth/profile decisions remain pending.
- #167 remains open because approval semantics, draft-vs-execute approval, post-approval modification, approval fatigue, and related HUM/AUZ/EVD testing decisions remain pending.
- #161 remains open because principal context freshness/degradation schema or profile treatment was explicitly deferred.
- #163 remains open because delegation lineage and receiving-side validation schema treatment was explicitly deferred.

No active testing procedure CSV changes were made in #209, #210, or #211.
