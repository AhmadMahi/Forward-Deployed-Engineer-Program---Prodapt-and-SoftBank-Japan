# Day 22: App Build Prompts

**App of the day:** Policy Q&A Assistant v2 (vector index, hybrid search, re-ranking and measured retrieval quality)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 22. Upgrades the Day 18 assistant with a real vector index, hybrid search, re-ranking and measured retrieval quality.

---

## Prompt 1: Retrieval service

```text
You are a senior GenAI engineer. Upgrade my Policy Q&A Assistant's retrieval layer (Python):
- Chunks from chunks.jsonl (id, doc, section, audience, text, text_with_header).
- Embeddings: OpenAI if OPENAI_API_KEY is set, else a HashingVectorizer stand-in, behind one embed() function. OFFLINE=1 forces offline.
- Vector index: FAISS IndexHNSWFlat (inner product) persisted to disk with an id mapping; a rebuild command that re-embeds everything.
- BM25 with rank_bm25 using a tokenizer that keeps codes like VPN-417.
- hybrid_search with reciprocal rank fusion and metadata filters (section, audience) applied before ranking.
- rerank(): LLM relevance scores when online, word-overlap stand-in offline.
Write unit tests for RRF, the tokenizer and filtering.
```

## Prompt 2: Evaluation script

```text
Write eval_retrieval.py: given tests.jsonl (question, expected_chunk_ids, answerable), compute hit@1, hit@3, hit@5 and MRR
for bm25, vector, hybrid and hybrid+rerank, plus refusal accuracy on unanswerable questions for thresholds 0.1 to 0.6.
Print tables and recommend settings with a short explanation.
```

## Prompt 3: Cost check before you scale

```text
Add cost_report.py: for my corpus size, average retrieved context, queries per day and answer length, estimate monthly token cost
for long context, long context with a cached prefix, and RAG. Prices come from a PRICE_PER_1M dict marked
"PLACEHOLDER prices, replace with the approved price sheet". Print a table and a one-line recommendation that also considers
how often the documents change and whether answers need citations.
```

## Prompt 4: API and UI

```text
Expose POST /ask returning answer, citations (id, doc, section, snippet), retrieval method, scores and latency per stage.
Then build a React page with a question box, the answer with clickable citation chips that reveal the passage,
and a "debug" toggle showing candidates before and after re-ranking.
```

---

## SmartDesk step 19: Hybrid search and re-ranking

```text
SmartDesk step 19. Upgrade the SmartDesk knowledge base from step 16:
1. Add BM25 next to vector search and fuse them with RRF. Keep the audience filter before ranking.
2. Retrieve 8 candidates, re-rank, keep 3, answer with citations or "I don't know".
3. Write tests/kb_questions.jsonl with ten questions and expected chunk ids (two unanswerable).
4. Add scripts/eval_kb.py printing hit@3 and MRR for keyword, vector, hybrid and hybrid + re-rank.
5. Tests run with OFFLINE=1 and no key.
Then show me the diff and the hit-rate table.
```

**Review checklist before you commit:** filters run before ranking; the index rebuild re-embeds everything; prices are labelled placeholders; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Add query rewriting for follow-up questions.
- Try HyDE and compare hit rate.
- Store vectors in Chroma or pgvector instead of FAISS.
