# High-Impact and Audit-Grade Pre-qualification Gate

## Status

This document is part of the AAEF v0.4.0 planning work.

It defines a pre-qualification gate for applying High-Impact and Audit-Grade assessment profiles.

This document is informative and does not create a certification scheme, formal standard, implementation conformance claim, audit opinion, or claim of complete mitigation.

## Purpose

AAEF assessment profiles allow assessment depth to vary by risk, impact, and assurance needs.

However, High-Impact and Audit-Grade profiles should not be selected merely because an action is important or because stronger assurance is desired.

Before applying these profiles, the assessed system should meet minimum architectural, authorization, enforcement, and evidence prerequisites.

This document defines those prerequisites.

## Scope

This pre-qualification gate applies when an assessor or organization intends to use:

- High-Impact assessment profile
- Audit-Grade assessment profile

It is especially relevant for agentic AI systems that can:

- perform high-impact actions,
- call privileged tools or APIs,
- modify sensitive data,
- initiate irreversible or externally visible actions,
- delegate authority to other agents or workflows,
- act on behalf of a human or organization,
- or operate under regulated, audited, or security-critical conditions.

## Relationship to Assessment Profiles

Assessment profiles describe assessment depth.

This pre-qualification gate describes whether a system has enough control structure to support a higher-assurance assessment profile.

If the pre-qualification gate is not satisfied, the assessor should avoid presenting the assessment as High-Impact or Audit-Grade assurance.

The system may still be assessed using a lower profile, or the gap may be recorded as a finding.

## Pre-qualification Outcomes

The pre-qualification gate may produce one of the following outcomes.

### Eligible

The system appears to meet the minimum prerequisites for the intended profile.

Assessment may proceed using the High-Impact or Audit-Grade profile.

### Eligible with Constraints

The system meets some prerequisites, but the assessment scope, evidence scope, or assurance claim must be limited.

The constraints should be recorded.

Examples:

- only specific workflows are eligible,
- only specific tools are eligible,
- only specific action classes are eligible,
- only specific evidence sources are reliable enough.

### Not Eligible

The system does not meet the minimum prerequisites.

The assessor should not present the assessment as High-Impact or Audit-Grade assurance.

The assessment may continue using a lower profile, or remediation may be required first.

### Not Assessed

The pre-qualification gate was not evaluated.

Not Assessed must not be treated as Eligible.

## Minimum Preconditions

### 1. Assessed Scope Is Defined

The assessed system, workflow, agent, tool, action class, and environment boundary should be defined.

The scope should identify:

- agentic system or agent instance,
- action types,
- tools and APIs,
- principals,
- delegated authority paths,
- data and resource boundaries,
- environments,
- and excluded components.

### 2. High-Impact Action Boundary Is Defined

The organization should define which actions are considered high-impact.

The definition may consider:

- sensitive data access,
- financial or operational impact,
- external communication,
- privilege changes,
- irreversible actions,
- safety impact,
- regulatory or contractual impact,
- and incident response significance.

### 3. Trusted Authorization Decision Point Exists

The system should have an identifiable authorization decision point.

The authorization decision point should evaluate trusted inputs such as:

- principal identity,
- agent identity,
- delegated authority,
- action type,
- resource,
- purpose,
- policy version,
- risk level,
- state or revocation status,
- and approval requirements.

Model output alone must not be treated as authorization.

### 4. Tool Dispatch Enforcement Path Is Enforced

There should be an enforced path between model-generated action proposals and tool or API execution.

The system should prevent direct bypass of the enforcement point.

The enforcement path should be able to deny, defer, escalate, or require approval before execution.

### 5. Principal and Delegation Context Is Traceable

The system should preserve context about:

- who or what initiated the action,
- on whose behalf the action was performed,
- which agent or workflow acted,
- what delegated authority was used,
- and how the authority chain can be reconstructed.

### 6. Policy Version and Decision Context Are Traceable

The assessment should be able to reconstruct which policy version and decision context applied at the time of the action.

Evidence should identify:

- policy reference,
- policy version,
- decision timestamp,
- decision result,
- decision rationale or reason code where applicable,
- and required approval or escalation context.

### 7. Evidence Is Independently Generated or Corroborated

For High-Impact and Audit-Grade assessments, evidence should not rely only on model self-report.

Evidence should be generated by, or corroborated with, trusted components such as:

- authorization service,
- tool dispatch layer,
- backend execution system,
- evidence writer,
- append-only or tamper-evident log,
- SIEM or audit logging system,
- or workflow control plane.

### 8. Evidence Supports Reconstruction

Evidence should support reconstruction of:

- proposed action,
- authorization decision,
- dispatch decision,
- execution result,
- principal context,
- delegated authority,
- policy context,
- approval or reauthorization where applicable,
- denial or non-execution where applicable,
- and relevant correlation identifiers.

### 9. Revocation, Freeze, and Denial Behavior Is Defined

The system should define behavior for:

- expired authority,
- revoked authority,
- downgraded authority,
- missing authority,
- ambiguous authority,
- unsafe state changes,
- freeze conditions,
- and denied or reauthorized actions.

For higher-assurance profiles, denial and non-execution should be evidenced.

### 10. Human Approval Is Reviewable Where Required

If human approval is part of the control design, the system should record:

- approver identity or role,
- action being approved,
- risk or impact information shown,
- approval timestamp,
- approval scope,
- approval decision,
- and any override or break-glass path.

Human approval should not be treated as meaningful assurance if it is only a UI click without sufficient context.

### 11. Testing and Sampling Are Feasible

The assessor should be able to sample relevant actions and evidence.

For High-Impact and Audit-Grade assessments, sampling should include boundary cases where feasible, such as:

- approved high-impact actions,
- denied actions,
- reauthorized actions,
- delegated actions,
- exception or override flows,
- actions influenced by untrusted content,
- and action sequences that may indicate task splitting or threshold avoidance.

### 12. Known Limitations Are Recorded

Known gaps and limitations should be recorded.

Examples:

- incomplete logging,
- missing policy versioning,
- unsupported denial evidence,
- weak correlation identifiers,
- partial SIEM integration,
- reliance on runtime self-report,
- or limited coverage of delegated workflows.

## Audit-Grade Additional Expectations

Audit-Grade assessment should generally require stronger evidence and clearer boundaries than High-Impact assessment.

Additional expectations may include:

- stronger evidence integrity,
- clearer retention and retrieval expectations,
- more complete traceability across authorization, dispatch, execution, and evidence,
- more explicit sampling rationale,
- more consistent reviewer judgment boundaries,
- stronger correlation with backend or SIEM logs,
- and clearer documentation of exceptions.

## Pre-qualification Checklist

| Area | Minimum expectation | Example evidence |
|---|---|---|
| Scope | Assessed system, workflow, actions, tools, and environment are defined | Scope statement; architecture diagram; tool registry |
| High-impact boundary | High-impact actions are defined | Risk taxonomy; action classification |
| Authorization | Trusted authorization decision point exists | Policy configuration; decision logs |
| Enforcement | Tool dispatch enforcement path is enforced | Dispatch logs; enforcement test results |
| Principal context | Principal and delegation context are traceable | Principal claims; delegation records; trace IDs |
| Policy traceability | Policy version and decision context are recorded | Policy version; decision record |
| Evidence quality | Evidence is independently generated or corroborated | Backend logs; evidence writer records; SIEM logs |
| Reconstruction | Action lifecycle can be reconstructed | Evidence event; action timeline |
| Revocation / denial | Revocation, freeze, denial, and reauthorization behavior is defined | Denial logs; revocation tests |
| Human approval | Approval is reviewable where required | Approval records; UI screenshots |
| Sampling | Assessment sampling is feasible | Sample list; test plan |
| Limitations | Known gaps are documented | Gap register; residual risk notes |

## Non-Goals

This document does not define a certification program.

It does not define audit sufficiency.

It does not guarantee that a system is safe, compliant, or fully controlled.

It does not require every AAEF assessment to use High-Impact or Audit-Grade profiles.

It does not replace organization-specific risk assessment.

## Relationship to Testing Procedures

This document should be used with:

- `docs/en/25-testing-procedures-and-pass-criteria.md`
- `assessment/aaef-testing-procedures-v0.4-draft.csv`

Testing procedures describe how controls may be evaluated.

This pre-qualification gate describes whether the system has enough control structure to support higher-assurance assessment profiles.

## Relationship to Trusted Control Boundary Work

This document should be coordinated with future Trusted Control Boundary integrity requirements.

The pre-qualification gate depends on whether authorization, enforcement, evidence generation, and backend execution can be treated as trusted enough for the claimed assessment profile.

## Open Questions

Future work should determine:

- whether pre-qualification should become machine-readable,
- whether High-Impact and Audit-Grade profiles need separate checklists,
- whether specific minimum evidence fields should be required,
- how pre-qualification should be represented in the assessment worksheet,
- how pre-qualification should interact with external framework mappings,
- and how failed pre-qualification should be reported.
