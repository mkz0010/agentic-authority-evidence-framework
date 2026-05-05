# post-v1.0.0 Next Roadmap Options

## Purpose

This document records next-roadmap options after the AAEF v1.0.0 release and the initial post-v1.0.0 repository, README, and public communication review work.

It supports issue #388, `[Track] post-v1.0.0: Repository and Roadmap Review`.

The goal is to avoid opening the next roadmap by inertia. The next roadmap should be opened only after maintainers choose a clear scope.

This document is planning material only. It does not publish a new release, change the active baseline, update the control catalog, update control IDs, update the evidence schema, update assessment artifacts, update testing procedures, add validators, add prototypes, add fixtures, add JSON examples, approve public announcement text, or make readiness, conformance, certification, compliance, audit, legal, or external-framework equivalence claims.

## Current posture

AAEF v1.0.0 has been published as a conservative release path planning release.

The active control and assessment baseline remains unchanged.

Post-v1.0.0 review has already produced:

- `docs/en/status/post-v100-repository-and-roadmap-review.md`
- `docs/en/status/post-v100-public-communication-and-readme-review.md`

A narrow README version / baseline status note has also been added to:

- `README.md`
- `README.ja.md`

This reduces the immediate public-entrypoint risk that readers may treat v1.0.0 as an active baseline update, certification claim, compliance claim, implementation-conformance claim, production-readiness claim, audit/legal sufficiency claim, or external-framework equivalence claim.

## Decision question

The next roadmap decision is:

> What should AAEF do after v1.0.0 without accidentally turning post-release review into unbounded roadmap expansion?

The decision should distinguish:

- immediate post-v1.0.0 cleanup;
- public communication;
- active baseline update candidates;
- implementation/adoption guidance;
- examples, fixtures, and validators;
- research positioning;
- AAEF-AI-VA or other implementation-specific work;
- deferral or no immediate roadmap.

## Option A: Close #388 after close-readiness checklist

Meaning:

- Treat the immediate post-v1.0.0 review as sufficient.
- Add a close-readiness checklist.
- Close #388 and milestone #15 if complete.
- Do not open a new roadmap immediately.

Benefits:

- Keeps the repository clean.
- Avoids roadmap inflation.
- Preserves the conservative post-v1.0.0 posture.
- Gives maintainers room to observe external feedback before opening new work.

Risks:

- Some useful next-step ideas may remain informal.
- Public communication or research positioning may be delayed.
- Implementation/adoption work may not receive a near-term roadmap.

Initial assessment:

- Safe default if no immediate next roadmap is needed.
- Recommended if maintainers want a pause after v1.0.0.

## Option B: Open a small post-v1.0.0 stabilization roadmap

Meaning:

- Open a bounded post-v1.0.0 stabilization roadmap.
- Focus on repository clarity, navigation, public entrypoints, and small cleanup.

Possible scope:

- README and README.ja wording checks;
- status index readability;
- document-map readability;
- release/status navigation;
- claim-boundary wording consistency;
- issue/milestone hygiene.

Benefits:

- Keeps work conservative.
- Reduces confusion for new readers.
- Does not require baseline changes.
- Supports public communication.

Risks:

- Could become repetitive if not bounded.
- May delay substantive next-version planning.
- Needs strict non-goals to avoid becoming v1.1.0 by another name.

Initial assessment:

- Good option if maintainers want more polish before external announcement.

## Option C: Open v1.1.0 planning

Meaning:

- Start a new versioned roadmap for targeted improvements after v1.0.0.

Possible scope:

- selected baseline-update candidates;
- refined guidance;
- examples and fixtures;
- validators;
- implementation/adoption support;
- clearer assessment/testing guidance;
- selected public communication artifacts.

Benefits:

- Gives a clear next version.
- Maintains momentum.
- Allows selected work to move beyond review.

Risks:

- Too early if next scope is not clear.
- Could dilute the meaning of v1.0.0 immediately after release.
- Could accidentally imply active baseline changes before they are scoped.

Initial assessment:

- Should not be opened until maintainers identify a specific bounded scope.
- Not recommended as the immediate next step unless there is a clear candidate set.

## Option D: Active baseline update candidate review

Meaning:

- Open a track to review whether any planning or readiness-review outputs should be promoted into active baseline artifacts.

Possible scope:

- control catalog updates;
- control ID changes or stability confirmation;
- evidence schema updates;
- assessment artifacts;
- testing procedures;
- validator expectations;
- example/fixture alignment;
- README and release-status implications.

Benefits:

- Provides a controlled path toward a future baseline update.
- Separates baseline work from communication and navigation cleanup.
- Keeps high-impact changes explicit.

Risks:

- High review burden.
- High consistency risk.
- Could create expectation that a new baseline is imminent.
- Requires careful claim boundaries.

Initial assessment:

- Valuable later, but not the safest immediate next step after v1.0.0.
- Should be opened only if maintainers are ready for baseline-impacting work.

## Option E: Public communication and announcement planning

Meaning:

- Prepare public communication materials after README entrypoint risk has been reduced.

Possible scope:

- release announcement;
- Zenn / Qiita article;
- LinkedIn post;
- maintainer note;
- public FAQ;
- safe wording review;
- announcement boundary checklist.

Benefits:

- Uses v1.0.0 release momentum.
- Helps explain AAEF to new readers.
- Can reinforce "Model output is not authority."
- Can explain why v1.0.0 does not equal certification or production readiness.

Risks:

- External wording can overclaim if not reviewed.
- Announcement may attract readers before navigation is fully polished.
- Public posts may be interpreted more loosely than repository docs.

Initial assessment:

- Good near-term candidate if external communication is a priority.
- Should use conservative wording and link to README/release notes.

## Option F: Implementation/adoption guidance roadmap

Meaning:

- Focus on helping readers understand how AAEF may be used without claiming implementation conformance or production readiness.

Possible scope:

- implementer walkthroughs;
- role-specific guidance;
- operator review guidance;
- risk-owner decision support;
- adoption entrypoint cleanup;
- non-normative examples;
- implementation boundary notes.

Benefits:

- Moves AAEF toward practical usability.
- Supports organizations evaluating the framework.
- Can remain non-baseline if scoped carefully.

Risks:

- Readers may treat guidance as implementation readiness.
- Examples may be mistaken for normative requirements.
- Could overlap with baseline update work if not separated.

Initial assessment:

- Useful, but should remain separate from baseline updates and conformance claims.

## Option G: Examples, fixtures, and validator roadmap

Meaning:

- Focus on repository hygiene, examples, fixtures, and validators.

Possible scope:

- evidence example hygiene;
- prototype fixtures;
- validator coverage;
- fixture consistency;
- non-normative example boundaries;
- scenario review.

Benefits:

- Strengthens repository quality.
- Makes examples easier to review.
- Supports future implementation-facing work.

Risks:

- Validators may be mistaken for semantic correctness.
- Examples may be mistaken for active baseline artifacts.
- Can become implementation-heavy.

Initial assessment:

- Useful if the next priority is engineering hygiene.
- Should preserve non-normative and non-conformance boundaries.

## Option H: Research positioning roadmap

Meaning:

- Focus on AAEF as a research contribution.

Possible scope:

- research framing;
- related-work boundary;
- paper outline;
- contribution statement;
- empirical validation future work;
- peer-review claim boundary;
- terminology stabilization.

Benefits:

- Helps academic or standards-facing work.
- Clarifies what AAEF contributes beyond existing security/compliance ideas.
- Supports future papers or talks.

Risks:

- Research framing may imply peer-reviewed acceptance if not careful.
- Could distract from repository stabilization.
- May require more literature review before publication.

Initial assessment:

- Valuable if the next goal is academic positioning.
- Should remain careful about empirical validation and peer-review boundaries.

## Option I: AAEF-AI-VA or implementation-specific spin-off alignment

Meaning:

- Keep parent AAEF stable while implementation-specific work proceeds separately in AAEF-AI-VA or another repository.

Possible scope:

- mapping AAEF principles into AAEF-AI-VA;
- implementation-specific evidence reconstruction;
- gated tool action request flows;
- local lab/demo safety;
- non-public patent-sensitive work kept out of public AAEF materials.

Benefits:

- Preserves parent AAEF as a framework/specification repository.
- Lets implementation learning happen without destabilizing the baseline.
- Avoids mixing public framework claims with implementation-specific claims.

Risks:

- Public AAEF and implementation-specific work may be confused.
- Patent-sensitive or non-public concepts must not leak into public AAEF materials.
- Implementation-specific results may be overgeneralized.

Initial assessment:

- Important, but should remain separate from immediate AAEF repository roadmap unless explicitly scoped.

## Recommended near-term path

Recommended near-term path:

1. Complete #388 with a close-readiness checklist.
2. Close milestone #15 if #388 is complete.
3. Do not immediately open v1.1.0 unless a bounded scope is chosen.
4. If external communication is next, open a small public communication / announcement planning track.
5. If repository polish is next, open a small post-v1.0.0 stabilization track.
6. If baseline changes are next, open an explicit active baseline update candidate review track.

## Recommended decision posture

The safest immediate decision is:

> Do not open a major v1.1.0 roadmap yet.
>
> Complete post-v1.0.0 review first.
>
> Then choose either a small stabilization roadmap, a public communication track, or a deliberately scoped baseline-update candidate review.

## Decision matrix

| Option | Good when | Avoid when |
| --- | --- | --- |
| Close #388 after checklist | maintainers want a clean pause | immediate public/roadmap work is already decided |
| post-v1.0.0 stabilization | repository clarity is the priority | scope would become version planning |
| v1.1.0 planning | a bounded improvement set is clear | scope is still vague |
| baseline update candidate review | maintainers are ready for baseline-impacting work | only communication/navigation cleanup is needed |
| public communication planning | external announcement is near-term | README/public-entrypoint risk is unresolved |
| implementation/adoption guidance | practical usability is the priority | claims may imply readiness/conformance |
| examples/fixtures/validators | repository engineering hygiene is priority | validators/examples may be overread |
| research positioning | academic/standards-facing work is priority | research claim boundaries are not ready |
| AAEF-AI-VA alignment | implementation-specific learning is priority | patent-sensitive content might leak into public docs |

## Non-goals

This roadmap-options note does not:

- open a new roadmap;
- publish a new release;
- change the active baseline;
- update the control catalog;
- update control IDs;
- update the evidence schema;
- update assessment artifacts;
- update testing procedures;
- add executable validators;
- add executable prototypes;
- add scenario fixtures;
- add JSON examples;
- update README release posture;
- update citation status;
- approve public announcement text;
- claim implementation readiness;
- claim adoption readiness;
- claim operational readiness;
- claim production readiness;
- claim implementation conformance;
- claim certification, compliance, or conformity;
- claim audit or legal sufficiency;
- claim automated risk acceptance;
- claim control conformance;
- claim external-framework equivalence.

## Close-readiness contribution

This artifact supports #388 by identifying next-roadmap options and recommending that maintainers avoid opening a major v1.1.0 roadmap until the next scope is clear.

After this artifact, #388 can proceed to a close-readiness checklist unless maintainers identify another immediate review gap.
