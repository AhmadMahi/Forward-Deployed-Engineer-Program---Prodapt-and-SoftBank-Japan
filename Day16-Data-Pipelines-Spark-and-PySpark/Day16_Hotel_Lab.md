# Day 16 Hotel Lab: Data Pipelines, Spark and PySpark

**Total time:** 105 to 120 minutes | **Day:** Tue 17 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells; you need Java 17 for local PySpark).
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day16_PostRead_Data_Pipelines_Spark_and_PySpark_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then run the medallion pipeline, add one aggregation and one Spark SQL query. | `Day16_Data_Pipelines_Spark_and_PySpark_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (DataFrame, join and batch pipeline). Stretch set optional. | `Day16_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: Spark concepts and SQL code boxes. | `Day16_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 14: SLA metrics pipeline. OpenAI Codex allowed; review every line. | `Day16_App_Build_Prompts.md` |

## Submit

Your **pipeline output table**: the gold table from your run (a screenshot or `show()` output), with the row counts for bronze, silver and gold.

## Stuck?

- `JAVA_HOME is not set` in VS Code: install Java 17 and restart the terminal. Colab does not need this.
- Spark is slow the first time: starting the JVM takes a few seconds. Later cells are faster.
- Counts change after a join: check for duplicate keys in the right-hand table.
- Gold count grows on every re-run: you used `mode("append")`. Use `overwrite`.
