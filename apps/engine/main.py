from fastapi import FastAPI, BackgroundTasks
from .schemas import GenerateRequest, GenerateResponse, JobStatusResponse, JobResultResponse
from .state import JobStatus, set_status, get_status, set_result, get_result
import uuid, asyncio
import urllib.parse

app = FastAPI(title="AI Cosplay Studio Engine")

@app.get("/")
def root():
    return {"status": "ok", "engine": "AI Cosplay Studio"}

@app.get("/health")
def health():
    return {"status": "ok"}

async def _process_job(job_id: str, req: GenerateRequest):
    try:
        set_status(job_id, JobStatus.PROCESSING)
        # имитация работы пайплайна
        await asyncio.sleep(1.5)
        # делаем простое SVG-превью с подсказкой prompt
        prompt_text = (req.prompt or "cosplay style")[:40]
        svg = f"""<svg xmlns='http://www.w3.org/2000/svg' width='512' height='320'>
  <rect width='100%' height='100%' fill='#111'/>
  <text x='20' y='60' fill='#00e5ff' font-size='28' font-family='Segoe UI, Arial'>AI Cosplay Studio</text>
  <text x='20' y='110' fill='#fff' font-size='16' font-family='Segoe UI, Arial'>job: {job_id[:8]}</text>
  <text x='20' y='150' fill='#ccc' font-size='16' font-family='Segoe UI, Arial'>prompt: {prompt_text}</text>
  <rect x='20' y='190' width='472' height='100' fill='#222' stroke='#444'/>
  <text x='30' y='245' fill='#aaa' font-size='14' font-family='Segoe UI, Arial'>[mock preview]</text>
</svg>"""
        data_url = "data:image/svg+xml;utf8," + urllib.parse.quote(svg)
        set_result(job_id, {"preview_data_url": data_url})
        set_status(job_id, JobStatus.DONE)
    except Exception:
        set_status(job_id, JobStatus.FAILED)

@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    set_status(job_id, JobStatus.QUEUED)
    background_tasks.add_task(_process_job, job_id, req)
    return GenerateResponse(ok=True, job_id=job_id, eta_sec=2, status=JobStatus.QUEUED.value)

@app.get("/jobs/{job_id}", response_model=JobStatusResponse)
def job_status(job_id: str):
    s = get_status(job_id)
    if not s:
        return JobStatusResponse(job_id=job_id, status="not_found")
    return JobStatusResponse(job_id=job_id, status=s.value)

@app.get("/results/{job_id}", response_model=JobResultResponse)
def job_result(job_id: str):
    r = get_result(job_id)
    if not r:
        # ещё не готово или нет такого job
        return JobResultResponse(job_id=job_id, preview_data_url="")
    return JobResultResponse(job_id=job_id, preview_data_url=r["preview_data_url"])

# ---------------------------------------------
# План интеграции image_utils (этап 2 — позже)
# ---------------------------------------------
# 1. При получении image_base64 в GenerateRequest:
#    - вызывать image_utils.save_base64_image()
#    - создавать уменьшенное превью через make_preview()
# 2. Сохранять путь и превью в set_result()
# 3. Возвращать preview_data_url в /results/{job_id}
#
# Пока код не активен — ожидает интеграции Pillow и тестирования локально.

