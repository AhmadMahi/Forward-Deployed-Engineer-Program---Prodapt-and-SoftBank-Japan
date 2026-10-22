# Day 17: App Build Prompts

**App of the day:** DevOps-ready FastAPI Service (tests, lint, pipeline YAML)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 17. Prepares a service for Azure DevOps: structure, tests, lint config and a CI pipeline. Tomorrow you push it to Azure Repos and add Docker.

---

## Prompt 1: Make the project CI-ready

```text
You are a senior DevOps mentor. Take a simple FastAPI Tasks API and make it CI-ready.
Project layout: app/ (main.py, models.py, routes.py), tests/ (test_api.py with at least 8 tests), requirements.txt,
requirements-dev.txt (pytest, pytest-cov, ruff), pyproject.toml with ruff settings, a Makefile or tasks.py with
lint, test and run commands, a .gitignore for Python, and a README with a "How CI works" section.
Explain each file's purpose in one line.
```

---

## Prompt 2: Write the Azure pipeline

```text
Write azure-pipelines.yml for this project:
- trigger on main and on pull requests to main
- stage Build: UsePythonVersion 3.11, cache pip, install, ruff check, pytest with coverage (Cobertura) and JUnit results
- PublishTestResults and PublishCodeCoverageResults tasks that run even if tests fail
- publish the app folder as a pipeline artifact named app
Explain every block with a short comment in the YAML.
```

---

## Prompt 3: Explain it to a manager

```text
Explain to a non-technical manager, in under 200 words, what this CI pipeline does, what it protects against,
and what the team needs to do when it goes red. Then give 5 quiz questions with answers on CI/CD and cloud models.
```

---

## Stretch ideas (try on your own)

- Add a coverage threshold that fails the build below 80 percent.
- Add a scheduled nightly run.
- Write the equivalent GitHub Actions workflow.
