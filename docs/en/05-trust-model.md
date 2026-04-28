# 05. Trust Model

AAEF treats trust as an operational state that must be explicit, bounded, evidenced, and revocable.

It does not treat trust as a static property of a model, vendor, agent, or system.

## Trust Components

AAEF defines the following trust components.

### Agent Identity

The system must identify which agent product and agent instance attempted or performed an action.

### Principal Binding

The system must identify the human, organization, system, or upstream agent on whose behalf the agent acted.

### Operator Accountability

The system must identify the person or organization responsible for deploying, configuring, or governing the agent.

### Delegated Authority

The system must define what authority was granted to the agent, by whom, under what conditions, for what purpose, and for how long.

### Authorization at Action Boundary

The system must evaluate whether the attempted action is allowed at the point of execution.

### Evidence

The system must generate and retain evidence sufficient to verify the action, authority, authorization decision, approval, result, and relevant context.

### Revocation

The system must support withdrawal of trust, authority, credentials, tool access, memory access, and downstream delegations.

## Trust Flow

A simplified AAEF trust flow is:

1. A principal gives an instruction or authority grant to an agent.
2. The agent operates within an identified runtime and context.
3. The agent may request to perform an action.
4. The action boundary evaluates identity, principal binding, authority scope, purpose, resource, risk, approval requirements, and revocation state.
5. The action is allowed, denied, escalated, or sent for human approval.
6. Evidence is generated.
7. Downstream delegations or results are recorded.
8. Trust may be reviewed, limited, or revoked.

## Trust Is Not Binary

AAEF does not assume that an agent is simply trusted or untrusted.

Trust may vary by:

- action type,
- resource,
- purpose,
- principal,
- runtime,
- risk level,
- evidence quality,
- approval status,
- historical behavior,
- and revocation state.

## Trust Domains

Organizations should define trust domains for agentic AI systems.

A trust domain may represent:

- an organization,
- tenant,
- business unit,
- workflow,
- platform,
- environment,
- data boundary,
- or authority issuer.

Cross-domain agent actions require explicit trust assumptions and additional evidence.


## Implementation Note: Principal Context Propagation

Principal binding is straightforward in a single synchronous application, but it becomes difficult in stateless API chains, asynchronous workflows, tool calls, queues, background jobs, and multi-agent delegation.

AAEF does not mandate a specific implementation mechanism. However, systems should preserve principal context through explicit propagation mechanisms such as signed claims, workflow metadata, correlation identifiers, session-bound authority grants, trace context, or structured delegation records.

If a system cannot preserve principal context across a workflow, high-impact actions in that workflow should be denied, escalated, or treated as unauthenticated authority use.

For v0.5.0 planning, AAEF also tracks Principal Context Degradation: cases where principal context is technically present but stale, ambiguous, semantically distant, or no longer sufficient for the requested high-impact action. See `docs/en/30-principal-context-degradation.md`.

## Action Assurance Levels

AAEF uses one maturity model across the framework.

### Level 0: Experimental

The agent is used only in sandbox, research, or non-production environments. It has no access to high-impact tools, sensitive data, external actions, or production systems.

### Level 1: Assisted

The agent assists humans but cannot independently perform high-impact actions. The human remains the effective action executor.

### Level 2: Tool-Governed

The agent can call approved tools under explicit policy controls, minimum authority, and evidence requirements. High-impact actions require approval or are not permitted.

### Level 3: Delegation-Governed

The agent can delegate tasks to other agents, services, or workflows, subject to attenuated delegation, delegation depth limits, revocation, and evidence requirements.

### Level 4: High-Impact Action Assured

The agent can perform high-impact actions only under strict authority, action-boundary authorization, risk-based approval, verifiable evidence, monitoring, revocation, and incident reconstruction controls.

## Level 4 Caution

Level 4 should be treated as exceptional.

Organizations should not deploy Level 4 agentic systems unless they can demonstrate, at minimum:

- complete inventory and ownership,
- reliable agent and agent-instance identity,
- principal binding across the full workflow,
- explicit and attenuated authority grants,
- action-boundary authorization,
- human approval for high-risk or critical actions,
- verifiable evidence for high-impact actions,
- revocation of active and downstream authority,
- isolation procedures for compromised or poisoned agents,
- incident reconstruction capability,
- and periodic review of action outcomes and evidence quality.

If these conditions cannot be met, the system should remain at Level 1, Level 2, or Level 3 depending on its actual control maturity. AAEF should not be used to justify granting autonomy before the organization can govern the resulting actions.
