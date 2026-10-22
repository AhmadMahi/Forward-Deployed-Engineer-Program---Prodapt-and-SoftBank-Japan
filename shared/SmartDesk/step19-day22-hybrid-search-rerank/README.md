# SmartDesk step 19 (Day 22): Hybrid search and re-ranking

**Increment:** Hybrid search and re-ranking

**Day folder:** [../../../Day22-Embeddings-Vector-DBs-and-RAG-App/](../../../Day22-Embeddings-Vector-DBs-and-RAG-App/) (see `Day22_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 18](../step18-day21-azure-cd/) | Next: [step 20](../step20-day23-patch-and-modernise/)

## Goal

Improve retrieval by combining keyword and vector search, then re-ranking, and measure it with a hit-rate table.

## What changed from the previous step

Adds BM25 keyword search, reciprocal rank fusion with the vector index, a simple re-ranker and a ten-question evaluation.

## Key files

- `hybrid.py`: BM25, RRF, re-ranking, evaluation set
- `retrieval.py`: vector index from step 16
- `test_hybrid.py`: tests

## How to run

```bash
python hybrid.py      # prints the hit-rate table for keyword, vector, hybrid and re-ranked
```

## How to test

```bash
python -m pytest -q
```

## RAG vs fine-tuning vs long context vs caching (NEW v4)

The FAQ is small, changes monthly and must be cited, so retrieval wins. Fine-tuning suits style or format, long context suits one-off large documents, and caching suits a stable prefix sent many times.

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
