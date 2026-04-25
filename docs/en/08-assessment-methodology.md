# 08. Assessment Methodology

AAEF assessments should determine whether an organization can govern high-impact agentic actions through authority, action boundaries, evidence, and revocation.

## Assessment Objectives

An AAEF assessment should answer:

1. Are agentic AI systems inventoried and governed?
2. Are high-impact actions defined?
3. Are agents and agent instances identifiable?
4. Are agent actions bound to principals?
5. Is delegated authority explicit and attenuated?
6. Are actions authorized at the point of execution?
7. Are high-risk tools governed by policy?
8. Is evidence generated for high-impact actions?
9. Can trust and authority be revoked?
10. Can incidents be reconstructed?

## Assessment Methods

AAEF assessment may include:

- document review,
- architecture review,
- configuration review,
- identity and token review,
- delegation policy review,
- authorization policy review,
- tool permission review,
- memory and retrieval design review,
- evidence and logging review,
- approval workflow review,
- incident response review,
- interviews,
- and scenario-based testing.

## Evidence Review

Assessors should request evidence such as:

- agent inventory,
- risk classification,
- ownership records,
- authority grant records,
- delegation chain records,
- authorization policies,
- tool access policies,
- approval records,
- action evidence logs,
- revocation records,
- incident response records,
- and test results.

## Scenario-Based Testing

Scenario tests should include at least:

- attempted high-impact action without authority,
- attempted action with expired delegation,
- attempted downstream delegation beyond allowed scope,
- attempted tool invocation based on indirect prompt injection,
- attempted task splitting to avoid approval,
- attempted action with missing principal binding,
- attempted use of untrusted retrieved content as instruction,
- revocation of an agent and dependent delegations,
- reconstruction of a high-impact action from evidence.

## Assessment Outcomes

Assessment findings may be categorized as:

- **Conformant**: The control is implemented and evidence supports operation.
- **Partially Conformant**: The control exists but has gaps in scope, enforcement, evidence, or consistency.
- **Non-Conformant**: The control is not implemented or cannot be demonstrated.
- **Not Applicable**: The control does not apply to the assessed system, with rationale.
- **Not Tested**: The control was not assessed.

## Maturity View

AAEF uses the following maturity levels consistently across the framework:

- **Level 0: Experimental** — sandbox or non-production agent use only.
- **Level 1: Assisted** — the agent assists humans but does not independently execute high-impact actions.
- **Level 2: Tool-Governed** — the agent can call approved tools under explicit policy and evidence controls.
- **Level 3: Delegation-Governed** — the agent can delegate tasks under attenuated delegation, depth limits, revocation, and evidence requirements.
- **Level 4: High-Impact Action Assured** — the agent can perform high-impact actions only under strict authority, action-boundary authorization, risk-based approval, evidence, monitoring, and revocation controls.

The maturity level should reflect both technical enforcement and evidence quality.

Assessors should be cautious with Level 4 claims. If principal context cannot be preserved, authority cannot be bounded, action-boundary authorization cannot be enforced, or evidence cannot support incident reconstruction, the system should not be considered Level 4.
