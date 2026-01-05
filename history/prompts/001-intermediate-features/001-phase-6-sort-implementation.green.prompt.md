---
id: {ID}
title: {TITLE}
stage: {STAGE}
date: {DATE_ISO}
surface: agent
model: claude-sonnet-4-5-20250929
feature: {FEATURE}
branch: {BRANCH}
user: {USER}
command: /sp.implement
labels: ["implementation", "sorting", "todo-app", "phase-6"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-intermediate-features/tasks.md
  - src/utils.py
  - src/commands.py
  - src/main.py
tests:
  - test_sorting.py
---

# {TITLE}

## Context
{PROMPT_TEXT}

## Response Summary
{RESPONSE_TEXT}

## Outcome & Impact
{OUTCOME_IMPACT}

## Tests Summary
{TESTS_SUMMARY}

## Files Summary
{FILES_SUMMARY}

## Next Prompts
{NEXT_PROMPTS}

## Reflection
{REFLECTION_NOTE}

## Evaluation
- **Failure modes observed:** {FAILURE_MODES}
- **Next experiment to improve prompt quality:** {EXPERIMENT}

---
**Prompt:** {PROMPT_TEXT}
**Response:** {RESPONSE_TEXT}
