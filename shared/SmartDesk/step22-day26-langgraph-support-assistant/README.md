# SmartDesk step 22 (Day 26): Support assistant with tools in a LangGraph flow

**Increment:** Support assistant with tools in a LangGraph flow

**Day folder:** [../../../Day26-LLM-Orchestration-Tools-and-LangGraph/](../../../Day26-LLM-Orchestration-Tools-and-LangGraph/) (see `Day26_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 21](../step21-day25-slm-llm-routing-cost/) | Next: [step 23](../step23-day27-agentic-crag-memory/)

## Goal

Turn SmartDesk into a support assistant that uses tools inside a LangGraph workflow, with a human approval step for refunds.

## What changed from the previous step

Adds narrow, validated tools, a stateful graph with conditional routing, a checkpointer for durable execution and an interrupt for human-in-the-loop approval.

## Key files

- `tools.py`: lookup_ticket, check_outage, create_refund_request
- `graph.py`: LangGraph flow with interrupt
- `test_graph.py`: routing, approval and rejection tests

## How to run

```bash
python graph.py
```

## How to test

```bash
python -m pytest -q
```

## Graph

```
START -> load -> classify -> network ----------------------> respond -> END
                          -> billing -> [human approval] ---> respond
                          -> other -------------------------> respond
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
