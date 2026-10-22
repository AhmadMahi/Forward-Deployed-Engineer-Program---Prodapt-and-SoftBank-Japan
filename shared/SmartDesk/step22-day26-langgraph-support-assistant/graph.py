"""SmartDesk step 22: a support assistant as a LangGraph flow with tools and a human approval interrupt.

classify -> (network: check_outage | billing: propose refund -> approval interrupt -> refund tool | other) -> respond
A checkpointer saves state, so a paused run can resume after a human decision (durable execution).
"""
import re
from typing import Optional, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import interrupt

from llm_client import complete
from tools import check_outage, create_refund_request, lookup_ticket

AREAS = ["setagaya", "shibuya", "yokohama"]


class State(TypedDict, total=False):
    ticket_id: int
    ticket: dict
    route: str
    tool_result: str
    approved: Optional[bool]
    reply: str
    log: list


def load(state):
    t = lookup_ticket(state["ticket_id"])
    return {"ticket": t, "log": [f"lookup_ticket({state['ticket_id']})"]}


def classify(state):
    return {"route": state["ticket"].get("category", "other")}


def network(state):
    body = state["ticket"]["body"].lower()
    area = next((a for a in AREAS if a in body), "unknown")
    return {"tool_result": check_outage(area), "log": state["log"] + [f"check_outage({area})"]}


def billing(state):
    wants_refund = bool(re.search(r"refund|charged twice|doubled", state["ticket"]["body"].lower()))
    if not wants_refund:
        return {"tool_result": "Billing question, no refund needed."}
    decision = interrupt({"action": "create_refund_request", "ticket_id": state["ticket_id"], "amount_jpy": 3000})
    if not decision.get("approved"):
        return {"approved": False, "tool_result": "Refund not approved by the team lead."}
    r = create_refund_request(state["ticket_id"], decision.get("amount_jpy", 3000))
    return {"approved": True, "tool_result": str(r), "log": state["log"] + ["create_refund_request"]}


def other(state):
    return {"tool_result": "Routed to a human agent."}


def respond(state):
    text, _ = complete(f"Write a short, kind reply to the customer. Facts: {state['tool_result']}\n"
                       f"Ticket: {state['ticket'].get('body', '')}")
    return {"reply": text}


def build():
    g = StateGraph(State)
    for name, fn in [("load", load), ("classify", classify), ("network", network), ("billing", billing),
                     ("other", other), ("respond", respond)]:
        g.add_node(name, fn)
    g.add_edge(START, "load")
    g.add_edge("load", "classify")
    g.add_conditional_edges("classify", lambda s: s["route"] if s["route"] in ("network", "billing") else "other",
                            ["network", "billing", "other"])
    for n in ("network", "billing", "other"):
        g.add_edge(n, "respond")
    g.add_edge("respond", END)
    return g.compile(checkpointer=InMemorySaver())


if __name__ == "__main__":
    from langgraph.types import Command
    app = build()
    cfg = {"configurable": {"thread_id": "ticket-2"}}
    print(app.invoke({"ticket_id": 2}, cfg).get("__interrupt__"))
    print(app.invoke(Command(resume={"approved": True, "amount_jpy": 3000}), cfg)["reply"])
