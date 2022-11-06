import pytest
from starlette.testclient import TestClient

from src.main import app


@pytest.fixture(scope='session')
def client():
    return TestClient(app)
