"""
Command functions for the todo app.
Contains all command implementations for add, update, list, filter, sort, etc.
"""
from typing import List
from .storage import tasks, current_filter, current_sort
from .models import Task
from .utils import get_visible_tasks, apply_filter, clear_filter, clear_sort, set_sort, validate_priority, parse_tags
from .display import print_tasks


def add_task(title: str, description: str = "", priority: str = "medium", tags: str = ""):
    """Add a new task with priority and tags.

    Args:
        title: The task title (required, cannot be empty)
        description: Optional description of the task
        priority: Priority level ('high', 'medium', 'low'), defaults to 'medium'
        tags: Comma-separated tags as a string
    """
    # Validate and normalize inputs
    if not title or not title.strip():
        print("Error: Task title cannot be empty.")
        return

    priority = validate_priority(priority)
    tag_list = parse_tags(tags)

    # Create new task with next available ID
    new_id = max([t.id for t in tasks], default=0) + 1
    try:
        new_task = Task(
            id=new_id,
            title=title.strip(),
            description=description.strip() if description else "",
            priority=priority,
            tags=tag_list
        )
        tasks.append(new_task)
        print(f"Task {new_id} added successfully with priority '{priority}' and {len(tag_list)} tags.")
    except ValueError as e:
        print(f"Error creating task: {e}")


def update_task(task_id: int, title: str = None, description: str = None,
                priority: str = None, tags: str = None):
    """Update an existing task.

    Args:
        task_id: ID of the task to update (must be positive integer)
        title: New title for the task (optional, cannot be empty if provided)
        description: New description for the task (optional)
        priority: New priority level (optional)
        tags: New tags as comma-separated string (optional)
    """
    if task_id <= 0:
        print("Error: Task ID must be a positive integer.")
        return

    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        print(f"Task {task_id} not found.")
        return

    # Update fields if provided
    if title is not None:
        if title.strip():
            task.title = title.strip()
        else:
            print("Error: Task title cannot be empty.")
            return
    if description is not None:
        task.description = description.strip() if description else ""
    if priority is not None:
        task.priority = validate_priority(priority)
    if tags is not None:
        task.tags = parse_tags(tags)

    print(f"Task {task_id} updated successfully.")


def list_tasks():
    """List tasks applying current filter and sort settings.

    Displays tasks based on active filters and sorts, with status messages
    indicating which filters/sorts are currently active.
    """
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
        print(f"Showing {len(visible_tasks)} tasks (all tasks, default order)")

    print_tasks(visible_tasks)


def filter_command(filter_type: str, value: str):
    """Apply a filter to the task list.

    Args:
        filter_type: Type of filter ('status', 'priority', 'tag')
        value: Value to filter by (e.g., 'pending', 'high', 'work')
    """
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
    """Clear the current filter.

    Removes any active filter and shows all tasks again.
    """
    clear_filter()
    print("Filter cleared. Showing all tasks.")


def sort_clear():
    """Clear the current sort.

    Resets the sort order back to the default (creation order).
    """
    clear_sort()
    print("Sort cleared. Tasks displayed in default order.")


def clear_all():
    """Clear both filters and sorts.

    Removes any active filters and resets sort order to default.
    """
    clear_filter()
    clear_sort()
    print("Filters and sorts cleared. Showing all tasks in default order.")


def sort_command(criteria: str):
    """Set the sort criteria.

    Args:
        criteria: Sort criteria ('created', 'created_desc', 'title', 'title_desc',
                 'priority', 'priority_rev')
    """
    valid_criteria = ["created", "created_desc", "title", "title_desc", "priority", "priority_rev"]
    if criteria not in valid_criteria:
        print(f"Invalid sort criteria. Use: {', '.join(valid_criteria)}")
        return

    set_sort(criteria)
    visible_tasks = get_visible_tasks()
    print(f"Sort set to: {criteria}. Showing {len(visible_tasks)} tasks.")