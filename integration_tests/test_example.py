# integration_tests/test_example.py

import pytest
from hello.app import app  # Adjust import based on actual path

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
