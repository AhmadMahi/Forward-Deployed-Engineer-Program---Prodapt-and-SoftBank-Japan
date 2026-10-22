import json

from quality_gate import compute_metrics, gate, main, tool_call_ok

BASE = json.load(open("baseline.json"))


def results(correct=9, out_tokens=200, bad_tool=False):
    rows = [{"correct": i < correct, "input_tokens": 1200, "output_tokens": out_tokens, "latency_ms": 400 + i * 50,
             "tool_call": {"name": "lookup_ticket", "args": {"ticket_id": "7" if bad_tool else 7}},
             "expected_tool": "lookup_ticket"} for i in range(10)]
    return rows


def test_gate_passes_on_good_run():
    assert gate(compute_metrics(results()), BASE) == []


def test_gate_fails_when_accuracy_drops():
    assert any("accuracy" in f for f in gate(compute_metrics(results(correct=6)), BASE))


def test_gate_fails_when_cost_rises():
    assert any("cost_per_query" in f for f in gate(compute_metrics(results(out_tokens=900)), BASE))


def test_tool_call_fidelity():
    assert tool_call_ok({"name": "check_outage", "args": {"area": "shibuya"}}, "check_outage")
    assert not tool_call_ok({"name": "check_outage", "args": {"area": "x", "extra": 1}}, "check_outage")
    assert any("tool_call_fidelity" in f for f in gate(compute_metrics(results(bad_tool=True)), BASE))


def test_cli_exit_codes(tmp_path):
    good, bad = tmp_path / "g.json", tmp_path / "b.json"
    good.write_text(json.dumps(compute_metrics(results())))
    bad.write_text(json.dumps(compute_metrics(results(correct=5))))
    assert main(["x", str(good), "baseline.json"]) == 0
    assert main(["x", str(bad), "baseline.json"]) == 1
