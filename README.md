# In-Memory Todo CLI App

A simple command-line Todo list application in Python that stores tasks entirely in memory (no persistence to disk).

## Features

- Add new tasks with unique IDs and pending status
- View all tasks with formatted output showing ID, title, and status
- Update existing task descriptions while preserving other attributes
- Delete tasks by ID
- Mark tasks as complete with visual status indicators
- Comprehensive error handling and input validation
- File-based storage for persistent task management (data saved between sessions)

## Prerequisites

- Python 3.13+
- UV package manager

## Setup

1. Clone or download the repository
2. Ensure you have Python 3.13+ installed: `python --version`
3. Install UV package manager: `pip install uv`
4. Create virtual environment: `uv venv`
5. Activate the virtual environment: `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\activate` (Windows)
6. Install dependencies: `uv pip install -e .`

## Usage

```bash
# Add a new task
python src/main.py add "Buy groceries"

# List all tasks
python src/main.py list

# Update a task
python src/main.py update 1 "Buy organic groceries"

# Mark a task as complete
python src/main.py complete 1

# Delete a task
python src/main.py delete 1

# Show help
python src/main.py --help
```

## Commands

- `add "<description>"` - Add a new task with a description
- `list` - Show all tasks with ID, status indicator, and title
- `update <id> "<new description>"` - Update task description by ID
- `complete <id>` - Mark task as completed by ID
- `delete <id>` - Remove task by ID

## Examples

```bash
# Add multiple tasks
python src/main.py add "Buy groceries"
python src/main.py add "Walk the dog"
python src/main.py add "Finish report"

# View all tasks
python src/main.py list
# Output:
# [○] 1: Buy groceries
# [○] 2: Walk the dog
# [○] 3: Finish report

# Mark a task as complete
python src/main.py complete 2

# View tasks again to see the completed status
python src/main.py list
# Output:
# [○] 1: Buy groceries
# [✓] 2: Walk the dog
# [○] 3: Finish report

# Update a task
python src/main.py update 3 "Finish project report"

# Delete a task
python src/main.py delete 1
```

## Error Handling

The application provides user-friendly error messages for various scenarios:

- Empty task descriptions: "Error: Task description cannot be empty"
- Non-existent task IDs: "Error: Task with ID X not found"
- Invalid command syntax: Shows help with available commands
- Very long task descriptions (over 1000 characters): "Error: Task description is too long (maximum 1000 characters)"

## Architecture

- `src/main.py`: CLI entry point and command handlers
- `src/models.py`: Task data model definition
- `src/storage.py`: In-memory storage manager with all CRUD operations
- Tasks are persisted in tasks.json file between runs

## Performance

- All commands execute under 1 second
- Efficient in-memory storage using Python dictionaries
- Optimized for up to 100+ tasks in memory