# Day 19: App Build Prompts

**App of the day:** Deploy the Full Stack Task Board to Azure (Containers + CD)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 19. Takes the React + FastAPI Task Board from Day 12 all the way to a cloud URL with a CD pipeline.

---

## Prompt 1: Make it cloud ready

```text
You are a senior cloud engineer mentoring beginners. Make my Task Board (api/: FastAPI + SQLAlchemy, web/: React Vite) cloud ready:
- api: settings from environment variables with pydantic-settings (DATABASE_URL, CORS_ORIGINS, APP_ENV, APP_VERSION, LOG_LEVEL),
  /health and /ready (checks the DB), structured logs to stdout, no local files
- web: API base URL from VITE_API_URL at build time
- Dockerfiles for both (api: slim, non-root, healthcheck; web: multi-stage to nginx)
- docker-compose.yml with api, web and a PostgreSQL database for local runs
Explain each change in one line.
```

---

## Prompt 2: Deploy to Azure Container Apps

```text
Give step-by-step Azure CLI commands (Cloud Shell, Bash) to deploy both containers to one Azure Container Apps environment:
resource group with tags, ACR, az acr build for both images, a managed identity with AcrPull, container apps for api (internal or external)
and web (external), environment variables and a secret for DATABASE_URL, then verification and full clean up commands.
Use variables for names and note which names must be globally unique.
```

---

## Prompt 3: CD pipeline with approvals

```text
Write azure-pipelines.yml for the Task Board with stages Test (api and web), Build (Docker@2 buildAndPush both images tagged
with Build.BuildId), DeployDev (AzureContainerApps@1, environment dev) and DeployProd (environment production with approval),
plus a smoke test that curls /health after each deployment. Explain how to create the service connections and the environment approval in the UI.
```

---

## Stretch ideas (try on your own)

- Add a rollback stage that redeploys the previous tag.
- Add Application Insights logging (research task).
- Estimate the monthly cost with the Azure pricing calculator and write down your assumptions.
