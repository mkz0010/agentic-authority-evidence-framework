# 00. Introduction

## Why AAEF Matters

Agentic AI changes the security question.

Traditional AI risk management often asks whether a model is accurate, safe, explainable, aligned, or trustworthy. These questions remain important, but they are not sufficient for agentic AI systems.

An AI agent does not merely generate outputs. It may interpret instructions, call tools, access data, delegate tasks, interact with other agents, and act on behalf of a human or an organization.

When an AI agent can take action, the central question is no longer only:

> Is the model trustworthy?

The operational question becomes:

> Was this action authorized, bounded, attributable, and evidenced?

AAEF exists to answer that question.

The **Agentic Authority & Evidence Framework (AAEF)** focuses on delegated authority, policy-enforced action boundaries, and verifiable evidence. It treats AI agents as non-human actors that may exercise authority within an organization, and therefore must be governed through controls that are explicit, enforceable, auditable, and revocable.

AAEF does not assume that AI agents will always reason correctly. It assumes that agents may misunderstand instructions, be manipulated by prompt injection, over-delegate authority, misuse tools, retain poisoned memory, or propagate risk through multi-agent workflows.

For that reason, AAEF does not place trust in model output alone.

Instead, AAEF requires trust to be established through:

- verifiable agent identity,
- clear principal binding,
- attenuated delegation,
- policy-enforced authorization at the point of action,
- risk-based human approval,
- verifiable evidence,
- and revocable trust.

AAEF is not a replacement for AI governance frameworks, Zero Trust frameworks, identity protocols, or agent communication standards. It is a complementary control profile focused on the practical assurance questions that arise when AI agents are allowed to act.

## The Core Question

AAEF helps organizations answer five questions:

1. **Who or what acted?**
2. **On whose behalf did it act?**
3. **What authority did it have?**
4. **Was the action allowed at the point of execution?**
5. **What evidence proves what happened?**

If an organization cannot answer these questions, it cannot reliably govern agentic AI in production.

If it can answer them, it can allow AI agents to operate with greater autonomy while keeping authority bounded, actions attributable, evidence verifiable, and trust revocable.

## AAEF in One Sentence

AAEF shifts agentic AI security from **trusting model behavior** to **governing authorized action**.

## Action Assurance

AAEF defines **action assurance** as the ability to verify that an agentic action was:

- performed by an identified agent or agent instance,
- bound to a human, organization, or upstream principal,
- within delegated authority,
- authorized at the point of execution,
- recorded with sufficient evidence,
- and subject to revocation, review, and response.

Action assurance is especially important when AI agents perform high-impact actions such as:

- sending external communications,
- accessing sensitive data,
- initiating payments,
- creating purchase orders,
- modifying access rights,
- changing production systems,
- deleting or exporting data,
- making customer-impacting decisions,
- or delegating tasks to other agents.
