"""SmartDesk starter (Day 2). A tiny command-line ticket logger.

Run:  python smartdesk.py list
      python smartdesk.py add "Aiko Tanaka" network high "No signal at home"
Your job on Day 2: fill in the TODO functions, then save tickets as JSON.
"""
import json
import sys
from pathlib import Path

DATA = Path(__file__).with_name("tickets.json")


def load_tickets(path=DATA):
    # TODO: return the list of tickets from the JSON file (an empty list if the file is missing)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def add_ticket(tickets, customer, category, priority, body):
    # TODO: build a new ticket dict with the next id, status "open", and append it
    raise NotImplementedError


def save_tickets(tickets, path=DATA):
    # TODO: write the tickets back to the JSON file
    raise NotImplementedError


def print_tickets(tickets):
    for t in tickets:
        print(f"#{t['id']:<3} {t['priority']:<6} {t['status']:<12} {t['customer']}: {t['body']}")


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "list"
    tickets = load_tickets()
    if command == "list":
        print_tickets(tickets)
    else:
        print("Commands: list, add (TODO)")
