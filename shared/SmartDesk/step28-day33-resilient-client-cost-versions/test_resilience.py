import pytest

from registry import RELEASES, check_release, cost_by_version, prompt_hash
from resilient_client import CircuitBreaker, CircuitOpen, ResilientClient, TransientError


def flaky(fail_times):
    state = {"n": 0}

    def call(prompt):
        state["n"] += 1
        if state["n"] <= fail_times:
            raise TransientError("429 rate limit")
        return "ok", {"input_tokens": 10, "output_tokens": 2}
    return call


def test_retries_then_succeeds():
    c = ResilientClient([("primary", flaky(2))], sleep=lambda s: None)
    assert c.complete("hi")["attempts"] == 3


def test_falls_back_to_second_model():
    c = ResilientClient([("primary", flaky(99)), ("fallback", flaky(0))], sleep=lambda s: None)
    assert c.complete("hi")["model"] == "fallback"


def test_all_down_raises_friendly_error():
    with pytest.raises(CircuitOpen):
        ResilientClient([("a", flaky(99))], sleep=lambda s: None).complete("hi")


def test_circuit_breaker_opens_and_resets():
    now = [0.0]
    b = CircuitBreaker(failures=2, reset_after=10, clock=lambda: now[0])
    b.record(False), b.record(False)
    assert not b.allow()
    now[0] = 11
    assert b.allow()


def test_registry_blocks_retired_models():
    assert check_release(RELEASES["2026.12.1"]) == []
    assert check_release({**RELEASES["2026.12.1"], "model": "gpt-5.5"})
    assert len(prompt_hash("summarise-v3")) == 12


def test_cost_by_version():
    log = [{"release": "r1", "model": "m", "input_tokens": 100, "output_tokens": 50, "est_cost": 0.001}] * 3
    assert cost_by_version(log)[("r1", "m")] == {"calls": 3, "tokens": 450, "est_cost": 0.003}
