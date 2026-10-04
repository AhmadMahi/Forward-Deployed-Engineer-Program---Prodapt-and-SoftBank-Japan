# Forward Deployed Engineer Program

Course materials for **Prodapt** and **SoftBank Japan**.

Prepared by Ahmed. Days 01 to 30 are published here. Later days will be added as they are delivered.

This file is the navigation guide. Pick a day from the index, open what you need.

---

## 1. Current status

| Item | Status |
| --- | --- |
| Days 01 to 30 | Published, full material |
| `Day31-Opening-Quiz-Only` | Holds the quiz on Day 30 only, ready for the start of Day 31 |
| Day 31 onward | Not yet published |

When the next batch arrives, drop the new day folders in at the root. The `Day31-Opening-Quiz-Only` folder already holds that day's opening quiz, so the new Day 31 content merges into it and the folder is renamed to carry its topic.

## 2. How folders are named

Every folder is `DayNN-Topic`, so you can find a session by subject without opening anything.

```text
Day09-FastAPI-MongoDB-and-JavaScript-Basics
Day23-RAG-Embeddings-and-Vector-DBs
```

Files inside keep their original `DayNN_` prefix, so a file still tells you its day when it is moved or attached on its own.

## 3. The eight files in every day folder

Learn these eight names once and you can navigate any day.

| File pattern | Type | What it is | When to use it |
| --- | --- | --- | --- |
| `DayNN_Deck_*.pptx` | Slides | The session deck | Present in class |
| `DayNN_PreRead_*.pdf` | PDF | A short, non-technical read | Send before class |
| `DayNN_PostRead_*.pdf` | PDF | Recap of the day plus topics that go further | Send after class |
| `DayNN_*_Colab.ipynb` | Notebook | Live demos. Option A cells run in Colab, Option B cells (commented) are for VS Code | Demo during the session |
| `DayNN_App_Build_Prompts.md` | Markdown | Prompts for building the day's app with an AI coding assistant | Give to learners for the build |
| `DayNN_HandsOn_Problem_Statements.pdf` | PDF | Practice problems, warm-up through to stretch | Lab time and homework |
| `DayNN_Workbook_Interactive.docx` | Word | Fill in the blanks, short answers, predict the output, write code. Works in Word, Google Docs or printed | Reinforcement |
| `DayNN_Quiz_on_DayMM_*.txt` | CSV in a .txt | 15 questions on the **previous** day, as CSV rows ready to paste into the quiz tool | Open the session |

### Three things to watch

1. **Quizzes look backwards.** The quiz in Day 05 tests Day 04. That is why Day 01 has no quiz and why there is a `Day31-Opening-Quiz-Only` folder holding nothing but the quiz on Day 30.
2. **Days 15 and 20 differ.** These are full days on professional skills. The hands-on PDF holds simulation and role play cards instead of coding problems, and the workbook uses writing practice instead of code boxes.
3. **Days 21 onward are GenAI.** These notebooks need an LLM API key, or they fall back to an offline demo mode. See section 7.

## 4. Session types

| Tag | Days | Meaning |
| --- | --- | --- |
| `assessment day` | 05, 11, 17, 21, 26 | A formal assessment runs in the session |
| `full day` | 15, 20 | Full day on FDE professional skills, role play rather than coding |
| `senior FDE session` | 22, 27 | Senior FDE joins. Day 22 is a feedback discussion, Day 27 is the FDE assessment debrief |
| `1:1 feedback` | 25, 30 | One-on-one feedback runs alongside the session |

## 5. Program at a glance

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
| [31](Day31-Opening-Quiz-Only) | Not yet published | - | Day 30 |

## 6. The program in blocks

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

## 7. Running the notebooks

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

### Days 21 to 30, GenAI

- **With an API key:** in Colab open Secrets (the key icon), add `OPENAI_API_KEY` and allow notebook access. In VS Code set the environment variable or use a `.env` file. Set `LLM_MODEL` to a current chat model you have access to. The notebooks default to `gpt-4o-mini`.
- **Without a key:** every cell still runs in offline demo mode using a small, clearly labelled stand-in model. Offline scores show how the code works, not how real models perform. Say this to the room before you demo, so nobody quotes an offline score as a real benchmark.

| Day | What you need |
| --- | --- |
| 27 (MCP) | The notebook pins the MCP Python SDK below version 2, because v2 renamed some APIs |
| 28 (security) | All attacks target a simulated bot |

> **Day 28 caution.** Only test systems you own or are authorised to test.

> **Azure caution (Days 18 and 19).** Only use subscriptions you have permission to use, and delete test resource groups once you are done.

## 8. Day by day index

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

### Day 31. Opening quiz only

Folder: `Day31-Opening-Quiz-Only`

| Open | File |
| --- | --- |
| [Quiz (15 questions on Day 30)](Day31-Opening-Quiz-Only/Day31_Quiz_on_Day30_LLM_Evaluation_and_QA.txt) | `Day31_Quiz_on_Day30_LLM_Evaluation_and_QA.txt` |

## 9. Using the quiz files

Each `DayNN_Quiz_on_DayMM_*.txt` holds 15 questions as CSV rows, ready to paste into your quiz tool. The filename tells you which day it tests, so `Day09_Quiz_on_Day08_FastAPI_Advanced_and_Security.txt` runs at the start of Day 09 and tests Day 08.

## 10. Using the app build prompts

Each day builds one app, and the prompts are written so learners only use concepts taught up to that point.

1. Copy one prompt at a time into an AI coding assistant.
2. Run the generated code in Colab or VS Code.
3. Read every line. Use the explain prompt when something is unclear.
4. Do not move to the next prompt until the current version runs without errors.

Each file ends with stretch ideas for learners who finish early.

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
| See the whole program | Section 5 |
| Find a day by subject | The folder name, or the blocks in section 6 |
| Know which days are assessments | Section 4 |
| Open one day's files | Section 8 |
| Set up a notebook | Section 7 |
| Run a GenAI day without an API key | Section 7, offline demo mode |
| Import a quiz | Section 9 |
| Understand the app builds | Section 10 |
| Plan a session | Section 11 |
| Know what is still to come | Section 1 |

## 13. Source notes

The notes that shipped with each source batch are kept unchanged:

- [SOURCE_NOTE_Days_01_to_10.md](SOURCE_NOTE_Days_01_to_10.md)
- [SOURCE_NOTE_Days_11_to_20.md](SOURCE_NOTE_Days_11_to_20.md)
- [SOURCE_NOTE_Days_21_to_30.md](SOURCE_NOTE_Days_21_to_30.md)
