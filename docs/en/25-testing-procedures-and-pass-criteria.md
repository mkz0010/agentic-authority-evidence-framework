# Testing Procedures and Pass Criteria

## Status

This document is part of the AAEF v0.4.0 planning work.

It defines an initial model for measurable testing procedures and pass criteria.

This document is informative and does not create a certification scheme, formal standard, implementation conformance claim, audit opinion, or claim of complete mitigation.

## Purpose

AAEF control requirements describe what should be governed in agentic AI systems.

Assessment worksheets record assessment results and evidence reviewed.

Testing procedures and pass criteria help reduce ambiguity when reviewers evaluate whether a control is implemented and supported by evidence.

This document defines how AAEF should express:

- testing objectives,
- testing methods,
- required evidence,
- sample selection,
- pass criteria,
- partial criteria,
- fail conditions,
- reviewer judgment boundaries,
- and automation potential.

## Relationship to the Control Catalog

The control catalog remains the machine-readable source of truth for control IDs and control requirements.

Current catalog file:

- `controls/aaef-controls-v0.1.csv`

Testing procedures are derived from and linked to catalog controls by `Control ID`.

Testing procedures must not introduce new control requirements unless the control catalog is also updated.

## Relationship to the Assessment Worksheet

The assessment worksheet records the result of an assessment.

Testing procedures provide guidance for how a reviewer may reach that result.

The worksheet and testing procedures should remain aligned on:

- control ID,
- domain,
- requirement level,
- applicable control scope,
- evidence expectations,
- and assessment result interpretation.

## Assessment Result Model

AAEF testing procedures should support at least the following result categories.

### Pass

A control may be assessed as Pass when:

- the control is implemented for the assessed scope,
- implementation is supported by appropriate evidence,
- evidence is traceable to the assessed action, system, or control context,
- evidence is generated independently or corroborated where required,
- no material gap is observed for the assessed scope.

### Partial

A control may be assessed as Partial when:

- the control is partially implemented,
- implementation coverage is incomplete,
- evidence exists but does not fully support the assessment objective,
- evidence is not sufficiently traceable for all assessed actions,
- the control is implemented for some systems or workflows but not all applicable scope.

Partial results should include remediation notes and residual risk.

### Fail

A control may be assessed as Fail when:

- the control is not implemented,
- the implementation does not operate as described,
- required evidence is missing,
- evidence contradicts the claimed implementation,
- the control can be bypassed in the assessed execution path,
- model or runtime self-report is treated as sufficient evidence where independent or corroborated evidence is required.

### Not Applicable

A control may be assessed as Not Applicable only when the assessed system, workflow, or action type is outside the defined applicability of the control.

The reason for non-applicability should be recorded.

### Not Assessed

A control may be marked Not Assessed when it was not evaluated.

Not Assessed must not be treated as Pass.

## Evidence Expectations

Testing procedures should distinguish evidence quality, not only evidence existence.

Useful evidence may include:

- authorization decision records,
- policy evaluation logs,
- tool dispatch records,
- backend execution logs,
- evidence writer records,
- SIEM or audit log entries,
- human approval records,
- revocation or freeze records,
- configuration exports,
- architecture diagrams,
- test results,
- sampling records,
- incident reconstruction artifacts.

Evidence should be evaluated for:

- source,
- independence,
- traceability,
- completeness,
- integrity,
- retention,
- correlation,
- and limitations.

## Sample Selection

Sampling should be risk-proportional.

Sample selection may consider:

- high-impact actions,
- privileged actions,
- actions involving sensitive data,
- actions involving external systems,
- delegated or chained actions,
- denied or reauthorized actions,
- exception or override flows,
- actions influenced by untrusted content,
- action sequences that may indicate task splitting or threshold avoidance.

For higher assurance profiles, samples should include executed actions, denied actions, and boundary cases where applicable.

## Reviewer Judgment

Some AAEF controls can be partially automated.

However, reviewer judgment may still be required when assessing:

- policy intent,
- appropriateness of evidence,
- adequacy of boundary design,
- sufficiency of sampling,
- residual risk,
- partial implementation,
- human approval quality,
- and whether evidence supports the claimed assurance level.

Testing procedures should identify where reviewer judgment is expected.

## Automation Potential

Testing procedures may classify automation potential as:

- `High`
- `Medium`
- `Low`
- `Not Recommended`

High automation potential means the check can largely be performed using structured artifacts, schemas, configuration, or logs.

Medium automation potential means automation can support the review, but human judgment remains important.

Low automation potential means review is mainly manual or context-dependent.

Not Recommended means automation may create misleading assurance or overlook important context.

## Initial Testing Procedure CSV

The initial machine-readable testing procedure draft is:

- `assessment/aaef-testing-procedures-v0.4-draft.csv`

This file is intended to provide a first measurable assessment aid linked to the control catalog.

It should be refined over time with more control-specific sampling guidance, thresholds, and evidence expectations.

## Required CSV Fields

The testing procedures CSV should include:

- `Control ID`
- `Domain`
- `Requirement Level`
- `Testing Objective`
- `Testing Method`
- `Required Evidence`
- `Sample Selection`
- `Pass Criteria`
- `Partial Criteria`
- `Fail Conditions`
- `Reviewer Judgment Required`
- `Automation Potential`
- `Notes`

## Non-Goals

This document does not define a certification program.

It does not define audit sufficiency.

It does not claim that passing AAEF testing procedures demonstrates compliance with any external framework.

It does not remove the need for reviewer judgment.

It does not replace organization-specific risk assessment.

## Open Questions

Future work should determine:

- whether control-specific thresholds are needed,
- how sampling should vary by assessment profile,
- how testing procedures should reference evidence event schema fields,
- how testing procedures should connect to external framework mappings,
- how testing procedures should represent automated vs. human review,
- whether additional validation rules are needed for testing procedure quality.
