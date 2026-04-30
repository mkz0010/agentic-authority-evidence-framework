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

## Update after evidence integrity testing row review

After #215, the active `AAEF-EVD-04` testing procedure row was reviewed for evidence integrity negative testing coverage.

Review result:

- No active CSV refinement is required at this time.
- The existing `AAEF-EVD-04` row already covers alteration, deletion, replay, reordering, truncation, selective omission, integrity verification, retention/deletion/redaction records, and evidence trust limitations.
- The attempted active CSV refinement branch produced no repository changes and was deleted without a PR.

Current issue status:

- #165 remains open because incident-response evidence preservation guidance, evidence depth/profile decisions, possible evidence integrity negative examples or validator fixtures, and later evidence sufficiency / limitation review remain pending.
- `AAEF-EVD-04` does not need immediate active CSV modification based on the current review.

## Incident-Response Evidence Preservation Guidance Proposal

The incident-response evidence preservation guidance proposal is recorded in `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md`.

This proposal addresses a remaining #165 work area after the evidence integrity negative testing review.

## Incident-Response Evidence Preservation Candidate Appendix

The incident-response evidence preservation candidate appendix is recorded in `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md`.

This appendix adds concrete preservation scenarios and reviewer-facing preservation package candidates for #165.

## Update after #217 and #218

PRs #217 and #218 completed the current v0.5.x incident-response evidence preservation planning sequence for #165.

Implemented work:

- #217 added `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md`.
- #218 added `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md`.

Current result:

- Incident-response evidence preservation now has both a guidance proposal and a detailed candidate appendix.
- The candidate appendix covers preservation levels, preservation scenarios, evidence packages, reviewer checklist candidates, and anti-patterns.
- No active testing procedure CSV change is required from #217 or #218.
- No Evidence Event Schema change is required from #217 or #218.
- No evidence example or validator fixture change is required from #217 or #218.

Current #165 status:

- The incident-response evidence preservation portion is substantially addressed for the current v0.5.x follow-up cycle.
- #165 remains open because evidence depth / E5 profile decisions, possible negative examples or validator fixtures, possible `AAEF-EVD-01` evidence sufficiency / limitation review, and temporary-document consolidation remain pending.

## Evidence Depth and E5 Profile Decision Proposal

The evidence depth and E5 profile decision proposal is recorded in `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md`.

The proposal recommends treating E5 as non-normative evidence depth terminology for examples, review, and future guidance, not as a certification level, required schema value, or active testing procedure requirement.

## Update after #220

PR #220 added the v0.5.x evidence depth and E5 profile decision proposal.

Implemented work:

- #220 added `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md`.

Current result:

- E5 is treated as non-normative evidence depth terminology for examples, review, and future guidance.
- E5 is not treated as a certification tier, formal profile, required schema value, active CSV requirement, or scoring scale in the current v0.5.x cycle.
- No active testing procedure CSV change is required from #220.
- No Evidence Event Schema change is required from #220.
- No evidence example or validator fixture change is required from #220.

Current #165 status:

- Evidence integrity schema support, integrity-focused example, evidence integrity negative test planning, incident-response preservation guidance, incident-response preservation candidate coverage, and E5/evidence depth decision work are now substantially addressed for the current v0.5.x follow-up cycle.
- #165 remains open because possible negative examples or validator fixtures, possible `AAEF-EVD-01` evidence sufficiency / limitation review, and temporary-document consolidation remain pending.

## Negative Evidence Examples and Validator Fixtures Decision Proposal

The negative evidence examples and validator fixtures decision proposal is recorded in `docs/en/status/v050x-negative-evidence-examples-fixtures-decision-proposal.md`.

The proposal recommends not adding schema-invalid validator fixtures or negative evidence examples immediately. It distinguishes structural schema validity from semantic evidence sufficiency and treats schema-valid negative evidence examples as possible future reviewer-facing guidance.

## Update after #222

PR #222 added the v0.5.x negative evidence examples and validator fixtures decision proposal.

Implemented work:

- #222 added `docs/en/status/v050x-negative-evidence-examples-fixtures-decision-proposal.md`.

Current result:

- Schema-invalid validator fixtures are not added in the current v0.5.x cycle.
- Schema-valid negative evidence examples are deferred.
- `tools/validate_evidence_schema.py` remains focused on structural schema validation.
- Evidence integrity failure is treated primarily as a semantic or assurance issue, not a JSON Schema validity issue.
- Reviewer-facing negative examples remain candidate future work.

Current #165 status:

- Evidence integrity schema support, integrity-focused example, evidence integrity negative test planning, incident-response preservation guidance, incident-response preservation candidate coverage, E5/evidence depth decision work, and negative example / validator fixture decision work are now substantially addressed for the current v0.5.x follow-up cycle.
- #165 remains open because possible `AAEF-EVD-01` evidence sufficiency / limitation review and temporary-document consolidation remain pending.

## AAEF-EVD-01 Evidence Sufficiency and Limitation Review Proposal

The `AAEF-EVD-01` evidence sufficiency and limitation review proposal is recorded in `docs/en/status/v050x-evd01-evidence-sufficiency-limitation-review-proposal.md`.

The proposal opens review of whether `AAEF-EVD-01` needs narrow refinement to distinguish evidence sufficiency from evidence integrity, schema validity, and model-generated or self-reported evidence.

## Update after AAEF-EVD-01 evidence sufficiency review

After #224, the active `AAEF-EVD-01` testing procedure row was reviewed for evidence sufficiency and limitation coverage.

Review result:

- No active CSV refinement is required at this time.
- The existing `AAEF-EVD-01` row already covers evidence completeness, high-impact action sampling, authorization, dispatch, backend and evidence records, reconstruction sufficiency, partial reconstruction gaps, and self-reported-only evidence failure.
- The coverage scan found the reviewed sufficiency criteria likely covered, including action-bound evidence, risk-proportionate evidence, self-report limitation, missing or partial evidence limitation, authorization/execution traceability, and insufficient-evidence fail handling.

Current #165 status:

- Evidence integrity schema support, integrity-focused example, evidence integrity negative test planning, incident-response preservation guidance, incident-response preservation candidate coverage, E5/evidence depth decision work, negative example / validator fixture decision work, and `AAEF-EVD-01` sufficiency review are now substantially addressed for the current v0.5.x follow-up cycle.
- #165 remains open only for temporary-document consolidation and any later decision on whether stable guidance should be extracted from the temporary v0.5.x materials.

## Issue #165 Evidence Integrity Consolidation Checkpoint

The #165 evidence integrity consolidation checkpoint is recorded in `docs/en/status/v050x-issue-165-evidence-integrity-consolidation-checkpoint.md`.

The checkpoint records that the major #165 workstreams are substantially addressed for the current v0.5.x follow-up cycle and that #165 appears close-ready if stable guidance extraction is tracked separately.
