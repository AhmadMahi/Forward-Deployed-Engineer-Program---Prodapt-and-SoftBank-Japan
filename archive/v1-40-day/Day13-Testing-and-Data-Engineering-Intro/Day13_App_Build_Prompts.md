# Day 13: App Build Prompts

**App of the day:** Tested Order Ingestion Service (pandas ETL + FastAPI + PyTest)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 13. Combines an ETL pipeline, an API on top of the clean data, and a full test suite.

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

---

## Prompt 2: Write the test suite

```text
Write a PyTest suite for the Order Ingestion Service:
- unit tests for each transform using small DataFrames and @pytest.mark.parametrize
- a fixture that creates a temporary SQLite database (tmp_path) for each test
- an idempotency test: running ingest twice loads 0 new rows the second time
- data quality tests: unique order_id, no null amount, amounts > 0, valid dates
- API tests with TestClient using dependency_overrides to point at the temp database
Show how to run with coverage (pytest-cov).
```

---

## Prompt 3: Explain ETL vs ELT in my code

```text
Rewrite the transform step as ELT: load raw rows into raw_orders, then a SQL script creates orders_clean.
Compare the two approaches for this project in a short table (speed, flexibility, replay, testing) and give 5 quiz questions with answers.
```

---

## Stretch ideas (try on your own)

- Add a JSON source with nested customer objects and flatten it with pandas.json_normalize.
- Write rejected rows to a rejects.csv with a reason column.
- Schedule the pipeline every hour with a simple loop or the schedule library.
