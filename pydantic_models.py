from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    """Model for a task with ID"""
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(BaseModel):
    """Model for creating a new task"""
    title: str
    description: Optional[str] = None
    completed: bool = False