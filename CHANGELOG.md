# Changelog

All notable changes to this repository are documented here.

This repo treats prompts like code:
- changes are versioned
- contracts are explicit
- examples are kept consistent with prompt output formats

## v0.3.0
Bug triage decision support.

### Added
- Bug triage prompt with CLARIFY and EXECUTE modes.
- Example demonstrating real-world bug triage output.
- Bug triage loop workflow defining a repeatable QA decision process.

### Notes
- Bug triage is treated as a decision-support activity.
- Outputs are designed to be pasted directly into issue trackers (e.g. Jira).

## v0.2.0
Lightweight contract quality gates.

### Added
- GitHub Actions workflow `contract-check` to enforce repository contracts.
- Automated validation of JSON example outputs.
- Automated check for explicit MODE (CLARIFY / EXECUTE) in all example inputs.
- Automated detection of unbalanced Markdown code fences.
- Local contract check script (`tools/contract_check.py`) aligned with CI behavior.

### Notes
- Quality gates validate repository integrity only.
- No LLM execution or test execution is performed in CI.

## v0.1.0
Initial public release with stable contracts.

### Added
- Core QA system prompt with non-negotiables and mode concept (CLARIFY / EXECUTE)
- Task prompts:
  - API test case generation prompt with strict JSON contract (EXECUTE) and questions-only gate (CLARIFY)
  - PR regression planning prompt with strict Markdown contract (EXECUTE) and questions-only gate (CLARIFY)
- PR regression workflow sequencing prompts into a repeatable PR gate
- Examples:
  - PR example with input set and expected output aligned to the prompt contract
- README with purpose, structure, and quick start

### Fixed
- Contract consistency across prompts, workflows, and examples
- Closed JSON code fence in API prompt
- Added MODE requirement visibility to workflow
- Normalized system prompt title formatting
