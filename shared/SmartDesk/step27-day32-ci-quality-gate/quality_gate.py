"""SmartDesk step 27: an LLM quality gate for CI. Fails the build when quality drops or cost rises.

Usage: python quality_gate.py metrics.json baseline.json   (exit code 1 on failure)
"""
import json
import sys

from token_cost import cost

TOOL_SCHEMAS = {"lookup_ticket": {"ticket_id": int}, "check_outage": {"area": str},
                "create_refund_request": {"ticket_id": int, "amount_jpy": int}}


def tool_call_ok(call, expected_name):
    """Tool-call fidelity: right tool, all required arguments, right types, nothing extra."""
    schema = TOOL_SCHEMAS.get(call.get("name"))
    if call.get("name") != expected_name or schema is None:
        return False
    args = call.get("args", {})
    return set(args) == set(schema) and all(isinstance(args[k], t) for k, t in schema.items())


def compute_metrics(results):
    """results: list of dicts with correct, input_tokens, output_tokens, latency_ms, tool_call, expected_tool."""
    n = len(results)
    lat = sorted(r["latency_ms"] for r in results)
    tool_rows = [r for r in results if r.get("expected_tool")]
    return {"accuracy": round(sum(r["correct"] for r in results) / n, 3),
            "cost_per_query": round(sum(cost(r["input_tokens"], r["output_tokens"]) for r in results) / n, 6),
            "p95_latency_ms": lat[min(n - 1, int(0.95 * n))],
            "tool_call_fidelity": round(sum(tool_call_ok(r["tool_call"], r["expected_tool"]) for r in tool_rows)
                                        / len(tool_rows), 3) if tool_rows else 1.0}


def gate(metrics, baseline):
    failures = [f"{k} {metrics[k]} < {v}" for k, v in baseline["min"].items() if metrics[k] < v]
    failures += [f"{k} {metrics[k]} > {v}" for k, v in baseline["max"].items() if metrics[k] > v]
    return failures


def main(argv):
    metrics, baseline = (json.load(open(p)) for p in argv[1:3])
    failures = gate(metrics, baseline)
    for k, v in metrics.items():
        print(f"{k:<20} {v}")
    print("QUALITY GATE:", "FAIL\n  " + "\n  ".join(failures) if failures else "PASS")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
