# API Test Cases Generator (risk-based, deterministic)

## What this is
A task prompt for generating high-signal API test cases from a spec excerpt.
This prompt enforces: clarification over guessing, risk-based prioritization, and strict output structure.

---

## Input
Paste inputs below.

### 1) API Spec (required)
Provide OpenAPI excerpt or a precise endpoint description.

```text
<PASTE_OPENAPI_OR_ENDPOINT_SPEC_HERE>
```
---
### 2) Context (required)

-Environments: <dev / stage / prod>

-Auth: <JWT / OAuth2 / API key / none / unknown>

-Base URL: <if known>

-Data constraints / business rules: <if known>

-Out of scope: <if any>

-Known incidents / recent changes (optional): <if any>

---
### 3) Execution constraints (optional)

-Tooling: <Postman / newman / pytest / Playwright / other>

-Rate limits: <if any>

-Test data strategy: <seeded / ephemeral / shared env>

-Observability: <logs / metrics / traces / request-id>

---
## Mode selection (required)
Set one:
- MODE=CLARIFY
- MODE=EXECUTE

If MODE is not provided, default to MODE=CLARIFY.

---

## Non-negotiables
1. Do not invent endpoints, fields, status codes, or behaviors not present in the spec or context.
2. MODE=CLARIFY: ask questions and STOP. Do not output JSON.
3. MODE=EXECUTE: output VALID JSON ONLY. Do not ask questions.
4. Prefer risk-based selection over exhaustive enumeration.
5. Make assumptions explicit and reference them using IDs (A1, A2, ...), but only in MODE=EXECUTE.
6. In MODE=EXECUTE, if required inputs are missing, refuse and instruct rerun in MODE=CLARIFY.

---

## Clarification gate (MODE=CLARIFY only)
If any of the following are missing or ambiguous, ask questions and STOP:
- authentication mechanism or required headers
- request and response schema
- expected success and error status codes
- idempotency or concurrency expectations for write endpoints
- pagination, filtering, or sorting rules (if listing resources)
- validation rules (required fields, formats, ranges)

Rules:
- Ask a maximum of 7 questions.
- Each question must unblock a concrete decision.

### MODE=CLARIFY output format (STRICT)
Return Markdown only:

Questions:
1. <question>
2. <question>
...
(up to 7)

Stop after questions.

---

## Risk model (MODE=EXECUTE only)
Create a short risk register and reference risks in test cases.

Risk scale:
- Impact: Low / Med / High
- Likelihood: Low / Med / High

---

## Output contract (MODE=EXECUTE only, STRICT)
Return VALID JSON ONLY, matching the structure below.
No markdown. No prose. No comments.

```json
{
  "meta": {
    "artifact": "api_testcases",
    "version": "1.0",
    "source": "user_input",
    "assumptions": [
      { "id": "A1", "text": "assumption text" }
    ]
  },
  "risks": [
    {
      "id": "R1",
      "area": "authz",
      "impact": "High",
      "likelihood": "Med",
      "rationale": "explicitly tied to provided input"
    }
  ],
  "testcases": [
    {
      "id": "TC-001",
      "priority": "P0",
      "risk_refs": ["R1"],
      "title": "short, specific description",
      "endpoint": "METHOD /path",
      "preconditions": [
        "state or data that must exist before execution"
      ],
      "request": {
        "headers": { "<key>": "<value or placeholder>" },
        "query": { "<key>": "<value or placeholder>" },
        "path_params": { "<key>": "<value or placeholder>" },
        "body": { "<json field>": "<value or placeholder>" }
      },
      "assertions": [
        { "type": "status_code", "expected": "200" },
        { "type": "schema", "expected": "matches_spec" },
        { "type": "field", "path": "$.data.id", "expected": "not_null" }
      ],
      "notes": "optional, short"
    }
  ]
}

Task

If MODE=CLARIFY: produce only the questions and stop.

If MODE=EXECUTE: produce only the JSON output contract.
---