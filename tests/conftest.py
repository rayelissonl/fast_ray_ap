import pytest
from fastapi.testclient import TestClient

from fast_ray_ap.app import app


@pytest.fixture()
def client():
    return TestClient(app)
