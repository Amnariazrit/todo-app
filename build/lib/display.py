"""
Display functions for the todo app.
Contains functions for formatting and printing tasks.
"""
from typing import List
from .models import Task


def format_task_line(task: Task) -> str:
    """Format a task as a single line for display.

    Args:
        task: Task object to format

    Returns:
        Formatted string representation of the task
    """
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

    return f"{id_str} {title_str} {priority_indicator:<7} {tags_str:<20} {status:<12}"


def print_tasks(task_list: List[Task]):
    """Print a formatted list of tasks.

    Args:
        task_list: List of Task objects to display
    """
    if not task_list:
        print("No tasks to display.")
        return

    print("-" * 80)
    print(f"{'ID':<4} {'Title':<30} {'Prio':<7} {'Tags':<20} {'Status':<12}")
    print("-" * 80)

    for task in task_list:
        print(format_task_line(task))

    print("-" * 80)


def print_welcome_message():
    """Print a welcome message for the application."""
    print("=" * 50)
    print("Welcome to the Todo App with Priority & Tags!")
    print("=" * 50)


def print_help():
    """Print help information for available commands.

    Displays usage information for all available commands in the todo app.
    """
    print("Available commands:")
    print("  add 'title' ['description'] ['priority'] ['tags']")
    print("  update id ['title'] ['description'] ['priority'] ['tags']")
    print("  delete id")
    print("  complete id")
    print("  list")
    print("  filter [status|priority|tag] [value]")
    print("  filter clear")
    print("  sort [created|created_desc|title|title_desc|priority|priority_rev]")
    print("  clear [filter|sort|all]")
    print("  help")