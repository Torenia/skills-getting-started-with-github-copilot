import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_signup_success():
    # Register a participant for an activity
    response = client.post("/activities/Chess Club/signup?email=test1@mergington.edu")
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]

def test_signup_duplicate():
    # Register the same participant twice
    client.post("/activities/Chess Club/signup?email=test2@mergington.edu")
    response = client.post("/activities/Chess Club/signup?email=test2@mergington.edu")
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"

def test_signup_activity_not_found():
    response = client.post("/activities/Nonexistent/signup?email=test3@mergington.edu")
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
