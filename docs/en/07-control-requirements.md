# 07. Control Requirements

This section provides AAEF control requirements.

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

## Requirements

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

### AAEF-PRN-02: Principal context shall be preserved and remain valid, current, bounded, and semantically connected across tool calls, workflow steps, delegations, long-running workflows, and reauthorization paths

**Domain:** Principal Binding
**Maturity:** Required

**Requirement:** Principal context shall be preserved and remain valid, current, bounded, and semantically connected across tool calls, workflow steps, delegations, long-running workflows, and reauthorization paths.
**Objective:** Prevent loss of accountability and degraded, stale, broadened, or ambiguous authority context across workflows.
**Applicability:** Tool-using, delegating, long-running, asynchronous, reauthorization, or cross-domain agentic workflows.
**Testing Procedure:** Trace sample workflows end-to-end and verify that principal context is preserved, remains valid and bounded, or is explicitly refreshed, reconfirmed, reauthorized, denied, or escalated when degraded.
**Evidence Examples:** Trace logs; correlation IDs; trace IDs; session-scoped authority tokens; signed principal claims; delegation records; context refresh records; principal reconfirmation records; reauthorization records; non-execution evidence.

**Implementation Note:** Principal context propagation is not automatic in stateless API chains, asynchronous workflows, queues, background jobs, long-running sessions, reauthorization flows, or multi-agent delegation.

Implementations should use explicit propagation mechanisms such as correlation IDs, trace IDs, session-scoped authority tokens, signed claims, workflow metadata, structured delegation records, or equivalent authority references.

Preserved principal context should not be treated as sufficient when it is stale, ambiguous, broadened, semantically distant from the requested action, or no longer tied to the original authority basis. If principal context cannot be preserved, validated, refreshed, reconfirmed, or reauthorized, high-impact actions should be denied, deferred, or escalated.

For the related v0.5.0 planning concept, see `docs/en/30-principal-context-degradation.md`.


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

### AAEF-DEL-05: Systems shall preserve sufficient delegation lineage metadata to reconstruct upstream and downstream authority decisions for high-impact actions, without requiring a specific graph database or tracing implementation

**Domain:** Delegation and Authority  
**Requirement:** Systems shall preserve sufficient delegation lineage metadata to reconstruct upstream and downstream authority decisions for high-impact actions, without requiring a specific graph database or tracing implementation.  
**Objective:** Enable reconstruction of how authority moved from principals or upstream agents to downstream agents, tools, workflows, and actions.  
**Applicability:** Multi-step, multi-agent, delegated, or workflow-based systems where high-impact actions may be caused by upstream or downstream authority transfers.  
**Testing Procedure:** Trace representative delegated workflows end-to-end and verify that principal, upstream action, downstream agent, delegated scope, constraints, decision points, and resulting high-impact actions can be reconstructed from evidence.  
**Evidence Examples:** Delegation chain ID; parent action ID; lineage node ID; upstream agent ID; downstream agent ID; delegated scope; constraints; correlation ID; trace ID; downstream action IDs.  
**Maturity:** Required

**Implementation Note:** AAEF requires reconstructability, not a specific graph database, tracing tool, or workflow engine. A chain, graph, trace, or external evidence system may be acceptable if it preserves sufficient references for review and incident reconstruction.

**Implementation Note:** Delegation lineage should help identify where authority was granted, where it was attenuated, whether constraints were preserved, which node performed the final action, and which downstream actions may require revocation or isolation.

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

### AAEF-AUZ-05: Authorization decisions for high-impact actions shall be based on trusted policy inputs and system state, not on untrusted natural-language content alone

**Domain:** Action Authorization  
**Requirement:** Authorization decisions for high-impact actions shall be based on trusted policy inputs and system state, not on untrusted natural-language content alone.  
**Objective:** Ensure that authorization decisions are made by the policy and authorization layer using trusted inputs and system state, rather than allowing untrusted natural-language content to change authority, purpose, resource, or approval requirements.  
**Applicability:** High-impact actions influenced by prompts, retrieved content, documents, messages, web pages, or external content.  
**Testing Procedure:** Test whether malicious instructions embedded in external content can alter authorization decisions, change policy inputs, modify risk classification, or bypass approval requirements.  
**Evidence Examples:** Authorization policy; prompt-injection test results; decision logs; trusted input definitions.  
**Maturity:** Required

### AAEF-AUZ-06: High-impact actions shall evaluate intent-authority alignment using trusted workflow context, structured authority grants, machine-enforceable policy references, or trusted constraints where feasible; intent alignment shall not rely solely on model self-assessment or agent-inferred purpose

**Domain:** Action Authorization  
**Requirement:** High-impact actions shall evaluate intent-authority alignment using trusted workflow context, structured authority grants, machine-enforceable policy references, or trusted constraints where feasible; intent alignment shall not rely solely on model self-assessment or agent-inferred purpose.  
**Objective:** Prevent semantically plausible actions from violating the principal intent or policy context under which authority was granted.  
**Applicability:** High-impact actions where intent, purpose, policy, workflow context, or organizational constraints affect execution appropriateness.  
**Testing Procedure:** Review sample high-impact actions and verify that intent alignment uses trusted policy references, workflow context, structured authority grants, or trusted constraints; test whether LLM-generated purpose or untrusted content alone can cause authorization to pass.  
**Evidence Examples:** Policy reference; workflow context ID; authority grant; trusted constraint record; intent alignment decision; alignment rationale; test results showing model self-assessment alone is insufficient.  
**Maturity:** Required

**Implementation Note:** Human-readable principal intent and model-generated purpose can support review, explanation, or escalation, but they should not be the sole source of high-impact authorization. Runtime authorization should prefer machine-enforceable policy references, structured authority grants, trusted workflow context, trusted system state, or explicit organizational constraints where feasible.

**Implementation Note:** Agent-inferred purpose is advisory unless it is bound to a trusted workflow, policy reference, or authority grant. This avoids circular reliance on the same model whose action is being authorized.

### AAEF-AUZ-07: High-impact actions shall evaluate material runtime state from defined trusted state sources before execution where environmental, operational, revocation, or risk conditions can affect authorization

**Domain:** Action Authorization  
**Requirement:** High-impact actions shall evaluate material runtime state from defined trusted state sources before execution where environmental, operational, revocation, or risk conditions can affect authorization.  
**Objective:** Prevent stale or unsafe execution when conditions have changed since authority was granted.  
**Applicability:** High-impact actions whose safety or authorization depends on current state, such as incident state, system health, inventory state, fraud risk, account state, market conditions, or revocation state.  
**Testing Procedure:** Review state-dependent authorization policies and test that defined state changes can deny, defer, escalate, freeze authority, or require additional verification before execution.  
**Evidence Examples:** Trusted state source references; state snapshot ID; state check timestamp; conditional policy reference; revocation state check; decision logs.  
**Maturity:** Required

**Implementation Note:** AAEF does not require a specific state provider or external API. Organizations should define which runtime states are material for each high-impact action category and should identify which state sources are trusted for authorization.

### AAEF-AUZ-08: High-impact actions shall be denied, deferred, or escalated when material deterministic or semantic ambiguity exists in authority, principal intent, runtime state, input trust, policy applicability, or evidence requirements; ambiguity resolution shall not rely solely on model self-assessment

**Domain:** Action Authorization  
**Requirement:** High-impact actions shall be denied, deferred, or escalated when material deterministic or semantic ambiguity exists in authority, principal intent, runtime state, input trust, policy applicability, or evidence requirements; ambiguity resolution shall not rely solely on model self-assessment.  
**Objective:** Ensure that authority is treated as necessary but not sufficient for execution under material uncertainty.  
**Applicability:** High-impact actions where ambiguity or uncertainty may materially affect execution appropriateness.  
**Testing Procedure:** Test deterministic ambiguity such as missing principal, missing authority scope, missing policy reference, unknown revocation state, unresolved input trust, and missing evidence; test semantic ambiguity such as unclear intent or purpose-policy mismatch; verify that a model assertion of no ambiguity does not override missing trusted inputs.  
**Evidence Examples:** Ambiguity decision logs; ambiguity type; escalation records; non-execution evidence; denial reason; evidence gap records; trusted input resolution records.  
**Maturity:** Required

**Implementation Note:** This control extends AAEF-AUZ-04. AAEF-AUZ-04 focuses on ambiguity in authority, principal, or purpose. AAEF-AUZ-08 covers broader material ambiguity, including runtime state, input trust, policy applicability, and evidence requirements.

**Implementation Note:** LLM-assisted ambiguity detection may help identify uncertainty, but the model should not be the only component allowed to clear ambiguity for high-impact actions. Deterministic ambiguity should be resolved by trusted system state, policy references, authority records, evidence availability, or independent runtime checks.

### AAEF-AUZ-09: Systems shall define safe handling for denied, deferred, escalated, retried, or reauthorization-required high-impact actions

**Domain:** Action Authorization
**Requirement:** Systems shall define safe handling for high-impact actions that are denied, deferred, escalated, retried, or require reauthorization due to insufficient authority, material ambiguity, state change, principal context degradation, or missing evidence, including scoped reauthorization, retry control, task splitting detection, and safe termination.
**Objective:** Prevent authority denial from becoming a bypass path through repeated retries, scope creep, unsafe reauthorization, tool switching, or task splitting.
**Applicability:** Systems where agents may request additional authority, retry actions, escalate actions, continue workflows after denial, or encounter degraded principal context before high-impact execution.
**Testing Procedure:** Review denial and reauthorization workflows and test that denied, deferred, escalated, retried, or reauthorization-required actions are safely handled, linked to the original action, scoped to principal intent and policy constraints, and unable to bypass prior denials through repeated retries, scope creep, alternate tools, or task splitting.
**Evidence Examples:** Denial records; non-execution evidence; reauthorization request; requested additional scope; escalation target; retry count; principal reconfirmation record; linked action ID; task splitting correlation; safe termination record.
**Maturity:** Required

**Implementation Note:** Denial, deferral, escalation, and reauthorization are control outcomes, not application errors. A denied action should not become an alternate path to execution through retries, prompt reformulation, alternate tools, broader approval requests, or decomposition into smaller actions.

Reauthorization should create a new scoped decision linked to the original denied or deferred action. It should not silently mutate the original denial or broaden authority beyond the requested and approved scope.

For the related v0.5.0 planning concept, see `docs/en/32-authority-denial-reauthorization-flow.md`.


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

### AAEF-TOOL-04: Tool invocation requests derived from untrusted or external content shall be subject to intent validation and policy checks before execution

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

### AAEF-MEM-04: For high-impact actions, retrieved or remembered content that materially influenced the action shall preserve provenance or trust metadata

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

### AAEF-EVD-05: Systems should record structured evidence for non-executed high-impact actions

**Domain:** Evidence and Auditability
**Requirement:** Systems should record structured evidence for denied, deferred, escalated, frozen, safely terminated, or otherwise non-executed high-impact actions where non-execution was caused by authority gaps, material ambiguity, state changes, principal context degradation, input trust gaps, policy uncertainty, or evidence gaps.
**Objective:** Make non-execution decisions reviewable so that denial, deferral, escalation, freeze, and safe termination can be audited, correlated, and improved.
**Applicability:** High-impact actions that are blocked, deferred, escalated, frozen, denied, or safely terminated before execution.
**Testing Procedure:** Review denied, deferred, escalated, frozen, and safely terminated high-impact action samples and verify that non-execution reason, ambiguity type, authority gap, principal context issue, escalation target, linked action context, and final non-execution outcome are recorded.
**Evidence Examples:** Non-execution decision; denial reason; ambiguity type; authority gap; principal context issue; state gap; policy gap; evidence gap; escalation target; linked action ID; safe termination record.
**Maturity:** Recommended

**Implementation Note:** Non-execution evidence is important because safe denial and safe termination are security-relevant outcomes. Evidence should support review of why execution did not proceed, what condition triggered non-execution, and whether related retries or reauthorization requests were later attempted.


### AAEF-EVD-06: Systems should record structured evidence for reauthorization and additional authority requests

**Domain:** Evidence and Auditability
**Requirement:** Systems should record structured evidence for reauthorization requests, additional scope requests, principal reconfirmation, retry decisions, and escalation decisions related to denied, deferred, or reauthorization-required high-impact actions.
**Objective:** Ensure that reauthorization does not become an unevidenced bypass path and that additional authority requests remain attributable, scoped, linked to prior denial or deferral, and reviewable.
**Applicability:** Systems where agents can request additional authority, ask for renewed approval, retry denied actions, request principal reconfirmation, or escalate blocked workflows.
**Testing Procedure:** Review reauthorization flows and verify that requested additional scope, approver or escalation target, principal reconfirmation, retry count, decision outcome, and linkage to the denied or deferred action are recorded and cannot silently broaden authority.
**Evidence Examples:** Reauthorization request ID; denied action ID; requested additional scope; approver or escalation target; principal reconfirmation; retry count; reauthorization decision; post-reauthorization effective scope.
**Maturity:** Recommended

**Implementation Note:** Reauthorization evidence should make clear what additional authority was requested, why it was requested, who or what approved it, what scope was granted, and how the new decision relates to the original denial or deferral.

For the related v0.5.0 planning concept, see `docs/en/32-authority-denial-reauthorization-flow.md`.


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

### AAEF-RES-04: Systems shall define and test conditional authority freeze behavior for high-impact workflows, including future-action denial, in-flight action handling, downstream delegation propagation, and evidence of freeze decisions; AAEF does not assume instantaneous global revocation in distributed systems

**Domain:** Response and Revocation  
**Requirement:** Systems shall define and test conditional authority freeze behavior for high-impact workflows, including future-action denial, in-flight action handling, downstream delegation propagation, and evidence of freeze decisions; AAEF does not assume instantaneous global revocation in distributed systems.  
**Objective:** Enable conditional freeze or revocation while making revocation scope, propagation, in-flight behavior, and residual risk explicit.  
**Applicability:** High-impact workflows with state-dependent authority, dynamic risk signals, active delegations, distributed execution, or time-sensitive revocation requirements.  
**Testing Procedure:** Test defined state or risk triggers and verify that affected authority grants, delegations, tool access, workflows, and in-flight actions are frozen, denied, escalated, isolated, or revoked according to documented behavior.  
**Evidence Examples:** Authority freeze record; revocation log; state trigger evidence; affected delegation IDs; in-flight action handling record; propagation record; incident or escalation record.  
**Maturity:** Required

**Implementation Note:** AAEF requires revocation and freeze behavior to be defined, evidenced, and testable. It does not assume instantaneous global revocation in distributed or asynchronous systems.

**Implementation Note:** Implementations should distinguish future-action denial, in-flight action handling, downstream delegation propagation, partial authority freeze, and incident isolation where applicable.


