# Days 21 to 30: Course Materials

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

| Day | Topic |
|---|---|
| 21 | GenAI Intro and Prompt Engineering (assessment day) |
| 22 | Context Engineering and RAG (senior FDE session, feedback discussion) |
| 23 | RAG, Embeddings and Vector DBs |
| 24 | FDE Skills 3a and LLM Orchestration |
| 25 | LLM Orchestration and FDE Skills 3b (one-on-one feedback) |
| 26 | Agentic AI and Agentic RAG (assessment day) |
| 27 | Agent Protocols and Advanced Use Cases (senior FDE session, FDE assessment debrief) |
| 28 | LLM Security and Guardrails |
| 29 | GenAI System Evaluation |
| 30 | LLM Evaluation and QA (one-on-one feedback) |

## What each day folder contains

**Deck** (.pptx), **pre-read** (PDF), **post-read** (PDF), **Colab notebook** (.ipynb), **app build prompts** (.md),
**hands-on activities** (PDF), **workbook** (.docx) and the **quiz** on the previous day (.txt, CSV rows).
The `Day31` folder holds only the quiz on Day 30, ready for the start of Day 31.

## Running the GenAI notebooks

- **With an API key:** in Colab, open Secrets (key icon), add `OPENAI_API_KEY` and allow notebook access. In VS Code, set the environment variable or use a `.env` file.
  Set `LLM_MODEL` to a current chat model you have access to (default `gpt-4o-mini`).
- **Without a key:** every cell still runs in **offline demo mode** using a small, clearly labelled stand-in model. Offline scores show how the code works, not how real models perform.
- **Day 27 (MCP):** the notebook pins the MCP Python SDK below version 2 because v2 renamed some APIs.
- **Day 28:** all attacks target a simulated bot. Only test systems you own or are authorised to test.
