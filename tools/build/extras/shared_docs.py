"""Build the shared PDFs and the Day 1 onboarding deck.

Usage: python tools/build/extras/shared_docs.py
Outputs:
    shared/Laptop_Setup_Guide.pdf
    shared/Codex_Setup_and_Dos_Donts.pdf
    Day01-Onboarding-and-FDE-Mindset-1/Day01_Deck_Program_Walkthrough.pptx
"""
import os
import sys
from types import SimpleNamespace

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.dirname(HERE))
import fde_render as R  # noqa: E402


def pdf(path, kicker, title, lede, sections, footer):
    st = R._pdf_styles()
    flow = []
    R._header(flow, st, kicker, title, lede)
    R._render_blocks(flow, sections, st)
    R._doc(path, footer, footer, flow)


LAPTOP = [
    dict(h="Before Day 1", paras=[
        "Install every **Required** item below on the laptop you will use in class, then run the check command. "
        "Bring the laptop to the Day 1 onboarding session, where the software check is done together. "
        "If you cannot install something because of company policy, tell your trainer before Day 1."],
        box="**Golden rule:** never paste an API key into a file you commit, a notebook cell, a prompt or a chat."),
    dict(h="1. Browser and Google account (Day 1 and Day 2)", bullets=[
        "Install a current Chrome or Edge.",
        "Sign in to a Google account and open https://colab.research.google.com to check Colab loads.",
        "Colab runs every notebook in this program, including the free GPU runtime on Day 25."],
        code="Check: open Colab, create a notebook, run  print('hello')"),
    dict(h="2. Python 3.12 or newer (Day 2)", bullets=[
        "Windows: install from python.org and tick 'Add python.exe to PATH'.",
        "macOS: install from python.org or with Homebrew (brew install python@3.12).",
        "Create a virtual environment for each project (Day 3 covers this)."],
        code="python --version          # Windows\npython3 --version         # macOS / Linux\n"
             "python -m pip --version"),
    dict(h="3. VS Code and the OpenAI Codex extension (Day 3)", bullets=[
        "Install VS Code from code.visualstudio.com.",
        "Add the Python and Jupyter extensions (published by Microsoft).",
        "Add the OpenAI Codex extension (published by OpenAI). You sign in with the program's API key in class "
        "on Day 3. Use approved models only.",
        "Full set-up steps: docs/CODEX_GUIDE.md in the course repository."],
        code="code --version"),
    dict(h="4. Git and a GitHub account (Day 3)", bullets=[
        "Install Git from git-scm.com (macOS: xcode-select --install also works).",
        "Create or use a GitHub account; you need it for Codex and the capstone repository."],
        code='git --version\ngit config --global user.name "Your Name"\n'
             'git config --global user.email "you@example.com"'),
    dict(h="5. Node.js LTS with npm (Day 8)", bullets=[
        "Install the current LTS release from nodejs.org.", "npm comes with Node.js."],
        code="node --version\nnpm --version"),
    dict(h="6. Postman (Day 9)", bullets=["Install the Postman desktop app and sign in or skip sign-in."],
         code="Check: send GET https://httpbin.org/get and see status 200"),
    dict(h="7. Docker Desktop (Day 20)", bullets=[
        "Install Docker Desktop and start it once.",
        "Larger companies need a paid Docker subscription. Check licensing with your IT team.",
        "Windows: enable WSL 2 when the installer asks."],
        code="docker --version\ndocker run --rm hello-world"),
    dict(h="8. Optional items", bullets=[
        "MongoDB Compass (Day 4): visual tool for MongoDB. Colab uses mongomock, so this is optional.",
        "Java 17 (Day 16): only to run PySpark on your laptop. Not needed in Colab.",
        "Hugging Face account (Day 25): some small models need a free account to download."]),
    dict(h="9. Python packages", paras=[
        "Each day installs its own packages in class (for example openai, pytest, pyspark, langchain, langgraph, mcp, "
        "transformers). In VS Code, install them inside a virtual environment:"],
        code="python -m venv .venv\n# Windows: .venv\\Scripts\\activate   macOS/Linux: source .venv/bin/activate\n"
             "pip install -r requirements.txt"),
    dict(h="10. Adding OPENAI_API_KEY", sub="In Google Colab", bullets=[
        "Click the key icon (Secrets) in the left sidebar.",
        "Add a secret named exactly OPENAI_API_KEY and paste the key as its value.",
        "Switch on 'Notebook access'. Notebooks read it with google.colab.userdata."]),
    dict(sub="In VS Code (.env file)", bullets=[
        "Create a file named .env at the project root containing one line: OPENAI_API_KEY=your-key-here",
        "Add .env to .gitignore before your first commit.",
        "Load it with python-dotenv, or set the variable in your terminal."],
        code="# .gitignore\n.env\n\n# check it is ignored\ngit check-ignore .env      # prints .env if ignored"),
    dict(h="Day 1 software check", table=[
        ["Item", "Check command or action", "Done"],
        ["Browser + Colab", "Run print('hello') in Colab", ""],
        ["Python 3.12+", "python --version", ""],
        ["VS Code + extensions", "code --version; Python, Jupyter, OpenAI Codex installed", ""],
        ["Git", "git --version", ""],
        ["Node.js LTS", "node --version; npm --version", ""],
        ["Postman", "GET request returns 200", ""],
        ["Docker Desktop", "docker run --rm hello-world", ""],
    ], after=["No API keys are needed for Days 1 and 2. Keys are issued in class."]),
]

CODEX = [
    dict(h="What OpenAI Codex is", paras=[
        "OpenAI Codex is an AI coding agent. In VS Code it can explain code, plan a change, edit files, run commands "
        "and tests, and show you every diff for review. You stay responsible for every line you accept."]),
    dict(h="Set up in five steps", bullets=[
        "Install the OpenAI Codex extension (published by OpenAI) in VS Code.",
        "Open the Codex panel and sign in with the program's OpenAI API key. Paste the key only into the sign-in prompt.",
        "Choose the approved default model (docs/MODEL_GUIDE.md).",
        "Set the sandbox to workspace-write with approvals; use read-only to explore.",
        "Add an AGENTS.md to your repository from shared/templates/AGENTS_learner_template.md."]),
    dict(h="The structured workflow", table=[
        ["Step", "You", "Codex"],
        ["Describe", "Goal, files involved, how to check it works", "Asks questions if unclear"],
        ["Plan", "Ask for a plan; approve or edit it", "Proposes small steps"],
        ["Small steps", "Approve one step at a time", "Edits a few files per step"],
        ["Test", "Run tests after every step", "Writes tests first if asked"],
        ["Review", "Read every diff; accept only what you can explain", "Explains any line"],
    ]),
    dict(h="Which model for what", table=[
        ["Task", "Model", "Effort"],
        ["Explain code, small edits, docstrings", "Light model (for example GPT-6 Luna, if approved)", "Low"],
        ["Most feature work", "Default: GPT-6.1 Sol", "Medium"],
        ["Hard debugging, large migrations", "GPT-6.1 Sol high effort; GPT-6 Astra with trainer approval", "High"],
        ["Security review and patches", "Default, with human verification", "Medium"],
        ["Retired models such as GPT-5.5", "Do not use", "n/a"],
    ], after=["Names checked 21 Oct 2026. Confirm against the approved model list."]),
    dict(h="Do", bullets=[
        "Plan first for multi-step work; approve the plan, then let Codex build in small steps.",
        "Keep tasks small and include only the relevant files to save tokens.",
        "Write or generate tests first; run them after every change.",
        "Read every diff; accept only code you can explain.",
        "Keep AGENTS.md updated with build, test and style rules.",
        "Use workspace-write sandbox with approvals; read-only for exploration.",
        "Run bandit, pip-audit and npm audit on AI-generated code; log findings.",
        "Check your daily token usage; stop runaway tasks."]),
    dict(h="Don't", bullets=[
        "Paste API keys, customer data or credentials into prompts or AGENTS.md.",
        "Use full-access or bypass modes on any laptop with real credentials.",
        "Ask open-ended 'improve everything' requests or paste the whole codebase.",
        "Use a top-tier model or high reasoning effort for routine edits.",
        "Merge AI code without tests and a human review.",
        "Use models outside the program's approved list."],
        box="**Vibe coding vs structured coding:** accepting whatever the tool writes is fine for a throwaway "
            "prototype. With customers, always use a goal, a plan, small steps, tests and a human review."),
]

DAY1 = SimpleNamespace(
    DAY=1, TITLE="Program Onboarding", DATE="Mon 26 Oct 2026", TRACK="Onboarding",
    SUBTITLE="Program walkthrough, laptop check, pre-assessment, ways of working and the SmartDesk project",
    NEXT="See you tomorrow for Day 2: Python basics, functions, data structures and files.",
    DECK=[
        dict(type="cards", title="Today's journey", greet="Hajimemashite (はじめまして): Nice to meet you", items=[
            ("Program walkthrough", "Calendar, tracks and assessment days (45 min)"),
            ("Laptop check", "Software check with the setup guide (75 min)"),
            ("Pre-assessment", "50 questions, no preparation needed (60 min)"),
            ("Expectations", "Ways of working and support (30 min)"),
            ("SmartDesk", "The project you build all program (30 min)"),
            ("FDE Mindset 1", "Afternoon session with the FDE team"),
        ]),
        dict(type="section", title="The program at a glance", sub="40 days, 26 Oct to 21 Dec 2026"),
        dict(type="table", title="Five tracks", header=["Track", "Days", "What you get"], rows=[
            ["Basics", "15", "Python, MongoDB, FastAPI, JavaScript, Node, React, testing, data, DevOps, Docker, Azure"],
            ["GenAI", "15", "LLMs, prompting, RAG, SLMs, agents, MCP, security, evaluation, LLMOps"],
            ["FDE Mindset", "5", "Days 1, 14, 19, 24, 29 with the FDE team"],
            ["Capstone", "5", "Days 36 to 40: team project, demo on 21 Dec"],
            ["Holiday", "-", "Mon 9 Nov, Deepavali"],
        ], note="GenAI starts in Week 3 (Day 12) and appears every week after."),
        dict(type="table", title="Weeks at a glance", header=["Week", "Dates", "Focus"], rows=[
            ["1", "26 to 30 Oct", "Python, OOP, OpenAI Codex, MongoDB, FastAPI"],
            ["2", "2 to 6 Nov", "SQLAlchemy, security, JavaScript, Node, React"],
            ["3", "10 to 13 Nov", "Full stack, GenAI intro, prompt engineering"],
            ["4", "16 to 20 Nov", "Testing, Spark, DevOps, RAG foundations"],
            ["5", "23 to 27 Nov", "Git, CI/CD, Docker, Azure, vector search, agentic security"],
            ["6", "30 Nov to 4 Dec", "SLMs and token cost, LangGraph, agents, MCP"],
            ["7", "7 to 11 Dec", "Guardrails, evaluation, LLMOps, deployment"],
            ["8 to 9", "14 to 21 Dec", "Observability, then the capstone"],
        ]),
        dict(type="cards", title="Assessment and special days", items=[
            ("Assessments", "Days 5, 10, 13, 17, 27 and 33."),
            ("Senior FDE interaction", "Opening slot on Days 22 and 28."),
            ("1:1 feedback", "End of Days 26 and 32."),
            ("Capstone demo", "Day 40, Mon 21 Dec 2026."),
        ]),
        dict(type="flow", title="A typical technical day", items=[
            ("Quiz", "15 questions on the previous day"),
            ("Sessions", "Deck and live notebook"),
            ("Hands-on", "Problems and app build"),
            ("Hotel lab", "90 to 120 min in the evening"),
            ("Pre-read", "Short read for tomorrow"),
        ]),
        dict(type="cards", title="Nine files every technical day", items=[
            ("Deck and reads", "Deck, pre-read, post-read (recap and beyond)."),
            ("Colab notebook", "Option A for Colab, Option B for VS Code. Offline mode for GenAI."),
            ("Practice", "Hands-on problems and an interactive workbook."),
            ("Build", "App build prompts for OpenAI Codex, with a SmartDesk step."),
            ("Quiz", "15 questions on the previous training day."),
            ("Hotel lab", "NEW (v4): the evening plan, with what to submit."),
        ]),
        dict(type="section", title="Laptop and software check", sub="Use shared/Laptop_Setup_Guide.pdf"),
        dict(type="table", title="Software check", header=["Item", "Needed from", "Check"], rows=[
            ["Browser + Google account", "Day 1 to 2", "Colab runs print('hello')"],
            ["Python 3.12+", "Day 2", "python --version"],
            ["VS Code + OpenAI Codex extension", "Day 3", "code --version"],
            ["Git + GitHub account", "Day 3", "git --version"],
            ["Node.js LTS", "Day 8", "node --version"],
            ["Postman", "Day 9", "GET returns 200"],
            ["Docker Desktop", "Day 20", "docker run --rm hello-world"],
        ], note="Optional: MongoDB Compass, Java 17, Hugging Face account."),
        dict(type="cards", title="Keys and secrets", items=[
            ("Where keys live", "Colab Secrets or a git-ignored .env file."),
            ("Where keys never go", "Code, notebooks, prompts, chats, front-end code, AGENTS.md."),
            ("Two budgets", "One key for Codex from Day 3, one for app calls from Day 12."),
            ("No key?", "GenAI notebooks run in offline demo mode."),
        ]),
        dict(type="section", title="Pre-assessment", sub="50 questions to find your starting point"),
        dict(type="callout", title="Pre-assessment: 50 questions, 60 minutes",
             text="There is no pass mark. It shows where you start, so we can support you well.",
             sub="Answer honestly. Skip a question rather than guess. Results are shared only with your trainers."),
        dict(type="section", title="Ways of working", sub="How we learn together"),
        dict(type="cards", title="Expectations", items=[
            ("Be on time", "Each day starts with the quiz."),
            ("Hands on keyboard", "Run every demo yourself."),
            ("Ask early", "If you are stuck for 15 minutes, ask."),
            ("Review AI code", "From Day 3, read every diff Codex writes."),
            ("Hotel lab", "Do the evening lab and submit the listed item."),
            ("Respect data", "No customer data or secrets in any tool."),
        ]),
        dict(type="section", title="SmartDesk", sub="One project, built step by step"),
        dict(type="cards", title="SmartDesk: a telecom support platform", items=[
            ("The brief", "Customers raise tickets; agents resolve them faster with AI help."),
            ("Users", "Customer, support agent, team lead, admin."),
            ("How it grows", "CLI, API, full stack, RAG, agents, production."),
            ("Where", "shared/SmartDesk and a SmartDesk prompt in each day's App_Build_Prompts.md."),
        ]),
        dict(type="cards", title="Before tomorrow", lead="Day 2 has no quiz. It starts straight away.", items=[
            ("Laptop", "Finish any Required install you could not complete today."),
            ("Pre-read", "Read the Day 2 pre-read on Python basics."),
            ("Colab", "Check you can open and run a Colab notebook."),
        ]),
    ])


def main():
    pdf(os.path.join(ROOT, "shared", "Laptop_Setup_Guide.pdf"), "FDE PROGRAM | LAPTOP SETUP GUIDE",
        "Laptop Setup Guide", "Install and check everything before Day 1 (Mon 26 Oct 2026). About 60 to 90 minutes.",
        LAPTOP, "FDE Program v4  |  Laptop Setup Guide")
    pdf(os.path.join(ROOT, "shared", "Codex_Setup_and_Dos_Donts.pdf"), "FDE PROGRAM | OPENAI CODEX",
        "OpenAI Codex: Setup and Do's and Don'ts", "A two-page card for Day 3 and every day after.",
        CODEX, "FDE Program v4  |  OpenAI Codex card")
    R.build_deck(DAY1, os.path.join(ROOT, "Day01-Onboarding-and-FDE-Mindset-1", "Day01_Deck_Program_Walkthrough.pptx"))
    print("shared docs built")


if __name__ == "__main__":
    main()
