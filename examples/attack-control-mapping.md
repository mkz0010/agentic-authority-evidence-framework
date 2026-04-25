# Attack-Control Mapping Example

This document provides an initial example of how AAEF controls may map to agentic AI attack patterns.

| Attack Pattern | Description | Relevant AAEF Controls |
|---|---|---|
| Ghost Agent | A malicious or unapproved agent impersonates a legitimate agent. | AAEF-ID-01, AAEF-ID-03, AAEF-EVD-01 |
| Principal Confusion | An action is attributed to the wrong human, organization, or upstream agent. | AAEF-PRN-01, AAEF-PRN-02, AAEF-EVD-02 |
| Delegation Escalation | A downstream agent receives more authority than the delegating party held. | AAEF-DEL-01, AAEF-DEL-02, AAEF-DEL-03 |
| Stale Delegation Reuse | Expired or revoked delegation is reused. | AAEF-DEL-04, AAEF-RES-01 |
| Direct Prompt Injection to Tool Use | A user prompt attempts to override policy and trigger a high-risk tool. | AAEF-AUZ-01, AAEF-AUZ-04, AAEF-AUZ-05, AAEF-TOOL-02 |
| Indirect Prompt Injection to Tool Use | External content such as a web page, email, ticket, or document contains instructions that cause unauthorized tool use. | AAEF-AUZ-05, AAEF-TOOL-04, AAEF-MEM-03, AAEF-MEM-04 |
| Tool-Intent Mismatch | A tool is invoked for a purpose different from the approved purpose. | AAEF-AUZ-02, AAEF-TOOL-02, AAEF-TOOL-04 |
| Tool Misuse | A legitimate tool is used for an unauthorized purpose. | AAEF-AUZ-02, AAEF-TOOL-01, AAEF-TOOL-03 |
| Task Splitting | A high-risk action is split into smaller actions to avoid approval. | AAEF-AUZ-03, AAEF-EVD-01, AAEF-HUM-01 |
| Memory Poisoning | Persistent memory influences future actions with false or malicious content. | AAEF-MEM-01, AAEF-MEM-02, AAEF-MEM-04, AAEF-RES-02 |
| Evidence Gap | The organization cannot reconstruct what happened. | AAEF-EVD-01, AAEF-EVD-02, AAEF-RES-03 |
| Approval Fatigue | Human approvers approve risky actions without understanding. | AAEF-HUM-01, AAEF-HUM-02 |
