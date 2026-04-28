# NIST AI RMF and Generative AI Profile Mapping

**Status:** Informative draft mapping for AAEF v0.4.x public review  
**AAEF version baseline:** v0.4.0 Public Review Draft with v0.4.x refinements  
**Scope:** Informative mapping from NIST AI RMF / NIST AI 600-1 Generative AI Profile concepts to AAEF agentic action assurance controls

## Purpose

This document provides an informative mapping between AAEF and selected NIST AI RMF / NIST AI 600-1 Generative AI Profile concerns.

AAEF does not replace the NIST AI RMF or the NIST Generative AI Profile.

AAEF is narrower than the AI RMF. It focuses on agentic action assurance: whether AI-enabled agents can take or trigger actions through tools, workflows, APIs, memory, retrieval, delegation, or backend execution paths, and whether those actions are authorized, bounded, evidenced, and reviewable.

## Source Handling and Limitations

This mapping uses public NIST framework names, function names, profile names, and high-level concepts as mapping anchors.

It does not reproduce the full NIST AI RMF or NIST AI 600-1 text.

This mapping is informative only. It is not a compliance mapping, certification claim, audit opinion, complete risk management process, or evidence of conformity with any NIST framework.

Reviewers and implementers should consult the current NIST source material directly when interpreting NIST AI RMF or NIST AI 600-1 content.

## Mapping Method

This mapping uses two levels:

- **AI RMF function-level alignment** — broad relationship between AAEF and AI RMF functions.
- **GenAI Profile topic-level alignment** — selected generative AI concerns where AAEF provides agentic action assurance support.

Subcategory-level or action-level mapping should be added only where public references support a more precise relationship and where doing so would not overstate AAEF coverage.

## AI RMF Function-Level Alignment

| NIST AI RMF function | AAEF relevance | Relationship |
| --- | --- | --- |
| GOVERN | AAEF GOV, ID, PRN, and catalog versioning guidance help define accountable ownership, agent identity, principal binding, and reviewable governance for agentic action paths. | Partial implementation support |
| MAP | AAEF threat model, high-impact action taxonomy, tool classification, memory/retrieval trust concepts, and assessment profiles help identify agentic action context and risk boundaries. | Partial implementation support |
| MEASURE | AAEF evidence schema, testing procedures, control-specific pass criteria, and audit-grade guidance help review authorization, dispatch, execution, non-execution, and evidence quality. | Evidence support |
| MANAGE | AAEF response, revocation, freeze, denial, reauthorization, and trusted control boundary guidance help manage selected agentic action risks. | Partial implementation support |

## Generative AI Profile Topic-Level Alignment

AAEF is relevant to generative AI systems when generated outputs can influence actions, tools, workflows, memory, retrieval, delegation, approvals, or backend execution.

| GenAI-facing concern | AAEF relevance | Relationship |
| --- | --- | --- |
| Tool use and external actions | AAEF AUZ and TOOL controls separate model output from authorization and tool dispatch authority. | Agentic action-specific support |
| Indirect prompt injection and external content influence | AAEF MEM, AUZ, TOOL, and EVD controls treat untrusted retrieved or remembered content as data rather than authority and require influence to be reviewable. | Partial implementation support |
| Memory and retrieval risks | AAEF MEM controls address memory writes, retrieval provenance, trust metadata, and influence of remembered or retrieved content on high-impact actions. | Partial implementation support |
| Human oversight and approval quality | AAEF HUM and AUZ controls address informed approval, approval fatigue, emergency intervention, and approval-to-execution evidence linkage. | Partial implementation support |
| Incident reconstruction | AAEF EVD and RES controls support reconstruction of what action occurred, under whose authority, through which tool or workflow, and with what outcome. | Evidence support |
| Complete generative AI risk management | AAEF does not cover all GenAI risks, model evaluation, content safety, data governance, human factors, lifecycle governance, or enterprise AI risk management. | Not equivalent |

## Non-Equivalence Statement

AAEF should not be presented as satisfying the NIST AI RMF or NIST AI 600-1.

AAEF does not provide complete AI risk management, GenAI risk management, certification readiness, audit sufficiency, compliance equivalence, or conformity evidence.

AAEF may be useful as an implementation-oriented companion for the narrower problem of agentic action assurance.

## Review Notes

The current external mapping CSV intentionally keeps NIST AI RMF function-level rows conservative.

The NIST AI 600-1 Generative AI Profile row should remain a topic-level informative mapping unless future work identifies public, specific references that support more precise mapping.

Future refinements may include:

- adding more precise public-reference-level mapping where appropriate;
- separating AI RMF function-level and GenAI Profile topic-level mappings into distinct records;
- identifying which AAEF controls are most useful for tool use, memory, retrieval, approval, and incident reconstruction;
- preserving limitations around non-equivalence and incomplete coverage.
