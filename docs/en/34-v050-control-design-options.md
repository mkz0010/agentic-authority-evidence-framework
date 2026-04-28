# v0.5.0 Control Design Options

**Status:** Non-normative v0.5.0 planning design note
**AAEF baseline:** v0.4.1 Public Review Draft
**Scope:** Control design options before changing the control catalog, evidence schema, assessment worksheet, or testing procedures

> **Planning status:** This document is non-normative v0.5.0 planning material. It is not part of the normative v0.4.1 Public Review Draft baseline unless explicitly incorporated into the control catalog, evidence schema, assessment artifacts, testing procedures, or release notes.

## Purpose

This document summarizes control design options for the initial v0.5.0 planning themes.

The purpose is to decide whether the v0.5.0 concepts should become:

- strengthened existing controls;
- new control requirements;
- evidence schema refinements;
- testing procedure refinements;
- reference architecture guidance;
- or planning guidance only.

This document does not change the control catalog. It records design options before making normative control changes.

## Design Principles

v0.5.0 control design should follow these principles:

1. Avoid unnecessary control sprawl.
2. Prefer strengthening existing controls where the existing domain already fits.
3. Add new controls only when the concept introduces a distinct assessable obligation.
4. Keep evidence fields tied to trusted workflow, authorization, enforcement, or evidence components.
5. Avoid relying on model self-assessment for authority, ambiguity, degradation, or trust decisions.
6. Preserve AAEF's core premise: model output is not authority.
7. Keep v0.5.0 implementable for real agentic AI systems.

## Normative Incorporation Rules

v0.5.0 planning concepts do not become normative AAEF requirements merely because they are described in planning documents.

A planning concept becomes normative only when it is explicitly incorporated into one or more normative or assessment artifacts, such as:

- the control catalog CSV;
- the human-readable control requirements;
- the testing procedures;
- the assessment worksheet or assessment profiles;
- the evidence schema or required evidence examples;
- release notes that explicitly identify the incorporated change.

### Incorporation Outcomes

Each v0.5.0 planning concept should be resolved into one of the following outcomes before release.

| Outcome | Meaning | Required action |
| --- | --- | --- |
| Planning only | The concept remains design input for future work. | Keep it marked as non-normative planning material. |
| Guidance only | The concept informs implementation or assessment interpretation, but does not create a new requirement. | Add or update guidance text without changing control obligations. |
| Testing refinement | The concept changes how an existing control is tested. | Update testing procedures and validation expectations. |
| Evidence refinement | The concept requires new or clearer evidence expectations. | Update evidence guidance, examples, or schema candidates as appropriate. |
| Existing control refinement | The concept strengthens an existing control without creating a new control ID. | Update the relevant control requirement, testing procedure, and assessment artifacts together. |
| New control | The concept introduces a distinct assessable obligation that does not fit existing controls. | Add a new control ID and update related testing, assessment, mapping, and evidence artifacts. |

### Promotion Criteria

Before a planning concept is promoted into the control catalog or other normative artifacts, it should satisfy the following criteria:

1. **Distinct obligation:** The concept creates a clearly assessable obligation that is not already covered by existing controls.
2. **Action boundary relevance:** The obligation relates to authorization, execution, evidence, recovery, delegation, principal binding, human approval, or governance of agentic actions.
3. **Trusted evidence source:** Required evidence can be generated or corroborated by trusted workflow, authorization, enforcement, backend, or evidence components.
4. **Pass/fail testability:** The obligation can be evaluated with clear pass, partial, and fail criteria.
5. **Implementation feasibility:** The requirement can be implemented without assuming a universal identity system, universal agent protocol, or certification scheme.
6. **Backward compatibility:** The change does not unintentionally redefine the v0.4.1 baseline unless the release explicitly says so.
7. **Mapping impact:** Any external framework mapping impact is reviewed without claiming compliance equivalence, certification readiness, or audit sufficiency.

### Promotion Decision Record

For each v0.5.0 planning theme, the release preparation process should record:

- the chosen incorporation outcome;
- affected controls, schema fields, testing procedures, or assessment artifacts;
- whether the change is normative or guidance-only;
- expected evidence sources;
- known implementation burden;
- residual ambiguity or deferred work.

This decision record may be maintained in the relevant planning issue, release checklist, or future release notes.


## Preliminary v0.5.0 Incorporation Outcome Register

The following register provides an initial, non-normative disposition for the current v0.5.0 planning themes.

These outcomes are planning assumptions only. They do not change the v0.4.1 baseline and do not create new control obligations unless later incorporated into the relevant normative or assessment artifacts.

| Planning theme | Primary expected outcome | Secondary possible outcome | Current disposition |
| --- | --- | --- | --- |
| Principal Context Degradation | Existing control refinement | Guidance and testing refinement | Treat as a cross-cutting authority lifecycle concept that may refine authorization, delegation, memory, and governance controls without immediately creating a new control ID. |
| Cross-Agent and Cross-Domain Authority | Existing control refinement | New control candidate if existing delegation and authorization controls cannot express cross-boundary handoff risk | Keep as a planning topic until the framework determines whether cross-agent authority is a refinement of existing delegation controls or a distinct assessable obligation. |
| Authority Denial and Reauthorization Flow | Testing refinement | Evidence refinement and existing control refinement | Treat primarily as a testable behavior for denial, freeze, expiry, and reauthorization paths before deciding whether new control text is needed. |
| Risk-Proportional Evidence and Performance Overhead | Guidance only | Evidence refinement and assessment profile refinement | Treat as implementation and assessment guidance unless specific evidence expectations become required for higher assurance levels. |
| Tamper-Evident Evidence Storage | Evidence refinement | New control candidate for high-impact or audit-grade profiles | Keep as an evidence-integrity planning topic. Avoid requiring tamper-evident storage universally unless scoped to higher-risk profiles. |
| Approval Quality and Approval Fatigue | Existing control refinement | New HUM control candidate if approval quality cannot be adequately represented by existing HUM controls | Treat as a human-approval assurance refinement while preserving the distinction between meaningful approval and approval UI presence. |

### Outcome Review Questions

Before any theme is promoted beyond this preliminary disposition, reviewers should answer:

1. Does the theme create a distinct assessable obligation, or does it clarify an existing obligation?
2. Can the theme be tested using trusted evidence rather than model or runtime self-report alone?
3. Is the expected implementation burden proportional to the risk tier or assurance level?
4. Does the theme require a new control ID, or can it be expressed through control text, testing procedures, assessment guidance, or evidence expectations?
5. Would incorporating the theme change external mapping claims or require new mapping caveats?
6. Does the theme need schema support, or is document-level guidance sufficient?

### Release Preparation Use

During v0.5.0 release preparation, this register should be updated to record the selected incorporation outcome for each theme.

If a theme remains unresolved, it should either:

- remain marked as non-normative planning material;
- be deferred to a later v0.5.x planning issue; or
- be converted into a narrower implementation, testing, or evidence guidance item.


## Authority Lifecycle Model Relationship

The current authority-related planning themes are consolidated in `docs/en/50-authority-lifecycle-model.md`.

That model should be used as shared design context before promoting any of the following themes into normative or assessment artifacts:

- Principal Context Degradation;
- Cross-Agent and Cross-Domain Authority;
- Authority Denial and Reauthorization Flow.

The model is non-normative and does not itself change the v0.4.1 baseline.

## Theme 1: Principal Context Degradation

See: `docs/en/30-principal-context-degradation.md`

### Design Problem

AAEF already requires principal binding and principal context preservation.

However, preserved context is not always valid context. Principal context may become stale, semantically distant, broadened, or ambiguous during long-running, delegated, asynchronous, or multi-agent workflows.

### Option A: Strengthen Existing Controls

Strengthen `AAEF-PRN-02` to clarify that principal context must not only be preserved, but remain valid, current, bounded, and semantically connected to the requested high-impact action.

Potential refinements:

- add freshness and validity language;
- mention degraded context as a denial, escalation, or reauthorization trigger;
- require evidence of context refresh or reconfirmation where applicable;
- update testing procedures to include long-running workflows.

Benefits:

- avoids new control sprawl;
- keeps the concept within Principal Binding;
- aligns with existing assessment rows.

Risks:

- `AAEF-PRN-02` may become too broad;
- degradation behavior may be underemphasized if hidden inside context preservation.

### Option B: Add a New Principal Binding Control

Add a new control such as:

`AAEF-PRN-03: Systems shall detect and safely handle material principal context degradation before high-impact execution.`

Potential requirement scope:

- context freshness;
- semantic continuity;
- scope drift;
- delegation drift;
- reconfirmation triggers;
- denial or escalation on material degradation.

Benefits:

- makes the concept directly assessable;
- gives v0.5.0 a clear new control artifact;
- supports dedicated testing and evidence.

Risks:

- increases catalog size;
- may overlap with `AAEF-PRN-02`, `AAEF-AUZ-08`, and `AAEF-AUZ-09`.

### Option C: Treat as Evidence and Testing Guidance Only

Keep existing control requirements unchanged, but update testing procedures and evidence schema guidance.

Benefits:

- lower disruption;
- useful for v0.5.x incremental refinement.

Risks:

- may not be strong enough for a v0.5.0 design theme;
- may leave ambiguity about whether degraded context must block execution.

### Recommended Direction

Use a hybrid approach:

- strengthen `AAEF-PRN-02`;
- add testing procedure refinements for long-running and delegated workflows;
- consider a new `AAEF-PRN-03` only if the strengthened `AAEF-PRN-02` becomes too broad.

For v0.5.0, the preferred first step is to strengthen `AAEF-PRN-02` and testing procedures before adding a new control.

## Theme 2: Cross-Agent and Cross-Domain Authority

See: `docs/en/31-cross-agent-cross-domain-authority.md`

### Design Problem

AAEF already addresses agent identity, principal binding, delegation, authorization, and evidence.

However, cross-agent and cross-domain workflows introduce a distinct problem: a receiving system must decide whether to rely on another agent's identity, authority claims, delegated scope, evidence, or execution results.

Agent-to-agent communication does not imply authority.

### Option A: Strengthen Existing Controls

Strengthen existing controls across `AAEF-ID`, `AAEF-PRN`, `AAEF-DEL`, `AAEF-AUZ`, `AAEF-EVD`, and `AAEF-RES`.

Potential refinements:

- add external agent identity expectations to `AAEF-ID-*`;
- add cross-domain principal context expectations to `AAEF-PRN-02`;
- add receiving-side delegation verification to `AAEF-DEL-*`;
- add receiving-side authorization to `AAEF-AUZ-*`;
- add cross-domain evidence limitation language to `AAEF-EVD-*`.

Benefits:

- keeps the framework compact;
- uses existing domains;
- avoids premature protocol-specific controls.

Risks:

- cross-domain authority may become scattered across domains;
- reviewers may miss the combined cross-domain failure mode.

### Option B: Add Dedicated Cross-Agent / Cross-Domain Controls

Add a small set of controls such as:

- `AAEF-XAD-01: Receiving systems shall verify external agent identity and authority before accepting high-impact delegated work.`
- `AAEF-XAD-02: Cross-domain authority assertions shall be constrained, attributable, time-bound, and evidence-linked where used.`
- `AAEF-XAD-03: Cross-domain evidence limitations shall be recorded when evidence cannot be independently verified.`

Benefits:

- makes the cross-domain problem explicit;
- aligns with `HIA-A2A`;
- provides clear assessment hooks for multi-agent ecosystems.

Risks:

- introduces a new domain;
- may be too early without implementation experience;
- may overlap with identity, delegation, and evidence controls.

### Option C: Define an Authority Assertion Profile First

Do not add controls yet. First define a non-normative authority assertion profile. A planning profile is maintained in `docs/en/35-authority-assertion-profile.md`.

Potential fields:

- issuer;
- subject agent;
- agent instance;
- principal reference;
- delegated scope;
- allowed action types;
- resources;
- purpose;
- trust domain;
- expiration;
- delegation depth;
- redelegation permission;
- revocation check reference;
- evidence reference;
- policy version;
- integrity or signature reference.

Benefits:

- clarifies the data model before control changes;
- avoids protocol lock-in;
- supports later schema and architecture work.

Risks:

- may not produce immediate control improvements;
- could drift into implementation design before control semantics are stable.

### Recommended Direction

Use a staged approach:

1. strengthen `HIA-A2A` guidance;
2. strengthen existing `ID`, `PRN`, `DEL`, `AUZ`, and `EVD` language for receiving-side verification;
3. define a non-normative authority assertion profile;
4. consider dedicated cross-agent controls only if the existing domains cannot express the requirements clearly.

For v0.5.0, the preferred first step is to strengthen existing controls and architecture guidance rather than immediately creating a new domain.

## Theme 3: Authority Denial and Reauthorization Flow

See: `docs/en/32-authority-denial-reauthorization-flow.md`

### Design Problem

AAEF already includes `AAEF-AUZ-09` and `AAEF-EVD-06`.

The remaining question is whether these controls are sufficient, or whether denial, retry, task splitting, safe termination, and reauthorization need stronger requirements or additional evidence fields.

### Option A: Strengthen Existing Controls

Strengthen `AAEF-AUZ-09`, `AAEF-EVD-05`, and `AAEF-EVD-06`.

Potential refinements:

- clarify safe denial, deferral, escalation, scoped reauthorization, retry control, task splitting detection, and safe termination;
- require linkage to the original denied or deferred action;
- require retry count or retry correlation where applicable;
- require principal reconfirmation where context is stale or degraded;
- clarify that reauthorization must create a new decision, not silently mutate the original denial.

Benefits:

- fits existing controls well;
- avoids new control sprawl;
- directly improves already-implemented v0.4.x controls.

Risks:

- `AAEF-AUZ-09` may become dense;
- testing procedures must become more specific.

### Option B: Add a Dedicated Reauthorization Control

Add a new control such as:

`AAEF-AUZ-10: Reauthorization shall be scoped, attributable, linked to the original denial, and unable to bypass prior control decisions through retry, task splitting, or scope creep.`

Benefits:

- makes reauthorization behavior independently assessable;
- reduces density in `AAEF-AUZ-09`;
- supports specific testing.

Risks:

- overlaps with `AAEF-AUZ-09` and `AAEF-EVD-06`;
- may be unnecessary if existing controls can be clarified.

### Option C: Treat as Testing Procedure Refinement

Keep controls unchanged, but refine testing procedures for:

- retry loops;
- scope creep;
- task splitting;
- reauthorization linkage;
- safe termination;
- non-execution evidence.

Benefits:

- low disruption;
- useful immediately for assessment.

Risks:

- control requirements may remain underspecified;
- implementations may miss reauthorization semantics.

### Recommended Direction

Strengthen existing controls first:

- update `AAEF-AUZ-09`;
- update `AAEF-EVD-05`;
- update `AAEF-EVD-06`;
- update testing procedures for retry, scope creep, task splitting, and reauthorization linkage.

A new `AAEF-AUZ-10` should be considered only if `AAEF-AUZ-09` becomes too broad.

## Cross-Theme Design Decisions

### Decision 1: Prefer Existing Domains First

The first v0.5.0 design pass should prefer strengthening existing controls before adding new domains.

Likely affected domains:

- `AAEF-PRN`
- `AAEF-DEL`
- `AAEF-AUZ`
- `AAEF-EVD`
- `AAEF-RES`
- `AAEF-ID`

### Decision 2: Add New Controls Only When Assessability Requires It

New controls should be added only where the requirement is:

- distinct;
- testable;
- evidence-backed;
- not clearly covered by existing controls;
- important enough to be visible in the catalog.

### Decision 3: Evidence Schema Changes Should Follow Control Semantics

Evidence schema fields should not be added before deciding which control obligations they support.

Candidate future fields should remain planning candidates until control behavior is stable.

### Decision 4: Testing Procedure Refinements Are Likely Required

Regardless of whether new controls are added, testing procedures will likely need v0.5.0 refinements for:

- long-running workflow context degradation;
- cross-agent authority verification;
- receiving-side authorization;
- retry loops;
- reauthorization linkage;
- task splitting;
- evidence trust gaps.

## Recommended v0.5.0 Control Design Path

The recommended path is:

1. Strengthen existing controls where feasible.
2. Add new controls only if strengthened controls become overloaded.
3. Define non-normative evidence and authority assertion candidates.
4. Refine testing procedures after control wording stabilizes.
5. Update reference architecture after the control semantics are clear.

## Candidate First Control Updates

A conservative first control update pass should focus on:

- `AAEF-PRN-02`
- `AAEF-DEL-05`
- `AAEF-AUZ-08`
- `AAEF-AUZ-09`
- `AAEF-EVD-05`
- `AAEF-EVD-06`
- `AAEF-RES-04`

These controls already carry much of the v0.5.0 design pressure.

## Non-Goals

This design note does not:

- add or modify controls;
- add or modify evidence schema fields;
- add or modify assessment worksheet rows;
- require a new control domain;
- require a specific identity protocol;
- require a specific agent-to-agent protocol;
- require a specific evidence store implementation.

## Open Questions

1. Is strengthening `AAEF-PRN-02` enough for Principal Context Degradation?
2. Should Cross-Agent and Cross-Domain Authority become a dedicated control domain?
3. Should AAEF define a non-normative authority assertion profile in v0.5.0?
4. Should reauthorization become a dedicated authorization control or remain part of `AAEF-AUZ-09`?
5. Which evidence schema fields are essential for v0.5.0, and which should remain optional?
6. How much testing procedure expansion is acceptable before assessment burden becomes too high?

## Evidence Integrity Levels Relationship

The current evidence-related planning themes are consolidated in `docs/en/51-evidence-integrity-levels.md`.

That model should be used as shared design context before promoting any of the following themes into normative or assessment artifacts:

- Risk-Proportional Evidence and Performance Overhead;
- Tamper-Evident Evidence Storage.

The model is non-normative and does not itself change the v0.4.1 baseline.

