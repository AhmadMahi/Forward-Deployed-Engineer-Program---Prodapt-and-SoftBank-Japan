# Day 29: App Build Prompts

**App of the day:** RAG Evaluation Dashboard (metrics, error analysis, slices)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 29. A tool that runs your RAG system on an eval set and shows where and why it fails.

---

## Prompt 1: Evaluation engine

```text
You are a senior GenAI evaluation engineer. Build an evaluation engine in Python for a RAG system exposed as a function answer(question) -> {answer, contexts}:
- Load eval items from eval.jsonl (question, expected, source_ids, topic, lang, answerable).
- Metrics: hit@1/3/5, MRR, context relevance (embedding similarity), faithfulness (claims split, LLM judge per claim, offline overlap stand-in),
  answer relevance, correctness (LLM rubric judge 1 to 5 with reasoning; offline phrase match), refusal accuracy for unanswerable items.
- Error categories: retrieval_miss, generation_error, unsupported_claim, wrong_refusal.
- Output: results.csv per item and summary.json with overall and per-slice (lang, topic) scores.
Tests with a tiny fake RAG system.
```

---

## Prompt 2: Dashboard

```text
Build a small FastAPI + React dashboard for the evaluation results: overall metric cards, a table of failures with filters by error type,
language and topic, a per-slice bar chart, and a side-by-side comparison of two runs (for example before and after a prompt change).
```

---

## Prompt 3: Judge calibration

```text
Write a script that samples 30 items, shows them to a human in the terminal for 1 to 5 scoring, then reports agreement with the LLM judge
(exact and within 1 point), a confusion table, and examples where they disagree most. Explain how to improve the rubric from these.
```

---

## Stretch ideas (try on your own)

- Add a position-bias test for pairwise judging.
- Generate synthetic questions from documents and mark them for human review.
- Track metrics over time in a CSV and plot the trend.
