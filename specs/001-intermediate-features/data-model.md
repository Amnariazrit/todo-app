# Data Model: Intermediate Level Features

## Task Entity

### Fields
- **id**: int - Unique identifier for the task
- **title**: str - Task title (required, non-empty when displayed)
- **description**: str - Optional task description (default: "")
- **completed**: bool - Task completion status (default: False)
- **priority**: str - Task priority level, one of {"high", "medium", "low"} (default: "medium")
- **tags**: list[str] - List of tag strings associated with the task (default: [])
- **created_at**: datetime - Timestamp when task was created (default: current time)

### Validation Rules
- **priority**: Must be one of "high", "medium", "low" (case-insensitive, normalized to lowercase)
- **tags**: Must be a list of non-empty strings (empty strings are filtered out, all tags normalized to lowercase)
- **title**: Must be non-empty after stripping whitespace

### State Transitions
- **creation**: When a task is created, it gets a unique ID, title, and default values for other fields
- **completion**: A task can transition from completed=False to completed=True (and vice versa)
- **update**: Any field except ID can be updated via the update command

## Filter Entity

### Fields
- **type**: str - Type of filter ("status", "priority", "tag")
- **value**: str - Value to filter by ("pending"/"completed", "high"/"medium"/"low", tag string)

### Validation Rules
- **type**: Must be one of the supported filter types
- **value**: Must be valid for the given filter type

## Sort Entity

### Fields
- **criteria**: str - Sorting criteria ("created", "created_desc", "title", "title_desc", "priority", "priority_rev")

### Validation Rules
- **criteria**: Must be one of the supported sorting criteria