# SmartDesk step 20 (Day 23): Patch and modernise the legacy CSV module

**Increment:** Patch and modernise SmartDesk's legacy CSV module (SME assignment); map SmartDesk to a maturity level

**Day folder:** [../../../Day23-Industry-Use-Cases-and-Agentic-Security-SME/](../../../Day23-Industry-Use-Cases-and-Agentic-Security-SME/) (see `Day23_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 19](../step19-day22-hybrid-search-rerank/) | Next: [step 21](../step21-day25-slm-llm-routing-cost/)

## Goal

Use scans, characterisation tests and OpenAI Codex to replace an unsafe legacy module in small, verified steps, and place SmartDesk on the GenAI maturity scale.

## What changed from the previous step

Adds the legacy module as found, a modern replacement, characterisation and security tests, and a note covering findings, approach, maturity level and service offer.

## Key files

- `legacy/csv_import_legacy.py`: the unsafe original (kept for the tests)
- `modern/csv_import.py`: the modernised module
- `tests/test_characterisation.py`: same behaviour for valid rows, safe behaviour for bad rows
- `PATCH_AND_MODERNISE_NOTE.md`: findings, approach, maturity level, service note

## How to run

```bash
bandit -r legacy modern
python -m pytest -q
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
