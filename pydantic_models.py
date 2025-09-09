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


class TaskUpdate(BaseModel):
    """Model for updating an existing task"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None