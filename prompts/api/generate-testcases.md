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
Non-negotiables

-Do not invent endpoints, fields, status codes, or behaviors not present in the spec or context.

-If critical details are missing, STOP and ask clarifying questions before producing test cases.

-Prefer risk-based selection over exhaustive enumeration.

-Make assumptions explicit and reference them using IDs (A1, A2, ...).

-Output MUST follow the contract below exactly.

-Do not include commentary outside the output contract.

---
Clarification gate (mandatory)

If any of the following are missing or ambiguous, ask questions and STOP:

-authentication mechanism or required headers

-request and response schema

-expected success and error status codes

-idempotency or concurrency expectations for write endpoints

-pagination, filtering, or sorting rules (if listing resources)

-validation rules (required fields, formats, ranges)

Rules:

-Ask a maximum of 7 questions.

-Each question must unblock a concrete decision.

-Do not proceed until clarified.

---
Risk model (must drive prioritization)

Create a short risk register and reference risks in test cases.

Risk scale:

-Impact: Low / Med / High

-Likelihood: Low / Med / High

Common risk areas (use only if applicable to inputs):

-authn / authz

-data validation

-error handling

-idempotency

-pagination

-rate limiting

-backward compatibility

-data integrity

-concurrency

-caching

-timeouts

-observability

---
Output contract (STRICT)

Return VALID JSON ONLY, matching the structure below.
No markdown. No prose. No comments.
```
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
```

---
Priority rules

-P0: core flows, auth, data integrity, security, money, high blast radius

-P1: important negatives, validation, boundary conditions, common failures

-P2: low-impact, rare, cosmetic, informational

---
Rules:

-Every testcase MUST reference at least one risk.

-Assertions must be concrete and testable.

-If performance or SLA is unknown, DO NOT fabricate numbers.
Use a note instead.

---
Required coverage buckets (if applicable)

Produce at least one testcase per bucket when present in the spec:

-Happy path core flow (P0)

-Authentication and authorization (P0 / P1)

-Validation and boundary values (P1)

-Error payload shape and mapping (P1)

-Idempotency and retry safety (P0 / P1) for POST/PUT/PATCH

-Pagination, filtering, sorting (P1) where applicable

-Concurrency and race conditions (P1) where applicable

-Observability and correlation IDs (P2) if supported

---
Task

Using the provided inputs, produce output strictly matching the JSON contract.
---