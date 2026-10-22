# Day 15: App Build Prompts

**App of the day:** Tested Order Ingestion Service (pandas ETL + FastAPI + PyTest)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 15. Combines an ETL pipeline, an API on top of the clean data, and a full test suite.

---

## Prompt 1: Build the pipeline

```text
You are a senior data engineering mentor. Build an "Order Ingestion Service" in Python.
Pipeline (pipeline.py), each step a small pure function:
- extract_csv(path) and extract_json(path) for two sources with slightly different column names
- standardise columns, strip whitespace, parse mixed date formats, coerce amounts to numbers,
  drop rows with missing or non-positive amounts, drop duplicate order_id
- load_incremental(df, conn) into SQLite that is idempotent (skip existing order_id) and returns counts
- a run log table pipeline_runs(run_at, source, rows_in, rows_loaded, rows_rejected)
Provide sample messy input files. Then an API (api.py, FastAPI) with GET /orders (filters city, date range),
GET /stats/daily and POST /ingest that triggers the pipeline.
```

## Prompt 2: Draft the test suite from the rules (NEW v4)

```text
Write a PyTest suite for the Order Ingestion Service. Base every expected value on these rules, not on the current code:
- amounts must be numbers > 0; rows with missing or non-positive amounts are rejected
- order_id is unique after a load; running ingest twice loads 0 new rows the second time
- dates in 2026-11-02 and 02/11/2026 formats both parse to 2026-11-02 (day first)
Include: unit tests for each transform with @pytest.mark.parametrize, a fixture that creates a temporary SQLite
database (tmp_path) per test, data quality tests, and API tests with TestClient using dependency_overrides.
Do not change pipeline.py or api.py. List any rule you think the code breaks instead of "fixing" the test.
```

**Review step:** run `pytest -q`. For every failing test, decide whether the test or the code is wrong, using the rules above. Write one line per decision in `REVIEW.md`.

## Prompt 3: Explain ETL vs ELT in my code

```text
Rewrite the transform step as ELT: load raw rows into raw_orders, then a SQL script creates orders_clean.
Compare the two approaches for this project in a short table (speed, flexibility, replay, testing) and give 5 quiz questions with answers.
```

---

## SmartDesk step 13: PyTest suite and legacy CSV import (ETL)

```text
SmartDesk step 13.
1. tests/test_tickets_api.py: TestClient tests for every ticket endpoint, including 404, 422 and the
   offline summarise and classify endpoints from Days 12 and 13. A fixture gives each test a fresh SQLite database.
2. app/legacy_import.py: ETL from the old helpdesk export (legacy_tickets.csv) into the tickets table.
   Strip spaces, lowercase priority, parse mixed dates (day first), drop rows with missing minutes, skip existing ticket_id.
3. tests/test_quality.py: unique ticket_id, priority in {low, medium, high}, minutes >= 0, import is idempotent.
Draft the tests from these rules first and show them to me before writing app/legacy_import.py.
Run pytest -q with OFFLINE=1 and show the result.
```

**Review checklist before you commit:** every test has a real assertion; expected values come from the rules; the import is idempotent; no customer data or secrets in prompts; you can explain every line Codex wrote.

## Stretch ideas (try on your own)

- Add a JSON source with nested customer objects and flatten it with pandas.json_normalize.
- Write rejected rows to rejects.csv with a reason column.
- Add pytest-cov and find one line your tests never run.
