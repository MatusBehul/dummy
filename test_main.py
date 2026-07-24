from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_greet_endpoint():
    """Test the /greet endpoint with various names."""
    # Test with a name
    response = client.get("/greet?name=World")
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, World!"}

    # Test with another name
    response = client.get("/greet?name=Alice")
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, Alice!"}

    # Test with special characters
    response = client.get("/greet?name=John%20Doe")
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, John Doe!"}


def test_root_endpoint():
    """Test that the root endpoint serves the SPA."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Dynamic Greeting" in response.content
    assert b"greetForm" in response.content


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])