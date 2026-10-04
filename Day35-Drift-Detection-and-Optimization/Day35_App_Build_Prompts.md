# Day 35: App Build Prompts

**App of the day:** Drift Watch: automated drift and quality monitoring

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 35. A scheduled job and small dashboard that every capstone team can reuse to watch drift and quality.

---

## Prompt 1: Drift engine

```text
You are a senior LLMOps engineer. Build "drift-watch" in Python:
- input: request logs (JSONL) with question, topic, lang, tokens, latency, feedback, release
- metrics per period vs a reference period: PSI for numeric and categorical fields, KS test for numeric fields, embedding centroid drift
  (OpenAI embeddings when a key is set, hashing stand-in offline), topic clustering of new questions with k-means and example questions per cluster
- golden set evaluation hook (import the Day 30 quality gate)
- thresholds in YAML; output report.md and report.json; exit code 1 on breaches
Include tests with synthetic data where drift is planted and where it is not (to check false alarms).
```

---

## Prompt 2: Optimisation runner

```text
Add an experiments runner: given a list of configurations (k, chunk size, prompt version, model, added documents), run the golden set for each,
report quality, cost and latency in one table, and highlight the best configuration that meets a cost budget. Enforce one change per experiment against the baseline.
```

---

## Prompt 3: Schedule and report

```text
Write an Azure DevOps scheduled pipeline that runs drift-watch weekly, publishes the report as an artifact, posts a summary to a Teams channel webhook
(placeholder URL from a secret variable), and opens a work item when thresholds are breached. Explain each YAML block.
```

---

## Stretch ideas (try on your own)

- Name new topic clusters with an LLM and suggest missing documents.
- Track metrics week over week in a trend chart.
- Automatically re-run ingestion when source documents change.
