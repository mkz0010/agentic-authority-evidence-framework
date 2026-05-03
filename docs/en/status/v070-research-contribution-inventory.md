# v0.7.0 Research Contribution Inventory

## Purpose

This document inventories candidate research contribution areas for AAEF as part of the v0.7.0 Research Positioning track.

It builds on `docs/en/status/v070-research-positioning-planning.md` by making the candidate research contribution areas more reviewable.

This document is planning and positioning material only. It does not claim empirical validation, peer review, implementation conformance, production readiness, certification, compliance, conformity, audit sufficiency, legal sufficiency, or equivalence with external standards or frameworks.

## Relationship to research positioning planning

The research positioning planning artifact defines the initial posture for discussing AAEF as a research-oriented framework.

This contribution inventory narrows that posture into specific contribution candidates that may support future research artifacts, papers, talks, comparisons, or review discussions.

The inventory should help reviewers distinguish between:

- what AAEF may contribute conceptually,
- what AAEF may help make reviewable,
- what evidence or evaluation would be needed before stronger claims could be made, and
- what AAEF must not claim at this stage.

## Inventory method

Each candidate contribution area is described using the following structure:

- **Candidate contribution**: what AAEF may contribute to research discussion.
- **Research relevance**: why the contribution may matter.
- **Reviewable boundary**: what the contribution makes easier to inspect or reason about.
- **Required caution**: what must not be overclaimed.
- **Future work**: possible later artifacts or evaluation work.

This structure is intended to keep research framing useful without turning planning material into unsupported validation claims.

## Contribution inventory summary

| Area | Candidate contribution | Reviewable boundary | Main caution |
| --- | --- | --- | --- |
| Action authority separation | Separates model output from authority to execute actions | Distinction between generated instruction-like text and execution authority | Does not prove a system is safe or compliant |
| Execution-bound decision review | Focuses review on the allow, deny, hold, or escalate decision point | Authorization and enforcement decision boundaries | Does not claim implementation conformance |
| Action-bound evidence | Connects evidence to a specific action or non-action | Evidence correlation to action request, decision, execution, and result | Does not claim audit sufficiency |
| Delegation and principal context | Makes acting principal and represented principal explicit | Who acted, on whose behalf, and under what authority | Does not solve all identity or delegation models |
| Non-execution reviewability | Treats denied, held, or not-executed actions as reviewable outcomes | Evidence for non-execution and blocked execution | Does not prove absence of all side effects |
| Reconstruction support | Supports post-event reconstruction of action chains | Timeline, authority chain, decision chain, and evidence gaps | Does not establish incident-response certification |
| Claim-boundary discipline | Separates useful assurance evidence from compliance or certification overclaims | Language used in controls, mappings, examples, and research materials | Does not create external-framework equivalence |

## Candidate contribution 1: Action authority separation

### Candidate contribution

AAEF frames model output as distinct from authority to execute an action.

This may contribute to research discussions by providing a clear boundary between:

- model-generated text,
- agent runtime interpretation,
- authorization decisions,
- tool dispatch,
- backend acceptance,
- evidence generation, and
- later review.

### Research relevance

Agentic AI systems often blur the practical distinction between generating an instruction and carrying out an action.

AAEF makes that distinction explicit by treating model output as insufficient authority by itself.

This may be useful in discussions of AI governance, AI safety, access control, operational risk, auditability, and accountability.

### Reviewable boundary

This contribution makes the following boundary easier to review:

- Was the model output merely a request, recommendation, or proposed action?
- Which component decided whether the action was authorized?
- Which component enforced the execution decision?
- Which component accepted or rejected the action?
- Which evidence shows the transition from proposed action to allowed, denied, held, or executed action?

### Required caution

This contribution does not prove that a system is safe, secure, compliant, auditable, or production-ready.

It also does not prove that a specific implementation correctly separates model output from execution authority.

### Future work

Potential future artifacts include:

- a terminology boundary note,
- a research question inventory,
- a related-work positioning note,
- a paper outline section on authority separation, and
- candidate evaluation scenarios for authority-bound action review.

## Candidate contribution 2: Execution-bound decision review

### Candidate contribution

AAEF emphasizes the point where an action is allowed, denied, held, or escalated.

This may contribute to research discussion by shifting review from model output alone to the execution decision boundary.

### Research relevance

Many AI risk discussions focus on what a model said, intended, or recommended.

AAEF focuses on whether the system permitted or prevented an action at the point where execution authority mattered.

This may help separate model behavior analysis from system governance analysis.

### Reviewable boundary

This contribution makes the following boundary easier to review:

- What action was requested?
- What policy or authority source was used?
- What decision was made?
- Was the action allowed, denied, held, escalated, or otherwise constrained?
- Which component enforced the decision?
- What evidence proves the decision outcome?

### Required caution

This contribution does not claim that any specific authorization model, policy engine, or enforcement point is complete.

It also does not claim that a passing validator result establishes implementation conformance or runtime correctness.

### Future work

Potential future artifacts include:

- an execution-decision research question inventory,
- a decision-boundary comparison note,
- operational reconstruction artifacts for allowed and denied actions, and
- evaluation walkthroughs focused on decision transitions.

## Candidate contribution 3: Action-bound evidence

### Candidate contribution

AAEF emphasizes evidence that can be tied to a specific action, decision, and execution outcome.

This may contribute to research discussions by distinguishing action-bound evidence from general logs, model explanations, or system self-reports.

### Research relevance

Agentic systems may generate plausible explanations after the fact. Such explanations are not necessarily reliable evidence of what occurred.

AAEF encourages evidence that can support reconstruction of:

- the action request,
- the authorization decision,
- the dispatch or non-dispatch outcome,
- backend acceptance or rejection,
- execution result, and
- reviewable event chain.

### Reviewable boundary

This contribution makes the following boundary easier to review:

- Is the evidence tied to the specific action under review?
- Is the evidence independently generated or corroborated?
- Can the evidence be correlated across authorization, dispatch, backend, and evidence components?
- Does the evidence distinguish execution from non-execution?
- Are evidence gaps visible?

### Required caution

This contribution does not claim that AAEF evidence is legally sufficient, audit sufficient, or tamper-proof in all deployments.

It also does not claim that every relevant event can always be reconstructed.

### Future work

Potential future artifacts include:

- an action-bound evidence research note,
- a reconstruction evidence gap taxonomy,
- a non-execution evidence checklist,
- an evidence quality research question inventory, and
- candidate evaluation scenarios for evidence reconstruction.

## Candidate contribution 4: Delegation and principal context

### Candidate contribution

AAEF makes principal context explicit by asking who or what acted, on whose behalf, and with what authority.

This may contribute to research discussions about delegated authority in agentic AI systems.

### Research relevance

Agentic AI systems may act across layers of delegation involving users, organizations, models, agent runtimes, tools, APIs, and backend services.

AAEF provides a way to discuss whether the acting component and represented principal are distinguishable.

### Reviewable boundary

This contribution makes the following boundary easier to review:

- Which principal requested or initiated the action?
- Which component acted?
- On whose behalf did the component act?
- What authority was asserted?
- Was that authority current, scoped, and appropriate for the action?
- Can the authority chain be reconstructed?

### Required caution

This contribution does not solve all identity, delegation, impersonation, consent, or legal agency questions.

It should not be presented as a complete identity governance framework.

### Future work

Potential future artifacts include:

- a principal-context terminology note,
- a delegation-boundary research question inventory,
- a principal context degradation note,
- a related-work comparison with identity and access-management concepts, and
- reconstruction scenarios involving stale or ambiguous principal context.

## Candidate contribution 5: Non-execution reviewability

### Candidate contribution

AAEF treats denied, held, escalated, or otherwise not-executed actions as reviewable outcomes.

This may contribute to research discussions by making non-execution part of the evidence and assurance model.

### Research relevance

For high-impact actions, proving that an action did not execute, was blocked, or was held for review can be as important as proving that an action executed correctly.

AAEF encourages review of both execution and non-execution paths.

### Reviewable boundary

This contribution makes the following boundary easier to review:

- Was the action denied, held, escalated, or not dispatched?
- Which component made that decision?
- Which component enforced that decision?
- What evidence supports non-execution?
- Was any partial execution, attempted execution, or side effect visible?
- Were gaps or ambiguities recorded?

### Required caution

This contribution does not prove the absence of all side effects.

It also does not prove that every denied or held action was risk-free.

### Future work

Potential future artifacts include:

- non-execution reconstruction planning,
- denied-action evidence examples,
- hold/escalation review questions,
- evidence gap classification for non-execution, and
- candidate evaluation scenarios for blocked or held actions.

## Candidate contribution 6: Operational reconstruction support

### Candidate contribution

AAEF supports reconstruction of action chains after execution, denial, hold, escalation, or evidence failure.

This may contribute to research discussions about post-event review and responsibility triage in agentic AI systems.

### Research relevance

When an AI-assisted action produces an unexpected result, reviewers need more than a model transcript.

They need to reconstruct the authority chain, decision chain, execution chain, and evidence chain.

AAEF provides a structured way to ask those reconstruction questions.

### Reviewable boundary

This contribution makes the following boundary easier to review:

- What was requested?
- Who or what requested it?
- What authority was used?
- What decision was made?
- What action was dispatched or not dispatched?
- What did the backend accept or reject?
- What evidence exists?
- What evidence is missing?
- Which component or role owns the gap?

### Required caution

This contribution does not establish incident-response certification, audit sufficiency, legal sufficiency, or root-cause completeness.

It should be treated as a reconstruction aid, not as a complete incident investigation methodology.

### Future work

Potential future artifacts include:

- operational reconstruction planning,
- reconstruction question sets,
- authority-chain reconstruction examples,
- evidence gap classification,
- reviewer/operator walkthroughs, and
- relationship notes connecting #321 and #322.

## Candidate contribution 7: Claim-boundary discipline

### Candidate contribution

AAEF repeatedly separates reviewable assurance evidence from unsupported claims of compliance, certification, safety, or equivalence.

This may contribute to research discussion by making claim boundaries explicit in framework artifacts.

### Research relevance

AI assurance discussions can easily overstate what a framework, checklist, mapping, or validator result proves.

AAEF uses conservative language to preserve the difference between:

- planning support,
- review support,
- implementation guidance,
- evidence sufficiency for a scoped action,
- empirical validation,
- certification,
- legal compliance,
- audit opinion, and
- external-framework equivalence.

### Reviewable boundary

This contribution makes the following boundary easier to review:

- What is the artifact claiming?
- What is the artifact explicitly not claiming?
- What evidence would be required for a stronger claim?
- Does a mapping imply equivalence?
- Does a validator result imply implementation correctness?
- Does a planning document imply production readiness?

### Required caution

This contribution does not make AAEF automatically conservative in every future use.

Future artifacts must continue to preserve claim-boundary discipline.

### Future work

Potential future artifacts include:

- a research claim-boundary checklist,
- a public communication checklist,
- external-review readiness guidance,
- related-work comparison boundaries, and
- paper or talk wording guidance.

## Cross-contribution relationships

The contribution areas are related but should remain distinguishable.

Action authority separation defines the central boundary. Execution-bound decision review focuses on the point where that boundary is applied. Action-bound evidence supports review of the outcome. Delegation and principal context explain whose authority is involved. Non-execution reviewability covers blocked or held actions. Operational reconstruction connects these artifacts after the fact. Claim-boundary discipline controls how strongly the framework may be described.

Future research artifacts should avoid collapsing these into a single broad claim.

## Candidate research questions

Future #321 work may develop questions such as:

- How should authority be represented separately from model output in agentic AI systems?
- What evidence is necessary to reconstruct an AI-assisted action?
- How should denied, held, or not-executed actions be represented in assurance evidence?
- How should principal context be preserved or degraded over time?
- How can reviewers distinguish model explanation from action-bound evidence?
- What are appropriate claim boundaries for AI assurance frameworks that are not certification schemes?
- How can action-bound authorization and evidence concepts be evaluated without overclaiming external-framework equivalence?

These questions are candidates only. They do not imply that AAEF has already answered them empirically.

## Relationship to future #321 work

This inventory suggests several natural follow-up artifacts:

- research question inventory,
- terminology and concept boundary note,
- related-work positioning note,
- research claim-boundary checklist,
- paper-outline candidate, and
- external-review readiness checklist.

This document does not close #321 by itself.

## Review questions

Reviewers should be able to answer:

- Does each contribution candidate preserve the thesis that model output is not authority?
- Does each contribution candidate distinguish conceptual contribution from empirical validation?
- Does each contribution candidate include a clear caution against overclaiming?
- Does the inventory avoid certification, compliance, conformity, audit sufficiency, legal sufficiency, peer-review, and external-framework equivalence claims?
- Does the inventory create useful follow-up paths for future #321 work?
- Does the inventory avoid changing the active control and assessment baseline?

## Scope reminder

This artifact is planning and positioning material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, or JSON examples.
