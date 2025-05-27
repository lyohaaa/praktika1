from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: int
    deadline: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskShort(TaskBase):
    id: int
    is_completed: bool

class TaskFull(TaskShort):
    created_at: datetime
    updated_at: Optional[datetime] = None