from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(
        title=task.title,
        description=task.description
    )
    
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

@router.get("", response_model=List[TaskResponse])
def get_tasks(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks