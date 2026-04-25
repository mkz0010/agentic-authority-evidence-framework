# 14. Evidence Event Schema

## Status

This document defines the initial draft of the **AAEF Agentic Action Evidence Event Schema** for public review.

Schema file:

- `schemas/agentic-action-evidence-event.schema.json`

Examples:

- `examples/agentic-action-evidence-event.minimal.json`
- `examples/agentic-action-evidence-event.valid.json`

This schema is intended for AAEF v0.2.0 discussion and review. It is not a certification format and does not guarantee compliance by itself.

## Purpose

AAEF focuses on action assurance for agentic AI systems.

The evidence event schema provides a structured way to record high-impact agentic actions so that an organization can later answer:

1. Who or what acted?
2. On whose behalf did it act?
3. What authority did it have?
4. Was the action allowed at the point of execution?
5. What evidence proves what happened?

The schema is designed to support:

- logging design,
- audit review,
- SIEM or evidence pipeline integration,
- incident reconstruction,
- control testing,
- and future interoperability discussion.

## Design Principles

### 1. Evidence should be structured

A log line such as `send_email success` is not enough for action assurance.

For high-impact actions, evidence should include identity, principal, authority, requested action, authorization decision, result, and evidence metadata.

### 2. Model output is not authority

The schema records the requested action and the authorization decision separately.

A model may propose an action, but the evidence event should show whether that action was authorized at the action boundary.

### 3. Trusted and untrusted inputs should be distinguishable

Agentic AI systems may process external emails, web pages, tickets, documents, tool results, retrieved content, or memory.

The schema includes:

- `trusted_inputs_used`
- `untrusted_inputs_excluded`
- `context.input_sources`
- `untrusted_content_influenced_action`

These fields help show whether untrusted content influenced a high-impact action or was excluded from authorization.

### 4. Evidence should support privacy and minimization

The schema allows references and digests rather than requiring raw sensitive content.

Examples:

- `argument_digest`
- `content_digest`
- `result_digest`
- `evidence_location`
- `privacy_notes`

Implementations should avoid storing unnecessary sensitive data in evidence events.

### 5. Evidence should support incident reconstruction

The schema includes fields such as:

- `correlation_id`
- `trace_id`
- `delegation_chain_id`
- `parent_action_id`
- `tool_result_reference`
- `revocation_reference`
- `incident_reference`

These fields support reconstruction of action sequences, delegation chains, and response actions.

## Required Top-Level Fields

The initial schema requires:

- `schema`
- `schema_version`
- `action_id`
- `timestamp`
- `agent`
- `principal`
- `delegation`
- `requested_action`
- `authorization`
- `result`
- `evidence`

Optional sections include:

- `approval`
- `context`
- `response`
- `extensions`

## Required Evidence Content

The schema is aligned with AAEF-EVD-02.

For high-impact actions, evidence should include at minimum:

- agent identity,
- agent instance,
- principal,
- requested action,
- resource,
- authority scope,
- authorization decision,
- timestamp,
- and result.

## Relationship to Existing Example

AAEF v0.1.x included:

- `examples/agentic-action-evidence-event.json`

That example demonstrated the concept.

This schema turns the evidence event into a structured draft format that can be validated and reviewed.

## Validation

The schema uses JSON Schema Draft 2020-12.

Possible validation tools include:

- `ajv`
- Python `jsonschema`
- IDE or editor JSON Schema support

Example with `ajv`:

```bash
ajv validate -s schemas/agentic-action-evidence-event.schema.json -d examples/agentic-action-evidence-event.valid.json
```

Example with Python:

```bash
python -m jsonschema schemas/agentic-action-evidence-event.schema.json -i examples/agentic-action-evidence-event.valid.json
```

Validation confirms structural conformance only.

It does not prove that:

- the action was safe,
- the authorization was correct,
- the evidence is complete,
- the implementation conforms to AAEF,
- or the organization is compliant with any law or standard.

## Open Questions for Review

Feedback is welcome on:

- Which fields should be required?
- Should `delegation` be required for all high-impact actions, or should authority be represented separately?
- How should privacy-preserving evidence be represented?
- Should raw tool arguments ever be stored?
- Should signatures or tamper-evidence be specified more strictly?
- How should cross-agent evidence be represented?
- How should long-running tasks and principal context degradation be represented?
- Should denied actions and executed actions use the same schema?
- Should the schema be split into action attempt, authorization decision, and execution result events?

## Future Work

Future versions may add:

- Tool Invocation Evidence Profile
- Cross-Agent Evidence Profile
- Principal Context Degradation fields
- High-Impact Action Taxonomy integration
- JSON Schema validation workflow
- example invalid events
- schema versioning policy
