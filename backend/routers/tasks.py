from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlmodel.ext.asyncio.session import AsyncSession
import models, schemas, dependencies
from db import get_db
from sqlmodel import select
from datetime import datetime


router = APIRouter(prefix="/api/{user_id}", tags=["tasks"])


@router.get("/tasks", response_model=List[schemas.TaskRead])
async def get_tasks(
    user_id: str,
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Verify that the user_id in the path matches the authenticated user
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this user's tasks"
        )
    
    # Build the query with optional status filtering
    statement = select(models.Task).where(models.Task.user_id == user_id)
    
    if status:
        if status.lower() == "completed":
            statement = statement.where(models.Task.completed == True)
        elif status.lower() == "pending":
            statement = statement.where(models.Task.completed == False)
        elif status.lower() != "all":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Status must be 'all', 'pending', or 'completed'"
            )
    
    # Apply pagination
    statement = statement.offset(skip).limit(limit)
    
    result = await db.execute(statement)
    tasks = result.scalars().all()
    
    return tasks


@router.post("/tasks", response_model=schemas.TaskRead)
async def create_task(
    task_create: schemas.TaskCreate,
    user_id: str,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Verify that the user_id in the path matches the authenticated user
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to create tasks for this user"
        )
    
    # Create a new task
    db_task = models.Task(
        title=task_create.title,
        description=task_create.description,
        completed=task_create.completed,
        user_id=user_id
    )
    
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    
    return db_task


@router.get("/tasks/{task_id}", response_model=schemas.TaskRead)
async def get_task(
    task_id: int,
    user_id: str,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Verify that the user_id in the path matches the authenticated user
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this user's tasks"
        )
    
    # Query for the specific task
    statement = select(models.Task).where(
        models.Task.id == task_id,
        models.Task.user_id == user_id
    )
    result = await db.execute(statement)
    task = result.scalar_one_or_none()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    return task


@router.put("/tasks/{task_id}", response_model=schemas.TaskRead)
async def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    user_id: str,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Verify that the user_id in the path matches the authenticated user
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this user's tasks"
        )
    
    # Query for the specific task
    statement = select(models.Task).where(
        models.Task.id == task_id,
        models.Task.user_id == user_id
    )
    result = await db.execute(statement)
    task = result.scalar_one_or_none()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Update the task with provided values
    for field, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    
    task.updated_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(task)
    
    return task


@router.delete("/tasks/{task_id}")
async def delete_task(
    task_id: int,
    user_id: str,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Verify that the user_id in the path matches the authenticated user
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this user's tasks"
        )
    
    # Query for the specific task
    statement = select(models.Task).where(
        models.Task.id == task_id,
        models.Task.user_id == user_id
    )
    result = await db.execute(statement)
    task = result.scalar_one_or_none()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    await db.delete(task)
    await db.commit()
    
    return {"message": "Task deleted successfully"}


@router.patch("/tasks/{task_id}/complete")
async def toggle_task_completion(
    task_id: int,
    user_id: str,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Verify that the user_id in the path matches the authenticated user
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this user's tasks"
        )
    
    # Query for the specific task
    statement = select(models.Task).where(
        models.Task.id == task_id,
        models.Task.user_id == user_id
    )
    result = await db.execute(statement)
    task = result.scalar_one_or_none()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Toggle the completion status
    task.completed = not task.completed
    task.updated_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(task)
    
    return {"completed": task.completed}