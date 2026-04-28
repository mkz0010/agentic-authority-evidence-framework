# 04. Threat Model

AAEF organizes threats around agentic action assurance.

The purpose of this threat model is not to catalog every possible AI risk. It is to identify threats that affect delegated authority, action boundaries, verifiable evidence, and revocable trust.

## T1: Identity and Authentication Threats

These threats affect the ability to determine who or what acted.

Examples:

- ghost agent impersonation,
- agent identity spoofing,
- agent instance confusion,
- issuer spoofing,
- cross-tenant agent confusion,
- stale or expired agent credentials,
- token audience confusion,
- credential passthrough abuse,
- use of unregistered or unapproved agents.

## T2: Principal Binding Threats

These threats affect the ability to determine on whose behalf an agent acted.

Examples:

- ambiguous principal binding,
- shared service account misuse,
- agent acting without a clear human or organizational principal,
- cross-user context confusion,
- agent action incorrectly attributed to the wrong user,
- loss of principal context across tool calls or delegations.

## T3: Delegation and Authority Threats

These threats affect whether an agent acted within delegated authority.

Examples:

- delegation chain escalation,
- overbroad authority grants,
- unbounded redelegation,
- excessive delegation depth,
- purpose drift,
- scope laundering,
- approval laundering,
- task splitting to avoid approval thresholds,
- stale delegation reuse,
- failure to revoke downstream delegations.

## T4: Prompt and Intent Manipulation Threats

These threats affect agent reasoning and action intent.

Examples:

- direct prompt injection,
- indirect prompt injection through documents, web pages, emails, or tickets,
- instruction smuggling,
- policy override manipulation,
- human approval manipulation,
- tool-intent mismatch,
- malicious reinterpretation of user intent,
- agent persuasion or social engineering.

## T5: Tool and Action Boundary Threats

These threats affect the boundary where model output becomes real action.

Examples:

- tool misuse,
- unauthorized tool invocation,
- action execution without policy enforcement,
- external communication abuse,
- destructive command execution,
- payment or purchase order abuse,
- privilege modification abuse,
- browser automation data exfiltration,
- high-risk action performed without approval.

## T6: Memory and Retrieval Threats

These threats affect the information agents use to make decisions.

Examples:

- memory poisoning,
- vector store poisoning,
- retrieval manipulation,
- trust tier confusion,
- shadow memory,
- retention abuse,
- cross-session contamination,
- use of untrusted retrieved content as instruction,
- poisoned data reused across agent workflows.

## T7: Multi-Agent and A2A Threats

These threats affect chains of agents and inter-agent collaboration.

For v0.5.0 planning, see `docs/en/31-cross-agent-cross-domain-authority.md` for the Cross-Agent and Cross-Domain Authority concept note.

Examples:

- rogue agent participation,
- agent collusion,
- delegation cascade,
- cross-agent prompt propagation,
- capability discovery abuse,
- consensus manipulation,
- swarm denial of service,
- untraceable sub-agent execution,
- loss of responsibility across agent chains.

## T8: Evidence and Auditability Threats

These threats affect the ability to prove what happened.

Examples:

- missing action evidence,
- incomplete authority records,
- unverifiable logs,
- log tampering,
- missing approval evidence,
- denial of agentic action,
- loss of delegation chain history,
- inability to reconstruct incident scope,
- evidence overcollection that creates privacy risk.

## T9: Revocation and Response Threats

These threats affect the ability to stop, isolate, or recover from agentic risk.

Examples:

- inability to revoke delegated authority,
- failure to revoke downstream delegations,
- delayed trust revocation,
- orphaned agent instances,
- persistent poisoned memory,
- unisolated compromised tool access,
- inability to quarantine agent workflows,
- incomplete incident impact tracing.
