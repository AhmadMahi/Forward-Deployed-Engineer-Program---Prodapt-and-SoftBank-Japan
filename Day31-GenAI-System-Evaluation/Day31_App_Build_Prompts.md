# Day 31: App Build Prompts

**App of the day:** RAG Evaluation Dashboard, with agent trajectory checks, judge calibration and security evals

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage: LLM judges cost tokens.

> Uses Days 1 to 31. Turn "it looks good" into numbers you can track: retrieval, faithfulness, trajectories, reliability and safety.

---

## Prompt 1: Evaluation engine

```text
You are a senior GenAI evaluation engineer. Build an evaluation engine in Python for a RAG system exposed as a function
answer(question) -> {answer, contexts}:
- Load eval items from eval.jsonl (question, expected, source_ids, topic, lang, answerable).
- Metrics: hit@1/3/5, MRR, context relevance (embedding similarity), faithfulness (claims split, LLM judge per claim,
  offline overlap stand-in), answer relevance, correctness (LLM rubric judge 1 to 5 with reasoning; offline phrase match),
  refusal accuracy for unanswerable items.
- Error categories: retrieval_miss, generation_error, unsupported_claim, wrong_refusal.
- Output: results.csv per item and summary.json with overall and per-slice (lang, topic) scores.
Model name from LLM_MODEL; OFFLINE=1 runs everything without a key. Tests with a tiny fake RAG system.
```

---

## Prompt 2: Agent trajectory and pass^k evaluation

```text
Add agent evaluation to the engine.
- agent_cases.jsonl: task, expected_tools (ordered), forbidden_tools, expected_answer, max_steps.
- For each run, record the tool calls from the agent's trace. Score tools_ok, in_order (subsequence), extra calls,
  forbidden calls, steps and final answer. A run passes only if all checks pass.
- Run each case k times (configurable) and report pass@k and pass^k per case and overall.
Tests with a fake agent that sometimes calls tools in the wrong order.
```

---

## Prompt 3: Judge calibration and security evals

```text
1. Write calibrate.py: sample 30 items, show each to a human in the terminal for a 1 to 5 score, then report agreement with
   the LLM judge (exact, within 1 point, Cohen's kappa on pass/fail), a confusion table, and the biggest disagreements.
   Add a position-bias test that swaps answer order in pairwise judging.
2. Write security_evals.py: run the Day 30 attack and benign sets against the guardrail, report block rate, false alarm
   rate and forbidden-call rate per guardrail version, and flag a regression if block rate drops by more than 0.05.
```

---

## Prompt 4: Dashboard

```text
Build a small FastAPI + React dashboard for the results: overall metric cards, a failures table with filters by error type,
language and topic, per-slice bar charts, an agent tab (trajectory pass rate, pass^k), a security tab, and a side-by-side
comparison of two runs (for example before and after a prompt change).
```

---

## SmartDesk step 26: Golden set and evaluation dashboard

```text
SmartDesk step 26. Using the work above:
1. Create a SmartDesk golden set of 30 items from the telecom FAQ (include Japanese questions and unanswerable ones).
2. Add 5 agent cases for the support assistant with expected and forbidden tools.
3. Run the evaluation engine, the agent evaluation (k = 3) and the security evals; save reports under eval/reports/.
4. Show everything in the dashboard. Add the evaluation command to AGENTS.md.
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** offline results are labelled as showing how the code works, not real quality; no customer data in eval files; judge prompts and rubrics are versioned; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Generate synthetic questions from documents and mark them for human review.
- Track metrics over time in a CSV and plot the trend.
- Add a cost column: tokens used by judges per evaluation run.
