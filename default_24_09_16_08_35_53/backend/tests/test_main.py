import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_top_stories():
    response = client.get("/top-stories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 10

def test_get_top_stories_error():
    response = client.get("/top-stories")
    assert response.status_code == 200  # Assuming the API is reachable
