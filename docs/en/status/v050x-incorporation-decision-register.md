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

## Incorporation Update after #189

PR #189 completed the first active testing procedure refinement based on the principal context testing candidate work.

The refinement did not add temporary `VTC-PCD-*` rows to the active testing procedure CSV.

Instead, it preserved the one-control-one-row testing model and refined existing active rows:

- `AAEF-AUZ-02` for material scope expansion and requested-vs-authorized scope review;
- `AAEF-AUZ-07` for revocation, expiry, downscoping, and authority lifecycle state changes.

This confirms the selected incorporation path for the first #161 batch:

- use VTC candidates as planning and review inputs;
- refine existing control-linked testing rows where appropriate;
- avoid promoting temporary VTC IDs into active testing artifacts unless the testing model is explicitly changed.

Remaining #161-related incorporation decisions include:

- whether and how to incorporate task drift tests;
- whether and how to incorporate retry-after-denial tests;
- whether and how to incorporate task splitting and aggregate-effect bypass tests;
- whether risk escalation and untrusted input influence require additional active testing refinement;
- whether related evidence/schema or assessment profile changes are needed.

## Incorporation Update after #194

PR #194 completed the first active testing procedure refinement based on the cross-agent delegation testing candidate work.

The refinement did not add temporary `VTC-A2A-*` rows to the active testing procedure CSV.

Instead, it preserved the one-control-one-row testing model and refined existing active rows:

- `AAEF-DEL-01` for delegated scope mismatch and delegated capability, operation, target, or resource comparison;
- `AAEF-DEL-05` for cross-agent authority lineage, communication-not-authority handling, and receiving-side validation.

This confirms the selected incorporation path for the first #163 batch:

- use VTC candidates as planning and review inputs;
- refine existing control-linked testing rows where appropriate;
- avoid promoting temporary VTC IDs into active testing artifacts unless the testing model is explicitly changed.

Remaining #163-related incorporation decisions include:

- whether and how to refine `AAEF-DEL-02` for capability-scoped delegation;
- whether and how to incorporate fire-and-forget delegation tests;
- whether and how to incorporate refusal propagation tests;
- whether downstream redelegation requires new active testing language;
- whether minimum delegation chain evidence expectations require additional refinement;
- whether related evidence/schema, control catalog, or assessment profile changes are needed.

## Incorporation Update after #199

PR #199 completed the first active testing procedure refinement based on the approval quality testing candidate work.

The refinement did not add temporary `VTC-APP-*` rows to the active testing procedure CSV.

Instead, it preserved the one-control-one-row testing model and refined existing active rows:

- `AAEF-HUM-01` for meaningful approval context, what the approver actually saw, vague approval prompt handling, and approval-to-action linkage;
- `AAEF-AUZ-03` for canonical action matching, approved scope, approval state source, and independent approval enforcement before dispatch or backend execution.

This confirms the selected incorporation path for the first #167 batch:

- use VTC candidates as planning and review inputs;
- refine existing control-linked testing rows where appropriate;
- avoid promoting temporary VTC IDs into active testing artifacts unless the testing model is explicitly changed.

Remaining #167-related incorporation decisions include:

- whether and how to incorporate draft-vs-execute approval operation-class tests;
- whether and how to incorporate post-approval payload modification tests;
- whether and how to incorporate model-generated approval summary evidence tests;
- whether approval evidence trusted-source expectations require `AAEF-EVD-03` refinement;
- whether approval fatigue and repeated approval behavior require additional `AAEF-HUM-02` refinement;
- whether related evidence/schema, control catalog, or assessment profile changes are needed.

## Incorporation Update after #201

PR #201 completed the evidence integrity CSV refinement proposal review.

The review concluded that immediate active testing procedure CSV refinement is not required for the first #165 incorporation step.

The current active testing procedure row `AAEF-EVD-04` already covers the primary evidence integrity and tamper-evident evidence requirements, including:

- critical and audit-grade evidence;
- undetected alteration;
- deletion;
- replay;
- reordering;
- truncation;
- selective omission;
- integrity verification;
- append-only evidence storage;
- write-restricted evidence stores;
- signed evidence records;
- hash chains;
- Merkle roots;
- external timestamps;
- immutable storage policies;
- independent corroborating logs;
- retention policy;
- deletion or redaction records;
- evidence trust limitations.

This confirms the selected incorporation path for the first #165 batch:

- do not add temporary evidence integrity candidate IDs to active testing artifacts;
- do not create new control IDs at this stage;
- use `AAEF-EVD-04` as the central active row for evidence integrity and tamper-evident evidence;
- defer schema, examples, negative tests, and incident-response preservation details to follow-up work.

Remaining #165-related incorporation decisions include:

- whether evidence integrity fields should be added to the Evidence Event Schema;
- whether E5 or higher-depth evidence examples should be introduced;
- whether negative tests should be added for tampering, deletion, replay, reordering, truncation, and selective omission;
- whether incident-response evidence preservation guidance should be created or refined;
- whether `AAEF-EVD-04` should receive a later minor wording refinement for verification result and failure handling;
- whether evidence integrity should be tied to assessment profiles or evidence depth levels.

## Incorporation Review Checkpoint after #202

After #202, the first incorporation review cycle for #161, #163, #165, and #167 is complete.

The current incorporation decisions are:

| Issue | Topic | Incorporation decision | Active artifact result | Status |
| --- | --- | --- | --- | --- |
| #161 | Principal context | Partially incorporate into existing active testing rows | Active testing procedure CSV refined | Open |
| #163 | Cross-agent delegation | Partially incorporate into existing active DEL testing rows | Active testing procedure CSV refined | Open |
| #165 | Evidence integrity | Treat as substantially represented by `AAEF-EVD-04` for the first step | No immediate active CSV change | Open |
| #167 | Approval quality | Partially incorporate into existing active HUM/AUZ testing rows | Active testing procedure CSV refined | Open |

The consolidated checkpoint is recorded in `docs/en/status/v050x-incorporation-review-checkpoint.md`.

The next incorporation phase should focus on smaller follow-up decisions rather than broad first-pass incorporation:

- evidence schema and examples;
- evidence integrity negative tests;
- delegation semantics;
- approval semantics;
- status document cleanup and publication readiness.

## Incorporation Update after #209, #210, and #211

PRs #209, #210, and #211 completed the first implementation wave for the evidence schema and examples track.

Incorporation decisions implemented:

| PR | Decision | Result |
| --- | --- | --- |
| #209 | Add narrow optional schema support before examples | Optional fields added under evidence and approval schema definitions |
| #210 | Add first integrity-focused example | `agentic-action-evidence-event.integrity-e5.json` added and validated |
| #211 | Add approval-to-execution binding example | `agentic-action-evidence-event.approval-binding.json` added and validated |

The implementation followed the selected path:

- schema-first;
- example-follow-up;
- optional fields only;
- no active testing procedure CSV changes;
- no new control IDs;
- no principal context or delegation lineage schema fields in the first implementation wave.

This confirms that the first T1 implementation wave is complete.

Remaining incorporation decisions include:

- whether evidence integrity negative tests should become active testing refinements, example artifacts, or separate guidance;
- whether evidence depth such as E5 should become profile guidance or remain example terminology;
- whether approval semantics require further HUM/AUZ/EVD testing procedure refinement;
- whether trusted approval evidence source expectations require additional `AAEF-EVD-03` refinement;
- whether principal context freshness/degradation requires schema fields later;
- whether delegation lineage or receiving-side validation requires schema fields later;
- whether temporary planning documents should be consolidated after the next follow-up cycle.

## Incorporation Decision after Evidence Integrity Testing Row Review

After #215, `AAEF-EVD-04` was reviewed against the evidence integrity negative test candidates.

Decision:

| Area | Decision |
| --- | --- |
| Active CSV change | Not required at this time |
| Target row | `AAEF-EVD-04` |
| Rationale | Existing testing objective, method, evidence, pass criteria, partial criteria, and fail conditions already cover the main negative test concepts |
| Candidate IDs in active CSV | Not added |
| New control IDs | Not added |
| Schema or example changes | Not required |

Observed existing coverage includes:

- undetected alteration;
- deletion;
- replay;
- reordering;
- truncation;
- selective omission;
- integrity verification;
- evidence trust limitations;
- retention, deletion, and redaction documentation.

Remaining decisions for #165:

- whether incident-response evidence preservation guidance is needed;
- whether evidence depth such as E5 should become profile guidance or remain example terminology;
- whether negative examples or validator fixtures would improve reviewability;
- whether `AAEF-EVD-01` should later receive evidence sufficiency / limitation refinement.

## Incident-Response Evidence Preservation Guidance Proposal

A temporary guidance proposal was added in `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md`.

Decision status:

| Area | Decision |
| --- | --- |
| Active CSV change | Not required in this proposal |
| Schema change | Not required in this proposal |
| Example change | Not required in this proposal |
| Primary issue | #165 |
| Primary active row | `AAEF-EVD-04` |

The proposal records preservation triggers, evidence types, preservation actions, trust-boundary considerations, and anti-patterns for incident-response evidence handling.

## Incident-Response Evidence Preservation Candidate Appendix

A temporary candidate appendix was added in `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md`.

Decision status:

| Area | Decision |
| --- | --- |
| Active CSV change | Not required in this appendix |
| Schema change | Not required in this appendix |
| Example change | Not required in this appendix |
| Primary issue | #165 |
| Primary active row | `AAEF-EVD-04` |

The appendix records preservation scenarios, preservation levels, minimal and dispute-grade evidence packages, reviewer checklist candidates, and anti-patterns for incident-response evidence handling.

## Incorporation Decision after Incident-Response Evidence Preservation Work

After #217 and #218, the incident-response evidence preservation work for #165 was reviewed.

Decision:

| Area | Decision |
| --- | --- |
| Guidance proposal | Added in #217 |
| Candidate appendix | Added in #218 |
| Active CSV change | Not required at this time |
| Evidence Event Schema change | Not required at this time |
| Evidence example change | Not required at this time |
| Validator fixture change | Not required at this time |
| Primary active row | `AAEF-EVD-04` |

Rationale:

- `AAEF-EVD-04` already covers evidence integrity and tamper-evident evidence.
- The new preservation materials are better treated as guidance and assessment support rather than active CSV changes at this stage.
- The candidate appendix provides sufficient scenario-level detail for review without introducing new control IDs, candidate IDs, schema fields, or example artifacts.

Remaining decisions for #165:

- whether evidence depth / E5 terminology should become profile guidance or remain example terminology;
- whether negative evidence examples or validator fixtures would improve reviewability;
- whether `AAEF-EVD-01` should later receive evidence sufficiency / limitation refinement;
- whether temporary planning documents should be consolidated after the current follow-up cycle.

## Evidence Depth and E5 Profile Decision Proposal

A temporary decision proposal was added in `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md`.

Decision status:

| Area | Decision |
| --- | --- |
| E5 formal profile | Deferred |
| Certification scale | Not created |
| Required schema field | Not added |
| Active CSV requirement | Not added |
| Example terminology | Allowed with non-normative framing |
| Future guidance | Candidate for later work |

The proposal records that evidence depth vocabulary may be useful for review and guidance, but should not become a formal certification or required schema/profile mechanism in the current v0.5.x cycle.

## Incorporation Decision after Evidence Depth and E5 Decision

After #220, the evidence depth / E5 treatment for #165 was reviewed.

Decision:

| Area | Decision |
| --- | --- |
| E5 formal profile | Deferred |
| Certification scale | Not created |
| Required schema field | Not added |
| Active CSV requirement | Not added |
| Example terminology | Allowed with non-normative framing |
| Future guidance | Candidate for later work |
| Primary active row | `AAEF-EVD-04` |

Rationale:

- E5 is useful as review vocabulary for stronger, dispute-grade, integrity-verifiable evidence.
- Formalizing E5 too early could create false assurance, certification confusion, mechanism lock-in, schema overreach, and audit gaming risk.
- The current v0.5.x cycle should preserve E5 as explanatory terminology rather than a compliance tier or required field.

Remaining decisions for #165:

- whether negative evidence examples or validator fixtures would improve reviewability;
- whether `AAEF-EVD-01` should later receive evidence sufficiency / limitation refinement;
- whether evidence depth guidance should be created later from the temporary proposal;
- whether temporary planning documents should be consolidated after the current follow-up cycle.

## Negative Evidence Examples and Validator Fixtures Decision Proposal

A temporary decision proposal was added in `docs/en/status/v050x-negative-evidence-examples-fixtures-decision-proposal.md`.

Decision status:

| Area | Decision |
| --- | --- |
| Schema-invalid fixtures | Not added now |
| Schema-valid negative examples | Deferred |
| Validator behavior | Unchanged |
| Evidence Event Schema | Unchanged |
| Active CSV | Unchanged |
| Future reviewer-facing examples | Candidate future work |

The proposal records that most evidence integrity failure states are semantic or assurance failures rather than JSON Schema failures.

## Incorporation Decision after Negative Evidence Examples and Validator Fixtures Decision

After #222, the negative evidence examples and validator fixtures question for #165 was reviewed.

Decision:

| Area | Decision |
| --- | --- |
| Schema-invalid fixtures | Not added in this cycle |
| Schema-valid negative examples | Deferred |
| Validator behavior | Unchanged |
| Evidence Event Schema | Unchanged |
| Active CSV | Unchanged |
| Reviewer-facing negative examples | Candidate future work |
| Primary active row | `AAEF-EVD-04` |

Rationale:

- Most evidence integrity failure states are semantic or assurance failures rather than JSON Schema failures.
- A failed, partial, unavailable, or limitation-bearing evidence state can be valid to record.
- Schema validity should not be confused with evidence sufficiency, evidence completeness, or tamper-evidence.
- The validator should continue to answer whether an evidence event is structurally valid, not whether the evidence is sufficient or trustworthy.

Remaining decisions for #165:

- whether `AAEF-EVD-01` should later receive evidence sufficiency / limitation refinement;
- whether evidence depth guidance should be created later from the temporary proposal;
- whether temporary planning documents should be consolidated after the current follow-up cycle.

## AAEF-EVD-01 Evidence Sufficiency and Limitation Review Proposal

A temporary review proposal was added in `docs/en/status/v050x-evd01-evidence-sufficiency-limitation-review-proposal.md`.

Decision status:

| Area | Decision |
| --- | --- |
| Active CSV change | Not made in this proposal |
| Target row under review | `AAEF-EVD-01` |
| Related row | `AAEF-EVD-04` |
| Schema change | Not required in this proposal |
| Example change | Not required in this proposal |
| Validator change | Not required in this proposal |

The proposal records that evidence sufficiency is distinct from evidence integrity and schema validity.

## Incorporation Decision after AAEF-EVD-01 Evidence Sufficiency Review

After #224, `AAEF-EVD-01` was reviewed for evidence sufficiency and limitation coverage.

Decision:

| Area | Decision |
| --- | --- |
| Active CSV change | Not required at this time |
| Target row | `AAEF-EVD-01` |
| Related row | `AAEF-EVD-04` |
| Schema change | Not required |
| Example change | Not required |
| Validator change | Not required |
| Guidance extraction | Candidate future work |

Rationale:

- `AAEF-EVD-01` already requires evidence sufficient to reconstruct what happened for sampled high-impact actions.
- The active row already references initiated-by, authority basis, requested action, resource, decision path, dispatch or execution result, timestamp, and correlation identifiers.
- Partial criteria already cover reconstruction gaps in authority, dispatch, result, timing, or correlation identifiers.
- Fail conditions already cover missing, self-reported-only, contradictory, or insufficient evidence.
- The row is sufficient for the current v0.5.x follow-up cycle without active CSV modification.

Remaining decisions for #165:

- whether temporary planning documents should be consolidated after the current follow-up cycle;
- whether stable evidence sufficiency, evidence depth, or incident-response preservation guidance should be extracted later.

## Issue #165 Evidence Integrity Consolidation Checkpoint

A temporary consolidation checkpoint was added in `docs/en/status/v050x-issue-165-evidence-integrity-consolidation-checkpoint.md`.

Decision status:

| Area | Decision |
| --- | --- |
| Active CSV change | Not required |
| Evidence Event Schema change | Not required |
| Example change | Not required |
| Validator change | Not required |
| Stable guidance extraction | Candidate future work |
| Issue disposition | Close-ready if future guidance extraction is tracked separately |

The checkpoint consolidates the #165 evidence integrity and tamper-evident evidence follow-up decisions for the current v0.5.x cycle.

## Tamper-Evident Evidence Selected Contexts Proposal

A temporary selected contexts proposal was added in `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-proposal.md`.

Decision status:

| Area | Decision |
| --- | --- |
| Active CSV change | Not made in this proposal |
| Evidence Event Schema change | Not made in this proposal |
| Example change | Not made in this proposal |
| Validator change | Not made in this proposal |
| Primary issue | #166 |
| Related rows | `AAEF-EVD-04`, `AAEF-EVD-01` |

The proposal identifies candidate required, recommended, and optional contexts for tamper-evident evidence.

## Tamper-Evident Evidence Selected Contexts Candidate Appendix

A temporary selected contexts candidate appendix was added in `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-candidate-appendix.md`.

Decision status:

| Area | Decision |
| --- | --- |
| Active CSV change | Not made in this appendix |
| Evidence Event Schema change | Not made in this appendix |
| Example change | Not made in this appendix |
| Validator change | Not made in this appendix |
| Primary issue | #166 |
| Related rows | `AAEF-EVD-04`, `AAEF-EVD-01` |

The appendix records concrete required, recommended, optional, and escalation contexts for tamper-evident evidence.

## Tamper-Evident Evidence Selected Contexts Incorporation Decision

A temporary incorporation decision was added in `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-incorporation-decision.md`.

Decision status:

| Area | Decision |
| --- | --- |
| Active CSV change | Not required at this time |
| Evidence Event Schema change | Not required at this time |
| Example change | Not required at this time |
| Validator change | Not required at this time |
| Context tier fields | Not added |
| Candidate context IDs in active CSV | Not added |
| Stable guidance extraction | Candidate future work |
| Primary issue | #166 |

The decision keeps selected-context requirements guidance-only for the current v0.5.x cycle.

## Update after Tamper-Evident Evidence Selected Contexts Incorporation Decision

After #229, the selected-context tamper-evident evidence incorporation decision for #166 was reviewed.

Decision:

| Area | Decision |
| --- | --- |
| Selected-context model | Guidance-only for the current cycle |
| Active CSV change | Not required at this time |
| Evidence Event Schema change | Not required at this time |
| Evidence example change | Not required at this time |
| Validator change | Not required at this time |
| Context tier fields | Not added |
| Candidate context IDs in active CSV | Not added |
| Stable guidance extraction | Candidate future work |
| Primary issue | #166 |

Rationale:

- `AAEF-EVD-04` already covers evidence integrity and tamper-evident evidence at the active testing procedure level.
- `AAEF-EVD-01` already covers evidence sufficiency and action reconstruction.
- Selected contexts are useful for review and implementation guidance, but should not become schema values or active CSV IDs before feedback.
- Context-specific evidence requirements may vary by action impact, reversibility, dispute likelihood, delegation complexity, and implementation maturity.
- Keeping the selected-context model guidance-only avoids false precision, certification confusion, and premature schema or CSV coupling.

Remaining decisions for #166:

- whether to add a consolidation / close-readiness checkpoint;
- whether stable selected-context guidance should be extracted later;
- whether selected-context examples should be added in a future cycle.
