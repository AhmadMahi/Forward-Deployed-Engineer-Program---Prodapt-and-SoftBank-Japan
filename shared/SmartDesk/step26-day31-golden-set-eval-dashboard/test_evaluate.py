from evaluate import dashboard, evaluate, faithfulness, load_golden, summary, trajectory_pass_k


def test_golden_set_shape():
    g = load_golden()
    assert len(g) == 12 and {r["category"] for r in g} == {"billing", "network", "account", "other"}


def test_metrics_and_slices(tmp_path):
    rows = evaluate()
    s = summary(rows)["all"]
    assert s["retrieval_hit"] >= 0.8 and s["citation_ok"] >= 0.75
    assert set(summary(rows, "category")) == {"billing", "network", "account", "other"}
    assert "Failures to analyse" in dashboard(rows, tmp_path / "d.md").read_text()


def test_faithfulness_catches_made_up_text():
    ctx = "Refunds are allowed within 14 days."
    assert faithfulness("Refunds are allowed within 14 days.", ctx) == 1.0
    assert faithfulness("Refunds are allowed within 90 days plus a free phone.", ctx) < 0.7


def test_pass_k_needs_every_run_right():
    good = ["lookup_ticket", "check_outage"]
    assert trajectory_pass_k([good, good, good], good, 3)
    assert not trajectory_pass_k([good, ["lookup_ticket"], good], good, 3)
