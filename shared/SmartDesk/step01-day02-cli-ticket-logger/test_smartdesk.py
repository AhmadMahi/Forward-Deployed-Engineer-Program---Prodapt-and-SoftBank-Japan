import pytest

from smartdesk import add_ticket, count_by, load_tickets, save_tickets


def test_add_and_save_round_trip(tmp_path):
    path = tmp_path / "t.json"
    tickets = []
    t = add_ticket(tickets, " Aiko ", "network", "high", "No signal")
    assert t["id"] == 1 and t["status"] == "open" and t["customer"] == "Aiko"
    save_tickets(tickets, path)
    assert load_tickets(path) == tickets


def test_missing_file_gives_empty_list(tmp_path):
    assert load_tickets(tmp_path / "missing.json") == []


def test_rejects_bad_input():
    with pytest.raises(ValueError):
        add_ticket([], "A", "weather", "high", "x")
    with pytest.raises(ValueError):
        add_ticket([], "A", "billing", "urgent", "x")
    with pytest.raises(ValueError):
        add_ticket([], "A", "billing", "high", "   ")


def test_count_by_priority():
    tickets = load_tickets()
    counts = count_by(tickets, "priority")
    assert sum(counts.values()) == len(tickets) == 15
