"""SmartDesk step 02: Ticket, Customer and Agent classes, plus a TicketStore with search.

The search feature is the first one built with OpenAI Codex on Day 3. The engineer reviewed the diff.
"""
import json
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path


class TicketError(Exception):
    """Raised for invalid ticket operations."""


@dataclass
class Customer:
    name: str
    email: str = ""


@dataclass
class Agent:
    name: str
    team: str = "support"

    def can_close(self, ticket):
        return ticket.status != "closed"


@dataclass
class Ticket:
    id: int
    customer: str
    category: str
    priority: str
    body: str
    status: str = "open"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    VALID_STATUS = ("open", "in_progress", "closed")

    def move_to(self, status):
        if status not in self.VALID_STATUS:
            raise TicketError(f"Unknown status {status!r}")
        if self.status == "closed":
            raise TicketError("A closed ticket cannot change status")
        self.status = status

    def to_dict(self):
        return asdict(self)


class UrgentTicket(Ticket):
    """A high priority ticket that must be answered within 4 hours."""

    SLA_HOURS = 4


class TicketStore:
    def __init__(self, tickets=None):
        self.tickets = list(tickets or [])

    @classmethod
    def from_json(cls, path):
        with open(path, encoding="utf-8") as f:
            return cls(Ticket(**t) for t in json.load(f))

    def add(self, ticket):
        if any(t.id == ticket.id for t in self.tickets):
            raise TicketError(f"Duplicate id {ticket.id}")
        self.tickets.append(ticket)

    def search(self, text="", status=None, priority=None):
        """Case-insensitive search in customer and body, with optional filters."""
        q = text.lower().strip()
        return [t for t in self.tickets
                if (not q or q in t.body.lower() or q in t.customer.lower())
                and (status is None or t.status == status)
                and (priority is None or t.priority == priority)]


DATA = Path(__file__).resolve().parents[1] / "data" / "tickets.json"

if __name__ == "__main__":
    store = TicketStore.from_json(DATA)
    for t in store.search("signal"):
        print(t.id, t.customer, t.body)
