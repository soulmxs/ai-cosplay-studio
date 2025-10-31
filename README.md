# 🎭 AI Cosplay Studio

Local AI cosplay photo studio (Electron + React UI, FastAPI engine).

## Run (dev)
### Engine
cd apps/engine
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

### Desktop (UI)
cd apps/desktop
npm install
npm start

### Upload and Preview (mock)
POST /upload — загружает изображение в папку uploads  
GET /preview/{job_id} — возвращает тестовый URL превью

## Job flow (mock)

1) POST /generate → { job_id, status:"queued" }
2) Server runs background task (processing)
3) GET /jobs/{job_id} → { status: "processing" | "done" }
4) GET /results/{job_id} → { preview_data_url: "data:image/svg+xml;..." }
