from enum import Enum

class JobStatus(str, Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    DONE = "done"
    FAILED = "failed"

# Простое in-memory хранилище
job_status: dict[str, JobStatus] = {}
job_result: dict[str, dict] = {}

def set_status(job_id: str, status: JobStatus):
    job_status[job_id] = status

def get_status(job_id: str) -> JobStatus | None:
    return job_status.get(job_id)

def set_result(job_id: str, result: dict):
    job_result[job_id] = result

def get_result(job_id: str) -> dict | None:
    return job_result.get(job_id)
