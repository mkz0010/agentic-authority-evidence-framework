# Agentic Authority & Evidence Framework / AAEF

[![Validate AAEF Artifacts](https://github.com/mkz0010/agentic-authority-evidence-framework/actions/workflows/validate-aaef-artifacts.yml/badge.svg)](https://github.com/mkz0010/agentic-authority-evidence-framework/actions/workflows/validate-aaef-artifacts.yml)

**AAEF: Agentic AI Systems를 위한 Action Assurance Control Profile**

## 번역 안내

이 문서는 영어 README를 기반으로 한 한국어 참고 번역입니다.

본 번역은 기계 번역을 기반으로 하며, 용어, 의미, 뉘앙스 또는 통제 요구사항 해석에 부정확함, 불완전함 또는 모호함이 포함될 수 있습니다.

AAEF의 공식 기준 문서는 영어 버전입니다.
이 한국어 번역과 영어 README 또는 `docs/en/` 아래의 영어 문서 사이에 충돌이나 불일치가 있는 경우, 영어 문서가 우선합니다.

보안, 컴플라이언스, 감사 또는 구현 의사결정에는 반드시 영어 문서를 참조하십시오.

## 개요

Agentic Authority & Evidence Framework, AAEF는 Agentic AI Systems에서 **위임된 권한**, **정책으로 강제되는 실행 경계**, **검증 가능한 증거**를 관리하기 위한 실무적 통제 프레임워크입니다.

AAEF는 단순히 텍스트를 생성하는 AI가 아니라, 도구를 호출하고, 데이터에 접근하고, 작업을 위임하며, 다른 에이전트와 상호작용하고, 인간 또는 조직을 대신하여 의미 있는 행위를 수행할 수 있는 AI Agent를 대상으로 합니다.

## 핵심 입장

AAEF는 Agentic AI 보안의 초점을 **모델의 행동을 신뢰하는 것** 에서 **승인된 행위를 통제하는 것** 으로 전환하는 것을 목표로 합니다.

기존 AI 리스크 관리는 모델이 정확한지, 안전한지, 설명 가능한지, 정렬되어 있는지, 신뢰할 수 있는지를 주로 다루었습니다. 이러한 질문은 여전히 중요합니다.

그러나 AI Agent가 실제 행위를 수행할 수 있을 때, 운영상의 핵심 질문은 다음과 같이 바뀝니다.

> 이 행위는 승인되었고, 경계가 설정되었으며, 귀속 가능하고, 증거로 검증 가능한가?

AAEF는 이 질문에 답하기 위해 존재합니다.

## AAEF가 다루는 다섯 가지 질문

AAEF는 조직이 다음 다섯 가지 질문에 답할 수 있도록 돕습니다.

1. **누가, 또는 무엇이 행위했는가?**
2. **누구를 대신하여 행위했는가?**
3. **어떤 권한을 가지고 있었는가?**
4. **실행 시점에 그 행위는 허용되었는가?**
5. **무엇이 일어났는지를 어떤 증거로 입증할 수 있는가?**

조직이 이 질문들에 답할 수 없다면, 운영 환경에서 Agentic AI Systems를 신뢰성 있게 통제할 수 없습니다.

## AAEF가 정의하지 않는 것

AAEF는 새로운 ID 프로토콜, 인증 프로토콜, 인가 프로토콜 또는 Agent 통신 프로토콜을 정의하지 않습니다.

AAEF는 AI 거버넌스 프레임워크, Zero Trust 프레임워크, ID 표준, Agent 통신 표준 또는 위협 분류 체계를 대체하지 않습니다.

대신, AAEF는 고영향 AI Agent 행위에 대한 action assurance controls를 정의하여 이러한 기존 접근을 보완하는 것을 목표로 합니다.

## 언어 / 번역

이 저장소의 영어 버전이 공식 기준 문서입니다.

다음 번역 README는 참고용으로 제공됩니다. 기계 번역을 기반으로 하며 부정확하거나 불완전하거나 모호한 용어가 포함될 수 있습니다.

- [English](README.md) — authoritative
- [日本語 / Japanese](README.ja.md) — reference translation
- [简体中文 / Simplified Chinese](README.zh-CN.md) — reference translation
- [한국어 / Korean](README.ko.md) — reference translation

보안, 컴플라이언스, 감사 또는 구현 의사결정에는 `docs/en/` 아래의 영어 문서를 참조하십시오.

## 대상 독자

AAEF는 다음 독자를 대상으로 합니다.

- 보안 아키텍트
- AI 애플리케이션 개발자
- AI 거버넌스 팀
- 내부 감사 팀
- 컴플라이언스 팀
- 리스크 관리 팀
- 플랫폼 엔지니어
- 도구 사용형 또는 자율형 AI Agent를 배포하려는 조직

## 문서 상태

**AAEF v0.4.0 Public Review Draft** 는 현재 공개 검토 baseline 입니다.

AAEF v0.4.0은 v0.3.x baseline을 확장하여 agentic AI action assurance를 enterprise assessment 및 audit support에서 더 쉽게 사용할 수 있도록 guidance를 추가합니다.

이전 v0.3.x, v0.2.x, v0.1.x releases 는 prior public review baselines 로 계속 참조할 수 있습니다.

AAEF v0.4.0에 추가된 주요 요소:

- control catalog versioning and change impact guidance
- measurable testing procedures and pass criteria
- machine-readable testing procedure draft
- High-Impact and Audit-Grade pre-qualification guidance
- Trusted Control Boundary integrity requirements
- external framework mapping methodology
- initial conservative external framework mapping draft
- validation for testing procedures and external mappings

AAEF v0.4.0은 공개 검토 초안입니다. 인증 체계, 공식 표준, implementation conformance claim, audit opinion, compliance equivalence 또는 완전한 완화 주장을 의미하지 않습니다.

Issues 및 Pull Requests를 통한 피드백을 환영합니다.

## 처음 읽을 문서

AAEF를 처음 읽는 경우, 영어 문서 기준으로 다음 순서를 권장합니다.

1. [`docs/en/13-one-page-overview.md`](docs/en/13-one-page-overview.md)
2. [`docs/en/02-core-principles.md`](docs/en/02-core-principles.md)
3. [`docs/en/17-reference-architecture.md`](docs/en/17-reference-architecture.md)
4. [`docs/en/06-control-domains.md`](docs/en/06-control-domains.md)
5. [`docs/en/07-control-requirements.md`](docs/en/07-control-requirements.md)
6. [`docs/en/14-evidence-event-schema.md`](docs/en/14-evidence-event-schema.md)
7. [`docs/en/12-assessment-quick-start.md`](docs/en/12-assessment-quick-start.md)

## 인용

이 작업을 참조하는 경우 다음과 같이 인용하십시오.

> Kazuma Horishita, *Agentic Authority & Evidence Framework (AAEF): An Action Assurance Control Profile for Agentic AI Systems*, v0.4.0 Public Review Draft, 2026.

## 라이선스

AAEF 문서는 **Creative Commons Attribution 4.0 International License（CC BY 4.0）** 에 따라 공개됩니다.

자세한 내용은 [LICENSE.md](LICENSE.md) 를 참조하십시오.
