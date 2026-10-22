# Day 20: App Build Prompts

**App of the day:** Containerised Task API with a Git workflow, a pipeline with security gates, and vulnerability report v2

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 20. Prepares the full stack app for deployment tomorrow: Git history, gated pipeline and hardened Docker images.

---

## Prompt 1: Repository and branching setup

```text
You are a senior DevOps mentor. For a project with a FastAPI back end (api/) and a React Vite front end (web/):
1. Propose a branching strategy for a team of 4 (main + short-lived feature branches) with naming rules.
2. Write a .gitignore covering Python, Node, editor files and .env.
3. Write a PULL_REQUEST_TEMPLATE.md (what, why, how to test, screenshots, security checklist, "AI-assisted: yes/no").
4. List the Azure Repos branch policies to set on main (green build, at least one human reviewer) and why each matters.
5. Show the exact Git commands for a typical feature from branch to merged PR.
```

## Prompt 2: Harden and Dockerise both apps

```text
Write production-quality Dockerfiles:
- api/Dockerfile: python:3.12-slim, layer caching, --no-cache-dir, non-root user with a fixed uid, HEALTHCHECK on /health,
  uvicorn on 0.0.0.0:8000, no secrets in ENV or COPY
- web/Dockerfile: multi-stage, node:22-slim to build with npm ci and npm run build, then nginx:alpine serving dist,
  with an nginx.conf that routes /api to the api service and falls back to index.html
- .dockerignore files for both (exclude .git, .env, tests, node_modules)
- docker-compose.yml running api, web and a database locally
Explain each hardening choice in one line.
```

## Prompt 3: Pipeline with security gates

```text
Write azure-pipelines.yml with stages:
- Test: api (ruff + pytest with results), web (npm ci + npm test)
- Security (depends on Test): bandit -r api -ll, pip-audit -r api/requirements.txt, npm audit --audit-level=high in web/,
  and python tools/scan_secrets.py (write this script: regex scan of tracked files, exit 1 on any hit)
- Build (depends on Security, main only): docker build both images tagged with Build.BuildId, then an image scan that fails on HIGH or CRITICAL
Use displayName on every step. Explain how to read a failed security stage in Azure DevOps.
```

## Prompt 4: Codex as pull request reviewer

```text
Review this diff as a senior reviewer. List up to 5 comments: line, problem, suggested fix, severity.
Check bugs, missing tests, error handling and security. Do not approve or reject; a human decides.
<paste the output of git diff main here, never secrets or customer data>
```

---

## SmartDesk step 17: Docker images, CI with security gates, vulnerability report v2

```text
SmartDesk step 17. For the SmartDesk API and dashboard:
1. Add hardened Dockerfiles and a docker-compose.yml (api, web, db).
2. Add a Security stage to the pipeline: bandit, pip-audit, npm audit and the secret scan. Each must fail the build.
3. Run all scans locally. Save the output as scans/before/.
4. Fix every medium or high finding in small commits, each with a test that proves the fix. Re-run and save scans/after/.
5. Fill shared/templates/Vulnerability_Report_Template.md as docs/vulnerability_report_v2.md, marking each fix as human or Codex-assisted.
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** the build fails when a gate fails; no `# nosec` without a written reason; the container runs as non-root; no key in any file, layer or prompt; a human approved the merge.

---

## Stretch ideas (try on your own)

- Add a pre-commit hook that runs ruff and the secret scan before each commit.
- Tag images with both the build id and the Git commit SHA.
- Compare image sizes for slim, alpine and distroless bases.
