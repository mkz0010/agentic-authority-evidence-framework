# AAEF v0.6.x Active Example Placement and Validation Planning

Status: Active example placement and validation planning  
Related issue: #280  
Related roadmap: #241  
Related candidate review: `docs/en/status/v060-active-evidence-example-candidate-review.md`  
Related permitted-action example: `docs/en/status/v060-permitted-action-evidence-example-planning.md`  
Related non-execution example: `docs/en/status/v060-non-execution-evidence-example-planning.md`  
Related release: AAEF v0.6.0 Practical Adoption Readiness Planning Release  
Current baseline note: AAEF v0.4.1 remains the current control and assessment baseline unless a later release explicitly updates the control catalog, evidence schema, assessment artifacts, or testing procedures.

## Purpose

This document plans where active evidence examples should live, how they should be named, and what validation expectations should apply before any v0.6.x planning examples are promoted into active examples or fixtures.

This document follows the active evidence example candidate review.

The purpose is to clarify:

- active example placement,
- example file naming,
- example grouping,
- validation expectations,
- schema-alignment expectations,
- controlled vocabulary expectations,
- index and discoverability expectations,
- maintenance expectations,
- and claim-boundary requirements.

This document is planning material. It does not create active examples, active fixtures, schema changes, control changes, assessment changes, or testing procedure changes.

## Decision posture

The current posture is:

> The permitted-action and non-execution evidence planning examples are strong candidates for later active example promotion, but promotion should wait until placement, naming, validation, schema alignment, controlled vocabulary treatment, claim boundaries, and maintenance expectations are clear.

This document defines those expectations at the planning level.

## Source artifacts

| Source artifact | Role |
| --- | --- |
| `v060-active-evidence-example-candidate-review.md` | Candidate review and initial disposition |
| `v060-permitted-action-evidence-example-planning.md` | Permitted-action evidence planning example |
| `v060-non-execution-evidence-example-planning.md` | Non-execution evidence planning example |
| `v060-implementation-reference-pattern-planning.md` | Reference implementation flow |
| `v060-auditor-evidence-request-checklist-planning.md` | Reviewer evidence request expectations |
| `v060-operator-runbook-planning.md` | Operational review expectations |

## Non-normative status

This document does not promote any planning example into an active example.

This document does not update:

- active controls,
- active evidence schema,
- active examples,
- active assessment artifacts,
- active testing procedures,
- mappings,
- CSVs,
- or the current control and assessment baseline.

Any future active example promotion must be handled through a separate PR.

## Placement decision requirements

Before active examples are created, the project should decide:

1. whether active examples live under `examples/`,
2. whether explanatory documentation lives under `docs/en/examples/`,
3. whether examples should be JSON-only, Markdown-only, or paired,
4. whether examples should be schema-validated,
5. whether examples should be cross-reference validated,
6. whether examples should be indexed in `docs/en/document-map.md`,
7. whether a new examples README is required,
8. and whether examples are stable enough to maintain as active artifacts.

## Placement options

| Option | Description | Pros | Cons | Initial disposition |
| --- | --- | --- | --- | --- |
| Keep in `docs/en/status/` | Leave examples as planning material only | Safest; no active implications | Low reuse value | Good fallback |
| Add `docs/en/examples/` | Create narrative documentation examples | Easy to read; docs-native | May not be machine-validated | Candidate |
| Add root `examples/` | Create active machine-readable examples | Clear fixture location; reusable | Requires validation and maintenance | Preferred candidate |
| Add schema-adjacent examples | Place near evidence schema | Strong schema linkage | May imply schema stability | Defer |
| Split narrative and JSON fixtures | Use Markdown explanation plus JSON fixtures | Best for implementers and auditors | More structure to maintain | Preferred long-term |

## Initial placement recommendation

Initial recommendation:

1. Use `examples/evidence/` for future machine-readable evidence examples.
2. Add `examples/README.md` if active examples are introduced.
3. Keep explanatory planning context in `docs/en/status/` until examples are promoted.
4. Do not place active examples directly beside the schema until schema-alignment expectations are confirmed.
5. Do not create active examples without at least JSON syntax validation and index/discoverability validation.

Candidate future paths:

- `examples/evidence/permitted-action-evidence.example.json`
- `examples/evidence/non-execution-evidence.example.json`
- `examples/evidence/README.md`

Optional later paths:

- `docs/en/examples/evidence-examples.md`
- `docs/en/examples/README.md`

## Candidate active example set

The first active example set should be intentionally small.

Recommended initial set:

| Example | Purpose | Candidate file |
| --- | --- | --- |
| Permitted action evidence | Show successful execution with authorization, dispatch, backend verification, and evidence linkage | `examples/evidence/permitted-action-evidence.example.json` |
| Non-execution evidence | Show fail-closed denial with dispatch rejection and backend non-invocation | `examples/evidence/non-execution-evidence.example.json` |

Defer for later:

| Example | Reason to defer |
| --- | --- |
| Standalone action request fixture | May require a separate action request schema or profile decision. |
| Standalone authorization decision fixture | Should align with authorization decision artifact profile first. |
| Standalone dispatch fixture | Needs controlled vocabulary for checks. |
| Standalone backend verification fixture | Needs clearer backend verification field expectations. |
| Full bundled scenario fixture | Useful, but should follow after simple examples are stable. |

## Naming expectations

Future active example names should be:

- lowercase,
- hyphen-separated,
- descriptive,
- stable,
- and explicit that the file is an example.

Recommended suffix:

- `.example.json`

Recommended names:

- `permitted-action-evidence.example.json`
- `non-execution-evidence.example.json`

Avoid names such as:

- `final-example.json`
- `compliant-example.json`
- `certified-example.json`
- `audit-ready-example.json`
- `production-example.json`

Reason:

Those names could imply conformance, audit sufficiency, certification, or production readiness.

## Example metadata expectations

Each active example should include or be accompanied by metadata describing:

| Metadata | Purpose |
| --- | --- |
| Example name | Human-readable example name |
| Example status | Active example, draft example, or planning example |
| Scenario | Scenario summary |
| Outcome | Executed or not executed |
| Related schema | Schema or profile used for validation |
| Related controls | Informative control references, if applicable |
| Claim boundary | What the example does not prove |
| Maintenance owner | Who updates it when schema or guidance changes |
| Validation command | How the example is validated |

If metadata is not included inside JSON, it should be included in `examples/evidence/README.md`.

## Validation expectations

At minimum, active JSON examples should pass:

1. JSON syntax validation.
2. Repository index/discoverability validation.
3. Link/path validation if referenced from Markdown.

Recommended but potentially later:

1. Active evidence schema validation.
2. Cross-reference validation across request, decision, dispatch, backend, and evidence identifiers.
3. Controlled vocabulary validation.
4. Required claim-boundary metadata validation.
5. Example freshness or version-reference validation.

## Validation phases

### Phase 1: Syntax and index validation

Purpose:

Ensure examples parse and are discoverable.

Candidate checks:

- every `*.example.json` parses as JSON,
- examples are listed in `examples/README.md`,
- examples are referenced from `docs/en/document-map.md` or an examples index,
- Markdown links are valid where applicable.

### Phase 2: Schema validation

Purpose:

Ensure examples conform to active schema or explicitly documented profile.

Candidate checks:

- permitted-action evidence example validates against active evidence schema,
- non-execution evidence example validates against active evidence schema,
- validation errors are actionable,
- schema limitations are documented.

### Phase 3: Cross-reference validation

Purpose:

Ensure example identifiers form a coherent evidence chain.

Candidate checks:

- `action_request_id` aligns across example objects,
- `authorization_decision_id` aligns across example objects,
- `dispatch_event_id` aligns with evidence event,
- `backend_verification_id` is present or explicitly null where appropriate,
- outcome and non-execution reason are coherent.

### Phase 4: Controlled vocabulary validation

Purpose:

Ensure example terms do not drift.

Candidate fields:

- `event_type`,
- `outcome`,
- `non_execution_reason`,
- `failed_boundary`,
- `dispatch_decision`,
- check result values,
- evidence source types.

## Schema-alignment expectations

Before promotion, the project should decide whether each field is:

| Category | Meaning |
| --- | --- |
| Active schema field | Already supported by active evidence schema. |
| Profile field | Supported by a planning profile but not active schema. |
| Example-only field | Useful for illustration but not active schema. |
| Candidate schema field | May justify future schema update. |
| Out-of-scope field | Should not appear in active examples. |

The active example PR should not silently introduce schema changes.

If examples contain fields not present in the active schema, the PR should explicitly say whether those fields are:

- illustrative,
- profile-bound,
- intentionally extra,
- or deferred schema candidates.

## Controlled vocabulary expectations

The non-execution example suggests values such as:

- `resource_scope_mismatch`,
- `missing_authorization_decision`,
- `decision_expired`,
- `approval_required`,
- `backend_verification_failed`,
- `evidence_required_unavailable`,
- `risk_freeze_active`.

Before promotion, the project should decide whether those values are:

- examples only,
- recommended vocabulary,
- active controlled vocabulary,
- or deferred for later vocabulary review.

Initial recommendation:

> Treat non-execution reason values as example vocabulary until a controlled vocabulary PR explicitly adopts them.

## Claim-boundary expectations

Every active example should state that it does not imply:

- certification,
- compliance,
- audit sufficiency,
- implementation conformance,
- production readiness,
- conformity,
- external framework equivalence,
- complete mitigation,
- or legal/regulatory adequacy.

Examples may support:

- implementation understanding,
- evidence design,
- reconstruction discussion,
- auditor preparation,
- consultant discovery,
- operator readiness,
- and public review.

## Example README expectations

If `examples/evidence/` is created, add:

- `examples/README.md`, or
- `examples/evidence/README.md`.

The README should explain:

- examples are illustrative,
- examples are not certification artifacts,
- examples are not audit opinions,
- examples may not cover all controls,
- examples may not prove production readiness,
- how to validate examples,
- and which examples are currently provided.

## Maintenance expectations

Active examples should be reviewed when any of the following changes:

- active evidence schema,
- authorization decision artifact profile,
- assessment procedure,
- testing procedure,
- controlled vocabulary,
- document map validation,
- release baseline,
- or claim-boundary language.

A future PR should decide whether examples require a formal maintenance checklist.

## Promotion readiness checklist

Before promoting examples, confirm:

- placement path is selected,
- naming convention is selected,
- JSON examples parse,
- examples are discoverable,
- validation expectations are documented,
- schema-alignment status is documented,
- controlled vocabulary status is documented,
- claim-boundary wording is included,
- examples are not named as compliant/certified/audit-ready,
- and no active baseline change is implied unless explicitly intended.

## Recommended next implementation PR

The next PR may either:

1. create `examples/evidence/` with README and two JSON examples, or
2. create a more detailed schema-alignment review before example creation.

Recommended next step:

> Create `examples/evidence/` with README and two JSON example candidates, while validating JSON syntax and documenting that schema validation is either applied or explicitly deferred.

## Relationship to #280

This document further addresses #280 by defining placement and validation expectations.

#280 should remain open until one of the following occurs:

- active examples are created,
- promotion is explicitly deferred,
- or a follow-up issue is created for active example implementation.

## Non-goals

This document does not:

- create active examples,
- create active fixtures,
- update active evidence schema,
- update active assessment artifacts,
- update testing procedures,
- change active controls,
- change the current control and assessment baseline,
- create controlled vocabulary,
- assert implementation conformance,
- assert audit sufficiency,
- claim compliance,
- claim certification,
- claim conformity,
- claim equivalence with external frameworks,
- or assert production readiness.

## Acceptance criteria

This planning document is sufficient when:

- active example placement options are documented,
- initial placement recommendation is recorded,
- naming expectations are defined,
- validation phases are described,
- schema-alignment expectations are documented,
- controlled vocabulary expectations are documented,
- claim-boundary expectations are preserved,
- maintenance expectations are identified,
- and no active baseline change is implied.
