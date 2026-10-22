"""Use the MCP server from an agent. The agent discovers tools at run time, then calls one.

Online: tool schemas are passed to the OpenAI API as function tools and the model picks the call.
Offline: a simple keyword planner picks the call, so the demo runs without a key.
"""
import asyncio
import json
import os
import re

from mcp import Client

from mcp_server import server


def to_openai_tools(tools):
    return [{"type": "function", "function": {"name": t.name, "description": t.description,
                                              "parameters": t.input_schema}} for t in tools]


def offline_plan(question):
    m = re.search(r"ticket (\d+)", question.lower())
    if m and "close" in question.lower():
        return "update_status", {"ticket_id": int(m.group(1)), "status": "closed"}
    if m:
        return "get_ticket", {"ticket_id": int(m.group(1))}
    return "search_tickets", {"text": question.split()[-1].strip("?.").lower(), "status": "open"}


async def ask(question):
    async with Client(server) as client:                    # in-memory transport; use stdio or HTTP in production
        tools = (await client.list_tools()).tools
        if os.getenv("OFFLINE") != "1" and os.getenv("OPENAI_API_KEY"):
            from openai import OpenAI
            r = OpenAI().chat.completions.create(model=os.getenv("LLM_MODEL", "gpt-6.1-sol"),
                                                 messages=[{"role": "user", "content": question}],
                                                 tools=to_openai_tools(tools))
            call = r.choices[0].message.tool_calls[0].function
            name, args = call.name, json.loads(call.arguments)
        else:
            name, args = offline_plan(question)
        result = await client.call_tool(name, args)
        return {"tools": [t.name for t in tools], "call": name, "args": args,
                "result": result.structured_content, "error": result.is_error}


if __name__ == "__main__":
    print(asyncio.run(ask("Show me ticket 3")))
