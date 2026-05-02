# AAEF v0.6.0 Legal and Compliance Applicability Note Planning Draft

Status: Planning input  
Related roadmap: #241  
Related track: #245  
Related operational track: #244  
Related implementer track: #243  
Related architecture track: #246  
Parent planning synthesis: `docs/en/status/v060-planning-input-synthesis.md`  
Related operational planning: `docs/en/status/v060-operational-responsibility-matrix-planning.md`  
Related architecture planning: `docs/en/status/v060-high-impact-production-minimum-architecture-profile-planning.md`  
Related implementer planning: `docs/en/status/v060-implementer-quick-start-planning.md`  
Planned release theme: AAEF v0.6.0 Practical Adoption Readiness

## Purpose

This document defines an initial planning draft for an AAEF Legal and Compliance Applicability Note.

The purpose is to clarify how AAEF may support legal, compliance, contractual, audit, and governance discussions about high-impact agentic actions without claiming certification, legal compliance, or replacement of external standards.

This document is planning material. It does not change active controls, assessment criteria, legal obligations, schema requirements, or the current control and assessment baseline.

## Intended audience

This planning draft is intended for:

- legal and compliance reviewers
- privacy and data protection reviewers
- audit and assurance teams
- risk owners
- vendor management and procurement teams
- security governance teams
- implementers who need to understand legal and compliance boundaries
- executives evaluating whether AAEF can support adoption decisions

## Core positioning

AAEF should be positioned as an action assurance and evidence framework for agentic AI systems.

AAEF may help an organization explain:

- who or what authorized an agentic action
- what action was requested
- what policy and context were used
- whether execution was mediated by an enforcement point
- whether backend execution was bound to authorization
- what evidence supports execution, refusal, denial, non-execution, override, or reauthorization
- which operational owner, system owner, policy owner, or risk owner was responsible
- what residual risks and exceptions were accepted

AAEF should not be positioned as:

- a legal compliance framework
- a certification scheme
- a substitute for regulatory analysis
- a replacement for ISO 42001, NIST AI RMF, EU AI Act obligations, OWASP guidance, CSA guidance, privacy law, sector-specific obligations, or contractual requirements
- a guarantee that an AI system is safe, lawful, compliant, or fit for a regulated purpose

## Recommended claim language

AAEF should use conservative support language.

Recommended phrases:

- AAEF may support assessment of agentic action authority and evidence.
- AAEF may support evidence collection for agentic action review.
- AAEF can help demonstrate how authorization, dispatch, execution, and evidence were handled.
- AAEF can support auditability of high-impact agentic actions.
- AAEF can help organizations document responsibility boundaries and residual risk decisions.
- AAEF may provide supplementary evidence for legal, compliance, audit, or governance review.

## Claim language to avoid

AAEF should avoid unsupported compliance or certification claims.

Avoid phrases such as:

- AAEF satisfies legal requirements.
- AAEF guarantees compliance.
- AAEF certifies an AI system.
- AAEF makes an AI agent safe.
- AAEF makes an organization compliant with a named law or regulation.
- AAEF replaces external standards.
- AAEF proves that an action was legally authorized.
- AAEF eliminates liability.
- AAEF eliminates residual risk.

## Applicability model

AAEF's legal and compliance value should be described as supplementary.

A future applicability note should distinguish between:

| Applicability type | Meaning |
| --- | --- |
| Direct requirement | A binding legal, regulatory, contractual, or policy obligation outside AAEF. |
| Supporting evidence | AAEF-generated or AAEF-aligned evidence that may help evaluate an obligation. |
| Control support | AAEF control or guidance that may support an organization's internal control design. |
| Assessment support | AAEF material that may help an assessor review authority, evidence, responsibility, or reconstruction. |
| Governance support | AAEF material that may help risk owners, executives, or oversight bodies make adoption decisions. |

AAEF should not blur these categories.

## Candidate legal and compliance questions AAEF may help answer

AAEF may help answer questions such as:

1. What action did the agentic system request or influence?
2. Was the action high-impact?
3. Which principal or delegated authority was associated with the action?
4. Which authorization policy was used?
5. Was approval required?
6. Was approval captured and bound to the action?
7. Was dispatch mediated by an enforcement point?
8. Did the backend verify authorization before execution?
9. Was the action executed, denied, refused, overridden, reauthorized, or not executed?
10. What evidence supports that lifecycle?
11. Who owns the policy, system, evidence, and residual risk?
12. Was an exception approved?
13. Did the exception expire?
14. Is there evidence of monitoring, alerting, or incident response?
15. Which third-party or SaaS provider responsibilities are outside the organization's direct control?

## Candidate applicability areas

The following areas are candidates for future applicability guidance.

| Area | How AAEF may support review |
| --- | --- |
| Internal governance | Documents authority, evidence, ownership, and residual risk decisions for agentic actions. |
| Audit readiness | Supports reconstruction of high-impact action lifecycles. |
| Vendor and SaaS review | Helps identify responsibility boundaries and evidence gaps for external components. |
| Contractual controls | Provides language and evidence expectations for agentic action controls. |
| Privacy and retention review | Helps identify what evidence is retained, why, for how long, and by whom. |
| Incident response | Supports reconstruction of disputed, suspicious, unauthorized, or mismatched actions. |
| AI impact assessment | Provides action-level evidence and responsibility context for high-impact use cases. |
| Board or executive reporting | Supports concise reporting on action assurance, exceptions, incidents, and residual risk. |

## Relationship to external standards and frameworks

AAEF should be described as complementary to external standards and frameworks.

A future applicability note may discuss conservative relationships to:

- ISO 42001
- NIST AI RMF
- EU AI Act obligations
- OWASP guidance
- CSA guidance
- internal governance and risk management frameworks
- sector-specific compliance programs
- contractual control requirements
- privacy and data protection requirements

However, any mapping should be conservative.

AAEF should not say that an AAEF artifact alone satisfies an external requirement unless a qualified legal, compliance, or audit reviewer has made that determination in a specific context.

## Responsibility boundary model

Legal and compliance applicability depends on clear responsibility boundaries.

The note should use the Operational Responsibility Matrix to distinguish:

| Responsibility area | Candidate legal/compliance relevance |
| --- | --- |
| Risk ownership | Who accepts residual risk for high-impact agentic actions. |
| Policy ownership | Who defines and approves authorization policy. |
| System ownership | Who owns the affected system or business process. |
| Agent ownership | Who owns agent configuration, deployment, and intended use. |
| Evidence ownership | Who controls evidence generation, retention, retrieval, and integrity. |
| Incident ownership | Who investigates unauthorized, suspicious, or mismatched execution. |
| Third-party ownership | Who manages external agents, tools, SaaS services, and responsibility gaps. |
| Legal/compliance review | Who reviews applicability, retention, privacy, contract, and regulatory implications. |

## Evidence privacy and retention considerations

AAEF evidence can support accountability, but evidence collection can also create privacy, confidentiality, security, and retention risks.

A future applicability note should address:

- what evidence is collected
- whether evidence includes personal data, confidential data, regulated data, or sensitive operational data
- who can access evidence
- how long evidence is retained
- when evidence should be minimized, redacted, aggregated, or access-controlled
- whether evidence is needed for audit, incident response, dispute resolution, or regulatory review
- how evidence retention interacts with deletion, litigation hold, legal hold, or contractual requirements

AAEF should avoid encouraging indiscriminate over-logging.

## Contractual applicability considerations

AAEF may support contractual discussions where agentic systems involve vendors, SaaS providers, managed service providers, model providers, tool providers, or external agents.

Candidate contract topics:

- responsibility for authorization decisions
- responsibility for tool dispatch enforcement
- responsibility for backend verification
- evidence generation and availability
- evidence retention and retrieval timelines
- incident notification
- support for investigation and reconstruction
- third-party subcontractor responsibility
- data handling and privacy expectations
- audit support and cooperation
- emergency disablement or freeze support

AAEF should not imply that these terms exist by default. They should be negotiated and documented where needed.

## SaaS and external agent responsibility boundaries

For SaaS or external agent deployments, organizations may not control all relevant components.

A future note should help identify:

| Boundary question | Why it matters |
| --- | --- |
| Who controls the agent runtime? | Determines whether model output and tool requests can be governed directly. |
| Who controls the tool gateway? | Determines where dispatch enforcement can occur. |
| Who issues authorization decisions? | Determines whether authority is internal, external, or shared. |
| Who controls backend execution? | Determines whether relying-party verification is feasible. |
| Who generates evidence? | Determines trustworthiness and completeness of action records. |
| Who retains evidence? | Determines audit, privacy, and incident response readiness. |
| Who can freeze or disable actions? | Determines containment capability. |
| Who accepts residual risk? | Determines governance accountability. |

## DPIA and AI impact assessment support

AAEF may support DPIA, AI impact assessment, or similar review processes by providing action-level evidence and responsibility structure.

Candidate support areas:

- high-impact action identification
- authority and delegation description
- approval and override handling
- evidence generation and retention description
- human review and escalation paths
- monitoring and incident response expectations
- third-party responsibility mapping
- residual risk documentation

AAEF should be described as input to such assessments, not a replacement for them.

## Candidate legal and compliance artifacts

The Legal and Compliance Applicability track may later produce:

| Candidate artifact | Purpose |
| --- | --- |
| Legal and Compliance Applicability Note | Explains conservative applicability and claim boundaries. |
| Evidence Privacy and Retention Policy template | Helps organizations govern evidence collection and retention. |
| Contractual Control Addendum | Provides candidate contract language for AAEF-aligned responsibilities. |
| SaaS / external agent responsibility matrix | Helps map responsibility gaps for external deployments. |
| DPIA / AI Impact Assessment support template | Helps translate AAEF evidence into impact assessment input. |

## Candidate anti-patterns

| Anti-pattern | Risk |
| --- | --- |
| Claiming AAEF compliance as legal compliance | Overstates what AAEF provides. |
| Treating evidence volume as evidence quality | Over-logging may not support accountability and may create privacy risk. |
| Ignoring third-party responsibility gaps | External dependencies may remain unauditable or ungoverned. |
| No retention rationale | Evidence may be retained too long, too briefly, or without legal basis. |
| No exception expiration | Temporary legal or compliance exceptions may become permanent bypasses. |
| No owner for residual risk | Compliance review cannot identify who accepted unresolved risk. |
| Mapping to external standards too aggressively | Creates misleading assurance or unsupported claims. |
| Treating AAEF as certification | Misrepresents the framework's role and maturity. |

## Suggested structure for a future applicability note

A future adoption-facing note should likely include:

1. scope and audience
2. conservative positioning statement
3. recommended and prohibited claim language
4. applicability model
5. relationship to external standards and frameworks
6. evidence privacy and retention considerations
7. contractual control considerations
8. SaaS and external agent responsibility boundaries
9. DPIA / AI impact assessment support
10. audit and assurance support
11. executive and risk owner communication guidance
12. anti-patterns and non-goals

## Open questions

The following questions should be resolved before promoting this planning draft into an adoption-facing note:

- Which external standards should be discussed first?
- Should crosswalks be deferred to separate documents?
- How conservative should applicability language be in the first public note?
- Should evidence privacy and retention be a separate artifact before contract language?
- Should SaaS / external agent responsibility mapping be a standalone template?
- What examples should be included without making legal advice claims?
- Should the note explicitly state that legal counsel should review context-specific obligations?
- How should AAEF discuss AI impact assessments without implying statutory sufficiency?
- Should contractual language be illustrative only, or should it become a formal addendum candidate?

## Acceptance criteria for this planning draft

This planning draft is sufficient when:

- conservative claim boundaries are documented
- recommended and prohibited language are identified
- supplementary applicability positioning is defined
- relationship to external standards is framed conservatively
- privacy, retention, contractual, SaaS, and impact assessment topics are identified
- anti-patterns are documented
- no active baseline change is implied
- #245 can use this document as input for a future Legal and Compliance Applicability Note

## Expected next steps

Recommended next steps:

1. Review conservative claim language.
2. Decide which external standards or frameworks should be referenced in the first applicability note.
3. Decide whether Evidence Privacy and Retention Policy should be the next legal/compliance artifact.
4. Decide whether SaaS / external agent responsibility mapping should be split into a separate planning draft.
5. Determine whether the eventual adoption-facing note should remain in status material first or move into a legal/compliance-oriented document path.
