"""Day 33 spec. GenAI 13: LLMOps (Assessment day).
Sources: archive/v1-40-day/Day31 (technical part: lifecycle, production failures, resilience) and
archive/v1-40-day/Day32 (MLOps vs LLMOps, fine-tuning, versioning, cost and latency). NEW (v4) topics are marked.
The FDE skills part of old Day 31 (escalations, emotional intelligence) moved to FDE-Mindset-Source.
"""
DAY = 33
FOLDER = "Day33-LLMOps"
SLUG = "LLMOps"
TITLE = "LLMOps"
SUBTITLE = "The LLM lifecycle, AgentOps, resilience, fine-tuning, versioning, and cost and latency"
DATE = "Thu 10 Dec 2026"
TRACK = "GenAI"
NEXT = "See you tomorrow for Day 34: LLM deployment and lifecycle."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 32"),
        ("Lifecycle and AgentOps", "Version prompts, tools, skills, MCP, models. NEW (v4)"),
        ("Resilience", "Failures, retries, fallbacks, circuit breakers"),
        ("LLMOps vs MLOps", "Fine-tuning, versioning, monitoring"),
        ("Cost and latency", "Builds on Day 25: trim, cache, route"),
        ("Assessment", "GenAI assessment 3, 1.5 hours"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Map the lifecycle", "Describe each stage of an LLM application and an agent's life."),
        ("Version everything", "Bundle prompts, tools, skills, MCP servers and models in one manifest."),
        ("Build resilience", "Add retries with backoff, fallbacks and a circuit breaker."),
        ("Control cost and latency", "Measure per request and pick the right lever."),
    ]),
    dict(type="section", title="The LLM lifecycle", sub="Shipping is the start, not the end"),
    dict(type="flow", title="Lifecycle of an LLM application", items=[
        ("Scope", "Use case, success metric, risks"),
        ("Build", "Prompts, RAG, tools, guardrails"),
        ("Evaluate", "Golden set, quality gate"),
        ("Deploy", "Environments, rollout"),
        ("Operate", "Monitor, improve, retire"),
    ], note="LLMOps is the discipline of running this loop reliably. Days 34 and 35 go deeper into deploy and operate."),
    dict(type="compare", title="What makes LLM apps different to operate", greet="Henka (変化): Change",
         left=dict(title="Traditional software", bullets=[
             "Same input, same output", "Bugs come from your code", "Costs mostly fixed"]),
         right=dict(title="LLM applications", bullets=[
             "Outputs vary run to run", "Behaviour changes when the provider updates or retires a model",
             "Cost grows with every token", "Quality can drift silently"])),
    dict(type="cards", title="AgentOps: what an agent is made of", new=True,
         lead="An agent is more than a prompt. Every part can change, so every part needs a version.", items=[
        ("Prompts", "System prompt, templates, few-shot examples."),
        ("Tools", "Function schemas and the code behind them."),
        ("Skills", "SKILL.md packages and AGENTS.md instructions."),
        ("MCP servers", "Server version, tool list, auth scopes."),
        ("Models", "Model name, version or snapshot, reasoning effort."),
        ("Data", "Index build, golden set, memory store schema."),
    ]),
    dict(type="bullets_code", title="An AgentOps release manifest", new=True, bullets=[
        "One file describes the whole agent",
        "A hash per part detects silent changes",
        "Rollback = deploy the previous manifest",
        "Store it with the eval report",
    ], code='''{
  "release": "smartdesk-agent-2.3.0",
  "prompts": {"system": "sys_v12@a41f9c"},
  "tools":   {"refund_tool": "1.4.0@77b2e0"},
  "skills":  {"triage": "SKILL.md@0c9d13"},
  "mcp_servers": {"tickets": "2.1.0"},
  "model":   {"name": "gpt-6.1-sol",
              "reasoning_effort": "medium"},
  "golden_set": "golden_v9"
}'''),
    dict(type="table", title="Model deprecation runbook", new=True, header=["Step", "What you do"], rows=[
        ["1. Watch", "Track provider deprecation notices and the approved model list weekly"],
        ["2. Inventory", "Find every manifest, notebook and agent that uses the retiring model"],
        ["3. Evaluate", "Run the golden set and cost check on the candidate replacement"],
        ["4. Canary", "Send a small share of traffic to the new model; compare metrics"],
        ["5. Switch", "Update the manifest, keep the old manifest for rollback until retirement"],
        ["6. Record", "Note the change, results and date in the decision log"],
    ], note="Example: GPT-5.5 retired from Codex for ChatGPT sign-ins on 14 Oct 2026. Teams migrated to the current default."),

    dict(type="section", title="What breaks in production", sub="Real failure modes and how to survive them"),
    dict(type="table", title="Common production failures", header=["Failure", "Signal", "First response"], rows=[
        ["Rate limits (429)", "Bursts of errors at peak time", "Backoff, queue, request a higher limit"],
        ["Timeouts and outages", "Latency spikes, 5xx from provider", "Retry, then fallback model"],
        ["Model update or retirement", "Golden pass rate drops; deprecation notice", "Pin version, run eval, follow the runbook"],
        ["Cost spike", "Tokens per request jump", "Find the prompt or loop causing it"],
        ["Retrieval breakage", "More \"I don't know\" answers", "Check index freshness and ingestion"],
        ["Tool or MCP change (NEW v4)", "Tool-call errors rise", "Pin tool and server versions, re-run tool tests"],
    ]),
    dict(type="bullets_code", title="Retry with exponential backoff", bullets=[
        "Retry only errors that may pass next time",
        "Wait longer after each failure",
        "Add jitter so clients do not retry together",
        "Give up after a few attempts",
    ], code='''import random, time

def call_with_retry(fn, attempts=4):
    for i in range(attempts):
        try:
            return fn()
        except (RateLimit, Timeout):
            if i == attempts - 1:
                raise
            wait = 2 ** i + random.random()
            time.sleep(wait)'''),
    dict(type="cards", title="Resilience patterns", items=[
        ("Fallback model", "If the main model fails, use a backup model or a cached answer."),
        ("Circuit breaker", "After repeated failures, stop calling for a while and fail fast."),
        ("Graceful message", "Tell the user clearly; never show a stack trace."),
        ("Timeouts everywhere", "Every external call, tool and MCP server has a limit."),
    ]),

    dict(type="section", title="LLMOps and MLOps", sub="Same goals, new moving parts"),
    dict(type="table", title="What changes", header=["Area", "Classic MLOps", "LLMOps"], rows=[
        ["Main artefact", "Your trained model", "Prompts, retrieval, tools + a provider model"],
        ["Training", "Frequent retraining", "Rare fine-tuning; mostly prompt and data changes"],
        ["Evaluation", "Accuracy on labelled data", "Golden sets, judges, faithfulness, trajectories"],
        ["Cost driver", "Training compute", "Tokens on every request"],
        ["Change risk", "New model release", "Prompt edits, tool changes, provider model updates"],
    ]),
    dict(type="table", title="Prompting, RAG or fine-tuning?", header=["Need", "Best first choice"], rows=[
        ["Answer from company documents that change", "RAG"],
        ["Follow a format or style consistently", "Structured outputs and examples, then fine-tuning"],
        ["Specialised classification at high volume", "Fine-tuning a smaller model, or an SLM (Day 25)"],
        ["Shorter prompts and lower latency for a fixed task", "Fine-tuning"],
        ["Up-to-date facts", "RAG or a tool (fine-tuning does not keep facts current)"],
    ], note="Try prompting first, add RAG for knowledge, fine-tune for behaviour.", greet="Shuren (習練): Practice and training"),
    dict(type="flow", title="A fine-tuning workflow", items=[
        ("Collect", "Real inputs and ideal outputs"),
        ("Clean", "Remove PII, fix errors, balance"),
        ("Split", "Train and validation sets"),
        ("Train", "Provider job or open model"),
        ("Evaluate", "Golden set vs base model"),
    ], note="Quality of examples matters more than quantity. Hundreds of excellent examples beat thousands of messy ones."),
    dict(type="bullets_code", title="Chat fine-tuning data (JSONL)", bullets=[
        "One conversation per line",
        "System, user and the ideal assistant reply",
        "Consistent style across examples",
        "Validate before uploading",
    ], code='''{"messages": [
  {"role": "system",
   "content": "Classify support tickets."},
  {"role": "user",
   "content": "I was charged twice"},
  {"role": "assistant",
   "content": "billing"}
]}'''),
    dict(type="cards", title="Monitoring: what to watch from day one", items=[
        ("Quality", "Golden pass rate, thumbs-down rate, \"I don't know\" rate."),
        ("Reliability", "Error rate by type, retries, breaker state."),
        ("Cost", "Tokens and cost per request, feature and day."),
        ("Versions", "Release manifest id on every log line (Day 35 goes deeper)."),
    ]),

    dict(type="section", title="Deployment, cost and latency", sub="Every token costs money and time"),
    dict(type="table", title="Where cost and latency come from", header=["Driver", "Effect", "Lever"], rows=[
        ["Input tokens", "Long prompts and contexts", "Trim context, prompt caching (Day 25)"],
        ["Output tokens", "Long answers; also slower", "Concise output, max tokens"],
        ["Reasoning effort", "Hidden tokens and time", "Lowest effort that passes the golden set"],
        ["Model size", "Bigger is slower and pricier", "Route easy requests to a small model or SLM"],
        ["Repeated questions", "Paying again for the same answer", "Cache answers or embeddings"],
        ["Agent loops", "Many calls per request", "Cap steps, cheaper models for sub-steps"],
    ], note="Prices change often. Keep them in configuration and label examples as placeholders."),
    dict(type="compare", title="Latency vs accuracy", left=dict(title="Optimise for speed", bullets=[
        "Chat and live support", "Smaller model, low reasoning effort", "Streaming, short answers", "Cache common questions",
    ]), right=dict(title="Optimise for accuracy", bullets=[
        "Refund decisions, compliance answers", "Default or top-tier model, higher effort",
        "Extra retrieval and re-ranking", "Human review for high-risk actions",
    ]), note="Decide per feature, write it down, and measure both on the golden set."),
    dict(type="callout", title="Assessment: GenAI assessment 3", text="1.5 hours on security, evaluation and LLMOps: "
         "guardrails, red-teaming, golden sets, quality gates, versioning, resilience and cost.",
         sub="Plan your time and attempt every question.", greet="Ganbatte kudasai (頑張ってください): Please do your best"),
    dict(type="cards", title="SmartDesk step 28: resilient client and dashboard", items=[
        ("Resilient client", "Retries with jitter, fallback model, circuit breaker, timeouts."),
        ("Release manifest", "Prompts, tools, skills, MCP servers and model with hashes."),
        ("Cost and version dashboard", "Cost per feature per day, by release id."),
        ("Build with Codex", "Use Day33_App_Build_Prompts.md. Review every line Codex writes."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("Lifecycle", "Scope, build, evaluate, deploy, operate. Then repeat."),
        ("AgentOps", "Version prompts, tools, skills, MCP servers and models together."),
        ("Resilience", "Backoff with jitter, fallbacks, circuit breakers, timeouts."),
        ("Cost and latency", "Measure per request; trim, cache, route, cap."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day33_Hotel_Lab.md: failures, retries, cost comparison."),
        ("Workbook", "Complete the Day 33 workbook."),
        ("Pre-read", "Skim the Day 34 pre-read on deploying AI services."),
    ]),
]

PREREAD = dict(title="Keeping AI Running Day After Day", lede="A light read before Day 33. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "Building an AI feature is the exciting part. Keeping it working every day, for thousands of users, is where most "
        "of the real work happens. Tomorrow is about running AI in production. It is also an assessment day."]),
    dict(h="1. A car needs servicing", paras=[
        "Buying a car is not the end; it needs fuel, servicing and repairs. AI applications are similar. The model "
        "provider updates models, users ask new kinds of questions, costs change. Running AI reliably is called **LLMOps**."]),
    dict(h="2. How AI apps break", table=[
        ["Problem", "Everyday comparison"],
        ["Too many requests at once (rate limits)", "A shop that only lets 50 people in at a time"],
        ["The AI provider is slow or down", "A supplier who does not deliver on time"],
        ["The model changes or is retired", "A favourite restaurant changes its chef, or closes"],
        ["Costs suddenly jump", "A phone bill that doubles because an app kept running"],
    ], after=["Good systems expect these problems: they try again sensibly, switch to a backup, and tell users clearly "
              "when something is wrong."]),
    dict(h="3. Knowing exactly what you shipped", new=True, paras=[
        "A pharmacy records the batch number of every medicine. AI teams do the same: they record the exact prompt, "
        "tools, skills, connected services and model behind every release. For agents this is called **AgentOps**."]),
    dict(h="4. Every word has a price", paras=[
        "AI services charge by the token. Teams cut cost by keeping prompts lean, reusing answers to repeated questions, "
        "and sending easy questions to smaller, cheaper models. You practised this on Day 25."],
        box="**Key idea:** you cannot manage what you do not measure. Log versions, tokens and latency for every request."),
    dict(h="5. About tomorrow's assessment", paras=[
        "Day 33 includes GenAI assessment 3 (1.5 hours): security and guardrails (Day 30), evaluation (Days 31 and 32) "
        "and LLMOps. Review those post-reads tonight."]),
    dict(h="6. Think about these before class", bullets=[
        "Recall a time a service you rely on failed. How did the company handle it?",
        "What would you need to record to explain an AI answer given six months ago?",
        "If your favourite AI model were retired next month, what would you need to check before switching?"],
        after=["Kiroku (記録): a record, keeping records"]),
])

POSTREAD = dict(title="LLMOps: Recap and Beyond", lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["LLM lifecycle", "Scope, build, evaluate, deploy, operate, and loop back."],
        ["AgentOps (NEW v4)", "Version prompts, tools, skills, MCP servers and models in one manifest with hashes."],
        ["Deprecation runbook (NEW v4)", "Watch, inventory, evaluate, canary, switch, record."],
        ["Failure modes", "Rate limits, timeouts, model updates, cost spikes, retrieval breaks, tool changes."],
        ["Resilience", "Backoff with jitter, fallbacks, circuit breakers, timeouts everywhere."],
        ["MLOps vs LLMOps", "LLMOps adds prompts, provider models, token costs, judges and drift."],
        ["Fine-tuning", "For behaviour, format or efficiency at volume; not for fresh facts."],
        ["Cost and latency", "Tokens x price; p50 and p95; trim, cache, route, cap agent steps."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Pin model versions", paras=[
        "Where the provider offers dated snapshots, use them in production and upgrade deliberately after running your "
        "golden set, instead of letting an alias change underneath you."]),
    dict(sub="2. Idempotent retries", paras=[
        "Retrying a request that triggers an action (send email, issue refund) can duplicate it. Use idempotency keys or "
        "check whether the action already happened before retrying."]),
    dict(sub="3. Distillation and parameter-efficient fine-tuning", paras=[
        "Use a large model to produce reviewed, high-quality outputs, then fine-tune a smaller model on them. For open "
        "models, LoRA trains small adapter layers instead of the whole model."]),
    dict(sub="4. Skills and MCP servers are supply chain (NEW v4)", paras=[
        "A skill or MCP server you did not write can change behaviour or leak data. Pin versions, review changes like "
        "code, and keep an allow-list. This links back to the Day 23 SME session."]),
    dict(sub="5. Budgets and alerts", paras=[
        "Set daily cost budgets per feature and alert at 80 percent. A runaway agent loop can burn a month's budget in hours."]),
    dict(h="Part C: Check yourself", bullets=[
        "What belongs in an AgentOps release manifest, and why hash each part?",
        "List the six steps of a model deprecation runbook.",
        "Which errors should you retry, and which should you never retry?",
        "Give one case where fine-tuning is right and one where RAG is right.",
        "How would you trade latency against accuracy for a refund decision?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Write a release manifest for SmartDesk with every prompt, tool and model it uses.",
        "Write a deprecation runbook entry for the model your SmartDesk assistant uses today.",
        "Add a circuit breaker to your SmartDesk LLM client."],
        after=["**Coming up on Day 34:** LLM deployment and lifecycle: managed agent runtimes, AI gateways, environments, "
               "secrets, streaming and canary releases.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems. Every notebook cell runs offline. Prices in the notebook are placeholders, not real "
                    "prices.", problems=[
    dict(title="Read the Incident Logs", level="Warm-up", concepts="log analysis",
         text="Using the notebook's simulated week of LLM logs, find when errors spiked, which error code dominated, and "
              "when tokens per request jumped.",
         sample="Errors peak 10:00 to 11:00 on 2026-12-02, mostly 429\nTokens per request triple from 2026-12-04",
         hints=["Group by hour and status; plot tokens per request by day."]),
    dict(title="Backoff with Jitter", level="Easy", concepts="retries",
         text="Wrap the flaky provider in a retry function with exponential backoff and jitter. Measure success rate with "
              "0, 2 and 4 retries.",
         sample="retries=0: 70% | retries=2: 98% | retries=4: 100%",
         hints=["Retry only transient errors, never 400 Bad Request."]),
    dict(title="Fallback and Circuit Breaker", level="Medium", concepts="resilience patterns",
         text="Add a fallback model and a circuit breaker that opens after 3 consecutive failures. Show the user always "
              "gets a response.",
         sample="breaker OPEN -> served by fallback\nafter cool-down -> HALF-OPEN -> CLOSED",
         hints=["Track consecutive failures and the time the breaker opened."]),
    dict(title="AgentOps Manifest", level="Medium", concepts="versioning prompts, tools, skills, MCP, models", new=True,
         text="Build a release manifest for the SmartDesk agent with a short hash for every prompt, tool schema, skill "
              "file and MCP server version. Change one tool description and show which part of the manifest changed.",
         sample="changed parts: ['tools.refund_tool']\nmanifest 2.3.0 -> 2.3.1",
         hints=["hashlib.sha256(text.encode()).hexdigest()[:6]", "Hash the tool schema as sorted JSON."]),
    dict(title="Model Deprecation Drill", level="Medium", concepts="deprecation runbook", new=True,
         text="Given a list of manifests and a deprecation notice for one model, list every affected release, run the "
              "golden set on the candidate model (offline stand-in), and write the runbook decision.",
         sample="affected: ['smartdesk-agent-2.3.0', 'faq-bot-1.1.0']\ncandidate pass rate 0.92 >= 0.90 -> CANARY",
         hints=["Use the approved model list in docs/MODEL_GUIDE.md as the source of candidates."]),
    dict(title="Cost per Feature and Two Model Choices", level="Medium", concepts="token accounting, placeholders",
         text="From the simulated request log, compute cost per feature, then compare the monthly cost of serving the FAQ "
              "bot with the large and the small model using placeholder prices.",
         sample="agent_research: 45% of cost from 9% of requests\nfaq_bot all-small: 6% of all-large cost (placeholder prices)",
         hints=["Look for features with long contexts or many calls per request."]),
    dict(title="Routing Trade-off", level="Stretch", concepts="cost vs quality, latency vs accuracy",
         text="Route easy questions to the small model and hard ones to the large model. Compare cost and simulated "
              "quality for all-large, all-small and routed, then write a one-paragraph recommendation.",
         sample="all large: cost 100%, quality 0.921\nrouted: cost 34%, quality 0.914 (simulated quality)",
         hints=["Validate routing on your golden set before trusting it."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "Running LLM applications reliably in production is called ________.",
        "Versioning an agent's prompts, tools, skills, MCP servers and models together is part of ________.",
        "HTTP status 429 means too many ________.",
        "Adding randomness to retry waits is called ________.",
        "Stopping calls for a while after repeated failures is a circuit ________.",
        "Fine-tuning is best for teaching ________, not fresh facts.",
        "A file that records every version behind a release is a release ________.",
        "Cost = input tokens x input price + output tokens x ________ price.",
        "p95 latency means 95% of requests are ________ than this value.",
        "Sending easy questions to a smaller model is called ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Why are LLM applications harder to operate than traditional software?",
        "Describe the steps you would follow when a model your agent uses is being retired.",
        "Describe how retries, fallbacks and circuit breakers work together.",
        "For SmartDesk, which feature should optimise for latency and which for accuracy? Why?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "for i in range(4):\n    print(2 ** i, end=\" \")",
        "failures, threshold = 0, 3\nfor ok in [False, False, True, False, False, False]:\n    failures = 0 if ok else failures + 1\nprint(\"OPEN\" if failures >= threshold else \"CLOSED\")",
        "old = {\"prompt\": \"a41f\", \"tool\": \"77b2\"}\nnew = {\"prompt\": \"a41f\", \"tool\": \"91c0\"}\nprint([k for k in old if old[k] != new[k]])",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a retry function with exponential backoff, jitter and a maximum of 3 attempts."),
        dict(q="Write a function that builds an AgentOps manifest with a short hash for each prompt and tool."),
        dict(q="Write one chat fine-tuning example in JSONL for classifying a support ticket."),
        dict(q="Write a cost function that reads placeholder prices from a dictionary."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="The LLM lifecycle, AgentOps, resilience, fine-tuning, versioning, and cost and latency", cells=[
    ("md", "## 1. Install"),
    ("code", '''# ===== Option A: Google Colab (active) =====
# Add your key once: click the key icon (Secrets) in the left sidebar, name it OPENAI_API_KEY, and allow notebook access.
!pip install -q openai tiktoken scikit-learn numpy pandas matplotlib

# ===== Option B: VS Code / local =====
# pip install openai tiktoken scikit-learn numpy pandas matplotlib
# Create a .env file (git-ignored) or set the variable in your terminal:  OPENAI_API_KEY=...
# No key? Everything still runs in OFFLINE demo mode with a tiny built-in stand-in model.
print("Setup done")'''),
    ("helpers",),
    ("md", "## 2. Incident simulation: a week of LLM request logs\nPlanted events: a rate-limit storm on 2 Dec and a "
           "prompt change that triples the context from 4 Dec."),
    ("code", '''import numpy as np, pandas as pd, matplotlib.pyplot as plt
rng = np.random.default_rng(31)
n = 8000
ts = pd.Timestamp("2026-11-30") + pd.to_timedelta(rng.integers(0, 7 * 24 * 60, n), unit="min")
logs = pd.DataFrame({"ts": ts, "model": "main-model-v1", "status": 200,
                     "latency_ms": rng.gamma(4, 300, n).round(), "tokens": rng.normal(900, 150, n).round()})
day, hour = logs.ts.dt.date.astype(str), logs.ts.dt.hour
burst = (day == "2026-12-02") & (hour == 10)                            # rate limit storm
logs.loc[burst & (rng.random(n) < 0.55), "status"] = 429
logs.loc[rng.random(n) < 0.01, "status"] = 503                          # background provider errors
logs.loc[logs.ts >= "2026-12-04", "tokens"] *= 3                        # a prompt change added a huge context
logs.loc[logs.status != 200, "latency_ms"] = rng.integers(20000, 30000, (logs.status != 200).sum())
logs = logs.sort_values("ts").reset_index(drop=True)

by_hour = logs.set_index("ts").resample("1h").agg(errors=("status", lambda s: (s != 200).mean()))
worst = by_hour.errors.idxmax()
print(f"Worst hour: {worst} with {by_hour.errors.max():.0%} errors")
print("Status codes in that hour:",
      logs[(logs.ts >= worst) & (logs.ts < worst + pd.Timedelta("1h"))].status.value_counts().to_dict())
daily_tokens = logs.groupby(logs.ts.dt.date)["tokens"].mean().round()
print("\\nAverage tokens per request by day:\\n", daily_tokens.to_string())

fig, ax = plt.subplots(1, 2, figsize=(11, 3.5))
by_hour.errors.plot(ax=ax[0], color="#FF8A3D", title="Error rate per hour")
daily_tokens.plot(ax=ax[1], kind="bar", color="#0FA3A3", title="Average tokens per request")
plt.tight_layout(); plt.show()'''),
    ("md", "## 3. A flaky provider: retries with backoff and jitter\nThe simulated provider fails 30% of the time with "
           "transient errors. Waits are scaled down so the demo runs fast."),
    ("code", '''import random, time

class Transient(Exception):
    pass

class FlakyProvider:
    def __init__(self, fail_rate, name):
        self.fail_rate, self.name, self.calls = fail_rate, name, 0
    def complete(self, prompt):
        self.calls += 1
        if random.random() < self.fail_rate:
            raise Transient(f"{self.name}: 429 or timeout")
        return f"[{self.name}] answer to: {prompt[:30]}"

def with_retry(fn, retries=3, base=0.001):
    for attempt in range(retries + 1):
        try:
            return fn()
        except Transient:
            if attempt == retries:
                raise
            time.sleep(base * (2 ** attempt) + random.random() * base)    # exponential backoff with jitter

random.seed(31)
main = FlakyProvider(0.30, "main")
for retries in [0, 2, 4]:
    ok = 0
    for i in range(500):
        try:
            with_retry(lambda: main.complete("hello"), retries=retries); ok += 1
        except Transient:
            pass
    print(f"retries={retries}: success {ok / 500:.0%}")'''),
    ("md", "## 4. Fallback model and circuit breaker"),
    ("code", '''class CircuitBreaker:
    def __init__(self, threshold=3, cooldown=0.05):
        self.threshold, self.cooldown = threshold, cooldown
        self.failures, self.opened_at, self.state = 0, None, "CLOSED"
        self.log = ["CLOSED"]

    def _set(self, state):
        if state != self.state:
            self.state = state
            self.log.append(state)

    def call(self, fn):
        if self.state == "OPEN":
            if time.time() - self.opened_at < self.cooldown:
                raise Transient("circuit open")
            self._set("HALF-OPEN")
        try:
            result = fn()
            self.failures = 0
            self._set("CLOSED")
            return result
        except Transient:
            self.failures += 1
            if self.failures >= self.threshold or self.state == "HALF-OPEN":
                self._set("OPEN")
                self.opened_at = time.time()
            raise

random.seed(7)
outage = FlakyProvider(0.95, "main")          # the main provider is having an outage
backup = FlakyProvider(0.02, "backup")
breaker = CircuitBreaker()
served = {"main": 0, "backup": 0, "error message": 0}
for i in range(40):
    time.sleep(0.005)                          # requests arrive over time, so the cool-down can expire
    try:
        breaker.call(lambda: outage.complete("Where is my order?")); served["main"] += 1
    except Transient:
        try:
            with_retry(lambda: backup.complete("Where is my order?"), retries=1); served["backup"] += 1
        except Transient:
            served["error message"] += 1
print("Served by:", served)
print("Calls that reached the failing main provider:", outage.calls, "out of 40 requests")
print("Breaker transitions:", " -> ".join(breaker.log[:9]), "...")'''),
    ("md", "**TODO 1:** make the circuit breaker log every state change with a timestamp, and add a `served_from_cache` "
           "option for frequent questions."),
    ("code", "# TODO: write your code here"),
    ("md", "## 5. NEW (v4): AgentOps, a release manifest for the whole agent\nAn agent is prompts, tools, skills, MCP "
           "servers and a model. Hash each part so any silent change shows up."),
    ("code", '''import hashlib, json, copy

def h(obj):
    text = obj if isinstance(obj, str) else json.dumps(obj, sort_keys=True)
    return hashlib.sha256(text.encode()).hexdigest()[:6]

agent = {
    "prompts": {"system": "You are SmartDesk, a telecom support agent. Cite policy ids. Never promise refunds over 5,000 JPY."},
    "tools": {"refund_tool": {"name": "refund", "description": "Issue a refund up to 5,000 JPY",
                              "parameters": {"ticket_id": "int", "amount_jpy": "int"}},
              "lookup_ticket": {"name": "lookup_ticket", "description": "Read a ticket by id", "parameters": {"ticket_id": "int"}}},
    "skills": {"triage": "# SKILL.md\\nClassify tickets as billing, network or account before answering."},
    "mcp_servers": {"tickets": "2.1.0"},
    "model": {"name": MODEL, "reasoning_effort": "medium"},   # model name from LLM_MODEL; see docs/MODEL_GUIDE.md
}

def manifest(agent, release):
    return {"release": release,
            "prompts": {k: h(v) for k, v in agent["prompts"].items()},
            "tools": {k: h(v) for k, v in agent["tools"].items()},
            "skills": {k: h(v) for k, v in agent["skills"].items()},
            "mcp_servers": dict(agent["mcp_servers"]),
            "model": dict(agent["model"]),
            "golden_set": "golden_v9"}

def changed_parts(a, b):
    out = []
    for part in ["prompts", "tools", "skills", "mcp_servers", "model"]:
        for k in set(a[part]) | set(b[part]):
            if a[part].get(k) != b[part].get(k):
                out.append(f"{part}.{k}")
    return out

m1 = manifest(agent, "smartdesk-agent-2.3.0")
agent2 = copy.deepcopy(agent)
agent2["tools"]["refund_tool"]["description"] = "Issue a refund up to 10,000 JPY"     # a risky silent change
m2 = manifest(agent2, "smartdesk-agent-2.3.1")
print(json.dumps(m1, indent=2))
print("changed parts:", changed_parts(m1, m2))'''),
    ("md", "**Why it matters:** the tool change above doubles the refund limit without touching the prompt. Only a "
           "per-part hash makes that visible in review."),
    ("md", "## 6. NEW (v4): Model deprecation runbook drill\nA provider announces a retirement. Find every affected "
           "release, evaluate a candidate on the golden set, then decide. Example from 2026: GPT-5.5 retired from Codex "
           "for ChatGPT sign-ins on 14 Oct 2026. Confirm candidates against the approved model list."),
    ("code", '''manifests = [
    {"release": "smartdesk-agent-2.3.0", "model": "legacy-model-a"},
    {"release": "faq-bot-1.1.0", "model": "legacy-model-a"},
    {"release": "summariser-0.9.0", "model": MODEL},
]
notice = {"retiring": "legacy-model-a", "date": "2027-01-31"}
candidate = MODEL                                          # confirm against docs/MODEL_GUIDE.md

affected = [m["release"] for m in manifests if m["model"] == notice["retiring"]]
print("1. Watch    : notice for", notice["retiring"], "retiring on", notice["date"])
print("2. Inventory: affected releases", affected)

GOLDEN = [("Classify this ticket: I was charged twice for my plan", "billing"),
          ("Classify this ticket: No signal at home since Monday", "network"),
          ("Classify this ticket: Cannot log in after password reset", "account"),
          ("Classify this ticket: Refund for duplicate invoice", "billing"),
          ("Classify this ticket: 5G data is very slow downtown", "network")]
passed = sum(llm("Reply with one word: billing, network or account.\\n" + q, model=candidate).strip().lower() == want
             for q, want in GOLDEN)
rate = passed / len(GOLDEN)
print(f"3. Evaluate : candidate {candidate} golden pass rate {rate:.2f} (offline scores show the code path only)")
decision = "CANARY" if rate >= 0.9 else "HOLD: fix prompts or try another approved model"
print("4. Canary   :", decision)
print("5. Switch   : update manifests, keep previous manifests for rollback until", notice["date"])
print("6. Record   : decision log entry written")'''),
    ("md", "## 7. LLMOps vs MLOps: preparing fine-tuning data"),
    ("code", '''import re
random.seed(32)
templates = {
    "billing": ["I was charged twice for order {o}", "Refund for {o} not received", "Invoice amount is wrong, contact me at {e}"],
    "network": ["No signal at home near {o}", "Data is very slow today", "Calls drop all the time, call me on {p}"],
    "account": ["Cannot log in to my account", "Change the plan on {o}", "SIM swap request, email {e}"],
}
rows = []
for label, ts_ in templates.items():
    for _ in range(20):
        t = random.choice(ts_).format(o=f"ORD-{random.randint(1000, 9999)}", e="mei@example.com", p="+81 90 1234 5678")
        rows.append({"text": t, "label": label})

PII = [r"[\\w.+-]+@[\\w-]+\\.[\\w.]+", r"\\+?\\d{1,3}[ -]?\\d{2,5}[ -]?\\d{3,4}[ -]?\\d{3,4}"]
def scrub(t):
    for p in PII:
        t = re.sub(p, "[redacted]", t)
    return t

SYSTEM = "Classify the support ticket as billing, network or account. Reply with one word."
examples, pii_removed = [], 0
for r in rows:
    clean = scrub(r["text"]); pii_removed += clean != r["text"]
    examples.append({"messages": [{"role": "system", "content": SYSTEM},
                                  {"role": "user", "content": clean},
                                  {"role": "assistant", "content": r["label"]}]})

def valid(ex):
    m = ex["messages"]
    return ([x["role"] for x in m] == ["system", "user", "assistant"] and all(x["content"].strip() for x in m)
            and m[2]["content"] in templates)

random.shuffle(examples)
split = int(len(examples) * 0.8)
for name, part in [("train.jsonl", examples[:split]), ("val.jsonl", examples[split:])]:
    with open(name, "w") as f:
        for ex in part:
            f.write(json.dumps(ex) + "\\n")
print(f"Valid: {sum(map(valid, examples))}/{len(examples)} | PII removed: {pii_removed} | train {split}, validation {len(examples) - split}")
print(examples[0])'''),
    ("code", '''import os
RUN_FINE_TUNE = False     # costs money: set True only with trainer approval, an API key and an approved fine-tunable model
if ONLINE and RUN_FINE_TUNE:
    import genai_helpers
    c = genai_helpers.client
    train_file = c.files.create(file=open("train.jsonl", "rb"), purpose="fine-tune")
    val_file = c.files.create(file=open("val.jsonl", "rb"), purpose="fine-tune")
    job = c.fine_tuning.jobs.create(training_file=train_file.id, validation_file=val_file.id,
                                    model=os.environ["FT_BASE_MODEL"])    # set from the approved model list
    print("Started fine-tuning job:", job.id)
else:
    print("Fine-tuning not started (RUN_FINE_TUNE is False). The data files are ready: train.jsonl, val.jsonl")'''),
    ("md", "## 8. A prompt registry and release manifest"),
    ("code", '''import difflib, os
registry = {}
def register(pid, text, note):
    registry[pid] = {"text": text, "sha": h(text), "note": note}
    return registry[pid]["sha"]

register("answer_v7", "Answer using ONLY the context.\\nCite chunk ids.\\nIf unsure, say I don't know.", "baseline")
register("answer_v8", "Answer using ONLY the context.\\nCite chunk ids.\\nAnswer in at most 3 sentences.\\nIf unsure, say I don't know.",
         "shorter answers to cut output tokens")
for line in difflib.unified_diff(registry["answer_v7"]["text"].splitlines(), registry["answer_v8"]["text"].splitlines(),
                                 "answer_v7", "answer_v8", lineterm=""):
    print(line)'''),
    ("md", "## 9. Cost and latency from request logs\n**The prices below are placeholders, not real prices.** Replace "
           "them with the approved price sheet. This builds on the Day 25 token cost calculator."),
    ("code", '''PRICES = {"large-model": {"in": 2.50, "out": 10.00}, "small-model": {"in": 0.15, "out": 0.60}}   # PLACEHOLDER per 1M tokens

rng = np.random.default_rng(32)
n = 6000
feature = rng.choice(["faq_bot", "summariser", "agent_research"], n, p=[0.7, 0.21, 0.09])
model = np.where(feature == "faq_bot", rng.choice(["large-model", "small-model"], n, p=[0.5, 0.5]), "large-model")
tok_in = np.where(feature == "agent_research", rng.normal(14000, 3000, n),
                  np.where(feature == "summariser", rng.normal(3000, 600, n), rng.normal(800, 150, n))).clip(100)
tok_out = np.where(feature == "summariser", rng.normal(400, 80, n), rng.normal(180, 50, n)).clip(10)
lat = (np.where(model == "large-model", 900, 300) + tok_out * np.where(model == "large-model", 12, 4) + rng.gamma(2, 150, n))
req = pd.DataFrame({"feature": feature, "model": model, "tok_in": tok_in.round(), "tok_out": tok_out.round(),
                    "latency_ms": lat.round()})
req["cost"] = [(r.tok_in * PRICES[r.model]["in"] + r.tok_out * PRICES[r.model]["out"]) / 1e6 for r in req.itertuples()]

by_feature = req.groupby("feature").agg(requests=("cost", "size"), cost=("cost", "sum"))
by_feature["share_of_requests"] = (by_feature.requests / n).round(2)
by_feature["share_of_cost"] = (by_feature.cost / by_feature.cost.sum()).round(2)
print(by_feature.round(2).to_string(), "\\n")
print("Latency by model (ms):\\n", req.groupby("model").latency_ms.quantile([0.5, 0.95]).unstack().round().to_string())

faq = req[req.feature == "faq_bot"]
for m in PRICES:
    c = ((faq.tok_in * PRICES[m]["in"] + faq.tok_out * PRICES[m]["out"]) / 1e6).sum()
    print(f"FAQ bot all on {m:<12}: {c:.2f} (placeholder units)")'''),
    ("md", "## 10. Caching and routing: latency vs accuracy\nQuality numbers here are **simulated** to show the trade-off. "
           "Measure real quality on your golden set."),
    ("code", '''questions = [f"faq question {i}" for i in range(3000)]
weights = 1 / np.arange(1, 3001) ** 1.1; weights /= weights.sum()          # a few questions are very common
stream = rng.choice(questions, 5000, p=weights)
cache, hits = {}, 0
for q in stream:
    key = q.strip().lower()
    if key in cache:
        hits += 1
    else:
        cache[key] = f"answer to {q}"
print(f"Cache hit rate {hits / len(stream):.0%} | model calls {len(stream) - hits} instead of {len(stream)}")

qs = pd.DataFrame({"hard": rng.random(2000) < 0.3})
QUALITY = {("large-model", True): 0.90, ("large-model", False): 0.93, ("small-model", True): 0.70, ("small-model", False): 0.92}
def run(policy):
    m = qs.hard.map(policy)
    quality = np.mean([QUALITY[(mm, hh)] for mm, hh in zip(m, qs.hard)])
    cost = sum((800 * PRICES[mm]["in"] + 180 * PRICES[mm]["out"]) / 1e6 for mm in m)
    return quality, cost
_, base_c = run(lambda hard: "large-model")
for name, pol in [("all large", lambda hard: "large-model"), ("all small", lambda hard: "small-model"),
                  ("routed", lambda hard: "large-model" if hard else "small-model")]:
    q, c = run(pol)
    print(f"{name:<10} quality {q:.3f} | cost {c / base_c:.0%} of all-large (simulated quality, placeholder prices)")'''),
    ("md", "**TODO 2 (SmartDesk step 28):** write a simple difficulty classifier (length, number of questions, words like "
           "\"compare\" or \"why\") and use it instead of the `hard` column. Log the release manifest id with every request."),
    ("code", "# TODO: write your code here"),
])
