# Workflow: API Test Design (LLM-assisted, engineering-grade)

## Goal
Produce a minimal, risk-based API test set with an explicit contract and clear assumptions.
This workflow is designed for spec review, new endpoint delivery, and change impact analysis.

## Inputs (required)
- MODE: CLARIFY or EXECUTE
- API spec excerpt (OpenAPI snippet or equivalent)
- System context:
  - environments (dev/stage/prod)
  - auth mechanism and required headers
  - base URL (if known)
  - data constraints / business rules
  - known incidents / recent changes
  - execution constraints (tools, rate limits, test data, observability)

## Outputs (required)
- MODE=CLARIFY: questions only (max 7)
- MODE=EXECUTE: strict JSON artifact:
  - risks
  - prioritised testcases with assertions
  - explicit assumptions

---

## Step 0: Preconditions
Before using an LLM:
- Confirm you have the correct spec version.
- Confirm whether this is a new endpoint, a change, or a bugfix.
- Ensure you have at least minimal auth and error-handling expectations.

If not, proceed in MODE=CLARIFY.

---

## Step 1: Clarify ambiguity (MODE=CLARIFY)
### Action
Run `prompts/api/generate-testcases.md` in MODE=CLARIFY.

### Provide
- spec excerpt
- system context (even partial)

### Expected outcome
A short list of questions that unblock:
- auth and headers
- request/response schema
- expected status codes and error mapping
- validation rules, defaults, idempotency, pagination (if relevant)

### Quality gate
Reject output if questions are generic or not tied to decision points.

---

## Step 2: Generate the contracted artifact (MODE=EXECUTE)
### Action
Run `prompts/api/generate-testcases.md` in MODE=EXECUTE.

### Provide
- updated spec excerpt
- clarified answers
- system context

### Expected outcome
VALID JSON ONLY:
- risks tied to input evidence
- P0/P1/P2 testcases with assertions
- explicit assumptions

### Quality gate
Reject output if it:
- invents endpoints/fields/status codes
- does not include risks
- has tests without risk_refs
- violates JSON validity

---

## Step 3: Convert to execution plan
### Action
From the JSON output:
- select P0 tests as minimum gate
- select P1 tests as targeted regression
- keep P2 as optional / informational

### Automation decision (separate from the prompt)
Tag each testcase as:
- automate now
- automate later
- manual only

Rules:
- automate now: high reuse, stable assertions, high risk
- automate later: unstable data/env, low frequency, unclear requirements

---

## Step 4: Evidence capture standard
For failures, capture:
- request/response samples (redacted)
- correlation IDs / request-id headers
- environment and config
- build/commit SHA

---

## Step 5: Maintain examples as reference
- Keep `examples/api/` aligned with the prompt contract.
- When the contract changes, update the example in the same PR.

---

## Success criteria
- minimal, high-signal test set
- risks are explicit and tied to evidence
- assumptions are explicit
- artifact is paste-ready and portable
