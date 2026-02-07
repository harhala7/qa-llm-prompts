# Prompt: Bug Triage From Report

## Purpose
Analyze a bug report and produce a clear triage decision.
This prompt is used to assess severity, reproducibility confidence, likely impact, and next investigation steps.

---

## Modes
- MODE=CLARIFY: ask questions only
- MODE=EXECUTE: produce the triage artifact

If required information is missing in MODE=EXECUTE, refuse and instruct to rerun in MODE=CLARIFY.

---

## Input (required)
- MODE: CLARIFY or EXECUTE
- Bug report:
  - description (what happened)
  - expected vs actual behavior (if known)
  - environment (if known)
  - frequency / reproducibility (if known)
- System context (if available):
  - application / service
  - user impact
  - recent changes or releases
  - observability available (logs, metrics, traces)

---

## Task

### If MODE=CLARIFY
Ask up to 7 questions to unblock triage.
Questions must:
- reduce ambiguity
- enable severity assessment
- enable reproducibility assessment
- identify missing evidence

Do not provide any triage conclusions in this mode.

---

### If MODE=EXECUTE
Produce the following artifact in **strict Markdown**.
Do not include commentary outside the defined sections.

---

## Output Contract (MODE=EXECUTE)

### Summary
- One-sentence description of the issue in neutral, technical terms.

### Triage Decision
- Severity: Blocker / Critical / Major / Minor
- Confidence in repro: High / Medium / Low
- Release impact: Block release / Can ship with mitigation / No release impact

### Evidence Assessment
- What is confirmed by the report
- What is assumed or missing

### Suspected Area
- Most likely area: frontend / backend / api / data / infra / unknown
- Rationale based on available evidence

### Reproduction Checklist
- Minimal steps required to reproduce
- Preconditions or data requirements
- Environment constraints

### Logging and Diagnostics Needed
- Logs to capture
- Metrics to inspect
- Additional instrumentation required (if any)

### Next Actions
- Immediate actions (who should do what)
- Information to request if confidence is low
- Whether this should trigger regression coverage

---

## Rules
- Do not guess missing facts.
- Make assumptions explicit.
- Prefer minimal, high-signal output.
- If confidence is low, state it clearly.
