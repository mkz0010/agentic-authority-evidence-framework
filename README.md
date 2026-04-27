# Agentic Authority & Evidence Framework / AAEF

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

**AAEF v0.2.1 Public Review Refinement** is the current tagged public review baseline.

AAEF v0.2.1 builds on the v0.2.0 Public Review Draft and incorporates post-v0.2.0 public review refinements for Evidence Event Schema profiles, Evidence Quality Gate guidance, assertion source and input influence assessment, High-Impact and Audit-Grade evidence examples, weak and adversarial evidence examples, existing enforcement implementation framing, high-impact action review surfaces, and Open Research Questions.

Earlier v0.2.0 and v0.1.x releases remain available as prior public review baselines.

The current control catalog file remains:

- `controls/aaef-controls-v0.1.csv`

The file name is retained for continuity, but the catalog contains the current v0.2.x public review control set.

The v0.2.0 Public Review Draft includes:

- preliminary OWASP Agentic Top 10 2026 mapping,
- Agentic Action Evidence Event JSON Schema,
- Evidence Event Schema validation workflow,
- expanded Evidence Event Schema sections for v0.2 control areas,
- High-Impact Action Taxonomy draft,
- v0.2 Control Expansion Notes,
- One-page Overview,
- Reference Architecture,
- v0.2.0 Release Preparation Checklist,
- authorization and revocation control expansion,
- human, delegation, and evidence control expansion,
- Assurance Model and Residual Risk Mapping,
- Assessment Quick Start,
- and Assessment Worksheet draft.

AAEF v0.2.0 remains a public review draft. It is not a certification scheme, formal standard, or claim of complete mitigation.

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

The file name is retained for continuity in the v0.2.x public review series. The catalog contains the current v0.2.x public review control set.

The Markdown control list in `docs/en/07-control-requirements.md` is maintained for readability and must remain consistent with the CSV catalog. This repository includes a validation script and GitHub Actions workflow to detect control ID drift.

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
│       ├── 18-v020-release-preparation-checklist.md
│       ├── 19-open-research-questions.md
│       ├── 20-assessment-profiles.md
│       ├── 21-action-sequence-monitoring.md
│       └── 22-assessment-automation-and-human-review.md
├── assessment/
│   ├── aaef-assessment-profiles-v0.3-draft.csv
│   └── aaef-assessment-worksheet-v0.2-draft.csv
├── assets/
│   └── aaef-reference-architecture.mmd
├── mappings/
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
│   └── validate_evidence_schema.py
└── .github/
    └── workflows/
        ├── validate-control-catalog.yml
        └── validate-evidence-schema.yml
```

## Citation

If you reference this work, please cite it as:

> Kazuma Horishita, *Agentic Authority & Evidence Framework (AAEF): An Action Assurance Control Profile for Agentic AI Systems*, v0.2.1 Public Review Refinement, 2026.

## Research and Open Questions

For research-oriented open questions, see [`docs/en/19-open-research-questions.md`](docs/en/19-open-research-questions.md).

## License

The AAEF documentation is released under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

See [LICENSE.md](LICENSE.md).
