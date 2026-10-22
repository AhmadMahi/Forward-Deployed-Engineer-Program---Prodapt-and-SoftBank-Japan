"""Day 20 spec. Git, CI/CD and Docker.
Source: archive/v1-40-day/Day18 + Day19 Session 1 (cloud-ready apps, compose, containerising front and back end).
NEW (v4) topics are marked.
"""
DAY = 20
FOLDER = "Day20-Git-CI-CD-and-Docker"
SLUG = "Git_CI_CD_and_Docker"
TITLE = "Git, CI/CD and Docker"
SUBTITLE = "Azure Repos, pipelines with security gates, AI pull request review, hardened Docker images, and containerising the full stack"
DATE = "Mon 23 Nov 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 21: Azure deployment and continuous delivery."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 18"),
        ("Git and Azure Repos (1 hr)", "Commits, branches, pull requests"),
        ("Pipelines (2 hrs)", "YAML, security gates, AI PR review. NEW (v4)"),
        ("Docker (2 hrs)", "Images, Dockerfiles, hardening. NEW (v4)"),
        ("Full stack (1.5 hrs)", "Containerise back end and front end"),
        ("SmartDesk", "Images, CI gates, vulnerability report v2"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Use Git daily", "Commit, branch, merge, resolve a conflict and open a pull request."),
        ("Gate every change", "Write pipeline YAML that fails on tests, bandit, pip-audit or a leaked secret."),
        ("Review safely", "Use Codex as a pull request reviewer while a human approves the merge."),
        ("Ship hardened images", "Write slim, non-root, scanned images for the API and the React app."),
    ]),

    dict(type="section", title="Git and Azure Repos", sub="Session 1 (1 hr). A time machine for your code"),
    dict(type="flow", title="The places your code lives", items=[
        ("Working folder", "Files you edit"),
        ("Staging area", "git add: chosen changes"),
        ("Repository", "git commit: saved snapshot"),
        ("Remote", "git push: shared with the team"),
    ]),
    dict(type="table", title="Commands you will use every day", header=["Command", "What it does"], rows=[
        ["git status", "What changed and what is staged"],
        ["git add file / git add .", "Stage changes for the next commit"],
        ["git commit -m \"message\"", "Save a snapshot with a message"],
        ["git switch -c feature/x", "Create and move to a new branch"],
        ["git pull / git push", "Get or send commits to the remote"],
        ["git log --oneline", "Short history of commits"],
    ]),
    dict(type="bullets_code", title="Merging and conflicts", greet="Kyouryoku (協力): Cooperation", bullets=[
        "Merge brings a branch's commits into main",
        "Conflict: both sides changed the same lines",
        "Git marks both versions in the file",
        "Choose, delete markers, add, commit",
    ], code='''git switch main
git merge feature/greeting

# CONFLICT in app.py
<<<<<<< HEAD
greeting = "Hello"
=======
greeting = "Konnichiwa"
>>>>>>> feature/greeting

# edit to the final version, then:
git add app.py
git commit -m "Resolve greeting conflict"'''),
    dict(type="flow", title="A pull request workflow in Azure Repos", items=[
        ("Branch", "feature/add-filter"),
        ("Push", "git push -u origin feature/add-filter"),
        ("Open PR", "Describe what and why"),
        ("Checks", "CI and security gates run"),
        ("Merge", "After human approval"),
    ], note="Branch policies on main can require a green build and at least one human reviewer."),

    dict(type="section", title="Azure Pipelines and security gates", sub="Session 2 (2 hrs). Stages, jobs, steps, and gates that stop bad code"),
    dict(type="table", title="Pipeline building blocks", header=["Level", "Contains", "Example"], rows=[
        ["Pipeline", "One or more stages", "azure-pipelines.yml"],
        ["Stage", "Jobs; can depend on other stages", "Test, Security, Docker"],
        ["Job", "Steps that run on one agent", "unit_tests"],
        ["Step", "A script or a task", "pytest -q, Docker@2"],
    ], note="Triggers decide when it runs: trigger for pushes to main, pr for pull requests."),
    dict(type="cards", title="Security gates in CI", new=True, items=[
        ("SAST: bandit", "Scans Python code for insecure patterns such as shell=True or hard-coded passwords."),
        ("Dependencies: pip-audit", "Checks pinned packages against known vulnerabilities (npm audit for Node)."),
        ("Secret scanning", "Finds keys and passwords in files and Git history before they leave the laptop."),
        ("Image scanning", "Scans the built image for vulnerable OS packages (for example Trivy)."),
    ], note="A gate is a step that fails the pipeline. Warnings that never fail are easy to ignore."),
    dict(type="code", title="A pipeline with a Security stage", new=True, code='''stages:
- stage: Test
  jobs:
  - job: unit
    steps:
    - script: pip install -r requirements.txt pytest ruff
    - script: ruff check . && pytest -q
- stage: Security
  dependsOn: Test
  jobs:
  - job: scan
    steps:
    - script: pip install bandit pip-audit
    - script: bandit -r app -ll          # fail on medium and high
    - script: pip-audit -r requirements.txt
    - script: python tools/scan_secrets.py   # exit 1 on any hit
- stage: Docker
  dependsOn: Security
  condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')'''),
    dict(type="flow", title="Fail, remediate, re-run", new=True, items=[
        ("Fail", "Gate goes red on a finding"),
        ("Triage", "Real issue or false positive?"),
        ("Remediate", "Fix code or upgrade package"),
        ("Prove", "Add a test for the fix"),
        ("Re-run", "Gate goes green; log it"),
    ], note="Suppress a finding only with a written reason (for example # nosec B101 with a comment)."),
    dict(type="table", title="Vulnerability report v2", new=True,
         header=["ID", "Finding", "Tool", "Severity", "Fix", "Fixed by", "Verified"], rows=[
        ["V-01", "subprocess with shell=True", "bandit", "High", "Pass a list, no shell", "Codex-assisted", "Yes"],
        ["V-02", "requests 2.19.0", "pip-audit", "Medium", "Upgrade to 2.20.0 or later", "Human", "Yes"],
        ["V-03", "API key in config.py", "secret scan", "High", "Revoke, rotate, env var", "Human", "Yes"],
    ], note="Template: shared/templates/Vulnerability_Report_Template.md. v1 was Day 7; v3 comes on Day 30."),
    dict(type="compare", title="AI pull request review with Codex", new=True, left=dict(title="Codex does", bullets=[
        "Reads the diff and explains it", "Flags bugs, missing tests, risky patterns",
        "Suggests changes as comments", "Saves reviewer time on routine checks",
    ]), right=dict(title="The human does", bullets=[
        "Decides if the change is right for the product", "Checks every Codex suggestion before accepting",
        "Approves the merge (branch policy)", "Owns the outcome",
    ]), note="Codex is a reviewer, never the approver. No secrets or customer data in review prompts."),
    dict(type="cards", title="A good pull request", items=[
        ("Small", "One idea per PR. Easier to review, faster to merge."),
        ("Explained", "What changed, why, and how to test it."),
        ("Green", "Tests and security gates pass before you ask for review."),
        ("Kind reviews", "Comment on code, not people. Suggest, do not command."),
    ]),

    dict(type="section", title="Docker", sub="Session 3 (2 hrs). It works on my machine, and on every machine"),
    dict(type="table", title="Docker vocabulary", header=["Term", "Meaning", "Analogy"], rows=[
        ["Dockerfile", "Recipe to build an image", "A recipe card"],
        ["Image", "Read-only package built from the recipe", "A frozen meal"],
        ["Container", "A running instance of an image", "The meal being eaten"],
        ["Registry", "Storage for images (ACR, Docker Hub)", "The freezer shop"],
    ]),
    dict(type="bullets_code", title="A Dockerfile for FastAPI", greet="Junbi (準備): Preparation", bullets=[
        "Start from a small official base image",
        "Copy requirements first for caching",
        "Then copy the code",
        "CMD starts the server on port 8000",
    ], code='''FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app",
     "--host", "0.0.0.0", "--port", "8000"]'''),
    dict(type="bullets_code", title="Build, run, inspect", bullets=[
        "build creates an image from the Dockerfile",
        "-p maps laptop port to container port",
        "logs and ps help debugging",
        ".dockerignore keeps images small",
    ], code='''docker build -t tasks-api:1.0 .
docker run -d -p 8000:8000 \\
  --name tasks tasks-api:1.0

docker ps
docker logs tasks
curl http://localhost:8000/health

docker stop tasks && docker rm tasks'''),
    dict(type="cards", title="Image hardening", new=True, greet="Anzen (安全): Safety", items=[
        ("Small base image", "slim or distroless: fewer packages, fewer vulnerabilities."),
        ("Non-root user", "If the app is broken into, the attacker is not root."),
        ("No secrets in layers", "Secrets come from the platform at runtime, never COPY or ENV."),
        ("Pin and scan", "Pin versions; scan the image in CI and fail on high findings."),
    ]),
    dict(type="bullets_code", title="A hardened Dockerfile", new=True, bullets=[
        "Pinned slim base",
        "No pip cache, no build tools left behind",
        "Runs as appuser, not root",
        "HEALTHCHECK runs check.py, which calls /health",
    ], code='''FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir \\
    -r requirements.txt
COPY app/ ./app
RUN useradd -m -u 10001 appuser
USER appuser
EXPOSE 8000
HEALTHCHECK CMD python /app/app/check.py
CMD ["uvicorn", "app.main:app",
     "--host", "0.0.0.0", "--port", "8000"]'''),

    dict(type="section", title="Containerising back end and front end", sub="Session 4 (1.5 hrs). The same image in every environment"),
    dict(type="cards", title="Habits of a cloud-ready app", lead="Build once, deploy the same image everywhere with different settings.", items=[
        ("Config from env", "URLs, secrets and flags come from environment variables."),
        ("Stateless", "No files or sessions stored inside the container."),
        ("Health endpoints", "/health says alive; /ready says able to serve."),
        ("Logs to stdout", "Print logs; the platform collects them."),
    ]),
    dict(type="bullets_code", title="Multi-stage build for the React front end", bullets=[
        "Stage 1 builds with Node",
        "Stage 2 serves static files with nginx",
        "Only the built files ship",
        "No API keys in front-end builds (Day 11 rule)",
    ], code='''FROM node:22-slim AS build
WORKDIR /web
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /web/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80'''),
    dict(type="bullets_code", title="docker compose: the full local stack", bullets=[
        "One file describes several services",
        "Services reach each other by name",
        "Volumes keep database data",
        "One command starts everything",
    ], code='''services:
  api:
    build: ./api
    ports: ["8000:8000"]
    environment:
      APP_ENV: local
      MONGO_URI: mongodb://db:27017
    depends_on: [db]
  web:
    build: ./web
    ports: ["8080:80"]
    depends_on: [api]
  db:
    image: mongo:7
    volumes: ["mongo-data:/data/db"]
volumes:
  mongo-data:'''),
    dict(type="cards", title="SmartDesk step 17: images and CI gates", items=[
        ("Images", "Hardened images for the SmartDesk API and dashboard."),
        ("CI gates", "Test, bandit, pip-audit, npm audit and secret scan in the pipeline."),
        ("Report v2", "Scan before and after fixes; log each finding in the template."),
        ("Build with Codex", "Use Day20_App_Build_Prompts.md. A human approves every merge."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("Git", "add, commit, branch, merge. Small, explained pull requests."),
        ("Gates", "Tests, SAST, dependency and secret scans fail the build. Fix, prove, re-run."),
        ("AI review", "Codex comments; a human approves."),
        ("Docker", "Slim, non-root, scanned images. Same image everywhere."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day20_Hotel_Lab.md: Git, Docker, gates, report v2."),
        ("Workbook", "Complete the Day 20 workbook."),
        ("Pre-read", "Skim the Day 21 pre-read on deploying to Azure."),
    ]),
]

PREREAD = dict(title="Saving Versions and Packing Boxes", lede="A light read before Day 20. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "Tomorrow you learn tools every software team uses daily: Git to track changes, pipelines to check them "
        "automatically, and Docker to package an app so it runs the same everywhere. You also add security checks that "
        "stop unsafe code before it ships."]),
    dict(h="1. Git: save points for your work", paras=[
        "Video games let you save progress so you can go back if something goes wrong. Git gives your code save "
        "points, called **commits**. Each one records what changed, who changed it and why."]),
    dict(h="2. Branches: parallel drafts", paras=[
        "When several people edit one document at the same time, it gets messy. Instead, each person works on their "
        "own copy, then the changes are carefully combined. In Git these copies are **branches**, and the request to "
        "combine them is a **pull request**, where teammates review the work first."],
        box="**Key idea:** the main branch should always work. New work happens on branches and is reviewed before joining main."),
    dict(h="3. Security guards at the door", new=True, paras=[
        "A pipeline runs checks every time someone pushes code. Some checks are guards: one looks for risky code, one "
        "checks that the libraries you use have no known holes, and one looks for passwords left in files. If a guard "
        "finds a problem, the door stays shut until it is fixed. An AI reviewer such as OpenAI Codex can leave helpful "
        "comments, but a person still decides to open the door."]),
    dict(h="4. Docker: packing the whole kitchen", paras=[
        "Imagine shipping a recipe to a friend abroad. Their oven and ingredients are different, so the dish turns out "
        "differently. Now imagine shipping a sealed box containing the dish, the ingredients and the oven. That is a "
        "**container**. It runs the same on your laptop, a test server or the cloud."],
        table=[["Docker word", "Plain meaning"], ["Dockerfile", "The recipe: step-by-step instructions to build the box"],
               ["Image", "The sealed box, built from the recipe"], ["Container", "The box opened and running"],
               ["Registry", "A warehouse that stores boxes so others can use them"]]),
    dict(h="5. A smaller box is a safer box", new=True, paras=[
        "Every extra item in the box is something that could break or be attacked. Good teams pack only what the app "
        "needs, and the app inside does not run with the master key (the root user)."]),
    dict(h="6. Think about these before class", bullets=[
        "Have you ever lost work because a file was overwritten? How would save points have helped?",
        "Why is a password in a code file dangerous even if the repository is private?",
        "Why might software that works on your laptop fail on someone else's?"],
        after=["Before class: install Git and Docker Desktop (see shared/Laptop_Setup_Guide.pdf). Junbi (準備): preparation"]),
])

POSTREAD = dict(title="Git, Pipelines and Docker: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Git areas", "Working folder, staging (git add), repository (git commit), remote (git push)."],
        ["Branches and PRs", "One branch per task; small, explained, green PRs; branch policies protect main."],
        ["Pipeline levels", "Pipeline, stages, jobs, steps. dependsOn for order; condition for main only."],
        ["Security gates (NEW v4)", "bandit (SAST), pip-audit and npm audit (dependencies), secret scan, image scan."],
        ["Fail, remediate, re-run (NEW v4)", "Triage, fix, prove with a test, re-run, log in vulnerability report v2."],
        ["AI PR review (NEW v4)", "Codex comments on the diff; a human approves the merge."],
        ["Docker terms", "Dockerfile (recipe), image (package), container (running), registry (storage)."],
        ["Image hardening (NEW v4)", "Slim base, non-root user, no secrets in layers, pinned versions, scanned in CI."],
        ["Full stack in containers", "Env config, /health and /ready, multi-stage React build, docker compose."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Good commit messages", paras=[
        "A short summary line, a blank line, then why. Your future self will thank you."],
        code="Add priority filter to ticket list\n\nAgents asked to focus on urgent work. Adds ?priority= to GET /tickets\nand a dropdown in the dashboard. Closes #42."),
    dict(sub="2. Layer caching", paras=[
        "Docker caches each instruction. Copy requirements.txt and install before copying code, so code edits do not "
        "reinstall every package. Builds go from minutes to seconds."]),
    dict(sub="3. Pre-commit hooks", paras=[
        "Run ruff and a secret scan on your laptop before every commit. A secret that never reaches the remote never "
        "needs rotating."]),
    dict(sub="4. A leaked secret is a burnt secret", paras=[
        "Deleting a key from the latest commit is not enough: it stays in history and may already be copied. Revoke "
        "and rotate it first, then clean up."]),
    dict(sub="5. Pipeline templates and variables", paras=[
        "Large teams reuse steps with templates and keep settings in variable groups, with secrets linked from Azure "
        "Key Vault. You meet Key Vault tomorrow."]),
    dict(h="Part C: Check yourself", bullets=[
        "What is the difference between git add and git commit?",
        "Name the four security gates from today and what each one catches.",
        "Why must a human, not Codex, approve the merge?",
        "Name three ways to harden a Docker image.",
        "What does -p 8000:8000 mean in docker run?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add a .dockerignore and compare image sizes before and after.",
        "Plant a fake key in a practice repo and make your secret scanner fail the build.",
        "Ask Codex to review one of your own pull requests and list which comments you accepted and why."],
        after=["**Coming up on Day 21:** Azure App Service, Container Apps, continuous delivery, Key Vault and managed identity.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems. Git and the security scanners run in Colab and VS Code. Docker commands need "
                    "Docker Desktop on your laptop.", problems=[
    dict(title="Feature Branch and Merge", level="Warm-up", concepts="init, add, commit, switch, merge",
         text="Create a repo for your Task API, make two commits, create feature/health-check, add a /health endpoint, "
              "commit, merge into main, and delete the branch.",
         sample="Fast-forward\n app/main.py | 4 ++++\nDeleted branch feature/health-check\n"
                "b2c3d4e Add health check endpoint\na1b2c3d Initial FastAPI app",
         hints=["git config user.name and user.email first.", "git branch -d feature/health-check"]),
    dict(title="Resolve a Conflict", level="Easy", concepts="merge conflicts",
         text="Change the same line on two branches, merge them, resolve the conflict by keeping a combined version, "
              "and commit.",
         sample="CONFLICT (content): Merge conflict in greeting.py\n... after fix ...\n[main 7c1d2e3] Resolve greeting conflict",
         hints=["Search the file for <<<<<<< and >>>>>>> markers."]),
    dict(title="Make the Security Gate Fail", level="Medium", concepts="bandit, gates, exit codes", new=True,
         text="Run bandit on the deliberately unsafe app in the notebook. Write gate(findings) that returns exit code 1 "
              "if any finding is medium or high. Fix each finding, re-run, and show the gate pass.",
         sample="Run 1: 5 findings, 3 blocking (HIGH 2, MEDIUM 1) -> gate FAIL\nRun 2: 3 LOW, 0 blocking -> gate PASS",
         hints=["bandit -f json gives machine-readable output.", "Fix the code; do not just add # nosec."]),
    dict(title="Secret Scanner", level="Medium", concepts="regex, Git history", new=True,
         text="Write scan_secrets(path) that flags API key and password patterns in files, and run it on a repo where a "
              "key was committed and then deleted. Show that the key is still in git log -p.",
         sample="config.py:3  possible API key\nhistory: commit 4f2a1c0 adds API_KEY=... (still recoverable)",
         hints=["Revoke and rotate first. Cleaning history comes second."]),
    dict(title="Vulnerability Report v2", level="Medium", concepts="triage, remediation, evidence", new=True,
         text="Fill the vulnerability report template for every finding from bandit, pip-audit and the secret scan: "
              "ID, finding, tool, severity, file, proposed fix, fixed by (human or Codex-assisted), verified, evidence. "
              "Include scan output before and after the fixes.",
         sample="| V-01 | shell=True in run_report | bandit | High | app/main.py | list args | Codex-assisted | Yes | run 2 clean |",
         hints=["Use shared/templates/Vulnerability_Report_Template.md.", "pip-audit needs internet; run it in Colab or VS Code."]),
    dict(title="Codex as Reviewer", level="Challenging", concepts="AI pull request review, human approval", new=True,
         text="Open a pull request with one deliberate bug and one missing test. Ask Codex in VS Code to review the diff "
              "using the review prompt in the notebook. Record each comment as accepted or rejected with a reason, then "
              "approve or request changes yourself.",
         sample="Comment 1: missing test for empty title  -> accepted, test added\n"
                "Comment 2: rename variable x            -> rejected, out of scope\nDecision: approved by human reviewer",
         hints=["Paste only the diff, never secrets or customer data."]),
    dict(title="Smaller and Safer Image", level="Stretch", concepts="slim images, non-root user, scanning", new=True,
         text="Write a hardened Dockerfile for the Task API and a multi-stage Dockerfile for the React app. Compare "
              "docker images sizes before and after, confirm the container runs as a non-root user, and scan the image.",
         sample="tasks-api:1.0 1.1GB (root)\ntasks-api:1.1 190MB (uid 10001)\nimage scan: 0 critical, 0 high",
         hints=["docker run --rm tasks-api:1.1 id", "Image scanners include Trivy and Docker Scout."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "The command that stages changes is git ________.",
        "To create and switch to a new branch, use git switch ________ feature/x.",
        "A request to merge a branch after review is a ________ request.",
        "In Azure Pipelines, stages contain ________, which contain steps.",
        "bandit is a ________ tool: it scans source code without running it.",
        "pip-audit checks installed ________ for known vulnerabilities.",
        "A step that fails the pipeline when a check fails is called a ________.",
        "Codex can review a pull request, but a ________ approves the merge.",
        "The recipe for building a Docker image is the ________.",
        "Hardened images run as a non-________ user.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain working folder, staging area, repository and remote.",
        "Describe the fail, remediate, re-run loop for a bandit finding.",
        "What should you do first when a secret scanner finds a real API key in Git history, and why?",
        "Give three reasons a slim, non-root image is safer.",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "import yaml\np = yaml.safe_load(\"stages:\\n- stage: Test\\n- stage: Security\\n  dependsOn: Test\")\n"
        "print([s[\"stage\"] for s in p[\"stages\"]], p[\"stages\"][1][\"dependsOn\"])",
        "findings = [{\"sev\": \"LOW\"}, {\"sev\": \"MEDIUM\"}]\nblock = {\"MEDIUM\", \"HIGH\"}\n"
        "print(\"FAIL\" if any(f[\"sev\"] in block for f in findings) else \"PASS\")",
        "lines = [\"FROM python:3.12-slim\", \"RUN useradd -m appuser\", \"USER appuser\"]\n"
        "print(any(l.startswith(\"USER\") and \"root\" not in l for l in lines))",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write the Git commands to create a branch, commit a change and push it."),
        dict(q="Write a Security stage in azure-pipelines.yml that runs bandit, pip-audit and a secret scan."),
        dict(q="Write a hardened Dockerfile for a FastAPI app in app/main.py."),
        dict(q="Write a docker-compose.yml with api, web and db services."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="Git, pipelines with security gates, AI pull request review, hardened images and the full stack in containers", cells=[
    ("md", "## 1. Setup\nGit is installed in Colab. Docker is not, so Docker commands are for VS Code with Docker Desktop. "
           "The security scanners (bandit, pip-audit) run in both."),
    ("code", '''# ===== Option A: Google Colab (active) =====
!git --version
!pip install -q pyyaml bandit pip-audit fastapi httpx

# ===== Option B: VS Code / local =====
# Install Git and Docker Desktop (see shared/Laptop_Setup_Guide.pdf), then:
# pip install pyyaml bandit pip-audit fastapi httpx
import os, shutil
shutil.rmtree("tasks-api", ignore_errors=True)
os.makedirs("tasks-api/app", exist_ok=True)
os.chdir("tasks-api")
print("Working in", os.getcwd())'''),
    ("helpers",),
    ("md", "## 2. A small app to version"),
    ("code", '''%%writefile app/main.py
from fastapi import FastAPI

app = FastAPI(title="Tasks API")
tasks = []

@app.get("/tasks")
def list_tasks():
    return tasks'''),
    ("code", '''%%writefile requirements.txt
fastapi==0.115.0
uvicorn==0.30.6'''),
    ("md", "## 3. First commits, a feature branch and a merge"),
    ("code", '''# ===== Option A: Google Colab (active) =====
!git init -q -b main
!git config user.name "Learner" && git config user.email "learner@example.com"
!git add . && git commit -q -m "Initial FastAPI app"
!git switch -q -c feature/health-check
!printf '\\n@app.get("/health")\\ndef health():\\n    return {"status": "ok"}\\n' >> app/main.py
!git add app/main.py && git commit -q -m "Add health check endpoint"
!git switch -q main && git merge -q feature/health-check && git branch -d feature/health-check
!git log --oneline

# ===== Option B: VS Code terminal =====
# Same commands without the "!" at the start.'''),
    ("md", "## 4. A merge conflict, resolved"),
    ("code", '''!echo 'greeting = "Hello"' > greeting.py && git add . && git commit -q -m "Add greeting"
!git switch -q -c feature/japanese
!echo 'greeting = "Konnichiwa"' > greeting.py && git commit -q -am "Japanese greeting"
!git switch -q main
!echo 'greeting = "Namaste"' > greeting.py && git commit -q -am "Hindi greeting"
!git merge feature/japanese || true
!cat greeting.py'''),
    ("code", '''# Resolve: keep both greetings, remove the markers
open("greeting.py", "w").write('greetings = ["Namaste", "Konnichiwa"]\\n')
!git add greeting.py && git commit -q -m "Resolve greeting conflict: keep both"
!git log --oneline --graph | head -8'''),
    ("md", "### TODO 1: Create a branch `feature/count`, add a `GET /tasks/count` endpoint, commit, and merge it into main."),
    ("code", "# TODO: write your code here"),
    ("md", "## 5. Push to Azure Repos (VS Code)\nCreate an empty repo in Azure DevOps first. Never paste tokens into a notebook."),
    ("code", '''# ===== Option B: VS Code terminal (recommended) =====
# git remote add origin https://dev.azure.com/<org>/<project>/_git/tasks-api
# git push -u origin main
# git switch -c feature/priority-filter
# ...commit...
# git push -u origin feature/priority-filter
# Then open a pull request: Repos > Pull requests > New pull request
print("Remote commands are listed above")''', ["skip-offline-check"]),
    ("md", "## 6. NEW (v4): Security gates\nWe add a deliberately unsafe report feature, scan it with **bandit**, fail the "
           "gate, fix the code, and re-run. Never write code like `unsafe_report.py` in real work."),
    ("code", '''%%writefile app/unsafe_report.py
import hashlib
import subprocess
import yaml

DB_PASSWORD = "admin123"                      # hard-coded password

def run_report(name):
    return subprocess.run(f"echo report {name}", shell=True, capture_output=True)   # shell injection risk

def load_settings(text):
    return yaml.load(text, Loader=yaml.Loader)   # unsafe loader

def ticket_hash(ticket_id):
    return hashlib.md5(str(ticket_id).encode()).hexdigest()   # weak hash'''),
    ("code", '''import json, subprocess

BLOCK = {"MEDIUM", "HIGH"}

def run_bandit(path="app"):
    r = subprocess.run(["bandit", "-r", path, "-f", "json", "-q"], capture_output=True, text=True)
    data = json.loads(r.stdout or "{}")
    return [{"id": x["test_id"], "issue": x["issue_text"], "severity": x["issue_severity"],
             "file": x["filename"], "line": x["line_number"]} for x in data.get("results", [])]

def gate(findings, name="bandit"):
    bad = [f for f in findings if f["severity"] in BLOCK]
    status = "FAIL" if bad else "PASS"
    print(f"{name} gate: {status} ({len(bad)} blocking of {len(findings)} findings)")
    return 1 if bad else 0

run1 = run_bandit()
for f in run1:
    print(f"{f['severity']:<7} {f['id']}  {f['file']}:{f['line']}  {f['issue']}")
exit_code = gate(run1)'''),
    ("md", "### Remediate\nEach fix removes the risky pattern rather than hiding it with `# nosec`."),
    ("code", '''%%writefile app/unsafe_report.py
import hashlib
import os
import subprocess
import yaml

DB_PASSWORD = os.getenv("DB_PASSWORD", "")      # from the environment or Key Vault, never in code

def run_report(name):
    return subprocess.run(["echo", "report", name], capture_output=True)   # list of args, no shell

def load_settings(text):
    return yaml.safe_load(text)                     # safe loader

def ticket_hash(ticket_id):
    return hashlib.sha256(str(ticket_id).encode()).hexdigest()'''),
    ("code", '''run2 = run_bandit()
for f in run2:
    print(f"{f['severity']:<7} {f['id']}  {f['issue']}")
exit_code = gate(run2)'''),
    ("md", "### Dependency scanning with pip-audit\n`pip-audit` needs internet to query the vulnerability database, so "
           "the live cell is skipped in the offline check. The next cell parses a **sample** report in pip-audit's "
           "JSON shape so the gate logic still runs offline."),
    ("code", '''%%writefile requirements-old.txt
requests==2.19.0'''),
    ("code", '''# Live scan (needs internet)
!pip-audit -r requirements-old.txt --format json -o audit.json || true
!cat audit.json | head -c 600''', ["skip-offline-check"]),
    ("code", '''# SAMPLE output in pip-audit's JSON shape (for offline practice). CVE-2018-18074 affects requests before 2.20.0.
sample_audit = {"dependencies": [{"name": "requests", "version": "2.19.0", "vulns": [
    {"id": "PYSEC-2018-28", "aliases": ["CVE-2018-18074"], "fix_versions": ["2.20.0"],
     "description": "Authorization header sent on HTTPS to HTTP redirect."}]}]}

def audit_findings(report):
    return [{"package": d["name"], "version": d["version"], "id": v["id"], "fix": ", ".join(v["fix_versions"]),
             "severity": "MEDIUM"} for d in report["dependencies"] for v in d["vulns"]]

deps = audit_findings(sample_audit)
print(deps)
gate(deps, "pip-audit")'''),
    ("md", "### Secret scanning (files and Git history)"),
    ("code", '''import re, pathlib
SECRET = re.compile(r"(?i)(api[_-]?key|secret|password|token)\\s*=\\s*['\\"][^'\\"]{6,}['\\"]|sk-[A-Za-z0-9_-]{20,}")

def scan_secrets(root="."):
    hits = []
    for p in pathlib.Path(root).rglob("*.py"):
        for i, line in enumerate(p.read_text(errors="ignore").splitlines(), 1):
            if SECRET.search(line):
                hits.append(f"{p}:{i}  {line.strip()[:60]}")
    return hits

# Commit a fake key, then "delete" it
open("config.py", "w").write('API_KEY = "fake-key-for-training-123456"\\n')
!git add config.py && git commit -q -m "Add config"
open("config.py", "w").write('import os\\nAPI_KEY = os.getenv("API_KEY", "")\\n')
!git commit -q -am "Read key from environment"

print("Files now:", scan_secrets() or "clean")
history = subprocess.run(["git", "log", "-p", "--all"], capture_output=True, text=True).stdout
print("Still in history:", bool(re.search(r"fake-key-for-training", history)))
print("Lesson: revoke and rotate the key first. Deleting the line does not remove it from history.")'''),
    ("md", "### Vulnerability report v2\nBuild the report rows from the scan results. The full template is "
           "`shared/templates/Vulnerability_Report_Template.md`."),
    ("code", '''import pandas as pd
rows = []
fixes = {"B602": "Pass a list of args, no shell", "B105": "Read from env / Key Vault",
         "B506": "yaml.safe_load", "B324": "Use sha256"}
reportable = [f for f in run1 if f["severity"] in BLOCK or f["id"] == "B105"]   # B105: low score, real risk
for n, f in enumerate(reportable, 1):
    rows.append({"ID": f"V-{n:02d}", "Finding": f["issue"][:45], "Tool": "bandit", "Severity": f["severity"],
                 "File": f"{os.path.basename(f['file'])}:{f['line']}", "Proposed fix": fixes.get(f["id"], "Review"),
                 "Fixed by": "Human", "Verified": "Yes" if not [x for x in run2 if x["id"] == f["id"]] else "No",
                 "Evidence": "bandit run 2"})
for d in deps:
    rows.append({"ID": f"V-{len(rows) + 1:02d}", "Finding": f"{d['package']} {d['version']} {d['id']}", "Tool": "pip-audit",
                 "Severity": d["severity"], "File": "requirements-old.txt", "Proposed fix": f"Upgrade to {d['fix']}",
                 "Fixed by": "Human", "Verified": "No", "Evidence": "re-run pip-audit after upgrade"})
rows.append({"ID": f"V-{len(rows) + 1:02d}", "Finding": "API key committed in config.py", "Tool": "secret scan",
             "Severity": "HIGH", "File": "config.py", "Proposed fix": "Revoke, rotate, env var", "Fixed by": "Human",
             "Verified": "Yes", "Evidence": "scan clean; key rotated"})
report = pd.DataFrame(rows)
print(report.to_string(index=False))
report.to_csv("vulnerability_report_v2.csv", index=False)      # copy rows into the Markdown template'''),
    ("md", "## 7. NEW (v4): AI pull request review with Codex, human approval\nIn VS Code, paste the diff into Codex "
           "with the review prompt below. Here we show the same flow: get the diff, ask a reviewer (the LLM online, a "
           "rule-based stand-in offline), then a **human** decides."),
    ("code", '''!git switch -q -c feature/delete-task
open("app/main.py", "a").write("""
@app.delete("/tasks/{idx}")
def delete_task(idx: int):
    tasks.pop(idx)
    return {"deleted": idx}
""")
!git add app/main.py && git commit -q -m "Add delete endpoint"
diff = subprocess.run(["git", "diff", "main", "--", "app/main.py"], capture_output=True, text=True).stdout
print(diff)'''),
    ("code", '''REVIEW_PROMPT = """You are reviewing a pull request for a FastAPI service.
List up to 5 comments. For each: line, problem, suggested fix, severity (low, medium, high).
Check: bugs, missing tests, error handling, security. Do not approve or reject; a human decides.
Diff:
"""

def offline_review(diff):
    notes = []
    if ".pop(" in diff and "HTTPException" not in diff:
        notes.append("high: pop(idx) raises IndexError for a missing task; return 404 with HTTPException")
    if "def test_" not in diff:
        notes.append("medium: no test added for the new endpoint")
    if "@app.delete" in diff:
        notes.append("low: consider returning 204 No Content for deletes")
    return "\\n".join(f"- {n}" for n in notes)

review = llm(REVIEW_PROMPT + diff, temperature=0) if ONLINE else offline_review(diff)
print("Reviewer comments:\\n" + review)

decisions = {"404 for missing task": "accepted", "missing test": "accepted", "204 status": "rejected: keep 200 for now"}
print("\\nHuman decisions:", decisions)
print("Merge approved by: human reviewer (branch policy requires 1 approval)")'''),
    ("md", "## 8. A multi-stage pipeline with security gates"),
    ("code", '''%%writefile azure-pipelines.yml
trigger:
  - main

pr:
  - main

variables:
  imageName: tasks-api

stages:
  - stage: Test
    displayName: Lint and test
    jobs:
      - job: unit
        pool:
          vmImage: ubuntu-latest
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: "3.12"
          - script: pip install -r requirements.txt pytest httpx ruff
            displayName: Install
          - script: ruff check . && python -m pytest -q --junitxml=results.xml
            displayName: Lint and tests
          - task: PublishTestResults@2
            condition: always()
            inputs:
              testResultsFiles: results.xml

  - stage: Security
    displayName: Security gates
    dependsOn: Test
    jobs:
      - job: scan
        pool:
          vmImage: ubuntu-latest
        steps:
          - script: pip install bandit pip-audit
            displayName: Install scanners
          - script: bandit -r app -ll
            displayName: SAST (fails on medium and high)
          - script: pip-audit -r requirements.txt
            displayName: Dependency audit
          - script: python tools/scan_secrets.py
            displayName: Secret scan

  - stage: Docker
    displayName: Build and scan image
    dependsOn: Security
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - job: build
        pool:
          vmImage: ubuntu-latest
        steps:
          - script: docker build -t $(imageName):$(Build.BuildId) .
            displayName: docker build
          - script: trivy image --exit-code 1 --severity HIGH,CRITICAL $(imageName):$(Build.BuildId)
            displayName: Image scan (needs Trivy on the agent)'''),
    ("code", '''import yaml
p = yaml.safe_load(open("azure-pipelines.yml"))
for st in p["stages"]:
    steps = [s.get("displayName") or s.get("task") for j in st["jobs"] for s in j["steps"]]
    print(f"{st['stage']:<9} after {st.get('dependsOn', '-'):<9} steps={steps}")'''),
    ("md", "## 9. NEW (v4): Docker images, plain and hardened"),
    ("code", '''%%writefile Dockerfile.plain
FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV API_KEY=changeme
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]'''),
    ("code", '''%%writefile Dockerfile
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app
RUN useradd -m -u 10001 appuser
USER appuser
EXPOSE 8000
HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]'''),
    ("code", '''%%writefile .dockerignore
.git
__pycache__/
*.pyc
.venv/
.env
tests/
*.md'''),
    ("code", '''def lint_dockerfile(path):
    lines = [l.strip() for l in open(path) if l.strip() and not l.startswith("#")]
    text = "\\n".join(lines)
    checks = {
        "slim or pinned small base": any(l.startswith("FROM") and ("slim" in l or "alpine" in l or "distroless" in l) for l in lines),
        "runs as non-root user": any(l.startswith("USER") and "root" not in l for l in lines),
        "no secrets in ENV": not re.search(r"ENV .*(KEY|SECRET|PASSWORD)=", text, re.I),
        "copies requirements before code": text.find("requirements.txt") < text.find("COPY app"),
        "no pip cache": "--no-cache-dir" in text,
        "has HEALTHCHECK": "HEALTHCHECK" in text,
    }
    return checks

for f in ["Dockerfile.plain", "Dockerfile"]:
    c = lint_dockerfile(f)
    print(f"{f:<17} {sum(c.values())}/{len(c)} checks passed")
    for name, ok in c.items():
        if not ok:
            print("   missing:", name)'''),
    ("code", '''# ===== Option B: VS Code with Docker Desktop =====
# docker build -f Dockerfile.plain -t tasks-api:1.0 .
# docker build -t tasks-api:1.1 .
# docker images | grep tasks-api              # compare sizes
# docker run --rm tasks-api:1.1 id            # uid=10001(appuser), not root
# docker run -d -p 8000:8000 --name tasks tasks-api:1.1 && curl localhost:8000/health
# trivy image tasks-api:1.1                   # or: docker scout cves tasks-api:1.1
print("Run the Docker commands above in your terminal")''', ["skip-offline-check"]),
    ("md", "## 10. Containerising back end and front end\nA cloud-ready API reads config from the environment and "
           "exposes `/health` and `/ready`. The React app uses a multi-stage build. Compose runs all three services."),
    ("code", '''%%writefile app/cloud.py
import logging, os, sys
from fastapi import FastAPI
from fastapi.responses import JSONResponse

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("tasks-api")
app = FastAPI(title="Tasks API")

def database_reachable() -> bool:
    return os.getenv("SIMULATE_DB_DOWN") != "1"       # real apps ping the database here

@app.get("/health")
def health():
    return {"status": "ok", "env": os.getenv("APP_ENV", "local"), "version": os.getenv("APP_VERSION", "dev")}

@app.get("/ready")
def ready():
    if not database_reachable():
        log.warning("Readiness failed: database unreachable")
        return JSONResponse({"ready": False}, status_code=503)
    return {"ready": True}'''),
    ("code", '''import importlib, sys
from fastapi.testclient import TestClient
sys.path.insert(0, os.getcwd())

def fresh_client(**env):
    for k in ["APP_ENV", "APP_VERSION", "SIMULATE_DB_DOWN"]:
        os.environ.pop(k, None)
    os.environ.update(env)
    import app.cloud as m
    importlib.reload(m)
    return TestClient(m.app)

print("Local:", fresh_client().get("/health").json())
print("Prod: ", fresh_client(APP_ENV="production", APP_VERSION="1.4.2").get("/health").json())
c = fresh_client(SIMULATE_DB_DOWN="1")
print("Ready with DB down:", c.get("/ready").status_code, c.get("/ready").json())'''),
    ("code", '''os.makedirs("web", exist_ok=True)
open("web/Dockerfile", "w").write("""FROM node:22-slim AS build
WORKDIR /web
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /web/dist /usr/share/nginx/html
EXPOSE 80
""")
open("docker-compose.yml", "w").write("""services:
  api:
    build: .
    ports: ["8000:8000"]
    environment:
      APP_ENV: local-compose
      MONGO_URI: mongodb://db:27017
    depends_on: [db]
  web:
    build: ./web
    ports: ["8080:80"]
    depends_on: [api]
  db:
    image: mongo:7
    volumes: ["mongo-data:/data/db"]
volumes:
  mongo-data:
""")
compose = yaml.safe_load(open("docker-compose.yml"))
for name, svc in compose["services"].items():
    print(f"{name:<4} image={svc.get('image', 'built from ' + str(svc.get('build'))):<24} ports={svc.get('ports', [])}")
# ===== Option B: VS Code with Docker Desktop =====
# docker compose up --build    then open http://localhost:8080 and http://localhost:8000/health'''),
    ("md", "### TODO 2 (SmartDesk step 17): add a `Security` stage for SmartDesk with bandit, pip-audit, `npm audit "
           "--audit-level=high` and the secret scan. Record before and after scans in vulnerability report v2."),
    ("code", "# TODO: write your code here"),
    ("md", "## 11. Check yourself\n1. Which bandit findings were HIGH, and how was each fixed?\n"
           "2. Why is the deleted key still a problem?\n3. Which Dockerfile checks did the plain image fail?"),
])
