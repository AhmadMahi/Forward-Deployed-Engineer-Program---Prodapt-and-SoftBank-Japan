import asyncio

import pytest
from mcp import Client

from agent_demo import ask
from mcp_server import server
from sandbox import run_code


def test_tools_are_discoverable():
    out = asyncio.run(ask("Show me ticket 3"))
    assert {"get_ticket", "search_tickets", "update_status"} <= set(out["tools"])
    assert out["call"] == "get_ticket" and out["result"]["id"] == 3


def test_agent_can_close_a_ticket():
    out = asyncio.run(ask("Please close ticket 7"))
    assert out["result"] == {"id": 7, "status": "closed"}


def test_invalid_status_is_rejected():
    async def go():
        async with Client(server) as c:
            return await c.call_tool("update_status", {"ticket_id": 1, "status": "deleted"})
    assert asyncio.run(go()).is_error


@pytest.mark.parametrize("code,ok", [("print(sum(range(10)))", True), ("raise SystemExit(3)", False)])
def test_sandbox_runs_code(code, ok):
    r = run_code(code)
    assert r["ok"] is ok
    if ok:
        assert r["stdout"].strip() == "45"


def test_sandbox_has_no_secrets_and_times_out():
    assert run_code("import os; print(os.environ.get('OPENAI_API_KEY'))")["stdout"].strip() == "None"
    assert run_code("while True: pass", timeout=1)["stderr"] == "timeout"
