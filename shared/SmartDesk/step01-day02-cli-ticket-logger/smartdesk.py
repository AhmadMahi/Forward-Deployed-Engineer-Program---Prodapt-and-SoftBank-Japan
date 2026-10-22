"""SmartDesk step 01: CLI ticket logger. Tickets are saved as JSON."""
import argparse
import json
from datetime import datetime
from pathlib import Path

DATA = Path(__file__).with_name("tickets.json")
CATEGORIES = ("billing", "network", "account", "other")
PRIORITIES = ("low", "medium", "high")


def load_tickets(path=DATA):
    path = Path(path)
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def next_id(tickets):
    return max((t["id"] for t in tickets), default=0) + 1


def add_ticket(tickets, customer, category, priority, body):
    if category not in CATEGORIES:
        raise ValueError(f"category must be one of {CATEGORIES}")
    if priority not in PRIORITIES:
        raise ValueError(f"priority must be one of {PRIORITIES}")
    if not body.strip():
        raise ValueError("body must not be empty")
    ticket = {"id": next_id(tickets), "customer": customer.strip(), "category": category, "priority": priority,
              "status": "open", "body": body.strip(), "created_at": datetime.now().isoformat(timespec="seconds")}
    tickets.append(ticket)
    return ticket


def save_tickets(tickets, path=DATA):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tickets, f, indent=2, ensure_ascii=False)


def count_by(tickets, key):
    counts = {}
    for t in tickets:
        counts[t[key]] = counts.get(t[key], 0) + 1
    return counts


def main(argv=None):
    p = argparse.ArgumentParser(description="SmartDesk ticket logger")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    sub.add_parser("stats")
    a = sub.add_parser("add")
    a.add_argument("customer")
    a.add_argument("category", choices=CATEGORIES)
    a.add_argument("priority", choices=PRIORITIES)
    a.add_argument("body")
    args = p.parse_args(argv)
    tickets = load_tickets()
    if args.command == "list":
        for t in tickets:
            print(f"#{t['id']:<3} {t['priority']:<6} {t['status']:<12} {t['customer']}: {t['body']}")
    elif args.command == "stats":
        print("By priority:", count_by(tickets, "priority"))
        print("By category:", count_by(tickets, "category"))
    else:
        t = add_ticket(tickets, args.customer, args.category, args.priority, args.body)
        save_tickets(tickets)
        print(f"Saved ticket #{t['id']}")


if __name__ == "__main__":
    main()
