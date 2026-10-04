# Day 34: App Build Prompts

**App of the day:** LLM Observability Starter Kit (logs, traces, dashboard, feedback)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 34. Drop-in instrumentation and a monitoring dashboard for your capstone application.

---

## Prompt 1: Instrumentation library

```text
You are a senior observability engineer. Build a Python module "llm_obs":
- log_event(**fields) writing JSON lines with ts, request_id, release, prompt_id, model, tokens, latency, retrieved ids, guardrail result,
  with PII masking and a never-log list for secrets
- a span() context manager and a Trace object that records nested spans; optional export to OpenTelemetry if installed
- a FastAPI middleware that creates a request id, starts a trace, and logs the outcome
- POST /feedback {request_id, thumbs, comment} stored and linked to the request
Include tests for masking, nesting and middleware.
```

---

## Prompt 2: Dashboard and alerts

```text
Build a monitoring dashboard (FastAPI + React) over the JSON logs: requests, p50/p95 latency, error rate by type, cost per feature,
thumbs-down rate, "I don't know" rate, guardrail blocks, all by day and by release. Add alert rules in YAML (metric, window, threshold or relative change, owner, runbook URL)
evaluated every 5 minutes, with a list of active alerts on the dashboard.
```

---

## Prompt 3: Review queue

```text
Add a review queue page: thumbs-down and escalated requests with the question, retrieved chunks, answer and trace; reviewers label the failure
(missing document, retrieval miss, hallucination, too long, unsafe) and optionally write the correct answer, which exports to the golden set JSONL with owner and date.
```

---

## Stretch ideas (try on your own)

- Group failures by label per week to show improvement.
- Sample full prompts for 5% of traffic only.
- Add a service level objective panel with error budget.
