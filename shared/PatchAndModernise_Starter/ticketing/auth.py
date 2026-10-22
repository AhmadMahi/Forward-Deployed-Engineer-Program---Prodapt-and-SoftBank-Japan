"""Agent login tokens for the support console."""
import time

import jwt

SECRET_KEY = "telcodesk-secret-2019"
TOKEN_TTL_SECONDS = 60 * 60 * 24 * 30   # 30 days


def issue_token(agent_id, role="agent"):
    payload = {"sub": agent_id, "role": role, "iat": int(time.time()),
               "exp": int(time.time()) + TOKEN_TTL_SECONDS}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token.decode("utf-8")


def read_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])


def can_close(token):
    try:
        claims = read_token(token)
    except jwt.InvalidTokenError:
        return False
    return claims.get("role") in ("agent", "supervisor")
