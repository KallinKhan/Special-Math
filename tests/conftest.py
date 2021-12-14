import pytest
from src import initialize_api


@pytest.fixture
def client():
    app = initialize_api()

    with app.test_client() as client:
        yield client
