# Day 20: App Build Prompts

**App of the day:** Request Log Investigator (FastAPI + React mini tool)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 20. A practical FDE tool: upload request logs, test hypotheses by grouping, and export a readout.

---

## Prompt 1: Build the analysis API

```text
You are a senior full stack mentor. Build a FastAPI service "Log Investigator".
- POST /datasets: upload a CSV of request logs (ts, endpoint, tenant, region, page_size, duration_ms); validate columns; store in SQLite or memory
- GET /datasets/{id}/summary: rows, time range, overall p50/p95/p99
- GET /datasets/{id}/groupby?col=endpoint: count, median and p95 per group, sorted by p95
- GET /datasets/{id}/hourly?filter_col=endpoint&filter_val=/reports/export: p95 by hour
- POST /datasets/{id}/hypotheses: save a hypothesis text with status (open|confirmed|rejected) and evidence text
- GET /datasets/{id}/readout: Markdown readout (problem, hypotheses with verdicts, top findings)
Use pandas for the calculations. Include TestClient tests with a small generated CSV.
```

---

## Prompt 2: Build the React front end

```text
Build a React (Vite) front end for Log Investigator: upload a CSV, see the summary, choose a column to group by and see a table
sorted by p95 with the worst row highlighted in orange, an hourly p95 line chart (use a simple SVG or recharts), a hypotheses panel to add and update
hypotheses with evidence, and a "Copy readout" button. Loading, error and empty states throughout. Teal theme.
```

---

## Prompt 3: Coach me on the readout

```text
Here are my findings from the Log Investigator: <paste numbers>. Act as a skeptical customer sponsor.
First, rewrite my readout as: answer first, two pieces of evidence with numbers, recommendation, next step with owner and date.
Then ask me three tough questions a sponsor might ask, and suggest strong, honest answers.
```

---

## Stretch ideas (try on your own)

- Add a p95 comparison between two date ranges to show whether a fix worked.
- Export the readout as a Markdown file.
- Add an issue tree editor that saves branches as a nested JSON structure.
