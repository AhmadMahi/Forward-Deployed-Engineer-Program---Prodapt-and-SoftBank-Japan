import pytest
from fastapi.testclient import TestClient

from app.main import DB, app

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean():
    DB.clear()


def new(**kw):
    body = {"customer": "Aiko", "category": "network", "priority": "high", "body": "No signal"} | kw
    return client.post("/tickets", json=body)


def test_create_and_get():
    r = new()
    assert r.status_code == 201 and r.json()["status"] == "open"
    assert client.get(f"/tickets/{r.json()['id']}").status_code == 200


def test_validation_errors():
    assert new(category="weather").status_code == 422
    assert new(body="").status_code == 422


def test_filter_update_delete():
    a, b = new().json(), new(priority="low").json()
    assert [t["id"] for t in client.get("/tickets", params={"priority": "low"}).json()] == [b["id"]]
    assert client.patch(f"/tickets/{a['id']}", json={"status": "closed"}).json()["status"] == "closed"
    assert client.delete(f"/tickets/{a['id']}").status_code == 204
    assert client.get(f"/tickets/{a['id']}").status_code == 404
