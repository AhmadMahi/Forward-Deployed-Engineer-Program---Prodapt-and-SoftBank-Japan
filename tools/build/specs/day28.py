"""Day 28 spec. GenAI 9: Agent Protocols (MCP, A2A) and Advanced Agents.
Source: archive/v1-40-day/Day27. The MCP demo is rebuilt on the current Python SDK (mcp 2.3.0): the v1 pin mcp<2 and
FastMCP are removed; FastMCP is now mcp.server.mcpserver.MCPServer, and mcp.Client connects in-process, over stdio or
over HTTP. Verified in mcp 2.3.0: in-process Client negotiates protocol 2026-07-28; Task types exist in mcp_types
(statuses working, input_required, completed, failed, cancelled) but MCPServer has no built-in task store, so the
notebook simulates the Tasks lifecycle with those types. NEW (v4) topics are marked.
"""
DAY = 28
FOLDER = "Day28-Agent-Protocols-MCP-and-A2A"
SLUG = "Agent_Protocols_MCP_and_A2A"
TITLE = "Agent Protocols (MCP, A2A) and Advanced Agents"
SUBTITLE = "MCP 2026-07-28 on the current SDK, A2A v1.0 signed Agent Cards, agentic handoff and a sandboxed data agent"
DATE = "Thu 03 Dec 2026"
TRACK = "GenAI"
NEXT = "See you on Monday for Day 30: LLM security and guardrails."
CLOSING_GREET = "Yoi shuumatsu wo (良い週末を): Have a great weekend"

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 27"),
        ("Senior FDE interaction", "1 to 2 hrs, plus the FDE assessment debrief"),
        ("Data analysis agent", "Safe code, sandboxed execution. NEW (v4)"),
        ("MCP 2026-07-28", "Stateless, OAuth 2.1, Tasks. NEW (v4)"),
        ("A2A v1.0", "Signed Agent Cards, the Agentic AI Foundation. NEW (v4)"),
        ("Build it", "MCP server on the current SDK, used by an agent and Codex. NEW (v4)"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Build a data agent", "Check generated code and run it in a sandbox with limits."),
        ("Explain MCP and A2A", "Roles, primitives, the 2026-07-28 changes and signed Agent Cards."),
        ("Build an MCP server", "With MCPServer on mcp 2.x, called from a client and an agent."),
        ("Connect Codex", "Add your MCP server to OpenAI Codex safely."),
    ]),
    dict(type="callout", title="Senior FDE interaction", text="A senior FDE walks through an agent deployment at a "
         "customer: legacy integration, security review, what broke in week one and how trust was rebuilt.",
         sub="Then the FDE assessment debrief. Capture one lesson for your capstone.",
         greet="Senpai (先輩): A senior colleague who guides you"),

    dict(type="section", title="A data analysis agent", sub="Plain-language questions, real numbers"),
    dict(type="flow", title="How it works", items=[
        ("Question", "\"Which city had the highest revenue?\""),
        ("Generate code", "Model writes pandas code"),
        ("Check code", "AST: block imports, files, dunders"),
        ("Run in sandbox", "Separate process, limits, no network"),
        ("Explain", "Answer with the number and the code"),
    ]),
    dict(type="table", title="Making generated code safe", header=["Risk", "Mitigation"], rows=[
        ["Reading or deleting files", "Block open, os, sys, subprocess; inspect the AST"],
        ["Calling the internet", "No network in the sandbox"],
        ["Endless loops, memory bombs", "CPU, memory and time limits; row limits"],
        ["Wrong but plausible answers", "Show the code and the result table with the answer"],
        ["Sensitive data", "Only approved, masked datasets, mounted read-only"],
    ]),
    dict(type="compare", title="Sandboxed code execution", new=True, left=dict(title="Not enough", bullets=[
        "exec() in your own process", "A blocklist of a few names", "Full network and file access",
    ]), right=dict(title="Container sandbox", bullets=[
        "Separate container per run, deleted after", "--network none, read-only file system",
        "CPU, memory and time limits", "Non-root user, approved data mounted read-only",
    ]), note="Today's notebook uses a subprocess with limits offline, and shows the Docker version for your laptop."),
    dict(type="code", title="A container sandbox in one command", new=True, code='''docker run --rm \\
  --network none --read-only --memory 256m --cpus 0.5 \\
  --pids-limit 64 --user 1000:1000 \\
  -v "$PWD/data:/data:ro" -v "$PWD/job:/job:ro" \\
  python:3.12-slim timeout 10 python /job/analysis.py''',
         note="Docker Desktop on your laptop. Managed code interpreters give the same isolation as a service."),

    dict(type="section", title="Model Context Protocol (MCP)", sub="One standard plug for tools and data"),
    dict(type="compare", title="Before and after MCP", left=dict(title="Before", bullets=[
        "Every app wires every tool its own way", "N apps x M tools integrations", "Hard to reuse or share",
    ]), right=dict(title="With MCP", bullets=[
        "Tools exposed once as an MCP server", "Any MCP-capable app can use them (including Codex)",
        "Like USB for AI integrations",
    ]), greet="Tsunagu (繋ぐ): To connect"),
    dict(type="table", title="MCP roles and primitives", header=["Term", "Meaning"], rows=[
        ["Host", "The AI application the user works in (IDE, Codex, chat app, agent)"],
        ["Client", "The connector inside the host that talks to one server"],
        ["Server", "Exposes capabilities from a system (database, CRM, files)"],
        ["Tools", "Actions the model can call, with JSON schemas"],
        ["Resources", "Read-only data the host can load as context"],
        ["Prompts", "Reusable prompt templates offered by the server"],
    ], note="Transports: stdio for local servers, Streamable HTTP for remote ones."),
    dict(type="cards", title="MCP specification 2026-07-28", new=True, items=[
        ("Stateless requests", "No initialize handshake; clients discover once and each request stands alone."),
        ("OAuth 2.1", "Remote servers verify bearer tokens with scopes and audience (resource indicators)."),
        ("Tasks", "Long-running calls return a task: working, input_required, completed, failed, cancelled."),
        ("Caching hints", "Servers say how long lists and results can be cached."),
    ], note="Checked against the Python SDK mcp 2.3.0, which negotiates protocol version 2026-07-28."),
    dict(type="bullets_code", title="An MCP server on the current SDK", new=True, bullets=[
        "mcp 2.x: FastMCP is now MCPServer",
        "Decorators register tools, resources, prompts",
        "Type hints become the schema",
        "Remove old pins such as mcp<2",
    ], code='''from mcp.server.mcpserver import MCPServer

mcp = MCPServer("smartdesk-tickets", version="1.0")

@mcp.tool()
def get_ticket(ticket_id: str) -> str:
    """Look up a ticket, e.g. T-1001."""
    return lookup(ticket_id)

@mcp.resource("policy://sla")
def sla_policy() -> str:
    return "P1: 4 hours. P2: 1 day."

if __name__ == "__main__":
    mcp.run()          # stdio''', greet="Atarashii (新しい): New"),
    dict(type="bullets_code", title="Calling it with mcp.Client", new=True, bullets=[
        "Pass the server object: in-process (tests)",
        "Pass StdioServerParameters: local process",
        "Pass a URL: remote Streamable HTTP",
        "Same calls in all three cases",
    ], code='''from mcp import Client, StdioServerParameters

async with Client(mcp) as c:            # in-process
    tools = await c.list_tools()
    r = await c.call_tool("get_ticket",
                          {"ticket_id": "T-1001"})
    print(c.protocol_version)           # 2026-07-28

params = StdioServerParameters(
    command="python", args=["mcp_server.py"])
async with Client(params) as c: ...'''),
    dict(type="bullets_code", title="Remote MCP: stateless HTTP and OAuth 2.1", new=True, bullets=[
        "stateless_http=True: no server session to lose",
        "A TokenVerifier checks each bearer token",
        "Require scopes per tool; short-lived tokens",
        "Check the token audience is this server",
    ], code='''from mcp.server.auth.settings import AuthSettings

mcp = MCPServer("smartdesk", token_verifier=MyVerifier(),
    auth=AuthSettings(
        issuer_url="https://login.example.com",
        resource_server_url="https://mcp.example.com",
        required_scopes=["tickets:read"],
        validate_token_resource=True))

mcp.run("streamable-http", stateless_http=True)'''),
    dict(type="flow", title="MCP Tasks: long-running tool calls", new=True, items=[
        ("Call", "Client starts a slow tool"),
        ("Task created", "Server returns a task id"),
        ("Working", "Client polls status"),
        ("Input required", "Optional: ask the user"),
        ("Completed", "Client fetches the result"),
    ], note="Use for exports, scans and reports. Set a TTL and allow cancel."),
    dict(type="cards", title="MCP from an agent and from Codex", new=True, items=[
        ("From an agent", "List MCP tools, wrap them as agent tools, let the agent call them."),
        ("From Codex", "Add the server in Codex settings (config.toml mcp_servers) or with 'codex mcp add'."),
        ("Least privilege", "Read-only tools for Codex; no customer data in a dev setup."),
        ("Review servers", "Install only reviewed MCP servers. Pin versions."),
    ], note="Check the current Codex documentation for the exact commands in your version."),
    dict(type="table", title="MCP security checklist", header=["Rule", "Why"], rows=[
        ["Authenticate remote servers (OAuth 2.1)", "Anyone can otherwise call your tools"],
        ["Least privilege per tool and scope", "A leaked token does less damage"],
        ["Validate inputs, log every call", "Audit and detect abuse"],
        ["Treat tool results as untrusted", "A server can inject instructions into the model"],
        ["Review and pin third-party servers", "Supply chain risk (Day 23, Day 30)"],
    ]),

    dict(type="section", title="Agent-to-Agent (A2A)", sub="Agents from different teams and vendors working together"),
    dict(type="compare", title="MCP and A2A", left=dict(title="MCP", bullets=[
        "Agent to tools and data", "Server exposes functions", "The agent stays in charge",
    ]), right=dict(title="A2A", bullets=[
        "Agent to agent", "Each agent keeps its own tools and reasoning", "Delegates whole tasks, gets results back",
    ])),
    dict(type="table", title="A2A building blocks", header=["Concept", "What it is"], rows=[
        ["Agent Card", "JSON at a well-known URL: name, skills, endpoint, auth"],
        ["Task", "A unit of work with a lifecycle: submitted, working, completed, failed"],
        ["Message", "Turns of conversation between client and remote agent"],
        ["Artifact", "The result produced by the task: text, file or data"],
    ]),
    dict(type="cards", title="A2A v1.0 and signed Agent Cards", new=True, items=[
        ("v1.0", "A stable specification, with JSON-RPC and gRPC bindings."),
        ("Signed Agent Cards", "The card is signed; clients verify it before trusting the skills and endpoint."),
        ("Why it matters", "A forged card could redirect tasks and data to an attacker."),
        ("Registry", "Keep an approved list of agents and their public keys."),
    ], note="Check the A2A v1.0 specification for the exact card fields and signature format."),
    dict(type="cards", title="The Agentic AI Foundation", new=True, items=[
        ("What it is", "A neutral, Linux Foundation home for open agent standards."),
        ("Projects", "MCP and AGENTS.md among others; OpenAI is a co-founder."),
        ("Why FDEs care", "Customers prefer open, vendor-neutral standards for long-lived integrations."),
        ("A2A", "Also governed under the Linux Foundation, with broad industry adoption."),
    ]),

    dict(type="section", title="Agentic handoff", sub="Never make the next person start from zero"),
    dict(type="cards", title="A good handoff payload", items=[
        ("Summary", "The goal and where things stand, in two sentences."),
        ("Facts collected", "Ticket id, amounts, what the customer said."),
        ("Steps tried", "Tools called and their results."),
        ("Reason", "Why the handoff: policy, low confidence, angry customer."),
        ("Suggested next step", "What the receiver should probably do."),
        ("Urgency", "How quickly a response is needed."),
    ]),
    dict(type="cards", title="SmartDesk step 24", items=[
        ("MCP server", "get_ticket, list_open_tickets, update_status; resource policy://sla."),
        ("Agent", "The Day 27 assistant now uses the tools through MCP."),
        ("Codex", "Add the server to Codex, read-only, for local development."),
        ("Analytics agent", "Sandboxed pandas over approved ticket CSVs."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("Data agents", "Check the AST, run in a sandbox with limits, show the code."),
        ("MCP", "MCPServer on mcp 2.x; stateless, OAuth 2.1, Tasks in 2026-07-28."),
        ("A2A", "Agent to agent; verify signed Agent Cards before delegating."),
        ("Handoffs", "Summary, facts, steps, reason, next step, urgency."),
    ]),
    dict(type="cards", title="Before Monday", lead="Monday starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day28_Hotel_Lab.md: MCP server, agent run, sandbox."),
        ("Workbook", "Complete the Day 28 workbook."),
        ("Pre-read", "Skim the Day 30 pre-read on AI security."),
    ]),
]

PREREAD = dict(title="Common Languages for AI", lede="A light read before Day 28. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "As AI agents spread, they need standard ways to connect to tools and to each other. Today you meet two "
        "important standards and build two advanced patterns: handing work over cleanly, and an agent that analyses "
        "data safely."]),
    dict(h="1. One plug for many devices", paras=[
        "Before USB, every printer, mouse and camera had its own cable. USB made one plug work everywhere. The **Model "
        "Context Protocol (MCP)** does this for AI: a company exposes its systems once as an MCP server, and any AI "
        "application that speaks MCP can use them, including coding tools such as OpenAI Codex."]),
    dict(h="2. Agents talking to agents", paras=[
        "Your travel agent calls an airline's booking desk. Each side has its own systems and rules; they agree on how "
        "to make and track requests. **Agent-to-Agent (A2A)** is an open protocol for this between AI agents."],
        table=[["Standard", "Connects", "Everyday comparison"],
               ["MCP", "An AI app to tools and data", "Plugging a device into a USB port"],
               ["A2A", "One AI agent to another agent", "Your agent phoning another company's agent"]]),
    dict(h="3. Checking the badge", new=True, paras=[
        "You would not hand a parcel to someone just because they say they are a courier; you check the badge. In "
        "A2A v1.0, an agent's description (its **Agent Card**) can be **signed**, so other agents can check it really "
        "comes from who it claims. MCP servers on the internet now check a **token** on every request, like a "
        "visitor pass with an expiry time."]),
    dict(h="4. An AI data analyst in a locked room", new=True, paras=[
        "Ask \"Which city sold the most last month?\" and an AI writes the code, runs it and explains the answer. "
        "Powerful, and risky. The code must run in a **sandbox**: a locked room with no internet, a time limit and only "
        "the approved data. The answer should show its working so people can check it."],
        box="**Key idea:** standards make AI easier to connect; security rules make it safe to connect."),
    dict(h="5. Think about these before class", bullets=[
        "Which SmartDesk systems would you expose to AI first, and which never?",
        "Describe a handoff you received that was done badly. What was missing?",
        "How would you check that an AI's number is correct?"],
        after=["Tsunagu (繋ぐ): to connect"]),
])

POSTREAD = dict(title="Protocols and Advanced Agents: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Data analysis agent", "Generate code, check the AST, run in a sandbox, show code and result."],
        ["Sandboxing (NEW v4)", "Container per run, no network, read-only data, CPU, memory and time limits."],
        ["MCP", "Open protocol connecting AI applications to tools, resources and prompts."],
        ["MCP 2026-07-28 (NEW v4)", "Stateless requests, OAuth 2.1 for remote servers, Tasks, caching hints."],
        ["Current SDK (NEW v4)", "mcp 2.x: MCPServer replaces FastMCP; mcp.Client connects in-process, stdio or HTTP."],
        ["A2A", "Agent Cards, tasks, messages, artifacts. Complements MCP."],
        ["A2A v1.0 (NEW v4)", "Signed Agent Cards: verify before you delegate."],
        ["Agentic AI Foundation (NEW v4)", "Linux Foundation home for open agent standards such as MCP and AGENTS.md."],
        ["Handoff payload", "Summary, facts, steps tried, reason, suggested next step, urgency."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Migrating v1 MCP code", paras=[
        "Old tutorials import FastMCP from mcp.server.fastmcp and pin mcp<2. On mcp 2.x that import fails with a "
        "message pointing to the migration guide. Rename to MCPServer, use mcp.Client, rerun your tests, then remove the "
        "pin. Ask Codex to do it in small steps, and review every diff."]),
    dict(sub="2. Securing remote MCP servers", paras=[
        "Use short-lived OAuth tokens with narrow scopes, check that each token was issued for your server, and log "
        "every call. Treat tool results as untrusted input: a malicious server can try to inject instructions."]),
    dict(sub="3. Tasks for slow tools", paras=[
        "Exports, scans and reports can take minutes. Return a task, let the client poll, allow cancel, and expire "
        "finished tasks after a TTL."]),
    dict(sub="4. Agent registries", paras=[
        "Enterprises keep a registry of approved agents, their signed cards and public keys, like an API catalogue. "
        "Delegate only to agents in the registry."]),
    dict(sub="5. Managed code execution", paras=[
        "Providers offer hosted code interpreters that run model-written code in isolated containers. For customer "
        "work, prefer these or your own container sandbox over in-process execution."]),
    dict(h="Part C: Check yourself", bullets=[
        "What problem does MCP solve?",
        "Name three changes in the MCP 2026-07-28 specification.",
        "Why should a client verify a signed Agent Card?",
        "List five limits for a code sandbox.",
        "What changed for FastMCP in mcp 2.x?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add a search_faq tool and an apology prompt to the MCP server.",
        "Tamper with a signed Agent Card and confirm verification fails.",
        "Run the data agent in Docker with --network none and compare with the subprocess sandbox."],
        after=["**Coming up on Day 30:** LLM security and guardrails: OWASP Top 10 for LLM and agentic applications, "
               "indirect injection, a red-team suite and vulnerability report v3.",
               "Yoi shuumatsu wo (良い週末を): have a great weekend"]),
])

HANDSON = dict(lede="Eight problems. The MCP and A2A parts run locally in Colab and VS Code; the data agent runs offline "
                    "with templates or online with a model. Offline results show how the code works, not real model "
                    "quality.", problems=[
    dict(title="MCP or A2A?", level="Warm-up", concepts="protocol choice",
         text="Decide which protocol fits: give an assistant access to a CRM; let a procurement agent ask a supplier's "
              "agent for a quote; expose a document store; delegate travel booking to a partner's agent.",
         sample="CRM access: MCP\nSupplier quote: A2A\nDocument store: MCP (resources)\nTravel booking: A2A",
         hints=["Tools and data: MCP. Another agent with its own reasoning: A2A."]),
    dict(title="Your First MCP Server on mcp 2.x", level="Easy", concepts="MCPServer, mcp.Client", new=True,
         text="Build an MCP server with MCPServer and tools get_ticket and list_open_tickets. Connect with mcp.Client "
              "in-process, list the tools, call both, and print the protocol version.",
         sample="protocol: 2026-07-28\ntools: ['get_ticket', 'list_open_tickets']\nget_ticket(T-1001) -> open, P2, network",
         hints=["from mcp.server.mcpserver import MCPServer", "async with Client(mcp) as c: ..."]),
    dict(title="Resources and Prompts", level="Medium", concepts="MCP resources, prompts",
         text="Add an SLA policy resource and a prompt template for apology emails. List and read them from the client.",
         sample="resources: ['policy://sla']\nprompts: ['apology_email']",
         hints=["@mcp.resource(\"policy://sla\") and @mcp.prompt()"]),
    dict(title="MCP Tools for an Agent", level="Medium", concepts="tool wrapping, create_agent", new=True,
         text="Wrap the MCP tools as LangChain tools and give them to a create_agent assistant. Ask about a ticket and "
              "print which MCP tool was called. Then write the Codex config entry for the same server.",
         sample="agent called MCP tool: get_ticket {'ticket_id': 'T-1001'}\n"
                "[mcp_servers.smartdesk]\ncommand = \"python\"\nargs = [\"mcp_server.py\"]",
         hints=["list_tools() gives name, description and input_schema.", "Read-only tools for Codex."]),
    dict(title="Task Lifecycle", level="Medium", concepts="MCP Tasks", new=True,
         text="Simulate a slow export tool that returns a task. Poll it until completed, then fetch the result. Add a "
              "cancel path and a TTL.",
         sample="task 4f2a: working -> working -> completed\nresult: 120 tickets exported\ncancelled task: cancelled",
         hints=["Statuses: working, input_required, completed, failed, cancelled."]),
    dict(title="Signed Agent Card", level="Medium", concepts="A2A v1.0, signatures", new=True,
         text="Sign the refund agent's card with an Ed25519 key. The support agent verifies the card before delegating. "
              "Change one skill in the card and show verification fails.",
         sample="card verified: True -> delegating task\ntampered card verified: False -> refuse to delegate",
         hints=["Sign the canonical JSON (sorted keys) of the card without its signatures field."]),
    dict(title="Data Analysis Agent in a Sandbox", level="Challenging", concepts="AST checks, subprocess limits", new=True,
         text="Ask five questions of the ticket dataset. Run each piece of generated code in a separate process with a "
              "time limit and no access to your files. Show the code, the result and a one-line explanation. Try three "
              "malicious snippets and a never-ending loop.",
         sample="Q: city with most P1 tickets? -> Osaka\nBlocked: import os\nBlocked: open(...)\nKilled: time limit 5s",
         hints=["Block imports, dunder attributes, open, exec and eval.", "Run the Docker version on your laptop."]),
    dict(title="Handoff Payload", level="Stretch", concepts="Pydantic, handoff design",
         text="Define a Handoff model and create a handoff from the bot to a human for an angry customer whose credit "
              "exceeds the bot's limit. Send it as an A2A-style task artifact.",
         sample="Handoff(reason='credit above bot limit', urgency='high', steps_tried=[...], suggested_next_step='approve 3,200 credit')",
         hints=["Write it so the receiver needs no further context."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "MCP stands for Model ________ Protocol.",
        "In MCP, the AI application the user works in is the ________.",
        "Read-only data offered by an MCP server is a ________.",
        "In mcp 2.x, FastMCP was renamed to ________.",
        "The MCP specification released on 2026-07-28 makes requests ________, with no initialize handshake.",
        "Remote MCP servers authorise requests with OAuth ________.",
        "A long-running MCP tool call can return a ________ that the client polls.",
        "An A2A agent publishes its capabilities in an Agent ________.",
        "In A2A v1.0, Agent Cards can be ________ so clients can verify them.",
        "Model-written code should run in a ________, not directly on your machine.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain MCP using the USB analogy, and name the three roles.",
        "Summarise three changes in the MCP 2026-07-28 specification and why each helps.",
        "Why verify a signed Agent Card before delegating a task?",
        "List five limits you would put on a code sandbox for a data agent.",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "import ast\ncode = \"import os\"\nprint(any(isinstance(n, ast.Import) for n in ast.walk(ast.parse(code))))",
        "statuses = ['working', 'working', 'completed']\nprint(statuses.index('completed') + 1, statuses[-1])",
        "card = {'name': 'Refunds', 'skills': ['refund']}\nimport json\nprint(json.dumps(card, sort_keys=True))",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write an MCPServer tool (mcp 2.x) that returns the status of a ticket."),
        dict(q="Write the async client code that lists tools and calls one with mcp.Client."),
        dict(q="Write a function that rejects code containing imports or open() using the ast module."),
        dict(q="Write an Agent Card (JSON) for an invoice-checking agent, with a signatures field."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="A sandboxed data agent, an MCP server on the current SDK used by an agent, MCP Tasks, signed A2A Agent Cards and agentic handoff",
                sign_off="Yoi shuumatsu wo (良い週末を): *Have a great weekend*", cells=[
    ("md", "## 1. Install\nThe MCP demo uses the **current** Python SDK (mcp 2.x). There is no `mcp<2` pin any more."),
    ("code", '''# ===== Option A: Google Colab (active) =====
# Add your key once: click the key icon (Secrets) in the left sidebar, name it OPENAI_API_KEY, and allow notebook access.
!pip install -q openai tiktoken scikit-learn numpy pandas "mcp>=2" langchain langchain-core langchain-openai langgraph cryptography

# ===== Option B: VS Code / local =====
# pip install openai tiktoken scikit-learn numpy pandas "mcp>=2" langchain langchain-core langchain-openai langgraph cryptography
# Create a .env file (git-ignored) or set the variable in your terminal:  OPENAI_API_KEY=...
# No key? Everything still runs in OFFLINE demo mode with built-in stand-ins.
import importlib.metadata as md
print("mcp", md.version("mcp"), "| langchain", md.version("langchain"))'''),
    ("helpers",),
    ("md", "## 2. A data analysis agent\nThe model writes pandas code. We check the code with the AST, then run it."),
    ("code", '''import ast, json, re, sys, os, subprocess, tempfile
import numpy as np, pandas as pd

rng = np.random.default_rng(28)
tickets = pd.DataFrame({
    "month": np.repeat(["Sep", "Oct", "Nov"], 8),
    "city": ["Tokyo", "Osaka", "Bengaluru", "Pune"] * 6,
    "priority": rng.choice(["P1", "P2", "P3"], 24, p=[0.2, 0.5, 0.3]),
    "minutes_to_resolve": rng.integers(20, 600, 24),
})
DATA_DIR = tempfile.mkdtemp()
CSV = os.path.join(DATA_DIR, "tickets.csv")
tickets.to_csv(CSV, index=False)

BANNED_NAMES = {"open", "exec", "eval", "compile", "__import__", "globals", "locals", "getattr", "setattr",
                "os", "sys", "subprocess", "input", "breakpoint"}

def check_code(code):
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            return "imports are not allowed"
        if isinstance(node, ast.Name) and node.id in BANNED_NAMES:
            return f"name '{node.id}' is not allowed"
        if isinstance(node, ast.Attribute) and node.attr.startswith("_"):
            return "private attributes are not allowed"
    return None

TEMPLATES = {   # offline stand-in for the model writing pandas code
    "most p1": "result = df[df.priority == 'P1'].groupby('city').size().idxmax()",
    "average resolution by month": "result = df.groupby('month', sort=False)['minutes_to_resolve'].mean().round(1).to_dict()",
    "slowest city": "result = df.groupby('city')['minutes_to_resolve'].median().idxmax()",
}

def write_code(question):
    if ONLINE:
        r = llm(f"Write pandas code using an existing DataFrame df with columns {list(tickets.columns)}. "
                f"Store the answer in a variable named result. No imports. Code only.\\nQuestion: {question}", temperature=0)
        return r.replace("```python", "").replace("```", "").strip()
    return next((c for k, c in TEMPLATES.items() if k in question.lower()), "result = len(df)")
print(check_code("result = df.head()"), "|", check_code("import os"))'''),
    ("md", "## 3. NEW (v4): Sandboxed code execution\nEach run happens in a **separate process** with a time limit, CPU and "
           "memory limits, an empty environment and a throwaway working folder. This is the offline fallback. On your "
           "laptop, the Docker cell below adds **no network** and a read-only file system."),
    ("code", '''def run_sandboxed(code, csv_path=CSV, timeout=5):
    problem = check_code(code)
    if problem:
        return f"BLOCKED: {problem}"
    job = (f"import pandas as pd\\ndf = pd.read_csv({csv_path!r})\\n"
           f"{code}\\nprint(repr(result))\\n")

    def limits():                                   # POSIX only (Colab, Linux, macOS)
        try:
            import resource
            resource.setrlimit(resource.RLIMIT_CPU, (timeout, timeout))
            resource.setrlimit(resource.RLIMIT_AS, (2_000_000_000, 2_000_000_000))
        except Exception:
            pass

    with tempfile.TemporaryDirectory() as work:
        try:
            p = subprocess.run([sys.executable, "-I", "-c", job], capture_output=True, text=True, timeout=timeout,
                               cwd=work, env={"OPENBLAS_NUM_THREADS": "1", "PATH": ""},
                               preexec_fn=limits if os.name == "posix" else None)
        except subprocess.TimeoutExpired:
            return f"KILLED: time limit {timeout}s"
    if p.returncode < 0:
        return f"KILLED: resource limit (signal {-p.returncode})"
    if p.returncode != 0:
        return f"ERROR: {p.stderr.strip().splitlines()[-1] if p.stderr.strip() else p.returncode}"
    return p.stdout.strip()

for q in ["Which city has the most P1 tickets?", "Average resolution by month?", "Which is the slowest city?"]:
    code = write_code(q)
    print(f"Q: {q}\\n   code: {code}\\n   result: {run_sandboxed(code)}\\n")

for evil in ["import os\\nresult = os.listdir('.')", "result = open('/etc/passwd').read()", "result = df.__class__.__bases__",
             "result = sum(i * i for i in range(10**12))"]:
    print(repr(evil[:40]), "->", run_sandboxed(evil, timeout=3))'''),
    ("md", "### The container version (Docker Desktop on your laptop)\nThis cell is skipped in the offline check and in "
           "Colab. It runs the same job with no network, a read-only file system and resource limits."),
    ("code", '''# ===== Option B only: VS Code / local with Docker Desktop =====
job_dir = tempfile.mkdtemp()
with open(os.path.join(job_dir, "analysis.py"), "w") as f:
    f.write("import pandas as pd\\ndf = pd.read_csv('/data/tickets.csv')\\n"
            "print(df.groupby('city')['minutes_to_resolve'].median().idxmax())\\n")
dockerfile = "FROM python:3.12-slim\nRUN pip install --no-cache-dir pandas\nUSER 1000:1000\n"
subprocess.run(["docker", "build", "-t", "smartdesk-sandbox", "-"], input=dockerfile, text=True, check=True)
cmd = ["docker", "run", "--rm", "--network", "none", "--read-only", "--memory", "256m", "--cpus", "0.5",
       "--pids-limit", "64", "-v", f"{DATA_DIR}:/data:ro", "-v", f"{job_dir}:/job:ro",
       "smartdesk-sandbox", "timeout", "10", "python", "/job/analysis.py"]
print(" ".join(cmd))
print(subprocess.run(cmd, capture_output=True, text=True).stdout)''', ["skip-offline-check"]),
    ("md", "Note: the image is built once with pandas pre-installed, because with `--network none` nothing can be "
           "downloaded at run time."),
    ("md", "## 4. NEW (v4): An MCP server on the current SDK\nIn mcp 2.x, `FastMCP` is now `MCPServer` "
           "(`from mcp.server.mcpserver import MCPServer`). We write the server to a file so it can also run over stdio."),
    ("code", '''%%writefile mcp_server.py
"""SmartDesk ticket tools as an MCP server (mcp 2.x)."""
import json, re
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("smartdesk-tickets", version="1.0",
                instructions="Read-only SmartDesk ticket tools. Ticket ids look like T-1001.")
TICKETS = {"T-1001": {"status": "open", "priority": "P2", "category": "network", "city": "Osaka"},
           "T-1002": {"status": "open", "priority": "P1", "category": "billing", "city": "Tokyo"},
           "T-1003": {"status": "closed", "priority": "P3", "category": "account", "city": "Pune"}}
AUDIT = []

@mcp.tool()
def get_ticket(ticket_id: str) -> str:
    """Look up one SmartDesk ticket by id, for example T-1001. Returns status, priority and category."""
    AUDIT.append(("get_ticket", ticket_id))
    if not re.fullmatch(r"T-\\d{4}", ticket_id):
        return json.dumps({"error": "ticket id must look like T-1234"})
    return json.dumps(TICKETS.get(ticket_id, {"error": "not found"}))

@mcp.tool()
def list_open_tickets(limit: int = 10) -> str:
    """List open ticket ids, newest first. limit is 1 to 20."""
    AUDIT.append(("list_open_tickets", limit))
    ids = [k for k, v in TICKETS.items() if v["status"] == "open"][: max(1, min(limit, 20))]
    return json.dumps(ids)

@mcp.resource("policy://sla")
def sla_policy() -> str:
    """The SmartDesk SLA policy."""
    return "P1 tickets must be resolved within 4 hours, P2 within 1 day, P3 within 3 days."

@mcp.prompt()
def apology_email(customer: str, issue: str) -> str:
    """A template for a short apology email."""
    return f"Write a short, warm apology email to {customer} about: {issue}. Offer one concrete next step."

if __name__ == "__main__":
    mcp.run()          # stdio; for remote use: mcp.run("streamable-http", stateless_http=True)'''),
    ("md", "### Connect with `mcp.Client` (in-process)\nPassing the server object connects in-process: ideal for tests "
           "and offline runs. Notebooks support top-level `await`."),
    ("code", '''import importlib, mcp_server
importlib.reload(mcp_server)
from mcp import Client

async with Client(mcp_server.mcp) as c:
    print("protocol:", c.protocol_version)
    tools = await c.list_tools()
    print("tools:", [t.name for t in tools.tools])
    print("schema:", tools.tools[0].input_schema)
    r = await c.call_tool("get_ticket", {"ticket_id": "T-1001"})
    print("get_ticket ->", r.content[0].text)
    r = await c.call_tool("list_open_tickets", {"limit": 5})
    print("list_open_tickets ->", r.content[0].text)
    bad = await c.call_tool("get_ticket", {"ticket_id": "DROP TABLE"})
    print("invalid input ->", bad.content[0].text)
    print("resources:", [str(x.uri) for x in (await c.list_resources()).resources])
    print("sla:", (await c.read_resource("policy://sla")).contents[0].text)
    p = await c.get_prompt("apology_email", {"customer": "Mei", "issue": "slow mobile data"})
    print("prompt:", p.messages[0].content.text)'''),
    ("md", "### Connect over stdio (a real separate process)"),
    ("code", '''from mcp import StdioServerParameters

params = StdioServerParameters(command=sys.executable, args=["mcp_server.py"])
async with Client(params) as c:
    r = await c.call_tool("get_ticket", {"ticket_id": "T-1002"})
    print("stdio:", c.protocol_version, "->", r.content[0].text)'''),
    ("md", "## 5. NEW (v4): Use the MCP server from an agent\nWe wrap each MCP tool as a LangChain tool and give them to "
           "a `create_agent` assistant. Offline, a small rule-based model decides the calls."),
    ("code", '''from typing import Any
from langchain.agents import create_agent
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_core.tools import StructuredTool

class OfflineTicketModel(BaseChatModel):
    """Rule-based stand-in. NOT intelligent: it lets the agent loop run without a key."""
    tool_names: list = []

    @property
    def _llm_type(self):
        return "offline-demo"

    def bind_tools(self, tools, **kwargs):
        return self.model_copy(update={"tool_names": [t.name for t in tools]})

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        user = next(m.content for m in reversed(messages) if isinstance(m, HumanMessage))
        used = [m for m in messages if isinstance(m, ToolMessage)]
        tid = re.search(r"T-\\d{4}", user)
        if tid and not used and "get_ticket" in self.tool_names:
            msg = AIMessage(content="", tool_calls=[{"name": "get_ticket", "args": {"ticket_id": tid.group(0)}, "id": "c1"}])
        elif not tid and not used and "list_open_tickets" in self.tool_names:
            msg = AIMessage(content="", tool_calls=[{"name": "list_open_tickets", "args": {"limit": 5}, "id": "c1"}])
        else:
            msg = AIMessage(content=f"[offline demo] From the ticket system: {used[-1].content if used else 'nothing found'}")
        return ChatResult(generations=[ChatGeneration(message=msg)])

def chat_model():
    if ONLINE:
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=MODEL, api_key=genai_helpers.OPENAI_API_KEY)
    return OfflineTicketModel()

def mcp_tools_for(client, listed):
    def make(t):
        async def call(**kwargs):
            r = await client.call_tool(t.name, kwargs)
            print(f"  [mcp] {t.name} {kwargs}")
            return r.content[0].text
        return StructuredTool.from_function(coroutine=call, name=t.name, description=t.description or "",
                                            args_schema=t.input_schema)
    return [make(t) for t in listed.tools]

import genai_helpers
async with Client(mcp_server.mcp) as c:
    tools = mcp_tools_for(c, await c.list_tools())
    agent = create_agent(chat_model(), tools=tools, system_prompt="You are a SmartDesk agent. Use the ticket tools.")
    for q in ["What is the status of T-1002?", "Which tickets are still open?"]:
        out = await agent.ainvoke({"messages": [{"role": "user", "content": q}]})
        print("Q:", q, "\\nA:", out["messages"][-1].content, "\\n")'''),
    ("md", "### Add the same server to OpenAI Codex\nCodex can use MCP servers too. Add a read-only server for local "
           "development in your Codex configuration (`~/.codex/config.toml`) or with the `codex mcp add` command. "
           "Check the current Codex documentation for your version.\n\n"
           "```toml\n[mcp_servers.smartdesk]\ncommand = \"python\"\nargs = [\"mcp_server.py\"]\n```\n\n"
           "Rules: only reviewed servers, read-only tools for Codex, no customer data or secrets in a dev setup."),
    ("md", "## 6. NEW (v4): MCP 2026-07-28: stateless, OAuth 2.1 and Tasks\n"
           "* **Stateless:** the client above reported protocol `2026-07-28`; each request stands alone, so a remote "
           "server can run behind a load balancer with `stateless_http=True`.\n"
           "* **OAuth 2.1:** remote servers verify a bearer token on every request (code below, not run here).\n"
           "* **Tasks:** long-running calls return a task the client polls. mcp 2.3.0 ships the `Task` types; we "
           "simulate the lifecycle with them."),
    ("code", '''# Shown, not run: a remote MCP server that checks OAuth 2.1 bearer tokens (mcp 2.x).
REMOTE_SERVER_EXAMPLE = """
from mcp.server.auth.provider import AccessToken
from mcp.server.auth.settings import AuthSettings
from mcp.server.mcpserver import MCPServer

class MyVerifier:
    async def verify_token(self, token: str) -> AccessToken | None:
        claims = check_signature_and_expiry(token)        # your identity provider's library
        if not claims:
            return None
        return AccessToken(token=token, client_id=claims["client_id"], scopes=claims["scope"].split(),
                           expires_at=claims["exp"], resource=claims["aud"])

mcp = MCPServer("smartdesk", token_verifier=MyVerifier(),
                auth=AuthSettings(issuer_url="https://login.example.com",
                                  resource_server_url="https://mcp.example.com",
                                  required_scopes=["tickets:read"], validate_token_resource=True))
mcp.run("streamable-http", stateless_http=True)
"""
print(REMOTE_SERVER_EXAMPLE)'''),
    ("code", '''import uuid, datetime as dt
import mcp_types as mt

class TaskBoard:
    """Simulated MCP task store using the SDK's Task type."""
    def __init__(self):
        self.tasks, self.results = {}, {}

    def create(self, ttl_ms=600_000):
        now = dt.datetime.now(dt.timezone.utc).isoformat()
        t = mt.Task(task_id=uuid.uuid4().hex[:4], status="working", created_at=now, last_updated_at=now,
                    ttl=ttl_ms, poll_interval=1000)
        self.tasks[t.task_id] = t
        return t

    def update(self, task_id, status, result=None):
        t = self.tasks[task_id].model_copy(update={"status": status,
                                                   "last_updated_at": dt.datetime.now(dt.timezone.utc).isoformat()})
        self.tasks[task_id] = t
        if result is not None:
            self.results[task_id] = result

board = TaskBoard()
task = board.create()
history = [task.status]
for step in range(3):                       # the slow export makes progress
    if step == 2:
        board.update(task.task_id, "completed", result="120 tickets exported to tickets_nov.csv")
    history.append(board.tasks[task.task_id].status)
print(f"task {task.task_id}: {' -> '.join(history)}")
print("result:", board.results[task.task_id])

other = board.create()
board.update(other.task_id, "cancelled")
print(f"task {other.task_id}:", board.tasks[other.task_id].status, "| allowed statuses:", list(mt.TaskStatus.__args__))'''),
    ("md", "## 7. NEW (v4): A2A v1.0 and signed Agent Cards\nTwo small FastAPI agents. The refund agent publishes a "
           "**signed** Agent Card; the support agent verifies the signature before delegating a task. This is a "
           "simplified form: follow the A2A v1.0 specification for the exact card fields and signature format."),
    ("code", '''import base64, logging
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpx2").setLevel(logging.WARNING)
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.exceptions import InvalidSignature
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

def canonical(card):
    body = {k: v for k, v in card.items() if k != "signatures"}
    return json.dumps(body, sort_keys=True, separators=(",", ":")).encode()

key = Ed25519PrivateKey.generate()          # the refund team's signing key
REGISTRY = {"refund-team-key-1": key.public_key()}   # approved agents and their public keys

CARD = {"name": "Refund Agent", "description": "Calculates late-delivery credits.", "version": "1.0",
        "url": "http://refund-agent.local/a2a", "skills": [{"id": "calculate_credit", "description": "Credit for minutes of outage"}]}
CARD["signatures"] = [{"kid": "refund-team-key-1", "alg": "EdDSA",
                       "signature": base64.urlsafe_b64encode(key.sign(canonical(CARD))).decode()}]

def verify(card):
    try:
        s = card["signatures"][0]
        REGISTRY[s["kid"]].verify(base64.urlsafe_b64decode(s["signature"]), canonical(card))
        return True
    except (KeyError, IndexError, InvalidSignature):
        return False

refund_agent = FastAPI(title="Refund Agent")

class TaskRequest(BaseModel):
    skill: str
    message: dict

@refund_agent.get("/.well-known/agent-card.json")
def agent_card():
    return CARD

@refund_agent.post("/tasks")
def create_task(req: TaskRequest):
    task_id = uuid.uuid4().hex[:8]
    if req.skill != "calculate_credit":
        return {"id": task_id, "status": "failed", "error": f"unknown skill {req.skill}"}
    credit = round(min(req.message["outage_minutes"] / 60 * 50, 2000), 2)    # 50 per hour, max 2,000
    return {"id": task_id, "status": "completed", "artifacts": [{"type": "data", "data": {"credit": credit}}]}

remote = TestClient(refund_agent)

def support_agent(outage_minutes, card=None):
    card = card or remote.get("/.well-known/agent-card.json").json()
    if not verify(card):
        return "Card verification failed: refusing to delegate."
    print("verified:", card["name"], "skills:", [s["id"] for s in card["skills"]])
    task = remote.post("/tasks", json={"skill": "calculate_credit", "message": {"outage_minutes": outage_minutes}}).json()
    print("task:", task["id"], task["status"])
    return f"Sorry for the outage. A credit of {task['artifacts'][0]['data']['credit']} has been added."

print(support_agent(180))
forged = json.loads(json.dumps(CARD))
forged["url"] = "http://attacker.example/a2a"
print(support_agent(180, card=forged))'''),
    ("md", "## 8. Agentic handoff"),
    ("code", '''from typing import Literal

class Handoff(BaseModel):
    from_agent: str
    to: str
    summary: str
    facts: dict
    steps_tried: list[str]
    reason: str
    suggested_next_step: str
    urgency: Literal["low", "medium", "high"]

h = Handoff(
    from_agent="smartdesk-bot", to="human-billing-team",
    summary="Customer Mei had no mobile data for 9 hours in Osaka and wants a credit; she is upset.",
    facts={"ticket_id": "T-1001", "outage_minutes": 540, "calculated_credit": 450.0},
    steps_tried=["get_ticket -> open, P2, network", "Refund Agent calculate_credit -> 450.0"],
    reason="Customer asked for a larger credit than the bot may approve",
    suggested_next_step="Review the outage report and approve a credit up to 1,000",
    urgency="high",
)
print(h.model_dump_json(indent=2))'''),
    ("md", "### TODO 1 (SmartDesk step 24): add an `update_status(ticket_id, status)` tool that is write-only for "
           "agents with an approval, and a `search_faq(query)` tool. Call both from the agent.\n"
           "### TODO 2: add a row limit (refuse data over 100,000 rows) and block `while` loops in `check_code`."),
    ("code", "# TODO: write your code here"),
    ("md", "## 9. Check yourself\n1. Which protocol version did the client report?\n"
           "2. What stopped the never-ending loop in the sandbox?\n3. Why did the forged card fail verification?\n"
           "4. Where would you set OAuth scopes for a remote MCP server?"),
])
