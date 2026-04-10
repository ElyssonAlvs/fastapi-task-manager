from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session, desc
from typing import Annotated, List, Optional
from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services import task_service

router = APIRouter(prefix="/v1/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Annotated[Session, Depends(get_db)]):
    return task_service.create_task(db, title=task.title, description=task.description)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = task_service.get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Annotated[Session, Depends(get_db)]
):
    task = task_service.get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    if task_update.title is not None:
        task.title = task_update.title

    if task_update.description is not None:
        task.description = task_update.description

    if task_update.status is not None:
        task.status = task_update.status

    db.commit()
    db.refresh(task)

    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    db.delete(task)
    db.commit()


@router.get("/", response_model=List[TaskResponse])
def get_tasks(
    db: Annotated[Session, Depends(get_db)],
    status: Annotated[Optional[str], Query(pattern="^(pending|done|in_progress)$")] = None,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(le=100)] = 10
):
    query = db.query(Task)

    if status:
        query = query.filter(Task.status == status)
        
    tasks = query.order_by(desc(Task.created_at)).offset(skip).limit(limit).all()

    return {
        "data": tasks,
        "count": len(tasks)
    }
