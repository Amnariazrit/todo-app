# Feature Specification: Intermediate Level Features for Todo App

**Feature Branch**: `001-intermediate-features`
**Created**: 2026-01-03
**Status**: Draft
**Input**: User description: "make a proper spec for intermediate level\n## Phase I – Intermediate Level Features Only\n### Organization & Usability for In-Memory Python Console Todo App\n\n### Context\n- Phase: Phase I (In-Memory Python Console App)\n- Prerequisite: Basic Level features (Add, Delete, Update, View, Mark Complete) already fully implemented\n- Goal: Extend the existing console app with Intermediate Level features to make it more polished and practical\n- Storage: Strictly in-memory (no file/database persistence)\n- Development: Strictly Spec-Driven using Claude Code + Spec-Kit Plus. No manual coding.\n\n### 1. Feature: Priorities\n#### User Stories\n- As a user, I want to assign a priority level (high, medium, low) to tasks so I can identify urgent items quickly.\n- As a user, I want to see the priority clearly when listing tasks.\n\n#### Acceptance Criteria\n- Task object gains a new attribute `priority: str` with allowed values: \"high\", \"medium\", \"low\"\n- Default priority: \"medium\" (if not specified)\n- During `add`: prompt \"Priority time (simplicity for console app)\n- After applying filter: show message \"Showing X tasks (filtered by ...)\"\n- `list` command respects current filter\n\n### 5. Feature: Sort Tasks\n#### User Stories\n- As a user, I want to reorder the task list by different criteria to suit my current needs.\n\n#### Acceptance Criteria\n- ompleted`    | New: Filter by status\n`filter priority high/medium/low`    | New: Filter by priority\n`filter tag <tag>`                   | New: Filter by tag\n`filter clear`                       | New: Clear active filter\n`sort created/created_desc/title/title_desc/priority/priority_rev` | New: Change sort order\n\n### Non-Functional Requirements\n- Task class must now include: `priority: str`, `tags: list[str]`\n- All input validation:\n  - Priority must be one of \"high\", \"medium\", \"low\" (case-insensitive)\n  - Tags must not contain empty strings after processing\n- Friendly error messages for invalid inputs\n- Console output remains clean, aligned, and easy to read\n- No persistence required\n- Performance: instant response even with 100+ tasks\n\n### Out of Scope for Phase I Intermediate\n- Due dates (reserved for Advanced Level)\n- Combining multiple filters\n- Persistent filter/sort across app restarts\n- Colored terminal output (optional bonus only)\n\nThis specification defines ONLY the Intermediate Level additions for the Phase I console application."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Task Prioritization (Priority: P1)

As a user, I want to assign a priority level (high, medium, low) to tasks so I can identify urgent items quickly.

**Why this priority**: Prioritizing tasks is fundamental to task management and allows users to focus on the most important items first, which is a core requirement for effective task management.

**Independent Test**: Can be fully tested by adding tasks with different priority levels and verifying that the priority is displayed when listing tasks, delivering the value of quickly identifying important tasks.

**Acceptance Scenarios**:

1. **Given** user wants to add a new task, **When** user specifies a priority level during the add command, **Then** the task is created with the specified priority and displayed with its priority level
2. **Given** user has tasks with different priorities, **When** user lists all tasks, **Then** each task shows its priority level clearly in the display
3. **Given** user adds a task without specifying priority, **When** task is created, **Then** the task gets a default "medium" priority

---

### User Story 2 - Task Tagging (Priority: P1)

As a user, I want to tag tasks with descriptive keywords so I can categorize and group them for better organization.

**Why this priority**: Tagging allows users to organize tasks by category, project, or context, which is essential for managing multiple types of tasks efficiently.

**Independent Test**: Can be fully tested by adding tasks with tags and verifying that tags are displayed when listing tasks, delivering the value of categorizing tasks.

**Acceptance Scenarios**:

1. **Given** user wants to add a new task, **When** user specifies tags during the add command, **Then** the task is created with the specified tags and displayed with its tags
2. **Given** user has tasks with different tags, **When** user lists all tasks, **Then** each task shows its associated tags clearly in the display
3. **Given** user adds a task without specifying tags, **When** task is created, **Then** the task has an empty tags list

---

### User Story 3 - Filter Tasks (Priority: P2)

As a user, I want to filter tasks by status, priority, or tags so I can focus on specific subsets of my tasks.

**Why this priority**: Filtering is crucial for managing large task lists and allows users to focus on relevant tasks based on their current needs.

**Independent Test**: Can be fully tested by creating tasks with different attributes and applying various filters, delivering the value of quickly finding specific tasks.

**Acceptance Scenarios**:

1. **Given** user has tasks with various statuses, **When** user applies a status filter (pending/completed), **Then** only tasks matching the status are displayed with a message showing the count
2. **Given** user has tasks with various priorities, **When** user applies a priority filter (high/medium/low), **Then** only tasks matching the priority are displayed with a message showing the count
3. **Given** user has tasks with various tags, **When** user applies a tag filter, **Then** only tasks containing the specified tag are displayed with a message showing the count

---

### User Story 4 - Sort Tasks (Priority: P2)

As a user, I want to reorder the task list by different criteria (creation time, title, priority) to suit my current needs.

**Why this priority**: Sorting allows users to organize their task list in ways that make sense for their workflow, improving productivity and task visibility.

**Independent Test**: Can be fully tested by creating tasks and applying different sort orders, delivering the value of organizing tasks in a preferred sequence.

**Acceptance Scenarios**:

1. **Given** user has multiple tasks, **When** user applies a sort command (by creation time, title, or priority), **Then** the tasks are displayed in the specified order
2. **Given** user has sorted tasks, **When** user adds a new task, **Then** the new task is added to the appropriate position based on current sort order or the sort is maintained as per application behavior

---

### User Story 5 - Clear Filters and Sorts (Priority: P3)

As a user, I want to clear active filters and sorts so I can return to viewing all tasks in their default order.

**Why this priority**: Clearing filters and sorts provides a way to reset the view and see all tasks again, which is important for usability.

**Independent Test**: Can be fully tested by applying filters/sorts and then clearing them, delivering the value of returning to the default view.

**Acceptance Scenarios**:

1. **Given** user has applied filters or sorts, **When** user runs the clear command, **Then** all filters are cleared and tasks are displayed in their default order

---

### Edge Cases

- What happens when a user enters an invalid priority value (not high/medium/low)?
- How does the system handle empty tags or tags with only whitespace?
- What happens when a user tries to filter by a tag that doesn't exist in any tasks?
- How does the system handle case sensitivity in priority values?
- What happens when the task list is empty and a user tries to apply filters or sorts?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add tasks with priority levels (high, medium, low)
- **FR-002**: System MUST assign a default "medium" priority to tasks when none is specified
- **FR-003**: System MUST allow users to add tasks with tags (list of strings)
- **FR-004**: System MUST display task priorities and tags when listing tasks
- **FR-005**: System MUST provide a filter command that can filter by status (pending/completed)
- **FR-006**: System MUST provide a filter command that can filter by priority (high/medium/low)
- **FR-007**: System MUST provide a filter command that can filter by tags
- **FR-008**: System MUST provide a filter clear command to remove active filters
- **FR-009**: System MUST provide a sort command that can sort by creation time (ascending/descending)
- **FR-010**: System MUST provide a sort command that can sort by title (ascending/descending)
- **FR-011**: System MUST provide a sort command that can sort by priority (ascending/descending)
- **FR-012**: System MUST validate priority values and reject invalid inputs with a friendly error message
- **FR-013**: System MUST validate tags and remove empty strings from tag lists
- **FR-014**: System MUST show a message indicating how many tasks are displayed after applying filters
- **FR-015**: System MUST ensure that the list command respects active filters and sorts

### Key Entities *(include if feature involves data)*

- **Task**: Represents a single task with attributes: id, title, status (pending/completed), priority (high/medium/low), tags (list of strings), creation timestamp
- **Filter**: Represents a filtering criterion that can be applied to task lists based on status, priority, or tags
- **Sort**: Represents a sorting criterion that determines the order of tasks in the display

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add tasks with priority levels and tags in under 30 seconds
- **SC-002**: Users can successfully filter tasks by status, priority, or tags with 100% accuracy
- **SC-003**: Users can successfully sort tasks by creation time, title, or priority with 100% accuracy
- **SC-004**: Users can clear filters and return to default view in under 10 seconds
- **SC-005**: 95% of user inputs with invalid priority values are rejected with clear error messages
- **SC-006**: All commands maintain responsive performance with task lists containing up to 100 tasks
