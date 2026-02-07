"""
Data models for the Todo CLI application.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List


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

        # Normalize and validate priority - defaults to 'medium' if invalid
        if self.priority:
            normalized_priority = self.priority.lower().strip()
            if normalized_priority in ['high', 'medium', 'low']:
                self.priority = normalized_priority
            else:
                self.priority = 'medium'  # default value
        else:
            self.priority = 'medium'  # default value

        if self.tags is None:
            self.tags = []
        elif not isinstance(self.tags, list):
            raise ValueError("Task tags must be a list of strings")

        if self.created_at is None:
            from datetime import datetime
            self.created_at = datetime.now()