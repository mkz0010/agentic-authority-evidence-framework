# ISO/IEC 42001 Feasibility and Initial Alignment Note

Status: Public Review Draft supporting note  
AAEF baseline: v0.4.x Public Review  
Issue context: #100

## Purpose

This note records a copyright-safe feasibility assessment for relating AAEF to ISO/IEC 42001:2023.

It does not provide a clause-by-clause mapping, compliance mapping, certification readiness assessment, audit opinion, or evidence of conformity with ISO/IEC 42001.

AAEF remains a Public Review Draft control profile and assessment aid for agentic action assurance.

## Source Handling

This note is based only on publicly available, high-level descriptions of ISO/IEC 42001 and related public metadata.

This repository must not reproduce:

- ISO/IEC 42001 requirement text;
- clause text;
- annex text;
- tables;
- figures;
- translated excerpts;
- detailed derived summaries of protected standard text.

If detailed clause-level analysis is required later, it should be performed by reviewers with appropriate licensed or authorized access, and protected text should not be committed to the public repository.

## Publicly Visible Scope

Public materials describe ISO/IEC 42001 as an international standard for artificial intelligence management systems.

At a high level, ISO/IEC 42001 concerns the establishment, implementation, maintenance, and continual improvement of an AI management system within an organizational context.

AAEF does not attempt to reproduce or restate ISO/IEC 42001 requirements.

## Feasibility Assessment

A high-level relationship between AAEF and ISO/IEC 42001 appears feasible, but only as informative alignment.

AAEF may support organizations that need implementation detail for agentic AI action assurance, especially where AI systems can take or trigger actions through tools, workflows, APIs, memory, retrieval, delegation, or backend execution paths.

However, AAEF is narrower than an AI management system standard.

AAEF focuses on:

- authorization boundaries for agentic actions;
- tool dispatch enforcement;
- backend execution boundaries;
- principal and agent identity;
- delegation, revocation, freeze, and reauthorization;
- memory and retrieval influence;
- human approval and override quality;
- evidence generation;
- auditability and incident reconstruction;
- trusted control boundary integrity;
- high-impact action assurance.

AAEF does not define a complete AI management system.

## Initial High-Level Alignment

The following alignment is conceptual and informative only.

| ISO/IEC 42001-facing concern | AAEF relevance | Relationship |
| --- | --- | --- |
| AI governance and accountability | AAEF GOV, ID, and PRN controls help identify governed agentic systems, accountable actors, agent identity, and principal binding. | Partial implementation support |
| Risk-based treatment of AI system behavior | AAEF high-impact action taxonomy, assessment profiles, and risk-proportional assurance guidance help classify and evaluate agentic action risk. | Partial implementation support |
| Operational control of AI-enabled actions | AAEF AUZ, TOOL, DEL, RES, MEM, and HUM controls define boundaries for authorization, tool use, delegation, revocation, memory influence, and human oversight. | Agentic action-specific support |
| Evidence and monitoring | AAEF EVD controls, evidence event schema, testing procedures, and audit-grade guidance support reviewability of high-impact agentic actions. | Evidence support |
| Incident response and reconstruction | AAEF response, revocation, non-execution, and reconstruction concepts help analyze what happened, under whose authority, and with what outcome. | Partial support |
| Management system completeness | AAEF does not cover all organizational AI management system requirements, lifecycle governance, certification processes, or full enterprise AI risk management. | Not equivalent |

## Clause Identifier Handling

Future ISO/IEC 42001 alignment work may reference clause identifiers or publicly visible titles where legally appropriate.

However, AAEF should not reproduce ISO/IEC 42001 requirement text, detailed clause content, tables, annex text, figures, or translated excerpts.

Clause identifier references, if used, should be treated as navigational references only. They must not imply equivalence, conformity, certification readiness, audit sufficiency, or full coverage.

Implementers and assessors should consult the official ISO/IEC 42001 text or an authorized national adoption through appropriate licensed or authorized access when detailed interpretation is required.

## Non-Equivalence Statement

AAEF should not be presented as satisfying ISO/IEC 42001.

AAEF does not establish ISO/IEC 42001 conformity, certification readiness, audit sufficiency, or compliance equivalence.

AAEF may be useful as an implementation-oriented companion for a narrow class of agentic AI assurance concerns, but it is not a replacement for an AI management system.

## Suggested Future Work

Future work may include:

- identifying whether public ISO materials allow safer high-level relationship statements;
- recording mapping limitations in the external mapping CSV;
- adding an explicitly non-equivalent ISO/IEC 42001 feasibility row if useful;
- evaluating whether clause identifier references can be used as navigational references without reproducing protected text;
- requesting review from someone with licensed or authorized access to ISO/IEC 42001 without committing protected text;
- keeping detailed clause-level analysis outside the public repository unless legally appropriate.

## Repository Handling Rules

For ISO/IEC 42001-related work:

- use high-level public metadata only unless a copyright-safe process is established;
- avoid clause-by-clause mapping unless a copyright-safe process is established;
- avoid reproducing protected text;
- treat clause identifiers, if used, as navigational references only;
- prefer relationship terms such as conceptual alignment, partial implementation support, evidence support, not assessed, and not equivalent;
- avoid compliance, certification, conformity, or audit sufficiency claims.
