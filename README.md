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

