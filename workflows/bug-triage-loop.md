# Workflow: Bug Triage Loop (LLM-assisted, QA-grade)

## Goal
Turn unstructured bug reports into clear, repeatable triage decisions.
This workflow standardizes severity assessment, repro confidence, and next actions.

---

## Inputs (required)
- MODE: CLARIFY or EXECUTE
- Bug report (raw input from Jira, email, Slack, monitoring alert)
- System context (if available):
  - application / service
  - environment
  - user impact
  - recent releases or changes
  - observability available (logs, metrics, traces)

---

## Outputs
- MODE=CLARIFY: questions only
- MODE=EXECUTE: structured triage decision (Markdown)

---

## Step 0: Intake
### Action
Collect the raw bug report as-is.
Do not normalize or rewrite it yet.

### Notes
- Preserve original wording and timestamps.
- Avoid early severity labeling.

---

## Step 1: Clarify ambiguity (MODE=CLARIFY)
### When to use
- Report is vague, incomplete, or contradictory.
- Environment, repro steps, or impact are unclear.

### Action
Run `prompts/bugs/triage-from-report.md` in MODE=CLARIFY.

### Expected outcome
A short list of targeted questions that unblock:
- severity assessment
- repro confidence
- investigation direction

### Quality gate
Reject output if questions are generic or do not reduce ambiguity.

---

## Step 2: Triage decision (MODE=EXECUTE)
### Preconditions
- Sufficient information available to assess impact and repro.
- Open questions from Step 1 are answered or explicitly noted as missing.

### Action
Run `prompts/bugs/triage-from-report.md` in MODE=EXECUTE.

### Expected outcome
A structured triage artifact containing:
- severity and release impact
- repro confidence
- suspected area
- minimal repro checklist
- logging and diagnostics needs
- next actions

### Quality gate
Reject output if:
- severity is not justified
- assumptions are implicit
- next actions are vague

---

## Step 3: Decision and routing
### Action
Based on the triage artifact:
- confirm or adjust severity
- assign ownership (team or individual)
- decide on release impact:
  - block release
  - ship with mitigation
  - no release impact

### Notes
This step is a human decision supported by the artifact, not automated.

---

## Step 4: Investigation feedback loop
### Action
As investigation progresses:
- update the bug ticket with new evidence
- revisit the triage decision if assumptions are invalidated
- rerun MODE=EXECUTE if severity or scope changes

---

## Step 5: Regression and closure
### Action
Once resolved:
- decide whether regression coverage is required
- link new or updated tests to the bug
- close the ticket with a summary of findings

---

## Success criteria
- triage decisions are consistent across reporters
- severity and release impact are explicit and justified
- investigation starts with clear hypotheses and evidence needs
- no critical bugs proceed without deliberate decision
