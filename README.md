# Forward Deployed Engineer Program (v4)

Course materials for **Prodapt** and **SoftBank Japan**. Prodapt Forward Deployed Engineer Program, technical stream.

Prepared by Ahmed. **40 working days, Mon 26 Oct to Mon 21 Dec 2026.** Mon 9 Nov is the Deepavali holiday (no day number).

This file is the navigation guide. Pick a day from the index and open what you need. For coding agents working on this repository, read [AGENTS.md](AGENTS.md) first.

**AI coding tool:** OpenAI Codex, used through the VS Code extension and signed in with the program's OpenAI API key (approved models only, see [docs/MODEL_GUIDE.md](docs/MODEL_GUIDE.md)). Codex is introduced on the afternoon of Day 3. It is not required on Days 1, 2, 4 or the FDE Mindset days.

---

## What changed in v4

GenAI now starts in Week 3, Basics were cut from 17 to 15 days, and there are new days on OpenAI Codex (Day 3), industry use cases and agentic security (Day 23) and small language models with token cost (Day 25). Every technical day has a new evening **Hotel Lab**, and a running project, **SmartDesk**, connects the days. Topics added in v4 are marked `NEW (v4)` in decks and notebooks. Full list: [docs/CHANGELOG_v4.md](docs/CHANGELOG_v4.md). The previous version is kept read only in [archive/v1-40-day](archive/v1-40-day/README_v1.md).

## 1. How the program is laid out

| Folders | What they are |
| --- | --- |
| `Day01-...` to `Day35-...` | One folder per day. Technical days hold 9 files; FDE Mindset days hold a placeholder README |
| `Day36-40-Capstone` | The five-day capstone, organised by project |
| `docs/` | Model guide, Codex guide, access and install plan, changelog |
| `shared/` | SmartDesk running project, templates, Laptop Setup Guide, Codex card, Patch and Modernise starter repo |
| `tools/` | Notebook and link checkers, and the build scripts that generate each day's files |
| `FDE-Mindset-Source/` | Archived v1 FDE material, unchanged, for the FDE team |
| `archive/v1-40-day/` | The previous version, read only |

Tracks: **15 Basics, 15 GenAI, 5 FDE Mindset, 5 Capstone.**

## 2. The nine files in every technical day

| File pattern | Type | What it is | When to use it |
| --- | --- | --- | --- |
| `DayNN_Deck_*.pptx` | Slides | The session deck. v4 topics marked `NEW (v4)` | Present in class |
| `DayNN_PreRead_*.pdf` | PDF | A short, non-technical read, plus self-study topics where listed | Send before class |
| `DayNN_PostRead_*_Recap_and_Beyond.pdf` | PDF | Recap of the day plus topics that go further | Send after class |
| `DayNN_*_Colab.ipynb` | Notebook | Live demos. Option A cells run in Colab, Option B cells (commented) are for VS Code. Offline demo mode for GenAI | Demo during the session |
| `DayNN_App_Build_Prompts.md` | Markdown | Step prompts for the day's build with OpenAI Codex, including the SmartDesk step | Give to learners for the build |
| `DayNN_HandsOn_Problem_Statements.pdf` | PDF | Warm-up, core and stretch problems | Lab time and hotel lab |
| `DayNN_Workbook_Interactive.docx` | Word | Fill in the blanks, short answers, predict the output, write code | Reinforcement |
| `DayNN_Quiz_on_DayMM_*.txt` | CSV in a .txt | 15 questions on the **previous training day** | Open the session |
| `DayNN_Hotel_Lab.md` | Markdown | **NEW (v4).** The evening hands-on: steps, time per step, files, what to submit | After class |

Day 2 has no quiz (first technical day), so it has 8 files.

### Three things to watch

1. **Quizzes look backwards and skip non-training days.** The quiz in Day 13 tests Day 12; the quiz in Day 15 tests Day 13 (Day 14 is FDE Mindset). The quiz on Day 35 sits in the capstone folder.
2. **FDE Mindset days are owned by the FDE team.** Days 1, 14, 19, 24 and 29 hold a placeholder README. Day 1 also holds the technical onboarding block.
3. **GenAI notebooks need an OpenAI API key, or they fall back to offline demo mode.** See section 6.

## 3. Session types

| Tag | Days | Meaning |
| --- | --- | --- |
| Assessment day | 05, 10, 13, 17, 27, 33 | A formal assessment (1.5 hrs) runs in the day |
| FDE Mindset | 01, 14, 19, 24, 29 | Owned by the FDE team |
| Senior FDE interaction | 22, 28 | Senior FDE joins in the opening slot (1 to 2 hrs). Day 28 includes the FDE assessment debrief |
| 1:1 feedback | 26, 32 | One-to-one feedback at the end of the day |
| SME session | 23 | 4-hour session on security in the agentic world, with the Patch and Modernise assignment |
| Participant presentations | 26, 27, 34, 35 | 20 minutes in the opening slot |


## 4. Program at a glance

| Day | Date (2026) | Week | Track | Topic | App of the day | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [01](Day01-Onboarding-and-FDE-Mindset-1) | Mon 26 Oct | 1 | FDE Mindset | Onboarding + FDE Mindset Session 1 |  |  |
| [02](Day02-Python-Basics-Functions-and-Files) | Tue 27 Oct | 1 | Basics | Python Basics + Functions, Data Structures and Files | Smart Study Planner + Personal Expense Tracker |  |
| [03](Day03-OOP-and-OpenAI-Codex-Walkthrough) | Wed 28 Oct | 1 | Basics | OOP + OpenAI Codex Walkthrough (half day) | Mini Library Management System | Codex half day |
| [04](Day04-Architecture-and-MongoDB) | Thu 29 Oct | 1 | Basics | Architecture and MongoDB | Inventory Dashboard |  |
| [05](Day05-API-Fundamentals-and-FastAPI-Core) | Fri 30 Oct | 1 | Basics | API Fundamentals and FastAPI Core | Quotes and Notes REST API | Assessment |
| [06](Day06-SQLAlchemy-and-API-Docs) | Mon 02 Nov | 2 | Basics | SQLAlchemy, Relationships and API Docs | Library Books API + Library API v2 |  |
| [07](Day07-FastAPI-Advanced-Security-and-MongoDB) | Tue 03 Nov | 2 | Basics | FastAPI Advanced, Security and MongoDB | Secure Notes API | Vulnerability report v1 |
| [08](Day08-JavaScript-and-Async-JavaScript) | Wed 04 Nov | 2 | Basics | JavaScript Fundamentals and Async JavaScript | JavaScript data script for the ticket API |  |
| [09](Day09-Nodejs-and-Express) | Thu 05 Nov | 2 | Basics | Node.js and Express | Tasks API in Express |  |
| [10](Day10-React-Basics) | Fri 06 Nov | 2 | Basics | React Basics | Personal Dashboard | Assessment |
| Holiday | Mon 09 Nov | 3 | Holiday | Deepavali |  |  |
| [11](Day11-React-UI-Logic-and-Full-Stack) | Tue 10 Nov | 3 | Basics | React UI Logic and Full-Stack Integration | Full Stack Task Board |  |
| [12](Day12-GenAI-Intro-LLMs-and-Tokens) | Wed 11 Nov | 3 | GenAI | GenAI 1: Introduction to GenAI, LLMs and Tokens | SmartDesk ticket summariser with token log |  |
| [13](Day13-Prompt-Engineering) | Thu 12 Nov | 3 | GenAI | GenAI 2: Prompt Engineering | Prompt Playground | Assessment |
| [14](Day14-FDE-Mindset-2) | Fri 13 Nov | 3 | FDE Mindset | FDE Mindset Session 2 |  |  |
| [15](Day15-Testing-and-Data-Engineering-Intro) | Mon 16 Nov | 4 | Basics | Testing and Data Engineering Intro | Tested Order Ingestion Service |  |
| [16](Day16-Data-Pipelines-Spark-and-PySpark) | Tue 17 Nov | 4 | Basics | Data Pipelines, Spark and PySpark | Retail Sales Batch Pipeline + Sales Insights Pipeline |  |
| [17](Day17-DevOps-and-Cloud-Fundamentals) | Wed 18 Nov | 4 | Basics | DevOps and Cloud Fundamentals | DevOps-ready FastAPI Service | Assessment |
| [18](Day18-Context-Engineering-and-RAG) | Thu 19 Nov | 4 | GenAI | GenAI 3: Context Engineering and RAG Foundations | Policy Q&A Assistant v1 |  |
| [19](Day19-FDE-Mindset-3) | Fri 20 Nov | 4 | FDE Mindset | FDE Mindset Session 3 |  |  |
| [20](Day20-Git-CI-CD-and-Docker) | Mon 23 Nov | 5 | Basics | Git, CI/CD and Docker | Containerised Task API | Vulnerability report v2 |
| [21](Day21-Azure-Deployment-and-CD) | Tue 24 Nov | 5 | Basics | Azure Deployment and Continuous Delivery | Deploy the Full Stack Task Board to Azure |  |
| [22](Day22-Embeddings-Vector-DBs-and-RAG-App) | Wed 25 Nov | 5 | GenAI | GenAI 4: Embeddings, Vector DBs and the RAG Application | Policy Q&A Assistant v2 | Senior FDE interaction |
| [23](Day23-Industry-Use-Cases-and-Agentic-Security-SME) | Thu 26 Nov | 5 | GenAI | GenAI 5: Industry Use Cases + Security for the Agentic World (SME) | Patch and Modernise assignment | SME session |
| [24](Day24-FDE-Mindset-4) | Fri 27 Nov | 5 | FDE Mindset | FDE Mindset Session 4 |  |  |
| [25](Day25-SLMs-and-Token-Optimisation) | Mon 30 Nov | 6 | GenAI | GenAI 6: Small Language Models + Token Cost and Optimisation | SLM vs LLM comparison + cost report |  |
| [26](Day26-LLM-Orchestration-Tools-and-LangGraph) | Tue 01 Dec | 6 | GenAI | GenAI 7: LLM Orchestration, Tool Calling and LangGraph | Customer Support Assistant | 1:1 feedback |
| [27](Day27-Agentic-AI-Agentic-RAG-and-Memory) | Wed 02 Dec | 6 | GenAI | GenAI 8: Agentic AI and Agentic RAG | Agentic HR and Ops Assistant | Assessment |
| [28](Day28-Agent-Protocols-MCP-and-A2A) | Thu 03 Dec | 6 | GenAI | GenAI 9: Agent Protocols (MCP, A2A) and Advanced Agents | Enterprise Agent Hub | Senior FDE interaction |
| [29](Day29-FDE-Mindset-5) | Fri 04 Dec | 6 | FDE Mindset | FDE Mindset Session 5 |  |  |
| [30](Day30-LLM-Security-and-Guardrails) | Mon 07 Dec | 7 | GenAI | GenAI 10: LLM Security and Guardrails | Guardrail Gateway | Vulnerability report v3 |
| [31](Day31-GenAI-System-Evaluation) | Tue 08 Dec | 7 | GenAI | GenAI 11: GenAI System Evaluation | RAG Evaluation Dashboard |  |
| [32](Day32-LLM-Evaluation-and-Quality-Gates) | Wed 09 Dec | 7 | GenAI | GenAI 12: LLM Evaluation and Quality Gates | LLM Quality Gate for CI | 1:1 feedback |
| [33](Day33-LLMOps) | Thu 10 Dec | 7 | GenAI | GenAI 13: LLMOps | Resilient LLM Client + LLM Cost and Version Control Center | Assessment |
| [34](Day34-LLM-Deployment-and-Lifecycle) | Fri 11 Dec | 7 | GenAI | GenAI 14: LLM Deployment and Lifecycle | Production LLM Gateway |  |
| [35](Day35-Observability-Drift-and-Optimisation) | Mon 14 Dec | 8 | GenAI | GenAI 15: Observability, Drift and Optimisation | LLM Observability Starter Kit + Drift Watch |  |
| [36 to 40](Day36-40-Capstone) | Tue 15 to Mon 21 Dec | 8 to 9 | Capstone | Capstone project | Six projects incl. Project 06 LegacyLift | Demo day 21 Dec |

## 5. The program in blocks

| Week | Dates | Block |
| --- | --- | --- |
| 1 | 26 to 30 Oct | Onboarding, Python, OOP, OpenAI Codex, MongoDB, FastAPI core |
| 2 | 2 to 6 Nov | SQLAlchemy, API security, JavaScript, Node.js, React |
| 3 | 10 to 13 Nov | Full stack, GenAI intro, prompt engineering (after the 9 Nov holiday) |
| 4 | 16 to 20 Nov | Testing, data engineering, Spark, DevOps, context engineering and RAG |
| 5 | 23 to 27 Nov | Git, CI/CD, Docker, Azure, embeddings and vector search, industry use cases and agentic security |
| 6 | 30 Nov to 4 Dec | SLMs and token cost, LangGraph, agents and memory, MCP and A2A |
| 7 | 7 to 11 Dec | Guardrails, evaluation, quality gates, LLMOps, deployment |
| 8 to 9 | 14 to 21 Dec | Observability and drift, then the capstone |

## 6. Running the notebooks

- **Colab (default):** upload the `.ipynb` file and run cells top to bottom. Add `OPENAI_API_KEY` in Colab Secrets (key icon, allow notebook access).
- **VS Code:** install Python 3.12+, the Python and Jupyter extensions, and Node.js LTS for Days 8 to 11. Comment out Option A and uncomment Option B where shown. Put keys in a git-ignored `.env` file.
- **Offline demo mode:** with no key, or with `OFFLINE=1`, GenAI cells use a small stand-in so every cell still runs. Offline scores show how the code works, not real model quality.
- **Model:** set `LLM_MODEL` to change the model. The default must be confirmed against the approved model list ([docs/MODEL_GUIDE.md](docs/MODEL_GUIDE.md)).
- **MongoDB days** use `mongomock` in Colab. In VS Code, set `MONGO_URI` to a local MongoDB or a free Atlas cluster.
- **Day 25** uses the free Colab GPU runtime for the small language model lab, with a CPU fallback.
- **Checks for maintainers:** `python tools/check_notebooks.py` runs every notebook in offline mode; `python tools/check_links.py` checks Markdown links.

## 7. The capstone, Days 36 to 40

Tue 15 Dec to Mon 21 Dec 2026: Day 36 Tue 15 Dec, Day 37 Wed 16 Dec, Day 38 Thu 17 Dec, Day 39 Fri 18 Dec, Day 40 Mon 21 Dec. Code freeze Day 39 at 17:00 IST. Deliverables due Day 40 at 09:00 IST.

Six projects, including the new **Project 06 LegacyLift** (modernise a legacy order-management app into FastAPI + React with OpenAI Codex, tests first). NEW (v4) baseline for every project: one modernisation step, `AGENTS.md` in the team repo, a security checklist mapped to the OWASP Top 10 for Agentic Applications, a vulnerability report, and a token and cost report.

Start with [Day36-40-Capstone/README.md](Day36-40-Capstone/README.md).

## 8. SmartDesk running project

A customer support platform for a telecom operator, built one step per technical day: from a Python CLI on Day 2 to a production LLM gateway with observability on Day 35. The day's main app stays the main build; SmartDesk is the thread that connects the days. Brief, steps and reference solutions: [shared/SmartDesk/README.md](shared/SmartDesk/README.md).

## 9. Day by day index

### Day 01. Onboarding + FDE Mindset Session 1

Mon 26 Oct 2026 | Week 1 | FDE Mindset | v4 action: Placeholder + onboarding

[README (placeholder)](Day01-Onboarding-and-FDE-Mindset-1/README.md) | [Day01_Deck_Program_Walkthrough.pptx](Day01-Onboarding-and-FDE-Mindset-1/Day01_Deck_Program_Walkthrough.pptx) | [Day01_Laptop_PreAssessment_Checklist.md](Day01-Onboarding-and-FDE-Mindset-1/Day01_Laptop_PreAssessment_Checklist.md)

### Day 02. Python Basics + Functions, Data Structures and Files

Tue 27 Oct 2026 | Week 1 | Basics | v4 action: Merge

[Deck](Day02-Python-Basics-Functions-and-Files/Day02_Deck_Python_Basics_Functions_and_Files.pptx) | [Pre-read](Day02-Python-Basics-Functions-and-Files/Day02_PreRead_Python_Basics_Functions_and_Files.pdf) | [Post-read](Day02-Python-Basics-Functions-and-Files/Day02_PostRead_Python_Basics_Functions_and_Files_Recap_and_Beyond.pdf) | [Notebook](Day02-Python-Basics-Functions-and-Files/Day02_Python_Basics_Functions_and_Files_Colab.ipynb) | [App prompts](Day02-Python-Basics-Functions-and-Files/Day02_App_Build_Prompts.md) | [Hands-on](Day02-Python-Basics-Functions-and-Files/Day02_HandsOn_Problem_Statements.pdf) | [Workbook](Day02-Python-Basics-Functions-and-Files/Day02_Workbook_Interactive.docx) | [Hotel lab](Day02-Python-Basics-Functions-and-Files/Day02_Hotel_Lab.md)

### Day 03. OOP + OpenAI Codex Walkthrough (half day) (Codex half day)

Wed 28 Oct 2026 | Week 1 | Basics | v4 action: Condense + new

[Deck](Day03-OOP-and-OpenAI-Codex-Walkthrough/Day03_Deck_OOP_and_OpenAI_Codex_Walkthrough.pptx) | [Pre-read](Day03-OOP-and-OpenAI-Codex-Walkthrough/Day03_PreRead_OOP_and_OpenAI_Codex_Walkthrough.pdf) | [Post-read](Day03-OOP-and-OpenAI-Codex-Walkthrough/Day03_PostRead_OOP_and_OpenAI_Codex_Walkthrough_Recap_and_Beyond.pdf) | [Notebook](Day03-OOP-and-OpenAI-Codex-Walkthrough/Day03_OOP_and_OpenAI_Codex_Walkthrough_Colab.ipynb) | [App prompts](Day03-OOP-and-OpenAI-Codex-Walkthrough/Day03_App_Build_Prompts.md) | [Hands-on](Day03-OOP-and-OpenAI-Codex-Walkthrough/Day03_HandsOn_Problem_Statements.pdf) | [Workbook](Day03-OOP-and-OpenAI-Codex-Walkthrough/Day03_Workbook_Interactive.docx) | [Quiz](Day03-OOP-and-OpenAI-Codex-Walkthrough/Day03_Quiz_on_Day02_Python_Basics_Functions_and_Files.txt) | [Hotel lab](Day03-OOP-and-OpenAI-Codex-Walkthrough/Day03_Hotel_Lab.md)

### Day 04. Architecture and MongoDB

Thu 29 Oct 2026 | Week 1 | Basics | v4 action: Reuse + update

[Deck](Day04-Architecture-and-MongoDB/Day04_Deck_Architecture_and_MongoDB.pptx) | [Pre-read](Day04-Architecture-and-MongoDB/Day04_PreRead_Architecture_and_MongoDB.pdf) | [Post-read](Day04-Architecture-and-MongoDB/Day04_PostRead_Architecture_and_MongoDB_Recap_and_Beyond.pdf) | [Notebook](Day04-Architecture-and-MongoDB/Day04_Architecture_and_MongoDB_Colab.ipynb) | [App prompts](Day04-Architecture-and-MongoDB/Day04_App_Build_Prompts.md) | [Hands-on](Day04-Architecture-and-MongoDB/Day04_HandsOn_Problem_Statements.pdf) | [Workbook](Day04-Architecture-and-MongoDB/Day04_Workbook_Interactive.docx) | [Quiz](Day04-Architecture-and-MongoDB/Day04_Quiz_on_Day03_OOP_and_OpenAI_Codex_Walkthrough.txt) | [Hotel lab](Day04-Architecture-and-MongoDB/Day04_Hotel_Lab.md)

### Day 05. API Fundamentals and FastAPI Core (Assessment)

Fri 30 Oct 2026 | Week 1 | Basics | v4 action: Merge

[Deck](Day05-API-Fundamentals-and-FastAPI-Core/Day05_Deck_API_Fundamentals_and_FastAPI_Core.pptx) | [Pre-read](Day05-API-Fundamentals-and-FastAPI-Core/Day05_PreRead_API_Fundamentals_and_FastAPI_Core.pdf) | [Post-read](Day05-API-Fundamentals-and-FastAPI-Core/Day05_PostRead_API_Fundamentals_and_FastAPI_Core_Recap_and_Beyond.pdf) | [Notebook](Day05-API-Fundamentals-and-FastAPI-Core/Day05_API_Fundamentals_and_FastAPI_Core_Colab.ipynb) | [App prompts](Day05-API-Fundamentals-and-FastAPI-Core/Day05_App_Build_Prompts.md) | [Hands-on](Day05-API-Fundamentals-and-FastAPI-Core/Day05_HandsOn_Problem_Statements.pdf) | [Workbook](Day05-API-Fundamentals-and-FastAPI-Core/Day05_Workbook_Interactive.docx) | [Quiz](Day05-API-Fundamentals-and-FastAPI-Core/Day05_Quiz_on_Day04_Architecture_and_MongoDB.txt) | [Hotel lab](Day05-API-Fundamentals-and-FastAPI-Core/Day05_Hotel_Lab.md)

### Day 06. SQLAlchemy, Relationships and API Docs

Mon 02 Nov 2026 | Week 2 | Basics | v4 action: Merge

[Deck](Day06-SQLAlchemy-and-API-Docs/Day06_Deck_SQLAlchemy_and_API_Docs.pptx) | [Pre-read](Day06-SQLAlchemy-and-API-Docs/Day06_PreRead_SQLAlchemy_and_API_Docs.pdf) | [Post-read](Day06-SQLAlchemy-and-API-Docs/Day06_PostRead_SQLAlchemy_and_API_Docs_Recap_and_Beyond.pdf) | [Notebook](Day06-SQLAlchemy-and-API-Docs/Day06_SQLAlchemy_and_API_Docs_Colab.ipynb) | [App prompts](Day06-SQLAlchemy-and-API-Docs/Day06_App_Build_Prompts.md) | [Hands-on](Day06-SQLAlchemy-and-API-Docs/Day06_HandsOn_Problem_Statements.pdf) | [Workbook](Day06-SQLAlchemy-and-API-Docs/Day06_Workbook_Interactive.docx) | [Quiz](Day06-SQLAlchemy-and-API-Docs/Day06_Quiz_on_Day05_API_Fundamentals_and_FastAPI_Core.txt) | [Hotel lab](Day06-SQLAlchemy-and-API-Docs/Day06_Hotel_Lab.md)

### Day 07. FastAPI Advanced, Security and MongoDB (Vulnerability report v1)

Tue 03 Nov 2026 | Week 2 | Basics | v4 action: Merge

[Deck](Day07-FastAPI-Advanced-Security-and-MongoDB/Day07_Deck_FastAPI_Advanced_Security_and_MongoDB.pptx) | [Pre-read](Day07-FastAPI-Advanced-Security-and-MongoDB/Day07_PreRead_FastAPI_Advanced_Security_and_MongoDB.pdf) | [Post-read](Day07-FastAPI-Advanced-Security-and-MongoDB/Day07_PostRead_FastAPI_Advanced_Security_and_MongoDB_Recap_and_Beyond.pdf) | [Notebook](Day07-FastAPI-Advanced-Security-and-MongoDB/Day07_FastAPI_Advanced_Security_and_MongoDB_Colab.ipynb) | [App prompts](Day07-FastAPI-Advanced-Security-and-MongoDB/Day07_App_Build_Prompts.md) | [Hands-on](Day07-FastAPI-Advanced-Security-and-MongoDB/Day07_HandsOn_Problem_Statements.pdf) | [Workbook](Day07-FastAPI-Advanced-Security-and-MongoDB/Day07_Workbook_Interactive.docx) | [Quiz](Day07-FastAPI-Advanced-Security-and-MongoDB/Day07_Quiz_on_Day06_SQLAlchemy_and_API_Docs.txt) | [Hotel lab](Day07-FastAPI-Advanced-Security-and-MongoDB/Day07_Hotel_Lab.md)

### Day 08. JavaScript Fundamentals and Async JavaScript

Wed 04 Nov 2026 | Week 2 | Basics | v4 action: Merge

[Deck](Day08-JavaScript-and-Async-JavaScript/Day08_Deck_JavaScript_and_Async_JavaScript.pptx) | [Pre-read](Day08-JavaScript-and-Async-JavaScript/Day08_PreRead_JavaScript_and_Async_JavaScript.pdf) | [Post-read](Day08-JavaScript-and-Async-JavaScript/Day08_PostRead_JavaScript_and_Async_JavaScript_Recap_and_Beyond.pdf) | [Notebook](Day08-JavaScript-and-Async-JavaScript/Day08_JavaScript_and_Async_JavaScript_Colab.ipynb) | [App prompts](Day08-JavaScript-and-Async-JavaScript/Day08_App_Build_Prompts.md) | [Hands-on](Day08-JavaScript-and-Async-JavaScript/Day08_HandsOn_Problem_Statements.pdf) | [Workbook](Day08-JavaScript-and-Async-JavaScript/Day08_Workbook_Interactive.docx) | [Quiz](Day08-JavaScript-and-Async-JavaScript/Day08_Quiz_on_Day07_FastAPI_Advanced_Security_and_MongoDB.txt) | [Hotel lab](Day08-JavaScript-and-Async-JavaScript/Day08_Hotel_Lab.md)

### Day 09. Node.js and Express

Thu 05 Nov 2026 | Week 2 | Basics | v4 action: Reuse + update

[Deck](Day09-Nodejs-and-Express/Day09_Deck_Nodejs_and_Express.pptx) | [Pre-read](Day09-Nodejs-and-Express/Day09_PreRead_Nodejs_and_Express.pdf) | [Post-read](Day09-Nodejs-and-Express/Day09_PostRead_Nodejs_and_Express_Recap_and_Beyond.pdf) | [Notebook](Day09-Nodejs-and-Express/Day09_Nodejs_and_Express_Colab.ipynb) | [App prompts](Day09-Nodejs-and-Express/Day09_App_Build_Prompts.md) | [Hands-on](Day09-Nodejs-and-Express/Day09_HandsOn_Problem_Statements.pdf) | [Workbook](Day09-Nodejs-and-Express/Day09_Workbook_Interactive.docx) | [Quiz](Day09-Nodejs-and-Express/Day09_Quiz_on_Day08_JavaScript_and_Async_JavaScript.txt) | [Hotel lab](Day09-Nodejs-and-Express/Day09_Hotel_Lab.md)

### Day 10. React Basics (Assessment)

Fri 06 Nov 2026 | Week 2 | Basics | v4 action: Reuse + update

[Deck](Day10-React-Basics/Day10_Deck_React_Basics.pptx) | [Pre-read](Day10-React-Basics/Day10_PreRead_React_Basics.pdf) | [Post-read](Day10-React-Basics/Day10_PostRead_React_Basics_Recap_and_Beyond.pdf) | [Notebook](Day10-React-Basics/Day10_React_Basics_Colab.ipynb) | [App prompts](Day10-React-Basics/Day10_App_Build_Prompts.md) | [Hands-on](Day10-React-Basics/Day10_HandsOn_Problem_Statements.pdf) | [Workbook](Day10-React-Basics/Day10_Workbook_Interactive.docx) | [Quiz](Day10-React-Basics/Day10_Quiz_on_Day09_Nodejs_and_Express.txt) | [Hotel lab](Day10-React-Basics/Day10_Hotel_Lab.md)

### Mon 09 Nov 2026. Holiday: Deepavali

### Day 11. React UI Logic and Full-Stack Integration

Tue 10 Nov 2026 | Week 3 | Basics | v4 action: Reuse + update

[Deck](Day11-React-UI-Logic-and-Full-Stack/Day11_Deck_React_UI_Logic_and_Full_Stack.pptx) | [Pre-read](Day11-React-UI-Logic-and-Full-Stack/Day11_PreRead_React_UI_Logic_and_Full_Stack.pdf) | [Post-read](Day11-React-UI-Logic-and-Full-Stack/Day11_PostRead_React_UI_Logic_and_Full_Stack_Recap_and_Beyond.pdf) | [Notebook](Day11-React-UI-Logic-and-Full-Stack/Day11_React_UI_Logic_and_Full_Stack_Colab.ipynb) | [App prompts](Day11-React-UI-Logic-and-Full-Stack/Day11_App_Build_Prompts.md) | [Hands-on](Day11-React-UI-Logic-and-Full-Stack/Day11_HandsOn_Problem_Statements.pdf) | [Workbook](Day11-React-UI-Logic-and-Full-Stack/Day11_Workbook_Interactive.docx) | [Quiz](Day11-React-UI-Logic-and-Full-Stack/Day11_Quiz_on_Day10_React_Basics.txt) | [Hotel lab](Day11-React-UI-Logic-and-Full-Stack/Day11_Hotel_Lab.md)

### Day 12. GenAI 1: Introduction to GenAI, LLMs and Tokens

Wed 11 Nov 2026 | Week 3 | GenAI | v4 action: Split + expand

[Deck](Day12-GenAI-Intro-LLMs-and-Tokens/Day12_Deck_GenAI_Intro_LLMs_and_Tokens.pptx) | [Pre-read](Day12-GenAI-Intro-LLMs-and-Tokens/Day12_PreRead_GenAI_Intro_LLMs_and_Tokens.pdf) | [Post-read](Day12-GenAI-Intro-LLMs-and-Tokens/Day12_PostRead_GenAI_Intro_LLMs_and_Tokens_Recap_and_Beyond.pdf) | [Notebook](Day12-GenAI-Intro-LLMs-and-Tokens/Day12_GenAI_Intro_LLMs_and_Tokens_Colab.ipynb) | [App prompts](Day12-GenAI-Intro-LLMs-and-Tokens/Day12_App_Build_Prompts.md) | [Hands-on](Day12-GenAI-Intro-LLMs-and-Tokens/Day12_HandsOn_Problem_Statements.pdf) | [Workbook](Day12-GenAI-Intro-LLMs-and-Tokens/Day12_Workbook_Interactive.docx) | [Quiz](Day12-GenAI-Intro-LLMs-and-Tokens/Day12_Quiz_on_Day11_React_UI_Logic_and_Full_Stack.txt) | [Hotel lab](Day12-GenAI-Intro-LLMs-and-Tokens/Day12_Hotel_Lab.md)

### Day 13. GenAI 2: Prompt Engineering (Assessment)

Thu 12 Nov 2026 | Week 3 | GenAI | v4 action: Split + expand

[Deck](Day13-Prompt-Engineering/Day13_Deck_Prompt_Engineering.pptx) | [Pre-read](Day13-Prompt-Engineering/Day13_PreRead_Prompt_Engineering.pdf) | [Post-read](Day13-Prompt-Engineering/Day13_PostRead_Prompt_Engineering_Recap_and_Beyond.pdf) | [Notebook](Day13-Prompt-Engineering/Day13_Prompt_Engineering_Colab.ipynb) | [App prompts](Day13-Prompt-Engineering/Day13_App_Build_Prompts.md) | [Hands-on](Day13-Prompt-Engineering/Day13_HandsOn_Problem_Statements.pdf) | [Workbook](Day13-Prompt-Engineering/Day13_Workbook_Interactive.docx) | [Quiz](Day13-Prompt-Engineering/Day13_Quiz_on_Day12_GenAI_Intro_LLMs_and_Tokens.txt) | [Hotel lab](Day13-Prompt-Engineering/Day13_Hotel_Lab.md)

### Day 14. FDE Mindset Session 2

Fri 13 Nov 2026 | Week 3 | FDE Mindset | v4 action: Placeholder

[README (placeholder)](Day14-FDE-Mindset-2/README.md)

### Day 15. Testing and Data Engineering Intro

Mon 16 Nov 2026 | Week 4 | Basics | v4 action: Reuse + update

[Deck](Day15-Testing-and-Data-Engineering-Intro/Day15_Deck_Testing_and_Data_Engineering_Intro.pptx) | [Pre-read](Day15-Testing-and-Data-Engineering-Intro/Day15_PreRead_Testing_and_Data_Engineering_Intro.pdf) | [Post-read](Day15-Testing-and-Data-Engineering-Intro/Day15_PostRead_Testing_and_Data_Engineering_Intro_Recap_and_Beyond.pdf) | [Notebook](Day15-Testing-and-Data-Engineering-Intro/Day15_Testing_and_Data_Engineering_Intro_Colab.ipynb) | [App prompts](Day15-Testing-and-Data-Engineering-Intro/Day15_App_Build_Prompts.md) | [Hands-on](Day15-Testing-and-Data-Engineering-Intro/Day15_HandsOn_Problem_Statements.pdf) | [Workbook](Day15-Testing-and-Data-Engineering-Intro/Day15_Workbook_Interactive.docx) | [Quiz](Day15-Testing-and-Data-Engineering-Intro/Day15_Quiz_on_Day13_Prompt_Engineering.txt) | [Hotel lab](Day15-Testing-and-Data-Engineering-Intro/Day15_Hotel_Lab.md)

### Day 16. Data Pipelines, Spark and PySpark

Tue 17 Nov 2026 | Week 4 | Basics | v4 action: Merge

[Deck](Day16-Data-Pipelines-Spark-and-PySpark/Day16_Deck_Data_Pipelines_Spark_and_PySpark.pptx) | [Pre-read](Day16-Data-Pipelines-Spark-and-PySpark/Day16_PreRead_Data_Pipelines_Spark_and_PySpark.pdf) | [Post-read](Day16-Data-Pipelines-Spark-and-PySpark/Day16_PostRead_Data_Pipelines_Spark_and_PySpark_Recap_and_Beyond.pdf) | [Notebook](Day16-Data-Pipelines-Spark-and-PySpark/Day16_Data_Pipelines_Spark_and_PySpark_Colab.ipynb) | [App prompts](Day16-Data-Pipelines-Spark-and-PySpark/Day16_App_Build_Prompts.md) | [Hands-on](Day16-Data-Pipelines-Spark-and-PySpark/Day16_HandsOn_Problem_Statements.pdf) | [Workbook](Day16-Data-Pipelines-Spark-and-PySpark/Day16_Workbook_Interactive.docx) | [Quiz](Day16-Data-Pipelines-Spark-and-PySpark/Day16_Quiz_on_Day15_Testing_and_Data_Engineering_Intro.txt) | [Hotel lab](Day16-Data-Pipelines-Spark-and-PySpark/Day16_Hotel_Lab.md)

### Day 17. DevOps and Cloud Fundamentals (Assessment)

Wed 18 Nov 2026 | Week 4 | Basics | v4 action: Reuse + update

[Deck](Day17-DevOps-and-Cloud-Fundamentals/Day17_Deck_DevOps_and_Cloud_Fundamentals.pptx) | [Pre-read](Day17-DevOps-and-Cloud-Fundamentals/Day17_PreRead_DevOps_and_Cloud_Fundamentals.pdf) | [Post-read](Day17-DevOps-and-Cloud-Fundamentals/Day17_PostRead_DevOps_and_Cloud_Fundamentals_Recap_and_Beyond.pdf) | [Notebook](Day17-DevOps-and-Cloud-Fundamentals/Day17_DevOps_and_Cloud_Fundamentals_Colab.ipynb) | [App prompts](Day17-DevOps-and-Cloud-Fundamentals/Day17_App_Build_Prompts.md) | [Hands-on](Day17-DevOps-and-Cloud-Fundamentals/Day17_HandsOn_Problem_Statements.pdf) | [Workbook](Day17-DevOps-and-Cloud-Fundamentals/Day17_Workbook_Interactive.docx) | [Quiz](Day17-DevOps-and-Cloud-Fundamentals/Day17_Quiz_on_Day16_Data_Pipelines_Spark_and_PySpark.txt) | [Hotel lab](Day17-DevOps-and-Cloud-Fundamentals/Day17_Hotel_Lab.md)

### Day 18. GenAI 3: Context Engineering and RAG Foundations

Thu 19 Nov 2026 | Week 4 | GenAI | v4 action: Reuse + update

[Deck](Day18-Context-Engineering-and-RAG/Day18_Deck_Context_Engineering_and_RAG.pptx) | [Pre-read](Day18-Context-Engineering-and-RAG/Day18_PreRead_Context_Engineering_and_RAG.pdf) | [Post-read](Day18-Context-Engineering-and-RAG/Day18_PostRead_Context_Engineering_and_RAG_Recap_and_Beyond.pdf) | [Notebook](Day18-Context-Engineering-and-RAG/Day18_Context_Engineering_and_RAG_Colab.ipynb) | [App prompts](Day18-Context-Engineering-and-RAG/Day18_App_Build_Prompts.md) | [Hands-on](Day18-Context-Engineering-and-RAG/Day18_HandsOn_Problem_Statements.pdf) | [Workbook](Day18-Context-Engineering-and-RAG/Day18_Workbook_Interactive.docx) | [Quiz](Day18-Context-Engineering-and-RAG/Day18_Quiz_on_Day17_DevOps_and_Cloud_Fundamentals.txt) | [Hotel lab](Day18-Context-Engineering-and-RAG/Day18_Hotel_Lab.md)

### Day 19. FDE Mindset Session 3

Fri 20 Nov 2026 | Week 4 | FDE Mindset | v4 action: Placeholder

[README (placeholder)](Day19-FDE-Mindset-3/README.md)

### Day 20. Git, CI/CD and Docker (Vulnerability report v2)

Mon 23 Nov 2026 | Week 5 | Basics | v4 action: Merge

[Deck](Day20-Git-CI-CD-and-Docker/Day20_Deck_Git_CI_CD_and_Docker.pptx) | [Pre-read](Day20-Git-CI-CD-and-Docker/Day20_PreRead_Git_CI_CD_and_Docker.pdf) | [Post-read](Day20-Git-CI-CD-and-Docker/Day20_PostRead_Git_CI_CD_and_Docker_Recap_and_Beyond.pdf) | [Notebook](Day20-Git-CI-CD-and-Docker/Day20_Git_CI_CD_and_Docker_Colab.ipynb) | [App prompts](Day20-Git-CI-CD-and-Docker/Day20_App_Build_Prompts.md) | [Hands-on](Day20-Git-CI-CD-and-Docker/Day20_HandsOn_Problem_Statements.pdf) | [Workbook](Day20-Git-CI-CD-and-Docker/Day20_Workbook_Interactive.docx) | [Quiz](Day20-Git-CI-CD-and-Docker/Day20_Quiz_on_Day18_Context_Engineering_and_RAG.txt) | [Hotel lab](Day20-Git-CI-CD-and-Docker/Day20_Hotel_Lab.md)

### Day 21. Azure Deployment and Continuous Delivery

Tue 24 Nov 2026 | Week 5 | Basics | v4 action: Reuse + update

[Deck](Day21-Azure-Deployment-and-CD/Day21_Deck_Azure_Deployment_and_CD.pptx) | [Pre-read](Day21-Azure-Deployment-and-CD/Day21_PreRead_Azure_Deployment_and_CD.pdf) | [Post-read](Day21-Azure-Deployment-and-CD/Day21_PostRead_Azure_Deployment_and_CD_Recap_and_Beyond.pdf) | [Notebook](Day21-Azure-Deployment-and-CD/Day21_Azure_Deployment_and_CD_Colab.ipynb) | [App prompts](Day21-Azure-Deployment-and-CD/Day21_App_Build_Prompts.md) | [Hands-on](Day21-Azure-Deployment-and-CD/Day21_HandsOn_Problem_Statements.pdf) | [Workbook](Day21-Azure-Deployment-and-CD/Day21_Workbook_Interactive.docx) | [Quiz](Day21-Azure-Deployment-and-CD/Day21_Quiz_on_Day20_Git_CI_CD_and_Docker.txt) | [Hotel lab](Day21-Azure-Deployment-and-CD/Day21_Hotel_Lab.md)

### Day 22. GenAI 4: Embeddings, Vector DBs and the RAG Application (Senior FDE interaction)

Wed 25 Nov 2026 | Week 5 | GenAI | v4 action: Reuse + update

[Deck](Day22-Embeddings-Vector-DBs-and-RAG-App/Day22_Deck_Embeddings_Vector_DBs_and_RAG_App.pptx) | [Pre-read](Day22-Embeddings-Vector-DBs-and-RAG-App/Day22_PreRead_Embeddings_Vector_DBs_and_RAG_App.pdf) | [Post-read](Day22-Embeddings-Vector-DBs-and-RAG-App/Day22_PostRead_Embeddings_Vector_DBs_and_RAG_App_Recap_and_Beyond.pdf) | [Notebook](Day22-Embeddings-Vector-DBs-and-RAG-App/Day22_Embeddings_Vector_DBs_and_RAG_App_Colab.ipynb) | [App prompts](Day22-Embeddings-Vector-DBs-and-RAG-App/Day22_App_Build_Prompts.md) | [Hands-on](Day22-Embeddings-Vector-DBs-and-RAG-App/Day22_HandsOn_Problem_Statements.pdf) | [Workbook](Day22-Embeddings-Vector-DBs-and-RAG-App/Day22_Workbook_Interactive.docx) | [Quiz](Day22-Embeddings-Vector-DBs-and-RAG-App/Day22_Quiz_on_Day21_Azure_Deployment_and_CD.txt) | [Hotel lab](Day22-Embeddings-Vector-DBs-and-RAG-App/Day22_Hotel_Lab.md)

### Day 23. GenAI 5: Industry Use Cases + Security for the Agentic World (SME) (SME session)

Thu 26 Nov 2026 | Week 5 | GenAI | v4 action: New

[Deck](Day23-Industry-Use-Cases-and-Agentic-Security-SME/Day23_Deck_Industry_Use_Cases_and_Agentic_Security_SME.pptx) | [Pre-read](Day23-Industry-Use-Cases-and-Agentic-Security-SME/Day23_PreRead_Industry_Use_Cases_and_Agentic_Security_SME.pdf) | [Post-read](Day23-Industry-Use-Cases-and-Agentic-Security-SME/Day23_PostRead_Industry_Use_Cases_and_Agentic_Security_SME_Recap_and_Beyond.pdf) | [Notebook](Day23-Industry-Use-Cases-and-Agentic-Security-SME/Day23_Industry_Use_Cases_and_Agentic_Security_SME_Colab.ipynb) | [App prompts](Day23-Industry-Use-Cases-and-Agentic-Security-SME/Day23_App_Build_Prompts.md) | [Hands-on](Day23-Industry-Use-Cases-and-Agentic-Security-SME/Day23_HandsOn_Problem_Statements.pdf) | [Workbook](Day23-Industry-Use-Cases-and-Agentic-Security-SME/Day23_Workbook_Interactive.docx) | [Quiz](Day23-Industry-Use-Cases-and-Agentic-Security-SME/Day23_Quiz_on_Day22_Embeddings_Vector_DBs_and_RAG_App.txt) | [Hotel lab](Day23-Industry-Use-Cases-and-Agentic-Security-SME/Day23_Hotel_Lab.md) | [Day23_Industry_Use_Cases_OnePager.pdf](Day23-Industry-Use-Cases-and-Agentic-Security-SME/Day23_Industry_Use_Cases_OnePager.pdf)

### Day 24. FDE Mindset Session 4

Fri 27 Nov 2026 | Week 5 | FDE Mindset | v4 action: Placeholder

[README (placeholder)](Day24-FDE-Mindset-4/README.md)

### Day 25. GenAI 6: Small Language Models + Token Cost and Optimisation

Mon 30 Nov 2026 | Week 6 | GenAI | v4 action: New

[Deck](Day25-SLMs-and-Token-Optimisation/Day25_Deck_SLMs_and_Token_Optimisation.pptx) | [Pre-read](Day25-SLMs-and-Token-Optimisation/Day25_PreRead_SLMs_and_Token_Optimisation.pdf) | [Post-read](Day25-SLMs-and-Token-Optimisation/Day25_PostRead_SLMs_and_Token_Optimisation_Recap_and_Beyond.pdf) | [Notebook](Day25-SLMs-and-Token-Optimisation/Day25_SLMs_and_Token_Optimisation_Colab.ipynb) | [Cost calculator notebook](Day25-SLMs-and-Token-Optimisation/Day25_Token_Cost_Calculator_Colab.ipynb) | [App prompts](Day25-SLMs-and-Token-Optimisation/Day25_App_Build_Prompts.md) | [Hands-on](Day25-SLMs-and-Token-Optimisation/Day25_HandsOn_Problem_Statements.pdf) | [Workbook](Day25-SLMs-and-Token-Optimisation/Day25_Workbook_Interactive.docx) | [Quiz](Day25-SLMs-and-Token-Optimisation/Day25_Quiz_on_Day23_Industry_Use_Cases_and_Agentic_Security_SME.txt) | [Hotel lab](Day25-SLMs-and-Token-Optimisation/Day25_Hotel_Lab.md)

### Day 26. GenAI 7: LLM Orchestration, Tool Calling and LangGraph (1:1 feedback)

Tue 01 Dec 2026 | Week 6 | GenAI | v4 action: Merge

[Deck](Day26-LLM-Orchestration-Tools-and-LangGraph/Day26_Deck_LLM_Orchestration_Tools_and_LangGraph.pptx) | [Pre-read](Day26-LLM-Orchestration-Tools-and-LangGraph/Day26_PreRead_LLM_Orchestration_Tools_and_LangGraph.pdf) | [Post-read](Day26-LLM-Orchestration-Tools-and-LangGraph/Day26_PostRead_LLM_Orchestration_Tools_and_LangGraph_Recap_and_Beyond.pdf) | [Notebook](Day26-LLM-Orchestration-Tools-and-LangGraph/Day26_LLM_Orchestration_Tools_and_LangGraph_Colab.ipynb) | [App prompts](Day26-LLM-Orchestration-Tools-and-LangGraph/Day26_App_Build_Prompts.md) | [Hands-on](Day26-LLM-Orchestration-Tools-and-LangGraph/Day26_HandsOn_Problem_Statements.pdf) | [Workbook](Day26-LLM-Orchestration-Tools-and-LangGraph/Day26_Workbook_Interactive.docx) | [Quiz](Day26-LLM-Orchestration-Tools-and-LangGraph/Day26_Quiz_on_Day25_SLMs_and_Token_Optimisation.txt) | [Hotel lab](Day26-LLM-Orchestration-Tools-and-LangGraph/Day26_Hotel_Lab.md)

### Day 27. GenAI 8: Agentic AI and Agentic RAG (Assessment)

Wed 02 Dec 2026 | Week 6 | GenAI | v4 action: Reuse + update

[Deck](Day27-Agentic-AI-Agentic-RAG-and-Memory/Day27_Deck_Agentic_AI_Agentic_RAG_and_Memory.pptx) | [Pre-read](Day27-Agentic-AI-Agentic-RAG-and-Memory/Day27_PreRead_Agentic_AI_Agentic_RAG_and_Memory.pdf) | [Post-read](Day27-Agentic-AI-Agentic-RAG-and-Memory/Day27_PostRead_Agentic_AI_Agentic_RAG_and_Memory_Recap_and_Beyond.pdf) | [Notebook](Day27-Agentic-AI-Agentic-RAG-and-Memory/Day27_Agentic_AI_Agentic_RAG_and_Memory_Colab.ipynb) | [App prompts](Day27-Agentic-AI-Agentic-RAG-and-Memory/Day27_App_Build_Prompts.md) | [Hands-on](Day27-Agentic-AI-Agentic-RAG-and-Memory/Day27_HandsOn_Problem_Statements.pdf) | [Workbook](Day27-Agentic-AI-Agentic-RAG-and-Memory/Day27_Workbook_Interactive.docx) | [Quiz](Day27-Agentic-AI-Agentic-RAG-and-Memory/Day27_Quiz_on_Day26_LLM_Orchestration_Tools_and_LangGraph.txt) | [Hotel lab](Day27-Agentic-AI-Agentic-RAG-and-Memory/Day27_Hotel_Lab.md)

### Day 28. GenAI 9: Agent Protocols (MCP, A2A) and Advanced Agents (Senior FDE interaction)

Thu 03 Dec 2026 | Week 6 | GenAI | v4 action: Reuse + update

[Deck](Day28-Agent-Protocols-MCP-and-A2A/Day28_Deck_Agent_Protocols_MCP_and_A2A.pptx) | [Pre-read](Day28-Agent-Protocols-MCP-and-A2A/Day28_PreRead_Agent_Protocols_MCP_and_A2A.pdf) | [Post-read](Day28-Agent-Protocols-MCP-and-A2A/Day28_PostRead_Agent_Protocols_MCP_and_A2A_Recap_and_Beyond.pdf) | [Notebook](Day28-Agent-Protocols-MCP-and-A2A/Day28_Agent_Protocols_MCP_and_A2A_Colab.ipynb) | [App prompts](Day28-Agent-Protocols-MCP-and-A2A/Day28_App_Build_Prompts.md) | [Hands-on](Day28-Agent-Protocols-MCP-and-A2A/Day28_HandsOn_Problem_Statements.pdf) | [Workbook](Day28-Agent-Protocols-MCP-and-A2A/Day28_Workbook_Interactive.docx) | [Quiz](Day28-Agent-Protocols-MCP-and-A2A/Day28_Quiz_on_Day27_Agentic_AI_Agentic_RAG_and_Memory.txt) | [Hotel lab](Day28-Agent-Protocols-MCP-and-A2A/Day28_Hotel_Lab.md)

### Day 29. FDE Mindset Session 5

Fri 04 Dec 2026 | Week 6 | FDE Mindset | v4 action: Placeholder

[README (placeholder)](Day29-FDE-Mindset-5/README.md)

### Day 30. GenAI 10: LLM Security and Guardrails (Vulnerability report v3)

Mon 07 Dec 2026 | Week 7 | GenAI | v4 action: Reuse + update

[Deck](Day30-LLM-Security-and-Guardrails/Day30_Deck_LLM_Security_and_Guardrails.pptx) | [Pre-read](Day30-LLM-Security-and-Guardrails/Day30_PreRead_LLM_Security_and_Guardrails.pdf) | [Post-read](Day30-LLM-Security-and-Guardrails/Day30_PostRead_LLM_Security_and_Guardrails_Recap_and_Beyond.pdf) | [Notebook](Day30-LLM-Security-and-Guardrails/Day30_LLM_Security_and_Guardrails_Colab.ipynb) | [App prompts](Day30-LLM-Security-and-Guardrails/Day30_App_Build_Prompts.md) | [Hands-on](Day30-LLM-Security-and-Guardrails/Day30_HandsOn_Problem_Statements.pdf) | [Workbook](Day30-LLM-Security-and-Guardrails/Day30_Workbook_Interactive.docx) | [Quiz](Day30-LLM-Security-and-Guardrails/Day30_Quiz_on_Day28_Agent_Protocols_MCP_and_A2A.txt) | [Hotel lab](Day30-LLM-Security-and-Guardrails/Day30_Hotel_Lab.md)

### Day 31. GenAI 11: GenAI System Evaluation

Tue 08 Dec 2026 | Week 7 | GenAI | v4 action: Reuse + update

[Deck](Day31-GenAI-System-Evaluation/Day31_Deck_GenAI_System_Evaluation.pptx) | [Pre-read](Day31-GenAI-System-Evaluation/Day31_PreRead_GenAI_System_Evaluation.pdf) | [Post-read](Day31-GenAI-System-Evaluation/Day31_PostRead_GenAI_System_Evaluation_Recap_and_Beyond.pdf) | [Notebook](Day31-GenAI-System-Evaluation/Day31_GenAI_System_Evaluation_Colab.ipynb) | [App prompts](Day31-GenAI-System-Evaluation/Day31_App_Build_Prompts.md) | [Hands-on](Day31-GenAI-System-Evaluation/Day31_HandsOn_Problem_Statements.pdf) | [Workbook](Day31-GenAI-System-Evaluation/Day31_Workbook_Interactive.docx) | [Quiz](Day31-GenAI-System-Evaluation/Day31_Quiz_on_Day30_LLM_Security_and_Guardrails.txt) | [Hotel lab](Day31-GenAI-System-Evaluation/Day31_Hotel_Lab.md)

### Day 32. GenAI 12: LLM Evaluation and Quality Gates (1:1 feedback)

Wed 09 Dec 2026 | Week 7 | GenAI | v4 action: Reuse + update

[Deck](Day32-LLM-Evaluation-and-Quality-Gates/Day32_Deck_LLM_Evaluation_and_Quality_Gates.pptx) | [Pre-read](Day32-LLM-Evaluation-and-Quality-Gates/Day32_PreRead_LLM_Evaluation_and_Quality_Gates.pdf) | [Post-read](Day32-LLM-Evaluation-and-Quality-Gates/Day32_PostRead_LLM_Evaluation_and_Quality_Gates_Recap_and_Beyond.pdf) | [Notebook](Day32-LLM-Evaluation-and-Quality-Gates/Day32_LLM_Evaluation_and_Quality_Gates_Colab.ipynb) | [App prompts](Day32-LLM-Evaluation-and-Quality-Gates/Day32_App_Build_Prompts.md) | [Hands-on](Day32-LLM-Evaluation-and-Quality-Gates/Day32_HandsOn_Problem_Statements.pdf) | [Workbook](Day32-LLM-Evaluation-and-Quality-Gates/Day32_Workbook_Interactive.docx) | [Quiz](Day32-LLM-Evaluation-and-Quality-Gates/Day32_Quiz_on_Day31_GenAI_System_Evaluation.txt) | [Hotel lab](Day32-LLM-Evaluation-and-Quality-Gates/Day32_Hotel_Lab.md)

### Day 33. GenAI 13: LLMOps (Assessment)

Thu 10 Dec 2026 | Week 7 | GenAI | v4 action: Merge

[Deck](Day33-LLMOps/Day33_Deck_LLMOps.pptx) | [Pre-read](Day33-LLMOps/Day33_PreRead_LLMOps.pdf) | [Post-read](Day33-LLMOps/Day33_PostRead_LLMOps_Recap_and_Beyond.pdf) | [Notebook](Day33-LLMOps/Day33_LLMOps_Colab.ipynb) | [App prompts](Day33-LLMOps/Day33_App_Build_Prompts.md) | [Hands-on](Day33-LLMOps/Day33_HandsOn_Problem_Statements.pdf) | [Workbook](Day33-LLMOps/Day33_Workbook_Interactive.docx) | [Quiz](Day33-LLMOps/Day33_Quiz_on_Day32_LLM_Evaluation_and_Quality_Gates.txt) | [Hotel lab](Day33-LLMOps/Day33_Hotel_Lab.md)

### Day 34. GenAI 14: LLM Deployment and Lifecycle

Fri 11 Dec 2026 | Week 7 | GenAI | v4 action: Reuse + update

[Deck](Day34-LLM-Deployment-and-Lifecycle/Day34_Deck_LLM_Deployment_and_Lifecycle.pptx) | [Pre-read](Day34-LLM-Deployment-and-Lifecycle/Day34_PreRead_LLM_Deployment_and_Lifecycle.pdf) | [Post-read](Day34-LLM-Deployment-and-Lifecycle/Day34_PostRead_LLM_Deployment_and_Lifecycle_Recap_and_Beyond.pdf) | [Notebook](Day34-LLM-Deployment-and-Lifecycle/Day34_LLM_Deployment_and_Lifecycle_Colab.ipynb) | [App prompts](Day34-LLM-Deployment-and-Lifecycle/Day34_App_Build_Prompts.md) | [Hands-on](Day34-LLM-Deployment-and-Lifecycle/Day34_HandsOn_Problem_Statements.pdf) | [Workbook](Day34-LLM-Deployment-and-Lifecycle/Day34_Workbook_Interactive.docx) | [Quiz](Day34-LLM-Deployment-and-Lifecycle/Day34_Quiz_on_Day33_LLMOps.txt) | [Hotel lab](Day34-LLM-Deployment-and-Lifecycle/Day34_Hotel_Lab.md)

### Day 35. GenAI 15: Observability, Drift and Optimisation

Mon 14 Dec 2026 | Week 8 | GenAI | v4 action: Merge

[Deck](Day35-Observability-Drift-and-Optimisation/Day35_Deck_Observability_Drift_and_Optimisation.pptx) | [Pre-read](Day35-Observability-Drift-and-Optimisation/Day35_PreRead_Observability_Drift_and_Optimisation.pdf) | [Post-read](Day35-Observability-Drift-and-Optimisation/Day35_PostRead_Observability_Drift_and_Optimisation_Recap_and_Beyond.pdf) | [Notebook](Day35-Observability-Drift-and-Optimisation/Day35_Observability_Drift_and_Optimisation_Colab.ipynb) | [App prompts](Day35-Observability-Drift-and-Optimisation/Day35_App_Build_Prompts.md) | [Hands-on](Day35-Observability-Drift-and-Optimisation/Day35_HandsOn_Problem_Statements.pdf) | [Workbook](Day35-Observability-Drift-and-Optimisation/Day35_Workbook_Interactive.docx) | [Quiz](Day35-Observability-Drift-and-Optimisation/Day35_Quiz_on_Day34_LLM_Deployment_and_Lifecycle.txt) | [Hotel lab](Day35-Observability-Drift-and-Optimisation/Day35_Hotel_Lab.md)

### Days 36 to 40. Capstone project (Demo day 21 Dec)

Tue 15 to Mon 21 Dec 2026 | Week 8 to 9 | Capstone | v4 action: Update

[Capstone README](Day36-40-Capstone/README.md)


## 10. Using the quiz files

Each quiz file holds 15 questions as CSV rows: question, options A to D, the correct letter, and a one-line explanation. Paste them into the quiz tool (Kahoot or similar) at the start of the day. The quiz always tests the previous training day; FDE Mindset days and the holiday are skipped.

## 11. Using the hotel labs

Every technical day has a `DayNN_Hotel_Lab.md`: the 90 to 120 minute evening hands-on learners do at the hotel after the post-read. It lists steps, time per step, the files to open and what to submit. Every hotel lab runs in the browser through Google Colab, except where Docker Desktop or Azure is stated. Template: [shared/templates/Hotel_Lab_Template.md](shared/templates/Hotel_Lab_Template.md).

## 12. Using the app build prompts

1. Open the project in VS Code and the OpenAI Codex panel, signed in with the program key.
2. Use one prompt at a time. Ask for a plan first on anything that touches several files.
3. Read every diff. Run the tests after every step.
4. Never paste keys, customer data or credentials into a prompt. Check daily token usage.
5. The last prompt in each file is the SmartDesk step for that day.

See [docs/CODEX_GUIDE.md](docs/CODEX_GUIDE.md) and the printable [Codex card](shared/Codex_Setup_and_Dos_Donts.pdf).

## 13. Suggested preparation for each session

- **Trainer, the day before:** run the notebook top to bottom in Colab (offline and, if available, online); skim the deck for `NEW (v4)` slides; check model names against the approved list; load the quiz.
- **Learners, the evening before:** finish the hotel lab, then read the next pre-read (about 15 minutes).
- **Azure days (17, 20, 21, 34, 38 to 40):** confirm the subscription window is open ([docs/ACCESS_AND_INSTALL.md](docs/ACCESS_AND_INSTALL.md)). Delete resource groups after each window.
- **Before Day 1:** every learner completes the [Laptop Setup Guide](shared/Laptop_Setup_Guide.pdf).

## 14. Shared materials

| Item | Path |
| --- | --- |
| Model guide | [docs/MODEL_GUIDE.md](docs/MODEL_GUIDE.md) |
| OpenAI Codex guide | [docs/CODEX_GUIDE.md](docs/CODEX_GUIDE.md) |
| Access and install plan | [docs/ACCESS_AND_INSTALL.md](docs/ACCESS_AND_INSTALL.md) |
| Changelog | [docs/CHANGELOG_v4.md](docs/CHANGELOG_v4.md) |
| Laptop Setup Guide | [shared/Laptop_Setup_Guide.pdf](shared/Laptop_Setup_Guide.pdf) |
| Codex setup and do's and don'ts card | [shared/Codex_Setup_and_Dos_Donts.pdf](shared/Codex_Setup_and_Dos_Donts.pdf) |
| Vulnerability report template | [shared/templates/Vulnerability_Report_Template.md](shared/templates/Vulnerability_Report_Template.md) |
| Hotel lab template | [shared/templates/Hotel_Lab_Template.md](shared/templates/Hotel_Lab_Template.md) |
| AGENTS.md template for learner repos | [shared/templates/AGENTS_learner_template.md](shared/templates/AGENTS_learner_template.md) |
| OWASP agentic checklist | [shared/templates/OWASP_Agentic_Checklist.md](shared/templates/OWASP_Agentic_Checklist.md) |
| Patch and Modernise starter repo | [shared/PatchAndModernise_Starter](shared/PatchAndModernise_Starter/README.md) |
| SmartDesk | [shared/SmartDesk](shared/SmartDesk/README.md) |

## 15. Maintaining the materials

Each technical day is generated from one spec file in `tools/build/specs/dayNN.py`. Edit the spec, then run `python tools/build/build_day.py NN` to rebuild the deck, pre-read, post-read, hands-on PDF, workbook and notebook in the v1 visual style. App prompts, quizzes and hotel labs are plain files in the day folder. Run `python tools/build/lint_content.py`, `python tools/check_notebooks.py` and `python tools/check_links.py` before you open a pull request.
