import json
from pathlib import Path

from cost_report import report
from router import route, slm_classify

TICKETS = json.loads((Path(__file__).resolve().parents[1] / "data" / "tickets.json").read_text())


def test_confident_tickets_stay_on_slm():
    r = route("I was charged twice and want a refund on my invoice")
    assert r["by"] == "slm" and r["label"] == "billing" and r["usage"]["input_tokens"] == 0


def test_unsure_tickets_escalate():
    r = route("Do you have a store open on Sunday?")
    assert r["by"] == "llm"


def test_slm_accuracy_on_sample():
    hits = sum(slm_classify(t["body"])[0] == t["category"] for t in TICKETS)
    assert hits / len(TICKETS) >= 0.7


def test_each_optimisation_saves_money():
    values = [v for _, v in report()]
    assert all(b < a for a, b in zip(values, values[1:]))
