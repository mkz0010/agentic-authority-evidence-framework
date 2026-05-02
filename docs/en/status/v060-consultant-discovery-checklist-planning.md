# AAEF v0.6.0 Consultant Discovery Checklist Planning

Status: Consultant discovery checklist planning  
Related roadmap: #241  
Related implementation reference: `docs/en/status/v060-implementation-reference-pattern-planning.md`  
Related evidence examples: `docs/en/status/v060-permitted-action-evidence-example-planning.md`, `docs/en/status/v060-non-execution-evidence-example-planning.md`  
Related auditor checklist: `docs/en/status/v060-auditor-evidence-request-checklist-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document provides a non-normative consultant discovery checklist for scoping AAEF-style review, advisory, pilot, or implementation planning engagements.

The checklist translates AAEF concepts into practical discovery questions a consultant can use before recommending implementation work, assessment work, remediation work, or risk-owner decision support.

This document is planning material. It does not create a consulting methodology requirement, audit standard, certification requirement, compliance requirement, conformity assessment, audit opinion, or implementation conformance profile.

## Intended users

This checklist is intended for:

- security consultants,
- AI security consultants,
- GRC consultants,
- implementation advisors,
- auditors preparing scoping interviews,
- security architects,
- risk owners,
- engineering managers,
- and operators preparing for external review.

## Non-normative status

This document is not an active assessment artifact.

It does not update:

- active controls,
- active evidence schema,
- active assessment worksheet,
- active testing procedures,
- active examples,
- mappings,
- CSVs,
- or the current control and assessment baseline.

Any future promotion into active consulting, assessment, or implementation artifacts must be handled through explicit review and PRs.

## Discovery objective

A consultant should use discovery to determine:

1. whether the system performs agentic actions,
2. which actions are high-impact,
3. who or what the principal is,
4. how authority is granted, constrained, delegated, and revoked,
5. where authorization decisions are made,
6. where dispatch enforcement occurs,
7. whether the backend independently verifies authority,
8. what evidence exists,
9. whether successful and non-executed actions can be reconstructed,
10. what assurance limitations remain,
11. and which adoption path is realistic.

## Discovery outputs

A discovery engagement should produce one or more of the following outputs.

| Output | Purpose |
| --- | --- |
| Agentic action inventory | Lists actions the system can perform. |
| High-impact action classification | Identifies actions needing stronger controls and evidence. |
| Authority and delegation map | Shows principals, authority sources, delegation, scope, and expiry. |
| Execution boundary map | Shows dispatchers, gateways, tools, and backend relying parties. |
| Evidence availability map | Shows which evidence exists and which is missing. |
| Non-execution visibility map | Shows whether denied, held, frozen, and failed actions are recorded. |
| Gap summary | Maps missing capabilities to AAEF concepts or controls. |
| Pilot recommendation | Defines a limited adoption path. |
| Risk-owner memo input | Supports risk acceptance, remediation, or deferral decisions. |
| Claim-boundary note | Prevents certification, compliance, audit, or equivalence overstatement. |

## Discovery phases

Recommended discovery phases:

| Phase | Purpose |
| --- | --- |
| 1. Context and scope | Understand the system, owner, business process, and action domain. |
| 2. Agentic action inventory | Identify what the agent can do. |
| 3. Impact classification | Identify high-impact actions. |
| 4. Authority model review | Identify principals, authority sources, delegation, and scope. |
| 5. Execution boundary review | Identify dispatch, tool, and backend enforcement points. |
| 6. Evidence review | Identify evidence sources, gaps, and limitations. |
| 7. Non-execution review | Determine whether boundary enforcement failures are visible. |
| 8. Operational review | Understand ownership, monitoring, escalation, and response. |
| 9. Risk-owner review | Determine who accepts residual risk and on what basis. |
| 10. Adoption recommendation | Recommend pilot, remediation, assessment, or deferral. |

## Phase 1: Context and scope

Ask:

- What business process does the agent support?
- What users, teams, or systems rely on the agent?
- What actions can the agent initiate or influence?
- Does the agent act in production, staging, test, or advisory-only mode?
- Does the agent access sensitive systems, regulated data, customer data, payment data, credentials, production infrastructure, or financial workflows?
- Who owns the agent system?
- Who owns the tools or backends the agent can invoke?
- Who owns the risk decision?
- What incidents, near misses, or concerns triggered the review?

Request:

- system overview,
- architecture diagram,
- data flow diagram,
- tool list,
- backend list,
- owner list,
- risk register entries,
- incident history if available.

Red flags:

- no clear system owner,
- no action inventory,
- agent can call production tools without a documented boundary,
- business owner and technical owner disagree on the system's purpose,
- agent is described as "only a chatbot" despite having tool access.

## Phase 2: Agentic action inventory

Ask:

- What tools can the agent invoke?
- What APIs can the agent call?
- What data can the agent read?
- What data can the agent modify?
- Can the agent send messages, emails, tickets, approvals, transactions, commands, or configuration changes?
- Can the agent trigger workflows in other systems?
- Can the agent create, modify, delete, approve, or escalate records?
- Can the agent delegate to other agents or workflows?
- Can the agent act without human confirmation?
- Which actions are currently logged?

Request:

- tool registry,
- API permission list,
- action catalog,
- workflow catalog,
- system integration list,
- agent runtime configuration,
- tool-router or gateway configuration.

Red flags:

- tool list is incomplete,
- tool permissions are broader than expected,
- agent can invoke general-purpose shell, browser, database, or admin tools,
- no distinction exists between read, write, approve, execute, and delete actions,
- tool access is granted through broad service credentials.

## Phase 3: High-impact action classification

Ask:

- Which actions can affect production availability?
- Which actions can affect confidentiality, integrity, or availability of sensitive data?
- Which actions can affect payments, billing, refunds, or financial records?
- Which actions can modify identity, access, credentials, or permissions?
- Which actions can trigger external communications?
- Which actions can affect legal, HR, compliance, or customer-impacting workflows?
- Which actions are irreversible or difficult to reverse?
- Which actions require approval today?
- Which actions should fail closed if evidence cannot be generated?

Request:

- high-impact action list,
- business impact criteria,
- risk assessment,
- approval matrix,
- change management records,
- operational runbooks,
- incident impact history.

Red flags:

- all actions are treated as the same risk level,
- no high-impact classification exists,
- production write actions are treated as low risk,
- approval requirements are informal,
- rollback is assumed but not tested.

## Phase 4: Principal and authority discovery

Ask:

- Who is the principal when the agent acts?
- Is the principal a human user, service account, team, tenant, organization, or delegated workflow?
- How is the principal authenticated?
- How is the principal bound to the session or action?
- What authority does the principal have?
- How is authority delegated to the agent?
- Is delegated authority narrower than the principal's original authority?
- Is authority time-bounded?
- Is authority action-bounded?
- Is authority resource-bounded?
- Can authority be revoked?
- Is authority lineage recorded?

Request:

- identity provider records,
- role/group mappings,
- service account records,
- delegation records,
- session binding records,
- approval records,
- authority lineage records,
- revocation records.

Red flags:

- agent acts only as a shared service account,
- principal cannot be reconstructed,
- delegated authority is broader than user authority,
- authority does not expire,
- revocation is manual or undocumented,
- authority lineage is missing.

## Phase 5: Authorization decision discovery

Ask:

- Where is the authorization decision made?
- Is the decision separate from model output?
- What policy engine, service, rule, or workflow makes the decision?
- Does the decision use trusted policy inputs?
- Are untrusted natural-language inputs excluded from authority?
- Does the decision produce a decision artifact?
- Does the decision include scope, expiry, policy version, and identifiers?
- Are deny, hold, require-approval, and require-reauthorization outcomes supported?
- Is meaningful human approval required for high-impact actions?
- Can an authorization decision be replayed or reused?

Request:

- policy rules,
- authorization service logs,
- decision artifacts,
- approval workflow records,
- policy version history,
- decision expiry behavior,
- denied decision records,
- reauthorization records.

Red flags:

- model output is treated as the authorization decision,
- natural-language text alone grants authority,
- no explicit decision artifact exists,
- policy version is missing,
- decision has no expiry,
- broad approval is reused across actions,
- deny/hold outcomes are not recorded.

## Phase 6: Dispatch and execution boundary discovery

Ask:

- Where is tool dispatch enforced?
- Is there a dispatcher, tool gateway, execution gateway, or equivalent boundary?
- What does the dispatcher check before execution?
- Does the dispatcher verify the authorization decision?
- Does it check action, resource, scope, principal, expiry, policy version, and evidence requirements?
- Does it fail closed?
- Does it record denied actions?
- Can the agent bypass the dispatcher?
- Are emergency or break-glass paths documented?

Request:

- dispatcher architecture,
- tool gateway configuration,
- enforcement logs,
- denied dispatch records,
- bypass path inventory,
- break-glass records,
- gateway access controls,
- test results for denied actions.

Red flags:

- tools can be invoked directly by the agent runtime,
- dispatcher only logs after execution,
- failed checks still allow backend calls,
- denied tool calls are not recorded,
- break-glass behavior is undocumented,
- scope matching is not implemented.

## Phase 7: Backend relying-party discovery

Ask:

- Does the backend independently verify authority?
- Does it verify the decision identifier?
- Does it verify principal, action, resource, scope, expiry, and policy version?
- Does it prevent replay?
- Does it rely only on the agent runtime's assertion?
- Does it use token introspection, signed decision artifacts, internal authorization APIs, mTLS, or another verification mechanism?
- Does backend verification happen before execution?
- Are backend rejection events recorded?

Request:

- backend authorization design,
- backend verification logs,
- token or decision validation records,
- replay protection design,
- backend rejection records,
- backend execution logs,
- service-to-service identity evidence.

Red flags:

- backend trusts a header set by the agent runtime,
- backend cannot link execution to authorization,
- backend verification occurs after execution,
- replay protection is absent,
- backend uses broad static credentials,
- backend rejection events are not visible.

## Phase 8: Evidence discovery

Ask:

- What evidence is generated for requested actions?
- What evidence is generated for permitted actions?
- What evidence is generated for denied or non-executed actions?
- Are action request, decision, dispatch, backend verification, execution, and evidence records linked?
- Who or what writes evidence?
- Is the evidence writer inside or outside the model-controlled path?
- Where is evidence stored?
- Who can modify or delete evidence?
- How long is evidence retained?
- Are evidence trust limitations documented?
- Can evidence be exported for review?

Request:

- evidence event records,
- evidence schema,
- SIEM logs,
- audit logs,
- evidence store design,
- retention policy,
- access control records,
- evidence writer identity,
- evidence limitation notes,
- sample permitted and non-execution evidence bundles.

Red flags:

- prompt logs are treated as sufficient evidence,
- evidence exists only inside the agent runtime,
- denied actions are not evidenced,
- records cannot be correlated,
- evidence can be edited without trace,
- evidence limitations are not disclosed.

## Phase 9: Reconstruction discovery

Ask:

- Can a reviewer reconstruct a sampled action from request to execution or non-execution?
- Can the reviewer identify the principal?
- Can the reviewer identify the agent instance?
- Can the reviewer identify the authorization decision?
- Can the reviewer identify dispatch enforcement?
- Can the reviewer identify backend verification?
- Can the reviewer distinguish execution from non-execution?
- Can the reviewer identify evidence limitations?
- How long does reconstruction take?
- Who performs reconstruction during an incident?

Request:

- sample reconstruction traces,
- correlation queries,
- evidence bundle exports,
- incident review examples,
- denied-action reconstruction examples,
- reconstruction runbooks.

Red flags:

- reconstruction requires manual guesswork,
- identifiers are inconsistent,
- evidence exists but is not correlated,
- non-execution cannot be reconstructed,
- incident responders do not know where evidence is stored.

## Phase 10: Operational readiness discovery

Ask:

- Who operates the agent system?
- Who monitors denied actions?
- Who reviews high-impact actions?
- Who responds to evidence gaps?
- Who can freeze agentic execution?
- Who approves reauthorization?
- Who owns policy updates?
- Who owns evidence retention?
- Who handles incident response?
- Are operational handoffs documented?

Request:

- operational responsibility matrix,
- monitoring rules,
- alerting configuration,
- incident response runbook,
- freeze/hold procedure,
- escalation matrix,
- policy change procedure,
- evidence retention procedure.

Red flags:

- no one owns denied-action review,
- no freeze/hold procedure exists,
- no escalation path exists,
- policy changes are not controlled,
- evidence retention is not owned,
- incident response excludes agentic actions.

## Phase 11: Legal, compliance, and claim-boundary discovery

Ask:

- Is the organization attempting to use AAEF for compliance support, audit support, internal governance, implementation guidance, or research?
- Are any certification, compliance, audit, conformity, or equivalence claims being made?
- Are external framework mappings being treated as informative or as equivalence?
- Are privacy, retention, data minimization, or legal hold requirements relevant to evidence?
- Are users informed that actions may be logged?
- Are third-party tools or external agents involved?
- Are contractual responsibilities clear?

Request:

- compliance scope statement,
- legal/compliance review notes,
- privacy assessment,
- evidence retention requirements,
- third-party responsibility matrix,
- external framework mapping assumptions,
- public or customer-facing claim language.

Red flags:

- AAEF is described as certification,
- AAEF is used as proof of legal compliance,
- mappings are treated as equivalence,
- evidence retention conflicts with privacy obligations,
- third-party responsibility is unclear,
- customer-facing claims overstate assurance.

## Phase 12: Risk owner discovery

Ask:

- Who accepts residual risk for high-impact agentic actions?
- What decision does the risk owner need to make?
- Which actions are acceptable with current controls?
- Which actions require remediation before use?
- Which actions should be disabled or held?
- What residual risk remains after controls?
- What evidence is needed for risk acceptance?
- What exception process exists?

Request:

- risk register,
- risk acceptance memo,
- exception records,
- business owner approval,
- remediation plan,
- action enablement decision,
- residual risk statement.

Red flags:

- no risk owner is identified,
- technical team accepts business risk informally,
- high-impact actions are enabled without risk acceptance,
- exceptions are undocumented,
- evidence gaps are ignored.

## Discovery scoring model

A consultant may use a simple qualitative readiness classification.

| Classification | Meaning |
| --- | --- |
| Not ready | Agentic actions exist but authority, enforcement, or evidence is not sufficiently defined. |
| Discovery ready | Enough information exists to complete action inventory and scoping. |
| Pilot ready | A limited high-impact action can be tested with bounded authority and evidence. |
| Review ready | Evidence packages can be reviewed for sampled actions. |
| Adoption candidate | Operational ownership, evidence, and risk decisions are sufficiently defined for controlled adoption planning. |

This classification is not an AAEF certification or conformance score.

## Common discovery red flags

High-priority red flags:

- model output is treated as authority,
- tool calls bypass dispatch enforcement,
- backend trusts agent runtime assertions,
- high-impact actions lack approval or authorization decisions,
- evidence is generated only by the agent runtime,
- denied actions are not recorded,
- principal identity cannot be reconstructed,
- authority does not expire,
- approval is broad or reusable,
- evidence cannot support reconstruction,
- AAEF is being presented as certification or compliance proof.

## Consultant deliverable outline

A discovery deliverable may include:

1. executive summary,
2. scope and system description,
3. agentic action inventory,
4. high-impact action classification,
5. authority and delegation map,
6. dispatch and backend verification map,
7. evidence availability map,
8. non-execution visibility assessment,
9. operational responsibility observations,
10. legal/compliance and claim-boundary notes,
11. risk-owner decision inputs,
12. key gaps and red flags,
13. recommended pilot scope,
14. recommended remediation priorities,
15. claim-boundary statement.

## Recommended pilot selection criteria

A good pilot action should be:

- high enough impact to matter,
- narrow enough to scope,
- bounded by clear policy,
- backed by identifiable principal authority,
- executable through a controllable dispatcher,
- verifiable by a backend,
- capable of producing evidence,
- reversible or operationally manageable,
- and acceptable to a risk owner.

Avoid starting with:

- broad administrative access,
- irreversible destructive actions,
- unclear principal identity,
- weak backend verification,
- missing evidence,
- or unclear ownership.

## Relationship to auditor checklist

The consultant discovery checklist asks:

> What exists and what should be scoped?

The auditor evidence request checklist asks:

> What evidence should be requested and reviewed?

These artifacts should be used together.

Consultant discovery can identify whether the organization is ready for an evidence request review.

## Relationship to implementation reference pattern

The implementation reference pattern describes:

- action request,
- authorization decision,
- dispatch enforcement,
- backend verification,
- evidence generation,
- non-execution behavior,
- and reconstruction.

This checklist helps a consultant determine whether those concepts exist in a real system and where gaps remain.

## Relationship to active artifacts

This document does not update active assessment procedures.

A future PR may choose to convert selected discovery questions into an active consulting worksheet or adoption readiness questionnaire. That would require explicit review.

## Claim boundaries

This checklist does not claim:

- certification,
- compliance,
- audit sufficiency,
- conformity,
- equivalence with external frameworks,
- production readiness,
- implementation conformance,
- or complete mitigation.

It may support:

- discovery,
- scoping,
- implementation planning,
- evidence planning,
- assessment preparation,
- consultant advisory work,
- risk-owner decision support,
- and public review.

## Non-goals

This document does not:

- change active controls,
- change the current control and assessment baseline,
- update schemas, examples, mappings, CSVs, or testing procedures,
- promote v0.5.0 or v0.6.0 planning material into active requirements,
- assert consulting methodology conformance,
- assert audit sufficiency,
- claim compliance,
- claim certification,
- claim conformity,
- claim equivalence with external frameworks,
- or assert production readiness.

## Acceptance criteria

This planning checklist is sufficient when:

- discovery phases are defined,
- consultant questions are documented,
- requested materials are identified,
- red flags are listed,
- pilot selection criteria are provided,
- discovery deliverable structure is described,
- relationship to auditor and implementation planning artifacts is explained,
- claim boundaries are preserved,
- and no active baseline change is implied.
