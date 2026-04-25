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

This repository contains **AAEF v0.1 Public Review Draft**.

This draft is intentionally incomplete. It is published to establish the core concepts, terminology, control domains, initial control requirements, and review direction for an open action assurance profile for agentic AI systems.

This revision incorporates early review feedback by clarifying evidence requirements, unifying maturity levels, strengthening prompt-injection-related controls, and making the control CSV the source of truth.

Feedback, issues, and pull requests are welcome.

## Control Catalog Source of Truth

The normative control catalog for v0.1 is `controls/aaef-controls-v0.1.csv`.

The Markdown control list in `docs/en/07-control-requirements.md` is maintained for readability and must remain consistent with the CSV catalog. This repository includes a validation script and GitHub Actions workflow to detect control ID drift.

## Repository Structure

```text
.
├── README.md
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
│       └── 10-maintenance-and-validation.md
├── examples/
│   ├── agentic-action-evidence-event.json
│   └── attack-control-mapping.md
├── tools/
│   └── validate_control_catalog.py
└── .github/
    └── workflows/
        └── validate-control-catalog.yml
```

## Citation

If you reference this work, please cite it as:

> Kazuma, *Agentic Authority & Evidence Framework (AAEF): An Action Assurance Control Profile for Agentic AI Systems*, v0.1 Public Review Draft, 2026.

## License

The AAEF documentation is released under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

See [LICENSE.md](LICENSE.md).
