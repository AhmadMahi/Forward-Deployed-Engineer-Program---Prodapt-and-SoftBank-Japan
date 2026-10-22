from fastapi.testclient import TestClient

import app as appmod
from token_cost import cost


def test_cost_by_hand():
    assert abs(cost(1000, 500) - (1000 * 1.0 + 500 * 4.0) / 1e6) < 1e-12
    assert cost(1000, 0, cached_t=1000) < cost(1000, 0)


def test_summarise_logs_usage(tmp_path, monkeypatch):
    monkeypatch.setattr(appmod, "LOG", str(tmp_path / "log.csv"))
    c = TestClient(appmod.app)
    r = c.post("/summarise", json={"id": 1, "body": "My bill doubled this month."})
    assert r.status_code == 200 and r.json()["summary"].startswith("[offline demo]")
    assert c.get("/usage/today").json()["calls"] == 1
    assert c.post("/summarise", json={"id": 2, "body": ""}).status_code == 422
