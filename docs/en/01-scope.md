# 01. Scope

## Purpose

AAEF provides an action assurance control profile for agentic AI systems.

It is intended to help organizations define, assess, and improve controls for AI agents that can take meaningful actions on behalf of humans or organizations.

## In Scope

AAEF applies to agentic AI systems that may:

- interpret user or system instructions,
- call external tools or APIs,
- access organizational data,
- operate under delegated authority,
- delegate tasks to other agents or services,
- participate in multi-agent workflows,
- perform actions that affect external parties, systems, data, money, rights, or obligations.

AAEF is most relevant for high-impact or semi-autonomous AI agents used in business, security, finance, operations, engineering, legal, compliance, customer support, procurement, and administrative workflows.

## Out of Scope

AAEF does not define:

- a new authentication protocol,
- a new authorization protocol,
- a new agent communication protocol,
- a model evaluation benchmark,
- a general AI ethics framework,
- a replacement for existing AI governance frameworks,
- a compliance certification scheme,
- or a legal standard of care.

AAEF may reference identity, authorization, attestation, transparency log, or governance technologies, but it is designed to remain implementation-neutral.

## Target Systems

AAEF may be applied to:

- tool-using AI assistants,
- autonomous workflow agents,
- software engineering agents,
- security operations agents,
- procurement agents,
- customer support agents,
- data analysis agents,
- robotic process automation enhanced by LLMs,
- multi-agent systems,
- agent platforms,
- and internal enterprise AI agent deployments.

## High-Impact Agentic Actions

AAEF is especially concerned with actions that may create operational, financial, legal, privacy, security, safety, or reputational impact.

Examples include:

- sending an email to an external party,
- submitting a payment or purchase order,
- updating customer records,
- changing access rights,
- modifying production infrastructure,
- running destructive commands,
- exporting sensitive data,
- committing code,
- approving a workflow,
- signing or accepting terms,
- delegating authority to another agent,
- or invoking an external service that creates real-world consequences.

## Design Goal

AAEF is designed to be used as:

- a control catalog,
- an assessment guide,
- a design review checklist,
- a basis for audit evidence planning,
- a reference for high-risk agentic action governance,
- and a mapping layer between existing AI governance, identity, security, and operational risk frameworks.
