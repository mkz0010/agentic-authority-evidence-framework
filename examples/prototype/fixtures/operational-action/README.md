# Operational Action Boundary Static Fixtures

Status: Static illustrative fixture family.

This directory contains non-executable static JSON fixtures for an AAEF main Operational Action Boundary Demo candidate:

> Logistics/RPA Shipment Action Boundary

These fixtures are designed to show how a simulated AI or automation proposal can be represented as an action request, checked by an authorization boundary, dispatched or not dispatched, verified or not invoked at a simulated backend boundary, recorded as evidence, and reconstructed by a reviewer.

They are not a logistics product, RPA integration, production automation system, deployment guide, conformance test, certification artifact, audit opinion, legal/compliance determination, evidence sufficiency determination, assessment sufficiency determination, or external-framework equivalence claim.

The file names and field shapes are illustrative fixture structure only; they are not a required AAEF schema, conformance format, or production data model.

`backend-verification.example.json` represents a simulated backend boundary check or non-invocation record, not a real backend integration or backend implementation pattern.

## Fixture paths

- `permitted-shipment-release/` — an allowed shipment hold release path.
- `denied-address-change/` — a denied address change path with non-execution evidence.
- `human-review-required-expedited-shipment/` — a held path requiring human review before dispatch.

Each path contains:

- `action-request.example.json`
- `authorization-decision.example.json`
- `dispatch-decision.example.json`
- `backend-verification.example.json`
- `evidence-event.example.json`
- `reconstruction-notes.example.json`

## How to read one scenario

Start with `action-request.example.json`, then follow the identifiers through `authorization-decision.example.json`, `dispatch-decision.example.json`, `backend-verification.example.json`, `evidence-event.example.json`, and `reconstruction-notes.example.json`.

The point is not to model logistics operations. The point is to see where proposal, authority, dispatch, backend invocation or non-invocation, evidence, and reconstruction are separated.

## Review questions

A reviewer should be able to ask:

1. What did the model or automation propose?
2. What action request was created?
3. What authority or policy boundary was checked?
4. Was dispatch allowed, denied, or held?
5. Was the simulated backend invoked or not invoked?
6. What evidence was recorded?
7. What can a reviewer reconstruct later?

## Boundary

These fixtures do not include:

- live AI calls
- external service calls
- real RPA
- real logistics processing
- real shipment processing
- real address changes
- real backend execution
- real credentials
- real customer data
- scanner behavior
- vulnerability assessment behavior
- exploit execution
- destructive production operations
- AAEF-AI-VA implementation details
- patent-sensitive browser-state or diagnostic reconstruction details
- commercial PoC material
