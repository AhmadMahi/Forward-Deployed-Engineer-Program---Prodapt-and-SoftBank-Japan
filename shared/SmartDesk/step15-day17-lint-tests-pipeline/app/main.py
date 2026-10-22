"""SmartDesk API (step 15 copy kept small): health and version endpoints for the pipeline demo."""
import os

from fastapi import FastAPI

app = FastAPI(title="SmartDesk API", version=os.getenv("APP_VERSION", "0.15.0"))


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": app.version, "commit": os.getenv("BUILD_SOURCEVERSION", "local")}
