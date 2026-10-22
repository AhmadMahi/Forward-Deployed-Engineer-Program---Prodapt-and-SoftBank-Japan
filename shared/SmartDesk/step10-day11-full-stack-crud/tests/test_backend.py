from fastapi.testclient import TestClient

from backend.main import DB, app

client = TestClient(app)


def test_create_update_close_flow():
    DB.clear()
    t = client.post("/api/tickets", json={"customer": "Aiko", "category": "network", "body": "No signal"}).json()
    assert client.patch(f"/api/tickets/{t['id']}", json={"priority": "high"}).json()["priority"] == "high"
    assert client.post(f"/api/tickets/{t['id']}/close").json()["status"] == "closed"
    assert client.patch(f"/api/tickets/{t['id']}", json={"body": "x"}).status_code == 409
    assert client.post("/api/tickets/999/close").status_code == 404


def test_cors_allows_vite_origin():
    r = client.options("/api/tickets", headers={"Origin": "http://localhost:5173", "Access-Control-Request-Method": "POST"})
    assert r.headers["access-control-allow-origin"] == "http://localhost:5173"


def test_no_api_key_in_frontend():
    import pathlib
    src = "".join(p.read_text() for p in pathlib.Path("frontend/src").glob("*.js*"))
    assert "OPENAI_API_KEY" not in src and "sk-" not in src
