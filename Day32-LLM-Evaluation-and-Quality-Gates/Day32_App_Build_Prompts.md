# Day 32: App Build Prompts

**App of the day:** LLM Quality Gate for CI (golden sets, regression and tool-call tests, cost metrics, reports)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Work **eval-first**: write or update the evals, see them fail, then ask Codex to implement until they pass.
3. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
4. Read every diff before you accept it. Run the tests and the gate after every step.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 32. A gate that stops a release when quality, tool calls or cost get worse.

---

## Prompt 1: Evaluation harness

```text
You are a senior LLM QA engineer. Build "llm-gate", a Python package and CLI:
- golden/*.jsonl with schema validation (Pydantic): id, question, expected, must_include, must_not_include, relevant_ids,
  tags, version, owner
- adapters: call a FastAPI endpoint (POST /ask) or import a Python function
- deterministic checks (phrases, JSON validity, max length), retrieval metrics (precision, recall, average precision at k),
  citation accuracy (every cited id retrieved and relevant), optional model-graded checks behind a flag
- BLEU and ROUGE-L for translation or summary suites only
- report.json and report.md with per-item results, per-tag slices and regressions versus a baseline report
- exit code 1 when thresholds in gate.yaml fail
Model name from LLM_MODEL; OFFLINE=1 runs everything without a key. Include tests and a sample golden set.
```

---

## Prompt 2: Tool-call fidelity suite

```text
Add a tool-call suite to llm-gate.
- tool_cases.jsonl: message, expected_tool (or null), expected_args.
- Load tool JSON Schemas from tools/schemas/*.json.
- For each case, get the model's tool call (OpenAI function calling online, a stub offline), then check: tool name,
  schema validity (jsonschema), exact argument values, and that no tool is called when expected_tool is null.
- Report pass rate per tool and list failures with the wrong field.
Include cases with commas in amounts and dates in different formats.
```

---

## Prompt 3: Token and cost metrics in the gate

```text
Extend llm-gate to record input and output tokens for every call (from the API usage field, estimated offline).
- gate.yaml gets cost rules: max avg_input_tokens rise vs baseline, max avg_output_tokens, max cost_per_query rise vs
  baseline (for example 20%).
- Prices come from prices.yaml with a header comment: PLACEHOLDER prices, replace with the approved price sheet.
- report.md shows cost per query and cost per 1,000 queries next to quality metrics, for this run and the baseline.
Show one run that passes and one that fails on cost.
```

---

## Prompt 4: CI integration

```text
Write an Azure Pipelines stage "Evaluate" that installs llm-gate, runs deterministic and tool-call suites on every pull
request and the full suite on main, uses the API key from a secret variable group, compares with the baseline report from
the last successful main run (pipeline artifact), publishes report.md as an artifact, and fails the stage on exit code 1.
Add the gate command to AGENTS.md so Codex runs it after each change. Explain each step.
```

---

## SmartDesk step 27: Quality gate in CI with cost metrics

```text
SmartDesk step 27. Using llm-gate:
1. Point it at the SmartDesk golden set from step 26 and add must_include phrases and citation checks.
2. Add 8 tool-call cases for the support assistant (refund, plan change, ticket lookup, and two "no tool" cases).
3. Add cost rules: cost per query may not rise more than 20% vs main (placeholder prices).
4. Add the Evaluate stage before the deploy stages in the SmartDesk pipeline.
5. Make the gate fail once on purpose (for example k = 1) and show the report, then restore it.
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** prices labelled as placeholders; the API key only in a secret variable; the gate fails on purpose at least once; golden items have owners; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Run each model-graded item 3 times and use the median to reduce noise.
- Track evaluation cost per run.
- Plot pass rate and cost per query across the last 20 pipeline runs.
