"""Day 26 spec. GenAI 7: LLM Orchestration, Tool Calling and LangGraph.
Source: technical parts of archive/v1-40-day/Day24 (LangChain) and Day25 (tool calling, LangGraph).
FDE skills parts (influence, negotiation, conflict, systems thinking) moved to FDE-Mindset-Source.
NEW (v4) topics are marked. Library versions checked: langchain 1.4.7, langgraph 1.2.16, openai-agents 0.24.0.
"""
DAY = 26
FOLDER = "Day26-LLM-Orchestration-Tools-and-LangGraph"
SLUG = "LLM_Orchestration_Tools_and_LangGraph"
TITLE = "LLM Orchestration, Tool Calling and LangGraph"
SUBTITLE = "Chains, LangChain v1 agents and middleware, safe tool calling, and durable LangGraph workflows"
DATE = "Tue 01 Dec 2026"
TRACK = "GenAI"
NEXT = "See you tomorrow for Day 27: agentic AI, agentic RAG and memory, plus GenAI assessment 2."

LC_OFFLINE = '''%%writefile lc_offline.py
"""Chat model for the LangChain and LangGraph demos.
ONLINE : get_chat_model() returns ChatOpenAI with the program model (LLM_MODEL).
OFFLINE: a small rule-based chat model. It is NOT intelligent. It makes tool calls from simple rules,
         so the agent loop, middleware, checkpoints and interrupts really run without a key.
"""
import itertools, json, re
from typing import Any
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.outputs import ChatGeneration, ChatResult
import genai_helpers

_ids = itertools.count(1)

def _call(name, args):
    return AIMessage(content="", tool_calls=[{"name": name, "args": args, "id": f"call_{next(_ids)}"}])

def support_planner(messages, tool_names):
    """Decide the next tool call for the support demos, or None to answer."""
    user = next((m.content for m in reversed(messages) if isinstance(m, HumanMessage)), "")
    low = user.lower()
    used = [m.name for m in messages if isinstance(m, ToolMessage)]
    results = [json.loads(m.content) for m in messages
               if isinstance(m, ToolMessage) and str(m.content).strip().startswith("{")]
    last = results[-1] if results else {}
    oid = re.search(r"ORD-\\d{4}", user)
    if oid and "get_order_status" in tool_names and "get_order_status" not in used:
        return _call("get_order_status", {"order_id": oid.group(0)})
    if "refund" in low and "amount" in last and "calculate_refund" in tool_names and "calculate_refund" not in used:
        return _call("calculate_refund", {"amount": last["amount"], "days_late": last.get("days_late", 0)})
    if ("issue" in low or "pay" in low) and "refund" in last and oid and "issue_refund" in tool_names \\
            and "issue_refund" not in used:
        return _call("issue_refund", {"order_id": oid.group(0), "amount": last["refund"]})
    if "policy" in low and "search_policy" in tool_names and "search_policy" not in used:
        return _call("search_policy", {"query": user})
    return None

class OfflineChatModel(BaseChatModel):
    tool_names: list = []
    planner: Any = None

    @property
    def _llm_type(self):
        return "offline-demo"

    def bind_tools(self, tools, **kwargs):
        names = []
        for t in tools:
            if hasattr(t, "name"):
                names.append(t.name)
            elif isinstance(t, dict):
                names.append(t.get("function", t).get("name"))
            else:
                names.append(getattr(t, "__name__", str(t)))
        return self.model_copy(update={"tool_names": names})

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        msg = (self.planner or support_planner)(messages, self.tool_names) if self.tool_names else None
        if msg is None:
            facts = [str(m.content) for m in messages if isinstance(m, ToolMessage)]
            human = next((m.content for m in reversed(messages) if isinstance(m, HumanMessage)), "")
            system = next((m.content for m in messages if isinstance(m, SystemMessage)), "")
            text = f"[offline demo] Based on the tools: {facts[-1]}" if facts else genai_helpers.offline_llm(human, system)
            msg = AIMessage(content=text)
        return ChatResult(generations=[ChatGeneration(message=msg)])

def get_chat_model(**kwargs):
    if genai_helpers.ONLINE:
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=genai_helpers.MODEL, api_key=genai_helpers.OPENAI_API_KEY, **kwargs)
    return OfflineChatModel(**kwargs)

print("Chat model:", "ChatOpenAI" if genai_helpers.ONLINE else "OfflineChatModel (offline demo)")
'''

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz and presentations", "15 questions on Day 25, then participant PPT presentations (20 min)"),
        ("Orchestration", "Chains, LLM as judge, LangChain v1 create_agent. NEW (v4)"),
        ("Tool calling", "Schemas, validation, tool token cost. NEW (v4)"),
        ("Frameworks compared", "Direct API, LangChain, OpenAI Agents SDK. NEW (v4)"),
        ("LangGraph", "State, branches, durable execution, interrupts. NEW (v4)"),
        ("1:1 feedback", "Personal progress conversations at the end of the day"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Orchestrate", "Build chains and a LangChain v1 agent with middleware."),
        ("Call tools safely", "Describe, validate, allowlist and cost your tools."),
        ("Choose a framework", "Compare direct API, LangChain and the OpenAI Agents SDK."),
        ("Build durable graphs", "Use LangGraph state, checkpoints and human approval interrupts."),
    ]),
    dict(type="section", title="Why orchestration?", sub="From single prompts to composable pipelines"),
    dict(type="cards", title="What an orchestration framework gives you", items=[
        ("Reusable parts", "Prompts, models, parsers, tools and retrievers as building blocks."),
        ("Composition", "Pipe parts together: prompt | model | parser."),
        ("Swap models", "Change the model without rewriting the app."),
        ("Batteries", "Retries, batching, streaming, tracing."),
    ], note="Start with plain code. Reach for a framework when the same plumbing keeps repeating."),
    dict(type="bullets_code", title="Chaining with LCEL", bullets=[
        "ChatPromptTemplate fills variables",
        "The | operator pipes components",
        "A parser turns output into a string or JSON",
        "invoke one input, batch many",
    ], code='''from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "You summarise for {audience}."),
    ("user", "{text}")])
chain = prompt | model | StrOutputParser()

chain.batch([{"audience": a, "text": notes}
             for a in ["CIO", "engineer", "end user"]])'''),
    dict(type="compare", title="LLM as judge", left=dict(title="What it is", bullets=[
        "A second model call scores the first answer",
        "Rubric: relevant, grounded, complete, tone",
        "Returns a score and a reason as JSON",
    ]), right=dict(title="Use it carefully", bullets=[
        "Judges have biases (length, position)",
        "Calibrate against human labels (Day 31)",
        "Use a cheap model; log every score",
        "Never the only gate for risky actions",
    ])),
    dict(type="bullets_code", title="LangChain v1: create_agent", new=True, bullets=[
        "One function builds a tool-calling agent",
        "Runs on LangGraph underneath",
        "Replaces AgentExecutor and initialize_agent",
        "Add a checkpointer for memory and resume",
    ], code='''from langchain.agents import create_agent

agent = create_agent(
    model,                       # ChatOpenAI or offline
    tools=[get_order_status, calculate_refund],
    system_prompt="You are a support assistant.",
)
out = agent.invoke({"messages": [
    {"role": "user",
     "content": "ORD-1042 was late. Refund?"}]})
print(out["messages"][-1].content)'''),
    dict(type="table", title="Middleware: hooks around the agent loop", new=True, header=["Hook or class", "Use it to"], rows=[
        ["@before_model / @after_model", "Log, trim context, check state before and after each model call"],
        ["@wrap_tool_call", "Audit, validate or retry every tool call"],
        ["ModelCallLimitMiddleware", "Stop runaway loops (cost control)"],
        ["HumanInTheLoopMiddleware", "Pause before risky tools for approval"],
        ["SummarizationMiddleware", "Compact long conversations"],
        ["PIIMiddleware", "Detect and redact personal data"],
    ], note="Checked against langchain 1.4.7. Middleware keeps cross-cutting rules out of your prompts."),
    dict(type="bullets", title="Reading older code", bullets=[
        "You will meet LLMChain, AgentExecutor and initialize_agent in older repos and blog posts",
        "They are legacy in LangChain v1: port them to LCEL chains or create_agent",
        "Imports moved: prompts and parsers live in langchain_core; agents in langchain.agents",
        "When unsure, ask Codex to explain the old code, then rewrite it in small tested steps",
    ]),

    dict(type="section", title="Tool calling", sub="The model asks; your code acts"),
    dict(type="flow", title="The tool calling loop", items=[
        ("Describe", "Send tools as JSON schemas"),
        ("Decide", "Model returns a tool call with arguments"),
        ("Validate + run", "Your code checks args and executes"),
        ("Return", "Result goes back as a tool message"),
        ("Answer", "Model replies, or calls another tool"),
    ], note="The model never runs code itself. Your application stays in control."),
    dict(type="bullets_code", title="Describing a tool", bullets=[
        "name and description guide the model",
        "parameters is a JSON schema",
        "Clear descriptions improve tool choice",
        "Required fields prevent half calls",
    ], code='''tools = [{
  "type": "function",
  "function": {
    "name": "get_order_status",
    "description": "Look up an order's status "
                   "by its id, e.g. ORD-1042",
    "parameters": {
      "type": "object",
      "properties": {
        "order_id": {"type": "string"}},
      "required": ["order_id"]}}}]'''),
    dict(type="table", title="Tool safety rules", header=["Rule", "Why"], rows=[
        ["Allowlist tools", "Only registered functions can ever run"],
        ["Validate arguments", "Pydantic models; reject bad ids and amounts"],
        ["Least privilege", "Read-only tools by default; separate write tools"],
        ["Confirm risky actions", "Refunds, deletes and emails need a human yes"],
        ["Limit loops", "Max steps and timeouts stop runaway agents"],
    ]),
    dict(type="cards", title="Tool design for agents", new=True, items=[
        ("Few, clear tools", "One job per tool. Verb-noun names: get_order_status."),
        ("Good descriptions", "When to use it, an example value, what it returns."),
        ("Small results", "Return only the fields the model needs, not whole records."),
        ("Errors as text", "Explain what went wrong so the model can recover."),
    ]),
    dict(type="cards", title="Tool token cost", new=True, items=[
        ("Schemas are input tokens", "Every tool definition is sent on every model call."),
        ("Results are input tokens", "Large tool outputs fill the context on the next call."),
        ("Many tools, many tokens", "20 verbose tools can cost more than the question itself."),
        ("Tool search", "Load only the relevant tools per request (tool search, tool selector middleware)."),
    ], note="Measure it: count tokens of your tool list in today's notebook. Prices are placeholders."),
    dict(type="table", title="Direct API, LangChain or OpenAI Agents SDK?", new=True,
         header=["Option", "Strengths", "Watch out for"], rows=[
        ["Direct OpenAI API", "Full control, fewest layers, easy to debug", "You write loops, retries, tracing"],
        ["LangChain v1 + LangGraph", "Middleware, graphs, checkpoints, many integrations", "Learning curve; pin versions"],
        ["OpenAI Agents SDK", "Agents, tools, handoffs, guardrails, tracing in few lines", "Opinionated loop; best with OpenAI models"],
    ], note="Same tools, three wrappers. Pick by control needed, team skills and what the customer already runs."),
    dict(type="bullets_code", title="The same assistant in the OpenAI Agents SDK", new=True, bullets=[
        "@function_tool builds the schema from type hints",
        "handoffs pass work to a specialist agent",
        "Runner runs the loop and records a trace",
        "Day 27 goes deeper",
    ], code='''from agents import Agent, Runner, function_tool

@function_tool
def order_status(order_id: str) -> str:
    """Look up an order, e.g. ORD-1042."""
    return get_order_status(order_id)

assistant = Agent(name="Support",
    instructions="Answer order questions.",
    tools=[order_status])
result = await Runner.run(assistant, "Where is ORD-2077?")
print(result.final_output)'''),

    dict(type="section", title="LangGraph", sub="Workflows as graphs: state, nodes, edges"),
    dict(type="cards", title="LangGraph building blocks", greet="Nagare (流れ): Flow", items=[
        ("State", "A typed dictionary passed between steps."),
        ("Nodes", "Functions that read state and return updates."),
        ("Edges", "Fixed paths from one node to the next."),
        ("Conditional edges", "Choose the next node from the state."),
        ("Cycles", "Loops for retries and agent behaviour."),
        ("Checkpoints", "Save state to pause, resume or ask a human."),
    ]),
    dict(type="bullets_code", title="A graph with a retry loop", bullets=[
        "add_node registers steps",
        "Edges connect them",
        "A router picks the next step",
        "compile() makes it runnable",
    ], code='''from langgraph.graph import StateGraph, START, END

g = StateGraph(State)
g.add_node("retrieve", retrieve)
g.add_node("answer", answer)
g.add_node("check", check)
g.add_edge(START, "retrieve")
g.add_edge("retrieve", "answer")
g.add_edge("answer", "check")
g.add_conditional_edges("check", route,
    {"retry": "retrieve", "done": END})
app = g.compile()'''),
    dict(type="cards", title="Durable execution", new=True, items=[
        ("Checkpointer", "Saves state after every step, per thread_id."),
        ("Resume after failure", "Invoke again on the same thread; finished steps are not rerun."),
        ("Time travel", "get_state_history lists every checkpoint for debugging."),
        ("In production", "Use a database checkpointer (for example Postgres), not memory."),
    ]),
    dict(type="bullets_code", title="Human-in-the-loop interrupts", new=True, bullets=[
        "interrupt() pauses the graph and saves state",
        "The caller sees the pending action",
        "Command(resume=...) continues with the decision",
        "Default to no: reject unless approved",
    ], code='''from langgraph.types import interrupt, Command

def approve_refund(state):
    ok = interrupt({"action": "issue_refund",
                    "amount": state["refund"]})
    return {"approved": ok == "yes"}

app = g.compile(checkpointer=InMemorySaver())
cfg = {"configurable": {"thread_id": "t-42"}}
app.invoke({"question": q}, cfg)      # pauses
app.invoke(Command(resume="yes"), cfg)''', note="Pausing costs nothing: state waits in the checkpointer."),
    dict(type="cards", title="SmartDesk step 22: support assistant", items=[
        ("Tools", "get_ticket, get_customer_plan, search_faq, issue_credit (risky)."),
        ("Graph", "classify, then tools, answer, check; retry once; else human."),
        ("Approval", "issue_credit pauses for a human yes. Default no."),
        ("Build with Codex", "Use Day26_App_Build_Prompts.md. Review every diff."),
    ]),
    dict(type="callout", title="1:1 feedback", text="Each of you meets your mentor for 15 minutes: assessment results, "
         "project progress and one focus for the next two weeks.",
         sub="Come with one thing you are proud of and one thing you want help with.",
         greet="Arigatou (ありがとう): Thank you"),
    dict(type="cards", title="Key takeaways", items=[
        ("Orchestration", "LCEL chains for pipelines; create_agent plus middleware for agents."),
        ("Tools", "Model proposes, code validates and executes. Tools cost tokens."),
        ("Frameworks", "Direct API, LangChain or Agents SDK: same ideas, different control."),
        ("LangGraph", "State, branches, checkpoints and interrupts make agents durable."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics, then GenAI assessment 2.", items=[
        ("Hotel lab", "Follow Day26_Hotel_Lab.md: add a tool and an approval interrupt."),
        ("Workbook", "Complete the Day 26 workbook."),
        ("Pre-read", "Skim the Day 27 pre-read on agents and memory."),
    ]),
]

PREREAD = dict(title="Tools, Flows and Loops", lede="A light read before Day 26. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "So far you have asked a model one question at a time. Real assistants need several steps: look something "
        "up, calculate, check, and sometimes ask a person. Today you learn how to connect those steps safely."]),
    dict(h="1. Recipes for AI", paras=[
        "A recipe lists steps in order: chop, fry, season, serve. A **chain** does the same with AI: fill a prompt, "
        "call the model, tidy the answer. Frameworks such as LangChain give you ready-made steps that snap together."]),
    dict(h="2. Letting the model use tools", paras=[
        "A support agent on the phone looks up your order in a system before answering. A model can do the same. We "
        "describe our functions as **tools**; the model asks for one, and our code decides whether to run it. The model "
        "never presses the button itself."]),
    dict(h="3. Every tool costs words", new=True, paras=[
        "Each tool's description is sent to the model on every call, and each tool result is read by the model. "
        "Many long tool descriptions mean many **tokens**, so more cost. Good tools are few, clear and return only "
        "what is needed."]),
    dict(h="4. Flowcharts that remember", paras=[
        "Some work is a straight line; some has branches and loops: \"if the answer is weak, search again\". A "
        "**graph** describes those branches. **LangGraph** runs such graphs and keeps a shared notebook of facts "
        "called **state**."]),
    dict(h="5. Pause, ask, continue", new=True, paras=[
        "Before refunding money, a careful assistant stops and asks a manager. A graph can **pause** at that step, "
        "save everything, and continue hours later with the manager's answer. Saving progress like this is called "
        "**durable execution**."],
        table=[["Everyday idea", "Technical term"], ["Recipe", "Chain"], ["Phone lookup", "Tool call"],
               ["Flowchart", "Graph"], ["Shared notebook", "State"], ["Save game", "Checkpoint"],
               ["Ask the manager", "Human-in-the-loop interrupt"]],
        box="**Key idea:** the model suggests; your code decides. Risky actions always need a human yes."),
    dict(h="6. Think about these before class", bullets=[
        "Which actions in a telecom support team should never happen without a person approving them?",
        "If an assistant had 30 tools, how could it pick the right one quickly and cheaply?",
        "What should happen if the system crashes halfway through a refund?"],
        after=["Nagare (流れ): flow"]),
])

POSTREAD = dict(title="Orchestration, Tools and LangGraph: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Chains (LCEL)", "prompt | model | parser; invoke one input, batch many."],
        ["LLM as judge", "A second call scores an answer with a rubric. Calibrate before you trust it."],
        ["create_agent (NEW v4)", "LangChain v1's one-call tool-calling agent, built on LangGraph."],
        ["Middleware (NEW v4)", "Hooks before and after model and tool calls: limits, approvals, PII, logging."],
        ["Tool calling", "Model proposes; code validates (Pydantic), allowlists and executes."],
        ["Tool token cost (NEW v4)", "Schemas and results are input tokens on every call. Keep tools few and lean."],
        ["Agents SDK (NEW v4)", "Agent, function_tool, Runner, handoffs, guardrails, tracing."],
        ["LangGraph", "State, nodes, edges, conditional edges, cycles."],
        ["Durable execution (NEW v4)", "Checkpointer per thread_id; resume after failure; interrupt() and Command(resume)."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Tool search", paras=[
        "When an agent has dozens of tools, send only the relevant ones. LangChain offers a tool selector middleware "
        "and provider tool search. Fewer tools per call means fewer tokens and better choices."]),
    dict(sub="2. Parallel tool calls", paras=[
        "Models can request several independent tool calls in one turn, for example two order lookups. Run them in "
        "parallel, but keep risky tools sequential and approved."]),
    dict(sub="3. Production checkpointers", paras=[
        "InMemorySaver is for demos. In production use a database-backed checkpointer so a restart does not lose "
        "paused approvals. Clean up old threads on a schedule."]),
    dict(sub="4. Streaming", paras=[
        "Agents can stream tokens and intermediate steps to the UI so users see progress. Stream the path trace as "
        "well as the answer."]),
    dict(sub="5. Version everything", paras=[
        "Pin langchain, langgraph and openai-agents versions in requirements. Agent frameworks change quickly; "
        "upgrade on purpose with tests (Day 33, AgentOps)."]),
    dict(h="Part C: Check yourself", bullets=[
        "Why does the model never execute a tool itself?",
        "Name three middleware hooks and one use for each.",
        "How do tool definitions affect the token bill?",
        "What happens when you invoke a paused graph with Command(resume=...)?",
        "When would you choose the direct API over a framework?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add a search_policy tool to the create_agent assistant and measure the extra schema tokens.",
        "Make the refund approval interrupt reject by default and log every decision.",
        "Print the Mermaid diagram of your graph and paste it into your SmartDesk README."],
        after=["**Coming up on Day 27:** agentic AI, corrective RAG, multi-agent systems, persistent memory and GenAI "
               "assessment 2.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Eight problems. Every notebook cell runs offline with a rule-based stand-in model; add an "
                    "OPENAI_API_KEY to see real tool choices. Offline results show how the code works, not real model "
                    "quality.", problems=[
    dict(title="Summary Chain for Three Audiences", level="Warm-up", concepts="ChatPromptTemplate, LCEL, batch",
         text="Build a chain that summarises a support incident for a given audience (CIO, engineer, end user) in "
              "3 bullet points, and run it on one text for all three audiences with batch().",
         sample="CIO: cost and risk focus\nEngineer: technical detail\nEnd user: what changes for me",
         hints=["prompt | model | StrOutputParser()"]),
    dict(title="Write Tool Schemas", level="Easy", concepts="JSON schema, descriptions",
         text="Write schemas for get_order_status(order_id), calculate_refund(amount, days_late) and "
              "create_ticket(summary, priority). Include descriptions with example values.",
         sample='{"name": "calculate_refund", "parameters": {"properties": {"amount": {"type": "number"}, ...}, "required": [...]}}',
         hints=["Use enum for priority: low, medium, high."]),
    dict(title="Validate Arguments", level="Easy", concepts="Pydantic, allowlist",
         text="Write run_tool(name, args_json) that rejects unknown tools and invalid arguments (bad order id format, "
              "negative amount) with clear error messages returned to the model.",
         sample='run_tool("delete_db", "{}") -> error: unknown tool\nrun_tool("calculate_refund", \'{"amount": -5}\') -> error: amount must be > 0',
         hints=["Return errors as text so the model can recover."]),
    dict(title="Agent with Middleware", level="Medium", concepts="create_agent, middleware", new=True,
         text="Build a create_agent assistant with get_order_status and calculate_refund. Add a @before_model logger, a "
              "@wrap_tool_call audit log and a ModelCallLimitMiddleware. Run it on two questions.",
         sample="[log] model call 1 (1 message)\n[audit] get_order_status {'order_id': 'ORD-1042'} -> ok\n"
                "[log] model call 2 (3 messages)\nFINAL: refund of 720",
         hints=["The handler in wrap_tool_call runs the tool; log before and after it."]),
    dict(title="Tool Token Budget", level="Medium", concepts="tool token cost, tool design", new=True,
         text="Count the tokens of your tool list. Compare 3 lean tools with 12 verbose tools, and estimate the cost "
              "per 1,000 conversations of 4 model calls each. Use the notebook's placeholder prices.",
         sample="lean (2 to 3 tools): about 150 tokens per call\nverbose (12 tools) : about 2,450 tokens per call\n"
                "extra per 1,000 conversations (4 calls each): about 9.2 (placeholder units)",
         hints=["Tool definitions are sent on every model call.", "Label prices as placeholders."]),
    dict(title="Same Assistant, Three Ways", level="Medium", concepts="direct API, LangChain, Agents SDK", new=True,
         text="Implement the order-status question with the direct API loop, create_agent and the OpenAI Agents SDK. "
              "Fill a table: lines of code, where validation lives, how you would test it, how you see a trace.",
         sample="| option     | lines | validation    | trace          |\n| direct API | 45    | run_tool      | your own logs  |\n"
                "| LangChain  | 20    | tool + middle | LangSmith/logs |\n| Agents SDK | 15    | function_tool | built-in trace |",
         hints=["The Agents SDK run needs a key; describe the offline result from the notebook."]),
    dict(title="Support Graph with Retry", level="Challenging", concepts="LangGraph, conditional edges",
         text="Build a graph: classify -> (order | policy | other) -> answer -> check. If check fails, retry once with a "
              "rewritten question, then hand off to a human. Print the Mermaid diagram.",
         sample="classify: order -> lookup -> answer -> check: pass\n"
                "classify: policy -> retrieve -> answer -> check: fail -> retry -> pass",
         hints=["Keep attempts in state to stop loops.", "app.get_graph().draw_mermaid()"]),
    dict(title="Durable Approval", level="Stretch", concepts="checkpoints, interrupt, Command(resume)", new=True,
         text="Add an approve_refund node that calls interrupt(). Run until it pauses, list the checkpoints, then "
              "resume once with 'no' and once (on a new thread) with 'yes'. Log every decision.",
         sample="paused at: approve_refund {'amount': 720.0}\ncheckpoints: 5\nthread A resume 'no'  -> refund rejected\n"
                "thread B resume 'yes' -> refund issued",
         hints=["Use InMemorySaver and a thread_id per conversation.", "Default to no."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "In LCEL, the ________ operator pipes the output of one component into the next.",
        "To run a chain on many inputs at once, use ________.",
        "In LangChain v1, the function that builds a tool-calling agent is ________.",
        "Code that runs before and after every model or tool call is called ________.",
        "In tool calling, the ________ never executes the tool itself.",
        "Tool parameters are described to the model as a JSON ________.",
        "Tool definitions are sent as ________ tokens on every model call.",
        "In LangGraph, the shared data passed between nodes is called ________.",
        "A ________ saves graph state after every step so it can resume.",
        "To continue a paused graph, invoke it with Command(________=...).",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain the tool calling loop in five steps, and say where validation happens.",
        "Give two uses of middleware in a support assistant and why they belong outside the prompt.",
        "Compare the direct OpenAI API, LangChain and the OpenAI Agents SDK for a customer that needs full audit logs.",
        "What is durable execution, and why does it matter for a refund approval that may wait hours?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "REGISTRY = {'get_order_status': None}\nname = 'delete_db'\nprint('ok' if name in REGISTRY else 'error: unknown tool')",
        "attempts, path = 0, []\nwhile True:\n    attempts += 1\n    path.append('try')\n    if attempts >= 2:\n        path.append('human'); break\nprint(path)",
        "tools_tokens, calls, convs = 400, 4, 1000\nprint(tools_tokens * calls * convs)",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a ChatPromptTemplate | model | StrOutputParser chain that summarises a ticket for an audience."),
        dict(q="Write a @wrap_tool_call middleware that logs the tool name, arguments and result."),
        dict(q="Write a Pydantic model RefundArgs with amount > 0 and days_late >= 0."),
        dict(q="Write a LangGraph node that calls interrupt() before issuing a refund and returns approved True or False."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="Chains, LangChain v1 agents and middleware, safe tool calling, the Agents SDK and durable LangGraph workflows",
                sign_off="Ganbatte (頑張って): *Do your best*", cells=[
    ("md", "## 1. Install"),
    ("code", '''# ===== Option A: Google Colab (active) =====
# Add your key once: click the key icon (Secrets) in the left sidebar, name it OPENAI_API_KEY, and allow notebook access.
!pip install -q openai tiktoken scikit-learn numpy pandas langchain langchain-core langchain-openai langgraph openai-agents nest_asyncio

# ===== Option B: VS Code / local =====
# pip install openai tiktoken scikit-learn numpy pandas langchain langchain-core langchain-openai langgraph openai-agents nest_asyncio
# Create a .env file (git-ignored) or set the variable in your terminal:  OPENAI_API_KEY=...
# No key? Everything still runs in OFFLINE demo mode with a rule-based stand-in model.
print("Setup done")'''),
    ("helpers",),
    ("md", "### A chat model for LangChain and LangGraph\nOnline you get `ChatOpenAI`. Offline you get a small rule-based "
           "model so the agent loop, middleware, checkpoints and interrupts really run."),
    ("code", LC_OFFLINE),
    ("code", '''import importlib, lc_offline
importlib.reload(lc_offline)
from lc_offline import get_chat_model
model = get_chat_model()'''),
    ("md", "## 2. Chaining with LCEL\nOne chain, three audiences, run with `batch()`."),
    ("code", '''from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

incident = ("The billing service was down for 40 minutes on Monday. 1,200 customers saw a payment error. "
            "A database connection limit was reached; we raised the limit and added an alert.")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You summarise incidents for {audience} in 3 short bullet points."),
    ("user", "{text}")])
chain = prompt | model | StrOutputParser()
for audience, out in zip(["a CIO", "an engineer", "an end user"],
                         chain.batch([{"audience": a, "text": incident} for a in ["a CIO", "an engineer", "an end user"]])):
    print(f"{audience}: {out[:120]}")'''),
    ("md", "## 3. LLM as judge\nA second call scores an answer against a rubric. Offline, a simple heuristic stands in."),
    ("code", '''import json, re

def judge(question, answer, context):
    if ONLINE:
        r = llm(f"Score the answer from 1 to 5 for relevance and groundedness in the context. "
                f"Reply as JSON with keys score and reason.\\nContext: {context}\\nQuestion: {question}\\nAnswer: {answer}",
                temperature=0)
        try:
            return json.loads(r[r.index("{"): r.rindex("}") + 1])
        except Exception:
            return {"score": None, "reason": "could not parse judge output"}
    words = lambda t: set(re.findall(r"[a-z0-9]+", t.lower()))
    overlap = len(words(answer) & words(context)) / max(1, len(words(answer)))
    return {"score": round(1 + 4 * overlap), "reason": f"offline overlap with context = {overlap:.2f}"}

ctx = "Late deliveries get 5% of the order value per day late, up to 50%."
for ans in ["You get 5% per day late, up to 50%.", "You get a free phone."]:
    print(ans, "->", judge("What refund for late delivery?", ans, ctx))'''),
    ("md", "## 4. Tools: schemas, validation and an allowlist"),
    ("code", '''from pydantic import BaseModel, Field, ValidationError

ORDERS = {"ORD-1042": {"status": "delivered", "amount": 4800, "days_late": 3},
          "ORD-2077": {"status": "in transit", "amount": 1200, "days_late": 0}}

class OrderArgs(BaseModel):
    order_id: str = Field(pattern=r"^ORD-\\d{4}$")

class RefundArgs(BaseModel):
    amount: float = Field(gt=0)
    days_late: int = Field(ge=0)

def get_order_status_fn(order_id):
    return json.dumps(ORDERS.get(order_id, {"error": "order not found"}))

def calculate_refund_fn(amount, days_late):
    return json.dumps({"refund": round(amount * min(0.05 * days_late, 0.5), 2)})   # 5% per day late, max 50%

REGISTRY = {"get_order_status": (get_order_status_fn, OrderArgs), "calculate_refund": (calculate_refund_fn, RefundArgs)}
TOOLS = [
    {"type": "function", "function": {"name": "get_order_status",
        "description": "Look up an order by id, for example ORD-1042. Returns status, amount and days late.",
        "parameters": {"type": "object", "properties": {"order_id": {"type": "string"}}, "required": ["order_id"]}}},
    {"type": "function", "function": {"name": "calculate_refund",
        "description": "Calculate a late delivery refund from the order amount and days late.",
        "parameters": {"type": "object", "properties": {"amount": {"type": "number"}, "days_late": {"type": "integer"}},
                       "required": ["amount", "days_late"]}}},
]

def run_tool(name, args_json):
    if name not in REGISTRY:
        return json.dumps({"error": f"unknown tool {name}"})
    fn, schema = REGISTRY[name]
    try:
        args = schema(**json.loads(args_json))
    except ValidationError as e:
        return json.dumps({"error": f"invalid arguments: {e.errors()[0]['msg']}"})
    except json.JSONDecodeError as e:
        return json.dumps({"error": f"invalid JSON: {e}"})
    return fn(**args.model_dump())

print(run_tool("delete_database", "{}"))
print(run_tool("get_order_status", '{"order_id": "1042"}'))
print(run_tool("calculate_refund", '{"amount": 4800, "days_late": 3}'))'''),
    ("md", "## 5. The tool calling loop with the direct OpenAI API"),
    ("code", '''import genai_helpers

def offline_tool_model(messages):
    # Stand-in for a model that supports tool calling: decides the next step from what it has seen so far.
    user = messages[0]["content"]
    results = [json.loads(m["content"]) for m in messages if m["role"] == "tool"]
    oid = re.search(r"ORD-\\d{4}", user)
    if not results and oid:
        return {"tool": "get_order_status", "args": json.dumps({"order_id": oid.group(0)})}
    if len(results) == 1 and "amount" in results[0]:
        return {"tool": "calculate_refund", "args": json.dumps({"amount": results[0]["amount"], "days_late": results[0]["days_late"]})}
    if results and "refund" in results[-1]:
        return {"answer": f"Your refund is {results[-1]['refund']} INR for the late delivery."}
    return {"answer": "I could not find that order. Please check the order id."}

def ask_with_tools(question, max_steps=5):
    messages = [{"role": "user", "content": question}]
    for step in range(max_steps):
        if ONLINE:
            r = genai_helpers.client.chat.completions.create(model=MODEL, messages=messages, tools=TOOLS)
            m = r.choices[0].message
            if not m.tool_calls:
                return m.content
            messages.append(m)
            for call in m.tool_calls:
                out = run_tool(call.function.name, call.function.arguments)
                print(f"step {step + 1}: {call.function.name}({call.function.arguments}) -> {out}")
                messages.append({"role": "tool", "tool_call_id": call.id, "content": out})
        else:
            d = offline_tool_model(messages)
            if "answer" in d:
                return d["answer"]
            out = run_tool(d["tool"], d["args"])
            print(f"step {step + 1}: {d['tool']}({d['args']}) -> {out}")
            messages.append({"role": "tool", "content": out})
    return "Stopped: too many steps"

print("ANSWER:", ask_with_tools("ORD-1042 arrived late. What refund do I get?"))
print("ANSWER:", ask_with_tools("Where is order ORD-9999?"))'''),
    ("md", "## 6. NEW (v4): LangChain v1 `create_agent` and middleware\nThe same tools, now as LangChain tools. "
           "Middleware adds logging, an audit trail and a call limit without touching the prompt."),
    ("code", '''from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware, before_model, wrap_tool_call
from langchain_core.tools import tool

@tool
def get_order_status(order_id: str) -> str:
    """Look up an order by id, for example ORD-1042. Returns status, amount and days late."""
    return run_tool("get_order_status", json.dumps({"order_id": order_id}))

@tool
def calculate_refund(amount: float, days_late: int) -> str:
    """Calculate a late delivery refund from the order amount and days late."""
    return run_tool("calculate_refund", json.dumps({"amount": amount, "days_late": days_late}))

AUDIT = []

@before_model
def log_model_call(state, runtime):
    print(f"  [log] model call with {len(state['messages'])} message(s)")

@wrap_tool_call
def audit_tool(request, handler):
    result = handler(request)                       # runs the tool
    AUDIT.append({"tool": request.tool_call["name"], "args": request.tool_call["args"], "result": str(result.content)[:60]})
    print(f"  [audit] {request.tool_call['name']} {request.tool_call['args']}")
    return result

agent = create_agent(get_chat_model(), tools=[get_order_status, calculate_refund],
                     system_prompt="You are a support assistant. Use tools; answer in one sentence.",
                     middleware=[log_model_call, audit_tool, ModelCallLimitMiddleware(run_limit=6)])

for q in ["ORD-1042 arrived 3 days late. What refund do I get?", "Where is ORD-2077?"]:
    out = agent.invoke({"messages": [{"role": "user", "content": q}]})
    print("FINAL:", out["messages"][-1].content, "\\n")
print("audit entries:", len(AUDIT))'''),
    ("md", "**Reading older code:** `LLMChain`, `AgentExecutor` and `initialize_agent` are legacy in LangChain v1. "
           "Port them to LCEL chains (section 2) or `create_agent` (above)."),
    ("md", "## 7. NEW (v4): Tool design and tool token cost\nTool definitions are input tokens on every model call. "
           "Prices are **placeholders**."),
    ("code", '''lean = TOOLS
verbose = [{"type": "function", "function": {"name": f"tool_{i}",
            "description": "This tool can be used in many situations to help the user with a wide variety of "
                           "account, order, billing, network and general questions. " * 3,
            "parameters": {"type": "object", "properties": {f"field_{j}": {"type": "string", "description": "A value"}
                                                            for j in range(5)}}}} for i in range(12)]
PRICE_PER_1M = {"input": 1.00, "output": 4.00}     # PLACEHOLDER prices

def tool_tokens(tools):
    return count_tokens(json.dumps(tools))

for name, tools in [("lean (2 tools)", lean), ("verbose (12 tools)", verbose)]:
    t = tool_tokens(tools)
    per_1000 = t * 4 * 1000 * PRICE_PER_1M["input"] / 1_000_000      # 4 model calls per conversation
    print(f"{name:<20} {t:>5} tokens per call | {per_1000:.2f} per 1,000 conversations (placeholder units)")'''),
    ("md", "**TODO:** rewrite one verbose tool into a lean one (clear name, one-line description with an example). "
           "Measure the saving."),
    ("md", "## 8. NEW (v4): The OpenAI Agents SDK in the comparison\nThe same assistant with `Agent`, `function_tool` and "
           "`Runner`. Needs an API key; offline we show what would run."),
    ("code", '''from agents import Agent, Runner, function_tool

@function_tool
def order_status(order_id: str) -> str:
    """Look up an order by id, for example ORD-1042."""
    return get_order_status_fn(order_id)

@function_tool
def refund_amount(amount: float, days_late: int) -> str:
    """Calculate a late-delivery refund."""
    return calculate_refund_fn(amount, days_late)

support = Agent(name="Support", instructions="Answer order and refund questions with the tools. Be concise.",
                tools=[order_status, refund_amount], model=MODEL)
print("Agent:", support.name, "| tools:", [t.name for t in support.tools])
print("order_status schema:", order_status.params_json_schema)

if ONLINE:
    result = await Runner.run(support, "ORD-1042 arrived 3 days late. What refund do I get?")
    print("FINAL:", result.final_output)
else:
    print("Offline: Runner.run needs an API key. The direct loop (section 5) and create_agent (section 6) show the same steps.")'''),
    ("code", '''import pandas as pd
print(pd.DataFrame([
    {"option": "Direct OpenAI API", "you write": "loop, retries, tracing", "best for": "full control, few layers"},
    {"option": "LangChain v1 + LangGraph", "you write": "tools, middleware, graph", "best for": "workflows, approvals, many integrations"},
    {"option": "OpenAI Agents SDK", "you write": "agents, tools, handoffs", "best for": "fast agent builds with built-in tracing"},
]).to_string(index=False))'''),
    ("md", "## 9. A LangGraph workflow with branches and a retry loop"),
    ("code", '''from typing import TypedDict
from langgraph.graph import StateGraph, START, END

POLICY = {"refund": "Late deliveries get 5% of the order value per day late, up to 50%.",
          "return": "Items can be returned within 30 days in original packaging."}

class State(TypedDict, total=False):
    question: str
    intent: str
    evidence: str
    answer: str
    attempts: int
    path: list

def classify(s):
    q = s["question"].lower()
    intent = "order" if re.search(r"ord-\\d{4}", q) else "policy" if any(w in q for w in ["refund", "return", "policy", "late"]) else "other"
    return {"intent": intent, "attempts": s.get("attempts", 0), "path": s.get("path", []) + [f"classify:{intent}"]}

def lookup_order(s):
    oid = re.search(r"ORD-\\d{4}", s["question"], re.I).group(0).upper()
    return {"evidence": get_order_status_fn(oid), "path": s["path"] + ["lookup_order"]}

def retrieve_policy(s):
    q = s["question"].lower()
    return {"evidence": " ".join(v for k, v in POLICY.items() if k in q), "path": s["path"] + ["retrieve_policy"]}

def answer(s):
    if not s.get("evidence"):
        return {"answer": "", "path": s["path"] + ["answer:empty"]}
    a = llm(f"Context: {s['evidence']}\\nQuestion: {s['question']}", system="Answer only from the context in one sentence.")
    return {"answer": a, "path": s["path"] + ["answer"]}

def check(s):
    return {"attempts": s["attempts"] + 1, "path": s["path"] + ["check"]}

def rewrite(s):
    return {"question": s["question"] + " (refund policy)", "path": s["path"] + ["rewrite"]}

def human(s):
    return {"answer": "Handed to a human agent.", "path": s["path"] + ["human"]}

def route_intent(s):
    return {"order": "lookup_order", "policy": "retrieve_policy"}.get(s["intent"], "human")

def route_check(s):
    if s.get("answer") and "don't know" not in s["answer"].lower():
        return "done"
    return "retry" if s["attempts"] < 2 else "human"

g = StateGraph(State)
for name, fn in [("classify", classify), ("lookup_order", lookup_order), ("retrieve_policy", retrieve_policy),
                 ("answer", answer), ("check", check), ("rewrite", rewrite), ("human", human)]:
    g.add_node(name, fn)
g.add_edge(START, "classify")
g.add_conditional_edges("classify", route_intent, {"lookup_order": "lookup_order", "retrieve_policy": "retrieve_policy", "human": "human"})
g.add_edge("lookup_order", "answer")
g.add_edge("retrieve_policy", "answer")
g.add_edge("answer", "check")
g.add_conditional_edges("check", route_check, {"done": END, "retry": "rewrite", "human": "human"})
g.add_edge("rewrite", "retrieve_policy")
g.add_edge("human", END)
app = g.compile()

for q in ["What is the status of ORD-2077?", "How much do I get if delivery is late?", "Can you sing a song?"]:
    out = app.invoke({"question": q})
    print(f"Q: {q}\\n   path: {' -> '.join(out['path'])}\\n   answer: {out['answer']}\\n")'''),
    ("code", "print(app.get_graph().draw_mermaid())"),
    ("md", "## 10. NEW (v4): Durable execution, checkpoints and human-in-the-loop interrupts\n"
           "The refund graph pauses before paying. State is saved per `thread_id`, so the approval can arrive later."),
    ("code", '''from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command

class RefundState(TypedDict, total=False):
    order_id: str
    refund: float
    approved: bool
    result: str
    path: list

def lookup(s):
    o = json.loads(get_order_status_fn(s["order_id"]))
    refund = json.loads(calculate_refund_fn(o["amount"], o["days_late"]))["refund"]
    return {"refund": refund, "path": s.get("path", []) + ["lookup"]}

def approve(s):
    decision = interrupt({"action": "issue_refund", "order_id": s["order_id"], "amount": s["refund"]})
    return {"approved": str(decision).lower() == "yes", "path": s["path"] + [f"approve:{decision}"]}  # default no

def pay(s):
    msg = f"refund of {s['refund']} issued" if s["approved"] else "refund rejected"
    return {"result": msg, "path": s["path"] + ["pay"]}

rg = StateGraph(RefundState)
for n, f in [("lookup", lookup), ("approve", approve), ("pay", pay)]:
    rg.add_node(n, f)
rg.add_edge(START, "lookup"); rg.add_edge("lookup", "approve"); rg.add_edge("approve", "pay"); rg.add_edge("pay", END)
refund_app = rg.compile(checkpointer=InMemorySaver())

cfg_a = {"configurable": {"thread_id": "thread-A"}}
paused = refund_app.invoke({"order_id": "ORD-1042"}, cfg_a)
print("paused at:", refund_app.get_state(cfg_a).next, "| pending:", paused["__interrupt__"][0].value)
print("checkpoints so far:", len(list(refund_app.get_state_history(cfg_a))))

done = refund_app.invoke(Command(resume="no"), cfg_a)
print("thread A ->", done["result"], "|", " -> ".join(done["path"]))

cfg_b = {"configurable": {"thread_id": "thread-B"}}
refund_app.invoke({"order_id": "ORD-1042"}, cfg_b)
print("thread B ->", refund_app.invoke(Command(resume="yes"), cfg_b)["result"])'''),
    ("md", "### Resume after a crash\nIf a step fails, invoke again on the same thread. Finished steps are not rerun."),
    ("code", '''FLAKY = {"fail": True}

def flaky_pay(s):
    if FLAKY["fail"]:
        FLAKY["fail"] = False
        raise RuntimeError("payment service timeout")
    return {"result": "refund issued after retry", "path": s["path"] + ["pay"]}

fg = StateGraph(RefundState)
fg.add_node("lookup", lookup); fg.add_node("pay", flaky_pay)
fg.add_edge(START, "lookup"); fg.add_edge("lookup", "pay"); fg.add_edge("pay", END)
flaky_app = fg.compile(checkpointer=InMemorySaver())
cfg = {"configurable": {"thread_id": "thread-C"}}
try:
    flaky_app.invoke({"order_id": "ORD-1042"}, cfg)
except RuntimeError as e:
    print("first run failed:", e, "| saved next step:", flaky_app.get_state(cfg).next)
print("resume:", flaky_app.invoke(None, cfg)["result"])'''),
    ("md", "### The same approval with `HumanInTheLoopMiddleware`\n`create_agent` can pause before a risky tool with "
           "one line of middleware."),
    ("code", '''from langchain.agents.middleware import HumanInTheLoopMiddleware

@tool
def issue_refund(order_id: str, amount: float) -> str:
    """Issue a refund. Risky: a human must approve."""
    return json.dumps({"refunded": amount, "order_id": order_id})

hitl_agent = create_agent(get_chat_model(), tools=[get_order_status, calculate_refund, issue_refund],
                          system_prompt="You are a support assistant.",
                          middleware=[HumanInTheLoopMiddleware(interrupt_on={"issue_refund": True})],
                          checkpointer=InMemorySaver())
cfg = {"configurable": {"thread_id": "agent-1"}}
out = hitl_agent.invoke({"messages": [{"role": "user", "content": "ORD-1042 was 3 days late. Please issue my refund."}]}, cfg)
if "__interrupt__" in out:
    req = out["__interrupt__"][0].value["action_requests"][0]
    print("needs approval:", req["name"], req["args"])
    out = hitl_agent.invoke(Command(resume={"decisions": [{"type": "reject", "message": "Supervisor review needed."}]}), cfg)
print("FINAL:", out["messages"][-1].content)'''),
    ("md", "### TODO 1: Add a `search_policy(query)` tool to the agent and measure its schema tokens.\n"
           "### TODO 2 (SmartDesk step 22): make `issue_credit` a risky tool that pauses for approval, and log every decision."),
    ("code", "# TODO: write your code here"),
    ("md", "## 11. Check yourself\n1. Where does argument validation happen in each of the three options?\n"
           "2. How many tokens did the verbose tools add per call?\n3. What would be lost if the refund graph used no checkpointer?"),
])
