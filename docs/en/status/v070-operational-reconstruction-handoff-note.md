# v0.7.0 Operational Reconstruction Handoff Note

## Purpose

This document defines a planning-level handoff note for the v0.7.0 Operational Reconstruction track.

It builds on:

- `docs/en/status/v070-operational-reconstruction-planning.md`
- `docs/en/status/v070-operational-reconstruction-question-set.md`
- `docs/en/status/v070-evidence-gap-classification-note.md`

The goal is to clarify how reviewers, operators, risk owners, maintainers, implementers, and approvers should hand off reconstruction results, evidence gaps, unresolved uncertainty, and follow-up decisions.

This document is planning and review material only. It does not define a complete incident-response procedure, forensic procedure, audit procedure, legal procedure, operational readiness process, production conformance process, or organizational responsibility model.

## Relationship to operational reconstruction

Operational reconstruction may not end with complete certainty.

A reviewer may determine that a conclusion is supported, partially supported, unsupported, conflicting, out of scope, or requires escalation. The next step is often a handoff to a role that can collect evidence, pause or continue operations, accept residual risk, approve follow-up, or open additional work.

This handoff note helps distinguish:

- what the reviewer can conclude,
- what the operator can do,
- what the risk owner must decide,
- what the maintainer or implementer must clarify,
- what the approver must confirm,
- what remains unsupported, and
- what should be split into future work.

## Handoff posture

Handoff should preserve uncertainty rather than hide it.

A handoff should not convert an evidence gap into a supported conclusion.

A handoff should not imply audit sufficiency, legal sufficiency, operational readiness, incident-response certification, implementation conformance, production readiness, compliance, conformity, or complete root-cause analysis.

A handoff should make clear:

- the scoped action or non-action,
- the current reconstruction conclusion,
- the evidence supporting the conclusion,
- the evidence gaps limiting the conclusion,
- the residual uncertainty,
- the recommended owner,
- the requested decision or action, and
- the claims that should not be made.

## Handoff participants

Operational reconstruction handoff may involve multiple roles.

| Role | Typical responsibility in handoff |
| --- | --- |
| Reviewer | Classifies reconstruction support, evidence gaps, unsupported conclusions, and needed escalation. |
| Operator | Determines immediate operational action such as pause, freeze, retry, rollback, monitoring, or evidence collection. |
| Risk owner | Accepts, rejects, escalates, or requests further review of residual uncertainty and business or safety impact. |
| Maintainer | Clarifies artifact scope, documentation, index, validator boundary, or future issue placement. |
| Implementer | Clarifies component behavior, evidence generation, policy behavior, dispatch behavior, or backend assumptions. |
| Approver | Confirms approval, denial, hold, or escalation state where human approval is relevant. |
| Evidence owner | Provides, explains, or improves evidence sources and correlation. |
| Backend owner | Confirms backend acceptance, rejection, execution, partial execution, failure, or side effects. |

These role descriptions are planning aids only. They do not define a complete responsibility model.

## Handoff triggers

A handoff may be needed when:

- a conclusion is only partially supported,
- a conclusion is unsupported,
- evidence conflicts,
- model output or runtime self-report is the only evidence,
- request evidence is missing,
- principal or authority evidence is missing,
- authorization decision evidence is missing,
- enforcement evidence is missing,
- backend evidence is missing,
- execution or non-execution evidence is missing,
- approval evidence is missing,
- timeline evidence is inconsistent,
- reconstruction scope is ambiguous,
- evidence ownership is ambiguous,
- residual uncertainty affects a high-impact action,
- an operational pause, freeze, retry, or rollback may be needed,
- a risk owner must accept or reject residual uncertainty,
- legal, audit, compliance, or incident-response review may be separately needed, or
- follow-up work should be opened.

## Handoff packet

A minimal handoff packet should include:

1. **Reconstruction object**

   The action, non-action, attempted action, denied action, held action, escalated action, backend rejection, or evidence gap being reviewed.

2. **Reviewed boundary**

   The systems, components, time range, principals, evidence sources, and exclusions.

3. **Current conclusion**

   Supported, partially supported, unsupported, conflicting, out of scope, or requires escalation.

4. **Supporting evidence**

   Evidence that supports the current conclusion.

5. **Evidence gaps**

   Missing, conflicting, untrusted, uncorrelated, ambiguous, or unowned evidence.

6. **Conclusion impact**

   Whether the gap blocks the conclusion, narrows the conclusion, adds uncertainty, requires owner decision, requires more evidence, requires scope change, or requires escalation.

7. **Residual uncertainty**

   What remains unknown or unsupported.

8. **Requested owner**

   The role or component owner expected to act.

9. **Requested action**

   Evidence collection, operational action, risk decision, approval confirmation, documentation clarification, implementation review, or follow-up issue.

10. **Claims to avoid**

   Conclusions that should not be made from the current evidence.

## Reviewer handoff

### Reviewer to operator

A reviewer may hand off to an operator when operational action may be needed.

The handoff should answer:

- What action or non-action was reconstructed?
- What conclusion is currently supported?
- What conclusion is unsupported or only partially supported?
- What evidence gaps affect operational state?
- Is there possible execution, partial execution, retry, fallback, or side effect?
- Should the workflow be paused, frozen, retried, reversed, monitored, or escalated?
- What additional operational evidence should be collected?
- What should not be concluded yet?

The reviewer should not tell the operator that the system is safe, compliant, audit-ready, or fully reconstructed unless separately supported.

### Reviewer to risk owner

A reviewer may hand off to a risk owner when residual uncertainty may affect business, safety, governance, or high-impact action decisions.

The handoff should answer:

- What decision or action is under review?
- What impact may have occurred?
- What evidence supports the current conclusion?
- What uncertainty remains?
- Which uncertainty blocks a stronger conclusion?
- Which uncertainty can be accepted only by a risk owner?
- What decision is requested?
- What follow-up evidence, remediation, or escalation is recommended?

The reviewer should not accept business risk on behalf of the risk owner unless explicitly authorized.

### Reviewer to maintainer

A reviewer may hand off to a maintainer when artifact scope, wording, validator boundaries, or follow-up issue placement needs clarification.

The handoff should answer:

- Which artifact or index is affected?
- Which claim or boundary is unclear?
- Which future work item should be split out?
- Is the issue documentation-only, planning-only, validation-related, or implementation-facing?
- What wording should be narrowed?
- What scope reminder is missing?

The reviewer should not treat documentation cleanup as evidence that an operational gap has been resolved.

### Reviewer to implementer

A reviewer may hand off to an implementer when component behavior, evidence production, policy behavior, dispatch behavior, or backend behavior needs clarification.

The handoff should answer:

- Which component behavior is unclear?
- Which evidence should the component have produced?
- Which evidence is missing or incomplete?
- Which assumption is being challenged?
- Which decision, dispatch, backend, or evidence path needs review?
- Is a design note, implementation issue, or validator boundary clarification needed?

The reviewer should not infer implementation conformance from design intent.

## Operator handoff

### Operator to reviewer

An operator may hand evidence or operational state back to a reviewer.

The handoff should answer:

- What operational action was taken?
- Was the workflow paused, frozen, retried, reversed, monitored, or escalated?
- What additional evidence was collected?
- What backend or downstream state was observed?
- Were side effects found?
- Did the new evidence change the reconstruction conclusion?
- What uncertainty remains?

The operator should distinguish observed operational state from audit, legal, or compliance conclusions.

### Operator to risk owner

An operator may hand off to a risk owner when operational uncertainty requires a risk decision.

The handoff should answer:

- What is the operational state now?
- What is known about execution, non-execution, partial execution, or side effects?
- What remains uncertain?
- What options exist?
- What operational impact may result from pause, retry, rollback, or continuation?
- What decision is required from the risk owner?

The operator should not silently accept residual uncertainty without risk-owner involvement when the uncertainty affects high-impact or business-relevant action.

## Risk-owner handoff

### Risk owner to operator

A risk owner may hand a decision back to an operator.

The handoff should answer:

- Is the residual uncertainty accepted, rejected, or escalated?
- Should operations continue, pause, freeze, retry, rollback, or change monitoring?
- What risk treatment is selected?
- What evidence or follow-up is still required?
- What communication or approval is needed?

The risk owner decision should be scoped to the reviewed boundary and should not imply audit or legal sufficiency unless separately established.

### Risk owner to reviewer

A risk owner may hand back a request for further reconstruction.

The handoff should answer:

- What conclusion is not yet acceptable?
- What evidence is needed?
- What uncertainty cannot be accepted?
- What scope should be expanded or narrowed?
- What follow-up review is required?
- What decision is deferred?

The risk owner should not request impossible certainty. The request should identify the decision need and acceptable evidence target.

### Risk owner to maintainer or implementer

A risk owner may request follow-up work when a gap reveals unclear ownership, missing evidence production, unclear policy behavior, or insufficient documentation.

The handoff should answer:

- What risk decision was affected?
- Which gap affected the decision?
- Which artifact, component, or process should be improved?
- Should this become a follow-up issue, PR, design note, validator clarification, or implementation task?
- What claim should be avoided until the follow-up is complete?

## Approver handoff

Human approval, denial, hold, or escalation may require special handling.

An approver handoff should answer:

- Was approval required?
- Who was the approver?
- Was the approver authorized for the action?
- Was approval granted, denied, held, escalated, missing, stale, or ambiguous?
- Was approval recorded before dispatch?
- Can approval be correlated to the action request and authorization decision?
- What should happen if approval evidence is missing?

Approval should not be inferred from execution alone.

## Evidence-owner handoff

An evidence owner may need to provide or improve evidence.

The handoff should answer:

- Which evidence source is missing, incomplete, conflicting, untrusted, uncorrelated, or outside scope?
- Which stable identifier, timestamp, source, or correlation field is missing?
- Which evidence source is authoritative for the event?
- What evidence can be collected now?
- What evidence cannot be recovered?
- What evidence production improvement should be considered?

Evidence-owner handoff should distinguish immediate reconstruction from future evidence pipeline improvement.

## Backend-owner handoff

A backend owner may need to confirm acceptance, rejection, execution, partial execution, failure, or side effects.

The handoff should answer:

- Did the backend receive the action?
- Did the backend accept, reject, fail, or partially execute the action?
- Did the backend produce side effects?
- Was there a retry, fallback, alternate path, or downstream action?
- What backend evidence supports the conclusion?
- What backend evidence is missing?
- Which backend boundary is outside scope?

Backend rejection should not be treated as proof of no side effects unless the evidence and boundary support that narrow conclusion.

## Handoff result categories

A handoff may result in:

| Result | Meaning |
| --- | --- |
| Evidence collected | Additional evidence was produced or recovered. |
| Conclusion narrowed | The conclusion was revised to fit available evidence. |
| Risk accepted | A risk owner accepted residual uncertainty within a defined boundary. |
| Operations changed | An operator paused, froze, retried, rolled back, monitored, or escalated. |
| Follow-up opened | A separate issue, PR, design note, or review task was opened. |
| Scope changed | The reconstruction boundary was narrowed or expanded. |
| Escalated externally | Separate legal, audit, compliance, incident-response, or organizational review was invoked. |
| Remains unresolved | The gap remains unresolved and should be recorded as such. |

These result categories do not establish operational readiness or complete reconstruction.

## Handoff anti-patterns

Avoid these handoff patterns:

- treating a gap as if it were resolved,
- treating model explanation as action-bound evidence,
- treating runtime self-report as independent evidence,
- treating backend rejection as proof that nothing happened,
- treating non-dispatch as proof of absence of all side effects,
- treating validator success as implementation conformance,
- treating documentation completeness as operational readiness,
- treating risk-owner acceptance as legal or audit sufficiency,
- handing off without identifying an owner,
- handing off without identifying the requested decision,
- closing a reconstruction without recording residual uncertainty, and
- expanding the conclusion beyond the reviewed boundary.

## Minimal handoff prompt

For a lightweight handoff, use:

1. What action, non-action, or gap is being handed off?
2. What conclusion is currently supported?
3. What evidence supports it?
4. What evidence is missing, conflicting, untrusted, uncorrelated, ambiguous, or unowned?
5. What conclusion should not be made?
6. Who owns the next step?
7. What decision or action is requested?
8. What residual uncertainty remains?
9. Does this require evidence collection, operational action, risk decision, approval confirmation, implementation review, documentation follow-up, or external review?
10. What should be recorded before closing the handoff?

This prompt is a review aid only.

## Relationship to future #322 work

This handoff note may support narrower follow-up artifacts such as:

- action timeline reconstruction checklist,
- authority chain reconstruction checklist,
- decision chain reconstruction checklist,
- execution and non-execution reconstruction checklist,
- reconstruction walkthrough candidates,
- #322 close-readiness checklist, and
- future operational reviewer guidance.

These should remain planning or review artifacts unless a later issue explicitly scopes executable fixtures, examples, validators, or implementation work.

## Review questions

Reviewers should be able to answer:

- Does this handoff note preserve the thesis that model output is not authority?
- Does this handoff note preserve evidence gaps instead of hiding them?
- Does this handoff note distinguish reviewer, operator, risk owner, maintainer, implementer, approver, evidence owner, and backend owner roles?
- Does this handoff note identify the next owner and requested decision?
- Does this handoff note avoid audit sufficiency, legal sufficiency, operational readiness, incident-response certification, complete reconstruction, complete root-cause analysis, implementation conformance, production readiness, certification, compliance, conformity, and external-framework equivalence claims?
- Does this handoff note create useful follow-up paths for #322 closure?

## Scope reminder

This artifact is planning and review material only.

It does not update the active control and assessment baseline, control catalog, evidence schema, assessment artifacts, testing procedures, executable validators, executable prototypes, scenario fixtures, or JSON examples.

It does not establish operational readiness, complete reconstruction, complete root-cause analysis, incident-response certification, audit sufficiency, legal sufficiency, empirical validation, implementation conformance, production readiness, certification, compliance, conformity, or external-framework equivalence.
