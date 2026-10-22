"""Generate the root README.md from the program table and the files in each day folder.

Usage: python tools/build/extras/readme.py
Re-run after adding or renaming day files so the day-by-day index stays correct.
"""
import glob
import os
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))

# day, date, week, track, topic, folder, action, app of the day, notes
PROGRAM = [
    (1, "Mon 26 Oct", 1, "FDE Mindset", "Onboarding + FDE Mindset Session 1", "Day01-Onboarding-and-FDE-Mindset-1", "Placeholder + onboarding", "", ""),
    (2, "Tue 27 Oct", 1, "Basics", "Python Basics + Functions, Data Structures and Files", "Day02-Python-Basics-Functions-and-Files", "Merge", "Smart Study Planner + Personal Expense Tracker", ""),
    (3, "Wed 28 Oct", 1, "Basics", "OOP + OpenAI Codex Walkthrough (half day)", "Day03-OOP-and-OpenAI-Codex-Walkthrough", "Condense + new", "Mini Library Management System", "Codex half day"),
    (4, "Thu 29 Oct", 1, "Basics", "Architecture and MongoDB", "Day04-Architecture-and-MongoDB", "Reuse + update", "Inventory Dashboard", ""),
    (5, "Fri 30 Oct", 1, "Basics", "API Fundamentals and FastAPI Core", "Day05-API-Fundamentals-and-FastAPI-Core", "Merge", "Quotes and Notes REST API", "Assessment"),
    (6, "Mon 02 Nov", 2, "Basics", "SQLAlchemy, Relationships and API Docs", "Day06-SQLAlchemy-and-API-Docs", "Merge", "Library Books API + Library API v2", ""),
    (7, "Tue 03 Nov", 2, "Basics", "FastAPI Advanced, Security and MongoDB", "Day07-FastAPI-Advanced-Security-and-MongoDB", "Merge", "Secure Notes API", "Vulnerability report v1"),
    (8, "Wed 04 Nov", 2, "Basics", "JavaScript Fundamentals and Async JavaScript", "Day08-JavaScript-and-Async-JavaScript", "Merge", "JavaScript data script for the ticket API", ""),
    (9, "Thu 05 Nov", 2, "Basics", "Node.js and Express", "Day09-Nodejs-and-Express", "Reuse + update", "Tasks API in Express", ""),
    (10, "Fri 06 Nov", 2, "Basics", "React Basics", "Day10-React-Basics", "Reuse + update", "Personal Dashboard", "Assessment"),
    (None, "Mon 09 Nov", 3, "Holiday", "Deepavali", "", "", "", ""),
    (11, "Tue 10 Nov", 3, "Basics", "React UI Logic and Full-Stack Integration", "Day11-React-UI-Logic-and-Full-Stack", "Reuse + update", "Full Stack Task Board", ""),
    (12, "Wed 11 Nov", 3, "GenAI", "GenAI 1: Introduction to GenAI, LLMs and Tokens", "Day12-GenAI-Intro-LLMs-and-Tokens", "Split + expand", "SmartDesk ticket summariser with token log", ""),
    (13, "Thu 12 Nov", 3, "GenAI", "GenAI 2: Prompt Engineering", "Day13-Prompt-Engineering", "Split + expand", "Prompt Playground", "Assessment"),
    (14, "Fri 13 Nov", 3, "FDE Mindset", "FDE Mindset Session 2", "Day14-FDE-Mindset-2", "Placeholder", "", ""),
    (15, "Mon 16 Nov", 4, "Basics", "Testing and Data Engineering Intro", "Day15-Testing-and-Data-Engineering-Intro", "Reuse + update", "Tested Order Ingestion Service", ""),
    (16, "Tue 17 Nov", 4, "Basics", "Data Pipelines, Spark and PySpark", "Day16-Data-Pipelines-Spark-and-PySpark", "Merge", "Retail Sales Batch Pipeline + Sales Insights Pipeline", ""),
    (17, "Wed 18 Nov", 4, "Basics", "DevOps and Cloud Fundamentals", "Day17-DevOps-and-Cloud-Fundamentals", "Reuse + update", "DevOps-ready FastAPI Service", "Assessment"),
    (18, "Thu 19 Nov", 4, "GenAI", "GenAI 3: Context Engineering and RAG Foundations", "Day18-Context-Engineering-and-RAG", "Reuse + update", "Policy Q&A Assistant v1", ""),
    (19, "Fri 20 Nov", 4, "FDE Mindset", "FDE Mindset Session 3", "Day19-FDE-Mindset-3", "Placeholder", "", ""),
    (20, "Mon 23 Nov", 5, "Basics", "Git, CI/CD and Docker", "Day20-Git-CI-CD-and-Docker", "Merge", "Containerised Task API", "Vulnerability report v2"),
    (21, "Tue 24 Nov", 5, "Basics", "Azure Deployment and Continuous Delivery", "Day21-Azure-Deployment-and-CD", "Reuse + update", "Deploy the Full Stack Task Board to Azure", ""),
    (22, "Wed 25 Nov", 5, "GenAI", "GenAI 4: Embeddings, Vector DBs and the RAG Application", "Day22-Embeddings-Vector-DBs-and-RAG-App", "Reuse + update", "Policy Q&A Assistant v2", "Senior FDE interaction"),
    (23, "Thu 26 Nov", 5, "GenAI", "GenAI 5: Industry Use Cases + Security for the Agentic World (SME)", "Day23-Industry-Use-Cases-and-Agentic-Security-SME", "New", "Patch and Modernise assignment", "SME session"),
    (24, "Fri 27 Nov", 5, "FDE Mindset", "FDE Mindset Session 4", "Day24-FDE-Mindset-4", "Placeholder", "", ""),
    (25, "Mon 30 Nov", 6, "GenAI", "GenAI 6: Small Language Models + Token Cost and Optimisation", "Day25-SLMs-and-Token-Optimisation", "New", "SLM vs LLM comparison + cost report", ""),
    (26, "Tue 01 Dec", 6, "GenAI", "GenAI 7: LLM Orchestration, Tool Calling and LangGraph", "Day26-LLM-Orchestration-Tools-and-LangGraph", "Merge", "Customer Support Assistant", "1:1 feedback"),
    (27, "Wed 02 Dec", 6, "GenAI", "GenAI 8: Agentic AI and Agentic RAG", "Day27-Agentic-AI-Agentic-RAG-and-Memory", "Reuse + update", "Agentic HR and Ops Assistant", "Assessment"),
    (28, "Thu 03 Dec", 6, "GenAI", "GenAI 9: Agent Protocols (MCP, A2A) and Advanced Agents", "Day28-Agent-Protocols-MCP-and-A2A", "Reuse + update", "Enterprise Agent Hub", "Senior FDE interaction"),
    (29, "Fri 04 Dec", 6, "FDE Mindset", "FDE Mindset Session 5", "Day29-FDE-Mindset-5", "Placeholder", "", ""),
    (30, "Mon 07 Dec", 7, "GenAI", "GenAI 10: LLM Security and Guardrails", "Day30-LLM-Security-and-Guardrails", "Reuse + update", "Guardrail Gateway", "Vulnerability report v3"),
    (31, "Tue 08 Dec", 7, "GenAI", "GenAI 11: GenAI System Evaluation", "Day31-GenAI-System-Evaluation", "Reuse + update", "RAG Evaluation Dashboard", ""),
    (32, "Wed 09 Dec", 7, "GenAI", "GenAI 12: LLM Evaluation and Quality Gates", "Day32-LLM-Evaluation-and-Quality-Gates", "Reuse + update", "LLM Quality Gate for CI", "1:1 feedback"),
    (33, "Thu 10 Dec", 7, "GenAI", "GenAI 13: LLMOps", "Day33-LLMOps", "Merge", "Resilient LLM Client + LLM Cost and Version Control Center", "Assessment"),
    (34, "Fri 11 Dec", 7, "GenAI", "GenAI 14: LLM Deployment and Lifecycle", "Day34-LLM-Deployment-and-Lifecycle", "Reuse + update", "Production LLM Gateway", ""),
    (35, "Mon 14 Dec", 8, "GenAI", "GenAI 15: Observability, Drift and Optimisation", "Day35-Observability-Drift-and-Optimisation", "Merge", "LLM Observability Starter Kit + Drift Watch", ""),
    ("36 to 40", "Tue 15 to Mon 21 Dec", "8 to 9", "Capstone", "Capstone project", "Day36-40-Capstone", "Update", "Six projects incl. Project 06 LegacyLift", "Demo day 21 Dec"),
]

KINDS = [("Deck", "_Deck_"), ("Pre-read", "_PreRead_"), ("Post-read", "_PostRead_"), ("Notebook", "_Colab.ipynb"),
         ("App prompts", "_App_Build_Prompts"), ("Hands-on", "_HandsOn_"), ("Workbook", "_Workbook_"),
         ("Quiz", "_Quiz_on_"), ("Hotel lab", "_Hotel_Lab")]


def link(path, label):
    return f"[{label}]({quote(path)})"


def day_files(folder):
    files = sorted(os.path.basename(f) for f in glob.glob(os.path.join(ROOT, folder, "*")) if os.path.isfile(f))
    out = []
    for label, key in KINDS:
        for f in files:
            if key in f:
                out.append(link(f"{folder}/{f}", label if label != "Notebook" or "Token_Cost" not in f
                                else "Cost calculator notebook"))
    extras = [f for f in files if not any(k in f for _, k in KINDS) and f not in ("README.md",)]
    out += [link(f"{folder}/{f}", f) for f in extras]
    return out


HEAD = """# Forward Deployed Engineer Program (v4)

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
"""

BLOCKS = """
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
"""

TAIL = """
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
"""


def main():
    md = [HEAD, "\n## 4. Program at a glance\n",
          "| Day | Date (2026) | Week | Track | Topic | App of the day | Notes |",
          "| --- | --- | --- | --- | --- | --- | --- |"]
    for day, date, week, track, topic, folder, action, app, notes in PROGRAM:
        label = f"{day:02d}" if isinstance(day, int) else (day or "Holiday")
        d = link(folder, label) if folder else label
        md.append(f"| {d} | {date} | {week} | {track} | {topic} | {app} | {notes} |")
    md.append(BLOCKS)
    md.append("## 9. Day by day index\n")
    for day, date, week, track, topic, folder, action, app, notes in PROGRAM:
        if not folder:
            md.append(f"### {date} 2026. Holiday: {topic}\n")
            continue
        label = f"Day {day:02d}" if isinstance(day, int) else f"Days {day}"
        extra = f" ({notes})" if notes else ""
        md.append(f"### {label}. {topic}{extra}\n")
        md.append(f"{date} 2026 | Week {week} | {track} | v4 action: {action}\n")
        if track == "FDE Mindset":
            files = [link(f"{folder}/README.md", "README (placeholder)")]
            if day == 1:
                files += [link(f"{folder}/{f}", f) for f in sorted(os.listdir(os.path.join(ROOT, folder)))
                          if f != "README.md"]
        elif folder == "Day36-40-Capstone":
            files = [link(f"{folder}/README.md", "Capstone README")]
        else:
            files = day_files(folder)
        md.append(" | ".join(files) + "\n")
    md.append(TAIL)
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print("README.md written")


if __name__ == "__main__":
    main()
