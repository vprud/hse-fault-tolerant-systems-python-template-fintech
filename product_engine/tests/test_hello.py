from fastapi.testclient import TestClient
from pytest import mark

from src.main import app

client = TestClient(app=app)


@mark.parametrize("name", [42, "foo"])
def test_hello(name):
    response = client.get(f"/hello/{name}")

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["message"] == f"Hello {name}"
