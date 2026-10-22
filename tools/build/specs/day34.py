"""Day 34 spec. GenAI 14: LLM Deployment and Lifecycle.
Source: archive/v1-40-day/Day33 (deployment architectures, environments, secrets, pipelines, scaling, releases).
NEW (v4) topics are marked.
"""
DAY = 34
FOLDER = "Day34-LLM-Deployment-and-Lifecycle"
SLUG = "LLM_Deployment_and_Lifecycle"
TITLE = "LLM Deployment and Lifecycle"
SUBTITLE = "Hosted, self-hosted and managed agent runtimes, AI gateways, versioning, rollback, environments and secrets"
DATE = "Fri 11 Dec 2026"
TRACK = "GenAI"
NEXT = "See you on Monday for Day 35: observability, drift and optimisation."
CLOSING_GREET = "Yoi shuumatsu wo (良い週末を): Have a great weekend"

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz and presentations", "15 questions on Day 33, then participant PPTs (20 min)"),
        ("Lifecycle and hosting", "Hosted, in-tenant, self-hosted"),
        ("Managed agent runtimes", "And data retention options. NEW (v4)"),
        ("Versioning and rollback", "Prompts, datasets, embeddings"),
        ("AI gateway", "Stateless MCP, no long-lived keys. NEW (v4)"),
        ("Scale and release", "Async, streaming, canary"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Choose where it runs", "Compare hosted APIs, in-tenant, self-hosted and managed agent runtimes."),
        ("Version and roll back", "Version prompts, datasets and embeddings, and roll back in one step."),
        ("Protect secrets", "Separate environments, keep keys in a vault, give agents short-lived tokens."),
        ("Ship safely", "Put a gateway in front of models; stream, limit and release by canary."),
    ]),
    dict(type="section", title="The lifecycle loop and hosting", sub="Where the model runs and who manages it"),
    dict(type="flow", title="The deployment lifecycle loop", items=[
        ("Package", "Code, prompts and manifest in one image"),
        ("Promote", "Dev, then test, then prod"),
        ("Release", "Canary or blue-green"),
        ("Observe", "Quality, cost, latency (Day 35)"),
        ("Roll back", "Previous manifest in one step"),
    ], note="The same artefact moves through every environment. Only configuration changes."),
    dict(type="table", title="Three hosting patterns", header=["Pattern", "Strengths", "Watch out for"], rows=[
        ["Hosted model API", "Fastest start, strongest models, no GPUs", "Data policies, rate limits, per-token cost"],
        ["Cloud-hosted in your tenant", "Enterprise controls, regional hosting", "Quotas, regional model availability"],
        ["Self-hosted open model", "Full control, data stays inside", "GPU cost, operations, upgrades, licences"],
    ], note="Azure OpenAI, for example, runs OpenAI models inside the customer's Azure tenant with enterprise controls."),
    dict(type="cards", title="Managed agent runtimes", new=True,
         lead="The provider runs the agent loop for you: tools, state, scaling. You configure and observe it.", items=[
        ("What you get", "Hosted loop, tool execution, conversation state, built-in tracing."),
        ("Examples", "The hosted Agents API from Day 27; cloud agent services in Azure and other clouds."),
        ("Good fit", "Fast pilots, standard tools, teams without platform engineers."),
        ("Watch out for", "Lock-in, data location, limited custom guardrails, cost visibility."),
    ]),
    dict(type="compare", title="Build your own loop or use a managed runtime?", new=True,
         left=dict(title="Your own runtime", bullets=[
             "Full control of tools and guardrails", "Any model behind your gateway", "You scale, patch and monitor it"]),
         right=dict(title="Managed agent runtime", bullets=[
             "Faster to start", "Provider handles scaling and state", "Check retention, region and export of traces"]),
         note="Many teams start managed, then move hot paths into their own runtime when needs grow."),
    dict(type="table", title="Data retention options", new=True, header=["Layer", "Question to ask", "Typical setting"], rows=[
        ["Provider API", "Does the provider store prompts and outputs, and for how long?", "Check current terms; ask about zero data retention"],
        ["Managed runtime", "Where are conversation state and traces kept?", "Region pinned; delete on request"],
        ["Your logs", "Who can read raw prompts?", "Metadata for all, full text sampled and masked"],
        ["Memory stores", "When do memories expire?", "TTL per user; delete on request (Day 27)"],
    ], note="Retention terms change. Confirm with the provider and the customer's policy before go-live."),

    dict(type="section", title="Versioning, rollback and environments", sub="Same code, different settings"),
    dict(type="cards", title="Version these together", items=[
        ("Prompts", "Text and id in Git, hash in the manifest."),
        ("Datasets", "Golden set and fine-tuning data with a version and hash."),
        ("Embeddings", "Embedding model, chunking settings, index build id."),
        ("Release manifest", "One file per release; rollback = deploy the previous one."),
    ], note="If you change the embedding model, rebuild the whole index. Never mix vectors from two models."),
    dict(type="table", title="Typical environments", header=["Environment", "Purpose", "Data"], rows=[
        ["Local / dev", "Build and try things", "Fake or sample data"],
        ["Test / staging", "Run golden sets, integration tests", "Realistic, anonymised"],
        ["Production", "Real users", "Real data, strict access"],
    ], note="Promote the same image and release manifest through each stage; only configuration changes."),
    dict(type="bullets_code", title="Settings from the environment", bullets=[
        "Every setting has a clear source",
        "Secrets never have defaults in prod",
        "Fail fast at startup if missing",
        "Key Vault references on Azure",
    ], code='''import os

ENV = os.getenv("APP_ENV", "dev")
MODEL = os.getenv("LLM_MODEL", "gpt-6.1-sol")
API_KEY = os.getenv("LLM_API_KEY")

if ENV == "prod" and not API_KEY:
    raise RuntimeError(
        "LLM_API_KEY missing in prod")'''),

    dict(type="section", title="The AI gateway", sub="One front door for every model call", new=True),
    dict(type="cards", title="The AI gateway pattern", greet="Iriguchi (入口): Entrance", new=True, items=[
        ("One entry point", "All apps and agents call the gateway, not providers directly."),
        ("Shared controls", "Auth, rate limits, budgets, model allow-list and guardrails."),
        ("Provider freedom", "Switch or mix models without changing apps."),
        ("Observability", "Every call logged with release, tokens, cost and latency."),
    ]),
    dict(type="compare", title="No long-lived keys in agents", new=True,
         left=dict(title="Risky", bullets=[
             "Provider key pasted into the agent's config", "Same key for every tool and user",
             "Never expires; leaks are permanent"]),
         right=dict(title="Safer", bullets=[
             "Only the gateway holds the provider key (in Key Vault)", "Agents get short-lived tokens with scopes",
             "Tokens expire in minutes and can be revoked"]),
         note="Links to Day 23 (agent identity) and Day 30 (scoped, short-lived tokens)."),
    dict(type="bullets_code", title="Stateless MCP servers", new=True, bullets=[
        "MCP spec 2026-07-28 is stateless (Day 28)",
        "Every request carries what it needs",
        "Any replica can answer: easy to scale",
        "Check a scoped token on every call",
    ], code='''@app.post("/mcp")
def mcp(req: dict, authorization: str = Header()):
    claims = verify(authorization)      # short-lived
    if req["method"] == "tools/list":
        return {"tools": TOOLS}
    if req["method"] == "tools/call":
        need = TOOLS_SCOPE[req["params"]["name"]]
        if need not in claims["scopes"]:
            raise HTTPException(403)
        return run_tool(req["params"])  # no session'''),

    dict(type="section", title="Scale and release", sub="Many users at once, change without big-bang risk"),
    dict(type="flow", title="A production inference pipeline", items=[
        ("Validate", "Auth, size limits, input guardrails"),
        ("Enrich", "Retrieve context, user profile"),
        ("Generate", "Model call with timeout and retry"),
        ("Check", "Output guardrails, schema validation"),
        ("Respond", "Stream, log, record cost"),
    ], note="Time every stage. When latency rises, you will know exactly where."),
    dict(type="bullets_code", title="Async with a concurrency limit", bullets=[
        "async def lets one process serve many users",
        "A semaphore caps calls in flight",
        "gather runs requests together",
        "Protects you from 429 storms",
    ], code='''import asyncio
limit = asyncio.Semaphore(10)

async def answer(q):
    async with limit:          # max 10 at once
        return await call_model(q)

results = await asyncio.gather(
    *[answer(q) for q in questions])'''),
    dict(type="bullets_code", title="Streaming responses", greet="Nagareru (流れる): To flow", bullets=[
        "Yield chunks as the model produces them",
        "FastAPI StreamingResponse sends them",
        "Time to first token matters most",
        "Browsers read the stream as it arrives",
    ], code='''from fastapi.responses import StreamingResponse

async def tokens(prompt):
    async for chunk in model_stream(prompt):
        yield chunk

@app.post("/chat/stream")
async def chat(req: ChatIn):
    return StreamingResponse(tokens(req.text),
        media_type="text/plain")'''),
    dict(type="table", title="Rolling out a new release", header=["Strategy", "How", "Best for"], rows=[
        ["Canary", "Send 5 to 10% of users to the new release, watch metrics", "Most changes"],
        ["Blue-green", "Two full environments; switch traffic at once, switch back if bad", "Fast rollback"],
        ["Shadow", "New release answers silently; compare with live answers", "Risky model swaps"],
        ["Feature flags", "Turn features on per user group without redeploying", "Gradual exposure"],
    ], note="Decide rollback thresholds before the canary starts."),
    dict(type="cards", title="SmartDesk step 29: production gateway on Azure", items=[
        ("Gateway", "Auth, budgets, model allow-list, streaming, canary routing."),
        ("Secrets", "Provider key in Key Vault; managed identity; agents get short-lived tokens."),
        ("Deploy", "Container Apps revisions for canary traffic (Azure window 2)."),
        ("Build with Codex", "Use Day34_App_Build_Prompts.md. Review every line Codex writes."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("Hosting", "Hosted, in-tenant, self-hosted or managed runtime; check retention."),
        ("Versioning", "Prompts, datasets and embeddings in one manifest; roll back in one step."),
        ("Gateway", "One front door; stateless MCP; no long-lived keys in agents."),
        ("Release", "Async, limits, streaming; canary with agreed thresholds."),
    ]),
    dict(type="cards", title="Before Monday", lead="Monday starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day34_Hotel_Lab.md: streaming gateway, canary and rollback."),
        ("Workbook", "Complete the Day 34 workbook."),
        ("Pre-read", "Skim the Day 35 pre-read on watching AI and drift."),
    ]),
]

PREREAD = dict(title="From Prototype to Production Service", lede="A light read before Day 34. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "A prototype that works for one person in a notebook is very different from a service that answers thousands of "
        "users safely. Tomorrow you learn how AI services are deployed, configured, secured and updated without breaking things."]),
    dict(h="1. Taxi, lease, own, or a driver service", table=[
        ["Option", "Everyday comparison", "Trade-off"],
        ["Use a model provider's API", "Taking a taxi", "Easy and powerful; you follow their rules and pay per trip"],
        ["Host it in your company's cloud", "Leasing a car", "More control and privacy; some setup"],
        ["Run an open model", "Owning a car", "Full control; you handle fuel and repairs yourself"],
        ["Managed agent runtime (NEW v4)", "A car with a hired driver", "Fast and convenient; check where the driver keeps your notes"],
    ]),
    dict(h="2. Practice kitchen and real kitchen", paras=[
        "Restaurants test new dishes in a practice kitchen before serving customers. Software teams use separate "
        "environments: development for building, testing for checking, production for real users. Passwords and keys, "
        "called **secrets**, are kept in a safe, never written into the recipe."]),
    dict(h="3. One front door", new=True, paras=[
        "A large office has one reception desk that checks badges, signs in visitors and keeps a log. An **AI gateway** "
        "does this for AI: every app and agent goes through it, so the company can control who uses which model, set "
        "budgets and see everything in one place. Agents get a visitor badge that expires, not a master key."]),
    dict(h="4. Changing safely", paras=[
        "Before switching every customer to a new menu, a restaurant might offer it at a few tables first. AI teams do "
        "this too, called a **canary release**: a small share of users get the new version while the team watches the numbers."],
        box="**Key idea:** release changes gradually, keep keys in a vault, and make it easy to switch back."),
    dict(h="5. Think about these before class", bullets=[
        "Would your organisation allow its data to be stored by an external AI provider? For how long?",
        "Which settings would differ between a test and a live version of SmartDesk?",
        "Why is a key that never expires more dangerous than one that lasts five minutes?"],
        after=["Nagareru (流れる): to flow"]),
])

POSTREAD = dict(title="LLM Deployment: Recap and Beyond", lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Hosting", "Hosted API, cloud-hosted in your tenant, self-hosted open model."],
        ["Managed agent runtimes (NEW v4)", "Provider runs the loop, tools and state; check lock-in, region and trace export."],
        ["Data retention (NEW v4)", "Ask the provider, runtime, your logs and memory stores how long data lives."],
        ["Versioning and rollback", "Prompts, datasets and embeddings in one manifest; rollback = previous manifest."],
        ["Environments and secrets", "Dev, test, prod; same image; secrets from Key Vault; fail fast if missing."],
        ["AI gateway (NEW v4)", "One entry point: auth, budgets, allow-list, guardrails, logging, provider switching."],
        ["Stateless MCP (NEW v4)", "Every request self-contained; scoped token checked per call; scales horizontally."],
        ["No long-lived keys (NEW v4)", "Only the gateway holds provider keys; agents get short-lived scoped tokens."],
        ["Scale and release", "Async with a semaphore, streaming, queues; canary, blue-green, shadow, flags."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Self-hosting open models", paras=[
        "Inference servers such as vLLM serve open models efficiently with continuous batching. Self-hosting makes sense "
        "with strict data rules, very high volume, or a need for custom models; budget for GPU capacity and operations."]),
    dict(sub="2. Server-sent events", paras=[
        "For browser chat UIs, servers often stream with server-sent events (text/event-stream), which browsers read "
        "easily and can reconnect automatically."]),
    dict(sub="3. Back-pressure", paras=[
        "When more requests arrive than you can serve, decide on purpose: queue them, return 429 with Retry-After, or "
        "degrade to a cheaper model. Never let them pile up silently until everything times out."]),
    dict(sub="4. Regional deployment", paras=[
        "For users in Japan and India, choose regions close to them and check that the models you need are available "
        "there. Data residency rules may decide the region for you."]),
    dict(sub="5. Token exchange for agents", paras=[
        "OAuth token exchange lets a gateway swap a user's token for a narrower, short-lived token that an agent or MCP "
        "server can use. The agent never sees the user's main credential or the provider key."]),
    dict(h="Part C: Check yourself", bullets=[
        "When would you choose a managed agent runtime over your own loop?",
        "What four places should you check for data retention?",
        "What does an AI gateway centralise?",
        "Why does a stateless MCP server scale more easily?",
        "Why should an agent never hold a long-lived provider key?"]),
    dict(h="Part D: Practice ideas for the weekend", bullets=[
        "Add a /ready endpoint that returns 503 when a required secret is missing in prod.",
        "Write rollback criteria for SmartDesk's next release.",
        "Draw SmartDesk's architecture with the gateway, Key Vault and the MCP server."],
        after=["**Coming up on Day 35:** observability, drift and optimisation, then the capstone from Tuesday.",
               "Yoi shuumatsu wo (良い週末を): have a great weekend"]),
])

HANDSON = dict(lede="Seven problems building a production-style LLM service. The model is simulated, so everything "
                    "runs without a key or GPU.", problems=[
    dict(title="Pick an Architecture", level="Warm-up", concepts="hosting options, managed runtimes", new=True,
         text="Recommend an architecture for: a bank that cannot send data outside its tenant; a start-up prototype; a "
              "call centre with 50 million requests a month; a team using three model providers; a two-week agent pilot "
              "with no platform team.",
         sample="Bank: model hosted in its own cloud tenant\nStart-up: hosted API\n"
                "Call centre: evaluate a fine-tuned small model, self-hosted\nThree providers: AI gateway\n"
                "Agent pilot: managed agent runtime, retention checked",
         hints=["Ask about data rules, volume, skills, budget and retention."]),
    dict(title="Fail-fast Settings", level="Easy", concepts="environments, secrets",
         text="Write settings loading for dev, test and prod. In prod, missing secrets must stop the service at startup "
              "with a clear message. Never print a secret value.",
         sample="APP_ENV=prod without LLM_API_KEY -> RuntimeError: LLM_API_KEY missing in prod",
         hints=["Print 'set' or 'not set', never the value."]),
    dict(title="Version and Roll Back", level="Medium", concepts="prompt, dataset and embedding versioning",
         text="Keep a release registry with two manifests (prompt, golden set and embedding settings). Promote 1.9.0 to "
              "prod, detect that its embedding model differs, then roll back to 1.8.0 in one call.",
         sample="prod -> 1.9.0 (embed: embed-v4, index must be rebuilt)\nrollback -> prod = 1.8.0",
         hints=["Changing the embedding model means rebuilding the whole index."]),
    dict(title="AI Gateway with Budgets", level="Medium", concepts="gateway, allow-list, budgets", new=True,
         text="Build a FastAPI gateway that checks a client key, enforces a model allow-list and a daily token budget per "
              "team, and logs every call. Test allowed, wrong model, over budget and bad key.",
         sample="200 ok | 403 model not allowed | 429 budget exceeded | 401 bad key",
         hints=["Store hashes of client keys, not the keys.", "Prices and budgets are placeholders."]),
    dict(title="Short-lived Tokens for a Stateless MCP Server", level="Challenging",
         concepts="stateless MCP, scoped tokens, no long-lived keys", new=True,
         text="Issue HMAC-signed tokens with scopes and a 5-minute expiry. Protect a stateless /mcp endpoint with "
              "tools/list and tools/call. Show that a read-only token cannot call the refund tool and an expired token fails.",
         sample="tools/list -> 2 tools\ncall lookup_ticket (scope tickets.read) -> 200\n"
                "call refund (needs refunds.write) -> 403\nexpired token -> 401",
         hints=["Put exp and scopes inside the signed payload.", "This is a simplified protocol; Day 28 uses the real MCP SDK."]),
    dict(title="Concurrency Limit and Streaming", level="Medium", concepts="asyncio, semaphore, StreamingResponse",
         text="Simulate a provider that rejects more than 20 calls in flight. Send 100 requests unlimited and with a "
              "semaphore of 10. Then measure time to first chunk vs total time for the streaming endpoint.",
         sample="unlimited: 80 rejected | semaphore 10: 0 rejected\nstreaming: first chunk about 100 ms, full answer about 320 ms",
         hints=["TestClient buffers streams; measure with httpx.stream against a running uvicorn server."]),
    dict(title="Canary and Rollback Rules", level="Stretch", concepts="canary, rollback criteria",
         text="Route 10% of users to release 1.9 by a stable hash of their user id. Given canary and baseline metrics, "
              "decide promote, hold or rollback, and write rollback test notes.",
         sample="canary share: 9.3% of 5,000 users (close to 10%)\nerror rate 3.1% vs 1.0% -> ROLLBACK",
         hints=["Use hashlib, not Python's hash(), which changes between runs."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "Calling a provider's model over the internet is the hosted ________ pattern.",
        "A service where the provider runs the agent loop, tools and state is a managed agent ________.",
        "How long a provider keeps prompts and outputs is its data ________ policy.",
        "A single entry point for all model calls is an AI ________.",
        "An MCP server that keeps no session between requests is ________.",
        "Agents should receive short-lived tokens with limited ________.",
        "If a required secret is missing in production, the service should fail ________.",
        "An asyncio ________ limits how many calls run at once.",
        "Releasing to a small share of users first is a ________ release.",
        "If you change the embedding model, you must rebuild the whole ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Compare hosted, in-tenant, self-hosted and managed agent runtimes for a telecom customer.",
        "What questions would you ask about data retention before go-live?",
        "Explain why only the gateway should hold the provider key.",
        "How would you decide whether to promote or roll back a canary?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "import os\nos.environ[\"APP_ENV\"] = \"prod\"\nkey = os.getenv(\"LLM_API_KEY\")\nprint(\"start\" if key or os.getenv(\"APP_ENV\") != \"prod\" else \"fail fast\")",
        "import time\ntoken = {\"scopes\": [\"tickets.read\"], \"exp\": time.time() - 10}\nprint(\"refunds.write\" in token[\"scopes\"], token[\"exp\"] > time.time())",
        "releases = [\"1.8.0\", \"1.9.0\"]\nprod = releases[-1]\nprod = releases[releases.index(prod) - 1]\nprint(prod)",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write code that loads LLM_MODEL with a default and requires LLM_API_KEY in prod."),
        dict(q="Write a function issue_token(scopes, ttl_s) that returns a signed token with an expiry."),
        dict(q="Write a gateway check that rejects a model not on the allow-list with 403."),
        dict(q="Write a function that assigns 10% of users to a canary by hashing user ids."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="Hosting choices, versioning and rollback, an AI gateway, stateless MCP with short-lived tokens, "
                         "streaming and canary releases",
                sign_off="Yoi shuumatsu wo (良い週末を): *Have a great weekend*", cells=[
    ("md", "## 1. Install"),
    ("code", '''# ===== Option A: Google Colab (active) =====
# Add your key once: click the key icon (Secrets) in the left sidebar, name it OPENAI_API_KEY, and allow notebook access.
!pip install -q openai tiktoken scikit-learn numpy pandas fastapi httpx uvicorn nest_asyncio

# ===== Option B: VS Code / local =====
# pip install openai tiktoken scikit-learn numpy pandas fastapi httpx uvicorn nest_asyncio
# Create a .env file (git-ignored) or set the variable in your terminal:  OPENAI_API_KEY=...
# No key? Everything still runs in OFFLINE demo mode with a tiny built-in stand-in model.
print("Setup done")'''),
    ("helpers",),
    ("code", '''import asyncio, os, time, json, hashlib, hmac, base64, random

def run_async(coro):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)
    import nest_asyncio; nest_asyncio.apply()
    return loop.run_until_complete(coro)
print("ready")'''),
    ("md", "## 2. NEW (v4): Choosing where it runs, including managed agent runtimes\nA simple decision helper. Real "
           "decisions also need the customer's data policy and the provider's current retention terms."),
    ("code", '''def recommend(data_must_stay_in_tenant, monthly_requests, providers, has_platform_team, is_agent_pilot):
    if data_must_stay_in_tenant:
        return "cloud-hosted in the customer's tenant (or self-hosted open model)"
    if providers > 1:
        return "AI gateway in front of several hosted APIs"
    if is_agent_pilot and not has_platform_team:
        return "managed agent runtime (check retention, region and trace export)"
    if monthly_requests > 20_000_000:
        return "evaluate a fine-tuned small model, self-hosted, behind a gateway"
    return "hosted model API"

cases = {"bank": (True, 2_000_000, 1, True, False), "start-up": (False, 50_000, 1, False, False),
         "call centre": (False, 50_000_000, 1, True, False), "three providers": (False, 5_000_000, 3, True, False),
         "agent pilot": (False, 20_000, 1, False, True)}
for name, args in cases.items():
    print(f"{name:<16} -> {recommend(*args)}")

RETENTION_CHECKLIST = ["Provider API: are prompts and outputs stored, and for how long?",
                       "Managed runtime: where are conversation state and traces kept?",
                       "Our logs: who can read raw prompts; how long are they kept?",
                       "Memory stores: TTL per user; delete on request?"]
print("\\nData retention checklist (confirm current terms with the provider):")
print("\\n".join(" - " + c for c in RETENTION_CHECKLIST))'''),
    ("md", "## 3. Settings per environment, with fail-fast secrets"),
    ("code", '''def load_settings():
    env = os.getenv("APP_ENV", "dev")
    s = {"env": env, "model": os.getenv("LLM_MODEL", MODEL), "max_concurrency": int(os.getenv("MAX_CONCURRENCY", "10")),
         "api_key": os.getenv("LLM_API_KEY")}
    if env == "prod" and not s["api_key"]:
        raise RuntimeError("LLM_API_KEY missing in prod: refusing to start")
    return {**s, "api_key": "set" if s["api_key"] else "not set"}       # never print the real value

print(load_settings())
os.environ["APP_ENV"] = "prod"
try:
    load_settings()
except RuntimeError as e:
    print("Startup blocked:", e)
os.environ["APP_ENV"] = "dev"'''),
    ("md", "## 4. Versioning prompts, datasets and embeddings, and rolling back"),
    ("code", '''def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()[:6]

RELEASES = {
    "1.8.0": {"prompt": {"id": "answer_v7", "sha": sha("Answer using ONLY the context. Cite ids.")},
              "golden_set": {"id": "golden_v8", "sha": sha("golden v8 rows")},
              "embedding": {"model": "embed-v3", "chunk_tokens": 400, "index": "idx-2026-12-01"}},
    "1.9.0": {"prompt": {"id": "answer_v8", "sha": sha("Answer using ONLY the context. Cite ids. Max 3 sentences.")},
              "golden_set": {"id": "golden_v9", "sha": sha("golden v9 rows")},
              "embedding": {"model": "embed-v4", "chunk_tokens": 400, "index": "idx-2026-12-10"}},
}
ENVIRONMENTS = {"dev": "1.9.0", "test": "1.9.0", "prod": "1.8.0"}
HISTORY = {"prod": ["1.8.0"]}

def promote(env, release):
    old, new = RELEASES[ENVIRONMENTS[env]], RELEASES[release]
    if old["embedding"]["model"] != new["embedding"]["model"]:
        print(f"  note: embedding model {old['embedding']['model']} -> {new['embedding']['model']}: index {new['embedding']['index']} must be fully rebuilt")
    ENVIRONMENTS[env] = release
    HISTORY.setdefault(env, []).append(release)
    print(f"{env} -> {release}")

def rollback(env):
    HISTORY[env].pop()
    ENVIRONMENTS[env] = HISTORY[env][-1]
    print(f"rollback -> {env} = {ENVIRONMENTS[env]}")

promote("prod", "1.9.0")
rollback("prod")
print(ENVIRONMENTS)'''),
    ("md", "## 5. NEW (v4): An AI gateway with client keys, a model allow-list and budgets\nOnly the gateway knows the "
           "provider key. Clients have their own keys; the gateway stores only their hashes. Budgets are placeholders."),
    ("code", '''%%writefile gateway.py
import hashlib, json, os, time
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="SmartDesk AI gateway")
ALLOWED_MODELS = {os.getenv("LLM_MODEL", "gpt-6.1-sol"), "small-model"}          # approved list, from config
CLIENTS = {hashlib.sha256(b"team-support-key").hexdigest(): {"team": "support", "daily_tokens": 2000}}  # demo key hash
USED = {}
LOG = []

class ChatIn(BaseModel):
    model: str
    text: str = Field(min_length=1, max_length=4000)

def fake_model(text):
    return f"[offline gateway answer] {text[:40]}", len(text) // 4 + 1, 20

@app.post("/v1/chat")
def chat(req: ChatIn, x_client_key: str = Header()):
    client = CLIENTS.get(hashlib.sha256(x_client_key.encode()).hexdigest())
    if not client:
        raise HTTPException(401, "unknown client key")
    if req.model not in ALLOWED_MODELS:
        raise HTTPException(403, f"model {req.model} not on the allow-list")
    used = USED.get(client["team"], 0)
    answer, tin, tout = fake_model(req.text)        # the real provider call uses the gateway's key from Key Vault
    if used + tin + tout > client["daily_tokens"]:
        raise HTTPException(429, "daily token budget exceeded")
    USED[client["team"]] = used + tin + tout
    LOG.append({"ts": time.time(), "team": client["team"], "model": req.model, "tokens_in": tin, "tokens_out": tout})
    return {"answer": answer, "tokens": tin + tout, "budget_left": client["daily_tokens"] - USED[client["team"]]}'''),
    ("code", '''import importlib, gateway
importlib.reload(gateway)
from fastapi.testclient import TestClient
gw = TestClient(gateway.app)
ok_model = next(iter(gateway.ALLOWED_MODELS))
H = {"x-client-key": "team-support-key"}
print("allowed     :", gw.post("/v1/chat", json={"model": ok_model, "text": "My bill doubled"}, headers=H).status_code)
print("wrong model :", gw.post("/v1/chat", json={"model": "random-model", "text": "hi"}, headers=H).status_code)
print("bad key     :", gw.post("/v1/chat", json={"model": ok_model, "text": "hi"}, headers={"x-client-key": "guess"}).status_code)
codes = [gw.post("/v1/chat", json={"model": ok_model, "text": "long question " * 100}, headers=H).status_code for _ in range(8)]
print("budget run  :", codes, "(429 = budget exceeded)")
print("log lines   :", len(gateway.LOG))'''),
    ("md", "## 6. NEW (v4): Stateless MCP-style server with short-lived, scoped tokens\nA simplified JSON-RPC handler "
           "that keeps no session: every request carries a signed token with scopes and an expiry. Day 28 uses the "
           "real MCP SDK; the security idea is the same."),
    ("code", '''SIGNING_KEY = os.urandom(32)          # in production: from Key Vault, rotated; never in code

def issue_token(sub, scopes, ttl_s=300):
    payload = json.dumps({"sub": sub, "scopes": scopes, "exp": time.time() + ttl_s}).encode()
    sig = hmac.new(SIGNING_KEY, payload, "sha256").hexdigest()
    return base64.urlsafe_b64encode(payload).decode() + "." + sig

def verify(token):
    try:
        body, sig = token.split(".")
        payload = base64.urlsafe_b64decode(body.encode())
    except Exception:
        raise PermissionError("malformed token")
    if not hmac.compare_digest(hmac.new(SIGNING_KEY, payload, "sha256").hexdigest(), sig):
        raise PermissionError("bad signature")
    claims = json.loads(payload)
    if claims["exp"] < time.time():
        raise PermissionError("expired")
    return claims

from fastapi import FastAPI, Header, HTTPException
mcp_app = FastAPI(title="SmartDesk tickets MCP (simplified, stateless)")
TOOLS = [{"name": "lookup_ticket", "scope": "tickets.read"}, {"name": "refund", "scope": "refunds.write"}]

@mcp_app.post("/mcp")
def mcp(req: dict, authorization: str = Header()):
    try:
        claims = verify(authorization.removeprefix("Bearer "))
    except PermissionError as e:
        raise HTTPException(401, str(e))
    if req.get("method") == "tools/list":
        return {"jsonrpc": "2.0", "id": req.get("id"), "result": {"tools": [t["name"] for t in TOOLS]}}
    if req.get("method") == "tools/call":
        tool = next((t for t in TOOLS if t["name"] == req["params"]["name"]), None)
        if tool is None:
            raise HTTPException(404, "unknown tool")
        if tool["scope"] not in claims["scopes"]:
            raise HTTPException(403, f"missing scope {tool['scope']}")
        return {"jsonrpc": "2.0", "id": req.get("id"), "result": {"ok": True, "tool": tool["name"], "by": claims["sub"]}}
    raise HTTPException(400, "unknown method")

mc = TestClient(mcp_app)
read_only = issue_token("agent-triage", ["tickets.read"])
expired = issue_token("agent-triage", ["tickets.read"], ttl_s=-1)
auth = lambda t: {"authorization": "Bearer " + t}
print("tools/list            :", mc.post("/mcp", json={"jsonrpc": "2.0", "id": 1, "method": "tools/list"}, headers=auth(read_only)).json()["result"])
print("call lookup_ticket    :", mc.post("/mcp", json={"id": 2, "method": "tools/call", "params": {"name": "lookup_ticket"}}, headers=auth(read_only)).status_code)
print("call refund (no scope):", mc.post("/mcp", json={"id": 3, "method": "tools/call", "params": {"name": "refund"}}, headers=auth(read_only)).status_code)
print("expired token         :", mc.post("/mcp", json={"id": 4, "method": "tools/list"}, headers=auth(expired)).status_code)'''),
    ("md", "**Why stateless helps:** any replica can answer any request, so you can scale out and restart freely. "
           "**Why short-lived tokens help:** a leaked token stops working in minutes, and it only opens the tools in its scopes."),
    ("md", "## 7. A production-style LLM service: timed pipeline, concurrency limit, streaming, canary\nThe model is "
           "simulated with realistic latency, so you can study the service without a key or a GPU."),
    ("code", '''%%writefile llm_service.py
import asyncio, os, random, time, hashlib
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

app = FastAPI(title="LLM Service")
LIMIT = asyncio.Semaphore(int(os.getenv("MAX_CONCURRENCY", "10")))
KB = {"roaming": "Roaming in Japan costs 980 JPY per day on the Travel plan.", "refund": "Refunds are paid within 14 days."}
RELEASES = {"stable": "1.8.0", "canary": "1.9.0"}
CANARY_PERCENT = int(os.getenv("CANARY_PERCENT", "10"))

class ChatIn(BaseModel):
    user_id: str
    text: str = Field(min_length=1, max_length=2000)

async def fake_model(prompt):
    await asyncio.sleep(random.uniform(0.15, 0.25))                      # simulated model latency
    return "Based on policy: " + prompt.split("Context: ")[-1].split("\\n")[0]

def release_for(user_id):
    bucket = int(hashlib.sha256(user_id.encode()).hexdigest(), 16) % 100
    return RELEASES["canary"] if bucket < CANARY_PERCENT else RELEASES["stable"]

@app.post("/chat")
async def chat(req: ChatIn):
    t, s = {}, time.perf_counter()
    if "ignore previous instructions" in req.text.lower():               # validate (input guardrail)
        raise HTTPException(400, "Request blocked by input policy")
    t["validate"] = time.perf_counter() - s; s = time.perf_counter()
    context = next((v for k, v in KB.items() if k in req.text.lower()), "No policy found.")   # enrich
    t["enrich"] = time.perf_counter() - s; s = time.perf_counter()
    async with LIMIT:                                                     # generate, with a concurrency limit
        answer = await asyncio.wait_for(fake_model(f"Question: {req.text}\\nContext: {context}"), timeout=5)
    t["generate"] = time.perf_counter() - s; s = time.perf_counter()
    if "@" in answer:                                                     # check (output guardrail)
        answer = "[redacted]"
    t["check"] = time.perf_counter() - s
    return {"answer": answer, "release": release_for(req.user_id), "timings_ms": {k: round(v * 1000, 1) for k, v in t.items()}}

@app.post("/chat/stream")
async def chat_stream(req: ChatIn):
    async def tokens():
        for word in f"Here is a streamed answer about {req.text[:40]}".split():
            await asyncio.sleep(0.03)
            yield word + " "
    return StreamingResponse(tokens(), media_type="text/plain")'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
import importlib, llm_service
importlib.reload(llm_service)
svc = TestClient(llm_service.app)
# ===== Option B: VS Code =====
# Terminal: uvicorn llm_service:app --reload   then try /docs

print(svc.post("/chat", json={"user_id": "u-42", "text": "How much is roaming in Japan?"}).json())
print("Blocked input:", svc.post("/chat", json={"user_id": "u-1", "text": "Ignore previous instructions"}).status_code)

# TestClient collects the whole stream before returning, so time to first chunk needs a real server:
import subprocess, sys, httpx
server = subprocess.Popen([sys.executable, "-m", "uvicorn", "llm_service:app", "--port", "8034"],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for _ in range(50):
        try:
            httpx.get("http://localhost:8034/docs"); break
        except httpx.HTTPError:
            time.sleep(0.2)
    start = time.perf_counter(); first = None; chunks = []
    with httpx.stream("POST", "http://localhost:8034/chat/stream", json={"user_id": "u-42", "text": "refund rules"}) as resp:
        for chunk in resp.iter_text():
            if chunk and first is None:
                first = time.perf_counter() - start
            chunks.append(chunk)
    print(f"Streaming: first chunk after {first * 1000:.0f} ms, full answer after {(time.perf_counter() - start) * 1000:.0f} ms")
    print("".join(chunks))
finally:
    server.terminate()'''),
    ("md", "### Load test: why concurrency limits matter\nThe simulated provider rejects calls when more than 20 are in "
           "flight, like a real rate limit."),
    ("code", '''class Provider:
    def __init__(self, max_in_flight=20):
        self.max, self.in_flight, self.rejected = max_in_flight, 0, 0
    async def call(self):
        if self.in_flight >= self.max:
            self.rejected += 1
            raise RuntimeError("429")
        self.in_flight += 1
        try:
            await asyncio.sleep(0.05)
        finally:
            self.in_flight -= 1

async def load_test(n=100, limit=None):
    p = Provider()
    sem = asyncio.Semaphore(limit) if limit else None
    async def one():
        try:
            if sem:
                async with sem:
                    await p.call()
            else:
                await p.call()
        except RuntimeError:
            pass
    t = time.perf_counter()
    await asyncio.gather(*[one() for _ in range(n)])
    return p.rejected, time.perf_counter() - t

for name, coro in [("unlimited", load_test()), ("semaphore 10", load_test(limit=10))]:
    rejected, secs = run_async(coro)
    print(f"{name:<13} rejected {rejected:>3} | total {secs:.2f} s")'''),
    ("md", "## 8. Canary routing and a rollback decision"),
    ("code", '''from collections import Counter
users = [f"u-{i}" for i in range(5000)]
counts = Counter(llm_service.release_for(u) for u in users)
print("Canary share:", f"{counts['1.9.0'] / len(users):.1%}", dict(counts))
print("u-42 is stable across calls:", len({llm_service.release_for("u-42") for _ in range(5)}) == 1)

def decide(canary, baseline):
    if canary["error_rate"] > baseline["error_rate"] * 2 or canary["p95_ms"] > baseline["p95_ms"] * 1.3:
        return "ROLLBACK"
    if canary["thumbs_down"] > baseline["thumbs_down"] + 0.02:
        return "HOLD and investigate"
    return "PROMOTE"

baseline = {"error_rate": 0.010, "p95_ms": 2400, "thumbs_down": 0.06}
for canary in [{"error_rate": 0.011, "p95_ms": 2300, "thumbs_down": 0.05},
               {"error_rate": 0.031, "p95_ms": 2500, "thumbs_down": 0.06},
               {"error_rate": 0.012, "p95_ms": 2450, "thumbs_down": 0.10}]:
    print(canary, "->", decide(canary, baseline))'''),
    ("md", "## 9. Deploying to Azure (in class, Azure window 2)\nThese commands need an Azure subscription and Docker "
           "Desktop, so they are skipped in offline checks. Read them; run them in class only."),
    ("code", '''# Azure Container Apps with two revisions for canary traffic (in class only)
# az acr build -r $ACR -t smartdesk-gateway:1.9.0 .
# az containerapp update -n smartdesk-gateway -g $RG --image $ACR.azurecr.io/smartdesk-gateway:1.9.0 --revision-suffix v190
# az containerapp ingress traffic set -n smartdesk-gateway -g $RG --revision-weight smartdesk-gateway--v180=90 smartdesk-gateway--v190=10
# Secrets: the provider key lives in Key Vault; the app reads it with a managed identity (no key in the image or YAML).
print("Azure deployment steps run in class only (subscription window).")''', ["skip-offline-check"]),
    ("md", "**TODO (SmartDesk step 29):** add a `/ready` endpoint that returns 503 when `LLM_API_KEY` is missing in prod, "
           "and put the gateway from section 5 in front of the streaming service."),
    ("code", "# TODO: write your code here"),
])
