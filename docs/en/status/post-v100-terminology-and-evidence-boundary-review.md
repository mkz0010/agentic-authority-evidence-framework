# Post-v1.0.0 Terminology and Evidence Boundary Review

Status: Non-normative planning and review artifact.

This document reviews terminology and evidence-boundary risks identified by external critique after AAEF v1.0.0.

This document does not rename terminology, update the active control and assessment baseline, update assessment outcomes, update evidence schemas, update examples, update validators, or open a v1.1.0 roadmap.

The active baseline remains AAEF v0.4.1 unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

AAEF v1.0.0 remains a conservative release path planning release.

## Purpose

The purpose of this review is to reduce the risk that AAEF is misread as:

- a certification scheme
- a compliance framework
- a conformity assessment
- an audit opinion
- a legal sufficiency model
- a production-readiness claim
- an implementation conformance decision
- an external-framework equivalence claim

This review also clarifies what AAEF evidence does and does not support.

The immediate goal is review and classification, not broad replacement of existing terminology.

## Background

External critique identified that AAEF's core thesis and action-boundary focus are strong, but some terminology and evidence language may create unintended expectations.

The most repeated concerns were:

- AAEF uses terms that may sound like audit, certification, compliance, or conformity language.
- Evidence language may be misread as legal proof or audit evidence sufficiency.
- Assessment outcome language may be misread as external conformance or certification.
- Human approval may be misread as risk acceptance.
- Model or runtime self-report may be misread as trusted evidence.
- Validator success may be misread as semantic correctness, evidence sufficiency, or implementation readiness.
- Mapping to external frameworks may be misread as equivalence.

This document records those risks and recommends conservative follow-up handling.

## Current posture

Current AAEF posture:

- AAEF v1.0.0 has been published.
- AAEF v1.0.0 remains a conservative release path planning release.
- The active control and assessment baseline remains AAEF v0.4.1 unless a later release explicitly updates baseline artifacts.
- Public communication refinement has been completed.
- Decomposition and practical package boundary review has been completed.
- AAEF-AI-VA is handled separately as an Applied Implementation.
- No v1.1.0 roadmap has been opened.
- No active-baseline candidate review has been opened.

## Review scope

This review covers terminology and evidence-boundary risks in the following categories:

- assurance language
- assessment language
- conformance language
- pass/fail language
- audit-grade language
- baseline language
- evidence proof language
- external mapping language
- human approval language
- evidence trust language
- validator interpretation language

This review does not modify the underlying artifacts.

## Terminology risk categories

### Assurance language

Terms such as "assurance" and "action assurance" are central to AAEF's current identity.

Risk:

- Readers may interpret "assurance" as a guarantee.
- Audit, legal, or compliance readers may interpret "assurance" as professional assurance.
- Commercial readers may assume AAEF produces externally reliable assurance outcomes.

Current recommended posture:

- Retain "Action Assurance" as project identity for now.
- Clarify that AAEF supports action-boundary review and evidence-based reconstruction.
- Avoid implying professional assurance, certification, compliance, or legal sufficiency.
- Consider adding "assurance-support" or "review-support" qualifiers in future public-facing material when precision is needed.

Possible safer wording:

- action-boundary review support
- action authority and evidence review
- action assurance support
- review-supporting evidence

### Conformance language

Terms such as "Conformant" and "Non-Conformant" may be read as formal conformity or compliance judgments.

Risk:

- Readers may interpret a conformant result as certification.
- Internal users may reuse the term in external reports.
- Legal or audit readers may ask who determined conformity, under what criteria, and with what authority.

Current recommended posture:

- Do not immediately rename all historical or baseline terms.
- Review whether future assessment-facing outputs should prefer less formal language.
- Add stronger caveats wherever outcome terms may be reused externally.
- Treat any broad terminology change as a separate scoped follow-up.

Possible safer wording candidates:

- Control-Aligned
- Evidence-Supported for Review
- Implemented
- Partially Supported
- Not Demonstrated
- Review-Supported
- Not Review-Supported

### Audit-grade language

Terms such as "audit-grade" may imply professional audit evidence quality.

Risk:

- Readers may infer audit sufficiency.
- External auditors may object to the implication.
- AAEF examples may be misused as audit evidence claims.

Current recommended posture:

- Avoid expanding use of "audit-grade" in future public-facing material.
- Consider future replacement in examples or filenames only through a scoped compatibility-aware follow-up.
- Prefer "review-grade", "structured evidence example", or "high-evidence review example" in future materials.

Possible safer wording candidates:

- review-grade evidence
- structured evidence example
- high-evidence review profile
- external-review support example

### Pass criteria language

Terms such as "Pass Criteria" may imply formal test pass/fail certification.

Risk:

- Readers may treat a pass result as formal approval.
- Implementers may reuse pass language as an external guarantee.
- The phrase may imply readiness or conformance beyond AAEF's scope.

Current recommended posture:

- Keep historical testing-procedure artifacts stable unless a later scoped update modifies them.
- In future materials, prefer "review criteria" or "evidence support criteria".
- Clarify that criteria support review, not certification, compliance, audit sufficiency, or legal sufficiency.

Possible safer wording candidates:

- review criteria
- evidence review criteria
- evidence support criteria
- control review indicators

### Baseline language

"Baseline" is useful but may be read as a normative standard.

Risk:

- Readers may assume the active baseline is a formal standard baseline.
- Readers may misunderstand the relationship between latest release and active baseline.
- Readers may assume all planning materials are baseline material.

Current recommended posture:

- Continue distinguishing latest release from active baseline.
- Keep the active baseline boundary visible.
- Clarify that planning, status, examples, validators, and profiles do not update the baseline unless explicitly promoted.

Possible safer wording candidates for explanatory contexts:

- active control and assessment baseline
- current public review reference set
- baseline-related artifacts
- planning record, not baseline material

### Assessment language

"Assessment" may be read as third-party assessment, audit assessment, compliance assessment, or certification assessment.

Risk:

- AAEF-based self-review may be mistaken for an external assessment.
- Commercial users may overstate AAEF assessment results.
- Readers may assume assessment sufficiency.

Current recommended posture:

- In public-facing language, prefer qualified forms when needed:
  - AAEF-based internal review
  - AAEF self-assessment
  - AAEF-supported review
  - AAEF-informed assessment
- Clarify that AAEF does not establish assessment sufficiency by itself.

### Evidence proves language

Phrases such as "evidence proves what happened" are risky.

Risk:

- "Proves" may be read as legal proof.
- It may imply factual truth, correctness, or admissibility.
- It may imply audit evidence sufficiency.
- It may imply the record cannot be incomplete, manipulated, or misleading.

Current recommended posture:

- Prefer "supports reconstruction" language.
- Treat evidence as structured records for review and reconstruction.
- Make clear that evidence quality depends on evidence producer, trust boundary, integrity, correlation, and context.

Possible safer wording candidates:

- evidence supports reconstruction of what was recorded
- evidence supports review of an action path
- evidence links request, decision, dispatch, result, and review context
- evidence does not by itself establish truth, legality, correctness, or sufficiency

## Evidence non-proof boundary

AAEF evidence should be understood as structured records for review and reconstruction.

AAEF evidence does not by itself establish:

- legal proof
- legal admissibility
- legal sufficiency
- audit evidence sufficiency
- compliance documentation sufficiency
- factual truth
- model correctness
- action correctness
- policy correctness
- risk acceptance
- implementation conformance
- control conformance
- production readiness
- external-framework equivalence

AAEF evidence may support:

- reconstruction of recorded action paths
- review of authorization and dispatch boundaries
- correlation between request, decision, dispatch, execution, non-execution, and result
- identification of missing or weak evidence
- reviewer questions
- risk-owner discussion
- incident reconstruction support
- future improvement planning

## Evidence trust boundary

Evidence strength depends on where and how the evidence was produced.

Evidence is stronger when it is produced or corroborated by components that are:

- outside the model output path
- outside the agent's self-report-only path
- close to enforcement or backend execution
- able to observe dispatch or non-dispatch
- able to bind request, decision, action digest, dispatch, and result
- protected against tampering
- independently timestamped or correlated
- retained in a controlled evidence store

Evidence is weaker when it is only:

- model-generated narrative
- agent runtime self-report
- user-provided text
- untrusted page content
- prompt content
- uncorroborated application log
- post-hoc explanation
- manually reconstructed without traceability

## Model and runtime self-report limitation

Model output is not authority.

Model output is also not trusted evidence by itself.

Agent runtime self-report may be useful context, but it should not be treated as sufficient trusted evidence when authority, execution, or review consequences depend on it.

A conservative AAEF implementation should prefer evidence produced or corroborated by trusted enforcement, gateway, backend, or evidence components.

## Compromised control boundary limitation

AAEF evidence depends on trust assumptions.

If the following components are compromised, evidence trust may be reduced or invalidated:

- Trusted Control Boundary
- authorization decision point
- tool dispatch enforcement point
- gateway
- backend relying party
- evidence writer
- evidence store
- policy store
- identity or principal context provider
- clock or timestamp source
- signing or integrity mechanism

AAEF should not imply that evidence remains fully reliable after compromise of the components responsible for producing, protecting, or correlating it.

## Human approval vs risk acceptance

Human approval is not risk acceptance by itself.

Human approval may support an action decision only when the approver has sufficient context, authority, and evidence-relevant information.

Risk acceptance requires an accountable risk owner or organizational process.

Human approval can be weak when:

- the approver sees only model output
- the approver does not see scope, authority, or risk context
- the approver does not see action digest or payload details
- the action changes after approval
- the approval is reused beyond its intended scope
- the approval is obtained through fatigue, laundering, or misleading summaries
- the approver is not the risk owner

AAEF should preserve the distinction between:

- human approval
- operational approval
- authorization decision
- risk owner acceptance
- legal approval
- audit acceptance
- business acceptance

## Validator interpretation boundary

Validator success supports structural and consistency checks.

Validator success does not establish:

- semantic correctness
- control conformance
- implementation conformance
- evidence sufficiency
- assessment sufficiency
- audit sufficiency
- legal sufficiency
- production readiness
- runtime safety
- vulnerability detection completeness
- policy correctness
- risk acceptance
- external-framework equivalence

Validators should be described as support tools, not assurance engines.

## External mapping boundary

External mappings or relationship notes are informative unless a later release explicitly scopes and supports a stronger claim.

AAEF external mapping material should not imply:

- compliance
- conformity
- certification
- equivalence
- full coverage
- control satisfaction
- audit sufficiency
- legal sufficiency
- regulatory acceptance

Preferred posture:

- relationship note
- comparison
- partial support
- complementary focus
- non-equivalence mapping
- implementation-dependent support

## Recommended follow-up options

### Option 1: Add "What AAEF Evidence Does Not Prove"

This is the strongest follow-up candidate.

A narrow document could clarify:

- evidence supports reconstruction
- evidence is not legal proof
- evidence is not audit evidence sufficiency
- evidence is not compliance sufficiency
- evidence is not model correctness
- evidence depends on trust boundaries
- compromised evidence components reduce trust

### Option 2: Add terminology cleanup planning

A future planning artifact could inventory risky terms and recommend scoped replacements.

Candidate terms:

- Conformant
- Non-Conformant
- Audit-Grade
- Pass Criteria
- Assurance
- Assessment
- Baseline
- Evidence proves

This should be compatibility-aware and should not rewrite historical artifacts casually.

### Option 3: Add reviewer-facing caveat language

A future reviewer-facing guidance artifact could provide standard caveat text for AAEF-based review outputs.

Candidate caveat:

> This AAEF-based review supports structured discussion of action authority, dispatch, execution, non-execution, and evidence traceability. It does not constitute certification, compliance determination, conformity assessment, audit opinion, legal opinion, evidence sufficiency determination, or risk acceptance.

### Option 4: Add human approval vs risk acceptance note

A future artifact could clarify roles and responsibilities:

- requester
- operator
- approver
- authorization decision component
- risk owner
- reviewer
- auditor
- legal reviewer
- backend relying party

### Option 5: Defer broad renaming

Broad renaming should be deferred unless a specific follow-up issue scopes:

- affected files
- compatibility impact
- baseline impact
- examples and fixtures impact
- validator impact
- public communication impact

## Recommended immediate posture

Recommended posture after this review:

1. Do not rename all terms immediately.
2. Do not update the active baseline.
3. Do not open a v1.1.0 roadmap.
4. Prefer a narrow follow-up for "What AAEF Evidence Does Not Prove".
5. Prefer a separate future terminology cleanup plan before any broad terminology replacement.
6. Treat AAEF-AI-VA applied evidence work as a source of evidence-boundary lessons only, not technical implementation detail for AAEF Core.
7. Keep external-facing language conservative.

## Non-goals

This review does not:

- rename all terminology
- update the active baseline
- create a v1.1.0 roadmap
- open an active-baseline candidate review
- update the control catalog
- update the evidence schema
- update assessment artifacts
- update testing procedures
- update validators
- update examples or fixtures
- move files
- split repositories
- create profile or package directories
- add AAEF-AI-VA technical implementation details
- add patent-sensitive browser-state or diagnostic reconstruction details
- promote any material into the active baseline
- establish implementation readiness
- establish operational readiness
- establish production readiness
- establish implementation conformance
- establish control conformance
- establish evidence sufficiency
- establish assessment sufficiency
- establish audit or legal sufficiency
- establish certification, compliance, conformity, or external-framework equivalence
- establish semantic correctness or empirical validation
- establish automated risk acceptance

## Close-readiness criteria

This track can be closed when:

- terminology risk categories have been documented
- evidence non-proof boundaries have been documented
- evidence trust boundaries have been documented
- model/runtime self-report limitations have been documented
- compromised TCB / gateway / evidence-writer / evidence-store limitations have been documented
- human approval vs risk acceptance boundaries have been documented
- validator interpretation boundaries have been documented
- recommended follow-up options have been documented
- no broad terminology rename has been made
- no active baseline update has been made
- no v1.1.0 roadmap has been opened
- no unsupported readiness, conformance, sufficiency, certification, compliance, audit/legal, or equivalence claim has been made
