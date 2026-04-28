# 11. High-Impact Action Taxonomy

## Status

This document defines the initial draft of the **AAEF High-Impact Action Taxonomy** for public review.

Machine-readable draft:

- `taxonomies/high-impact-action-taxonomy-v0.2-draft.csv`

This taxonomy is intended for AAEF v0.2.0 discussion and review. It is not a certification scheme, legal standard, or exhaustive list of all high-risk agentic AI actions.

## Machine-Readable CSV

The taxonomy is also provided as a machine-readable CSV file:

- `taxonomies/high-impact-action-taxonomy-v0.2-draft.csv`

The CSV includes the following columns:

- `Category ID`
- `Category Name`
- `Definition`
- `Example Actions`
- `Typical Impact`
- `Recommended Baseline`
- `Key AAEF Control Areas`
- `Suggested Evidence`

The CSV is intended to support assessment tooling, review worksheets, mappings, and future validation workflows.

## Purpose

AAEF v0.1.x requires organizations to define high-impact agentic actions.

That flexibility is necessary because impact depends on organizational context, business process, regulatory environment, data sensitivity, and operational risk.

However, if every organization defines high-impact actions differently, AAEF assessment results may become difficult to compare and apply.

This taxonomy provides recommended baseline categories for actions that should normally be treated as high-impact by default.

Organizations may define additional high-impact actions based on their context, but AAEF recommends treating the categories in this document as a starting baseline.

## Design Principle

The taxonomy is based on a simple principle:

> An agentic action should be treated as high-impact when it can materially affect people, money, access, systems, sensitive data, legal obligations, security posture, or downstream agent behavior.

The goal is not to block AI agents from performing useful work.

The goal is to identify actions that require stronger controls, such as:

- explicit authority scope,
- action-boundary authorization,
- risk-based approval,
- evidence generation,
- revocation capability,
- incident reconstruction,
- and periodic review.

## Relationship to AAEF Controls

The taxonomy supports, but does not replace, the following AAEF control areas:

- AAEF-GOV-02: High-Impact Action Definition
- AAEF-AUZ-01: Action Boundary Authorization
- AAEF-AUZ-03: Risk-Based Approval
- AAEF-TOOL-03: High-Risk Tool Classification
- AAEF-EVD-01: High-Impact Action Evidence
- AAEF-EVD-02: Evidence Fields
- AAEF-HUM-01: Approval UX Clarity
- AAEF-RES-01: Revocation Capability
- AAEF-RES-03: Incident Reconstruction

## Recommended Baseline Categories

### HIA-COMM: External Communication

Actions that send, publish, or transmit information to external parties.

Examples:

- sending email to a customer, vendor, regulator, or partner,
- posting externally visible content,
- sending messages through external SaaS platforms,
- submitting forms to external systems,
- replying to customers through a support channel.

Why it matters:

External communication may create reputational, contractual, privacy, regulatory, or fraud risk.

Recommended treatment:

- authorize recipient, purpose, and content class,
- require approval for sensitive or irreversible external communication,
- retain evidence of agent, principal, recipient, purpose, authorization, approval, and result.

---

### HIA-DATA: Sensitive Data Access or Export

Actions that access, retrieve, summarize, transform, copy, export, or transmit sensitive data.

Examples:

- exporting customer records,
- retrieving personal data,
- accessing payment-related data,
- summarizing confidential documents,
- sending internal data to external tools,
- moving data across trust boundaries.

Why it matters:

Sensitive data actions may create privacy, confidentiality, regulatory, contractual, or security risk.

Recommended treatment:

- bind action to principal, purpose, and data scope,
- distinguish read, export, and external transfer,
- record data class, resource, purpose, authorization decision, and evidence location,
- avoid storing unnecessary raw sensitive content in evidence events.

---

### HIA-FIN: Payment, Purchase, or Financial Commitment

Actions that initiate, approve, prepare, modify, or execute financial transactions or commitments.

Examples:

- creating purchase orders,
- initiating payments,
- changing invoice details,
- approving refunds,
- modifying billing records,
- committing budget or spend.

Why it matters:

Financial actions may create direct monetary loss, fraud, dispute, audit, or regulatory risk.

Recommended treatment:

- enforce explicit authority limits,
- define amount, currency, vendor, account, purpose, and expiration constraints,
- require human approval for thresholds or unusual patterns,
- retain evidence of authorization, approval, and external effect.

---

### HIA-AUTH: Access Rights or Privilege Change

Actions that grant, revoke, modify, or recommend access rights, roles, permissions, credentials, or security-sensitive entitlements.

Examples:

- adding a user to an admin group,
- changing IAM roles,
- granting SaaS access,
- rotating or retrieving secrets,
- modifying MFA or authentication policies,
- creating service accounts.

Why it matters:

Access changes may enable privilege escalation, persistence, data exposure, or downstream compromise.

Recommended treatment:

- require strong principal binding and purpose,
- deny on authority ambiguity,
- require evidence for requested change, approver, policy, result, and revocation path,
- consider separation of duties for critical changes.

---

### HIA-SYS: Production System Change

Actions that modify production systems, operational configuration, infrastructure, routing, availability, or business-critical workflows.

Examples:

- changing production configuration,
- modifying firewall or routing rules,
- updating production database state,
- restarting critical services,
- changing workflow automation rules,
- modifying operational thresholds.

Why it matters:

Production changes may cause outage, data corruption, security degradation, or cascading failures.

Recommended treatment:

- classify tools and operations by risk,
- require change context, approval, rollback or isolation plan,
- record system, resource, policy, approval, result, and correlation ID.

---

### HIA-CODE: Code Commit, Merge, Deployment, or Execution

Actions that write, modify, merge, deploy, execute, or trigger code in repositories, CI/CD pipelines, runtime environments, or automation systems.

Examples:

- committing code,
- opening or merging pull requests,
- triggering production deployment,
- executing scripts,
- running generated code,
- modifying CI/CD configuration,
- changing infrastructure-as-code.

Why it matters:

Code actions may introduce vulnerabilities, backdoors, outages, or unexpected code execution.

Recommended treatment:

- treat code execution and deployment as high-risk tool use,
- require repository, branch, environment, purpose, and approval evidence,
- retain code reference, diff or digest, tool invocation, result, and rollback or isolation reference.

---

### HIA-LEGAL: Contract, Legal, or Regulatory Commitment

Actions that create, modify, accept, submit, or communicate legal, regulatory, contractual, or compliance-relevant commitments.

Examples:

- accepting contract terms,
- submitting regulatory responses,
- sending legal notices,
- making compliance attestations,
- modifying terms of service,
- responding to audit requests.

Why it matters:

Legal and regulatory actions may bind an organization or create obligations, liability, or compliance exposure.

Recommended treatment:

- require explicit principal authority and human approval,
- retain evidence of content, recipient, authority, approval, timestamp, and submission result,
- preserve review context and versioned artifacts.

---

### HIA-CUST: Customer-Impacting Decision or Action

Actions that materially affect a customer, user, patient, employee, applicant, or other individual.

Examples:

- approving or denying service,
- changing account status,
- suspending a user,
- issuing refunds or penalties,
- changing service terms for an individual,
- making eligibility or prioritization decisions.

Why it matters:

Customer-impacting actions may affect rights, access, service quality, fairness, safety, or business relationships.

Recommended treatment:

- require purpose and policy basis,
- retain decision inputs, authority, approval where applicable, and outcome,
- support appeal, review, or reconstruction where appropriate.

---

### HIA-SEC: Security Response, Blocking, or Containment

Actions that affect security posture, detection, response, containment, access, blocking, quarantine, or enforcement.

Examples:

- blocking an IP address,
- disabling a user account,
- quarantining an endpoint,
- escalating an incident,
- modifying detection logic,
- suppressing an alert,
- isolating an agent or workflow.

Why it matters:

Security actions may protect the organization, but can also cause denial of service, evidence loss, or attacker-assisted disruption if misused.

Recommended treatment:

- require incident or policy context,
- record detection source, action, target, authority, result, and rollback path,
- require additional review for broad or irreversible actions.

---

### HIA-MEM: Persistent Memory Write or Trust-State Update

Actions that write persistent memory, update long-term agent context, modify trust state, or alter future agent behavior.

Examples:

- writing long-term user preferences,
- storing retrieved content as memory,
- changing agent trust state,
- modifying allowlists or denylists,
- updating learned workflow instructions,
- persisting assumptions that affect future actions.

Why it matters:

Persistent memory and trust-state changes can influence future actions, create long-lived poisoning risk, or degrade principal context over time.

Recommended treatment:

- require memory write control,
- retain provenance, trust level, content digest, purpose, and expiration where applicable,
- support review, correction, and revocation of persistent memory.

---

### HIA-A2A: External Agent Delegation or Cross-Domain Agent Action

Actions that delegate tasks, authority, evidence, tool access, or workflow participation to another agent, especially across organizational or trust boundaries.

Examples:

- delegating work to an external agent,
- accepting delegated work from another agent,
- invoking an agent operated by another organization,
- exchanging authority claims,
- relying on external agent capability declarations,
- forwarding principal context across trust domains.

Why it matters:

Agent-to-agent communication does not imply authority to delegate work. Cross-domain agent actions may create identity, authority, evidence, and revocation gaps.

For v0.5.0 planning, see `docs/en/31-cross-agent-cross-domain-authority.md` for the Cross-Agent and Cross-Domain Authority concept note.

Recommended treatment:

- verify agent identity, issuer, operator, principal binding, and authority scope,
- record delegation chain, accepted authority, constraints, and evidence exchange,
- ensure downstream revocation and incident reconstruction.

---

## Category Summary

| Category | Name | Typical Impact |
|---|---|---|
| HIA-COMM | External Communication | Reputation, confidentiality, fraud, regulatory exposure |
| HIA-DATA | Sensitive Data Access or Export | Privacy, confidentiality, data leakage |
| HIA-FIN | Payment, Purchase, or Financial Commitment | Financial loss, fraud, audit exposure |
| HIA-AUTH | Access Rights or Privilege Change | Privilege escalation, persistence, compromise |
| HIA-SYS | Production System Change | Outage, corruption, cascading failure |
| HIA-CODE | Code Commit, Merge, Deployment, or Execution | Vulnerability, backdoor, runtime compromise |
| HIA-LEGAL | Contract, Legal, or Regulatory Commitment | Liability, legal obligation, compliance exposure |
| HIA-CUST | Customer-Impacting Decision or Action | Rights, fairness, service impact |
| HIA-SEC | Security Response, Blocking, or Containment | Defensive impact, disruption, evidence risk |
| HIA-MEM | Persistent Memory Write or Trust-State Update | Long-term poisoning, future behavior influence |
| HIA-A2A | External Agent Delegation or Cross-Domain Agent Action | Cross-domain authority, delegation, evidence gaps |

## Suggested Evidence Fields

For high-impact actions, evidence should generally include:

- high-impact action category,
- agent ID,
- agent instance ID,
- principal ID,
- principal context or context ID,
- authority scope,
- delegation chain where applicable,
- requested action,
- target resource,
- purpose,
- risk level,
- authorization decision,
- policy ID,
- approval reference where required,
- input source trust metadata where relevant,
- result,
- external effect indicator,
- evidence hash or evidence location,
- revocation or isolation reference where applicable.

These fields align with the AAEF Agentic Action Evidence Event Schema.

## Suggested Assessment Questions

Assessors may ask:

1. Has the organization defined high-impact agentic actions?
2. Does the definition include the recommended AAEF baseline categories?
3. Are high-impact actions mapped to tools, APIs, workflows, and permissions?
4. Are high-impact actions subject to action-boundary authorization?
5. Are high-impact actions evidenced using structured evidence events?
6. Are approval thresholds defined and reviewed?
7. Can the organization reconstruct a high-impact action from evidence?
8. Can delegated or downstream high-impact actions be revoked?
9. Are persistent memory writes classified and reviewed?
10. Are external agent delegations treated as high-impact by default?

## Implementation Guidance

Organizations should not treat this taxonomy as static.

At minimum, they should:

- review categories during agentic system design,
- map categories to concrete tools and operations,
- identify which categories require human approval,
- identify which categories require stronger evidence retention,
- define risk thresholds,
- periodically review action history,
- and update the taxonomy as agent capabilities change.

## What This Taxonomy Does Not Do

This taxonomy does not:

- replace organizational risk assessment,
- define legal or regulatory obligations,
- define a certification scheme,
- prove that an action is safe,
- remove the need for threat modeling,
- or fully define implementation-specific approval workflows.

## Open Questions for Review

Feedback is welcome on:

- whether any category is missing,
- whether any category should be split,
- whether the baseline is too broad or too narrow,
- how to treat internal-only communication,
- how to define sensitive data consistently,
- whether persistent memory writes should always be high-impact,
- how to classify read-only but high-sensitivity actions,
- how to represent action sequences and task splitting,
- how this taxonomy should integrate with evidence event schema fields.

## Future Work

Future versions may add:

- CSV and JSON versions of the taxonomy,
- examples for each category,
- mappings to AAEF controls,
- mappings to OWASP Agentic Top 10 risks,
- assessment worksheet integration,
- and reference architecture annotations.
