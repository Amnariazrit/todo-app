from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime
import json
import os

# Initialize FastAPI app
app = FastAPI(title="Premium Todo API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class Task(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    priority: str  # low, medium, high
    tags: List[str] = []
    completed: bool = False
    created_at: datetime
    updated_at: datetime
    user_id: str

class User(BaseModel):
    id: str
    email: str
    name: str
    created_at: datetime
    updated_at: datetime
    preferences: dict = {}

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    token: str
    user: User

class RegisterRequest(BaseModel):
    email: str
    password: str
    name: str

class CreateTaskRequest(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str  # low, medium, high
    tags: List[str] = []

class UpdateTaskRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None  # low, medium, high
    tags: Optional[List[str]] = None
    completed: Optional[bool] = None

# In-memory storage (in production, use a database)
tasks_db = []
users_db = []

# Sample user for testing
sample_user = User(
    id=str(uuid.uuid4()),
    email="user@example.com",
    name="Sample User",
    created_at=datetime.now(),
    updated_at=datetime.now(),
    preferences={}
)
users_db.append(sample_user)

# Sample tasks for testing
sample_tasks = [
    Task(
        id=str(uuid.uuid4()),
        title="Complete project proposal",
        description="Finish the proposal document for the new project",
        priority="high",
        tags=["work", "important"],
        completed=False,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        user_id=sample_user.id
    ),
    Task(
        id=str(uuid.uuid4()),
        title="Buy groceries",
        description="Get milk, eggs, bread, and fruits",
        priority="medium",
        tags=["personal"],
        completed=True,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        user_id=sample_user.id
    )
]
tasks_db.extend(sample_tasks)

@app.get("/")
def read_root():
    return {"message": "Premium Todo API", "version": "1.0.0"}

@app.post("/auth/login", response_model=LoginResponse)
def login(request: LoginRequest):
    # Find user by email
    user = next((u for u in users_db if u.email == request.email), None)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # In a real app, you would verify the password here
    # For this example, we'll just return a dummy token
    
    return LoginResponse(
        token=f"dummy_token_for_{user.id}",
        user=user
    )

@app.post("/auth/register", response_model=LoginResponse)
def register(request: RegisterRequest):
    # Check if user already exists
    existing_user = next((u for u in users_db if u.email == request.email), None)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    # Create new user
    new_user = User(
        id=str(uuid.uuid4()),
        email=request.email,
        name=request.name,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        preferences={}
    )
    users_db.append(new_user)
    
    return LoginResponse(
        token=f"dummy_token_for_{new_user.id}",
        user=new_user
    )

@app.get("/tasks", response_model=List[Task])
def get_tasks(user_id: str = "default_user"):
    # In a real app, you would validate the JWT token and extract user_id
    user_tasks = [task for task in tasks_db if task.user_id == user_id]
    return user_tasks

@app.post("/tasks", response_model=Task)
def create_task(request: CreateTaskRequest, user_id: str = "default_user"):
    # In a real app, you would validate the JWT token and extract user_id
    new_task = Task(
        id=str(uuid.uuid4()),
        title=request.title,
        description=request.description,
        priority=request.priority,
        tags=request.tags,
        completed=False,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        user_id=user_id
    )
    tasks_db.append(new_task)
    return new_task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str, user_id: str = "default_user"):
    # In a real app, you would validate the JWT token and extract user_id
    task = next((t for t in tasks_db if t.id == task_id and t.user_id == user_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, request: UpdateTaskRequest, user_id: str = "default_user"):
    # In a real app, you would validate the JWT token and extract user_id
    task_index = next((i for i, t in enumerate(tasks_db) if t.id == task_id and t.user_id == user_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Update the task
    task = tasks_db[task_index]
    update_data = request.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(task, field, value)
    
    task.updated_at = datetime.now()
    tasks_db[task_index] = task
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str, user_id: str = "default_user"):
    # In a real app, you would validate the JWT token and extract user_id
    global tasks_db
    initial_length = len(tasks_db)
    tasks_db = [t for t in tasks_db if not (t.id == task_id and t.user_id == user_id)]
    
    if len(tasks_db) == initial_length:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {"message": "Task deleted successfully"}

@app.get("/users/preferences")
def get_user_preferences(user_id: str = "default_user"):
    # In a real app, you would validate the JWT token and extract user_id
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user.preferences

@app.put("/users/preferences")
def update_user_preferences(preferences: dict, user_id: str = "default_user"):
    # In a real app, you would validate the JWT token and extract user_id
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.preferences.update(preferences)
    user.updated_at = datetime.now()
    
    return user.preferences

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)