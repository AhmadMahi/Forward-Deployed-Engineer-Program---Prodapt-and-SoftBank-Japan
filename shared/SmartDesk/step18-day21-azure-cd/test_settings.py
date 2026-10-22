import pytest

from settings import load_settings


def test_missing_settings_fail_fast():
    with pytest.raises(RuntimeError, match="JWT_SECRET"):
        load_settings({"DATABASE_URL": "sqlite://"})


def test_secrets_never_printed():
    s = load_settings({"DATABASE_URL": "postgresql://user:pw@host/db", "JWT_SECRET": "abc123"})
    assert "abc123" not in repr(s) and "pw@host" not in repr(s)
    assert "abc123" not in f"{s.jwt_secret}"


def test_pipeline_uses_key_vault_and_approvals():
    y = open("azure-pipelines-cd.yml").read()
    assert "group: smartdesk-kv" in y and "environment: smartdesk-prod" in y
    assert "password" not in y.lower().replace("no passwords", "")
