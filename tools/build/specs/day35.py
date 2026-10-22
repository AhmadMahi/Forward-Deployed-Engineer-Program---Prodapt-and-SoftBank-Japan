"""Day 35 spec. GenAI 15: Observability, Drift and Optimisation.
Sources: archive/v1-40-day/Day34 (observability and monitoring) and archive/v1-40-day/Day35 (drift detection and
optimisation), merged into one day. NEW (v4) topics are marked.
"""
DAY = 35
FOLDER = "Day35-Observability-Drift-and-Optimisation"
SLUG = "Observability_Drift_and_Optimisation"
TITLE = "Observability, Drift and Optimisation"
SUBTITLE = "Logs, traces and OpenTelemetry GenAI spans, cost per trace, drift detection and scheduled evals"
DATE = "Mon 14 Dec 2026"
TRACK = "GenAI"
NEXT = "See you tomorrow for the capstone project (Days 36 to 40)."
CLOSING_GREET = "Otsukaresama deshita (お疲れ様でした): Thank you for your hard work today"

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz and presentations", "15 questions on Day 34, then participant PPTs (20 min)"),
        ("Observability", "Logs, metrics, traces, quality signals"),
        ("OpenTelemetry GenAI", "Standard spans, token and cost per trace. NEW (v4)"),
        ("Alerts and feedback", "Dashboards, alert rules, review queue"),
        ("Drift", "Data, concept, knowledge, provider and model. NEW (v4)"),
        ("Optimise and automate", "Experiments, re-ranking, scheduled evals"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Instrument an app", "Emit JSON logs and OpenTelemetry GenAI spans with token and cost per trace."),
        ("Monitor and alert", "Track latency, errors, cost and quality; write alerts that matter."),
        ("Detect drift", "Measure PSI, KS and embedding shift; spot provider and model drift."),
        ("Automate improvement", "Run experiments and schedule evals in CI or with Codex automations."),
    ]),
    dict(type="section", title="Observability", sub="Being able to ask any question about your running system"),
    dict(type="table", title="The three pillars, plus one for LLMs", header=["Signal", "Answers", "Example"], rows=[
        ["Logs", "What happened in this request?", "Request 7f3a: retrieved c7, answered in 1.9 s"],
        ["Metrics", "How is the system doing overall?", "p95 latency 2.4 s, error rate 0.8%"],
        ["Traces", "Where did the time and tokens go?", "Retrieval 120 ms, model 1,650 ms, 2,400 tokens"],
        ["Quality signals", "Are answers still good?", "Thumbs-down rate, faithfulness on samples"],
    ], note="Monitoring tells you something is wrong. Observability helps you find out why."),
    dict(type="bullets_code", title="Structured JSON logs", bullets=[
        "One JSON object per line",
        "Always include a request id and release id",
        "Log prompt id, context ids, tokens, latency, outcome",
        "Never log secrets; mask personal data",
    ], code='''import json, logging, uuid, time

def log(event, **fields):
    rec = {"ts": time.time(), "event": event}
    logging.info(json.dumps({**rec, **fields}))

rid = str(uuid.uuid4())[:8]
log("answer", request_id=rid, release="2.3.0",
    prompt_id="answer_v8", model="gpt-6.1-sol",
    tokens_in=812, tokens_out=164,
    latency_ms=1930, retrieved=["c7", "c2"],
    guardrail="pass")'''),
    dict(type="cards", title="OpenTelemetry GenAI semantic conventions", new=True,
         lead="A shared vocabulary for LLM spans, so any backend can read them. Check the current spec version.", items=[
        ("Span names", "For example chat {model}, embeddings {model}, execute_tool {tool}."),
        ("Request", "gen_ai.operation.name, gen_ai.request.model, gen_ai.request.temperature."),
        ("Response", "gen_ai.response.model, gen_ai.response.finish_reasons."),
        ("Usage", "gen_ai.usage.input_tokens and gen_ai.usage.output_tokens."),
    ], note="Prompt and output content are opt-in in the conventions. Keep them off by default and mask personal data."),
    dict(type="bullets_code", title="A GenAI span with the OpenTelemetry SDK", new=True, greet="Ashiato (足跡): Footprints", bullets=[
        "One trace per user request",
        "Child spans for retrieval, model and tools",
        "Standard gen_ai.* attributes",
        "Export to Azure Monitor, Grafana or others",
    ], code='''tracer = provider.get_tracer("smartdesk")

with tracer.start_as_current_span(f"chat {m}") as s:
    s.set_attribute("gen_ai.operation.name", "chat")
    s.set_attribute("gen_ai.request.model", m)
    answer = llm(prompt)
    u = usage()
    s.set_attribute("gen_ai.usage.input_tokens",
                    u["input_tokens"])
    s.set_attribute("gen_ai.usage.output_tokens",
                    u["output_tokens"])'''),
    dict(type="flow", title="Token and cost per trace", new=True, items=[
        ("Collect spans", "All spans that share a trace id"),
        ("Sum tokens", "Input and output from gen_ai.usage.*"),
        ("Price them", "Placeholder prices from config"),
        ("Attach", "Cost per trace, feature and user"),
        ("Alert", "On traces far above normal"),
    ], note="An agent request can make ten model calls. Cost per trace shows the real price of one user question."),
    dict(type="cards", title="The LLM app dashboard", items=[
        ("Traffic", "Requests per minute, by feature."),
        ("Latency", "p50 and p95, time to first token."),
        ("Errors", "Rate by type: 429, timeout, validation, guardrail."),
        ("Cost", "Per trace, per day and per feature, against budget."),
        ("Quality", "Thumbs-down rate, \"I don't know\" rate, sampled faithfulness."),
        ("Safety", "Guardrail blocks, PII redactions, injection flags."),
    ]),
    dict(type="table", title="Alerts that help, not annoy", header=["Alert", "Rule", "Why this rule"], rows=[
        ["Error spike", "Error rate above 5% for 5 minutes", "Avoid paging on a single blip"],
        ["Slow responses", "p95 above 1.3x the trailing baseline", "Users feel the tail"],
        ["Quality drop", "Thumbs-down rate doubles vs last week", "Relative change catches regressions"],
        ["Cost runaway", "Cost per trace above 3x the median", "Catches agent loops early"],
    ], note="Every alert needs an owner and a runbook link. An alert nobody acts on is noise."),
    dict(type="flow", title="From feedback to improvement", items=[
        ("Collect", "Thumbs, comments, escalations"),
        ("Triage", "Review queue, label the failure"),
        ("Fix", "Prompt, retrieval, data or guardrail"),
        ("Add test", "Failure becomes a golden item"),
        ("Verify", "Quality gate passes, then release"),
    ], note="Every fixed failure becomes a test, so it can never silently return."),

    dict(type="section", title="Drift", sub="When the world changes under your system"),
    dict(type="table", title="Drift in LLM applications", header=["Type", "What changes", "Example"], rows=[
        ["Data (input) drift", "What users send", "New 5G plan questions, more Japanese queries"],
        ["Concept drift", "What a correct answer is", "Refund period changes from 30 to 14 days"],
        ["Knowledge drift", "Your documents vs reality", "Index not rebuilt after the policy update"],
        ["Provider and model drift (NEW v4)", "The model behind the same name", "New snapshot makes answers longer"],
        ["Output drift", "What the system returns", "More refusals, lower confidence"],
    ]),
    dict(type="bullets_code", title="Population stability index (PSI)", bullets=[
        "Bucket a feature in both periods",
        "Compare the share in each bucket",
        "Below 0.1: stable; above 0.25: big shift",
        "Works for lengths, scores, categories",
    ], code='''import numpy as np

def psi(ref, cur, bins=10):
    q = np.linspace(0, 1, bins + 1)
    edges = np.quantile(ref, q)
    r = np.histogram(ref, edges)[0] / len(ref)
    c = np.histogram(cur, edges)[0] / len(cur)
    r, c = r + 1e-6, c + 1e-6
    return float(np.sum((c - r) * np.log(c / r)))'''),
    dict(type="table", title="Choosing a drift test", header=["Signal", "Test", "Reads as"], rows=[
        ["Numeric (length, latency, score)", "KS test or PSI", "p-value below 0.01 or PSI above 0.25"],
        ["Categories (topic, language)", "PSI or chi-square", "Share of each category changed"],
        ["Meaning of questions", "Embedding centroid distance", "Average question moved in meaning"],
        ["Quality", "Golden set and feedback trends", "Scores or thumbs-down changed"],
    ], note="Thresholds are starting points; tune them on your own history.", greet="Henka (変化): Change"),
    dict(type="cards", title="Provider and model drift", new=True,
         lead="The model name in your config stayed the same. The model behind it did not.", items=[
        ("Signals", "gen_ai.response.model changes; output tokens, refusals or golden scores shift."),
        ("Pin", "Use dated snapshots where offered; log the response model on every span."),
        ("Re-evaluate", "Run the golden set whenever the response model changes."),
        ("Respond", "Adjust prompts, roll back the manifest, or follow the deprecation runbook (Day 33)."),
    ]),
    dict(type="table", title="Responses to drift", header=["Drift", "Response"], rows=[
        ["New topics (data drift)", "Add documents, extend the golden set, update routing"],
        ["Policy changed (concept drift)", "Update golden answers first, then documents and prompts"],
        ["Stale index (knowledge drift)", "Automate ingestion and index rebuilds on document change"],
        ["Provider or model update", "Pin versions, run golden set, adjust prompt or roll back"],
        ["Longer or vaguer outputs", "Tighten format instructions, set max tokens, re-evaluate"],
    ]),

    dict(type="section", title="Optimise and automate", sub="Improve with experiments; let schedules do the routine"),
    dict(type="flow", title="An optimisation cycle", items=[
        ("Hypothesis", "\"Re-ranking will fix 5G misses\""),
        ("Experiment", "Change one thing"),
        ("Measure", "Golden set: quality, cost, latency"),
        ("Decide", "Keep, revert or refine"),
        ("Release", "Canary, then full"),
    ]),
    dict(type="cards", title="Levers you can pull", lead="Most quality problems in RAG systems are retrieval or data problems, not model problems.", items=[
        ("Retrieval", "Chunking, k, hybrid search, re-ranking, query rewriting."),
        ("Prompt", "Clearer rules, examples, output format, length limits."),
        ("Model", "Larger for hard cases, smaller for easy ones (routing)."),
        ("Data", "Missing documents, outdated content, better metadata."),
    ]),
    dict(type="table", title="Scheduled evals: a weekly automation plan", new=True, header=["Job", "When", "Action on failure"], rows=[
        ["Ingest changed documents, rebuild index", "On change or nightly", "Alert data owner"],
        ["Golden set evaluation", "Nightly and on every change", "Block release"],
        ["Response model check (provider drift)", "Daily", "Run evals before accepting the new snapshot"],
        ["Drift report (PSI, KS, embeddings)", "Weekly", "Open a review ticket"],
        ["Cost per trace report", "Weekly to stakeholders", "Discuss in review"],
    ], note="Run them as a CI schedule (Azure DevOps or GitHub Actions) or as Codex automations. A person reviews every breach."),
    dict(type="bullets_code", title="A scheduled eval in CI", new=True, bullets=[
        "Runs every Monday at 03:00",
        "Offline-safe; key from a secret variable",
        "Non-zero exit opens a review",
        "Report saved as an artifact",
    ], code='''# azure-pipelines-weekly.yml
schedules:
- cron: "0 3 * * 1"
  displayName: Weekly drift and eval
  branches: { include: [main] }
  always: true
steps:
- script: pip install -r requirements.txt
- script: python weekly_job.py ref.csv cur.csv
  env:
    OPENAI_API_KEY: $(OPENAI_API_KEY)
- publish: report.md'''),
    dict(type="cards", title="SmartDesk step 30: observability and capstone hand-off", items=[
        ("Instrument", "OpenTelemetry GenAI spans with token and cost per trace."),
        ("Watch", "Dashboard, alert rules and a weekly drift and eval job."),
        ("Hand off", "README, AGENTS.md, decision log and runbooks ready for the capstone team."),
        ("Build with Codex", "Use Day35_App_Build_Prompts.md. Review every line Codex writes."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("Signals", "Logs, metrics, traces, plus quality and safety signals."),
        ("OpenTelemetry GenAI", "Standard spans; token and cost per trace."),
        ("Drift", "Data, concept, knowledge, provider and model drift; PSI, KS, embeddings."),
        ("Automation", "Experiments one change at a time; scheduled evals with human review."),
    ]),
    dict(type="cards", title="Before the capstone", lead="Tomorrow starts the 5-day capstone. Teams are formed in the first session.", items=[
        ("Hotel lab", "Follow Day35_Hotel_Lab.md: logs, token per trace, drift alert."),
        ("Workbook", "Complete the Day 35 workbook."),
        ("Capstone", "Read all six capstone briefs and rank your top two."),
    ]),
]

PREREAD = dict(title="Watching AI While It Works", lede="A light read before Day 35. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "Once an AI system is live, you need to know how it is doing right now, and whether the world around it has "
        "changed. Tomorrow you build the instruments, spot drift, and automate the routine checks. It is the last "
        "teaching day before the capstone."]),
    dict(h="1. A car dashboard and a flight recorder", paras=[
        "A car's dashboard shows speed, fuel and warning lights. A flight recorder lets investigators see exactly what "
        "happened. AI systems need both: a dashboard of requests, speed, errors, cost and user happiness, and logs and "
        "traces that record each request step by step."],
        table=[["Signal", "Question it answers"], ["Logs", "What happened in this one request?"],
               ["Metrics", "How is the whole system doing?"], ["Traces", "Which step was slow, and how many tokens did it use?"],
               ["Feedback", "Are users getting good answers?"]]),
    dict(h="2. A common language for AI traces", new=True, paras=[
        "Electricians everywhere use the same colours for wires, so anyone can read a fuse box. **OpenTelemetry** gives "
        "AI traces the same kind of shared labels: which model, how many tokens in and out. Any monitoring tool can then "
        "read them, and you can add up the cost of one user question."]),
    dict(h="3. Maps go out of date", paras=[
        "A city map from five years ago still looks correct, but new roads have opened. AI systems face the same problem, "
        "called **drift**: users ask new things, policies change, documents go stale, and sometimes the provider quietly "
        "updates the model behind the same name."]),
    dict(h="4. Let the schedule do the routine", new=True, paras=[
        "Checking for drift and re-running tests can happen automatically every night or week, through a pipeline "
        "schedule or a scheduled coding-agent task. People are alerted only when something needs attention."],
        box="**Key idea:** if you cannot see it, you cannot fix it. Instrument first, then improve one change at a time."),
    dict(h="5. Preparing for the capstone", paras=[
        "From tomorrow you work in teams on a five-day capstone project. Read the six project briefs tonight and choose "
        "your top two."]),
    dict(h="6. Think about these before class", bullets=[
        "Which three numbers would you want on a dashboard for SmartDesk?",
        "How would you notice that users had started asking about something new?",
        "If an AI answer got longer every week, which number would show it first?"],
        after=["Ashiato (足跡): footprints, the trail left behind"]),
])

POSTREAD = dict(title="Observability, Drift and Optimisation: Recap and Beyond",
                lede="What we covered today, plus what to carry into the capstone.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Signals", "Logs, metrics, traces, plus quality and safety signals."],
        ["Structured logs", "JSON per line with request id, release, prompt id, model, tokens, latency, context ids."],
        ["OpenTelemetry GenAI (NEW v4)", "Standard gen_ai.* span attributes; content capture opt-in; check the spec version."],
        ["Cost per trace (NEW v4)", "Sum tokens across spans of one trace; price with placeholder config; alert on outliers."],
        ["Alerts", "Sustained windows, relative changes, an owner and a runbook for each."],
        ["Feedback loop", "Collect, triage, fix, add a golden test, verify with the quality gate."],
        ["Drift types", "Data, concept, knowledge, provider and model (NEW v4), output."],
        ["Detection", "PSI, KS test, embedding centroid shift; response model changes."],
        ["Scheduled evals (NEW v4)", "CI schedules or Codex automations; non-zero exit opens a human review."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. LLM observability tools", paras=[
        "Several tools record prompts, retrieved context, outputs, tokens and scores per request, and many now accept "
        "OpenTelemetry GenAI spans. Check data handling and retention before sending customer data to any tool."]),
    dict(sub="2. Sampling and privacy", paras=[
        "Log metadata for all requests and full content for a masked sample, plus every request with negative feedback. "
        "Set retention periods that match the customer's policy and local law."]),
    dict(sub="3. Effect size, not only p-values", paras=[
        "With millions of requests, tiny meaningless differences become significant. Look at how big the change is, and "
        "confirm with real examples."]),
    dict(sub="4. Topic discovery", paras=[
        "Cluster recent questions on embeddings and ask a model to name each cluster. New clusters with high refusal "
        "rates show exactly which documents are missing."]),
    dict(h="Part C: Capstone hand-off", paras=[
        "Your capstone (Days 36 to 40, 15 to 21 Dec 2026) should include at least: a golden set, a quality gate, "
        "structured logs or OpenTelemetry spans, one dashboard, one drift or quality check, a token and cost report, a "
        "vulnerability report, and an `AGENTS.md` in the team repo. Evaluators will look for them."],
        bullets=["Start from `Day36-40-Capstone/00_Capstone_Guide.pdf` and the project briefs in `Day36-40-Capstone/Projects/`.",
                 "Reuse your SmartDesk code: gateway (Day 34), resilient client (Day 33), quality gate (Day 32), guardrails (Day 30).",
                 "Code freeze is Day 39 at 17:00 IST; deliverables are due Day 40 at 09:00 IST."]),
    dict(h="Part D: Check yourself", bullets=[
        "Which gen_ai.* attributes would you set on a chat span?",
        "How do you compute the cost of one trace?",
        "How do you read a PSI of 0.3?",
        "What signals tell you the provider changed the model behind the same name?",
        "Why should a scheduled eval open a review instead of fixing things automatically?"]),
    dict(h="Part E: Practice ideas for tonight", bullets=[
        "Read all six capstone briefs and rank your top two with reasons.",
        "Draft your capstone's golden set with 10 items.",
        "List which notebooks from Days 2 to 35 you will reuse."],
        after=["**Coming up:** the capstone (Days 36 to 40). Real-world project options, built end to end in teams, "
               "evaluated with a shared rubric.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems using simulated production traffic with planted problems to find. Prices are "
                    "placeholders, not real prices.", problems=[
    dict(title="Design the Log Line", level="Warm-up", concepts="structured logging",
         text="List every field your LLM request log should contain and why. Mark which fields must be masked or never logged.",
         sample="request_id, ts, user_hash, release, prompt_id, model, tokens_in, tokens_out, latency_ms, retrieved_ids, guardrail, feedback\n"
                "Never: API keys; mask: emails, phone numbers",
         hints=["Think about what you need at 3 am during an incident."]),
    dict(title="OpenTelemetry GenAI Spans and Cost per Trace", level="Medium",
         concepts="OpenTelemetry, gen_ai.* attributes, token and cost per trace", new=True,
         text="Instrument a SmartDesk agent request with a root span and child spans for retrieval, two model calls and "
              "one tool call, using gen_ai.* attributes. Export to the in-memory exporter, then compute tokens and cost "
              "per trace with placeholder prices.",
         sample="trace f49b20: 5 spans | input 699 | output 39 | cost 0.00086 (placeholder units)\n"
                "most expensive span: the first chat call (planning step with the long context)",
         hints=["Group finished spans by span.context.trace_id.", "Check the current spec version for attribute names."]),
    dict(title="Monitoring Dashboard and Alerts", level="Medium", concepts="metrics, sustained and relative thresholds",
         text="From the simulated month, plot daily requests, p95 latency, error rate, cost, thumbs-down rate and output "
              "tokens. Implement four alert rules and tune the one that is too noisy.",
         sample="slow_fixed_4s fires on most days (too noisy)\nslow_vs_baseline fires on 12-24\nquality_drop fires from 12-18",
         hints=["Compare against a trailing baseline, not a fixed number only."]),
    dict(title="Find the Root Cause", level="Challenging", concepts="investigation by release",
         text="Something changed on 2026-12-18. Use the logs to find what changed (release, model, prompt) and how it "
              "affected tokens, latency and feedback.",
         sample="release 1.9.0 started 2026-12-18: output tokens +60%, thumbs-down rate nearly tripled (0.075 -> 0.208)",
         hints=["Group metrics by release, not just by day."]),
    dict(title="PSI, KS and Embedding Drift", level="Medium", concepts="data drift detection",
         text="Compute PSI for question length and topic share between week 1 and week 4, a KS test on answer tokens, and "
              "the embedding centroid drift per week. Sanity-check PSI on two halves of week 1.",
         sample="length PSI week1 vs week4: 0.16 (moderate) | half A vs B: 0.03 (stable)\n"
                "topic PSI: 1.28 (significant, 5g_plan appeared) | centroid drift week 4: 0.40 (jump)",
         hints=["Always sanity-check a drift metric on two samples that should match."]),
    dict(title="Provider and Model Drift", level="Medium", concepts="response model, golden scores, output tokens", new=True,
         text="In the simulated logs the response model snapshot changes mid-month while the configured model name stays "
              "the same. Detect the change from gen_ai.response.model, compare output tokens and golden pass rate before "
              "and after, and write the action you would take.",
         sample="response model changed on 2026-12-09: snapshot-a -> snapshot-b\n"
                "output tokens +37% | golden pass rate 0.96 -> 0.85 -> run evals, adjust prompt or roll back",
         hints=["Log the response model on every span, not only the requested one."]),
    dict(title="Scheduled Weekly Eval", level="Stretch", concepts="automation, CI schedule, Codex automations", new=True,
         text="Write weekly_job.py that computes drift metrics and golden set results, writes a Markdown report and exits "
              "with code 1 if any threshold is breached. Add an Azure DevOps or GitHub Actions schedule, and write the "
              "prompt you would give a Codex automation to run it and summarise the report.",
         sample="report_2026-W51.md written\npsi_topic 1.28 > 0.25 -> exit 1 (review needed)",
         hints=["The key comes from a secret variable; the job must also run in offline mode."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "The three classic observability signals are logs, metrics and ________.",
        "Every log line should include a request ________.",
        "The open standard for traces and metrics is ________.",
        "In the GenAI conventions, token counts go in gen_ai.usage.input_tokens and gen_ai.usage.________.",
        "Adding up tokens across all spans of one request gives the cost per ________.",
        "An alert should fire on a ________ problem, not a single blip.",
        "A change in what the correct answer is, is ________ drift.",
        "When the model behind the same name changes, it is provider or ________ drift.",
        "As a rule of thumb, PSI above ________ is a significant shift.",
        "Henka means ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain the difference between logs, metrics and traces with SmartDesk examples.",
        "Why is cost per trace more useful than cost per model call for an agent?",
        "How would you detect that the provider changed the model behind the same name?",
        "Which jobs would you schedule for your capstone, how often, and who reviews the result?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "spans = [{\"trace\": \"a\", \"in\": 100, \"out\": 20}, {\"trace\": \"a\", \"in\": 300, \"out\": 50}, {\"trace\": \"b\", \"in\": 80, \"out\": 10}]\nprint(sum(s[\"in\"] + s[\"out\"] for s in spans if s[\"trace\"] == \"a\"))",
        "import numpy as np\nr = np.array([0.5, 0.5]); c = np.array([0.5, 0.5])\nprint(float(np.sum((c - r) * np.log(c / r))))",
        "golden = {\"q\": \"refund period\", \"must_include\": [\"30 days\"]}\nanswer = \"Refunds within 14 days.\"\nprint(all(m in answer for m in golden[\"must_include\"]))",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write code that creates an OpenTelemetry span for a chat call with gen_ai.request.model and token usage attributes."),
        dict(q="Write a function cost_per_trace(spans, prices) that groups spans by trace id (placeholder prices)."),
        dict(q="Write a PSI function for two numeric arrays."),
        dict(q="Write the skeleton of a weekly job that exits with code 1 on threshold breaches."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="JSON logs, OpenTelemetry GenAI spans, token and cost per trace, alerts, drift detection, "
                         "optimisation and scheduled evals",
                sign_off="Otsukaresama deshita (お疲れ様でした): *Thank you for your hard work today*", cells=[
    ("md", "## 1. Install"),
    ("code", '''# ===== Option A: Google Colab (active) =====
# Add your key once: click the key icon (Secrets) in the left sidebar, name it OPENAI_API_KEY, and allow notebook access.
!pip install -q openai tiktoken scikit-learn numpy pandas scipy matplotlib opentelemetry-sdk

# ===== Option B: VS Code / local =====
# pip install openai tiktoken scikit-learn numpy pandas scipy matplotlib opentelemetry-sdk
# Create a .env file (git-ignored) or set the variable in your terminal:  OPENAI_API_KEY=...
# No key? Everything still runs in OFFLINE demo mode with a tiny built-in stand-in model.
print("Setup done")'''),
    ("helpers",),
    ("md", "## 2. Instrumenting requests: JSON logs and simple spans"),
    ("code", '''import json, time, uuid, random, re, sys
from contextlib import contextmanager
import numpy as np, pandas as pd, matplotlib.pyplot as plt

LOG_FILE = "requests.jsonl"
open(LOG_FILE, "w").close()

def mask(text):
    text = re.sub(r"[\\w.+-]+@[\\w-]+\\.[\\w.]+", "[email]", text)
    return re.sub(r"\\+?\\d[\\d -]{8,}\\d", "[phone]", text)

def log(**fields):
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps({"ts": time.time(), **fields}) + "\\n")

@contextmanager
def span(name, trace):
    t = time.perf_counter()
    yield
    trace.append({"span": name, "ms": round((time.perf_counter() - t) * 1000, 1)})

def handle(question, release="2.3.0"):
    rid, trace = uuid.uuid4().hex[:8], []
    with span("retrieve", trace):
        time.sleep(random.uniform(0.005, 0.015)); docs = ["c7", "c2"]
    with span("generate", trace):
        time.sleep(random.uniform(0.04, 0.08))
        answer = llm(f"Context: Roaming in Japan costs 980 JPY per day.\\nQuestion: {question}")
    with span("guardrail", trace):
        time.sleep(0.002); verdict = "pass"
    log(event="answer", request_id=rid, release=release, prompt_id="answer_v8", question=mask(question),
        retrieved=docs, guardrail=verdict, **usage(), latency_ms=round(sum(s["ms"] for s in trace), 1), trace=trace)
    return rid, trace

random.seed(34)
for q in ["How much is roaming in Japan?", "Email me at mei@example.com about roaming", "Call +81 90 1234 5678 about roaming"]:
    rid, trace = handle(q)
    print(rid, " | ".join(f"{s['span']} {s['ms']} ms" for s in trace))
print("\\nA logged line (personal data masked):\\n", open(LOG_FILE).readlines()[2])'''),
    ("md", "## 3. NEW (v4): OpenTelemetry GenAI spans, and token and cost per trace\nWe use the OpenTelemetry SDK with "
           "an in-memory exporter, so nothing leaves the notebook. Attribute names follow the OpenTelemetry GenAI "
           "semantic conventions as described in the course sources; **check the current spec version** before you "
           "build dashboards on them. `app.*` attributes are our own, not part of the standard."),
    ("code", '''from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

exporter = InMemorySpanExporter()
provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(exporter))
# ===== Option B: send to a real backend instead =====
# from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
# provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
tracer = provider.get_tracer("smartdesk")

def chat_span(prompt, model=MODEL):
    with tracer.start_as_current_span(f"chat {model}") as s:
        s.set_attribute("gen_ai.operation.name", "chat")
        s.set_attribute("gen_ai.request.model", model)
        s.set_attribute("gen_ai.request.temperature", 0.2)
        answer = llm(prompt, model=model)
        u = usage()
        s.set_attribute("gen_ai.response.model", model)
        s.set_attribute("gen_ai.usage.input_tokens", u["input_tokens"])
        s.set_attribute("gen_ai.usage.output_tokens", u["output_tokens"])
        return answer

def agent_request(question):
    with tracer.start_as_current_span("invoke_agent smartdesk") as root:
        root.set_attribute("gen_ai.operation.name", "invoke_agent")
        root.set_attribute("app.release", "2.3.0")
        with tracer.start_as_current_span("retrieve policies") as r:
            r.set_attribute("app.retrieved_ids", ["c7", "c2"])
        plan = chat_span("Plan the steps to answer: " + question + " Context: " + "Roaming policy text. " * 120)
        with tracer.start_as_current_span("execute_tool lookup_ticket") as t:
            t.set_attribute("gen_ai.operation.name", "execute_tool")
            t.set_attribute("gen_ai.tool.name", "lookup_ticket")
        return chat_span("Write the final answer for: " + question + " Notes: " + plan)

for q in ["Why was I charged roaming in Osaka?", "Is 5G available on my plan?", "Cancel my add-on please"]:
    agent_request(q)

spans = exporter.get_finished_spans()
print(len(spans), "spans exported")
for s in spans[:5]:
    print(f"{s.name:<32} trace {format(s.context.trace_id, '032x')[:6]} | {dict(s.attributes)}")'''),
    ("code", '''PRICE_PER_1M = {"input": 1.00, "output": 4.00}          # PLACEHOLDER prices, not real

rows = []
for s in spans:
    a = s.attributes
    rows.append({"trace": format(s.context.trace_id, "032x")[:6], "span": s.name,
                 "input": a.get("gen_ai.usage.input_tokens", 0), "output": a.get("gen_ai.usage.output_tokens", 0),
                 "ms": (s.end_time - s.start_time) / 1e6})
df_spans = pd.DataFrame(rows)
df_spans["cost"] = (df_spans.input * PRICE_PER_1M["input"] + df_spans.output * PRICE_PER_1M["output"]) / 1e6
per_trace = df_spans.groupby("trace").agg(spans=("span", "size"), input=("input", "sum"), output=("output", "sum"),
                                          cost=("cost", "sum"), ms=("ms", "sum"))
print(per_trace.round(5).to_string())
top = df_spans.sort_values("cost", ascending=False).iloc[0]
print(f"\\nMost expensive span: {top.span} in trace {top.trace} ({top.cost:.5f}, placeholder units)")
print("Alert rule idea: cost per trace above 3x the median ->", (per_trace.cost > 3 * per_trace.cost.median()).any())'''),
    ("md", "## 4. A simulated month of production traffic\nPlanted events: a new release on 18 Dec, a latency incident on "
           "24 Dec, and a new question topic (5G plans) growing in the last week."),
    ("code", '''rng = np.random.default_rng(34)
days = pd.date_range("2026-12-01", "2026-12-30")
rows = []
for d in days:
    n = int(rng.normal(900, 80))
    release = "1.9.0" if d >= pd.Timestamp("2026-12-18") else "1.8.0"
    new_share = 0.0 if d < pd.Timestamp("2026-12-23") else min(0.25, 0.03 * (d.day - 22))
    topics = rng.choice(["billing", "network", "roaming", "5g_plan"], n, p=[0.4, 0.3, 0.3 - new_share, new_share])
    tok_out = rng.normal(260 if release == "1.9.0" else 160, 30, n)
    lat = rng.gamma(4, 450, n) + tok_out * 4 + (2500 if d == pd.Timestamp("2026-12-24") else 0)
    err = rng.random(n) < (0.06 if d == pd.Timestamp("2026-12-24") else 0.008)
    idk = np.where(topics == "5g_plan", rng.random(n) < 0.6, rng.random(n) < 0.05)
    down_p = np.where(idk, 0.5, 0.18 if release == "1.9.0" else 0.05)
    rows.append(pd.DataFrame({"day": d, "release": release, "topic": topics, "tokens_out": tok_out.round(),
                              "latency_ms": lat.round(), "error": err, "idk": idk, "thumbs_down": rng.random(n) < down_p}))
traffic = pd.concat(rows, ignore_index=True)
traffic["cost"] = (900 * PRICE_PER_1M["input"] + traffic.tokens_out * PRICE_PER_1M["output"]) / 1e6   # placeholder prices
print(len(traffic), "requests over", traffic.day.nunique(), "days")

daily = traffic.groupby("day").agg(requests=("error", "size"), p95_ms=("latency_ms", lambda s: s.quantile(0.95)),
                                   error_rate=("error", "mean"), cost=("cost", "sum"), thumbs_down=("thumbs_down", "mean"),
                                   tokens_out=("tokens_out", "mean"), idk_rate=("idk", "mean"))
fig, axes = plt.subplots(2, 3, figsize=(13, 6))
for ax, col, color in zip(axes.flat, ["requests", "p95_ms", "error_rate", "cost", "thumbs_down", "tokens_out"],
                          ["#0FA3A3", "#0FA3A3", "#FF8A3D", "#0B5D63", "#FF8A3D", "#0B5D63"]):
    daily[col].plot(ax=ax, color=color, marker=".", title=col); ax.set_xlabel("")
plt.tight_layout(); plt.show()'''),
    ("md", "### Alert rules: sustained and relative"),
    ("code", '''baseline = daily.rolling(7, min_periods=5).median().shift(1)          # trailing 7-day baseline
rules = {
    "error_spike":           daily.error_rate > 0.05,
    "slow_fixed_4s (noisy)": daily.p95_ms > 4000,
    "slow_vs_baseline":      daily.p95_ms > baseline.p95_ms * 1.3,
    "quality_drop":          daily.thumbs_down > baseline.thumbs_down * 2,
    "idk_rising":            (daily.idk_rate > baseline.idk_rate * 1.5).rolling(2).sum() == 2,
}
for name, fired in rules.items():
    hits = [d.strftime("%m-%d") for d in daily.index[fired.fillna(False).astype(bool)]]
    print(f"{name:<22} fired on {len(hits):>2} days: {hits[:8]}{' ...' if len(hits) > 8 else ''}")

by_release = traffic.groupby("release").agg(tokens_out=("tokens_out", "mean"), p95_ms=("latency_ms", lambda s: s.quantile(0.95)),
                                            thumbs_down=("thumbs_down", "mean")).round(3)
print("\\nRoot cause view, by release:\\n", by_release)'''),
    ("md", "### Feedback loop: thumbs-down to review queue to golden set"),
    ("code", '''traffic["week"] = ((traffic.day - traffic.day.min()).dt.days // 7 + 1).clip(upper=4)
queue = traffic[traffic.thumbs_down & (traffic.week == 4)].sample(frac=1, random_state=1)
print("Review queue size (week 4):", len(queue))
reviewed = queue.head(5).assign(label=["missing_doc", "missing_doc", "too_long", "missing_doc", "too_long"])
golden_new = [{"id": f"fb-{i + 1:03d}", "question": f"<real {r.topic} question from log>", "must_include": ["<expected phrase>"],
               "source": "user feedback", "failure": r.label, "owner": "mei", "added": "2026-12-14"}
              for i, r in enumerate(reviewed.itertuples())]
with open("golden_additions.jsonl", "w") as f:
    for g in golden_new:
        f.write(json.dumps(g) + "\\n")
print(pd.Series([g["failure"] for g in golden_new]).value_counts().to_string())'''),
    ("md", "## 5. Drift: reference and current periods with planted drift"),
    ("code", '''from scipy.stats import ks_2samp
rng = np.random.default_rng(35)
TEMPLATES = {
    "billing": ["Why is my bill higher this month", "I was charged twice for my plan", "How do I get a refund for roaming"],
    "network": ["No signal at home since Monday", "Mobile data is very slow downtown", "Calls drop on the train"],
    "roaming": ["How much is roaming in Korea", "Do I need to switch on roaming", "Why was I charged roaming in Osaka"],
    "5g_plan": ["Is 5G available on my plan", "How do I upgrade to the 5G Unlimited plan", "Why does my phone not show 5G"],
}
def make_week(week, n=600):
    new = 0.0 if week < 4 else 0.25
    ja = 0.10 if week < 4 else 0.25
    topics = rng.choice(list(TEMPLATES), n, p=[0.4 - new / 3, 0.3 - new / 3, 0.3 - new / 3, new])
    rows = []
    for t in topics:
        q = rng.choice(TEMPLATES[t])
        if week == 4 and rng.random() < 0.5:
            q += " and what should I do if I am travelling abroad that week"           # longer questions in week 4
        rows.append({"week": week, "topic": t, "lang": "ja" if rng.random() < ja else "en", "question": q,
                     "q_len": len(q.split()), "answer_tokens": rng.normal(170 if week < 4 else 240, 30)})
    return pd.DataFrame(rows)
data = pd.concat([make_week(w) for w in [1, 2, 3, 4]], ignore_index=True)

def psi(ref, cur, bins=10):
    edges = np.unique(np.quantile(ref, np.linspace(0, 1, bins + 1)))
    edges[0], edges[-1] = -np.inf, np.inf
    r = np.histogram(ref, edges)[0] / len(ref) + 1e-6
    c = np.histogram(cur, edges)[0] / len(cur) + 1e-6
    return float(np.sum((c - r) * np.log(c / r)))

def psi_cat(ref, cur):
    cats = sorted(set(ref) | set(cur))
    r = np.array([(ref == k).mean() for k in cats]) + 1e-3          # smoothing: a brand new category still gives a large PSI
    c = np.array([(cur == k).mean() for k in cats]) + 1e-3
    return float(np.sum((c - r) * np.log(c / r)))

w1, w4 = data[data.week == 1], data[data.week == 4]
half = len(w1) // 2
print(f"PSI question length  week1 vs week4: {psi(w1.q_len, w4.q_len):.2f}")
print(f"PSI question length  week1 half A vs B (sanity check): {psi(w1.q_len[:half], w1.q_len[half:]):.2f}")
print(f"PSI topic            week1 vs week4: {psi_cat(w1.topic, w4.topic):.2f}")
print(f"PSI language         week1 vs week4: {psi_cat(w1.lang, w4.lang):.2f}")
ks = ks_2samp(w1.answer_tokens, w4.answer_tokens)
print(f"KS test answer tokens: statistic {ks.statistic:.2f}, p-value {ks.pvalue:.1e}  (small p-value = distributions differ)")'''),
    ("code", '''def centroid(texts):
    v = embed(list(texts)).mean(axis=0)
    return v / np.linalg.norm(v)

ref = centroid(w1.question.sample(200, random_state=1))
drift = {w: round(1 - float(ref @ centroid(data[data.week == w].question.sample(200, random_state=2))), 3) for w in [1, 2, 3, 4]}
print("Centroid drift vs week 1:", drift)
pd.Series(drift).plot(marker="o", color="#FF8A3D", title="Question embedding drift vs week 1")
plt.xlabel("week"); plt.ylabel("1 - cosine"); plt.show()'''),
    ("md", "## 6. NEW (v4): Provider and model drift\nThe configured model name never changes, but on 9 Dec the "
           "provider starts serving a new snapshot behind it. Logging `gen_ai.response.model` on every span makes this "
           "visible. Snapshots and scores here are simulated."),
    ("code", '''rng = np.random.default_rng(9)
pdays = pd.date_range("2026-12-01", "2026-12-16")
prows = []
for d in pdays:
    snap = "snapshot-b" if d >= pd.Timestamp("2026-12-09") else "snapshot-a"
    prows.append({"day": d, "requested_model": MODEL, "response_model": f"{MODEL}-{snap}",
                  "tokens_out": rng.normal(230 if snap == "snapshot-b" else 170, 8),
                  "golden_pass": rng.normal(0.85 if snap == "snapshot-b" else 0.95, 0.01)})
plog = pd.DataFrame(prows)

changes = plog[plog.response_model != plog.response_model.shift()].iloc[1:]
for r in changes.itertuples():
    print(f"response model changed on {r.day:%Y-%m-%d}: requested {r.requested_model} -> served {r.response_model}")
summary = plog.groupby("response_model").agg(tokens_out=("tokens_out", "mean"), golden_pass=("golden_pass", "mean")).round(2)
print(summary)
before, after = summary.iloc[0], summary.iloc[1]
print(f"output tokens {after.tokens_out / before.tokens_out - 1:+.0%} | golden pass rate {before.golden_pass:.2f} -> {after.golden_pass:.2f}")
print("Action:", "run full evals, adjust the prompt or roll back; follow the Day 33 runbook"
      if after.golden_pass < 0.9 else "no action")'''),
    ("md", "## 7. Concept drift: the golden set must change too"),
    ("code", '''golden_old = {"q": "What is the refund period?", "must_include": ["30 days"]}
golden_new = {"q": "What is the refund period?", "must_include": ["14 days"], "must_not_include": ["30 days"],
              "version": 2, "changed": "policy update 2026-12-01"}
def passes(g, answer):
    return all(m in answer for m in g["must_include"]) and not any(m in answer for m in g.get("must_not_include", []))
stale_answer = "Refunds are accepted within 30 days."
print("Old golden item, stale answer: ", "PASSES (wrong!)" if passes(golden_old, stale_answer) else "fails")
print("New golden item, stale answer: ", "passes" if passes(golden_new, stale_answer) else "FAILS (correct)")'''),
    ("md", "## 8. Optimisation experiments: change one thing at a time\nCompare: baseline, k=5, a simple keyword "
           "re-ranker on the top 10, adding the missing 5G document, and the data fix plus re-ranking."),
    ("code", '''KNOWLEDGE = """Bills are issued on the 1st of each month. Duplicate charges are refunded within 14 days.
Roaming in Korea costs 980 JPY per day on the Travel plan. Roaming must be switched on in the app before travel.
Roaming charges in Japan do not apply because Japan is the home network.
No signal at home can be reported in the app; an engineer visits within 3 working days.
Slow mobile data downtown is usually caused by congestion between 18:00 and 21:00.
Calls that drop on trains are a known coverage gap; a fix is planned for March."""
FIVE_G_DOC = """5G is available on the 5G Unlimited and 5G Lite plans only.
Upgrades to 5G Unlimited are done in the app and take effect the next day.
Phones show 5G only when 5G is switched on in network settings and the plan includes 5G."""

def build_index(text):
    chunks = [s.strip() for s in re.split(r"(?<=[.!?])\\s+", text) if s.strip()]
    return chunks, embed(chunks)

GOLDEN = [("How long do duplicate charge refunds take?", "within 14 days"), ("How much is roaming in Korea?", "980 JPY"),
          ("When is the engineer visit for no signal?", "3 working days"), ("Why is data slow downtown in the evening?", "congestion"),
          ("Is 5G available on my plan?", "5G Lite"), ("How do I upgrade to 5G Unlimited?", "in the app"),
          ("Why does my phone not show 5G?", "network settings")]

def rerank(q, chunks, idx):
    qw = set(re.findall(r"[a-z0-9]+", q.lower()))
    return sorted(idx, key=lambda i: -len(qw & set(re.findall(r"[a-z0-9]+", chunks[i].lower()))))

def hit_rate(chunks, vecs, k, use_rerank=False):
    hits = 0
    for q, frag in GOLDEN:
        cand = list(np.argsort(vecs @ embed(q)[0])[::-1][:10 if use_rerank else k])
        top = rerank(q, chunks, cand)[:k] if use_rerank else cand
        hits += any(frag in chunks[i] for i in top)
    return hits / len(GOLDEN)

base = build_index(KNOWLEDGE)
fixed = build_index(KNOWLEDGE + "\\n" + FIVE_G_DOC)
results = {"baseline (k=3)": hit_rate(*base, 3), "k=5": hit_rate(*base, 5), "re-rank top 10 (k=3)": hit_rate(*base, 3, True),
           "add 5G document (k=3)": hit_rate(*fixed, 3), "5G document + re-rank": hit_rate(*fixed, 3, True)}
for name, r in results.items():
    print(f"{name:<24} hit rate {r:.2f}")
print("\\nThe data fix (adding the missing document) beats tuning. Re-ranking cannot help when the evidence is missing.")'''),
    ("md", "## 9. NEW (v4): Scheduled evals with CI or Codex automations\nA weekly job computes drift and golden "
           "results, writes a report and exits non-zero on a breach. A CI schedule or a Codex automation runs it; a "
           "person reviews every breach."),
    ("code", '''%%writefile weekly_job.py
import sys
import numpy as np, pandas as pd

THRESHOLDS = {"psi_topic": 0.25, "psi_length": 0.25, "golden_hit_rate": 0.9}

def psi_cat(ref, cur):
    cats = sorted(set(ref) | set(cur))
    r = np.array([(ref == k).mean() for k in cats]) + 1e-3
    c = np.array([(cur == k).mean() for k in cats]) + 1e-3
    return float(np.sum((c - r) * np.log(c / r)))

def psi_num(ref, cur, bins=10):
    edges = np.unique(np.quantile(ref, np.linspace(0, 1, bins + 1)))
    edges[0], edges[-1] = -np.inf, np.inf
    r = np.histogram(ref, edges)[0] / len(ref) + 1e-3
    c = np.histogram(cur, edges)[0] / len(cur) + 1e-3
    return float(np.sum((c - r) * np.log(c / r)))

def main(ref_path, cur_path, golden_hit_rate, week):
    ref, cur = pd.read_csv(ref_path), pd.read_csv(cur_path)
    m = {"psi_topic": round(psi_cat(ref.topic, cur.topic), 2),
         "psi_length": round(psi_num(ref.q_len, cur.q_len), 2),
         "golden_hit_rate": golden_hit_rate}
    breaches = [k for k, v in m.items() if (v > THRESHOLDS[k] if k.startswith("psi") else v < THRESHOLDS[k])]
    lines = [f"# LLMOps weekly report {week}", "", "| Metric | Value | Threshold | Status |", "|---|---|---|---|"]
    lines += [f"| {k} | {v} | {THRESHOLDS[k]} | {'REVIEW' if k in breaches else 'ok'} |" for k, v in m.items()]
    lines += ["", "Action: " + ("review the breached metrics this week." if breaches else "no action needed.")]
    open(f"report_{week}.md", "w").write("\\n".join(lines))
    print("\\n".join(lines))
    return 1 if breaches else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]))'''),
    ("code", '''import subprocess
w1.to_csv("week1.csv", index=False); w4.to_csv("week4.csv", index=False)
r = subprocess.run([sys.executable, "weekly_job.py", "week1.csv", "week4.csv", str(round(results["baseline (k=3)"], 2)), "2026-W51"],
                   capture_output=True, text=True)
print(r.stdout)
print("exit code:", r.returncode, "(1 means a person should review; the scheduler opens a ticket or alert)")'''),
    ("code", '''%%writefile azure-pipelines-weekly.yml
# Weekly drift and eval job. The key comes from a secret pipeline variable; the job also runs offline.
schedules:
- cron: "0 3 * * 1"
  displayName: Weekly drift and eval
  branches:
    include: [main]
  always: true
pool:
  vmImage: ubuntu-latest
steps:
- script: pip install numpy pandas scipy
  displayName: Install
- script: python weekly_job.py data/ref.csv data/cur.csv 0.95 $(Build.BuildNumber)
  displayName: Drift and golden set
  env:
    OPENAI_API_KEY: $(OPENAI_API_KEY)
- publish: report_$(Build.BuildNumber).md
  artifact: weekly-report
  condition: always()'''),
    ("code", '''CODEX_AUTOMATION_PROMPT = """Every Monday at 09:00 IST:
1. Pull main. Run: python weekly_job.py data/ref.csv data/cur.csv <golden_hit_rate> <ISO week>.
2. If the exit code is 0, post a two-line summary of the report.
3. If the exit code is 1, open a draft issue titled 'Weekly drift review <week>' with the report attached
   and the three most likely causes. Do not change prompts, code or data. A person decides the fix.
Never print secrets. Use the approved model only."""
print(CODEX_AUTOMATION_PROMPT)'''),
    ("md", "**TODO (SmartDesk step 30):** add the KS test on answer tokens to `weekly_job.py` with a p-value threshold of "
           "0.01, add a `cost_per_trace_p95` metric from section 3, and write the capstone hand-off notes in your README."),
    ("code", "# TODO: write your code here"),
])
