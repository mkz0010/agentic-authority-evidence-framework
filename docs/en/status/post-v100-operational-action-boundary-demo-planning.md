# Post-v1.0.0 Operational Action Boundary Demo Planning

Status: Non-normative planning and review artifact.

This document proposes a narrow AAEF main public demo planning track.

The proposed demo theme is:

> Operational Action Boundary Demo: Logistics RPA Shipment Action Boundary

This document does not add demo fixtures, update validators, update examples, update the root README, update the active baseline, open a v1.1.0 roadmap, or approve production implementation work.

The active baseline remains AAEF v0.4.1 unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

AAEF v1.0.0 remains a conservative release path planning release.

## Purpose

AAEF main may benefit from a small public-facing demo that explains the core thesis:

> Model output is not authority.

The purpose of this planning artifact is to decide whether AAEF main should prepare an illustrative demo that shows how an AI or automation proposal becomes an action request, is checked by an authorization boundary, is dispatched or not dispatched, is verified or not invoked at the backend boundary, and leaves evidence for later review.

The initial proposed domain is operational automation rather than vulnerability assessment, code review, compliance mapping, or AAEF-AI-VA implementation.

## Reader-stage assumption

AAEF readers may arrive at different stages.

At the current public-framework stage, many readers are still likely to be in a concept-understanding stage:

- What does `Model output is not authority` mean?
- Why is AI-generated intent different from executable authority?
- Why should authorization, dispatch, backend verification, evidence, and review be separated?
- Why is non-execution evidence useful?

For those readers, a static illustrative fixture may be the right first public demo.

However, pilot or adoption evaluators may quickly move to a different question:

> If we introduce AAEF-style boundaries into our system, what changes?

For those readers, static artifacts may not be enough. A later minimal executable proof-of-concept may be useful if it shows only the boundary mechanics without claiming production readiness or implementation sufficiency.

This planning track therefore separates:

- static explanatory demo needs, and
- possible later minimal executable demo needs.

## Motivation

AAEF-AI-VA is an Applied Implementation with separate commercial, safety, operational, public-exposure, and patent-sensitive boundaries.

AAEF-AI-VA should not become the primary public demo of AAEF main.

AAEF main should be able to explain the framework using a safe, static, domain-neutral operational action-boundary example that does not depend on vulnerability assessment, scanner behavior, customer PoC material, commercial implementation detail, or AAEF-AI-VA technical design.

A logistics/RPA-style shipment action boundary is a useful first candidate because it is concrete, operational, understandable to non-security readers, and naturally supports permitted, denied, and human-review-required paths.

## RPA-plus-AI trust-transfer problem

The key reader-facing motivation is the RPA-plus-AI trust-transfer problem.

Rule-based RPA and operational automation may already be trusted because they are deterministic, bounded by known procedures, and embedded in existing business workflows.

When AI recommendations are introduced into the same execution path, that existing trust can be carried over without re-examining the authorization boundary.

AAEF should make that boundary visible.

The relevant question is not only:

> Did the AI formally have authority?

The more important review question may be:

> Did the system preserve a visible boundary between automation output, action request, authorization decision, dispatch, backend verification, evidence, and reviewer reconstruction?

## Proposed demo theme

The proposed first theme is:

> Operational Action Boundary Demo: Logistics RPA Shipment Action Boundary

The demo should show that automation or AI-assisted workflow output may propose shipment-related actions, but execution authority remains separate.

The demo should focus on the action boundary, not on logistics product design.

The scenario should remain static and illustrative unless a later issue explicitly approves a minimal executable proof-of-concept.

## Proposed scenario paths

The initial demo planning should consider three static paths.

### 1. Permitted shipment release

The automation proposes releasing a normal shipment hold.

The action may be permitted when:

- payment is confirmed
- item value is within the automation's allowed range
- no address change is involved
- no fraud or exception flag is present
- inventory is confirmed
- the action is within the actor's assigned operational scope

Expected AAEF path:

- action request created
- authorization decision allows the action
- dispatch decision forwards the action to the backend
- backend verification accepts the authorized request
- evidence records execution
- reviewer can reconstruct why the action was executed

This path shows that AAEF does not prohibit automation. It separates automation output from execution authority.

### 2. Denied address change / non-execution

The automation proposes applying a delivery address change.

The action may be denied when:

- the order is high value
- the new address is not previously associated with the customer
- identity verification is incomplete
- fraud risk is elevated
- the request is based only on unverified support notes

Expected AAEF path:

- action request created
- authorization decision denies the action
- dispatch decision refuses to forward the action
- backend is not invoked
- evidence records non-execution
- reviewer can reconstruct why the action was not executed

This path demonstrates non-execution evidence. The action did not happen, and that fact is itself recorded as reviewable evidence.

### 3. Human review required expedited shipment

The automation proposes expediting a high-value shipment.

The action may require human review when:

- the shipment is high value
- the customer is under a special contract or SLA
- the decision may affect inventory allocation
- additional cost or exception handling is involved
- the operational risk is not suitable for automatic execution

Expected AAEF path:

- action request created
- authorization decision requires human review
- dispatch decision refuses automatic execution
- backend is not invoked pending review
- evidence records the pending or non-executed state
- reviewer can see that automation did not directly execute the shipment action

This path demonstrates that human review is not merely a button click. The review boundary should preserve what was reviewed, by whom, under what authority, and within what scope.

## Static demo vs minimal executable demo

The first public AAEF main demo should distinguish two different reader needs.

A static fixture helps readers understand the concept:

- model or automation output is not authority
- action requests should be bounded
- authorization should be separate from proposal
- dispatch should be controlled
- backend verification should not rely only on model output
- evidence should support later reconstruction
- non-execution should be recorded when relevant

A minimal executable demo would serve a different purpose. It would help readers imagine what changes when AAEF-style boundaries are inserted into their own system.

The minimum executable proof-of-concept should show only three dynamic moments:

1. an action request is created from an AI or automation proposal
2. an authorization gate allows, denies, or holds the request
3. an evidence record is produced for later reconstruction

A later minimal executable demo does not need:

- live AI
- real RPA
- external services
- real shipment processing
- real address changes
- real credentials
- real customer data
- production backend execution
- vulnerability assessment behavior
- scanner behavior
- exploit execution
- customer PoC material

Static fixtures are appropriate for the current AAEF main public explanation stage.

A minimal executable demo may become appropriate later when readers move from concept understanding to adoption or pilot evaluation.

## Demo ladder

A useful public explanation path may be staged as follows.

| Level | Purpose | Possible form | Intended reader |
| --- | --- | --- | --- |
| Level 0: Minimal Use Guide | Explain how to begin an AAEF review conversation. | `docs/en/minimal-use-guide.md` | First-time reader |
| Level 1: Static Action Boundary Demo | Show the concept through static request / decision / dispatch / evidence chains. | Static fixtures and walkthrough | Concept-understanding reader |
| Level 2: Minimal Executable Boundary Demo | Show how request creation, gate decision, and evidence generation move. | Local mock CLI or script with no external services | Adoption or pilot evaluator |
| Level 3: Applied Implementation | Show a domain-specific implementation. | AAEF-AI-VA or other applied implementation | Implementation-specific evaluator |

This document only plans Level 1 and records the possible future need for Level 2.

It does not approve Level 2 implementation.

## Why logistics/RPA as the first demo

A logistics/RPA scenario appears stronger than a software-maintenance example as the first AAEF main demo.

A software-maintenance example is valuable, but it may be misread as an AI code-review safety sample.

A logistics/RPA example is more clearly about operational action authority.

The logistics/RPA example is useful because it is:

- not a vulnerability assessment scenario
- not tied to AAEF-AI-VA
- not a code-review example
- not dependent on commercial implementation details
- understandable to non-security readers
- close to real-world automation
- connected to physical or operational consequences
- suitable for showing allowed, denied, and human-review-required paths
- suitable for demonstrating non-execution evidence

It also avoids making the first public demo appear to be a scanner, compliance tool, audit system, or production automation product.

## Proposed later repository work

This planning artifact does not perform these changes.

If approved later, follow-up issues may consider:

1. Example orientation cleanup
   - `examples/README.md`
   - `examples/prototype/README.md`
   - `docs/en/document-map.md`
   - possibly the root `README.md` as a short first-stop link only

2. Static fixture addition
   - `examples/prototype/fixtures/operational-action/`
   - `permitted-shipment-release/`
   - `denied-address-change/`
   - `human-review-required-expedited-shipment/`

3. Static fixture file family
   - `action-request.example.json`
   - `authorization-decision.example.json`
   - `dispatch-decision.example.json`
   - `backend-verification.example.json`
   - `evidence-event.example.json`
   - `reconstruction-notes.example.json`

4. Prototype fixture validation
   - required files exist
   - JSON files are valid objects
   - correlation identifiers match
   - action type is consistent across the chain
   - authorization and dispatch decisions are consistent
   - backend invocation or non-invocation is consistent with dispatch
   - evidence outcome matches the scenario path
   - static/demo boundary fields are present where applicable

5. Reviewer walkthrough
   - what did the model or automation propose?
   - what action request was created?
   - what authority was checked?
   - was the action dispatched?
   - was the backend invoked?
   - what evidence was recorded?
   - can a reviewer reconstruct why the action was executed, denied, or held for review?

Any such follow-up should preserve the non-normative and claim-boundary posture.

## Boundary against AAEF-AI-VA

AAEF-AI-VA should remain an Applied Implementation with separate commercial, safety, public-exposure, and patent-sensitive boundaries.

This AAEF main demo should not import:

- AAEF-AI-VA implementation details
- scanner behavior
- tool gateway commercial design
- vulnerability assessment workflows
- customer PoC details
- patent-sensitive browser-state or diagnostic reconstruction detail
- commercial licensing or delivery material

The relationship should remain:

- AAEF main: public framework explanation and static action-boundary examples
- AAEF-AI-VA: applied implementation in the vulnerability-assessment domain

## Deferred example families

The following example families may be considered later, but should not be the first demo:

- Data Release / External Communication Boundary Demo
- Payment RPA Action Boundary Demo
- Financial Trading Bot Boundary Demo
- Software Maintenance Action Boundary Demo

Payment RPA is closely related to this demo's framing because it also involves existing operational automation, trust transfer, monetary impact, and authority-sensitive execution. It may be a strong next candidate after the logistics/RPA framing is reviewed.

The software-maintenance scenario is valuable, but it should be deferred because it may be misread as an AI code-review sample. It can be introduced later once the operational action-boundary framing is already clear.

## Non-goals

This planning artifact does not introduce:

- production automation system
- logistics product
- scanner
- vulnerability assessment behavior
- AAEF-AI-VA implementation detail
- commercial PoC material
- customer deployment guidance
- legal sufficiency claim
- audit sufficiency claim
- compliance sufficiency claim
- evidence sufficiency claim
- assessment sufficiency claim
- certification claim
- conformity claim
- external-framework equivalence claim
- production readiness claim
- live AI call
- external service call
- real shipment processing
- real address change
- real backend execution
- real credential use
- real customer data
- exploit execution
- destructive production operation

The demo should remain static and illustrative unless a future issue explicitly scopes a minimal executable proof-of-concept.

## Suggested first review questions

1. Is an Operational Action Boundary Demo appropriate for AAEF main?
2. Does the logistics/RPA scenario explain `Model output is not authority` better than a code-review or vulnerability-assessment example?
3. Does the proposal make the RPA-plus-AI trust-transfer problem visible? That is, does it show how trust established for rule-based automation may be carried over to AI-assisted workflows without re-examining the authorization boundary?
4. Does the proposed scope avoid AAEF-AI-VA commercial, safety, public-exposure, and patent-sensitive boundary risks?
5. Does the demo clearly distinguish model/automation output, action request, authorization, dispatch, backend verification, evidence, and reviewer reconstruction?
6. Does the static vs minimal executable demo distinction help avoid over-building too early?
7. Does the document avoid implying production readiness, certification, audit sufficiency, legal sufficiency, compliance sufficiency, evidence sufficiency, assessment sufficiency, or external-framework equivalence?
8. Should this begin as a planning/status document before adding new fixtures, validators, or README links?

## Recommended initial decision

Approve a narrow planning track for an AAEF main static demo:

> Operational Action Boundary Demo: Logistics RPA Shipment Action Boundary

Initial scope should be limited to this planning document.

Static fixtures, example-orientation cleanup, prototype validators, README links, walkthroughs, and any minimal executable proof-of-concept should be handled only by later, separately scoped follow-up issues.
