# Day 35 Hotel Lab: Observability, Drift and Optimisation

**Total time:** 105 to 120 minutes | **Day:** Mon 14 Dec 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- No API key? Every cell runs in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read, including the capstone hand-off section. | `Day35_PostRead_Observability_Drift_and_Optimisation_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then add structured logs and a token-per-trace metric; inject drift into sample data and detect it. | `Day35_Observability_Drift_and_Optimisation_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (observability and drift). Stretch problem optional. | `Day35_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: monitoring and drift questions. | `Day35_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 30: drift watch and capstone hand-off. OpenAI Codex allowed; review every line. | `Day35_App_Build_Prompts.md` |

## Submit

A **monitoring screenshot** (the dashboard charts or your cost-per-trace table) and one **drift alert** (the weekly report showing a breached metric).

## Stuck?

- `ModuleNotFoundError: opentelemetry`: run the install cell again, then **Runtime > Restart session**.
- Spans list is empty: run the span cell after the helpers cell; spans are exported only when each `with` block ends.
- Drift numbers differ slightly from the sample: the data is random but seeded. Rerun from the top to match.
- Offline hit rates look low: the offline embeddings are a simple stand-in. Compare experiments with each other, not with real quality.
