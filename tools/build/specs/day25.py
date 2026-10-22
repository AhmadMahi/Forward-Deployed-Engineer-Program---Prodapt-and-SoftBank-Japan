"""Day 25 spec. GenAI 6: Small Language Models + Token Cost and Optimisation.
NEW day in v4 (no v1 source). Every topic is NEW (v4).
"""
import types

DAY = 25
FOLDER = "Day25-SLMs-and-Token-Optimisation"
SLUG = "SLMs_and_Token_Optimisation"
TITLE = "SLMs and Token Optimisation"
SUBTITLE = "Small language models, when to use them, token economics, optimisation and FinOps for GenAI and Codex"
DATE = "Mon 30 Nov 2026"
TRACK = "GenAI"
NEXT = "See you tomorrow for Day 26: LLM orchestration, tool calling and LangGraph."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz and review", "15 questions on Day 23; Patch and Modernise review"),
        ("What SLMs are", "Small open-weight models. NEW (v4)"),
        ("SLM or LLM?", "Latency, cost, privacy, on-prem. NEW (v4)"),
        ("Hands-on SLM", "Run a small model in Colab. NEW (v4)"),
        ("Token economics", "Price input, output, cached, reasoning. NEW (v4)"),
        ("Optimise and govern", "Caching, routing, FinOps. NEW (v4)"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Explain SLMs", "Say what a small language model is and name open-weight families."),
        ("Choose SLM or LLM", "Decide by latency, cost, privacy and where the model must run."),
        ("Estimate cost per feature", "Turn tokens per request into cost per 1,000 tickets."),
        ("Cut cost safely", "Apply caching, trimming, output limits and routing, then measure."),
    ]),
    dict(type="callout", title="Opening: Patch and Modernise review", new=True,
         text="Show your vulnerability report: one finding, the fix, and the test that proves it.",
         sub="Two minutes per team. We look for findings rated correctly, fixes proven by tests, and modernisation "
             "in small verified steps. Rubric: Day 23 assignment brief (100 points)."),

    dict(type="section", title="Small language models", sub="Smaller, faster, cheaper, and often good enough", new=True),
    dict(type="cards", title="What an SLM is", new=True, items=[
        ("Small", "Roughly a few hundred million to a few billion parameters, not hundreds of billions."),
        ("Open-weight, usually", "You download the weights and run them on your own hardware."),
        ("Narrow but strong", "Very good at focused tasks: classify, extract, route, short replies."),
        ("Local", "Fits on a laptop, a phone, a single GPU or an on-prem server."),
    ]),
    dict(type="table", title="Open-weight families you will meet", new=True, header=["Family", "Typical small sizes", "Notes"], rows=[
        ["Phi", "Small instruct models", "Strong reasoning for their size"],
        ["Gemma", "Small instruct models", "Several sizes, multilingual variants"],
        ["Llama", "Small instruct models", "Large ecosystem of fine-tunes"],
        ["Qwen", "From under 1B upwards", "Good multilingual, including Japanese"],
        ["Mistral small models", "Small instruct models", "Efficient, popular for on-prem"],
    ], note="Sizes and licences change often. Check the model card and licence before any customer use."),
    dict(type="compare", title="When to use an SLM vs an LLM", new=True, left=dict(title="Pick an SLM when", bullets=[
        "The task is narrow and repetitive", "Latency must be very low", "Data must stay on-prem or on-device",
        "Volume is high and cost matters",
    ]), right=dict(title="Pick an LLM when", bullets=[
        "The task is open-ended or multi-step", "Broad knowledge or strong reasoning is needed",
        "Volume is low and quality matters most", "You do not want to run infrastructure",
    ]), note="Most production systems use both: SLM first, LLM on escalation."),
    dict(type="cards", title="Four questions to decide", new=True, items=[
        ("How hard?", "Classify a ticket: easy. Plan a network migration: hard."),
        ("How often?", "Ten calls a day or a million? Volume multiplies every cost."),
        ("How private?", "Customer data that cannot leave the network points to on-prem."),
        ("How fast?", "An agent waiting on screen needs an answer in under a second."),
    ]),
    dict(type="flow", title="Quantisation: shrinking a model", new=True, items=[
        ("FP16", "2 bytes per weight"),
        ("INT8", "1 byte per weight"),
        ("INT4", "Half a byte per weight"),
        ("Trade-off", "Less memory, small quality loss"),
    ], note="A 3B parameter model needs about 6 GB at FP16, 3 GB at INT8 and 1.5 GB at INT4 (weights only)."),
    dict(type="bullets_code", title="Light fine-tuning with LoRA (concept)", new=True, bullets=[
        "Freeze the base model",
        "Train two small matrices per layer",
        "A few MB of adapter instead of a full copy",
        "Use only after prompting and RAG fall short",
    ], code='''# LoRA on one d x d weight matrix
d, r = 4096, 8
full = d * d      # 16,777,216
lora = 2 * d * r  # 65,536
print(f"{lora/full:.2%}")
# 0.39% of the weights'''),
    dict(type="bullets_code", title="Hands-on: a small model in Colab", new=True, bullets=[
        "Runtime > Change runtime type > GPU",
        "No GPU? CPU fallback with a smaller model",
        "Same 20 SmartDesk tickets for both models",
        "Measure accuracy, latency and estimated cost",
    ], code='''from transformers import pipeline
import torch

gpu = torch.cuda.is_available()
SLM_ID = ("Qwen/Qwen2.5-1.5B-Instruct" if gpu
          else "Qwen/Qwen2.5-0.5B-Instruct")
slm = pipeline("text-generation", model=SLM_ID,
               device=0 if gpu else -1)
out = slm("Classify: my bill doubled. Label:",
          max_new_tokens=5)'''),
    dict(type="table", title="What a typical comparison shows", new=True, header=["Measure", "Small open-weight model", "API LLM"], rows=[
        ["Accuracy on 4 clear labels", "Good, slightly lower", "High"],
        ["Latency per ticket", "Low on GPU, higher on CPU", "Network round trip plus queue"],
        ["Cost per 1,000 tickets", "Your compute only", "Tokens x price"],
        ["Data location", "Stays where you run it", "Sent to the provider"],
        ["Effort to operate", "You patch, scale, monitor", "Provider runs it"],
    ], note="Your own numbers tonight decide. Offline mode shows how the code works, not real model quality."),

    dict(type="section", title="Token economics", sub="Every feature has a price per request", new=True),
    dict(type="cards", title="The four token prices", new=True, items=[
        ("Input", "Everything you send: system prompt, context, tools, user text."),
        ("Cached input", "A repeated prefix served from cache at a discount."),
        ("Output", "The visible answer. Usually several times the input price."),
        ("Reasoning", "Hidden thinking tokens. Billed as output."),
    ]),
    dict(type="code", title="Cost per feature: the formula", new=True, code='''# PLACEHOLDER prices per 1M tokens. Not real prices. Use the approved price sheet.
PRICE = {"input": 1.00, "cached_input": 0.10, "output": 4.00}

def cost_per_request(inp, out, cached_share=0.0, reasoning=0):
    cached = inp * cached_share
    return ((inp - cached) * PRICE["input"] + cached * PRICE["cached_input"]
            + (out + reasoning) * PRICE["output"]) / 1_000_000

# SmartDesk answer: 1,500 in, 300 out
print(cost_per_request(1500, 300) * 1000)   # 2.7 per 1,000 tickets (placeholder units)''',
         note="Cost per feature per day = cost per request x requests per day."),
    dict(type="flow", title="Where SmartDesk tokens go", new=True, items=[
        ("System", "800: rules, tone, policy"),
        ("Context", "500: retrieved FAQ chunks"),
        ("Ticket", "200: the customer text"),
        ("Output", "300: the reply"),
    ], note="The fixed system prompt is over half the input. That is what caching targets."),

    dict(type="section", title="Optimisation", sub="Measure first, then cut", new=True),
    dict(type="cards", title="Seven levers to cut token cost", new=True, items=[
        ("Prompt caching", "Stable text first, variable text last."),
        ("Trim context", "Compact history; send only what the task needs."),
        ("Retrieval top-k", "Three good chunks beat ten average ones."),
        ("Output limits", "Set max tokens; ask for short formats."),
        ("Batching", "Group jobs that can wait for a lower price."),
        ("Reasoning effort", "Low for routine tasks; high only when needed."),
    ], note="Lever seven, model routing, is on the next slide."),
    dict(type="bullets_code", title="Cache-friendly prompt layout", new=True, bullets=[
        "Same opening on every call: system rules, policy, tool list",
        "Variable parts at the end: ticket text, user question",
        "Do not put timestamps or IDs at the top",
        "Check cached tokens in the usage report",
    ], code='''messages = [
  sys(RULES),      # stable
  sys(POLICY),     # stable
  user(FAQ_TOP3),  # varies
  user(ticket),    # varies
]
# Stable prefix first -> cache hits.
# usage shows cached tokens.'''),
    dict(type="flow", title="Model routing: SLM first, LLM on escalation", new=True, items=[
        ("Ticket in", "Every ticket starts here"),
        ("SLM classifies", "Cheap, fast, local"),
        ("Confident?", "Yes: done. No: escalate"),
        ("LLM answers", "Hard or unclear cases only"),
        ("Log both", "Tokens, cost, route taken"),
    ], note="Measure the escalation rate. If it climbs, routing stops saving money."),
    dict(type="table", title="Before and after: SmartDesk per 1,000 tickets", new=True, header=["Step", "What changed", "Cost (placeholder units)"], rows=[
        ["Baseline", "1,500 in, 300 out, default LLM", "2.70"],
        ["+ Caching", "50% of input served from cache", "2.02"],
        ["+ Trimming", "Context 500 to 250; output cap 150", "1.18"],
        ["+ Routing", "80% handled by the SLM", "0.25"],
    ], note="Placeholder prices. Run the calculator notebook with the approved price sheet before quoting a customer."),

    dict(type="section", title="FinOps for GenAI and Codex", sub="Budgets, quotas and a daily check", new=True),
    dict(type="cards", title="FinOps basics", new=True, items=[
        ("Budgets", "A monthly budget per project; alerts at 50%, 80% and 100%."),
        ("Per-user quotas", "Daily token limits per learner or per API key."),
        ("Daily usage check", "Look at yesterday's spend every morning. Spot runaway jobs early."),
        ("Separate projects", "Codex and app calls on separate keys, so costs are visible."),
    ]),
    dict(type="cards", title="Codex usage: do's and don'ts", new=True, items=[
        ("Do", "Small tasks, relevant files only, approved default model."),
        ("Do", "Check your daily usage; stop a runaway task."),
        ("Don't", "Use a top-tier model or high effort for routine edits."),
        ("Don't", "Paste the whole codebase or 'improve everything'."),
    ], note="Model choice by task: see docs/MODEL_GUIDE.md. Confirm names against the approved model list."),
    dict(type="cards", title="SmartDesk step 21: SLM first, LLM for hard cases", items=[
        ("Classify with an SLM", "Category for every ticket, with a confidence score."),
        ("Escalate to the LLM", "Low confidence or complex replies go to the default model."),
        ("Cost report", "Cost per 1,000 tickets before and after optimisation."),
        ("Build with Codex", "Use Day25_App_Build_Prompts.md. Review every line."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("SLMs", "Small, local, cheap and fast; great for narrow tasks."),
        ("Choose by four questions", "How hard, how often, how private, how fast."),
        ("Tokens are money", "Input, cached, output and reasoning tokens are priced differently."),
        ("Measure, cut, govern", "Caching, trimming, routing; budgets and daily checks."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day25_Hotel_Lab.md: SLM comparison and cost report."),
        ("Workbook", "Complete the Day 25 workbook."),
        ("Pre-read", "Skim the Day 26 pre-read on orchestration and tool calling."),
    ]),
]

PREREAD = dict(title="Small Models, Real Savings",
               lede="A light read before Day 25. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "So far you have called one large model for everything. Today you learn that a small model is often enough, "
        "and how to work out what each AI feature really costs."]),
    dict(h="1. Not every job needs an expert", new=True, paras=[
        "A hospital receptionist can sort most visitors without a doctor. A **small language model (SLM)** is like "
        "that receptionist: it is small enough to run on a laptop or your own server, and it is very good at narrow "
        "jobs such as sorting tickets into categories."]),
    dict(h="2. Open-weight models", new=True, paras=[
        "Some companies publish the weights of their models so anyone can download and run them. Families you will "
        "hear about include Phi, Gemma, Llama, Qwen and Mistral's small models. Each has its own licence, so always "
        "check it before using one for a customer."]),
    dict(h="3. Packing lighter", new=True, paras=[
        "**Quantisation** stores each number in the model with fewer bits, like compressing a photo. The model takes "
        "less memory and runs faster, with a small loss in quality."]),
    dict(h="4. Paying by the word piece", new=True, paras=[
        "API models charge per token. What you send is **input**, what comes back is **output**, and output costs more. "
        "If you send the same long instructions every time, a **cache** can make the repeated part cheaper."],
        table=[["Everyday idea", "AI term"], ["Small, local helper", "SLM"], ["Compressing the model", "Quantisation"],
               ["Remembering the repeated part", "Prompt caching"], ["Ask the expert only when needed", "Model routing"],
               ["A spending limit", "Budget or quota"]],
        box="**Key idea:** the cheapest token is the one you never send. Measure first, then cut."),
    dict(h="5. Think about these before class", bullets=[
        "Which SmartDesk jobs are simple enough for a small model?",
        "If 50,000 tickets arrive a day, why does saving a fraction of a cent per ticket matter?",
        "What customer data should never leave the company network?"],
        after=["Kenyaku (倹約): thrift, careful saving"]),
])

POSTREAD = dict(title="SLMs and Token Optimisation: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["SLMs", "Small, usually open-weight models that run locally and do narrow tasks well."],
        ["SLM or LLM", "Decide by how hard, how often, how private and how fast."],
        ["Quantisation", "Fewer bits per weight: FP16 2 bytes, INT8 1 byte, INT4 half a byte."],
        ["LoRA", "Train small adapter matrices instead of the whole model; use after prompting and RAG."],
        ["Token prices", "Input, cached input, output and reasoning tokens are priced differently."],
        ["Optimisation", "Caching, trimming, top-k, output limits, batching, reasoning effort, routing."],
        ["FinOps", "Budgets, per-user quotas and a daily usage check, for app calls and for Codex."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Serving SLMs in production", paras=[
        "In production, small models are served by inference servers that batch requests and keep the model in GPU "
        "memory. You then call them over HTTP, much like an API LLM, but you run and patch the server yourself."]),
    dict(sub="2. Distillation", paras=[
        "A large model can label thousands of examples, and a small model is then trained on those labels. The small "
        "model learns the narrow task well and costs far less to run. Check the provider's terms before doing this."]),
    dict(sub="3. Semantic caching", paras=[
        "Prompt caching reuses an identical prefix. Semantic caching goes further: if a new question means the same "
        "as an old one, return the stored answer. It saves money but can return stale answers, so set an expiry."]),
    dict(sub="4. Measuring the escalation rate", paras=[
        "Routing only saves money while most requests stay on the small model. Track the share that escalates to the "
        "LLM every day. A sudden rise often means new ticket types or drift (Day 35)."]),
    dict(sub="5. Cost in the quality gate", paras=[
        "On Day 32 you add cost per query to the CI quality gate, so a change that doubles cost fails like a change "
        "that breaks accuracy."]),
    dict(h="Part C: Check yourself", bullets=[
        "Give two reasons a telecom operator might run an SLM on-prem.",
        "How much memory do the weights of a 3B model need at INT4?",
        "Why should stable text come first in a prompt?",
        "What happens to routing savings if the escalation rate doubles?",
        "What should a daily usage check look for?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add five tricky tickets to the comparison and see which model fails first.",
        "Change the cached share in the calculator from 0.5 to 0.8 and record the saving.",
        "Write a one-line budget rule for your team's Codex use."],
        after=["**Coming up on Day 26:** LLM orchestration, tool calling and LangGraph.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems. Every notebook cell runs offline; add an OPENAI_API_KEY to see real model "
                    "behaviour. Offline results show how the code works, not real model quality. All prices are "
                    "placeholders.", problems=[
    dict(title="SLM or LLM?", level="Warm-up", concepts="model choice, latency, privacy", new=True,
         text="For ten SmartDesk jobs (for example: tag ticket language, classify category, draft a refund reply, "
              "summarise a 40-minute call, detect abusive text, plan a fibre rollout), choose SLM or LLM and give a "
              "one-line reason using the four questions: how hard, how often, how private, how fast.",
         sample="tag language      -> SLM: narrow, very high volume\n"
                "plan fibre rollout -> LLM: open-ended, multi-step, low volume",
         hints=["There is no single right answer. The reason matters more than the choice."]),
    dict(title="Memory Footprint", level="Easy", concepts="quantisation", new=True,
         text="Write weights_gb(params_billion, bits) and print a table of weight memory for 0.5B, 1.5B, 3B and 7B "
              "models at 16, 8 and 4 bits.",
         sample="params  fp16   int8   int4\n0.5B    1.0    0.5    0.25\n3.0B    6.0    3.0    1.5\n7.0B   14.0    7.0    3.5",
         hints=["bytes = params x bits / 8. Weights only; runtime memory is higher."]),
    dict(title="SLM vs LLM on 20 Tickets", level="Medium", concepts="accuracy, latency, cost", new=True,
         text="Run the notebook comparison on the 20 labelled SmartDesk tickets. Report accuracy, average latency and "
              "estimated cost per 1,000 tickets for both models, then list the tickets each model got wrong.",
         sample="model   accuracy  avg_ms  cost_per_1k\nslm       0.85      ...     ...\nllm       0.90      ...     ...",
         hints=["Use the same prompt and label set for both.", "Offline numbers come from stand-ins; say so."]),
    dict(title="Token Bill per Feature", level="Medium", concepts="input, output, cached, reasoning tokens", new=True,
         text="Using the placeholder prices, compute the cost per 1,000 requests for three SmartDesk features: "
              "ticket summary (600 in, 60 out), FAQ answer (1,500 in, 300 out) and escalation plan with reasoning "
              "(2,000 in, 400 out, 3,000 reasoning).",
         sample="summary     : 0.84 per 1,000\nfaq answer  : 2.70 per 1,000\nplan        : 15.60 per 1,000",
         hints=["Reasoning tokens are billed as output."]),
    dict(title="Caching and Trimming", level="Medium", concepts="prompt caching, context trimming, output limits",
         new=True,
         text="Start from the FAQ answer feature. Apply 50% cached input, then trim context from 500 to 250 tokens "
              "and cap output at 150. Print the cost per 1,000 after each step and the total saving.",
         sample="baseline : 2.70\n+ cache  : 2.02\n+ trim   : 1.18\nsaving   : 56%",
         hints=["Change one thing at a time so you know which lever saved what."]),
    dict(title="Route SLM First", level="Challenging", concepts="model routing, escalation", new=True,
         text="Write route(ticket) that uses the SLM classifier and escalates to the LLM when confidence is below a "
              "threshold. Try thresholds 0.5, 0.7 and 0.9 and report escalation rate, accuracy and cost per 1,000.",
         sample="threshold  escalated  accuracy  cost_per_1k\n0.5          10%        ...       ...\n0.9          45%        ...       ...",
         hints=["A higher threshold escalates more: better accuracy, higher cost."]),
    dict(title="FinOps Guard", level="Stretch", concepts="budgets, quotas, daily usage", new=True,
         text="Build a small usage tracker: per-user daily token quota, a project monthly budget, and alerts at 50%, "
              "80% and 100%. Feed it a week of simulated Codex and app usage and print the alerts raised.",
         sample="day 3: user ana reached 80% of daily quota\nday 5: project at 50% of monthly budget",
         hints=["Keep Codex and app usage separate, as in the access plan."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "A small model whose weights you can download is called an open-________ model.",
        "Storing each weight with fewer bits is called ________.",
        "At INT8 each weight takes ________ byte.",
        "LoRA trains small ________ matrices instead of the whole model.",
        "A repeated prompt prefix can be billed at a lower ________ input price.",
        "Hidden thinking tokens are billed as ________ tokens.",
        "Sending easy requests to an SLM and hard ones to an LLM is called model ________.",
        "The share of requests sent on to the LLM is the ________ rate.",
        "A daily token limit per user is a per-user ________.",
        "For cache hits, put ________ text at the start of the prompt.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain to a customer why a small model on their own servers might suit ticket classification.",
        "When would you NOT use an SLM? Give one SmartDesk example.",
        "Describe three levers that reduce token cost and the risk each one brings.",
        "Why should Codex and app calls use separate keys or projects?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "params, bits = 3_000_000_000, 4\nprint(params * bits / 8 / 1e9)",
        "PRICE = {'input': 1.0, 'cached_input': 0.1, 'output': 4.0}   # placeholder\n"
        "inp, out, share = 1000, 100, 0.5\n"
        "print((inp*(1-share)*PRICE['input'] + inp*share*PRICE['cached_input'] + out*PRICE['output']) / 1_000_000)",
        "conf = [0.95, 0.4, 0.8, 0.6, 0.99]\nprint(sum(c < 0.7 for c in conf) / len(conf))",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebooks.", items=[
        dict(q="Write weights_gb(params_billion, bits) that returns weight memory in GB."),
        dict(q="Write cost_per_request(inp, out, cached_share=0, reasoning=0) with placeholder prices, labelled."),
        dict(q="Write route(ticket, threshold) that uses an SLM first and escalates to the LLM when confidence is low."),
        dict(q="Write check_quota(user, tokens_today, quota) that returns 'ok', 'warn' (80% or more) or 'block'."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

# ------------------------------------------------------------------ notebook 1: SLM vs LLM
TICKETS = '''TICKETS = [   # 20 labelled SmartDesk tickets (synthetic)
    ("I was charged twice for my November bill.", "billing"),
    ("Please refund the roaming charge from my trip.", "billing"),
    ("Why is there a late payment fee on my invoice?", "billing"),
    ("My payment failed but the money left my bank.", "billing"),
    ("Can I get a copy of last month's invoice?", "billing"),
    ("No signal at home since Monday.", "network"),
    ("Mobile data is very slow in the evenings.", "network"),
    ("Is there an outage in Osaka today?", "network"),
    ("5G keeps dropping to 4G on my phone.", "network"),
    ("Calls cut out after a few seconds in my office.", "network"),
    ("I cannot log in after resetting my password.", "account"),
    ("Please change the email address on my account.", "account"),
    ("My new SIM card is not activated yet.", "account"),
    ("I want to upgrade my plan to unlimited.", "account"),
    ("Someone else is using my account, please lock it.", "account"),
    ("Do you have a shop near Shibuya station?", "other"),
    ("What are your customer service opening hours?", "other"),
    ("I want to give feedback about your friendly staff.", "other"),
    ("Can I recycle my old phone with you?", "other"),
    ("My bill is fine but the network is terrible lately.", "network"),
]
LABELS = ["billing", "network", "account", "other"]
print(len(TICKETS), "tickets")'''

NOTEBOOK = dict(subtitle="Small language models vs an API LLM on SmartDesk tickets, and the levers that cut token cost",
                cells=[
    ("md", "## 1. Install\nFor the small model, use a **GPU runtime** in Colab: *Runtime > Change runtime type > GPU*. "
           "No GPU? The notebook falls back to a smaller model on CPU. No downloads possible? It uses a clearly "
           "labelled offline stand-in so every cell still runs."),
    ("code", '''# ===== Option A: Google Colab (active) =====
# Add your key once: click the key icon (Secrets) in the left sidebar, name it OPENAI_API_KEY, and allow notebook access.
!pip install -q openai tiktoken scikit-learn numpy pandas matplotlib transformers accelerate huggingface_hub

# ===== Option B: VS Code / local =====
# pip install openai tiktoken scikit-learn numpy pandas matplotlib transformers accelerate huggingface_hub torch
# Create a .env file (git-ignored) or set the variable in your terminal:  OPENAI_API_KEY=...
# Some small models need a free Hugging Face account: huggingface-cli login (optional)
print("Setup done")'''),
    ("helpers",),
    ("md", "## 2. NEW (v4): The SmartDesk test set\nTwenty synthetic tickets with the correct category. Both models get "
           "exactly the same tickets and the same label set."),
    ("code", TICKETS),
    ("md", "## 3. NEW (v4): Quantisation in numbers\nWeight memory = parameters x bits / 8. This is weights only; "
           "running the model needs extra memory."),
    ("code", '''import pandas as pd

def weights_gb(params_billion, bits):
    return params_billion * 1e9 * bits / 8 / 1e9

rows = [{"params": f"{p}B", "fp16": weights_gb(p, 16), "int8": weights_gb(p, 8), "int4": weights_gb(p, 4)}
        for p in [0.5, 1.5, 3, 7]]
print(pd.DataFrame(rows).to_string(index=False))'''),
    ("md", "### LoRA (concept)\nLoRA freezes the model and trains two small matrices per layer. How small?"),
    ("code", '''d, r = 4096, 8
full, lora = d * d, 2 * d * r
print(f"full matrix: {full:,} weights | LoRA rank {r}: {lora:,} weights | {lora / full:.2%}")'''),
    ("md", "## 4. NEW (v4): Load a small open-weight model\nThe model IDs below are examples from the Qwen family; "
           "Phi, Gemma, Llama and Mistral small models work the same way. Check the model card and licence first.\n\n"
           "The next cell downloads a model, so the offline check skips it. If it fails or you are offline, the "
           "notebook uses the stand-in in section 5."),
    ("code", '''import os
slm_pipe, SLM_ID = None, "offline stand-in"
try:
    import torch
    from transformers import pipeline
    HAVE_TRANSFORMERS = os.getenv("OFFLINE") != "1"
except Exception:
    HAVE_TRANSFORMERS = False
print("transformers available:", HAVE_TRANSFORMERS)'''),
    ("code", '''if HAVE_TRANSFORMERS:
    gpu = torch.cuda.is_available()
    SLM_ID = "Qwen/Qwen2.5-1.5B-Instruct" if gpu else "Qwen/Qwen2.5-0.5B-Instruct"   # CPU fallback: smaller model
    try:
        slm_pipe = pipeline("text-generation", model=SLM_ID, device=0 if gpu else -1)
        print("Loaded", SLM_ID, "on", "GPU" if gpu else "CPU")
    except Exception as e:
        slm_pipe, SLM_ID = None, "offline stand-in"
        print("Could not load the model, using the offline stand-in:", type(e).__name__)''', ["skip-offline-check"]),
    ("md", "## 5. NEW (v4): Two classifiers, one interface\nBoth return `(label, confidence)`. The offline stand-in is "
           "a keyword rule. It is **not** a language model; it only lets the code run without downloads."),
    ("code", '''import re, time

KEYWORDS = {"billing": ["bill", "charge", "refund", "invoice", "payment", "fee"],
            "network": ["signal", "network", "slow", "outage", "5g", "4g", "calls", "data"],
            "account": ["password", "log in", "login", "account", "sim", "plan", "email"]}

def offline_slm(text):
    """Offline stand-in for a small model: keyword counts, with a rough confidence."""
    low = text.lower()
    scores = {lab: sum(w in low for w in words) for lab, words in KEYWORDS.items()}
    best = max(scores, key=scores.get)
    total = sum(scores.values())
    if total == 0:
        return "other", 0.6
    return best, round(scores[best] / total, 2)

PROMPT = ("Classify the support ticket into exactly one of: billing, network, account, other. "
          "Reply with one word.\\nTicket: {t}")

def classify_slm(text):
    if slm_pipe is None:
        return offline_slm(text)
    out = slm_pipe(PROMPT.format(t=text) + "\\nLabel:", max_new_tokens=4, do_sample=False,
                   return_full_text=False)[0]["generated_text"].lower()
    label = next((l for l in LABELS if l in out), None)
    return (label, 0.9) if label else ("other", 0.3)        # unparseable answer = low confidence

def classify_llm(text):
    out = llm(PROMPT.format(t=text), temperature=0).strip().lower()
    label = next((l for l in LABELS if l in out), "other")
    return label, 0.95

print(classify_slm("My payment failed twice"), classify_llm("My payment failed twice"))'''),
    ("md", "## 6. NEW (v4): Compare accuracy, latency and estimated cost\nPrices are **placeholders**, not real prices. "
           "The SLM cost is a placeholder estimate of your own compute per 1M tokens."),
    ("code", '''PRICE_PER_1M = {   # PLACEHOLDER prices, replace with the approved price sheet
    "llm": {"input": 1.00, "output": 4.00},
    "slm": {"input": 0.05, "output": 0.20},   # placeholder estimate of self-hosted compute
}

def est_cost(kind, text, label):
    p = PRICE_PER_1M[kind]
    return (count_tokens(PROMPT.format(t=text)) * p["input"] + count_tokens(label) * p["output"]) / 1_000_000

results = []
for kind, fn in [("slm", classify_slm), ("llm", classify_llm)]:
    for text, gold in TICKETS:
        t0 = time.perf_counter()
        label, conf = fn(text)
        ms = (time.perf_counter() - t0) * 1000
        results.append({"model": kind, "ticket": text, "gold": gold, "pred": label, "conf": conf,
                        "ms": ms, "cost": est_cost(kind, text, label)})
df = pd.DataFrame(results)
summary = df.assign(correct=df.gold == df.pred).groupby("model").agg(
    accuracy=("correct", "mean"), avg_ms=("ms", "mean"), cost_per_1k=("cost", lambda c: c.mean() * 1000))
print("Mode:", "ONLINE" if ONLINE else "OFFLINE demo", "| SLM:", SLM_ID)
print(summary.round(4).to_string())'''),
    ("code", '''wrong = df[df.gold != df.pred][["model", "ticket", "gold", "pred"]]
print(wrong.to_string(index=False) if len(wrong) else "No mistakes")'''),
    ("md", "**TODO:** add five tricky tickets (two topics in one, sarcasm, Japanese text) and run the comparison again."),
    ("md", "## 7. NEW (v4): Model routing, SLM first\nUse the SLM's confidence. Below the threshold, escalate to the LLM."),
    ("code", '''def route(text, threshold=0.7):
    label, conf = classify_slm(text)
    if conf >= threshold:
        return label, "slm", est_cost("slm", text, label)
    label2, _ = classify_llm(text)
    return label2, "llm", est_cost("slm", text, label) + est_cost("llm", text, label2)

rows = []
for th in [0.5, 0.7, 0.9]:
    out = [(route(t, th), gold) for t, gold in TICKETS]
    rows.append({"threshold": th,
                 "escalated": sum(r[1] == "llm" for r, _ in out) / len(out),
                 "accuracy": sum(r[0] == g for r, g in out) / len(out),
                 "cost_per_1k": sum(r[2] for r, _ in out) / len(out) * 1000})
print(pd.DataFrame(rows).round(4).to_string(index=False))'''),
    ("md", "## 8. NEW (v4): Optimisation levers on one prompt\nTrim the context, cap the output and keep stable text "
           "first. Watch the token count drop."),
    ("code", '''RULES = "You are SmartDesk, a polite telecom support assistant. Follow the refund policy. " * 20
FAQ = ["Refunds are possible within 14 days.", "Roaming charges appear on the next bill.",
       "Outages are posted on the status page.", "Invoices are in the app under Billing.",
       "Password resets expire after 30 minutes.", "SIM activation takes up to 2 hours."]
ticket = "Please refund the roaming charge from my trip to Seoul."

def build_prompt(top_k, max_words_rules):
    rules = " ".join(RULES.split()[:max_words_rules])
    return f"{rules}\\n\\nFAQ:\\n" + "\\n".join(FAQ[:top_k]) + f"\\n\\nTicket: {ticket}"

for name, k, words in [("baseline", 6, 400), ("top-k 3", 3, 400), ("top-k 3 + trimmed rules", 3, 60)]:
    print(f"{name:<24} {count_tokens(build_prompt(k, words)):>5} input tokens")
print("Output limit: pass max_tokens=150 to llm() to cap the reply length.")'''),
    ("md", "Next: open `Day25_Token_Cost_Calculator_Colab.ipynb` to turn these savings into cost per 1,000 tickets."),
    ("md", "## 9. Check yourself\n1. Which model made more mistakes, and on which kind of ticket?\n"
           "2. What threshold would you choose for SmartDesk, and why?\n"
           "3. Which numbers in this notebook are placeholders?"),
])

# ------------------------------------------------------------------ notebook 2: token cost calculator
CALC = dict(subtitle="Cost per 1,000 SmartDesk tickets before and after caching, trimming and model routing",
            cells=[
    ("md", "## How to use\nChange the inputs in section 1 and run all cells. Every price here is a **placeholder**. "
           "Replace them with the approved price sheet before you quote numbers to anyone. No API key needed."),
    ("code", '''# ===== Option A: Google Colab (active) =====
!pip install -q pandas matplotlib

# ===== Option B: VS Code / local =====
# pip install pandas matplotlib
print("Setup done")'''),
    ("md", "## 1. NEW (v4): Inputs"),
    ("code", '''TICKETS_PER_DAY = 50_000

# Tokens per request for the SmartDesk FAQ answer
SYSTEM_TOKENS, CONTEXT_TOKENS, TICKET_TOKENS, OUTPUT_TOKENS = 800, 500, 200, 300
CACHED_SHARE = 0.5            # share of input tokens served from the prompt cache

# PLACEHOLDER prices per 1M tokens. Not real prices. Replace with the approved price sheet.
PRICES = {
    "llm_default": {"input": 1.00, "cached_input": 0.10, "output": 4.00},
    "slm_selfhosted": {"input": 0.05, "cached_input": 0.05, "output": 0.20},   # placeholder compute estimate
}

# Optimisation settings
TRIMMED_CONTEXT, OUTPUT_CAP = 250, 150
SLM_HANDLED_SHARE = 0.8       # share of tickets the SLM resolves without escalation
SLM_TOKENS_IN, SLM_TOKENS_OUT = 250, 5    # short classification prompt'''),
    ("md", "## 2. NEW (v4): The cost function\nReasoning tokens are billed as output."),
    ("code", '''def cost_per_request(model, inp, out, cached_share=0.0, reasoning=0):
    p = PRICES[model]
    cached = inp * cached_share
    return ((inp - cached) * p["input"] + cached * p["cached_input"] + (out + reasoning) * p["output"]) / 1_000_000

def per_1k(c):
    return round(c * 1000, 2)'''),
    ("md", "## 3. NEW (v4): Before and after, step by step"),
    ("code", '''import pandas as pd

inp = SYSTEM_TOKENS + CONTEXT_TOKENS + TICKET_TOKENS
baseline = cost_per_request("llm_default", inp, OUTPUT_TOKENS)

cached = cost_per_request("llm_default", inp, OUTPUT_TOKENS, cached_share=CACHED_SHARE)

inp_trim = SYSTEM_TOKENS + TRIMMED_CONTEXT + TICKET_TOKENS
share_trim = min(1.0, CACHED_SHARE * inp / inp_trim)      # same cached prefix, smaller total
trimmed = cost_per_request("llm_default", inp_trim, OUTPUT_CAP, cached_share=share_trim)

slm_step = cost_per_request("slm_selfhosted", SLM_TOKENS_IN, SLM_TOKENS_OUT)
routed = slm_step + (1 - SLM_HANDLED_SHARE) * trimmed     # every ticket hits the SLM; some escalate

steps = pd.DataFrame([
    {"step": "Baseline", "change": "default LLM, no optimisation", "per_1k": per_1k(baseline)},
    {"step": "+ Caching", "change": f"{CACHED_SHARE:.0%} of input cached", "per_1k": per_1k(cached)},
    {"step": "+ Trimming", "change": f"context {CONTEXT_TOKENS}->{TRIMMED_CONTEXT}, output cap {OUTPUT_CAP}",
     "per_1k": per_1k(trimmed)},
    {"step": "+ Routing", "change": f"SLM handles {SLM_HANDLED_SHARE:.0%}", "per_1k": per_1k(routed)},
])
steps["per_day"] = (steps.per_1k * TICKETS_PER_DAY / 1000).round(2)
steps["saving_vs_baseline"] = (1 - steps.per_1k / steps.per_1k.iloc[0]).map("{:.0%}".format)
print("All values in placeholder price units.")
print(steps.to_string(index=False))'''),
    ("code", '''import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.bar(steps.step, steps.per_1k, color=["#0E3B43", "#0FA3A3", "#0FA3A3", "#FF8A3D"])
ax.set_ylabel("Cost per 1,000 tickets\\n(placeholder units)")
ax.set_title("SmartDesk FAQ answer: cost after each lever")
for i, v in enumerate(steps.per_1k):
    ax.text(i, v, f"{v:.2f}", ha="center", va="bottom")
plt.tight_layout()
plt.show()'''),
    ("md", "## 4. NEW (v4): Sensitivity: how much does each input matter?"),
    ("code", '''rows = []
for share in [0.0, 0.25, 0.5, 0.75]:
    for slm_share in [0.5, 0.7, 0.9]:
        t = cost_per_request("llm_default", inp_trim, OUTPUT_CAP, cached_share=min(1.0, share * inp / inp_trim))
        rows.append({"cached_share": share, "slm_handled": slm_share, "per_1k": per_1k(slm_step + (1 - slm_share) * t)})
grid = pd.DataFrame(rows).pivot(index="cached_share", columns="slm_handled", values="per_1k")
print("Cost per 1,000 tickets (placeholder units)")
print(grid.to_string())'''),
    ("md", "## 5. NEW (v4): FinOps: budget and quota check\nA monthly budget with alerts at 50%, 80% and 100%, and a "
           "per-user daily token quota for Codex. Numbers are placeholders."),
    ("code", '''MONTHLY_BUDGET = 300.0               # placeholder units
DAILY_QUOTA_TOKENS = 400_000         # per learner, Codex, placeholder
spend_per_day = steps.per_day.iloc[-1]

alerts, total = [], 0.0
for day in range(1, 31):
    total += spend_per_day
    for level in [0.5, 0.8, 1.0]:
        if total >= level * MONTHLY_BUDGET and not any(a[1] == level for a in alerts):
            alerts.append((day, level))
print(f"Projected month: {total:.2f} of {MONTHLY_BUDGET:.0f} (placeholder units)")
for day, level in alerts:
    print(f"day {day:>2}: budget alert at {level:.0%}")

codex_usage = {"ana": [120_000, 350_000, 410_000], "kenji": [90_000, 80_000, 60_000]}
for user, days in codex_usage.items():
    for d, used in enumerate(days, 1):
        state = "block" if used >= DAILY_QUOTA_TOKENS else "warn" if used >= 0.8 * DAILY_QUOTA_TOKENS else "ok"
        if state != "ok":
            print(f"day {d}: {user} {state} ({used:,} of {DAILY_QUOTA_TOKENS:,} tokens)")'''),
    ("md", "**TODO (cost report):** copy the before and after table into your SmartDesk cost report, add the SLM vs "
           "LLM comparison table from the other notebook, and write two sentences on the risks of each lever."),
])

EXTRA_NOTEBOOKS = [types.SimpleNamespace(DAY=25, TITLE="Token Cost Calculator", NOTEBOOK=CALC,
                                         FILENAME="Day25_Token_Cost_Calculator_Colab.ipynb")]
