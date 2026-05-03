# v0.7.0 Research Question Inventory

## Purpose

This document inventories candidate research questions for the v0.7.0 Research Positioning track.

It builds on:

- `docs/en/status/v070-research-positioning-planning.md`
- `docs/en/status/v070-research-contribution-inventory.md`

The goal is to make AAEF's research direction easier to review, discuss, and refine without claiming empirical validation, peer review, implementation conformance, production readiness, certification, compliance, conformity, audit sufficiency, legal sufficiency, or equivalence with external standards or frameworks.

## Relationship to prior research positioning artifacts

The research positioning planning artifact defines the overall posture for discussing AAEF as a research-oriented framework.

The research contribution inventory identifies candidate areas where AAEF may contribute to research discussion.

This research question inventory turns those candidate contribution areas into reviewable research questions.

These questions are candidates only. They do not imply that AAEF has already answered them empirically.

## Inventory method

Each research question group is described using the following structure:

- **Question focus**: the area of inquiry.
- **Candidate questions**: research questions that may be developed later.
- **Why it matters**: why the question may be useful.
- **Current boundary**: what AAEF does not yet claim.
- **Possible future work**: artifacts, studies, comparisons, or evaluation paths that may support stronger future claims.

This structure is intended to make research planning explicit while preserving conservative claim boundaries.

## Question inventory summary

| Area | Question focus | Current boundary |
| --- | --- | --- |
| Authority separation | How model output should be separated from action authority | Does not prove safe or correct implementation |
| Execution decision boundaries | How allow, deny, hold, and escalation decisions should be reviewed | Does not claim implementation conformance |
| Action-bound evidence | What evidence is needed to reconstruct a specific action or non-action | Does not claim audit or legal sufficiency |
| Delegation and principal context | How acting and represented principals should be distinguished | Does not solve all identity or legal agency questions |
| Non-execution reviewability | How denied, held, or not-dispatched actions should be evidenced | Does not prove absence of all side effects |
| Operational reconstruction | How action chains should be reconstructed after execution or failure | Does not establish incident-response certification |
| Claim-boundary discipline | How assurance language should avoid overclaiming | Does not create external-framework equivalence |
| Evaluation design | How AAEF concepts might be evaluated in future work | Does not claim empirical validation |
| Related-work positioning | How AAEF should be compared with adjacent fields | Does not claim replacement, equivalence, or superiority |

## Question group 1: Authority separation

### Question focus

This group asks how model output should be separated from authority to execute actions.

### Candidate questions

- How should an agentic system distinguish between model-generated action proposals and authorized action requests?
- What information should be required before model output can be transformed into an action request?
- Which component should be responsible for converting model output into a reviewable action request?
- How should systems preserve evidence that model output was not treated as authority by itself?
- What failure modes occur when model output is treated as authority without an execution-bound authorization step?
- How can reviewers identify whether a system separates generation, authorization, dispatch, and backend acceptance?

### Why it matters

Agentic AI systems may produce text that resembles instructions, commands, or operational decisions.

Without a clear authority boundary, reviewers may not be able to distinguish between what the model generated and what the system was authorized to do.

AAEF's core thesis is that model output is not authority. This question group explores how that thesis can be represented, reviewed, and eventually evaluated.

### Current boundary

AAEF does not claim that any specific implementation correctly separates model output from execution authority.

AAEF also does not claim that authority separation alone makes a system safe, secure, compliant, or production-ready.

### Possible future work

Potential future work includes:

- terminology and concept boundary note,
- authority-separation evaluation scenario candidates,
- comparison with access-control and policy-enforcement models,
- implementation review checklist expansion, and
- paper-outline material on action authority separation.

## Question group 2: Execution decision boundaries

### Question focus

This group asks how execution decisions should be represented and reviewed.

### Candidate questions

- What should count as an execution-bound authorization decision in an agentic AI system?
- How should allow, deny, hold, escalation, and non-dispatch decisions be represented?
- What evidence should connect an action request to an execution decision?
- How should reviewers distinguish authorization decision logic from tool dispatch enforcement?
- What information should be visible when a decision is held for human review?
- How should policy versions, authority sources, and decision context be represented without exposing inappropriate sensitive data?
- How should a system prevent a model or runtime from bypassing the execution decision boundary?

### Why it matters

Risk often materializes at the point where a system decides whether an action may be executed.

Reviewing model output alone is insufficient if the key control point is the execution decision boundary.

AAEF may contribute by making this boundary explicit and reviewable.

### Current boundary

AAEF does not claim that any specific authorization model, policy engine, tool gateway, or backend enforcement pattern is complete.

AAEF also does not claim that validator success proves runtime correctness or implementation conformance.

### Possible future work

Potential future work includes:

- execution-decision terminology note,
- authorization decision artifact profile refinement,
- evaluation walkthroughs for allowed, denied, and held actions,
- operational reconstruction scenarios, and
- research comparison with policy decision and policy enforcement concepts.

## Question group 3: Action-bound evidence

### Question focus

This group asks what evidence is needed to reconstruct a specific action or non-action.

### Candidate questions

- What evidence is necessary to reconstruct an AI-assisted action from request to result?
- How should evidence be tied to a specific action request, authorization decision, dispatch outcome, backend result, and review event?
- How should systems distinguish action-bound evidence from model explanations or runtime self-reports?
- Which evidence should be independently generated or corroborated?
- How should evidence gaps be represented?
- How should evidence show whether an action was executed, denied, held, not dispatched, or partially attempted?
- What minimum evidence is needed for a reviewer to understand what happened without overclaiming audit sufficiency?

### Why it matters

Agentic systems may produce plausible narratives that do not reliably prove what occurred.

AAEF emphasizes action-bound evidence so reviewers can reason about specific actions rather than relying only on general logs or model explanations.

### Current boundary

AAEF does not claim legal sufficiency, audit sufficiency, tamper-proof evidence, or complete reconstruction in all deployments.

AAEF also does not claim that its evidence model is sufficient for every legal, regulatory, operational, or forensic context.

### Possible future work

Potential future work includes:

- action-bound evidence research note,
- evidence gap classification,
- non-execution evidence checklist,
- reconstruction exercise expansion,
- evaluation scenario candidates, and
- comparison with audit logging and evidence-based assurance practices.

## Question group 4: Delegation and principal context

### Question focus

This group asks how acting principals, represented principals, and authority context should be distinguished.

### Candidate questions

- How should an agentic system represent who or what acted?
- How should a system represent on whose behalf an action was taken?
- How should a system distinguish user intent, organizational authority, model output, runtime behavior, and backend acceptance?
- What evidence should support the authority chain for an action?
- How should principal context expire, degrade, or require reauthorization over time?
- What should reviewers do when principal context is stale, ambiguous, or incomplete?
- How should delegation be represented without claiming to solve all legal agency questions?

### Why it matters

Agentic systems may act across layers of delegation involving users, organizations, models, runtimes, tools, APIs, and backend systems.

Without explicit principal context, responsibility and authority may become difficult to reconstruct.

### Current boundary

AAEF does not claim to solve all identity governance, delegation, impersonation, consent, or legal agency questions.

AAEF should not be presented as a complete identity and access-management framework.

### Possible future work

Potential future work includes:

- principal context terminology note,
- principal context degradation planning,
- delegation-boundary research questions,
- reconstruction scenarios involving stale authority,
- comparison with identity and access-management concepts, and
- risk-owner decision support links.

## Question group 5: Non-execution reviewability

### Question focus

This group asks how denied, held, escalated, or not-dispatched actions should be represented and reviewed.

### Candidate questions

- What evidence is needed to show that an action was denied, held, escalated, or not dispatched?
- How should systems distinguish non-execution from failed execution?
- How should systems represent partial attempts, blocked attempts, or ambiguous side effects?
- What evidence should prove that a tool dispatch enforcement point prevented execution?
- What should reviewers ask when non-execution evidence is incomplete?
- How should high-impact action workflows represent hold, freeze, and escalation states?
- How can non-execution reviewability be evaluated without claiming absence of all side effects?

### Why it matters

For high-impact actions, evidence that an action did not execute can be as important as evidence that an action executed correctly.

AAEF may contribute by treating non-execution outcomes as first-class review targets.

### Current boundary

AAEF does not prove absence of all side effects.

AAEF also does not claim that every denied, held, or not-dispatched action is risk-free.

### Possible future work

Potential future work includes:

- non-execution reconstruction planning,
- denied-action and held-action walkthroughs,
- evidence gap classification for non-execution,
- high-impact action review questions, and
- operational reconstruction track alignment.

## Question group 6: Operational reconstruction

### Question focus

This group asks how reviewers should reconstruct action chains after execution, denial, hold, escalation, or evidence failure.

### Candidate questions

- What sequence of events should be reconstructed after an AI-assisted action?
- How should reviewers reconstruct the action request, authority source, authorization decision, dispatch outcome, backend response, and evidence chain?
- How should evidence gaps be assigned to components or roles?
- What reconstruction questions should operators, reviewers, risk owners, and auditors ask?
- How should reconstruction handle conflicting evidence?
- How should reconstruction handle missing evidence?
- How should reconstruction distinguish action failure, evidence failure, authorization failure, dispatch failure, and backend rejection?
- How should AAEF connect research positioning with operational reconstruction work under #322?

### Why it matters

When an AI-assisted action produces an unexpected outcome, reviewers need more than a transcript.

They need a way to reconstruct the authority, decision, execution, and evidence chains.

### Current boundary

AAEF does not claim incident-response certification, root-cause completeness, legal sufficiency, or audit sufficiency.

AAEF should be treated as a reconstruction aid, not as a complete incident investigation methodology.

### Possible future work

Potential future work includes:

- operational reconstruction planning,
- reconstruction question sets,
- authority-chain reconstruction examples,
- evidence gap taxonomy,
- reviewer/operator walkthroughs, and
- relationship notes between #321 and #322.

## Question group 7: Claim-boundary discipline

### Question focus

This group asks how research, planning, mapping, and review materials should avoid overstating what AAEF proves.

### Candidate questions

- What language should AAEF use when describing planning, review, implementation guidance, evidence, and evaluation?
- How should AAEF distinguish a framework proposal from a validated method?
- How should AAEF distinguish external-framework mapping from equivalence?
- How should AAEF distinguish validator success from implementation conformance?
- How should AAEF distinguish review support from audit sufficiency?
- How should public-facing materials avoid implying certification, compliance, conformity, safety, or legal sufficiency?
- What evidence would be needed before stronger claims could be considered?

### Why it matters

AI assurance frameworks can easily overclaim what they establish.

AAEF's conservative posture is part of its research and practical value because it keeps evidence, review, compliance, certification, and legal claims separate.

### Current boundary

AAEF does not claim certification, compliance, conformity, audit sufficiency, legal sufficiency, peer review, empirical validation, or external-framework equivalence.

Future materials must preserve this boundary unless later work explicitly defines the evidence and review process for stronger claims.

### Possible future work

Potential future work includes:

- research claim-boundary checklist,
- public communication checklist,
- external-review readiness checklist,
- related-work comparison guidance,
- paper wording guidance, and
- release-note claim-boundary review.

## Question group 8: Evaluation design

### Question focus

This group asks how AAEF concepts might be evaluated in future work.

### Candidate questions

- What would count as evidence that AAEF improves action reconstruction?
- What would count as evidence that AAEF improves reviewer understanding of authority boundaries?
- What scenario types would be suitable for evaluating action authority separation?
- How should allowed, denied, held, and failed actions be represented in evaluation scenarios?
- What metrics could be used without implying certification or conformance?
- How should qualitative reviewer studies be designed?
- How should prototype fixtures be used without overclaiming deployed-system validation?
- What would be required before claiming empirical support for a specific AAEF concept?

### Why it matters

AAEF currently includes planning and review artifacts, but future research may require evaluation designs.

This question group helps separate candidate evaluation paths from current validation claims.

### Current boundary

AAEF does not currently claim empirical validation, deployed-system validation, peer-reviewed validation, or implementation conformance.

Existing validators should not be interpreted as proving production readiness or runtime correctness.

### Possible future work

Potential future work includes:

- evaluation design planning,
- research scenario selection,
- reviewer study outline,
- prototype fixture evaluation boundary note,
- metric definition planning, and
- empirical claim-boundary checklist.

## Question group 9: Related-work positioning

### Question focus

This group asks how AAEF should be compared with adjacent fields and frameworks.

### Candidate questions

- How does AAEF relate to AI governance discussions without claiming equivalence?
- How does AAEF relate to access control and policy enforcement without claiming replacement?
- How does AAEF relate to audit logging without claiming audit sufficiency?
- How does AAEF relate to AI safety discussions without claiming that it solves AI safety?
- How does AAEF relate to model governance while focusing on action authority and evidence?
- How does AAEF relate to incident reconstruction without claiming a complete incident-response methodology?
- How should AAEF compare with external standards, frameworks, and guidance without implying compliance or conformity?

### Why it matters

AAEF sits near several existing domains. Research positioning requires careful comparison without overclaiming novelty, superiority, equivalence, or replacement.

### Current boundary

AAEF should not claim to replace, satisfy, certify against, or be equivalent to external standards, regulations, audit methods, governance frameworks, or safety frameworks.

### Possible future work

Potential future work includes:

- related-work positioning note,
- conservative comparison matrix,
- external-framework mapping claim-boundary checklist,
- research introduction outline, and
- public research communication guidance.

## Cross-question relationships

The question groups are related but should remain distinguishable.

Authority separation defines the central thesis. Execution decision boundaries identify where authority is applied. Action-bound evidence supports review. Delegation and principal context explain whose authority is involved. Non-execution reviewability covers blocked, held, or not-dispatched actions. Operational reconstruction connects the evidence after the fact. Claim-boundary discipline governs how strongly AAEF may be described. Evaluation design asks how future evidence could be developed. Related-work positioning asks how AAEF should be discussed in the broader research landscape.

Future research artifacts should avoid collapsing these questions into a single broad claim.

## Possible prioritization

Near-term #321 follow-up work may prioritize:

1. claim-boundary checklist,
2. terminology and concept boundary note,
3. related-work positioning note,
4. paper-outline candidate,
5. evaluation design planning.

The best next artifact depends on whether the immediate goal is external communication, academic framing, reviewer readiness, or future empirical work.

## Review questions

Reviewers should be able to answer:

- Does each question group preserve the thesis that model output is not authority?
- Does each question group distinguish candidate inquiry from answered research?
- Does each question group include a clear current boundary?
- Does this inventory avoid empirical validation, peer-review, implementation conformance, production-readiness, certification, compliance, conformity, audit sufficiency, legal sufficiency, and external-framework equivalence claims?
- Does this inventory connect clearly to the research positioning planning and research contribution inventory artifacts?
- Does this inventory create useful follow-up paths for #321 without changing the active baseline?

## Scope reminder

This artifact is planning and positioning material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, or JSON examples.
