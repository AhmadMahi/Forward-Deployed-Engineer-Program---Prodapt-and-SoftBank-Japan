# SmartDesk step 13 (Day 15): PyTest suite and legacy CSV import

**Increment:** PyTest suite; legacy CSV import (ETL)

**Day folder:** [../../../Day15-Testing-and-Data-Engineering-Intro/](../../../Day15-Testing-and-Data-Engineering-Intro/) (see `Day15_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 12](../step12-day13-structured-classification/) | Next: [step 14](../step14-day16-pyspark-sla-metrics/)

## Goal

Import tickets from the old system with a tested ETL job, and grow the PyTest suite.

## What changed from the previous step

Adds a pandas ETL (extract, transform, load into SQLite) with data quality checks and parametrised tests. Codex may draft tests; you review them.

## Key files

- `etl_import.py`: extract, transform, load, quality report
- `tests/test_etl.py`: ETL tests
- `../data/legacy_tickets.csv`: messy input with duplicates, blanks and mixed dates

## How to run

```bash
python etl_import.py
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
