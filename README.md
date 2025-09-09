# TODO List with FastAPI
A simple TODO list application built with FastAPI, 
using an in-memory dictionary as a database, 
Pydantic models for data validation, and comprehensive unit tests.

## Installation

1. **Create project:**
   ```bash
   mkdir todo_list_fastapi
   cd todo_list_fastapi
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Mac/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Start

```bash
uvicorn main:app --reload
```
API will available in address: http://127.0.0.1:8000

## Documentation

FastAPI automatically generates interactive documentation.:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

### Welcome page http://127.0.0.1:8000/ 

### GET /tasks
Get all tasks **response:**
```json
[
  {
    "id": 1,
    "title": "ONE",
    "description": "task one description",
    "completed": false
  }
]
```

### POST /tasks
Create a new task
**body:**
```json
{
  "title": "ONE",
  "description": "task one description",
  "completed": false
}
```

### PUT /tasks/{task_id}
Update task
**body:**
```json
{
  "title": "Updated ONE",
  "completed": true
}
```

### DELETE /tasks/{id}
Delete task

## Unit Tests

Run tests with:
```bash
pytest test_main.py -v
```

## Use `requests.http` file for example requests