from fastapi import FastAPI
from .schemas import GenerateRequest, GenerateResponse
import uuid

app = FastAPI(title="AI Cosplay Studio Engine")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    # TODO: подключить SDXL + ControlNet + IP-Adapter
    job_id = str(uuid.uuid4())
    return GenerateResponse(ok=True, job_id=job_id, eta_sec=2)
