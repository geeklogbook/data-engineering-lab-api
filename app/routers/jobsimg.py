import random
from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

IMAGES_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "jobs" / "images"
IMAGES = list(IMAGES_DIR.glob("*.jpeg"))

router = APIRouter(prefix="/jobsimg", tags=["jobsimg"])


@router.get("")
def get_jobsimg():
    path = random.choice(IMAGES)
    return FileResponse(path, media_type="image/jpeg")
