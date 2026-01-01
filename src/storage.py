"""
File-based storage manager for the Todo CLI application.
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from models import Task


class TaskManager:
    """Manages file-based storage of tasks."""

    def __init__(self, storage_file="tasks.json"):
        """Initialize the task manager with file-based storage."""
        self.storage_file = storage_file
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the storage file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._tasks = {}
                    for task_data in data.get('tasks', []):
                        # Convert datetime string back to datetime object
                        task_data['created_at'] = datetime.fromisoformat(task_data['created_at'])
                        task = Task(**task_data)
                        self._tasks[task.id] = task

                    # Set the next_id based on the highest ID found
                    if self._tasks:
                        self._next_id = max(self._tasks.keys()) + 1
                    else:
                        self._next_id = 1
            except (json.JSONDecodeError, KeyError, ValueError):
                # If there's an error loading the file, start with empty storage
                self._tasks = {}
                self._next_id = 1
        else:
            # If file doesn't exist, start with empty storage
            self._tasks = {}
            self._next_id = 1

    def save_tasks(self):
        """Save tasks to the storage file."""
        tasks_data = []
        for task in self._tasks.values():
            task_dict = task.__dict__.copy()
            # Convert datetime to ISO format string for JSON serialization
            task_dict['created_at'] = task.created_at.isoformat()
            tasks_data.append(task_dict)

        data = {
            'tasks': tasks_data
        }

        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_task(self, title: str) -> Task:
        """
        Add a new task with the given title.

        Args:
            title: The title/description of the task

        Returns:
            The newly created Task object

        Raises:
            ValueError: If title is empty, None, or too long
        """
        if not title or not isinstance(title, str):
            raise ValueError("Task title must be a non-empty string")

        # Validate task description length
        if len(title) > 1000:  # Set a reasonable limit for task descriptions
            raise ValueError("Task description is too long (maximum 1000 characters)")

        task = Task(
            id=self._next_id,
            title=title,
            status='pending',
            created_at=datetime.now()
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        self.save_tasks()  # Save after adding
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None) -> Optional[Task]:
        """
        Update a task's title by its ID.

        Args:
            task_id: The ID of the task to update
            title: The new title for the task (optional)

        Returns:
            The updated Task object if successful, None if task not found
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if title is not None:
            if not title or not isinstance(title, str):
                raise ValueError("Task title must be a non-empty string")

            # Validate task description length
            if len(title) > 1000:  # Set a reasonable limit for task descriptions
                raise ValueError("Task description is too long (maximum 1000 characters)")

        task = self._tasks.get(task_id)
        if task is None:
            return None

        if title is not None:
            task.title = title
        self.save_tasks()  # Save after updating
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if task_id in self._tasks:
            del self._tasks[task_id]
            self.save_tasks()  # Save after deletion
            return True
        return False

    def list_tasks(self) -> List[Task]:
        """
        List all tasks.

        Returns:
            A list of all Task objects
        """
        return list(self._tasks.values())

    def mark_complete(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as completed by its ID.

        Args:
            task_id: The ID of the task to mark as completed

        Returns:
            The updated Task object if successful, None if task not found
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self._tasks.get(task_id)
        if task is None:
            return None

        task.status = 'completed'
        self.save_tasks()  # Save after marking complete
        return task