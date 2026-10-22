"""Business logic for TelcoDesk Legacy."""
from . import auth, db
from .legacy_csv_import import import_file

VALID_PRIORITIES = ("low", "medium", "high")


def create_ticket(conn, customer, msisdn, category, priority, body, created_at="2026-01-01 00:00:00"):
    if priority not in VALID_PRIORITIES:
        raise ValueError("priority must be low, medium or high")
    if not body:
        raise ValueError("body is required")
    return db.insert_ticket(conn, customer, msisdn, category, priority, body, created_at)


def import_legacy(conn, path):
    count = 0
    for row in import_file(path):
        db.insert_ticket(conn, row["customer"], row["msisdn"], row["category"], row["priority"],
                         row["body"], row["created_at"])
        count += 1
    return count


def close(conn, token, ticket_id):
    if not auth.can_close(token):
        raise PermissionError("not allowed to close tickets")
    return db.close_ticket(conn, ticket_id)
