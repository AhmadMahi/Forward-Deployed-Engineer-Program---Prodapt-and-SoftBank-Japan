# SmartDesk step 16 (Day 18): RAG over the telecom FAQ with citations

**Increment:** RAG over the telecom FAQ with citations

**Day folder:** [../../../Day18-Context-Engineering-and-RAG/](../../../Day18-Context-Engineering-and-RAG/) (see `Day18_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 15](../step15-day17-lint-tests-pipeline/) | Next: [step 17](../step17-day20-docker-ci-security-gates/)

## Goal

Answer customer questions from the FAQ only, with a citation for every fact and an honest 'I don't know'.

## What changed from the previous step

Adds retrieval (OpenAI embeddings online, TF-IDF offline), permission-aware filtering by role, injection-safe context and cited answers.

## Key files

- `retrieval.py`: index and cosine similarity
- `rag.py`: retrieve, permission filter, grounded answer with citations
- `test_rag.py`: retrieval, citation, unknown, permission and injection tests
- `../data/telecom_faq.json`: the FAQ

## How to run

```bash
python rag.py
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
