# Changelog

## Unreleased

### Added

- Added a temporary v0.5.x evidence integrity negative tests track proposal.

### Changed

- Updated v0.5.x status documents after the first evidence schema and example implementation wave.

### Added

- Added an approval-binding evidence example using optional approval source, approval binding, and enforcement fields.
- Added an integrity-focused evidence example using optional evidence integrity and trust limitation fields.
- Added optional Evidence Event Schema fields for evidence integrity, evidence trust limitations, approval evidence source, approval binding, and approval enforcement references.
- Added a temporary v0.5.x evidence schema/example implementation readiness review.
- Added a temporary v0.5.x evidence example design proposal.
- Added a temporary v0.5.x evidence schema field proposal.
- Added a temporary v0.5.x evidence schema and examples track proposal.
- Added a temporary v0.5.x next phase track plan.
- Added a temporary v0.5.x incorporation review checkpoint for #161, #163, #165, and #167.

### Changed

- Updated v0.5.x status documents after the evidence integrity CSV refinement proposal review.

### Added

- Added a temporary v0.5.x evidence integrity CSV refinement proposal.

### Changed

- Updated v0.5.x status documents after the approval quality testing procedure refinement.
- Refined `AAEF-HUM-01` and `AAEF-AUZ-03` testing procedure language for approval quality and approval-to-execution binding.

### Added

- Added a temporary v0.5.x approval quality CSV refinement proposal.
- Added a temporary v0.5.x approval quality testing candidate appendix.
- Added a temporary v0.5.x approval quality testing proposal.

### Changed

- Updated v0.5.x status documents after the cross-agent delegation testing procedure refinement.
- Refined `AAEF-DEL-01` and `AAEF-DEL-05` testing procedure language for cross-agent delegation authority validation.

### Added

- Added a temporary v0.5.x cross-agent delegation CSV refinement proposal.
- Added a temporary v0.5.x cross-agent delegation testing candidate appendix.
- Added a temporary v0.5.x cross-agent delegation testing proposal.

### Changed

- Updated v0.5.x status documents after the principal context testing procedure refinement.
- Refined `AAEF-AUZ-02` and `AAEF-AUZ-07` testing procedure language for scope expansion and authority lifecycle state changes.

### Added

- Added a temporary v0.5.x principal context testing CSV refinement proposal.
- Added a temporary v0.5.x principal context testing candidate appendix.
- Added a temporary v0.5.x principal context testing proposal for the first testing incorporation batch.
- Added a temporary v0.5.x testing incorporation readiness review for selected testing candidates.
- Added temporary v0.5.x testing draft pass/fail criteria for selected testing candidates.
- Added a temporary v0.5.x testing candidate mapping document for likely control areas and evidence expectations.
- Added a temporary v0.5.x testing procedure candidate matrix for selected testing candidates.
- Added a temporary v0.5.x testing candidate selection document for #161, #163, and #167.
- Added a temporary v0.5.x incorporation decision register for #161 through #167.
- Added temporary v0.5.x follow-up status tracking under `docs/en/status/`.
- Added a document map to classify AAEF documents by role without moving existing files.
- Added non-normative approval quality testing and evidence guidance for v0.5.x follow-up work.
- Added non-normative tamper-evident evidence requirements guidance for selected v0.5.x contexts.
- Added non-normative evidence integrity profile guidance for high-impact and audit-grade v0.5.x follow-up work.
- Added non-normative principal context degradation testing guidance for v0.5.x follow-up work.
- Added non-normative cross-agent budget propagation guidance for v0.5.x follow-up work.
- Added non-normative cross-agent delegation negative test guidance for v0.5.x follow-up work.
- Added non-normative capability-scoped cross-agent delegation guidance for v0.5.x follow-up work.
- Added a researcher overview as a research-facing entry point with reading paths, review questions, and links to open research questions and v0.5.x follow-up work.

## v0.5.0 Public Review Planning Release - 2026-04-29

### Changed

- Added a v0.5.0 release preparation checklist with validation steps, issue review guidance, follow-up issue candidates, and draft release notes.
- Added a v0.5.0 release scope decision record clarifying that current planning models remain non-normative unless explicitly incorporated into future normative or assessment artifacts.
- Added a non-normative v0.5.0 approval quality model for meaningful approval, approval context sufficiency, batch approval risk, approval fatigue, and approval evidence expectations.
- Refined cross-agent authority lifecycle guidance for capability-scoped delegation, explicit acceptance or refusal, delegation chain limits, evidence linkage, and budget propagation.
- Added a non-normative v0.5.0 evidence integrity levels model for risk-proportional evidence, tamper-evident storage, and performance overhead tradeoffs.
- Added `docs/en/18-implementation-guidance.md` to close the documentation numbering gap and provide non-normative implementation adoption guidance.
- Added a non-normative v0.5.0 authority lifecycle model covering principal context degradation, cross-agent authority, denial, freeze, revocation, and reauthorization.
- Added a preliminary v0.5.0 incorporation outcome register for current planning themes.
- Added v0.5.0 planning incorporation rules to clarify when planning concepts become guidance, testing refinements, evidence refinements, existing control refinements, or new controls.
- Clarified that `docs/en/30-49` v0.5.0 planning materials are non-normative unless explicitly incorporated into catalog, schema, assessment, testing, or release artifacts.
- Clarified the v0.5.0 planning overview by grouping the six planning themes into authority lifecycle and supporting assurance themes.
- Added missing v0.5.0 planning document index entries for Principal Context Degradation and tamper-evident evidence negative tests.
- Clarified current-status wording for v0.2-originated documents that remain part of the v0.4.1 Public Review Draft baseline.

## v0.4.1 Public Review Refinement Release - 2026-04-28

This maintenance release refines the v0.4.0 Public Review Draft based on post-release review work.

Additional documentation consistency fixes:
- Added missing human-readable control requirement sections for `AAEF-HUM-03` and `AAEF-HUM-04`.
- Updated One-page Overview references from v0.2-specific wording to current public review support artifacts.
- Updated Korean and Simplified Chinese README document status and citation text to v0.4.1.
- Updated README repository structure to include current v0.5.0 planning documents and mapping files.

### Changed

- Refined control-specific testing procedure criteria across all 44 controls.
- Updated testing procedure pass, partial, fail, sample selection, notes, and automation potential fields.
- Refined external framework mapping methodology and copyright-sensitive source handling.
- Updated external mapping records to use more conservative, non-equivalence-oriented language.
- Refreshed OWASP Agentic Top 10 mapping for the v0.4.x baseline.
- Added NIST AI RMF / Generative AI Profile mapping.
- Added ISO/IEC 42001 feasibility note and high-level mapping row.
- Added CSA Agentic Trust Framework mapping.

### Notes

- This release remains a Public Review Draft.
- External mappings are informative alignment aids only.
- External mappings do not imply compliance equivalence, certification readiness, audit sufficiency, or conformity with external frameworks.
- ISO/IEC 42001-related materials are handled at a high-level, copyright-safe feasibility level only.

## v0.4.0 Public Review Draft - 2026-04-28

This release expands the v0.3.x public review baseline with enterprise assessment usability guidance for agentic AI action assurance.

### Added

- Added Control Catalog Versioning and Change Impact guidance.
- Added Testing Procedures and Pass Criteria guidance.
- Added machine-readable testing procedure draft.
- Added validation for testing procedures.
- Added High-Impact and Audit-Grade Pre-qualification Gate guidance.
- Added Trusted Control Boundary Integrity Requirements.
- Added External Framework Mapping Methodology.
- Added initial conservative external framework mapping draft.
- Added validation for external framework mappings.

### Changed

- Updated README document status, Start Here, repository structure, and citation text for v0.4.0.
- Updated One-page Overview current status for v0.4.0.
- Updated `CITATION.cff` for the v0.4.0 public review draft.
- Expanded consolidated artifact validation to include testing procedures and external mappings.

### Notes

- This release remains a public review draft.
- It does not create a certification scheme, formal standard, implementation conformance claim, audit opinion, compliance equivalence, or claim of complete mitigation.
- External mappings are informative only and do not claim compliance equivalence or audit sufficiency.
- v0.3.1 remains available as the prior maintenance release.

## v0.3.1 Maintenance Release - 2026-04-27

This maintenance release improves repository organization, version reference consistency, and automated validation after the v0.3.0 Public Review Draft.

### Added

- Added a consolidated GitHub Actions workflow for AAEF artifact validation.

### Changed

- Moved release preparation checklists into `docs/en/release/`.
- Marked release preparation checklists as historical release preparation artifacts.
- Clarified current version references after the v0.3.0 release.
- Updated `CITATION.cff` for the v0.3.1 maintenance release.
- Consolidated validation workflows into `.github/workflows/validate-aaef-artifacts.yml`.

### Notes

- This release does not change the v0.3.0 Public Review Draft baseline scope.
- This release remains part of the public review draft series.
- It does not create a certification scheme, formal standard, implementation conformance claim, audit opinion, or claim of complete mitigation.

## v0.3.0 Public Review Draft - 2026-04-27

This release expands the v0.2.x public review baseline with implementation profiles, evidence quality assessment criteria, action sequence monitoring, assessment automation guidance, and infrastructure / SIEM evidence integration patterns.

### Added

- Added Evidence Quality Gate assessment outcomes and assertion source strength guidance.
- Added Assessment Profiles and tiered applicability guidance for Lite, Standard, High-Impact, and Audit-Grade profiles.
- Added Assessment Profile Mapping sidecar CSV without changing the Control Catalog.
- Added validation for the Assessment Profile Mapping.
- Added TCB implementation capability patterns to the Reference Architecture.
- Added Action Sequence Monitoring and Task Splitting guidance.
- Added Assessment Automation and Human Review Classification guidance.
- Added Infrastructure and SIEM Evidence Integration guidance.
- Added v0.3.0 Release Preparation Checklist.

### Changed

- Updated README document status, repository structure, and citation metadata for v0.3.0.
- Updated One-page Overview current status for v0.3.0.
- Clarified that automated repository validation is structural validation, not security assurance, audit opinion, or implementation conformance.

### Notes

- This release remains a public review draft.
- It does not create a certification scheme or claim complete mitigation.
- v0.2.1 remains available as the prior public review refinement baseline.

## v0.2.1 Public Review Refinement - 2026-04-27

This release incorporates post-v0.2.0 public review refinements.

### Added

- Added Evidence Event Schema profile guidance for Minimal, High-Impact, Audit-Grade, Non-Execution, and Override / Break-Glass evidence profiles.
- Added High-Impact and Audit-Grade Evidence Event examples.
- Added validation coverage for High-Impact and Audit-Grade Evidence Event examples.
- Added Evidence Quality Gate guidance for high-impact actions.
- Added weak and adversarial evidence examples for high-impact action assessment.
- Added Open Research Questions for agentic action assurance.
- Added high-impact action review surface guidance.

### Changed

- Improved README onboarding and role-based reading paths.
- Strengthened Trusted Control Boundary and Tool Dispatch Enforcement Point guidance.
- Clarified evidence assertion sources and input influence assessment.
- Clarified that AAEF can be implemented using existing identity, authorization, runtime isolation, enforcement, and audit mechanisms.
- Linked Evidence Event Schema profiles to concrete examples.
- Aligned the assessment worksheet with the control catalog.
- Renamed worksheet `Maturity` to `Requirement Level`.

### Tooling

- Added assessment worksheet validation.
- Expanded evidence schema validation to include High-Impact and Audit-Grade examples.

### Notes

- This release remains a public review refinement.
- It does not create a certification scheme or claim complete mitigation.
- v0.2.0 remains available as the prior public review baseline.

## v0.2.0 Public Review Draft - 2026-04-26

- Added preliminary OWASP Agentic Top 10 2026 mapping.
- Added initial Agentic Action Evidence Event JSON Schema.
- Added minimal, valid, and invalid evidence event examples.
- Added Evidence Event Schema validation workflow.
- Expanded the Evidence Event Schema for v0.2 control areas, including authorization decision artifacts, intent alignment, state checks, input influence assessment, delegation lineage, override, non-execution, and reauthorization.
- Added High-Impact Action Taxonomy draft.
- Added v0.2 Control Expansion Notes.
- Added authorization and revocation control expansion entries.
- Added human, delegation, and evidence control expansion entries.
- Added Assurance Model and Residual Risk Mapping.
- Added Assessment Quick Start and Assessment Worksheet draft.
- Added One-page Overview for first-time readers.
- Added Reference Architecture and Mermaid diagram source.
- Added v0.2.0 Release Preparation Checklist.
- Updated README repository structure and document status for the v0.2.0 Public Review Draft.
- Updated citation metadata to use the full author name and v0.2.0 public review release metadata.

## v0.1.5 Public Review Draft

- Added the public GitHub repository URL to `CITATION.cff`.

## v0.1.4 Public Review Draft

- Added links to external articles and announcements in the main README.
- Clarified that external articles are explanatory materials and that the English repository documentation remains authoritative.

## v0.1.3 Public Review Draft

- Added machine-translated reference README files for Japanese, Simplified Chinese, and Korean.
- Added translation disclaimer and language links to the main README.
- Clarified that the English README and `docs/en/` are authoritative.
- Added a translation feedback issue template.

## v0.1 Public Review Draft — revised pre-publication package

Incorporates early review feedback:

- Declares `controls/aaef-controls-v0.1.csv` as the control catalog source of truth.
- Adds validation script and GitHub Actions workflow for control ID consistency.
- Unifies maturity levels across trust model and assessment methodology.
- Strengthens prompt-injection-related controls.
- Clarifies why logs are not automatically evidence.
- Adds implementation guidance for principal context propagation and reflects it in `AAEF-PRN-02` testing and evidence expectations.
- Raises high-impact retrieval and memory provenance expectations in `AAEF-MEM-04` from recommended to required.
- Clarifies the distinction between authorization-layer controls (`AAEF-AUZ-05`) and tool-dispatch controls (`AAEF-TOOL-04`).
- Adds caution and prerequisites for Level 4 autonomy.
- Improves CONTRIBUTING and SECURITY guidance.
- Updates CITATION metadata with independent consultant affiliation.

## v0.1 Public Review Draft

Initial public review draft.

Includes:

- project positioning,
- scope statement,
- core principles,
- initial terminology,
- threat model,
- trust model,
- control domains,
- initial control requirements,
- assessment methodology,
- relationship to existing frameworks,
- control catalog CSV,
- example agentic action evidence event,
- attack-control mapping example.

- Added a maintenance and validation note explaining the purpose and limits of the control catalog validator.
- Made the control catalog validator independent from the current working directory and documented local execution.
- v0.1.2: Removed placeholder repository URL from CITATION.cff. Add repository-code after the public GitHub URL is finalized.
