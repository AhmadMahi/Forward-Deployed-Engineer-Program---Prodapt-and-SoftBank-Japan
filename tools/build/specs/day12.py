"""Day 12 spec. GenAI 1: Introduction to GenAI, LLMs and Tokens.
Source: archive/v1-40-day/Day21 part 1 (GenAI intro), expanded to a full day. NEW (v4) topics are marked.
"""
DAY = 12
FOLDER = "Day12-GenAI-Intro-LLMs-and-Tokens"
SLUG = "GenAI_Intro_LLMs_and_Tokens"
TITLE = "GenAI Intro, LLMs and Tokens"
SUBTITLE = "How LLMs generate text, the 2026 model landscape, tokens and cost, and your first LLM API call"
DATE = "Wed 11 Nov 2026"
TRACK = "GenAI"
NEXT = "See you tomorrow for Day 13: prompt engineering, plus GenAI assessment 1."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 11"),
        ("How LLMs work", "Transformers, attention, next-token loop"),
        ("Model landscape", "Reasoning, open-weight, LLM vs SLM. NEW (v4)"),
        ("Tokens 101", "Context window, token types, cost. NEW (v4)"),
        ("First API call", "Python and FastAPI, with a token log"),
        ("SmartDesk", "Ticket summariser with token logging"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Explain LLMs", "Describe tokens, next-token prediction and attention in plain words."),
        ("Choose a model type", "Tell reasoning, light and open-weight models apart, and when an SLM fits."),
        ("Count and price tokens", "Estimate input, output, reasoning and cached tokens and their cost."),
        ("Call an LLM safely", "Call the OpenAI API from Python and FastAPI, with keys out of code."),
    ]),
    dict(type="section", title="What generative AI is", sub="Very good next-word prediction, at enormous scale"),
    dict(type="flow", title="How an LLM answers", items=[
        ("Tokenise", "Text split into tokens (word pieces)"),
        ("Embed", "Each token becomes a vector"),
        ("Transform", "Layers of attention mix in context"),
        ("Predict", "Probabilities for the next token"),
        ("Repeat", "Append and predict again"),
    ], note="The model generates one token at a time. Everything else is built on this loop."),
    dict(type="table", title="Words you will hear", header=["Term", "Meaning"], rows=[
        ["Token", "A piece of text, roughly 3 to 4 characters of English on average"],
        ["Context window", "How many tokens the model can see at once (prompt plus output)"],
        ["Parameters", "The learned numbers inside the model"],
        ["Temperature", "Randomness: low is focused, high is creative"],
        ["Hallucination", "Fluent but false output"],
        ["Inference", "Running the trained model to get an answer"],
    ]),
    dict(type="cards", title="Three big ideas inside a transformer", greet="Chuui (注意): Attention", items=[
        ("Embeddings", "Tokens become vectors; similar meanings sit close together."),
        ("Self-attention", "Each token looks at every other token and decides what matters."),
        ("Stacked layers", "Many attention layers build richer understanding step by step."),
    ]),
    dict(type="bullets_code", title="Attention in one formula", bullets=[
        "Q: what each token is looking for",
        "K: what each token offers",
        "V: the information passed along",
        "softmax turns scores into weights",
    ], code='''import numpy as np

def attention(Q, K, V):
    d = Q.shape[-1]
    scores = Q @ K.T / np.sqrt(d)
    w = np.exp(scores)
    w = w / w.sum(axis=1, keepdims=True)
    return w @ V, w

# "The bank of the river": attention helps
# "bank" look at "river", not "money".'''),
    dict(type="table", title="Three families of transformer models", header=["Family", "Good at", "Examples"], rows=[
        ["Encoder-only", "Understanding: classify, embed, search", "BERT-style models, embedding models"],
        ["Decoder-only", "Generating text and code", "GPT models, Llama, Qwen"],
        ["Encoder-decoder", "Transforming input to output", "T5-style translation models"],
    ], note="Most chat models today are decoder-only. Many use mixture of experts (MoE) inside."),
    dict(type="cards", title="Beyond text: multimodal and computer use", items=[
        ("Multimodal input", "Models read images, audio and documents as well as text."),
        ("Multimodal output", "Some models produce images or speech, not only text."),
        ("Computer use", "The model sees a screen and clicks or types through a sandboxed browser."),
        ("What it means for FDEs", "More tasks become possible, and more things can go wrong. Keep a human check."),
    ], note="Computer-use agents return on Day 27 (hosted agents)."),

    dict(type="section", title="The 2026 model landscape", sub="Reasoning, open-weight and small models", new=True),
    dict(type="compare", title="Standard vs reasoning models", new=True, left=dict(title="Standard (fast) models", bullets=[
        "Answer straight away", "Low latency, lower cost", "Great for summaries, extraction, classification",
    ]), right=dict(title="Reasoning models", bullets=[
        "Think internally before answering", "Reasoning tokens are billed as output",
        "Better on multi-step logic, code, planning", "Slower and more expensive per task",
    ]), note="Reasoning effort (low, medium, high) trades quality for tokens and time."),
    dict(type="table", title="OpenAI models used in this program", new=True, header=["Tier", "Example", "Use for"], rows=[
        ["Light, cost-efficient", "GPT-6 Luna (if approved)", "Routine edits, simple classification, high volume"],
        ["Default", "GPT-6.1 Sol", "Most feature work and app calls"],
        ["Top tier", "GPT-6 Astra (trainer approval)", "Hard problems where the default fails"],
        ["Retired", "GPT-5.5 and older", "Do not use; migrate to the current default"],
    ], note="Names checked 21 Oct 2026. Confirm against the approved model list. See docs/MODEL_GUIDE.md."),
    dict(type="cards", title="Open-weight models", new=True, items=[
        ("What they are", "Model weights you can download and run on your own hardware."),
        ("Families", "For example Phi, Gemma, Llama, Qwen and Mistral small models."),
        ("Why teams use them", "Data stays on-prem, fixed cost, can be fine-tuned."),
        ("Trade-offs", "You run, patch, scale and evaluate them yourself. Check each licence."),
    ]),
    dict(type="compare", title="LLM vs SLM: a preview of Day 25", new=True, left=dict(title="Large language model (LLM)", bullets=[
        "Broad knowledge and reasoning", "Usually called through an API", "Higher cost and latency per call",
    ]), right=dict(title="Small language model (SLM)", bullets=[
        "Narrow tasks done well (classify, extract)", "Can run on a laptop, phone or on-prem",
        "Cheap, fast, private", "Weaker on open-ended reasoning",
    ]), note="Common pattern: SLM first, escalate to an LLM when needed. Day 25 goes deep."),

    dict(type="section", title="Tokens 101", sub="The unit you are billed in", new=True),
    dict(type="bullets_code", title="Tokenisation in practice", new=True, bullets=[
        "Common words are one token; rare words split into pieces",
        "Numbers, code and non-English text often use more tokens",
        "Japanese text can use more tokens per character than English",
        "Count with tiktoken; estimate about 4 characters per token",
    ], code='''import tiktoken
enc = tiktoken.get_encoding("o200k_base")
ids = enc.encode("Tokenisation is fascinating")
print(len(ids))
print([enc.decode([i]) for i in ids])
# ['Token', 'isation', ' is', ' fascinating']'''),
    dict(type="cards", title="Four kinds of tokens on your bill", new=True, items=[
        ("Input tokens", "System prompt, user message, retrieved context, tool definitions."),
        ("Output tokens", "The visible answer. Usually priced several times higher than input."),
        ("Reasoning tokens", "Hidden thinking by reasoning models. Billed as output."),
        ("Cached input tokens", "Repeated prompt prefixes served from cache at a discount."),
    ]),
    dict(type="flow", title="The context window budget", new=True, items=[
        ("System", "Rules and role"),
        ("Context", "Docs, history, tools"),
        ("User", "Today's request"),
        ("Reasoning", "Hidden thinking"),
        ("Output", "The answer"),
    ], note="Everything must fit in the window. More context costs more and can make answers worse."),
    dict(type="code", title="Cost per request: the formula", new=True, code='''# PLACEHOLDER prices per 1M tokens. Not real prices. Use the approved price sheet.
PRICE = {"input": 1.00, "cached_input": 0.10, "output": 4.00}

def cost(input_t, output_t, cached_t=0, reasoning_t=0):
    fresh = input_t - cached_t
    return (fresh * PRICE["input"] + cached_t * PRICE["cached_input"]
            + (output_t + reasoning_t) * PRICE["output"]) / 1_000_000

print(round(cost(1200, 300) * 1000, 4), "per 1,000 requests")''',
         note="Cost per feature = cost per request x requests per day. Always state that prices are placeholders."),

    dict(type="section", title="Your first LLM API call", sub="From Python, then behind FastAPI"),
    dict(type="bullets_code", title="Calling the OpenAI API from Python", bullets=[
        "Key from Colab Secrets or a .env file, never in code",
        "Model from the LLM_MODEL variable",
        "The response includes token usage",
        "Offline demo mode works without a key",
    ], code='''import os
from openai import OpenAI

client = OpenAI()   # reads OPENAI_API_KEY
model = os.getenv("LLM_MODEL", "gpt-6.1-sol")

r = client.chat.completions.create(
    model=model,
    messages=[{"role": "user",
               "content": "Summarise: my bill doubled."}])
print(r.choices[0].message.content)
print(r.usage.prompt_tokens, r.usage.completion_tokens)'''),
    dict(type="bullets_code", title="Behind a FastAPI endpoint, with a token log", bullets=[
        "The front end never sees the key (Day 11 rule)",
        "Validate input with Pydantic",
        "Log tokens and cost for every call",
        "Return a clear error on timeouts",
    ], code='''@app.post("/summarise")
def summarise(t: Ticket):
    text = llm(f"Summarise in one line: {t.body}")
    u = usage()
    log.append({"ticket": t.id, **u,
                "cost": cost(u["input_tokens"],
                             u["output_tokens"])})
    return {"summary": text, "usage": u}'''),
    dict(type="cards", title="SmartDesk step 11: ticket summariser", items=[
        ("Goal", "Summarise each SmartDesk ticket in one line through the API."),
        ("Token log", "Write prompt, input, output tokens and estimated cost to a CSV."),
        ("Safety", "Key in Secrets or .env. Offline mode for anyone without a key."),
        ("Build with Codex", "Use Day12_App_Build_Prompts.md. Review every line Codex writes."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("LLMs", "Predict the next token, one at a time, from context."),
        ("Model choice", "Light, default or top tier; reasoning effort costs tokens."),
        ("Tokens", "Input, output, reasoning and cached tokens are priced differently."),
        ("API calls", "Keys out of code, model from LLM_MODEL, log every call."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day12_Hotel_Lab.md: post-read, notebook, problems, token log."),
        ("Workbook", "Complete the Day 12 workbook."),
        ("Pre-read", "Skim the Day 13 pre-read on prompt engineering. Assessment day."),
    ]),
]

PREREAD = dict(title="How AI Writes", lede="A light read before Day 12. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "From today the program adds generative AI: tools like ChatGPT and the OpenAI models behind them, and how to "
        "build reliable products with them. Today you learn how these models work, how they are priced, and how to "
        "call one from your own code."]),
    dict(h="1. A very well-read autocomplete", paras=[
        "Your phone suggests the next word as you type. A large language model (LLM) does the same thing, but it has "
        "learned from an enormous amount of text, so its suggestions can form whole essays, emails or programs. It "
        "writes one small piece at a time, called a **token**, each time choosing what is most likely to come next."]),
    dict(h="2. Paying attention", paras=[
        "In \"I sat on the bank of the river\", you know \"bank\" means the riverside, not a place for money, because "
        "you noticed the word \"river\". Modern models do this with a mechanism called **attention**: every word looks "
        "at the other words to work out what it means in this sentence."]),
    dict(h="3. Thinkers and sprinters", new=True, paras=[
        "Some models answer straight away. Others, called **reasoning models**, think quietly before they answer. "
        "Thinking helps with hard problems but takes longer and costs more. You can often choose how hard the model "
        "thinks with a setting called **reasoning effort**."]),
    dict(h="4. Big brains and small brains", new=True, paras=[
        "Large models know a lot and reason well, but cost more per question. **Small language models (SLMs)** are "
        "cheaper and fast enough to run on a laptop. Many teams use a small model for simple jobs and a large one only "
        "when needed."]),
    dict(h="5. Paying by the word piece", new=True, paras=[
        "AI providers charge by the token. What you send is **input**; what the model writes back is **output**, and "
        "output usually costs more. A short, focused question is cheaper than pasting a whole document."],
        table=[["Everyday idea", "AI term"], ["Word pieces", "Tokens"], ["How much it can read at once", "Context window"],
               ["Thinking before answering", "Reasoning tokens"], ["Remembering a repeated question", "Cached tokens"]],
        box="**Key idea:** AI can sound confident and still be wrong. Always check important facts."),
    dict(h="6. Think about these before class", bullets=[
        "Ask an AI assistant the same question twice. Are the answers identical? Why might they differ?",
        "If every question cost money, how would you write your questions differently?",
        "Where would a confident but wrong answer be dangerous in a telecom support team?"],
        after=["Kotoba (言葉): words, language"]),
])

POSTREAD = dict(title="GenAI, LLMs and Tokens: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["LLM loop", "Tokenise, embed, transform with attention, predict the next token, repeat."],
        ["Attention", "softmax(QK^T / sqrt(d)) V: each token weighs the others."],
        ["Architectures", "Encoder-only (understand), decoder-only (generate), encoder-decoder (transform)."],
        ["Multimodal and computer use", "Models read images and audio; some can operate a sandboxed screen."],
        ["Reasoning models (NEW v4)", "Think before answering; reasoning effort trades cost for quality."],
        ["Open-weight and SLMs (NEW v4)", "Run on your own hardware; cheap and private, narrower skills."],
        ["Tokens (NEW v4)", "Input, output, reasoning and cached tokens are priced differently."],
        ["First API call", "Key from Secrets or .env, model from LLM_MODEL, log usage for every call."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Mixture of experts (MoE)", paras=[
        "A router sends each token to a few specialist sub-networks. The model has huge capacity but uses only part of "
        "it per token, so cost per token stays lower."]),
    dict(sub="2. Temperature and sampling", paras=[
        "Temperature reshapes the next-token probabilities. Low values give focused, repeatable output. Reasoning "
        "models may fix or ignore temperature; check the API documentation for the model you use."]),
    dict(sub="3. Speed tiers and batching", paras=[
        "Providers offer faster tiers at a higher price and batch processing at a lower price for jobs that can wait. "
        "Pick by how quickly the user needs the answer."]),
    dict(sub="4. Prompt caching", paras=[
        "When many requests share the same opening (system prompt, tool list, policy text), the provider can cache it "
        "and charge less for those tokens. Keep stable text at the start of the prompt. More on Day 13 and Day 25."]),
    dict(sub="5. Counting before you call", paras=[
        "Count tokens with tiktoken before sending a large document. If it will not fit, or will cost too much, trim or "
        "retrieve only the relevant part. That is the idea behind RAG on Day 18."]),
    dict(h="Part C: Check yourself", bullets=[
        "Why does an LLM sometimes give different answers to the same question?",
        "In your own words, what does attention do?",
        "Why can a reasoning model cost more even when its visible answer is short?",
        "When would you choose a small open-weight model over an API LLM?",
        "Why should the API key never be in front-end code?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Count tokens for the same sentence in English and Japanese. What do you notice?",
        "Estimate the monthly cost of summarising 5,000 tickets a day using the placeholder prices.",
        "Add a cost column to your SmartDesk token log."],
        after=["**Coming up on Day 13:** prompt engineering, structured outputs and GenAI assessment 1.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems. Every notebook cell runs offline; add an OPENAI_API_KEY to see real model "
                    "behaviour. Offline results show how the code works, not real model quality.", problems=[
    dict(title="Count the Tokens", level="Warm-up", concepts="tokens, context window", new=True,
         text="Tokenise three texts of different lengths (a tweet, an email, a page of a policy) and estimate how many "
              "pages would fit into a 128,000 token context window.",
         sample="Tweet: 31 tokens\nEmail: 212 tokens\nPolicy page: 640 tokens\nApprox. pages in 128k: 200",
         hints=["Use tiktoken if available, otherwise about 4 characters per token."]),
    dict(title="Temperature Explorer", level="Easy", concepts="softmax, sampling",
         text="Given logits for 5 candidate next words, print the probabilities at temperature 0.2, 1.0 and 2.0, and "
              "sample 10 words at each temperature.",
         sample="T=0.2: 'sunny' 0.97\nT=2.0: 'sunny' 0.38, 'rainy' 0.24 ...",
         hints=["probs = exp(logits / T) / sum(exp(logits / T))"]),
    dict(title="Attention by Hand", level="Medium", concepts="Q, K, V, softmax",
         text="Using small made-up vectors for the words in \"bank of the river\", compute the attention weights and "
              "show which word \"bank\" attends to most.",
         sample="bank attends most to: river (0.41)",
         hints=["Make the vectors for bank and river similar on purpose."]),
    dict(title="Pick the Model", level="Easy", concepts="reasoning vs standard, LLM vs SLM", new=True,
         text="For eight SmartDesk tasks (for example: classify a ticket, plan a network migration, summarise a call, "
              "draft a refund policy), choose light, default, top-tier or SLM, and give a one-line reason.",
         sample="classify ticket      -> SLM or light model: narrow, high volume\n"
                "plan migration       -> default, high reasoning effort: multi-step\n"
                "summarise call       -> light model: simple, cheap",
         hints=["Ask: how hard, how often, how private, how fast?"]),
    dict(title="Token Bill Calculator", level="Medium", concepts="input, output, reasoning, cached tokens", new=True,
         text="Write cost(input_t, output_t, cached_t, reasoning_t) using the placeholder prices in the notebook. "
              "Compare the cost per 1,000 requests for a short answer, a long answer and a reasoning answer.",
         sample="short     (1200 in, 150 out)          : 0.00180 per request\n"
                "long      (1200 in, 1200 out)         : 0.00600 per request\n"
                "reasoning (1200 in, 300 out, 2000 rsn) : 0.01040 per request",
         hints=["Reasoning tokens are billed as output.", "Label every price as a placeholder."]),
    dict(title="Your First API Call", level="Medium", concepts="OpenAI API, keys, usage",
         text="Call the model through llm() for three prompts and print the answer, input tokens and output tokens. "
              "Show that the cell still runs with no key (offline demo mode).",
         sample="Mode: OFFLINE demo\n[offline demo] Summarise: my bill doubled ... | in=12 out=9",
         hints=["Never print or hard-code the key.", "Read the model from LLM_MODEL."]),
    dict(title="SmartDesk Summariser API", level="Stretch", concepts="FastAPI, token log, cost",
         text="Wrap the summariser in a FastAPI POST /summarise endpoint. Log every call to a CSV with ticket id, "
              "input tokens, output tokens and estimated cost. Test it with TestClient.",
         sample="POST /summarise -> 200 {\"summary\": \"...\", \"usage\": {...}}\ntoken_log.csv: 3 rows",
         hints=["Use the Pydantic Ticket model from Day 5.", "Return 422 for an empty body."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "An LLM generates text one ________ at a time.",
        "The maximum amount of text a model can see at once is its context ________.",
        "Low ________ makes output more focused and consistent.",
        "The mechanism that lets each token weigh other tokens is called ________.",
        "Chat models like GPT are usually ________-only transformers.",
        "Models that think before answering are called ________ models.",
        "Hidden thinking tokens are billed as ________ tokens.",
        "A repeated prompt prefix can be served from ________ at a lower price.",
        "Models whose weights you can download are called open-________ models.",
        "Fluent but false model output is called a ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain next-token prediction to someone who has never used AI.",
        "When would you choose a reasoning model, and when a light model? Give one SmartDesk example of each.",
        "Why do output tokens usually cost more than input tokens, and how does that change how you write prompts?",
        "Why must AI output be checked, even when it sounds confident?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "PRICE = {'input': 1.0, 'output': 4.0}   # placeholder\nprint((1000 * PRICE['input'] + 500 * PRICE['output']) / 1_000_000)",
        "text = 'abcdefghijklmnop'\nprint(max(1, round(len(text) / 4)))",
        "import numpy as np\nlogits = np.array([2.0, 1.0])\np = np.exp(logits) / np.exp(logits).sum()\nprint(p.round(2))",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a function estimate_tokens(text) that uses tiktoken if available, otherwise 4 characters per token."),
        dict(q="Write cost(input_t, output_t, cached_t=0) using placeholder prices, and label them as placeholders."),
        dict(q="Write the code that reads the model name from LLM_MODEL with a default, and the key from the environment."),
        dict(q="Write a FastAPI endpoint POST /summarise that returns the summary and token usage."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="Transformers, the 2026 model landscape, tokens and cost, and your first LLM API call", cells=[
    ("md", "## 1. Install"),
    ("code", '''# ===== Option A: Google Colab (active) =====
# Add your key once: click the key icon (Secrets) in the left sidebar, name it OPENAI_API_KEY, and allow notebook access.
!pip install -q openai tiktoken scikit-learn numpy pandas fastapi httpx

# ===== Option B: VS Code / local =====
# pip install openai tiktoken scikit-learn numpy pandas fastapi httpx
# Create a .env file (git-ignored) or set the variable in your terminal:  OPENAI_API_KEY=...
# No key? Everything still runs in OFFLINE demo mode with a tiny built-in stand-in model.
print("Setup done")'''),
    ("helpers",),
    ("md", "## 2. Next-token prediction and temperature\nAn LLM scores every candidate next token. Softmax turns scores "
           "into probabilities. Temperature reshapes them."),
    ("code", '''import numpy as np
words = ["sunny", "rainy", "cloudy", "windy", "snowy"]
logits = np.array([3.0, 1.5, 1.2, 0.5, -1.0])

def softmax(x, T=1.0):
    z = np.exp((x - x.max()) / T)
    return z / z.sum()

rng = np.random.default_rng(7)
for T in [0.2, 1.0, 2.0]:
    p = softmax(logits, T)
    print(f"T={T}:", {w: round(float(v), 2) for w, v in zip(words, p)})
    print("   sample:", list(rng.choice(words, size=8, p=p)))'''),
    ("md", "## 3. Attention by hand\nSmall made-up vectors for \"bank of the river\". `bank` and `river` are similar on purpose."),
    ("code", '''tokens = ["bank", "of", "the", "river"]
E = np.array([[0.9, 0.1, 0.8], [0.1, 0.9, 0.1], [0.1, 0.8, 0.2], [0.8, 0.2, 0.9]])

def attention(Q, K, V):
    d = Q.shape[-1]
    scores = Q @ K.T / np.sqrt(d)
    w = np.exp(scores)
    w = w / w.sum(axis=1, keepdims=True)
    return w @ V, w

_, W = attention(E, E, E)
others = {t: round(float(W[0, i]), 2) for i, t in enumerate(tokens) if t != "bank"}
print("bank attends to:", others)
print("bank attends most to:", max(others, key=others.get))'''),
    ("md", "## 4. NEW (v4): The 2026 model landscape\nA simple routing table. Names come from `docs/MODEL_GUIDE.md`; "
           "confirm them against the approved model list before class."),
    ("code", '''MODEL_TIERS = {   # confirm against the approved model list
    "light":   {"example": "GPT-6 Luna (if approved)", "reasoning_effort": "low"},
    "default": {"example": "GPT-6.1 Sol", "reasoning_effort": "medium"},
    "top":     {"example": "GPT-6 Astra (trainer approval)", "reasoning_effort": "high"},
    "slm":     {"example": "small open-weight model (Day 25)", "reasoning_effort": "n/a"},
}

def pick_tier(task):
    t = task.lower()
    if any(w in t for w in ["classify", "tag", "detect language"]):
        return "slm"
    if any(w in t for w in ["summarise", "extract", "rewrite"]):
        return "light"
    if any(w in t for w in ["plan", "migrate", "design", "debug"]):
        return "top" if "critical" in t else "default"
    return "default"

for task in ["classify a ticket", "summarise a call", "plan a network migration", "debug a critical outage",
             "draft a reply"]:
    tier = pick_tier(task)
    print(f"{task:<26} -> {tier:<7} {MODEL_TIERS[tier]['example']}")'''),
    ("md", "**TODO:** add two SmartDesk tasks of your own and justify the tier you pick."),
    ("md", "## 5. NEW (v4): Tokens 101\nCount tokens with `tiktoken`. Compare English, Japanese, code and numbers."),
    ("code", '''samples = {
    "english":  "My mobile data stopped working after the update.",
    "japanese": "アップデート後にモバイルデータが使えなくなりました。",
    "code":     "def refund(order_id: int) -> bool: return True",
    "numbers":  "Invoice 2026-11-11 total 12,345.67 JPY",
}
for name, text in samples.items():
    print(f"{name:<9} {len(text):>3} chars -> {count_tokens(text):>3} tokens")'''),
    ("code", '''policy_page = "Customers may request a refund within 14 days of purchase. " * 60
per_page = count_tokens(policy_page)
print("Tokens per policy page:", per_page)
print("Pages that fit in a 128,000 token window:", 128_000 // per_page)'''),
    ("md", "### Cost per request\nPrices below are **placeholders**, not real prices. Replace them with the approved "
           "price sheet before using the numbers anywhere."),
    ("code", '''PRICE_PER_1M = {"input": 1.00, "cached_input": 0.10, "output": 4.00}   # PLACEHOLDER prices

def cost(input_t, output_t, cached_t=0, reasoning_t=0):
    fresh = input_t - cached_t
    return (fresh * PRICE_PER_1M["input"] + cached_t * PRICE_PER_1M["cached_input"]
            + (output_t + reasoning_t) * PRICE_PER_1M["output"]) / 1_000_000

cases = {"short answer": (1200, 150, 0, 0), "long answer": (1200, 1200, 0, 0),
         "reasoning answer": (1200, 300, 0, 2000), "short, cached prefix": (1200, 150, 1000, 0)}
for name, args in cases.items():
    print(f"{name:<22} {cost(*args):.5f} per request | {cost(*args) * 1000:.2f} per 1,000 (placeholder units)")'''),
    ("md", "## 6. Your first LLM API call\n`llm()` calls the OpenAI API when a key is present, otherwise the offline "
           "stand-in. `usage()` returns the token counts of the last call."),
    ("code", '''prompts = ["Summarise in one line: my bill doubled this month and nobody answers the phone.",
           "Explain a context window to a new support agent in two sentences.",
           "Give one tip to reduce token cost."]
for p in prompts:
    out = llm(p)
    u = usage()
    print(f"in={u['input_tokens']:>4} out={u['output_tokens']:>4} | {out[:90]}")'''),
    ("md", "## 7. Behind FastAPI, with a token log\nThe key stays on the server. Every call is logged with tokens and "
           "estimated cost. We test with `TestClient`, so no server is needed."),
    ("code", '''import csv, os
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI(title="SmartDesk summariser")
LOG = "token_log.csv"

class Ticket(BaseModel):
    id: int
    body: str = Field(min_length=1, max_length=4000)

@app.post("/summarise")
def summarise(t: Ticket):
    try:
        text = llm(f"Summarise this support ticket in one line: {t.body}")
    except Exception as e:                       # timeouts, rate limits
        raise HTTPException(status_code=503, detail=f"LLM unavailable: {type(e).__name__}")
    u = usage()
    row = {"ticket": t.id, **u, "est_cost": round(cost(u["input_tokens"], u["output_tokens"]), 6)}
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=row.keys())
        if new:
            w.writeheader()
        w.writerow(row)
    return {"summary": text, "usage": u}

client_api = TestClient(app)
for i, body in enumerate(["No signal at home since Monday.", "Charged twice for my November plan.",
                          "Cannot log in to the app after password reset."], 1):
    r = client_api.post("/summarise", json={"id": i, "body": body})
    print(r.status_code, r.json()["summary"][:70])
print(client_api.post("/summarise", json={"id": 9, "body": ""}).status_code, "for an empty body")
print(open(LOG).read())'''),
    ("md", "**TODO (SmartDesk step 11):** add a `prompt_chars` column and a daily total cost line to the log."),
    ("md", "## 8. Check yourself\n1. Why did Japanese text use more tokens per character?\n"
           "2. Which case was most expensive, and why?\n3. Where is the API key in this notebook? Where is it not?"),
])
