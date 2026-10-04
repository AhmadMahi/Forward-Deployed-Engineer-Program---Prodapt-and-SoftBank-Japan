# Day 16: App Build Prompts

**App of the day:** Sales Insights Pipeline with a SQL Question Bank (PySpark + Spark SQL + FastAPI)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Consolidates Weeks 1 to 3: a production-style Spark pipeline, SQL gold tables, tests, and a small API to serve the results.

---

## Prompt 1: Production pipeline

```text
You are a senior data engineer. Turn a prototype PySpark job into a production-style pipeline "sales_insights".
- config.py: paths, DDL schemas, quality thresholds
- layers.py: read_bronze(run_date), to_silver, to_gold (gold built with spark.sql from temp views: daily revenue by city and segment,
  top product per day with RANK, day-over-day change with LAG)
- checks.py: not_empty, unique_key, valid_ranges (rejects to a separate table with reason), reconciliation; raise PipelineError
- run.py: argparse --date and --backfill-from/--backfill-to; dynamic partition overwrite; a run_log Parquet table
Generate realistic sample data for 30 days. Include a README with run commands for Colab and local.
```

---

## Prompt 2: Tests and SQL question bank

```text
1. Write PyTest tests for every function in layers.py and checks.py with a session-scoped local SparkSession and tiny DataFrames.
2. Create questions.sql with 8 business questions as comments, each followed by a Spark SQL query against the gold tables
(using WHERE, GROUP BY, HAVING, JOIN, a CTE and a window function at least once each), and a Python script that runs them all and prints results.
```

---

## Prompt 3: Serve the gold tables

```text
Add a small FastAPI app that reads the gold Parquet tables with pandas (pyarrow) and exposes
GET /revenue/daily?city=&from=&to=, GET /revenue/top-cities?date=, and GET /pipeline/runs. Include TestClient tests and explain
why we serve precomputed gold tables instead of running Spark per request.
```

---

## Stretch ideas (try on your own)

- Add a backfill command that reruns a date range.
- Add an alert (printed message or email stub) when a quality check fails.
- Visualise daily revenue with Matplotlib from the gold table.
