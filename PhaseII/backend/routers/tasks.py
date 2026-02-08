from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlmodel.ext.asyncio.session import AsyncSession
import models, schemas, dependencies
from db import get_db
from sqlmodel import select
from datetime import datetime


# Main API router
router = APIRouter(prefix="/api/v1", tags=["tasks"])

# Backward compatibility router for legacy clients
legacy_router = APIRouter(tags=["tasks_legacy"])


# Legacy route mappings
@legacy_router.get("/tasks", response_model=List[schemas.TaskRead])
async def get_tasks_legacy(
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Legacy route for getting tasks"""
    return await get_tasks(status, skip, limit, current_user_id, db)


@legacy_router.post("/tasks", response_model=schemas.TaskRead)
async def create_task_legacy(
    task_create: schemas.TaskCreate,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Legacy route for creating tasks"""
    return await create_task(task_create, current_user_id, db)


@legacy_router.get("/tasks/{task_id}", response_model=schemas.TaskRead)
async def get_task_legacy(
    task_id: int,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Legacy route for getting a specific task"""
    return await get_task(task_id, current_user_id, db)


@legacy_router.put("/tasks/{task_id}", response_model=schemas.TaskRead)
async def update_task_legacy(
    task_id: int,
    task_update: schemas.TaskUpdate,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Legacy route for updating a task"""
    return await update_task(task_id, task_update, current_user_id, db)


@legacy_router.delete("/tasks/{task_id}")
async def delete_task_legacy(
    task_id: int,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Legacy route for deleting a task"""
    return await delete_task(task_id, current_user_id, db)


@legacy_router.patch("/tasks/{task_id}/complete")
async def toggle_task_completion_legacy(
    task_id: int,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Legacy route for toggling task completion"""
    return await toggle_task_completion(task_id, current_user_id, db)


@router.get("/tasks", response_model=List[schemas.TaskRead])
async def get_tasks(
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Build the query with optional status filtering
    statement = select(models.Task).where(models.Task.user_id == current_user_id)

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
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Create a new task
    db_task = models.Task(
        title=task_create.title,
        description=task_create.description,
        completed=task_create.completed,
        user_id=current_user_id
    )

    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)

    return db_task


@router.get("/tasks/{task_id}", response_model=schemas.TaskRead)
async def get_task(
    task_id: int,
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Query for the specific task
    statement = select(models.Task).where(
        models.Task.id == task_id,
        models.Task.user_id == current_user_id
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
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Query for the specific task
    statement = select(models.Task).where(
        models.Task.id == task_id,
        models.Task.user_id == current_user_id
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
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Query for the specific task
    statement = select(models.Task).where(
        models.Task.id == task_id,
        models.Task.user_id == current_user_id
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
    current_user_id: str = Depends(dependencies.get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Query for the specific task
    statement = select(models.Task).where(
        models.Task.id == task_id,
        models.Task.user_id == current_user_id
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