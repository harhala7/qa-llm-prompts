# Changelog

All notable changes to this repository are documented here.

This repo treats prompts like code:
- changes are versioned
- contracts are explicit
- examples are kept consistent with prompt output formats

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
