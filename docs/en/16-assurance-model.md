# 16. Assurance Model

## Status

This document defines an initial AAEF assurance model for v0.2 public review.

It is not a certification scheme and does not claim that implementing AAEF controls eliminates agentic AI risk.

The purpose of this document is to clarify:

- what AAEF controls are intended to assure,
- which security properties they improve,
- which threat areas they relate to,
- what assumptions they depend on,
- and what residual risks may remain.

Related mapping:

- `mappings/threat-control-assurance-mapping.md`
- `mappings/threat-control-assurance-mapping-v0.2-draft.csv`

## Why This Matters

A security framework should define not only what to implement, but also what the implementation is expected to achieve.

AAEF controls are intended to support action assurance for agentic AI systems. They help answer questions such as:

- who or what acted,
- on whose behalf the action occurred,
- what authority was available,
- whether the action was authorized at the point of execution,
- what evidence shows what happened,
- whether authority could be revoked or frozen,
- and what residual risk remains.

Without an assurance model, implementers may overestimate what AAEF provides.

## Assurance Types

AAEF uses the following assurance types.

### Preventive

Controls that help prevent unauthorized, unsafe, overbroad, or policy-violating actions before execution.

Examples:

- action-boundary authorization,
- least-privilege tool configuration,
- constrained delegation,
- high-impact approval thresholds.

### Detective

Controls that help detect ambiguous, abnormal, risky, or policy-relevant conditions.

Examples:

- runtime state checks,
- ambiguity detection,
- provenance and trust metadata,
- approval fatigue metrics.

### Evidentiary

Controls that help produce structured evidence for review, audit, incident reconstruction, or accountability.

Examples:

- evidence event records,
- delegation lineage,
- approval evidence,
- non-execution evidence.

### Responsive

Controls that help stop, isolate, revoke, freeze, recover, or contain agentic risk.

Examples:

- revocation capability,
- conditional authority freeze,
- workflow isolation,
- downstream delegation invalidation.

### Governance

Controls that support ownership, inventory, classification, review, and accountability.

Examples:

- agent inventory,
- high-impact action taxonomy,
- owner assignment,
- control validation process.

## Assurance Strength

AAEF does not assign a universal numeric assurance score to each control.

Assurance strength depends on implementation factors such as:

- whether enforcement happens outside the model,
- whether policy inputs are trusted,
- whether evidence is tamper-evident,
- whether decision artifacts are action-bound,
- whether revocation is timely enough for the workflow,
- whether human approval is meaningful,
- whether controls are tested against realistic attack scenarios,
- and whether residual risks are documented.

In the mapping, assurance strength should be interpreted as contextual rather than absolute.

## What AAEF Does Not Guarantee

AAEF does not guarantee that:

- a model will reason correctly,
- natural-language intent will always be interpreted correctly,
- prompt injection will always be detected,
- semantic influence from untrusted content can always be excluded,
- revocation is instantaneous in distributed systems,
- human approval will always be meaningful,
- evidence is complete unless evidence collection is correctly implemented,
- or an implementation is secure simply because it claims to use AAEF.

AAEF controls reduce and evidence risk. They do not eliminate all risk.

## Trusted Control Boundary Assumption

Several AAEF controls assume that some components are trusted enough to enforce policy and record evidence.

Depending on implementation, the trusted control boundary may include:

- authorization decision point,
- policy store,
- authority verifier,
- revocation checker,
- tool dispatch enforcement point,
- evidence writer,
- identity and delegation verifier,
- approval workflow,
- and tamper-evident evidence storage.

If these components are compromised, bypassed, or implemented inside an untrusted model-controlled path, AAEF control effectiveness may be reduced.

AAEF should therefore be evaluated with explicit implementation assumptions.

## Evidence Assertions and Limitations

Some evidence fields are direct observations. Others are assertions.

For example, a field indicating that untrusted content did not influence an action is not strong evidence unless the event also records:

- who or what determined that assertion,
- what method was used,
- what confidence applies,
- and what limitations remain.

Implementers should distinguish:

- factual observations,
- policy engine decisions,
- runtime tracker outputs,
- human review results,
- model-generated explanations,
- and best-effort implementation assertions.

## Residual Risk

Residual risk is the risk that remains after a control is implemented.

Common residual risks include:

- policy inputs may be wrong or incomplete,
- authority may be overbroad,
- model-generated purpose may be misleading,
- semantic ambiguity may remain unresolved,
- evidence may be incomplete,
- revocation may arrive too late,
- human approval may be rushed or uninformed,
- external agents may not be trustworthy,
- and implementation-specific bypass paths may exist.

AAEF assessments should document residual risk instead of implying complete mitigation.

## How to Use the Mapping

The threat-control assurance mapping should be used to:

1. identify which threats a control is intended to address,
2. classify the assurance type,
3. understand the primary expected effect,
4. identify residual risk,
5. document implementation assumptions,
6. and guide assessment worksheet design.

The mapping should not be used as proof of compliance by itself.

## Review Questions

- Should each AAEF control include assurance type directly in the control catalog?
- Should residual risk be documented per control or per assessment scenario?
- Should assurance strength be qualitative or left implementation-specific?
- Which implementation assumptions should be mandatory for high-impact actions?
- How should this model connect to future assessment worksheets?
