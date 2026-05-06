# Post-v1.0.0 Decomposition and Practical Package Boundary Review

Status: Non-normative planning and review artifact.

This document reviews how AAEF should distinguish AAEF Core, Profiles, Practical Packages, Applied Implementations, and External Strategy / Business / Capital Formation material after AAEF v1.0.0.

This document does not move files, split repositories, create profile directories, create package directories, update the active control and assessment baseline, or open a v1.1.0 roadmap.

The active baseline remains AAEF v0.4.1 unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

AAEF v1.0.0 remains a conservative release path planning release.

## Purpose

The purpose of this review is to introduce decomposition boundaries without weakening AAEF's role as a broad foundational framework for AI action authority, execution boundaries, evidence, authorization, non-execution, human approval, responsibility separation, and reviewability.

Decomposition does not mean shrinking AAEF.

It means making future material easier to classify, use, review, and package without mixing together:

- public framework material
- audience-specific profiles
- practical review packages
- applied implementations
- private strategy
- patent-sensitive implementation detail
- business or capital-formation material

## Current repository shape

AAEF is no longer best understood as a compact framework only.

The current repository is better described as:

> A broad framework ecosystem with an emerging practical package substrate.

This means AAEF now includes:

- core framework material
- control and assessment material
- evidence schema material
- reference architecture material
- status and planning records
- role guidance
- implementation guidance
- external mapping methodology and examples
- examples and validators
- public communication and roadmap review material
- possible practical package candidates

This shape is not a problem by itself.

The risk is that readers may not know which materials are stable core framework material, which are planning or historical records, which are audience profiles, which are practical package candidates, and which belong in applied implementation repositories.

## Why decomposition boundary design is needed now

Boundary design is needed now because AAEF has grown beyond a single short specification.

Without boundaries, future readers may confuse:

- AAEF Core with planning material
- Profiles with normative baseline material
- Practical Packages with certification or compliance offerings
- Applied Implementations with Core requirements
- AAEF-AI-VA implementation work with AAEF Core
- external strategy with public framework material

Boundary design should happen before major profile, package, or applied-implementation outputs are folded back into AAEF.

## What decomposition does not mean

This review does not recommend immediate repository splitting.

It does not recommend moving many files.

It does not recommend shrinking AAEF Core.

It does not recommend converting planning material into active baseline material.

It does not recommend promoting any profile, package, implementation, or example into the active baseline.

It does not authorize public inclusion of patent-sensitive AAEF-AI-VA implementation detail.

It does not authorize commercial strategy, pricing strategy, customer targeting, investor strategy, or capital-formation strategy in AAEF Core.

## Proposed layer model

Future AAEF work should be classified using the following layer model.

### Layer 1: AAEF Core

AAEF Core is the stable public foundation.

It should contain the core concepts, boundaries, and review model that make AAEF identifiable as AAEF.

AAEF Core should remain broad enough to support multiple profiles, practical packages, and applied implementations.

### Layer 2: AAEF Profiles

AAEF Profiles are use-case-specific or audience-specific interpretations of AAEF.

Profiles should help readers apply AAEF to a domain or role without changing the Core.

Possible profile areas include:

- vulnerability assessment
- AI agent operations
- evidence logging
- executive risk ownership
- legal and compliance review
- AI incident reconstruction
- agent IAM and delegation

### Layer 3: AAEF Practical Packages

AAEF Practical Packages are productizable or service-oriented review packages built from AAEF concepts.

They should be scoped as review packages, not certifications or compliance claims.

Possible practical packages include:

- AI Agent Action Risk Review
- AI Action Evidence Review
- Tool Execution Boundary Review
- Human Approval Flow Review
- Non-Execution Evidence Review
- AI Incident Reconstruction Readiness Review
- AI Vulnerability Assessment Safety Review

### Layer 4: Applied Implementations

Applied Implementations are reference implementations, fixtures, validators, demos, examples, or applied projects that demonstrate or test AAEF concepts.

AAEF-AI-VA should generally be treated as an Applied Implementation.

Applied Implementations may inform AAEF Core, Profiles, or Practical Packages, but their implementation details should not automatically become Core material.

### Layer 5: External Strategy / Business / Capital Formation

External Strategy / Business / Capital Formation material should remain outside AAEF Core.

This includes:

- investor or patron strategy
- representative or overseas agent strategy
- pricing strategy
- customer target lists
- domestic AI compute feasibility strategy
- commercial service packaging detail
- patent-sensitive commercialization strategy

## AAEF Core retention criteria

Material should remain in AAEF Core when removing it would weaken the framework's ability to explain action authority, execution boundaries, evidence, and reviewability for agentic AI systems.

Core material should generally satisfy one or more of the following criteria:

- it defines the AAEF thesis
- it defines core terms
- it defines action authority boundaries
- it defines request, authorization, dispatch, execution, non-execution, and evidence relationships
- it defines control domains or control requirements
- it defines evidence schema concepts
- it supports baseline interpretation
- it supports assessment methodology
- it supports reference architecture
- it preserves claim boundaries
- it applies across many profiles or practical packages

## Materials that should stay in Core

The following should remain Core or Core-adjacent foundation material:

- "Model output is not authority"
- five practical assurance questions
- authority boundary model
- action request / authorization / dispatch / execution / evidence separation
- evidence event schema
- assessment methodology
- high-impact action taxonomy
- trusted control boundary
- principal context degradation
- non-execution evidence
- human approval quality
- evidence integrity levels
- reference architecture
- conservative external framework relationship
- baseline and claim-boundary notes
- non-goal language
- document map and public navigation references

## Profile boundary

Profiles should interpret AAEF for a specific role, audience, or use case.

A Profile may include:

- domain-specific language
- role-specific reading paths
- use-case-specific interpretation
- profile-specific review questions
- profile-specific evidence expectations
- profile-specific caveats

A Profile should not:

- silently update AAEF Core
- change the active baseline
- claim implementation conformance
- claim evidence sufficiency
- claim assessment sufficiency
- claim certification, compliance, conformity, audit sufficiency, legal sufficiency, or external-framework equivalence

## Materials that should be marked as Profiles

The following types of material may become Profile material:

- operator guidance
- risk-owner guidance
- legal and compliance reviewer guidance
- security architect guidance
- implementation guidance
- vulnerability assessment application material
- incident reconstruction material
- evidence logging guidance
- agent IAM / delegation guidance
- AI agent operations guidance

## Practical package boundary

Practical Packages should be scoped review packages that help a reader or service provider apply AAEF to a bounded practical question.

A Practical Package may include:

- review scope
- intake questions
- evidence request checklist
- reviewer walkthrough
- sample report structure
- non-claim language
- risk finding categories
- recommended next actions

A Practical Package should not be described as:

- certification
- compliance validation
- conformity assessment
- legal opinion
- audit opinion
- production-readiness approval
- implementation conformance decision
- automated risk acceptance

## Materials that should be marked as Practical Packages

The following are practical package candidates:

- consultant discovery checklist
- auditor evidence request checklist
- AI Agent Action Risk Review
- Tool Execution Boundary Review
- Human Approval Flow Review
- Non-Execution Evidence Review
- AI Action Evidence Review
- AI Incident Reconstruction Readiness Review
- AI Vulnerability Assessment Safety Review

## Applied implementation boundary

Applied Implementations may demonstrate AAEF concepts through reference implementations, local labs, fixtures, validators, demos, or evidence packages.

Applied Implementations may include:

- sanitized public samples
- static/mock evidence packages
- structural validators
- local-lab candidates
- evidence package examples
- AAEF-AI-VA safe local-lab work

Applied Implementations should not automatically become AAEF Core.

Applied Implementations should not introduce patent-sensitive implementation details into public AAEF materials.

Applied Implementation findings may be returned to AAEF as:

- Core clarification candidates
- Profile candidates
- Practical Package candidates
- reviewer guidance candidates
- validator limitation observations
- evidence model feedback

## AAEF-AI-VA boundary

AAEF-AI-VA should generally be treated as an Applied Implementation.

AAEF-AI-VA may provide useful evidence about:

- AI output being treated as a request
- gate decisions controlling execution
- dispatch and non-dispatch evidence
- execution and non-execution evidence
- reviewer walkthrough needs
- local-lab evidence package structure
- structural validator needs
- AAEF five-question mapping

AAEF Core should not include AAEF-AI-VA technical implementation details unless a later review explicitly identifies a safe, abstract, non-patent-sensitive concept that belongs in Core.

## External strategy boundary

External Strategy / Business / Capital Formation material should not enter AAEF Core.

This includes:

- investor strategy
- patron strategy
- representative strategy
- pricing strategy
- customer target lists
- NDA-dependent commercial planning
- domestic AI compute hardware feasibility detail
- business development playbooks
- patent-sensitive commercialization strategy

Such material may be useful to the broader project, but it should remain outside the public framework.

## Materials that should remain outside AAEF Core

The following should not be placed in AAEF Core:

- AAEF-AI-VA technical implementation details
- patent-sensitive browser-state or diagnostic reconstruction detail
- Browser State Intelligence implementation detail
- Gated AI Diagnostic Request implementation detail
- DOM / HAR / screenshot / accessibility / event / storage / console integration detail
- investor or patron strategy
- overseas representative contracts
- pricing strategy
- customer target lists
- domestic AI compute hardware feasibility detail
- commercial service packaging detail
- legal conclusions
- compliance claims
- certification claims
- conformity claims

## First candidate practical package

The recommended first practical package candidate is:

> AI Agent Action Risk Review

This is a strong first candidate because it:

- aligns closely with the AAEF thesis
- applies across industries
- can be explained without claiming certification or compliance
- can use AAEF's five questions directly
- can include evidence request and review checklists
- can produce a sample report without claiming production readiness
- is compatible with lessons from AAEF-AI-VA applied evidence work
- has lower claim risk than certification, compliance, or formal audit language

## Candidate package scope: AI Agent Action Risk Review

A future AI Agent Action Risk Review package could review:

- what actions an AI agent may request
- who or what acts
- on whose behalf the action is requested
- what authority is required
- where authorization is evaluated
- where dispatch is enforced
- whether non-execution is evidenced
- what evidence supports later review
- what residual risks remain

It should be framed as a risk review package, not as certification, compliance, audit sufficiency, legal sufficiency, or production-readiness approval.

## Work not yet authorized

This review does not authorize:

- moving files
- repository splitting
- profile directory creation
- package directory creation
- active baseline updates
- v1.1.0 roadmap creation
- active-baseline candidate review
- AAEF-AI-VA implementation details in AAEF Core
- patent-sensitive implementation detail in public materials
- commercial strategy in AAEF Core
- legal or compliance conclusions
- certification or conformity claims

## Claim boundaries

This document does not establish:

- implementation readiness
- operational readiness
- production readiness
- implementation conformance
- control conformance
- evidence sufficiency
- assessment sufficiency
- audit sufficiency
- legal sufficiency
- certification
- compliance
- conformity
- semantic correctness
- empirical validation
- automated risk acceptance
- external-framework equivalence

## Recommended next step

Recommended next step after this review:

1. Close this track if the boundary model is accepted.
2. Continue AAEF-AI-VA applied evidence work separately as an Applied Implementation.
3. Use lessons from AAEF-AI-VA only at an abstract, non-patent-sensitive level when returning ideas to AAEF.
4. Consider a future narrow track for the first practical package candidate: AI Agent Action Risk Review.
5. Do not open a major v1.1.0 roadmap until package/profile scope is clearer.

## Close-readiness criteria

This track can be closed when:

- the layer model has been documented
- AAEF Core retention criteria have been documented
- Profile, Practical Package, Applied Implementation, and External Strategy boundaries have been documented
- AI Agent Action Risk Review has been identified as the first practical package candidate
- non-goals and claim boundaries have been documented
- no files have been moved
- no active baseline update has been made
- no v1.1.0 roadmap has been opened
- no unsupported readiness, conformance, sufficiency, certification, compliance, audit/legal, or external-framework equivalence claim has been made
