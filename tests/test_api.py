"""
API tests
"""

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    """Create test client"""
    from app.main import app
    return TestClient(app)


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_generate_content(client):
    """Test content generation endpoint"""
    payload = {
        "prompt": "Explain photosynthesis",
        "parameters": {"max_length": 512}
    }
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 200
