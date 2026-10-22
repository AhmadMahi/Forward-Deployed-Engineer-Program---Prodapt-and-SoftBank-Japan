"""Run analytics code from the data agent in a sandbox.

Here: a separate Python process with isolated mode, an empty environment (no API keys), a temp folder,
a CPU time limit and a memory limit. In class: run it in a container with no network, for example
docker run --rm --network none --memory 256m --cpus 0.5 --read-only python:3.12-slim python -c "..."
"""
import subprocess
import sys
import tempfile


def _limits():
    import resource
    resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))


def run_code(code, timeout=5):
    with tempfile.TemporaryDirectory() as tmp:
        try:
            p = subprocess.run([sys.executable, "-I", "-c", code], cwd=tmp, env={}, capture_output=True, text=True,
                               timeout=timeout, preexec_fn=_limits)
            return {"ok": p.returncode == 0, "stdout": p.stdout[-2000:], "stderr": p.stderr[-2000:]}
        except subprocess.TimeoutExpired:
            return {"ok": False, "stdout": "", "stderr": "timeout"}
