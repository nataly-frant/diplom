from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.crud.finished_stock import get_or_update
from app.schemas.finished_stock import \
    CacheFinishedStock as CacheFinishedStockSchema

router = APIRouter()


def fake_fetch():
    return {
        "Lipton 25": "full",
        "Lipton 50": "full",
        "Lipton 100": "full",
        "BrookBond 50": "full",
        "BrookBond 100": "low",
        "BrookBond 250": "empty",
        "Beseda 20": "full",
        "Beseda 50": "empty"
    }


@router.get("/", response_model=CacheFinishedStockSchema)
def get_status(db: Session = Depends(get_db)):
    return get_or_update(db, fake_fetch)
