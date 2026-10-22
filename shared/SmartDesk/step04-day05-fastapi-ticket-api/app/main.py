"""SmartDesk step 04: FastAPI ticket API with Pydantic models (in-memory storage)."""
from datetime import datetime
from typing import Literal, Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

Category = Literal["billing", "network", "account", "other"]
Priority = Literal["low", "medium", "high"]
Status = Literal["open", "in_progress", "closed"]

app = FastAPI(title="SmartDesk API", version="0.4.0")


class TicketIn(BaseModel):
    customer: str = Field(min_length=1, max_length=80)
    category: Category
    priority: Priority = "medium"
    body: str = Field(min_length=1, max_length=2000)


class TicketUpdate(BaseModel):
    priority: Optional[Priority] = None
    status: Optional[Status] = None


class TicketOut(TicketIn):
    id: int
    status: Status
    created_at: datetime


DB: dict[int, TicketOut] = {}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tickets", response_model=TicketOut, status_code=201)
def create_ticket(t: TicketIn):
    new_id = max(DB, default=0) + 1
    DB[new_id] = TicketOut(id=new_id, status="open", created_at=datetime.now(), **t.model_dump())
    return DB[new_id]


@app.get("/tickets", response_model=list[TicketOut])
def list_tickets(status: Optional[Status] = None, priority: Optional[Priority] = None,
                 limit: int = Query(50, ge=1, le=200)):
    rows = [t for t in DB.values() if (status is None or t.status == status)
            and (priority is None or t.priority == priority)]
    return rows[:limit]


@app.get("/tickets/{ticket_id}", response_model=TicketOut)
def get_ticket(ticket_id: int):
    if ticket_id not in DB:
        raise HTTPException(404, "Ticket not found")
    return DB[ticket_id]


@app.patch("/tickets/{ticket_id}", response_model=TicketOut)
def update_ticket(ticket_id: int, change: TicketUpdate):
    t = get_ticket(ticket_id)
    DB[ticket_id] = t.model_copy(update=change.model_dump(exclude_none=True))
    return DB[ticket_id]


@app.delete("/tickets/{ticket_id}", status_code=204)
def delete_ticket(ticket_id: int):
    get_ticket(ticket_id)
    del DB[ticket_id]
