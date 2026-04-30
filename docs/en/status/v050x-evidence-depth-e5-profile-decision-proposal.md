# v0.5.x Evidence Depth and E5 Profile Decision Proposal

**Status:** Temporary, non-normative decision proposal

## Purpose

This document proposes how AAEF should treat evidence depth terminology such as E5.

It follows:

- `docs/en/status/v050x-evidence-schema-and-examples-track-proposal.md`
- `docs/en/status/v050x-evidence-schema-field-proposal.md`
- `docs/en/status/v050x-evidence-example-design-proposal.md`
- `docs/en/status/v050x-evidence-schema-example-implementation-readiness.md`
- `docs/en/status/v050x-evidence-integrity-negative-tests-track-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-guidance-proposal.md`
- `docs/en/status/v050x-incident-response-evidence-preservation-candidate-appendix.md`
- `docs/en/status/v050x-follow-up-status.md`
- `docs/en/status/v050x-incorporation-decision-register.md`

Primary source issue:

- #165 — evidence integrity and tamper-evident evidence

Related active row:

- `AAEF-EVD-04`

This proposal does not update active testing procedures.

It does not update the Evidence Event Schema.

It does not add evidence examples.

It does not add validator fixtures.

It does not create a certification scale.

It does not close #165 by itself.

## Decision Context

Recent v0.5.x work introduced or expanded:

- optional evidence integrity fields;
- an integrity-focused evidence example;
- an approval-to-execution binding example;
- evidence integrity negative test candidates;
- incident-response evidence preservation guidance;
- incident-response preservation scenario candidates.

During that work, the term E5 appeared as a useful shorthand for stronger, dispute-grade, integrity-verifiable evidence.

However, AAEF should avoid accidentally turning E5 into:

- a certification tier;
- a universal maturity model;
- a required schema field;
- a required evidence label;
- a compliance score;
- a claim that one evidence mechanism is always sufficient.

## Proposed Decision

E5 should be treated as non-normative evidence depth terminology for review, examples, and future guidance.

It should not be treated as a required profile, certification level, or formal scoring scale in the current v0.5.x cycle.

Recommended decision:

| Area | Recommendation |
| --- | --- |
| Formal profile | Defer |
| Certification tier | Do not create |
| Required schema field | Do not add |
| Required active CSV value | Do not add |
| Example terminology | Allow with explicit non-normative framing |
| Assessment guidance | Candidate for later guidance |
| Reviewer vocabulary | Useful, but should remain explanatory |
| Public claim | Avoid claiming E5 compliance or E5 certification |

## Proposed Evidence Depth Vocabulary

The following vocabulary is proposed as explanatory, not normative.

| Level | Name | Description |
| --- | --- | --- |
| E0 | No usable evidence | No reliable evidence is available for the action or claim. |
| E1 | Narrative or self-reported evidence | Evidence is mainly model-generated, agent-reported, implementation self-reported, or manually asserted. |
| E2 | Local runtime evidence | Evidence exists in runtime traces, local logs, prompts, tool-call transcripts, or implementation logs, but lacks strong independent corroboration. |
| E3 | Action-bound system evidence | Evidence is bound to a specific action and includes authorization, dispatch, execution, non-execution, or approval records from relevant systems. |
| E4 | Corroborated and integrity-checked evidence | Evidence is generated or corroborated by trusted enforcement, backend, approval, or evidence systems and includes integrity or consistency checks. |
| E5 | Dispute-grade evidence | Evidence supports high-assurance incident reconstruction, includes action-bound linkage, independent corroboration, integrity verification, preservation context, and explicit trust limitations. |

These levels should be used carefully.

They describe evidence depth, not organizational maturity or system trustworthiness.

## E5 Candidate Characteristics

E5-style evidence may include:

- canonical action identifier;
- action digest or canonical action representation;
- authorization decision artifact;
- approval workflow record where applicable;
- dispatch record;
- execution or non-execution record;
- enforcement decision record;
- backend system-of-record evidence;
- integrity proof or verification result;
- failed or unavailable verification state when relevant;
- external anchor or independent corroboration where available;
- incident-response preservation context where relevant;
- evidence trust limitations;
- reviewer access, export, or handoff record for dispute-grade cases.

E5 should not require every implementation to use the same integrity mechanism.

Equivalent mechanisms may include:

- append-only or write-restricted evidence stores;
- signed records;
- hash chains;
- Merkle roots;
- immutable storage;
- external timestamping;
- independent corroborating logs;
- backend system-of-record reconciliation;
- preservation and chain-of-custody controls.

## What E5 Is Not

E5 is not:

- proof that the action was correct;
- proof that the action was authorized;
- proof that the model behaved safely;
- proof that business impact was acceptable;
- a substitute for authorization controls;
- a substitute for approval quality controls;
- a substitute for execution enforcement;
- a certification mark;
- a required schema value;
- a universal audit grade.

E5-style evidence can support review.

It does not replace the review.

## Relationship to `AAEF-EVD-04`

`AAEF-EVD-04` covers evidence integrity and tamper-evident evidence.

Evidence depth terminology may help explain what stronger evidence looks like, but `AAEF-EVD-04` should not require all evidence to be E5.

The active row can remain mechanism-neutral.

No active CSV change is recommended in this proposal.

## Relationship to Evidence Examples

The existing integrity-focused example may use E5-like framing as non-normative example terminology.

That usage should remain acceptable if it is clear that:

- the example is illustrative;
- E5 is not a required schema value;
- E5 is not a certification level;
- the example does not imply one required implementation mechanism.

No example change is required in this proposal.

## Relationship to Evidence Event Schema

No schema change is recommended.

Do not add fields such as:

- `evidence_depth_level`;
- `evidence_profile`;
- `e5_compliant`;
- `assurance_score`;
- `certification_level`.

If future guidance needs evidence depth metadata, it should be revisited separately and justified by concrete assessment or interoperability needs.

## Relationship to Assessment Guidance

Evidence depth vocabulary may later be useful in:

- assessment quick-start guidance;
- reviewer checklists;
- evidence sufficiency examples;
- incident-response preservation guidance;
- profile-specific evidence expectations.

However, the current proposal recommends deferring stable incorporation.

## Risks of Formalizing Too Early

Formalizing E5 too early could create risks:

| Risk | Explanation |
| --- | --- |
| False assurance | Teams may claim E5 evidence without meaningful integrity or reconstruction support. |
| Mechanism lock-in | AAEF may accidentally favor one technical implementation. |
| Certification confusion | Users may interpret E5 as a certification or maturity level. |
| Schema overreach | Evidence depth may be pushed into schema fields before the concept stabilizes. |
| Audit gaming | Teams may satisfy a label while omitting unfavorable evidence or trust limitations. |
| Scope creep | Evidence depth may expand beyond evidence integrity into full organizational scoring. |

## Recommended Near-Term Handling

For the current v0.5.x follow-up cycle:

1. Keep E5 as non-normative terminology.
2. Allow E5-style wording only in examples, proposals, or guidance with clear disclaimers.
3. Do not add active CSV requirements for E5.
4. Do not add schema fields for evidence depth.
5. Do not create an AAEF evidence-depth certification scale.
6. Revisit after more evidence examples, reviewer checklists, and assessment guidance exist.

## Candidate Future Work

Future work may include:

- evidence depth guidance appendix;
- reviewer-facing evidence depth examples;
- evidence sufficiency and limitation guidance for `AAEF-EVD-01`;
- mapping between evidence depth and assessment confidence;
- incident-response evidence package profiles;
- public-facing explanation of why evidence depth is not certification.

## Relationship to #165

This proposal advances #165 by resolving the immediate E5 / evidence depth decision for the current cycle.

It does not close #165.

Remaining #165 work may include:

- deciding whether negative evidence examples or validator fixtures would improve reviewability;
- deciding whether `AAEF-EVD-01` needs evidence sufficiency or limitation refinement;
- deciding whether evidence depth guidance should be created later;
- consolidating temporary planning documents after the current follow-up cycle.

## Non-Goals

This proposal does not:

- update active testing procedure CSV;
- add testing procedure rows;
- add candidate IDs to active CSV;
- update the Evidence Event Schema;
- add evidence examples;
- add validator fixtures;
- change control catalog CSV;
- change human-readable control requirements;
- change assessment worksheet;
- change assessment profiles;
- change external framework mapping CSV;
- create GitHub issues;
- create a certification scale;
- close #161, #163, #165, or #167.

It records the evidence depth / E5 decision proposal before any active incorporation decision.
