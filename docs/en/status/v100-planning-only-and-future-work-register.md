# v1.0.0 Planning-Only and Future-Work Register

## Purpose

This document registers planning-only, historical, future-work, and non-goal areas for the path toward AAEF v1.0.0.

It supports:

- roadmap #350, `[Roadmap] Toward v1.0.0: Stable Baseline and Release Path`
- track #351, `[Track] v1.0.0: Baseline Scope and Promotion Decision`
- `docs/en/status/v100-baseline-scope-and-promotion-decision.md`
- `docs/en/status/v100-promoted-artifact-candidate-inventory.md`
- `docs/en/status/post-v070-version-status-and-baseline-reference-note.md`

The goal is to prevent v1.0.0 scope creep by making explicit what should not be automatically promoted into the active baseline, stable guidance, examples, validators, or release claims.

This document is planning and register material only. It does not publish v1.0.0, create a release tag, update the active baseline, update the control catalog, update the evidence schema, update assessment artifacts, update testing procedures, add examples, add fixtures, or add executable validators.

## Register posture

This register does not devalue planning-only, historical, or future-work materials.

Many of these materials are important.

The point is to avoid treating them as if they already have a stable v1.0.0 role.

A domain may be important and still be deferred.

A planning artifact may be useful and still remain planning-only.

A historical artifact may explain why a decision was made without becoming current guidance.

A non-goal may be intentionally excluded to protect conservative claim boundaries.

## Categories

| Category | Meaning |
| --- | --- |
| Planning-only | Useful planning or review material that should not be treated as active baseline or stable guidance unless later promoted. |
| Historical | Versioned context from earlier work that should remain available but should not be used as current entry-point guidance by itself. |
| Future work | Important area that should be deferred beyond v1.0.0 unless separately scoped. |
| Narrow-scope candidate | Area that may be included only if tightly scoped by a later track. |
| Non-goal | Area that v1.0.0 should not claim or imply. |
| Requires separate track | Area requiring its own roadmap, evidence, validation, or implementation work before promotion. |

## Register summary

| Area | Category | Initial v1.0.0 posture |
| --- | --- | --- |
| v0.5.x and v0.6.x planning documents | Planning-only / historical | Preserve as context; do not treat as current entry-point guidance unless summarized or promoted. |
| v0.7.0 roadmap and track planning artifacts | Planning-only / stable guidance candidates by exception | Keep track-specific status docs as planning material unless separately promoted into guidance. |
| Release preparation checklists | Historical / planning-only | Preserve as release history; do not treat as current release requirements. |
| Version status and baseline reference notes | Stable status reference candidate | Use for entry-point clarification, but not as baseline replacement. |
| Research positioning materials | Planning-only / stable explanatory candidate | Preserve for framing; do not claim empirical validation or peer review. |
| External framework mapping materials | Contextual reference / non-equivalence | Preserve as mapping context only; no equivalence or compliance claim. |
| Memory and Retrieval | Future work / requires separate track | Defer unless separately scoped. |
| Advanced cross-agent / cross-domain delegation | Future work / narrow-scope candidate | Defer broad treatment; include only narrow existing concepts if explicitly scoped. |
| Approval laundering and approval fatigue formal testing | Future work / requires separate track | Defer formal testing unless narrowly scoped. |
| Semantic validators | Future work | Defer to avoid validator overclaiming. |
| Production reference implementation | Non-goal unless separately scoped | Do not imply production implementation readiness. |
| Certification / compliance / conformity | Non-goal | Keep explicitly out of scope. |
| Legal sufficiency | Non-goal | Keep explicitly out of scope. |
| Audit sufficiency | Non-goal | Keep explicitly out of scope. |
| External-framework equivalence | Non-goal | Keep explicitly out of scope. |
| Empirical validation claim | Non-goal unless separately performed | Do not imply empirical validation from planning or validator results. |

## Planning-only register

### v0.5.x planning material

Initial posture:

- Planning-only / historical.

Reasoning:

- v0.5.x materials contain important design and planning context.
- They may include concepts relevant to v1.0.0, but they were created as planning materials.
- They should not be treated as active baseline by file age, document number, or conceptual importance alone.

Recommended v1.0.0 treatment:

- Preserve as versioned planning context.
- Promote only through a later explicit decision.
- Summarize or reference where useful, rather than forcing all v0.5.x material into v1.0.0.

Promotion caution:

- Do not treat historical planning language as current baseline language without review.

### v0.6.x adoption and practical readiness material

Initial posture:

- Planning-only / review-readiness candidate.

Reasoning:

- v0.6.x materials strengthened practical adoption, operator guidance, legal/compliance applicability framing, implementation readiness, and validation-hardening planning.
- Some materials may be useful for v1.0.0 adoption guidance.
- They still need synthesis before becoming stable guidance.

Recommended v1.0.0 treatment:

- Review for adoption-package promotion.
- Preserve non-certification, non-compliance, and non-audit-sufficiency boundaries.
- Avoid treating adoption-readiness planning as operational readiness.

Promotion caution:

- Do not imply that planning material proves real-world deployment readiness.

### v0.7.0 roadmap and track planning artifacts

Initial posture:

- Planning-only by default.
- Stable guidance candidate by exception.

Reasoning:

- v0.7.0 produced mature planning and reviewability materials.
- Some areas, especially evidence gap classification, operational reconstruction, and risk-owner decision support, are strong stable guidance candidates.
- Track planning artifacts themselves should not automatically become baseline.

Recommended v1.0.0 treatment:

- Promote mature synthesized guidance where appropriate.
- Keep roadmap and track-specific coordination artifacts as planning/status material.
- Avoid making every v0.7.0 status file part of v1.0.0 baseline.

Promotion caution:

- Do not confuse roadmap completion with baseline adoption.

### Release preparation and wrap-up artifacts

Initial posture:

- Historical / planning-only.

Reasoning:

- Release preparation and wrap-up documents explain release posture and decisions.
- They are useful for traceability, but they are not necessarily current usage guidance.

Recommended v1.0.0 treatment:

- Preserve for traceability.
- Use them as evidence of planning decisions.
- Do not treat release-preparation checklists as standing release gates unless explicitly updated.

Promotion caution:

- Do not use older release-preparation language as current release status unless verified.

### Research positioning material

Initial posture:

- Planning-only / stable explanatory candidate.

Reasoning:

- Research positioning artifacts clarify candidate contributions, questions, and claim boundaries.
- They support future academic or research communication.
- They do not establish empirical validation, peer review, or accepted research claims.

Recommended v1.0.0 treatment:

- Preserve as explanatory context.
- Summarize carefully if needed in v1.0.0 public materials.
- Keep empirical validation and peer-review claims out of scope unless separately supported.

Promotion caution:

- Do not convert candidate research questions into research conclusions.

## Historical register

Historical materials should remain accessible when they explain:

- why a release was prepared,
- why a baseline was not changed,
- why a planning track was opened,
- why a planning track was closed,
- why a concept was deferred,
- why a claim boundary was preserved, or
- how the framework evolved.

Historical material should not be used as current guidance unless:

- a later artifact explicitly promotes it,
- a current entry-point document points to it for a specific purpose, or
- the historical context is clearly marked as historical.

## Future-work register

### Memory and Retrieval

Initial posture:

- Future work / requires separate track.

Why it matters:

- Memory and Retrieval affects persistent context, retrieved context, stale context, context poisoning, retrieval poisoning, cross-session influence, and action justification.
- It may affect who or what the system believes it is acting for.
- It may affect evidence interpretation and operational reconstruction.

Why it should be deferred:

- The domain is broad.
- It likely requires separate control language, evidence expectations, examples, testing procedures, and validator boundaries.
- Forcing it into v1.0.0 could destabilize the release scope.

Recommended v1.0.0 posture:

- Mention as future work where needed.
- Do not require Memory and Retrieval coverage for v1.0.0.
- Do not imply that v1.0.0 fully addresses memory or retrieval risks.

### Advanced cross-agent / cross-domain delegation

Initial posture:

- Future work / narrow-scope candidate.

Why it matters:

- Cross-agent and cross-domain delegation can affect authority propagation, delegated principals, downstream actions, budget propagation, tool access, and evidence chains.

Why it should be deferred:

- Full treatment may require additional controls, examples, assessment procedures, evidence expectations, and boundary definitions.
- The current framework contains useful concepts, but broad stable coverage should not be assumed.

Recommended v1.0.0 posture:

- Preserve existing concepts.
- Avoid broad claims.
- Allow narrow guidance only if explicitly scoped.

### Approval laundering and approval fatigue formal testing

Initial posture:

- Future work / requires separate test formalization.

Why it matters:

- Human approval can be degraded by rubber-stamping, fatigue, approval laundering, unclear delegated authority, or misleading presentation.
- These issues are practically important for high-impact actions.

Why it should be deferred:

- Formal testing criteria require careful design.
- Evidence expectations must be precise.
- It may require additional examples or assessment procedures.

Recommended v1.0.0 posture:

- Preserve approval-quality concerns.
- Do not claim full formal testing coverage unless separately scoped.
- Consider later approval-quality test formalization.

### Semantic validators

Initial posture:

- Future work.

Why it matters:

- Semantic validators may eventually help check deeper consistency, claim boundaries, or control semantics.

Why it should be deferred:

- Semantic validation can overclaim meaning, intent, correctness, or sufficiency.
- Current validator posture is safer when structural and scope-bounded.
- Adding semantic validators prematurely could create false assurance.

Recommended v1.0.0 posture:

- Preserve current validator claim boundaries.
- Do not require semantic validators for v1.0.0.
- Consider only narrow semantic checks if separately scoped and clearly bounded.

### Production reference implementation

Initial posture:

- Non-goal unless separately scoped.

Why it matters:

- A production reference implementation could help adoption.

Why it should be deferred:

- It would require security review, implementation validation, operational assumptions, threat modeling, deployment boundaries, and maintenance expectations.
- v1.0.0 documentation should not imply production readiness without that work.

Recommended v1.0.0 posture:

- Do not claim production reference implementation readiness.
- Keep prototype and reference materials clearly bounded.
- Treat implementation materials as review or guidance unless separately validated.

### Empirical validation

Initial posture:

- Non-goal unless separately performed.

Why it matters:

- Empirical validation could strengthen research and adoption claims.

Why it should be deferred:

- Planning artifacts and repository validators do not provide empirical validation by themselves.
- Empirical work requires study design, data, method, evaluation, and interpretation.

Recommended v1.0.0 posture:

- Do not claim empirical validation.
- Preserve candidate research questions.
- Consider future empirical evaluation as a separate track.

## Non-goal register

v1.0.0 should not claim or imply the following.

### Certification

AAEF v1.0.0 should not be described as a certification scheme.

It may provide a framework, baseline, guidance, or assessment-support material, but certification would require a separate governance and conformity-assessment structure.

### Compliance

AAEF v1.0.0 should not claim legal or regulatory compliance.

It may help organizations reason about AI-agent action authority and evidence, but it should not be represented as satisfying laws, regulations, or third-party requirements.

### Audit sufficiency

AAEF v1.0.0 should not claim audit sufficiency.

It may help organize evidence expectations and review questions, but audit sufficiency depends on scope, auditor judgment, evidence quality, context, and applicable criteria.

### Legal sufficiency

AAEF v1.0.0 should not claim legal sufficiency.

It is not legal advice and should not be represented as determining legal authorization, liability, compliance, or enforceability.

### External-framework equivalence

AAEF v1.0.0 should not claim equivalence to NIST, ISO, OWASP, MITRE, CSA, or other external frameworks.

Mappings may be contextual and conservative, but they should not be presented as compliance, substitution, or equivalence.

### Production readiness

AAEF v1.0.0 should not claim production readiness.

A document baseline can be usable without proving that an implementation is deployable, secure, complete, or operationally mature.

### Implementation conformance

AAEF v1.0.0 should not claim that a specific implementation conforms unless a separate conformance process exists.

Implementation reviewability is not implementation conformance.

### Automated risk acceptance

AAEF v1.0.0 should not automate risk acceptance.

Risk-owner decision materials support review and judgment. They do not replace management decision-making.

## Narrow-scope candidate register

Some areas may be included in v1.0.0 if they are tightly scoped.

| Area | Possible narrow scope | Required caution |
| --- | --- | --- |
| Cross-agent authority | Preserve core delegation questions and evidence expectations already documented. | Do not claim full cross-agent governance coverage. |
| Approval quality | Preserve approval evidence and human decision-accountability concerns. | Do not claim full laundering/fatigue testing coverage. |
| Implementation reviewability | Provide reading paths and responsibility boundaries. | Do not claim implementation conformance. |
| Validator boundaries | Define what validators check and do not check. | Do not imply semantic sufficiency. |
| External mappings | Provide conservative context. | Do not imply equivalence or compliance. |

## Register maintenance rules

This register should be updated when:

- a future-work domain is explicitly scoped into a v1.0.0 track,
- a planning-only artifact is promoted into stable guidance,
- a stable guidance candidate is promoted into baseline,
- an area is moved from future work to non-goal,
- a claim boundary changes,
- a new release communication plan changes public wording, or
- a later roadmap replaces this register.

Until such an update occurs, future-work and non-goal areas should not be treated as v1.0.0 deliverables.

## Relationship to #351 acceptance criteria

This register supports #351 by documenting:

- planning-only artifacts,
- historical artifacts,
- future-work domains,
- deferred domains,
- non-goals,
- claim boundaries, and
- areas requiring separate tracks.

It complements `docs/en/status/v100-promoted-artifact-candidate-inventory.md` by clarifying what should not be promoted automatically.

## Review questions

Reviewers should be able to answer:

- Does this register prevent v1.0.0 scope creep?
- Does it preserve planning-only and historical context without deleting useful material?
- Does it explicitly defer unresolved domains?
- Does it distinguish future work from non-goals?
- Does it preserve conservative claim boundaries?
- Does it prevent roadmap completion from being mistaken for baseline change?
- Does it support follow-up planning under #351 and roadmap #350?

## Scope reminder

This artifact is planning and register material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, JSON examples, release tags, or GitHub Releases.

It does not establish operational readiness, production readiness, implementation conformance, empirical validation, certification, compliance, conformity, audit sufficiency, legal sufficiency, automated risk acceptance, or external-framework equivalence.
