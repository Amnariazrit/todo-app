# Data Model: In-Memory Todo CLI App

## Task Entity

**Name**: Task
**Description**: Represents a single todo item with ID, title, status, and creation timestamp

**Fields**:
- `id`: int - Unique identifier for the task (primary key)
- `title`: str - Title/description of the task (required)
- `status`: str - Current status of the task ("pending" or "completed")
- `created_at`: datetime - Timestamp when the task was created

**Validation Rules**:
- `id` must be a positive integer
- `title` must not be empty or None
- `status` must be either "pending" or "completed"
- `created_at` must be a valid datetime object

**State Transitions**:
- From "pending" to "completed" when marked complete
- No other state transitions allowed

## Task List Collection

**Name**: Task List
**Description**: Collection of Task entities stored in memory during application runtime

**Operations**:
- Add new task with next sequential ID
- Get task by ID
- Update task by ID
- Delete task by ID
- List all tasks
- Mark task complete by ID

**Constraints**:
- Must maintain sequential ID assignment
- Must not allow duplicate IDs
- Must handle operations on non-existent task IDs gracefully