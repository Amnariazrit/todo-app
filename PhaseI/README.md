# Phase I - Console Todo App

This phase contains the command-line Todo application built with Python.

## Features
- Add new tasks with unique IDs and pending status
- View all tasks with formatted output showing ID, title, and status
- Update existing task descriptions while preserving other attributes
- Delete tasks by ID
- Mark tasks as complete with visual status indicators
- Comprehensive error handling and input validation

## Files
- `main.py` - CLI entry point and command handlers
- `models.py` - Task data model
- `storage.py` - In-memory storage manager
- `commands.py` - Command implementations
- `utils.py` - Utility functions
- `display.py` - Formatting and display functions

## Usage
```bash
python main.py add "Buy groceries"
python main.py list
python main.py update 1 "Buy organic groceries"
python main.py complete 1
python main.py delete 1
```