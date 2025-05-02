import os
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import (
    CacheLineStatus,
    CacheRawStock,
    CacheFinishedStock,
    CacheProductionPlan,
    InfoCard,
    User,
    Role
)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/diplom_nat"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def populate():
    db = SessionLocal()

    try:
        # Очистим таблицы
        db.query(CacheLineStatus).delete()
        db.query(CacheRawStock).delete()
        db.query(CacheFinishedStock).delete()
        db.query(CacheProductionPlan).delete()
        db.query(InfoCard).delete()
        db.query(User).delete()
        db.query(Role).delete()

        # Добавляем роль
        role_admin = Role(name="admin")
        db.add(role_admin)
        db.commit()

        # Добавляем пользователя
        user = User(
            username="admin",
            email="admin@example.com",
            hashed_password="hashed_password",  # для теста
            role_id=role_admin.id
        )
        db.add(user)
        db.commit()

        # Добавляем несколько статусов линий
        line_status = CacheLineStatus(
            data_json={
                "line1": "active",
                "line2": "idle",
                "line3": "error",
                "line4": "active",
                "line5": "idle"
            },
            updated_at=datetime.now()
        )
        db.add(line_status)

        # Добавляем склад сырья
        raw_stock = CacheRawStock(
            data_json={
                "Tea": "available",
                "Filter paper": "available",
                "Mailer": "available"
            },
            updated_at=datetime.now()
        )
        db.add(raw_stock)

        # Добавляем склад готовой продукции
        finished_stock = CacheFinishedStock(
            data_json={
                "Lipton 25": "full",
                "Lipton 50": "full",
                "Lipton 100": "full",
                "BrookBond 50": "full",
                "BrookBond 100": "low",
                "BrookBond 250": "empty",
                "Beseda 20": "full",
                "Beseda 50": "empty"
            },
            updated_at=datetime.now()
        )
        db.add(finished_stock)

        # Добавляем производственные планы
        production_plan = CacheProductionPlan(
            data_json={
                "Lipton 50": "scheduled",
                "Lipton 100": "in_progress",
                "BrookBond 50": "scheduled",
                "BrookBond 250": "in_progress",
                "Beseda 20": "completed",
                "Beseda 50": "delayed",
            },
            updated_at=datetime.now()
        )
        db.add(production_plan)

        # Добавляем карточки справочника
        for i in range(1, 6):
            info_card = InfoCard(
                title=f"Процесс №{i}",
                content=f"Описание технологического процесса {i}",
                order=i,
                type="text",
                created_by_id=user.id
            )
            db.add(info_card)

        db.commit()

    finally:
        db.close()


if __name__ == "__main__":
    populate()
