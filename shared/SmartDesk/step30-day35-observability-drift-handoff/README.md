# SmartDesk step 30 (Day 35): Observability, drift watch and capstone hand-off

**Increment:** Observability and drift watch; capstone hand-off

**Day folder:** [../../../Day35-Observability-Drift-and-Optimisation/](../../../Day35-Observability-Drift-and-Optimisation/) (see `Day35_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 29](../step29-day34-production-gateway-canary/) | Next: [the capstone](../../../Day36-40-Capstone/)

## Goal

See what SmartDesk does in production: traces with token and cost per request, drift alerts, and a clean hand-off to the capstone.

## What changed from the previous step

Adds OpenTelemetry spans with GenAI semantic convention attributes, token and cost per trace, PSI category drift, length drift, provider drift from scheduled evals, and the capstone hand-off note.

## Key files

- `tracing.py`: OpenTelemetry GenAI spans, per-trace totals
- `drift.py`: PSI, length and provider drift
- `CAPSTONE_HANDOFF.md`: what to carry into Days 36 to 40
- `test_observability.py`: tests

## How to run

```bash
python -c "from tracing import *; print(ticket_trace('No signal', lambda p: ('ok', {'input_tokens': 9, 'output_tokens': 3})), per_trace_totals())"
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
