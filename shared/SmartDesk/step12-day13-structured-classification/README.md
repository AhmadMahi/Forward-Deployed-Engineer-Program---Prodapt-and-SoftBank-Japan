# SmartDesk step 12 (Day 13): Structured classification

**Increment:** Category classification with structured output and prompt templates

**Day folder:** [../../../Day13-Prompt-Engineering/](../../../Day13-Prompt-Engineering/) (see `Day13_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 11](../step11-day12-llm-summary-token-log/) | Next: [step 13](../step13-day15-pytest-and-csv-etl/)

## Goal

Classify every ticket into a category and priority with a JSON Schema output, validated by Pydantic.

## What changed from the previous step

Adds prompt templates (stable text first for caching, ticket text last as data) and a structured-output classifier.

## Key files

- `prompts.py`: system prompt, user template, JSON Schema
- `classifier.py`: online structured output, offline rules, validation
- `test_classifier.py`: schema, accuracy and injection-awareness tests

## How to run

```bash
python -c "from classifier import classify; print(classify('I was charged twice'))"
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
