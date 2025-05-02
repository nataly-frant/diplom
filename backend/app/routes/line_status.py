from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.line_status import get_or_update_line_status
from app.dependencies.db import get_db
from app.schemas.line_status import CacheLineStatus as CacheLineStatusSchema

router = APIRouter()


def fake_fetch_line_status():
    return {
        "line1": "active",
        "line2": "idle",
        "line3": "error",
        "line4": "active",
        "line5": "idle"
    }


@router.get("/", response_model=CacheLineStatusSchema)
def get_all_line_statuses(db: Session = Depends(get_db)):
    return get_or_update_line_status(db, fake_fetch_line_status)
