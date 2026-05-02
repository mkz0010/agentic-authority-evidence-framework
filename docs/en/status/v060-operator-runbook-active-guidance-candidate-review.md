# AAEF v0.6.x Operator Runbook Active Guidance Candidate Review

Status: Active guidance candidate review  
Related issue: #283  
Related roadmap: #241  
Related split plan: `docs/en/status/v060-adoption-follow-up-split-planning.md`  
Related operator planning artifact: `docs/en/status/v060-operator-runbook-planning.md`  
Related operational responsibility matrix: `docs/en/status/v060-operational-responsibility-matrix-planning.md`  
Related adoption package index: `docs/en/status/v060-adoption-package-index-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document reviews whether the v0.6.0 operator runbook planning artifact contains material that should later be promoted into active operational guidance.

The purpose is not to promote the runbook immediately.

The purpose is to separate:

- reusable operational guidance candidates,
- organization-specific illustrative material,
- candidate operational checklists,
- candidate escalation and freeze/hold guidance,
- evidence and monitoring review expectations,
- operational metrics and reporting candidates,
- and claim-boundary requirements.

This document is review and planning material. It does not change active controls, evidence schema, assessment artifacts, testing procedures, examples, mappings, or the current control and assessment baseline.

## Review scope

This review covers:

- `docs/en/status/v060-operator-runbook-planning.md`
- related operational responsibility expectations
- whether selected runbook sections should later become active operational guidance

This review does not cover:

- product-specific SIEM queries,
- production incident response procedures,
- legally binding operational requirements,
- certification criteria,
- audit sufficiency criteria,
- or organization-specific operating models.

## Source artifact summary

| Source artifact | Role | Current status |
| --- | --- | --- |
| `v060-operator-runbook-planning.md` | Operator runbook planning | Non-normative planning material |
| `v060-operational-responsibility-matrix-planning.md` | Operational role/responsibility planning | Non-normative planning material |
| `v060-adoption-package-index-planning.md` | Role-based adoption navigation | Non-normative planning material |
| `examples/evidence/README.md` | Evidence example candidate entry point | Active example candidate documentation |
| `mappings/README.md` | External mapping entry point | Informative mapping documentation |

## Candidate promotion question

The central question is:

> Should parts of the operator runbook planning artifact become active AAEF operational guidance in a later PR?

This review answers:

> Several sections are strong candidates for later active operational guidance, but promotion should be selective and should preserve organization-specific flexibility.

## Review criteria

Candidate operational guidance should be reviewed against the following criteria.

| Criterion | Question |
| --- | --- |
| Reusability | Can many organizations use the guidance without major customization? |
| Role clarity | Does the guidance clarify who does what? |
| Operational usefulness | Does it help daily, weekly, monthly, or incident-driven operations? |
| Evidence linkage | Does it connect operations to evidence review and reconstruction? |
| Boundary clarity | Does it preserve AAEF's action-boundary and evidence boundaries? |
| Non-prescriptiveness | Does it avoid forcing a single operating model? |
| Tool neutrality | Does it avoid product-specific SIEM, SOAR, ticketing, or cloud assumptions? |
| Claim boundary | Does it avoid audit sufficiency, compliance, certification, and production-readiness claims? |
| Maintainability | Can it be kept current as AAEF evolves? |

## Strong active guidance candidates

The following runbook concepts are strong candidates for later active guidance.

| Candidate area | Initial disposition | Reason |
| --- | --- | --- |
| Daily operator review questions | Promote later | Useful across organizations and low risk. |
| Weekly evidence and exception review | Promote later | Supports recurring assurance without being too prescriptive. |
| Freeze/hold trigger review | Promote later with caution | Operationally important, but may require organization-specific thresholds. |
| Failed/denied action review | Promote later | Closely aligned with AAEF fail-closed posture and evidence examples. |
| Evidence availability checks | Promote later | Supports evidence trust and reconstruction. |
| Escalation decision questions | Promote later with caution | Useful but escalation paths differ by organization. |
| Handoff points between operators, risk owners, and implementers | Promote later | Helps adoption and responsibility clarity. |
| Operational metrics categories | Promote later as illustrative categories | Useful for reporting, but exact metrics should remain organization-specific. |

## Areas that should remain illustrative or organization-specific

The following areas should not be promoted as binding guidance without further review.

| Area | Reason |
| --- | --- |
| Product-specific SIEM queries | Tooling differs significantly. |
| Exact alert thresholds | Thresholds depend on risk appetite and system design. |
| Staffing models | Organization-specific. |
| Incident severity taxonomy | Often defined by existing IR programs. |
| Retention periods | Legal, regulatory, contractual, and organizational context dependent. |
| Escalation time limits | Operationally useful, but organization-specific. |
| Evidence store architecture | Should align with architecture and TCB decisions. |
| On-call procedures | Organization-specific. |

## Daily operator guidance candidate review

Daily operator guidance is a strong active guidance candidate if it remains question-based rather than prescriptive.

Candidate questions:

- Were high-impact agentic actions executed in the last review period?
- Were any high-impact agentic actions denied or not executed?
- Were any actions executed without expected authorization evidence?
- Were any actions executed with expired or mismatched authorization decisions?
- Were any backend relying-party verification checks missing or failed?
- Were any evidence events missing, delayed, incomplete, or inconsistent?
- Were any freeze/hold states triggered or bypassed?
- Were denied actions reviewed for repeated attempts or suspicious patterns?

Initial disposition:

> Promote later as reusable daily review guidance, not as a mandatory checklist for all environments.

## Weekly/monthly review candidate

Weekly or monthly review guidance is also a strong candidate if framed as review categories.

Candidate review categories:

- evidence completeness trends,
- denied-action trends,
- exception aging,
- repeated policy mismatch patterns,
- freeze/hold usage,
- backend verification failures,
- stale authorization decision attempts,
- risk-owner exception decisions,
- operator handoff issues,
- unresolved reconstruction gaps.

Initial disposition:

> Promote later as recurring review guidance with organization-specific cadence.

## Incident and exception candidate review

Incident and exception guidance is valuable but should remain conservative.

Candidate incident/exception questions:

- Did the agentic action cross an expected boundary?
- Was the action authorized at the action boundary?
- Was authorization based on trusted policy inputs rather than model output alone?
- Did dispatch enforcement validate the authorization decision?
- Did the backend independently verify the decision before execution?
- Was evidence generated by an appropriate component?
- Can the action be reconstructed without relying solely on model self-report?
- Was the action denied, held, or executed?
- Who accepted residual risk or exception handling?

Initial disposition:

> Promote later as incident reconstruction guidance, not as a complete incident response procedure.

## Freeze/hold guidance candidate review

Freeze/hold behavior is operationally important but sensitive.

Candidate guidance:

- Define conditions under which agentic action execution should be paused.
- Preserve evidence of freeze/hold activation.
- Record who initiated or approved freeze/hold.
- Record whether attempted actions were denied because freeze/hold was active.
- Ensure post-freeze review covers denied attempts and any emergency overrides.

Risks:

- Thresholds can be organization-specific.
- Freeze/hold may affect business continuity.
- Emergency override handling may require governance and legal review.

Initial disposition:

> Promote later only as high-level freeze/hold guidance, not as specific operational thresholds.

## Evidence review candidate

Evidence review guidance is one of the strongest candidates for active guidance.

Candidate guidance:

- Review whether evidence links action request, authorization decision, dispatch enforcement, backend verification, and execution/non-execution outcome.
- Review whether evidence contains limitations and trust assumptions.
- Review whether evidence was generated outside model-only self-reporting.
- Review whether evidence supports reconstruction.
- Review whether non-execution events are recorded, not only successful execution events.

Initial disposition:

> Promote later as active operational evidence review guidance.

## Operator metrics candidate review

Metrics are useful, but should be framed carefully.

Candidate metric categories:

- number of high-impact actions requested,
- number of high-impact actions executed,
- number of denied/non-executed actions,
- authorization mismatch rate,
- backend verification failure rate,
- missing evidence event count,
- stale or expired decision attempts,
- exception count and aging,
- freeze/hold activation count,
- reconstruction success rate.

Initial disposition:

> Promote later as illustrative metric categories, not required KPIs.

## Handoff guidance candidate review

Operational handoff guidance is a strong candidate because AAEF adoption requires multiple roles.

Candidate handoff points:

- operator to implementer when enforcement gaps are found,
- operator to risk owner when exceptions or residual risk decisions are required,
- operator to auditor/reviewer when evidence requests are made,
- operator to security architecture when TCB or evidence boundary issues appear,
- operator to legal/compliance when retention, privacy, or contractual issues arise.

Initial disposition:

> Promote later as reusable handoff guidance.

## Active guidance placement options

Potential placement options:

| Option | Description | Initial disposition |
| --- | --- | --- |
| Keep in `docs/en/status/` | Leave as planning/review material | Good short-term, low risk |
| Add `docs/en/operations/README.md` | Create an operations entry point | Candidate if operational materials grow |
| Add `docs/en/operator-guidance.md` | Create a single active operator guidance document | Candidate for focused promotion |
| Add to existing assessment docs | Integrate with assessment flow | Defer; may blur assessment vs operations |
| Add checklist under examples/templates | Create a practical checklist artifact | Candidate later |
| Keep as role path in adoption index | Maintain role navigation only | Good fallback |

Initial recommendation:

> Do not create active operator guidance in this PR. Use a later PR to either add a focused `docs/en/operator-guidance.md` or create an operations entry point if more operational artifacts are expected.

## Promotion readiness checklist

Before promoting any operator runbook material into active guidance, confirm:

- guidance is tool-neutral,
- guidance is role-clear,
- guidance is not organization-specific,
- exact thresholds are avoided or marked illustrative,
- evidence review linkage is preserved,
- non-execution review is included,
- freeze/hold guidance is high-level unless separately approved,
- claim boundaries are explicit,
- baseline status is preserved,
- and no audit sufficiency or production-readiness claim is implied.

## Recommended next follow-up

Recommended next follow-up after this review:

> Define active operator guidance placement and scope.

Candidate future artifact:

- `docs/en/status/v060-operator-guidance-placement-and-scope-planning.md`

Alternative future implementation:

- `docs/en/operator-guidance.md`

If moving directly to active guidance, the implementation PR should be narrow and should avoid thresholds, product-specific monitoring rules, and audit sufficiency language.

## Relationship to #283

This document partially addresses #283 by reviewing the operator runbook planning artifact for active guidance candidates.

#283 should remain open until one of the following occurs:

- active operator guidance placement and scope are defined,
- active guidance is created,
- or promotion is explicitly deferred.

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

This review is sufficient when:

- reusable active guidance candidates are identified,
- organization-specific areas are separated,
- daily/weekly review candidates are documented,
- evidence review candidates are documented,
- freeze/hold and incident guidance risks are identified,
- placement options are described,
- promotion readiness criteria are documented,
- and no active baseline change is implied.
