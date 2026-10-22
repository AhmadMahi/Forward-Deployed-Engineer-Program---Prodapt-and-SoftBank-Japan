from drift import drift_alerts, psi
from tracing import EXPORTER, per_trace_totals, ticket_trace


def fake_call(prompt):
    return "network", {"input_tokens": len(prompt.split()) * 2, "output_tokens": 5}


def test_spans_follow_genai_conventions():
    EXPORTER.clear()
    ticket_trace("No signal in Setagaya", fake_call)
    spans = [s for s in EXPORTER.get_finished_spans() if s.name.startswith("chat")]
    assert len(spans) == 2
    for s in spans:
        for key in ("gen_ai.operation.name", "gen_ai.request.model", "gen_ai.usage.input_tokens", "gen_ai.usage.output_tokens"):
            assert key in s.attributes


def test_token_and_cost_per_trace():
    EXPORTER.clear()
    ticket_trace("Charged twice", fake_call)
    totals = list(per_trace_totals().values())
    assert len(totals) == 1 and totals[0]["spans"] == 3 and totals[0]["tokens"] > 0 and totals[0]["cost"] > 0


def test_psi_detects_shift():
    base = ["billing"] * 30 + ["network"] * 40 + ["account"] * 20 + ["other"] * 10
    assert psi(base, base, ["billing", "network", "account", "other"]) == 0
    outage_week = ["billing"] * 10 + ["network"] * 80 + ["account"] * 5 + ["other"] * 5
    alerts = drift_alerts(base, outage_week, [60] * 50, [62] * 50, [("d1", 0.9), ("d2", 0.9)])
    assert alerts and alerts[0].startswith("category drift")


def test_provider_drift_alert():
    alerts = drift_alerts(["billing"] * 10, ["billing"] * 10, [60], [60], [("d1", 0.91), ("d2", 0.9), ("d3", 0.8)])
    assert alerts == ["provider drift on d3: golden set score 0.8"]
