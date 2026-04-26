## Unreleased / v0.2.0 Public Review Draft — Work in Progress

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
- Updated README repository structure and document status for v0.2 work-in-progress artifacts.
- Updated citation metadata to use the full author name.

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

# Changelog

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
