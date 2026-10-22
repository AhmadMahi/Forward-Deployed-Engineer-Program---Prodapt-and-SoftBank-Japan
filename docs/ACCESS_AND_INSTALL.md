# Access and Install Plan

Install and verification steps are in the [Laptop Setup Guide](../shared/Laptop_Setup_Guide.pdf). Check every Required item before Day 1.

## Software

| Software | Needed from | Required? | Notes |
|---|---|---|---|
| Modern browser (Chrome or Edge) | Day 1 (26 Oct) | Required | Colab, Azure portal and Azure DevOps (web). Azure Cloud Shell not needed. |
| Google account (for Google Colab) | Day 2 (27 Oct) | Required | Colab runs all notebooks, including the free GPU runtime for the SLM lab on Day 25. |
| Python 3.12 or newer | Day 2 (27 Oct) | Required | For VS Code work; Colab has Python built in. |
| VS Code | Day 3 (28 Oct) | Required | Main editor from Day 3. |
| OpenAI Codex extension for VS Code | Day 3 (28 Oct) | Required | Signed in with the program's OpenAI API key; approved models only. |
| Git | Day 3 (28 Oct) | Required | Version control from Day 3; CI from Day 17. |
| MongoDB Compass | Day 4 (29 Oct) | Optional | Visual tool for MongoDB; Colab uses mongomock. |
| Node.js LTS (with npm) | Day 8 (04 Nov) | Required | JavaScript, Express and React (Vite). |
| Postman | Day 9 (05 Nov) | Required | API testing. |
| Java 17 | Day 16 (17 Nov) | Optional | Only to run PySpark locally; not needed in Colab. |
| Docker Desktop | Day 20 (23 Nov) | Required | Containers from Day 20. Larger companies need a paid Docker subscription; check licensing. |
| Hugging Face account (free) | Day 25 (30 Nov) | Optional | Some small models need a free account to download. |
| Python packages (pip, per day) | Day 2 (27 Oct) | Required | See the Libraries line in each day's README or deck; installed in class (for example pytest, mcp, pyspark, openai, transformers, langchain, langgraph). |

## Access

| Access | From | Until | Notes |
|---|---|---|---|
| OpenAI API key for Codex (VS Code extension) | Day 3 (28 Oct) | Day 40 (21 Dec) | Approved models only; daily usage check; per-learner budget. Little or no use on Days 4 and FDE days. |
| OpenAI API key for LLM app calls (GenAI notebooks and SmartDesk) | Day 12 (11 Nov) | Day 40 (21 Dec) | Separate project or budget from Codex. Notebooks have an offline demo mode without a key. |
| GitHub account (repos, Codex, CI) | Day 3 (28 Oct) | Day 40 (21 Dec) | Needed for Codex and the capstone repo. |
| MongoDB Atlas free tier (optional) | Day 4 (29 Oct) | Day 7 (03 Nov) | Colab uses mongomock, so Atlas is optional. |
| Azure DevOps organisation (web) | Day 17 (18 Nov) | Day 21 (24 Nov) | Repos and Pipelines; reused in the capstone (Days 36 to 40). |
| Azure subscription, window 1 (web portal) | Day 17 (18 Nov) | Day 21 (24 Nov) | DevOps, CI/CD and deployment labs (Days 17, 20, 21). Delete resource groups after Day 21. |
| Azure subscription, window 2 | Day 34 (11 Dec) | Day 34 (11 Dec) | LLM gateway deployment lab. |
| Azure subscription, window 3 (capstone) | Day 38 (17 Dec) | Day 40 (21 Dec) | Team deployments and demo day. Delete resource groups after Day 40. |
| Colab GPU runtime (free tier) | Day 25 (30 Nov) | Day 25 (30 Nov) | SLM lab. Free GPU availability varies; a CPU fallback uses a smaller model. |

## Keys and secrets

- In Colab: click the key icon (Secrets), add `OPENAI_API_KEY`, and allow notebook access.
- In VS Code: put `OPENAI_API_KEY=...` in a `.env` file at the project root. `.env` must be listed in `.gitignore`.
- Never commit a key, paste it into a prompt, or put it in front-end code.
