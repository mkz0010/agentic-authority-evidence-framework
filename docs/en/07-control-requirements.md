# 07. Control Requirements

This section provides the initial AAEF v0.1 control requirements.

The normative control catalog is available as CSV:

- `controls/aaef-controls-v0.1.csv`

The CSV file is the source of truth for control IDs, requirement text, objectives, applicability, testing procedures, evidence examples, and maturity classification. This Markdown file is maintained for readability and must remain consistent with the CSV catalog.

## Requirement Format

Each requirement uses the following structure:

- **Control ID**
- **Domain**
- **Requirement**
- **Objective**
- **Applicability**
- **Testing Procedure**
- **Evidence Examples**
- **Maturity**

## Initial Requirements

### AAEF-GOV-01: Maintain an inventory of agentic AI systems that can access data, call tools, delegate tasks, or perform actions

**Domain:** Governance  
**Requirement:** Maintain an inventory of agentic AI systems that can access data, call tools, delegate tasks, or perform actions.  
**Objective:** Ensure agentic systems are known and governable.  
**Applicability:** All production or pilot agentic AI systems.  
**Testing Procedure:** Review inventory and compare against deployed agents, tools, and workflows.  
**Evidence Examples:** Agent inventory; system registry; owner records.  
**Maturity:** Required

### AAEF-GOV-02: Define high-impact agentic actions based on operational, financial, legal, privacy, security, safety, and reputational risk

**Domain:** Governance  
**Requirement:** Define high-impact agentic actions based on operational, financial, legal, privacy, security, safety, and reputational risk.  
**Objective:** Establish action risk boundaries.  
**Applicability:** Organizations using agents for business or operational actions.  
**Testing Procedure:** Review high-impact action taxonomy and approval thresholds.  
**Evidence Examples:** Risk taxonomy; policy document; approval matrix.  
**Maturity:** Required

### AAEF-GOV-03: Assign a business owner, technical owner, and risk owner for each production agentic AI system

**Domain:** Governance  
**Requirement:** Assign a business owner, technical owner, and risk owner for each production agentic AI system.  
**Objective:** Ensure accountability.  
**Applicability:** Production agentic AI systems.  
**Testing Procedure:** Review ownership records and interview responsible parties.  
**Evidence Examples:** RACI; ownership register; governance records.  
**Maturity:** Required

### AAEF-ID-01: Each production agent shall have a unique and verifiable identity

**Domain:** Agent Identity  
**Requirement:** Each production agent shall have a unique and verifiable identity.  
**Objective:** Identify which agent acted.  
**Applicability:** Production agents.  
**Testing Procedure:** Inspect identity records and verification mechanisms.  
**Evidence Examples:** Agent registry; identity claims; credentials.  
**Maturity:** Required

### AAEF-ID-02: Systems shall distinguish between an agent product and a specific agent instance

**Domain:** Agent Identity  
**Requirement:** Systems shall distinguish between an agent product and a specific agent instance.  
**Objective:** Avoid instance confusion.  
**Applicability:** Multi-instance or multi-tenant agent systems.  
**Testing Procedure:** Review logs and identity model for product vs instance distinction.  
**Evidence Examples:** Agent instance ID; runtime metadata; logs.  
**Maturity:** Required

### AAEF-ID-03: Agent identity records shall identify the issuer and operator responsible for the agent

**Domain:** Agent Identity  
**Requirement:** Agent identity records shall identify the issuer and operator responsible for the agent.  
**Objective:** Support accountability and trust decisions.  
**Applicability:** Agents operated across teams, tenants, vendors, or domains.  
**Testing Procedure:** Review issuer/operator metadata.  
**Evidence Examples:** Agent card; registry; operator metadata.  
**Maturity:** Recommended

### AAEF-PRN-01: Each high-impact agentic action shall be bound to a principal

**Domain:** Principal Binding  
**Requirement:** Each high-impact agentic action shall be bound to a principal.  
**Objective:** Identify on whose behalf the action occurred.  
**Applicability:** High-impact actions.  
**Testing Procedure:** Sample action evidence and verify principal binding.  
**Evidence Examples:** Action logs; principal claims; session records.  
**Maturity:** Required

### AAEF-PRN-02: Principal context shall be preserved across tool calls, workflow steps, and delegations.

**Domain:** Principal Binding  
**Requirement:** Principal context shall be preserved across tool calls, workflow steps, and delegations.  
**Objective:** Prevent loss of accountability across workflows.  
**Applicability:** Tool-using or delegating agents.  
**Testing Procedure:** Trace sample workflows end-to-end and verify that principal context is preserved through correlation IDs, trace IDs, session-scoped authority tokens, signed claims, workflow metadata, or structured delegation records.  
**Evidence Examples:** Trace logs; correlation IDs; trace IDs; session-scoped authority tokens; signed principal claims; delegation records; tool invocation metadata.  
**Maturity:** Required

**Implementation Note:** Principal context propagation is not automatic in stateless API chains, asynchronous workflows, queues, background jobs, or multi-agent delegation. Implementations should use explicit propagation mechanisms such as correlation IDs, trace IDs, session-scoped authority tokens, signed claims, workflow metadata, or structured delegation records. If principal context cannot be preserved, high-impact actions should be denied or escalated.

### AAEF-DEL-01: Delegated authority shall not exceed the authority held by the delegating party

**Domain:** Delegation and Authority  
**Requirement:** Delegated authority shall not exceed the authority held by the delegating party.  
**Objective:** Prevent delegation-based escalation.  
**Applicability:** Systems supporting delegation or sub-agents.  
**Testing Procedure:** Compare delegator and delegatee scopes.  
**Evidence Examples:** Delegation policy; token claims; scope records.  
**Maturity:** Required

### AAEF-DEL-02: Delegations shall include constraints such as action type, resource, purpose, duration, amount, count, and delegation depth where applicable

**Domain:** Delegation and Authority  
**Requirement:** Delegations shall include constraints such as action type, resource, purpose, duration, amount, count, and delegation depth where applicable.  
**Objective:** Bound delegated authority.  
**Applicability:** Delegating agents and workflows.  
**Testing Procedure:** Review delegation records for constraints.  
**Evidence Examples:** Authority grants; delegation chain; policy config.  
**Maturity:** Required

### AAEF-DEL-03: Delegation chains for high-impact actions shall be recorded as evidence

**Domain:** Delegation and Authority  
**Requirement:** Delegation chains for high-impact actions shall be recorded as evidence.  
**Objective:** Support audit and incident reconstruction.  
**Applicability:** High-impact delegated actions.  
**Testing Procedure:** Review evidence for delegation chain completeness.  
**Evidence Examples:** Delegation logs; action evidence; trace IDs.  
**Maturity:** Required

### AAEF-DEL-04: Revocation of upstream authority shall invalidate dependent downstream delegations

**Domain:** Delegation and Authority  
**Requirement:** Revocation of upstream authority shall invalidate dependent downstream delegations.  
**Objective:** Prevent orphaned authority.  
**Applicability:** Delegating agents and multi-agent workflows.  
**Testing Procedure:** Test upstream revocation and downstream invalidation.  
**Evidence Examples:** Revocation test; policy logs; token invalidation records.  
**Maturity:** Required

### AAEF-AUZ-01: High-impact actions shall be authorized at the point of execution

**Domain:** Action Authorization  
**Requirement:** High-impact actions shall be authorized at the point of execution.  
**Objective:** Prevent model output from becoming unchecked action.  
**Applicability:** High-impact actions.  
**Testing Procedure:** Test attempted action at execution boundary.  
**Evidence Examples:** Authorization policy; decision logs; denial records.  
**Maturity:** Required

### AAEF-AUZ-02: Authorization decisions shall evaluate requested purpose and target resource

**Domain:** Action Authorization  
**Requirement:** Authorization decisions shall evaluate requested purpose and target resource.  
**Objective:** Prevent purpose/resource mismatch.  
**Applicability:** High-impact actions with resource access.  
**Testing Procedure:** Review policy inputs and sample decisions.  
**Evidence Examples:** Authorization logs; policy definitions.  
**Maturity:** Required

### AAEF-AUZ-03: High-risk and critical actions shall require explicit approval or additional verification

**Domain:** Action Authorization  
**Requirement:** High-risk and critical actions shall require explicit approval or additional verification.  
**Objective:** Apply risk-proportional friction.  
**Applicability:** High-risk and critical actions.  
**Testing Procedure:** Review approval threshold and sampled approvals.  
**Evidence Examples:** Approval records; risk rules; UI screenshots.  
**Maturity:** Required

### AAEF-AUZ-04: If authority, principal, or purpose cannot be determined, high-impact actions shall be denied or escalated

**Domain:** Action Authorization  
**Requirement:** If authority, principal, or purpose cannot be determined, high-impact actions shall be denied or escalated.  
**Objective:** Fail safe on ambiguity.  
**Applicability:** High-impact actions.  
**Testing Procedure:** Test missing/ambiguous authority cases.  
**Evidence Examples:** Test results; decision logs.  
**Maturity:** Required

### AAEF-AUZ-05: Authorization decisions for high-impact actions shall be based on trusted policy inputs and system state, not on untrusted natural-language content alone.

**Domain:** Action Authorization  
**Requirement:** Authorization decisions for high-impact actions shall be based on trusted policy inputs and system state, not on untrusted natural-language content alone.  
**Objective:** Ensure that authorization decisions are made by the policy and authorization layer using trusted inputs and system state, rather than allowing untrusted natural-language content to change authority, purpose, resource, or approval requirements.  
**Applicability:** High-impact actions influenced by prompts, retrieved content, documents, messages, web pages, or external content.  
**Testing Procedure:** Test whether malicious instructions embedded in external content can alter authorization decisions, change policy inputs, modify risk classification, or bypass approval requirements.  
**Evidence Examples:** Authorization policy; prompt-injection test results; decision logs; trusted input definitions.  
**Maturity:** Required

### AAEF-TOOL-01: Tools available to agents shall be configured with minimum authority necessary

**Domain:** Tool and Action Boundary  
**Requirement:** Tools available to agents shall be configured with minimum authority necessary.  
**Objective:** Limit blast radius.  
**Applicability:** Tool-using agents.  
**Testing Procedure:** Review tool permissions and compare to business need.  
**Evidence Examples:** Tool permission matrix; API scopes.  
**Maturity:** Required

### AAEF-TOOL-02: Tool invocation shall be governed by explicit policy rather than model output alone

**Domain:** Tool and Action Boundary  
**Requirement:** Tool invocation shall be governed by explicit policy rather than model output alone.  
**Objective:** Prevent prompt-driven tool misuse.  
**Applicability:** Tool-using agents.  
**Testing Procedure:** Review enforcement point between model and tool.  
**Evidence Examples:** Policy engine config; invocation logs.  
**Maturity:** Required

### AAEF-TOOL-03: Tools capable of external communication, payment, deletion, privilege change, code execution, or sensitive data export shall be classified as high-risk

**Domain:** Tool and Action Boundary  
**Requirement:** Tools capable of external communication, payment, deletion, privilege change, code execution, or sensitive data export shall be classified as high-risk.  
**Objective:** Ensure risky tools receive stronger controls.  
**Applicability:** Agents with powerful tools.  
**Testing Procedure:** Review tool classification and controls.  
**Evidence Examples:** Tool registry; risk classification.  
**Maturity:** Required

### AAEF-TOOL-04: Tool invocation requests derived from untrusted or external content shall be subject to intent validation and policy checks before execution.

**Domain:** Tool and Action Boundary  
**Requirement:** Tool invocation requests derived from untrusted or external content shall be subject to intent validation and policy checks before execution.  
**Objective:** Ensure that the tool dispatch layer does not execute tool calls merely because untrusted content caused the model to request them; derived tool requests must still pass intent validation and action-boundary policy checks.  
**Applicability:** Agents that process external content and can invoke tools or APIs.  
**Testing Procedure:** Inject tool-use instructions into external content and verify that the tool dispatch layer denies, escalates, or requires approval unless the requested tool use is independently authorized.  
**Evidence Examples:** Tool invocation policy; test cases; denial logs; approval records.  
**Maturity:** Required

### AAEF-MEM-01: Systems shall control what information agents may write to persistent memory

**Domain:** Memory and Retrieval  
**Requirement:** Systems shall control what information agents may write to persistent memory.  
**Objective:** Prevent memory poisoning and retention abuse.  
**Applicability:** Agents with persistent memory.  
**Testing Procedure:** Review memory write policy and examples.  
**Evidence Examples:** Memory policy; write logs; retention rules.  
**Maturity:** Required

### AAEF-MEM-02: Retrieval sources shall be assigned trust levels or provenance metadata where feasible

**Domain:** Memory and Retrieval  
**Requirement:** Retrieval sources shall be assigned trust levels or provenance metadata where feasible.  
**Objective:** Avoid trust confusion in retrieval.  
**Applicability:** RAG-enabled agents.  
**Testing Procedure:** Review data source registry and trust metadata.  
**Evidence Examples:** Source registry; provenance labels; retrieval logs.  
**Maturity:** Recommended

### AAEF-MEM-03: External content retrieved from documents, web pages, messages, tickets, or emails shall not be treated as trusted instruction by default

**Domain:** Memory and Retrieval  
**Requirement:** External content retrieved from documents, web pages, messages, tickets, or emails shall not be treated as trusted instruction by default.  
**Objective:** Reduce indirect prompt injection impact.  
**Applicability:** Agents processing external content.  
**Testing Procedure:** Test indirect prompt injection scenarios.  
**Evidence Examples:** Prompt handling policy; test results.  
**Maturity:** Required

### AAEF-MEM-04: For high-impact actions, retrieved or remembered content that materially influenced the action shall preserve provenance or trust metadata.

**Domain:** Memory and Retrieval  
**Requirement:** For high-impact actions, retrieved or remembered content that materially influenced the action shall preserve provenance or trust metadata.  
**Objective:** Support review of whether untrusted, low-trust, or poisoned content influenced a high-impact agentic action.  
**Applicability:** High-impact actions performed by RAG-enabled agents, agents with persistent memory, or agents using external content.  
**Testing Procedure:** Review whether action evidence can identify retrieved or remembered content sources that materially influenced the high-impact action.  
**Evidence Examples:** Retrieval logs; source provenance metadata; memory records; content references; action evidence references.  
**Maturity:** Required

### AAEF-EVD-01: High-impact actions shall generate evidence sufficient to reconstruct what happened

**Domain:** Evidence and Auditability  
**Requirement:** High-impact actions shall generate evidence sufficient to reconstruct what happened.  
**Objective:** Support audit and response.  
**Applicability:** High-impact actions.  
**Testing Procedure:** Review action evidence for completeness.  
**Evidence Examples:** Action logs; event records; trace IDs.  
**Maturity:** Required

### AAEF-EVD-02: Evidence for high-impact actions shall include agent identity, agent instance, principal, requested action, resource, authority scope, authorization decision, timestamp, and result

**Domain:** Evidence and Auditability  
**Requirement:** Evidence for high-impact actions shall include agent identity, agent instance, principal, requested action, resource, authority scope, authorization decision, timestamp, and result.  
**Objective:** Standardize evidence quality.  
**Applicability:** High-impact actions.  
**Testing Procedure:** Sample evidence records and verify required fields.  
**Evidence Examples:** Structured logs; evidence event records.  
**Maturity:** Required

### AAEF-EVD-03: Where human approval is required, approval evidence shall be linked to the action evidence

**Domain:** Evidence and Auditability  
**Requirement:** Where human approval is required, approval evidence shall be linked to the action evidence.  
**Objective:** Connect approval and execution.  
**Applicability:** Actions requiring human approval.  
**Testing Procedure:** Trace approval to executed action.  
**Evidence Examples:** Approval ID; workflow record; action event.  
**Maturity:** Required

### AAEF-EVD-04: Critical action evidence should be protected against undetected alteration

**Domain:** Evidence and Auditability  
**Requirement:** Critical action evidence should be protected against undetected alteration.  
**Objective:** Improve evidence reliability.  
**Applicability:** Critical actions.  
**Testing Procedure:** Review tamper-evidence mechanisms.  
**Evidence Examples:** Signed logs; append-only log; integrity checks.  
**Maturity:** Recommended

### AAEF-HUM-01: Human approval requests shall clearly present the agent, principal, requested action, resource, purpose, risk level, and consequence

**Domain:** Human Oversight  
**Requirement:** Human approval requests shall clearly present the agent, principal, requested action, resource, purpose, risk level, and consequence.  
**Objective:** Enable informed approval.  
**Applicability:** Approval workflows.  
**Testing Procedure:** Review approval UI and sampled records.  
**Evidence Examples:** Approval screenshots; approval records.  
**Maturity:** Required

### AAEF-HUM-02: Approval workflows shall be designed to reduce blind approval and approval fatigue

**Domain:** Human Oversight  
**Requirement:** Approval workflows shall be designed to reduce blind approval and approval fatigue.  
**Objective:** Prevent ineffective oversight.  
**Applicability:** Frequent approval workflows.  
**Testing Procedure:** Review batching, thresholds, and UX patterns.  
**Evidence Examples:** Approval metrics; UX design; policy.  
**Maturity:** Recommended

### AAEF-RES-01: Organizations shall be able to revoke agent authority, tool access, credentials, and active delegations

**Domain:** Response and Revocation  
**Requirement:** Organizations shall be able to revoke agent authority, tool access, credentials, and active delegations.  
**Objective:** Stop risky or compromised agents.  
**Applicability:** Production agents.  
**Testing Procedure:** Test revocation path.  
**Evidence Examples:** Revocation logs; access config; test evidence.  
**Maturity:** Required

### AAEF-RES-02: Organizations shall be able to isolate agent instances or workflows when compromise, poisoning, or unauthorized behavior is suspected

**Domain:** Response and Revocation  
**Requirement:** Organizations shall be able to isolate agent instances or workflows when compromise, poisoning, or unauthorized behavior is suspected.  
**Objective:** Contain incidents.  
**Applicability:** Production agents and workflows.  
**Testing Procedure:** Review isolation procedure and test where possible.  
**Evidence Examples:** Incident playbook; isolation test results.  
**Maturity:** Required

### AAEF-RES-03: Organizations shall be able to reconstruct the sequence of high-impact agentic actions during incident review

**Domain:** Response and Revocation  
**Requirement:** Organizations shall be able to reconstruct the sequence of high-impact agentic actions during incident review.  
**Objective:** Support investigation and accountability.  
**Applicability:** High-impact agentic workflows.  
**Testing Procedure:** Perform reconstruction from evidence samples.  
**Evidence Examples:** Incident reconstruction report; logs; timeline.  
**Maturity:** Required
