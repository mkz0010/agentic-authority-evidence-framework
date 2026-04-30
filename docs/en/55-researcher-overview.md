# Researcher Overview

**Status:** Non-normative research-facing overview

## Purpose

This document provides a research-oriented entry point to the Agentic Authority and Evidence Framework (AAEF).

It is intended for researchers, reviewers, students, standards participants, security architects, AI governance practitioners, and implementers who want to understand AAEF as a research and design object rather than only as an implementation checklist.

This document does not create new control requirements and does not change the current control and assessment baseline.

## Current Status

AAEF v0.5.0 is the latest public review planning release.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, testing procedures, or related normative or assessment artifacts.

The v0.5.0 planning materials are non-normative unless explicitly incorporated into future control, evidence, assessment, testing, mapping, or release artifacts.

## Document Map and Follow-up Status

For document classification and navigation, see `docs/en/document-map.md`.

For temporary v0.5.x follow-up status, see `docs/en/status/v050x-follow-up-status.md`.

For v0.5.x incorporation decision direction, see `docs/en/status/v050x-incorporation-decision-register.md`.

For v0.5.x testing candidate selection, see `docs/en/status/v050x-testing-candidate-selection.md`.

For v0.5.x testing procedure candidate matrix, see `docs/en/status/v050x-testing-procedure-candidate-matrix.md`.

For v0.5.x testing candidate mapping, see `docs/en/status/v050x-testing-candidate-mapping.md`.

For v0.5.x draft pass/fail criteria, see `docs/en/status/v050x-testing-draft-pass-fail-criteria.md`.

For v0.5.x testing incorporation readiness review, see `docs/en/status/v050x-testing-incorporation-readiness-review.md`.

For v0.5.x principal context testing proposal, see `docs/en/status/v050x-principal-context-testing-proposal.md`.

For v0.5.x principal context testing candidate appendix, see `docs/en/status/v050x-principal-context-testing-candidate-appendix.md`.

For v0.5.x principal context testing CSV refinement proposal, see `docs/en/status/v050x-principal-context-testing-csv-refinement-proposal.md`.

For v0.5.x cross-agent delegation testing proposal, see `docs/en/status/v050x-cross-agent-delegation-testing-proposal.md`.

For v0.5.x cross-agent delegation testing candidate appendix, see `docs/en/status/v050x-cross-agent-delegation-testing-candidate-appendix.md`.

For v0.5.x cross-agent delegation CSV refinement proposal, see `docs/en/status/v050x-cross-agent-delegation-csv-refinement-proposal.md`.

For v0.5.x approval quality testing proposal, see `docs/en/status/v050x-approval-quality-testing-proposal.md`.

For v0.5.x approval quality testing candidate appendix, see `docs/en/status/v050x-approval-quality-testing-candidate-appendix.md`.

For v0.5.x approval quality CSV refinement proposal, see `docs/en/status/v050x-approval-quality-csv-refinement-proposal.md`.

For v0.5.x evidence integrity CSV refinement proposal, see `docs/en/status/v050x-evidence-integrity-csv-refinement-proposal.md`.

For the v0.5.x incorporation review checkpoint, see `docs/en/status/v050x-incorporation-review-checkpoint.md`.

For the v0.5.x next phase track plan, see `docs/en/status/v050x-next-phase-track-plan.md`.

For the v0.5.x evidence schema and examples track proposal, see `docs/en/status/v050x-evidence-schema-and-examples-track-proposal.md`.

For the v0.5.x evidence schema field proposal, see `docs/en/status/v050x-evidence-schema-field-proposal.md`.

For the v0.5.x evidence example design proposal, see `docs/en/status/v050x-evidence-example-design-proposal.md`.

For the v0.5.x evidence schema/example implementation readiness review, see `docs/en/status/v050x-evidence-schema-example-implementation-readiness.md`.

For the v0.5.x evidence integrity negative tests track proposal, see `docs/en/status/v050x-evidence-integrity-negative-tests-track-proposal.md`.

For the v0.5.x evidence integrity negative tests candidate appendix, see `docs/en/status/v050x-evidence-integrity-negative-tests-candidate-appendix.md`.

For the v0.5.x evidence integrity negative tests CSV refinement proposal, see `docs/en/status/v050x-evidence-integrity-negative-tests-csv-refinement-proposal.md`.

For the v0.5.x incident-response evidence preservation guidance proposal, see `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md`.

For the v0.5.x incident-response evidence preservation candidate appendix, see `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md`.

For the v0.5.x evidence depth and E5 profile decision proposal, see `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md`.

For the v0.5.x negative evidence examples and validator fixtures decision proposal, see `docs/en/status/v050x-negative-evidence-examples-fixtures-decision-proposal.md`.

For the v0.5.x `AAEF-EVD-01` evidence sufficiency and limitation review proposal, see `docs/en/status/v050x-evd01-evidence-sufficiency-limitation-review-proposal.md`.

For the v0.5.x issue #165 evidence integrity consolidation checkpoint, see `docs/en/status/v050x-issue-165-evidence-integrity-consolidation-checkpoint.md`.

For the v0.5.x tamper-evident evidence selected contexts proposal, see `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-proposal.md`.

## Research Motivation

AAEF focuses on a specific problem in agentic AI assurance:

How should authority, execution boundaries, and evidence be structured when AI agents perform actions on behalf of human or organizational principals?

AAEF does not attempt to make model output itself authoritative.

Instead, AAEF treats authority as something that should be granted, scoped, checked, enforced, evidenced, reviewable, and revocable outside the model output itself.

## Core Research Claims

### Model output is not authority

A model recommendation, plan, tool-call proposal, or explanation should not by itself authorize an action.

Authority should be represented through trusted decision, policy, workflow, approval, backend, or enforcement components rather than inferred from model output alone.

### Authority should be action-bound

Authority should be tied to a principal, action, target, scope, policy context, validity window, and evidence context.

This is especially important for high-impact actions, long-running workflows, delegated tasks, and cross-agent handoffs.

### Evidence is not merely logging

Logs are not automatically evidence.

Evidence should be attributable, action-bound, context-bound, reviewable, and sufficiently independent or corroborated for the assessed action and risk level.

### Inter-agent communication is not delegation authority

An agent may be able to communicate with another agent without being authorized to delegate work, expand scope, spend resources, invoke high-impact capabilities, or cross an authority boundary.

This distinction is central to AAEF's v0.5.x follow-up work on cross-agent and cross-domain authority.

## What v0.5.0 Added

AAEF v0.5.0 added non-normative planning models and decision records for future development.

Key materials include:

| Topic | Document |
| --- | --- |
| v0.5.0 planning overview | `docs/en/33-v050-planning-overview.md` |
| Incorporation rules and outcome register | `docs/en/34-v050-control-design-options.md` |
| Authority Lifecycle Model | `docs/en/50-authority-lifecycle-model.md` |
| Evidence Integrity Levels | `docs/en/51-evidence-integrity-levels.md` |
| Approval Quality Model | `docs/en/52-approval-quality-model.md` |
| v0.5.0 release scope decision | `docs/en/53-v050-release-scope-decision.md` |
| v0.5.0 release preparation checklist | `docs/en/54-v050-release-preparation-checklist.md` |

These documents do not change the v0.4.1 control and assessment baseline by themselves.

## Relationship to Open Research Questions

This document is an entry point.

The detailed catalog of open research questions is maintained in:

- `docs/en/19-open-research-questions.md`

Use this document to understand the research framing, reading order, and review priorities.

Use `docs/en/19-open-research-questions.md` to review the detailed unresolved questions and possible research projects.

## Relationship to Existing Research Areas

AAEF intersects with several research and practice areas:

- AI agent safety;
- AI governance;
- access control and authorization;
- auditability and evidence design;
- workflow security;
- multi-agent systems;
- security assurance;
- GRC and compliance assessment;
- incident reconstruction;
- human approval and oversight.

AAEF is narrower than general AI safety and broader than simple logging, prompt guardrails, or tool-use policy.

Its focus is action assurance: whether an agentic action was authorized, bounded, enforced, evidenced, and reviewable.

## Suggested Reading Path for Researchers

Researchers may start with the following sequence:

1. `README.md`
2. `docs/en/00-introduction.md`
3. `docs/en/02-core-principles.md`
4. `docs/en/03-definitions.md`
5. `docs/en/05-trust-model.md`
6. `docs/en/16-assurance-model.md`
7. `docs/en/18-implementation-guidance.md`
8. `docs/en/19-open-research-questions.md`
9. `docs/en/33-v050-planning-overview.md`
10. `docs/en/50-authority-lifecycle-model.md`
11. `docs/en/51-evidence-integrity-levels.md`
12. `docs/en/52-approval-quality-model.md`
13. `docs/en/53-v050-release-scope-decision.md`
14. `docs/en/59-principal-context-degradation-testing.md`
15. `docs/en/60-evidence-integrity-profile-guidance.md`
16. `docs/en/61-tamper-evident-evidence-requirements.md`
17. `docs/en/62-approval-quality-testing-guidance.md`

For readers focused on cross-agent systems, start with:

1. `docs/en/31-cross-agent-cross-domain-authority.md`
2. `docs/en/46-cross-agent-authority-examples.md`
3. `docs/en/50-authority-lifecycle-model.md`
4. `docs/en/56-capability-scoped-cross-agent-delegation.md`
5. `docs/en/57-cross-agent-delegation-negative-tests.md`
6. `docs/en/58-cross-agent-budget-propagation.md`
7. the open Cross-Agent and Cross-Domain Authority umbrella issue and related v0.5.x follow-up issues.

## Current v0.5.x Follow-up Areas

The active v0.5.x follow-up work includes:

- principal context degradation testing criteria;
- capability-scoped cross-agent delegation controls;
- delegation acceptance/refusal and chain accountability negative tests;
- cross-agent budget propagation guidance;
- evidence integrity levels for high-impact and audit-grade profiles;
- tamper-evident evidence requirements for selected contexts;
- approval quality testing and evidence expectations.

These follow-up items may later inform guidance, testing refinements, evidence expectations, assessment profiles, schema candidates, or control refinements.

## Review Questions for Researchers

Feedback is especially useful on the following questions.

### Authority and delegation

- Is the action-bound authority model implementable in real agentic systems?
- When does principal context degrade enough to require reauthorization?
- How should authority be attenuated across tools, subgoals, agents, or domains?
- Should cross-agent capability-scoped delegation become a dedicated control area?

### Evidence and auditability

- What evidence is necessary to reconstruct an agentic action chain?
- Which evidence artifacts are most useful for incident reconstruction?
- When is independently generated or corroborated evidence required?
- When should tamper-evident evidence be required, recommended, or optional?

### Human approval

- When does human approval become meaningful authorization?
- How should approval fatigue be measured?
- What evidence proves that approval was bound to the canonical action executed?
- How should approval, reauthorization, override, and break-glass evidence be distinguished?

### Adversarial behavior

- How can systems detect approval laundering, task splitting, retry-after-denial loops, or authority drift?
- Which AAEF assumptions are easiest to bypass?
- Which planning concepts are too broad, too strict, or too vague?
- Where should AAEF prefer implementation-neutral properties over specific mechanisms?

## Non-Goals

This document is not a control catalog.

It is not an implementation checklist.

It does not claim that AAEF has solved the research questions it identifies.

It does not make v0.5.0 planning material normative.

The purpose is to help researchers and reviewers understand where AAEF currently stands, what problems it is trying to frame, and where focused review or empirical study would be most useful.
