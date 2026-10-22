import pytest

pytest.importorskip("langgraph")

from langgraph.types import Command  # noqa: E402

from graph import build  # noqa: E402
from tools import REFUNDS  # noqa: E402


def run(ticket_id, thread):
    app = build()
    cfg = {"configurable": {"thread_id": thread}}
    return app, cfg, app.invoke({"ticket_id": ticket_id}, cfg)


def test_network_ticket_uses_outage_tool():
    _, _, out = run(1, "n1")
    assert "Mast repair" in out["tool_result"] and "check_outage(setagaya)" in out["log"]


def test_refund_pauses_for_approval_then_resumes():
    REFUNDS.clear()
    app, cfg, out = run(2, "b1")
    assert "__interrupt__" in out and not REFUNDS
    final = app.invoke(Command(resume={"approved": True, "amount_jpy": 3000}), cfg)
    assert final["approved"] is True and REFUNDS == [{"ticket_id": 2, "amount_jpy": 3000}]


def test_rejected_refund_creates_nothing():
    REFUNDS.clear()
    app, cfg, _ = run(12, "b2")
    final = app.invoke(Command(resume={"approved": False}), cfg)
    assert final["approved"] is False and REFUNDS == []
