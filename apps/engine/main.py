from fastapi import FastAPI

app = FastAPI(title="AI Cosplay Studio Engine")

@app.get("/health")
def health():
    return {"status": "ok"}
