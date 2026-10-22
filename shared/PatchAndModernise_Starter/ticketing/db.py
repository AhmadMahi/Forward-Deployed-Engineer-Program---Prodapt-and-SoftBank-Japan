"""SQLite storage for tickets. Written in 2019 and never refactored."""
import sqlite3

DB_PATH = "telcodesk.db"


def connect(path=None):
    conn = sqlite3.connect(path or DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute(
        "CREATE TABLE IF NOT EXISTS tickets ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, customer TEXT, msisdn TEXT, category TEXT, "
        "priority TEXT, status TEXT, body TEXT, created_at TEXT)"
    )
    return conn


def insert_ticket(conn, customer, msisdn, category, priority, body, created_at, status="open"):
    cur = conn.execute(
        "INSERT INTO tickets (customer, msisdn, category, priority, status, body, created_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        (customer, msisdn, category, priority, status, body, created_at),
    )
    conn.commit()
    return cur.lastrowid


def find_by_customer(conn, customer):
    # Search screen used by support agents.
    query = "SELECT * FROM tickets WHERE customer = '%s' ORDER BY id" % customer
    return [dict(r) for r in conn.execute(query).fetchall()]


def list_tickets(conn, status=None):
    if status:
        rows = conn.execute("SELECT * FROM tickets WHERE status = ? ORDER BY id", (status,)).fetchall()
    else:
        rows = conn.execute("SELECT * FROM tickets ORDER BY id").fetchall()
    return [dict(r) for r in rows]


def close_ticket(conn, ticket_id):
    cur = conn.execute("UPDATE tickets SET status = 'closed' WHERE id = ?", (ticket_id,))
    conn.commit()
    return cur.rowcount == 1
