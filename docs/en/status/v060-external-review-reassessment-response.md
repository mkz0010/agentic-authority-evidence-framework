# AAEF v0.6.0 External Review Reassessment Response

Status: External review response and follow-up synthesis  
Related roadmap: #241  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Related audit: `docs/en/status/v060-version-reference-audit.md`  
Related research positioning: `docs/en/status/v060-research-positioning-review.md`  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document records a response to an external reassessment of AAEF after the v0.6.0 version-reference clarification.

The reassessment correctly distinguished:

- v0.6.0 as the latest public review planning and adoption-readiness release,
- v0.5.0 as the prior public review planning release,
- v0.4.1 as the current control and assessment baseline,
- and v0.5.0 / v0.6.0 planning materials as non-normative unless explicitly incorporated or promoted.

The purpose of this response is to convert the reassessment into concrete follow-up direction for making AAEF more adoptable by:

- field implementers,
- auditors and assessors,
- operators and administrators,
- risk owners and managers,
- consultants and advisory teams,
- and research reviewers.

This document is review-response and planning material. It does not change active controls, schemas, assessment procedures, testing procedures, mappings, examples, or the current control and assessment baseline.

## Reassessment summary

The reassessment gave AAEF an overall strong evaluation after version semantics were clarified.

Key positive findings included:

- strong conceptual clarity around "Model output is not authority",
- high-quality control design in the current v0.4.1 baseline,
- strong evidence model and evidence quality concepts,
- strong internal framework governance through Normative Incorporation Rules and promotion criteria,
- appropriate separation between active baseline and non-normative planning material,
- and honest claim boundaries around certification, compliance, audit sufficiency, conformity, and equivalence.

The reassessment also identified continuing adoption gaps:

- implementation bridge examples remain insufficient,
- evidence bootstrap and self-reference limits remain structurally important,
- external framework mapping remains incomplete for enterprise interoperability,
- and v0.6.0 adoption-readiness material remains draft/planning material.

## Response position

AAEF accepts the reassessment's core conclusion:

> AAEF is conceptually strong and structurally disciplined, but adoption requires implementation bridges, clearer assurance limitations, and conservative interoperability materials.

This response treats those points as follow-up drivers, not as contradictions of the v0.6.0 release posture.

AAEF should continue to avoid overstating maturity while making the framework easier to evaluate, pilot, implement, assess, and explain.

## Version-structure clarification

The reassessment depended on the following version semantics.

| Layer | Role | Status |
| --- | --- | --- |
| v0.6.0 | Latest public review planning release | Practical Adoption Readiness planning material |
| v0.5.0 | Prior public review planning release | Historical non-normative planning material |
| v0.4.1 | Current control and assessment baseline | Current active AAEF control / assessment reference point |

Interpretation:

- v0.6.0 does not automatically change active controls.
- v0.5.0 planning material remains useful as design input, but is not automatically active.
- v0.4.1 remains the current control and assessment baseline until explicitly updated.
- Future promotion must be handled by explicit PRs that modify active artifacts.

This separation remains a core AAEF governance strength.

## Accepted strengths

AAEF should preserve and build on the following strengths identified by the reassessment.

### Conceptual clarity

The phrase:

> Model output is not authority.

should remain the central thesis.

It is effective because it separates model-generated text, recommendations, or tool-call suggestions from executable authority.

### Control design quality

The current control and assessment baseline contains strong control patterns for:

- authorization at the action boundary,
- meaningful approval,
- trusted policy inputs,
- avoidance of natural-language-only authority,
- non-reliance on model self-assessment,
- authority lineage,
- evidence quality,
- and reconstruction support.

### Evidence model

The evidence model remains one of AAEF's strongest differentiators.

AAEF should continue to emphasize that logs are not automatically evidence. Evidence must be structured, attributable, bounded, and suitable for assessment or reconstruction.

### Framework governance

AAEF should preserve its layered maturity model:

- active baseline,
- planning material,
- candidate promotion,
- and explicit incorporation.

This prevents planning material from becoming active requirements by accident.

### Conservative claim boundaries

AAEF should continue to avoid claims that it is:

- a formal standard,
- a certification scheme,
- a legal compliance claim,
- an audit opinion,
- a conformity assessment,
- or an equivalence claim with external frameworks.

This restraint improves trust.

## Accepted adoption gaps

The reassessment identifies several gaps that AAEF should accept as real adoption barriers.

### Gap 1: Implementation bridge

Current issue:

Implementers need clearer examples of how AAEF-style authorization, dispatch enforcement, backend verification, and evidence generation can be implemented in real agentic AI stacks.

Affected audiences:

- implementers,
- security architects,
- consultants,
- operators,
- engineering managers.

Adoption risk:

Without implementation bridges, AAEF may remain conceptually strong but difficult to pilot.

### Gap 2: Evidence bootstrap and self-reference

Current issue:

If evidence generation occurs inside the same environment being assessed, the evidence writer may become part of the trust problem.

Affected audiences:

- auditors,
- security architects,
- incident responders,
- risk owners,
- consultants.

Adoption risk:

Organizations may over-trust evidence generated by untrusted or insufficiently isolated components.

### Gap 3: External framework mapping

Current issue:

Organizations need conservative mapping material to understand how AAEF relates to existing AI governance, security, audit, and risk frameworks.

Affected audiences:

- compliance teams,
- auditors,
- risk owners,
- consultants,
- security governance teams.

Adoption risk:

Without mapping, AAEF may be hard to integrate into existing enterprise risk, audit, or compliance programs.

### Gap 4: Persona-specific adoption artifacts

Current issue:

Different audiences need different entry points.

A field implementer does not need the same artifact as an auditor, risk owner, or consultant.

Affected audiences:

- all adoption audiences.

Adoption risk:

A single documentation path creates adoption friction.

## Adoption personas and required artifacts

AAEF should support the following adoption personas.

| Persona | Primary question | Needed artifact |
| --- | --- | --- |
| Field implementer | How do I build this into an agent stack? | Implementation reference pattern and minimal prototype |
| Security architect | Where do I place controls and trust boundaries? | Architecture placement guide |
| Operator / administrator | How do I run this day to day? | Operational responsibility matrix and runbook |
| Auditor / assessor | What evidence do I request and how do I judge it? | Evidence review guide and assessment checklist |
| Risk owner / manager | What decision can I make from this? | Risk decision memo and acceptance criteria |
| Consultant | How do I explain and scope this for a client? | Advisory scoping guide and discovery questions |
| Legal / compliance reviewer | What claims can and cannot be made? | Applicability and claim-boundary guide |
| Research reviewer | What is the contribution and how is it evaluated? | Research abstract and related-work map |

## Recommended v0.6.x follow-up priorities

The reassessment suggests the following follow-up priorities.

### P0: Implementation Reference Pattern

Create a non-normative implementation reference pattern showing a minimal AAEF-style flow:

1. action request,
2. authorization decision artifact,
3. dispatch enforcement,
4. backend relying-party verification,
5. evidence event generation,
6. non-execution behavior,
7. reconstruction query.

This should remain illustrative and should not imply certification or implementation conformance.

Candidate artifact:

`docs/en/status/v060-implementation-reference-pattern-planning.md`

### P1: Evidence Bootstrap and TCB Limitation Note

Create a planning note that explains assurance limitations when the evidence writer, policy enforcement, or runtime environment are inside the same trust boundary as the model-controlled path.

Candidate artifact:

`docs/en/status/v060-evidence-bootstrap-and-tcb-limitation-note.md`

The note should clarify:

- evidence self-reference risk,
- evidence writer placement,
- evidence trust assumptions,
- when assurance becomes weak,
- and what compensating controls may be needed.

### P1: External Framework Mapping Enrichment Plan

Create a conservative plan for external mapping enrichment, starting with NIST AI RMF or another carefully selected framework.

Candidate artifact:

`docs/en/status/v060-external-framework-mapping-enrichment-plan.md`

The plan should avoid equivalence and compliance claims.

### P1: Persona-Specific Adoption Package Plan

Create a plan for adoption packages by audience.

Candidate artifact:

`docs/en/status/v060-persona-adoption-package-plan.md`

Suggested packages:

- implementer quick start package,
- auditor assessment package,
- operator runbook package,
- risk owner decision package,
- consultant scoping package.

### P2: Related-Work Mapping Plan

Create a research-facing plan that maps AAEF's concepts to related work in:

- AI governance,
- Zero Trust,
- IAM,
- audit logging,
- software supply chain evidence,
- assurance cases,
- agent security,
- and AI safety evaluation.

Candidate artifact:

`docs/en/status/v060-related-work-mapping-plan.md`

## Recommended first follow-up

The first follow-up should be:

> Implementation Reference Pattern

Rationale:

Implementation feasibility remains the lowest-scored adoption dimension. A minimal implementation pattern would help every adoption persona:

- implementers can build,
- auditors can see expected evidence,
- operators can understand runtime responsibilities,
- managers can estimate adoption effort,
- consultants can scope pilots,
- and researchers can evaluate feasibility.

This should be planning or illustrative material first, not active requirements.

## Consultant-facing implications

For consultants, AAEF should become easier to use in discovery and advisory work.

A consultant needs:

- scoping questions,
- system boundary questions,
- high-impact action classification questions,
- evidence availability questions,
- approval and delegation questions,
- runtime enforcement questions,
- and residual risk questions.

AAEF should support a consulting workflow such as:

1. identify agentic actions,
2. classify impact,
3. identify principals and delegated authority,
4. identify execution boundaries,
5. identify available evidence,
6. identify evidence trust limitations,
7. map gaps to AAEF controls,
8. define pilot remediation steps,
9. record claim boundaries.

## Auditor-facing implications

For auditors and assessors, AAEF should become easier to evaluate without implying certification.

An auditor needs:

- evidence request lists,
- assessment criteria,
- reconstruction questions,
- evidence source trust assumptions,
- exceptions and non-execution records,
- approval-to-execution linkage,
- and residual risk notes.

AAEF should support audit-style review without claiming to be an audit standard.

## Manager and risk-owner implications

For managers and risk owners, AAEF should support decision-making.

A manager or risk owner needs to know:

- which agentic actions are high-impact,
- which actions are allowed,
- which actions require approval,
- which actions must fail closed,
- what evidence exists,
- what residual risk remains,
- and who accepts that risk.

AAEF should help produce risk decisions, not just technical controls.

## Field implementation implications

For field implementers, AAEF should become executable as a pattern.

A field implementation guide should answer:

- what code component creates the authorization decision,
- where the policy engine runs,
- what the dispatcher verifies,
- what the backend independently checks,
- what evidence is written,
- what happens when evidence is missing,
- and how incidents are reconstructed.

## Claim-boundary implications

AAEF should remain careful.

Adoption material should not claim:

- certification,
- legal compliance,
- regulatory compliance,
- audit sufficiency,
- conformity,
- equivalence,
- or complete mitigation.

Adoption material may claim:

- planning support,
- implementation guidance,
- assessment support,
- evidence structuring,
- reconstruction support,
- risk decision support,
- and public review control-profile guidance.

## Response summary

AAEF accepts the reassessment as broadly accurate after version semantics were clarified.

The key response is:

- Preserve v0.4.1 as the current control and assessment baseline.
- Preserve v0.5.0 and v0.6.0 as non-normative planning material unless explicitly promoted.
- Treat implementation feasibility as the highest-priority adoption gap.
- Treat evidence bootstrap and TCB limitations as an important assurance boundary issue.
- Treat external framework mapping as important but conservative.
- Continue avoiding certification, compliance, audit, conformity, and equivalence claims.
- Move toward persona-specific adoption packages.

## Recommended next step

Create a planning artifact for the P0 follow-up:

> AAEF v0.6.0 Implementation Reference Pattern Planning

This should define the shape of a minimal illustrative implementation without changing active controls or implying implementation conformance.

## Non-goals

This response does not:

- change active controls,
- change the current control and assessment baseline,
- update schemas, examples, mappings, CSVs, or testing procedures,
- promote v0.5.0 or v0.6.0 planning material into active requirements,
- claim certification,
- claim compliance,
- provide an audit opinion,
- claim conformity,
- claim equivalence with external frameworks,
- or assert production readiness.

## Acceptance criteria

This response is sufficient when:

- the reassessment is acknowledged,
- accepted strengths are recorded,
- accepted adoption gaps are recorded,
- adoption personas are identified,
- follow-up priorities are listed,
- implementation feasibility is identified as the first adoption priority,
- claim boundaries are preserved,
- and no active baseline change is implied.
