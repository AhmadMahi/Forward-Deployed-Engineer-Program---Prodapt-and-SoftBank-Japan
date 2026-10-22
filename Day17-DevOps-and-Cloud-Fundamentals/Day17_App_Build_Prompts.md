# Day 17: App Build Prompts

**App of the day:** DevOps-ready FastAPI Service (tests, lint, security scans, pipeline YAML)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 17. Make a FastAPI service ready for CI: tests, lint, security scans and an Azure Pipelines file.

---

## Prompt 1: Make the project CI-ready

```text
You are a senior DevOps mentor. Take a simple FastAPI Tasks API and make it CI-ready.
Project layout: app/ (main.py, models.py, routes.py), tests/ (test_api.py with at least 8 tests), requirements.txt
(pinned versions), requirements-dev.txt (pytest, pytest-cov, ruff, bandit, pip-audit), pyproject.toml with ruff settings,
a Makefile or tasks.py with lint, test, scan and run commands, a .gitignore for Python (including .env), and a README
with a "How CI works" section. Explain each file's purpose in one line.
```

## Prompt 2: Write the Azure pipeline with a security stage (NEW v4)

```text
Write azure-pipelines.yml for this project:
- trigger on main and on pull requests to main
- stage Build: UsePythonVersion 3.12, cache pip, install, ruff check, pytest with coverage (Cobertura) and JUnit results;
  PublishTestResults and PublishCodeCoverageResults run even if tests fail
- stage Security (depends on Build): bandit -r app -ll, pip-audit -r requirements.txt, and a simple secret scan step
- publish the app folder as a pipeline artifact named app
Explain every block with a short comment in the YAML. Do not put any secret values in the file.
```

## Prompt 3: Scan, triage and fix (NEW v4)

```text
Run bandit and pip-audit on this project and show me the findings as a table:
tool, ID, severity, file and line, what it means in one sentence, proposed fix.
Do not change any code yet. Wait for me to choose which findings to fix.
```

**Review step:** pick the fixes yourself, ask Codex to apply them one at a time, re-run the scans and the tests after each one.

## Prompt 4: Explain it to a manager

```text
Explain to a non-technical manager, in under 200 words, what this CI pipeline does, what the security stage protects
against, and what the team needs to do when it goes red. Then give 5 quiz questions with answers on CI/CD, DevSecOps and cloud models.
```

---

## SmartDesk step 15: Lint, tests and pipeline YAML

```text
SmartDesk step 15.
1. Add ruff settings to pyproject.toml and fix all lint errors in the back end (no behaviour changes).
2. Make sure pytest -q passes with OFFLINE=1 (tests from Day 15).
3. Write azure-pipelines.yml with two stages: Build (ruff, pytest with JUnit results) and Security
   (bandit -r app -ll, pip-audit -r requirements.txt). Trigger on main and pull requests.
4. Add a "CI" section to AGENTS.md with the exact lint, test and scan commands.
Show me the plan first, then the diff. Explain each pipeline stage in one sentence.
```

**Review checklist before you commit:** no secrets in YAML or AGENTS.md; every scan finding is fixed or has a written reason; tests still pass; you can explain every line Codex wrote.

## Stretch ideas (try on your own)

- Add a coverage threshold that fails the build below 80 percent.
- Add a scheduled nightly run of the Security stage.
- Write the equivalent GitHub Actions workflow.
