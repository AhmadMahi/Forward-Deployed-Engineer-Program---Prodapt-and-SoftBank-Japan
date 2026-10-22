"""Settings for SmartDesk in Azure.

Container Apps injects secrets as environment variables (secret refs to Key Vault, read with managed identity).
Locally they come from a git-ignored .env file. Secret values are never printed or logged.
"""
import os
from dataclasses import dataclass, field

REQUIRED = ("DATABASE_URL", "JWT_SECRET")


class SecretStr(str):
    def __repr__(self):
        return "SecretStr('**********')"

    __str__ = __repr__


@dataclass(frozen=True)
class Settings:
    environment: str
    database_url: SecretStr = field(repr=False)
    jwt_secret: SecretStr = field(repr=False)
    llm_model: str = "gpt-6.1-sol"          # confirm against the approved model list


def load_settings(env=os.environ):
    missing = [k for k in REQUIRED if not env.get(k)]
    if missing:
        raise RuntimeError(f"Missing required settings: {', '.join(missing)}")
    return Settings(environment=env.get("APP_ENV", "dev"), database_url=SecretStr(env["DATABASE_URL"]),
                    jwt_secret=SecretStr(env["JWT_SECRET"]), llm_model=env.get("LLM_MODEL", "gpt-6.1-sol"))
