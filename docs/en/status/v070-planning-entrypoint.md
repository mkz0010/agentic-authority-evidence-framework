# v0.7.0 Planning Entrypoint

## Status

This is the v0.7.0 planning entrypoint.

This document opens the next planning location after completion of the v0.6.0 / v0.6.x Practical Adoption Readiness cycle.

This document is:

- a planning entrypoint;
- a navigation aid for the next work cycle;
- a bridge from the v0.6.x completion checkpoint to future work;
- non-normative unless a later release explicitly promotes content into active guidance.

This document is not:

- a new control baseline;
- an evidence schema update;
- an assessment artifact update;
- a testing procedure update;
- a certification scheme;
- a compliance claim;
- a conformity claim;
- an audit opinion;
- a legal sufficiency claim;
- a production-readiness claim;
- an external framework equivalence claim;
- an empirical validation claim;
- a peer-review claim.

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

The purpose of this entrypoint is to make the next planning location visible after v0.6.x completion.

The v0.6.0 / v0.6.x cycle completed practical adoption-readiness planning, role-specific adoption guidance, active evidence example hardening, prototype fixture scoping, conservative external framework mapping, and research related-work positioning.

The next planning cycle should build on that foundation without reopening completed v0.6.x work.

This document is related to #317.

## Starting point

The starting point for v0.7.0 planning is the v0.6.x completion checkpoint:

- `docs/en/status/v060-practical-adoption-readiness-completion-checkpoint.md`

At the completion checkpoint:

- the v0.6.0 roadmap was closed;
- the initial v0.6.0 track issues were closed;
- the v0.6.x child follow-ups were closed;
- the deferred hardening and expansion follow-ups were closed;
- no `v0.6.0` labeled issues remained open;
- evidence example hygiene validation was added;
- conservative external mapping coverage was expanded;
- AAEF v0.4.1 remained the current control and assessment baseline.

## Candidate v0.7.0 focus

The v0.7.0 planning cycle should focus on the next layer after adoption readiness:

> Evaluation readiness, implementation reviewability, and research-facing positioning.

The purpose is not to claim that AAEF is empirically validated, production-ready, compliant, certified, conformant, or equivalent to an external framework.

The purpose is to define how AAEF could be reviewed, evaluated, explained, and extended in later work.

## Candidate planning themes

### 1. Evaluation readiness

Candidate questions:

- What can be evaluated using existing AAEF artifacts?
- Which evaluations are document/artifact reviews rather than empirical validation?
- Which scenario walkthroughs could test action authority separation?
- Which negative tests could demonstrate whether failures are detectable or reviewable?
- What evidence would be required before any stronger effectiveness claim?

Candidate outputs:

- evaluation design options;
- scenario walkthrough plans;
- negative test plans;
- reconstruction exercise plans;
- evaluation claim-boundary guidance.

### 2. Implementation reviewability

Candidate questions:

- What should implementers be able to review before building an AAEF-aligned system?
- Which parts of the prototype examples are static fixtures only?
- What minimal reference architecture can be reviewed without implying production readiness?
- How should implementation assumptions be documented?
- Which validator results support example hygiene but not conformance?

Candidate outputs:

- implementation review checklist;
- reference implementation boundary note;
- prototype validator scope note;
- implementation assumption inventory.

### 3. Research-facing positioning

Candidate questions:

- Which AAEF concepts are strongest as research contribution candidates?
- Which claims require citation support before public research use?
- Which adjacent frameworks and research areas should be cited?
- What would a conservative abstract say?
- What should be avoided in academic, workshop, or public-facing positioning?

Candidate outputs:

- research abstract draft;
- citation inventory planning;
- related-work source inventory;
- contribution and limitation statement;
- forbidden-claims checklist for research use.

### 4. Operational evaluation and reconstruction

Candidate questions:

- Can operators reconstruct why an action executed or did not execute?
- Are denied or blocked actions sufficiently reviewable?
- What operational evidence is required to support incident triage?
- Which evidence relationships should remain illustrative rather than mandatory?

Candidate outputs:

- action reconstruction exercise;
- non-execution review checklist;
- operator evaluation scenario set;
- evidence review workflow draft.

### 5. Governance and risk-owner decision support

Candidate questions:

- How should risk owners decide which agentic actions require stronger controls?
- How should approval scope, authority, and residual risk be represented?
- How can AAEF support risk discussions without becoming a compliance claim?
- How should executive-facing materials preserve claim boundaries?

Candidate outputs:

- risk-owner decision worksheet;
- high-impact action classification planning;
- residual-risk communication guide;
- executive-facing claim-boundary note.

## Candidate child tracks

The following tracks are candidates only. They should be converted into smaller issues before implementation.

| Candidate track | Purpose |
| --- | --- |
| Evaluation Readiness | Define evaluation methods without claiming empirical validation. |
| Implementation Reviewability | Make future implementation work reviewable without claiming production readiness. |
| Research Positioning | Prepare conservative research-facing materials and citation planning. |
| Operational Reconstruction | Define reviewable action and non-execution reconstruction exercises. |
| Risk-Owner Decision Support | Improve decision support while avoiding compliance and certification claims. |

## First recommended issue split

The first v0.7.0 issues should be narrow.

Recommended initial issues:

| Issue candidate | Scope |
| --- | --- |
| `[Track] v0.7.0: Evaluation Readiness` | Plan evaluation design options and claim boundaries. |
| `[Track] v0.7.0: Implementation Reviewability` | Plan reviewable implementation assumptions and reference boundaries. |
| `[Track] v0.7.0: Research Positioning` | Plan citation inventory, abstract, and contribution/limitation framing. |
| `[Track] v0.7.0: Operational Reconstruction` | Plan action reconstruction and non-execution review exercises. |
| `[Track] v0.7.0: Risk-Owner Decision Support` | Plan high-impact action and residual-risk decision support. |

These should remain planning issues until a later PR explicitly adds artifacts.

## Non-goals for v0.7.0 planning

The v0.7.0 planning entrypoint does not authorize:

- changing active controls;
- changing the evidence schema;
- changing assessment artifacts;
- changing testing procedures;
- claiming implementation conformance;
- claiming production readiness;
- claiming empirical validation;
- claiming peer review;
- claiming certification;
- claiming compliance;
- claiming conformity;
- claiming audit sufficiency;
- claiming legal sufficiency;
- claiming external framework equivalence;
- claiming complete external framework coverage;
- claiming mitigation completeness.

## Baseline statement

AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates one or more of:

- control catalog;
- evidence schema;
- assessment artifacts;
- testing procedures.

The v0.7.0 planning entrypoint does not change that baseline.

## Planning discipline

Future v0.7.0 work should preserve the discipline used during the v0.6.x completion cycle:

- small PRs;
- explicit issue scope;
- validation before merge;
- extended merge descriptions;
- conservative claim boundaries;
- active baseline separation;
- narrow follow-up splitting when scope expands.

## Recommended next step

After this entrypoint is merged, create the first small v0.7.0 track issues.

The recommended starting order is:

1. Evaluation Readiness;
2. Implementation Reviewability;
3. Research Positioning;
4. Operational Reconstruction;
5. Risk-Owner Decision Support.

This order starts from evaluation boundaries before moving into implementation, research, operations, or executive-facing materials.
