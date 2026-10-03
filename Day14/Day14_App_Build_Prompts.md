# Day 14: App Build Prompts

**App of the day:** Retail Sales Batch Pipeline (PySpark, medallion layers)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 13 and 14. A real batch pipeline structure you will extend with SQL on Day 16.

---

## Prompt 1: Build the pipeline

```text
You are a senior data engineer mentoring beginners. Build a PySpark batch pipeline project "retail_pipeline".
Must run locally with master local[*] (Python 3.10+, pyspark, Java 17) and in Google Colab.

Structure:
  data/raw/ (generate sample CSVs: orders with duplicates, nulls, bad amounts, untrimmed cities; customers; products)
  pipeline/config.py      (paths, explicit schemas as DDL strings)
  pipeline/bronze.py      (read raw with explicit schemas, add ingest_date, write Parquet)
  pipeline/silver.py      (dedupe, validate, trim, cast dates; write rejects with a reason column)
  pipeline/gold.py        (daily revenue by city and category; customer lifetime value; top product per day with a window)
  pipeline/run.py         (runs all layers for a given --date, logs row counts per step, idempotent with overwrite per partition)
Every function takes and returns DataFrames so it is easy to test. Add clear comments.
```

---

## Prompt 2: Test the transformations

```text
Write PyTest tests for the silver and gold functions using a session-scoped SparkSession fixture (local[1])
and tiny DataFrames built with spark.createDataFrame. Cover: duplicates removed, invalid amounts rejected with the right reason,
join keeps unknown customers as "unknown", gold totals match a hand-calculated example, re-running gives identical counts.
```

---

## Prompt 3: Explain the plan

```text
For the gold daily revenue job, show df.explain() output and explain in plain English where the shuffles happen,
why the broadcast join helps, and two changes that would make it faster. Then 5 quiz questions with answers.
```

---

## Stretch ideas (try on your own)

- Generate 2 million synthetic orders and compare run time with 1 vs 4 shuffle partitions.
- Add a data quality summary table to the gold layer.
- Convert the gold output to Delta Lake format (research task).
