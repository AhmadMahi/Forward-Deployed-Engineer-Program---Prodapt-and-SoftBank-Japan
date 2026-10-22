"""Static checks on the Dockerfiles and pipeline, so hardening rules cannot silently regress."""
from pathlib import Path

HERE = Path(__file__).parent


def test_api_image_is_hardened():
    d = (HERE / "Dockerfile").read_text()
    assert "-slim" in d and ":latest" not in d
    users = [line.split()[1] for line in d.splitlines() if line.startswith("USER ")]
    assert users and users[-1] != "root"
    assert "HEALTHCHECK" in d
    assert "OPENAI_API_KEY" not in d and "ENV SECRET" not in d


def test_dockerignore_excludes_secrets():
    assert ".env" in (HERE / ".dockerignore").read_text().split()


def test_pipeline_has_all_gates():
    y = (HERE / "azure-pipelines.yml").read_text()
    for gate in ("bandit", "pip-audit", "gitleaks", "trivy", "pytest"):
        assert gate in y
