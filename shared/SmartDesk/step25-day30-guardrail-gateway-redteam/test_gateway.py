from fastapi.testclient import TestClient

import redteam_suite
from gateway import EVENTS, app
from guardrails import check_output

client = TestClient(app)


def test_red_team_suite_passes():
    results = redteam_suite.run(client)
    failed = [r["id"] for r in results if not r["pass"]]
    assert not failed, failed
    assert any(e["kind"] == "dropped_document" for e in EVENTS)


def test_output_guard_blocks_secrets_and_promises():
    fake_key = "sk-" + "x" * 24                     # built at run time; not a real key
    assert not check_output(f"Here is the key {fake_key}")[0]
    assert not check_output("We guarantee a refund today")[0]


def test_refund_needs_scoped_single_use_approval():
    assert client.post("/tools/refund", params={"ticket_id": 2, "approval_token": "x"}).status_code == 403
    tok = client.post("/approvals", params={"ticket_id": 2, "approver": "rin"}).json()["approval_token"]
    assert client.post("/tools/refund", params={"ticket_id": 9, "approval_token": tok}).status_code == 403
    tok = client.post("/approvals", params={"ticket_id": 2, "approver": "rin"}).json()["approval_token"]
    assert client.post("/tools/refund", params={"ticket_id": 2, "approval_token": tok}).status_code == 200
    assert client.post("/tools/refund", params={"ticket_id": 2, "approval_token": tok}).status_code == 403
