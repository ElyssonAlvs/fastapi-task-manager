from sqlalchemy import Column, Integer, String, Enum
import enum
from app.database import Base
    
class TaskStatus(str, enum.Enum):
    pending = "pending"
    done = "done"
    in_progress = "in_progress"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending)