from fastapi import FastAPI

app = FastAPI(title="SmartDesk API", version="0.17.0")


@app.get("/health")
def health():
    return {"status": "ok"}
