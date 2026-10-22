import pytest

from models import DATA, Agent, Ticket, TicketError, TicketStore, UrgentTicket


def store():
    return TicketStore.from_json(DATA)


def test_search_text_is_case_insensitive():
    ids = [t.id for t in store().search("SIGNAL")]
    assert 1 in ids


def test_search_with_filters():
    results = store().search(status="open", priority="high")
    assert results and all(t.status == "open" and t.priority == "high" for t in results)


def test_closed_ticket_cannot_reopen():
    t = Ticket(1, "A", "billing", "low", "x", status="closed")
    with pytest.raises(TicketError):
        t.move_to("open")


def test_duplicate_id_rejected():
    s = store()
    with pytest.raises(TicketError):
        s.add(Ticket(1, "A", "billing", "low", "x"))


def test_inheritance_and_agent():
    u = UrgentTicket(99, "B", "network", "high", "Outage")
    assert isinstance(u, Ticket) and u.SLA_HOURS == 4
    assert Agent("Kenji").can_close(u)
