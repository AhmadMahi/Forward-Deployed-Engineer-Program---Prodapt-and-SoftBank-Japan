# Day 30: App Build Prompts

**App of the day:** LLM Quality Gate for CI (golden sets + regression tests + reports)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 30. A reusable evaluation harness you can drop into any GenAI project and pipeline.

---

## Prompt 1: Evaluation harness

```text
You are a senior LLM QA engineer. Build "llm-gate", a Python package and CLI:
- golden/*.jsonl with schema validation (Pydantic): id, question, expected, must_include, must_not_include, relevant_ids, tags, version, owner
- adapters: call a FastAPI endpoint (POST /ask) or import a Python function
- deterministic checks (phrases, JSON validity, max length), retrieval metrics (precision, recall, average precision at k),
  optional model-graded checks (faithfulness and correctness rubrics) behind a flag
- BLEU and ROUGE-L for translation or summary suites only
- report.json and report.md with per-item results, per-tag slices and regressions versus a baseline report
- exit code 1 when thresholds in gate.yaml fail
Include tests and a sample golden set.
```

---

## Prompt 2: CI integration

```text
Write an Azure Pipelines stage "Evaluate" that installs llm-gate, runs the fast suite on every pull request and the full suite on main,
uses the API key from a secret variable group, compares with the baseline report from the last successful main run (pipeline artifact),
publishes report.md as an artifact and comments a summary on the pull request. Explain each step.
```

---

## Prompt 3: Golden set governance

```text
Write a one-page guide for maintaining golden datasets on a customer project: who owns items, how to add production failures,
review rules, versioning and change logs, how to retire outdated items when policies change, and how to keep sensitive data out.
```

---

## Stretch ideas (try on your own)

- Run each model-graded item 3 times and use the median to reduce noise.
- Track evaluation cost per run.
- Plot pass rate across the last 20 pipeline runs.
