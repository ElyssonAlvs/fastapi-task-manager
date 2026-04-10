from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[str] = Field(
        None, pattern="^(pending|completed|in_progress)$")
