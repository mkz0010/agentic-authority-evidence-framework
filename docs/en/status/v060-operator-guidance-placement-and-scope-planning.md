# AAEF v0.6.x Operator Guidance Placement and Scope Planning

Status: Operator guidance placement and scope planning  
Related issue: #283  
Related roadmap: #241  
Related candidate review: `docs/en/status/v060-operator-runbook-active-guidance-candidate-review.md`  
Related operator runbook planning: `docs/en/status/v060-operator-runbook-planning.md`  
Related operational responsibility matrix: `docs/en/status/v060-operational-responsibility-matrix-planning.md`  
Related adoption package index: `docs/en/status/v060-adoption-package-index-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document defines where future active operator guidance should live and what scope it should cover.

It follows the Operator Runbook Active Guidance Candidate Review.

The purpose is to prevent operational guidance from becoming too broad, too organization-specific, or too prescriptive.

This document is planning material. It does not create active operator guidance, active operational requirements, active controls, evidence schema changes, assessment artifacts, testing procedures, or current baseline changes.

## Decision posture

The current posture is:

> Operator guidance should be useful for day-to-day AAEF-style operations, but it should remain tool-neutral, organization-flexible, evidence-centered, and non-certification-oriented.

The next active guidance should focus on reusable operational review questions and handoff expectations.

It should not define:

- SIEM queries,
- SOAR playbooks,
- staffing models,
- exact alert thresholds,
- incident severity taxonomies,
- retention periods,
- on-call schedules,
- or organization-specific escalation timelines.

## Source artifacts

| Source artifact | Role |
| --- | --- |
| `v060-operator-runbook-planning.md` | Broad non-normative operator runbook planning |
| `v060-operator-runbook-active-guidance-candidate-review.md` | Review of reusable active guidance candidates |
| `v060-operational-responsibility-matrix-planning.md` | Candidate role and responsibility context |
| `v060-adoption-package-index-planning.md` | Role-based navigation context |
| `examples/evidence/README.md` | Evidence example candidate entry point |
| `docs/en/status/v060-auditor-evidence-request-checklist-planning.md` | Auditor/reviewer evidence request context |
| `docs/en/status/v060-consultant-discovery-checklist-planning.md` | Consultant discovery context |

## Candidate placement options

| Option | Description | Initial disposition |
| --- | --- | --- |
| `docs/en/operator-guidance.md` | Single active operator guidance document | Preferred next active guidance target |
| `docs/en/operations/README.md` | Dedicated operations area | Defer until multiple operations documents exist |
| `docs/en/status/` only | Keep all material as planning/review | Safe but limits adoption usefulness |
| `examples/operations/` | Practical checklists/templates | Defer until active guidance stabilizes |
| Existing assessment docs | Integrate operator review into assessment flow | Defer; may blur assessment vs operations |
| Adoption index only | Keep guidance discoverable only through adoption package index | Useful navigation, but not enough as active guidance |

## Initial placement decision

Initial recommendation:

> Use `docs/en/operator-guidance.md` as the first focused active operator guidance document.

Rationale:

- It is easy to find.
- It avoids creating a broad operations directory too early.
- It keeps the first active guidance artifact focused.
- It separates operator guidance from assessment methodology.
- It supports implementers, operators, auditors, consultants, and risk owners without overloading the README.

Deferred:

- `docs/en/operations/README.md`
- `examples/operations/`
- product-specific runbook templates
- SIEM/SOAR-specific procedures

## Active guidance scope

The first active operator guidance document should cover:

1. purpose and scope,
2. operator role context,
3. daily review questions,
4. recurring evidence review categories,
5. denied / non-executed action review,
6. evidence availability and reconstruction checks,
7. high-level freeze/hold review,
8. handoff points,
9. illustrative operational metrics categories,
10. claim boundaries and non-goals.

It should not cover:

- exact review frequency requirements,
- incident severity definitions,
- mandatory staffing or role structures,
- specific tooling,
- exact thresholds,
- legal retention periods,
- contractual evidence retention terms,
- or audit sufficiency criteria.

## Candidate active guidance sections

Recommended sections for `docs/en/operator-guidance.md`:

| Section | Include? | Notes |
| --- | --- | --- |
| Purpose | Yes | Explain operator-facing use. |
| Scope | Yes | Clarify tool-neutral and non-certification posture. |
| Operator role context | Yes | Link to responsibility planning without making staffing claims. |
| Daily review questions | Yes | Strong candidate from review. |
| Recurring review categories | Yes | Use weekly/monthly as examples, not requirements. |
| Denied/non-executed action review | Yes | Central to AAEF fail-closed posture. |
| Evidence availability checks | Yes | Central to evidence/reconstruction value. |
| Freeze/hold review | Yes, high level only | Avoid thresholds. |
| Handoff points | Yes | Useful across organizations. |
| Metrics categories | Yes, illustrative only | Avoid required KPIs. |
| Product-specific queries | No | Defer. |
| Incident response procedure | No | Not an IR playbook. |
| Staffing model | No | Organization-specific. |
| Retention periods | No | Legal/contractual context dependent. |

## Operator guidance boundary language

Future active operator guidance should include language such as:

> This document provides operator-facing guidance for reviewing AAEF-style agentic action assurance signals, evidence, denied/non-executed actions, and handoff points. It does not define mandatory staffing models, SIEM queries, incident response procedures, retention periods, certification criteria, audit sufficiency, or legal/compliance obligations.

## Daily review scope

Daily review guidance should remain question-based.

Candidate questions:

- Were high-impact agentic actions requested?
- Which high-impact actions executed?
- Which actions were denied or not executed?
- Were denied actions expected?
- Were any repeated denied attempts observed?
- Were authorization decisions present and unexpired?
- Did dispatch enforcement use the expected decision?
- Did backend verification occur where expected?
- Were evidence events present, complete, and linkable?
- Are there reconstruction gaps?
- Did freeze/hold status affect any attempted actions?
- Are any issues ready for handoff to implementers, risk owners, auditors, or security architects?

## Recurring evidence review scope

Recurring review should cover categories rather than fixed cadence.

Candidate categories:

- evidence completeness,
- authorization mismatch patterns,
- backend verification failures,
- stale decision attempts,
- denied/non-executed action trends,
- exception aging,
- freeze/hold events,
- reconstruction gaps,
- evidence limitation patterns,
- repeated action attempts near policy boundaries.

The active guidance should say organizations may adapt cadence based on risk, impact, and operating model.

## Denied and non-executed action review scope

Denied and non-executed action review should be included because it is central to AAEF.

Candidate review questions:

- Why was the action denied or not executed?
- Which boundary denied it?
- Was the denial expected under policy?
- Was backend invocation prevented where appropriate?
- Was non-execution evidence recorded?
- Was the attempted action repeated?
- Was there evidence of prompt-influenced or untrusted-input-influenced request drift?
- Does the pattern require implementer, risk owner, or security review?

## Freeze/hold scope

Freeze/hold guidance should remain high-level.

Include:

- whether freeze/hold was active,
- who initiated or approved it,
- which attempted actions were affected,
- whether attempted actions were denied during freeze/hold,
- whether emergency override occurred,
- whether post-freeze review was completed.

Do not include:

- exact freeze thresholds,
- business continuity decisions,
- emergency override approval hierarchies,
- or mandatory recovery timelines.

## Handoff scope

Active operator guidance should identify handoff points.

Candidate handoffs:

| Handoff | Trigger |
| --- | --- |
| Operator to implementer | Enforcement, logging, evidence, or backend verification gap |
| Operator to risk owner | Exception, residual risk, or repeated high-impact denial pattern |
| Operator to auditor/reviewer | Evidence request, reconstruction request, or control review |
| Operator to security architect | TCB, evidence boundary, or architecture weakness |
| Operator to legal/compliance | Retention, privacy, contractual, or legal concern |

## Metrics scope

Metrics should be illustrative categories, not required KPIs.

Candidate categories:

- high-impact action requests,
- executed high-impact actions,
- denied/non-executed actions,
- authorization mismatch rate,
- backend verification failure count,
- missing evidence event count,
- stale decision attempts,
- freeze/hold activation count,
- exception aging,
- reconstruction success or gap rate.

## Explicit exclusions

The first active operator guidance should explicitly exclude:

- product-specific SIEM queries,
- SOAR automation rules,
- on-call schedules,
- exact staffing requirements,
- exact alert thresholds,
- retention schedules,
- legal advice,
- compliance determination,
- certification criteria,
- audit sufficiency,
- production-readiness claims,
- and incident response playbook replacement.

## Relationship to active baseline

Future active operator guidance may be active guidance without changing the current control and assessment baseline.

If guidance is added, it should state:

- it supports operation and adoption,
- it does not update active controls unless explicitly stated,
- it does not update evidence schema unless explicitly stated,
- it does not update assessment artifacts unless explicitly stated,
- it does not update testing procedures unless explicitly stated,
- and v0.4.1 remains the current control and assessment baseline unless a later release explicitly changes it.

## Recommended next implementation PR

Recommended next PR:

> Add `docs/en/operator-guidance.md`.

Candidate PR scope:

- create a concise active operator guidance document,
- keep it tool-neutral,
- include daily review questions,
- include recurring evidence review categories,
- include denied/non-executed action review,
- include evidence availability checks,
- include high-level freeze/hold review,
- include handoff points,
- include illustrative metrics categories,
- preserve claim boundaries,
- register it in `docs/en/document-map.md`,
- optionally link it from the adoption package index.

Do not include:

- thresholds,
- SIEM queries,
- staffing models,
- retention periods,
- or incident response procedures.

## Relationship to #283

This document further addresses #283 by defining placement and scope for future active operator guidance.

#283 should remain open until one of the following occurs:

- active operator guidance is created,
- active guidance promotion is explicitly deferred,
- or a separate implementation issue is created.

## Non-goals

This document does not:

- create active operator guidance,
- create operational requirements,
- create product-specific monitoring rules,
- define SIEM or SOAR queries,
- define incident response procedures,
- define staffing models,
- define retention periods,
- promote planning material into active requirements,
- change active controls,
- change the current control and assessment baseline,
- update evidence schema,
- update assessment artifacts,
- update testing procedures,
- assert production readiness,
- assert implementation conformance,
- assert audit sufficiency,
- claim compliance,
- claim certification,
- claim conformity,
- or claim equivalence with external frameworks.

## Acceptance criteria

This planning document is sufficient when:

- active operator guidance placement is selected,
- active operator guidance scope is defined,
- excluded areas are documented,
- first active guidance document sections are proposed,
- claim boundaries are preserved,
- next implementation PR is defined,
- and no active baseline change is implied.
