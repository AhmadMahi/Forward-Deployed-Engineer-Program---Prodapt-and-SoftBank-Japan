# Day 18: App Build Prompts

**App of the day:** Containerised Task API with Git workflow and multi-stage pipeline

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 18. Prepares the full stack app for deployment tomorrow: Git history, pipeline and Docker images.

---

## Prompt 1: Repository and branching setup

```text
You are a senior DevOps mentor. For a project with a FastAPI back end (api/) and a React Vite front end (web/):
1. Propose a branching strategy for a team of 4 (main + short-lived feature branches) with naming rules.
2. Write a .gitignore covering Python, Node and editor files.
3. Write a PULL_REQUEST_TEMPLATE.md (what, why, how to test, screenshots, checklist).
4. List the Azure Repos branch policies to set on main and why each matters.
5. Show the exact Git commands for a typical feature from branch to merged PR.
```

---

## Prompt 2: Dockerise both apps

```text
Write production-quality Dockerfiles:
- api/Dockerfile: python:3.11-slim, layer caching, non-root user, HEALTHCHECK on /health, uvicorn on 0.0.0.0:8000
- web/Dockerfile: multi-stage, node:20 to build with npm ci and npm run build, then nginx:alpine serving dist, with an nginx.conf that
  routes /api to the api service and falls back to index.html for client routes
- .dockerignore files for both
- docker-compose.yml running api and web together locally
Explain each instruction briefly.
```

---

## Prompt 3: Multi-stage pipeline

```text
Write azure-pipelines.yml with stages: Test (api: ruff + pytest with results; web: npm ci + npm test),
then Build (docker build both images tagged with Build.BuildId) that depends on Test and only runs on main.
Use variables, displayName on every step, and caching for pip and npm. Explain how to read a failed run in Azure DevOps.
```

---

## Stretch ideas (try on your own)

- Add a pre-commit hook that runs ruff before each commit.
- Scan the image for vulnerabilities with Trivy in the pipeline (research task).
- Tag images with both the build id and latest.
