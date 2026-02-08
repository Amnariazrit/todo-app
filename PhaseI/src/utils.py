"""
Utility functions for the todo app.
Contains helper functions for validation, filtering, and sorting.
"""
from typing import List, Dict, Optional, Callable
from datetime import datetime
from .storage import tasks, current_filter, current_sort
from .models import Task


def validate_priority(input_str: str) -> str:
    """Validate and normalize priority input.

    Args:
        input_str: Priority string to validate

    Returns:
        Normalized priority string ('high', 'medium', 'low')
        Defaults to 'medium' if input is invalid
    """
    priority = input_str.lower().strip()
    if priority in {"high", "medium", "low"}:
        return priority
    return "medium"  # default


def parse_tags(input_str: str) -> List[str]:
    """Parse and normalize tag input.

    Args:
        input_str: Comma-separated tags string

    Returns:
        List of normalized, unique tags (lowercase, no duplicates)
    """
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


def get_visible_tasks() -> List[Task]:
    """Get tasks applying current filter and sort settings.

    Returns:
        List of tasks that match current filter criteria, sorted by current sort criteria
    """
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
    """Apply a filter to the task list.

    Args:
        filter_type: Type of filter ('status', 'priority', 'tag')
        value: Value to filter by
    """
    global current_filter
    if filter_type in ["status", "priority", "tag"]:
        current_filter = {"type": filter_type, "value": value.lower()}


def clear_filter():
    """Clear the current filter.

    Removes any active filter, showing all tasks.
    """
    global current_filter
    current_filter = None


def set_sort(criteria: str):
    """Set the current sort criteria.

    Args:
        criteria: Sort criteria to apply
    """
    global current_sort
    if criteria in SORT_CONFIG:
        current_sort = criteria


def clear_sort():
    """Clear the current sort back to default.

    Resets the sort order to the default (creation order).
    """
    global current_sort
    current_sort = "created"


# Sorting configuration
SORT_CONFIG = {
    "created":       (lambda t: t.created_at, False),
    "created_desc":  (lambda t: t.created_at, True),
    "title":         (lambda t: t.title.lower(), False),
    "title_desc":    (lambda t: t.title.lower(), True),
    "priority":      (lambda t: ["high", "medium", "low"].index(t.priority), False),
    "priority_rev":  (lambda t: ["low", "medium", "high"].index(t.priority), False),
}