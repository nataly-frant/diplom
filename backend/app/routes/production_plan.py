from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.crud.production_plan import get_or_update
from app.schemas.production_plan import CacheProductionPlan as CacheProductionPlanSchema

router = APIRouter()


def fake_fetch():
    return {
        "Lipton 50": "scheduled",
        "Lipton 100": "in_progress",
        "BrookBond 50": "scheduled",
        "BrookBond 250": "in_progress",
        "Beseda 20": "completed",
        "Beseda 50": "delayed",
    }


@router.get("/", response_model=CacheProductionPlanSchema)
def get_status(db: Session = Depends(get_db)):
    return get_or_update(db, fake_fetch)
