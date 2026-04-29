# AAEF Document Map

**Status:** Non-normative navigation and classification aid

## Purpose

This document classifies AAEF documents and related artifacts by role.

It does not move files, change document status, change the current control and assessment baseline, or make planning material normative.

The purpose is to make the repository easier to navigate while preserving existing links and release history.

## Classification Principles

AAEF documents should be understood by role, not only by topic.

The most important distinction is whether a document is:

- current baseline or assessment-relevant material;
- stable explanatory material;
- research-facing material;
- non-normative planning material;
- non-normative follow-up guidance or testing guidance;
- examples;
- temporary status or coordination material.

A document's location or number does not by itself make it normative.

The current baseline is determined by the release notes and explicit baseline statements in the repository.

## Current Baseline and Assessment-Relevant Artifacts

These artifacts are closest to assessment, validation, schema, mapping, or control operation.

| Path | Purpose | Classification |
| --- | --- | --- |
| `controls/aaef-controls-v0.1.csv` | Control catalog artifact | Baseline / assessment-relevant artifact |
| `assessment/aaef-assessment-profiles-v0.3-draft.csv` | Assessment artifact | Baseline / assessment-relevant artifact |
| `assessment/aaef-assessment-worksheet-v0.2-draft.csv` | Assessment artifact | Baseline / assessment-relevant artifact |
| `assessment/aaef-testing-procedures-v0.4-draft.csv` | Assessment artifact | Baseline / assessment-relevant artifact |
| `schemas/agentic-action-evidence-event.schema.json` | Evidence schema artifact | Baseline / assessment-relevant artifact |
| `examples/agentic-action-evidence-event.audit-grade.json` | Evidence example artifact | Baseline / assessment-relevant artifact |
| `examples/agentic-action-evidence-event.high-impact.json` | Evidence example artifact | Baseline / assessment-relevant artifact |
| `examples/agentic-action-evidence-event.invalid.json` | Evidence example artifact | Baseline / assessment-relevant artifact |
| `examples/agentic-action-evidence-event.json` | Evidence example artifact | Baseline / assessment-relevant artifact |
| `examples/agentic-action-evidence-event.minimal.json` | Evidence example artifact | Baseline / assessment-relevant artifact |
| `examples/agentic-action-evidence-event.valid.json` | Evidence example artifact | Baseline / assessment-relevant artifact |
| `mappings/aaef-external-framework-mapping-v0.4-draft.csv` | External framework mapping artifact | Baseline / assessment-relevant artifact |
| `mappings/threat-control-assurance-mapping-v0.2-draft.csv` | External framework mapping artifact | Baseline / assessment-relevant artifact |

## Stable Framework Explanation

These documents explain the core framework, terminology, principles, trust model, assurance model, or implementation orientation.

| Path | Purpose | Classification |
| --- | --- | --- |
| `docs/en/00-introduction.md` | Framework introduction | Stable explanatory material |
| `docs/en/01-scope.md` | Framework scope | Stable explanatory material |
| `docs/en/02-core-principles.md` | Core principles | Stable explanatory material |
| `docs/en/03-definitions.md` | Definitions | Stable explanatory material |
| `docs/en/04-threat-model.md` | Threat model | Stable explanatory material |
| `docs/en/05-trust-model.md` | Trust model | Stable explanatory material |
| `docs/en/16-assurance-model.md` | Assurance model | Stable explanatory material |
| `docs/en/18-implementation-guidance.md` | Implementation guidance | Stable explanatory material |

## Research-Facing Material

These documents help researchers, reviewers, students, standards participants, and implementers understand AAEF as a research and design object.

| Path | Purpose | Classification |
| --- | --- | --- |
| `docs/en/19-open-research-questions.md` | Detailed open research questions | Research-facing material |
| `docs/en/55-researcher-overview.md` | Researcher-facing entry point and reading path | Research-facing material |

## v0.5.0 Planning Material

These documents were created to clarify future design direction.

They are non-normative unless a later release explicitly incorporates them into control, evidence, assessment, testing, schema, mapping, or release artifacts.

| Path | Purpose | Classification |
| --- | --- | --- |
| `docs/en/30-principal-context-degradation.md` | Principal context degradation concept | Non-normative planning material |
| `docs/en/31-cross-agent-cross-domain-authority.md` | Cross-agent and cross-domain authority planning | Non-normative planning material |
| `docs/en/33-v050-planning-overview.md` | v0.5.0 planning overview | Non-normative planning material |
| `docs/en/34-v050-control-design-options.md` | v0.5.0 control design options and incorporation notes | Non-normative planning material |
| `docs/en/36-risk-proportional-evidence-profile.md` | Risk-proportional evidence planning | Non-normative planning material |
| `docs/en/37-tamper-evident-evidence-storage.md` | Tamper-evident evidence storage planning | Non-normative planning material |
| `docs/en/39-approval-quality-approval-fatigue.md` | Approval quality and approval fatigue planning | Non-normative planning material |
| `docs/en/50-authority-lifecycle-model.md` | Authority Lifecycle Model | Non-normative planning model |
| `docs/en/51-evidence-integrity-levels.md` | Evidence Integrity Levels | Non-normative planning model |
| `docs/en/52-approval-quality-model.md` | Approval Quality Model | Non-normative planning model |
| `docs/en/53-v050-release-scope-decision.md` | v0.5.0 release scope decision | Release planning / decision record |
| `docs/en/54-v050-release-preparation-checklist.md` | v0.5.0 release preparation checklist | Release planning / validation checklist |

## v0.5.x Follow-up Guidance and Testing Guidance

These documents capture the first follow-up guidance or testing pass after v0.5.0.

They do not change the v0.4.1 control and assessment baseline by themselves.

| Path | Purpose | Classification |
| --- | --- | --- |
| `docs/en/56-capability-scoped-cross-agent-delegation.md` | Capability-scoped cross-agent delegation guidance | Non-normative follow-up guidance |
| `docs/en/57-cross-agent-delegation-negative-tests.md` | Cross-agent delegation negative tests | Non-normative follow-up testing guidance |
| `docs/en/58-cross-agent-budget-propagation.md` | Cross-agent budget propagation guidance | Non-normative follow-up guidance |
| `docs/en/59-principal-context-degradation-testing.md` | Principal context degradation testing guidance | Non-normative follow-up testing guidance |
| `docs/en/60-evidence-integrity-profile-guidance.md` | Evidence integrity profile guidance | Non-normative follow-up guidance |
| `docs/en/61-tamper-evident-evidence-requirements.md` | Tamper-evident evidence requirements guidance | Non-normative follow-up guidance |
| `docs/en/62-approval-quality-testing-guidance.md` | Approval quality testing guidance | Non-normative follow-up testing and evidence guidance |

## Examples

These documents provide explanatory examples, evidence examples, or scenario-oriented material.

| Path | Purpose | Classification |
| --- | --- | --- |
| `docs/en/40-approval-evidence-examples.md` | Approval evidence examples | Examples |
| `docs/en/42-tamper-evident-evidence-examples.md` | Tamper-evident evidence examples | Examples |
| `docs/en/44-evidence-depth-examples.md` | Evidence depth examples | Examples |
| `docs/en/45-principal-context-degradation-examples.md` | Principal context degradation examples | Examples |
| `docs/en/46-cross-agent-authority-examples.md` | Cross-agent authority examples | Examples |
| `docs/en/48-non-execution-reauthorization-negative-tests.md` | Non-execution and reauthorization negative tests | Examples / non-normative negative test guidance |
| `docs/en/49-tamper-evident-evidence-negative-tests.md` | Tamper-evident evidence negative tests | Examples / non-normative negative test guidance |

## Temporary Status and Coordination Documents

Temporary status documents are kept under `docs/en/status/`.

They may be removed, replaced, or archived when the related milestone, follow-up work, or incorporation decision is complete.

| Path | Purpose | Classification |
| --- | --- | --- |
| _No matching documents in this category yet._ |  |  |
| `docs/en/status/v050x-incorporation-decision-register.md` | v0.5.x incorporation direction register | Temporary status / coordination material |
| `docs/en/status/v050x-testing-candidate-selection.md` | v0.5.x testing candidate selection | Temporary status / coordination material |
| `docs/en/status/v050x-testing-procedure-candidate-matrix.md` | v0.5.x testing procedure candidate matrix | Temporary status / coordination material |
| `docs/en/status/v050x-testing-candidate-mapping.md` | v0.5.x testing candidate mapping | Temporary status / coordination material |
| `docs/en/status/v050x-testing-draft-pass-fail-criteria.md` | v0.5.x testing draft pass/fail criteria | Temporary status / coordination material |
| `docs/en/status/v050x-testing-incorporation-readiness-review.md` | v0.5.x testing incorporation readiness review | Temporary status / coordination material |
| `docs/en/status/v050x-principal-context-testing-proposal.md` | v0.5.x principal context testing proposal | Temporary status / coordination material |
| `docs/en/status/v050x-principal-context-testing-candidate-appendix.md` | v0.5.x principal context testing candidate appendix | Temporary status / coordination material |
| `docs/en/status/v050x-principal-context-testing-csv-refinement-proposal.md` | v0.5.x principal context testing CSV refinement proposal | Temporary status / coordination material |
| `docs/en/status/v050x-cross-agent-delegation-testing-proposal.md` | v0.5.x cross-agent delegation testing proposal | Temporary status / coordination material |
| `docs/en/status/v050x-cross-agent-delegation-testing-candidate-appendix.md` | v0.5.x cross-agent delegation testing candidate appendix | Temporary status / coordination material |
| `docs/en/status/v050x-cross-agent-delegation-csv-refinement-proposal.md` | v0.5.x cross-agent delegation CSV refinement proposal | Temporary status / coordination material |
| `docs/en/status/v050x-approval-quality-testing-proposal.md` | v0.5.x approval quality testing proposal | Temporary status / coordination material |
| `docs/en/status/v050x-approval-quality-testing-candidate-appendix.md` | v0.5.x approval quality testing candidate appendix | Temporary status / coordination material |
| `docs/en/status/v050x-approval-quality-csv-refinement-proposal.md` | v0.5.x approval quality CSV refinement proposal | Temporary status / coordination material |
| `docs/en/status/v050x-evidence-integrity-csv-refinement-proposal.md` | v0.5.x evidence integrity CSV refinement proposal | Temporary status / coordination material |
| `docs/en/status/v050x-incorporation-review-checkpoint.md` | v0.5.x incorporation review checkpoint | Temporary status / coordination material |
| `docs/en/status/v050x-next-phase-track-plan.md` | v0.5.x next phase track plan | Temporary status / coordination material |
| `docs/en/status/v050x-evidence-schema-and-examples-track-proposal.md` | v0.5.x evidence schema and examples track proposal | Temporary status / coordination material |
| `docs/en/status/v050x-evidence-schema-field-proposal.md` | v0.5.x evidence schema field proposal | Temporary status / coordination material |

## Physical Organization Policy

This map is intentionally a logical classification layer.

Existing numbered documents remain in place to preserve links, release history, issue references, and review context.

Large-scale physical movement of existing documents should be considered separately, preferably in a future repository-structure cleanup release or milestone.

## Non-Goals

This document does not:

- change the current baseline;
- change the normative status of any document;
- move existing documents;
- close follow-up issues;
- replace release notes;
- replace changelog entries;
- replace milestone tracking.

It is a navigation and classification aid only.
