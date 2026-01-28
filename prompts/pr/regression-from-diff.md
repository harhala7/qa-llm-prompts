# PR Regression & Change Impact Analysis (QA gate)

## What this is
A task prompt for analyzing pull requests and producing a focused,
risk-based regression plan.

This prompt is designed for real PR review and release decisions.
It prioritizes detection of unintended side effects over test volume.

---

## Input
Paste inputs below.

### 1) PR Description (required)

<PASTE_PR_DESCRIPTION_HERE>

---

### 2) Code Diff or Change Summary (required)

Provide either:

full diff, or

list of changed files with relevant snippets
```
<PASTE_DIFF_OR_CHANGE_SUMMARY_HERE>
```
---
### 3) System Context (required)

- Components / services affected:

- Deployment scope: <single service / multi-service / shared lib>

- Critical user journeys:

- Data stores involved:

- Auth mechanisms involved:

- Backward compatibility expectations:

- Rollout strategy: <all at once / canary / feature flag>

- Monitoring & alerting available:

---

### Non-negotiables

- Do not assume behavior not evidenced in the diff or context.

- If the change intent or scope is unclear, STOP and ask clarifying questions.

- Prefer minimal, high-signal regression over exhaustive testing.

- Tie every test or risk to evidence in the diff.

- Do not invent tests for unaffected areas.

- Output MUST follow the format below exactly.

---
### Clarification gate (mandatory)

- If any of the following are unclear, ask questions and STOP:

- intended behavior change vs refactor

- backward compatibility expectations

- data migration or schema impact

- feature flag or config behavior

- deployment and rollback strategy

---
#### Rules:

- Ask a maximum of 7 questions.

- Each question must unblock a concrete risk or test decision.

- Do not proceed until clarified.

### Risk model

- Create a concise risk register derived directly from the diff.

### Risk scale:

- Impact: Low / Med / High

- Likelihood: Low / Med / High

#### Common regression risk areas (use only if supported by inputs):

- authn / authz

- data persistence and migrations

- serialization / deserialization

- config and feature flags

- default values and fallbacks

- backward compatibility

- error handling and mapping

- concurrency and race conditions

- caching and invalidation

- performance and timeouts

- logging and observability

---
### Output format (STRICT)
#### Summary

- Change intent:

- Areas touched:

- Non-obvious side effects:

---
### Risk Register
```
- Risk ID	Area	
- Impact	Likelihood	
- Evidence in diff	
- What could break					
```
### Regression Checklist (ordered by priority)
```
- Test ID	Priority	
- Type (manual / auto)	
- Scope (unit / component / integration / e2e)	
- What to execute	
- Expected result	Risk refs					
```

#### Rules:

P0: core flows, data integrity, security, high blast radius

P1: important negatives, edge cases, compatibility

P2: low-impact or informational checks

Each test MUST reference at least one risk.

---

### Targeted Negative & Edge Cases

#### List only cases directly implied by the diff.

- EC-1:

- EC-2:

---

### Observability & Rollback Signals

- Metrics or logs to watch:

- Symptoms that require rollback:

- Data integrity checks post-deploy:

---

### Task

Using the provided inputs, produce the output exactly in the format above.