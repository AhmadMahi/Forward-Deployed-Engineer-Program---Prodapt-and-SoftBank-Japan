"""Password hashing and short-lived JWTs with roles and scopes.

The signing secret comes from the environment. Never commit it.
"""
import hashlib
import hmac
import os
import secrets
from datetime import datetime, timedelta, timezone

import jwt

SECRET = os.getenv("JWT_SECRET") or secrets.token_urlsafe(32)   # a random dev secret if none is set
ALGORITHM = "HS256"
TOKEN_MINUTES = 15                                               # short-lived on purpose
ROLE_SCOPES = {"agent": ["tickets:read", "tickets:write"],
               "lead": ["tickets:read", "tickets:write", "analytics:read"]}


def hash_password(password, salt=None):
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 200_000).hex()
    return f"{salt}${digest}"


def verify_password(password, stored):
    salt, _ = stored.split("$")
    return hmac.compare_digest(hash_password(password, salt), stored)


def create_token(username, role, minutes=TOKEN_MINUTES):
    now = datetime.now(timezone.utc)
    payload = {"sub": username, "role": role, "scopes": ROLE_SCOPES[role], "iat": now,
               "exp": now + timedelta(minutes=minutes)}
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


def decode_token(token):
    return jwt.decode(token, SECRET, algorithms=[ALGORITHM])          # checks signature and expiry
