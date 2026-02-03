# Workflow: PR Regression Gate (LLM-assisted, engineering-grade)

## Goal
Produce a minimal, high-signal regression plan for a PR, backed by explicit risks and evidence from the diff.
This workflow is designed for repeatability and reviewability.

## Inputs (required)
- PR description
- Diff (or changed files + key snippets)
- System context:
  - components/services
  - deployment scope
  - critical user journeys
  - data stores
  - auth mechanisms
  - backward compatibility expectations
  - rollout strategy
  - monitoring/alerting

## Outputs (required)
1. Risk register with evidence
2. Ordered regression checklist
3. Targeted edge cases
4. Observability and rollback signals

---

## Step 0: Preconditions
Before involving an LLM, ensure:
- you have the correct diff (rebased, not outdated)
- PR description explains intent (feature vs refactor vs bugfix)
- you know the deployment scope (what ships together)

If any of these are missing, do not proceed. Fix inputs first.

---

## Step 1: Change intent and scope extraction
### Action
Use the task prompt:
- `prompts/pr/regression-from-diff.md`

### Provide
- PR description
- diff/snippets
- system context

### Expected outcome
A structured summary of what changed, what areas are touched, and what side effects are plausible.

### Quality gate
Reject output if it:
- invents behavior not present in inputs
- lists generic tests unrelated to the diff
- does not tie risks to evidence

If rejected, provide stricter context or reduce diff to relevant parts and rerun.

---

## Step 2: Convert risks into regression checks
### Action
From the risk register, derive a minimal test set:
- P0 covers: core flow, auth, data integrity, highest blast radius
- P1 covers: validation edges, compatibility, common failure modes
- P2 covers: informational checks only if cheap

### Rules
- every test must reference at least one risk
- avoid duplicates
- prefer checks that detect side effects fast (smoke + targeted negatives)

### Output
A regression checklist you can paste into:
- PR comment
- Jira subtasks
- release checklist

---

## Step 3: Decide what to automate now vs later
### Action
For each regression check, fill two separate fields:
- Execution: manual / auto
- Automation plan: now / later / n/a

### Decision rules
Set Automation plan = now if:
- it covers P0/P1 risks
- it is stable and deterministic
- it will be reused frequently

Set Automation plan = later if:
- environment/test data is unstable
- it is rare or low impact
- it depends on unclear requirements

Set Automation plan = n/a if:
- the check is intentionally manual-only (e.g., exploratory)

---

## Step 4: Execution plan
### Minimal standard set (default)
- Run existing CI suite (unit/component)
- Run impacted integration tests
- Execute 3 to 10 targeted regression checks from the checklist
- Verify negative cases only where risks imply them

### Evidence capture
For any failure, capture:
- request/response samples (redacted)
- logs/trace IDs
- exact build/commit SHA
- environment and configuration

---

## Step 5: Post-merge / post-deploy validation
### Action
Define what to watch:
- logs and error rates
- key business metrics if applicable
- latency/timeouts if touched
- data integrity checks for write paths

### Rollback triggers (must be explicit)
- sustained error rate increase
- data corruption signals
- security/auth failures
- broken core journey confirmed

---

## Quality gates (workflow-level)
This workflow is considered successful if:
- regression checks are linked to risks with evidence
- test set is minimal and prioritised
- assumptions and unknowns are explicit
- outputs are paste-ready for PR or Jira

Failure modes:
- generic checklist not tied to diff
- too many tests with no prioritisation
- hidden assumptions
- invented system behaviors

---

## Notes
- Treat this workflow as versioned process documentation.
- Update it when repeated review pain appears (new risk classes, recurring escapes).
