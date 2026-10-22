"""Day 21 spec. Azure Deployment and Continuous Delivery.
Source: archive/v1-40-day/Day19 Sessions 2 to 4 (Azure hosting options, CD pipelines, safe release habits).
NEW (v4) topics are marked.
"""
DAY = 21
FOLDER = "Day21-Azure-Deployment-and-CD"
SLUG = "Azure_Deployment_and_CD"
TITLE = "Azure Deployment and Continuous Delivery"
SUBTITLE = "App Service, Container Apps, CD pipelines with environments, Key Vault and managed identity, and deploying SmartDesk"
DATE = "Tue 24 Nov 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 22: embeddings, vector databases and the RAG application."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 20"),
        ("Azure hosting (2 hrs)", "App Service, Container Apps, VMs in the portal"),
        ("CD pipelines (2 hrs)", "Service connections, variables vs secrets, environments"),
        ("Secrets done right", "Key Vault and managed identity. NEW (v4)"),
        ("End to end (2.5 hrs)", "CI/CD demo and deploying SmartDesk"),
        ("Best practices", "Tag, smoke test, roll back, clean up"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Pick a host", "Choose App Service, Container Apps, AKS or a VM for a given app."),
        ("Write a CD pipeline", "Build once, deploy dev, approve, deploy prod with the same image."),
        ("Handle secrets", "Keep secrets in Key Vault and read them with a managed identity."),
        ("Release safely", "Smoke test, roll back by tag, and clean up resources."),
    ]),

    dict(type="section", title="Azure hosting options", sub="Session 1 (2 hrs). Pick the simplest one that fits"),
    dict(type="table", title="Where to run an app on Azure", header=["Service", "Best for", "Scaling", "You manage"], rows=[
        ["App Service", "Web apps and APIs, code or container", "Manual or rules", "App settings"],
        ["Container Apps", "Containers, microservices, jobs", "Automatic, to zero", "Container + scale rules"],
        ["AKS", "Large platforms, full Kubernetes", "Very flexible", "Much more"],
        ["Virtual Machine", "Special requirements, legacy software", "You build it", "Everything, including OS patches"],
    ], note="FDE default: start with App Service or Container Apps. Move to AKS only with a clear reason."),
    dict(type="flow", title="From image to URL", items=[
        ("Build", "Docker image from your Dockerfile"),
        ("Push", "To Azure Container Registry"),
        ("Deploy", "App Service or Container Apps pulls it"),
        ("Configure", "Settings and secret references"),
        ("Verify", "Hit /health, check logs"),
    ]),
    dict(type="bullets_code", title="Registry and App Service", bullets=[
        "az acr build builds in the cloud",
        "Linux plan hosts the container",
        "WEBSITES_PORT tells it your port",
        "Portal: App Services > Create > Container",
    ], code='''az acr create -g rg-demo -n acrdemo123 \\
  --sku Basic
az acr build -r acrdemo123 \\
  -t tasks-api:1.0 .

az appservice plan create -g rg-demo \\
  -n plan-demo --is-linux --sku B1
az webapp create -g rg-demo -p plan-demo \\
  -n tasks-api-demo123 \\
  --container-image-name \\
  acrdemo123.azurecr.io/tasks-api:1.0
az webapp config appsettings set \\
  -g rg-demo -n tasks-api-demo123 \\
  --settings WEBSITES_PORT=8000'''),
    dict(type="bullets_code", title="Azure Container Apps in one command", greet="Shukka (出荷): Shipping out", bullets=[
        "containerapp up builds and deploys from source",
        "ingress external gives a public URL",
        "target-port is your app's port",
        "Scales automatically, even to zero",
    ], code='''az containerapp up \\
  --name tasks-api \\
  --resource-group rg-demo \\
  --location centralindia \\
  --source . \\
  --ingress external \\
  --target-port 8000

az containerapp logs show \\
  -n tasks-api -g rg-demo --follow'''),
    dict(type="cards", title="Virtual machines: the concept", items=[
        ("What you get", "A full server: you choose the OS, size and disks."),
        ("What you own", "Patching, security, scaling, backups and monitoring."),
        ("When it fits", "Legacy software, special drivers, lift-and-shift migrations."),
        ("Cost trap", "A VM bills while it runs, even when idle. Stop or delete it."),
    ]),

    dict(type="section", title="Continuous delivery with Azure Pipelines", sub="Session 2 (2 hrs). Every merge to main can reach users safely"),
    dict(type="flow", title="A CD pipeline", items=[
        ("Test", "Lint, tests, security gates"),
        ("Build + push", "Image tagged with build id"),
        ("Deploy dev", "Automatic"),
        ("Approve", "A person checks dev"),
        ("Deploy prod", "Same image, prod settings"),
    ], note="Environments in Azure DevOps hold approvals and show deployment history."),
    dict(type="cards", title="Service connections", items=[
        ("What they are", "Saved, scoped access from the pipeline to Azure or a registry."),
        ("Prefer federation", "Workload identity federation: no stored client secret to leak."),
        ("Scope tightly", "One resource group per connection where possible."),
        ("Reference by name", "azureSubscription: sc-azure. Never paste credentials in YAML."),
    ]),
    dict(type="compare", title="Variables vs secrets", left=dict(title="Plain variables", bullets=[
        "Region, app name, image tag", "Visible in YAML and logs", "Fine to commit to Git",
    ]), right=dict(title="Secret variables", bullets=[
        "Passwords, connection strings, keys", "Masked in logs as ***", "Must be mapped into env for scripts",
        "Best stored in Key Vault, linked to the pipeline",
    ]), note="Never echo a secret in a script step. Masking is a safety net, not a plan."),
    dict(type="bullets_code", title="Deployment stage with an environment", bullets=[
        "deployment job targets an environment",
        "Approvals are set on the environment",
        "The same image tag moves forward",
        "Service connection holds Azure access",
    ], code='''- stage: DeployProd
  dependsOn: DeployDev
  jobs:
  - deployment: prod
    environment: production
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureContainerApps@1
            inputs:
              azureSubscription: sc-azure
              containerAppName: tasks-api
              resourceGroup: rg-prod
              imageToDeploy: $(img)'''),

    dict(type="section", title="Key Vault and managed identity", sub="Session 2 continued. No secrets in code, YAML or images", new=True),
    dict(type="cards", title="Azure Key Vault", new=True, items=[
        ("What it stores", "Secrets, keys and certificates, encrypted and access-controlled."),
        ("Who can read", "Azure RBAC roles such as Key Vault Secrets User."),
        ("Audit", "Every read can be logged. You see who accessed what."),
        ("Rotation", "Change a secret in one place; apps pick up the new version."),
    ]),
    dict(type="cards", title="Managed identity", new=True, items=[
        ("The problem", "To read Key Vault, the app needs a credential. Where do you keep that one?"),
        ("The answer", "Azure gives the app its own identity. No password to store or rotate."),
        ("How it works", "The app asks Azure for a short-lived token, then calls Key Vault with it."),
        ("Least privilege", "Grant only the roles it needs: Key Vault Secrets User, AcrPull."),
    ]),
    dict(type="flow", title="Reading a secret with a managed identity", new=True, items=[
        ("Assign", "Turn on the app's identity"),
        ("Grant", "Role on the Key Vault"),
        ("Token", "App gets a short-lived token"),
        ("Read", "Key Vault returns the secret"),
        ("Use", "As an env var or via the SDK"),
    ]),
    dict(type="code", title="Key Vault + managed identity in practice", new=True, code='''# 1. Give the app an identity; let it read secrets
az webapp identity assign -g rg-demo -n tasks-api-demo123
az role assignment create --assignee <principalId> \\
  --role "Key Vault Secrets User" --scope <vault-id>

# 2. App setting that points at Key Vault
az webapp config appsettings set -g rg-demo \\
  -n tasks-api-demo123 --settings \\
  "DATABASE_URL=@Microsoft.KeyVault(SecretUri=<secret-uri>)"

# 3. Or read it in Python with the SDK
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
kv = SecretClient(VAULT_URL, DefaultAzureCredential())
db_url = kv.get_secret("db-url").value''',
         note="The same identity can get AcrPull on the registry, so no registry password is stored either."),

    dict(type="section", title="End-to-end CI/CD and deploying SmartDesk", sub="Session 3 (2.5 hrs). From merge to a live URL"),
    dict(type="flow", title="The end-to-end demo", items=[
        ("Merge", "PR approved by a human"),
        ("CI", "Tests and security gates"),
        ("Image", "Built, scanned, pushed to ACR"),
        ("Dev", "Deployed and smoke tested"),
        ("Prod", "After approval, same tag"),
    ]),
    dict(type="table", title="Safe release habits", header=["Habit", "Why"], rows=[
        ["Tag images with the build id", "Know exactly what is running; roll back by tag"],
        ["Deploy to dev first", "Catch config problems before users do"],
        ["Smoke test /health after deploy", "Fail the pipeline if the app is not up"],
        ["Secrets in Key Vault, read by managed identity", "Not in YAML, images, Git or pipeline logs"],
        ["Clean up test resources", "Avoid surprise costs: delete the resource group"],
    ]),
    dict(type="bullets_code", title="Smoke test and rollback", bullets=[
        "curl --fail turns an error into a red stage",
        "Retries allow for start-up time",
        "Rollback = redeploy the previous tag",
        "Practise rollback before you need it",
    ], code='''- script: |
    curl --fail --retry 5 --retry-delay 10 \\
      https://$(appUrl)/health
  displayName: Smoke test

# Rollback
az containerapp update -n tasks-api \\
  -g rg-prod \\
  --image acr.azurecr.io/tasks-api:<previous-tag>'''),
    dict(type="callout", title="Azure subscription window 1", text="Azure labs run in class only, Days 17 to 21. Delete your resource groups after today.",
         sub="No access tonight? The notebook simulates the pipeline, secrets and rollback offline. The thinking is the same."),
    dict(type="cards", title="SmartDesk step 18: deployed to Azure with CD", items=[
        ("Host", "SmartDesk API and dashboard on Container Apps (or App Service)."),
        ("Secrets", "Database URL and JWT secret in Key Vault, read by managed identity."),
        ("Pipeline", "Test, Security, Build, DeployDev, approval, DeployProd, smoke test."),
        ("Runbook", "Deploy, verify, roll back, rotate a secret, clean up."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("Hosting", "App Service or Container Apps first; AKS or VMs only when needed."),
        ("CD", "Same image through dev and prod, with approvals on environments."),
        ("Secrets", "Key Vault plus managed identity: nothing to leak in code or YAML."),
        ("Habits", "Tag, smoke test, roll back by tag, clean up."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day21_Hotel_Lab.md: CD cells, offline problems, runbook."),
        ("Workbook", "Complete the Day 21 workbook."),
        ("Pre-read", "Skim the Day 22 pre-read on searching by meaning."),
    ]),
]

PREREAD = dict(title="Opening Day for Your App", lede="A light read before Day 21. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "Yesterday you packed your app into a container and added security gates. Tomorrow you put it on the internet "
        "using Microsoft Azure, and set up a pipeline that delivers every approved change automatically."]),
    dict(h="1. The same box, different addresses", paras=[
        "A food truck is the same truck whether it parks at a festival or outside an office. Only the location and the "
        "menu prices change. A cloud-ready app works the same way: the same container runs in a test environment and "
        "in production. Only its settings change, such as which database to use."]),
    dict(h="2. Where to park the truck", table=[
        ["Azure option", "Everyday comparison", "Good for"],
        ["App Service", "A rented shop with staff who keep it running", "Most web apps and APIs"],
        ["Container Apps", "A market stall that grows or shrinks with the crowd", "Containers that need automatic scaling"],
        ["Kubernetes (AKS)", "Running your own shopping mall", "Large platforms with dedicated teams"],
        ["Virtual machine", "Renting an empty building", "Special or legacy software"]],
        box="**Key idea:** choose the simplest option that meets the need. Simple systems are easier to keep running."),
    dict(h="3. Releases with a safety gate", paras=[
        "Many teams first release to a test environment, check it, and only then promote the same version to "
        "production. A person can approve the final step. Azure DevOps calls these **environments**, and the "
        "approval is a gate."]),
    dict(h="4. A safe for passwords", new=True, paras=[
        "Apps need passwords, for example to reach a database. Writing them in the code is like taping the shop key to "
        "the door. **Azure Key Vault** is a locked safe for passwords and keys. But the app needs a key to open the "
        "safe. A **managed identity** solves this: Azure itself vouches for the app, like a staff badge, so there is "
        "no key to lose."]),
    dict(h="5. Think about these before class", bullets=[
        "What settings would differ between a test and a live version of an app?",
        "Why should passwords never be written inside the app's code or pipeline files?",
        "Who in a telecom company would approve a production release, and what would they check?"],
        after=["Shukka (出荷): shipping out, sending goods to customers"]),
])

POSTREAD = dict(title="Deploying to Azure: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["App Service", "PaaS for web apps; Linux plan; deploy code or a container; set WEBSITES_PORT."],
        ["Container Apps", "Serverless containers; az containerapp up --source; scales automatically, even to zero."],
        ["AKS and VMs", "Full control, full responsibility. Choose only with a clear need."],
        ["CD pipeline", "Test, build and push, deploy dev, approval, deploy prod with the same image tag."],
        ["Service connections", "Scoped access from pipeline to Azure; prefer workload identity federation."],
        ["Variables vs secrets", "Secrets are masked and must be mapped into env; best linked from Key Vault."],
        ["Key Vault (NEW v4)", "Encrypted store for secrets, keys, certificates; RBAC roles; audit; rotation."],
        ["Managed identity (NEW v4)", "Azure-issued identity for the app; short-lived tokens; no stored password."],
        ["Safe habits", "Tag by build id, smoke test after deploy, roll back by tag, clean up."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Key Vault references in App Service", paras=[
        "The app still reads an environment variable; the value comes from Key Vault at runtime through the app's "
        "managed identity."],
        code='az webapp config appsettings set -g rg-demo -n tasks-api-demo123 --settings \\\n'
             '  "DATABASE_URL=@Microsoft.KeyVault(SecretUri=https://kv-demo.vault.azure.net/secrets/db-url/)"'),
    dict(sub="2. Pulling from a private registry securely", paras=[
        "Grant the app's managed identity the AcrPull role on the registry. No registry passwords are stored anywhere."]),
    dict(sub="3. Key Vault in the pipeline", paras=[
        "The AzureKeyVault task or a variable group linked to Key Vault fetches secrets at run time. Only map the "
        "secrets each step needs."]),
    dict(sub="4. Deployment slots", paras=[
        "App Service slots let you deploy to a staging slot, warm it up, and swap it with production almost instantly. "
        "Swapping back is your rollback."]),
    dict(sub="5. Scale rules in Container Apps", code=
        "az containerapp update -n tasks-api -g rg-demo --min-replicas 0 --max-replicas 5 \\\n"
        "  --scale-rule-name http --scale-rule-type http --scale-rule-http-concurrency 50"),
    dict(h="Part C: Check yourself", bullets=[
        "Why should the same image be deployed to dev and prod?",
        "When would you choose Container Apps over App Service? When a VM?",
        "Where are deployment approvals configured in Azure DevOps?",
        "How does a managed identity remove the need for a stored password?",
        "How would you roll back a bad release?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Write a one-page runbook for SmartDesk: deploy, verify, roll back, rotate a secret, clean up.",
        "Add a smoke test stage to your pipeline YAML.",
        "List every secret SmartDesk uses and where each will live in Key Vault."],
        after=["**Coming up on Day 22:** embeddings, vector databases, hybrid search and the RAG application.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems. Every problem runs offline in the notebook. Steps that create Azure resources are "
                    "marked optional; do them in class only, in the subscription window, and delete them afterwards.", problems=[
    dict(title="Choose the Host", level="Warm-up", concepts="App Service, Container Apps, AKS, VMs",
         text="For six workloads (a FastAPI API, a nightly batch job, a legacy Windows app, a 40-service platform, a "
              "static React site, an event-driven worker) choose a host and give a one-line reason.",
         sample="FastAPI API      -> App Service or Container Apps: simple PaaS\nnightly batch    -> Container Apps job: runs and stops\n"
                "legacy Windows   -> VM: needs a full OS",
         hints=["Start with the simplest option that meets the need."]),
    dict(title="CD Pipeline YAML", level="Medium", concepts="stages, environments, approvals",
         text="Write a pipeline with Test, Build (Docker@2 buildAndPush to ACR, tag with Build.BuildId), DeployDev and "
              "DeployProd (deployment jobs targeting dev and production environments). Validate it with yaml.safe_load "
              "and print the stage order.",
         sample="Test -> Build -> DeployDev -> DeployProd\nDeployProd environment: production",
         hints=["Approvals are configured on the environment in the Azure DevOps UI, not in YAML."]),
    dict(title="Variables or Secrets?", level="Easy", concepts="pipeline variables, masking",
         text="Sort twelve settings (region, image tag, DB password, JWT secret, app name, API key, log level, "
              "storage connection string and others) into plain variables and Key Vault secrets. Write a mask() "
              "function that hides secret values in a log line.",
         sample="plain : region, imageTag, appName, logLevel ...\nsecret: dbPassword, jwtSecret, apiKey ...\n"
                "log   : connecting with password=***",
         hints=["If it would hurt to see it in a screenshot, it is a secret."]),
    dict(title="Key Vault with a Managed Identity", level="Medium", concepts="Key Vault, managed identity, least privilege", new=True,
         text="Using the offline vault simulator in the notebook, give the app an identity, grant it only the Key Vault "
              "Secrets User role, and read db-url. Show that an identity without the role is refused, and that a "
              "rotated secret is picked up without a code change.",
         sample="tasks-api (Secrets User) -> db-url v1 OK\nreport-job (no role)     -> 403 Forbidden\nafter rotation           -> db-url v2 OK",
         hints=["The simulator mirrors the real flow: identity, role, token, read."]),
    dict(title="Spot the Leak", level="Easy", concepts="secrets hygiene", new=True,
         text="Review a pipeline YAML and a Dockerfile that contain four secret mistakes (password in YAML, echo of a "
              "secret, ENV with a key, connection string in appsettings). Fix each with Key Vault, managed identity or "
              "secret variables.",
         sample="Line 12: DB_PASSWORD in YAML -> Key Vault reference\nLine 20: echo $(apiKey)     -> remove",
         hints=["Search for password, secret, key, token and connection."]),
    dict(title="Release Simulator", level="Challenging", concepts="dev, approval, prod, smoke test, rollback",
         text="Use the notebook's release simulator to promote image tags 101 and 102. Make tag 102 fail its smoke test "
              "in dev so it never reaches prod. Then force a bad tag into prod and roll back to the previous tag.",
         sample="101: dev OK -> approved -> prod OK\n102: dev smoke test FAIL -> stopped\n103: prod FAIL -> rolled back to 101",
         hints=["Keep a history list per environment so rollback knows the previous good tag."]),
    dict(title="Runbook", level="Stretch", concepts="operations, rollback, rotation",
         text="Write a one-page runbook for SmartDesk: deploy, verify, read logs, roll back to the previous image tag, "
              "rotate a Key Vault secret, and clean up resources.",
         sample="Rollback: az containerapp update -n smartdesk-api -g rg-prod --image <acr>/smartdesk-api:<previous-tag>",
         hints=["Write it for a teammate who has never seen the app."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "Azure's private image storage is Azure Container ________.",
        "App Service needs the ________ setting when the container listens on port 8000.",
        "Azure ________ Apps can scale containers down to zero.",
        "With a virtual machine you are responsible for patching the ________.",
        "In Azure DevOps, approvals are configured on an ________.",
        "Saved, scoped access from a pipeline to Azure is a service ________.",
        "Secret pipeline variables are ________ in logs.",
        "Azure's encrypted store for secrets, keys and certificates is Azure Key ________.",
        "An Azure-issued identity for an app, with no stored password, is a ________ identity.",
        "Images should be tagged with the build ________ so you can roll back.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Compare App Service, Container Apps and a VM for the SmartDesk API.",
        "Describe each stage of a CD pipeline with approvals.",
        "Explain how a managed identity reads a Key Vault secret, step by step.",
        "How would you roll back a bad deployment?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "import os\nos.environ[\"APP_ENV\"] = \"prod\"\nprint(os.getenv(\"APP_ENV\", \"local\"), os.getenv(\"MISSING\", \"default\"))",
        "stages = [\"Test\", \"Build\", \"DeployDev\", \"DeployProd\"]\nfailed = \"DeployDev\"\nprint(stages[: stages.index(failed) + 1])",
        "roles = {\"tasks-api\": [\"Key Vault Secrets User\"]}\nwho = \"report-job\"\n"
        "print(\"OK\" if \"Key Vault Secrets User\" in roles.get(who, []) else \"403\")",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write the az command to deploy a container app from source with external ingress on port 8000."),
        dict(q="Write a deployment job that targets a production environment."),
        dict(q="Write Python that reads a secret from Key Vault with DefaultAzureCredential."),
        dict(q="Write a smoke test step that fails the pipeline if /health does not answer."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="Azure hosting, CD pipelines with environments, Key Vault and managed identity, and safe releases", cells=[
    ("md", "## 1. Setup\nAzure steps run in class only, during the subscription window, in **Azure Cloud Shell** or a VS Code "
           "terminal with the Azure CLI. Every other cell runs offline here, including simulators for the pipeline, "
           "Key Vault and rollback."),
    ("code", '''# ===== Option A: Google Colab (active) =====
!pip install -q fastapi httpx pyyaml

# ===== Option B: VS Code / local =====
# pip install fastapi uvicorn httpx pyyaml
# For live Azure work also: pip install azure-identity azure-keyvault-secrets, and install the Azure CLI.
import os, shutil
shutil.rmtree("deploy-demo", ignore_errors=True)
os.makedirs("deploy-demo/app", exist_ok=True)
os.chdir("deploy-demo")
print("Working in", os.getcwd())'''),
    ("md", "## 2. Choosing a host"),
    ("code", '''import pandas as pd
workloads = {
    "FastAPI API": {"container": True, "scale_to_zero": False, "full_os": False, "many_services": False},
    "nightly batch job": {"container": True, "scale_to_zero": True, "full_os": False, "many_services": False},
    "legacy Windows app": {"container": False, "scale_to_zero": False, "full_os": True, "many_services": False},
    "40-service platform": {"container": True, "scale_to_zero": False, "full_os": False, "many_services": True},
}

def choose_host(w):
    if w["full_os"]:
        return "Virtual Machine"
    if w["many_services"]:
        return "AKS (with a platform team)"
    if w["scale_to_zero"]:
        return "Container Apps"
    return "App Service or Container Apps"

print(pd.DataFrame([{"workload": k, "host": choose_host(v)} for k, v in workloads.items()]).to_string(index=False))'''),
    ("md", "## 3. A cloud-ready API with a smoke-testable /health"),
    ("code", '''%%writefile app/main.py
import logging, os, sys
from fastapi import FastAPI

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
APP_ENV = os.getenv("APP_ENV", "local")
APP_VERSION = os.getenv("APP_VERSION", "dev")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///local.db")   # in Azure: a Key Vault reference

app = FastAPI(title="Tasks API")

@app.get("/health")
def health():
    return {"status": "ok", "env": APP_ENV, "version": APP_VERSION, "db_configured": bool(DATABASE_URL)}'''),
    ("code", '''import importlib, sys
from fastapi.testclient import TestClient
sys.path.insert(0, os.getcwd())
import app.main as m
importlib.reload(m)
print(TestClient(m.app).get("/health").json())'''),
    ("md", "## 4. Deploy with the Azure CLI (in class, Cloud Shell)\nNames must be globally unique, so add your initials "
           "and a number. **Delete the resource group when you finish.**"),
    ("code", '''# ===== Option A: Azure Cloud Shell (Bash) =====
# RG=rg-day21-yourname; LOC=centralindia; ACR=acrday21yourname
# az group create -n $RG -l $LOC --tags owner=yourname project=training
# az acr create -g $RG -n $ACR --sku Basic
# az acr build -r $ACR -t tasks-api:1.0 .
#
# --- Option 1: Azure Container Apps (simplest) ---
# az containerapp up --name tasks-api --resource-group $RG --location $LOC \\
#   --source . --ingress external --target-port 8000 --env-vars APP_ENV=dev APP_VERSION=1.0
#
# --- Option 2: Azure App Service for containers ---
# az appservice plan create -g $RG -n plan-day21 --is-linux --sku B1
# az webapp create -g $RG -p plan-day21 -n tasks-api-yourname --container-image-name $ACR.azurecr.io/tasks-api:1.0
# az webapp config appsettings set -g $RG -n tasks-api-yourname --settings WEBSITES_PORT=8000 APP_ENV=dev
#
# --- Clean up ---
# az group delete -n $RG --yes --no-wait
print("Azure commands are listed above. Run them in class only.")''', ["skip-offline-check"]),
    ("md", "## 5. The CD pipeline"),
    ("code", '''%%writefile azure-pipelines.yml
trigger:
  - main

variables:
  acrServiceConnection: sc-acr          # Docker registry service connection
  azureSubscription: sc-azure            # Azure Resource Manager service connection (workload identity federation)
  repository: tasks-api
  acrLoginServer: acrday21yourname.azurecr.io
  tag: $(Build.BuildId)

stages:
  - stage: Test
    jobs:
      - job: unit
        pool: { vmImage: ubuntu-latest }
        steps:
          - task: UsePythonVersion@0
            inputs: { versionSpec: "3.12" }
          - script: pip install -r requirements.txt pytest httpx && python -m pytest -q
            displayName: Tests

  - stage: Build
    dependsOn: Test
    jobs:
      - job: image
        pool: { vmImage: ubuntu-latest }
        steps:
          - task: Docker@2
            displayName: Build and push image
            inputs:
              command: buildAndPush
              containerRegistry: $(acrServiceConnection)
              repository: $(repository)
              tags: $(tag)

  - stage: DeployDev
    dependsOn: Build
    jobs:
      - deployment: dev
        environment: dev
        pool: { vmImage: ubuntu-latest }
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureContainerApps@1
                  inputs:
                    azureSubscription: $(azureSubscription)
                    containerAppName: tasks-api-dev
                    resourceGroup: rg-day21-dev
                    imageToDeploy: $(acrLoginServer)/$(repository):$(tag)
                - script: curl --fail --retry 5 --retry-delay 10 https://$(devUrl)/health
                  displayName: Smoke test dev

  - stage: DeployProd
    dependsOn: DeployDev
    jobs:
      - deployment: prod
        environment: production          # add an approval check on this environment in the UI
        pool: { vmImage: ubuntu-latest }
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureContainerApps@1
                  inputs:
                    azureSubscription: $(azureSubscription)
                    containerAppName: tasks-api
                    resourceGroup: rg-day21-prod
                    imageToDeploy: $(acrLoginServer)/$(repository):$(tag)
                - script: curl --fail --retry 5 --retry-delay 10 https://$(prodUrl)/health
                  displayName: Smoke test prod'''),
    ("code", '''import yaml
p = yaml.safe_load(open("azure-pipelines.yml"))
for st in p["stages"]:
    job = st["jobs"][0]
    env = job.get("environment", "")
    print(f"{st['stage']:<11} after {st.get('dependsOn', '-'):<10} {'environment=' + env if env else ''}")'''),
    ("md", "## 6. Variables vs secrets\nSecret variables are masked in logs. Masking is a safety net: never print a secret."),
    ("code", '''settings = {"region": "centralindia", "appName": "tasks-api", "imageTag": "101", "logLevel": "INFO",
            "dbPassword": "S3cret-db-pass", "jwtSecret": "jwt-signing-value", "apiKey": "training-api-key-value"}
SECRET_WORDS = ("password", "secret", "key", "token", "connection")
secrets = {k: v for k, v in settings.items() if any(w in k.lower() for w in SECRET_WORDS)}
plain = {k: v for k, v in settings.items() if k not in secrets}
print("plain :", list(plain))
print("secret:", list(secrets), "-> Key Vault")

def mask(line):
    for v in secrets.values():
        line = line.replace(v, "***")
    return line

print(mask(f"connecting to db with password={settings['dbPassword']}"))'''),
    ("md", "## 7. NEW (v4): Key Vault and managed identity\nA small **offline simulator** of the real flow: the app has an "
           "identity, the identity has a role on the vault, the app gets a short-lived token and reads the secret. "
           "The real SDK calls are in the next cell."),
    ("code", '''import time, uuid

class FakeAzure:
    """Offline stand-in for Microsoft Entra ID + Key Vault, for practice only."""
    def __init__(self):
        self.identities, self.roles, self.tokens = {}, {}, {}
        self.vault = {"db-url": ["postgresql://smartdesk@db-dev:5432/app"]}   # versions, newest last
        self.audit = []

    def assign_identity(self, app):
        self.identities[app] = str(uuid.uuid4())
        return self.identities[app]

    def grant(self, app, role):
        self.roles.setdefault(app, set()).add(role)

    def get_token(self, app, lifetime_s=3600):
        if app not in self.identities:
            raise PermissionError("no managed identity")
        tok = uuid.uuid4().hex
        self.tokens[tok] = (app, time.time() + lifetime_s)
        return tok

    def get_secret(self, token, name):
        app, expires = self.tokens.get(token, (None, 0))
        ok = app and time.time() < expires and "Key Vault Secrets User" in self.roles.get(app, set())
        self.audit.append({"app": app, "secret": name, "result": "OK" if ok else "403"})
        if not ok:
            raise PermissionError("403 Forbidden")
        return self.vault[name][-1]

    def rotate(self, name, value):
        self.vault[name].append(value)

az = FakeAzure()
az.assign_identity("tasks-api")
az.grant("tasks-api", "Key Vault Secrets User")
az.assign_identity("report-job")               # identity, but no role

for app_name in ["tasks-api", "report-job"]:
    try:
        v = az.get_secret(az.get_token(app_name), "db-url")
        print(f"{app_name:<10} -> OK, version {len(az.vault['db-url'])}")
    except PermissionError as e:
        print(f"{app_name:<10} -> {e}")

az.rotate("db-url", "postgresql://smartdesk@db-dev-2:5432/app")
az.get_secret(az.get_token("tasks-api"), "db-url")
print("after rotation -> version", len(az.vault["db-url"]), "read without a code change")
print(pd.DataFrame(az.audit))'''),
    ("code", '''# ===== Real Azure (in class): the same flow =====
# az webapp identity assign -g $RG -n tasks-api-yourname                  # or: az containerapp identity assign --system-assigned
# az role assignment create --assignee <principalId> --role "Key Vault Secrets User" --scope <key-vault-resource-id>
# az webapp config appsettings set -g $RG -n tasks-api-yourname --settings \\
#   "DATABASE_URL=@Microsoft.KeyVault(SecretUri=https://<vault>.vault.azure.net/secrets/db-url/)"
#
# Python SDK (pip install azure-identity azure-keyvault-secrets):
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
client = SecretClient("https://<vault>.vault.azure.net", DefaultAzureCredential())
print(client.get_secret("db-url").value[:12], "...")''', ["skip-offline-check"]),
    ("md", "### Key Vault in the pipeline\nThe `AzureKeyVault@2` task fetches only the secrets a stage needs. They "
           "arrive as secret variables, masked in logs."),
    ("code", '''kv_step = yaml.safe_load("""
- task: AzureKeyVault@2
  inputs:
    azureSubscription: sc-azure
    KeyVaultName: kv-smartdesk-dev
    SecretsFilter: 'db-url,jwt-secret'
    RunAsPreJob: false
- script: python migrate.py
  env:
    DATABASE_URL: $(db-url)          # map only what this step needs
""")
print("Secrets fetched:", kv_step[0]["inputs"]["SecretsFilter"])
print("Mapped into env:", list(kv_step[1]["env"]))'''),
    ("md", "## 8. End to end: a release simulator\nThe same tag moves dev, then (after approval) prod. A failed smoke test stops "
           "promotion. Rollback redeploys the previous good tag."),
    ("code", '''class Release:
    def __init__(self):
        self.history = {"dev": [], "prod": []}

    def smoke(self, tag, healthy):
        return healthy.get(tag, True)

    def deploy(self, env, tag, healthy):
        self.history[env].append(tag)
        if self.smoke(tag, healthy):
            return True
        bad = self.history[env].pop()
        previous = self.history[env][-1] if self.history[env] else None
        print(f"   {env}: smoke test FAIL for {bad}" + (f" -> rolled back to {previous}" if previous else ""))
        return False

    def promote(self, tag, approved=True, healthy=None, healthy_prod=None):
        healthy = healthy or {}
        if not self.deploy("dev", tag, healthy):
            return f"{tag}: stopped in dev"
        if not approved:
            return f"{tag}: dev OK, waiting for approval"
        if not self.deploy("prod", tag, healthy_prod or healthy):
            return f"{tag}: prod failed, rolled back"
        return f"{tag}: dev OK -> approved -> prod OK"

r = Release()
print(r.promote("101"))
print(r.promote("102", healthy={"102": False}))
print(r.promote("103", healthy_prod={"103": False}))
print("Running now:", {env: (h[-1] if h else None) for env, h in r.history.items()})'''),
    ("md", "### TODO 1 (SmartDesk step 18): write a one-page runbook for SmartDesk: deploy, verify, read logs, roll back, "
           "rotate the db-url secret, clean up. Paste it in a Markdown cell below."),
    ("code", "# TODO: write your code here"),
    ("md", "## 9. Check yourself\n1. Why was report-job refused even though it had an identity?\n"
           "2. Which tag is running in prod at the end, and why?\n3. Which settings above belong in Key Vault?"),
])
