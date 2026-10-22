# SmartDesk deployment runbook (one page)

**Service:** smartdesk-api on Azure Container Apps | **Resource group:** rg-smartdesk-training | **Owner:** your team

## Before you deploy
1. CI is green on `main` (security gates and tests).
2. New secrets are added to Key Vault, not to YAML or code.
3. The container app's managed identity has `get` access to the Key Vault secrets.

## Deploy
1. Merge the pull request. The CD pipeline builds, pushes and deploys to **dev**.
2. Check the smoke test and `/health` in dev.
3. Approve the **prod** environment check in Azure DevOps.

## Verify
- `/health` returns `{"status": "ok"}`. `/version` shows the new build id.
- Logs show no errors for 10 minutes.

## Roll back
- Container Apps keeps revisions. Switch traffic back to the previous revision in the portal, or re-run the last good pipeline.

## After the training window
- Delete the resource group after Day 21 to stop costs.
