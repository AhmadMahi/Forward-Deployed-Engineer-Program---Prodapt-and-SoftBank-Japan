import pytest
from fastapi.testclient import TestClient

from app.db import SessionLocal
from app.main import app, transfer_tickets

client = TestClient(app)


def new(customer="Aiko", **kw):
    return client.post("/tickets", json={"customer": customer, "category": "network", "body": "No signal"} | kw)


def test_relationship_and_join():
    new("Kenji"), new("Kenji", category="billing")
    assert len(client.get("/customers/Kenji/tickets").json()) == 2
    assert client.get("/reports/tickets-per-customer").json()["Kenji"] == 2


def test_comment_on_missing_ticket():
    assert client.post("/tickets/999/comments", json={"author": "a", "text": "b"}).status_code == 404
    tid = new().json()["id"]
    assert client.post(f"/tickets/{tid}/comments", json={"author": "Agent", "text": "Checking"}).status_code == 201


def test_rollback_on_error():
    new("Rin")
    db = SessionLocal()
    with pytest.raises(ValueError):
        transfer_tickets(db, "Rin", "Nobody")
    assert len(client.get("/customers/Rin/tickets").json()) == 1
    db.close()


def test_swagger_docs():
    spec = client.get("/openapi.json").json()
    assert "/tickets" in spec["paths"] and spec["info"]["version"] == "0.5.0"
