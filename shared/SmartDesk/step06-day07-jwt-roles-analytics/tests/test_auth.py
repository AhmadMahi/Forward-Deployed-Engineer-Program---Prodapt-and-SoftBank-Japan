from datetime import datetime, timedelta, timezone

import jwt
from fastapi.testclient import TestClient

from app.main import _mock, app
from app.security import ALGORITHM, SECRET

client = TestClient(app)


def token(user, password):
    return client.post("/auth/login", data={"username": user, "password": password}).json()["access_token"]


def h(t):
    return {"Authorization": f"Bearer {t}"}


def test_login_and_roles():
    agent, lead = token("kenji", "agent-demo-pass"), token("rin", "lead-demo-pass")
    body = {"customer": "Aiko", "category": "network", "priority": "high", "body": "No signal"}
    assert client.post("/tickets", json=body, headers=h(agent)).status_code == 201
    assert client.get("/analytics/by-category", headers=h(agent)).status_code == 403
    r = client.get("/analytics/by-category", headers=h(lead))
    assert r.status_code == 200 and r.json()[0]["count"] >= 1


def test_wrong_password_and_missing_token():
    assert client.post("/auth/login", data={"username": "kenji", "password": "x"}).status_code == 401
    assert client.get("/tickets").status_code == 401


def test_expired_token_rejected():
    old = datetime.now(timezone.utc) - timedelta(hours=1)
    t = jwt.encode({"sub": "kenji", "scopes": ["tickets:read"], "exp": old}, SECRET, algorithm=ALGORITHM)
    r = client.get("/tickets", headers=h(t))
    assert r.status_code == 401 and r.json()["detail"] == "Token expired"


def test_nosql_injection_is_treated_as_text():
    _mock.insert_one({"customer": "Kenji", "category": "billing", "status": "open"})
    t = token("kenji", "agent-demo-pass")
    r = client.get("/tickets", params={"customer": '{"$ne": null}'}, headers=h(t))
    assert r.status_code == 200 and r.json() == []
