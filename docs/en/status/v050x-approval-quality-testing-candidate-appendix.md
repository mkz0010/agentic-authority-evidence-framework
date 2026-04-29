# v0.5.x Approval Quality Testing Candidate Appendix

**Status:** Temporary, non-normative testing candidate appendix

## Purpose

This document converts the approval quality testing proposal into candidate appendix form before any active testing procedure CSV update.

It builds on:

- `docs/en/status/v050x-approval-quality-testing-proposal.md`
- `docs/en/status/v050x-testing-incorporation-readiness-review.md`
- `docs/en/status/v050x-testing-draft-pass-fail-criteria.md`
- `docs/en/status/v050x-testing-candidate-mapping.md`
- `docs/en/status/v050x-testing-procedure-candidate-matrix.md`
- `docs/en/status/v050x-testing-candidate-selection.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Related guidance documents:

- `docs/en/39-approval-quality-approval-fatigue.md`
- `docs/en/40-approval-evidence-examples.md`
- `docs/en/47-approval-quality-assessment-guidance.md`
- `docs/en/52-approval-quality-model.md`
- `docs/en/62-approval-quality-testing-guidance.md`

This document does not change the v0.4.1 control and assessment baseline.

It does not update the active testing procedure CSV.

It does not create executable fixtures.

## Scope

This appendix covers six approval quality candidates:

- VTC-APP-01 — Vague Approval Prompt for High-Impact Action
- VTC-APP-02 — Approval to Draft Treated as Approval to Execute
- VTC-APP-03 — Canonical Action Mismatch
- VTC-APP-04 — Approval Payload Modified After Approval
- VTC-APP-08 — Model-Generated Approval Summary Accepted as Evidence
- VTC-APP-09 — Approval Without Independent Enforcement

These are candidate appendix entries only.

They are not active AAEF testing requirements.

## Candidate Appendix Format

Each candidate entry includes:

| Field | Meaning |
| --- | --- |
| Candidate ID | Temporary VTC candidate identifier. |
| Candidate title | Human-readable candidate title. |
| Candidate objective | What the candidate test is intended to verify. |
| Candidate procedure | Review-oriented procedure language. |
| Draft pass criteria | Draft pass intent for future testing procedure review. |
| Draft fail criteria | Draft fail intent for future testing procedure review. |
| Draft N/A criteria | Draft not-applicable intent. |
| Expected evidence | Evidence expected to support review. |
| Likely control area | Likely control or concept area affected. |
| Candidate applicability | Candidate profile or context applicability. |

## Candidate Appendix Entries

### VTC-APP-01 — Vague Approval Prompt for High-Impact Action

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-APP-01 |
| Candidate title | Vague Approval Prompt for High-Impact Action |
| Candidate objective | Verify that high-impact approval prompts present sufficient action-bound context before approval is relied upon. |
| Candidate procedure | Review approval prompts, tickets, approval UI, workflow records, or equivalent review surfaces for high-impact approval-gated actions. Determine whether the approver saw enough action, principal, authority, risk, scope, and consequence context before approving. |
| Draft pass criteria | The approval prompt presents the action, target, scope, risk, expected effect, principal context, authority basis, and material limitations before approval is granted or relied upon. Evidence links the approval decision to the final dispatched or executed action. |
| Draft fail criteria | A vague prompt such as “Proceed?” authorizes high-impact action, or evidence cannot show what the approver saw. |
| Draft N/A criteria | The system has no human approval workflow or no high-impact approval-gated actions. |
| Expected evidence | Approval prompt or review surface; context presented to approver; principal and agent context; requested action; target, resource, scope, risk, and expected effect; approval decision; linkage to final dispatched or executed action. |
| Likely control area | HUM / AUZ |
| Candidate applicability | High-impact actions, high-risk actions, delegated actions, externally effective actions, irreversible actions, approval-gated execution. |

### VTC-APP-02 — Approval to Draft Treated as Approval to Execute

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-APP-02 |
| Candidate title | Approval to Draft Treated as Approval to Execute |
| Candidate objective | Verify that approval for draft, analysis, preview, or recommendation does not authorize execute, publish, send, delete, spend, or externally effective action. |
| Candidate procedure | Review approval and execution records for workflows where lower-impact preparation or preview operations are distinct from execution operations. Determine whether approval is bound to the approved operation class. |
| Draft pass criteria | Approval is bound to the approved operation class, and execution-specific approval is required before externally effective action. Evidence shows approved operation class, attempted or executed operation class, mismatch check, and outcome. |
| Draft fail criteria | Lower-impact approval is reused for execution or externally effective action. |
| Draft N/A criteria | The system has no distinct draft, preview, analysis, recommendation, and execution operation classes. |
| Expected evidence | Approved operation class; attempted or executed operation class; approval scope; operation mismatch check; denial, reapproval, escalation, or execution outcome. |
| Likely control area | HUM / AUZ |
| Candidate applicability | Draft-to-send workflows, preview-to-publish workflows, recommendation-to-execution workflows, approval-gated external actions. |

### VTC-APP-03 — Canonical Action Mismatch

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-APP-03 |
| Candidate title | Canonical Action Mismatch |
| Candidate objective | Verify that the executed action matches the approved canonical action or requires fresh approval when materially different. |
| Candidate procedure | Compare the approved canonical action, action digest, action ID, or equivalent approval-bound representation with the final dispatched or executed action. Determine whether mismatch causes denial, reapproval, or escalation before execution. |
| Draft pass criteria | The executed action matches the approved canonical action, or material mismatch triggers reapproval, denial, or escalation before execution. |
| Draft fail criteria | A materially different action executes under prior approval. |
| Draft N/A criteria | The system has no approval-to-execution binding or no approval-gated execution path. |
| Expected evidence | Approved canonical action; action digest or canonical action ID where available; final dispatched or executed action; mismatch check; approval, reapproval, denial, or execution outcome. |
| Likely control area | HUM / AUZ / EVD |
| Candidate applicability | Approval-to-dispatch binding, approval-to-tool binding, canonical action IDs, action digests, externally effective execution. |

### VTC-APP-04 — Approval Payload Modified After Approval

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-APP-04 |
| Candidate title | Approval Payload Modified After Approval |
| Candidate objective | Verify that material post-approval changes to payload, target, recipient, amount, tool, environment, or effect invalidate approval or require reapproval. |
| Candidate procedure | Review approved action payloads and final execution payloads for post-approval changes. Determine whether material changes trigger invalidation, reapproval, denial, or escalation before execution. |
| Draft pass criteria | Material post-approval changes invalidate prior approval or require reapproval before execution. Evidence shows the approved payload, post-approval change, materiality or mismatch check, and resulting decision. |
| Draft fail criteria | Modified action executes under old approval after a material change. |
| Draft N/A criteria | The system does not allow post-approval modification before execution. |
| Expected evidence | Approved payload, target, recipient, amount, tool, or environment; post-approval modification; materiality or mismatch check; invalidation, reapproval, denial, escalation, or execution outcome. |
| Likely control area | HUM / AUZ / EVD |
| Candidate applicability | Approval-gated payloads, transfers, sends, deletes, publishes, production changes, externally effective actions. |

### VTC-APP-08 — Model-Generated Approval Summary Accepted as Evidence

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-APP-08 |
| Candidate title | Model-Generated Approval Summary Accepted as Evidence |
| Candidate objective | Verify that model-generated approval claims or summaries are not treated as approval evidence unless supported by trusted approval workflow records. |
| Candidate procedure | Review approval evidence sources and determine whether model-generated summaries, rationales, or claims are accepted as approval evidence without corroborating trusted workflow records. |
| Draft pass criteria | The system rejects model-only approval claims and relies on trusted approval workflow evidence. Evidence shows source trust status and the trusted approval record where applicable. |
| Draft fail criteria | Model-generated summary, rationale, or claim is treated as approval evidence. |
| Draft N/A criteria | The system has no model-generated approval summaries and no approval evidence ingestion path. |
| Expected evidence | Approval evidence source; trust status of evidence source; trusted approval workflow record where applicable; rejection or limitation of model-only approval claim; resulting authorization or execution decision. |
| Likely control area | HUM / EVD |
| Candidate applicability | Approval evidence ingestion, audit review, model-generated summaries, approval records, evidence quality review. |

### VTC-APP-09 — Approval Without Independent Enforcement

| Field | Candidate content |
| --- | --- |
| Candidate ID | VTC-APP-09 |
| Candidate title | Approval Without Independent Enforcement |
| Candidate objective | Verify that the execution boundary independently verifies approval state before execution. |
| Candidate procedure | Review approval-gated execution paths and determine whether the tool dispatcher, backend API, policy gateway, or equivalent execution boundary verifies approval state and scope before allowing execution. |
| Draft pass criteria | The execution boundary verifies approval state, approved action, approval scope, and linkage to the requested execution before allowing action. |
| Draft fail criteria | Execution proceeds based on agent self-report, UI state alone, or approval not verified at the execution boundary. |
| Draft N/A criteria | The system has no human approval-gated execution boundary. |
| Expected evidence | Approval event; enforcement check; approval state source; approved action or scope; execution decision; linkage between approval, authorization, dispatch, and execution. |
| Likely control area | HUM / AUZ / TOOL |
| Candidate applicability | Approval-gated tool calls, backend execution, policy gateways, high-impact actions, externally effective actions. |

## Minimal First Incorporation Subset

If a later PR updates active testing artifacts, the smallest initial subset should be:

- VTC-APP-01 — Vague Approval Prompt for High-Impact Action
- VTC-APP-03 — Canonical Action Mismatch
- VTC-APP-09 — Approval Without Independent Enforcement

These three candidates are the most directly tied to meaningful approval and execution-bound enforcement.

VTC-APP-02 and VTC-APP-04 should remain close behind, but may require clearer operation-class and materiality expectations before active incorporation.

VTC-APP-08 is strong, but may map more cleanly to evidence quality refinement than human approval refinement.

## Candidate Appendix Review Questions

Before any active testing procedure CSV update, reviewers should confirm:

- whether each candidate maps to existing HUM, AUZ, EVD, TOOL, or future approval quality rows;
- whether approval context and approval enforcement should be refined together or separately;
- whether model-only approval evidence should be handled under HUM, EVD, or both;
- whether minimum approval context fields should be profile-dependent;
- whether canonical action mismatch should be tested through approval, authorization, evidence, or all three;
- whether N/A criteria are narrow enough;
- whether the active control catalog already provides sufficient control coverage;
- whether a candidate appendix should be maintained separately from the active testing CSV;
- whether VTC-APP-01, VTC-APP-03, and VTC-APP-09 are sufficient as a first incorporation subset.

## Relationship to #167

This appendix supports #167 by converting selected approval quality tests into candidate appendix form.

It does not close #167.

Remaining #167 work includes:

- deciding whether any candidates should be incorporated into active testing artifacts;
- deciding whether approval quality requires new control catalog entries;
- defining minimum approval context fields;
- defining approval-to-execution binding evidence expectations;
- defining post-approval modification materiality;
- deciding whether related evidence/schema candidates are needed.

## Non-Goals

This document does not:

- update testing procedure CSV;
- add active testing procedure rows;
- create executable fixtures;
- add control IDs;
- change the control catalog;
- change the evidence schema;
- change assessment profiles;
- close #167;
- claim that the candidate entries are active AAEF requirements.

It is a temporary candidate appendix for the v0.5.x incorporation phase.
