# Day 30: App Build Prompts

**App of the day:** Guardrail Gateway for LLM Apps (FastAPI middleware + red-team suite), with vulnerability report v3

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.
6. Only attack systems you own or are authorised to test. Keep attack examples generic and non-harmful.

> Uses Days 1 to 30. A reusable safety layer you can put in front of any LLM feature, with agent identity, approval gates and tests that run on every release.

---

## Prompt 1: Build the gateway

```text
You are a senior AI security engineer. Build a "Guardrail Gateway" as a FastAPI service that sits in front of an LLM:
POST /chat {user_id, message, documents[], tool_results[]} ->
1. input checks: injection score (regex signals + optional moderation API), length limits, per-user rate limit
2. context checks: scan each document and tool result, strip hidden markup (HTML comments), quarantine suspicious items,
   wrap the rest in <document> or <tool_result> tags
3. model call with a system prompt that holds no secrets and states the instruction hierarchy
4. output checks: secrets list, PII redaction (email, Indian and Japanese phone formats, card numbers with a Luhn check), blocked topics
5. response with an audit record (what was blocked and why)
Offline stand-in model for tests (OFFLINE=1). Model name from LLM_MODEL. Configuration in a YAML policy file.
```

---

## Prompt 2: Agent identity and approval gates

```text
Add agent identity to the gateway.
- POST /agent-tokens issues a JWT for a registered agent: sub = agent id, scope list, aud = "smartdesk-api", expiry 5 minutes.
  The signing key comes from an environment variable (later Key Vault), never from code.
- Every tool endpoint calls require(token, scope) and rejects expired, wrong-audience or missing-scope tokens.
- /actions: agents submit proposed tool calls. Score risk from the policy file (tool, amount thresholds, data sensitivity),
  auto-run low risk, queue medium risk for review, block high risk until approved via /approvals/{id}.
  Tools not in the policy are blocked (fail closed).
- Store decisions in SQLite with an audit log that includes the agent id.
Tests: expired token, wrong scope, unknown tool, refund above the limit.
```

---

## Prompt 3: Red-team regression suite and vulnerability report v3

```text
Write a PyTest red-team suite for the gateway: 30 attack prompts across direct injection, indirect injection in documents
and tool results, role play and obfuscation (describe categories; keep examples generic and non-harmful), and 30 benign
prompts that look similar. Assert block rate >= 90% and false alarm rate <= 10%, and print a report of misses.
Then write scripts/vuln_report.py that turns the failures and fixes into vulnerability_report_v3.md using the columns in
shared/templates/Vulnerability_Report_Template.md (ID, finding, tool, severity, affected file, proposed fix, fixed by,
verified, evidence). Explain how to add new findings as tests.
```

---

## Prompt 4: Brownfield step with tests first

```text
In the legacy module app/legacy/refunds.py, do NOT change behaviour yet.
1. Write characterisation tests that pin the current behaviour, including surprising cases.
2. Propose a plan of small refactor steps. Wait for my approval.
3. Do step 1 only, show the diff, and run the tests, bandit and pip-audit.
```

---

## SmartDesk step 25: Guardrail gateway and red-team suite

```text
SmartDesk step 25. Put the guardrail gateway in front of every SmartDesk LLM call:
1. The support assistant calls tools only with scoped, short-lived agent tokens.
2. Refunds over the policy limit and account changes need human approval.
3. The red-team suite runs in CI and fails the build below the thresholds.
4. Write vulnerability_report_v3.md with at least four findings, each with evidence and verified yes or no.
5. Update AGENTS.md with the security test command.
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** no secret in any prompt or system message; signing key from the environment; unknown tools fail closed; red-team tests pass offline; every finding in report v3 has evidence; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Add a counterfactual fairness test endpoint.
- Add a kill switch that disables the model call and revokes all agent tokens instantly.
- Visualise blocked requests per day on a small dashboard.
