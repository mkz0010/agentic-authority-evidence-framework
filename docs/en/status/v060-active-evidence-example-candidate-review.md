# AAEF v0.6.x Active Evidence Example Candidate Review

Status: Active example candidate review  
Related issue: #280  
Related roadmap: #241  
Related split plan: `docs/en/status/v060-adoption-follow-up-split-planning.md`  
Related permitted-action example: `docs/en/status/v060-permitted-action-evidence-example-planning.md`  
Related non-execution example: `docs/en/status/v060-non-execution-evidence-example-planning.md`  
Related implementation reference: `docs/en/status/v060-implementation-reference-pattern-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document reviews whether the v0.6.0 permitted-action and non-execution evidence planning examples are candidates for later promotion into active examples, fixtures, or schema-adjacent examples.

The purpose is not to promote the examples immediately.

The purpose is to separate:

- planning-only illustrative material,
- reusable active example candidates,
- schema-alignment questions,
- validation implications,
- fixture naming considerations,
- and claim-boundary requirements.

This document is review and planning material. It does not change active controls, schemas, examples, mappings, testing procedures, assessment artifacts, or the current control and assessment baseline.

## Review scope

This review covers:

- `v060-permitted-action-evidence-example-planning.md`
- `v060-non-execution-evidence-example-planning.md`
- the supporting implementation reference pattern in `v060-implementation-reference-pattern-planning.md`
- whether selected structures should later become active examples or fixtures

This review does not cover:

- production implementation code,
- SDK-specific examples,
- external framework mapping,
- active control updates,
- active evidence schema updates,
- or assessment procedure updates.

## Source example summary

| Source artifact | Scenario | Current status |
| --- | --- | --- |
| `v060-permitted-action-evidence-example-planning.md` | Permitted high-impact service API key rotation | Non-normative planning example |
| `v060-non-execution-evidence-example-planning.md` | Denied key rotation due to scope mismatch | Non-normative planning example |
| `v060-implementation-reference-pattern-planning.md` | Minimal action request / authorization / dispatch / backend / evidence flow | Non-normative planning pattern |

## Candidate promotion question

The central question is:

> Should the paired permitted-action and non-execution planning examples become active AAEF examples or fixtures in a later PR?

This review answers:

> They are strong candidates for later active example promotion, but should not be promoted until schema alignment, fixture scope, validation behavior, and claim boundaries are explicitly reviewed.

## Review criteria

Candidate examples should be reviewed against the following criteria.

| Criterion | Question |
| --- | --- |
| Schema alignment | Are fields aligned with the active evidence schema or clearly outside it? |
| Stability | Are fields stable enough to be reused? |
| Minimality | Is the example small enough to be maintainable? |
| Pairing value | Do permitted and non-execution examples work as a useful pair? |
| Validation potential | Can the examples be machine-validated? |
| Evidence value | Do examples support reconstruction and reviewer understanding? |
| Claim boundary | Can examples remain non-conformance and non-certification artifacts? |
| Placement | Should examples live in status, docs, examples, or schema fixtures? |
| Maintenance | Who updates examples when schemas or controls change? |

## Permitted-action example review

### Strengths

The permitted-action example is valuable because it shows:

- a structured action request,
- explicit principal binding,
- trusted and untrusted input distinction,
- authorization decision artifact,
- policy version and expiry,
- dispatcher enforcement checks,
- backend relying-party verification,
- evidence event linkage,
- reconstruction questions,
- and evidence trust limitations.

### Candidate active-example value

The example is a strong candidate for later active example promotion because it demonstrates the full permitted-action path:

1. request,
2. authorization,
3. dispatch,
4. backend verification,
5. execution,
6. evidence,
7. reconstruction.

### Open questions

Before promotion, the following questions should be resolved:

- Which fields correspond to the active evidence schema?
- Which fields are illustrative implementation fields?
- Should action request and authorization decision examples be separate fixtures?
- Should backend verification be represented in the active evidence example?
- Should evidence trust limitations be mandatory in examples?
- Should the scenario remain API key rotation or be replaced with a more generic action?
- Should example IDs and timestamps follow a stable fixture convention?

### Initial disposition

Initial disposition:

> Promote later, after schema-alignment review and fixture placement decision.

## Non-execution example review

### Strengths

The non-execution example is valuable because it shows:

- attempted action outside authorized scope,
- available authorization decision,
- dispatcher denial,
- backend non-invocation,
- non-execution evidence,
- failed boundary identification,
- expected vs requested resource comparison,
- reconstruction questions,
- and common non-execution reasons.

### Candidate active-example value

The example is a strong candidate for later active example promotion because non-execution is central to AAEF's fail-closed posture.

It helps reviewers understand that evidence should cover not only successful actions but also:

- denied dispatch,
- scope mismatch,
- missing authorization,
- expired decisions,
- approval gaps,
- backend rejection,
- evidence-required-unavailable outcomes,
- freeze/hold events.

### Open questions

Before promotion, the following questions should be resolved:

- Should non-execution examples become required active examples?
- Should `backend_verification_id: null` be represented differently?
- Should backend non-invocation have its own event shape?
- Should denial reasons use a controlled vocabulary?
- Should non-execution reasons align with active controls or threat taxonomy?
- Should fail-closed behavior be represented in assessment artifacts?
- Should common non-execution reasons become a maintained reference list?

### Initial disposition

Initial disposition:

> Promote later as a paired active example candidate, after controlled vocabulary and schema-alignment review.

## Pairing review

The permitted-action and non-execution examples are more valuable as a pair than as isolated examples.

Together, they show:

| Dimension | Permitted example | Non-execution example |
| --- | --- | --- |
| Outcome | Executed | Not executed |
| Boundary behavior | Allowed after checks | Denied after mismatch |
| Backend role | Verifies and executes | Not invoked due to dispatch denial |
| Evidence role | Execution reconstruction | Fail-closed reconstruction |
| Reviewer value | Shows expected success path | Shows enforcement path |
| Operator value | Shows normal review | Shows exception/denial review |
| Auditor value | Shows evidence package | Shows denied-action evidence |

Initial paired disposition:

> Keep examples paired in future promotion work.

## Active example placement options

Potential placement options:

| Option | Description | Pros | Cons |
| --- | --- | --- | --- |
| Keep in `docs/en/status/` | Leave as planning material only | Low risk | Not reusable as active examples |
| Move to `docs/en/examples/` | Create documentation examples | Easier to find | Requires new index conventions |
| Add under `examples/` | Treat as active example fixtures | More reusable | Requires validation/maintenance decisions |
| Add under schema-adjacent path | Place near evidence schema | Good schema linkage | May imply schema stability |
| Split into JSON fixtures and explanatory docs | Use machine-readable examples plus narrative | Strongest for implementers/auditors | More maintenance |

Initial recommendation:

> Use a later PR to decide whether to create an `examples/` or `docs/en/examples/` convention before promotion.

## Active example candidate fields

The following field groups appear useful as candidate active example content.

| Field group | Candidate status | Notes |
| --- | --- | --- |
| Action request identifiers | Candidate | Useful for correlation. |
| Principal identifiers | Candidate | Central to authority reconstruction. |
| Agent instance/session identifiers | Candidate | Useful for incident reconstruction. |
| Input source trust flags | Candidate | Important for untrusted-input separation. |
| Authorization decision identifiers | Candidate | Central to AAEF model. |
| Policy version | Candidate | Useful for review and drift analysis. |
| Decision expiry | Candidate | Important for replay and stale authority. |
| Dispatcher check results | Candidate | Useful for enforcement evidence. |
| Backend verification result | Candidate | Important for relying-party verification. |
| Evidence trust limitations | Candidate | Important for claim boundaries. |
| Non-execution reason | Candidate | Important for fail-closed review. |
| Backend non-invocation flag | Candidate | Important for denied dispatch cases. |

## Schema-alignment questions

Before active promotion, review:

- whether active schema already supports the proposed fields,
- whether example-only fields should remain outside schema,
- whether examples imply schema changes,
- whether schema validation should apply to examples,
- whether both permitted and non-execution outcomes are represented,
- whether evidence limitations are structurally represented,
- and whether backend verification linkage is schema-supported.

This review does not decide schema changes.

## Validation implications

If promoted, examples may need one or more validators:

| Validation | Purpose |
| --- | --- |
| JSON syntax validation | Ensure example files parse. |
| Evidence schema validation | Ensure active example records conform. |
| Cross-reference validation | Ensure request/decision/dispatch/backend/evidence IDs align. |
| Controlled vocabulary validation | Ensure outcome and denial reasons are stable. |
| Markdown index validation | Ensure examples are discoverable. |

Initial recommendation:

> Do not promote examples as active fixtures until validation expectations are defined.

## Fixture naming considerations

Candidate naming convention:

- `examples/permitted-action-evidence.example.json`
- `examples/non-execution-evidence.example.json`
- `examples/action-request.example.json`
- `examples/authorization-decision.example.json`
- `examples/dispatch-enforcement.example.json`
- `examples/backend-verification.example.json`

Alternative:

- keep one bundled example per scenario,
- split by event type,
- or provide both narrative and machine-readable versions.

Initial recommendation:

> Define example placement and naming before moving content out of status planning documents.

## Claim-boundary requirements for active examples

If promoted later, examples must clearly state that they do not imply:

- certification,
- compliance,
- audit sufficiency,
- implementation conformance,
- production readiness,
- conformity,
- external framework equivalence,
- or complete mitigation.

Examples may support:

- implementation understanding,
- evidence design,
- reconstruction discussion,
- auditor preparation,
- consultant discovery,
- and public review.

## Risks of premature promotion

Premature promotion could create risks:

| Risk | Why it matters |
| --- | --- |
| Schema drift | Examples may diverge from active schema. |
| Implied conformance | Readers may treat examples as required implementation. |
| Over-specific scenario | API key rotation may look like the only supported pattern. |
| Missing validation | Active examples without validators may decay. |
| Claim confusion | Examples may be misread as certification or audit sufficiency. |
| Maintenance burden | Active examples require update discipline. |

## Initial review conclusion

The permitted-action and non-execution evidence planning examples are strong candidates for active example promotion, but promotion should be deferred until a follow-up PR resolves:

1. active example placement,
2. schema alignment,
3. validation expectations,
4. fixture naming,
5. controlled vocabulary treatment,
6. claim-boundary wording,
7. and maintenance expectations.

## Recommended next follow-up

Recommended next follow-up after this review:

> Define active example placement and validation expectations.

Candidate future artifact:

`docs/en/status/v060-active-example-placement-and-validation-planning.md`

Alternative:

If the project wants to move faster, the next PR may create active examples directly under a chosen examples path, but that PR should include validation or explicitly explain why validation is deferred.

## Relationship to #280

This document partially addresses #280 by documenting the candidate review and initial disposition.

#280 should remain open until one of the following is completed:

- promotion criteria and placement are accepted,
- active examples are created,
- or promotion is explicitly deferred.

## Non-goals

This document does not:

- promote planning examples into active examples,
- create active fixtures,
- update the active evidence schema,
- update active assessment artifacts,
- update testing procedures,
- change active controls,
- change the current control and assessment baseline,
- assert implementation conformance,
- assert audit sufficiency,
- claim compliance,
- claim certification,
- claim conformity,
- claim equivalence with external frameworks,
- or assert production readiness.

## Acceptance criteria

This review is sufficient when:

- permitted and non-execution planning examples are reviewed,
- candidate promotion value is described,
- open schema-alignment questions are identified,
- placement options are documented,
- validation implications are identified,
- claim-boundary requirements are preserved,
- initial disposition is documented,
- and no active baseline change is implied.
