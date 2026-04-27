# Agentic Authority & Evidence Framework / AAEF

[![Validate AAEF Artifacts](https://github.com/mkz0010/agentic-authority-evidence-framework/actions/workflows/validate-aaef-artifacts.yml/badge.svg)](https://github.com/mkz0010/agentic-authority-evidence-framework/actions/workflows/validate-aaef-artifacts.yml)

**AAEF: Agentic AI SystemsのためのAction Assurance Control Profile**

## 翻訳に関する注意

この文書は、英語版READMEを基にした日本語参考訳です。

本翻訳は機械翻訳を基にしており、用語、意味、ニュアンス、統制要件の解釈に誤り、不完全さ、曖昧さが含まれる可能性があります。

AAEFの正本は英語版です。
日本語訳と英語版READMEまたは `docs/en/` 配下の英語文書の間に矛盾または不一致がある場合、英語文書が優先されます。

セキュリティ、コンプライアンス、監査、実装判断に利用する場合は、必ず英語版を参照してください。

## 概要

Agentic Authority & Evidence Framework、AAEFは、Agentic AI Systemsにおける **委任された権限**、**ポリシーで強制される実行境界**、および **検証可能な証跡** を統治するための実務的なコントロールフレームワークです。

AAEFは、単に文章を生成するAIではなく、ツールを呼び出し、データへアクセスし、タスクを委任し、他のエージェントと相互作用し、人間または組織の代理として意味のある行為を実行するAIエージェントを対象としています。

## 中心となる考え方

AAEFは、Agentic AIのセキュリティを **モデルの挙動を信じること** から **認可された行為を統治すること** へ移すことを目的としています。

従来のAIリスク管理では、モデルが正確か、安全か、説明可能か、整合しているか、信頼できるかが問われてきました。これらは今後も重要です。

しかし、AIエージェントが実際に行為できる場合、実務上の問いは次のように変わります。

> その行為は、認可され、境界づけられ、帰属可能で、証跡によって検証可能か。

AAEFは、この問いに答えるために存在します。

## AAEFが扱う5つの問い

AAEFは、組織が以下の5つの問いに答えられるようにすることを目的としています。

1. **誰、または何が行為したのか**
2. **誰の代理として行為したのか**
3. **どの権限を持っていたのか**
4. **実行時点でその行為は許可されていたのか**
5. **何が起きたことを、どの証跡で証明できるのか**

これらに答えられない場合、組織は本番環境でAgentic AI Systemsを確実に統制できません。

## AAEFが定義しないもの

AAEFは、新しいIDプロトコル、認証プロトコル、認可プロトコル、またはエージェント通信プロトコルを定義するものではありません。

AAEFは、AIガバナンスフレームワーク、Zero Trustフレームワーク、アイデンティティ標準、エージェント通信標準、脅威分類を置き換えるものでもありません。

AAEFは、高影響なAIエージェントの行為に対するAction Assurance Controlを定義することで、これらを補完することを目的としています。

## 言語 / 翻訳

このリポジトリの英語版が正本です。

以下の翻訳READMEは参考訳です。機械翻訳を基にしており、用語、意味、ニュアンスに不正確、不完全、または曖昧な箇所が含まれる可能性があります。

- [English](README.md) — authoritative
- [日本語 / Japanese](README.ja.md) — reference translation
- [简体中文 / Simplified Chinese](README.zh-CN.md) — reference translation
- [한국어 / Korean](README.ko.md) — reference translation

セキュリティ、コンプライアンス、監査、実装判断に利用する場合は、`docs/en/` 配下の英語文書を参照してください。

## 対象読者

AAEFは、主に以下の読者を想定しています。

- セキュリティアーキテクト
- AIアプリケーション開発者
- AIガバナンスチーム
- 内部監査部門
- コンプライアンス部門
- リスク管理部門
- プラットフォームエンジニア
- ツール利用型または自律型AIエージェントを本番導入しようとする組織

## ドキュメントの状態

**AAEF v0.3.0 Public Review Draft** が現在の公開レビュー baseline です。

**AAEF v0.3.1 Maintenance Release** は、このbaselineに対する最新のタグ付きメンテナンスリリースです。

AAEF v0.3.1 は v0.3.0 の公開レビュー範囲を変更しません。リリース後の整理、リリース作業記録の整理、バージョン表記の整合性、統合されたvalidation自動化を追加しています。

AAEF v0.3.0 は v0.2.x baseline を拡張し、implementation profiles、evidence quality assessment criteria、assessment profile mapping、TCB implementation capability patterns、action sequence monitoring、assessment automation guidance、infrastructure / SIEM evidence integration guidance を追加しています。

過去の v0.2.x および v0.1.x リリースは、以前の公開レビュー baseline として引き続き参照できます。

AAEF v0.3.0 は公開レビュー草案です。認証制度、正式標準、または完全なリスク軽減を主張するものではありません。

フィードバック、Issue、Pull Requestを歓迎します。

## 最初に読む文書

AAEFを初めて読む場合は、英語版の以下の文書から読むことを推奨します。

1. [`docs/en/13-one-page-overview.md`](docs/en/13-one-page-overview.md)
2. [`docs/en/02-core-principles.md`](docs/en/02-core-principles.md)
3. [`docs/en/17-reference-architecture.md`](docs/en/17-reference-architecture.md)
4. [`docs/en/06-control-domains.md`](docs/en/06-control-domains.md)
5. [`docs/en/07-control-requirements.md`](docs/en/07-control-requirements.md)
6. [`docs/en/14-evidence-event-schema.md`](docs/en/14-evidence-event-schema.md)
7. [`docs/en/12-assessment-quick-start.md`](docs/en/12-assessment-quick-start.md)

## 引用

この成果物を参照する場合は、以下のように引用してください。

> Kazuma Horishita, *Agentic Authority & Evidence Framework (AAEF): An Action Assurance Control Profile for Agentic AI Systems*, v0.3.1 Maintenance Release, 2026.

## ライセンス

AAEFのドキュメントは、**Creative Commons Attribution 4.0 International License（CC BY 4.0）** の下で公開されています。

詳細は [LICENSE.md](LICENSE.md) を参照してください。
