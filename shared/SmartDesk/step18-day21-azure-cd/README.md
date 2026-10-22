# SmartDesk step 18 (Day 21): Deployed to Azure with CD

**Increment:** Deployed to Azure with CD

**Day folder:** [../../../Day21-Azure-Deployment-and-CD/](../../../Day21-Azure-Deployment-and-CD/) (see `Day21_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 17](../step17-day20-docker-ci-security-gates/) | Next: [step 19](../step19-day22-hybrid-search-rerank/)

## Goal

Ship SmartDesk to Azure Container Apps through a pipeline with dev and prod stages, Key Vault secrets and an approval gate.

## What changed from the previous step

Adds a CD pipeline, settings loaded from Key Vault-backed environment variables with masked secrets, and a one-page runbook.

## Key files

- `azure-pipelines-cd.yml`: build, deploy dev, approve, deploy prod
- `settings.py`: fail-fast settings, masked secrets
- `RUNBOOK.md`: deployment runbook
- `test_settings.py`: tests

## How to run

```bash
# runs in Azure DevOps during the class subscription window; locally:
DATABASE_URL=sqlite:// JWT_SECRET=dev python -c "import settings; print(settings.load_settings())"
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
