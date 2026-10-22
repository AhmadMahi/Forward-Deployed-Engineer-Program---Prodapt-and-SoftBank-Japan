"""Database setup. SQLite file by default; tests use an in-memory database."""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import StaticPool

URL = os.getenv("DATABASE_URL", "sqlite:///./smartdesk.db")
engine = create_engine(URL, connect_args={"check_same_thread": False},
                       poolclass=StaticPool if URL.endswith(":memory:") else None)
SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
