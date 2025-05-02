from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.info_card import InfoCardCreate, InfoCard
from app.crud.info_card import create_info_card, get_all_cards
from app.dependencies.db import get_db

router = APIRouter()


@router.get("/production-lines", response_model=List[InfoCard])
def get_production_lines(db: Session = Depends(get_db)):
    return get_all_cards(db)


@router.get("/technological-cards", response_model=List[InfoCard])
def get_technological_cards(db: Session = Depends(get_db)):
    return get_all_cards(db)

@router.get("/finished-products", response_model=List[InfoCard])
def get_finished_products(db: Session = Depends(get_db)):
    return get_all_cards(db)

@router.get("/raw-materials", response_model=List[InfoCard])
def get_raw_materials(db: Session = Depends(get_db)):
    return get_all_cards(db)

@router.get("/maintenance", response_model=List[InfoCard])
def get_maintenance(db: Session = Depends(get_db)):
    return get_all_cards(db)

@router.get("/onboarding", response_model=List[InfoCard])
def get_onboarding(db: Session = Depends(get_db)):
    return get_all_cards(db)

@router.get("/standards", response_model=List[InfoCard])
def get_standards(db: Session = Depends(get_db)):
    return get_all_cards(db)
