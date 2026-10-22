# SmartDesk step 14 (Day 16): PySpark SLA metrics

**Increment:** PySpark SLA metrics pipeline

**Day folder:** [../../../Day16-Data-Pipelines-Spark-and-PySpark/](../../../Day16-Data-Pipelines-Spark-and-PySpark/) (see `Day16_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 13](../step13-day15-pytest-and-csv-etl/) | Next: [step 15](../step15-day17-lint-tests-pipeline/)

## Goal

Compute SLA metrics per category with a small PySpark batch pipeline and a Spark SQL query.

## What changed from the previous step

Adds a bronze, silver, gold pipeline: de-duplicate events, compute resolution hours and SLA breaches, aggregate by category.

## Key files

- `sla_pipeline.py`: SparkSession, transformations, aggregation, Spark SQL
- `test_sla_pipeline.py`: pipeline tests

## How to run

```bash
python sla_pipeline.py     # Colab or a laptop with Java 17
```

## How to test

```bash
python -m pytest -q        # skipped if pyspark is not installed
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
