"""
Storage module for the todo app.
Contains global state variables for tasks and filters.
"""
from typing import List, Dict, Optional
from .models import Task

# Global tasks list
tasks: List[Task] = []

# Current filter (e.g., {"type": "priority", "value": "high"})
current_filter: Optional[Dict] = None

# Current sort criteria (default: "created")
current_sort: str = "created"

# Initialize with some sample tasks for testing
def initialize_sample_tasks():
    """Initialize the tasks list with sample tasks for testing."""
    global tasks
    if not tasks:  # Only initialize if empty
        from datetime import datetime
        sample_task = Task(
            id=1,
            title="Sample task for testing",
            description="This is a sample task to demonstrate the functionality",
            completed=False,
            priority="medium",
            tags=["sample", "test"],
            created_at=datetime.now()
        )
        tasks.append(sample_task)