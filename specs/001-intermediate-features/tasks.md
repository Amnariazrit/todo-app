# Tasks: Intermediate Level Features for Todo App

**Feature**: Intermediate Level Features for Todo App
**Branch**: 001-intermediate-features
**Generated from**: specs/001-intermediate-features/spec.md and specs/001-intermediate-features/plan.md

## Implementation Strategy

MVP scope: Implement User Story 1 (Task Prioritization) first to deliver core value, then incrementally add other features. Each user story is designed to be independently testable and deliverable.

## Dependencies

User stories dependencies:
- US2 (Task Tagging) has no dependencies
- US3 (Filter Tasks) depends on US1 and US2 (needs priority and tags to filter)
- US4 (Sort Tasks) depends on US1 and US2 (needs priority and tags to sort)
- US5 (Clear Filters and Sorts) depends on US3 and US4 (needs filter and sort functionality)

## Parallel Execution Examples

Per user story:
- US1: Task model updates (task.py) can be done in parallel with storage updates (storage.py)
- US2: Tag validation (utils.py) can be done in parallel with command updates (commands.py)
- US3: Filter implementation can be done in parallel with display updates
- US4: Sort implementation can be done in parallel with command updates

---

## Phase 1: Setup

- [X] T001 Create src/task.py file with basic Task class structure per plan
- [X] T002 Create src/storage.py file with global tasks list and state variables per plan
- [X] T003 Create src/utils.py file with helper function structure per plan
- [X] T004 Create src/commands.py file with command function structure per plan
- [X] T005 Create src/display.py file with display function structure per plan
- [X] T006 Create src/main.py file with main command dispatcher per plan

## Phase 2: Foundational Components

- [X] T007 [P] Implement basic Task class with id, title, description, completed attributes in src/task.py
- [X] T008 [P] Set up global tasks list in src/storage.py
- [X] T009 [P] Implement basic validate_priority function in src/utils.py
- [X] T010 [P] Implement basic parse_tags function in src/utils.py
- [X] T011 [P] Create placeholder command functions in src/commands.py
- [X] T012 [P] Create placeholder display functions in src/display.py
- [X] T013 [P] Set up basic main dispatcher in src/main.py

## Phase 3: User Story 1 - Task Prioritization (Priority: P1)

Goal: Enable users to assign priority levels (high, medium, low) to tasks and see them displayed.

Independent Test: Can be fully tested by adding tasks with different priority levels and verifying that the priority is displayed when listing tasks, delivering the value of quickly identifying important tasks.

- [X] T014 [P] [US1] Extend Task class with priority attribute in src/task.py
- [X] T015 [P] [US1] Add priority validation to Task.__init__ in src/task.py
- [X] T016 [US1] Update add_task command to accept and use priority parameter in src/commands.py
- [X] T017 [US1] Update list_tasks command to display priority in output in src/commands.py
- [X] T018 [P] [US1] Implement priority display formatting in src/display.py
- [X] T019 [P] [US1] Complete validate_priority function with proper validation in src/utils.py
- [X] T020 [US1] Test priority assignment and display functionality

## Phase 4: User Story 2 - Task Tagging (Priority: P1)

Goal: Enable users to tag tasks with descriptive keywords for categorization and grouping.

Independent Test: Can be fully tested by adding tasks with tags and verifying that tags are displayed when listing tasks, delivering the value of categorizing tasks.

- [X] T021 [P] [US2] Extend Task class with tags attribute in src/task.py
- [X] T022 [P] [US2] Add tags validation to Task.__init__ in src/task.py
- [X] T023 [US2] Update add_task command to accept and use tags parameter in src/commands.py
- [X] T024 [US2] Update list_tasks command to display tags in output in src/commands.py
- [X] T025 [P] [US2] Implement tag display formatting in src/display.py
- [X] T026 [P] [US2] Complete parse_tags function with proper validation in src/utils.py
- [X] T027 [US2] Test tag assignment and display functionality

## Phase 5: User Story 3 - Filter Tasks (Priority: P2)

Goal: Enable users to filter tasks by status, priority, or tags to focus on specific subsets.

Independent Test: Can be fully tested by creating tasks with different attributes and applying various filters, delivering the value of quickly finding specific tasks.

- [X] T028 [P] [US3] Implement get_visible_tasks function with filtering logic in src/utils.py
- [X] T029 [P] [US3] Implement apply_filter function in src/utils.py
- [X] T030 [P] [US3] Implement clear_filter function in src/utils.py
- [X] T031 [US3] Create filter_command function in src/commands.py
- [X] T032 [US3] Update list_tasks to use get_visible_tasks in src/commands.py
- [X] T033 [US3] Add filter status functionality in src/commands.py
- [X] T034 [US3] Add filter priority functionality in src/commands.py
- [X] T035 [US3] Add filter tag functionality in src/commands.py
- [X] T036 [US3] Add filter clear functionality in src/commands.py
- [X] T037 [US3] Update main.py to handle filter commands
- [X] T038 [US3] Test filtering by status functionality
- [X] T039 [US3] Test filtering by priority functionality
- [X] T040 [US3] Test filtering by tag functionality

## Phase 6: User Story 4 - Sort Tasks (Priority: P2)

Goal: Enable users to reorder the task list by different criteria (creation time, title, priority) to suit their needs.

Independent Test: Can be fully tested by creating tasks and applying different sort orders, delivering the value of organizing tasks in a preferred sequence.

- [X] T041 [P] [US4] Implement set_sort function in src/utils.py
- [X] T042 [P] [US4] Define SORT_CONFIG with all sorting options in src/utils.py
- [X] T043 [US4] Update get_visible_tasks to apply sorting in src/utils.py
- [X] T044 [US4] Create sort_command function in src/commands.py
- [X] T045 [US4] Update list_tasks to show sort status in output in src/commands.py
- [X] T046 [US4] Update main.py to handle sort commands
- [X] T047 [US4] Test sorting by creation time functionality
- [X] T048 [US4] Test sorting by title functionality
- [X] T049 [US4] Test sorting by priority functionality

## Phase 7: User Story 5 - Clear Filters and Sorts (Priority: P3)

Goal: Enable users to clear active filters and sorts to return to viewing all tasks in default order.

Independent Test: Can be fully tested by applying filters/sorts and then clearing them, delivering the value of returning to the default view.

- [X] T050 [US5] Update get_visible_tasks to handle no filters/sorts in src/utils.py
- [X] T051 [US5] Create filter_clear command in src/commands.py
- [X] T052 [US5] Update list_tasks to show appropriate status messages in src/commands.py
- [X] T053 [US5] Test clearing filters functionality
- [X] T054 [US5] Test clearing sorts functionality

## Phase 8: Polish & Cross-Cutting Concerns

- [X] T055 [P] Add input validation for all commands to handle edge cases
- [X] T056 [P] Implement proper error messages for invalid inputs
- [X] T057 [P] Add status messages showing active filters/sorts in list output
- [X] T058 [P] Ensure consistent formatting across all display functions
- [X] T059 [P] Update main.py help text to include new commands
- [X] T060 [P] Test all commands together for integration issues
- [X] T061 [P] Perform end-to-end testing of all features
- [X] T062 [P] Update documentation comments in all files