from pydantic import BaseModel
from typing import Optional, Literal

class GenerateRequest(BaseModel):
    image_base64: Optional[str] = None
    prompt: Optional[str] = None
    seed: Optional[int] = None
    mode: Optional[Literal["img2img", "txt2img"]] = "img2img"

class GenerateResponse(BaseModel):
    ok: bool
    job_id: str
    eta_sec: Optional[int] = None
    status: Optional[str] = "queued"

class JobStatusResponse(BaseModel):
    job_id: str
    status: str

class JobResultResponse(BaseModel):
    job_id: str
    preview_data_url: str
