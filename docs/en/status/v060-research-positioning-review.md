# AAEF v0.6.0 Research Positioning Review

Status: Research positioning review  
Related roadmap: #241  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document reviews AAEF v0.6.0 as a research and development artifact.

The purpose is to clarify how AAEF can be positioned for research review, academic presentation, security research discussion, and future paper development without overstating its maturity or making certification, compliance, audit, conformity, or equivalence claims.

This document is research-positioning material. It does not change active controls, schemas, assessment procedures, testing procedures, mappings, examples, or the current control and assessment baseline.

## Research positioning summary

AAEF can be positioned as:

> An action assurance framework for agentic AI systems that treats model output as insufficient authority and instead evaluates whether agentic actions are authorized, bounded, attributable, and evidenced.

The core research proposition is:

> Model output is not authority.

This proposition reframes agentic AI safety from a model-centric trust question into an action-governance and assurance question.

## Research problem

Agentic AI systems can invoke tools, access data, delegate tasks, interact with other agents, and execute actions on behalf of users or organizations.

For these systems, model-level properties such as helpfulness, alignment, accuracy, safety, or explainability are necessary but insufficient.

A production system must also answer:

1. Who or what acted?
2. On whose behalf did it act?
3. What authority did it have?
4. Was the action allowed at the point of execution?
5. What evidence proves what happened?

AAEF treats these questions as the core of agentic action assurance.

## Research contribution candidates

AAEF may support the following research contribution claims.

| Candidate contribution | Description | Claim boundary |
| --- | --- | --- |
| Action assurance framing | Reframes agentic AI governance around authorized, bounded, attributable, and evidenced actions. | Does not claim to solve all AI safety or AI governance problems. |
| Authority separation principle | Separates model output from execution authority. | Does not claim model behavior is irrelevant. |
| Enforcement boundary model | Distinguishes authorization decision, tool dispatch enforcement, backend relying-party verification, and evidence generation. | Does not mandate a specific product, SDK, cloud, policy engine, or architecture. |
| Evidence-centered assurance model | Defines structured evidence expectations for agentic actions. | Does not claim evidence alone proves safety or compliance. |
| Cross-role adoption planning | Organizes planning material for implementers, operators, legal/compliance reviewers, security architects, and risk owners. | Does not promote all planning material into active requirements. |
| Claim-boundary discipline | Explicitly avoids certification, compliance, equivalence, and audit-sufficiency claims. | Does not replace legal, compliance, audit, or risk judgment. |

## Research questions

Candidate research questions include:

| ID | Research question |
| --- | --- |
| RQ-01 | How should delegated authority be represented, constrained, and verified in agentic AI systems? |
| RQ-02 | What evidence is necessary to reconstruct and assess high-impact AI agent actions? |
| RQ-03 | How should systems separate model-generated recommendations from executable authority? |
| RQ-04 | What runtime boundaries are necessary to prevent prompt-derived or context-derived content from becoming authority? |
| RQ-05 | How can authorization decision artifacts support auditability and incident reconstruction? |
| RQ-06 | How should cross-agent delegation, revocation, budget propagation, and accountability chains be represented? |
| RQ-07 | What minimal implementation profile is sufficient for practical adoption without overburdening implementers? |
| RQ-08 | How can agentic action assurance be evaluated without claiming certification or legal compliance? |
| RQ-09 | How should risk owners decide whether a high-impact agentic action is acceptable? |
| RQ-10 | How can AAEF-style controls be compared with existing AI governance, security, and audit frameworks without implying equivalence? |

## Hypotheses and design assumptions

Candidate hypotheses:

| ID | Hypothesis |
| --- | --- |
| H-01 | Treating model output as non-authoritative reduces ambiguity around who or what authorized an agentic action. |
| H-02 | Separating authorization, dispatch enforcement, backend verification, and evidence generation improves auditability. |
| H-03 | Structured evidence records improve incident reconstruction for high-impact agentic actions. |
| H-04 | Role-specific adoption artifacts make an action assurance framework easier to evaluate by implementers, operators, legal/compliance reviewers, security architects, and risk owners. |
| H-05 | Explicit claim boundaries reduce the risk that an early framework is mistaken for certification, legal compliance, or audit sufficiency. |

Design assumptions:

- Agentic AI systems can produce outputs that influence actions but should not directly confer authority.
- Authority should be represented outside the model output itself.
- High-impact actions require stronger evidence than low-impact actions.
- Backend relying parties should not rely solely on agent runtime assertions.
- Evidence should support reconstruction, review, and dispute resolution.
- Planning artifacts should not become active requirements without explicit incorporation.

## Evaluation directions

AAEF may be evaluated through several complementary methods.

| Evaluation direction | Possible method | Output |
| --- | --- | --- |
| Conceptual evaluation | Compare AAEF concepts with AI governance, Zero Trust, IAM, audit logging, and agent security literature. | Related-work analysis and conceptual gap map. |
| Architecture evaluation | Apply AAEF to reference architectures for tool-using agents. | Architecture mapping and control placement analysis. |
| Scenario evaluation | Test AAEF against agentic misuse scenarios such as prompt injection, excessive agency, unauthorized tool use, delegation abuse, and evidence tampering. | Scenario-to-control analysis and residual risk discussion. |
| Evidence evaluation | Assess whether evidence event structures support reconstruction of high-impact actions. | Evidence sufficiency and reconstruction analysis. |
| Implementation evaluation | Build a minimal prototype using authorization decision artifacts, dispatch checks, backend verification, and evidence logging. | Feasibility prototype and implementation lessons. |
| Practitioner review | Ask implementers, auditors, operators, security architects, legal/compliance reviewers, and risk owners to review the framework. | Role-specific feedback and adoption friction analysis. |
| Negative testing | Analyze how AAEF could be bypassed, gamed, or misrepresented. | Abuse-case catalog and framework-hardening recommendations. |

## Candidate paper framing

Candidate paper titles:

1. **Model Output Is Not Authority: Action Assurance for Agentic AI Systems**
2. **Toward Action Assurance for AI Agents: Authorization, Execution Boundaries, and Evidence**
3. **Governing Agentic AI Actions Through Authority Separation and Verifiable Evidence**
4. **From Model Trust to Action Assurance: A Framework for High-Impact Agentic AI Systems**
5. **AAEF: A Public Review Framework for Agentic Authority and Evidence**

Recommended initial title:

> Model Output Is Not Authority: Action Assurance for Agentic AI Systems

## Candidate abstract

Agentic AI systems increasingly perform actions by invoking tools, accessing data, delegating tasks, and interacting with external systems. Existing AI safety and governance discussions often focus on model behavior, model alignment, or output trustworthiness, but these properties are insufficient when model outputs can lead to real-world actions. This paper introduces the Agentic Authority & Evidence Framework (AAEF), a public review action assurance framework for agentic AI systems. AAEF is based on the principle that model output is not authority. It separates model-generated intent or recommendations from executable authority, and organizes assurance around authorization decisions, execution boundaries, backend relying-party verification, and verifiable evidence. The framework defines research questions and evaluation directions for assessing whether agentic actions are authorized, bounded, attributable, and evidenced. AAEF is not a certification scheme, legal compliance claim, audit opinion, or equivalence claim with external frameworks. Instead, it provides a research and planning foundation for evaluating high-impact agentic AI actions and for developing future implementation, operational, legal/compliance, security architecture, and risk owner adoption artifacts.

## Candidate paper structure

A short paper or workshop paper could use the following structure:

1. Introduction
2. Problem: model output is not authority
3. Background and related work
4. Agentic action assurance model
5. AAEF framework overview
6. Authority separation and execution boundary model
7. Evidence and reconstruction model
8. Evaluation directions
9. Limitations and claim boundaries
10. Future work
11. Conclusion

## Candidate presentation structure

A 15-minute presentation could use the following structure:

| Section | Time | Content |
| --- | ---: | --- |
| Problem framing | 2 min | AI agents can act; model trust is insufficient. |
| Core thesis | 2 min | Model output is not authority. |
| AAEF overview | 3 min | Authority, execution boundary, evidence. |
| v0.6.0 contribution | 3 min | Practical Adoption Readiness and five workstreams. |
| Research questions | 2 min | RQ-01 through RQ-10. |
| Evaluation plan | 2 min | scenario, architecture, evidence, prototype, practitioner review. |
| Closing | 1 min | research milestone, not certification or compliance claim. |

## Relevant AAEF artifacts for research review

| Research use | AAEF artifact |
| --- | --- |
| Framework overview | `README.md`, `docs/en/13-one-page-overview.md`, `docs/en/55-researcher-overview.md` |
| Core thesis | `docs/en/02-core-principles.md` |
| Threat model | `docs/en/04-threat-model.md` |
| Trust model | `docs/en/05-trust-model.md` |
| Control requirements | `docs/en/07-control-requirements.md` |
| Assessment | `docs/en/12-assessment-quick-start.md`, assessment worksheet |
| Evidence model | `docs/en/14-evidence-event-schema.md` |
| Architecture | `docs/en/17-reference-architecture.md` |
| Testing | `docs/en/25-testing-procedures-and-pass-criteria.md` |
| High-impact profile | `docs/en/26-high-impact-audit-grade-prequalification.md` |
| External mapping method | `docs/en/28-external-framework-mapping-methodology.md` |
| Research overview | `docs/en/55-researcher-overview.md` |
| v0.6.0 release positioning | `docs/en/status/v060-release-decision-record.md`, `docs/en/status/v060-release-readiness-review.md` |

## Suitable dissemination modes

Potential dissemination modes:

| Mode | Fit | Notes |
| --- | --- | --- |
| Security research workshop | High | Good fit for early conceptual and applied security framing. |
| AI governance workshop | High | Good fit for risk, assurance, and organizational adoption framing. |
| Software engineering / systems workshop | Medium | Good fit if implementation prototype is added. |
| Audit / GRC practitioner session | High | Good fit for evidence, accountability, and assurance claims. |
| Academic short paper | Medium to high | Needs related work, evaluation design, and limitations. |
| Conference poster | High | Good near-term format for problem framing and framework overview. |
| Technical article | Medium | Useful after research framing is stable. |

This document does not select a specific venue or submission deadline.

## Claim boundaries for research use

AAEF research positioning should avoid claiming that AAEF:

- is a formal standard
- is a certification scheme
- proves an AI agent is safe
- guarantees compliance
- provides an audit opinion
- establishes conformity with external frameworks
- is equivalent to NIST, ISO, OWASP, CSA, or any other external framework
- eliminates the need for human governance, legal review, audit review, or risk acceptance

AAEF may claim that it provides:

- a public review framework
- an action assurance control profile
- a structured research artifact
- a planning foundation
- a terminology and evidence model
- a basis for future implementation and evaluation

## Recommended next research steps

Recommended next steps:

1. Create a concise research problem statement.
2. Prepare a 1-page research abstract.
3. Prepare a related-work map.
4. Define an evaluation plan using scenarios and evidence reconstruction.
5. Identify a minimal prototype scope.
6. Prepare a 10-15 slide research presentation.
7. Decide whether to target a workshop, poster, practitioner session, or short paper first.

## Non-goals

This document does not:

- change active controls
- change the current control and assessment baseline
- modify schemas, CSVs, examples, mappings, or testing procedures
- create a certification claim
- create a compliance claim
- create an audit opinion
- claim equivalence with external frameworks
- select a specific academic venue
- assert peer-reviewed acceptance

## Acceptance criteria

This review is sufficient when:

- AAEF is positioned as a research and development artifact
- candidate research contributions are listed
- research questions are identified
- evaluation directions are documented
- candidate paper and presentation framing are proposed
- claim boundaries are preserved
- no active baseline change is implied
