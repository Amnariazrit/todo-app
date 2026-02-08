from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    title: str  # Required field


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskRead(TaskBase):
    id: int
    user_id: str
    created_at: datetime
    updated_at: datetime


class TaskList(BaseModel):
    tasks: List[TaskRead]
    total_count: int


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    email: str
    name: str
    password: str  # Add password field


class UserRead(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserRead


class TokenData(BaseModel):
    userId: Optional[str] = None