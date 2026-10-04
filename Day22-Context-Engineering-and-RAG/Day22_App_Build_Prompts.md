# Day 22: App Build Prompts

**App of the day:** Policy Q&A Assistant v1 (RAG with chunking and citations)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 22. The first version of a RAG app; tomorrow you upgrade retrieval with a vector database, hybrid search and re-ranking.

---

## Prompt 1: Ingestion pipeline

```text
You are a senior GenAI engineer. Build the ingestion part of a "Policy Q&A Assistant" in Python.
- Load .md, .txt and .pdf files from a docs/ folder (pypdf for PDFs).
- Clean text (fix hyphenated line breaks, collapse whitespace, keep headings).
- Chunk with a structure-aware chunker: split by headings, then sentences up to max_tokens with overlap; add contextual headers.
- Each chunk: id, doc_name, section, text, text_with_header, token_count, char_start.
- Save chunks to chunks.jsonl and print statistics (chunks per doc, average tokens, chunks cut mid-sentence).
Make chunk size and overlap configurable. Include tests for the chunker.
```

---

## Prompt 2: Query pipeline and API

```text
Add the query side as a FastAPI app:
- POST /ask {question, k} -> retrieves top-k chunks (embeddings via OpenAI if OPENAI_API_KEY is set, else a hashing vectorizer),
  assembles context within a token budget (rules, question, chunks, optional history summary), calls the model with a grounded prompt,
  and returns answer, citations (chunk ids with doc and section), and the context actually used.
- If no chunk passes a similarity threshold, answer "I don't know" without calling the model.
Include TestClient tests that run offline.
```

---

## Prompt 3: Evaluate my chunking

```text
Given my chunks.jsonl and these 10 test questions with the expected section for each, write a script that measures
for chunk sizes 200, 400 and 800 tokens: hit rate at k=3 and mean rank of the correct section. Print a comparison table and recommend a size.
```

---

## Stretch ideas (try on your own)

- Add parent-child retrieval: match small chunks, send the parent section.
- Add a simple chat memory with a running summary.
- Show the cited chunk text when the user hovers over a citation in a React UI.
