# Day 23: App Build Prompts

**App of the day:** Policy Q&A Assistant v2 (hybrid search, re-ranking, citations)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 23. Upgrades the Day 22 assistant with a real vector index, hybrid search, re-ranking and measured retrieval quality.

---

## Prompt 1: Retrieval service

```text
You are a senior GenAI engineer. Upgrade my Policy Q&A Assistant's retrieval layer (Python):
- Chunks from chunks.jsonl (id, doc, section, text, text_with_header).
- Embeddings: OpenAI if OPENAI_API_KEY is set, else a HashingVectorizer stand-in, behind one embed() function.
- Vector index: FAISS IndexHNSWFlat (inner product) persisted to disk with an id mapping; rebuild command.
- BM25 with rank_bm25 using a tokenizer that keeps codes like VPN-417.
- hybrid_search with reciprocal rank fusion and optional metadata filters (doc, section).
- rerank(): LLM relevance scores when online, word-overlap stand-in offline.
Write unit tests for RRF, the tokenizer and filtering.
```

---

## Prompt 2: Evaluation script

```text
Write eval_retrieval.py: given tests.jsonl (question, expected_chunk_ids, answerable), compute hit@1, hit@3, hit@5 and MRR
for bm25, vector, hybrid and hybrid+rerank, plus refusal accuracy on unanswerable questions for thresholds 0.1 to 0.6.
Print tables and recommend settings with a short explanation.
```

---

## Prompt 3: API and UI

```text
Expose POST /ask returning answer, citations (id, doc, section, snippet), retrieval method, scores and latency per stage.
Then build a React page with a question box, the answer with clickable citation chips that reveal the passage,
and a "debug" toggle showing candidates before and after re-ranking.
```

---

## Stretch ideas (try on your own)

- Add query rewriting for follow-up questions.
- Try HyDE and compare hit rate.
- Store vectors in Chroma or pgvector instead of FAISS.
