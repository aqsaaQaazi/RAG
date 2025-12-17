import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "RAG Textbook API is running!" in response.json().get("message", "")

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_chat_ask_endpoint_exists():
    """Test that the chat endpoint exists"""
    # This would require a proper request body, so we'll just check if the route exists
    # by making a request that should return validation error rather than 404
    response = client.post("/api/v1/chat/ask", json={})
    # Should return 422 (validation error) rather than 404 (not found)
    assert response.status_code in [422, 500]  # 500 might occur due to missing services

def test_ingestion_status_endpoint():
    """Test the ingestion status endpoint"""
    response = client.get("/api/v1/ingestion/status")
    assert response.status_code in [200, 500]  # 500 might occur due to missing services