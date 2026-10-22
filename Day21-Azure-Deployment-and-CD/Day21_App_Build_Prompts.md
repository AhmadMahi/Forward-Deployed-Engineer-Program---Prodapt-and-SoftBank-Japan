# Day 21: App Build Prompts

**App of the day:** Deploy the Full Stack Task Board to Azure with continuous delivery, Key Vault and managed identity

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff and every command before you run it. Azure commands create billable resources.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, connection strings, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 21. Takes the React + FastAPI Task Board all the way to a cloud URL with a CD pipeline. Azure steps run in class only, in subscription window 1 (Days 17 to 21).

---

## Prompt 1: Make it cloud ready

```text
You are a senior cloud engineer mentoring beginners. Make my Task Board (api/: FastAPI + SQLAlchemy, web/: React Vite) cloud ready:
- api: settings from environment variables with pydantic-settings (DATABASE_URL, CORS_ORIGINS, APP_ENV, APP_VERSION, LOG_LEVEL),
  /health and /ready (checks the DB), structured logs to stdout, no local files
- web: API base URL from VITE_API_URL at build time (never a key or secret in the front end)
- Confirm both Dockerfiles from Day 20 are hardened (slim, non-root, healthcheck)
Explain each change in one line.
```

## Prompt 2: Deploy to Azure Container Apps with Key Vault and managed identity

```text
Give step-by-step Azure CLI commands (Cloud Shell, Bash) to deploy both containers to one Azure Container Apps environment:
resource group with owner and project tags, ACR, az acr build for both images, a Key Vault holding DATABASE_URL and JWT_SECRET,
a system-assigned managed identity for each app with only AcrPull on the registry and Key Vault Secrets User on the vault,
container apps for api and web with secrets that reference Key Vault, then verification and full clean up commands.
Use variables for names and note which names must be globally unique. No passwords anywhere in the commands.
```

## Prompt 3: CD pipeline with approvals and smoke tests

```text
Write azure-pipelines.yml for the Task Board with stages Test, Security (from Day 20), Build (Docker@2 buildAndPush both images
tagged with Build.BuildId), DeployDev (AzureContainerApps@1, environment dev) and DeployProd (environment production with approval),
plus a smoke test that curls /health after each deployment. Use an Azure Resource Manager service connection with workload identity
federation. Fetch only the secrets each stage needs with AzureKeyVault@2. Explain how to create the service connection and the
environment approval in the UI.
```

---

## SmartDesk step 18: Deployed to Azure with CD

```text
SmartDesk step 18. Deploy SmartDesk (API and dashboard):
1. Move DATABASE_URL and JWT_SECRET into Key Vault. The apps read them through managed identity. Remove them from .env.example values.
2. Add DeployDev and DeployProd stages with a production approval and smoke tests.
3. Write docs/RUNBOOK.md: deploy, verify, read logs, roll back to the previous tag, rotate a Key Vault secret, clean up.
4. Add a test that fails if any file in the repo contains a connection string or a key pattern.
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** no secret in YAML, images, Git or logs; each identity has only the roles it needs; prod deploys only after a human approval; the runbook has a tested rollback; the resource group is deleted after class.

---

## Stretch ideas (try on your own)

- Use an App Service deployment slot and swap for zero-downtime releases.
- Add a scale rule to the Container App and load test it with a short script.
- Estimate the monthly cost with the Azure pricing calculator and write down your assumptions (prices change; date your estimate).
