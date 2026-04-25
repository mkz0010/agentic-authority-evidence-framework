# Agentic Authority & Evidence Framework / AAEF

**AAEF：面向 Agentic AI Systems 的 Action Assurance Control Profile**

## 翻译说明

本文档是基于英文 README 的简体中文参考译文。

本译文基于机器翻译，可能包含术语、含义、语气或控制要求解释方面的不准确、不完整或歧义。

AAEF 的权威版本为英文版本。  
如果本中文译文与英文 README 或 `docs/en/` 下的英文文档存在冲突或不一致，应以英文版本为准。

在进行安全、合规、审计或实现决策时，请务必参考英文文档。

## 概述

Agentic Authority & Evidence Framework，简称 AAEF，是一个实用的控制框架，用于治理 Agentic AI Systems 中的以下内容：

- 被委托的权限
- 由策略强制执行的动作边界
- 可验证的证据
- 可撤销的信任

AAEF 面向的不只是生成文本的 AI，而是能够调用工具、访问数据、委托任务，并代表人类或组织执行有实际影响动作的 AI Agent。

## 核心立场

AAEF 旨在将 Agentic AI 的安全重点从：

> 信任模型行为

转向：

> 治理被授权的动作

传统 AI 风险管理通常关注模型是否准确、安全、可解释、对齐或可信。这些问题仍然重要。

但是，当 AI Agent 能够执行实际动作时，操作层面的核心问题变为：

> 这个动作是否被授权、被边界限制、可归属，并且可以通过证据验证？

AAEF 正是为回答这个问题而存在。

## AAEF 关注的五个问题

AAEF 帮助组织回答以下五个实践性问题：

1. 谁，或者什么实体，执行了动作？
2. 它代表谁执行了动作？
3. 它拥有什么权限？
4. 在执行时，该动作是否被允许？
5. 有什么证据可以证明发生了什么？

如果组织无法回答这些问题，就无法可靠地治理生产环境中的 Agentic AI Systems。

## AAEF 不是什么

AAEF 不定义：

- 新的身份协议
- 新的认证协议
- 新的授权协议
- 新的 Agent 通信协议
- 模型评估基准
- 通用 AI 伦理框架
- 现有 AI 治理框架的替代品
- 合规认证机制
- 法律意义上的注意义务标准

AAEF 旨在补充现有的 AI 治理、Zero Trust、身份管理、授权、Agentic AI 安全和 Agent 通信标准。

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

本仓库包含 **AAEF v0.1.3 Public Review Draft**。

该草案并非最终版本。  
它的目的在于公开 AAEF 的核心概念、术语、控制域、初始控制要求以及公开评审方向。

欢迎通过 Issues 和 Pull Requests 提供反馈。

## 许可证

AAEF 文档基于 **Creative Commons Attribution 4.0 International License（CC BY 4.0）** 发布。

详情请参见 `LICENSE.md`。
