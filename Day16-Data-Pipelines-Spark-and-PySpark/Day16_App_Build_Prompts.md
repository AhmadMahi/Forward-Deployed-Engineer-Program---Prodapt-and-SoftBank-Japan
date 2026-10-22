# Day 16: App Build Prompts

**Apps of the day:** Retail Sales Batch Pipeline (PySpark, medallion layers) and Sales Insights Pipeline with a SQL Question Bank (PySpark + Spark SQL + FastAPI)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 16. A batch pipeline from raw files to gold tables, a bank of business questions in SQL, and a small API that serves the results.

---

## Prompt 1: Build the pipeline

```text
You are a senior data engineer mentoring beginners. Build a PySpark batch pipeline project "retail_pipeline".
Must run locally with master local[1] (Python 3.12+, pyspark, Java 17) and in Google Colab.

Structure:
  data/raw/ (generate sample CSVs: orders with duplicates, nulls, bad amounts, untrimmed cities; customers; products)
  pipeline/config.py      (paths, explicit schemas as DDL strings, quality thresholds)
  pipeline/bronze.py      (read raw with explicit schemas, add ingest_date, write Parquet)
  pipeline/silver.py      (dedupe, validate, trim, cast dates; write rejects with a reason column)
  pipeline/gold.py        (daily revenue by city and category with spark.sql; top product per day with RANK; day-over-day change with LAG)
  pipeline/checks.py      (not_empty, unique_key, reconciliation; raise PipelineError)
  pipeline/run.py         (runs all layers for a given --date, logs row counts per step to a run_log table, idempotent overwrite per partition)
Every function takes and returns DataFrames so it is easy to test. Add clear comments.
```

## Prompt 2: Tests and SQL question bank

```text
1. Write PyTest tests for every function in silver.py, gold.py and checks.py with a session-scoped SparkSession
   fixture (local[1]) and tiny DataFrames. Cover: duplicates removed, invalid amounts rejected with the right reason,
   unknown customers kept as "unknown", gold totals match a hand-calculated example, re-running gives identical counts.
2. Create questions.sql with 8 business questions as comments, each followed by a Spark SQL query against the gold tables
   (using WHERE, GROUP BY, HAVING, JOIN, a CTE and a window function at least once each), and a script that runs them all.
```

## Prompt 3: Serve the gold tables

```text
Add a small FastAPI app that reads the gold Parquet tables with pandas (pyarrow) and exposes
GET /revenue/daily?city=&from=&to=, GET /revenue/top-cities?date=, and GET /pipeline/runs. Include TestClient tests and explain
why we serve precomputed gold tables instead of running Spark per request.
```

## Prompt 4: Generate one transformation, then verify it (NEW v4)

```text
Write a PySpark function customer_lifetime_value(silver_orders, customers) for gold.py.
Rules: only orders with amount > 0; duplicate order_id counts once; customers with no orders appear with 0;
output customer_id, name, orders, total, avg_order rounded to 2 decimals. Use pyspark.sql.functions only, no UDFs.
Do not change any other file.
```

**Verify before you keep it:** build a golden example of 5 to 8 rows with the answer worked out by hand, compare row counts before and after each join, reconcile the total with silver, and check one number with pandas. Write a one-line verdict (keep, fix or reject) in `REVIEW.md`.

---

## SmartDesk step 14: PySpark SLA metrics pipeline

```text
SmartDesk step 14. Build smartdesk_pipeline/ with PySpark (local[1]).
1. bronze: read the ticket events export (ticket_id, priority, opened_at, resolved_at, agent_id) as received.
2. silver: drop duplicate ticket_id, trim and lowercase priority, parse timestamps, keep unresolved tickets with a flag.
3. gold: sla_metrics per priority per day: tickets, met (resolved within high=60, medium=240, low=1440 minutes,
   on the boundary counts as met), pct_met rounded to 1 decimal. Write Parquet partitioned by day with overwrite.
4. checks: not empty, unique ticket_id in silver, gold tickets equal resolved silver tickets.
5. tests/test_sla.py: a golden example with a duplicate, an unresolved ticket and a ticket exactly on the SLA.
Write the golden test first and show it to me before writing gold.py.
```

**Review checklist before you commit:** the golden example was worked out by hand; counts are printed after each step; re-running a day gives the same output; you can explain every line Codex wrote.

## Stretch ideas (try on your own)

- Generate 2 million synthetic orders and compare run time with 1 vs 4 shuffle partitions.
- Add a data quality summary table to the gold layer.
- Use `df.explain()` and explain where the shuffles happen.
