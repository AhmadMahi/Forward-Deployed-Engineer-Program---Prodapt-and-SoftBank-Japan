"""Build the v4 capstone guide, project briefs and kickoff deck.

Usage: python tools/build/extras/capstone_build.py
Writes into Day36-40-Capstone/ using the same visual style as the day materials (fde_render).
"""
import os
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import fde_render as R  # noqa: E402
import capstone_content as C  # noqa: E402

OUT = os.path.join(ROOT, "Day36-40-Capstone")
NEW = '  <font name="Helvetica-Bold" size="9" color="#FF7A2F">NEW (v4)</font>'


def _p(flow, st, text, style="body"):
    from reportlab.platypus import Paragraph
    flow.append(Paragraph(R._md(text), st[style]))


def _bul(flow, st, items):
    from reportlab.platypus import Paragraph
    for b in items:
        flow.append(Paragraph(R._md(b), st["bullet"], bulletText="•"))


def _h(flow, st, text, new=False):
    from reportlab.platypus import Paragraph
    flow.append(Paragraph(R._md(text) + (NEW if new else ""), st["h2"]))


def schedule(flow, st, checkpoints=True):
    from reportlab.platypus import Paragraph
    for head, items, cp in C.SCHEDULE:
        flow.append(Paragraph(R._md(head), st["h3"]))
        _bul(flow, st, items + ([cp] if (cp and checkpoints) else []))


def table(flow, header, rows, st, widths):
    """Like fde_render._table, with column widths given as fractions."""
    from reportlab.lib.colors import HexColor
    from reportlab.platypus import Paragraph, Table, TableStyle
    data = [[Paragraph(f"<b>{R._md(str(h))}</b>", st["box"]) for h in header]]
    data += [[Paragraph(R._md(str(v)), st["box"]) for v in r] for r in rows]
    tb = Table(data, colWidths=[481.9 * w for w in widths], repeatRows=1)
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), HexColor("#" + R.CARD)),
                            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#FFFFFF"), HexColor("#" + R.CARD2)]),
                            ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#9ED9D4")),
                            ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    flow.append(tb)


def rubric(flow, st):
    table(flow, C.RUBRIC[0], C.RUBRIC[1:], st, [0.28, 0.1, 0.62])


def build_guide():
    from reportlab.platypus import Spacer
    st = R._pdf_styles()
    flow = []
    R._header(flow, st, "DAYS 36 TO 40 | CAPSTONE", "Capstone Guide",
              "Five days, one real-world product, built end to end by your team. Tue 15 Dec to Mon 21 Dec 2026.")
    _h(flow, st, "1. What the capstone is")
    _p(flow, st, "For the final week you work in teams of 3 to 4 and build a complete product for a realistic customer "
                 "scenario, using everything from Days 1 to 35: Python, APIs, databases, React, testing, data "
                 "pipelines, cloud and containers, GenAI, agents, security, evaluation and LLMOps. You also practise "
                 "the FDE Mindset skills: scoping with a customer, handling ambiguity, communicating progress and "
                 "presenting results.")
    _p(flow, st, "**Goal:** a working, tested, deployable product with measured quality, and a confident ten minute "
                 "demo. Depth beats breadth: a smaller scope done well scores higher than many half-finished features.")
    _h(flow, st, "2. Choose one of six projects")
    rows = [[p["no"], p["name"] + (" (NEW v4)" if p.get("new") else ""), p["core"]] for p in C.PROJECTS]
    table(flow, ["#", "Project", "Core skills"], rows, st, [0.07, 0.53, 0.4])
    flow.append(Spacer(1, 6))
    _p(flow, st, "Full briefs are in the Projects folder. Each team picks one project in the first hour of Day 36. Two "
                 "teams may choose the same project; they will be compared on the same checklist.")
    _h(flow, st, "3. Technical baseline (every project)")
    _bul(flow, st, C.BASELINE)
    _h(flow, st, "4. Baseline additions in v4 (every project)", new=True)
    _bul(flow, st, C.BASELINE_V4)
    _h(flow, st, "5. Day-by-day plan")
    schedule(flow, st)
    _h(flow, st, "6. Daily stand-up (15 minutes)")
    _p(flow, st, "Each person answers three questions: what I finished yesterday, what I will finish today, what is "
                 "blocking me. The team updates its board and decision log. Mentors join at least once a day. In the "
                 "evening, follow Hotel_Lab.md to prepare the next stand-up.")
    _h(flow, st, "7. Rules")
    _bul(flow, st, [
        "OpenAI Codex (VS Code extension, program API key, approved models only) is the AI coding tool. Work through "
        "reviewed pull requests. Disclose in the README which parts were generated and how you reviewed them.",
        "Never paste API keys, customer data or credentials into prompts or AGENTS.md. Check daily token usage.",
        "Use only the generated or public sample data. Never use real customer or personal data.",
        "Keep secrets out of Git. Use environment variables or a secret store such as Azure Key Vault.",
        "Every team member must be able to explain every part of the system during Q&A.",
        "Cloud resources (Azure window 3, Days 38 to 40): use tags, stay within the agreed budget, and delete "
        "resource groups after demo day."])
    _h(flow, st, "8. Deliverables (due Day 40, Mon 21 Dec 2026, 09:00 IST)")
    table(flow, ["Deliverable", "Details"], [
        ["Repository", "Code, tests, Dockerfiles, pipeline YAML, golden set, AGENTS.md (NEW v4), README with setup, "
                       "architecture and AI tool disclosure"],
        ["Architecture diagram", "Components, data flow, where AI is used, guardrails"],
        ["Evaluation report", "Golden set results, metrics, error analysis, slices, known limits"],
        ["Operations note", "How to deploy, monitor, roll back; one runbook"],
        ["Security checklist (NEW v4)", "OWASP Top 10 for Agentic Applications, one line of evidence per item"],
        ["Vulnerability report (NEW v4)", "Findings, severity, fix, verified, from scans and red-team tests"],
        ["Token and cost report (NEW v4)", "Tokens and estimated cost per request and per 1,000 requests, before "
                                           "and after one optimisation (placeholder prices labelled)"],
        ["Modernisation note (NEW v4)", "The legacy module, characterisation tests, the steps taken and the PR links"],
        ["Demo deck", "8 to 12 slides: problem, solution, demo, results, limits, next steps"],
        ["Decision log", "Key decisions with options, reasons and dates"],
    ], st, [0.32, 0.68])
    _h(flow, st, "9. Demo day format")
    _bul(flow, st, ["10 minutes: problem and users (1), live demo (5), results and evaluation (2), limits and next "
                    "steps (2).",
                    "5 minutes of Q&A from evaluators acting as the customer's sponsor, IT lead and security lead.",
                    "Every team member speaks. Lead with the answer, show evidence, be honest about limits."])
    _h(flow, st, "10. Evaluation rubric (100 points)")
    rubric(flow, st)
    flow.append(Spacer(1, 6))
    _p(flow, st, "Each criterion is scored on four levels; points = weight x level / 4.")
    table(flow, C.LEVELS[0], C.LEVELS[1:], st, [0.25, 0.75])
    flow.append(Spacer(1, 6))
    _p(flow, st, "Grade bands: 85 to 100 Distinction, 70 to 84 Merit, 55 to 69 Pass, below 55 Needs resubmission. "
                 "Individual scores can be adjusted by up to 10 points based on peer feedback and Q&A.")
    _h(flow, st, "11. Submission checklist")
    _bul(flow, st, ["README lets a stranger run the project in under 15 minutes",
                    "CI pipeline is green on main, with security gates (bandit, pip-audit, npm audit)",
                    "Golden set and evaluation report are committed",
                    "AGENTS.md, security checklist, vulnerability report and token and cost report are committed "
                    "(NEW v4)",
                    "No secrets or personal data in the repository",
                    "Demo works without internet surprises (have a recorded backup)",
                    "Azure resources tagged and scheduled for deletion"])
    _p(flow, st, "Ganbatte (頑張って): do your best")
    R._doc(os.path.join(OUT, "00_Capstone_Guide.pdf"), "Capstone  |  Guide", "Capstone  |  Guide", flow)


def build_brief(p):
    from reportlab.platypus import Spacer
    st = R._pdf_styles()
    flow = []
    kicker = f"CAPSTONE PROJECT {p['no']}" + (" | NEW (v4)" if p.get("new") else "")
    R._header(flow, st, kicker, p["name"], p["customer"])
    _h(flow, st, "1. The customer's problem")
    _p(flow, st, p["problem"])
    _h(flow, st, "2. Users")
    _bul(flow, st, p["users"])
    _h(flow, st, "3. User stories")
    _bul(flow, st, p["stories"])
    _h(flow, st, "4. Requirements")
    for label, key in (("Must have", "must"), ("Should have", "should"), ("Could have (stretch)", "could")):
        _p(flow, st, label, "h3")
        _bul(flow, st, p[key])
    _h(flow, st, "5. Data")
    _p(flow, st, p["data"])
    _h(flow, st, "6. Suggested AI approach")
    _p(flow, st, p["approach"])
    _h(flow, st, "7. Suggested architecture")
    R._code(flow, C.ARCH, st)
    _h(flow, st, "8. v4 baseline for this project", new=not p.get("new"))
    _p(flow, st, "**Modernisation step:** " + p["modern"])
    _bul(flow, st, C.BASELINE_V4[1:])
    _h(flow, st, "9. How to do it: day by day")
    schedule(flow, st, checkpoints=False)
    _h(flow, st, "10. Project-specific acceptance checks")
    _p(flow, st, "Evaluators run these during or after the demo. They count towards Core functionality and AI quality.")
    _bul(flow, st, p["checks"])
    _h(flow, st, "11. Golden set: starter items")
    _p(flow, st, "Extend these to at least 20 items (30 for PolicyPal) with expected answers, sources and tags.")
    _bul(flow, st, p["golden"])
    _h(flow, st, "12. How you will be evaluated")
    rubric(flow, st)
    flow.append(Spacer(1, 6))
    _h(flow, st, "13. Common pitfalls")
    _bul(flow, st, p["pitfalls"])
    _h(flow, st, "14. Getting started")
    nb = p["file"] + "_Starter.ipynb"
    pr = p["file"] + "_Prompts.md"
    _bul(flow, st, [f"Open Starter_Notebooks/{nb} in Colab or VS Code to generate the data and see a working "
                    "baseline.",
                    f"Use App_Build_Prompts/{pr} with OpenAI Codex to scaffold the project. Review every diff.",
                    "Write your problem statement and assumptions log before writing code."])
    _p(flow, st, "Ganbatte (頑張って): do your best")
    name = f"{p['file']}_Brief.pdf"
    label = f"Capstone {p['no']}  |  {p['key']}"
    R._doc(os.path.join(OUT, "Projects", name), label, label, flow)


def build_deck():
    spec = types.SimpleNamespace(
        DAY=36, TITLE="Capstone Project", DATE="Tue 15 Dec to Mon 21 Dec 2026", TRACK="Capstone",
        SUBTITLE="Days 36 to 40: build a real product end to end, measure it, and present it like an FDE",
        NEXT="Demo day is Monday 21 December. Build something you are proud of.",
        CLOSING_GREET="Ganbatte kudasai (頑張ってください): Please do your best")
    proj = C.PROJECTS
    spec.DECK = [
        dict(type="cards", title="Capstone week at a glance", greet="Ohayou gozaimasu (おはようございます): Good morning",
             items=[("Day 36 Tue 15 Dec", "Quiz, teams, scoping and design"),
                    ("Day 37 Wed 16 Dec", "Core build: data, API, AI core"),
                    ("Day 38 Thu 17 Dec", "Front end, guardrails, evaluation"),
                    ("Day 39 Fri 18 Dec", "Deploy, observe, rehearse. Code freeze 17:00 IST"),
                    ("Day 40 Mon 21 Dec", "Deliverables 09:00 IST. Demo day and evaluation"),
                    ("Every day", "15 minute stand-up, decision log, evening hotel lab")]),
        dict(type="cards", title="By the end of the capstone you can", items=[
            ("Scope like an FDE", "Turn a customer brief into a clear MVP with success metrics."),
            ("Build end to end", "Data, API, AI, UI, tests, containers and pipeline."),
            ("Prove quality and safety", "Golden set, metrics, quality gate, security checklist."),
            ("Present with confidence", "Answer first, live demo, honest limits, strong Q&A.")]),
        dict(type="section", title="Choose your project", sub="Six realistic customer scenarios"),
        dict(type="cards", title="The six projects", items=[
            ("ShopSmart", "E-commerce recommendations and a grounded shopping assistant."),
            ("BookFinder", "Library search in plain language, with availability and reservations."),
            ("PolicyPal", "HR and IT policy chatbot with citations, guardrails and handoff."),
            ("SupportPilot", "Agentic support assistant with tools, approvals and an MCP server."),
            ("InsightDesk", "PySpark sales pipeline and a safe natural-language data agent."),
            ("LegacyLift NEW (v4)", "Modernise a legacy order app to FastAPI + React with Codex, tests first.")],
             note="Full briefs, starter notebooks and build prompts are in the capstone folder."),
        dict(type="table", title="Which project fits your team?", header=["Project", "Strongest focus",
                                                                         "Course days used most"],
             rows=[[p["key"] + (" (NEW v4)" if p.get("new") else ""), p["focus"], p["days"]] for p in proj]),
        dict(type="section", title="What every team must deliver", sub="The technical baseline"),
        dict(type="cards", title="Technical baseline", items=[
            ("Back end", "FastAPI with Pydantic, 6+ endpoints, a database."),
            ("Front end", "React with loading, error and empty states."),
            ("AI core", "RAG, recommendations, agent or data agent."),
            ("Quality", "Golden set, metrics, quality gate in CI."),
            ("Safety", "Guardrails, secrets handling, least privilege."),
            ("Operations", "Docker, deployment, logs, a monitoring view.")]),
        dict(type="cards", title="Baseline additions in v4", new=True, items=[
            ("Modernisation step", "One legacy module from your brief, characterisation tests first, small PRs."),
            ("AGENTS.md", "Build, test and style commands; folders not to touch; no secrets in prompts."),
            ("Security checklist", "Mapped to the OWASP Top 10 for Agentic Applications."),
            ("Vulnerability report", "bandit, pip-audit, npm audit and red-team findings, fixed and verified."),
            ("Token and cost report", "Cost per request and per 1,000, before and after one optimisation."),
            ("Templates", "shared/templates: OWASP checklist, vulnerability report, learner AGENTS.md.")]),
        dict(type="table", title="Deliverables (due Day 40, 09:00 IST)", header=["Deliverable", "What it contains"],
             rows=[["Repository", "Code, tests, Dockerfiles, pipeline, golden set, README, AGENTS.md, AI tool "
                                  "disclosure"],
                   ["Architecture diagram", "Components, data flow, AI usage, guardrails"],
                   ["Evaluation report", "Metrics, error analysis, slices, known limits"],
                   ["Operations note", "Deploy, monitor, roll back, one runbook"],
                   ["Security and cost (NEW v4)", "OWASP Agentic checklist, vulnerability report, token and cost "
                                                  "report"],
                   ["Demo deck and decision log", "8 to 12 slides; key decisions with options and reasons"]]),
        dict(type="section", title="How you will be evaluated", sub="100 points, four levels per criterion"),
        dict(type="table", title="Rubric part 1", header=["Criterion", "Points", "Evaluators look for"], rows=[
            ["Problem understanding and scoping", "10", "Problem statement, users, metrics, assumptions, MVP"],
            ["Architecture and design", "10", "Clear diagram, layered code, reasoned choices"],
            ["Core functionality", "20", "Must-haves work end to end; acceptance checks pass"],
            ["AI and data quality", "15", "Golden set of 20+, metrics, error analysis"]]),
        dict(type="table", title="Rubric part 2", header=["Criterion", "Points", "Evaluators look for"], rows=[
            ["Engineering quality", "10", "Tests, CI green, pull requests, AGENTS.md, modernisation step"],
            ["Security and responsible AI", "10", "Guardrails, secrets, red-team, OWASP checklist, vulnerability "
                                                  "report"],
            ["Deployment and operations", "10", "Containers, deployment, logs, monitoring, drift check, cost report"],
            ["Demo and communication", "10", "Answer first, live demo, honest limits, Q&A"],
            ["Teamwork and process", "5", "Stand-ups, decision log, fair contribution"]],
             note="Points = weight x level / 4. Distinction 85+, Merit 70+, Pass 55+."),
        dict(type="section", title="Demo day", sub="Ten minutes to show what you built"),
        dict(type="flow", title="Your 10 minute demo", items=[
            ("1 min", "Problem and users"), ("5 min", "Live demo of real user stories"),
            ("2 min", "Results: metrics and evaluation"), ("2 min", "Limits and next steps"),
            ("5 min Q&A", "Sponsor, IT and security questions")],
             note="Every team member speaks. Have a recorded backup in case the network fails."),
        dict(type="cards", title="Rules of the week", greet="Chiimu waaku (チームワーク): Teamwork", items=[
            ("OpenAI Codex, reviewed", "Approved models only; reviewed PRs; disclose what was generated."),
            ("Sample data only", "Never real customer or personal data."),
            ("Secrets stay secret", "Environment variables or Key Vault, never Git or prompts."),
            ("Everyone can explain everything", "Q&A may be directed at any team member.")]),
        dict(type="callout", title="Your first two hours", greet="Ganbatte (頑張って): Do your best",
             text="Form teams, choose a project, then write the problem statement, users, success metrics and "
                  "assumptions log before any code. Checkpoint 1 at the end of today is a design review with your "
                  "mentor.",
             sub="Depth beats breadth: a smaller scope done well scores higher than many half-finished features."),
        dict(type="cards", title="Key reminders", items=[
            ("Scope first", "Agree the MVP; keep a visible backlog for extras."),
            ("Measure", "Golden set and token log from day one; numbers on demo day."),
            ("Ship small, often", "Pull requests, green CI with security gates, daily checkpoints."),
            ("Communicate", "Stand-ups, decision log, honest status.")]),
    ]
    R.build_deck(spec, os.path.join(OUT, "Capstone_Kickoff_Deck.pptx"))


if __name__ == "__main__":
    build_guide()
    for p in C.PROJECTS:
        build_brief(p)
    build_deck()
    print("Capstone guide, 6 briefs and kickoff deck built.")
