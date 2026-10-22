"""Day 32 spec. GenAI 12: LLM Evaluation and Quality Gates.
Source: archive/v1-40-day/Day30 (REUSE + UPDATE). NEW (v4) topics are marked.
"""
DAY = 32
FOLDER = "Day32-LLM-Evaluation-and-Quality-Gates"
SLUG = "LLM_Evaluation_and_Quality_Gates"
TITLE = "LLM Evaluation and Quality Gates"
SUBTITLE = "Golden datasets, prompt regression tests, tool-call fidelity, context precision and recall, and cost-aware quality gates"
DATE = "Wed 09 Dec 2026"
TRACK = "GenAI"
NEXT = "See you tomorrow for Day 33: LLMOps, plus GenAI assessment 3."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 31"),
        ("Golden datasets", "The trusted reference set"),
        ("Prompt and tool tests", "Regression tests and tool-call fidelity. NEW (v4)"),
        ("RAG metrics", "Precision, recall, faithfulness, citations"),
        ("Cost-aware gates", "Tokens and cost in the quality gate. NEW (v4)"),
        ("1:1 feedback", "Short individual feedback while you build"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Curate golden data", "Build, version and maintain a golden dataset."),
        ("Test prompts and tools", "Regression-test prompts and check tool calls with exact arguments."),
        ("Grade retrieval", "Compute context precision, recall and citation accuracy."),
        ("Gate releases", "Block releases on quality, token and cost regressions, writing evals first."),
    ]),

    dict(type="section", title="Golden datasets", sub="The answers you trust most"),
    dict(type="cards", title="What makes a dataset golden", greet="Kihon (基本): The foundation", items=[
        ("Verified", "Answers checked by subject experts, not just generated."),
        ("Representative", "Real user wording, all topics, languages and edge cases."),
        ("Versioned", "Stored in Git with a version number and change log."),
        ("Maintained", "Policies change; golden answers must change with them."),
    ]),
    dict(type="table", title="Golden item fields", header=["Field", "Example"], rows=[
        ["id", "leave-003"],
        ["question", "When does carried over leave expire?"],
        ["expected_answer", "31 March of the following year"],
        ["relevant_chunk_ids", "[c7]"],
        ["tags", "topic: leave, lang: en, difficulty: easy"],
        ["must_include / must_not_include", "[\"31 March\"] / [\"30 June\"]"],
        ["expected_tool (agents)", "lookup_leave_balance(employee_id=...)"],
    ]),
    dict(type="table", title="Metrics and eval frameworks", header=["Need", "Metric", "Tools you may meet"], rows=[
        ["Fixed format output", "Exact match, schema validation", "PyTest, Pydantic"],
        ["Retrieval", "Precision, recall, average precision", "Ragas, your own code"],
        ["Grounded answers", "Faithfulness, citation accuracy", "Ragas, DeepEval, LLM judges"],
        ["Prompt suites in CI", "Pass rate vs threshold", "promptfoo, OpenAI Evals, PyTest"],
    ], note="Concepts carry over between tools. Check each tool's current documentation."),

    dict(type="section", title="Prompt and tool regression testing", sub="Every prompt change is a code change"),
    dict(type="flow", title="Regression testing a prompt change", items=[
        ("Baseline", "Run prompt v1 on the golden set"),
        ("Change", "Write prompt v2"),
        ("Run", "Same golden set, same settings"),
        ("Compare", "Per item and overall"),
        ("Decide", "Ship only if no important regressions"),
    ]),
    dict(type="bullets_code", title="Prompt unit tests with PyTest", bullets=[
        "Load the golden set once",
        "parametrize over items",
        "Check required and forbidden phrases",
        "A summary test enforces the threshold",
    ], code='''GOLDEN = load_jsonl("golden_v3.jsonl")

@pytest.mark.parametrize("item", GOLDEN,
                         ids=lambda i: i["id"])
def test_item(item):
    out = answer(item["question"], PROMPT_V2)
    for p in item["must_include"]:
        assert p.lower() in out.lower()
    for p in item["must_not_include"]:
        assert p.lower() not in out.lower()

def test_overall_pass_rate():
    assert pass_rate(PROMPT_V2) >= 0.90'''),
    dict(type="compare", title="Deterministic and model-graded checks", left=dict(title="Deterministic", bullets=[
        "Must include, must not include", "Valid JSON, length limits", "Fast, free, exact", "Run on every commit",
    ]), right=dict(title="Model-graded", bullets=[
        "Faithfulness, tone, helpfulness", "Rubric judges", "Slower, costs tokens", "Run nightly or before release",
    ])),
    dict(type="cards", title="Tool-call fidelity tests", new=True,
         lead="For agents, the tool call is the answer. Test it like an API contract.", items=[
        ("Right tool", "The model picks the expected tool for the request."),
        ("Valid arguments", "Arguments match the JSON Schema: types and required fields."),
        ("Right values", "IDs, amounts and dates are extracted exactly."),
        ("No call when not needed", "Small talk or out-of-scope requests call no tool."),
    ]),
    dict(type="bullets_code", title="A tool-call fidelity test", new=True, bullets=[
        "Golden cases: request plus expected call",
        "Validate arguments against the schema",
        "Compare values exactly",
        "Run on every prompt or model change",
    ], code='''CASES = [
  ("Refund 300 on order ORD-77",
   "issue_refund",
   {"order_id": "ORD-77", "amount": 300}),
  ("Hi, thanks!", None, None),
]

@pytest.mark.parametrize("msg,tool,args", CASES)
def test_tool_call(msg, tool, args):
    call = choose_tool(msg)
    assert call.name == tool
    if tool:
        validate(call.args, SCHEMAS[tool])
        assert call.args == args'''),

    dict(type="section", title="Grading retrieval and grounding", sub="Is retrieval finding the right things, in the right order?"),
    dict(type="table", title="Context precision and recall", header=["Metric", "Question", "Formula (simple form)"], rows=[
        ["Context precision", "Of what we retrieved, how much was relevant?", "relevant retrieved / retrieved"],
        ["Context recall", "Of what was needed, how much did we retrieve?", "needed facts found / needed facts"],
        ["Average precision", "Were relevant chunks ranked first?", "mean of precision at each hit"],
    ], note="Rank-aware precision rewards putting relevant chunks first."),
    dict(type="bullets_code", title="Computing them", greet="Seikaku (正確): Accurate", bullets=[
        "Precision punishes noise",
        "Recall punishes missing evidence",
        "Average precision rewards good order",
        "Track both; trade-offs are common",
    ], code='''def precision(retrieved, relevant):
    hits = [c for c in retrieved if c in relevant]
    return len(hits) / len(retrieved)

def recall(retrieved, relevant):
    found = set(retrieved) & set(relevant)
    return len(found) / len(relevant)'''),
    dict(type="cards", title="Faithfulness, relevance and citations", items=[
        ("Faithfulness", "Every claim supported by the retrieved context (Day 31)."),
        ("Answer relevance", "The answer addresses the question that was asked."),
        ("Citation accuracy", "Every cited chunk was retrieved and supports the claim."),
        ("Refusal accuracy", "Unanswerable questions get \"I don't know\", not a guess."),
    ]),
    dict(type="table", title="Choosing a metric (and where BLEU fits)", header=["Task", "Prefer"], rows=[
        ["Fixed format output (JSON, labels, tool calls)", "Exact match, schema validation"],
        ["Translation", "BLEU or chrF, plus human review"],
        ["Summaries", "ROUGE plus faithfulness"],
        ["Open-ended answers (RAG)", "Faithfulness, correctness judge, must-include phrases, citations"],
    ], note="BLEU counts shared word sequences: a correct paraphrase can score near zero."),

    dict(type="section", title="Quality gates in CI/CD", sub="Evaluation that blocks bad releases"),
    dict(type="flow", title="An LLM quality gate", items=[
        ("Pull request", "Prompt, model or config change"),
        ("Fast checks", "Deterministic and tool tests"),
        ("Golden eval", "Quality metrics vs thresholds"),
        ("Cost check", "Tokens and cost per query. NEW (v4)"),
        ("Gate", "Fail the pipeline on regressions"),
    ], note="Same pipeline ideas as Day 20, with quality and cost metrics as the tests."),
    dict(type="table", title="Token and cost metrics in the gate", new=True, header=["Metric", "Why", "Example rule"], rows=[
        ["Input tokens per query", "Context bloat creeps in quietly", "No more than 10% above baseline"],
        ["Output tokens per query", "Verbose prompts cost more", "Under 300 on average"],
        ["Estimated cost per query", "Ties quality to budget", "Under the agreed budget (placeholder prices)"],
        ["Cost per 1,000 queries", "What the customer pays", "Reported on every pull request"],
    ], note="A change that is 1% better but 3 times the cost needs a human decision, not an automatic merge."),
    dict(type="flow", title="Eval-first development with Codex", new=True, items=[
        ("Write evals", "Golden items for the new behaviour"),
        ("See them fail", "Proves the test can fail"),
        ("Ask Codex", "Implement until evals pass"),
        ("Review", "Read the diff, run the gate"),
        ("Keep", "Evals stay as regression tests"),
    ], note="Tell Codex the eval command in AGENTS.md so it runs the evals after each change."),
    dict(type="callout", title="Hands-on time", greet="Ganbatte (頑張って): Do your best",
         text="Create a versioned golden set, write prompt and tool-call fidelity tests, compute precision, recall and "
              "citation accuracy, then wire a quality gate that also checks tokens and cost. Make it fail on purpose.",
         sub="1:1 feedback runs during this block. Bring one question about your progress."),
    dict(type="cards", title="SmartDesk step 27: quality gate in CI", items=[
        ("Golden set", "SmartDesk golden items with must-include phrases and citations."),
        ("Tool tests", "Fidelity tests for the support assistant's tool calls."),
        ("Cost metrics", "Tokens and cost per query, compared with main."),
        ("CI stage", "Evaluate stage before deploy. Build with Codex; review every line."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("Golden data", "Verified, representative, versioned, maintained."),
        ("Regression tests", "Prompts and tool calls tested on every change."),
        ("Retrieval", "Precision for noise, recall for missing evidence, citations checked."),
        ("Gates", "Quality, tokens and cost thresholds; evals written first."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz, plus GenAI assessment 3.", items=[
        ("Hotel lab", "Follow Day32_Hotel_Lab.md: a gate that passes and fails."),
        ("Workbook", "Complete the Day 32 workbook."),
        ("Pre-read", "Skim the Day 33 pre-read on running AI like a product."),
    ]),
]

PREREAD = dict(title="Quality Checks Before Every Release",
               lede="A light read before Day 32. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "Yesterday you measured how good an AI system is. Today you make those measurements automatic, so that every "
        "change to a prompt, model or setting is checked for quality and cost before it reaches users."]),
    dict(h="1. The answer key", paras=[
        "Teachers mark exams against an answer key that experts have checked. A **golden dataset** is the answer key "
        "for an AI system: questions with verified answers, kept safe and updated when policies change."]),
    dict(h="2. Small changes, surprising effects", paras=[
        "Changing one word in a prompt, or switching to a cheaper model to save money, can quietly break answers that "
        "worked yesterday. **Regression testing** reruns the golden questions after every change and flags anything "
        "that got worse, just like the tests you wrote for code."],
        box="**Key idea:** treat prompts like code. Version them, test them, and review changes."),
    dict(h="3. Did we fetch the right pages?", table=[
        ["Measure", "Question", "Everyday version"],
        ["Precision", "How much of what we fetched was useful?", "Of 10 books brought, how many were relevant?"],
        ["Recall", "How much of what we needed did we fetch?", "Of the 3 books needed, how many arrived?"],
    ]),
    dict(h="4. Pressing the right button", new=True, paras=[
        "When an AI agent takes an action, the action is the answer. If a customer asks for a refund of 300 on order 77, "
        "the agent must call the refund tool with exactly that order and amount. **Tool-call fidelity** tests check "
        "this the way a bank checks every transfer."]),
    dict(h="5. Good and affordable", new=True, paras=[
        "A change that makes answers slightly better but triples the bill is not automatically a win. Quality gates "
        "now also check **tokens and cost per question**, so nobody is surprised by the invoice."]),
    dict(h="6. Think about these before class", bullets=[
        "Who in a telecom company could verify golden answers for a support assistant?",
        "What change might someone make to save cost that could quietly reduce quality?",
        "Can you think of two correct answers to a question that share almost no words?"],
        after=["Kihon (基本): the foundation, the basics"]),
])

POSTREAD = dict(title="LLM Evaluation and Quality Gates: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Golden dataset", "Verified, representative, versioned, maintained. Fields: id, question, expected, relevant ids, "
                           "tags, must include and must not include."],
        ["Prompt regression", "Rerun the golden set for every prompt, model or retrieval change; compare per item."],
        ["Deterministic checks", "Phrases, JSON validity, length. Fast; run on every commit."],
        ["Model-graded checks", "Faithfulness, tone, correctness rubrics. Slower; nightly or before release."],
        ["Tool-call fidelity (NEW v4)", "Right tool, schema-valid arguments, exact values, no call when not needed."],
        ["Context precision and recall", "Relevant retrieved / retrieved; needed evidence found / needed evidence."],
        ["Citations", "Every cited chunk was retrieved and is relevant."],
        ["BLEU", "n-gram overlap with brevity penalty. Good for translation, weak for open answers."],
        ["Cost in the gate (NEW v4)", "Tokens and estimated cost per query, compared with the baseline."],
        ["Eval-first with Codex (NEW v4)", "Write the evals, see them fail, let Codex implement, keep evals as tests."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Baselines from main", paras=[
        "Compare a pull request's scores with the main branch's latest scores, not with fixed numbers only. A drop of "
        "more than a tolerance (for example 2 points) fails the gate even if the absolute score is still high."]),
    dict(sub="2. Non-determinism", paras=[
        "Model outputs vary between runs. Use temperature 0 where the model allows it, run important items several "
        "times, and set thresholds with a little slack rather than demanding perfection."]),
    dict(sub="3. Cost-aware evaluation tiers", paras=[
        "Run cheap deterministic and tool tests on every push, a small golden subset with model judges on pull "
        "requests, and the full suite nightly. Track the cost of the evaluation run itself."]),
    dict(sub="4. Ready-made tools", paras=[
        "Frameworks such as promptfoo, DeepEval, Ragas and the OpenAI Evals project help define datasets, metrics and CI "
        "integrations. Concepts from today carry over directly; check each tool's current documentation."]),
    dict(sub="5. Keep the golden set alive", paras=[
        "Add every production failure that users report as a new golden item, with an owner and date. The set grows to "
        "reflect reality."]),
    dict(h="Part C: Check yourself", bullets=[
        "What makes a dataset golden rather than just a test set?",
        "What four things does a tool-call fidelity test check?",
        "What is the difference between context precision and context recall?",
        "Why include cost per query in a quality gate?",
        "What does eval-first development with Codex look like, step by step?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add 10 golden items for your capstone domain with must include and must not include phrases.",
        "Add three tool-call fidelity cases, including one where no tool should be called.",
        "Wire the quality gate into your pipeline as a stage before deployment."],
        after=["**Coming up on Day 33:** LLMOps: lifecycle, AgentOps, versioning, monitoring and cost strategies, plus "
               "GenAI assessment 3.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Eight problems that turn evaluation into automatic quality checks. All run offline; with a key, "
                    "model-graded checks become meaningful. Offline results show how the code works, not real model "
                    "quality. Prices are placeholders.", problems=[
    dict(title="Golden Set v1", level="Warm-up", concepts="dataset curation",
         text="Write 12 golden items in JSONL with id, question, expected, relevant chunk ids, tags, must_include and "
              "must_not_include. Save as golden_v1.jsonl.",
         sample='{"id": "leave-003", "question": "When does carried over leave expire?", "must_include": ["31 March"], ...}',
         hints=["must_not_include catches common wrong answers."]),
    dict(title="Deterministic Tests", level="Easy", concepts="PyTest parametrize",
         text="Write a parametrized PyTest that checks must_include and must_not_include for every golden item, with "
              "item ids shown in the test names.",
         sample="12 passed in 0.8s",
         hints=["ids=lambda i: i[\"id\"] gives readable test names."]),
    dict(title="Catch a Regression", level="Medium", concepts="prompt and config versions",
         text="A teammate changes k from 3 to 1 \"to save cost\" in config v2. Run the golden tests for v1 and v2 and "
              "report which items regressed.",
         sample="v1: 8/12 passed (offline)\nv2: 6/12 passed\nRegressed: leave-003, travel-003",
         hints=["Compare per item, not only totals."]),
    dict(title="Tool-call Fidelity", level="Medium", concepts="tool selection, JSON Schema, exact arguments", new=True,
         text="Write 8 cases for the SmartDesk assistant (refund, plan change, ticket lookup, and two where no tool should "
              "be called). Test the tool name, schema validity and exact argument values.",
         sample="8 cases: tool 8/8 | schema 7/7 | exact args 6/7\nFAIL: 'Refund 1,200 on ORD-9' -> amount 1 (comma parsing)",
         hints=["A wrong amount is worse than no call. Test values, not just names."]),
    dict(title="Context Precision, Recall and Citations", level="Medium", concepts="retrieval metrics, citations",
         text="Compute precision, recall and average precision for k = 1, 3 and 5, then check citation accuracy: is every "
              "cited chunk retrieved and relevant?",
         sample="k=1: precision 0.58 recall 0.58\nk=5: precision 0.18 recall 0.92\ncitation accuracy: 0.83",
         hints=["More chunks usually raise recall and lower precision."]),
    dict(title="BLEU from Scratch", level="Medium", concepts="n-grams, brevity penalty",
         text="Implement BLEU (1 to 4-grams, brevity penalty). Score an exact copy, a correct paraphrase and a wrong "
              "answer that reuses words. Explain the result.",
         sample="copy 1.00 | paraphrase 0.11 | wrong but similar words 0.63",
         hints=["Add 1 smoothing so a missing 4-gram does not make the score zero."]),
    dict(title="Cost-aware Quality Gate", level="Challenging", concepts="thresholds, tokens, cost, exit codes", new=True,
         text="Extend quality_gate.py so it fails when recall < 0.85, pass rate drops more than 0.05 versus the v1 "
              "baseline, or estimated cost per query rises more than 20% versus the baseline. Show v1 pass, v2 fail on "
              "quality and v3 (k = 8) fail on cost.",
         sample="v1: PASS\nv2: FAIL recall 0.58 < 0.85\nv3: FAIL cost per query up 54% vs baseline -> exit 1",
         hints=["sys.exit(1) makes the CI step fail.", "Label prices as placeholders in the report."]),
    dict(title="Eval-first Feature with Codex", level="Stretch", concepts="eval-first development, AGENTS.md", new=True,
         text="Write golden items requiring a citation like [c7] in every answer. Run them and see them fail. Then ask "
              "Codex to add citations to the RAG answer, rerun the evals and the gate, and record the diff summary.",
         sample="before: citation tests 0/12\nafter Codex change: 12/12, gate PASS",
         hints=["Add the eval command to AGENTS.md so Codex runs it after each change."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "A verified, versioned reference set of questions and answers is a ________ dataset.",
        "Rerunning tests after a change to catch things that got worse is ________ testing.",
        "Checks such as must-include phrases are ________ checks.",
        "Context precision = relevant retrieved / ________.",
        "Context recall = needed evidence found / needed ________.",
        "Checking that an agent called the right tool with exact arguments is tool-call ________ testing.",
        "Tool arguments are validated against a JSON ________.",
        "BLEU's brevity ________ stops very short outputs scoring well.",
        "Writing evals before asking Codex to build a feature is eval-________ development.",
        "To make a CI step fail, a script exits with a non-zero ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "What makes a golden dataset trustworthy?",
        "Describe how you would test a prompt change and a tool-calling change before release.",
        "Why should a quality gate include token and cost metrics? Give an example rule.",
        "When is BLEU a poor choice of metric?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        'retrieved = ["c1", "c4", "c7"]\nrelevant = {"c4"}\nprint(round(sum(c in relevant for c in retrieved) / len(retrieved), 2))',
        'call = {"name": "issue_refund", "args": {"order_id": "ORD-77", "amount": "300"}}\n'
        'expected = {"order_id": "ORD-77", "amount": 300}\nprint(call["args"] == expected)',
        'base, new = 0.0040, 0.0052          # cost per query, placeholder\nprint(new > base * 1.2)',
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a golden item as a JSON line, including must_include and must_not_include."),
        dict(q="Write a PyTest test parametrized over tool-call cases that checks name and exact arguments."),
        dict(q="Write functions for context precision and context recall."),
        dict(q="Write a gate check that exits with code 1 if cost per query rises more than 20% versus the baseline."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

HANDBOOK = '''%%writefile knowledge.md
# Sakura Logistics Employee Handbook (sample)
## 1. Working hours
Standard working hours are 9:30 to 18:30, Monday to Friday. Teams in the Tokyo office follow JST and teams in the Bengaluru office follow IST.
Flexible start times between 8:00 and 11:00 are allowed with manager approval.
## 2. Leave policy
Full-time employees receive 18 days of paid leave per year. Leave accrues monthly at 1.5 days.
Unused leave can be carried forward up to a maximum of 10 days. Carried forward leave expires on 31 March of the following year.
Sick leave is separate: employees receive 8 days of paid sick leave per year. A medical certificate is required for sick leave longer than 2 consecutive days.
## 3. Remote work
Employees may work remotely up to 2 days per week. Remote work must be logged in the HR portal by 10:00 on the same day.
Remote work from another country requires approval from HR and the security team at least 14 days in advance.
## 4. Expenses
Travel expenses must be submitted within 30 days with receipts. Meals during business travel are reimbursed up to 2,000 INR or 4,000 JPY per day.
Expenses above 50,000 INR require approval from a director before booking.
## 5. Security
Laptops must use full disk encryption. Customer data must never be copied to personal devices or uploaded to unapproved AI tools.
Security incidents must be reported to security@sakura-logistics.example within 1 hour of discovery.
## IT FAQ
Error VPN-417 means your VPN certificate has expired. Renew it from the IT self-service portal and restart the VPN client.
Password resets are done through the self-service portal. Passwords must be at least 14 characters long.
Approved AI tools are listed on the IT intranet page. Do not paste customer data into tools that are not on that list.
New laptops are issued within 5 working days of a request approved by your manager.
## Travel FAQ
Book flights through the corporate travel desk at least 10 days before travel. Economy class is standard for flights under 6 hours.
Hotel stays are reimbursed up to 6,000 INR per night in India and 15,000 JPY per night in Japan.
Visa support letters are issued by HR within 3 working days.'''

NOTEBOOK = dict(subtitle="Golden datasets, prompt regression tests, tool-call fidelity, precision and recall, citations, "
                         "BLEU and cost-aware quality gates", cells=[
    ("md", "## 1. Install"),
    ("code", '''# ===== Option A: Google Colab (active) =====
# Add your key once: click the key icon (Secrets) in the left sidebar, name it OPENAI_API_KEY, and allow notebook access.
!pip install -q openai scikit-learn numpy pandas pytest jsonschema tiktoken

# ===== Option B: VS Code / local =====
# pip install openai scikit-learn numpy pandas pytest jsonschema tiktoken
# Create a .env file (git-ignored) or set the variable in your terminal:  OPENAI_API_KEY=...
# No key? Everything still runs in OFFLINE demo mode with a tiny built-in stand-in model.
print("Setup done")'''),
    ("helpers",),
    ("md", "## 2. The system under test, with versioned configs\nv2 lowers k \"to save cost\". v3 raises k \"to improve "
           "recall\". Both are realistic changes a teammate might make."),
    ("code", HANDBOOK),
    ("code", '''%%writefile rag_system.py
import re, numpy as np
from genai_helpers import llm, embed, usage

TEXT = open("knowledge.md").read()
CHUNKS = [s.strip() for s in re.split(r"(?<=[.!?])\\s+", re.sub(r"#+ .*\\n", "", TEXT)) if s.strip()]
IDS = [f"c{i + 1}" for i in range(len(CHUNKS))]
VECS = embed(CHUNKS)
BASE = "Answer using ONLY the context. If the answer is not there, say \\"I don't know\\"."
CONFIGS = {
    "v1": {"k": 3, "system": BASE},
    "v2": {"k": 1, "system": "Answer briefly. " + BASE},          # "save cost"
    "v3": {"k": 8, "system": BASE},                               # "improve recall"
}

def retrieve(question, k):
    order = np.argsort(VECS @ embed(question)[0])[::-1][:k]
    return [IDS[i] for i in order], [CHUNKS[i] for i in order]

def answer(question, version="v1", cite=False):
    cfg = CONFIGS[version]
    ids, ctx = retrieve(question, cfg["k"])
    context = "\\n".join(f"[{i}] {c}" if cite else c for i, c in zip(ids, ctx))
    out = llm("Context:\\n" + context + f"\\n\\nQuestion: {question}", system=cfg["system"], temperature=0)
    if cite and "[" not in out:                         # offline stand-in: cite the chunk the answer came from
        src = next((i for i, c in zip(ids, ctx) if c.strip(" ") in out or out.strip() in c), None)
        out = out + (f" [{src}]" if src else "")
    return out, ids

def answer_with_usage(question, version="v1"):
    out, ids = answer(question, version)
    return out, ids, usage()'''),
    ("md", "## 3. A golden dataset (versioned JSONL)"),
    ("code", '''import json, re, importlib, rag_system
importlib.reload(rag_system)
from rag_system import CHUNKS, IDS, answer, retrieve

def cid(fragment):
    return [IDS[i] for i, c in enumerate(CHUNKS) if fragment in c]

GOLDEN = [
    ("leave-001", "How many paid leave days do full-time staff get?", "18 days", ["18 days"], ["8 days"], "18 days of paid leave", "leave"),
    ("leave-002", "How many sick days do I get each year?", "8 days", ["8 days"], ["18 days"], "8 days of paid sick leave", "leave"),
    ("leave-003", "When does carried over leave expire?", "31 March", ["31 March"], ["30 June"], "expires on 31 March", "leave"),
    ("remote-001", "How many days a week can I work remotely?", "2 days", ["2 days"], ["5 days"], "up to 2 days per week", "remote"),
    ("remote-002", "How far ahead must I request remote work abroad?", "14 days", ["14 days"], [], "at least 14 days in advance", "remote"),
    ("travel-001", "Hotel limit per night in Japan?", "15,000 JPY", ["15,000 JPY"], ["6,000 INR per night in Japan"], "15,000 JPY", "travel"),
    ("travel-002", "Deadline for submitting travel expenses?", "30 days", ["30 days"], [], "within 30 days", "travel"),
    ("travel-003", "How early should flights be booked?", "10 days", ["10 days"], [], "10 days before travel", "travel"),
    ("it-001", "What does error VPN-417 mean?", "VPN certificate has expired", ["certificate"], [], "VPN-417", "it"),
    ("it-002", "Minimum password length?", "14 characters", ["14 characters"], [], "14 characters", "it"),
    ("it-003", "How long does a new laptop take?", "5 working days", ["5 working days"], [], "5 working days", "it"),
    ("sec-001", "How fast must I report a security incident?", "1 hour", ["1 hour"], ["24 hours"], "within 1 hour", "security"),
]
with open("golden_v1.jsonl", "w") as f:
    for gid, q, exp, inc, exc, frag, topic in GOLDEN:
        f.write(json.dumps({"id": gid, "question": q, "expected": exp, "must_include": inc, "must_not_include": exc,
                            "relevant_ids": cid(frag), "tags": {"topic": topic, "lang": "en"}, "version": 1}) + "\\n")
golden = [json.loads(l) for l in open("golden_v1.jsonl")]
print(len(golden), "golden items. Example:\\n", json.dumps(golden[2], indent=2))'''),
    ("md", "## 4. Prompt regression tests with PyTest\nThe version under test comes from an environment variable, exactly "
           "as a CI pipeline would set it."),
    ("code", '''%%writefile test_golden.py
import json, os, pytest
from rag_system import answer

VERSION = os.getenv("PROMPT_VERSION", "v1")
GOLDEN = [json.loads(l) for l in open("golden_v1.jsonl")]

@pytest.mark.parametrize("item", GOLDEN, ids=lambda i: i["id"])
def test_golden_item(item):
    out, _ = answer(item["question"], VERSION)
    for phrase in item["must_include"]:
        assert phrase.lower() in out.lower(), f"missing '{phrase}' in: {out}"
    for phrase in item["must_not_include"]:
        assert phrase.lower() not in out.lower(), f"forbidden '{phrase}' in: {out}"'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!PROMPT_VERSION=v1 python -m pytest -q --color=no -p no:cacheprovider test_golden.py 2>&1 | tail -2
!PROMPT_VERSION=v2 python -m pytest -q --color=no -p no:cacheprovider test_golden.py 2>&1 | tail -2
# ===== Option B: VS Code terminal =====
# Windows PowerShell:  $env:PROMPT_VERSION="v2"; pytest -q test_golden.py
# macOS/Linux:          PROMPT_VERSION=v2 pytest -q test_golden.py'''),
    ("md", "### Per-item comparison: what exactly regressed?"),
    ("code", '''import pandas as pd

def passes(item, version):
    out, ids = answer(item["question"], version)
    ok = all(p.lower() in out.lower() for p in item["must_include"]) and not any(p.lower() in out.lower() for p in item["must_not_include"])
    return ok, ids

rows = []
for g in golden:
    ok1, _ = passes(g, "v1"); ok2, _ = passes(g, "v2")
    rows.append({"id": g["id"], "v1": ok1, "v2": ok2, "status": "REGRESSED" if ok1 and not ok2 else ("fixed" if ok2 and not ok1 else "")})
cmp = pd.DataFrame(rows)
print(cmp.to_string(index=False))
print(f"\\nv1 pass rate {cmp.v1.mean():.2f} | v2 pass rate {cmp.v2.mean():.2f} | regressed: {list(cmp[cmp.status == 'REGRESSED'].id)}")
if not ONLINE:
    print("Offline, the stand-in answers by picking one sentence, so absolute pass rates are low. The comparison between versions is still meaningful.")'''),
    ("md", "## 5. NEW (v4): Tool-call fidelity tests\nFor agents, the tool call is the answer. We test the tool name, "
           "schema-valid arguments, exact values, and that no tool is called when none is needed. Offline, a small "
           "rule-based chooser stands in for the model's function calling."),
    ("code", '''%%writefile tools_under_test.py
import json, os, re

SCHEMAS = {
    "issue_refund": {"type": "object", "required": ["order_id", "amount"], "additionalProperties": False,
                     "properties": {"order_id": {"type": "string", "pattern": "^ORD-[0-9]+$"}, "amount": {"type": "integer", "minimum": 1}}},
    "change_plan": {"type": "object", "required": ["customer_id", "plan"], "additionalProperties": False,
                    "properties": {"customer_id": {"type": "string"}, "plan": {"type": "string", "enum": ["Basic", "Family 5G", "Unlimited"]}}},
    "lookup_ticket": {"type": "object", "required": ["ticket_id"], "additionalProperties": False,
                      "properties": {"ticket_id": {"type": "string", "pattern": "^T-[0-9]+$"}}},
}

def choose_tool(message):
    """Return (tool_name, args) or (None, None). Offline rule-based stand-in for model function calling.
    Online, send SCHEMAS as tools to the chat completions API and read message.tool_calls instead."""
    m = message.lower()
    order = re.search(r"ORD-\\d+", message)
    if "refund" in m and order:
        amount = re.search(r"refund (?:of )?([\\d,]+)", m)
        return "issue_refund", {"order_id": order.group(0), "amount": int(amount.group(1).split(",")[0]) if amount else 0}
    plan = next((p for p in ["Basic", "Family 5G", "Unlimited"] if p.lower() in m), None)
    cust = re.search(r"C-\\d+", message)
    if ("switch" in m or "change" in m) and plan and cust:
        return "change_plan", {"customer_id": cust.group(0), "plan": plan}
    ticket = re.search(r"T-\\d+", message)
    if ticket and ("status" in m or "ticket" in m):
        return "lookup_ticket", {"ticket_id": ticket.group(0)}
    return None, None'''),
    ("code", '''%%writefile test_tool_calls.py
import pytest
from jsonschema import validate
from tools_under_test import SCHEMAS, choose_tool

CASES = [
    ("Please refund 300 on order ORD-77", "issue_refund", {"order_id": "ORD-77", "amount": 300}),
    ("Refund of 50 for ORD-12 please", "issue_refund", {"order_id": "ORD-12", "amount": 50}),
    ("Refund 1,200 on ORD-9", "issue_refund", {"order_id": "ORD-9", "amount": 1200}),
    ("Switch C-1002 to the Family 5G plan", "change_plan", {"customer_id": "C-1002", "plan": "Family 5G"}),
    ("What is the status of ticket T-881?", "lookup_ticket", {"ticket_id": "T-881"}),
    ("Hi, thanks for your help!", None, None),
    ("What is the weather in Osaka?", None, None),
]

@pytest.mark.parametrize("msg,tool,args", CASES, ids=[c[0][:24] for c in CASES])
def test_tool_call(msg, tool, args):
    name, got = choose_tool(msg)
    assert name == tool, f"expected tool {tool}, got {name}"
    if tool:
        validate(got, SCHEMAS[tool])          # schema-valid arguments
        assert got == args, f"args {got} != {args}"'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!python -m pytest -q --color=no -p no:cacheprovider test_tool_calls.py 2>&1 | tail -4
# ===== Option B: VS Code terminal =====
# pytest -q test_tool_calls.py'''),
    ("md", "One case fails on purpose: the chooser reads `1,200` as `1`. A wrong amount is worse than no call. "
           "**TODO:** fix the parsing in `tools_under_test.py` and rerun until all cases pass."),
    ("md", "## 6. Context precision, recall and average precision"),
    ("code", '''def precision(ret, rel):
    return sum(c in rel for c in ret) / len(ret)

def recall(ret, rel):
    return len(set(ret) & set(rel)) / len(rel)

def avg_precision(ret, rel):
    hits, total = 0, 0.0
    for k, c in enumerate(ret, 1):
        if c in rel:
            hits += 1
            total += hits / k
    return total / len(rel)

table = []
for k in [1, 3, 5]:
    p, r, ap = [], [], []
    for g in golden:
        ret, _ = retrieve(g["question"], k)
        rel = set(g["relevant_ids"])
        p.append(precision(ret, rel)); r.append(recall(ret, rel)); ap.append(avg_precision(ret, rel))
    table.append({"k": k, "precision": round(sum(p) / len(p), 2), "recall": round(sum(r) / len(r), 2), "avg_precision": round(sum(ap) / len(ap), 2)})
print(pd.DataFrame(table).to_string(index=False))'''),
    ("md", "## 7. Citations, written eval-first\n**NEW (v4): eval-first development with Codex.** First we write the "
           "eval for the new behaviour (every answer cites a retrieved, relevant chunk) and watch it fail. Then we "
           "turn the feature on (the change you would ask Codex for) and rerun the same eval."),
    ("code", '''CITE = re.compile(r"\\[(c\\d+)\\]")

def citation_eval(cite):
    rows = []
    for g in golden:
        out, ids = answer(g["question"], "v1", cite=cite)
        cited = CITE.findall(out)
        rows.append({"id": g["id"], "has_citation": bool(cited),
                     "cited_retrieved": bool(cited) and all(c in ids for c in cited),
                     "cited_relevant": bool(cited) and all(c in g["relevant_ids"] for c in cited)})
    return pd.DataFrame(rows)

before = citation_eval(cite=False)
print("BEFORE (eval written, feature not built):", before[["has_citation", "cited_retrieved", "cited_relevant"]].mean().round(2).to_dict())
after = citation_eval(cite=True)
print("AFTER  (feature built, same eval):        ", after[["has_citation", "cited_retrieved", "cited_relevant"]].mean().round(2).to_dict())'''),
    ("md", "A Codex prompt for the change: *\"Make `answer()` include the chunk id in square brackets for every fact it "
           "uses. Do not change retrieval. Run `python -m pytest test_golden.py` and the citation eval, and show the "
           "diff.\"* Put the eval command in `AGENTS.md` so Codex runs it after every change."),
    ("md", "## 8. BLEU from scratch, and where it misleads"),
    ("code", '''import math
from collections import Counter

def ngrams(tokens, n):
    return Counter(tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1))

def bleu(candidate, reference, max_n=4):
    c, r = re.findall(r"\\w+", candidate.lower()), re.findall(r"\\w+", reference.lower())
    logs = []
    for n in range(1, max_n + 1):
        cn, rn = ngrams(c, n), ngrams(r, n)
        overlap = sum(min(cnt, rn[g]) for g, cnt in cn.items())
        logs.append(math.log((overlap + 1) / (max(1, sum(cn.values())) + 1)))      # add-1 smoothing
    bp = 1.0 if len(c) > len(r) else math.exp(1 - len(r) / max(1, len(c)))
    return round(bp * math.exp(sum(logs) / max_n), 2)

ref = "Carried forward leave expires on 31 March of the following year."
cases = {
    "exact copy": ref,
    "correct paraphrase": "Any leave you roll over must be used by the end of next March.",
    "wrong, similar words": "Carried forward leave expires on 30 June of the following year.",
}
for name, cand in cases.items():
    print(f"{name:<22} BLEU {bleu(cand, ref)}")
print("\\nThe wrong answer scores far higher than the correct paraphrase. Use BLEU for translation-like tasks, not open answers.")'''),
    ("md", "## 9. NEW (v4): Token and cost metrics\nPrices are **placeholders**, not real prices. Offline token counts "
           "are estimates."),
    ("code", '''from rag_system import answer_with_usage
PRICE_PER_1M = {"input": 1.00, "output": 4.00}       # PLACEHOLDER prices

def cost_profile(version):
    tin, tout = [], []
    for g in golden:
        _, _, u = answer_with_usage(g["question"], version)
        tin.append(u["input_tokens"]); tout.append(u["output_tokens"])
    cpq = (sum(tin) * PRICE_PER_1M["input"] + sum(tout) * PRICE_PER_1M["output"]) / 1_000_000 / len(golden)
    return {"version": version, "avg_input_tokens": round(sum(tin) / len(tin)), "avg_output_tokens": round(sum(tout) / len(tout)),
            "cost_per_query": round(cpq, 6), "cost_per_1000": round(cpq * 1000, 3)}

print(pd.DataFrame([cost_profile(v) for v in ["v1", "v2", "v3"]]).to_string(index=False))
print("(placeholder prices)")'''),
    ("md", "## 10. A cost-aware quality gate for CI"),
    ("code", '''%%writefile quality_gate.py
import json, os, sys
from rag_system import answer_with_usage

VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"
THRESHOLDS = {"recall": 0.85}          # absolute floor for retrieval
MAX_DROP = 0.05                         # allowed pass-rate drop versus the baseline (v1)
MAX_COST_RISE = 0.20                    # allowed rise in cost per query versus the baseline
PRICE_PER_1M = {"input": 1.00, "output": 4.00}   # PLACEHOLDER prices

golden = [json.loads(l) for l in open("golden_v1.jsonl")]
passed, recalls, tin, tout = 0, [], 0, 0
for g in golden:
    out, ids, u = answer_with_usage(g["question"], VERSION)
    ok = all(p.lower() in out.lower() for p in g["must_include"]) and not any(p.lower() in out.lower() for p in g["must_not_include"])
    passed += ok
    recalls.append(len(set(ids) & set(g["relevant_ids"])) / len(g["relevant_ids"]))
    tin += u["input_tokens"]; tout += u["output_tokens"]
cost = (tin * PRICE_PER_1M["input"] + tout * PRICE_PER_1M["output"]) / 1_000_000 / len(golden)
scores = {"pass_rate": round(passed / len(golden), 2), "recall": round(sum(recalls) / len(recalls), 2),
          "avg_input_tokens": round(tin / len(golden)), "cost_per_query": round(cost, 6)}
failures = [f"{k} {scores[k]} < {v}" for k, v in THRESHOLDS.items() if scores[k] < v]
if VERSION != "v1" and os.path.exists("report_v1.json"):
    base = json.load(open("report_v1.json"))["scores"]
    if scores["pass_rate"] < base["pass_rate"] - MAX_DROP:
        failures.append(f"pass_rate dropped {base['pass_rate'] - scores['pass_rate']:.2f} vs baseline")
    rise = scores["cost_per_query"] / base["cost_per_query"] - 1
    if rise > MAX_COST_RISE:
        failures.append(f"cost per query up {rise:.0%} vs baseline (placeholder prices)")
print(f"{VERSION}: {'FAIL' if failures else 'PASS'} {scores}" + (f" -> {failures}" if failures else ""))
json.dump({"version": VERSION, "scores": scores, "failures": failures}, open(f"report_{VERSION}.json", "w"), indent=2)
sys.exit(1 if failures else 0)'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!python quality_gate.py v1 && echo "Gate passed: release allowed"
!python quality_gate.py v2 || echo "Gate failed: release blocked"
!python quality_gate.py v3 || echo "Gate failed: release blocked"
# ===== Option B: VS Code terminal / Azure Pipelines step =====
# python quality_gate.py v3      (a non-zero exit code fails the pipeline stage)'''),
    ("md", "v2 fails on quality (recall). v3 retrieves more but every query now carries much more context: it fails "
           "on cost. A change like v3 needs a human decision about whether the quality gain is worth the price."),
    ("md", "### TODO: with a real model (API key), add an absolute threshold of `pass_rate >= 0.9` to `THRESHOLDS`, add "
           "an `avg_output_tokens` limit, and rerun the gate for all three versions."),
    ("code", "# TODO: write your code here"),
])
