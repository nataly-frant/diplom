from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.crud.raw_stock import get_or_update
from app.schemas.raw_stock import CacheRawStock

router = APIRouter()


def fake_fetch():
    return {
        "Tea": "available",
        "Filter paper": "low",
        "Mailer": "empty"
    }


@router.get("/", response_model=CacheRawStock)
def get_status(db: Session = Depends(get_db)):
    return get_or_update(db, fake_fetch)
