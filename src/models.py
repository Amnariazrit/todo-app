"""
Data models for the Todo CLI application.
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """Represents a single todo item."""
    id: int
    title: str
    status: str  # 'pending' or 'completed'
    created_at: datetime

    def __post_init__(self):
        """Validate the task attributes after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not self.title or not isinstance(self.title, str):
            raise ValueError("Task title must be a non-empty string")

        if self.status not in ['pending', 'completed']:
            raise ValueError("Task status must be either 'pending' or 'completed'")

        if not isinstance(self.created_at, datetime):
            raise ValueError("Task created_at must be a datetime object")