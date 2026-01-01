# CLI Interface Contract: In-Memory Todo CLI App

## Command Structure
```
python todo.py <command> [arguments]
```

## Commands

### Add Command
- **Syntax**: `python todo.py add "<task description>"`
- **Purpose**: Add a new task to the todo list
- **Arguments**:
  - task description (required, string)
- **Success Response**: Task added with new ID and "pending" status
- **Error Responses**:
  - Empty description: "Error: Task description cannot be empty"
  - Invalid syntax: Help message displayed

### List Command
- **Syntax**: `python todo.py list`
- **Purpose**: Display all tasks with ID, title, and status
- **Arguments**: None
- **Success Response**: Formatted list of all tasks
- **Error Responses**: "No tasks found" when list is empty

### Update Command
- **Syntax**: `python todo.py update <task_id> "<new description>"`
- **Purpose**: Update the description of an existing task
- **Arguments**:
  - task_id (required, integer)
  - new description (required, string)
- **Success Response**: Task updated successfully
- **Error Responses**:
  - Invalid ID: "Error: Task with ID <id> not found"
  - Empty description: "Error: Task description cannot be empty"

### Complete Command
- **Syntax**: `python todo.py complete <task_id>`
- **Purpose**: Mark a task as completed
- **Arguments**:
  - task_id (required, integer)
- **Success Response**: Task marked as completed
- **Error Responses**:
  - Invalid ID: "Error: Task with ID <id> not found"

### Delete Command
- **Syntax**: `python todo.py delete <task_id>`
- **Purpose**: Remove a task from the list
- **Arguments**:
  - task_id (required, integer)
- **Success Response**: Task deleted successfully
- **Error Responses**:
  - Invalid ID: "Error: Task with ID <id> not found"