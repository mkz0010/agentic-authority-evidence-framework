# v0.6.x Research Related-Work Candidate Map

## Status

This is a v0.6.x candidate status artifact for research related-work mapping.

This document is:

- a candidate map for adjacent research and practice areas;
- a planning aid for future citation inventory, research positioning, and review work;
- non-normative unless a later release explicitly promotes content into active guidance.

This document is not:

- a completed literature review;
- a citation inventory;
- an external framework equivalence mapping;
- a compliance crosswalk;
- a certification, conformity, audit, or legal sufficiency mapping;
- an empirical validation result;
- a change to the current AAEF control and assessment baseline.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This candidate map prepares AAEF for future research review, workshop submission, academic presentation, and related-work analysis.

It is intended to help reviewers distinguish:

- where AAEF overlaps with existing research, standards, frameworks, and operational practices;
- where AAEF may complement existing work;
- where AAEF should avoid overstating novelty or coverage;
- where further citation review is required before making stronger positioning claims.

The central conservative positioning remains:

> Model output is not authority.

AAEF is positioned as an action assurance control profile for agentic AI systems. It focuses on action authority, execution boundaries, evidence, and reconstruction rather than treating model output as an authorization source.

## Mapping method

Each category below is treated as a candidate related-work area, not as a completed survey.

For each area, future work should distinguish:

| Dimension | Meaning |
| --- | --- |
| Category | Research, standards, governance, or practice area adjacent to AAEF. |
| Representative source types | Types of sources likely to be reviewed in a future citation inventory. |
| Relationship to AAEF | Why the area is relevant to AAEF. |
| Overlap | Concepts that may overlap with AAEF. |
| Complement | How the area may strengthen or contextualize AAEF. |
| Distinction | Where AAEF should not claim to replace the area. |
| Claim boundary | Conservative language required to avoid unsupported equivalence, compliance, or novelty claims. |
| Candidate follow-up | Possible next artifact or review activity. |

## Candidate related-work categories

### 1. Agentic AI security and control boundaries

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | Agentic AI security guidance, agent security taxonomies, autonomous workflow security analyses, AI agent risk reports. |
| Relationship to AAEF | AAEF directly addresses agentic systems that can request or trigger actions through tools, APIs, workflows, or delegated execution paths. |
| Overlap | Goal hijacking, excessive agency, unsafe delegation, tool misuse, memory misuse, unauthorized workflow execution. |
| Complement | Existing agentic AI security work can provide threat categories and attack examples for AAEF evaluation. |
| Distinction | AAEF should not claim to be a complete taxonomy of all agentic AI risks. |
| Claim boundary | AAEF may complement agentic AI security guidance by focusing on authority, enforcement, and evidence boundaries. |
| Candidate follow-up | Add a citation inventory for agentic AI security guidance and identify which categories are relevant to AAEF controls. |

### 2. Tool-use and function-calling authorization

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | Tool-use security papers, function-calling platform documentation, API authorization patterns, agent tool governance guidance. |
| Relationship to AAEF | AAEF separates model output from authorization and requires action requests to pass through enforceable control boundaries. |
| Overlap | Tool invocation control, argument validation, allowlists, scoped credentials, policy checks, dispatch enforcement. |
| Complement | Tool-use research can inform concrete examples of dispatch-time and backend enforcement failures. |
| Distinction | AAEF should not claim to mandate one SDK, orchestration framework, or tool-calling implementation model. |
| Claim boundary | AAEF describes control expectations and evidence boundaries rather than a universal function-calling architecture. |
| Candidate follow-up | Map representative tool-use failure modes to AAEF action request, authorization decision, dispatch decision, and backend verification artifacts. |

### 3. Prompt injection and indirect prompt injection defenses

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | Prompt injection research, indirect prompt injection papers, LLM application security guidance, red-team reports. |
| Relationship to AAEF | AAEF treats model output and untrusted content as insufficient authority for high-impact action. |
| Overlap | Untrusted input influence, tool-call manipulation, instruction hierarchy bypass, retrieval or web-content injection. |
| Complement | Prompt injection research can provide negative tests and realistic attack scenarios for AAEF adoption packages. |
| Distinction | AAEF should not claim to solve prompt injection in general or remove the need for model-side, retrieval-side, or application-side defenses. |
| Claim boundary | AAEF reduces reliance on model obedience by requiring separate authority and evidence controls for actions. |
| Candidate follow-up | Prepare a candidate prompt-injection-to-AAEF-control mapping with explicit residual-risk language. |

### 4. Human approval and human-in-the-loop control

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | Human-in-the-loop governance research, approval workflow design, human factors studies, security operations approval procedures. |
| Relationship to AAEF | AAEF includes human approval as possible evidence or authority input, but does not treat a UI click as automatically sufficient. |
| Overlap | Approval capture, reviewer identity, approval scope, approval freshness, escalation, emergency override. |
| Complement | Human factors and operational research can strengthen AAEF guidance on reviewer burden and approval quality. |
| Distinction | AAEF should not claim that human approval alone guarantees safe or authorized action. |
| Claim boundary | Human approval is one possible authority input, and its sufficiency depends on scope, identity, timing, and evidence quality. |
| Candidate follow-up | Add reviewer-burden and approval-spoofing scenarios to future operator or risk-owner guidance. |

### 5. Authorization architecture and PDP/PEP patterns

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | Access control architecture, policy decision point and policy enforcement point patterns, zero trust authorization guidance, IAM design references. |
| Relationship to AAEF | AAEF depends on the separation of authorization decision, tool dispatch enforcement, and backend verification. |
| Overlap | Policy evaluation, enforcement points, principal binding, action scoping, revocation, delegation, decision logging. |
| Complement | Existing authorization architecture provides mature vocabulary for implementer guidance. |
| Distinction | AAEF should not claim to replace IAM, zero trust architecture, or formal access-control models. |
| Claim boundary | AAEF adapts authorization separation concepts to agentic action assurance and action-bound evidence. |
| Candidate follow-up | Prepare an implementation-neutral note comparing AAEF authorization components with generic PDP/PEP vocabulary. |

### 6. Evidence, audit logging, and action reconstruction

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | Audit logging guidance, incident reconstruction research, forensic logging practices, evidence quality criteria, SIEM and detection engineering references. |
| Relationship to AAEF | AAEF emphasizes action-bound evidence that supports reconstruction of who or what requested, authorized, dispatched, and verified an action. |
| Overlap | Structured logging, correlation IDs, event integrity, retention, evidence sufficiency, traceability. |
| Complement | Logging and forensic practices can improve evidence quality and operational usefulness. |
| Distinction | AAEF should not claim that the presence of logs alone proves authorization, safety, compliance, or correctness. |
| Claim boundary | AAEF treats evidence as support for assessment and reconstruction, not as automatic proof of compliance or safety. |
| Candidate follow-up | Define a future citation inventory for logging, reconstruction, and evidence quality references. |

### 7. Provenance, tamper-evident records, and attestable logs

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | Provenance research, tamper-evident logging, signed records, transparency logs, attestation, secure boot, TEE, TPM, and root-of-trust references. |
| Relationship to AAEF | AAEF evidence may be strengthened when records can be protected against tampering and tied to trustworthy execution environments. |
| Overlap | Record integrity, signing, append-only records, attestation, runtime identity, policy version binding. |
| Complement | Provenance and attestation work can support stronger future evidence profiles. |
| Distinction | AAEF should not require hardware root of trust or remote attestation for all deployments unless a later profile explicitly defines such a requirement. |
| Claim boundary | Tamper-evident and attestable mechanisms may strengthen evidence, but AAEF does not currently make hardware-backed assurance mandatory. |
| Candidate follow-up | Add a future optional profile concept for stronger evidence integrity and attestable execution boundaries. |

### 8. AI governance and AI risk management frameworks

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | AI risk management frameworks, AI governance standards, responsible AI management systems, organizational AI policy guidance. |
| Relationship to AAEF | AAEF can support operationalization of action authority and evidence expectations within broader AI governance programs. |
| Overlap | Risk management, accountability, documentation, oversight, monitoring, impact management. |
| Complement | Governance frameworks can provide organizational context for deciding which actions require AAEF-style controls. |
| Distinction | AAEF should not claim equivalence to AI governance standards or claim compliance with them. |
| Claim boundary | AAEF may be used as a supporting control profile or adoption aid, not as a substitute for governance, legal, or management-system obligations. |
| Candidate follow-up | Prepare a conservative source inventory and relationship note for AI governance frameworks without turning it into a compliance crosswalk. |

### 9. AI assurance, safety cases, and assurance cases

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | AI assurance literature, safety cases, assurance cases, structured argumentation, evidence-based assurance methods. |
| Relationship to AAEF | AAEF evidence and control expectations may support assurance arguments about action governance. |
| Overlap | Claims, evidence, assumptions, argument structure, residual risk, review boundaries. |
| Complement | Assurance-case methods can help organize AAEF evidence into reviewable claims and limitations. |
| Distinction | AAEF should not claim that its artifacts automatically constitute a complete assurance case. |
| Claim boundary | AAEF can provide action-bound evidence inputs for assurance work, but assurance conclusions require separate argumentation and review. |
| Candidate follow-up | Draft a research contribution matrix distinguishing AAEF controls, evidence, and possible assurance-case inputs. |

### 10. Operational monitoring and incident response

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | Security monitoring guidance, incident response playbooks, detection engineering, AI incident reporting, SOC operations references. |
| Relationship to AAEF | AAEF can help define what should be observable when agentic systems request or execute high-impact actions. |
| Overlap | Detection triggers, escalation, rollback, freeze, evidence capture, incident reconstruction. |
| Complement | Operational practices can make AAEF evidence usable during incidents rather than only during design reviews. |
| Distinction | AAEF should not claim to be a complete incident response framework. |
| Claim boundary | AAEF supports action-focused observability and reconstruction; incident response still requires separate operational procedures. |
| Candidate follow-up | Add future operator guidance for AAEF-specific incident triage and evidence review. |

### 11. Software supply chain and runtime enforcement

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | Software supply chain security, runtime policy enforcement, dependency and model supply chain guidance, secure deployment references. |
| Relationship to AAEF | Agentic action assurance depends on trustworthy enforcement components, policy versions, tools, runtime configurations, and evidence pipelines. |
| Overlap | Component integrity, versioning, deployment controls, runtime policy, dependency trust, configuration drift. |
| Complement | Supply chain and runtime enforcement work can help protect the components AAEF relies on. |
| Distinction | AAEF should not claim to solve software supply chain security. |
| Claim boundary | AAEF assumes enforceable and reviewable components; protecting those components requires separate secure engineering and supply chain controls. |
| Candidate follow-up | Identify assumptions AAEF makes about enforcement component integrity and list them as future review candidates. |

### 12. Compliance-adjacent control mapping

| Dimension | Candidate mapping |
| --- | --- |
| Representative source types | Security control catalogs, audit frameworks, risk management standards, sector-specific compliance obligations, internal policy mappings. |
| Relationship to AAEF | Organizations may want to relate AAEF concepts to existing control environments. |
| Overlap | Control ownership, evidence, assessment procedures, risk acceptance, management review. |
| Complement | Compliance-adjacent mapping can help adoption discussions and internal governance alignment. |
| Distinction | AAEF should not claim compliance, certification, audit sufficiency, or external framework equivalence. |
| Claim boundary | Any mapping should be clearly labeled as informative and non-equivalent unless independently reviewed under the target framework. |
| Candidate follow-up | Prepare a non-equivalence mapping template with explicit disclaimers and reviewer notes. |

## Conservative contribution positioning

AAEF may be positioned conservatively as follows:

- AAEF emphasizes action authority rather than model output trust.
- AAEF focuses on action-bound evidence and reconstruction for agentic systems.
- AAEF separates action request, authorization decision, dispatch decision, backend verification, and evidence capture.
- AAEF can support adoption discussions for organizations evaluating agentic AI risks.
- AAEF may complement existing AI risk, AI security, authorization, logging, and governance frameworks.
- AAEF is a control profile and adoption aid, not a standard, certification scheme, legal compliance claim, audit opinion, or external framework equivalence claim.

## Explicitly avoided claims

Future research, adoption, and mapping work should avoid unsupported claims such as:

- AAEF is the first framework to solve agentic AI security.
- AAEF fully covers agentic AI security.
- AAEF proves legal or regulatory compliance.
- AAEF is equivalent to an established standard.
- AAEF makes agentic systems safe.
- AAEF is production-ready.
- AAEF is empirically validated.
- AAEF is peer-reviewed.
- AAEF replaces IAM, zero trust, AI governance, incident response, secure SDLC, or software supply chain controls.

## Candidate external reference examples

This section lists candidate reference areas for future review. It is not a completed citation inventory.

| Candidate source area | Candidate reason for review | Current use in this document |
| --- | --- | --- |
| NIST AI Risk Management Framework | General AI risk management context. | Candidate governance and risk-management context only. |
| NIST AI 600-1 Generative AI Profile | Generative AI risk profile context. | Candidate risk context only. |
| OWASP Top 10 for Large Language Model Applications | LLM application security risks such as prompt injection and insecure output handling. | Candidate attack and control context only. |
| OWASP Top 10 for Agentic Applications | Agentic AI risk categories and security guidance. | Candidate agentic security context only. |
| MITRE ATLAS | AI adversary tactics and techniques knowledge base. | Candidate threat-model context only. |
| ISO/IEC 42001:2023 | AI management system requirements context. | Candidate governance context only, not compliance mapping. |
| CSA AI Controls Matrix | Cloud-based AI control framework context. | Candidate control-context reference only, not equivalence mapping. |

Before any future artifact cites or maps these sources, the source name, version, publication state, and intended use should be rechecked against official or primary sources.

## Review checklist

Before this candidate map is promoted, extended, or used in a research-facing artifact, review whether:

- unsupported novelty claims have been introduced;
- equivalence language has appeared accidentally;
- compliance, certification, conformity, audit sufficiency, legal sufficiency, production readiness, or empirical validation claims have appeared accidentally;
- internal AAEF artifacts and external sources have been clearly separated;
- non-normative status is explicit;
- active baseline impact is explicitly excluded;
- citation inventory work is clearly separated from candidate mapping work;
- future follow-ups are narrow and reviewable.

## Recommended next step

Recommended follow-up options:

1. Add a candidate citation inventory planning artifact.
2. Add a research contribution matrix.
3. Add evaluation design options for future empirical or case-study work.
4. Add a conservative non-equivalence mapping template for adoption discussions.

For #286, the most direct next step after this candidate map is likely a citation inventory planning artifact or a research contribution matrix.
