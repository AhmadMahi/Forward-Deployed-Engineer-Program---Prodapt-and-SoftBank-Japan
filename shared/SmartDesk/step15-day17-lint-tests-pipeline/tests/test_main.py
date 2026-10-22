from fastapi.testclient import TestClient

from app.main import app


def test_health_and_version():
    c = TestClient(app)
    assert c.get("/health").json() == {"status": "ok"}
    assert c.get("/version").json()["commit"] == "local"
