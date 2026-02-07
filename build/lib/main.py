"""
Main entry point for the todo app.
Contains the command dispatcher and main execution logic.
"""
import sys
from .commands import add_task, update_task, list_tasks, filter_command, filter_clear, sort_command, sort_clear, clear_all, delete_task, toggle_task_completion
from .display import print_help


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [command] [args...]")
        print_help()
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

    elif command == "clear":
        if len(sys.argv) < 3:
            # Clear both filters and sorts by default
            clear_all()
        else:
            subcommand = sys.argv[2].lower()
            if subcommand == "filter" or subcommand == "filters":
                filter_clear()
            elif subcommand == "sort" or subcommand == "sorts":
                sort_clear()
            elif subcommand == "all":
                clear_all()
            else:
                print("Usage: python main.py clear [filter|sort|all]")
                return

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python main.py delete id")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number")
            return

        delete_task(task_id)

    elif command == "complete":
        if len(sys.argv) < 3:
            print("Usage: python main.py complete id")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number")
            return

        toggle_task_completion(task_id)

    elif command == "help":
        print_help()

    else:
        print(f"Unknown command: {command}")
        print_help()


if __name__ == "__main__":
    main()