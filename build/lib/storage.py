"""
Persistent storage module for the todo app.
Contains global state variables for tasks and filters with file persistence.
"""
from typing import List, Dict, Optional
from .models import Task
import json
import os
from datetime import datetime

# Global tasks list
tasks: List[Task] = []

# Current filter (e.g., {"type": "priority", "value": "high"})
current_filter: Optional[Dict] = None

# Current sort criteria (default: "created")
current_sort: str = "created"

# File path for persistence
TASKS_FILE = "tasks.json"

def save_tasks_to_file():
    """Save tasks to a JSON file."""
    tasks_data = []
    for task in tasks:
        task_dict = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'priority': task.priority,
            'tags': task.tags,
            'created_at': task.created_at.isoformat() if hasattr(task, 'created_at') and task.created_at else datetime.now().isoformat()
        }
        tasks_data.append(task_dict)

    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks_data, f, indent=2)

def load_tasks_from_file():
    """Load tasks from a JSON file."""
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                tasks_data = json.load(f)

            tasks = []
            for task_data in tasks_data:
                # Create task manually since we need to handle datetime
                task = Task(
                    id=task_data['id'],
                    title=task_data['title'],
                    description=task_data['description'],
                    completed=task_data.get('completed', False),
                    priority=task_data.get('priority', 'medium'),
                    tags=task_data.get('tags', [])
                )

                # Handle datetime separately
                if 'created_at' in task_data:
                    from datetime import datetime
                    task.created_at = datetime.fromisoformat(task_data['created_at'])

                tasks.append(task)
        except Exception as e:
            print(f"Error loading tasks from file: {e}")
            tasks = []
    else:
        tasks = []

# Load tasks when module is imported
load_tasks_from_file()