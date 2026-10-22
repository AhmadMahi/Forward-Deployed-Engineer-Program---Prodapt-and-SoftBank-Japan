import pytest

from ticketing import auth, db, diagnostics, service


def test_create_and_list(conn):
    tid = service.create_ticket(conn, "Aiko", "+819012345678", "network", "high", "No signal")
    rows = db.list_tickets(conn)
    assert rows[0]["id"] == tid
    assert rows[0]["status"] == "open"


def test_create_rejects_bad_priority(conn):
    with pytest.raises(ValueError):
        service.create_ticket(conn, "Aiko", "+819012345678", "network", "urgent", "No signal")


def test_find_by_customer(conn):
    service.create_ticket(conn, "Ravi", "+819098765432", "billing", "medium", "Charged twice")
    service.create_ticket(conn, "Mei", "+818011112222", "account", "low", "Locked out")
    assert [t["customer"] for t in db.find_by_customer(conn, "Ravi")] == ["Ravi"]


def test_token_round_trip():
    token = auth.issue_token("agent-7", role="agent")
    assert isinstance(token, str)
    assert auth.read_token(token)["sub"] == "agent-7"


def test_close_needs_valid_token(conn):
    tid = service.create_ticket(conn, "Ken", "+817033334444", "network", "medium", "Roaming")
    assert service.close(conn, auth.issue_token("agent-1"), tid) is True
    with pytest.raises(PermissionError):
        service.close(conn, "not-a-token", tid)


def test_viewer_cannot_close(conn):
    tid = service.create_ticket(conn, "Ken", "+817033334444", "network", "medium", "Roaming")
    with pytest.raises(PermissionError):
        service.close(conn, auth.issue_token("viewer-1", role="viewer"), tid)


def test_ping_builds_command():
    assert diagnostics.ping_host("10.0.0.1", count=2) == "ping -c 2 10.0.0.1"
