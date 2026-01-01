"""
Main entry point for the Todo CLI application.
"""
import argparse
import sys
from pathlib import Path

# Add the src directory to the path so we can import modules
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path))

from storage import TaskManager


def add_task(task_manager: TaskManager, args: list):
    """Handle the add command to create a new task."""
    if not args:
        print("Error: Task description cannot be empty")
        return

    title = " ".join(args)
    if not title.strip():
        print("Error: Task description cannot be empty")
        return

    # Validate task description length
    if len(title) > 1000:  # Set a reasonable limit for task descriptions
        print("Error: Task description is too long (maximum 1000 characters)")
        return

    try:
        task = task_manager.add_task(title.strip())
        print(f"Task {task.id} added successfully: {task.title}")
    except ValueError as e:
        print(f"Error: {e}")


def list_tasks(task_manager: TaskManager):
    """Handle the list command to display all tasks."""
    tasks = task_manager.list_tasks()

    if not tasks:
        print("No tasks found")
        return

    # Format and print tasks
    for task in tasks:
        status_indicator = "X" if task.status == "completed" else "O"
        print(f"[{status_indicator}] {task.id}: {task.title}")


def mark_complete(task_manager: TaskManager, task_id: int):
    """Handle the complete command to mark a task as completed."""
    try:
        task = task_manager.mark_complete(task_id)
        if task:
            print(f"Task {task.id} marked as completed: {task.title}")
        else:
            print(f"Error: Task with ID {task_id} not found")
    except ValueError as e:
        print(f"Error: {e}")


def update_task(task_manager: TaskManager, task_id: int, args: list):
    """Handle the update command to modify a task's description."""
    # Join the title arguments and check if it's empty
    new_title = " ".join(args) if args else ""

    if not new_title.strip():
        print("Error: Task description cannot be empty")
        return

    # Validate task description length
    if len(new_title) > 1000:  # Set a reasonable limit for task descriptions
        print("Error: Task description is too long (maximum 1000 characters)")
        return

    try:
        task = task_manager.update_task(task_id, new_title.strip())
        if task:
            print(f"Task {task.id} updated successfully: {task.title}")
        else:
            print(f"Error: Task with ID {task_id} not found")
    except ValueError as e:
        print(f"Error: {e}")


def delete_task(task_manager: TaskManager, task_id: int):
    """Handle the delete command to remove a task."""
    try:
        success = task_manager.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Error: Task with ID {task_id} not found")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description="Todo CLI Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", nargs="*", help="Task description")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("title", nargs="*", help="New task description")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("id", type=int, help="Task ID")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    try:
        args = parser.parse_args()
    except SystemExit:
        # argparse calls sys.exit() when there's an argument error, so we catch it
        # and return a more user-friendly message
        return

    # Initialize task manager with file-based storage
    task_manager = TaskManager("tasks.json")

    if args.command == "add":
        add_task(task_manager, args.title)
    elif args.command == "list":
        list_tasks(task_manager)
    elif args.command == "update":
        update_task(task_manager, args.id, args.title)
    elif args.command == "complete":
        mark_complete(task_manager, args.id)
    elif args.command == "delete":
        delete_task(task_manager, args.id)
    elif args.command is None:
        print("Error: No command provided. Use 'add', 'list', 'update', 'complete', or 'delete'.")
        parser.print_help()
    else:
        print(f"Error: Unknown command '{args.command}'. Use 'add', 'list', 'update', 'complete', or 'delete'.")
        parser.print_help()


if __name__ == "__main__":
    main()