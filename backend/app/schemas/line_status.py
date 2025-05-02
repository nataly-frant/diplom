from pydantic import BaseModel
from typing import Any
from datetime import datetime


class CacheLineStatus(BaseModel):
    id: int
    data_json: Any
    updated_at: datetime

    class Config:
        orm_mode = True
