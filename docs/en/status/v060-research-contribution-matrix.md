# v0.6.x Research Contribution Matrix

## Status

This is a v0.6.x candidate status artifact for research contribution analysis.

This document is:

- a candidate contribution matrix for research positioning;
- a bridge between the related-work candidate map and future citation inventory work;
- a planning aid for research abstracts, paper outlines, review discussions, and evaluation design.

This document is not:

- a completed research paper;
- a peer-reviewed contribution claim;
- an empirical validation result;
- a literature review;
- a citation inventory;
- an external framework equivalence mapping;
- a compliance crosswalk;
- a certification, conformity, legal, audit, or production-readiness claim;
- a change to the current AAEF control and assessment baseline.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

The purpose of this matrix is to clarify which AAEF ideas may be framed as candidate research contributions and which boundaries must be preserved before research, publication, or external review.

The matrix is intentionally conservative. It does not attempt to prove novelty. Instead, it separates:

- the problem area AAEF addresses;
- the candidate contribution AAEF may offer;
- adjacent research or practice areas that must be reviewed;
- what AAEF should not claim;
- what evidence or evaluation would be needed before stronger claims are made.

This supports later work such as:

- citation inventory planning;
- a research abstract;
- a workshop or conference paper outline;
- an evaluation design note;
- a research claim-boundary note.

## Contribution analysis method

Each candidate contribution is evaluated using the following dimensions.

| Dimension | Meaning |
| --- | --- |
| Candidate contribution | The AAEF idea that may be research-relevant. |
| Problem addressed | The practical or conceptual problem the idea responds to. |
| Adjacent work to review | Research, standards, frameworks, or operational practice areas that may overlap. |
| AAEF framing | How AAEF can describe the contribution conservatively. |
| Distinction boundary | What AAEF should not claim to replace or prove. |
| Possible evaluation path | How future work might evaluate the candidate contribution. |
| Claim boundary | Language required to avoid unsupported novelty, safety, compliance, or equivalence claims. |
| Candidate follow-up | A narrow future artifact that can make the contribution easier to review. |

## Candidate contribution matrix

| Candidate contribution | Problem addressed | Adjacent work to review | AAEF framing | Distinction boundary | Possible evaluation path | Claim boundary | Candidate follow-up |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model output is not authority | Agentic systems may transform generated text into actions without a separate authority boundary. | Agentic AI security, prompt injection, tool-use security, authorization architecture, human approval design. | AAEF frames model output as an action request or input, not an authorization decision. | Does not claim to solve all prompt injection, model deception, or unsafe generation risks. | Review action flows and test whether tool execution requires an authority artifact independent of model text. | AAEF may reduce reliance on model obedience for action authorization; it does not make model output trustworthy. | Prepare a concise research problem statement around action authority separation. |
| Action-bound evidence and reconstruction | Reviewers may be unable to reconstruct why an agentic action occurred or why it was blocked. | Audit logging, incident reconstruction, provenance, SIEM evidence, assurance cases. | AAEF emphasizes evidence tied to a specific action request, authorization decision, dispatch decision, backend verification, and outcome. | Does not claim that logs alone prove compliance, safety, or correctness. | Run reconstruction exercises for permitted and non-executed action examples. | Evidence supports review and reconstruction; it is not automatic proof of sufficiency. | Add evaluation design options for action reconstruction tasks. |
| Authorization / dispatch / backend separation | Systems may rely on one enforcement point or conflate authorization with tool dispatch. | PDP/PEP patterns, IAM, zero trust, API security, runtime policy enforcement. | AAEF decomposes agentic execution into decision, dispatch, and backend relying-party checks. | Does not replace IAM, zero trust architecture, or backend access-control requirements. | Compare reference flows with and without backend relying-party verification. | AAEF adapts authorization separation to agentic action assurance; it is not a universal access-control architecture. | Draft a focused matrix comparing AAEF components with generic PDP/PEP vocabulary. |
| Non-execution as a reviewable outcome | Failed or denied actions may be invisible, unreviewed, or treated as operational noise. | Incident response, denied transaction logging, security monitoring, safety interlocks. | AAEF treats non-execution and fail-closed behavior as evidence-relevant outcomes. | Does not claim every denial is correct, sufficient, or safe. | Review whether denied actions produce enough evidence to explain why execution did not occur. | AAEF can make non-execution reviewable; it does not prove all denials are correct. | Add a non-execution evaluation checklist or case-study design. |
| Principal and authority binding for agentic actions | Agent actions may blur human, service, agent, delegation, and approval authority. | Identity governance, delegation, approval workflows, access-control models, human-in-the-loop systems. | AAEF asks whether the authority behind an action can be traced and reviewed. | Does not define a complete identity governance model. | Evaluate whether sample evidence can identify requester, approving authority, policy, and action scope. | AAEF can support principal/authority review for actions; it does not replace organizational IAM governance. | Add a principal/authority evidence review matrix. |
| High-impact action orientation | Not all agentic actions require the same control strength, but high-impact actions need clearer boundaries. | Risk management, safety cases, impact assessments, security control baselines, operational risk review. | AAEF centers stronger review on high-impact actions and action consequences. | Does not prescribe universal impact categories for every organization. | Case-study classification of actions by potential impact and required evidence strength. | AAEF can help structure high-impact action review; organizations still define impact and risk appetite. | Add evaluation design options for high-impact action classification. |
| Conservative external-framework relationship model | Users may want to map AAEF to standards but overstate compliance or equivalence. | AI governance frameworks, security control catalogs, compliance mapping, audit frameworks. | AAEF uses informative relationship language and forbids equivalence and compliance claims without independent review. | Does not claim compliance, certification, conformity, or audit sufficiency. | Review mapping artifacts for forbidden relationship terms and unsupported claims. | AAEF mappings are informative unless independently assessed under the target framework. | Add citation inventory planning for external framework relationship references. |
| Adoption-facing persona bridge | Research artifacts can be difficult for implementers, operators, auditors, consultants, and risk owners to apply. | Implementation guidance, operational runbooks, audit evidence checklists, risk-owner decision support. | AAEF connects conceptual action assurance to role-specific adoption materials. | Does not claim that adoption materials are production-ready or sufficient for audit. | Persona walkthroughs where each role identifies decisions and evidence needed for an agentic action. | AAEF adoption materials support review and planning; they are not a managed service, certification path, or complete methodology. | Draft a research contribution subsection on persona-specific adoption readiness. |
| Static fixture and validator boundary | Prototype examples can accidentally imply implementation conformance or production readiness. | Reference implementations, conformance tests, examples, developer documentation, secure prototyping. | AAEF distinguishes static examples, local validation, and executable prototype code. | Does not claim fixture validity equals conformance, implementation readiness, or production readiness. | Evaluate whether fixture validation catches structural errors without overstating assurance. | Static fixtures can improve reviewability; they do not prove implementation correctness. | Add a future evaluation note for prototype fixture validation scope. |
| Claim-boundary discipline as a framework property | AI safety and governance artifacts can overclaim novelty, safety, compliance, or equivalence. | Assurance cases, responsible AI governance, standards mapping, research methodology, compliance communications. | AAEF repeatedly encodes non-goals, exclusions, and baseline boundaries into planning and adoption artifacts. | Does not claim that conservative wording alone provides assurance. | Review artifacts for unsupported claims before and after validation/checklist changes. | Claim-boundary discipline supports trustworthy communication; it is not a substitute for technical control effectiveness. | Add a research claim-boundary note or forbidden-claims checklist. |

## Research contribution candidates by maturity

This section separates candidate contributions by current maturity. The categories are planning aids only.

| Maturity | Candidate contributions | Interpretation |
| --- | --- | --- |
| Strong conceptual candidates | Model output is not authority; action-bound evidence and reconstruction; authorization / dispatch / backend separation. | These are central to AAEF's framing and likely suitable for research positioning if supported by related-work review. |
| Strong adoption candidates | Adoption-facing persona bridge; non-execution as a reviewable outcome; high-impact action orientation. | These are useful for practice-oriented or workshop framing, but require careful distinction from full methodology or production-readiness claims. |
| Strong artifact candidates | Static fixture and validator boundary; conservative external-framework relationship model. | These can be demonstrated through repository artifacts, validators, and mapping hygiene, but should not be overstated as empirical validation. |
| Cross-cutting communication candidate | Claim-boundary discipline as a framework property. | This may be a distinctive strength of AAEF's public artifacts, but it should be framed as research and governance hygiene rather than proof of safety. |

## Evaluation directions

Future evaluation work may include the following options.

### Artifact review evaluation

Review whether AAEF artifacts consistently preserve:

- action authority separation;
- evidence traceability;
- non-execution reviewability;
- claim-boundary discipline;
- baseline-change clarity.

This is a document and artifact quality evaluation. It should not be described as empirical validation of real-world safety.

### Scenario walkthrough evaluation

Apply AAEF to representative agentic action scenarios and evaluate whether reviewers can identify:

- requested action;
- requester or principal;
- authority basis;
- policy version;
- dispatch decision;
- backend relying-party verification;
- execution or non-execution outcome;
- evidence required for reconstruction.

This can support research discussion, but should not be described as production validation unless performed against real systems under a defined study design.

### Negative test evaluation

Use adversarial or failure scenarios such as:

- prompt-injected tool call;
- stale authorization decision;
- mismatched action hash;
- missing backend verification;
- absent evidence event;
- denied action without reconstruction record;
- ambiguous human approval scope.

The evaluation target should be whether AAEF-style controls make these failures detectable or reviewable, not whether AAEF eliminates all risk.

### Persona review evaluation

Ask implementers, operators, auditors, consultants, risk owners, and legal/compliance reviewers to assess whether AAEF materials help them identify:

- what decision they own;
- what evidence they need;
- what residual risk remains;
- what claims should not be made.

This can support adoption-readiness evaluation, but should not be described as certification or audit validation.

## Claims requiring future evidence before use

The following claim types should not be used without additional research, evidence, or independent review.

| Claim type | Why it should not be used now |
| --- | --- |
| Novelty claim | Related-work review and citation inventory are not complete. |
| Completeness claim | AAEF does not cover all agentic AI security, governance, or safety risks. |
| Effectiveness claim | Empirical evaluation has not been performed. |
| Compliance claim | AAEF is not a legal or regulatory compliance framework. |
| Equivalence claim | External framework equivalence has not been established and should not be implied. |
| Certification claim | AAEF is not a certification scheme. |
| Production-readiness claim | AAEF planning and examples do not prove deployment readiness. |
| Audit sufficiency claim | AAEF evidence may support review, but audit conclusions require separate criteria and procedures. |
| Peer-review claim | No peer-reviewed acceptance is asserted by this artifact. |

## Conservative research positioning language

The following language is preferred for future research-facing work:

- AAEF proposes an action assurance control profile for agentic AI systems.
- AAEF treats model output as insufficient authority for high-impact action.
- AAEF emphasizes separable authorization, dispatch enforcement, backend verification, and action-bound evidence.
- AAEF may complement AI risk, security, authorization, logging, assurance, and governance work.
- AAEF's current research status is design-oriented and artifact-oriented.
- Further related-work review, citation inventory, and evaluation are required before stronger novelty or effectiveness claims are made.

The following language should be avoided:

- AAEF is the first framework to solve agentic AI security.
- AAEF proves that agentic systems are safe.
- AAEF guarantees compliance.
- AAEF is equivalent to an established external standard.
- AAEF is production-ready.
- AAEF is empirically validated.
- AAEF is peer-reviewed.
- AAEF replaces IAM, zero trust, incident response, governance, assurance cases, or secure SDLC controls.

## Recommended next step

Recommended next follow-ups for #286:

1. Add a citation inventory planning artifact that defines source eligibility, source version checks, source categories, and exclusion criteria.
2. Add evaluation design options using this contribution matrix as the input.
3. Draft a concise research abstract and problem statement using only conservative positioning language.

The most direct next step after this matrix is likely citation inventory planning, because the contribution candidates now clarify which claims require external support.
