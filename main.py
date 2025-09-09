from fastapi import FastAPI, HTTPException, status
from pydantic_models import Task, TaskCreate, TaskUpdate


app = FastAPI(
    title="Todo list API",
    version="0.0.1",
    description="A simple API to manage a todo list",
)

db_tasks_storage = {}
current_id = 1

def raise_exception(status_code: int, message: str):
        raise HTTPException(status_code=status_code, detail=message)

@app.get("/")
def welcome_page():
    return {"message": "Welcome to the API"}

@app.get("/tasks", response_model=list[Task])
def get_tasks():
    """Retrieve all tasks"""
    return list(db_tasks_storage.values())

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
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

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    """Update an existing task"""
    stored_task = db_tasks_storage.get(task_id)
    if not stored_task:
        raise_exception(404, "Task not found")

    if task_update.title is not None:
        stored_task.title = task_update.title
    if task_update.description is not None:
        stored_task.description = task_update.description
    if task_update.completed is not None:
        stored_task.completed = task_update.completed

    return stored_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Delete a task"""
    task_to_delete = db_tasks_storage.get(task_id)
    if not task_to_delete:
        raise_exception(404, "Task not found")

    del db_tasks_storage[task_id]

    return {"message": f"Task '{task_to_delete.title}' deleted successfully"}