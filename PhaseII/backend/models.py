from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
import uuid


class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    user_id: str = Field(foreign_key="user.id")  # Note: SQLModel uses lowercase table names by default


class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to user (if we had a User model)
    # user: "User" = Relationship(back_populates="tasks")


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    name: str


class User(UserBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship to tasks (if we had a Task model)
    # tasks: List["Task"] = Relationship(back_populates="user")