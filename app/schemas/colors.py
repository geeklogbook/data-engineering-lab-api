from pydantic import BaseModel
from datetime import datetime

class Color(BaseModel):
    id: int
    timestamp: datetime
    color: str

class ColorResponse(BaseModel):
    columns: list[str]
    data: list[list[str]]