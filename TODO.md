# TODO / Roadmap

This file tracks planned work. Keep items small and contract-driven.

## v0.2.0 - Quality gates (lightweight)
- Add GitHub Actions workflow `contract-check`:
  - validate JSON examples (parse + fail on invalid)
  - check that examples include MODE line in inputs
  - basic markdown sanity checks (headings present, no unclosed fences)
- Add PR checklist section (template or docs):
  - contract updated
  - example updated
  - changelog updated (if behavior changed)

## v0.3.0 - More real-work prompts
- `prompts/api/spec-review.md` (CLARIFY/EXECUTE)
- `prompts/bugs/triage-from-report.md` (CLARIFY/EXECUTE)
- `prompts/pr/diff-to-test-impact.md` (CLARIFY/EXECUTE)

## v0.4.0 - More workflows
- API Spec Review Gate workflow
- Bug triage loop workflow
- Release regression workflow (changeset to minimal suite)

## vNext (optional, only if it stays simple)
- Add `contracts/` with a JSON Schema for `api_testcases`
- Introduce prompt headers: Prompt-ID, Version, Contract summary
