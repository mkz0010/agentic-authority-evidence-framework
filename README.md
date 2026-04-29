# Agentic Authority & Evidence Framework / AAEF

[![Validate AAEF Artifacts](https://github.com/mkz0010/agentic-authority-evidence-framework/actions/workflows/validate-aaef-artifacts.yml/badge.svg)](https://github.com/mkz0010/agentic-authority-evidence-framework/actions/workflows/validate-aaef-artifacts.yml)

**AAEF: An Action Assurance Control Profile for Agentic AI Systems**

Agentic Authority & Evidence Framework (AAEF) is a practical control framework for governing **delegated authority**, **policy-enforced action boundaries**, and **verifiable evidence** in agentic AI systems.

AAEF is designed for AI agents that do more than generate text. It focuses on agents that can call tools, access data, delegate tasks, interact with other agents, and perform meaningful actions on behalf of humans or organizations.

## Core Position

AAEF shifts agentic AI security from **trusting model behavior** to **governing authorized action**.

Traditional AI risk management often asks whether a model is accurate, safe, explainable, aligned, or trustworthy. Those questions remain important, but they are not sufficient when AI agents can take action.

For agentic AI systems, the operational question becomes:

> Was this action authorized, bounded, attributable, and evidenced?

AAEF exists to answer that question.

## What AAEF Focuses On

AAEF focuses on five practical assurance questions:

1. **Who or what acted?**
2. **On whose behalf did it act?**
3. **What authority did it have?**
4. **Was the action allowed at the point of execution?**
5. **What evidence proves what happened?**

If an organization cannot answer these questions, it cannot reliably govern agentic AI systems in production.

## What AAEF Is Not

AAEF does **not** define a new identity protocol, authentication protocol, authorization protocol, or agent communication protocol.

AAEF does **not** replace AI governance frameworks, Zero Trust frameworks, identity standards, agent communication standards, or threat taxonomies.

Instead, AAEF is intended to complement them by defining action assurance controls for high-impact AI agent actions.

## Language / Translations

The English version of this repository is the authoritative version.

The following translated README files are provided for reference only. They are based on machine translation and may contain inaccurate, incomplete, or ambiguous terminology.

If there is any conflict or inconsistency between a translated README and the English documentation, the English version prevails.

- [English](README.md) — authoritative
- [日本語 / Japanese](README.ja.md) — reference translation
- [简体中文 / Simplified Chinese](README.zh-CN.md) — reference translation
- [한국어 / Korean](README.ko.md) — reference translation

For security, compliance, audit, or implementation decisions, refer to the English documentation under `docs/en/`.

## Articles and Announcements

The following articles introduce the motivation, design concepts, and technical background of AAEF.

- [Model Output Is Not Authority: Action Assurance for AI Agents](https://dev.to/mkz0010/model-output-is-not-authority-action-assurance-for-ai-agents-4ljd) — DEV Community
- [AIエージェント時代に必要なのは「モデルを信じること」ではなく「行為を統治すること」だ](https://zenn.dev/mkz0010/articles/bc7b94b515b8b5) — Zenn
- [Prompt Injection対策を「プロンプト」ではなく「実行境界」で考える](https://qiita.com/mkz0010/items/244d97087146a3038ac8) — Qiita
- [AAEF v0.1.3 Public Review Draft announcement](https://www.linkedin.com/feed/update/urn:li:activity:7453853837167263744/) — LinkedIn

These articles are explanatory materials. The authoritative documentation remains this repository, especially the English README and `docs/en/`.

## Intended Audience

AAEF is intended for:

- security architects,
- AI application developers,
- AI governance teams,
- internal audit teams,
- compliance teams,
- risk management teams,
- platform engineering teams,
- and organizations preparing to deploy tool-using or autonomous AI agents.

## Document Status

**AAEF v0.5.0 Public Review Planning Release** is the latest public review planning release.

AAEF v0.5.0 is a non-normative planning and design-clarification release. It adds planning models and incorporation guidance for authority lifecycle, evidence integrity, approval quality, and future v0.5.x work. AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

Earlier v0.3.x, v0.2.x, and v0.1.x releases remain available as prior public review baselines.

The current control catalog file remains:

- `controls/aaef-controls-v0.1.csv`

The file name is retained for continuity, but the catalog contains the current public review control set.

The v0.4.x Public Review Draft includes:

- preliminary OWASP Agentic Top 10 2026 mapping,
- Agentic Action Evidence Event JSON Schema,
- Evidence Event Schema validation workflow,
- High-Impact Action Taxonomy draft,
- Reference Architecture,
- Assurance Model and Residual Risk Mapping,
- Assessment Quick Start,
- Assessment Worksheet draft,
- Evidence Quality Gate assessment criteria,
- Assessment Profiles and tiered applicability guidance,
- Assessment Profile Mapping sidecar CSV,
- TCB implementation capability patterns,
- Action Sequence Monitoring and Task Splitting guidance,
- Assessment Automation and Human Review Classification guidance,
- Infrastructure and SIEM Evidence Integration guidance,
- Control Catalog Versioning and Change Impact guidance,
- Testing Procedures and Pass Criteria guidance,
- machine-readable testing procedure draft,
- High-Impact and Audit-Grade Pre-qualification Gate guidance,
- Trusted Control Boundary Integrity Requirements,
- External Framework Mapping Methodology,
- initial conservative external framework mapping draft,
- validation for testing procedures and external mappings,
- and historical release preparation records under `docs/en/release/`.

AAEF v0.5.0 remains a public review planning release. It is not a certification scheme, formal standard, implementation conformance claim, audit opinion, compliance equivalence, or claim of complete mitigation.

Feedback, issues, and pull requests are welcome.

## Start Here

If you are new to AAEF, start with the documents below:

1. [`docs/en/13-one-page-overview.md`](docs/en/13-one-page-overview.md) — quick mental model and current public review baseline
2. [`docs/en/02-core-principles.md`](docs/en/02-core-principles.md) — core principles, including “Model output is not authority”
3. [`docs/en/17-reference-architecture.md`](docs/en/17-reference-architecture.md) — how the model, authorization, enforcement, and evidence layers relate
4. [`docs/en/06-control-domains.md`](docs/en/06-control-domains.md) — control domain overview
5. [`docs/en/07-control-requirements.md`](docs/en/07-control-requirements.md) — detailed control requirements
6. [`docs/en/14-evidence-event-schema.md`](docs/en/14-evidence-event-schema.md) — evidence event schema and evidence model
7. [`docs/en/12-assessment-quick-start.md`](docs/en/12-assessment-quick-start.md) — how to start reviewing a system using AAEF
8. [`docs/en/20-assessment-profiles.md`](docs/en/20-assessment-profiles.md) — draft assessment profiles and tiered applicability guidance
9. [`docs/en/25-testing-procedures-and-pass-criteria.md`](docs/en/25-testing-procedures-and-pass-criteria.md) — testing procedures, pass criteria, evidence expectations, and reviewer judgment guidance
10. [`docs/en/26-high-impact-audit-grade-prequalification.md`](docs/en/26-high-impact-audit-grade-prequalification.md) — pre-qualification gate for High-Impact and Audit-Grade assessment profiles
11. [`docs/en/27-trusted-control-boundary-integrity.md`](docs/en/27-trusted-control-boundary-integrity.md) — integrity requirements for the Trusted Control Boundary
12. [`docs/en/28-external-framework-mapping-methodology.md`](docs/en/28-external-framework-mapping-methodology.md) — informative external framework mapping methodology

## Role-Based Reading Paths

| Reader | Start with | Then read | Deep dive |
|---|---|---|---|
| New readers | [`One-page Overview`](docs/en/13-one-page-overview.md) | [`Core Principles`](docs/en/02-core-principles.md) | [`Introduction`](docs/en/00-introduction.md) / [`Scope`](docs/en/01-scope.md) |
| Implementers | [`Reference Architecture`](docs/en/17-reference-architecture.md) | [`Control Requirements`](docs/en/07-control-requirements.md) | [`Evidence Event Schema`](docs/en/14-evidence-event-schema.md), examples, and validation tools |
| Security architects | [`Reference Architecture`](docs/en/17-reference-architecture.md) | [`Threat Model`](docs/en/04-threat-model.md) / [`Trust Model`](docs/en/05-trust-model.md) | Controls and mappings |
| Auditors / assessors | [`Assessment Quick Start`](docs/en/12-assessment-quick-start.md) | [`Assessment Profiles`](docs/en/20-assessment-profiles.md) and [`Control Requirements`](docs/en/07-control-requirements.md) | Assessment worksheet and [`Assurance Model`](docs/en/16-assurance-model.md) |
| Governance / risk teams | [`One-page Overview`](docs/en/13-one-page-overview.md) | [`High-Impact Action Taxonomy`](docs/en/11-high-impact-action-taxonomy.md) and [`Assessment Profiles`](docs/en/20-assessment-profiles.md) | [`Relationship to Existing Frameworks`](docs/en/09-relationship-to-existing-frameworks.md) and [`Assurance Model`](docs/en/16-assurance-model.md) |

## How the Core Documents Fit Together

| Document | What it answers | Practical role |
|---|---|---|
| [`Control Requirements`](docs/en/07-control-requirements.md) | What must be controlled? | Defines requirements, review criteria, and assessment items |
| [`Reference Architecture`](docs/en/17-reference-architecture.md) | Where should controls be enforced? | Shows responsibility separation across model, authorization, dispatch, tools, and evidence |
| [`Evidence Event Schema`](docs/en/14-evidence-event-schema.md) | What evidence should exist? | Defines structured evidence for audit logs, SIEM events, incident reconstruction, and evidence review |
| [`Assessment Worksheet`](assessment/aaef-assessment-worksheet-v0.2-draft.csv) | How should controls be reviewed? | Supports applicability review, evidence review, findings, residual risk, and remediation tracking |
| [`Assessment Profiles`](docs/en/20-assessment-profiles.md) | How deeply should AAEF be applied? | Provides draft Lite, Standard, High-Impact, and Audit-Grade applicability guidance based on action risk and agent autonomy |
| [`Assessment Profile Mapping`](assessment/aaef-assessment-profiles-v0.3-draft.csv) | Which controls are expected under each profile? | Provides a sidecar profile applicability mapping without changing the Control Catalog |

In short:

```text
Control Requirements define what must be true.
Reference Architecture shows where those controls are enforced.
Evidence Event Schema records what happened and why.
Assessment Worksheet helps review whether the controls and evidence exist.
```

## Control Catalog Source of Truth

The control catalog CSV is the machine-readable source of truth for control IDs, requirement text, objectives, applicability, testing procedures, evidence examples, and maturity classification.

Current catalog file:

- `controls/aaef-controls-v0.1.csv`

The file name is retained for continuity. The catalog remains the current machine-readable control source of truth unless superseded by a later catalog file.

Control catalog versioning and change impact guidance is documented in [`docs/en/24-control-catalog-versioning.md`](docs/en/24-control-catalog-versioning.md).

The Markdown control list in `docs/en/07-control-requirements.md` is maintained for readability and must remain consistent with the CSV catalog. This repository includes a validation script and GitHub Actions workflow to detect control ID drift.

## Planning Material Boundary

Documents under `docs/en/30-54` are v0.5.0 planning materials. They are non-normative unless explicitly incorporated into the control catalog, evidence schema, assessment artifacts, testing procedures, or release notes.

These documents currently remain under `docs/en/` for public review continuity. A future release may move them into a dedicated planning directory if the repository structure is reorganized.

## Repository Structure

```text
.
├── README.md
├── README.ja.md
├── README.zh-CN.md
├── README.ko.md
├── LICENSE.md
├── CITATION.cff
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── controls/
│   └── aaef-controls-v0.1.csv
├── docs/
│   └── en/
│       ├── 00-introduction.md
│       ├── 01-scope.md
│       ├── 02-core-principles.md
│       ├── 03-definitions.md
│       ├── 04-threat-model.md
│       ├── 05-trust-model.md
│       ├── 06-control-domains.md
│       ├── 07-control-requirements.md
│       ├── 08-assessment-methodology.md
│       ├── 09-relationship-to-existing-frameworks.md
│       ├── 10-maintenance-and-validation.md
│       ├── 11-high-impact-action-taxonomy.md
│       ├── 12-assessment-quick-start.md
│       ├── 13-one-page-overview.md
│       ├── 14-evidence-event-schema.md
│       ├── 15-v02-control-expansion-notes.md
│       ├── 16-assurance-model.md
│       ├── 17-reference-architecture.md
│       ├── 18-implementation-guidance.md
│       ├── 19-open-research-questions.md
│       ├── 20-assessment-profiles.md
│       ├── 21-action-sequence-monitoring.md
│       ├── 22-assessment-automation-and-human-review.md
│       ├── 23-infrastructure-siem-evidence-integration.md
│       ├── 24-control-catalog-versioning.md
│       ├── 25-testing-procedures-and-pass-criteria.md
│       ├── 26-high-impact-audit-grade-prequalification.md
│       ├── 27-trusted-control-boundary-integrity.md
│       ├── 28-external-framework-mapping-methodology.md
│       ├── 29-iso-iec-42001-feasibility.md
│       ├── 30-principal-context-degradation.md
│       ├── 31-cross-agent-cross-domain-authority.md
│       ├── 32-authority-denial-reauthorization-flow.md
│       ├── 33-v050-planning-overview.md
│       ├── 34-v050-control-design-options.md
│       ├── 35-authority-assertion-profile.md
│       ├── 36-risk-proportional-evidence-profile.md
│       ├── 37-tamper-evident-evidence-storage.md
│       ├── 38-v050-evidence-schema-field-candidates.md
│       ├── 39-approval-quality-approval-fatigue.md
│       ├── 40-approval-evidence-examples.md
│       ├── 41-non-execution-reauthorization-examples.md
│       ├── 42-tamper-evident-evidence-examples.md
│       ├── 43-risk-proportional-evidence-assessment-guidance.md
│       ├── 44-evidence-depth-examples.md
│       ├── 45-principal-context-degradation-examples.md
│       ├── 46-cross-agent-authority-examples.md
│       ├── 47-approval-quality-assessment-guidance.md
│       ├── 48-non-execution-reauthorization-negative-tests.md
│       ├── 49-tamper-evident-evidence-negative-tests.md
│       ├── 50-authority-lifecycle-model.md
│       ├── 51-evidence-integrity-levels.md
│       ├── 52-approval-quality-model.md
│       ├── 53-v050-release-scope-decision.md
│       ├── 54-v050-release-preparation-checklist.md
│       ├── 55-researcher-overview.md
│       ├── 56-capability-scoped-cross-agent-delegation.md
│       ├── 57-cross-agent-delegation-negative-tests.md
│       ├── 58-cross-agent-budget-propagation.md
│       ├── 59-principal-context-degradation-testing.md
│       ├── 60-evidence-integrity-profile-guidance.md
│       ├── 61-tamper-evident-evidence-requirements.md
│       ├── 62-approval-quality-testing-guidance.md
│       ├── document-map.md
│       └── status/
│           ├── README.md
│           ├── v050x-follow-up-status.md
│           ├── v050x-incorporation-decision-register.md
│           ├── v050x-testing-candidate-selection.md
│           ├── v050x-testing-procedure-candidate-matrix.md
│           ├── v050x-testing-candidate-mapping.md
│           ├── v050x-testing-draft-pass-fail-criteria.md
│           ├── v050x-testing-incorporation-readiness-review.md
│           ├── v050x-principal-context-testing-proposal.md
│           ├── v050x-principal-context-testing-candidate-appendix.md
│           ├── v050x-principal-context-testing-csv-refinement-proposal.md
│           ├── v050x-cross-agent-delegation-testing-proposal.md
│           ├── v050x-cross-agent-delegation-testing-candidate-appendix.md
│           ├── v050x-cross-agent-delegation-csv-refinement-proposal.md
│           ├── v050x-approval-quality-testing-proposal.md
│           ├── v050x-approval-quality-testing-candidate-appendix.md
│           ├── v050x-approval-quality-csv-refinement-proposal.md
│           ├── v050x-evidence-integrity-csv-refinement-proposal.md
│           ├── v050x-incorporation-review-checkpoint.md
│           ├── v050x-next-phase-track-plan.md
│           ├── v050x-evidence-schema-and-examples-track-proposal.md
│           ├── v050x-evidence-schema-field-proposal.md
│           ├── v050x-evidence-example-design-proposal.md
│           └── v050x-evidence-schema-example-implementation-readiness.md
│       └── release/
│           ├── v0.2.0-preparation-checklist.md
│           ├── v0.3.0-preparation-checklist.md
│           └── v0.4.0-preparation-checklist.md
├── assessment/
│   ├── aaef-assessment-profiles-v0.3-draft.csv
│   ├── aaef-assessment-worksheet-v0.2-draft.csv
│   └── aaef-testing-procedures-v0.4-draft.csv
├── assets/
│   └── aaef-reference-architecture.mmd
├── mappings/
│   ├── aaef-external-framework-mapping-v0.4-draft.csv
│   ├── csa-agentic-trust-framework.md
│   ├── nist-ai-rmf-genai-profile.md
│   ├── owasp-agentic-top10-2026.md
│   ├── threat-control-assurance-mapping.md
│   └── threat-control-assurance-mapping-v0.2-draft.csv
├── schemas/
│   └── agentic-action-evidence-event.schema.json
├── taxonomies/
│   └── high-impact-action-taxonomy-v0.2-draft.csv
├── examples/
│   ├── agentic-action-evidence-event.json
│   ├── agentic-action-evidence-event.minimal.json
│   ├── agentic-action-evidence-event.valid.json
│   ├── agentic-action-evidence-event.high-impact.json
│   ├── agentic-action-evidence-event.audit-grade.json
│   ├── agentic-action-evidence-event.invalid.json
│   └── attack-control-mapping.md
├── tools/
│   ├── validate_assessment_profiles.py
│   ├── validate_assessment_worksheet.py
│   ├── validate_control_catalog.py
│   ├── validate_external_mappings.py
│   ├── validate_evidence_schema.py
│   └── validate_testing_procedures.py
└── .github/
    └── workflows/
        └── validate-aaef-artifacts.yml
```

## Citation

If you reference this work, please cite it as:

> Kazuma Horishita, *Agentic Authority & Evidence Framework (AAEF): An Action Assurance Control Profile for Agentic AI Systems*, v0.5.0 Public Review Planning Release, 2026.

## Research and Open Questions

For document classification and navigation, see [`docs/en/document-map.md`](docs/en/document-map.md).

For a research-facing entry point, see [`docs/en/55-researcher-overview.md`](docs/en/55-researcher-overview.md). For the detailed catalog of open research questions, see [`docs/en/19-open-research-questions.md`](docs/en/19-open-research-questions.md).

## License

The AAEF documentation is released under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

See [LICENSE.md](LICENSE.md).
