"""SmartDesk step 03: store tickets in MongoDB and chart them by priority.

Uses mongomock by default so it runs anywhere. Set MONGO_URI to use a real MongoDB or Atlas cluster.
"""
import json
import os
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "tickets.json"


def get_collection():
    uri = os.getenv("MONGO_URI")
    if uri:
        from pymongo import MongoClient
        client = MongoClient(uri)
    else:
        import mongomock
        client = mongomock.MongoClient()
    col = client["smartdesk"]["tickets"]
    col.create_index("ticket_id", unique=True)
    col.create_index([("status", 1), ("priority", 1)])
    return col


def load_sample(col):
    with open(DATA, encoding="utf-8") as f:
        docs = [{**t, "ticket_id": t.pop("id")} for t in json.load(f)]
    col.insert_many(docs)
    return len(docs)


def open_high_priority(col):
    return list(col.find({"status": "open", "priority": "high"}, {"_id": 0, "ticket_id": 1, "customer": 1}))


def close_ticket(col, ticket_id):
    return col.update_one({"ticket_id": ticket_id}, {"$set": {"status": "closed"}}).modified_count


def count_by_priority(col):
    rows = col.aggregate([{"$group": {"_id": "$priority", "n": {"$sum": 1}}}])
    return {r["_id"]: r["n"] for r in rows}


def save_chart(counts, path="tickets_by_priority.png"):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    order = [p for p in ("high", "medium", "low") if p in counts]
    plt.figure(figsize=(5, 3))
    plt.bar(order, [counts[p] for p in order], color=["#FF8A3D", "#0FA3A3", "#0E3B43"][:len(order)])
    plt.title("SmartDesk tickets by priority")
    plt.ylabel("Tickets")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path


if __name__ == "__main__":
    col = get_collection()
    load_sample(col)
    print("Open high priority:", open_high_priority(col))
    counts = count_by_priority(col)
    print("By priority:", counts, "->", save_chart(counts))
