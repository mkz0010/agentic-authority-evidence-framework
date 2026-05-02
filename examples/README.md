# AAEF Examples

This directory contains example artifacts for AAEF.

## Current example sets

- [`examples/evidence/`](evidence/) — active evidence example candidates for AAEF-style agentic action evidence.

## Status and claim boundaries

Examples in this directory are provided to support implementation understanding, evidence design, reconstruction discussion, auditor preparation, consultant discovery, operator readiness, and public review.

These examples do not imply:

- certification,
- compliance,
- audit sufficiency,
- implementation conformance,
- production readiness,
- conformity,
- external framework equivalence,
- complete mitigation,
- or legal/regulatory adequacy.

## Validation

JSON examples should pass syntax validation:

    py tools/validate_json_examples.py

Schema validation is not automatically implied by presence in this directory. If schema validation applies to an example, the example README or validation tooling should say so explicitly.

## Prototype examples

- [Prototype Examples](prototype/README.md) — Non-executable boundary and planned structure for future prototype-facing examples.
