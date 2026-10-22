# SmartDesk step 27 (Day 32): Quality gate in CI with cost metrics

**Increment:** Quality gate in CI with cost metrics

**Day folder:** [../../../Day32-LLM-Evaluation-and-Quality-Gates/](../../../Day32-LLM-Evaluation-and-Quality-Gates/) (see `Day32_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 26](../step26-day31-golden-set-eval-dashboard/) | Next: [step 28](../step28-day33-resilient-client-cost-versions/)

## Goal

Stop a release when answer quality, tool-call fidelity, cost per query or latency gets worse.

## What changed from the previous step

Adds a quality gate with minimum and maximum thresholds, tool-call fidelity checks and cost per query (placeholder prices), plus the CI step that runs it.

## Key files

- `quality_gate.py`: metrics, tool-call fidelity and gate
- `baseline.json`: thresholds
- `azure-pipelines-quality-gate.yml`: CI step
- `test_quality_gate.py`: pass and fail runs

## How to run

```bash
python quality_gate.py metrics.json baseline.json
```

## How to test

```bash
python -m pytest -q
```

## Eval-first development with Codex (NEW v4)

Write or extend the golden set and the gate first, then ask Codex for the change, then run the gate. A change is done when the gate passes, not when the code compiles.

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
