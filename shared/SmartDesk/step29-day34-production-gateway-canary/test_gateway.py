import os

from fastapi.testclient import TestClient

os.environ["ADMIN_TOKEN"] = "test-only-token"
from gateway import RELEASES, STATE, app, pick_release  # noqa: E402

client = TestClient(app)


def test_streaming_response():
    with client.stream("POST", "/v1/chat", json={"user_id": "u1", "message": "No signal"}) as r:
        chunks = list(r.iter_text())
    assert r.status_code == 200 and len(chunks) >= 1 and "No signal" in "".join(chunks)
    assert r.headers["x-release"] in RELEASES.values()


def test_canary_share_is_close_to_target_and_sticky():
    STATE["canary_percent"] = 10
    share = sum(pick_release(f"user-{i}") == "canary" for i in range(2000)) / 2000
    assert 0.07 < share < 0.13
    assert pick_release("user-42") == pick_release("user-42")


def test_rollback_needs_admin_token():
    assert client.post("/admin/canary", params={"percent": 0}, headers={"x-admin-token": "wrong"}).status_code == 403
    assert client.post("/admin/canary", params={"percent": 0}, headers={"x-admin-token": "test-only-token"}).status_code == 200
    assert all(pick_release(f"u{i}") == "stable" for i in range(200))
