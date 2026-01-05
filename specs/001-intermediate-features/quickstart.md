# Quickstart Guide: Intermediate Level Features

## Overview
This guide provides instructions for implementing the intermediate level features for the in-memory Python console todo app, including priorities, tags, filtering, and sorting.

## Implementation Steps

### 1. Update Task Class (`src/task.py`)
```python
from datetime import datetime
from typing import List, Optional

class Task:
    def __init__(
        self,
        id: int,
        title: str,
        description: str = "",
        completed: bool = False,
        priority: str = "medium",
        tags: List[str] = None,
        created_at = None
    ):
        self.id = id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.completed = completed
        self.priority = priority.lower().strip() if priority else "medium"
        if self.priority not in {"high", "medium", "low"}:
            self.priority = "medium"
        self.tags = (
            [tag.strip().lower() for tag in tags if tag.strip()]
            if tags
            else []
        )
        self.created_at = created_at or datetime.now()
```

### 2. Set Up Global State (`src/storage.py`)
```python
from typing import List, Dict, Optional
from .task import Task

tasks: List[Task] = []
current_filter: Optional[Dict] = None
current_sort: str = "created"
```

### 3. Create Helper Functions (`src/utils.py`)
```python
from typing import List, Dict, Optional, Callable
from datetime import datetime
from .storage import tasks, current_filter, current_sort
from .task import Task

def get_visible_tasks() -> List[Task]:
    """Get tasks applying current filter and sort settings."""
    filtered_tasks = tasks

    # Apply filter if active
    if current_filter:
        filter_type = current_filter["type"]
        filter_value = current_filter["value"]

        if filter_type == "status":
            if filter_value == "pending":
                filtered_tasks = [t for t in filtered_tasks if not t.completed]
            elif filter_value == "completed":
                filtered_tasks = [t for t in filtered_tasks if t.completed]
        elif filter_type == "priority":
            filtered_tasks = [t for t in filtered_tasks if t.priority == filter_value]
        elif filter_type == "tag":
            filtered_tasks = [t for t in filtered_tasks if filter_value in t.tags]

    # Apply sort
    sort_key, reverse = SORT_CONFIG.get(current_sort, SORT_CONFIG["created"])
    sorted_tasks = sorted(filtered_tasks, key=sort_key, reverse=reverse)

    return sorted_tasks

def apply_filter(filter_type: str, value: str):
    """Apply a filter to the task list."""
    global current_filter
    if filter_type in ["status", "priority", "tag"]:
        current_filter = {"type": filter_type, "value": value.lower()}

def clear_filter():
    """Clear the current filter."""
    global current_filter
    current_filter = None

def set_sort(criteria: str):
    """Set the current sort criteria."""
    global current_sort
    if criteria in SORT_CONFIG:
        current_sort = criteria

def validate_priority(input_str: str) -> str:
    """Validate and normalize priority input."""
    priority = input_str.lower().strip()
    if priority in {"high", "medium", "low"}:
        return priority
    return "medium"  # default

def parse_tags(input_str: str) -> List[str]:
    """Parse and normalize tag input."""
    if not input_str:
        return []
    # Split by comma and normalize
    tags = [tag.strip().lower() for tag in input_str.split(",") if tag.strip()]
    # Remove duplicates while preserving order
    unique_tags = []
    for tag in tags:
        if tag not in unique_tags:
            unique_tags.append(tag)
    return unique_tags

# Sorting configuration
SORT_CONFIG = {
    "created":       (lambda t: t.created_at, False),
    "created_desc":  (lambda t: t.created_at, True),
    "title":         (lambda t: t.title.lower(), False),
    "title_desc":    (lambda t: t.title.lower(), True),
    "priority":      (lambda t: ["high", "medium", "low"].index(t.priority), False),
    "priority_rev":  (lambda t: ["low", "medium", "high"].index(t.priority), False),
}
```

### 4. Update Commands (`src/commands.py`)
```python
from typing import List
from .storage import tasks, current_filter, current_sort
from .task import Task
from .utils import get_visible_tasks, apply_filter, clear_filter, set_sort, validate_priority, parse_tags
from .display import print_tasks

def add_task(title: str, description: str = "", priority: str = "medium", tags: str = ""):
    """Add a new task with priority and tags."""
    # Validate and normalize inputs
    priority = validate_priority(priority)
    tag_list = parse_tags(tags)

    # Create new task with next available ID
    new_id = max([t.id for t in tasks], default=0) + 1
    new_task = Task(
        id=new_id,
        title=title,
        description=description,
        priority=priority,
        tags=tag_list
    )
    tasks.append(new_task)
    print(f"Task {new_id} added successfully with priority '{priority}' and {len(tag_list)} tags.")

def update_task(task_id: int, title: str = None, description: str = None,
                priority: str = None, tags: str = None):
    """Update an existing task."""
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        print(f"Task {task_id} not found.")
        return

    if title is not None:
        task.title = title.strip()
    if description is not None:
        task.description = description.strip()
    if priority is not None:
        task.priority = validate_priority(priority)
    if tags is not None:
        task.tags = parse_tags(tags)

    print(f"Task {task_id} updated successfully.")

def list_tasks():
    """List tasks applying current filter and sort settings."""
    visible_tasks = get_visible_tasks()

    # Show filter/sort status message
    status_parts = []
    if current_filter:
        ftype = current_filter["type"]
        fvalue = current_filter["value"]
        status_parts.append(f"filtered by {ftype}: {fvalue}")
    if current_sort != "created":
        status_parts.append(f"sorted by {current_sort}")

    if status_parts:
        status_msg = ", ".join(status_parts)
        print(f"Showing {len(visible_tasks)} tasks ({status_msg})")
    else:
        print(f"Showing {len(visible_tasks)} tasks")

    print_tasks(visible_tasks)

def filter_command(filter_type: str, value: str):
    """Apply a filter to the task list."""
    if filter_type not in ["status", "priority", "tag"]:
        print("Invalid filter type. Use: status, priority, or tag")
        return

    if filter_type == "status" and value not in ["pending", "completed"]:
        print("Invalid status value. Use: pending or completed")
        return
    elif filter_type == "priority" and value not in ["high", "medium", "low"]:
        print("Invalid priority value. Use: high, medium, or low")
        return

    apply_filter(filter_type, value)
    visible_tasks = get_visible_tasks()
    print(f"Filter applied: {filter_type} = {value}. Showing {len(visible_tasks)} tasks.")

def filter_clear():
    """Clear the current filter."""
    clear_filter()
    print("Filter cleared. Showing all tasks.")

def sort_command(criteria: str):
    """Set the sort criteria."""
    valid_criteria = ["created", "created_desc", "title", "title_desc", "priority", "priority_rev"]
    if criteria not in valid_criteria:
        print(f"Invalid sort criteria. Use: {', '.join(valid_criteria)}")
        return

    set_sort(criteria)
    visible_tasks = get_visible_tasks()
    print(f"Sort set to: {criteria}. Showing {len(visible_tasks)} tasks.")
```

### 5. Update Display (`src/display.py`)
```python
from typing import List
from .task import Task

def format_task_line(task: Task) -> str:
    """Format a task as a single line for display."""
    # Format priority indicator
    priority_map = {"high": "[HIGH]", "medium": "[MED]", "low": "[LOW]"}
    priority_indicator = priority_map[task.priority]

    # Format tags (show up to 4, then +N more)
    if len(task.tags) == 0:
        tags_str = ""
    elif len(task.tags) <= 4:
        tags_str = f"[{', '.join(task.tags)}]"
    else:
        shown_tags = ', '.join(task.tags[:4])
        extra_count = len(task.tags) - 4
        tags_str = f"[{shown_tags}, +{extra_count} more]"

    # Format status
    status = "Complete" if task.completed else "Incomplete"

    # Format the line with fixed-width columns
    id_str = f"{task.id:3d}"
    title_str = task.title[:25] + "..." if len(task.title) > 25 else task.title
    title_str = f"{title_str:<28}"

    return f"{id_str} {title_str} {priority_indicator} {tags_str:<20} {status}"

def print_tasks(task_list: List[Task]):
    """Print a formatted list of tasks."""
    if not task_list:
        print("No tasks to display.")
        return

    print("-" * 80)
    print(f"{'ID':<4} {'Title':<30} {'Prio':<7} {'Tags':<20} {'Status'}")
    print("-" * 80)

    for task in task_list:
        print(format_task_line(task))

    print("-" * 80)
```

### 6. Update Main (`src/main.py`)
```python
import sys
from .commands import add_task, update_task, list_tasks, filter_command, filter_clear, sort_command

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [command] [args...]")
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python main.py add 'title' ['description'] ['priority'] ['tags']")
            return

        title = sys.argv[2]
        description = sys.argv[3] if len(sys.argv) > 3 else ""
        priority = sys.argv[4] if len(sys.argv) > 4 else "medium"
        tags = sys.argv[5] if len(sys.argv) > 5 else ""

        add_task(title, description, priority, tags)

    elif command == "update":
        if len(sys.argv) < 3:
            print("Usage: python main.py update id ['title'] ['description'] ['priority'] ['tags']")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number")
            return

        # Extract optional parameters
        title = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] != "None" else None
        description = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] != "None" else None
        priority = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] != "None" else None
        tags = sys.argv[6] if len(sys.argv) > 6 and sys.argv[6] != "None" else None

        update_task(task_id, title, description, priority, tags)

    elif command == "list":
        list_tasks()

    elif command == "filter":
        if len(sys.argv) < 3:
            print("Usage: python main.py filter [status|priority|tag] [value]")
            return

        filter_type = sys.argv[2]
        if len(sys.argv) < 4:
            if filter_type == "clear":
                filter_clear()
            else:
                print("Usage: python main.py filter [status|priority|tag] [value]")
            return

        value = sys.argv[3]
        filter_command(filter_type, value)

    elif command == "sort":
        if len(sys.argv) < 3:
            print("Usage: python main.py sort [created|created_desc|title|title_desc|priority|priority_rev]")
            return

        criteria = sys.argv[2]
        sort_command(criteria)

    else:
        print(f"Unknown command: {command}")
        print("Available commands: add, update, list, filter, sort")

if __name__ == "__main__":
    main()
```

## API Contracts
No formal API contracts needed as this is a console application. Commands follow the patterns described above.

## Testing
To verify implementation:
1. Add tasks with different priorities and tags
2. List tasks to see the new display format
3. Apply filters and verify correct task display
4. Apply sorts and verify correct ordering
5. Clear filters and verify return to default view