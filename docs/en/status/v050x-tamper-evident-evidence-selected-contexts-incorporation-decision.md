# v0.5.x Tamper-Evident Evidence Selected Contexts Incorporation Decision

**Status:** Temporary, non-normative incorporation decision

## Purpose

This document records the incorporation decision after the v0.5.x tamper-evident evidence selected contexts proposal and candidate appendix.

It follows:

- `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-proposal.md`
- `docs/en/status/v050x-tamper-evident-evidence-selected-contexts-candidate-appendix.md`
- `docs/en/status/v050x-issue-165-evidence-integrity-consolidation-checkpoint.md`
- `docs/en/status/v050x-evidence-depth-e5-profile-decision-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md`
- `docs/en/status/v050x-follow-up-status.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Primary source issue:

- #166 — define tamper-evident evidence requirements for selected contexts

Related active rows:

- `AAEF-EVD-04`
- `AAEF-EVD-01`

This decision does not update active testing procedures.

It does not update the Evidence Event Schema.

It does not add evidence examples.

It does not add validator fixtures.

It does not close #166 by itself.

## Decision Summary

Selected-context tamper-evident evidence requirements should remain guidance-only for the current v0.5.x follow-up cycle.

Decision:

| Area | Decision |
| --- | --- |
| Active CSV change | Not required at this time |
| Evidence Event Schema change | Not required at this time |
| Evidence example change | Not required at this time |
| Validator fixture or behavior change | Not required at this time |
| Context tier fields | Not added |
| Candidate context IDs | Not added to active CSV |
| Stable guidance extraction | Candidate future work |
| Issue #166 disposition | Continue with status tracking / close-readiness review after this decision |

## Rationale

The selected-context proposal and appendix provide enough detail for review without requiring immediate active artifact changes.

Reasons:

- `AAEF-EVD-04` already covers evidence integrity and tamper-evident evidence at the active testing procedure level.
- `AAEF-EVD-01` already covers evidence sufficiency and action reconstruction.
- Selected contexts are useful for guidance, but should not become schema values before implementation feedback.
- Context-specific tamper-evident evidence requirements may vary by organization, impact, reversibility, dispute likelihood, and implementation maturity.
- Adding context tiers to the Evidence Event Schema could imply a false certification or scoring model.
- Adding candidate context IDs to active CSV could overfit the current proposal before the context model stabilizes.
- Examples may be useful later, but should follow stable selected-context guidance.

## Current Guidance Outcome

The current selected-context guidance identifies:

- contexts where tamper-evident evidence should normally be expected;
- contexts where it should be strongly recommended;
- contexts where ordinary evidence may be acceptable unless escalation factors apply;
- cross-cutting escalation factors that increase evidence integrity expectations;
- common tamper-evident evidence package expectations;
- relationship to `AAEF-EVD-04`, `AAEF-EVD-01`, E5/evidence depth, and incident response.

This is sufficient for the current planning stage.

## Active CSV Decision

No active testing procedure CSV refinement is recommended at this time.

`AAEF-EVD-04` should remain mechanism-neutral and context-neutral in the current active CSV.

A later refinement may be considered if reviewers decide that selected-context guidance should be referenced directly in active testing criteria.

## Schema Decision

No Evidence Event Schema change is recommended at this time.

Do not add fields such as:

- `tamper_evident_context`;
- `context_tier`;
- `selected_context_id`;
- `tamper_evident_required`;
- `tamper_evident_profile`;
- `evidence_depth_level`;
- `e5_compliant`.

Those fields may create false precision or imply certification semantics before the selected-context model is stable.

## Example Decision

No new evidence example is required at this time.

Future examples may be useful after the selected-context model stabilizes.

Candidate future examples may include:

- financial action with required tamper-evident evidence;
- access control change with required tamper-evident evidence;
- low-impact read-only action with optional evidence expectations;
- incident-response evidence package with failed or unavailable verification state;
- approval-gated action where tamper-evident approval-to-execution binding is expected.

## Validator Decision

No validator change is recommended at this time.

The validator should continue to answer structural schema validity questions.

It should not determine whether:

- a selected context applies;
- tamper-evident evidence is required;
- evidence is sufficient;
- evidence is complete;
- evidence is independently corroborated;
- an action is high-impact;
- an action is safe or authorized.

Those decisions belong to assessment, policy, risk classification, and review procedures.

## Guidance-Only Decision

The selected contexts should remain non-normative guidance for now.

Recommended current handling:

1. Keep the selected-context proposal and appendix as temporary v0.5.x coordination material.
2. Do not incorporate context IDs into active CSV.
3. Do not add schema fields for selected-context tiers.
4. Do not create examples until selected-context guidance stabilizes.
5. Use the appendix as reviewer-facing planning material.
6. Consider stable guidance extraction later.

## Relationship to #166

This decision advances #166 by resolving the immediate incorporation question.

Current #166 result:

- selected contexts proposal added;
- selected contexts candidate appendix added;
- incorporation decision recorded;
- active CSV, schema, example, and validator changes are not required for the current cycle.

#166 may become close-ready after a status update records this decision.

## Future Work Outside Immediate Incorporation

Future work may include:

- stable selected-context guidance extraction;
- implementer-facing selected-context examples;
- reviewer checklist integration;
- assessment quick-start integration;
- context-specific evidence package examples;
- public summary of tamper-evident evidence selected contexts;
- feedback-driven active CSV refinement.

These should not block the current incorporation decision.

## Non-Goals

This decision does not:

- update active testing procedure CSV;
- add testing procedure rows;
- add candidate IDs to active CSV;
- update the Evidence Event Schema;
- add evidence examples;
- add validator fixtures;
- update `tools/validate_evidence_schema.py`;
- create an evidence depth certification scale;
- create selected-context schema fields;
- change control catalog CSV;
- change human-readable control requirements;
- change assessment worksheet;
- change assessment profiles;
- change external framework mapping CSV;
- create GitHub issues;
- close #161, #163, #165, #166, or #167.

It records the selected-context incorporation decision before any issue closure decision.
