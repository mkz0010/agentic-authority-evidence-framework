# Contributing to AAEF

AAEF is currently in **Public Review Draft** status.

Contributions are welcome in the form of:

- issue reports,
- terminology improvements,
- control requirement feedback,
- threat model additions,
- evidence requirement suggestions,
- mappings to existing frameworks,
- examples and implementation notes,
- reference architecture proposals.

## Feedback Priorities for v0.1

The most useful feedback at this stage is:

1. **Control requirement precision** — ambiguous, excessive, missing, or untestable controls.
2. **Threat-to-control mapping** — especially prompt injection, delegation abuse, approval laundering, and evidence gaps.
3. **Evidence requirements** — fields, retention, attribution, tamper-evidence, privacy minimization, and incident reconstruction.
4. **Implementation notes** — patterns for preserving principal context, enforcing action-boundary authorization, and revoking downstream delegations.
5. **Framework mappings** — OWASP Agentic AI risks, CSA ATF, NIST AI RMF, OpenID/OAuth-related work, MCP/A2A, FINOS, and sector-specific controls.
6. **Operational maturity** — when Level 4 autonomy is inappropriate, and what prerequisites should be required.

## Contribution Principles

Please keep contributions aligned with the core scope of AAEF:

- delegated authority,
- policy-enforced action boundaries,
- verifiable evidence,
- risk-based human approval,
- revocable trust,
- auditability of high-impact agentic actions.

AAEF is not intended to become a general-purpose AI ethics framework, model evaluation benchmark, agent communication protocol, or identity protocol.

## Suggested Issue Types

- Ambiguous definition
- Missing control
- Missing threat
- Evidence requirement improvement
- Existing framework mapping
- Implementation note
- Editorial improvement

## Style

Use clear, implementation-neutral language.

Where possible, separate:

- requirement,
- objective,
- applicability,
- testing procedure,
- evidence examples.

## Control Catalog Consistency

The normative control catalog is `controls/aaef-controls-v0.1.csv`.

When adding, removing, or renaming a control, update both:

- `controls/aaef-controls-v0.1.csv`
- `docs/en/07-control-requirements.md`

Then run:

```bash
python tools/validate_control_catalog.py
```

## License

By contributing, you agree that your contribution will be licensed under CC BY 4.0 unless otherwise stated.
