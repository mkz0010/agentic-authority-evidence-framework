# AAEF Evidence Examples

This directory contains active evidence example candidates for AAEF-style agentic action evidence.

## Current examples

| Example | Purpose |
| --- | --- |
| [`permitted-action-evidence.example.json`](permitted-action-evidence.example.json) | Shows a permitted high-impact action with request, authorization, dispatch, backend verification, execution, evidence linkage, and claim-boundary metadata. |
| [`non-execution-evidence.example.json`](non-execution-evidence.example.json) | Shows fail-closed non-execution caused by a resource scope mismatch, including dispatch denial, backend non-invocation, evidence linkage, and claim-boundary metadata. |

## Status

These files are active example candidates.

They are intended to make the v0.6.x evidence planning examples easier to inspect, reuse, and validate at the JSON syntax level.

They are not conformance fixtures, certification artifacts, audit opinions, production-ready implementation examples, or legal/compliance claims.

## Validation

Minimum validation:

    py tools/validate_json_examples.py

Current validation scope:

- JSON syntax validation for `*.example.json` files.

Deferred validation:

- active evidence schema validation,
- cross-reference validation,
- controlled vocabulary validation,
- required claim-boundary metadata validation,
- example freshness/version-reference validation.

Those checks should be added only through explicit follow-up work.

## Claim boundaries

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

They may support:

- implementation understanding,
- evidence design,
- reconstruction discussion,
- auditor preparation,
- consultant discovery,
- operator readiness,
- and public review.

## Related planning artifacts

- `docs/en/status/v060-active-evidence-example-candidate-review.md`
- `docs/en/status/v060-active-example-placement-and-validation-planning.md`
- `docs/en/status/v060-permitted-action-evidence-example-planning.md`
- `docs/en/status/v060-non-execution-evidence-example-planning.md`
