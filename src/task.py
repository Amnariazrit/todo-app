"""
Task class for the todo app.
Represents a single task with attributes: id, title, description, status, priority, tags, and creation timestamp.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Task:
    """Represents a single todo item."""
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "medium"  # 'high', 'medium', 'low'
    tags: List[str] = None
    created_at: datetime = None

    def __post_init__(self):
        """Validate the task attributes after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not self.title or not isinstance(self.title, str):
            raise ValueError("Task title must be a non-empty string")

        if self.priority not in ['high', 'medium', 'low']:
            raise ValueError("Task priority must be 'high', 'medium', or 'low'")

        if self.tags is None:
            self.tags = []
        elif not isinstance(self.tags, list):
            raise ValueError("Task tags must be a list of strings")

        if self.created_at is None:
            from datetime import datetime
            self.created_at = datetime.now()