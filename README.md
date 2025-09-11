# TODO List with FastAPI

A simple TODO list application built with FastAPI, 
using an in-memory dictionary as a database, 
Pydantic models for data validation, and comprehensive unit tests.

## Project structure

```
todo_list_fast_api/
├── main.py                 # FastAPI application
├── pydantic_models.py      # Pydantic models for validation
├── requirements.txt        # Python dependencies
├── requests.http           # Example HTTP requests for testing
├── test_main.py            # Unit tests
├── README.md               # This file
```

## How to run

1. **Clone and go to the folder:**
   ```bash
   git clone https://github.com/pflaumax/fastapi_todo_list.git
   cd todo_list_fastapi
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment:**
   
   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **Mac/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Start

```bash
uvicorn app:app --reload
```
 `--reload` is optional and recommended only for development,
as it automatically restarts the server when code changes.
Alternatively, you can start the server with simply:
```bash
uvicorn app:app
```

API will available in address: http://127.0.0.1:8000 with message:
```json
{"message":"Welcome to the API"}
```

## Documentation

FastAPI automatically generates interactive documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Use `requests.http` file for example requests

## Endpoints
 Welcome page http://127.0.0.1:8000/ 

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

### DELETE /tasks/{task_id}
Delete task
**body:**
```json
{
  "message": "Task 'ONE' deleted successfully"
}
```


## Unit Tests

Run tests with:
```bash
pytest test_app.py -v
```

## Stop

Quit uvicorn server by Press `CTRL+C`

## Feature updates
* Use a persistent database
* Add Dockerfile and GitHub Actions CI
* Add logging