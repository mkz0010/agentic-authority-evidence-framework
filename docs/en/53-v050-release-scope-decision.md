# v0.5.0 Release Scope Decision

**Status:** Non-normative v0.5.0 planning decision record

> **Planning status:** This document records the intended v0.5.0 planning scope. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifacts, testing procedures, or release notes.

## Purpose

This document records the intended scope decision for AAEF v0.5.0 planning work.

The v0.5.0 planning cycle introduced several models and design notes for authority lifecycle, evidence integrity, approval quality, and incorporation rules.

The purpose of this document is to decide how those planning topics should be treated for the v0.5.0 release, and to separate:

- non-normative planning models;
- implementation and assessment guidance;
- future testing or evidence refinements;
- future existing-control refinements;
- possible new control candidates;
- deferred v0.5.x work.

## Scope Decision Summary

AAEF v0.5.0 should be treated as a planning-model and incorporation-framework release.

For v0.5.0, the planning models should remain non-normative unless a later release explicitly incorporates them into normative or assessment artifacts.

This means v0.5.0 should not, by itself, change:

- the control catalog CSV;
- the human-readable control requirements;
- the assessment worksheet;
- the assessment profiles;
- the testing procedure CSV;
- the evidence schema;
- the evidence examples;
- the external framework mapping CSV.

The planning models should instead provide structured design input for later v0.5.x refinements.

## v0.5.0 Planning Themes and Release Disposition

| Planning theme | Primary disposition for v0.5.0 | Future incorporation path | Related material |
| --- | --- | --- | --- |
| Principal Context Degradation | Non-normative planning model | Existing control refinement, guidance, and testing refinement candidate | `docs/en/30-principal-context-degradation.md`, `docs/en/50-authority-lifecycle-model.md` |
| Cross-Agent and Cross-Domain Authority | Non-normative planning model | Existing control refinement or new cross-agent control candidate if existing controls cannot express capability-scoped delegation, explicit acceptance/refusal, delegation chain limits, or budget propagation | `docs/en/31-cross-agent-cross-domain-authority.md`, `docs/en/50-authority-lifecycle-model.md` |
| Authority Denial and Reauthorization Flow | Non-normative planning model | Testing refinement, evidence refinement, and existing control refinement candidate | `docs/en/32-authority-denial-reauthorization-flow.md`, `docs/en/50-authority-lifecycle-model.md` |
| Risk-Proportional Evidence and Performance Overhead | Non-normative planning model | Guidance, evidence refinement, and assessment profile refinement candidate | `docs/en/36-risk-proportional-evidence-profile.md`, `docs/en/51-evidence-integrity-levels.md` |
| Tamper-Evident Evidence Storage | Non-normative planning model | Evidence refinement and possible high-impact or audit-grade profile requirement candidate | `docs/en/37-tamper-evident-evidence-storage.md`, `docs/en/51-evidence-integrity-levels.md` |
| Approval Quality and Approval Fatigue | Non-normative planning model | Existing HUM control refinement, guidance, testing refinement, or new HUM control candidate | `docs/en/39-approval-quality-approval-fatigue.md`, `docs/en/52-approval-quality-model.md` |

## v0.5.0 Included Planning Models

The following planning models are in scope for v0.5.0 as non-normative planning material:

| Document | Scope |
| --- | --- |
| `docs/en/34-v050-control-design-options.md` | Incorporation rules, outcome register, and control design options for v0.5.0 planning topics |
| `docs/en/50-authority-lifecycle-model.md` | Authority lifecycle model covering principal context degradation, cross-agent authority, denial, freeze, revocation, expiry, and reauthorization |
| `docs/en/51-evidence-integrity-levels.md` | Evidence integrity levels model covering risk-proportional evidence, tamper-evident evidence, and performance overhead tradeoffs |
| `docs/en/52-approval-quality-model.md` | Approval quality model covering meaningful approval, context sufficiency, approval fatigue, batch approval risk, and approval evidence expectations |
| `docs/en/53-v050-release-scope-decision.md` | Release scope decision record for v0.5.0 planning material |

## Explicitly Out of Scope for v0.5.0

The following are out of scope for v0.5.0 unless a later PR explicitly changes this decision:

- adding new control IDs;
- changing existing control requirements;
- changing the control catalog CSV;
- changing required evidence schema fields;
- changing evidence example validity expectations;
- changing testing procedure pass/fail criteria;
- changing assessment worksheet fields;
- changing assessment profile mappings;
- claiming compliance equivalence with external frameworks;
- treating v0.5.0 planning notes as certification, audit, or conformance criteria.

## Deferred v0.5.x Candidate Work

The following work should be considered for v0.5.x follow-up releases.

| Candidate work | Possible artifact impact |
| --- | --- |
| Principal context degradation testing criteria | Testing procedures, control guidance, assessment methodology |
| Cross-agent capability-scoped delegation controls | Control catalog, control requirements, testing procedures, evidence expectations |
| Delegation acceptance/refusal and chain accountability tests | Testing procedures, evidence examples, authority lifecycle guidance |
| Cross-agent budget propagation | New or refined control guidance, resource governance controls, assessment guidance |
| Evidence integrity levels for high-impact or audit-grade profiles | Assessment profiles, evidence guidance, prequalification guidance |
| Tamper-evident evidence requirements for selected contexts | Evidence guidance, testing procedures, possibly schema or examples |
| Approval context sufficiency and fatigue tests | HUM controls, testing procedures, assessment guidance, evidence expectations |

## Issue Handling Decision

The current v0.5.0 planning issues should not be closed merely because a planning model exists.

They should remain open until the project decides one of the following for each issue:

- close as addressed by non-normative planning guidance;
- close after incorporation into a normative or assessment artifact;
- convert into a narrower v0.5.x follow-up issue;
- defer explicitly as future research or implementation guidance.

## Release Preparation Checklist

Release preparation should follow `docs/en/54-v050-release-preparation-checklist.md`.

That checklist records validation steps, issue review guidance, follow-up issue candidates, and draft release note language for v0.5.0.

## Release Note Guidance

The v0.5.0 release notes should state that v0.5.0 is a planning and design-clarification release.

Recommended release note language:

AAEF v0.5.0 adds non-normative planning models for authority lifecycle, evidence integrity, and approval quality, and clarifies how planning concepts may be incorporated into future normative or assessment artifacts. It does not change the v0.4.1 control catalog, evidence schema, assessment worksheet, assessment profiles, or testing procedures unless explicitly stated in later release artifacts.

## Relationship to Existing AAEF Artifacts

This decision record is intended to guide v0.5.0 release preparation.

It does not itself change the v0.4.1 baseline.

Future normative incorporation should follow the incorporation rules in `docs/en/34-v050-control-design-options.md` and should update affected control, evidence, assessment, testing, mapping, and release artifacts together.
