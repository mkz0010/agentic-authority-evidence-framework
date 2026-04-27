# 13. AAEF One-Page Overview

## What Is AAEF?

AAEF stands for **Agentic Authority & Evidence Framework**.

It is an action assurance control profile for agentic AI systems.

AAEF focuses on a specific problem:

> When an AI agent takes action through tools, APIs, workflows, or other systems, how do we know the action was authorized, bounded, attributable, and evidenced?

AAEF is not primarily about whether a model produced a good answer.

It is about whether an agentic action should be allowed to happen, under whose authority, within what boundaries, and with what evidence.

## Core Principle

> Model output is not authority.

A model may propose an action.

A model may explain an action.

A model may generate a tool call.

But model output alone should not be treated as permission to execute a high-impact action.

Authorization should come from trusted policy, delegated authority, principal binding, runtime state, and enforceable control points.

## The Five Questions

AAEF helps reviewers and implementers ask five practical questions.

| Question | Meaning |
|---|---|
| Who or what acted? | Agent identity and runtime instance |
| On whose behalf? | Principal binding and delegated authority |
| What was allowed? | Authority scope, constraints, and action boundary |
| Was it allowed at execution time? | Authorization, runtime state, revocation, and ambiguity checks |
| What evidence exists? | Structured evidence for review, audit, and reconstruction |

## What AAEF Covers

AAEF covers control areas such as:

- agent identity,
- principal binding,
- delegation and authority,
- action authorization,
- tool invocation control,
- memory and context control,
- evidence and auditability,
- human oversight,
- response and revocation.

AAEF also includes supporting materials for v0.2 public review:

- High-Impact Action Taxonomy,
- Evidence Event JSON Schema,
- Evidence Schema validation workflow,
- OWASP Agentic Top 10 mapping,
- Assurance Model and Residual Risk Mapping,
- Assessment Quick Start,
- Assessment Worksheet.

## What Counts as High-Impact?

A high-impact action is an agentic action that can materially affect people, money, access, systems, sensitive data, legal obligations, security posture, or downstream agent behavior.

Examples include:

- sending external communications,
- exporting sensitive data,
- making payments or purchases,
- changing access rights,
- modifying production systems,
- committing or deploying code,
- making customer-impacting decisions,
- performing security containment,
- writing persistent memory or trust state,
- delegating authority to another agent.

## What AAEF Does Not Claim

AAEF does not guarantee that:

- a model will always reason correctly,
- natural-language intent will always be interpreted correctly,
- prompt injection will always be detected,
- semantic influence from untrusted content can always be excluded,
- revocation is instantaneous in distributed systems,
- human approval will always be meaningful,
- evidence is complete unless evidence collection is correctly implemented,
- or an implementation is secure simply because it claims to use AAEF.

AAEF is a framework for reducing, constraining, evidencing, and reviewing agentic action risk.

It is not a magic safety layer.

## Implementation Framing

AAEF does not require replacing existing identity, authorization, runtime isolation, or enforcement mechanisms.

It can be implemented using existing mechanisms such as OS users, service accounts, workload identities, IAM, API gateways, policy engines, workflow runners, containers, serverless functions, CLI wrappers, backend services, and audit pipelines.

AAEF focuses on the assurance requirement:

- the model may propose an action,
- the proposed action should not be treated as authority by itself,
- high-impact execution should pass through an authorization or enforcement boundary,
- and evidence should link the proposed action, principal, authorization or enforcement decision, dispatched operation, executed effect, and result.

In short, AAEF is not a new authorization stack. It is a framework for making agentic action authority, enforcement, and evidence boundaries explicit and reviewable.

## How to Read This Repository

Start here:

1. `README.md`  
   Repository entry point and current status.

2. `docs/en/00-introduction.md`  
   Why AAEF exists.

3. `docs/en/02-core-principles.md`  
   The core ideas behind AAEF.

4. `docs/en/06-control-domains.md`  
   The control domain structure.

5. `docs/en/07-control-requirements.md`  
   Human-readable control requirements.

6. `controls/aaef-controls-v0.1.csv`  
   Machine-readable control catalog source.

Then read the v0.2 public review artifacts:

- `docs/en/11-high-impact-action-taxonomy.md`
- `docs/en/14-evidence-event-schema.md`
- `docs/en/15-v02-control-expansion-notes.md`
- `docs/en/16-assurance-model.md`
- `docs/en/12-assessment-quick-start.md`
- `assessment/aaef-assessment-worksheet-v0.2-draft.csv`

## How AAEF Can Be Used

AAEF can support:

- security requirements for agentic AI systems,
- architecture review,
- tool authorization design,
- high-impact action classification,
- evidence event design,
- approval workflow review,
- incident reconstruction,
- AI governance review,
- internal assessment,
- and public discussion of agentic AI control patterns.

## Simple Mental Model

AAEF separates four things that are often blurred together:

| Layer | Question |
|---|---|
| Model | What does the AI propose? |
| Authority | Is the action permitted? |
| Enforcement | Can only the permitted action execute? |
| Evidence | Can the action be reviewed later? |

The model can suggest.

The authority layer decides.

The enforcement layer constrains.

The evidence layer records.

## Current Status

AAEF v0.3.0 Public Review Draft is the current public review baseline.

AAEF v0.3.0 builds on the v0.2.x baseline and adds implementation profiles, evidence quality assessment criteria, assessment profile mapping, TCB implementation capability patterns, action sequence monitoring, assessment automation guidance, and infrastructure / SIEM evidence integration guidance.

These materials remain public review drafts and are not a certification scheme, formal standard, or claim of complete mitigation.

Feedback is welcome through Issues, Pull Requests, and Discussions.
