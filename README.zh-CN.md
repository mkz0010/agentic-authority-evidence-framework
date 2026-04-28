# Agentic Authority & Evidence Framework / AAEF

[![Validate AAEF Artifacts](https://github.com/mkz0010/agentic-authority-evidence-framework/actions/workflows/validate-aaef-artifacts.yml/badge.svg)](https://github.com/mkz0010/agentic-authority-evidence-framework/actions/workflows/validate-aaef-artifacts.yml)

**AAEF：面向 Agentic AI Systems 的 Action Assurance Control Profile**

## 翻译说明

本文档是基于英文 README 的简体中文参考译文。

本译文基于机器翻译，可能包含术语、含义、语气或控制要求解释方面的不准确、不完整或歧义。

AAEF 的权威版本为英文版本。
如果本中文译文与英文 README 或 `docs/en/` 下的英文文档存在冲突或不一致，应以英文版本为准。

在进行安全、合规、审计或实现决策时，请务必参考英文文档。

## 概述

Agentic Authority & Evidence Framework，简称 AAEF，是一个实用的控制框架，用于治理 Agentic AI Systems 中的 **被委托的权限**、**由策略强制执行的动作边界** 和 **可验证的证据**。

AAEF 面向的不只是生成文本的 AI，而是能够调用工具、访问数据、委托任务、与其他 Agent 交互，并代表人类或组织执行有实际影响动作的 AI Agent。

## 核心立场

AAEF 旨在将 Agentic AI 的安全重点从 **信任模型行为** 转向 **治理被授权的动作**。

传统 AI 风险管理通常关注模型是否准确、安全、可解释、对齐或可信。这些问题仍然重要。

但是，当 AI Agent 能够执行实际动作时，操作层面的核心问题变为：

> 这个动作是否被授权、被边界限制、可归属，并且可以通过证据验证？

AAEF 正是为回答这个问题而存在。

## AAEF 关注的五个问题

AAEF 帮助组织回答以下五个实践性问题：

1. **谁，或者什么实体，执行了动作？**
2. **它代表谁执行了动作？**
3. **它拥有什么权限？**
4. **在执行时，该动作是否被允许？**
5. **有什么证据可以证明发生了什么？**

如果组织无法回答这些问题，就无法可靠地治理生产环境中的 Agentic AI Systems。

## AAEF 不是什么

AAEF 不定义新的身份协议、认证协议、授权协议或 Agent 通信协议。

AAEF 不取代 AI 治理框架、Zero Trust 框架、身份标准、Agent 通信标准或威胁分类。

相反，AAEF 旨在通过为高影响 AI Agent 动作定义 action assurance controls 来补充这些现有方法。

## 语言 / 翻译

本仓库的英文版本是权威版本。

以下翻译 README 仅供参考。它们基于机器翻译，可能包含不准确、不完整或有歧义的术语。

- [English](README.md) — authoritative
- [日本語 / Japanese](README.ja.md) — reference translation
- [简体中文 / Simplified Chinese](README.zh-CN.md) — reference translation
- [한국어 / Korean](README.ko.md) — reference translation

在进行安全、合规、审计或实现决策时，请参考 `docs/en/` 下的英文文档。

## 目标读者

AAEF 面向以下读者：

- 安全架构师
- AI 应用开发者
- AI 治理团队
- 内部审计团队
- 合规团队
- 风险管理团队
- 平台工程团队
- 准备部署工具型或自治型 AI Agent 的组织

## 文档状态

**AAEF v0.4.0 Public Review Draft** 是当前公开评审 baseline。

AAEF v0.4.0 在 v0.3.x baseline 的基础上增加了 enterprise assessment usability guidance，使 agentic AI action assurance 更容易用于企业评估和审计辅助场景。

此前的 v0.3.x、v0.2.x、v0.1.x releases 仍可作为 prior public review baselines 参考。

AAEF v0.4.0 新增的主要内容包括：

- control catalog versioning and change impact guidance
- measurable testing procedures and pass criteria
- machine-readable testing procedure draft
- High-Impact and Audit-Grade pre-qualification guidance
- Trusted Control Boundary integrity requirements
- external framework mapping methodology
- initial conservative external framework mapping draft
- validation for testing procedures and external mappings

AAEF v0.4.0 仍是公开评审草案。它不是认证机制、正式标准、implementation conformance claim、audit opinion、compliance equivalence，也不声称能够完全缓解所有风险。

欢迎通过 Issues 和 Pull Requests 提供反馈。

## 首次阅读

如果你是第一次阅读 AAEF，建议从以下英文文档开始：

1. [`docs/en/13-one-page-overview.md`](docs/en/13-one-page-overview.md)
2. [`docs/en/02-core-principles.md`](docs/en/02-core-principles.md)
3. [`docs/en/17-reference-architecture.md`](docs/en/17-reference-architecture.md)
4. [`docs/en/06-control-domains.md`](docs/en/06-control-domains.md)
5. [`docs/en/07-control-requirements.md`](docs/en/07-control-requirements.md)
6. [`docs/en/14-evidence-event-schema.md`](docs/en/14-evidence-event-schema.md)
7. [`docs/en/12-assessment-quick-start.md`](docs/en/12-assessment-quick-start.md)

## 引用

如果引用本项目，请使用以下格式：

> Kazuma Horishita, *Agentic Authority & Evidence Framework (AAEF): An Action Assurance Control Profile for Agentic AI Systems*, v0.4.0 Public Review Draft, 2026.

## 许可证

AAEF 文档基于 **Creative Commons Attribution 4.0 International License（CC BY 4.0）** 发布。

详情请参见 [LICENSE.md](LICENSE.md)。
