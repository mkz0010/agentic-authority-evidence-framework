# v0.5.x Incorporation Decision Register

**Status:** Temporary, non-normative incorporation decision register

## Purpose

This document records the initial incorporation direction for v0.5.x follow-up work after the first guidance and testing pass.

It is a temporary coordination document.

It does not change the v0.4.1 control and assessment baseline.

It does not promote any guidance into normative status by itself.

## Scope

This register covers the currently tracked v0.5.x follow-up issues:

- #161 — Principal context degradation testing criteria
- #162 — Capability-scoped cross-agent delegation controls
- #163 — Delegation acceptance/refusal and chain accountability negative tests
- #164 — Cross-agent budget propagation guidance
- #165 — Evidence integrity levels for high-impact and audit-grade profiles
- #166 — Tamper-evident evidence requirements for selected contexts
- #167 — Approval quality testing and evidence expectations

## Decision Legend

| Direction | Meaning |
| --- | --- |
| Keep as guidance | The material should remain non-normative guidance for now. |
| Control refinement candidate | The material may refine existing controls or become future control language. |
| Testing procedure candidate | The material may become test cases, pass/fail criteria, or executable fixtures. |
| Evidence expectation candidate | The material may become required, recommended, or optional evidence expectations. |
| Schema candidate | The material may introduce future evidence schema fields. |
| Assessment profile candidate | The material may affect assessment depth, profile selection, or assurance level. |
| Implementation guidance candidate | The material may become practical implementation guidance rather than control text. |
| Split or defer | The material should be split into later issues or deferred. |

## Summary Decision Matrix

| Issue | Initial guidance document | Primary incorporation direction | Secondary direction | Immediate recommendation |
| --- | --- | --- | --- | --- |
| #161 | `docs/en/59-principal-context-degradation-testing.md` | Testing procedure candidate | Evidence/schema and assessment profile candidates | Select a smaller set of high-value degradation tests before changing testing procedures. |
| #162 | `docs/en/56-capability-scoped-cross-agent-delegation.md` | Control refinement candidate | Implementation guidance and evidence/schema candidates | Treat capability-scoped delegation as a future cross-agent authority control candidate, but do not update the catalog yet. |
| #163 | `docs/en/57-cross-agent-delegation-negative-tests.md` | Testing procedure candidate | Evidence expectation candidate | Promote selected negative tests into testing candidates after prioritization. |
| #164 | `docs/en/58-cross-agent-budget-propagation.md` | Implementation guidance candidate | Evidence/schema, testing, and control candidates | Keep broad budget propagation as guidance first; consider narrower requirements for high-impact cross-agent contexts. |
| #165 | `docs/en/60-evidence-integrity-profile-guidance.md` | Assessment profile candidate | Evidence/schema candidate | Use as the basis for future high-impact and audit-grade evidence integrity profile refinement. |
| #166 | `docs/en/61-tamper-evident-evidence-requirements.md` | Evidence expectation candidate | Schema and testing candidates | Consider selected-context requirements only; avoid universal tamper-evident evidence requirements. |
| #167 | `docs/en/62-approval-quality-testing-guidance.md` | Testing procedure candidate | HUM control refinement, evidence/schema, and assessment profile candidates | Prioritize negative tests and approval evidence expectations before changing HUM controls. |

## Recommended Incorporation Waves

The following waves are non-normative planning guidance.

They are intended to reduce review risk and avoid premature baseline changes.

### Wave 1: Testing candidate selection

Candidate sources:

- #161 principal context degradation tests
- #163 cross-agent delegation negative tests
- #167 approval quality negative tests

Recommended focus:

- select a small number of high-value tests;
- avoid importing every planning-level negative test into testing procedures;
- define pass/fail intent before editing testing CSVs;
- preserve a distinction between guidance examples and assessment criteria.

### Wave 2: Evidence and schema candidate review

Candidate sources:

- #164 budget/resource propagation evidence
- #165 evidence integrity bands
- #166 tamper-evident evidence fields
- #167 approval evidence fields
- #161 principal context freshness fields
- #162 cross-agent delegation authority fields

Recommended focus:

- identify fields that are repeatedly needed across documents;
- separate required fields from optional or profile-dependent fields;
- avoid schema expansion before evidence expectations are stable;
- consider privacy, retention, storage, and implementation burden.

### Wave 3: Assessment profile refinement

Candidate sources:

- #161 principal context degradation
- #165 evidence integrity levels
- #166 tamper-evident selected contexts
- #167 approval quality
- #164 resource propagation for high-impact cross-agent contexts

Recommended focus:

- high-impact profile expectations;
- audit-grade profile expectations;
- externally effective actions;
- cross-agent and cross-domain authority paths;
- destructive, privileged, financial, and production actions.

### Wave 4: Control refinement proposal

Candidate sources:

- #162 capability-scoped delegation
- #167 approval quality
- #164 cross-agent budget propagation in selected contexts
- #161 principal context degradation when tied to reauthorization or authorization freshness

Recommended focus:

- draft candidate control refinements first;
- review whether existing AUZ, TOOL, EVD, HUM, GOV, or PRN controls can be refined;
- avoid creating a new control domain until the need is clear;
- keep candidate control text separate from the active control catalog until approved.

### Wave 5: Implementation guidance refinement

Candidate sources:

- #162 receiving-side validation;
- #164 budget enforcement points;
- #166 tamper-evident implementation-neutral mechanisms;
- #167 approval-to-execution binding;
- #161 freshness and reauthorization checks.

Recommended focus:

- clarify implementable architecture patterns;
- separate required properties from example mechanisms;
- avoid mandating specific identity, token, logging, SIEM, storage, or approval technologies.

## Issue-by-Issue Notes

### #161 — Principal context degradation testing criteria

Initial decision:

- Primary direction: testing procedure candidate.
- Secondary direction: evidence/schema and assessment profile candidates.
- Control direction: possible refinement to authorization or reauthorization expectations, but not a standalone control yet.

Recommended next step:

- select a minimum test subset for stale context, task drift, scope expansion, risk escalation, revocation, retry after denial, task splitting, and untrusted input influence.

Closure condition:

- this issue should remain open until selected tests are either incorporated, split into testing issues, or explicitly deferred.

### #162 — Capability-scoped cross-agent delegation controls

Initial decision:

- Primary direction: control refinement candidate.
- Secondary direction: implementation guidance and evidence/schema candidates.
- Testing direction: should be covered partly through #163.

Recommended next step:

- draft candidate control language separately before modifying the control catalog.
- evaluate whether this belongs under existing authorization/delegation controls or a future cross-agent authority control area.

Closure condition:

- this issue should remain open until a control refinement proposal, deferral decision, or split issue set exists.

### #163 — Delegation acceptance/refusal and chain accountability negative tests

Initial decision:

- Primary direction: testing procedure candidate.
- Secondary direction: evidence expectation candidate.
- Control direction: not primary.

Recommended next step:

- prioritize tests for communication mistaken for authority, fire-and-forget delegation, refusal propagation failure, scope mismatch, unauthorized downstream delegation, chain depth overflow, broken chain evidence, budget propagation failure, retry pressure, task splitting, and model-only rationale.

Closure condition:

- this issue should remain open until the test subset is selected, split, or deferred.

### #164 — Cross-agent budget propagation guidance

Initial decision:

- Primary direction: implementation guidance candidate.
- Secondary direction: evidence/schema, testing, and control candidates.
- Control direction: selected-context only, not universal.

Recommended next step:

- identify which resource constraints are necessary for high-impact cross-agent contexts.
- avoid universal budget metadata requirements for low-risk actions.

Closure condition:

- this issue should remain open until selected-context expectations are defined or deferred.

### #165 — Evidence integrity levels for high-impact and audit-grade profiles

Initial decision:

- Primary direction: assessment profile candidate.
- Secondary direction: evidence/schema candidate.
- Control direction: not primary.

Recommended next step:

- decide whether Evidence Integrity bands remain explanatory guidance or become assessment profile inputs for high-impact and audit-grade contexts.

Closure condition:

- this issue should remain open until assessment profile impact is incorporated, split, or deferred.

### #166 — Tamper-evident evidence requirements for selected contexts

Initial decision:

- Primary direction: evidence expectation candidate.
- Secondary direction: schema and testing candidates.
- Control direction: selected-context only.

Recommended next step:

- identify required-candidate contexts, recommended contexts, and optional contexts.
- avoid requiring tamper-evident evidence for all actions.

Closure condition:

- this issue should remain open until selected contexts and schema/testing follow-ups are decided.

### #167 — Approval quality testing and evidence expectations

Initial decision:

- Primary direction: testing procedure candidate.
- Secondary direction: HUM control refinement, evidence/schema, and assessment profile candidates.
- Control direction: likely HUM refinement after testing/evidence expectations are stable.

Recommended next step:

- prioritize tests for vague approval prompts, draft-vs-execute mismatch, canonical action mismatch, blind approval, rubber-stamp approval, batch approval, approval laundering, expired approval, and missing enforcement.

Closure condition:

- this issue should remain open until selected tests, evidence expectations, HUM refinements, or deferrals are created.

## Cross-Cutting Decisions

### Do not close #161 through #167 yet

The initial guidance/testing pass is complete, but incorporation decisions remain active.

### Do not update baseline artifacts in this phase

This register should not update:

- control catalog CSV;
- human-readable control requirements;
- assessment worksheet;
- assessment profiles;
- testing procedure CSV;
- external framework mapping CSV;
- evidence schema;
- evidence examples.

### Prefer smaller incorporation PRs

Future incorporation work should use smaller PRs organized by artifact type, such as:

- testing candidates;
- evidence/schema candidates;
- assessment profile refinements;
- control refinement proposals;
- implementation guidance refinements.

### Preserve non-normative status until explicit incorporation

Planning documents and follow-up guidance remain non-normative unless a later PR explicitly updates the relevant normative or assessment artifact.

## Relationship to Status Tracker

The current status tracker is maintained in:

- `docs/en/status/v050x-follow-up-status.md`

This register complements that tracker by recording the initial incorporation direction.

The status tracker answers:

- what has been completed;
- which documents exist;
- why issues remain open.

This register answers:

- where the completed guidance may be incorporated next;
- which artifact types are likely affected;
- what should not be promoted yet.

## Removal or Archive Condition

This document should be removed, replaced, or archived when:

- incorporation decisions for #161 through #167 are complete;
- follow-up issues are closed, split, superseded, or deferred;
- selected guidance is incorporated into stable artifacts;
- or a later release replaces this register with a stable roadmap or changelog entry.

## Non-Goals

This document does not:

- promote any guidance to normative status;
- update controls;
- update testing procedures;
- update assessment profiles;
- update the evidence schema;
- add required evidence fields;
- close follow-up issues;
- supersede the changelog;
- supersede release notes.

It is a temporary decision register for the v0.5.x incorporation phase.
