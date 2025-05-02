from pydantic import BaseModel
from typing import Optional


class InfoCardBase(BaseModel):
    title: str
    content: Optional[str] = None
    parent_id: Optional[int] = None
    order: Optional[int] = 0
    type: Optional[str] = None


class InfoCardCreate(InfoCardBase):
    created_by_id: int


class InfoCard(InfoCardBase):
    id: int
    created_by_id: int

    class Config:
        orm_mode = True
