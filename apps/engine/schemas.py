from pydantic import BaseModel, Field
from typing import Literal, Optional

Mode = Literal["img2img", "txt2img"]

class GenerateRequest(BaseModel):
    mode: Mode = Field(default="img2img", description="img2img or txt2img")
    prompt: str = Field(default="cosplay style", description="text style prompt")
    strength: float = Field(default=0.5, ge=0.0, le=1.0)
    seed: Optional[int] = None

class GenerateResponse(BaseModel):
    ok: bool
    job_id: str
    eta_sec: int = 1
