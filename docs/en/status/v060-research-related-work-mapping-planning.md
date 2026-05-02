# v0.6.x Research Related-Work Mapping Planning

This document defines a conservative planning boundary for future AAEF research related-work mapping.

It is a planning artifact for #286. It does not add an external framework equivalence claim, compliance crosswalk, certification mapping, formal literature review, legal conclusion, audit conclusion, or normative framework relationship.

## Status

Planning artifact.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

The v0.6.0 and v0.6.x adoption materials remain non-normative unless explicitly promoted into active guidance or active examples.

## Purpose

The purpose of this planning document is to define how AAEF should prepare a research related-work mapping without overclaiming novelty, equivalence, compliance, certification, or formal academic coverage.

The mapping should help readers understand where AAEF sits relative to adjacent research and practice areas while preserving the core AAEF boundary:

> Model output is not authority.

## Mapping goals

A future related-work mapping should help explain:

- which research and practice areas are adjacent to AAEF,
- which problems AAEF directly addresses,
- which problems AAEF intentionally does not address,
- where AAEF appears complementary rather than equivalent,
- where AAEF may need stronger references,
- where terminology may overlap with existing work,
- where novelty claims should be avoided or softened, and
- what evidence would be needed before making stronger research claims.

## Candidate related-work categories

A future mapping may include categories such as:

- agentic AI security and control boundaries,
- tool-use and function-calling authorization,
- prompt injection and indirect prompt injection defenses,
- human approval and human-in-the-loop control,
- authorization and policy decision architecture,
- evidence, audit logging, and reconstruction,
- provenance and tamper-evident records,
- governance, risk, and accountability frameworks,
- AI assurance and AI risk management,
- operational monitoring and incident response,
- software supply chain and runtime enforcement,
- safety cases and assurance cases, and
- compliance-adjacent control mapping.

These categories are candidates only. A later PR should decide the exact structure.

## Source eligibility planning

A future related-work mapping should prefer sources that are:

- primary standards or framework documents,
- peer-reviewed academic papers,
- official technical documentation,
- reputable industry reports,
- well-scoped security research writeups,
- project-maintained public documentation, or
- clearly labeled public review drafts.

Where possible, the mapping should distinguish:

- academic research,
- standards and frameworks,
- industry guidance,
- implementation documentation,
- incident or case-study material, and
- AAEF internal design artifacts.

## Source exclusion planning

A future mapping should avoid relying on:

- unsourced marketing claims,
- vendor-only claims without technical support,
- informal social posts as primary evidence,
- unclear summaries of standards,
- stale drafts where a newer authoritative version exists,
- claims that cannot be traced to a source,
- sources that assert legal or compliance sufficiency without context, and
- sources used only to imply equivalence.

## Mapping dimensions

A future mapping may compare related work across dimensions such as:

- authority separation,
- execution enforcement,
- action-bound evidence,
- backend verification,
- non-execution evidence,
- reconstruction support,
- human approval scope,
- policy and authorization model,
- runtime control boundary,
- audit and assurance posture,
- governance and risk-owner decision support,
- operational monitoring,
- implementation neutrality, and
- claim boundaries.

The mapping should avoid scoring unless a later PR defines a conservative scoring method.

## Claim boundaries

A related-work mapping should not claim that AAEF:

- is equivalent to an external framework,
- satisfies an external standard,
- provides compliance sufficiency,
- provides audit sufficiency,
- provides certification criteria,
- provides conformity criteria,
- proves legal adequacy,
- is production-ready,
- is a complete security architecture,
- replaces existing AI risk frameworks,
- replaces existing authorization models, or
- replaces software assurance, governance, or incident response practices.

The mapping may describe relationships, overlaps, gaps, and complementary roles.

## Novelty language planning

Novelty claims should be conservative.

Acceptable wording may include:

- AAEF emphasizes action authority rather than model output trust.
- AAEF focuses on action-bound evidence and reconstruction for agentic systems.
- AAEF is positioned as a control profile and adoption aid, not a standard or certification scheme.
- AAEF may complement existing AI risk and security frameworks.

Avoid stronger claims such as:

- AAEF is the first framework to solve this problem.
- AAEF fully covers agentic AI security.
- AAEF proves compliance.
- AAEF is equivalent to an established standard.
- AAEF makes agentic systems safe.

## Research output options

A later PR may create one or more of the following:

- `docs/en/status/v060-research-related-work-candidate-map.md`,
- `docs/en/research-related-work.md`,
- a table of related-work categories,
- a citation inventory,
- a gap and overlap matrix,
- a conservative novelty statement,
- a research positioning memo, or
- a publication-oriented related-work outline.

Initial recommendation:

- First create a candidate related-work map as a status artifact.
- Keep citations and relationship claims conservative.
- Promote to an active research-facing document only after the candidate map is reviewed.

## Relationship to existing mappings

AAEF already includes external framework mapping artifacts.

A research related-work mapping should not replace those mappings.

It should distinguish:

- framework relationship mapping,
- research related-work positioning,
- compliance-adjacent mapping,
- implementation guidance, and
- active baseline artifacts.

## Validation and review planning

A future related-work mapping should be reviewed for:

- source traceability,
- outdated references,
- unsupported novelty claims,
- accidental equivalence claims,
- compliance overclaims,
- unclear distinction between research and implementation,
- unclear distinction between AAEF artifacts and external sources,
- terminology conflict,
- missing adjacent domains, and
- overbroad scope.

If a future mapping includes tables, validation may include Markdown index checks and link/reference consistency checks where practical.

## Explicit exclusions

This planning document does not add:

- a completed related-work map,
- external framework equivalence claims,
- compliance crosswalks,
- certification mappings,
- conformity mappings,
- legal conclusions,
- audit conclusions,
- production readiness claims,
- implementation conformance criteria,
- new controls,
- new evidence schema fields,
- new assessment procedures,
- new testing procedures, or
- active baseline changes.

## Recommended next step

After this planning artifact is reviewed, create a candidate related-work map as a status document.

The next PR should remain conservative and should separate:

- source inventory,
- relationship descriptions,
- gaps and overlaps,
- novelty language, and
- explicit claim boundaries.
