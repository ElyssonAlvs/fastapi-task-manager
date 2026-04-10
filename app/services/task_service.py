from sqlalchemy.orm import Session
from app.models.task import Task

def create_task(db: Session, title: str, description: str | None):
    task = Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session, status=None, skip=0, limit=10):
    query = db.query(Task)

    if status:
        query = query.filter(Task.status == status)

    return query.offset(skip).limit(limit).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()