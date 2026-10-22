# Day 28: App Build Prompts

**App of the day:** Guardrail Gateway for LLM Apps (FastAPI middleware + red-team suite)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 28. A reusable safety layer you can put in front of any LLM feature, with tests that run on every release.

---

## Prompt 1: Build the gateway

```text
You are a senior AI security engineer. Build a "Guardrail Gateway" as a FastAPI service that sits in front of an LLM:
POST /chat {user_id, message, documents[]} ->
1. input checks: injection score (regex signals + optional moderation API), length limits, per-user rate limit
2. context checks: scan each document, quarantine suspicious ones, wrap the rest in <document> tags
3. model call with a system prompt that holds no secrets and states the instruction hierarchy
4. output checks: secrets list, PII redaction (email, Indian and Japanese phone formats, card numbers with a Luhn check), blocked topics
5. response with an audit record (what was blocked and why)
Offline stand-in model for tests. Configuration in a YAML policy file.
```

---

## Prompt 2: Action approvals

```text
Add an /actions endpoint where agents submit proposed tool calls. Score risk from a policy file (tool, amount thresholds, data sensitivity),
auto-run low risk, queue medium risk for review, block high risk until approved via /approvals/{id}. Store everything in SQLite with an audit log.
Include tests for unknown tools defaulting to high risk.
```

---

## Prompt 3: Red-team regression suite

```text
Write a PyTest red-team suite for the gateway: 30 attack prompts across direct injection, indirect injection in documents,
role play and obfuscation (describe categories; keep examples generic and non-harmful), and 30 benign prompts that look similar.
Assert block rate >= 90% and false alarm rate <= 10%, and print a report of misses. Explain how to add new findings as tests.
```

---

## Stretch ideas (try on your own)

- Add a counterfactual fairness test endpoint.
- Add a kill switch that disables the model call instantly.
- Visualise blocked requests per day on a small dashboard.
