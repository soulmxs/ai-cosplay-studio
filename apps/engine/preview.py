from fastapi import FastAPI
import random

app = FastAPI(title="AI Cosplay Preview Mock")

@app.get("/preview/{job_id}")
def preview(job_id: str):
    samples = [
        "https://placekitten.com/400/400",
        "https://placebear.com/400/400",
        "https://picsum.photos/400"
    ]
    return {"job_id": job_id, "preview_url": random.choice(samples)}
