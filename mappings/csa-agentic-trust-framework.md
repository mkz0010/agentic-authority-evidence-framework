# CSA Agentic Trust Framework Mapping

**Status:** Informative draft mapping for AAEF v0.4.x public review
**AAEF version baseline:** v0.4.0 Public Review Draft with v0.4.x refinements
**Scope:** Informative mapping from CSA Agentic Trust Framework concepts to AAEF agentic action assurance controls

## Purpose

This document provides an informative mapping between AAEF and the CSA Agentic Trust Framework.

AAEF does not replace the CSA Agentic Trust Framework.

AAEF focuses on agentic action assurance: whether AI-enabled agents can take or trigger high-impact actions through tools, workflows, APIs, memory, retrieval, delegation, or backend execution paths, and whether those actions are authorized, bounded, evidenced, revocable, and reviewable.

## Source Handling and Limitations

This mapping uses public CSA / ATF names, high-level concepts, and public framing as mapping anchors.

It does not reproduce the full CSA Agentic Trust Framework specification text.

This mapping is informative only. It is not a CSA compliance mapping, certification claim, audit opinion, complete implementation guide, or evidence of conformity with CSA guidance.

Reviewers and implementers should consult the current CSA / ATF source material directly when interpreting ATF requirements or implementation guidance.

Public sources:

- CSA article: https://cloudsecurityalliance.org/blog/2026/02/02/the-agentic-trust-framework-zero-trust-governance-for-ai-agents
- ATF repository: https://github.com/massivescale-ai/agentic-trust-framework

## Mapping Method

This mapping uses high-level ATF-facing concerns as anchors.

It avoids claiming that AAEF implements ATF. Instead, it identifies where AAEF provides related implementation support, evidence support, or partial alignment for agentic action assurance.

## High-Level Alignment

| ATF-facing concern | AAEF relevance | Relationship |
| --- | --- | --- |
| Agent identity and accountability | AAEF ID, PRN, and GOV controls identify which agent acted, on whose behalf, under which owner or operator context, and within which governed system boundary. | Partial implementation support |
| Purpose, behavior, and action intent | AAEF AUZ, GOV, and EVD controls bind high-impact actions to purpose, resource, risk, authorization decisions, and reviewable evidence. | Partial implementation support |
| Input, output, memory, and context handling | AAEF MEM, AUZ, TOOL, and EVD controls address external content influence, retrieval trust, memory provenance, and authorization isolation from untrusted content. | Partial implementation support |
| Least privilege and execution boundaries | AAEF TOOL, AUZ, DEL, and PRN controls define minimum authority, action boundary authorization, delegation constraints, and principal binding across workflows. | Agentic action-specific support |
| Revocation, containment, and incident response | AAEF RES, DEL, and EVD controls address revocation, downstream freeze, isolation, non-execution evidence, and incident reconstruction. | Evidence and response support |
| Progressive autonomy and maturity | AAEF assessment profiles and high-impact action taxonomy may support risk-proportional review, but AAEF does not define a complete ATF maturity model. | Related |
| Complete ATF implementation | AAEF does not provide a full ATF implementation, maturity program, promotion/demotion model, or enterprise governance operating model. | Not equivalent |

## AAEF Control Clusters

The following AAEF control clusters are especially relevant to ATF-style agent governance:

- **Governance:** AAEF-GOV-01, AAEF-GOV-02, AAEF-GOV-03
- **Agent identity:** AAEF-ID-01, AAEF-ID-02, AAEF-ID-03
- **Principal binding:** AAEF-PRN-01, AAEF-PRN-02
- **Authorization:** AAEF-AUZ-01, AAEF-AUZ-02, AAEF-AUZ-03, AAEF-AUZ-04, AAEF-AUZ-05
- **Tool execution:** AAEF-TOOL-01, AAEF-TOOL-02, AAEF-TOOL-03, AAEF-TOOL-04
- **Delegation:** AAEF-DEL-01, AAEF-DEL-02, AAEF-DEL-03, AAEF-DEL-04, AAEF-DEL-05
- **Memory and retrieval:** AAEF-MEM-01, AAEF-MEM-02, AAEF-MEM-03, AAEF-MEM-04
- **Human oversight:** AAEF-HUM-01, AAEF-HUM-02, AAEF-HUM-03, AAEF-HUM-04
- **Evidence:** AAEF-EVD-01, AAEF-EVD-02, AAEF-EVD-03, AAEF-EVD-04, AAEF-EVD-05
- **Response:** AAEF-RES-01, AAEF-RES-02, AAEF-RES-03, AAEF-RES-04

## Non-Equivalence Statement

AAEF should not be presented as satisfying the CSA Agentic Trust Framework.

AAEF does not provide complete ATF implementation, maturity certification, audit sufficiency, compliance equivalence, or conformity evidence.

AAEF may be useful as an implementation-oriented companion for the narrower problem of agentic action assurance.

## Review Notes

Future refinements may include:

- mapping AAEF controls to public ATF core elements where appropriate;
- identifying where ATF maturity concepts could inform AAEF assessment profiles;
- distinguishing preventive controls from response and reconstruction controls;
- adding implementation examples for identity, authorization, tool dispatch, and revocation;
- preserving limitations around non-equivalence and incomplete coverage.
