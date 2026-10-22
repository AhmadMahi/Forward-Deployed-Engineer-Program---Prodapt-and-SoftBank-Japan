"""Day 17 spec. Basics: DevOps and Cloud Fundamentals (Assessment day).
Source: archive/v1-40-day/Day17 (reused and updated). NEW (v4) topics are marked.
"""
DAY = 17
FOLDER = "Day17-DevOps-and-Cloud-Fundamentals"
SLUG = "DevOps_and_Cloud_Fundamentals"
TITLE = "DevOps and Cloud Fundamentals"
SUBTITLE = "DevOps and CI/CD, DevSecOps scanning, cloud models and migration paths, Azure and Azure DevOps"
DATE = "Wed 18 Nov 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 18: context engineering and RAG foundations."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 16"),
        ("DevOps and CI/CD", "Culture, the loop, automated build and test"),
        ("DevSecOps", "SAST, dependency and secret scanning. NEW (v4)"),
        ("Cloud basics", "IaaS, PaaS, SaaS; regions; migration paths"),
        ("Azure DevOps", "Boards, Repos, Pipelines (web)"),
        ("Assessment", "Basics assessment 3 (1.5 hrs)"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Explain DevOps and CI/CD", "Describe the loop, CI, delivery and deployment."),
        ("Add security to CI", "Run SAST, dependency and secret scans, and read the results."),
        ("Pick a cloud model", "Choose IaaS, PaaS or SaaS and a migration path for a scenario."),
        ("Navigate Azure DevOps", "Use Boards, Repos and Pipelines in the browser."),
    ]),
    dict(type="table", title="How today is organised", header=["Session", "Duration", "Focus"], rows=[
        ["Session 1", "1 hr", "DevOps and CI/CD concepts; DevSecOps intro (NEW v4)"],
        ["Session 2", "1.5 hrs", "IaaS, PaaS, SaaS; Azure regions and resource groups; migration paths"],
        ["Session 3", "2 hrs", "Azure DevOps: Boards, Repos, Pipelines (web)"],
        ["Assessment", "1.5 hrs", "Basics assessment 3: testing, data engineering, DevOps"],
    ]),

    dict(type="section", title="DevOps and CI/CD", sub="Session 1 (1 hr): building and running software as one team"),
    dict(type="compare", title="Before and after DevOps", left=dict(title="Separate silos", bullets=[
        "Developers \"throw code over the wall\"", "Operations deploy months later", "Big, risky releases",
        "Blame when things break",
    ]), right=dict(title="DevOps", bullets=[
        "One team owns build and run", "Small changes shipped often", "Automation everywhere",
        "Learn from failures without blame",
    ])),
    dict(type="flow", title="The DevOps loop", items=[
        ("Plan", "Boards, backlog"),
        ("Code", "Branches, reviews"),
        ("Build + test", "Automated CI"),
        ("Release", "Automated CD"),
        ("Operate", "Logs, alerts, feedback"),
    ], note="The loop never ends: what you learn in production shapes the next plan."),
    dict(type="table", title="Three CI/CD terms", header=["Term", "What happens automatically", "Human step"], rows=[
        ["Continuous Integration", "Every push is built and tested", "Merge when green"],
        ["Continuous Delivery", "Every green build is ready to release", "Click to deploy"],
        ["Continuous Deployment", "Every green build goes to production", "None"],
    ], note="Most teams start with CI, then add delivery. Full deployment needs strong tests."),
    dict(type="flow", title="A typical CI pipeline", greet="Kaizen (改善): Continuous improvement", items=[
        ("Trigger", "Push or pull request"),
        ("Install", "Dependencies"),
        ("Lint", "Style and obvious bugs"),
        ("Test", "Unit and integration"),
        ("Package", "Artifact or image"),
    ], note="If any step fails, the pipeline stops and the team is told immediately."),
    dict(type="cards", title="DevSecOps: security inside the loop", new=True, items=[
        ("Shift left", "Find security problems at commit time, not after release."),
        ("Everyone's job", "Developers fix findings like failing tests."),
        ("Automated gates", "Scans run in CI on every push and pull request."),
        ("AI-generated code too", "Code from Codex goes through the same scans and review."),
    ]),
    dict(type="table", title="Three scans every Python project should run", new=True,
         header=["Scan", "Finds", "Tool today"], rows=[
        ["SAST (static analysis)", "Risky code: eval, shell=True, hard-coded passwords", "bandit"],
        ["Dependency scanning", "Libraries with known vulnerabilities (CVEs)", "pip-audit (npm audit for JS)"],
        ["Secret scanning", "Keys, tokens and passwords committed to the repo", "A secret scanner in CI"],
    ], note="Day 20 turns these into CI gates and vulnerability report v2."),
    dict(type="bullets_code", title="Reading a bandit finding", new=True, bullets=[
        "Each finding has an ID, severity and confidence",
        "It points to the file and line",
        "Fix the code, or justify and suppress",
        "Never suppress just to make CI green",
    ], code='''>> Issue: [B602:subprocess_popen_with_shell_equals_true]
   subprocess call with shell=True identified,
   security issue.
   Severity: High   Confidence: High
   Location: app/report.py:12
11  def export(name):
12      subprocess.run(f"zip {name}.zip data", shell=True)

Fix: subprocess.run(["zip", f"{name}.zip", "data"])'''),

    dict(type="section", title="Cloud basics", sub="Session 2 (1.5 hrs): who manages what"),
    dict(type="table", title="IaaS, PaaS and SaaS", header=["Model", "You manage", "Provider manages", "Azure example"],
         rows=[
        ["On-premises", "Everything", "Nothing", "Your own servers"],
        ["IaaS", "OS, runtime, app, data", "Hardware, network", "Virtual Machines"],
        ["PaaS", "App and data", "OS, runtime, scaling", "App Service"],
        ["SaaS", "Your data and users", "Everything else", "Microsoft 365"],
    ], note="The pizza analogy: make it at home, take and bake, delivery, or dine out."),
    dict(type="cards", title="Choosing a model", lead="FDEs usually prefer PaaS for speed, and IaaS only when the "
                                                       "customer requires it.", items=[
        ("IaaS when", "You need full control of the OS or special software."),
        ("PaaS when", "You want to deploy code and let the platform run it."),
        ("SaaS when", "A ready-made product already solves the problem."),
    ]),
    dict(type="flow", title="How Azure is organised", items=[
        ("Tenant", "Your organisation's identity (Entra ID)"),
        ("Subscription", "Billing and access boundary"),
        ("Resource group", "Folder for related resources"),
        ("Resources", "Apps, databases, storage"),
    ], note="Delete a resource group and everything inside goes with it: great for clean up, dangerous by accident."),
    dict(type="cards", title="Regions and resource groups in practice", items=[
        ("Pick a region", "Close to users and where data must stay, for example Japan East."),
        ("One group per app and stage", "rg-smartdesk-dev, rg-smartdesk-prod."),
        ("Tag everything", "owner, project, stage. Helps cost and clean up."),
        ("Clean up", "Delete training resource groups after Day 21."),
    ]),
    dict(type="table", title="Cloud migration paths: rehost to replace", header=["Path", "What changes", "Example"],
         rows=[
        ["Rehost", "Nothing in the app; move the VM (lift and shift)", "Old ticketing server to an Azure VM"],
        ["Replatform", "Small changes to use a managed service", "Same app, database moved to Azure SQL"],
        ["Refactor", "Code changes, same design", "Add config and health checks for App Service"],
        ["Rearchitect", "Change the design", "Split a monolith into services"],
        ["Rebuild", "Write it again, cloud native", "New FastAPI + React app"],
        ["Replace", "Buy instead of build", "Move to a SaaS helpdesk"],
    ], note="Left is faster and cheaper to start; right gives more cloud benefit. Day 23 revisits this."),

    dict(type="section", title="Azure DevOps", sub="Session 3 (2 hrs): one tool chain for the whole loop, in the browser"),
    dict(type="table", title="Azure DevOps services", header=["Service", "Used for", "When"], rows=[
        ["Boards", "Backlog, sprints, work items", "Today"],
        ["Repos", "Git repositories and pull requests", "Today and Day 20"],
        ["Pipelines", "CI/CD with YAML", "Today, Days 20 and 21"],
        ["Test Plans", "Manual and exploratory testing", "Overview"],
        ["Artifacts", "Package feeds (pip, npm)", "Overview"],
    ], note="GitHub plus GitHub Actions is a common alternative with the same ideas."),
    dict(type="flow", title="Web walkthrough: from story to green build", items=[
        ("Boards", "Create a user story"),
        ("Repos", "Import the SmartDesk repo"),
        ("Branch + PR", "Link the story to the PR"),
        ("Pipelines", "New pipeline from YAML"),
        ("Run", "Read each step's log"),
    ], note="Everything today runs in the browser. No local Azure tools are needed."),
    dict(type="bullets_code", title="A pipeline file with a security stage", new=True, bullets=[
        "Lives in the repo as azure-pipelines.yml",
        "Stages run in order; any failure stops the run",
        "Build: lint and test",
        "Security: bandit and pip-audit",
    ], code='''trigger:
  - main
pool:
  vmImage: ubuntu-latest
stages:
  - stage: Build
    jobs:
      - job: test
        steps:
          - script: pip install -r requirements-dev.txt
          - script: ruff check .
          - script: pytest -q --junitxml=results.xml
  - stage: Security
    jobs:
      - job: scan
        steps:
          - script: pip install bandit pip-audit
          - script: bandit -r app -ll
          - script: pip-audit -r requirements.txt'''),
    dict(type="cards", title="SmartDesk step 15: lint, tests and pipeline YAML", items=[
        ("Lint", "ruff check passes on the whole repo."),
        ("Tests", "pytest -q with JUnit results published."),
        ("Pipeline YAML", "Build and Security stages in azure-pipelines.yml."),
        ("Build with Codex", "Use Day17_App_Build_Prompts.md. Review every line Codex writes."),
    ]),
    dict(type="callout", title="Assessment: Basics assessment 3",
         text="Basics assessment 3 (1.5 hrs): testing, data engineering and DevOps.",
         sub="Covers Days 15 to 17: PyTest and TestClient, ETL and data quality, Spark and SQL, CI/CD, cloud models "
             "and DevSecOps scans. Quick MCQs first, then the coding task.",
         greet="Ganbatte kudasai (頑張ってください): Please do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("DevOps", "One team, small changes, automation, blameless learning."),
        ("DevSecOps", "SAST, dependency and secret scans on every push."),
        ("Cloud", "IaaS control, PaaS speed, SaaS ready-made; rehost to replace."),
        ("Azure DevOps", "Boards, Repos, Pipelines; YAML in the repo."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.",
         items=[
        ("Hotel lab", "Follow Day17_Hotel_Lab.md: YAML plus a one-paragraph explanation."),
        ("Workbook", "Complete the Day 17 workbook."),
        ("Pre-read", "Skim the Day 18 pre-read on giving AI the right information."),
    ]),
]

PREREAD = dict(title="From My Laptop to the World",
               lede="A light read before Day 17. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "So far, everything you built runs on your laptop or in Colab. Real users cannot reach it. This week you learn "
        "how teams ship software safely and often, and how the cloud gives you computers on demand."]),
    dict(h="1. DevOps: one team, one goal", paras=[
        "Imagine a restaurant where the chefs cook, then hand plates to a separate team who decides weeks later "
        "whether to serve them. Food goes cold and nobody owns the result. DevOps joins the people who build software "
        "(development) with the people who run it (operations), so the same team cooks and serves."]),
    dict(h="2. Assembly lines for code: CI/CD", paras=[
        "Car factories check every part automatically as it moves down the line. **Continuous Integration** does the "
        "same for code: every change is automatically built and tested. **Continuous Delivery** keeps the product "
        "always ready to ship at the press of a button."],
        box="**Key idea:** small changes, checked automatically, shipped often, are far safer than big changes shipped "
            "rarely."),
    dict(h="3. Locks checked on the line", new=True, paras=[
        "The same assembly line can also check for security problems: risky code, parts (libraries) with known flaws, "
        "and keys left lying around. Doing this early is called **DevSecOps**. It matters even more now that AI tools "
        "write some of the code."]),
    dict(h="4. Renting computers: the cloud", table=[
        ["Option", "Cloud name", "You look after"],
        ["Own the car", "On-premises", "Everything, including the building and hardware"],
        ["Lease a car", "IaaS (Infrastructure as a Service)", "The operating system, software and data"],
        ["Taxi", "PaaS (Platform as a Service)", "Just your app and its data"],
        ["Bus", "SaaS (Software as a Service)", "Just your account and how you use it"]]),
    dict(h="5. Meet Azure and today's assessment", paras=[
        "Microsoft Azure is one of the largest cloud providers. You organise everything into **resource groups**, like "
        "folders, inside a **subscription**, which is how usage is billed. Azure DevOps is Microsoft's tool set for "
        "planning work, storing code and running CI/CD pipelines. Today also includes Basics assessment 3 on testing, "
        "data engineering and DevOps."]),
    dict(h="6. Think about these before class", bullets=[
        "What steps would you check by hand before releasing an app? Which could a machine check instead?",
        "Which apps that you use are SaaS?",
        "Why might a bank prefer IaaS, while a start-up prefers PaaS?"],
        after=["Kaizen (改善): continuous improvement"]),
])

POSTREAD = dict(title="DevOps and Cloud: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["DevOps", "Shared ownership, small changes, automation, blameless learning."],
        ["DevOps loop", "Plan, code, build and test, release, operate and monitor, repeat."],
        ["CI / delivery / deployment", "Every push tested; every green build release-ready; or released automatically."],
        ["DevSecOps (NEW v4)", "SAST (bandit), dependency scanning (pip-audit, npm audit), secret scanning in CI."],
        ["IaaS / PaaS / SaaS", "Less to manage and less control as you move right."],
        ["Migration paths", "Rehost, replatform, refactor, rearchitect, rebuild, replace."],
        ["Azure hierarchy", "Tenant, subscription, resource group, resources; pick the region with care."],
        ["Azure DevOps", "Boards, Repos, Pipelines, Test Plans, Artifacts."],
        ["Pipeline YAML", "trigger, pool, stages, jobs and steps in azure-pipelines.yml."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. The shared responsibility model", paras=[
        "Security is shared. In every model the cloud provider secures the physical data centres; you always remain "
        "responsible for your data, your users and how you grant access."]),
    dict(sub="2. Triage of scan results", paras=[
        "Not every finding is equal. Fix high-severity findings first, check whether the vulnerable code path is used, "
        "and record each decision. You started vulnerability report v1 on Day 7; Day 20 extends it to v2 with CI gates."]),
    dict(sub="3. DORA metrics", paras=[
        "Teams often track deployment frequency, lead time for changes, change failure rate and time to restore "
        "service. They show whether DevOps practices are working."]),
    dict(sub="4. Infrastructure as Code", paras=[
        "Instead of clicking in the portal, describe resources in files (Bicep, ARM or Terraform), review them like "
        "code and recreate environments identically."]),
    dict(sub="5. Tags and cost control", paras=[
        "Tag resources with owner and project, set budgets and alerts, and delete test resource groups when finished. "
        "Check current pricing and free offers on the Azure website, as they change."]),
    dict(h="Part C: Check yourself", bullets=[
        "What is the difference between continuous delivery and continuous deployment?",
        "Name the three DevSecOps scans and one tool for each.",
        "Give one example each of IaaS, PaaS and SaaS on Azure.",
        "When would you choose rehost over rebuild?",
        "What happens when you delete a resource group?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Run bandit on your SmartDesk back end and fix one finding.",
        "Write an azure-pipelines.yml with Build and Security stages for your Day 15 tests.",
        "Classify ten tools you use at work as IaaS, PaaS or SaaS."],
        after=["**Coming up on Day 18:** context engineering and RAG foundations.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems on DevOps, DevSecOps and cloud concepts with a local CI simulator. Azure tasks use "
                    "the web portal and Azure DevOps in the browser; delete any resources afterwards.", problems=[
    dict(title="Map the Loop", level="Warm-up", concepts="DevOps loop",
         text="For your SmartDesk app, write what happens at each stage of the DevOps loop: plan, code, build and test, "
              "release, operate and monitor.",
         sample='Plan: user story "filter tickets by priority" on the board\nCode: feature branch + pull request\n...',
         hints=["Be concrete: name the tool and the artefact at each stage."]),
    dict(title="Delivery or Deployment?", level="Easy", concepts="CI, continuous delivery, continuous deployment",
         text="For each team, say which practice they use: (a) tests run on every push, release monthly by hand; "
              "(b) every green build waits for a manager's click; (c) every green build goes live.",
         sample="(a) CI only\n(b) Continuous delivery\n(c) Continuous deployment",
         hints=["Ask: is there a human approval step?"]),
    dict(title="Cloud Model and Migration Path", level="Easy", concepts="IaaS, PaaS, SaaS, rehost to replace",
         text="Pick a model and a migration path for: a legacy ticketing server needing a custom Windows driver; a "
              "FastAPI service; company email; an old reporting app the team wants to rewrite; a database nobody wants "
              "to patch.",
         sample="Legacy server: IaaS, rehost\nFastAPI: PaaS (App Service), refactor\nEmail: SaaS, replace",
         hints=["The more you must control, the further left you go."]),
    dict(title="Local CI Simulator", level="Medium", concepts="pipeline steps, fail fast",
         text="Using the notebook, run the CI simulator on the sample project. Introduce a failing test, watch the "
              "pipeline stop, then fix it and get a green run.",
         sample="[1/2] Lint         ... OK\n[2/2] Unit tests   ... FAILED\nPipeline stopped",
         hints=["Read the failing test output before changing code."]),
    dict(title="Scan and Fix", level="Medium", concepts="SAST, secret scanning", new=True,
         text="Run bandit and the notebook's secret scanner on the sample report module. Record each finding (tool, "
              "severity, file, line, proposed fix), fix the code, and re-run until both scans are clean.",
         sample="bandit: 4 issues (B404 Low, B105 Low, B602 High, B307 Medium)\nsecrets: 1 finding in report.py:3\n"
                "after fixes: bandit -ll 0 issues, secrets 0 findings",
         hints=["Move the secret to an environment variable.", "Use a list of arguments instead of shell=True."]),
    dict(title="Write a Pipeline YAML with a Security Stage", level="Challenging",
         concepts="azure-pipelines.yml, stages", new=True,
         text="Write a pipeline that triggers on main and pull requests, runs on ubuntu-latest, uses Python 3.12, has "
              "a Build stage (install, ruff, pytest with JUnit results) and a Security stage (bandit, pip-audit). "
              "Validate it with yaml.safe_load.",
         sample="Stages: Build (3 steps), Security (3 steps)\nTrigger: ['main']",
         hints=["PublishTestResults should run even if tests fail: condition: always()."]),
    dict(title="Boards Backlog", level="Stretch", concepts="Azure Boards, user stories",
         text="Write 6 user stories for SmartDesk with acceptance criteria, group them into 2 sprints, and mark one as "
              "a bug and one as a security task. If you have Azure DevOps access, enter them in Boards.",
         sample="As an agent, I want to filter tickets by priority so that I can focus on urgent work.\n"
                "Acceptance: filter shows only matching tickets; clearing it shows all.",
         hints=["Use the format: As a ..., I want ..., so that ..."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "DevOps brings together development and ________.",
        "Automatically building and testing every change is called continuous ________.",
        "In continuous ________, every green build goes to production with no human step.",
        "Finding security problems early in the loop is called shifting ________.",
        "bandit is a ________ tool: it reads code without running it.",
        "pip-audit checks project ________ for known vulnerabilities.",
        "Azure App Service is an example of ________.",
        "Moving a VM to the cloud without changing the app is called ________.",
        "A container for related Azure resources is a resource ________.",
        "The Azure DevOps service that runs CI/CD is ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain the difference between continuous delivery and continuous deployment.",
        "Why should code written with OpenAI Codex go through the same security scans as your own code?",
        "When would you choose rehost, and when rebuild? Give a SmartDesk example.",
        "What happens when you delete a resource group, and why is that useful and dangerous?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "steps = ['lint OK', 'tests FAILED', 'package']\nfor s in steps:\n    print(s)\n    if 'FAILED' in s:\n"
        "        break",
        "import yaml\ncfg = yaml.safe_load('trigger: [main]\\nstages:\\n  - stage: Build\\n  - stage: Security')\n"
        "print(len(cfg['stages']), cfg['trigger'][0])",
        "import subprocess\nsubprocess.run(f'zip {name}.zip data', shell=True)\n"
        "# Which DevSecOps scan flags this line, and why?",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a minimal azure-pipelines.yml that triggers on main and runs pytest."),
        dict(q="Add a Security stage that runs bandit and pip-audit."),
        dict(q="Rewrite subprocess.run(f\"zip {name}.zip data\", shell=True) so bandit does not flag it."),
        dict(q="Write a Python function that returns True if a line looks like a hard-coded password or key."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="A local CI simulator, DevSecOps scans (SAST, dependencies, secrets), pipeline YAML with a "
                         "security stage, and cloud model practice", cells=[
    ("md", "## 1. Setup\nWe cannot create cloud resources from this notebook, so we simulate a CI pipeline locally and "
           "prepare the files you push to Azure DevOps in the browser."),
    ("code", '''# ===== Option A: Google Colab (active) =====
!pip install -q pytest ruff bandit pip-audit pyyaml openai tiktoken scikit-learn

# ===== Option B: VS Code / local =====
# pip install pytest ruff bandit pip-audit pyyaml openai tiktoken scikit-learn   (in your activated venv)
import os
os.makedirs("ci_demo", exist_ok=True)
os.chdir("ci_demo")
print("Working in", os.getcwd())'''),
    ("md", "## 2. A tiny project to build and test"),
    ("code", '''%%writefile calc.py
def add(a, b):
    return a + b


def discount(price, pct):
    if not 0 <= pct <= 100:
        raise ValueError("pct must be 0 to 100")
    return round(price * (1 - pct / 100), 2)'''),
    ("code", '''%%writefile test_calc.py
import pytest

from calc import add, discount


def test_add():
    assert add(2, 3) == 5


def test_discount():
    assert discount(200, 10) == 180.0


def test_bad_discount():
    with pytest.raises(ValueError):
        discount(100, 120)'''),
    ("code", '''%%writefile requirements.txt
fastapi==0.115.0
pyyaml==6.0.2'''),
    ("md", "## 3. A local CI simulator\nEach step is a shell command. The pipeline stops at the first failure, just like "
           "Azure Pipelines."),
    ("code", '''import subprocess, time, zipfile, glob, shutil

def run_pipeline(steps):
    shutil.rmtree("__pycache__", ignore_errors=True)   # a CI agent always starts clean, so do we
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    start = time.perf_counter()
    for i, (name, cmd) in enumerate(steps, 1):
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env)
        status = "OK" if r.returncode == 0 else "FAILED"
        print(f"[{i}/{len(steps)}] {name:<14} ... {status}")
        if r.returncode != 0:
            print((r.stdout + r.stderr)[-800:])
            print("Pipeline stopped. Fix the problem and push again.")
            return False
    print(f"Pipeline succeeded in {time.perf_counter() - start:.1f} s")
    return True

def package():
    with zipfile.ZipFile("app.zip", "w") as z:
        for f in glob.glob("*.py") + ["requirements.txt"]:
            if not f.startswith("test_"):
                z.write(f)
    return "app.zip"

STEPS = [
    ("Lint", "ruff check --isolated calc.py test_calc.py"),
    ("Unit tests", "python -m pytest -q test_calc.py"),
]
if run_pipeline(STEPS):
    print("Artifact:", package())'''),
    ("md", "### Break it on purpose\nThis cell introduces a bug, runs the pipeline (it fails), then restores the file."),
    ("code", '''good = open("calc.py").read()
open("calc.py", "w").write(good.replace("return a + b", "return a - b"))
run_pipeline(STEPS)
open("calc.py", "w").write(good)
print("\\nBug fixed. Running again:")
_ = run_pipeline(STEPS)'''),
    ("md", "### TODO 1: Add a step that fails if any Python file is longer than 200 lines, and see it pass."),
    ("code", "# TODO: write your code here"),
    ("md", "## 4. NEW (v4): DevSecOps: SAST, dependency and secret scanning\nA small report module with three common "
           "problems. Imagine Codex wrote it quickly. The scans find what a quick read misses."),
    ("code", '''%%writefile report.py
import subprocess

DB_PASSWORD = "changeme123"          # hard-coded secret (demo only)


def export(name):
    subprocess.run(f"zip {name}.zip data", shell=True)


def total(expr):
    return eval(expr)'''),
    ("code", '''# SAST with bandit: -ll shows medium and high severity, -f txt for readable output
!bandit -q report.py || true'''),
    ("code", '''import re

SECRET_PATTERNS = [
    re.compile(r"(password|passwd|secret|api_key|token)\\s*=\\s*['\\"][^'\\"]{6,}['\\"]", re.I),
    re.compile(r"-----BEGIN (RSA |EC )?PRIVATE KEY-----"),
]

def scan_secrets(paths):
    findings = []
    for path in paths:
        for n, line in enumerate(open(path), 1):
            if any(p.search(line) for p in SECRET_PATTERNS):
                findings.append((path, n, line.strip()[:60]))
    return findings

for f in scan_secrets(glob.glob("*.py")):
    print("SECRET?", f)'''),
    ("code", '''# Dependency scanning needs the internet to download the vulnerability database.
!pip-audit -r requirements.txt || true''', ["skip-offline-check"]),
    ("md", "### Fix, then re-scan\nMove the secret to an environment variable, pass arguments as a list, and replace "
           "`eval` with a safe parser."),
    ("code", '''%%writefile report.py
import ast
import os
import subprocess

DB_PASSWORD = os.environ.get("DB_PASSWORD", "")   # read from the environment or a secret store


def export(name):
    subprocess.run(["zip", f"{name}.zip", "data"], check=False)


def total(expr):
    tree = ast.parse(expr, mode="eval")
    if not all(isinstance(n, (ast.Expression, ast.BinOp, ast.Constant, ast.Add, ast.Sub, ast.Mult, ast.Div))
               for n in ast.walk(tree)):
        raise ValueError("only arithmetic is allowed")
    return eval(compile(tree, "<expr>", "eval"), {"__builtins__": {}})  # nosec B307: input checked above'''),
    ("code", '''!bandit -q -ll report.py && echo "bandit: no medium or high issues"
print("secrets:", scan_secrets(["report.py"]) or "none found")'''),
    ("md", "Notice the `# nosec` comment: it records **why** a finding is accepted. Never add it just to turn CI green. "
           "The remaining low-severity note on `subprocess` is reviewed and accepted."),
    ("md", "### Explain a finding in plain English\nUseful when you write the vulnerability report. Runs offline too."),
    ("helpers",),
    ("code", '''finding = "B602 subprocess_popen_with_shell_equals_true, severity High, report.py line 7"
print(llm(f"Explain this bandit finding to a junior developer in two sentences, then give the fix: {finding}"))'''),
    ("md", "## 5. The pipeline file for Azure DevOps, with a security stage"),
    ("code", '''%%writefile azure-pipelines.yml
trigger:
  - main
pr:
  - main

pool:
  vmImage: ubuntu-latest

stages:
  - stage: Build
    jobs:
      - job: test
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: "3.12"
            displayName: Use Python 3.12
          - script: pip install -r requirements.txt pytest ruff
            displayName: Install dependencies
          - script: ruff check .
            displayName: Lint
          - script: python -m pytest -q --junitxml=test-results.xml
            displayName: Run tests
          - task: PublishTestResults@2
            condition: always()
            inputs:
              testResultsFiles: test-results.xml
            displayName: Publish test results

  - stage: Security
    dependsOn: Build
    jobs:
      - job: scan
        steps:
          - script: pip install bandit pip-audit
            displayName: Install scanners
          - script: bandit -r . -ll
            displayName: SAST (bandit)
          - script: pip-audit -r requirements.txt
            displayName: Dependency scan (pip-audit)'''),
    ("code", '''import yaml
cfg = yaml.safe_load(open("azure-pipelines.yml"))
print("Trigger:", cfg["trigger"], "| PR:", cfg["pr"])
print("Agent:", cfg["pool"]["vmImage"])
for stage in cfg["stages"]:
    steps = stage["jobs"][0]["steps"]
    print(f"Stage {stage['stage']}:")
    for i, step in enumerate(steps, 1):
        kind = "task" if "task" in step else "script"
        print(f"   {i}. {step['displayName']}  ({kind})")'''),
    ("md", "**TODO (SmartDesk step 15):** add a secret-scanning step to the Security stage and explain each stage in "
           "one sentence."),
    ("md", "## 6. Cloud models and migration paths: quick check"),
    ("code", '''scenarios = {
    "Legacy app that needs a custom Windows driver": "IaaS",
    "FastAPI service the team just wants to deploy": "PaaS",
    "Company email and documents": "SaaS",
    "Managed relational database nobody wants to patch": "PaaS",
    "Full control of a GPU machine with custom drivers": "IaaS",
}
my_answers = {   # TODO: change these to your own answers, then run
    "Legacy app that needs a custom Windows driver": "IaaS",
    "FastAPI service the team just wants to deploy": "PaaS",
    "Company email and documents": "SaaS",
    "Managed relational database nobody wants to patch": "IaaS",
    "Full control of a GPU machine with custom drivers": "IaaS",
}
score = sum(my_answers[s] == m for s, m in scenarios.items())
for s, m in scenarios.items():
    mark = "correct" if my_answers[s] == m else f"expected {m}"
    print(f"- {s}: {my_answers[s]} ({mark})")
print(f"Score: {score}/{len(scenarios)}")

PATHS = ["rehost", "replatform", "refactor", "rearchitect", "rebuild", "replace"]
migrations = {"Old ticketing server, no time to change code": "rehost",
              "Same app, but move its database to Azure SQL": "replatform",
              "Rewrite the reporting tool as FastAPI + React": "rebuild",
              "Switch to a SaaS helpdesk product": "replace"}
for case, path in migrations.items():
    print(f"{path:<11} (step {PATHS.index(path) + 1} of 6)  {case}")'''),
    ("md", "## 7. Azure in the browser\nOpen portal.azure.com with the program subscription. Create a resource group "
           "named `rg-day17-yourname` in the region your trainer gives you, add tags `owner` and `project`, look at the "
           "Overview page, then **delete it**. Then open dev.azure.com, create a user story in Boards and a new "
           "pipeline from the YAML above. No local Azure tools are needed."),
])
