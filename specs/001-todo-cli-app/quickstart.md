# Quickstart: In-Memory Todo CLI App

## Setup

1. Ensure you have Python 3.13+ installed
2. Install UV package manager if not already installed
3. Clone or create the project directory
4. Navigate to the project root directory
5. Run `uv venv` to create a virtual environment
6. Run `uv pip install -e .` to install the project in development mode

## Usage Examples

### Add a new task
```bash
python src/main.py add "Buy groceries"
```

### List all tasks
```bash
python src/main.py list
```

### Update a task
```bash
python src/main.py update 1 "Buy organic groceries"
```

### Mark a task as complete
```bash
python src/main.py complete 1
```

### Delete a task
```bash
python src/main.py delete 1
```

### Get help
```bash
python src/main.py --help
```

## Project Structure
```
src/
├── main.py          # Entry point and CLI interface
├── models.py        # Task data model
└── storage.py       # In-memory storage manager
```

## Key Components

- **models.py**: Contains the Task dataclass definition
- **storage.py**: Contains the TaskManager class for in-memory operations
- **main.py**: Contains the CLI argument parser and main execution logic