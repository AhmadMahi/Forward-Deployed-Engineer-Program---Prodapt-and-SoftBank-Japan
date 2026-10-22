"""Command line entry point: python -m ticketing.cli import data/legacy_tickets.csv"""
import sys

from . import db, service


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    conn = db.connect()
    if argv[:1] == ["import"] and len(argv) == 2:
        print("Imported", service.import_legacy(conn, argv[1]), "tickets")
    elif argv[:1] == ["list"]:
        for t in db.list_tickets(conn):
            print(t["id"], t["priority"], t["status"], t["customer"], "-", t["body"][:50])
    else:
        print("usage: python -m ticketing.cli import <file> | list")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
