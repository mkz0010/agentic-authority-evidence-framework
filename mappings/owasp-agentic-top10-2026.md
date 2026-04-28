# OWASP Agentic Top 10 2026 Mapping

**Status:** Informative draft mapping for AAEF v0.4.x public review
**AAEF version baseline:** v0.4.0 Public Review Draft with v0.4.x refinements
**Scope:** Informative mapping from OWASP Agentic Top 10 risks to AAEF action assurance controls

## Purpose

This document provides a preliminary mapping between AAEF controls and the OWASP Top 10 for Agentic Applications 2026.

AAEF does **not** replace OWASP guidance.

OWASP identifies major agentic AI security risks. AAEF complements that work by mapping those risks to action assurance controls, including:

- delegated authority,
- policy-enforced action boundaries,
- verifiable evidence,
- human oversight,
- and revocable trust.

This mapping is intended to help reviewers understand how AAEF can support prevention, detection, evidence generation, and incident reconstruction for agentic AI risks.

## Attribution

This mapping references the **OWASP Top 10 for Agentic Applications 2026**, published by the OWASP Gen AI Security Project / Agentic Security Initiative.

OWASP materials are provided under **CC BY-SA 4.0**. This mapping is an independent interpretation and is not endorsed by OWASP.

Source:

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Source Handling and Limitations

This document uses OWASP risk identifiers, risk names, and high-level public context as mapping anchors.

It does not reproduce the full OWASP guidance, examples, mitigations, or detailed source text. Reviewers and implementers should consult the current OWASP source material directly when interpreting OWASP risk categories.

This mapping is informative only. It is not an OWASP compliance mapping, certification claim, audit opinion, complete mitigation claim, or replacement for OWASP guidance.

## Mapping Method

Each OWASP risk is mapped to:

- **AAEF Perspective** — how AAEF interprets the risk through action assurance.
- **Relevant AAEF Threats** — threat categories from `docs/en/04-threat-model.md`.
- **Relevant AAEF Controls** — control requirements from `controls/aaef-controls-v0.1.csv` and related AAEF guidance.
- **Evidence Requirements** — evidence that should be captured for high-impact agentic actions.
- **v0.4.x Review Notes** — limitations, future work, or areas where AAEF should explicitly defer to OWASP or other specialized controls.

This mapping is intentionally conservative. It does not claim that AAEF fully mitigates every OWASP risk. In several cases, AAEF provides governance, authorization, evidence, and response controls that complement other technical security measures.

---

## Summary Table

| OWASP ID | OWASP Risk | AAEF Perspective | Relevant AAEF Threats | Key AAEF Controls | v0.4.x Review Notes |
|---|---|---|---|---|---|
| ASI01 | Agent Goal Hijack | Manipulated goals become dangerous when they influence high-impact actions. AAEF focuses on authorization at the action boundary and evidence of trusted/untrusted inputs. | T4, T5, T8, T9 | AAEF-AUZ-01, AAEF-AUZ-03, AAEF-AUZ-05, AAEF-TOOL-04, AAEF-MEM-03, AAEF-MEM-04, AAEF-EVD-01, AAEF-EVD-02 | Add Principal Context Degradation controls. |
| ASI02 | Tool Misuse and Exploitation | Legitimate tools may be misused when model output reaches tool execution without policy enforcement. AAEF separates authorization from tool dispatch. | T5, T3, T4, T8 | AAEF-TOOL-01, AAEF-TOOL-02, AAEF-TOOL-03, AAEF-TOOL-04, AAEF-AUZ-01, AAEF-AUZ-02, AAEF-EVD-01, AAEF-RES-01 | Add Tool Invocation Evidence Profile. |
| ASI03 | Identity and Privilege Abuse | Agent identity, agent instance identity, principal binding, and authority scope must be explicit and reviewable. | T1, T2, T3, T9 | AAEF-ID-01, AAEF-ID-02, AAEF-ID-03, AAEF-PRN-01, AAEF-PRN-02, AAEF-DEL-01, AAEF-DEL-02, AAEF-RES-01 | Strengthen cross-domain identity and principal binding. |
| ASI04 | Agentic Supply Chain Vulnerabilities | AAEF does not replace supply chain security, but it requires inventory, operator accountability, tool classification, provenance, evidence, and isolation. | T1, T5, T6, T7, T9 | AAEF-GOV-01, AAEF-GOV-03, AAEF-ID-03, AAEF-TOOL-03, AAEF-MEM-02, AAEF-EVD-01, AAEF-RES-02, AAEF-RES-03 | Map to AI/agent supply chain frameworks in future AAEF work. |
| ASI05 | Unexpected Code Execution (RCE) | Code execution should be treated as high-risk tool execution requiring explicit authorization, evidence, and isolation. | T5, T8, T9 | AAEF-TOOL-01, AAEF-TOOL-02, AAEF-TOOL-03, AAEF-TOOL-04, AAEF-AUZ-01, AAEF-AUZ-03, AAEF-EVD-04, AAEF-RES-02 | AAEF complements, but does not define, sandboxing or runtime containment. |
| ASI06 | Memory & Context Poisoning | Retrieved and remembered content should not become trusted instruction by default; provenance and influence on high-impact actions should be evidenced. | T6, T4, T8, T9 | AAEF-MEM-01, AAEF-MEM-02, AAEF-MEM-03, AAEF-MEM-04, AAEF-AUZ-05, AAEF-TOOL-04, AAEF-RES-02 | Add memory lifecycle and context influence schema details. |
| ASI07 | Insecure Inter-Agent Communication | The ability to communicate with another agent does not imply authority to delegate work to that agent. | T7, T1, T2, T3, T8, T9 | AAEF-ID-01, AAEF-ID-02, AAEF-ID-03, AAEF-PRN-01, AAEF-DEL-01, AAEF-DEL-03, AAEF-AUZ-01, AAEF-RES-01 | Add dedicated Cross-Agent / Cross-Domain Authority domain. |
| ASI08 | Cascading Failures | Cascades require sequence-level evidence, downstream revocation, isolation, and reconstruction across workflows and delegations. | T7, T3, T5, T8, T9 | AAEF-GOV-02, AAEF-DEL-02, AAEF-DEL-04, AAEF-AUZ-03, AAEF-TOOL-03, AAEF-EVD-01, AAEF-RES-01, AAEF-RES-02, AAEF-RES-03 | Add action-sequence and dependency evidence guidance. |
| ASI09 | Human-Agent Trust Exploitation | Human approval is not assurance unless the approver has sufficient context, authority, time, and independence. | T4, T8, T9 | AAEF-HUM-01, AAEF-HUM-02, AAEF-AUZ-03, AAEF-AUZ-04, AAEF-AUZ-05, AAEF-EVD-03 | Add approval quality and approval fatigue controls. |
| ASI10 | Rogue Agents | Rogue agents should be addressed through inventory, identity, operator accountability, authorization denial on ambiguity, evidence, isolation, and revocation. | T1, T2, T3, T7, T8, T9 | AAEF-GOV-01, AAEF-GOV-03, AAEF-ID-01, AAEF-ID-02, AAEF-ID-03, AAEF-AUZ-01, AAEF-AUZ-04, AAEF-RES-01, AAEF-RES-02 | Add agent admission and external agent trust controls. |

---

## Detailed Mapping

### ASI01: Agent Goal Hijack

#### AAEF Perspective

Agent goal hijack becomes most dangerous when a manipulated goal crosses from reasoning into execution.

AAEF treats this as an action assurance problem:

- Was the requested action still within the original principal intent?
- Was the action authorized at the point of execution?
- Did untrusted content influence the goal, purpose, or action selection?
- Was the influence recorded as evidence?

AAEF does not rely on prompt filtering alone. It focuses on action-boundary authorization and evidence of trusted vs untrusted inputs.

#### Relevant AAEF Threats

- T4: Prompt and Intent Manipulation Threats
- T5: Tool and Action Boundary Threats
- T8: Evidence and Auditability Threats
- T9: Revocation and Response Threats

#### Relevant AAEF Controls

- AAEF-AUZ-01: Action Boundary Authorization
- AAEF-AUZ-02: Purpose and Resource Binding
- AAEF-AUZ-03: Risk-Based Approval
- AAEF-AUZ-05: Authorization Isolation from Untrusted Content
- AAEF-TOOL-02: Tool Invocation Policy
- AAEF-TOOL-04: Tool Invocation from Untrusted Content
- AAEF-MEM-03: External Content as Data
- AAEF-MEM-04: Retrieved or Remembered Content Provenance
- AAEF-EVD-01: High-Impact Action Evidence
- AAEF-EVD-02: Evidence Fields
- AAEF-RES-03: Incident Reconstruction

#### Evidence Requirements

For high-impact actions that may be affected by goal hijack, evidence should include:

- original principal instruction or principal context reference,
- requested action,
- declared purpose,
- input sources,
- trusted inputs used for authorization,
- untrusted inputs excluded from authorization,
- authorization decision,
- approval evidence where required,
- result,
- and whether untrusted content influenced the action.

#### v0.4.x Review Notes

Future AAEF work should define **Principal Context Degradation** to address long-running tasks where the original principal intent becomes semantically distant from later actions.

---

### ASI02: Tool Misuse and Exploitation

#### AAEF Perspective

Tool misuse occurs when legitimate tools are used in unsafe, unintended, or excessive ways.

AAEF maps this risk to the separation between:

- model output,
- authorization decision,
- and tool dispatch.

A model may propose a tool call, but the tool should only be invoked if the action is authorized, within scope, and evidenced.

#### Relevant AAEF Threats

- T5: Tool and Action Boundary Threats
- T3: Delegation and Authority Threats
- T4: Prompt and Intent Manipulation Threats
- T8: Evidence and Auditability Threats

#### Relevant AAEF Controls

- AAEF-TOOL-01: Tool Minimum Authority
- AAEF-TOOL-02: Tool Invocation Policy
- AAEF-TOOL-03: High-Risk Tool Classification
- AAEF-TOOL-04: Tool Invocation from Untrusted Content
- AAEF-AUZ-01: Action Boundary Authorization
- AAEF-AUZ-02: Purpose and Resource Binding
- AAEF-AUZ-03: Risk-Based Approval
- AAEF-EVD-01: High-Impact Action Evidence
- AAEF-EVD-02: Evidence Fields
- AAEF-RES-01: Revocation Capability

#### Evidence Requirements

Evidence should include:

- tool invoked,
- operation or action type,
- tool arguments or a privacy-preserving argument digest,
- target resource,
- authority scope,
- purpose,
- authorization decision,
- approval reference where required,
- result,
- and external effect indicator.

#### v0.4.x Review Notes

Future AAEF work may define a **Tool Invocation Evidence Profile** for high-risk tools.

---

### ASI03: Identity and Privilege Abuse

#### AAEF Perspective

Agentic systems introduce identity and privilege questions that are more complex than a single user token.

AAEF requires systems to distinguish:

- agent product,
- agent instance,
- principal,
- operator,
- issuer,
- delegated authority,
- and downstream delegation.

Privilege abuse should be addressed through explicit authority scope, attenuated delegation, and revocable trust.

#### Relevant AAEF Threats

- T1: Identity and Authentication Threats
- T2: Principal Binding Threats
- T3: Delegation and Authority Threats
- T9: Revocation and Response Threats

#### Relevant AAEF Controls

- AAEF-ID-01: Agent Identity
- AAEF-ID-02: Agent Instance Distinction
- AAEF-ID-03: Issuer and Operator Identification
- AAEF-PRN-01: Principal Binding
- AAEF-PRN-02: Principal Context Preservation
- AAEF-DEL-01: Attenuated Delegation
- AAEF-DEL-02: Delegation Constraints
- AAEF-DEL-03: Delegation Chain Evidence
- AAEF-DEL-04: Downstream Revocation
- AAEF-AUZ-01: Action Boundary Authorization
- AAEF-AUZ-04: Deny on Authority Ambiguity
- AAEF-RES-01: Revocation Capability

#### Evidence Requirements

Evidence should include:

- agent identity,
- agent instance identity,
- issuer,
- operator,
- principal,
- authority scope,
- delegation chain,
- credential or token reference where appropriate,
- authorization decision,
- revocation state,
- and downstream delegation references.

#### v0.4.x Review Notes

Future AAEF work should strengthen guidance for cross-domain principal binding and external agent identity verification.

---

### ASI04: Agentic Supply Chain Vulnerabilities

#### AAEF Perspective

AAEF does not replace software supply chain, AI supply chain, model supply chain, or vendor risk controls.

However, supply chain compromise becomes relevant to AAEF when compromised tools, plugins, models, memory sources, retrieval sources, or agent components can influence high-impact actions.

AAEF contributes by requiring inventory, ownership, issuer/operator accountability, tool classification, provenance, evidence, isolation, and incident reconstruction.

#### Relevant AAEF Threats

- T1: Identity and Authentication Threats
- T5: Tool and Action Boundary Threats
- T6: Memory and Retrieval Threats
- T7: Multi-Agent and A2A Threats
- T9: Revocation and Response Threats

#### Relevant AAEF Controls

- AAEF-GOV-01: Agentic System Inventory
- AAEF-GOV-03: Ownership and Accountability
- AAEF-ID-03: Issuer and Operator Identification
- AAEF-TOOL-01: Tool Minimum Authority
- AAEF-TOOL-03: High-Risk Tool Classification
- AAEF-MEM-02: Retrieval Source Trust
- AAEF-MEM-04: Retrieved or Remembered Content Provenance
- AAEF-EVD-01: High-Impact Action Evidence
- AAEF-EVD-02: Evidence Fields
- AAEF-RES-02: Agent Isolation
- AAEF-RES-03: Incident Reconstruction

#### Evidence Requirements

Evidence should include:

- agent component or tool identity,
- issuer/operator,
- tool or component version where available,
- retrieval source provenance,
- memory source provenance,
- affected action IDs,
- authority scope used,
- isolation actions,
- and incident reconstruction timeline.

#### v0.4.x Review Notes

AAEF should avoid overclaiming in supply chain security. A future mapping may connect AAEF to AI BOM, SBOM, model supply chain, plugin registry, MCP server, and vendor risk frameworks.

---

### ASI05: Unexpected Code Execution (RCE)

#### AAEF Perspective

Unexpected code execution should be treated as high-risk tool execution.

AAEF does not define sandboxing, runtime isolation, exploit mitigation, or secure code execution environments. Those are technical security domains outside AAEF's core scope.

AAEF complements those controls by requiring that code execution actions be classified, authorized, evidenced, and revocable.

#### Relevant AAEF Threats

- T5: Tool and Action Boundary Threats
- T8: Evidence and Auditability Threats
- T9: Revocation and Response Threats

#### Relevant AAEF Controls

- AAEF-TOOL-01: Tool Minimum Authority
- AAEF-TOOL-02: Tool Invocation Policy
- AAEF-TOOL-03: High-Risk Tool Classification
- AAEF-TOOL-04: Tool Invocation from Untrusted Content
- AAEF-AUZ-01: Action Boundary Authorization
- AAEF-AUZ-03: Risk-Based Approval
- AAEF-AUZ-04: Deny on Authority Ambiguity
- AAEF-EVD-01: High-Impact Action Evidence
- AAEF-EVD-02: Evidence Fields
- AAEF-EVD-04: Tamper-Evident Evidence
- AAEF-RES-02: Agent Isolation
- AAEF-RES-03: Incident Reconstruction

#### Evidence Requirements

Evidence should include:

- code execution tool identity,
- requested command or code reference,
- resource or environment,
- execution purpose,
- authority scope,
- approval reference where required,
- result,
- output or output digest,
- external effect indicator,
- and containment or isolation status.

#### v0.4.x Review Notes

AAEF may define a high-risk action category for code execution and production system changes, but should continue to defer sandboxing and exploit prevention details to specialized security frameworks.

---

### ASI06: Memory & Context Poisoning

#### AAEF Perspective

Memory and context poisoning are critical because untrusted or poisoned information can influence future action selection, authorization requests, tool calls, and delegation.

AAEF treats retrieved and remembered content as data by default, not trusted instruction.

For high-impact actions, AAEF requires provenance or trust metadata for retrieved or remembered content that materially influenced the action.

#### Relevant AAEF Threats

- T6: Memory and Retrieval Threats
- T4: Prompt and Intent Manipulation Threats
- T8: Evidence and Auditability Threats
- T9: Revocation and Response Threats

#### Relevant AAEF Controls

- AAEF-MEM-01: Memory Write Control
- AAEF-MEM-02: Retrieval Source Trust
- AAEF-MEM-03: External Content as Data
- AAEF-MEM-04: Retrieved or Remembered Content Provenance
- AAEF-AUZ-05: Authorization Isolation from Untrusted Content
- AAEF-TOOL-04: Tool Invocation from Untrusted Content
- AAEF-EVD-01: High-Impact Action Evidence
- AAEF-EVD-02: Evidence Fields
- AAEF-RES-02: Agent Isolation
- AAEF-RES-03: Incident Reconstruction

#### Evidence Requirements

Evidence should include:

- memory write event or retrieval event reference,
- source type,
- source trust level,
- provenance metadata,
- content digest where appropriate,
- whether retrieved or remembered content influenced the action,
- authorization inputs used,
- untrusted inputs excluded,
- and isolation or remediation actions.

#### v0.4.x Review Notes

Future AAEF work should refine how evidence events represent context influence, memory writes, memory reads, and retrieval provenance.

---

### ASI07: Insecure Inter-Agent Communication

#### AAEF Perspective

Agent-to-agent communication creates authority and evidence problems.

AAEF's position is:

> The ability to communicate with another agent does not imply authority to delegate work to that agent.

Inter-agent communication should preserve identity, principal context, authority scope, delegation constraints, evidence, and revocation status.

#### Relevant AAEF Threats

- T7: Multi-Agent and A2A Threats
- T1: Identity and Authentication Threats
- T2: Principal Binding Threats
- T3: Delegation and Authority Threats
- T8: Evidence and Auditability Threats
- T9: Revocation and Response Threats

#### Relevant AAEF Controls

- AAEF-ID-01: Agent Identity
- AAEF-ID-02: Agent Instance Distinction
- AAEF-ID-03: Issuer and Operator Identification
- AAEF-PRN-01: Principal Binding
- AAEF-PRN-02: Principal Context Preservation
- AAEF-DEL-01: Attenuated Delegation
- AAEF-DEL-02: Delegation Constraints
- AAEF-DEL-03: Delegation Chain Evidence
- AAEF-DEL-04: Downstream Revocation
- AAEF-AUZ-01: Action Boundary Authorization
- AAEF-AUZ-04: Deny on Authority Ambiguity
- AAEF-EVD-01: High-Impact Action Evidence
- AAEF-RES-01: Revocation Capability

#### Evidence Requirements

Evidence should include:

- upstream agent identity,
- downstream agent identity,
- trust domain,
- principal binding,
- delegation chain,
- authority scope,
- delegation constraints,
- accepted or rejected delegation decision,
- cross-domain evidence references,
- and revocation status.

#### v0.4.x Review Notes

Future AAEF work should add a dedicated **Cross-Agent / Cross-Domain Authority** domain or control set.

Candidate controls may include:

- Agent-to-Agent Authority Verification
- Cross-Domain Principal Binding
- Agent Capability Declaration Verification
- Delegation Acceptance Policy
- Cross-Domain Evidence Exchange
- External Agent Trust Revocation

---

### ASI08: Cascading Failures

#### AAEF Perspective

Cascading failures occur when one agentic error, compromise, or misjudgment propagates through tools, workflows, delegations, or other agents.

AAEF contributes by requiring high-impact action classification, delegation constraints, downstream revocation, evidence, isolation, and incident reconstruction.

For cascades, evidence must support sequence-level reconstruction, not only single-action review.

#### Relevant AAEF Threats

- T7: Multi-Agent and A2A Threats
- T3: Delegation and Authority Threats
- T5: Tool and Action Boundary Threats
- T8: Evidence and Auditability Threats
- T9: Revocation and Response Threats

#### Relevant AAEF Controls

- AAEF-GOV-02: High-Impact Action Definition
- AAEF-DEL-02: Delegation Constraints
- AAEF-DEL-03: Delegation Chain Evidence
- AAEF-DEL-04: Downstream Revocation
- AAEF-AUZ-03: Risk-Based Approval
- AAEF-TOOL-03: High-Risk Tool Classification
- AAEF-EVD-01: High-Impact Action Evidence
- AAEF-EVD-02: Evidence Fields
- AAEF-RES-01: Revocation Capability
- AAEF-RES-02: Agent Isolation
- AAEF-RES-03: Incident Reconstruction

#### Evidence Requirements

Evidence should include:

- action sequence ID or correlation ID,
- upstream and downstream actions,
- delegation chain,
- tool invocations,
- risk levels,
- authorization decisions,
- approval records,
- revocation events,
- isolation events,
- and incident reconstruction timeline.

#### v0.4.x Review Notes

Future AAEF work should add guidance for action sequences, dependency evidence, and cascade reconstruction.

---

### ASI09: Human-Agent Trust Exploitation

#### AAEF Perspective

Human-agent trust exploitation occurs when humans over-trust agents, approve actions without sufficient context, or are socially influenced by agent outputs.

AAEF treats human approval as useful but insufficient by itself.

Human approval is not assurance unless the approver has sufficient context, authority, time, and independence to evaluate the action.

#### Relevant AAEF Threats

- T4: Prompt and Intent Manipulation Threats
- T8: Evidence and Auditability Threats
- T9: Revocation and Response Threats

#### Relevant AAEF Controls

- AAEF-HUM-01: Approval UX Clarity
- AAEF-HUM-02: Approval Fatigue Mitigation
- AAEF-AUZ-03: Risk-Based Approval
- AAEF-AUZ-04: Deny on Authority Ambiguity
- AAEF-AUZ-05: Authorization Isolation from Untrusted Content
- AAEF-EVD-01: High-Impact Action Evidence
- AAEF-EVD-02: Evidence Fields
- AAEF-EVD-03: Approval Evidence
- AAEF-RES-03: Incident Reconstruction

#### Evidence Requirements

Evidence should include:

- approval request content,
- agent identity,
- principal,
- requested action,
- resource,
- purpose,
- risk level,
- consequence summary,
- approver identity,
- approval decision,
- approval timestamp,
- and link between approval and executed action.

#### v0.4.x Review Notes

Future AAEF work should expand approval quality controls, including approval threshold calibration, approval sampling, approval outcome monitoring, separation of duties, and approval bypass detection.

---

### ASI10: Rogue Agents

#### AAEF Perspective

Rogue agents include unapproved, impersonating, compromised, misconfigured, or unauthorized agents participating in workflows.

AAEF maps this risk to inventory, identity, operator accountability, denial on authority ambiguity, evidence, isolation, and revocation.

A system should not allow high-impact actions by agents that are not inventoried, identifiable, authorized, and accountable.

#### Relevant AAEF Threats

- T1: Identity and Authentication Threats
- T2: Principal Binding Threats
- T3: Delegation and Authority Threats
- T7: Multi-Agent and A2A Threats
- T8: Evidence and Auditability Threats
- T9: Revocation and Response Threats

#### Relevant AAEF Controls

- AAEF-GOV-01: Agentic System Inventory
- AAEF-GOV-03: Ownership and Accountability
- AAEF-ID-01: Agent Identity
- AAEF-ID-02: Agent Instance Distinction
- AAEF-ID-03: Issuer and Operator Identification
- AAEF-PRN-01: Principal Binding
- AAEF-AUZ-01: Action Boundary Authorization
- AAEF-AUZ-04: Deny on Authority Ambiguity
- AAEF-EVD-01: High-Impact Action Evidence
- AAEF-EVD-02: Evidence Fields
- AAEF-RES-01: Revocation Capability
- AAEF-RES-02: Agent Isolation
- AAEF-RES-03: Incident Reconstruction

#### Evidence Requirements

Evidence should include:

- agent inventory record,
- agent identity,
- agent instance identity,
- issuer,
- operator,
- principal,
- authorization decision,
- denial reason where applicable,
- isolation action,
- revocation event,
- and incident reconstruction data.

#### v0.4.x Review Notes

Future AAEF work should consider controls for agent admission, external agent trust decisions, and rogue agent quarantine.

---

## Cross-Cutting Observations

### 1. AAEF is strongest where OWASP risks become actions

AAEF is most directly applicable when an OWASP risk crosses into:

- tool invocation,
- external communication,
- data access or export,
- financial action,
- privilege change,
- persistent memory write,
- code execution,
- inter-agent delegation,
- or other high-impact actions.

### 2. AAEF is not a complete technical mitigation framework

AAEF does not fully specify:

- sandboxing,
- exploit prevention,
- secure coding,
- SBOM or AI BOM management,
- model evaluation,
- network segmentation,
- cryptographic protocol design,
- or runtime isolation.

Those should be handled by specialized frameworks and implementation-specific controls.

### 3. AAEF adds an evidence layer

AAEF's contribution is strongest when it asks:

> If this risk resulted in an agentic action, what evidence would prove what happened?

This evidence perspective should be preserved in future mappings.

### 4. Future work should continue tracking A2A, evidence schema, and principal context

This mapping suggests that future work should continue tracking:

- Cross-Agent / Cross-Domain Authority
- Principal Context Degradation
- Evidence Event Schema
- High-Impact Action Taxonomy
- Approval Quality and Approval Fatigue Controls
- Tool Invocation Evidence Profile

## Review Questions

Feedback is welcome on:

- whether the mapped controls are appropriate,
- whether any controls are overclaimed,
- where AAEF should explicitly defer to OWASP or other frameworks,
- what evidence requirements are missing,
- how to represent cross-agent evidence,
- and whether additional AAEF controls are needed in future AAEF work.
