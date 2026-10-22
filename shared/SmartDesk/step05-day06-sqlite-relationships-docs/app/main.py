"""SmartDesk step 05: SQLite persistence with relationships. Swagger docs at /docs."""
from typing import Literal

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .db import Base, engine, get_db
from .models import Comment, Customer, Ticket

app = FastAPI(title="SmartDesk API", version="0.5.0",
              description="Telecom support tickets. Customers have many tickets; tickets have comments.",
              openapi_tags=[{"name": "tickets", "description": "Create and manage tickets"},
                            {"name": "reports", "description": "Simple joins and counts"}])
Base.metadata.create_all(engine)


class TicketIn(BaseModel):
    customer: str = Field(min_length=1, max_length=80, examples=["Aiko Tanaka"])
    category: Literal["billing", "network", "account", "other"]
    priority: Literal["low", "medium", "high"] = "medium"
    body: str = Field(min_length=1, examples=["No signal at home since Monday."])


class CommentIn(BaseModel):
    author: str = Field(min_length=1)
    text: str = Field(min_length=1)


class TicketOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    category: str
    priority: str
    status: str
    body: str


@app.post("/tickets", response_model=TicketOut, status_code=201, tags=["tickets"])
def create_ticket(t: TicketIn, db: Session = Depends(get_db)):
    customer = db.scalar(select(Customer).where(Customer.name == t.customer)) or Customer(name=t.customer)
    ticket = Ticket(customer=customer, category=t.category, priority=t.priority, body=t.body)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


@app.post("/tickets/{ticket_id}/comments", status_code=201, tags=["tickets"])
def add_comment(ticket_id: int, c: CommentIn, db: Session = Depends(get_db)):
    if not db.get(Ticket, ticket_id):
        raise HTTPException(404, "Ticket not found")
    db.add(Comment(ticket_id=ticket_id, author=c.author, text=c.text))
    db.commit()
    return {"ok": True}


@app.get("/customers/{name}/tickets", response_model=list[TicketOut], tags=["reports"])
def customer_tickets(name: str, db: Session = Depends(get_db)):
    return db.scalars(select(Ticket).join(Customer).where(Customer.name == name)).all()


@app.get("/reports/tickets-per-customer", tags=["reports"])
def tickets_per_customer(db: Session = Depends(get_db)):
    rows = db.execute(select(Customer.name, func.count(Ticket.id)).join(Ticket).group_by(Customer.name)).all()
    return {name: n for name, n in rows}


def transfer_tickets(db: Session, from_name: str, to_name: str):
    """Move all tickets to another customer in one transaction. Rolls back on any error."""
    try:
        src = db.scalar(select(Customer).where(Customer.name == from_name))
        dst = db.scalar(select(Customer).where(Customer.name == to_name))
        if src is None or dst is None:
            raise ValueError("Unknown customer")
        for t in list(src.tickets):
            t.customer = dst
        db.commit()
    except (ValueError, IntegrityError):
        db.rollback()
        raise
