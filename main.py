from fastapi import FastAPI
from pydantic_models import Task, TaskCreate


app = FastAPI(title="Todo list API", version="0.0.1")

db_tasks_storage = {}
current_id = 1

@app.get("/tasks")
def get_tasks():
    """Retrieve all tasks"""
    return list(db_tasks_storage.values())

@app.post("/tasks")
def create_task(task: TaskCreate):
    """Create a new task"""
    global current_id

    new_task = Task(
        id=current_id,
        title=task.title,
        description=task.description,
        completed=task.completed
    )

    db_tasks_storage[current_id] = new_task
    current_id += 1

    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    """Update an existing task"""
    pass

@app.delete("/tasks/{id}")
def delete_task(task_id: int):
    """Delete a task"""
    pass