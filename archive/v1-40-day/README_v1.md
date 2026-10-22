# Forward Deployed Engineer Program

Course materials for **Prodapt** and **SoftBank Japan**.

Prepared by Ahmed. **40 days, complete.** Days 01 to 35 are taught sessions. Days 36 to 40 are the capstone project.

This file is the navigation guide. Pick a day from the index, open what you need.

---

## 1. How the program is laid out

| Folders | What they are |
| --- | --- |
| `Day01-...` to `Day35-...` | One folder per taught session, eight files each |
| `Day36-40-Capstone` | A single folder for the five day capstone, organised by project rather than by day |

Folders are named `DayNN-Topic`, so you can find a session by subject without opening anything.

```text
Day09-FastAPI-MongoDB-and-JavaScript-Basics
Day23-RAG-Embeddings-and-Vector-DBs
Day34-Observability-and-Monitoring
```

Files inside keep their original `DayNN_` prefix, so a file still tells you its day when it is moved or attached on its own.

## 2. The eight files in every taught day, Days 01 to 35

| File pattern | Type | What it is | When to use it |
| --- | --- | --- | --- |
| `DayNN_Deck_*.pptx` | Slides | The session deck | Present in class |
| `DayNN_PreRead_*.pdf` | PDF | A short, non-technical read | Send before class |
| `DayNN_PostRead_*.pdf` | PDF | Recap of the day plus topics that go further | Send after class |
| `DayNN_*_Colab.ipynb` | Notebook | Live demos. Option A cells run in Colab, Option B cells (commented) are for VS Code | Demo during the session |
| `DayNN_App_Build_Prompts.md` | Markdown | Prompts for building the day's app with an AI coding assistant | Give to learners for the build |
| `DayNN_HandsOn_Problem_Statements.pdf` | PDF | Practice problems, warm-up through to stretch | Lab time and homework |
| `DayNN_Workbook_Interactive.docx` | Word | Fill in the blanks, short answers, predict the output, write code | Reinforcement |
| `DayNN_Quiz_on_DayMM_*.txt` | CSV in a .txt | 15 questions on the **previous** day, as CSV rows | Open the session |

### Three things to watch

1. **Quizzes look backwards.** The quiz in Day 05 tests Day 04. That is why Day 01 has no quiz, and why the quiz for Day 36 sits inside the capstone folder rather than in a Day 35 folder.
2. **Days 15 and 20 differ.** Full days on professional skills. The hands-on PDF holds simulation and role play cards instead of coding problems, and the workbook uses writing practice instead of code boxes.
3. **Days 21 onward are GenAI.** These notebooks need an LLM API key, or they fall back to an offline demo mode. See section 6.

## 3. Session types

| Tag | Days | Meaning |
| --- | --- | --- |
| `assessment day` | 05, 11, 17, 21, 26, 32 | A formal assessment runs in the session. Day 32 runs 1.5 hours |
| `full day` | 15, 20 | Full day on FDE professional skills, role play rather than coding |
| `senior FDE session` | 22, 27 | Senior FDE joins. Day 22 is a feedback discussion, Day 27 is the FDE assessment debrief |
| `1:1 feedback` | 25, 30 | One-on-one feedback runs alongside the session |

## 4. Program at a glance

| Day | Topic | App of the day | Quiz covers |
| --- | --- | --- | --- |
| [01](Day01-Python-Basics) | Python Basics | Smart Study Planner (command line app in Python) | no quiz |
| [02](Day02-Functions-Data-Structures-and-Files) | Functions Data Structures and Files | Personal Expense Tracker (command line, saves to JSON) | Day 01 |
| [03](Day03-OOP-and-Design-Principles) | OOP and Design Principles | Mini Library Management System (OOP, command line) | Day 02 |
| [04](Day04-Architecture-and-MongoDB) | Architecture and MongoDB | Inventory Dashboard (Python + MongoDB + Matplotlib) | Day 03 |
| [05](Day05-API-Fundamentals-and-FastAPI) | API Fundamentals and FastAPI `assessment day` | Quotes and Notes REST API (FastAPI, in memory) | Day 04 |
| [06](Day06-FastAPI-Core-and-SQLAlchemy-Intro) | FastAPI Core and SQLAlchemy Intro | Library Books API (FastAPI + Pydantic + SQLAlchemy + SQLite) | Day 05 |
| [07](Day07-SQLAlchemy-and-API-Docs) | SQLAlchemy and API Docs | Library API v2: authors, books, tags and loans | Day 06 |
| [08](Day08-FastAPI-Advanced-and-Security) | FastAPI Advanced and Security | Secure Notes API (FastAPI + JWT + MongoDB) | Day 07 |
| [09](Day09-FastAPI-MongoDB-and-JavaScript-Basics) | FastAPI MongoDB and JavaScript Basics | Shop Analytics API (FastAPI + MongoDB) with a JavaScript data script | Day 08 |
| [10](Day10-Async-JavaScript-and-Node-js) | Async JavaScript and Node js | Tasks API in Express with an async client and Postman tests | Day 09 |
| [11](Day11-React-Basics) | React Basics `assessment day` | Personal Dashboard (React components, props, state and events) | Day 10 |
| [12](Day12-React-UI-Logic-and-API-Integration) | React UI Logic and API Integration | Full Stack Task Board (React + FastAPI) | Day 11 |
| [13](Day13-Testing-and-Data-Engineering-Intro) | Testing and Data Engineering Intro | Tested Order Ingestion Service (pandas ETL + FastAPI + PyTest) | Day 12 |
| [14](Day14-Data-Pipelines-and-Spark-Intro) | Data Pipelines and Spark Intro | Retail Sales Batch Pipeline (PySpark, medallion layers) | Day 13 |
| [15](Day15-FDE-Professional-Skills-1) | FDE Professional Skills 1 `full day` | FDE Field Notebook (FastAPI + React) | Day 14 |
| [16](Day16-PySpark-Batch-Pipelines-and-SQL) | PySpark Batch Pipelines and SQL | Sales Insights Pipeline with a SQL Question Bank (PySpark + Spark SQL + FastAPI) | Day 15 |
| [17](Day17-DevOps-and-Cloud-Fundamentals) | DevOps and Cloud Fundamentals `assessment day` | DevOps-ready FastAPI Service (tests, lint, pipeline YAML) | Day 16 |
| [18](Day18-Git-CI-CD-and-Docker) | Git CI CD and Docker | Containerised Task API with Git workflow and multi-stage pipeline | Day 17 |
| [19](Day19-Containers-and-Azure-Deployment) | Containers and Azure Deployment | Deploy the Full Stack Task Board to Azure (Containers + CD) | Day 18 |
| [20](Day20-FDE-Professional-Skills-2) | FDE Professional Skills 2 `full day` | Request Log Investigator (FastAPI + React mini tool) | Day 19 |
| [21](Day21-GenAI-Intro-and-Prompt-Engineering) | GenAI Intro and Prompt Engineering `assessment day` | Prompt Playground (FastAPI + React) with prompt templates | Day 20 |
| [22](Day22-Context-Engineering-and-RAG) | Context Engineering and RAG `senior FDE session` | Policy Q&A Assistant v1 (RAG with chunking and citations) | Day 21 |
| [23](Day23-RAG-Embeddings-and-Vector-DBs) | RAG Embeddings and Vector DBs | Policy Q&A Assistant v2 (hybrid search, re-ranking, citations) | Day 22 |
| [24](Day24-FDE-Skills-3a-and-LLM-Orchestration) | FDE Skills 3a and LLM Orchestration | Meeting Notes Assistant (LangChain chains + FastAPI) | Day 23 |
| [25](Day25-LLM-Orchestration-and-FDE-Skills-3b) | LLM Orchestration and FDE Skills 3b `1:1 feedback` | Customer Support Copilot (tool calling + LangGraph) | Day 24 |
| [26](Day26-Agentic-AI-and-Agentic-RAG) | Agentic AI and Agentic RAG `assessment day` | Agentic HR and Ops Assistant (CRAG + supervisor agents) | Day 25 |
| [27](Day27-Agent-Protocols-and-Advanced-Use-Cases) | Agent Protocols and Advanced Use Cases `senior FDE session` | Enterprise Agent Hub (MCP servers + A2A-style agents + data agent) | Day 26 |
| [28](Day28-LLM-Security-and-Guardrails) | LLM Security and Guardrails | Guardrail Gateway for LLM Apps (FastAPI middleware + red-team suite) | Day 27 |
| [29](Day29-GenAI-System-Evaluation) | GenAI System Evaluation | RAG Evaluation Dashboard (metrics, error analysis, slices) | Day 28 |
| [30](Day30-LLM-Evaluation-and-QA) | LLM Evaluation and QA `1:1 feedback` | LLM Quality Gate for CI (golden sets + regression tests + reports) | Day 29 |
| [31](Day31-LLMOps-Intro-and-FDE-Skills-4) | LLMOps Intro and FDE Skills 4 | Resilient LLM Client and Incident Toolkit | Day 30 |
| [32](Day32-LLMOps) | LLMOps `assessment day` | LLM Cost and Version Control Center | Day 31 |
| [33](Day33-LLM-Deployment-and-Lifecycle) | LLM Deployment and Lifecycle | Production LLM Gateway (FastAPI, async, streaming, canary) | Day 32 |
| [34](Day34-Observability-and-Monitoring) | Observability and Monitoring | LLM Observability Starter Kit (logs, traces, dashboard, feedback) | Day 33 |
| [35](Day35-Drift-Detection-and-Optimization) | Drift Detection and Optimization | Drift Watch: automated drift and quality monitoring | Day 34 |
| [36 to 40](Day36-40-Capstone) | Capstone Project, five days | One of five team projects | Day 35 (quiz sits in the capstone folder) |

## 5. The program in blocks

| Block | Focus | Days |
| --- | --- | --- |
| Days 01 to 04 | Python and data foundations | [01](Day01-Python-Basics), [02](Day02-Functions-Data-Structures-and-Files), [03](Day03-OOP-and-Design-Principles), [04](Day04-Architecture-and-MongoDB) |
| Days 05 to 08 | APIs and backend with FastAPI | [05](Day05-API-Fundamentals-and-FastAPI), [06](Day06-FastAPI-Core-and-SQLAlchemy-Intro), [07](Day07-SQLAlchemy-and-API-Docs), [08](Day08-FastAPI-Advanced-and-Security) |
| Days 09 to 10 | JavaScript and Node.js | [09](Day09-FastAPI-MongoDB-and-JavaScript-Basics), [10](Day10-Async-JavaScript-and-Node-js) |
| Days 11 to 12 | React and full stack | [11](Day11-React-Basics), [12](Day12-React-UI-Logic-and-API-Integration) |
| Days 13 to 14 | Testing and data engineering | [13](Day13-Testing-and-Data-Engineering-Intro), [14](Day14-Data-Pipelines-and-Spark-Intro) |
| Day 15 | FDE professional skills 1 | [15](Day15-FDE-Professional-Skills-1) |
| Day 16 | PySpark batch pipelines and SQL | [16](Day16-PySpark-Batch-Pipelines-and-SQL) |
| Days 17 to 19 | DevOps, containers and Azure | [17](Day17-DevOps-and-Cloud-Fundamentals), [18](Day18-Git-CI-CD-and-Docker), [19](Day19-Containers-and-Azure-Deployment) |
| Day 20 | FDE professional skills 2 | [20](Day20-FDE-Professional-Skills-2) |
| Days 21 to 23 | GenAI, prompting and RAG | [21](Day21-GenAI-Intro-and-Prompt-Engineering), [22](Day22-Context-Engineering-and-RAG), [23](Day23-RAG-Embeddings-and-Vector-DBs) |
| Days 24 to 25 | LLM orchestration and FDE skills 3 | [24](Day24-FDE-Skills-3a-and-LLM-Orchestration), [25](Day25-LLM-Orchestration-and-FDE-Skills-3b) |
| Days 26 to 27 | Agentic AI and agent protocols | [26](Day26-Agentic-AI-and-Agentic-RAG), [27](Day27-Agent-Protocols-and-Advanced-Use-Cases) |
| Days 28 to 30 | LLM security, evaluation and QA | [28](Day28-LLM-Security-and-Guardrails), [29](Day29-GenAI-System-Evaluation), [30](Day30-LLM-Evaluation-and-QA) |
| Days 31 to 35 | LLMOps, deployment and monitoring | [31](Day31-LLMOps-Intro-and-FDE-Skills-4), [32](Day32-LLMOps), [33](Day33-LLM-Deployment-and-Lifecycle), [34](Day34-Observability-and-Monitoring), [35](Day35-Drift-Detection-and-Optimization) |
| Days 36 to 40 | Capstone project | [36 to 40](Day36-40-Capstone) |

## 6. Running the notebooks

### Days 01 to 20, general

- **Colab:** upload the `.ipynb` file and run the cells top to bottom.
- **VS Code:** install Python, plus the Python and Jupyter extensions. Open the notebook, then comment out the Option A cells and uncomment Option B where the notebook shows you.

| Days | What you need |
| --- | --- |
| 04, 08, 09 (MongoDB) | Colab uses `mongomock`. In VS Code, set `MONGO_URI` to a local MongoDB or a free Atlas cluster |
| 09, 10 (Node.js) | Install Node.js LTS for the VS Code path |
| 11, 12 (React) | `show_react()` renders React inside the notebook output and needs internet for the React CDN. For real projects use Vite in VS Code as the notebook describes |
| 12 (full stack) | In Colab the app opens inside the notebook. In VS Code run `uvicorn fullstack:app --reload` and open `http://127.0.0.1:8000` |
| 14, 16 (Spark) | Works in Colab after `pip install pyspark`. In VS Code install Java 17 first |
| 18, 19 (Docker and Azure) | Docker commands need Docker Desktop. Azure commands run in Azure Cloud Shell |

### Days 21 to 35, GenAI and LLMOps

- **With an API key:** in Colab open Secrets (the key icon), add `OPENAI_API_KEY` and allow notebook access. In VS Code set the environment variable or use a `.env` file. Set `LLM_MODEL` to a current chat model you have access to. The notebooks default to `gpt-4o-mini`.
- **Without a key:** every cell still runs in offline demo mode using a small, clearly labelled stand-in model. Offline scores show how the code works, not how real models perform. Say this to the room before you demo, so nobody quotes an offline score as a real benchmark.

| Day | What to know |
| --- | --- |
| 27 (MCP) | The notebook pins the MCP Python SDK below version 2, because v2 renamed some APIs |
| 28 (security) | All attacks target a simulated bot |
| 32 (LLMOps) | Fine-tuning is switched off by default with `RUN_FINE_TUNE = False`, because running it costs money. Turn it on deliberately |
| 32, 34 (cost) | Prices in these notebooks are illustrative placeholders. Use your provider's current pricing before quoting any figure |

> **Day 28 caution.** Only test systems you own or are authorised to test.

> **Azure caution (Days 18, 19, 33 and the capstone).** Only use subscriptions you have permission to use, tag resources, and delete test resource groups once you are done.

## 7. The capstone, Days 36 to 40

Everything for the final week lives in [Day36-40-Capstone](Day36-40-Capstone). It is organised by project, not by day, because all five days run on the same team project.

Teams of 3 to 4 build one complete product end to end, using everything from Days 01 to 35. Two teams may pick the same project and are compared on the same checklist. The guide states the goal plainly: depth beats breadth, and a smaller scope done well scores higher than many half-finished features.

### What is in the folder

| Open | What it is |
| --- | --- |
| [Capstone guide](Day36-40-Capstone/00_Capstone_Guide.pdf) | The full brief: plan, rules, deliverables, demo format, rubric, grade bands, checklist. Read this first |
| [Kickoff deck](Day36-40-Capstone/Capstone_Kickoff_Deck.pptx) | Day 36 kickoff: projects, schedule, baseline, rubric, demo day |
| [Evaluator scoring sheet](Day36-40-Capstone/Capstone_Evaluator_Scoring_Sheet.xlsx) | Rubric with one sheet per team, up to 8 teams, automatic totals, grade bands and a summary |
| [Quiz on Day 35](Day36-40-Capstone/Day36_Quiz_on_Day35_Drift_Detection_and_Optimization.txt) | Runs at the start of Day 36 |
| [Projects/](Day36-40-Capstone/Projects) | The five project briefs |
| [Starter_Notebooks/](Day36-40-Capstone/Starter_Notebooks) | One per project. Generates the data, runs a baseline, seeds the golden set |
| [App_Build_Prompts/](Day36-40-Capstone/App_Build_Prompts) | Four day-by-day prompts per project for an AI coding assistant |

### The five projects

Each team picks one in the first hour of Day 36.

| # | Project | What it is | Core skills | Brief | Starter | Prompts |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | **ShopSmart** | E-commerce Recommendation and Shopping Assistant | Embeddings for product descriptions, hybrid search with RRF | [PDF](Day36-40-Capstone/Projects/Capstone_01_ShopSmart_Brief.pdf) | [ipynb](Day36-40-Capstone/Starter_Notebooks/Capstone_01_ShopSmart_Starter.ipynb) | [md](Day36-40-Capstone/App_Build_Prompts/Capstone_01_ShopSmart_Prompts.md) |
| 02 | **BookFinder** | Library Book Finder with Natural Language Search | Embeddings and hybrid search with RRF | [PDF](Day36-40-Capstone/Projects/Capstone_02_BookFinder_Brief.pdf) | [ipynb](Day36-40-Capstone/Starter_Notebooks/Capstone_02_BookFinder_Starter.ipynb) | [md](Day36-40-Capstone/App_Build_Prompts/Capstone_02_BookFinder_Prompts.md) |
| 03 | **PolicyPal** | Enterprise HR and IT Policy Chatbot | Context engineering and chunking | [PDF](Day36-40-Capstone/Projects/Capstone_03_PolicyPal_Brief.pdf) | [ipynb](Day36-40-Capstone/Starter_Notebooks/Capstone_03_PolicyPal_Starter.ipynb) | [md](Day36-40-Capstone/App_Build_Prompts/Capstone_03_PolicyPal_Prompts.md) |
| 04 | **SupportPilot** | Agentic Customer Support Copilot | Tool calling and LangGraph | [PDF](Day36-40-Capstone/Projects/Capstone_04_SupportPilot_Brief.pdf) | [ipynb](Day36-40-Capstone/Starter_Notebooks/Capstone_04_SupportPilot_Starter.ipynb) | [md](Day36-40-Capstone/App_Build_Prompts/Capstone_04_SupportPilot_Prompts.md) |
| 05 | **InsightDesk** | Retail Sales Pipeline and Natural Language Data Agent | Data agent with sandboxed code | [PDF](Day36-40-Capstone/Projects/Capstone_05_InsightDesk_Brief.pdf) | [ipynb](Day36-40-Capstone/Starter_Notebooks/Capstone_05_InsightDesk_Starter.ipynb) | [md](Day36-40-Capstone/App_Build_Prompts/Capstone_05_InsightDesk_Prompts.md) |

### Technical baseline, every project

| Requirement | From days |
| --- | --- |
| FastAPI back end with Pydantic models and at least 6 endpoints | 05 to 08 |
| A database: SQL with SQLAlchemy and / or MongoDB | 04, 06 to 09 |
| React front end with loading, error and empty states | 11, 12 |
| An AI component: RAG, recommendation with embeddings, agent or data agent | 21 to 27 |
| Tests with PyTest and a GitHub or Azure DevOps CI pipeline | 13, 17, 18 |
| Dockerfile and docker-compose, Azure deployment or documented steps | 18, 19, 33 |
| Guardrails and secrets handling | 08, 28 |
| Golden set, metrics and a quality gate | 29, 30 |
| Structured logs and a monitoring report or dashboard | 34, 35 |

### Day by day

A 15 minute stand-up opens each day from Day 37: what I finished yesterday, what I will finish today, what is blocking me. Mentors join at least once a day.

| Day | Date | Focus | Work | Checkpoint |
| --- | --- | --- | --- | --- |
| 36 | Mon 14 Dec 2026 | Kick-off and design | Quiz on Day 35. Teams of 3 to 4 formed and project chosen. Problem statement, users, success metrics, assumptions log. Architecture diagram and data model. Repository, board and CI skeleton. | Checkpoint 1: design review with mentor |
| 37 | Tue 15 Dec 2026 | Core build | Data loaded. Back end API with main endpoints. AI core working end to end. Golden set draft of 20 items. | Checkpoint 2: walking skeleton demo |
| 38 | Wed 16 Dec 2026 | Complete features and quality | Front end connected to the API. Guardrails and error handling. Evaluation run and first error analysis. Tests in CI, quality gate added. | Checkpoint 3: feature-complete MVP |
| 39 | Thu 17 Dec 2026 | Harden, deploy, observe | Docker images. Deploy to Azure or a documented local deployment. Structured logs and a monitoring view. Red-team and slice checks. Demo rehearsal with peer feedback. | Code freeze at 17:00 IST |
| 40 | Fri 18 Dec 2026 | Demo day | Final rehearsal in the morning. Demo of 10 minutes plus 5 minutes Q and A per team. Evaluator scoring with the rubric. Individual reflection and peer feedback. | Closing and certificates |

Dates come from the capstone guide. Confirm them against the delivery schedule before you publish them to learners.

### Deliverables, due Day 40 at 09:00 IST

| Deliverable | Details |
| --- | --- |
| Repository | Code, tests, Dockerfiles, pipeline YAML, golden set, README with setup, architecture and AI tool disclosure |
| Architecture diagram | Components, data flow, where AI is used, guardrails |
| Evaluation report | Golden set results, metrics, error analysis, slices, known limits |
| Operations note | How to deploy, monitor and roll back. One runbook |
| Demo deck | 8 to 12 slides: problem, solution, demo, results, limits, next steps |
| Decision log | Key decisions with options, reasons and dates |

### Demo day format

- 10 minutes: problem and users (1), live demo (5), results and evaluation (2), limits and next steps (2).
- 5 minutes of Q and A from evaluators acting as the customer's sponsor, IT lead and security lead.
- Every team member speaks. Lead with the answer, show evidence, be honest about limits.

### Rubric, 100 points

| Criterion | Points |
| --- | --- |
| Problem understanding and scoping | 10 |
| Architecture and design | 10 |
| Core functionality | 20 |
| AI and data quality | 15 |
| Engineering quality | 10 |
| Security, guardrails and responsible AI | 10 |
| Deployment and operations | 10 |
| Demo and communication | 10 |
| Teamwork and process | 5 |
| **Total** | **100** |

Each criterion is scored on four levels, and points equal weight times level divided by 4.

| Level | Meaning |
| --- | --- |
| 4 Excellent | Goes beyond the brief, production-minded, evidence for every claim |
| 3 Good | Meets the brief fully with minor gaps |
| 2 Developing | Partly meets the brief, important gaps or untested parts |
| 1 Beginning | Major parts missing or not working |

| Grade band | Score |
| --- | --- |
| Distinction | 85 to 100 |
| Merit | 70 to 84 |
| Pass | 55 to 69 |
| Needs resubmission | Below 55 |

Individual scores can be adjusted by up to 10 points based on peer feedback and Q and A.

### Rules to state at kickoff

1. AI coding assistants are allowed and encouraged. Teams disclose in the README which parts were generated and how they reviewed them.
2. Use only the generated or public sample data. Never use real customer or personal data.
3. Keep secrets out of Git. Use environment variables or a secret store.
4. Every team member must be able to explain every part of the system during Q and A.
5. Cloud resources: use tags, stay within the agreed budget, and delete resource groups after demo day.

### Submission checklist

- README lets a stranger run the project in under 15 minutes
- CI pipeline is green on main
- Golden set and evaluation report are committed
- No secrets or personal data in the repository
- Demo works without internet surprises, with a recorded backup ready
- Azure resources tagged and scheduled for deletion

## 8. Day by day index, Days 01 to 35

Every file below links straight to it.

### Days 01 to 04. Python and data foundations

#### Day 01. Python Basics

Folder: `Day01-Python-Basics`

App of the day: **Smart Study Planner (command line app in Python)**

| Open | File |
| --- | --- |
| [Deck](Day01-Python-Basics/Day01_Deck_Python_Basics.pptx) | `Day01_Deck_Python_Basics.pptx` |
| [Pre-read](Day01-Python-Basics/Day01_PreRead_Talking_to_Computers.pdf) | `Day01_PreRead_Talking_to_Computers.pdf` |
| [Post-read](Day01-Python-Basics/Day01_PostRead_Recap_and_Beyond.pdf) | `Day01_PostRead_Recap_and_Beyond.pdf` |
| [Notebook](Day01-Python-Basics/Day01_Python_Basics_Colab.ipynb) | `Day01_Python_Basics_Colab.ipynb` |
| [App prompts](Day01-Python-Basics/Day01_App_Build_Prompts.md) | `Day01_App_Build_Prompts.md` |
| [Hands-on](Day01-Python-Basics/Day01_HandsOn_Problem_Statements.pdf) | `Day01_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day01-Python-Basics/Day01_Workbook_Interactive.docx) | `Day01_Workbook_Interactive.docx` |

#### Day 02. Functions Data Structures and Files

Folder: `Day02-Functions-Data-Structures-and-Files`

App of the day: **Personal Expense Tracker (command line, saves to JSON)**

| Open | File |
| --- | --- |
| [Deck](Day02-Functions-Data-Structures-and-Files/Day02_Deck_Functions_Data_Structures_and_Files.pptx) | `Day02_Deck_Functions_Data_Structures_and_Files.pptx` |
| [Pre-read](Day02-Functions-Data-Structures-and-Files/Day02_PreRead_Organising_Things.pdf) | `Day02_PreRead_Organising_Things.pdf` |
| [Post-read](Day02-Functions-Data-Structures-and-Files/Day02_PostRead_Functions_Data_and_Files_Recap_and_Beyond.pdf) | `Day02_PostRead_Functions_Data_and_Files_Recap_and_Beyond.pdf` |
| [Notebook](Day02-Functions-Data-Structures-and-Files/Day02_Functions_Data_Structures_and_Files_Colab.ipynb) | `Day02_Functions_Data_Structures_and_Files_Colab.ipynb` |
| [App prompts](Day02-Functions-Data-Structures-and-Files/Day02_App_Build_Prompts.md) | `Day02_App_Build_Prompts.md` |
| [Hands-on](Day02-Functions-Data-Structures-and-Files/Day02_HandsOn_Problem_Statements.pdf) | `Day02_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day02-Functions-Data-Structures-and-Files/Day02_Workbook_Interactive.docx) | `Day02_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 01)](Day02-Functions-Data-Structures-and-Files/Day02_Quiz_on_Day01_Python_Basics.txt) | `Day02_Quiz_on_Day01_Python_Basics.txt` |

#### Day 03. OOP and Design Principles

Folder: `Day03-OOP-and-Design-Principles`

App of the day: **Mini Library Management System (OOP, command line)**

| Open | File |
| --- | --- |
| [Deck](Day03-OOP-and-Design-Principles/Day03_Deck_OOP_and_Design_Principles.pptx) | `Day03_Deck_OOP_and_Design_Principles.pptx` |
| [Pre-read](Day03-OOP-and-Design-Principles/Day03_PreRead_Blueprints_and_Good_Habits.pdf) | `Day03_PreRead_Blueprints_and_Good_Habits.pdf` |
| [Post-read](Day03-OOP-and-Design-Principles/Day03_PostRead_OOP_and_Design_Recap_and_Beyond.pdf) | `Day03_PostRead_OOP_and_Design_Recap_and_Beyond.pdf` |
| [Notebook](Day03-OOP-and-Design-Principles/Day03_OOP_and_Design_Principles_Colab.ipynb) | `Day03_OOP_and_Design_Principles_Colab.ipynb` |
| [App prompts](Day03-OOP-and-Design-Principles/Day03_App_Build_Prompts.md) | `Day03_App_Build_Prompts.md` |
| [Hands-on](Day03-OOP-and-Design-Principles/Day03_HandsOn_Problem_Statements.pdf) | `Day03_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day03-OOP-and-Design-Principles/Day03_Workbook_Interactive.docx) | `Day03_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 02)](Day03-OOP-and-Design-Principles/Day03_Quiz_on_Day02_Functions_Data_Structures_and_Files.txt) | `Day03_Quiz_on_Day02_Functions_Data_Structures_and_Files.txt` |

#### Day 04. Architecture and MongoDB

Folder: `Day04-Architecture-and-MongoDB`

App of the day: **Inventory Dashboard (Python + MongoDB + Matplotlib)**

| Open | File |
| --- | --- |
| [Deck](Day04-Architecture-and-MongoDB/Day04_Deck_Architecture_and_MongoDB.pptx) | `Day04_Deck_Architecture_and_MongoDB.pptx` |
| [Pre-read](Day04-Architecture-and-MongoDB/Day04_PreRead_How_Apps_Talk_and_Remember.pdf) | `Day04_PreRead_How_Apps_Talk_and_Remember.pdf` |
| [Post-read](Day04-Architecture-and-MongoDB/Day04_PostRead_Architecture_and_MongoDB_Recap_and_Beyond.pdf) | `Day04_PostRead_Architecture_and_MongoDB_Recap_and_Beyond.pdf` |
| [Notebook](Day04-Architecture-and-MongoDB/Day04_Architecture_and_MongoDB_Colab.ipynb) | `Day04_Architecture_and_MongoDB_Colab.ipynb` |
| [App prompts](Day04-Architecture-and-MongoDB/Day04_App_Build_Prompts.md) | `Day04_App_Build_Prompts.md` |
| [Hands-on](Day04-Architecture-and-MongoDB/Day04_HandsOn_Problem_Statements.pdf) | `Day04_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day04-Architecture-and-MongoDB/Day04_Workbook_Interactive.docx) | `Day04_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 03)](Day04-Architecture-and-MongoDB/Day04_Quiz_on_Day03_OOP_and_Design_Principles.txt) | `Day04_Quiz_on_Day03_OOP_and_Design_Principles.txt` |

### Days 05 to 08. APIs and backend with FastAPI

#### Day 05. API Fundamentals and FastAPI (assessment day)

Folder: `Day05-API-Fundamentals-and-FastAPI`

App of the day: **Quotes and Notes REST API (FastAPI, in memory)**

| Open | File |
| --- | --- |
| [Deck](Day05-API-Fundamentals-and-FastAPI/Day05_Deck_API_Fundamentals_and_FastAPI.pptx) | `Day05_Deck_API_Fundamentals_and_FastAPI.pptx` |
| [Pre-read](Day05-API-Fundamentals-and-FastAPI/Day05_PreRead_The_Web_s_Postal_Service.pdf) | `Day05_PreRead_The_Web_s_Postal_Service.pdf` |
| [Post-read](Day05-API-Fundamentals-and-FastAPI/Day05_PostRead_APIs_and_FastAPI_Recap_and_Beyond.pdf) | `Day05_PostRead_APIs_and_FastAPI_Recap_and_Beyond.pdf` |
| [Notebook](Day05-API-Fundamentals-and-FastAPI/Day05_API_Fundamentals_and_FastAPI_Colab.ipynb) | `Day05_API_Fundamentals_and_FastAPI_Colab.ipynb` |
| [App prompts](Day05-API-Fundamentals-and-FastAPI/Day05_App_Build_Prompts.md) | `Day05_App_Build_Prompts.md` |
| [Hands-on](Day05-API-Fundamentals-and-FastAPI/Day05_HandsOn_Problem_Statements.pdf) | `Day05_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day05-API-Fundamentals-and-FastAPI/Day05_Workbook_Interactive.docx) | `Day05_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 04)](Day05-API-Fundamentals-and-FastAPI/Day05_Quiz_on_Day04_Architecture_and_MongoDB.txt) | `Day05_Quiz_on_Day04_Architecture_and_MongoDB.txt` |

#### Day 06. FastAPI Core and SQLAlchemy Intro

Folder: `Day06-FastAPI-Core-and-SQLAlchemy-Intro`

App of the day: **Library Books API (FastAPI + Pydantic + SQLAlchemy + SQLite)**

| Open | File |
| --- | --- |
| [Deck](Day06-FastAPI-Core-and-SQLAlchemy-Intro/Day06_Deck_FastAPI_Core_and_SQLAlchemy_Intro.pptx) | `Day06_Deck_FastAPI_Core_and_SQLAlchemy_Intro.pptx` |
| [Pre-read](Day06-FastAPI-Core-and-SQLAlchemy-Intro/Day06_PreRead_Forms_Rules_and_Translators.pdf) | `Day06_PreRead_Forms_Rules_and_Translators.pdf` |
| [Post-read](Day06-FastAPI-Core-and-SQLAlchemy-Intro/Day06_PostRead_FastAPI_Core_and_ORM_Recap_and_Beyond.pdf) | `Day06_PostRead_FastAPI_Core_and_ORM_Recap_and_Beyond.pdf` |
| [Notebook](Day06-FastAPI-Core-and-SQLAlchemy-Intro/Day06_FastAPI_Core_and_SQLAlchemy_Intro_Colab.ipynb) | `Day06_FastAPI_Core_and_SQLAlchemy_Intro_Colab.ipynb` |
| [App prompts](Day06-FastAPI-Core-and-SQLAlchemy-Intro/Day06_App_Build_Prompts.md) | `Day06_App_Build_Prompts.md` |
| [Hands-on](Day06-FastAPI-Core-and-SQLAlchemy-Intro/Day06_HandsOn_Problem_Statements.pdf) | `Day06_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day06-FastAPI-Core-and-SQLAlchemy-Intro/Day06_Workbook_Interactive.docx) | `Day06_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 05)](Day06-FastAPI-Core-and-SQLAlchemy-Intro/Day06_Quiz_on_Day05_API_Fundamentals_and_FastAPI.txt) | `Day06_Quiz_on_Day05_API_Fundamentals_and_FastAPI.txt` |

#### Day 07. SQLAlchemy and API Docs

Folder: `Day07-SQLAlchemy-and-API-Docs`

App of the day: **Library API v2: authors, books, tags and loans**

| Open | File |
| --- | --- |
| [Deck](Day07-SQLAlchemy-and-API-Docs/Day07_Deck_SQLAlchemy_and_API_Docs.pptx) | `Day07_Deck_SQLAlchemy_and_API_Docs.pptx` |
| [Pre-read](Day07-SQLAlchemy-and-API-Docs/Day07_PreRead_Connections_Promises_and_Manuals.pdf) | `Day07_PreRead_Connections_Promises_and_Manuals.pdf` |
| [Post-read](Day07-SQLAlchemy-and-API-Docs/Day07_PostRead_Relationships_and_Docs_Recap_and_Beyond.pdf) | `Day07_PostRead_Relationships_and_Docs_Recap_and_Beyond.pdf` |
| [Notebook](Day07-SQLAlchemy-and-API-Docs/Day07_SQLAlchemy_and_API_Docs_Colab.ipynb) | `Day07_SQLAlchemy_and_API_Docs_Colab.ipynb` |
| [App prompts](Day07-SQLAlchemy-and-API-Docs/Day07_App_Build_Prompts.md) | `Day07_App_Build_Prompts.md` |
| [Hands-on](Day07-SQLAlchemy-and-API-Docs/Day07_HandsOn_Problem_Statements.pdf) | `Day07_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day07-SQLAlchemy-and-API-Docs/Day07_Workbook_Interactive.docx) | `Day07_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 06)](Day07-SQLAlchemy-and-API-Docs/Day07_Quiz_on_Day06_FastAPI_Core_and_SQLAlchemy_Intro.txt) | `Day07_Quiz_on_Day06_FastAPI_Core_and_SQLAlchemy_Intro.txt` |

#### Day 08. FastAPI Advanced and Security

Folder: `Day08-FastAPI-Advanced-and-Security`

App of the day: **Secure Notes API (FastAPI + JWT + MongoDB)**

| Open | File |
| --- | --- |
| [Deck](Day08-FastAPI-Advanced-and-Security/Day08_Deck_FastAPI_Advanced_and_Security.pptx) | `Day08_Deck_FastAPI_Advanced_and_Security.pptx` |
| [Pre-read](Day08-FastAPI-Advanced-and-Security/Day08_PreRead_Keys_Guards_and_Helpers.pdf) | `Day08_PreRead_Keys_Guards_and_Helpers.pdf` |
| [Post-read](Day08-FastAPI-Advanced-and-Security/Day08_PostRead_Advanced_FastAPI_and_Security_Recap_and_Beyond.pdf) | `Day08_PostRead_Advanced_FastAPI_and_Security_Recap_and_Beyond.pdf` |
| [Notebook](Day08-FastAPI-Advanced-and-Security/Day08_FastAPI_Advanced_and_Security_Colab.ipynb) | `Day08_FastAPI_Advanced_and_Security_Colab.ipynb` |
| [App prompts](Day08-FastAPI-Advanced-and-Security/Day08_App_Build_Prompts.md) | `Day08_App_Build_Prompts.md` |
| [Hands-on](Day08-FastAPI-Advanced-and-Security/Day08_HandsOn_Problem_Statements.pdf) | `Day08_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day08-FastAPI-Advanced-and-Security/Day08_Workbook_Interactive.docx) | `Day08_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 07)](Day08-FastAPI-Advanced-and-Security/Day08_Quiz_on_Day07_SQLAlchemy_and_API_Docs.txt) | `Day08_Quiz_on_Day07_SQLAlchemy_and_API_Docs.txt` |

### Days 09 to 10. JavaScript and Node.js

#### Day 09. FastAPI MongoDB and JavaScript Basics

Folder: `Day09-FastAPI-MongoDB-and-JavaScript-Basics`

App of the day: **Shop Analytics API (FastAPI + MongoDB) with a JavaScript data script**

| Open | File |
| --- | --- |
| [Deck](Day09-FastAPI-MongoDB-and-JavaScript-Basics/Day09_Deck_FastAPI_MongoDB_and_JavaScript_Basics.pptx) | `Day09_Deck_FastAPI_MongoDB_and_JavaScript_Basics.pptx` |
| [Pre-read](Day09-FastAPI-MongoDB-and-JavaScript-Basics/Day09_PreRead_Big_Lists_and_a_New_Language.pdf) | `Day09_PreRead_Big_Lists_and_a_New_Language.pdf` |
| [Post-read](Day09-FastAPI-MongoDB-and-JavaScript-Basics/Day09_PostRead_Mongo_APIs_and_JavaScript_Recap_and_Beyond.pdf) | `Day09_PostRead_Mongo_APIs_and_JavaScript_Recap_and_Beyond.pdf` |
| [Notebook](Day09-FastAPI-MongoDB-and-JavaScript-Basics/Day09_FastAPI_MongoDB_and_JavaScript_Basics_Colab.ipynb) | `Day09_FastAPI_MongoDB_and_JavaScript_Basics_Colab.ipynb` |
| [App prompts](Day09-FastAPI-MongoDB-and-JavaScript-Basics/Day09_App_Build_Prompts.md) | `Day09_App_Build_Prompts.md` |
| [Hands-on](Day09-FastAPI-MongoDB-and-JavaScript-Basics/Day09_HandsOn_Problem_Statements.pdf) | `Day09_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day09-FastAPI-MongoDB-and-JavaScript-Basics/Day09_Workbook_Interactive.docx) | `Day09_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 08)](Day09-FastAPI-MongoDB-and-JavaScript-Basics/Day09_Quiz_on_Day08_FastAPI_Advanced_and_Security.txt) | `Day09_Quiz_on_Day08_FastAPI_Advanced_and_Security.txt` |

#### Day 10. Async JavaScript and Node js

Folder: `Day10-Async-JavaScript-and-Node-js`

App of the day: **Tasks API in Express with an async client and Postman tests**

| Open | File |
| --- | --- |
| [Deck](Day10-Async-JavaScript-and-Node-js/Day10_Deck_Async_JavaScript_and_Node_js.pptx) | `Day10_Deck_Async_JavaScript_and_Node_js.pptx` |
| [Pre-read](Day10-Async-JavaScript-and-Node-js/Day10_PreRead_Never_Wait_Around.pdf) | `Day10_PreRead_Never_Wait_Around.pdf` |
| [Post-read](Day10-Async-JavaScript-and-Node-js/Day10_PostRead_Async_JavaScript_and_Express_Recap_and_Beyond.pdf) | `Day10_PostRead_Async_JavaScript_and_Express_Recap_and_Beyond.pdf` |
| [Notebook](Day10-Async-JavaScript-and-Node-js/Day10_Async_JavaScript_and_Node_js_Colab.ipynb) | `Day10_Async_JavaScript_and_Node_js_Colab.ipynb` |
| [App prompts](Day10-Async-JavaScript-and-Node-js/Day10_App_Build_Prompts.md) | `Day10_App_Build_Prompts.md` |
| [Hands-on](Day10-Async-JavaScript-and-Node-js/Day10_HandsOn_Problem_Statements.pdf) | `Day10_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day10-Async-JavaScript-and-Node-js/Day10_Workbook_Interactive.docx) | `Day10_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 09)](Day10-Async-JavaScript-and-Node-js/Day10_Quiz_on_Day09_FastAPI_MongoDB_and_JavaScript_Basics.txt) | `Day10_Quiz_on_Day09_FastAPI_MongoDB_and_JavaScript_Basics.txt` |

### Days 11 to 12. React and full stack

#### Day 11. React Basics (assessment day)

Folder: `Day11-React-Basics`

App of the day: **Personal Dashboard (React components, props, state and events)**

| Open | File |
| --- | --- |
| [Deck](Day11-React-Basics/Day11_Deck_React_Basics.pptx) | `Day11_Deck_React_Basics.pptx` |
| [Pre-read](Day11-React-Basics/Day11_PreRead_Building_Screens_from_Blocks.pdf) | `Day11_PreRead_Building_Screens_from_Blocks.pdf` |
| [Post-read](Day11-React-Basics/Day11_PostRead_React_Basics_Recap_and_Beyond.pdf) | `Day11_PostRead_React_Basics_Recap_and_Beyond.pdf` |
| [Notebook](Day11-React-Basics/Day11_React_Basics_Colab.ipynb) | `Day11_React_Basics_Colab.ipynb` |
| [App prompts](Day11-React-Basics/Day11_App_Build_Prompts.md) | `Day11_App_Build_Prompts.md` |
| [Hands-on](Day11-React-Basics/Day11_HandsOn_Problem_Statements.pdf) | `Day11_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day11-React-Basics/Day11_Workbook_Interactive.docx) | `Day11_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 10)](Day11-React-Basics/Day11_Quiz_on_Day10_Async_JavaScript_and_Node_js.txt) | `Day11_Quiz_on_Day10_Async_JavaScript_and_Node_js.txt` |

#### Day 12. React UI Logic and API Integration

Folder: `Day12-React-UI-Logic-and-API-Integration`

App of the day: **Full Stack Task Board (React + FastAPI)**

| Open | File |
| --- | --- |
| [Deck](Day12-React-UI-Logic-and-API-Integration/Day12_Deck_React_UI_Logic_and_API_Integration.pptx) | `Day12_Deck_React_UI_Logic_and_API_Integration.pptx` |
| [Pre-read](Day12-React-UI-Logic-and-API-Integration/Day12_PreRead_Showing_the_Right_Thing.pdf) | `Day12_PreRead_Showing_the_Right_Thing.pdf` |
| [Post-read](Day12-React-UI-Logic-and-API-Integration/Day12_PostRead_React_and_APIs_Recap_and_Beyond.pdf) | `Day12_PostRead_React_and_APIs_Recap_and_Beyond.pdf` |
| [Notebook](Day12-React-UI-Logic-and-API-Integration/Day12_React_UI_Logic_and_API_Integration_Colab.ipynb) | `Day12_React_UI_Logic_and_API_Integration_Colab.ipynb` |
| [App prompts](Day12-React-UI-Logic-and-API-Integration/Day12_App_Build_Prompts.md) | `Day12_App_Build_Prompts.md` |
| [Hands-on](Day12-React-UI-Logic-and-API-Integration/Day12_HandsOn_Problem_Statements.pdf) | `Day12_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day12-React-UI-Logic-and-API-Integration/Day12_Workbook_Interactive.docx) | `Day12_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 11)](Day12-React-UI-Logic-and-API-Integration/Day12_Quiz_on_Day11_React_Basics.txt) | `Day12_Quiz_on_Day11_React_Basics.txt` |

### Days 13 to 14. Testing and data engineering

#### Day 13. Testing and Data Engineering Intro

Folder: `Day13-Testing-and-Data-Engineering-Intro`

App of the day: **Tested Order Ingestion Service (pandas ETL + FastAPI + PyTest)**

| Open | File |
| --- | --- |
| [Deck](Day13-Testing-and-Data-Engineering-Intro/Day13_Deck_Testing_and_Data_Engineering_Intro.pptx) | `Day13_Deck_Testing_and_Data_Engineering_Intro.pptx` |
| [Pre-read](Day13-Testing-and-Data-Engineering-Intro/Day13_PreRead_Checking_Your_Work_and_Moving_Data.pdf) | `Day13_PreRead_Checking_Your_Work_and_Moving_Data.pdf` |
| [Post-read](Day13-Testing-and-Data-Engineering-Intro/Day13_PostRead_Testing_and_Data_Engineering_Recap_and_Beyond.pdf) | `Day13_PostRead_Testing_and_Data_Engineering_Recap_and_Beyond.pdf` |
| [Notebook](Day13-Testing-and-Data-Engineering-Intro/Day13_Testing_and_Data_Engineering_Intro_Colab.ipynb) | `Day13_Testing_and_Data_Engineering_Intro_Colab.ipynb` |
| [App prompts](Day13-Testing-and-Data-Engineering-Intro/Day13_App_Build_Prompts.md) | `Day13_App_Build_Prompts.md` |
| [Hands-on](Day13-Testing-and-Data-Engineering-Intro/Day13_HandsOn_Problem_Statements.pdf) | `Day13_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day13-Testing-and-Data-Engineering-Intro/Day13_Workbook_Interactive.docx) | `Day13_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 12)](Day13-Testing-and-Data-Engineering-Intro/Day13_Quiz_on_Day12_React_UI_Logic_and_API_Integration.txt) | `Day13_Quiz_on_Day12_React_UI_Logic_and_API_Integration.txt` |

#### Day 14. Data Pipelines and Spark Intro

Folder: `Day14-Data-Pipelines-and-Spark-Intro`

App of the day: **Retail Sales Batch Pipeline (PySpark, medallion layers)**

| Open | File |
| --- | --- |
| [Deck](Day14-Data-Pipelines-and-Spark-Intro/Day14_Deck_Data_Pipelines_and_Spark_Intro.pptx) | `Day14_Deck_Data_Pipelines_and_Spark_Intro.pptx` |
| [Pre-read](Day14-Data-Pipelines-and-Spark-Intro/Day14_PreRead_When_Data_Gets_Big.pdf) | `Day14_PreRead_When_Data_Gets_Big.pdf` |
| [Post-read](Day14-Data-Pipelines-and-Spark-Intro/Day14_PostRead_Spark_and_Pipelines_Recap_and_Beyond.pdf) | `Day14_PostRead_Spark_and_Pipelines_Recap_and_Beyond.pdf` |
| [Notebook](Day14-Data-Pipelines-and-Spark-Intro/Day14_Data_Pipelines_and_Spark_Intro_Colab.ipynb) | `Day14_Data_Pipelines_and_Spark_Intro_Colab.ipynb` |
| [App prompts](Day14-Data-Pipelines-and-Spark-Intro/Day14_App_Build_Prompts.md) | `Day14_App_Build_Prompts.md` |
| [Hands-on](Day14-Data-Pipelines-and-Spark-Intro/Day14_HandsOn_Problem_Statements.pdf) | `Day14_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day14-Data-Pipelines-and-Spark-Intro/Day14_Workbook_Interactive.docx) | `Day14_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 13)](Day14-Data-Pipelines-and-Spark-Intro/Day14_Quiz_on_Day13_Testing_and_Data_Engineering_Intro.txt) | `Day14_Quiz_on_Day13_Testing_and_Data_Engineering_Intro.txt` |

### Day 15. FDE Professional Skills 1 (full day on professional skills)

Folder: `Day15-FDE-Professional-Skills-1`

App of the day: **FDE Field Notebook (FastAPI + React)**

| Open | File |
| --- | --- |
| [Deck](Day15-FDE-Professional-Skills-1/Day15_Deck_FDE_Professional_Skills_1.pptx) | `Day15_Deck_FDE_Professional_Skills_1.pptx` |
| [Pre-read](Day15-FDE-Professional-Skills-1/Day15_PreRead_The_Engineer_Who_Goes_to_the_Problem.pdf) | `Day15_PreRead_The_Engineer_Who_Goes_to_the_Problem.pdf` |
| [Post-read](Day15-FDE-Professional-Skills-1/Day15_PostRead_FDE_Identity_and_Action_Recap_and_Beyond.pdf) | `Day15_PostRead_FDE_Identity_and_Action_Recap_and_Beyond.pdf` |
| [Notebook](Day15-FDE-Professional-Skills-1/Day15_FDE_Professional_Skills_1_Colab.ipynb) | `Day15_FDE_Professional_Skills_1_Colab.ipynb` |
| [App prompts](Day15-FDE-Professional-Skills-1/Day15_App_Build_Prompts.md) | `Day15_App_Build_Prompts.md` |
| [Hands-on (simulation and role play cards)](Day15-FDE-Professional-Skills-1/Day15_HandsOn_Problem_Statements.pdf) | `Day15_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day15-FDE-Professional-Skills-1/Day15_Workbook_Interactive.docx) | `Day15_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 14)](Day15-FDE-Professional-Skills-1/Day15_Quiz_on_Day14_Data_Pipelines_and_Spark_Intro.txt) | `Day15_Quiz_on_Day14_Data_Pipelines_and_Spark_Intro.txt` |

### Day 16. PySpark Batch Pipelines and SQL

Folder: `Day16-PySpark-Batch-Pipelines-and-SQL`

App of the day: **Sales Insights Pipeline with a SQL Question Bank (PySpark + Spark SQL + FastAPI)**

| Open | File |
| --- | --- |
| [Deck](Day16-PySpark-Batch-Pipelines-and-SQL/Day16_Deck_PySpark_Batch_Pipelines_and_SQL.pptx) | `Day16_Deck_PySpark_Batch_Pipelines_and_SQL.pptx` |
| [Pre-read](Day16-PySpark-Batch-Pipelines-and-SQL/Day16_PreRead_Asking_Data_Good_Questions.pdf) | `Day16_PreRead_Asking_Data_Good_Questions.pdf` |
| [Post-read](Day16-PySpark-Batch-Pipelines-and-SQL/Day16_PostRead_Pipelines_and_SQL_Recap_and_Beyond.pdf) | `Day16_PostRead_Pipelines_and_SQL_Recap_and_Beyond.pdf` |
| [Notebook](Day16-PySpark-Batch-Pipelines-and-SQL/Day16_PySpark_Batch_Pipelines_and_SQL_Colab.ipynb) | `Day16_PySpark_Batch_Pipelines_and_SQL_Colab.ipynb` |
| [App prompts](Day16-PySpark-Batch-Pipelines-and-SQL/Day16_App_Build_Prompts.md) | `Day16_App_Build_Prompts.md` |
| [Hands-on](Day16-PySpark-Batch-Pipelines-and-SQL/Day16_HandsOn_Problem_Statements.pdf) | `Day16_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day16-PySpark-Batch-Pipelines-and-SQL/Day16_Workbook_Interactive.docx) | `Day16_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 15)](Day16-PySpark-Batch-Pipelines-and-SQL/Day16_Quiz_on_Day15_FDE_Professional_Skills_1.txt) | `Day16_Quiz_on_Day15_FDE_Professional_Skills_1.txt` |

### Days 17 to 19. DevOps, containers and Azure

#### Day 17. DevOps and Cloud Fundamentals (assessment day)

Folder: `Day17-DevOps-and-Cloud-Fundamentals`

App of the day: **DevOps-ready FastAPI Service (tests, lint, pipeline YAML)**

| Open | File |
| --- | --- |
| [Deck](Day17-DevOps-and-Cloud-Fundamentals/Day17_Deck_DevOps_and_Cloud_Fundamentals.pptx) | `Day17_Deck_DevOps_and_Cloud_Fundamentals.pptx` |
| [Pre-read](Day17-DevOps-and-Cloud-Fundamentals/Day17_PreRead_From_My_Laptop_to_the_World.pdf) | `Day17_PreRead_From_My_Laptop_to_the_World.pdf` |
| [Post-read](Day17-DevOps-and-Cloud-Fundamentals/Day17_PostRead_DevOps_and_Cloud_Recap_and_Beyond.pdf) | `Day17_PostRead_DevOps_and_Cloud_Recap_and_Beyond.pdf` |
| [Notebook](Day17-DevOps-and-Cloud-Fundamentals/Day17_DevOps_and_Cloud_Fundamentals_Colab.ipynb) | `Day17_DevOps_and_Cloud_Fundamentals_Colab.ipynb` |
| [App prompts](Day17-DevOps-and-Cloud-Fundamentals/Day17_App_Build_Prompts.md) | `Day17_App_Build_Prompts.md` |
| [Hands-on](Day17-DevOps-and-Cloud-Fundamentals/Day17_HandsOn_Problem_Statements.pdf) | `Day17_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day17-DevOps-and-Cloud-Fundamentals/Day17_Workbook_Interactive.docx) | `Day17_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 16)](Day17-DevOps-and-Cloud-Fundamentals/Day17_Quiz_on_Day16_PySpark_Batch_Pipelines_and_SQL.txt) | `Day17_Quiz_on_Day16_PySpark_Batch_Pipelines_and_SQL.txt` |

#### Day 18. Git CI CD and Docker

Folder: `Day18-Git-CI-CD-and-Docker`

App of the day: **Containerised Task API with Git workflow and multi-stage pipeline**

| Open | File |
| --- | --- |
| [Deck](Day18-Git-CI-CD-and-Docker/Day18_Deck_Git_CI_CD_and_Docker.pptx) | `Day18_Deck_Git_CI_CD_and_Docker.pptx` |
| [Pre-read](Day18-Git-CI-CD-and-Docker/Day18_PreRead_Saving_Versions_and_Packing_Boxes.pdf) | `Day18_PreRead_Saving_Versions_and_Packing_Boxes.pdf` |
| [Post-read](Day18-Git-CI-CD-and-Docker/Day18_PostRead_Git_Pipelines_and_Docker_Recap_and_Beyond.pdf) | `Day18_PostRead_Git_Pipelines_and_Docker_Recap_and_Beyond.pdf` |
| [Notebook](Day18-Git-CI-CD-and-Docker/Day18_Git_CI_CD_and_Docker_Colab.ipynb) | `Day18_Git_CI_CD_and_Docker_Colab.ipynb` |
| [App prompts](Day18-Git-CI-CD-and-Docker/Day18_App_Build_Prompts.md) | `Day18_App_Build_Prompts.md` |
| [Hands-on](Day18-Git-CI-CD-and-Docker/Day18_HandsOn_Problem_Statements.pdf) | `Day18_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day18-Git-CI-CD-and-Docker/Day18_Workbook_Interactive.docx) | `Day18_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 17)](Day18-Git-CI-CD-and-Docker/Day18_Quiz_on_Day17_DevOps_and_Cloud_Fundamentals.txt) | `Day18_Quiz_on_Day17_DevOps_and_Cloud_Fundamentals.txt` |

#### Day 19. Containers and Azure Deployment

Folder: `Day19-Containers-and-Azure-Deployment`

App of the day: **Deploy the Full Stack Task Board to Azure (Containers + CD)**

| Open | File |
| --- | --- |
| [Deck](Day19-Containers-and-Azure-Deployment/Day19_Deck_Containers_and_Azure_Deployment.pptx) | `Day19_Deck_Containers_and_Azure_Deployment.pptx` |
| [Pre-read](Day19-Containers-and-Azure-Deployment/Day19_PreRead_Opening_Day_for_Your_App.pdf) | `Day19_PreRead_Opening_Day_for_Your_App.pdf` |
| [Post-read](Day19-Containers-and-Azure-Deployment/Day19_PostRead_Deploying_to_Azure_Recap_and_Beyond.pdf) | `Day19_PostRead_Deploying_to_Azure_Recap_and_Beyond.pdf` |
| [Notebook](Day19-Containers-and-Azure-Deployment/Day19_Containers_and_Azure_Deployment_Colab.ipynb) | `Day19_Containers_and_Azure_Deployment_Colab.ipynb` |
| [App prompts](Day19-Containers-and-Azure-Deployment/Day19_App_Build_Prompts.md) | `Day19_App_Build_Prompts.md` |
| [Hands-on](Day19-Containers-and-Azure-Deployment/Day19_HandsOn_Problem_Statements.pdf) | `Day19_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day19-Containers-and-Azure-Deployment/Day19_Workbook_Interactive.docx) | `Day19_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 18)](Day19-Containers-and-Azure-Deployment/Day19_Quiz_on_Day18_Git_CI_CD_and_Docker.txt) | `Day19_Quiz_on_Day18_Git_CI_CD_and_Docker.txt` |

### Day 20. FDE Professional Skills 2 (full day on professional skills)

Folder: `Day20-FDE-Professional-Skills-2`

App of the day: **Request Log Investigator (FastAPI + React mini tool)**

| Open | File |
| --- | --- |
| [Deck](Day20-FDE-Professional-Skills-2/Day20_Deck_FDE_Professional_Skills_2.pptx) | `Day20_Deck_FDE_Professional_Skills_2.pptx` |
| [Pre-read](Day20-FDE-Professional-Skills-2/Day20_PreRead_When_Nobody_Knows_Exactly_What_Is_Wrong.pdf) | `Day20_PreRead_When_Nobody_Knows_Exactly_What_Is_Wrong.pdf` |
| [Post-read](Day20-FDE-Professional-Skills-2/Day20_PostRead_Ambiguity_and_Embedded_Problem_Solving_Recap_and_Beyond.pdf) | `Day20_PostRead_Ambiguity_and_Embedded_Problem_Solving_Recap_and_Beyond.pdf` |
| [Notebook](Day20-FDE-Professional-Skills-2/Day20_FDE_Professional_Skills_2_Colab.ipynb) | `Day20_FDE_Professional_Skills_2_Colab.ipynb` |
| [App prompts](Day20-FDE-Professional-Skills-2/Day20_App_Build_Prompts.md) | `Day20_App_Build_Prompts.md` |
| [Hands-on (simulation and role play cards)](Day20-FDE-Professional-Skills-2/Day20_HandsOn_Problem_Statements.pdf) | `Day20_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day20-FDE-Professional-Skills-2/Day20_Workbook_Interactive.docx) | `Day20_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 19)](Day20-FDE-Professional-Skills-2/Day20_Quiz_on_Day19_Containers_and_Azure_Deployment.txt) | `Day20_Quiz_on_Day19_Containers_and_Azure_Deployment.txt` |

### Days 21 to 23. GenAI, prompting and RAG

#### Day 21. GenAI Intro and Prompt Engineering (assessment day)

Folder: `Day21-GenAI-Intro-and-Prompt-Engineering`

App of the day: **Prompt Playground (FastAPI + React) with prompt templates**

| Open | File |
| --- | --- |
| [Deck](Day21-GenAI-Intro-and-Prompt-Engineering/Day21_Deck_GenAI_Intro_and_Prompt_Engineering.pptx) | `Day21_Deck_GenAI_Intro_and_Prompt_Engineering.pptx` |
| [Pre-read](Day21-GenAI-Intro-and-Prompt-Engineering/Day21_PreRead_How_AI_Writes.pdf) | `Day21_PreRead_How_AI_Writes.pdf` |
| [Post-read](Day21-GenAI-Intro-and-Prompt-Engineering/Day21_PostRead_GenAI_and_Prompting_Recap_and_Beyond.pdf) | `Day21_PostRead_GenAI_and_Prompting_Recap_and_Beyond.pdf` |
| [Notebook](Day21-GenAI-Intro-and-Prompt-Engineering/Day21_GenAI_Intro_and_Prompt_Engineering_Colab.ipynb) | `Day21_GenAI_Intro_and_Prompt_Engineering_Colab.ipynb` |
| [App prompts](Day21-GenAI-Intro-and-Prompt-Engineering/Day21_App_Build_Prompts.md) | `Day21_App_Build_Prompts.md` |
| [Hands-on](Day21-GenAI-Intro-and-Prompt-Engineering/Day21_HandsOn_Problem_Statements.pdf) | `Day21_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day21-GenAI-Intro-and-Prompt-Engineering/Day21_Workbook_Interactive.docx) | `Day21_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 20)](Day21-GenAI-Intro-and-Prompt-Engineering/Day21_Quiz_on_Day20_FDE_Professional_Skills_2.txt) | `Day21_Quiz_on_Day20_FDE_Professional_Skills_2.txt` |

#### Day 22. Context Engineering and RAG (senior FDE session, feedback discussion)

Folder: `Day22-Context-Engineering-and-RAG`

App of the day: **Policy Q&A Assistant v1 (RAG with chunking and citations)**

| Open | File |
| --- | --- |
| [Deck](Day22-Context-Engineering-and-RAG/Day22_Deck_Context_Engineering_and_RAG.pptx) | `Day22_Deck_Context_Engineering_and_RAG.pptx` |
| [Pre-read](Day22-Context-Engineering-and-RAG/Day22_PreRead_Giving_AI_the_Right_Information.pdf) | `Day22_PreRead_Giving_AI_the_Right_Information.pdf` |
| [Post-read](Day22-Context-Engineering-and-RAG/Day22_PostRead_Context_and_RAG_Recap_and_Beyond.pdf) | `Day22_PostRead_Context_and_RAG_Recap_and_Beyond.pdf` |
| [Notebook](Day22-Context-Engineering-and-RAG/Day22_Context_Engineering_and_RAG_Colab.ipynb) | `Day22_Context_Engineering_and_RAG_Colab.ipynb` |
| [App prompts](Day22-Context-Engineering-and-RAG/Day22_App_Build_Prompts.md) | `Day22_App_Build_Prompts.md` |
| [Hands-on](Day22-Context-Engineering-and-RAG/Day22_HandsOn_Problem_Statements.pdf) | `Day22_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day22-Context-Engineering-and-RAG/Day22_Workbook_Interactive.docx) | `Day22_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 21)](Day22-Context-Engineering-and-RAG/Day22_Quiz_on_Day21_GenAI_Intro_and_Prompt_Engineering.txt) | `Day22_Quiz_on_Day21_GenAI_Intro_and_Prompt_Engineering.txt` |

#### Day 23. RAG Embeddings and Vector DBs

Folder: `Day23-RAG-Embeddings-and-Vector-DBs`

App of the day: **Policy Q&A Assistant v2 (hybrid search, re-ranking, citations)**

| Open | File |
| --- | --- |
| [Deck](Day23-RAG-Embeddings-and-Vector-DBs/Day23_Deck_RAG_Embeddings_and_Vector_DBs.pptx) | `Day23_Deck_RAG_Embeddings_and_Vector_DBs.pptx` |
| [Pre-read](Day23-RAG-Embeddings-and-Vector-DBs/Day23_PreRead_Searching_by_Meaning.pdf) | `Day23_PreRead_Searching_by_Meaning.pdf` |
| [Post-read](Day23-RAG-Embeddings-and-Vector-DBs/Day23_PostRead_Embeddings_and_Retrieval_Recap_and_Beyond.pdf) | `Day23_PostRead_Embeddings_and_Retrieval_Recap_and_Beyond.pdf` |
| [Notebook](Day23-RAG-Embeddings-and-Vector-DBs/Day23_RAG_Embeddings_and_Vector_DBs_Colab.ipynb) | `Day23_RAG_Embeddings_and_Vector_DBs_Colab.ipynb` |
| [App prompts](Day23-RAG-Embeddings-and-Vector-DBs/Day23_App_Build_Prompts.md) | `Day23_App_Build_Prompts.md` |
| [Hands-on](Day23-RAG-Embeddings-and-Vector-DBs/Day23_HandsOn_Problem_Statements.pdf) | `Day23_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day23-RAG-Embeddings-and-Vector-DBs/Day23_Workbook_Interactive.docx) | `Day23_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 22)](Day23-RAG-Embeddings-and-Vector-DBs/Day23_Quiz_on_Day22_Context_Engineering_and_RAG.txt) | `Day23_Quiz_on_Day22_Context_Engineering_and_RAG.txt` |

### Days 24 to 25. LLM orchestration and FDE skills 3

#### Day 24. FDE Skills 3a and LLM Orchestration

Folder: `Day24-FDE-Skills-3a-and-LLM-Orchestration`

App of the day: **Meeting Notes Assistant (LangChain chains + FastAPI)**

| Open | File |
| --- | --- |
| [Deck](Day24-FDE-Skills-3a-and-LLM-Orchestration/Day24_Deck_FDE_Skills_3a_and_LLM_Orchestration.pptx) | `Day24_Deck_FDE_Skills_3a_and_LLM_Orchestration.pptx` |
| [Pre-read](Day24-FDE-Skills-3a-and-LLM-Orchestration/Day24_PreRead_Persuading_People_Orchestrating_Models.pdf) | `Day24_PreRead_Persuading_People_Orchestrating_Models.pdf` |
| [Post-read](Day24-FDE-Skills-3a-and-LLM-Orchestration/Day24_PostRead_Influence_and_Orchestration_Recap_and_Beyond.pdf) | `Day24_PostRead_Influence_and_Orchestration_Recap_and_Beyond.pdf` |
| [Notebook](Day24-FDE-Skills-3a-and-LLM-Orchestration/Day24_FDE_Skills_3a_and_LLM_Orchestration_Colab.ipynb) | `Day24_FDE_Skills_3a_and_LLM_Orchestration_Colab.ipynb` |
| [App prompts](Day24-FDE-Skills-3a-and-LLM-Orchestration/Day24_App_Build_Prompts.md) | `Day24_App_Build_Prompts.md` |
| [Hands-on](Day24-FDE-Skills-3a-and-LLM-Orchestration/Day24_HandsOn_Problem_Statements.pdf) | `Day24_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day24-FDE-Skills-3a-and-LLM-Orchestration/Day24_Workbook_Interactive.docx) | `Day24_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 23)](Day24-FDE-Skills-3a-and-LLM-Orchestration/Day24_Quiz_on_Day23_RAG_Embeddings_and_Vector_DBs.txt) | `Day24_Quiz_on_Day23_RAG_Embeddings_and_Vector_DBs.txt` |

#### Day 25. LLM Orchestration and FDE Skills 3b (one-on-one feedback)

Folder: `Day25-LLM-Orchestration-and-FDE-Skills-3b`

App of the day: **Customer Support Copilot (tool calling + LangGraph)**

| Open | File |
| --- | --- |
| [Deck](Day25-LLM-Orchestration-and-FDE-Skills-3b/Day25_Deck_LLM_Orchestration_and_FDE_Skills_3b.pptx) | `Day25_Deck_LLM_Orchestration_and_FDE_Skills_3b.pptx` |
| [Pre-read](Day25-LLM-Orchestration-and-FDE-Skills-3b/Day25_PreRead_Tools_Flows_and_Loops.pdf) | `Day25_PreRead_Tools_Flows_and_Loops.pdf` |
| [Post-read](Day25-LLM-Orchestration-and-FDE-Skills-3b/Day25_PostRead_Tools_Graphs_and_Systems_Recap_and_Beyond.pdf) | `Day25_PostRead_Tools_Graphs_and_Systems_Recap_and_Beyond.pdf` |
| [Notebook](Day25-LLM-Orchestration-and-FDE-Skills-3b/Day25_LLM_Orchestration_and_FDE_Skills_3b_Colab.ipynb) | `Day25_LLM_Orchestration_and_FDE_Skills_3b_Colab.ipynb` |
| [App prompts](Day25-LLM-Orchestration-and-FDE-Skills-3b/Day25_App_Build_Prompts.md) | `Day25_App_Build_Prompts.md` |
| [Hands-on](Day25-LLM-Orchestration-and-FDE-Skills-3b/Day25_HandsOn_Problem_Statements.pdf) | `Day25_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day25-LLM-Orchestration-and-FDE-Skills-3b/Day25_Workbook_Interactive.docx) | `Day25_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 24)](Day25-LLM-Orchestration-and-FDE-Skills-3b/Day25_Quiz_on_Day24_FDE_Skills_3a_and_LLM_Orchestration.txt) | `Day25_Quiz_on_Day24_FDE_Skills_3a_and_LLM_Orchestration.txt` |

### Days 26 to 27. Agentic AI and agent protocols

#### Day 26. Agentic AI and Agentic RAG (assessment day)

Folder: `Day26-Agentic-AI-and-Agentic-RAG`

App of the day: **Agentic HR and Ops Assistant (CRAG + supervisor agents)**

| Open | File |
| --- | --- |
| [Deck](Day26-Agentic-AI-and-Agentic-RAG/Day26_Deck_Agentic_AI_and_Agentic_RAG.pptx) | `Day26_Deck_Agentic_AI_and_Agentic_RAG.pptx` |
| [Pre-read](Day26-Agentic-AI-and-Agentic-RAG/Day26_PreRead_AI_That_Works_Towards_a_Goal.pdf) | `Day26_PreRead_AI_That_Works_Towards_a_Goal.pdf` |
| [Post-read](Day26-Agentic-AI-and-Agentic-RAG/Day26_PostRead_Agents_and_Agentic_RAG_Recap_and_Beyond.pdf) | `Day26_PostRead_Agents_and_Agentic_RAG_Recap_and_Beyond.pdf` |
| [Notebook](Day26-Agentic-AI-and-Agentic-RAG/Day26_Agentic_AI_and_Agentic_RAG_Colab.ipynb) | `Day26_Agentic_AI_and_Agentic_RAG_Colab.ipynb` |
| [App prompts](Day26-Agentic-AI-and-Agentic-RAG/Day26_App_Build_Prompts.md) | `Day26_App_Build_Prompts.md` |
| [Hands-on](Day26-Agentic-AI-and-Agentic-RAG/Day26_HandsOn_Problem_Statements.pdf) | `Day26_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day26-Agentic-AI-and-Agentic-RAG/Day26_Workbook_Interactive.docx) | `Day26_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 25)](Day26-Agentic-AI-and-Agentic-RAG/Day26_Quiz_on_Day25_LLM_Orchestration_and_FDE_Skills_3b.txt) | `Day26_Quiz_on_Day25_LLM_Orchestration_and_FDE_Skills_3b.txt` |

#### Day 27. Agent Protocols and Advanced Use Cases (senior FDE session, FDE assessment debrief)

Folder: `Day27-Agent-Protocols-and-Advanced-Use-Cases`

App of the day: **Enterprise Agent Hub (MCP servers + A2A-style agents + data agent)**

| Open | File |
| --- | --- |
| [Deck](Day27-Agent-Protocols-and-Advanced-Use-Cases/Day27_Deck_Agent_Protocols_and_Advanced_Use_Cases.pptx) | `Day27_Deck_Agent_Protocols_and_Advanced_Use_Cases.pptx` |
| [Pre-read](Day27-Agent-Protocols-and-Advanced-Use-Cases/Day27_PreRead_Common_Languages_for_AI.pdf) | `Day27_PreRead_Common_Languages_for_AI.pdf` |
| [Post-read](Day27-Agent-Protocols-and-Advanced-Use-Cases/Day27_PostRead_Protocols_and_Advanced_Agents_Recap_and_Beyond.pdf) | `Day27_PostRead_Protocols_and_Advanced_Agents_Recap_and_Beyond.pdf` |
| [Notebook](Day27-Agent-Protocols-and-Advanced-Use-Cases/Day27_Agent_Protocols_and_Advanced_Use_Cases_Colab.ipynb) | `Day27_Agent_Protocols_and_Advanced_Use_Cases_Colab.ipynb` |
| [App prompts](Day27-Agent-Protocols-and-Advanced-Use-Cases/Day27_App_Build_Prompts.md) | `Day27_App_Build_Prompts.md` |
| [Hands-on](Day27-Agent-Protocols-and-Advanced-Use-Cases/Day27_HandsOn_Problem_Statements.pdf) | `Day27_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day27-Agent-Protocols-and-Advanced-Use-Cases/Day27_Workbook_Interactive.docx) | `Day27_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 26)](Day27-Agent-Protocols-and-Advanced-Use-Cases/Day27_Quiz_on_Day26_Agentic_AI_and_Agentic_RAG.txt) | `Day27_Quiz_on_Day26_Agentic_AI_and_Agentic_RAG.txt` |

### Days 28 to 30. LLM security, evaluation and QA

#### Day 28. LLM Security and Guardrails

Folder: `Day28-LLM-Security-and-Guardrails`

App of the day: **Guardrail Gateway for LLM Apps (FastAPI middleware + red-team suite)**

| Open | File |
| --- | --- |
| [Deck](Day28-LLM-Security-and-Guardrails/Day28_Deck_LLM_Security_and_Guardrails.pptx) | `Day28_Deck_LLM_Security_and_Guardrails.pptx` |
| [Pre-read](Day28-LLM-Security-and-Guardrails/Day28_PreRead_Keeping_AI_Safe_and_Trustworthy.pdf) | `Day28_PreRead_Keeping_AI_Safe_and_Trustworthy.pdf` |
| [Post-read](Day28-LLM-Security-and-Guardrails/Day28_PostRead_Security_and_Guardrails_Recap_and_Beyond.pdf) | `Day28_PostRead_Security_and_Guardrails_Recap_and_Beyond.pdf` |
| [Notebook](Day28-LLM-Security-and-Guardrails/Day28_LLM_Security_and_Guardrails_Colab.ipynb) | `Day28_LLM_Security_and_Guardrails_Colab.ipynb` |
| [App prompts](Day28-LLM-Security-and-Guardrails/Day28_App_Build_Prompts.md) | `Day28_App_Build_Prompts.md` |
| [Hands-on](Day28-LLM-Security-and-Guardrails/Day28_HandsOn_Problem_Statements.pdf) | `Day28_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day28-LLM-Security-and-Guardrails/Day28_Workbook_Interactive.docx) | `Day28_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 27)](Day28-LLM-Security-and-Guardrails/Day28_Quiz_on_Day27_Agent_Protocols_and_Advanced_Use_Cases.txt) | `Day28_Quiz_on_Day27_Agent_Protocols_and_Advanced_Use_Cases.txt` |

#### Day 29. GenAI System Evaluation

Folder: `Day29-GenAI-System-Evaluation`

App of the day: **RAG Evaluation Dashboard (metrics, error analysis, slices)**

| Open | File |
| --- | --- |
| [Deck](Day29-GenAI-System-Evaluation/Day29_Deck_GenAI_System_Evaluation.pptx) | `Day29_Deck_GenAI_System_Evaluation.pptx` |
| [Pre-read](Day29-GenAI-System-Evaluation/Day29_PreRead_How_Good_Is_Our_AI_Really.pdf) | `Day29_PreRead_How_Good_Is_Our_AI_Really.pdf` |
| [Post-read](Day29-GenAI-System-Evaluation/Day29_PostRead_Evaluating_GenAI_Systems_Recap_and_Beyond.pdf) | `Day29_PostRead_Evaluating_GenAI_Systems_Recap_and_Beyond.pdf` |
| [Notebook](Day29-GenAI-System-Evaluation/Day29_GenAI_System_Evaluation_Colab.ipynb) | `Day29_GenAI_System_Evaluation_Colab.ipynb` |
| [App prompts](Day29-GenAI-System-Evaluation/Day29_App_Build_Prompts.md) | `Day29_App_Build_Prompts.md` |
| [Hands-on](Day29-GenAI-System-Evaluation/Day29_HandsOn_Problem_Statements.pdf) | `Day29_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day29-GenAI-System-Evaluation/Day29_Workbook_Interactive.docx) | `Day29_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 28)](Day29-GenAI-System-Evaluation/Day29_Quiz_on_Day28_LLM_Security_and_Guardrails.txt) | `Day29_Quiz_on_Day28_LLM_Security_and_Guardrails.txt` |

#### Day 30. LLM Evaluation and QA (one-on-one feedback)

Folder: `Day30-LLM-Evaluation-and-QA`

App of the day: **LLM Quality Gate for CI (golden sets + regression tests + reports)**

| Open | File |
| --- | --- |
| [Deck](Day30-LLM-Evaluation-and-QA/Day30_Deck_LLM_Evaluation_and_QA.pptx) | `Day30_Deck_LLM_Evaluation_and_QA.pptx` |
| [Pre-read](Day30-LLM-Evaluation-and-QA/Day30_PreRead_Quality_Checks_Before_Every_Release.pdf) | `Day30_PreRead_Quality_Checks_Before_Every_Release.pdf` |
| [Post-read](Day30-LLM-Evaluation-and-QA/Day30_PostRead_LLM_Evaluation_and_QA_Recap_and_Beyond.pdf) | `Day30_PostRead_LLM_Evaluation_and_QA_Recap_and_Beyond.pdf` |
| [Notebook](Day30-LLM-Evaluation-and-QA/Day30_LLM_Evaluation_and_QA_Colab.ipynb) | `Day30_LLM_Evaluation_and_QA_Colab.ipynb` |
| [App prompts](Day30-LLM-Evaluation-and-QA/Day30_App_Build_Prompts.md) | `Day30_App_Build_Prompts.md` |
| [Hands-on](Day30-LLM-Evaluation-and-QA/Day30_HandsOn_Problem_Statements.pdf) | `Day30_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day30-LLM-Evaluation-and-QA/Day30_Workbook_Interactive.docx) | `Day30_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 29)](Day30-LLM-Evaluation-and-QA/Day30_Quiz_on_Day29_GenAI_System_Evaluation.txt) | `Day30_Quiz_on_Day29_GenAI_System_Evaluation.txt` |

### Days 31 to 35. LLMOps, deployment and monitoring

#### Day 31. LLMOps Intro and FDE Skills 4

Folder: `Day31-LLMOps-Intro-and-FDE-Skills-4`

App of the day: **Resilient LLM Client and Incident Toolkit**

| Open | File |
| --- | --- |
| [Deck](Day31-LLMOps-Intro-and-FDE-Skills-4/Day31_Deck_LLMOps_Intro_and_FDE_Skills_4.pptx) | `Day31_Deck_LLMOps_Intro_and_FDE_Skills_4.pptx` |
| [Pre-read](Day31-LLMOps-Intro-and-FDE-Skills-4/Day31_PreRead_Keeping_AI_Running_Day_After_Day.pdf) | `Day31_PreRead_Keeping_AI_Running_Day_After_Day.pdf` |
| [Post-read](Day31-LLMOps-Intro-and-FDE-Skills-4/Day31_PostRead_LLMOps_and_Escalations_Recap_and_Beyond.pdf) | `Day31_PostRead_LLMOps_and_Escalations_Recap_and_Beyond.pdf` |
| [Notebook](Day31-LLMOps-Intro-and-FDE-Skills-4/Day31_LLMOps_Intro_and_FDE_Skills_4_Colab.ipynb) | `Day31_LLMOps_Intro_and_FDE_Skills_4_Colab.ipynb` |
| [App prompts](Day31-LLMOps-Intro-and-FDE-Skills-4/Day31_App_Build_Prompts.md) | `Day31_App_Build_Prompts.md` |
| [Hands-on](Day31-LLMOps-Intro-and-FDE-Skills-4/Day31_HandsOn_Problem_Statements.pdf) | `Day31_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day31-LLMOps-Intro-and-FDE-Skills-4/Day31_Workbook_Interactive.docx) | `Day31_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 30)](Day31-LLMOps-Intro-and-FDE-Skills-4/Day31_Quiz_on_Day30_LLM_Evaluation_and_QA.txt) | `Day31_Quiz_on_Day30_LLM_Evaluation_and_QA.txt` |

#### Day 32. LLMOps (assessment day, 1.5 hours)

Folder: `Day32-LLMOps`

App of the day: **LLM Cost and Version Control Center**

| Open | File |
| --- | --- |
| [Deck](Day32-LLMOps/Day32_Deck_LLMOps.pptx) | `Day32_Deck_LLMOps.pptx` |
| [Pre-read](Day32-LLMOps/Day32_PreRead_Running_AI_Like_a_Product.pdf) | `Day32_PreRead_Running_AI_Like_a_Product.pdf` |
| [Post-read](Day32-LLMOps/Day32_PostRead_LLMOps_Recap_and_Beyond.pdf) | `Day32_PostRead_LLMOps_Recap_and_Beyond.pdf` |
| [Notebook](Day32-LLMOps/Day32_LLMOps_Colab.ipynb) | `Day32_LLMOps_Colab.ipynb` |
| [App prompts](Day32-LLMOps/Day32_App_Build_Prompts.md) | `Day32_App_Build_Prompts.md` |
| [Hands-on](Day32-LLMOps/Day32_HandsOn_Problem_Statements.pdf) | `Day32_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day32-LLMOps/Day32_Workbook_Interactive.docx) | `Day32_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 31)](Day32-LLMOps/Day32_Quiz_on_Day31_LLMOps_Intro_and_FDE_Skills_4.txt) | `Day32_Quiz_on_Day31_LLMOps_Intro_and_FDE_Skills_4.txt` |

#### Day 33. LLM Deployment and Lifecycle

Folder: `Day33-LLM-Deployment-and-Lifecycle`

App of the day: **Production LLM Gateway (FastAPI, async, streaming, canary)**

| Open | File |
| --- | --- |
| [Deck](Day33-LLM-Deployment-and-Lifecycle/Day33_Deck_LLM_Deployment_and_Lifecycle.pptx) | `Day33_Deck_LLM_Deployment_and_Lifecycle.pptx` |
| [Pre-read](Day33-LLM-Deployment-and-Lifecycle/Day33_PreRead_From_Prototype_to_Production_Service.pdf) | `Day33_PreRead_From_Prototype_to_Production_Service.pdf` |
| [Post-read](Day33-LLM-Deployment-and-Lifecycle/Day33_PostRead_LLM_Deployment_Recap_and_Beyond.pdf) | `Day33_PostRead_LLM_Deployment_Recap_and_Beyond.pdf` |
| [Notebook](Day33-LLM-Deployment-and-Lifecycle/Day33_LLM_Deployment_and_Lifecycle_Colab.ipynb) | `Day33_LLM_Deployment_and_Lifecycle_Colab.ipynb` |
| [App prompts](Day33-LLM-Deployment-and-Lifecycle/Day33_App_Build_Prompts.md) | `Day33_App_Build_Prompts.md` |
| [Hands-on](Day33-LLM-Deployment-and-Lifecycle/Day33_HandsOn_Problem_Statements.pdf) | `Day33_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day33-LLM-Deployment-and-Lifecycle/Day33_Workbook_Interactive.docx) | `Day33_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 32)](Day33-LLM-Deployment-and-Lifecycle/Day33_Quiz_on_Day32_LLMOps.txt) | `Day33_Quiz_on_Day32_LLMOps.txt` |

#### Day 34. Observability and Monitoring

Folder: `Day34-Observability-and-Monitoring`

App of the day: **LLM Observability Starter Kit (logs, traces, dashboard, feedback)**

| Open | File |
| --- | --- |
| [Deck](Day34-Observability-and-Monitoring/Day34_Deck_Observability_and_Monitoring.pptx) | `Day34_Deck_Observability_and_Monitoring.pptx` |
| [Pre-read](Day34-Observability-and-Monitoring/Day34_PreRead_Watching_AI_While_It_Works.pdf) | `Day34_PreRead_Watching_AI_While_It_Works.pdf` |
| [Post-read](Day34-Observability-and-Monitoring/Day34_PostRead_Observability_Recap_and_Beyond.pdf) | `Day34_PostRead_Observability_Recap_and_Beyond.pdf` |
| [Notebook](Day34-Observability-and-Monitoring/Day34_Observability_and_Monitoring_Colab.ipynb) | `Day34_Observability_and_Monitoring_Colab.ipynb` |
| [App prompts](Day34-Observability-and-Monitoring/Day34_App_Build_Prompts.md) | `Day34_App_Build_Prompts.md` |
| [Hands-on](Day34-Observability-and-Monitoring/Day34_HandsOn_Problem_Statements.pdf) | `Day34_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day34-Observability-and-Monitoring/Day34_Workbook_Interactive.docx) | `Day34_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 33)](Day34-Observability-and-Monitoring/Day34_Quiz_on_Day33_LLM_Deployment_and_Lifecycle.txt) | `Day34_Quiz_on_Day33_LLM_Deployment_and_Lifecycle.txt` |

#### Day 35. Drift Detection and Optimization

Folder: `Day35-Drift-Detection-and-Optimization`

App of the day: **Drift Watch: automated drift and quality monitoring**

| Open | File |
| --- | --- |
| [Deck](Day35-Drift-Detection-and-Optimization/Day35_Deck_Drift_Detection_and_Optimization.pptx) | `Day35_Deck_Drift_Detection_and_Optimization.pptx` |
| [Pre-read](Day35-Drift-Detection-and-Optimization/Day35_PreRead_When_the_World_Moves_On.pdf) | `Day35_PreRead_When_the_World_Moves_On.pdf` |
| [Post-read](Day35-Drift-Detection-and-Optimization/Day35_PostRead_Drift_and_Optimisation_Recap_and_Beyond.pdf) | `Day35_PostRead_Drift_and_Optimisation_Recap_and_Beyond.pdf` |
| [Notebook](Day35-Drift-Detection-and-Optimization/Day35_Drift_Detection_and_Optimization_Colab.ipynb) | `Day35_Drift_Detection_and_Optimization_Colab.ipynb` |
| [App prompts](Day35-Drift-Detection-and-Optimization/Day35_App_Build_Prompts.md) | `Day35_App_Build_Prompts.md` |
| [Hands-on](Day35-Drift-Detection-and-Optimization/Day35_HandsOn_Problem_Statements.pdf) | `Day35_HandsOn_Problem_Statements.pdf` |
| [Workbook](Day35-Drift-Detection-and-Optimization/Day35_Workbook_Interactive.docx) | `Day35_Workbook_Interactive.docx` |
| [Quiz (15 questions on Day 34)](Day35-Drift-Detection-and-Optimization/Day35_Quiz_on_Day34_Observability_and_Monitoring.txt) | `Day35_Quiz_on_Day34_Observability_and_Monitoring.txt` |

## 9. Using the quiz files

Each `DayNN_Quiz_on_DayMM_*.txt` holds 15 questions as CSV rows, ready to paste into your quiz tool. The filename tells you which day it tests, so `Day09_Quiz_on_Day08_FastAPI_Advanced_and_Security.txt` runs at the start of Day 09 and tests Day 08. The last quiz, on Day 35, sits in the capstone folder and runs at the start of Day 36.

## 10. Using the app build prompts

For Days 01 to 35, each day builds one app, and the prompts are written so learners only use concepts taught up to that point.

1. Copy one prompt at a time into an AI coding assistant.
2. Run the generated code in Colab or VS Code.
3. Read every line. Use the explain prompt when something is unclear.
4. Do not move to the next prompt until the current version runs without errors.

Each file ends with stretch ideas for learners who finish early. The capstone prompts work the same way, but run one per working session across Days 36 to 39.

## 11. Suggested preparation for each session

| When | Do this |
| --- | --- |
| Before class | Send the pre-read. Review the deck and run the notebook end to end |
| Session open | Run the quiz from that day's folder, which covers the previous day |
| Session body | Present the deck, demo from the notebook |
| Lab time | Hand out the hands-on problems and the app build prompts |
| After class | Send the post-read and the workbook |

## 12. Quick answers

| I want to | Go to |
| --- | --- |
| See the whole program | Section 4 |
| Find a day by subject | The folder name, or the blocks in section 5 |
| Know which days are assessments | Section 3 |
| Open one day's files | Section 8 |
| Set up a notebook | Section 6 |
| Run a GenAI day without an API key | Section 6, offline demo mode |
| Plan the capstone week | Section 7 |
| Score a capstone team | Section 7, rubric and the evaluator scoring sheet |
| Import a quiz | Section 9 |
| Understand the app builds | Section 10 |
| Plan a session | Section 11 |

## 13. Source notes

The notes that shipped with each source batch are kept unchanged:

- [SOURCE_NOTE_Days_01_to_10.md](SOURCE_NOTE_Days_01_to_10.md)
- [SOURCE_NOTE_Days_11_to_20.md](SOURCE_NOTE_Days_11_to_20.md)
- [SOURCE_NOTE_Days_21_to_30.md](SOURCE_NOTE_Days_21_to_30.md)
- [SOURCE_NOTE_Days_31_to_40.md](SOURCE_NOTE_Days_31_to_40.md)
