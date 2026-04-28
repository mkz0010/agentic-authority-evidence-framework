# 16. Assurance Model

## Status

This document originated as an initial AAEF assurance model during the v0.2 public review cycle and remains part of the current v0.4.1 Public Review Draft baseline.

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

### Assertion Source Limitations

AAEF assurance depends not only on the presence of evidence, but also on the trustworthiness of the component that generated each evidence assertion.

Implementers and assessors should distinguish between:

- direct observations from trusted enforcement components,
- policy engine decisions,
- provenance or source-tracking metadata,
- backend execution records,
- independent evidence pipeline records,
- human reviewer assertions,
- model-generated explanations,
- and best-effort implementation assertions.

For high-impact actions, model-generated claims about input influence, authorization correctness, or safe execution should not be treated as equivalent to independently generated enforcement or evidence records.

This is particularly important when evaluating prompt injection, indirect prompt injection, RAG-sourced content, external messages, user-uploaded files, memory, or agent-to-agent inputs.

If the source, method, confidence, or limitations of an assertion are unclear, the assurance conclusion should be weakened or recorded as a residual evidence limitation.

### Evidence Quality Limitations

AAEF evidence supports reviewability and reconstructability, but evidence does not establish truth by itself.

The strength of an assurance conclusion depends on the trustworthiness of the components that generated, protected, correlated, and retained the evidence.

For high-impact actions, evidence generated only by the model or Agent Runtime should not be treated as equivalent to evidence generated by trusted authorization, dispatch enforcement, backend, or independent evidence pipeline components.

Assessment results should distinguish between:

- structurally valid evidence,
- independently generated evidence,
- tamper-evident evidence,
- and weak or self-reported evidence.

A strong assurance conclusion should not rely solely on model-generated explanations, screenshots, unverified assertions, or mutable logs for high-impact actions.

### Assertion Source Strength

The strength of an assurance conclusion depends on the source of the assertion, not only on the presence of an evidence field.

An evidence event may contain assertions about authorization, input influence, policy state, dispatch, execution, approval, or trust state. These assertions have different assurance value depending on who or what generated them.

AAEF should treat assertion sources as having different evidentiary strength.

| Assertion source | Typical assurance strength | Notes |
|---|---|---|
| Trusted enforcement component | Strong | Examples include a Tool Dispatch Enforcement Point, authorization gateway, or enforcement layer outside the model-controlled runtime. |
| Backend or tool relying-party record | Strong | Stronger when the backend verifies authorization, dispatch attestation, request digest, or equivalent enforcement proof. |
| Policy engine decision | Strong | Stronger when the policy decision is action-bound, versioned, and linked to the executed operation. |
| Evidence pipeline or SIEM correlation | Strong to moderate | Stronger when independently retained, correlated, and protected against tampering. |
| Human reviewer assertion | Moderate | Useful when the reviewed action, evidence, and approval context are clear and action-bound. |
| Application runtime self-report | Moderate to weak | Depends on runtime isolation, privilege, evidence retention, and whether the runtime is inside the trusted boundary. |
| Agent runtime self-report | Weak | Should not be treated as strong evidence for high-impact actions without corroboration. |
| Model self-assessment | Very weak / advisory | Should not be treated as sufficient evidence of authorization, non-influence, or safe execution for high-impact actions. |
| Unknown or missing assertion source | Insufficient | Missing assertion source should be recorded as an evidence limitation. |

This hierarchy is not a certification scale.

It is intended to help assessors distinguish between evidence that was independently generated by trusted components and evidence that was asserted by the model, agent runtime, or implementation under review.

For high-impact actions, strong assurance usually requires evidence generated or corroborated by components outside the model-controlled path.

### Evidence Quality Assessment Principles

Evidence quality assessment should distinguish between:

- structural validity,
- source trustworthiness,
- action binding,
- independence,
- integrity protection,
- correlation,
- and reconstructability.

Structural validity means that an evidence event conforms to the expected schema.

Meaningful evidence means that the evidence can support an assurance conclusion about what was proposed, authorized, dispatched, executed, denied, deferred, escalated, or reviewed.

An evidence event can be structurally valid but still weak for assurance.

Examples include:

- a valid event generated only by the agent runtime,
- a valid event with no action-bound authorization reference,
- a valid event with no dispatch or backend execution correlation,
- a valid event with model-only input influence assertions,
- or a valid event stored in mutable logs without integrity protection.

For high-impact actions, assessors should avoid treating schema validity as equivalent to assurance strength.

Evidence quality depends on whether the evidence can support later review, audit, and incident reconstruction.

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
