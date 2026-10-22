# Day 35: App Build Prompts

**Apps of the day:** LLM Observability Starter Kit + Drift Watch

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 35. Drop-in instrumentation, a monitoring dashboard and a scheduled drift and eval job that every capstone team can reuse.

---

## Prompt 1: Instrumentation library with OpenTelemetry GenAI spans (NEW v4)

```text
You are a senior observability engineer mentoring beginners. Build a Python module "llm_obs":
- log_event(**fields) writing JSON lines with ts, request_id, release, prompt_id, model, tokens, latency, retrieved ids and guardrail result,
  with PII masking and a never-log list for secrets.
- OpenTelemetry tracing with the opentelemetry-sdk: a root span per request and child spans for retrieval, model calls and tool calls.
  Use the GenAI semantic convention attributes (gen_ai.operation.name, gen_ai.request.model, gen_ai.response.model,
  gen_ai.usage.input_tokens, gen_ai.usage.output_tokens). Add a comment: check the current spec version. Prompt content capture off by default.
- cost_per_trace(spans, prices) that sums tokens per trace id; prices from prices.yaml marked as PLACEHOLDER.
- A FastAPI middleware that creates a request id, starts the root span, and logs the outcome. POST /feedback {request_id, thumbs, comment}.
Tests: masking, span attributes, cost per trace, middleware. Use the in-memory span exporter in tests.
```

## Prompt 2: Dashboard and alerts

```text
Build a monitoring dashboard (FastAPI + React) over the logs and spans: requests, p50/p95 latency, error rate by type, cost per trace and per
feature, thumbs-down rate, "I don't know" rate and guardrail blocks, all by day and by release. Add alert rules in YAML (metric, window,
threshold or relative change, owner, runbook URL) and a list of active alerts. Include a cost runaway rule: cost per trace above 3x the median.
```

## Prompt 3: Drift Watch with provider and model drift (NEW v4)

```text
Build "drift-watch" in Python:
- Input: request logs (JSONL) with question, topic, lang, tokens, latency, feedback, release, requested_model and response_model.
- Per period vs a reference period: PSI for numeric and categorical fields, KS test for numeric fields, embedding centroid drift
  (OpenAI embeddings when a key is set, hashing stand-in offline), and topic clusters of new questions.
- Provider and model drift: detect when response_model changes while requested_model stays the same, and compare output tokens and
  golden pass rate before and after.
- Golden set hook (import the Day 32 quality gate). Thresholds in YAML. Output report.md and report.json; exit code 1 on breaches.
Tests with synthetic data where drift is planted and where it is not (to check false alarms).
```

## Prompt 4: Scheduled evals in CI or as a Codex automation (NEW v4)

```text
Write an Azure DevOps scheduled pipeline (weekly, Monday 03:00) that runs drift-watch and the golden set, publishes the report as an
artifact, and opens a work item when thresholds are breached. The OpenAI key comes from a secret variable; the job also runs with OFFLINE=1.
Then write the prompt for a Codex automation that runs the same job weekly, posts a short summary, and opens a draft issue on a breach
without changing prompts, code or data. Explain each YAML block.
```

---

## SmartDesk step 30: Observability and drift watch; capstone hand-off

```text
SmartDesk step 30. Using the work above:
1. Instrument every SmartDesk request with OpenTelemetry GenAI spans and log cost per trace.
2. Add the dashboard page and three alert rules with owners and runbook links.
3. Add the weekly drift and eval job (CI schedule) and save the first report in docs/reports/.
4. Capstone hand-off: update README.md (architecture, how to run offline, how to deploy), AGENTS.md (build, test, style, folders not to touch,
   never put secrets in prompts), the decision log, and the runbooks from Days 33 and 34.
5. All tests pass with OFFLINE=1. Show me the diff and a three-line summary.
```

**Review checklist before you commit:** no secrets or raw personal data in logs or spans; prices labelled as placeholders; every alert has an owner; the scheduled job only opens reviews and never changes code by itself; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Name new topic clusters with an LLM and suggest missing documents.
- Track metrics week over week in a trend chart.
- Sample full prompts for 5% of traffic only, with masking.
