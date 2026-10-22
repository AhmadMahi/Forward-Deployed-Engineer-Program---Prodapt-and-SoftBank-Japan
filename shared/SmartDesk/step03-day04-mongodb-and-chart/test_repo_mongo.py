import pytest

import repo_mongo as r


@pytest.fixture
def col(monkeypatch):
    monkeypatch.delenv("MONGO_URI", raising=False)
    c = r.get_collection()
    r.load_sample(c)
    return c


def test_counts_add_up(col):
    counts = r.count_by_priority(col)
    assert sum(counts.values()) == 15


def test_open_high_priority(col):
    ids = {d["ticket_id"] for d in r.open_high_priority(col)}
    assert 1 in ids and 5 not in ids


def test_close_and_unique_index(col):
    assert r.close_ticket(col, 1) == 1
    assert col.find_one({"ticket_id": 1})["status"] == "closed"
    with pytest.raises(Exception):
        col.insert_one({"ticket_id": 1})


def test_chart_file(col, tmp_path):
    out = r.save_chart(r.count_by_priority(col), tmp_path / "c.png")
    assert out.exists() and out.stat().st_size > 0
