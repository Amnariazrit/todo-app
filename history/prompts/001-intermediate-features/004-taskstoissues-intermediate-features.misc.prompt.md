---
id: 004
title: taskstoissues-intermediate-features
stage: misc
date_iso: 2026-01-03
surface: agent
model: Claude Sonnet 4.5
feature: intermediate-features
branch: 001-intermediate-features
user: Claude Code User
command: /sp.taskstoissues
labels:
  - issues
  - todo-app
  - intermediate-features
  - tasks
  - github
links:
  spec: specs/001-intermediate-features/spec.md
  tasks: specs/001-intermediate-features/tasks.md
  ticket: null
  adr: null
  pr: null
files_yaml:
  - specs/001-intermediate-features/tasks.md
tests_yaml:
  - tasks to issues conversion
  - issue creation attempt
---

## Summary

This PHR documents the attempt to convert tasks from tasks.md to GitHub issues. The attempt failed because the `gh` command-line tool was not available in the environment.

## Expected GitHub Issues

Based on the tasks.md file, the following issues would have been created:

### Phase 1: Setup (6 issues)
- T001: Create src/task.py file with basic Task class structure
- T002: Create src/storage.py file with global tasks list and state variables
- T003: Create src/utils.py file with helper function structure
- T004: Create src/commands.py file with command function structure
- T005: Create src/display.py file with display function structure
- T006: Create src/main.py file with main command dispatcher

### Phase 2: Foundational Components (7 issues)
- T007: Implement basic Task class with id, title, description, completed attributes
- T008: Set up global tasks list
- T009: Implement basic validate_priority function
- T010: Implement basic parse_tags function
- T011: Create placeholder command functions
- T012: Create placeholder display functions
- T013: Set up basic main dispatcher

### Phase 3: User Story 1 - Task Prioritization (7 issues)
- T014: Extend Task class with priority attribute
- T015: Add priority validation to Task.__init__
- T016: Update add_task command to accept and use priority parameter
- T017: Update list_tasks command to display priority in output
- T018: Implement priority display formatting
- T019: Complete validate_priority function with proper validation
- T020: Test priority assignment and display functionality

### Phase 4: User Story 2 - Task Tagging (7 issues)
- T021: Extend Task class with tags attribute
- T022: Add tags validation to Task.__init__
- T023: Update add_task command to accept and use tags parameter
- T024: Update list_tasks command to display tags in output
- T025: Implement tag display formatting
- T026: Complete parse_tags function with proper validation
- T027: Test tag assignment and display functionality

### Phase 5: User Story 3 - Filter Tasks (13 issues)
- T028: Implement get_visible_tasks function with filtering logic
- T029: Implement apply_filter function
- T030: Implement clear_filter function
- T031: Create filter_command function
- T032: Update list_tasks to use get_visible_tasks
- T033: Add filter status functionality
- T034: Add filter priority functionality
- T035: Add filter tag functionality
- T036: Add filter clear functionality
- T037: Update main.py to handle filter commands
- T038: Test filtering by status functionality
- T039: Test filtering by priority functionality
- T040: Test filtering by tag functionality

### Phase 6: User Story 4 - Sort Tasks (9 issues)
- T041: Implement set_sort function
- T042: Define SORT_CONFIG with all sorting options
- T043: Update get_visible_tasks to apply sorting
- T044: Create sort_command function
- T045: Update list_tasks to show sort status in output
- T046: Update main.py to handle sort commands
- T047: Test sorting by creation time functionality
- T048: Test sorting by title functionality
- T049: Test sorting by priority functionality

### Phase 7: User Story 5 - Clear Filters and Sorts (5 issues)
- T050: Update get_visible_tasks to handle no filters/sorts
- T051: Create filter_clear command
- T052: Update list_tasks to show appropriate status messages
- T053: Test clearing filters functionality
- T054: Test clearing sorts functionality

### Phase 8: Polish & Cross-Cutting Concerns (8 issues)
- T055: Add input validation for all commands to handle edge cases
- T056: Implement proper error messages for invalid inputs
- T057: Add status messages showing active filters/sorts in list output
- T058: Ensure consistent formatting across all display functions
- T059: Update main.py help text to include new commands
- T060: Test all commands together for integration issues
- T061: Perform end-to-end testing of all features
- T062: Update documentation comments in all files

## Conversion Attempt Result

The task-to-issues conversion failed because the `gh` command-line tool was not available in the environment. To complete this process, you would need to:

1. Install the GitHub CLI (`gh`) on your system
2. Authenticate with `gh auth login`
3. Run the command again in an environment with GitHub CLI access

## Alternative Approach

If GitHub CLI is not available, you could:
1. Manually create the issues in the GitHub web interface
2. Use the GitHub API directly
3. Export the tasks to a CSV format and import them

## Response Summary

Attempted to convert 62 tasks from tasks.md to GitHub issues but failed due to missing `gh` command. Documented all expected issues by phase and task ID for manual creation.