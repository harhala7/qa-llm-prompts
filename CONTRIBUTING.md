# Contributing

This repository treats prompts as engineering artifacts.
Changes are expected to be small, explicit, and contract-driven.

## Scope
Contributions are limited to:
- prompts (system or task-level)
- workflows that sequence prompts into repeatable QA processes
- examples that demonstrate expected inputs and outputs

Documentation and examples must remain aligned with prompt contracts.

---

## Modes
All task prompts operate in two modes:

- MODE=CLARIFY  
  Used to remove ambiguity. Output must be questions only.

- MODE=EXECUTE  
  Used to produce the contracted artifact. Output must strictly follow the defined format.

If required inputs are missing in MODE=EXECUTE, the prompt must refuse and instruct a rerun in MODE=CLARIFY.

---

## Prompt changes
When modifying or adding a prompt:
- do not rely on role-play or generic instructions
- make assumptions explicit
- forbid guessing; missing data must trigger clarification
- define a strict output contract (JSON or structured Markdown)

If a prompt’s output contract changes:
- update or add a corresponding example in the same PR

---

## Workflow changes
Workflows should:
- describe step-by-step usage of prompts
- clearly separate clarification from execution
- avoid embedding business logic that belongs in prompts

Workflows are process documentation and should be versioned accordingly.

---

## Examples
Examples are mandatory for behavior changes.

Rules:
- examples must match the prompt’s output contract exactly
- MODE must be explicit in example inputs
- examples should be realistic but minimal

If examples drift from the contract, the contract takes precedence.

---

## Pull requests
Guidelines:
- one logical change per PR
- keep diffs small and reviewable
- avoid formatting-only changes unless required by tooling
- update CHANGELOG.md when behavior or contracts change

PRs that introduce ambiguity, guessing, or non-deterministic output will be rejected.

---

## Non-goals
This repository is not:
- a generic prompt collection
- a tutorial or AI playground
- a replacement for real testing

It is decision-support tooling for QA engineers.
