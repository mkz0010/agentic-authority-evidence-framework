# Threat-Control Assurance Mapping

## Status

This is an initial v0.2 public review draft.

It maps AAEF controls to threat areas, assurance types, primary assurance effects, residual risks, and implementation assumptions.

This mapping does not claim complete mitigation. It is intended to help implementers understand what each control is expected to improve and what may remain outside the control's guarantee.

## Threat Areas

AAEF currently organizes threats into the following areas:

| Threat ID | Threat Area |
|---|---|
| T1 | Identity and Authentication Threats |
| T2 | Principal Binding Threats |
| T3 | Delegation and Authority Threats |
| T4 | Prompt and Intent Manipulation Threats |
| T5 | Tool and Action Boundary Threats |
| T6 | Memory and Retrieval Threats |
| T7 | Multi-Agent and A2A Threats |
| T8 | Evidence and Auditability Threats |
| T9 | Revocation and Response Threats |

## Assurance Types

| Assurance Type | Meaning |
|---|---|
| Preventive | Blocks or reduces unsafe or unauthorized action before execution |
| Detective | Detects risky, ambiguous, abnormal, or policy-relevant conditions |
| Evidentiary | Produces evidence for review, audit, or reconstruction |
| Responsive | Enables revocation, isolation, escalation, containment, or recovery |
| Governance | Supports ownership, inventory, classification, and accountability |

## Mapping Table

| Control ID | Related Threats | Assurance Type | Primary Effect | Residual Risk | Implementation Assumptions |
|---|---|---|---|---|---|
| AAEF-GOV-01 | T1; T5; T8 | Governance | Makes agentic systems knowable and governable. | Shadow agents or unregistered workflows may remain. | Inventory process covers production, pilots, and tool-enabled workflows. |
| AAEF-GOV-02 | T3; T5; T8 | Governance | Defines which actions require stronger controls. | Taxonomy may omit emerging or organization-specific high-impact actions. | Risk taxonomy is reviewed and mapped to tools and workflows. |
| AAEF-GOV-03 | T8; T9 | Governance | Assigns accountability for agentic systems. | Ownership may be nominal without operational authority. | Owners have authority and responsibility to act. |
| AAEF-ID-01 | T1 | Preventive / Evidentiary | Identifies which agent acted. | Identity can still be stolen, replayed, or misissued. | Agent identity is verifiable and checked by enforcement points. |
| AAEF-ID-02 | T1 | Evidentiary | Distinguishes product identity from runtime instance identity. | Instance metadata may be incomplete or inconsistently propagated. | Logs and evidence preserve instance IDs across workflows. |
| AAEF-ID-03 | T1; T7 | Governance / Evidentiary | Identifies issuer and operator for trust decisions. | Issuer/operator metadata may be stale or unauthenticated. | Registry metadata is maintained and trusted. |
| AAEF-PRN-01 | T2 | Preventive / Evidentiary | Binds high-impact actions to a principal. | Principal may be incorrectly inferred or shared. | Principal binding is derived from trusted identity/session context. |
| AAEF-PRN-02 | T2; T3; T7 | Preventive / Evidentiary | Preserves principal context across tools, workflows, and delegations. | Context may degrade over long-running or asynchronous workflows. | Explicit propagation mechanisms are used and tested. |
| AAEF-DEL-01 | T3 | Preventive | Prevents delegated authority from exceeding delegator authority. | Delegator authority may itself be overbroad. | Authority comparison is enforced by trusted policy components. |
| AAEF-DEL-02 | T3 | Preventive | Constrains delegated authority by action, resource, purpose, time, count, or depth. | Constraints may be incomplete or too broad. | Delegation constraints are machine-readable where feasible. |
| AAEF-DEL-03 | T3; T8 | Evidentiary | Records delegation chains for high-impact actions. | Evidence may record chain existence but not semantic correctness. | Delegation evidence is linked to action evidence. |
| AAEF-DEL-04 | T3; T9 | Responsive | Invalidates downstream delegations after upstream revocation. | Propagation may be delayed or partial in distributed systems. | Downstream delegation dependencies are known and testable. |
| AAEF-DEL-05 | T3; T7; T8; T9 | Evidentiary / Responsive | Supports reconstruction of upstream and downstream authority lineage. | Lineage may be incomplete across domains or unsynchronized systems. | Correlation IDs, trace IDs, or equivalent references are preserved. |
| AAEF-AUZ-01 | T5 | Preventive | Requires authorization at the point of execution. | Decision can be bypassed if dispatch layer is outside trusted boundary. | Tool dispatch enforces decisions and cannot be bypassed by model output. |
| AAEF-AUZ-02 | T3; T4; T5 | Preventive | Checks requested purpose and target resource. | Purpose may be model-generated or semantically misleading. | Purpose/resource inputs are trusted or policy-bound where feasible. |
| AAEF-AUZ-03 | T5; T8 | Preventive / Governance | Applies approval or verification to high-risk actions. | Approval may become fatigued or rubber-stamped. | Approval UX and thresholds support meaningful review. |
| AAEF-AUZ-04 | T2; T3; T5 | Preventive | Fails safe when authority, principal, or purpose cannot be determined. | Ambiguity detection may be incomplete. | Missing authority or context is detected outside model self-assessment. |
| AAEF-AUZ-05 | T4; T5 | Preventive / Evidentiary | Separates authorization decisions from untrusted natural-language content. | Semantic influence may still remain. | Trusted policy inputs and system state exist and are used. |
| AAEF-AUZ-06 | T3; T4; T5 | Preventive / Detective | Checks intent-authority alignment using trusted context or policy references. | Natural-language intent may remain ambiguous. | Intent alignment does not rely solely on model self-assessment. |
| AAEF-AUZ-07 | T5; T9 | Preventive / Detective | Checks runtime state before high-impact execution. | State sources may be stale, unavailable, or incomplete. | Trusted state sources are defined and checked at execution time. |
| AAEF-AUZ-08 | T2; T3; T4; T5; T8 | Preventive / Detective | Denies, defers, or escalates under material ambiguity. | Semantic ambiguity may be hard to resolve deterministically. | Model self-assessment is not the sole basis for clearing ambiguity. |
| AAEF-AUZ-09 | T3; T5; T8 | Preventive / Evidentiary | Controls denial, deferral, reauthorization, and retry flows. | Reauthorization may still create scope creep if poorly governed. | Reauthorization is scoped, attributable, and linked to prior denial. |
| AAEF-TOOL-01 | T5 | Preventive | Limits tool blast radius through minimum authority. | Tools may still have excessive or hidden capabilities. | Tool permissions are reviewed against business need. |
| AAEF-TOOL-02 | T4; T5 | Preventive | Prevents model output alone from invoking tools. | Policy enforcement can be bypassed if not at dispatch boundary. | Tool dispatch is governed by explicit policy enforcement. |
| AAEF-TOOL-03 | T5; T8 | Governance / Preventive | Classifies high-risk tools for stronger controls. | Risk classification may lag new tool capabilities. | Tool registry is maintained and reviewed. |
| AAEF-TOOL-04 | T4; T5; T6 | Preventive / Detective | Subjects untrusted-content-derived tool requests to checks. | Intent validation may still depend on uncertain semantics. | Tool requests derived from untrusted content pass independent policy checks. |
| AAEF-MEM-01 | T6 | Preventive | Controls writes to persistent memory. | Memory write policy may miss indirect or derived data. | Persistent memory writes are mediated and logged. |
| AAEF-MEM-02 | T6; T8 | Detective / Evidentiary | Labels retrieval sources with trust or provenance metadata. | Provenance may be absent or unreliable for some sources. | Source registry and provenance metadata are maintained. |
| AAEF-MEM-03 | T4; T6 | Preventive | Prevents external content from becoming trusted instruction by default. | Model may still semantically follow untrusted content. | Prompt handling and tool dispatch enforce source trust boundaries. |
| AAEF-MEM-04 | T4; T6; T8 | Evidentiary / Detective | Preserves provenance for retrieved or remembered content influencing actions. | Influence may be difficult to prove fully. | Retrieval and memory systems expose source references to evidence events. |
| AAEF-EVD-01 | T8 | Evidentiary | Generates evidence sufficient for reconstruction. | Evidence may be incomplete or not tamper-evident. | Evidence requirements are implemented consistently. |
| AAEF-EVD-02 | T8 | Evidentiary | Standardizes key evidence fields for high-impact actions. | Fields may be present but inaccurate or self-reported. | Evidence field sources and trust levels are documented. |
| AAEF-EVD-03 | T8; T9 | Evidentiary | Links approval evidence to action evidence. | Approval and execution may still diverge if not action-bound. | Approval records are bound to specific action requests. |
| AAEF-EVD-04 | T8 | Evidentiary | Protects critical evidence against undetected alteration. | Tamper-evidence may not prevent deletion or data loss. | Integrity mechanism and retention policy are defined. |
| AAEF-EVD-05 | T8; T5 | Evidentiary | Records denied, deferred, escalated, or frozen high-impact actions. | Low-risk non-execution may be under-recorded. | Evidence depth is risk-proportional and high-impact non-execution is reviewable. |
| AAEF-EVD-06 | T3; T5; T8 | Evidentiary / Detective | Records reauthorization and additional scope requests. | Reauthorization can still be socially or procedurally abused. | Requests are scoped, linked to denial, and reviewed. |
| AAEF-HUM-01 | T4; T5; T8 | Preventive / Governance | Presents action context for informed human approval. | Human may still approve blindly or misunderstand risk. | Approval UI is clear and complete. |
| AAEF-HUM-02 | T8; T9 | Governance / Detective | Reduces blind approval and approval fatigue. | Fatigue may remain under high volume or poor thresholds. | Approval patterns are monitored and tuned. |
| AAEF-HUM-03 | T8; T9 | Evidentiary / Responsive | Records human override as append-only evidence. | Override may still be abused if authority is too broad. | Override actor, reason, scope, and linked action are recorded. |
| AAEF-HUM-04 | T3; T8; T9 | Preventive / Responsive | Constrains break-glass authority with scope, expiration, and review. | Emergency privileges may still be misused or not revoked. | Break-glass grants are time-bound, attributable, and post-reviewed. |
| AAEF-RES-01 | T9 | Responsive | Revokes agent authority, tool access, credentials, and delegations. | Revocation may not reach in-flight or offline workflows instantly. | Revocation paths are tested and documented. |
| AAEF-RES-02 | T6; T7; T9 | Responsive | Isolates compromised or suspicious agent instances or workflows. | Isolation may disrupt service or miss downstream effects. | Isolation procedures are tested and linked to evidence. |
| AAEF-RES-03 | T8; T9 | Responsive / Evidentiary | Reconstructs high-impact action sequence during incident review. | Reconstruction may be incomplete if evidence gaps exist. | Correlation and trace references are preserved. |
| AAEF-RES-04 | T5; T9 | Responsive / Preventive | Defines conditional authority freeze under state or risk triggers. | Distributed revocation may be delayed or partial. | Freeze behavior, in-flight handling, and propagation limits are documented. |
## Notes

- This mapping is qualitative and implementation-dependent.
- A control can provide more than one assurance type.
- Residual risk should be reviewed during assessment and not copied blindly.
- Implementation assumptions should be tested where possible.
- Future versions may add assurance strength, test depth, and assessment worksheet references.
