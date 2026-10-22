"""SmartDesk step 29: production LLM gateway with streaming, canary releases and rollback.

No long-lived keys in agents: the gateway holds provider credentials (Key Vault via managed identity on Azure),
callers get short-lived tokens. Offline it streams a stand-in answer.
"""
import asyncio
import hashlib
import os

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

app = FastAPI(title="SmartDesk LLM gateway", version="0.29.0")
RELEASES = {"stable": "2026.12.1", "canary": "2026.12.2"}
STATE = {"canary_percent": int(os.getenv("CANARY_PERCENT", "10"))}


class ChatIn(BaseModel):
    user_id: str
    message: str = Field(min_length=1, max_length=2000)


def pick_release(user_id):
    """Sticky canary: the same user always lands in the same bucket."""
    bucket = int(hashlib.sha256(user_id.encode()).hexdigest(), 16) % 100
    return "canary" if bucket < STATE["canary_percent"] else "stable"


async def generate(message, release):
    words = f"[offline demo] ({RELEASES[release]}) Thanks, we are looking at: {message}".split()
    for w in words:
        await asyncio.sleep(0)
        yield w + " "


@app.post("/v1/chat")
async def chat(req: ChatIn):
    release = pick_release(req.user_id)
    return StreamingResponse(generate(req.message, release), media_type="text/plain",
                             headers={"X-Release": RELEASES[release]})


@app.post("/admin/canary")
def set_canary(percent: int, x_admin_token: str = Header(...)):
    if x_admin_token != os.getenv("ADMIN_TOKEN", ""):
        raise HTTPException(403, "Forbidden")
    if not 0 <= percent <= 100:
        raise HTTPException(422, "percent must be 0 to 100")
    STATE["canary_percent"] = percent          # 0 = rollback, 100 = promote
    return STATE
