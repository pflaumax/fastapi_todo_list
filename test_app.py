from fastapi.testclient import TestClient
import app
import pytest


@pytest.fixture
def client():
    """Create a client for the app"""
    return TestClient(app.app)


@pytest.fixture(autouse=True)
def reset_db():
    """Reset the list database before each test"""
    app.db_tasks_storage.clear()
    app.current_id = 1


def test_get_empty_tasks(client):
    """Test retrieving tasks when none exist"""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_create_task(client):
    """Test creating a new task"""
    task_data = {
        "title": "Learn about mutable tests",
        "description": "mutmut",
        "completed": False
    }
    response = client.post("/tasks", json=task_data)

    assert response.status_code == 201
    created_task = response.json()
    assert created_task["id"] == 1
    assert created_task["title"] == "Learn about mutable tests"
    assert created_task["description"] == "mutmut"
    assert created_task["completed"] == False


def test_create_task_without_description(client):
    """Test creating a task without a description"""
    task_data = {"title": "Learn about PostGIS"}
    response = client.post("/tasks", json=task_data)

    assert response.status_code == 201
    created_task = response.json()
    assert created_task["title"] == "Learn about PostGIS"
    assert created_task["description"] is None
    assert created_task["completed"] == False


def test_get_tasks_after_creating(client):
    """Get tasks after creating one"""
    task_data = {"title": "Learn about PgBouncer"}
    client.post("/tasks", json=task_data)

    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Learn about PgBouncer"


def test_update_task(client):
    """Test updating an existing task"""
    task_data = {"title": "Old title"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]

    update_data = {
        "title": "New title",
        "completed": True
    }
    response = client.put(f"/tasks/{task_id}", json=update_data)

    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["title"] == "New title"
    assert updated_task["completed"] == True


def test_update_nonexistent_task(client):
    """Test updating a task that does not exist"""
    update_data = {"title": "Nonexistent task"}
    response = client.put("/tasks/999", json=update_data)

    assert response.status_code == 404
    assert "Task not found" in response.json()["detail"]


def test_delete_task(client):
    """Test deleting an existing task"""
    task_data = {"title": "Check new GIL changes"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Task '{task_data['title']}' deleted successfully"}

    get_response = client.get("/tasks")
    assert len(get_response.json()) == 0


def test_delete_nonexistent_task(client):
    """Test deleting a task that does not exist"""
    response = client.delete("/tasks/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}