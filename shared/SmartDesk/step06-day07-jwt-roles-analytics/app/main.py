"""SmartDesk step 06: JWT login with roles, and a Mongo analytics endpoint."""
import os
import re

import jwt
from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field

from .security import create_token, decode_token, hash_password, verify_password

app = FastAPI(title="SmartDesk API", version="0.6.0")
oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Demo users. Passwords come from the environment in real use; these are test-only values.
USERS = {"kenji": {"hash": hash_password(os.getenv("DEMO_AGENT_PASSWORD", "agent-demo-pass")), "role": "agent"},
         "rin": {"hash": hash_password(os.getenv("DEMO_LEAD_PASSWORD", "lead-demo-pass")), "role": "lead"}}


import mongomock  # noqa: E402

_mock = mongomock.MongoClient()["smartdesk"]["tickets"]     # offline default


def get_collection():
    uri = os.getenv("MONGO_URI")
    if uri:
        from pymongo import MongoClient
        return MongoClient(uri)["smartdesk"]["tickets"]
    return _mock


def require(scope):
    def checker(token: str = Depends(oauth2)):
        try:
            claims = decode_token(token)
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(401, "Invalid token")
        if scope not in claims.get("scopes", []):
            raise HTTPException(403, f"Missing scope {scope}")
        return claims
    return checker


@app.post("/auth/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = USERS.get(form.username)
    if not user or not verify_password(form.password, user["hash"]):
        raise HTTPException(401, "Wrong username or password")
    return {"access_token": create_token(form.username, user["role"]), "token_type": "bearer"}


class TicketIn(BaseModel):
    customer: str = Field(min_length=1, max_length=80)
    category: str = Field(pattern="^(billing|network|account|other)$")
    priority: str = Field("medium", pattern="^(low|medium|high)$")
    body: str = Field(min_length=1, max_length=2000)


@app.post("/tickets", status_code=201)
def create(t: TicketIn, claims=Depends(require("tickets:write"))):
    col = get_collection()
    doc = t.model_dump() | {"status": "open", "created_by": claims["sub"]}
    col.insert_one(doc)
    return {"ok": True}


@app.get("/tickets")
def search(customer: str = Query("", max_length=80), page: int = Query(1, ge=1), size: int = Query(10, le=50),
           claims=Depends(require("tickets:read"))):
    # NoSQL injection defence: the query value is a plain string, escaped for regex, never a dict from the client.
    query = {"customer": {"$regex": re.escape(customer), "$options": "i"}} if customer else {}
    cur = get_collection().find(query, {"_id": 0}).skip((page - 1) * size).limit(size)
    return list(cur)


@app.get("/analytics/by-category")
def by_category(claims=Depends(require("analytics:read"))):
    rows = get_collection().aggregate([
        {"$group": {"_id": {"category": "$category", "status": "$status"}, "n": {"$sum": 1}}},
        {"$sort": {"n": -1}}])
    return [{"category": r["_id"]["category"], "status": r["_id"]["status"], "count": r["n"]} for r in rows]
