# Implementation Tasks: In-Memory Todo CLI App

**Feature**: In-Memory Todo CLI App
**Branch**: 001-todo-cli-app
**Generated**: 2026-01-01
**Based on**: specs/001-todo-cli-app/spec.md, plan.md, data-model.md, contracts/cli-contract.md

## Phase 1: Setup

### Goal
Initialize project structure and development environment according to the implementation plan.

### Independent Test Criteria
- Project directory structure matches plan
- Virtual environment is properly configured
- Basic project files exist and are correctly structured

### Tasks

- [X] T001 Create project directory structure: src/, tests/, and root files (README.md, CLAUDE.md, pyproject.toml)
- [X] T002 [P] Initialize UV virtual environment and create pyproject.toml with Python 3.13+ requirement
- [X] T003 [P] Create initial src/__init__.py and tests/__init__.py files
- [X] T004 [P] Create placeholder src/main.py, src/models.py, and src/storage.py files

## Phase 2: Foundational Components

### Goal
Implement core data model and storage components that will be used by all user stories.

### Independent Test Criteria
- Task data model is properly defined with all required attributes
- In-memory storage manager supports all required operations
- Both components have proper type hints and error handling

### Tasks

- [X] T005 Create Task data model in src/models.py with id, title, status, and created_at attributes
- [X] T006 Implement TaskManager class in src/storage.py with in-memory storage using dict
- [X] T007 [P] Add sequential ID assignment functionality to TaskManager
- [X] T008 [P] Implement add_task method in TaskManager with validation
- [X] T009 [P] Implement get_task method in TaskManager
- [X] T010 [P] Implement update_task method in TaskManager
- [X] T011 [P] Implement delete_task method in TaskManager
- [X] T012 [P] Implement list_tasks method in TaskManager
- [X] T013 [P] Implement mark_complete method in TaskManager
- [X] T014 [P] Add proper error handling for invalid task IDs in all TaskManager methods

## Phase 3: [US1] Add New Tasks

### Goal
Implement the ability to add new tasks to the todo list from the command line (User Story 1 - Priority P1).

### User Story Reference
A user wants to quickly add tasks to their todo list from the command line. They run a command like `python todo.py add "Buy groceries"` and the task gets added to their list with a unique ID and pending status.

### Independent Test Criteria
- Can run `python todo.py add "Buy milk"` and see a new task with ID 1 and status "pending"
- When existing tasks exist, new tasks get the next sequential ID
- Proper error handling for empty descriptions

### Tasks

- [X] T015 [P] [US1] Implement CLI argument parsing for add command in src/main.py
- [X] T016 [P] [US1] Create add_task function in src/main.py that connects CLI to TaskManager
- [X] T017 [US1] Test add command with valid description creates task with proper ID and status
- [X] T018 [P] [US1] Implement validation for empty task descriptions with error message
- [X] T019 [US1] Verify new tasks get next sequential ID when other tasks exist

## Phase 4: [US2] View All Tasks

### Goal
Implement the ability to view all tasks in a readable format from the command line (User Story 2 - Priority P1).

### User Story Reference
A user wants to see all their tasks in a readable format. They run `python todo.py list` and see a formatted list showing all tasks with their IDs, titles, and completion status.

### Independent Test Criteria
- Can run `python todo.py list` and see all tasks with ID, title, and status
- When no tasks exist, appropriate message indicates no tasks exist
- Output format is readable and clear

### Tasks

- [X] T020 [P] [US2] Implement CLI argument parsing for list command in src/main.py
- [X] T021 [P] [US2] Create list_tasks function in src/main.py that connects CLI to TaskManager
- [X] T022 [US2] Implement formatted output for tasks showing ID, title, and status
- [X] T023 [US2] Handle case when no tasks exist with appropriate message
- [X] T024 [US2] Test list command displays all tasks correctly

## Phase 5: [US3] Mark Tasks as Complete

### Goal
Implement the ability to mark tasks as complete from the command line (User Story 3 - Priority P2).

### User Story Reference
A user wants to mark tasks as complete when they finish them. They run `python todo.py complete 1` to mark task with ID 1 as completed, changing its status from pending to completed.

### Independent Test Criteria
- Can run `python todo.py complete 1` to change task status from "pending" to "completed"
- When listing tasks, completed tasks show proper status indicator
- Proper error handling for invalid task IDs

### Tasks

- [X] T025 [P] [US3] Implement CLI argument parsing for complete command in src/main.py
- [X] T026 [P] [US3] Create mark_complete function in src/main.py that connects CLI to TaskManager
- [X] T027 [US3] Test complete command changes task status from "pending" to "completed"
- [X] T028 [P] [US3] Verify completed tasks show proper indicator when listed
- [X] T029 [US3] Implement error handling for invalid task IDs in complete command

## Phase 6: [US4] Update Existing Tasks

### Goal
Implement the ability to update task descriptions from the command line (User Story 4 - Priority P2).

### User Story Reference
A user wants to modify the description of an existing task. They run `python todo.py update 1 "Buy organic milk"` to change the title of task ID 1.

### Independent Test Criteria
- Can run `python todo.py update 1 "New description"` to update task title while preserving other attributes
- Proper error handling for non-existent task IDs
- Proper error handling for empty descriptions

### Tasks

- [X] T030 [P] [US4] Implement CLI argument parsing for update command in src/main.py
- [X] T031 [P] [US4] Create update_task function in src/main.py that connects CLI to TaskManager
- [X] T032 [US4] Test update command changes title while preserving ID and status
- [X] T033 [P] [US4] Implement validation for empty task descriptions in update command
- [X] T034 [US4] Implement error handling for non-existent task IDs in update command

## Phase 7: [US5] Delete Tasks

### Goal
Implement the ability to delete tasks from the command line (User Story 5 - Priority P2).

### User Story Reference
A user wants to remove tasks they no longer need. They run `python todo.py delete 1` to remove the task with ID 1 from their list.

### Independent Test Criteria
- Can run `python todo.py delete 1` to remove task from the list
- After deletion, the task no longer appears when listing tasks
- Sequential ID counter does not reset after deletion

### Tasks

- [X] T035 [P] [US5] Implement CLI argument parsing for delete command in src/main.py
- [X] T036 [P] [US5] Create delete_task function in src/main.py that connects CLI to TaskManager
- [X] T037 [US5] Test delete command removes task from list
- [X] T038 [US5] Verify deleted task no longer appears when listing tasks
- [X] T039 [US5] Confirm sequential ID counter does not reset after deletion

## Phase 8: Error Handling and Input Validation

### Goal
Implement comprehensive error handling and input validation for all operations based on specification edge cases.

### Independent Test Criteria
- All edge cases from specification are handled properly
- User-friendly error messages for all invalid operations
- Validation for empty task descriptions across all commands
- Proper handling of invalid task IDs across all commands

### Tasks

- [X] T040 [P] Implement validation for non-existent task IDs across all commands
- [X] T041 [P] Implement validation for empty or invalid task descriptions
- [X] T042 [P] Add error handling for invalid command syntax
- [X] T043 [P] Create user-friendly error messages for all validation failures
- [X] T044 Handle special characters and very long task descriptions appropriately
- [X] T045 Test all edge cases identified in the specification

## Phase 9: Documentation and Polish

### Goal
Complete documentation and final testing to ensure the application meets all success criteria.

### Independent Test Criteria
- README.md contains clear setup and usage instructions
- All functionality works as specified in the user stories
- Performance meets success criteria (commands execute under 1 second)

### Tasks

- [X] T046 Create comprehensive README.md with setup instructions using UV
- [X] T047 [P] Add usage examples for all commands to README.md
- [X] T048 [P] Document all features and prerequisites in README.md
- [X] T049 Test all acceptance scenarios from specification
- [X] T050 [P] Verify all commands execute in under 1 second for performance requirement
- [X] T051 Test with 100+ tasks to verify performance with large lists
- [X] T052 Final integration testing of all features working together

## Dependencies

### User Story Completion Order
- Setup (Phase 1) → Foundational (Phase 2) → [US1] Add → [US2] List → [US3] Complete → [US4] Update → [US5] Delete

### Task Dependencies
- T005-T014 (Foundational) required before T015+ (User Stories)
- T015-T019 ([US1] Add) can be tested independently after foundational
- T020-T024 ([US2] List) can be tested independently after foundational
- T025-T029 ([US3] Complete) depends on foundational and can be tested independently
- T030-T034 ([US4] Update) depends on foundational and can be tested independently
- T035-T039 ([US5] Delete) depends on foundational and can be tested independently

## Parallel Execution Examples

### Per User Story
- **[US1] Add**: T015 and T016 can run in parallel (parsing and function)
- **[US2] List**: T020 and T021 can run in parallel (parsing and function)
- **[US3] Complete**: T025 and T026 can run in parallel (parsing and function)
- **[US4] Update**: T030 and T031 can run in parallel (parsing and function)
- **[US5] Delete**: T035 and T036 can run in parallel (parsing and function)

## Implementation Strategy

### MVP First
- Focus on [US1] Add and [US2] List as minimum viable product (both P1 priority)
- These two stories provide core value: adding and viewing tasks

### Incremental Delivery
1. Setup + Foundational + [US1] Add + [US2] List = MVP
2. Add [US3] Complete and [US5] Delete for basic CRUD
3. Add [US4] Update for full functionality
4. Complete error handling, documentation, and testing

### Testing Approach
- Each user story can be tested independently
- Integration testing after all user stories are complete
- Performance testing as final verification