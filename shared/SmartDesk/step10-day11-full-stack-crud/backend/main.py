"""SmartDesk step 10 back end: CRUD plus close, with CORS for the Vite dev server."""
from datetime import datetime
from typing import Literal, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="SmartDesk API", version="0.10.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_methods=["*"],
                   allow_headers=["*"])
DB: dict[int, dict] = {}


class TicketIn(BaseModel):
    customer: str = Field(min_length=1, max_length=80)
    category: Literal["billing", "network", "account", "other"]
    priority: Literal["low", "medium", "high"] = "medium"
    body: str = Field(min_length=1, max_length=2000)


class TicketPatch(BaseModel):
    priority: Optional[Literal["low", "medium", "high"]] = None
    body: Optional[str] = Field(None, min_length=1)


@app.get("/api/tickets")
def list_tickets():
    return sorted(DB.values(), key=lambda t: t["id"])


@app.post("/api/tickets", status_code=201)
def create(t: TicketIn):
    i = max(DB, default=0) + 1
    DB[i] = {"id": i, "status": "open", "created_at": datetime.now().isoformat(), **t.model_dump()}
    return DB[i]


@app.patch("/api/tickets/{i}")
def update(i: int, p: TicketPatch):
    if i not in DB:
        raise HTTPException(404, "Ticket not found")
    if DB[i]["status"] == "closed":
        raise HTTPException(409, "Closed tickets cannot be edited")
    DB[i].update(p.model_dump(exclude_none=True))
    return DB[i]


@app.post("/api/tickets/{i}/close")
def close(i: int):
    if i not in DB:
        raise HTTPException(404, "Ticket not found")
    DB[i]["status"] = "closed"
    return DB[i]
