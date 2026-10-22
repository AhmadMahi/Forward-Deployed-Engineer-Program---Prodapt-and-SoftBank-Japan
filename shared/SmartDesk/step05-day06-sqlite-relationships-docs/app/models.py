"""SQLAlchemy models: one customer has many tickets; one ticket has many comments."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base


class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)
    tickets: Mapped[list["Ticket"]] = relationship(back_populates="customer", cascade="all, delete-orphan")


class Ticket(Base):
    __tablename__ = "tickets"
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    category: Mapped[str] = mapped_column(String(20))
    priority: Mapped[str] = mapped_column(String(10), default="medium")
    status: Mapped[str] = mapped_column(String(15), default="open")
    body: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    customer: Mapped[Customer] = relationship(back_populates="tickets")
    comments: Mapped[list["Comment"]] = relationship(back_populates="ticket", cascade="all, delete-orphan")


class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    ticket_id: Mapped[int] = mapped_column(ForeignKey("tickets.id"))
    author: Mapped[str] = mapped_column(String(80))
    text: Mapped[str] = mapped_column(Text)
    ticket: Mapped[Ticket] = relationship(back_populates="comments")
