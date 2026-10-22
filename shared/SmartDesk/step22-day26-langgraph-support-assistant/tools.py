"""SmartDesk tools. Each tool has a narrow job, a short description and validated input (fewer tokens, fewer mistakes)."""
import json
from pathlib import Path

TICKETS = {t["id"]: t for t in json.loads((Path(__file__).resolve().parents[1] / "data" / "tickets.json").read_text())}
OUTAGES = {"setagaya": "Mast repair in progress. Expected fix 18:00 today.", "shibuya": "Evening congestion. Extra capacity added."}
REFUNDS = []


def lookup_ticket(ticket_id: int) -> dict:
    """Get one ticket by id."""
    return TICKETS.get(ticket_id, {"error": "not found"})


def check_outage(area: str) -> str:
    """Check the outage map for an area name."""
    return OUTAGES.get(area.lower(), "No known outage in this area.")


def create_refund_request(ticket_id: int, amount_jpy: int) -> dict:
    """Create a refund request. Only call after human approval."""
    if amount_jpy <= 0 or amount_jpy > 20000:
        raise ValueError("amount must be between 1 and 20,000 JPY")
    REFUNDS.append({"ticket_id": ticket_id, "amount_jpy": amount_jpy})
    return {"status": "refund requested", "ticket_id": ticket_id, "amount_jpy": amount_jpy}
