from sqlalchemy.orm import Session
from app.models.info_card import InfoCard
from app.schemas.info_card import InfoCardCreate


def create_info_card(db: Session, card: InfoCardCreate):
    db_card = InfoCard(**card.dict())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def get_all_cards(db: Session):
    # return db.query(InfoCard).all()
    return [
        {
            "id": 1,
            "created_by_id": 1,
            "title": "Организационная структура",
            "content": "Описание организационной структуры предприятия ООО «Юнилевер Русь».",
            "parent_id": None,
            "order": 1,
            "type": "Раздел",
        },
        {
            "id": 2,
            "created_by_id": 1,
            "title": "Основные направления деятельности",
            "content": "Информация о ключевых направлениях работы предприятия, включая производство и логистику.",
            "parent_id": 1,
            "order": 2,
            "type": "Подраздел",
        },
        {
            "id": 3,
            "created_by_id": 1,
            "title": "Информационная система",
            "content": "Анализ текущего состояния информационной системы и её возможностей.",
            "parent_id": 1,
            "order": 3,
            "type": "Подраздел",
        }
    ]
