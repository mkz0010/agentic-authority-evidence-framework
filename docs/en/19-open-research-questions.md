# Open Research Questions

## Status

This document collects open research questions related to the Agentic Authority and Evidence Framework (AAEF).

These questions are not AAEF control requirements.

They are intended to help researchers, students, reviewers, and implementers identify areas where further empirical study, measurement, experimentation, or formalization may be useful.

## Purpose

AAEF is primarily an action assurance framework for agentic AI systems.

However, several AAEF concepts are intentionally not fully solved by the framework itself. They involve measurement limits, system design tradeoffs, human factors, runtime behavior, and adversarial conditions that require additional research.

This document makes those open questions explicit.

The goal is to clarify:

- what AAEF currently treats as unresolved,
- what can be measured or studied,
- where empirical validation would be useful,
- and how real-world incidents or proof-of-concept attacks can be mapped to AAEF controls and evidence concepts.

## Scope Note

This document should not be read as an implementation checklist.

Implementation guidance remains in:

- `docs/en/12-assessment-quick-start.md`
- `docs/en/14-evidence-event-schema.md`
- `docs/en/16-assurance-model.md`
- `docs/en/17-reference-architecture.md`

This document is research-facing and intentionally exploratory.

## Principal Context Degradation

Principal Context Degradation refers to the loss, weakening, staleness, or ambiguity of the principal context under which an agentic AI system acts.

Open questions include:

- How can principal context degradation be measured in long-running agentic tasks?
- What signals indicate that an agent no longer has sufficient fresh authority to continue acting?
- How should session age, task duration, task drift, delegation depth, and environmental changes affect authorization?
- When should an agent require reauthorization due to context degradation?
- How can systems distinguish ordinary task continuation from authority drift?

Possible measurement signals include:

- session age,
- task duration,
- delegation depth,
- authority age,
- intent drift,
- environment state change,
- tool risk escalation,
- context source volatility,
- and human confirmation freshness.

## Delegation Chain Risk

AAEF treats delegation lineage and authority attenuation as important for reconstructability.

Open questions include:

- How does delegation chain depth correlate with incident risk?
- At what delegation depth does authority become difficult to reconstruct?
- How should downstream agents inherit, attenuate, or lose authority?
- What evidence is needed to reconstruct multi-step delegation decisions?
- How should redelegation limits be represented and enforced?

## Evidence Quality Gate Effectiveness

AAEF distinguishes between structurally valid evidence and meaningful evidence.

Open questions include:

- How can the effectiveness of an Evidence Quality Gate be empirically tested?
- Which evidence artifacts are most predictive of successful incident reconstruction?
- Can weak evidence patterns be detected automatically?
- Which evidence gaps most strongly correlate with failed audit review?
- What minimum evidence set is necessary for high-impact action assurance?

Examples of evidence quality questions include:

- whether model-only explanations should ever support a Pass result,
- whether screenshots can be useful as supporting evidence,
- when mutable logs are insufficient,
- and how to evaluate action-bound authorization evidence.

## Weak and Adversarial Evidence Patterns

Some evidence is merely weak. Other evidence patterns may be adversarial.

Open questions include:

- How can systems detect approval laundering?
- How can replayed authorization decision artifacts be detected?
- How should action digest mismatch be classified?
- What evidence proves that a human approval was bound to the canonical action actually executed?
- How should systems detect payload substitution after approval?
- Can adversarial evidence patterns be identified before incident review?

These questions are relevant because schema-valid evidence may still fail to prove that the executed action matched the authorized action.

## Untrusted Input Influence

AAEF does not assume that semantic influence can always be proven with certainty.

Open questions include:

- What are the practical limits of detecting untrusted input influence?
- How should systems distinguish source presence from semantic influence?
- What level of source tracking is feasible without overclaiming certainty?
- How should runtime tracking, retrieval provenance, policy evaluation, human review, and model self-assessment be weighted?
- Should `confidence` be used at all, or should systems instead record determination basis and limitations?

A key research risk is that a numeric or subjective confidence value may imply measurement precision that does not actually exist.

Alternative approaches may include:

- `determined_by`,
- `determination_basis`,
- `model_self_assessment_only`,
- and `limitations`.

## Human Approval Fatigue

Human approval is not automatically meaningful approval.

Open questions include:

- Under what frequency, context, or risk conditions does human approval become ineffective?
- How often do humans approve agentic actions without understanding the canonical action?
- What evidence should prove that approval was meaningfully bound to the action?
- How should approval prompts present risk, scope, resource, operation, and external effect?
- What is the relationship between approval frequency and approval quality?

## Dispatch Integrity and TDE Bypass

AAEF treats the Tool Dispatch Enforcement Point as a critical boundary for high-impact actions.

Open questions include:

- How can systems prove that a tool action passed through an approved dispatch enforcement point?
- What evidence is sufficient to detect TDE bypass?
- How should backend APIs verify dispatch attestation?
- How should canonical action requests be bound to authorization decisions?
- How should credential isolation be measured or evidenced?
- What evidence proves that a model-influenced runtime could not directly invoke high-impact tools?

## Multi-Agent and Cross-Agent Authority

Multi-agent and cross-agent authority are important, but not fully addressed in the current AAEF draft.

Open questions include:

- How should authority propagate across agents?
- How should downstream agents prove inherited authority?
- How should cross-agent evidence be correlated?
- How should one agent’s output be treated when it becomes another agent’s input?
- How should revocation propagate across agent chains?
- How should organizations prevent authority amplification across agent boundaries?

These questions may be candidates for a later AAEF phase after Evidence Profiles, Evidence Quality, Assertion Sources, and Dispatch Integrity are more stable.

## Incident Mapping

AAEF can be evaluated against real-world incidents, public research, and proof-of-concept attacks.

Open questions include:

- Which AAEF controls map to known agentic AI incidents?
- Which controls would have prevented, detected, or limited the incident?
- What evidence would have been needed to reconstruct the action chain?
- Which failures involved untrusted input influence?
- Which failures involved excessive tool authority?
- Which failures involved missing authorization or dispatch enforcement?
- Which failures involved weak or misleading evidence?

Potential incident categories include:

- agentic assistant misuse,
- CI/CD agent compromise,
- indirect prompt injection,
- tool or credential misuse,
- cross-context data leakage,
- approval laundering,
- and autonomous or semi-autonomous cyber operations.

## Research Use Cases

Possible research projects include:

- applying the AAEF control catalog to real-world agentic AI security incidents,
- evaluating Evidence Quality Gate effectiveness,
- proposing metrics for Principal Context Degradation,
- analyzing delegation chain depth and incident risk,
- measuring human approval fatigue,
- evaluating untrusted input influence detection limits,
- and comparing AAEF with existing AI security or cloud assurance frameworks.

## Non-Goals

This document does not claim that AAEF has solved these research questions.

It also does not make these questions mandatory implementation requirements.

The purpose is to make open problems visible, so that future research, review, implementation experience, and incident analysis can improve the framework.
