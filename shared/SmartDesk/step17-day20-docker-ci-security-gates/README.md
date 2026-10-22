# SmartDesk step 17 (Day 20): Docker images and CI security gates

**Increment:** Docker images; CI with security gates; vulnerability report v2

**Day folder:** [../../../Day20-Git-CI-CD-and-Docker/](../../../Day20-Git-CI-CD-and-Docker/) (see `Day20_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 16](../step16-day18-rag-faq-citations/) | Next: [step 18](../step18-day21-azure-cd/)

## Goal

Containerise SmartDesk with hardened images and stop the build when a security gate fails.

## What changed from the previous step

Adds Dockerfiles (API and front end), `.dockerignore`, a CI pipeline with bandit, pip-audit, gitleaks and trivy gates, an AI review checklist and vulnerability report v2.

## Key files

- `Dockerfile`: hardened API image
- `frontend.Dockerfile`: multi-stage front-end image
- `azure-pipelines.yml`: security gates then build and scan
- `vulnerability_report_v2.md`: report v2
- `CODEX_PR_REVIEW.md`: AI review with human approval

## How to run

```bash
docker build -t smartdesk-api .
docker run -p 8000:8000 smartdesk-api      # Docker Desktop on your laptop
```

## How to test

```bash
python -m pytest -q        # static checks on the Dockerfile and pipeline
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
