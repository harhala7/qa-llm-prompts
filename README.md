# qa-llm-prompts

Engineering-grade prompts and workflows for QA work assisted by LLMs.
This repository treats prompts like code: versioned, refactorable, and constrained by output contracts.

## What this repository is
- A reusable prompt system for real QA tasks (API testing, PR regression)
- A set of repeatable workflows that combine prompts into processes
- Examples that show realistic inputs and expected outputs

## What this repository is not
- A collection of generic "act as a senior QA" prompts
- A tutorial or a theoretical guide
- A replacement for testing, this is decision support

## Structure
- `system/`
  - `qa-core.md`: core QA mindset and non-negotiables (no guessing, risk-based, explicit assumptions)
- `prompts/`
  - `api/`: prompts for API test design and spec review
  - `pr/`: prompts for regression planning from diffs
- `workflows/`
  - step-by-step processes that combine prompts for repeatable outcomes
- `examples/`
  - realistic inputs and expected outputs for credibility and reuse

## Quick start
1. Read `system/qa-core.md` and apply it as the base system prompt.
2. Choose a task prompt:
   - API test design: `prompts/api/generate-testcases.md`
   - PR regression: `prompts/pr/regression-from-diff.md`
3. Follow the workflow:
   - PR gate: `workflows/pr-regression-gate.md`
4. Use examples as reference:
   - `examples/pr/`

## Operating rules
- If inputs are missing, prompts must force clarification, not guessing.
- Outputs must follow strict contracts (structured, deterministic, paste-ready).
- Prefer high-signal minimal test sets over exhaustive checklists.

## Versioning
Prompts and workflows evolve. Breaking changes should be introduced via:
- a new version identifier in the prompt header, or
- a new file (keeping the old version for history)

## Contributing
Keep changes small and reviewable:
- one prompt or workflow change per PR
- update or add an example when behavior changes
